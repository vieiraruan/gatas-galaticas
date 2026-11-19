/// Progresso de uma criança. Estrelas, jogadas e cápsulas são guardadas
/// por nível de dificuldade: a chave é `nivel:idDoNó`.
class Progresso {
  final int xp;
  final int peixinhos;
  final Map<String, int> xpPorDia; // "2026-11-19" → XP do dia
  final Map<String, int> estrelas;
  final Map<String, int> jogadas;
  final Set<String> capsulas;

  const Progresso({
    this.xp = 0,
    this.peixinhos = 0,
    this.xpPorDia = const {},
    this.estrelas = const {},
    this.jogadas = const {},
    this.capsulas = const {},
  });

  static const vazio = Progresso();

  static String chave(String nivel, String no) => '$nivel:$no';

  int estrelasDe(String nivel, String no) => estrelas[chave(nivel, no)] ?? 0;
  int jogadasDe(String nivel, String no) => jogadas[chave(nivel, no)] ?? 0;
  bool capsulaAberta(String nivel, String no) =>
      capsulas.contains(chave(nivel, no));

  Progresso copyWith({
    int? xp,
    int? peixinhos,
    Map<String, int>? xpPorDia,
    Map<String, int>? estrelas,
    Map<String, int>? jogadas,
    Set<String>? capsulas,
  }) =>
      Progresso(
        xp: xp ?? this.xp,
        peixinhos: peixinhos ?? this.peixinhos,
        xpPorDia: xpPorDia ?? this.xpPorDia,
        estrelas: estrelas ?? this.estrelas,
        jogadas: jogadas ?? this.jogadas,
        capsulas: capsulas ?? this.capsulas,
      );

  factory Progresso.fromJson(Map<String, dynamic> j) => Progresso(
        xp: (j['xp'] as int?) ?? 0,
        peixinhos: (j['peixinhos'] as int?) ?? 0,
        xpPorDia: Map<String, int>.from((j['xpPorDia'] as Map?) ?? const {}),
        estrelas: Map<String, int>.from((j['estrelas'] as Map?) ?? const {}),
        jogadas: Map<String, int>.from((j['jogadas'] as Map?) ?? const {}),
        capsulas: ((j['capsulas'] as List?) ?? const []).cast<String>().toSet(),
      );

  Map<String, dynamic> toJson() => {
        'xp': xp,
        'peixinhos': peixinhos,
        'xpPorDia': xpPorDia,
        'estrelas': estrelas,
        'jogadas': jogadas,
        'capsulas': capsulas.toList(),
      };
}
