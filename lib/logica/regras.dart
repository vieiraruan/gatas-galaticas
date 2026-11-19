import 'dart:math';

import '../modelos/conteudo.dart';
import '../modelos/progresso.dart';

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

  /// Bloqueado se algum nó jogável anterior ainda não tem estrelas.
  bool bloqueado(int i) {
    for (var j = 0; j < i; j++) {
      final n = nos[j];
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
  'historia': ['historia', 'hum'],
  'geografia': ['geografia', 'hum'],
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
  const MissaoDoDia(this.planeta, this.no, this.indice, this.feita);
}

/// Até 3 sugestões para hoje: o próximo nó de cada disciplina do rodízio.
/// Na sexta (revisão) e no fim de semana, sugere os planetas com mais
/// coisa pendente.
List<MissaoDoDia> missoesDoDia({
  required ConteudoAno conteudo,
  required BimestreConteudo bimestre,
  required Progresso progresso,
  required String nivel,
  required DateTime hoje,
}) {
  final rodizio = conteudo.rodizio[hoje.weekday] ?? const [];
  final ordem = <Planeta>[];
  for (final d in rodizio) {
    final p = planetaDaDisciplina(bimestre, d);
    if (p != null && !ordem.contains(p)) ordem.add(p);
  }
  for (final p in bimestre.planetas) {
    if (!ordem.contains(p)) ordem.add(p);
  }
  final out = <MissaoDoDia>[];
  for (final p in ordem) {
    final r = RegrasPlaneta(p, progresso, nivel);
    final i = r.atual;
    if (i < 0) continue;
    out.add(MissaoDoDia(p, r.nos[i], i, false));
    if (out.length == 3) break;
  }
  return out;
}

// ---------------------------------------------------------------------------
// Montagem das perguntas de uma partida

List<Exercicio> montarPartida(No no, Nivel nivel, Random rnd) {
  final missoes = missoesDoNo(no);
  if (missoes.isEmpty) return const [];
  final total = switch (no) {
    NoMissao() => nivel.perguntasMissao,
    NoRevisao() => nivel.perguntasRevisao,
    _ => nivel.perguntasChefao,
  };
  List<Exercicio> lista;
  if (no is NoMissao) {
    lista = _sortear(missoes.first, nivel, total, rnd);
  } else {
    final porMissao = (total / missoes.length).ceil() + (no is NoChefao ? 1 : 0);
    lista = [for (final m in missoes) ..._sortear(m, nivel, porMissao, rnd)]
      ..shuffle(rnd);
    lista = lista.take(total).toList();
  }
  return [for (final e in lista) adaptar(e, nivel, rnd)];
}

List<Exercicio> _sortear(Missao m, Nivel nivel, int n, Random rnd) {
  final base = nivel.desafio && m.exerciciosDesafio.isNotEmpty
      ? m.exerciciosDesafio
      : m.exercicios;
  final out = <Exercicio>[];
  while (out.length < n) {
    out.addAll((List.of(base)..shuffle(rnd)).take(n - out.length));
  }
  return out;
}

/// Ajusta a pergunta ao nível: menos opções, menos itens, sem dicas.
Exercicio adaptar(Exercicio e, Nivel nivel, Random rnd) {
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
