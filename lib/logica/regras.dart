import 'dart:math';

import '../modelos/conteudo.dart';
import '../modelos/progresso.dart';
import '../modelos/rotina.dart';

/// Regras do jogo, no mesmo espírito da Galáxia do Saber.
/// Tudo aqui é puro (sem I/O) para facilitar os testes.

const metaXpDia = 30;
const xpPorNivel = 60;
const patentes = [
  'Cadete',
  'Piloto',
  'Navegador',
  'Tenente',
  'Capitão',
  'Comandante',
  'Almirante',
  'Lenda da Galáxia',
];

String chaveDia(DateTime d) =>
    '${d.year}-${d.month.toString().padLeft(2, '0')}-${d.day.toString().padLeft(2, '0')}';

int nivelJogador(int xp) => xp ~/ xpPorNivel + 1;

String patente(int xp) =>
    patentes[min(patentes.length - 1, (nivelJogador(xp) - 1) ~/ 2)];

/// Dias seguidos (até hoje, ou até ontem se hoje ainda não jogou).
int sequenciaDias(Map<String, int> xpPorDia, DateTime hoje) {
  var d = DateTime(hoje.year, hoje.month, hoje.day);
  if ((xpPorDia[chaveDia(d)] ?? 0) == 0) d = DateTime(d.year, d.month, d.day - 1);
  var n = 0;
  while ((xpPorDia[chaveDia(d)] ?? 0) > 0) {
    n++;
    d = DateTime(d.year, d.month, d.day - 1);
  }
  return n;
}

/// Bimestre do calendário escolar: fev–abr 1º, mai–jul 2º, ago–set 3º,
/// out–dez 4º. Janeiro (férias) conta como 1º.
int bimestreDoCalendario(DateTime data) {
  final m = data.month;
  if (m <= 4) return 1;
  if (m <= 7) return 2;
  if (m <= 9) return 3;
  return 4;
}

/// Estrelas pela porcentagem de acertos de primeira.
int estrelasPorAcerto(int acertos, int total) {
  if (total == 0) return 1;
  final p = acertos * 100 / total;
  if (p >= 90) return 3;
  if (p >= 70) return 2;
  return 1;
}

// ---------------------------------------------------------------------------
// Nós do caminho de um planeta

sealed class No {
  final String id;
  const No(this.id);
  String get rotulo;
  String get emoji;
}

class NoMissao extends No {
  final Missao missao;
  final Setor setor;
  final int indiceSetor;
  NoMissao(this.missao, this.setor, this.indiceSetor) : super(missao.id);
  @override
  String get rotulo => missao.titulo;
  @override
  String get emoji => missao.emoji;
}

class NoRevisao extends No {
  final Setor setor;
  final int indiceSetor;
  NoRevisao(this.setor, this.indiceSetor) : super('${setor.id}-revisao');
  @override
  String get rotulo => 'Revisão: ${setor.titulo}';
  @override
  String get emoji => '🏆';
}

class NoCapsula extends No {
  final Setor setor;
  final int indiceSetor;
  NoCapsula(this.setor, this.indiceSetor) : super('${setor.id}-capsula');
  @override
  String get rotulo => 'Cápsula de peixinhos';
  @override
  String get emoji => '📦';
}

class NoChefao extends No {
  final Planeta planeta;
  NoChefao(this.planeta) : super('${planeta.id}-chefao');
  @override
  String get rotulo => 'Chefão: ${planeta.chefaoNome}';
  @override
  String get emoji => planeta.chefaoEmoji;
}

/// Treino para uma prova marcada pelos pais: mistura os assuntos da prova.
class NoTreino extends No {
  final Planeta planeta;
  final List<Setor> setores;
  NoTreino(this.planeta, this.setores, String provaId) : super('treino-$provaId');
  @override
  String get rotulo => 'Treino para a prova';
  @override
  String get emoji => '📝';
}

/// Prova surpresa: uma pergunta de cada missão já feita.
class NoSurpresa extends No {
  final List<Missao> missoes;
  NoSurpresa(this.missoes) : super('surpresa');
  @override
  String get rotulo => 'Prova surpresa';
  @override
  String get emoji => '🚨';
}

/// Setor (planeta) de um nó; -1 para o chefão e nós especiais.
int setorDoNo(No no) => switch (no) {
      NoMissao(:final indiceSetor) => indiceSetor,
      NoRevisao(:final indiceSetor) => indiceSetor,
      NoCapsula(:final indiceSetor) => indiceSetor,
      _ => -1,
    };

List<No> nosDoPlaneta(Planeta p) => [
      for (var i = 0; i < p.setores.length; i++) ...[
        for (final m in p.setores[i].missoes) NoMissao(m, p.setores[i], i),
        NoRevisao(p.setores[i], i),
        NoCapsula(p.setores[i], i),
      ],
      NoChefao(p),
    ];

/// Missões jogáveis que alimentam um nó (revisão e chefão misturam várias).
List<Missao> missoesDoNo(No no) => switch (no) {
      NoMissao(:final missao) => <Missao>[missao],
      NoRevisao(:final setor) => setor.missoes,
      NoCapsula() => const <Missao>[],
      NoChefao(:final planeta) => planeta.missoes.toList(),
      NoTreino(:final setores) => setores.expand((x) => x.missoes).toList(),
      NoSurpresa(:final missoes) => missoes,
    }
        .where((m) => !m.emBreve)
        .toList();

/// Nó ainda sem conteúdo: aparece no caminho, mas não bloqueia nem joga.
bool emBreve(No no) => no is! NoCapsula && missoesDoNo(no).isEmpty;

class RegrasPlaneta {
  final Planeta planeta;
  final Progresso progresso;
  final String nivel;
  late final List<No> nos = nosDoPlaneta(planeta);

  RegrasPlaneta(this.planeta, this.progresso, this.nivel);

  int estrelas(No no) => progresso.estrelasDe(nivel, no.id);
  bool capsulaAberta(No no) => progresso.capsulaAberta(nivel, no.id);

  /// Bloqueado se algum nó jogável anterior do mesmo setor (planeta) ainda
  /// não tem estrelas. Os planetas são livres; o chefão pede todos.
  bool bloqueado(int i) {
    final setor = setorDoNo(nos[i]);
    for (var j = 0; j < i; j++) {
      final n = nos[j];
      if (setor >= 0 && setorDoNo(n) != setor) continue;
      if (n is NoCapsula || emBreve(n)) continue;
      if (estrelas(n) == 0) return true;
    }
    return false;
  }

  /// Índice do próximo nó a jogar (ou -1 se terminou).
  int get atual => nos.indexWhere(
      (n) => n is! NoCapsula && !emBreve(n) && estrelas(n) == 0);

  /// Cápsula pronta para abrir: revisão anterior feita e ainda fechada.
  bool capsulaPronta(int i) {
    final n = nos[i];
    if (n is! NoCapsula || capsulaAberta(n)) return false;
    final rev = nos[i - 1];
    return emBreve(rev) ? false : estrelas(rev) > 0;
  }

  /// Índices dos nós de um setor (planeta), em ordem.
  List<int> indicesDoSetor(int setor) =>
      [for (var i = 0; i < nos.length; i++) if (setorDoNo(nos[i]) == setor) i];

  int get indiceChefao => nos.length - 1;

  /// Próximo nó a jogar dentro de um setor (ou -1 se terminou).
  int atualDoSetor(int setor) {
    for (final i in indicesDoSetor(setor)) {
      final n = nos[i];
      if (n is! NoCapsula && !emBreve(n) && estrelas(n) == 0) return i;
    }
    return -1;
  }

  ({int ganhas, int maximo, int feitas, int total}) resumoDoSetor(int setor) {
    final jogaveis = [
      for (final i in indicesDoSetor(setor))
        if (nos[i] is! NoCapsula && !emBreve(nos[i])) nos[i]
    ];
    return (
      ganhas: jogaveis.fold(0, (s, n) => s + estrelas(n)),
      maximo: jogaveis.length * 3,
      feitas: jogaveis.where((n) => estrelas(n) > 0).length,
      total: jogaveis.length,
    );
  }

  bool get temConteudo => nos.any((n) => !emBreve(n) && n is! NoCapsula);

  ({int ganhas, int maximo, int feitas, int total, bool chefao}) get resumo {
    final jogaveis =
        nos.where((n) => n is! NoCapsula && !emBreve(n)).toList();
    return (
      ganhas: jogaveis.fold(0, (s, n) => s + estrelas(n)),
      maximo: jogaveis.length * 3,
      feitas: jogaveis.where((n) => estrelas(n) > 0).length,
      total: jogaveis.length,
      chefao: estrelas(nos.last) > 0,
    );
  }
}

// ---------------------------------------------------------------------------
// Missões do dia (rodízio da BNCC)

/// Apelidos: disciplina da BNCC → sufixo do id do planeta.
const _apelidos = {
  'portugues': ['portugues', 'por'],
  'matematica': ['matematica', 'mat'],
  'ciencias': ['ciencias', 'cie'],
  'humanas': ['humanas', 'hum'],
  'etica': ['etica', 'eti'],
  'ingles': ['ingles', 'ing'],
  // Trilha v1 (antes de Ciências Humanas).
  'historia': ['historia', 'humanas', 'hum'],
  'geografia': ['geografia', 'humanas', 'hum'],
};

Planeta? planetaDaDisciplina(BimestreConteudo b, String disciplina) {
  final sufixos = _apelidos[disciplina] ?? [disciplina];
  for (final p in b.planetas) {
    if (sufixos.any((s) => p.id.endsWith('-$s'))) return p;
  }
  return null;
}

class MissaoDoDia {
  final Planeta planeta;
  final No no;
  final int indice;
  final bool feita;

  /// Por que foi sugerida (ex.: '📝 Prova em 3 dias'), ou null.
  final String? motivo;
  const MissaoDoDia(this.planeta, this.no, this.indice, this.feita, {this.motivo});
}

/// Até 3 sugestões para hoje:
/// 1. assuntos de provas marcadas pelos pais para os próximos 14 dias;
/// 2. as matérias que têm aula hoje (horário dos pais) ou o rodízio da BNCC;
/// 3. os outros planetas com coisa pendente.
List<MissaoDoDia> missoesDoDia({
  required ConteudoAno conteudo,
  required BimestreConteudo bimestre,
  required Progresso progresso,
  required String nivel,
  required DateTime hoje,
  Rotina rotina = Rotina.vazia,
  int? bimestreAtual,
}) {
  final out = <MissaoDoDia>[];
  final usados = <String>{};
  void add(Planeta p, RegrasPlaneta r, int i, {String? motivo}) {
    if (i < 0 || out.length >= 3 || usados.contains('${p.id}#$i')) return;
    usados.add('${p.id}#$i');
    out.add(MissaoDoDia(p, r.nos[i], i, false, motivo: motivo));
  }

  // 1. Provas chegando.
  final abertos = bimestreAtual ?? bimestre.numero;
  for (final prova in rotina.proximas(hoje, dentroDeDias: 14)) {
    final dias = prova.diasAte(hoje);
    final motivo = dias == 0
        ? '📝 Prova hoje!'
        : dias == 1
            ? '📝 Prova amanhã'
            : '📝 Prova em $dias dias';
    for (final b in conteudo.bimestres.where((b) => b.numero <= abertos)) {
      for (final p in b.planetas) {
        if (materiaDoPlaneta(p) != prova.materia) continue;
        final r = RegrasPlaneta(p, progresso, nivel);
        for (var s = 0; s < p.setores.length; s++) {
          if (prova.assuntos.contains(p.setores[s].id)) {
            add(p, r, r.atualDoSetor(s), motivo: motivo);
          }
        }
      }
    }
  }

  // 2. Aulas de hoje (ou rodízio) e 3. o resto do bimestre.
  final doDia = rotina.temHorario
      ? (rotina.horario[hoje.weekday] ?? const <String>[])
      : (conteudo.rodizio[hoje.weekday] ?? const <String>[]);
  final ordem = <Planeta>[];
  for (final d in doDia) {
    final p = planetaDaDisciplina(bimestre, d);
    if (p != null && !ordem.contains(p)) ordem.add(p);
  }
  final comAula = ordem.length;
  for (final p in bimestre.planetas) {
    if (!ordem.contains(p)) ordem.add(p);
  }
  for (var k = 0; k < ordem.length && out.length < 3; k++) {
    final p = ordem[k];
    final r = RegrasPlaneta(p, progresso, nivel);
    add(p, r, r.atual,
        motivo: rotina.temHorario && k < comAula ? '🏫 Teve aula hoje' : null);
  }
  return out;
}

// ---------------------------------------------------------------------------
// Galáxias (matérias) e planetas (assuntos)

class InfoGalaxia {
  final String materia;
  final String nome;
  final String emoji;
  const InfoGalaxia(this.materia, this.nome, this.emoji);
}

const galaxias = [
  InfoGalaxia('portugues', 'Galáxia das Letras', '📚'),
  InfoGalaxia('matematica', 'Galáxia dos Números', '🔢'),
  InfoGalaxia('ciencias', 'Galáxia da Natureza', '🔬'),
  InfoGalaxia('humanas', 'Galáxia dos Povos', '🌎'),
  InfoGalaxia('etica', 'Galáxia da Gentileza', '💗'),
  InfoGalaxia('ingles', 'Galáxia Hello', '🗣️'),
];

const nomesMaterias = {
  'portugues': 'Português',
  'matematica': 'Matemática',
  'ciencias': 'Ciências Naturais',
  'humanas': 'Ciências Humanas',
  'etica': 'Ética',
  'ingles': 'Inglês',
};

InfoGalaxia galaxiaDe(String materia) => galaxias.firstWhere((g) => g.materia == materia,
    orElse: () => InfoGalaxia(materia, 'Galáxia $materia', '🌌'));

/// Matéria de um planeta do conteúdo, pelo fim do id (ex.: a4b4-mat).
String materiaDoPlaneta(Planeta p) {
  final sufixo = p.id.split('-').last;
  for (final g in galaxias) {
    if ((_apelidos[g.materia] ?? [g.materia]).contains(sufixo)) return g.materia;
  }
  return sufixo;
}

/// Os pedaços (um por bimestre) de uma galáxia ao longo do ano.
List<({BimestreConteudo bimestre, Planeta planeta})> partesDaGalaxia(
        ConteudoAno c, String materia) =>
    [
      for (final b in c.bimestres)
        for (final p in b.planetas)
          if (materiaDoPlaneta(p) == materia) (bimestre: b, planeta: p)
    ];

// ---------------------------------------------------------------------------
// Montagem das perguntas de uma partida

List<Exercicio> montarPartida(No no, Nivel nivel, Random rnd) {
  final missoes = missoesDoNo(no);
  if (missoes.isEmpty) return const [];
  final total = switch (no) {
    NoMissao() => nivel.perguntasMissao,
    NoRevisao() || NoTreino() => nivel.perguntasRevisao,
    NoSurpresa() => missoes.length,
    _ => nivel.perguntasChefao,
  };
  List<Exercicio> lista;
  if (no is NoSurpresa) {
    lista = [for (final m in missoes) ..._sortear(m, nivel, 1, rnd)];
  } else if (no is NoMissao) {
    lista = _sortear(missoes.first, nivel, total, rnd);
  } else {
    final porMissao = (total / missoes.length).ceil() + (no is NoChefao ? 1 : 0);
    lista = [for (final m in missoes) ..._sortear(m, nivel, porMissao, rnd)]
      ..shuffle(rnd);
    lista = lista.take(total).toList();
  }
  return [for (final e in lista) adaptar(e, nivel, rnd)];
}

List<Exercicio> _sortear(Missao m, Nivel nivel, int n, Random rnd) =>
    sortearPorMistura([...m.exercicios, ...m.exerciciosDesafio], nivel.mistura, n, rnd);

/// Sorteia [n] perguntas seguindo a mistura de complexidade do nível
/// (ex.: {3: 60, 2: 30, 1: 10}). Quando falta pergunta de uma
/// complexidade, completa com a mais próxima, primeiro as mais fáceis.
List<Exercicio> sortearPorMistura(
    List<Exercicio> todas, Map<int, int> mistura, int n, Random rnd) {
  if (todas.isEmpty || n <= 0) return const [];
  final porC = <int, List<Exercicio>>{};
  for (final e in todas) {
    (porC[e.complexidade] ??= []).add(e);
  }
  for (final l in porC.values) {
    l.shuffle(rnd);
  }
  // Cotas por complexidade, arredondadas, somando n.
  final niveis = mistura.keys.toList()..sort((a, b) => b.compareTo(a));
  final total = mistura.values.fold(0, (a, b) => a + b);
  final cotas = <int, int>{};
  var usados = 0;
  for (final c in niveis) {
    final q = (n * mistura[c]! / (total == 0 ? 1 : total)).round();
    cotas[c] = q;
    usados += q;
  }
  if (niveis.isNotEmpty) cotas[niveis.first] = cotas[niveis.first]! + (n - usados);

  final out = <Exercicio>[];
  final usadas = <Exercicio>{};
  Exercicio? pegar(int alvo) {
    // A própria complexidade; depois as mais fáceis; depois as mais difíceis.
    final ordem = [
      alvo,
      for (var c = alvo - 1; c >= 1; c--) c,
      for (var c = alvo + 1; c <= 4; c++) c,
    ];
    for (final c in ordem) {
      final l = porC[c];
      if (l == null) continue;
      for (final e in l) {
        if (!usadas.contains(e)) return e;
      }
    }
    return null;
  }

  for (final c in niveis) {
    for (var i = 0; i < cotas[c]!; i++) {
      final e = pegar(c);
      if (e == null) break;
      usadas.add(e);
      out.add(e);
    }
  }
  // Banco pequeno: repete perguntas até completar.
  while (out.length < n) {
    out.addAll((List.of(todas)..shuffle(rnd)).take(n - out.length));
  }
  return out..shuffle(rnd);
}

/// Uma pergunta de "aquecimento": complexidade abaixo da do nível, das
/// missões do nó. Oferecida depois de 2 erros seguidos, nunca como castigo.
Exercicio? aquecimento(No no, Nivel nivel, Random rnd, {Set<Exercicio> evitar = const {}}) {
  final todas = [
    for (final m in missoesDoNo(no)) ...m.exercicios,
  ];
  if (todas.isEmpty) return null;
  final alvo = max(1, nivel.complexidade - 1);
  final candidatas = todas.where((e) => e.complexidade <= alvo && !evitar.contains(e)).toList();
  final base = candidatas.isNotEmpty
      ? candidatas
      : (todas.toList()..sort((a, b) => a.complexidade.compareTo(b.complexidade)))
          .take(3)
          .toList();
  return adaptar((base..shuffle(rnd)).first, nivel, rnd);
}

/// Acerto mínimo e número de missões seguidas para convidar a subir de nível.
const acertoParaConvite = 80;
const missoesParaConvite = 2;

/// Chave da sequência de missões boas de uma unidade num nível.
String chaveSequencia(String nivel, Setor setor) => '$nivel:${setor.id}';

/// Atualiza a sequência de missões com 80% ou mais e diz se é hora de
/// convidar a criança a subir de nível. Depois do convite a contagem
/// recomeça; a criança escolhe se sobe, e o app nunca rebaixa sozinho.
({int sequencia, bool convidar}) avaliarConvite(int sequenciaAntes, int acerto) {
  if (acerto < acertoParaConvite) return (sequencia: 0, convidar: false);
  final s = sequenciaAntes + 1;
  if (s >= missoesParaConvite) return (sequencia: 0, convidar: true);
  return (sequencia: s, convidar: false);
}

/// Ajusta a pergunta ao nível: menos opções, menos itens, sem dicas.
Exercicio adaptar(Exercicio e, Nivel nivel, Random rnd) =>
    _adaptar(e, nivel, rnd).copiarInfo(e);

Exercicio _adaptar(Exercicio e, Nivel nivel, Random rnd) {
  switch (e) {
    case Escolha():
      var opcoes = e.opcoes;
      var correta = e.correta;
      if (e.embaralhar && opcoes.length > nivel.opcoes) {
        final erradas = [
          for (var i = 0; i < opcoes.length; i++)
            if (i != correta) opcoes[i]
        ]..shuffle(rnd);
        opcoes = [opcoes[correta], ...erradas.take(nivel.opcoes - 1)];
        correta = 0;
      }
      return Escolha(
        pergunta: e.pergunta,
        explicacao: e.explicacao,
        opcoes: opcoes,
        correta: correta,
        embaralhar: e.embaralhar,
        visuais: e.visuais,
        dica: nivel.dicas ? e.dica : null,
        dicaVisuais: nivel.dicas ? e.dicaVisuais : const [],
      );
    case Completar():
      if (e.opcoes.length <= nivel.opcoes) return e;
      final erradas = e.opcoes.sublist(1)..shuffle(rnd);
      return Completar(e.pergunta, e.explicacao,
          [e.opcoes.first, ...erradas.take(nivel.opcoes - 1)]);
    case Separar():
      if (e.itens.length <= nivel.itensSeparar) return e;
      final itens = List.of(e.itens)..shuffle(rnd);
      final escolhidos = <({String texto, int grupo})>[];
      for (var g = 0; g < e.grupos.length; g++) {
        final i = itens.where((x) => x.grupo == g);
        if (i.isNotEmpty) escolhidos.add(i.first);
      }
      for (final x in itens) {
        if (escolhidos.length >= nivel.itensSeparar) break;
        if (!escolhidos.contains(x)) escolhidos.add(x);
      }
      return Separar(e.pergunta, e.explicacao, e.grupos, escolhidos);
    case Ligar():
      if (nivel.id == 'f' && e.pares.length > 3) {
        return Ligar(e.pergunta, (List.of(e.pares)..shuffle(rnd)).take(3).toList());
      }
      return e;
    default:
      return e;
  }
}

/// Monta a prova surpresa: até 3 missões já feitas (com estrela), de
/// matérias diferentes quando der.
NoSurpresa? montarSurpresa(Iterable<Planeta> planetas, Progresso progresso,
    String nivel, Random rnd) {
  final feitas = <(String, Missao)>[];
  for (final p in planetas) {
    final r = RegrasPlaneta(p, progresso, nivel);
    for (final n in r.nos) {
      if (n is NoMissao && !n.missao.emBreve && r.estrelas(n) > 0) {
        feitas.add((materiaDoPlaneta(p), n.missao));
      }
    }
  }
  if (feitas.isEmpty) return null;
  feitas.shuffle(rnd);
  final escolhidas = <Missao>[];
  final materias = <String>{};
  for (final (mat, m) in feitas) {
    if (materias.add(mat)) escolhidas.add(m);
    if (escolhidas.length == 3) break;
  }
  for (final (_, m) in feitas) {
    if (escolhidas.length == 3) break;
    if (!escolhidas.contains(m)) escolhidas.add(m);
  }
  return NoSurpresa(escolhidas);
}

/// Oferece a prova surpresa no fim de uma missão? No máximo uma por dia,
/// com 40% de chance a cada missão.
bool sortearSurpresa(Progresso p, DateTime hoje, Random rnd) =>
    (p.surpresasPorDia[chaveDia(hoje)] ?? 0) == 0 && rnd.nextDouble() < 0.4;

// ---------------------------------------------------------------------------
// Desafios de aprendizado no meio da missão

enum TipoDesafio { relampago, sequencia }

class Desafio {
  final TipoDesafio tipo;

  /// Antes de qual pergunta (índice) o desafio aparece.
  final int antesDe;
  const Desafio(this.tipo, this.antesDe);

  String get titulo => switch (tipo) {
        TipoDesafio.relampago => '⚡ Desafio relâmpago!',
        TipoDesafio.sequencia => '🔥 Desafio da sequência!',
      };
  String get descricao => switch (tipo) {
        TipoDesafio.relampago =>
          'Responda a próxima pergunta em até $segundosRelampago segundos e ganhe +$bonusDesafio suprimentos!',
        TipoDesafio.sequencia =>
          'Acerte as próximas 3 perguntas seguidas e ganhe +$bonusDesafio suprimentos!',
      };
}

const segundosRelampago = 25;
const bonusDesafio = 2;

/// Sorteia um desafio para uma missão ou revisão (metade das vezes).
Desafio? sortearDesafio(No no, int perguntas, Random rnd) {
  if (no is! NoMissao && no is! NoRevisao) return null;
  if (perguntas < 4 || rnd.nextDouble() >= 0.5) return null;
  final tipo = TipoDesafio.values[rnd.nextInt(TipoDesafio.values.length)];
  final ultimo = tipo == TipoDesafio.sequencia ? perguntas - 3 : perguntas - 1;
  return Desafio(tipo, 1 + rnd.nextInt(max(1, ultimo)));
}

/// Recompensa de uma partida.
({int xp, int peixinhos}) recompensa(No no, int estrelas, Nivel nivel) {
  final chefao = no is NoChefao;
  return (
    xp: ((chefao ? 30 : 10 + estrelas * 2) * nivel.multiplicador).round(),
    peixinhos: ((chefao ? 20 : estrelas * 3) * nivel.multiplicador).round(),
  );
}

int peixinhosDaCapsula(Nivel nivel, Random rnd) =>
    ((10 + rnd.nextInt(16)) * nivel.multiplicador).round();
