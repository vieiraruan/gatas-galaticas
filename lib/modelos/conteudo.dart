import 'dart:ui' show Color;

/// Conteúdo de um ano escolar: bimestres → planetas (disciplinas) →
/// setores (unidades) → missões. Formato em docs/formato_conteudo.md.

Color corHex(String hex) =>
    Color(int.parse('FF${hex.replaceFirst('#', '')}', radix: 16));

List<T> _lista<T>(Object? json, T Function(Map<String, dynamic>) f) =>
    ((json as List?) ?? const [])
        .map((e) => f(e as Map<String, dynamic>))
        .toList();

List<String> _textos(Object? json) =>
    ((json as List?) ?? const []).cast<String>();

// ---------------------------------------------------------------------------
// Visuais (desenhos que acompanham perguntas e cartões)

sealed class Visual {
  const Visual();

  factory Visual.fromJson(Map<String, dynamic> j) {
    switch (j['tipo']) {
      case 'svg':
        return VisualSvg([j['svg'] as String]);
      case 'svgs':
        return VisualSvg(_textos(j['svgs']));
      case 'emoji':
        return VisualEmoji(j['texto'] as String, (j['tamanho'] as num).toDouble());
      case 'caixa':
        return VisualCaixa(j['texto'] as String, j['estilo'] as String);
      case 'comparar':
        return VisualComparar([
          for (final i in j['itens'] as List)
            (n: i['n'] as int, d: i['d'] as int, svg: i['svg'] as String)
        ]);
      case 'grupos':
        return VisualGrupos(j['n'] as int, j['tamanho'] as int);
      case 'tabuada':
        return VisualTabuada(j['d'] as int, j['n'] as int);
      case 'dinheiro':
        return VisualDinheiro((j['valores'] as List).cast<int>());
      case 'valorPosicional':
        return VisualValorPosicional(_textos(j['numeros']));
    }
    throw FormatException('Visual desconhecido: ${j['tipo']}');
  }
}

class VisualSvg extends Visual {
  final List<String> svgs;
  const VisualSvg(this.svgs);
}

class VisualEmoji extends Visual {
  final String texto;
  final double tamanho;
  const VisualEmoji(this.texto, this.tamanho);
}

/// Caixa de texto: 'texto' (texto para leitura), 'poema' ou 'destaque'.
class VisualCaixa extends Visual {
  final String texto;
  final String estilo;
  const VisualCaixa(this.texto, this.estilo);
}

class VisualComparar extends Visual {
  final List<({int n, int d, String svg})> itens;
  const VisualComparar(this.itens);
}

class VisualGrupos extends Visual {
  final int n;
  final int tamanho;
  const VisualGrupos(this.n, this.tamanho);
}

class VisualTabuada extends Visual {
  final int d;
  final int n;
  const VisualTabuada(this.d, this.n);
}

/// Valores em centavos (ex.: 200 = nota de R$ 2).
class VisualDinheiro extends Visual {
  final List<int> valores;
  const VisualDinheiro(this.valores);
}

class VisualValorPosicional extends Visual {
  final List<String> numeros;
  const VisualValorPosicional(this.numeros);
}

List<Visual> _visuais(Object? j) => _lista(j, Visual.fromJson);

// ---------------------------------------------------------------------------
// Exercícios
//
// Textos usam uma marcação simples: **negrito**, quebras de linha com \n,
// [[3/4]] para frações e {nome} para o nome da criança.

sealed class Exercicio {
  final String pergunta;
  final String? explicacao;
  const Exercicio(this.pergunta, this.explicacao);

  factory Exercicio.fromJson(Map<String, dynamic> j) {
    final p = j['pergunta'] as String;
    final e = j['explicacao'] as String?;
    switch (j['tipo']) {
      case 'escolha':
        return Escolha(
          pergunta: p,
          explicacao: e,
          opcoes: _textos(j['opcoes']),
          correta: (j['correta'] as int?) ?? 0,
          embaralhar: (j['embaralhar'] as bool?) ?? true,
          visuais: _visuais(j['visuais']),
          dica: j['dica'] as String?,
          dicaVisuais: _visuais(j['dicaVisuais']),
        );
      case 'verdadeiroFalso':
        return VerdadeiroFalso(p, e, j['resposta'] as bool);
      case 'completar':
        return Completar(p, e, _textos(j['opcoes']));
      case 'ordenar':
        return Ordenar(p, e, _textos(j['itens']));
      case 'ligar':
        return Ligar(p, [
          for (final par in j['pares'] as List)
            ((par as List)[0] as String, par[1] as String)
        ]);
      case 'separar':
        return Separar(p, e, _textos(j['grupos']), [
          for (final i in j['itens'] as List)
            (texto: i['texto'] as String, grupo: i['grupo'] as int)
        ]);
    }
    throw FormatException('Exercício desconhecido: ${j['tipo']}');
  }
}

/// Múltipla escolha. `opcoes[correta]` é a certa.
class Escolha extends Exercicio {
  final List<String> opcoes;
  final int correta;
  final bool embaralhar;
  final List<Visual> visuais;
  final String? dica;
  final List<Visual> dicaVisuais;

  const Escolha({
    required String pergunta,
    String? explicacao,
    required this.opcoes,
    this.correta = 0,
    this.embaralhar = true,
    this.visuais = const [],
    this.dica,
    this.dicaVisuais = const [],
  }) : super(pergunta, explicacao);

  String get respostaCerta => opcoes[correta];
}

class VerdadeiroFalso extends Exercicio {
  final bool resposta;
  const VerdadeiroFalso(super.pergunta, super.explicacao, this.resposta);
}

/// Frase com ___ ; `opcoes[0]` é a certa.
class Completar extends Exercicio {
  final List<String> opcoes;
  const Completar(super.pergunta, super.explicacao, this.opcoes);
}

/// `itens` já está na ordem certa.
class Ordenar extends Exercicio {
  final List<String> itens;
  const Ordenar(super.pergunta, super.explicacao, this.itens);
}

class Ligar extends Exercicio {
  final List<(String, String)> pares;
  const Ligar(String pergunta, this.pares) : super(pergunta, null);
}

class Separar extends Exercicio {
  final List<String> grupos;
  final List<({String texto, int grupo})> itens;
  const Separar(super.pergunta, super.explicacao, this.grupos, this.itens);
}

// ---------------------------------------------------------------------------
// Estrutura

class CartaoBriefing {
  final String emoji;
  final String texto;
  final List<Visual> visuais;
  const CartaoBriefing(this.emoji, this.texto, this.visuais);

  factory CartaoBriefing.fromJson(Map<String, dynamic> j) => CartaoBriefing(
      j['emoji'] as String, j['texto'] as String, _visuais(j['visuais']));
}

class Missao {
  final String id;
  final String titulo;
  final String emoji;
  final String? descricao;
  final List<CartaoBriefing> briefing;
  final List<Exercicio> exercicios;
  final List<Exercicio> exerciciosDesafio;
  final bool geradas;

  const Missao({
    required this.id,
    required this.titulo,
    required this.emoji,
    this.descricao,
    this.briefing = const [],
    this.exercicios = const [],
    this.exerciciosDesafio = const [],
    this.geradas = false,
  });

  /// Missão ainda sem perguntas (só o modelo da BNCC).
  bool get emBreve => exercicios.isEmpty;

  factory Missao.fromJson(Map<String, dynamic> j) => Missao(
        id: j['id'] as String,
        titulo: j['titulo'] as String,
        emoji: j['emoji'] as String,
        descricao: j['descricao'] as String?,
        briefing: _lista(j['briefing'], CartaoBriefing.fromJson),
        exercicios: _lista(j['exercicios'], Exercicio.fromJson),
        exerciciosDesafio: _lista(j['exerciciosDesafio'], Exercicio.fromJson),
        geradas: (j['geradas'] as bool?) ?? false,
      );
}

class Setor {
  final String id;
  final String titulo;
  final String subtitulo;
  final List<Missao> missoes;

  const Setor(this.id, this.titulo, this.subtitulo, this.missoes);

  factory Setor.fromJson(Map<String, dynamic> j) => Setor(
        j['id'] as String,
        j['titulo'] as String,
        (j['subtitulo'] as String?) ?? '',
        _lista(j['missoes'], Missao.fromJson),
      );
}

class Planeta {
  final String id;
  final String disciplina;
  final String nomeCurto;
  final String nome;
  final String emoji;
  final Color cor;
  final Color corEscura;
  final Color corClara;
  final String chefaoEmoji;
  final String chefaoNome;
  final List<String> decoracao;
  final List<Setor> setores;

  const Planeta({
    required this.id,
    required this.disciplina,
    required this.nomeCurto,
    required this.nome,
    required this.emoji,
    required this.cor,
    required this.corEscura,
    required this.corClara,
    required this.chefaoEmoji,
    required this.chefaoNome,
    required this.decoracao,
    required this.setores,
  });

  Iterable<Missao> get missoes => setores.expand((s) => s.missoes);

  factory Planeta.fromJson(Map<String, dynamic> j) => Planeta(
        id: j['id'] as String,
        disciplina: j['disciplina'] as String,
        nomeCurto: j['nomeCurto'] as String,
        nome: j['nome'] as String,
        emoji: j['emoji'] as String,
        cor: corHex(j['cor'] as String),
        corEscura: corHex(j['corEscura'] as String),
        corClara: corHex(j['corClara'] as String),
        chefaoEmoji: j['chefao']['emoji'] as String,
        chefaoNome: j['chefao']['nome'] as String,
        decoracao: _textos(j['decoracao']),
        setores: _lista(j['setores'], Setor.fromJson),
      );
}

class BimestreConteudo {
  final int numero;
  final String titulo;
  final List<Planeta> planetas;

  const BimestreConteudo(this.numero, this.titulo, this.planetas);

  factory BimestreConteudo.fromJson(Map<String, dynamic> j) => BimestreConteudo(
        j['numero'] as int,
        j['titulo'] as String,
        _lista(j['planetas'], Planeta.fromJson),
      );
}

class ConteudoAno {
  final int ano;
  final String titulo;
  final List<BimestreConteudo> bimestres;

  /// Dia da semana (1 = segunda) → ids de disciplina (ex.: 'portugues').
  final Map<int, List<String>> rodizio;

  const ConteudoAno(this.ano, this.titulo, this.bimestres, this.rodizio);

  BimestreConteudo? bimestre(int numero) {
    for (final b in bimestres) {
      if (b.numero == numero) return b;
    }
    return null;
  }

  factory ConteudoAno.fromJson(Map<String, dynamic> j) {
    const dias = ['segunda', 'terca', 'quarta', 'quinta', 'sexta'];
    final r = (j['rodizioDiario'] as Map<String, dynamic>?) ?? const {};
    return ConteudoAno(
      j['ano'] as int,
      j['titulo'] as String,
      _lista(j['bimestres'], BimestreConteudo.fromJson)
        ..sort((a, b) => a.numero.compareTo(b.numero)),
      {
        for (var i = 0; i < dias.length; i++)
          if (r[dias[i]] != null) i + 1: _textos(r[dias[i]]),
      },
    );
  }
}

// ---------------------------------------------------------------------------
// Níveis de dificuldade

class Nivel {
  final String id;
  final String nome;
  final String emoji;
  final Color cor;
  final String descricao;
  final int perguntasMissao;
  final int perguntasRevisao;
  final int perguntasChefao;
  final int opcoes;
  final int itensSeparar;
  final bool dicas;
  final int tempoSegundos;
  final double multiplicador;
  final bool desafio;

  const Nivel({
    required this.id,
    required this.nome,
    required this.emoji,
    required this.cor,
    required this.descricao,
    required this.perguntasMissao,
    required this.perguntasRevisao,
    required this.perguntasChefao,
    required this.opcoes,
    required this.itensSeparar,
    required this.dicas,
    required this.tempoSegundos,
    required this.multiplicador,
    required this.desafio,
  });

  factory Nivel.fromJson(Map<String, dynamic> j) => Nivel(
        id: j['id'] as String,
        nome: j['nome'] as String,
        emoji: j['emoji'] as String,
        cor: corHex(j['cor'] as String),
        descricao: j['descricao'] as String,
        perguntasMissao: j['perguntasMissao'] as int,
        perguntasRevisao: j['perguntasRevisao'] as int,
        perguntasChefao: j['perguntasChefao'] as int,
        opcoes: j['opcoes'] as int,
        itensSeparar: j['itensSeparar'] as int,
        dicas: j['dicas'] as bool,
        tempoSegundos: j['tempoSegundos'] as int,
        multiplicador: (j['multiplicador'] as num).toDouble(),
        desafio: j['desafio'] as bool,
      );
}
