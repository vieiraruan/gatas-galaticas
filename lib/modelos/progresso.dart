/// Progresso de uma criança. Estrelas, jogadas e cápsulas são guardadas
/// por nível de dificuldade: a chave é `nivel:idDoNó`.
class Progresso {
  final int xp;
  final int peixinhos;
  final Map<String, int> xpPorDia; // "2026-11-19" → XP do dia
  final Map<String, int> estrelas;
  final Map<String, int> jogadas;
  final Set<String> capsulas;
  final Map<String, int> labirintosPorDia; // "2026-11-23" → labirintos feitos

  /// Suprimentos da Nave Gatística por matéria (ex.: 'matematica' → 7).
  final Map<String, int> suprimentos;

  /// Peças da Nave Gatística já construídas.
  final Set<String> pecas;

  /// Respostas por matéria, para o acompanhamento dos pais.
  final Map<String, int> acertosPorMateria;
  final Map<String, int> respostasPorMateria;

  /// "2026-11-24" → provas surpresa oferecidas no dia.
  final Map<String, int> surpresasPorDia;

  const Progresso({
    this.xp = 0,
    this.peixinhos = 0,
    this.xpPorDia = const {},
    this.estrelas = const {},
    this.jogadas = const {},
    this.capsulas = const {},
    this.labirintosPorDia = const {},
    this.suprimentos = const {},
    this.pecas = const {},
    this.acertosPorMateria = const {},
    this.respostasPorMateria = const {},
    this.surpresasPorDia = const {},
  });

  static const vazio = Progresso();

  static String chave(String nivel, String no) => '$nivel:$no';

  int estrelasDe(String nivel, String no) => estrelas[chave(nivel, no)] ?? 0;
  int jogadasDe(String nivel, String no) => jogadas[chave(nivel, no)] ?? 0;
  bool capsulaAberta(String nivel, String no) =>
      capsulas.contains(chave(nivel, no));

  /// Maior número de estrelas de um nó em qualquer nível.
  int melhorEstrela(String no) {
    var m = 0;
    for (final e in estrelas.entries) {
      if (e.key.endsWith(':$no') && e.value > m) m = e.value;
    }
    return m;
  }

  Progresso copyWith({
    int? xp,
    int? peixinhos,
    Map<String, int>? xpPorDia,
    Map<String, int>? estrelas,
    Map<String, int>? jogadas,
    Set<String>? capsulas,
    Map<String, int>? labirintosPorDia,
    Map<String, int>? suprimentos,
    Set<String>? pecas,
    Map<String, int>? acertosPorMateria,
    Map<String, int>? respostasPorMateria,
    Map<String, int>? surpresasPorDia,
  }) =>
      Progresso(
        xp: xp ?? this.xp,
        peixinhos: peixinhos ?? this.peixinhos,
        xpPorDia: xpPorDia ?? this.xpPorDia,
        estrelas: estrelas ?? this.estrelas,
        jogadas: jogadas ?? this.jogadas,
        capsulas: capsulas ?? this.capsulas,
        labirintosPorDia: labirintosPorDia ?? this.labirintosPorDia,
        suprimentos: suprimentos ?? this.suprimentos,
        pecas: pecas ?? this.pecas,
        acertosPorMateria: acertosPorMateria ?? this.acertosPorMateria,
        respostasPorMateria: respostasPorMateria ?? this.respostasPorMateria,
        surpresasPorDia: surpresasPorDia ?? this.surpresasPorDia,
      );

  static Map<String, int> _mapa(Object? j) =>
      Map<String, int>.from((j as Map?) ?? const {});

  factory Progresso.fromJson(Map<String, dynamic> j) => Progresso(
        xp: (j['xp'] as int?) ?? 0,
        peixinhos: (j['peixinhos'] as int?) ?? 0,
        xpPorDia: _mapa(j['xpPorDia']),
        estrelas: _mapa(j['estrelas']),
        jogadas: _mapa(j['jogadas']),
        capsulas: ((j['capsulas'] as List?) ?? const []).cast<String>().toSet(),
        labirintosPorDia: _mapa(j['labirintosPorDia']),
        suprimentos: _mapa(j['suprimentos']),
        pecas: ((j['pecas'] as List?) ?? const []).cast<String>().toSet(),
        acertosPorMateria: _mapa(j['acertosPorMateria']),
        respostasPorMateria: _mapa(j['respostasPorMateria']),
        surpresasPorDia: _mapa(j['surpresasPorDia']),
      );

  Map<String, dynamic> toJson() => {
        'xp': xp,
        'peixinhos': peixinhos,
        'xpPorDia': xpPorDia,
        'estrelas': estrelas,
        'jogadas': jogadas,
        'capsulas': capsulas.toList(),
        'labirintosPorDia': labirintosPorDia,
        'suprimentos': suprimentos,
        'pecas': pecas.toList(),
        'acertosPorMateria': acertosPorMateria,
        'respostasPorMateria': respostasPorMateria,
        'surpresasPorDia': surpresasPorDia,
      };
}
