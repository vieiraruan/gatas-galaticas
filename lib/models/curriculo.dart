/// Modelos do conteúdo pedagógico (trilha de um ano escolar).
///
/// O conteúdo vem de `assets/curriculo/ano_N.json`. Veja
/// `docs/formato_curriculo.md` para o formato completo.
class Questao {
  final String enunciado;
  final List<String> alternativas;
  final int correta;
  final String? explicacao;

  const Questao({
    required this.enunciado,
    required this.alternativas,
    required this.correta,
    this.explicacao,
  });

  factory Questao.fromJson(Map<String, dynamic> json) {
    final alternativas = (json['alternativas'] as List).cast<String>();
    final correta = json['correta'] as int;
    if (correta < 0 || correta >= alternativas.length) {
      throw FormatException(
          'Questão "${json['enunciado']}" tem índice "correta" inválido.');
    }
    return Questao(
      enunciado: json['enunciado'] as String,
      alternativas: alternativas,
      correta: correta,
      explicacao: json['explicacao'] as String?,
    );
  }
}

class Missao {
  final String id;
  final String titulo;
  final String componente; // Ex.: Língua Portuguesa, Matemática, Ciências...
  final List<String> habilidadesBncc; // Ex.: EF01MA01
  final List<Questao> questoes;

  const Missao({
    required this.id,
    required this.titulo,
    required this.componente,
    required this.habilidadesBncc,
    required this.questoes,
  });

  factory Missao.fromJson(Map<String, dynamic> json) => Missao(
        id: json['id'] as String,
        titulo: json['titulo'] as String,
        componente: json['componente'] as String,
        habilidadesBncc:
            ((json['habilidadesBncc'] as List?) ?? const []).cast<String>(),
        questoes: (json['questoes'] as List)
            .map((q) => Questao.fromJson(q as Map<String, dynamic>))
            .toList(),
      );
}

class Bimestre {
  final int numero; // 1 a 4
  final String titulo;
  final List<Missao> missoes;

  const Bimestre({
    required this.numero,
    required this.titulo,
    required this.missoes,
  });

  factory Bimestre.fromJson(Map<String, dynamic> json) => Bimestre(
        numero: json['numero'] as int,
        titulo: json['titulo'] as String,
        missoes: (json['missoes'] as List)
            .map((m) => Missao.fromJson(m as Map<String, dynamic>))
            .toList(),
      );
}

class TrilhaAno {
  final int ano; // 1 a 5
  final String titulo;
  final List<Bimestre> bimestres;

  const TrilhaAno({
    required this.ano,
    required this.titulo,
    required this.bimestres,
  });

  factory TrilhaAno.fromJson(Map<String, dynamic> json) => TrilhaAno(
        ano: json['ano'] as int,
        titulo: json['titulo'] as String,
        bimestres: (json['bimestres'] as List)
            .map((b) => Bimestre.fromJson(b as Map<String, dynamic>))
            .toList()
          ..sort((a, b) => a.numero.compareTo(b.numero)),
      );

  Bimestre? bimestre(int numero) {
    for (final b in bimestres) {
      if (b.numero == numero) return b;
    }
    return null;
  }

  Missao? missao(String id) {
    for (final b in bimestres) {
      for (final m in b.missoes) {
        if (m.id == id) return m;
      }
    }
    return null;
  }
}
