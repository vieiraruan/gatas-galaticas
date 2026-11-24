import 'dart:math';

import 'labirinto.dart' show Dir, Pos, DesafioPorta;

/// Minijogos das pausas entre missões. Versões próprias de gêneros
/// clássicos (tiro com rolagem lateral, cobrinha e voo de toque), com
/// nomes, regras e visual nossos. Tudo puro, sem Flutter, para testar.
///
/// Coordenadas normalizadas: a tela vai de 0 a 1 nos dois eixos.

enum Minijogo {
  labirinto('🌌', 'Labirinto Orbital', 'Leve a gata até a cápsula de fuga.'),
  patrulha('✨', 'Patrulha da Luz', 'Reacenda os drones do Apagão com raios de luz.'),
  cauda('☄️', 'Cauda de Cometa', 'Pegue a resposta certa e faça a cauda crescer.'),
  travessia('🪐', 'Travessia do Cinturão', 'Toque para voar entre os asteroides.');

  final String emoji;
  final String nome;
  final String descricao;
  const Minijogo(this.emoji, this.nome, this.descricao);
}

/// Dificuldade cresce com o ano (1º a 5º), sempre suave.
double _fatorAno(int ano) => 0.75 + 0.1 * (ano.clamp(1, 5) - 1); // 0,75 … 1,15

// ---------------------------------------------------------------------------
// Patrulha da Luz (rolagem lateral)

class Drone {
  double x;
  double y;
  final double vel;
  final bool asteroide; // asteroide não acende: só desviar
  bool aceso = false;
  double brilho = 0; // anima a explosão de cores ao acender
  Drone(this.x, this.y, this.vel, {this.asteroide = false});
}

class Raio {
  double x;
  final double y;
  Raio(this.x, this.y);
}

class Patrulha {
  final int ano;
  final Random rnd;
  final double duracao; // segundos de jogo
  double tempo = 0;
  double naveY = 0.5;
  static const naveX = 0.12;
  int escudos = 3;
  int acesos = 0;
  double invencivel = 0;
  double _proxDrone = 0.6;
  double _proxRaio = 0;
  final drones = <Drone>[];
  final raios = <Raio>[];

  Patrulha(this.ano, this.rnd, {this.duracao = 60});

  bool get acabou => escudos <= 0 || tempo >= duracao;

  void moverPara(double y) => naveY = y.clamp(0.08, 0.92);

  void passo(double dt) {
    if (acabou) return;
    tempo += dt;
    invencivel = max(0, invencivel - dt);
    final f = _fatorAno(ano);

    // Disparo automático: a criança só se preocupa em mirar.
    _proxRaio -= dt;
    if (_proxRaio <= 0) {
      raios.add(Raio(naveX + 0.05, naveY));
      _proxRaio = 0.35;
    }
    for (final r in raios) {
      r.x += 1.2 * dt;
    }
    raios.removeWhere((r) => r.x > 1.05);

    _proxDrone -= dt;
    if (_proxDrone <= 0) {
      final asteroide = ano >= 3 && rnd.nextDouble() < 0.25;
      drones.add(
        Drone(
          1.08,
          0.1 + rnd.nextDouble() * 0.8,
          (0.18 + rnd.nextDouble() * 0.12) * f,
          asteroide: asteroide,
        ),
      );
      _proxDrone = (1.3 - min(tempo, 50) / 100) / f;
    }
    for (final d in drones) {
      d.x -= d.vel * dt * (d.aceso ? 0.4 : 1);
      if (d.aceso) d.brilho += dt;
    }

    // Raio encosta no drone: ele acende e vira estrela colorida.
    for (final d in drones) {
      if (d.aceso || d.asteroide) continue;
      for (final r in List.of(raios)) {
        if ((r.x - d.x).abs() < 0.05 && (r.y - d.y).abs() < 0.06) {
          d.aceso = true;
          acesos++;
          raios.remove(r);
          break;
        }
      }
    }

    // Drone apagado ou asteroide encosta na nave: perde um escudo.
    for (final d in drones) {
      if (d.aceso || invencivel > 0) continue;
      if ((d.x - naveX).abs() < 0.06 && (d.y - naveY).abs() < 0.07) {
        escudos--;
        invencivel = 1.5;
        d.aceso = !d.asteroide;
        if (d.asteroide) d.x = -1;
      }
    }
    drones.removeWhere((d) => d.x < -0.1 || d.brilho > 1.2);
  }
}

// ---------------------------------------------------------------------------
// Cauda de Cometa (cobrinha com perguntas)

class Resposta {
  final Pos pos;
  final String texto;
  final bool certa;
  const Resposta(this.pos, this.texto, this.certa);
}

class Cauda {
  final int colunas;
  final int linhas;
  final Random rnd;
  final List<DesafioPorta> desafios;
  int _desafio = 0;

  late List<Pos> corpo; // corpo.first é a nave
  Dir dir = Dir.direita;
  Dir? _proxima;
  int crescer = 0;
  int pontos = 0;
  int acertos = 0;
  int erros = 0;
  bool bateu = false;
  final estrelas = <Pos>{};
  List<Resposta> respostas = [];
  DesafioPorta? pergunta;
  String? retorno; // explicação depois de um erro

  Cauda(this.rnd, this.desafios, {this.colunas = 12, this.linhas = 14}) {
    final meio = Pos(colunas ~/ 3, linhas ~/ 2);
    corpo = [meio, Pos(meio.x - 1, meio.y), Pos(meio.x - 2, meio.y)];
    for (var i = 0; i < 3; i++) {
      _novaEstrela();
    }
    _novaPergunta();
  }

  /// Velocidade em casas por segundo, pelo ano.
  static double velocidade(int ano) => 3.5 + 0.5 * (ano.clamp(1, 5) - 1);

  void virar(Dir d) {
    final atual = _proxima ?? dir;
    if (d == atual.oposta) return; // não dá meia-volta em cima da cauda
    _proxima = d;
  }

  Set<Pos> get _ocupadas => {...corpo, ...estrelas, ...respostas.map((r) => r.pos)};

  Pos? _casaLivre() {
    final ocupadas = _ocupadas;
    final cabeca = corpo.first;
    final livres = [
      for (var y = 0; y < linhas; y++)
        for (var x = 0; x < colunas; x++)
          if (!ocupadas.contains(Pos(x, y)) && (x - cabeca.x).abs() + (y - cabeca.y).abs() > 2)
            Pos(x, y),
    ];
    return livres.isEmpty ? null : livres[rnd.nextInt(livres.length)];
  }

  void _novaEstrela() {
    final p = _casaLivre();
    if (p != null) estrelas.add(p);
  }

  void _novaPergunta() {
    respostas = [];
    if (desafios.isEmpty) {
      pergunta = null;
      return;
    }
    final d = desafios[_desafio++ % desafios.length];
    pergunta = d;
    for (var i = 0; i < d.opcoes.length; i++) {
      final p = _casaLivre();
      if (p != null) respostas.add(Resposta(p, d.opcoes[i], i == d.correta));
    }
  }

  /// Avança uma casa. O espaço "dá a volta": sair por um lado entra pelo outro.
  void passo() {
    if (bateu) return;
    dir = _proxima ?? dir;
    _proxima = null;
    final c = corpo.first;
    final nova = Pos((c.x + dir.dx) % colunas, (c.y + dir.dy) % linhas);
    final cresce = crescer > 0;
    final semRabo = cresce ? corpo : corpo.sublist(0, corpo.length - 1);
    if (semRabo.contains(nova)) {
      bateu = true;
      return;
    }
    corpo = [nova, ...semRabo];
    if (cresce) crescer--;

    if (estrelas.remove(nova)) {
      pontos += 1;
      crescer += 1;
      _novaEstrela();
    }
    final r = respostas.where((r) => r.pos == nova).firstOrNull;
    if (r != null) {
      if (r.certa) {
        acertos++;
        pontos += 5;
        crescer += 3;
        retorno = null;
      } else {
        erros++;
        final p = pergunta!;
        retorno = 'A resposta era: ${p.opcoes[p.correta]}';
      }
      _novaPergunta();
    }
  }
}

// ---------------------------------------------------------------------------
// Travessia do Cinturão (voo de toque)

class Coluna {
  double x;
  final double centro; // centro da passagem
  final double abertura;
  bool contada = false;
  Coluna(this.x, this.centro, this.abertura);
}

class Travessia {
  final int ano;
  final Random rnd;
  double y = 0.45;
  double vy = 0;
  double tempo = 0;
  int passagens = 0;
  bool bateu = false;
  bool comecou = false;
  static const naveX = 0.25;
  static const raio = 0.035;
  final colunas = <Coluna>[];
  double _proxColuna = 0;

  Travessia(this.ano, this.rnd);

  /// Passagem mais larga nos anos iniciais.
  double get abertura => 0.36 - 0.025 * (ano.clamp(1, 5) - 1);
  double get velocidade => 0.25 * _fatorAno(ano);

  void tocar() {
    if (bateu) return;
    comecou = true;
    vy = -0.55;
  }

  void passo(double dt) {
    if (bateu || !comecou) return;
    tempo += dt;
    vy = min(vy + 1.2 * dt, 0.7); // gravidade suave
    y += vy * dt;
    if (y < raio) {
      y = raio;
      vy = 0;
    }
    _proxColuna -= dt;
    if (_proxColuna <= 0) {
      final ab = abertura;
      colunas.add(Coluna(1.1, ab / 2 + 0.08 + rnd.nextDouble() * (0.84 - ab), ab));
      _proxColuna = 0.42 / velocidade;
    }
    for (final c in colunas) {
      c.x -= velocidade * dt;
      if (!c.contada && c.x < naveX) {
        c.contada = true;
        passagens++;
      }
    }
    colunas.removeWhere((c) => c.x < -0.15);

    if (y > 1 - raio) bateu = true;
    for (final c in colunas) {
      if ((c.x - naveX).abs() < 0.06 + raio &&
          (y - raio < c.centro - c.abertura / 2 || y + raio > c.centro + c.abertura / 2)) {
        bateu = true;
      }
    }
  }
}

/// Peixinhos de uma partida de minijogo: poucos, para o estudo continuar
/// sendo o centro.
int peixinhosDoMinijogo(int pontos) => (3 + pontos ~/ 3).clamp(3, 15);
