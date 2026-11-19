/// Perfil de uma criança. Cada perfil está ligado a um ano escolar (1º a 5º).
class PerfilCrianca {
  final String id;
  final String nome;
  final int ano;
  final String avatar; // emoji usado como avatar

  const PerfilCrianca({
    required this.id,
    required this.nome,
    required this.ano,
    required this.avatar,
  });

  PerfilCrianca copyWith({String? nome, int? ano, String? avatar}) =>
      PerfilCrianca(
        id: id,
        nome: nome ?? this.nome,
        ano: ano ?? this.ano,
        avatar: avatar ?? this.avatar,
      );

  factory PerfilCrianca.fromJson(Map<String, dynamic> json) => PerfilCrianca(
        id: json['id'] as String,
        nome: json['nome'] as String,
        ano: json['ano'] as int,
        avatar: json['avatar'] as String,
      );

  Map<String, dynamic> toJson() =>
      {'id': id, 'nome': nome, 'ano': ano, 'avatar': avatar};
}

const avataresDisponiveis = ['🦊', '🐼', '🐯', '🐸', '🦄', '🐙', '🦁', '🐧'];
