import 'package:material_ui/material_ui.dart';

/// Mostra textos do conteúdo com a marcação simples:
/// **negrito**, \n, [[3/4]] (fração empilhada) e {nome}.
class TextoRico extends StatelessWidget {
  final String texto;
  final String nome;
  final TextStyle? estilo;
  final TextAlign alinhamento;

  const TextoRico(
    this.texto, {
    super.key,
    this.nome = 'Astronauta',
    this.estilo,
    this.alinhamento = TextAlign.start,
  });

  @override
  Widget build(BuildContext context) {
    final base = DefaultTextStyle.of(context).style.merge(estilo);
    return Text.rich(
      TextSpan(style: base, children: spans(texto, nome, base)),
      textAlign: alinhamento,
    );
  }

  static final _re = RegExp(r'\*\*|\[\[(\d+)/(\d+)\]\]');

  static List<InlineSpan> spans(String texto, String nome, TextStyle base) {
    texto = texto.replaceAll('{nome}', nome);
    final out = <InlineSpan>[];
    var negrito = false;
    var i = 0;
    for (final m in _re.allMatches(texto)) {
      if (m.start > i) {
        out.add(TextSpan(
            text: texto.substring(i, m.start),
            style: negrito ? const TextStyle(fontWeight: FontWeight.w900) : null));
      }
      if (m.group(0) == '**') {
        negrito = !negrito;
      } else {
        out.add(WidgetSpan(
          alignment: PlaceholderAlignment.middle,
          child: Fracao(m.group(1)!, m.group(2)!,
              tamanho: (base.fontSize ?? 16) * 0.95, cor: base.color),
        ));
      }
      i = m.end;
    }
    if (i < texto.length) {
      out.add(TextSpan(
          text: texto.substring(i),
          style: negrito ? const TextStyle(fontWeight: FontWeight.w900) : null));
    }
    return out;
  }

  /// Versão para leitura em voz alta: tira a marcação e lê as frações.
  static String paraFala(String texto, String nome) {
    const partes = {
      2: ['meio', 'meios'],
      3: ['terço', 'terços'],
      4: ['quarto', 'quartos'],
      5: ['quinto', 'quintos'],
      6: ['sexto', 'sextos'],
      7: ['sétimo', 'sétimos'],
      8: ['oitavo', 'oitavos'],
      9: ['nono', 'nonos'],
      10: ['décimo', 'décimos'],
      100: ['centésimo', 'centésimos'],
    };
    return texto
        .replaceAll('{nome}', nome)
        .replaceAll('**', '')
        .replaceAll('___', ', lacuna, ')
        .replaceAllMapped(RegExp(r'\[\[(\d+)/(\d+)\]\]'), (m) {
      final n = int.parse(m[1]!), d = int.parse(m[2]!);
      final p = partes[d];
      if (p == null) return ' $n sobre $d ';
      return ' $n ${n == 1 ? p[0] : p[1]} ';
    });
  }
}

class Fracao extends StatelessWidget {
  final String numerador;
  final String denominador;
  final double tamanho;
  final Color? cor;

  const Fracao(this.numerador, this.denominador,
      {super.key, this.tamanho = 16, this.cor});

  @override
  Widget build(BuildContext context) {
    final st = TextStyle(
        fontSize: tamanho, fontWeight: FontWeight.w900, height: 1.05, color: cor);
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 3),
      child: IntrinsicWidth(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Text(numerador, style: st, textAlign: TextAlign.center),
            Container(height: 2.5, color: cor ?? Colors.black87),
            Text(denominador, style: st, textAlign: TextAlign.center),
          ],
        ),
      ),
    );
  }
}
