/// O que os pais configuram para cada criança: horário das aulas e provas.
class Prova {
  final String id;
  final String materia; // 'matematica', 'portugues'...
  final DateTime data;

  /// Ids dos setores (planetas) que caem na prova.
  final List<String> assuntos;

  /// Outros assuntos ou recados escritos pelos pais.
  final String observacao;

  const Prova({
    required this.id,
    required this.materia,
    required this.data,
    this.assuntos = const [],
    this.observacao = '',
  });

  /// Dias até a prova (0 = hoje, negativo = já passou).
  int diasAte(DateTime hoje) => DateTime(data.year, data.month, data.day)
      .difference(DateTime(hoje.year, hoje.month, hoje.day))
      .inDays;

  factory Prova.fromJson(Map<String, dynamic> j) => Prova(
        id: j['id'] as String,
        materia: j['materia'] as String,
        data: DateTime.parse(j['data'] as String),
        assuntos: ((j['assuntos'] as List?) ?? const []).cast<String>(),
        observacao: (j['observacao'] as String?) ?? '',
      );

  Map<String, dynamic> toJson() => {
        'id': id,
        'materia': materia,
        'data': data.toIso8601String().substring(0, 10),
        'assuntos': assuntos,
        'observacao': observacao,
      };
}

class Rotina {
  /// Dia da semana (1 = segunda ... 5 = sexta) → matérias que têm aula.
  /// Vazio = usar o rodízio sugerido pelo app.
  final Map<int, List<String>> horario;
  final List<Prova> provas;

  const Rotina({this.horario = const {}, this.provas = const []});

  static const vazia = Rotina();

  bool get temHorario => horario.values.any((l) => l.isNotEmpty);

  /// Provas de hoje em diante, da mais próxima para a mais distante.
  List<Prova> proximas(DateTime hoje, {int dentroDeDias = 9999}) => [
        for (final p in provas)
          if (p.diasAte(hoje) >= 0 && p.diasAte(hoje) <= dentroDeDias) p
      ]..sort((a, b) => a.data.compareTo(b.data));

  Rotina copyWith({Map<int, List<String>>? horario, List<Prova>? provas}) =>
      Rotina(horario: horario ?? this.horario, provas: provas ?? this.provas);

  factory Rotina.fromJson(Map<String, dynamic> j) => Rotina(
        horario: {
          for (final e in ((j['horario'] as Map?) ?? const {}).entries)
            int.parse(e.key as String): (e.value as List).cast<String>(),
        },
        provas: [
          for (final p in (j['provas'] as List?) ?? const [])
            Prova.fromJson(p as Map<String, dynamic>)
        ],
      );

  Map<String, dynamic> toJson() => {
        'horario': {for (final e in horario.entries) '${e.key}': e.value},
        'provas': [for (final p in provas) p.toJson()],
      };
}
