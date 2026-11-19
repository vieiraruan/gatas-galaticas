/// Perfil de uma criança: nome, ano escolar (1º a 5º), gatinho capitão
/// e nível de dificuldade escolhido.
class PerfilCrianca {
  final String id;
  final String nome;
  final int ano;
  final String gato;
  final String nivel;
  final bool som;

  const PerfilCrianca({
    required this.id,
    required this.nome,
    required this.ano,
    required this.gato,
    this.nivel = 'f',
    this.som = true,
  });

  PerfilCrianca copyWith(
          {String? nome, int? ano, String? gato, String? nivel, bool? som}) =>
      PerfilCrianca(
        id: id,
        nome: nome ?? this.nome,
        ano: ano ?? this.ano,
        gato: gato ?? this.gato,
        nivel: nivel ?? this.nivel,
        som: som ?? this.som,
      );

  factory PerfilCrianca.fromJson(Map<String, dynamic> j) => PerfilCrianca(
        id: j['id'] as String,
        nome: j['nome'] as String,
        ano: j['ano'] as int,
        gato: (j['gato'] as String?) ?? 'jojo',
        nivel: (j['nivel'] as String?) ?? 'f',
        som: (j['som'] as bool?) ?? true,
      );

  Map<String, dynamic> toJson() => {
        'id': id,
        'nome': nome,
        'ano': ano,
        'gato': gato,
        'nivel': nivel,
        'som': som,
      };
}
