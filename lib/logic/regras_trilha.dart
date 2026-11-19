import '../models/curriculo.dart';
import '../models/progresso.dart';

/// Regras da trilha: qual é o bimestre atual, qual é a missão do dia e
/// quais missões estão liberadas. Tudo aqui é puro (sem I/O) para facilitar
/// os testes.

/// Quantas missões novas a criança pode concluir por dia.
const missoesNovasPorDia = 1;

/// Bimestre do calendário escolar para uma data.
/// Calendário aproximado: fev–abr = 1º, mai–jul = 2º, ago–set = 3º,
/// out–dez = 4º. Janeiro (férias) conta como 1º, preparando o novo ano.
int bimestreDoCalendario(DateTime data) {
  final mes = data.month;
  if (mes <= 4) return 1;
  if (mes <= 7) return 2;
  if (mes <= 9) return 3;
  return 4;
}

DateTime _dia(DateTime d) => DateTime(d.year, d.month, d.day);

bool mesmoDia(DateTime a, DateTime b) => _dia(a) == _dia(b);

enum StatusMissao { concluida, disponivel, amanha, bloqueada }

class RegrasTrilha {
  final TrilhaAno trilha;
  final Progresso progresso;
  final DateTime hoje;

  RegrasTrilha({
    required this.trilha,
    required this.progresso,
    required this.hoje,
  });

  int get bimestreAtual => bimestreDoCalendario(hoje);

  /// Bimestres até o atual ficam abertos (para a criança poder recuperar
  /// o que ficou para trás). Bimestres futuros ficam fechados.
  bool bimestreAberto(int numero) => numero <= bimestreAtual;

  int get missoesConcluidasHoje =>
      progresso.concluidas.values.where((m) => mesmoDia(m.data, hoje)).length;

  bool get podeFazerMissaoNova => missoesConcluidasHoje < missoesNovasPorDia;

  /// A missão do dia: a primeira missão não concluída do bimestre atual.
  /// Se o bimestre atual já terminou, pega a primeira pendente dos
  /// bimestres anteriores. Retorna null se não há nada pendente.
  Missao? get missaoDoDia {
    final ordem = <int>[
      bimestreAtual,
      for (var n = 1; n < bimestreAtual; n++) n,
    ];
    for (final numero in ordem) {
      final b = trilha.bimestre(numero);
      if (b == null) continue;
      for (final m in b.missoes) {
        if (!progresso.concluiu(m.id)) return m;
      }
    }
    return null;
  }

  StatusMissao status(Bimestre bimestre, Missao missao) {
    if (progresso.concluiu(missao.id)) return StatusMissao.concluida;
    if (!bimestreAberto(bimestre.numero)) return StatusMissao.bloqueada;
    // Dentro do bimestre, as missões seguem em ordem.
    final primeiraPendente =
        bimestre.missoes.firstWhere((m) => !progresso.concluiu(m.id));
    if (primeiraPendente.id != missao.id) return StatusMissao.bloqueada;
    return podeFazerMissaoNova ? StatusMissao.disponivel : StatusMissao.amanha;
  }

  /// Dias seguidos (até hoje ou ontem) com pelo menos uma missão concluída.
  int get sequenciaDias {
    final dias = progresso.concluidas.values.map((m) => _dia(m.data)).toSet();
    var dia = _dia(hoje);
    if (!dias.contains(dia)) {
      dia = dia.subtract(const Duration(days: 1));
    }
    var sequencia = 0;
    while (dias.contains(dia)) {
      sequencia++;
      dia = DateTime(dia.year, dia.month, dia.day - 1);
    }
    return sequencia;
  }
}

/// Estrelas de 1 a 3 conforme a porcentagem de acertos.
int estrelasPorAcertos(int acertos, int total) {
  if (total == 0) return 1;
  final p = acertos / total;
  if (p >= 0.9) return 3;
  if (p >= 0.6) return 2;
  return 1;
}
