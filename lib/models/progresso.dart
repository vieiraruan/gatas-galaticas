/// Resultado de uma missão concluída por uma criança.
class MissaoConcluida {
  final String missaoId;
  final DateTime data; // dia em que foi concluída pela primeira vez
  final int estrelas; // 1 a 3

  const MissaoConcluida({
    required this.missaoId,
    required this.data,
    required this.estrelas,
  });

  factory MissaoConcluida.fromJson(Map<String, dynamic> json) =>
      MissaoConcluida(
        missaoId: json['missaoId'] as String,
        data: DateTime.parse(json['data'] as String),
        estrelas: json['estrelas'] as int,
      );

  Map<String, dynamic> toJson() => {
        'missaoId': missaoId,
        'data': data.toIso8601String(),
        'estrelas': estrelas,
      };
}

/// Progresso de uma criança na sua trilha.
class Progresso {
  final Map<String, MissaoConcluida> concluidas;

  const Progresso(this.concluidas);

  static const vazio = Progresso({});

  bool concluiu(String missaoId) => concluidas.containsKey(missaoId);

  int get totalEstrelas =>
      concluidas.values.fold(0, (soma, m) => soma + m.estrelas);

  factory Progresso.fromJson(Map<String, dynamic> json) => Progresso({
        for (final item in (json['concluidas'] as List))
          (item['missaoId'] as String):
              MissaoConcluida.fromJson(item as Map<String, dynamic>),
      });

  Map<String, dynamic> toJson() =>
      {'concluidas': concluidas.values.map((m) => m.toJson()).toList()};
}
