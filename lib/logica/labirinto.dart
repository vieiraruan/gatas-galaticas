import 'dart:collection';
import 'dart:math';

import '../modelos/conteudo.dart';

/// Labirinto Orbital: o minijogo opcional entre uma missão e outra.
/// Tudo aqui é puro (sem Flutter) para facilitar os testes.

enum Dir {
  cima(0, -1, 1),
  baixo(0, 1, 2),
  esquerda(-1, 0, 4),
  direita(1, 0, 8);

  final int dx;
  final int dy;
  final int bit;
  const Dir(this.dx, this.dy, this.bit);

  Dir get oposta => switch (this) {
        Dir.cima => Dir.baixo,
        Dir.baixo => Dir.cima,
        Dir.esquerda => Dir.direita,
        Dir.direita => Dir.esquerda,
      };
}

class Pos {
  final int x;
  final int y;
  const Pos(this.x, this.y);
  Pos mover(Dir d) => Pos(x + d.dx, y + d.dy);
  @override
  bool operator ==(Object other) => other is Pos && other.x == x && other.y == y;
  @override
  int get hashCode => x * 1000 + y;
  @override
  String toString() => '($x,$y)';
}

/// Quanto o labirinto cresce em cada ano (veja o documento de ideias).
class ConfigLabirinto {
  final int lado;
  final int portas;
  final int pocas;
  final int novelos;
  final int aspiradores;
  final int peixes;

  /// Segundos para ganhar o bônus de tempo (0 = sem relógio).
  final int segundosBonus;

  const ConfigLabirinto({
    required this.lado,
    required this.portas,
    required this.pocas,
    required this.novelos,
    required this.aspiradores,
    required this.peixes,
    required this.segundosBonus,
  });

  /// `calmo`: primeiro labirinto do dia, sem nada perseguindo a gata.
  factory ConfigLabirinto.doAno(int ano, {bool calmo = false}) {
    final a = ano.clamp(1, 5);
    final lado = 4 + a; // 5×5 no 1º ano … 9×9 no 5º.
    return ConfigLabirinto(
      lado: lado,
      portas: const [1, 2, 2, 3, 3][a - 1],
      pocas: const [2, 3, 3, 4, 4][a - 1],
      novelos: const [0, 2, 2, 3, 3][a - 1],
      aspiradores: calmo ? 0 : const [0, 0, 1, 2, 3][a - 1],
      peixes: lado,
      segundosBonus: a >= 3 ? lado * 12 : 0,
    );
  }
}

enum Item { porta, poca, novelo, peixe, respiro }

class Aspirador {
  /// Corredor reto que ele patrulha, ida e volta.
  final List<Pos> trilho;
  int passo = 0;
  int sentido = 1;
  Aspirador(this.trilho);

  Pos get pos => trilho[passo];

  void andar() {
    if (trilho.length < 2) return;
    if (passo + sentido < 0 || passo + sentido >= trilho.length) sentido = -sentido;
    passo += sentido;
  }
}

class Labirinto {
  final int lado;

  /// Passagens abertas de cada casa, como soma dos `Dir.bit`.
  final List<List<int>> abertas;
  final Pos inicio;
  final Pos saida;
  final Map<Pos, Item> itens;
  final List<Aspirador> aspiradores;

  Labirinto._(this.lado, this.abertas, this.inicio, this.saida, this.itens,
      this.aspiradores);

  bool dentro(Pos p) => p.x >= 0 && p.y >= 0 && p.x < lado && p.y < lado;

  bool aberto(Pos p, Dir d) => (abertas[p.y][p.x] & d.bit) != 0;

  void _abrir(Pos p, Dir d) {
    final q = p.mover(d);
    abertas[p.y][p.x] |= d.bit;
    abertas[q.y][q.x] |= d.oposta.bit;
  }

  /// Menor caminho entre duas casas, ignorando os itens.
  List<Pos> caminho(Pos de, Pos para, {Set<Pos> evitar = const {}}) {
    final veio = <Pos, Pos>{};
    final fila = Queue<Pos>()..add(de);
    final vistos = {de};
    while (fila.isNotEmpty) {
      final p = fila.removeFirst();
      if (p == para) break;
      for (final d in Dir.values) {
        final q = p.mover(d);
        if (!aberto(p, d) || vistos.contains(q) || evitar.contains(q)) continue;
        vistos.add(q);
        veio[q] = p;
        fila.add(q);
      }
    }
    if (!vistos.contains(para)) return const [];
    final out = [para];
    while (out.last != de) {
      out.add(veio[out.last]!);
    }
    return out.reversed.toList();
  }

  List<Pos> get solucao => caminho(inicio, saida);

  factory Labirinto.gerar(ConfigLabirinto c, Random rnd) {
    final n = c.lado;
    final lab = Labirinto._(
      n,
      List.generate(n, (_) => List.filled(n, 0)),
      const Pos(0, 0),
      Pos(n - 1, n - 1),
      {},
      [],
    );

    // 1. Labirinto perfeito (busca em profundidade com pilha).
    final visitado = {lab.inicio};
    final pilha = [lab.inicio];
    while (pilha.isNotEmpty) {
      final p = pilha.last;
      final viz = [
        for (final d in Dir.values)
          if (lab.dentro(p.mover(d)) && !visitado.contains(p.mover(d))) d
      ];
      if (viz.isEmpty) {
        pilha.removeLast();
        continue;
      }
      final d = viz[rnd.nextInt(viz.length)];
      lab._abrir(p, d);
      visitado.add(p.mover(d));
      pilha.add(p.mover(d));
    }

    // 2. Derruba algumas paredes: mais caminhos, menos becos (mais calmo).
    final extras = (n * n * 0.12).round();
    for (var k = 0, tentativas = 0; k < extras && tentativas < 500; tentativas++) {
      final p = Pos(rnd.nextInt(n), rnd.nextInt(n));
      final d = Dir.values[rnd.nextInt(4)];
      if (!lab.dentro(p.mover(d)) || lab.aberto(p, d)) continue;
      lab._abrir(p, d);
      k++;
    }

    final rota = lab.solucao;
    final naRota = rota.toSet();
    final livres = [
      for (var y = 0; y < n; y++)
        for (var x = 0; x < n; x++)
          if (!naRota.contains(Pos(x, y))) Pos(x, y)
    ]..shuffle(rnd);

    // 3. Portas-código espalhadas pela rota (nunca na entrada ou na saída).
    for (var i = 1; i <= c.portas; i++) {
      final idx = (rota.length * i / (c.portas + 1)).round().clamp(1, rota.length - 2);
      lab.itens[rota[idx]] = Item.porta;
    }

    // 4. Janela de respiro na metade da rota, se a casa estiver livre.
    final meio = rota[(rota.length / 2).floor().clamp(1, rota.length - 2)];
    if (!lab.itens.containsKey(meio)) {
      lab.itens[meio] = Item.respiro;
    } else if (rota.length > 4) {
      final alt = rota[(rota.length / 2).floor() + 1];
      if (!lab.itens.containsKey(alt) && alt != lab.saida) lab.itens[alt] = Item.respiro;
    }

    // 5. Poças fora da rota, sem isolar nenhum pedaço do labirinto.
    var pocas = 0;
    for (final p in List.of(livres)) {
      if (pocas >= c.pocas) break;
      final bloqueadas = {
        for (final e in lab.itens.entries)
          if (e.value == Item.poca) e.key,
        p
      };
      final alcancaveis = lab._alcancaveis(bloqueadas);
      if (alcancaveis == n * n - bloqueadas.length) {
        lab.itens[p] = Item.poca;
        livres.remove(p);
        pocas++;
      }
    }

    // 6. Novelos: metade fora da rota, metade nela (só atrasam um pouco).
    final rotaLivre = [
      for (final p in rota.sublist(1, rota.length - 1))
        if (!lab.itens.containsKey(p)) p
    ]..shuffle(rnd);
    for (var i = 0; i < c.novelos; i++) {
      final fonte = i.isEven && rotaLivre.isNotEmpty ? rotaLivre : livres;
      if (fonte.isEmpty) break;
      lab.itens[fonte.removeLast()] = Item.novelo;
    }

    // 7. Peixinhos nas casas livres que sobraram.
    for (var i = 0; i < c.peixes && livres.isNotEmpty; i++) {
      lab.itens[livres.removeLast()] = Item.peixe;
    }

    // 8. Aspiradores-sentinela em corredores retos, longe da entrada.
    final usados = <Pos>{};
    for (final t in lab._corredores(rnd)) {
      if (lab.aspiradores.length >= c.aspiradores) break;
      if (t.any((p) =>
          usados.contains(p) ||
          (p.x + p.y) < 3 ||
          p == lab.saida ||
          lab.itens[p] == Item.porta ||
          lab.itens[p] == Item.poca)) {
        continue;
      }
      usados.addAll(t);
      lab.aspiradores.add(Aspirador(t));
    }
    return lab;
  }

  int _alcancaveis(Set<Pos> bloqueadas) {
    final vistos = {inicio};
    final fila = Queue<Pos>()..add(inicio);
    while (fila.isNotEmpty) {
      final p = fila.removeFirst();
      for (final d in Dir.values) {
        final q = p.mover(d);
        if (aberto(p, d) && !bloqueadas.contains(q) && vistos.add(q)) fila.add(q);
      }
    }
    return vistos.length;
  }

  /// Trechos retos de 3 ou 4 casas, embaralhados.
  List<List<Pos>> _corredores(Random rnd) {
    final out = <List<Pos>>[];
    for (var y = 0; y < lado; y++) {
      for (var x = 0; x < lado; x++) {
        for (final d in [Dir.direita, Dir.baixo]) {
          final t = [Pos(x, y)];
          while (t.length < 4 && aberto(t.last, d)) {
            t.add(t.last.mover(d));
          }
          if (t.length >= 3) out.add(t);
        }
      }
    }
    return out..shuffle(rnd);
  }
}

// ---------------------------------------------------------------------------
// Poderes das gatas

enum Poder {
  olharSoberano('👁️', 'Olhar Soberano', 'Mostra o caminho até a saída por 3 segundos.'),
  invasaoRapida('💻', 'Invasão Rápida', 'A próxima porta abre sem precisar responder.'),
  charmeFatal('💖', 'Charme Fatal', 'Os aspiradores param para fazer carinho por 4 segundos.'),
  passagemSecreta('🕳️', 'Passagem Secreta', 'O próximo passo atravessa uma parede.'),
  miadoSonico('📣', 'Miado Sônico', 'Tira do caminho poças, novelos e aspiradores perto da gata.');

  final String emoji;
  final String nome;
  final String descricao;
  const Poder(this.emoji, this.nome, this.descricao);
}

Poder poderDaGata(String gatoId) => switch (gatoId) {
      'jojo' => Poder.olharSoberano,
      'nala' => Poder.invasaoRapida,
      'shanti' => Poder.charmeFatal,
      'luna' => Poder.passagemSecreta,
      'baguera' => Poder.miadoSonico,
      _ => Poder.olharSoberano,
    };

/// Usos do poder: 1, e mais 1 se a missão anterior teve 3 estrelas.
int usosDoPoder(int estrelasMissao) => estrelasMissao >= 3 ? 2 : 1;

// ---------------------------------------------------------------------------
// Desafios de lembrança das portas

/// Pergunta de porta: sempre de toque único, para não quebrar o ritmo.
class DesafioPorta {
  final String pergunta;
  final List<String> opcoes;
  final int correta;
  final String? explicacao;
  final List<Visual> visuais;
  const DesafioPorta(this.pergunta, this.opcoes, this.correta, this.explicacao,
      [this.visuais = const []]);
}

DesafioPorta? _paraDesafio(Exercicio e, Random rnd) {
  switch (e) {
    case Escolha():
      final ordem = List.generate(e.opcoes.length, (i) => i);
      if (e.embaralhar) ordem.shuffle(rnd);
      final ops = [for (final i in ordem.take(3)) e.opcoes[i]];
      if (!ordem.take(3).contains(e.correta)) ops[rnd.nextInt(ops.length)] = e.respostaCerta;
      return DesafioPorta(e.pergunta, ops, ops.indexOf(e.respostaCerta), e.explicacao, e.visuais);
    case VerdadeiroFalso():
      return DesafioPorta(e.pergunta, const ['Verdadeiro', 'Falso'], e.resposta ? 0 : 1,
          e.explicacao);
    case Completar():
      final ops = (List.of(e.opcoes.take(3))..shuffle(rnd));
      return DesafioPorta(e.pergunta, ops, ops.indexOf(e.opcoes.first), e.explicacao);
    default:
      return null;
  }
}

/// Perguntas para as portas: primeiro de missões feitas ANTES (revisão
/// espaçada), depois da missão que acabou de terminar.
List<DesafioPorta> desafiosDeLembranca({
  required List<Missao> anteriores,
  required List<Missao> recentes,
  required Random rnd,
  int quantidade = 8,
}) {
  List<DesafioPorta> de(List<Missao> ms) => [
        for (final m in ms)
          for (final e in m.exercicios) ?_paraDesafio(e, rnd)
      ]..shuffle(rnd);
  final antes = de(anteriores);
  final agora = de(recentes);
  final out = <DesafioPorta>[];
  // Duas de cada três perguntas relembram missões anteriores.
  while (out.length < quantidade && (antes.isNotEmpty || agora.isNotEmpty)) {
    final usarAntes = antes.isNotEmpty && (agora.isEmpty || out.length % 3 != 2);
    out.add((usarAntes ? antes : agora).removeLast());
  }
  return out;
}

/// Recompensa do labirinto: menor que a de uma missão, para o estudo
/// continuar sendo o centro.
({int xp, int peixinhos}) recompensaLabirinto({
  required int peixesPegos,
  required bool bonusTempo,
  required double multiplicador,
}) =>
    (
      xp: (5 * multiplicador).round(),
      peixinhos: ((peixesPegos + 5 + (bonusTempo ? 3 : 0)) * multiplicador).round(),
    );
