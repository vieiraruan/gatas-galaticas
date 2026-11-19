import 'package:flutter_svg/flutter_svg.dart';
import 'package:material_ui/material_ui.dart';

import '../modelos/conteudo.dart';
import 'texto_rico.dart';

/// Desenha os visuais que acompanham perguntas e cartões.
class Visuais extends StatelessWidget {
  final List<Visual> visuais;
  final String nome;
  const Visuais(this.visuais, {super.key, this.nome = 'Astronauta'});

  @override
  Widget build(BuildContext context) {
    if (visuais.isEmpty) return const SizedBox.shrink();
    return Padding(
      padding: const EdgeInsets.only(top: 14, bottom: 4),
      child: Wrap(
        alignment: WrapAlignment.center,
        crossAxisAlignment: WrapCrossAlignment.center,
        spacing: 8,
        runSpacing: 8,
        children: [for (final v in visuais) _visual(v)],
      ),
    );
  }

  Widget _visual(Visual v) => switch (v) {
        VisualSvg(:final svgs) => Wrap(
            alignment: WrapAlignment.center,
            spacing: 6,
            runSpacing: 6,
            children: [for (final s in svgs) _Svg(s)],
          ),
        VisualEmoji(:final texto, :final tamanho) =>
          Text(texto, style: TextStyle(fontSize: tamanho)),
        VisualCaixa() => _Caixa(v, nome),
        VisualComparar(:final itens) => Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              for (final i in itens)
                Padding(
                  padding: const EdgeInsets.symmetric(vertical: 4),
                  child: Row(mainAxisSize: MainAxisSize.min, children: [
                    SizedBox(
                        width: 44,
                        child: Fracao('${i.n}', '${i.d}', tamanho: 20)),
                    const SizedBox(width: 8),
                    _Svg(i.svg),
                  ]),
                ),
            ],
          ),
        VisualGrupos() => _Grupos(v),
        VisualTabuada() => _Tabuada(v),
        VisualDinheiro(:final valores) => Wrap(
            alignment: WrapAlignment.center,
            crossAxisAlignment: WrapCrossAlignment.center,
            spacing: 8,
            runSpacing: 8,
            children: [for (final c in valores) _Dinheiro(c)],
          ),
        VisualValorPosicional(:final numeros) => _ValorPosicional(numeros),
      };
}

class _Svg extends StatelessWidget {
  final String svg;
  const _Svg(this.svg);

  @override
  Widget build(BuildContext context) {
    // Os desenhos têm largura fixa; encolhem em telas estreitas.
    return ConstrainedBox(
      constraints: const BoxConstraints(maxWidth: 320),
      child: SvgPicture.string(svg, fit: BoxFit.contain),
    );
  }
}

class _Caixa extends StatelessWidget {
  final VisualCaixa caixa;
  final String nome;
  const _Caixa(this.caixa, this.nome);

  @override
  Widget build(BuildContext context) {
    final (fundo, borda, italico, centro) = switch (caixa.estilo) {
      'poema' => (const Color(0xFFFFF8E6), const Color(0xFFFFC800), true, false),
      'destaque' => (const Color(0xFFF7F4FF), null, false, true),
      _ => (const Color(0xFFF3F8FF), const Color(0xFF1C8FE0), false, false),
    };
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.fromLTRB(18, 14, 18, 14),
      decoration: BoxDecoration(
        color: fundo,
        borderRadius: BorderRadius.circular(16),
        border: borda == null ? null : Border(left: BorderSide(color: borda, width: 6)),
      ),
      child: TextoRico(
        caixa.texto,
        nome: nome,
        alinhamento: centro ? TextAlign.center : TextAlign.start,
        estilo: TextStyle(
          fontSize: centro ? 22 : 18,
          height: 1.5,
          fontStyle: italico ? FontStyle.italic : FontStyle.normal,
          color: const Color(0xFF3C3C3C),
        ),
      ),
    );
  }
}

class _Grupos extends StatelessWidget {
  final VisualGrupos g;
  const _Grupos(this.g);

  @override
  Widget build(BuildContext context) {
    final cheios = g.n ~/ g.tamanho, resto = g.n % g.tamanho;
    Widget caixa(int bolinhas, Color cor) => Container(
          width: 66,
          padding: const EdgeInsets.all(5),
          decoration: BoxDecoration(
            border: Border.all(color: cor, width: 2),
            borderRadius: BorderRadius.circular(10),
          ),
          child: Wrap(spacing: 3, runSpacing: 3, children: [
            for (var i = 0; i < bolinhas; i++)
              Container(
                  width: 11,
                  height: 11,
                  decoration: BoxDecoration(color: cor, shape: BoxShape.circle)),
          ]),
        );
    const roxo = Color(0xFF7C6BF0), vermelho = Color(0xFFE5534B);
    return Column(mainAxisSize: MainAxisSize.min, children: [
      Wrap(alignment: WrapAlignment.center, spacing: 6, runSpacing: 6, children: [
        for (var i = 0; i < cheios; i++) caixa(g.tamanho, roxo),
        if (resto > 0) caixa(resto, vermelho),
      ]),
      const SizedBox(height: 6),
      Text(
        '$cheios ${cheios == 1 ? 'grupo' : 'grupos'} de ${g.tamanho}'
        '${resto > 0 ? ' e ${resto == 1 ? 'sobra' : 'sobram'} $resto' : ' e não sobra nada'}',
        style: const TextStyle(fontSize: 16),
      ),
    ]);
  }
}

class _Tabuada extends StatelessWidget {
  final VisualTabuada t;
  const _Tabuada(this.t);

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: 300,
      child: Wrap(
        children: [
          for (var i = 1; i <= 10; i++)
            Builder(builder: (_) {
              final p = t.d * i;
              final destaque = p <= t.n && t.d * (i + 1) > t.n;
              return Container(
                width: 150,
                padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 1),
                decoration: BoxDecoration(
                  color: destaque ? const Color(0xFF2FB36D) : null,
                  borderRadius: BorderRadius.circular(8),
                ),
                child: Opacity(
                  opacity: p <= t.n ? 1 : 0.35,
                  child: Text('${t.d} × $i = $p',
                      style: TextStyle(
                          fontSize: 17,
                          color: destaque ? Colors.white : null)),
                ),
              );
            }),
        ],
      ),
    );
  }
}

class _Dinheiro extends StatelessWidget {
  final int centavos;
  const _Dinheiro(this.centavos);

  @override
  Widget build(BuildContext context) {
    const tinta = Color(0xFF2B2350);
    if (centavos >= 200) {
      final cor = switch (centavos) {
        200 => const Color(0xFFBFE3F5),
        500 => const Color(0xFFD9C7F0),
        1000 => const Color(0xFFF7C3B5),
        _ => const Color(0xFFFBE39A),
      };
      return Container(
        width: 96,
        height: 50,
        alignment: Alignment.center,
        decoration: BoxDecoration(
          color: cor,
          borderRadius: BorderRadius.circular(8),
          border: Border.all(color: Colors.black26, width: 3),
        ),
        child: Text('R\$ ${centavos ~/ 100}',
            style: const TextStyle(
                fontSize: 19, fontWeight: FontWeight.w900, color: tinta)),
      );
    }
    final (tam, cor) = switch (centavos) {
      100 => (62.0, const Color(0xFFF2C94C)),
      50 => (56.0, const Color(0xFFD8D8D8)),
      25 => (52.0, const Color(0xFFF2C94C)),
      10 => (46.0, const Color(0xFFE8C25A)),
      _ => (42.0, const Color(0xFFD9925B)),
    };
    return Container(
      width: tam,
      height: tam,
      alignment: Alignment.center,
      decoration: BoxDecoration(
        color: cor,
        shape: BoxShape.circle,
        border: Border.all(color: Colors.black26, width: 3),
      ),
      child: Column(mainAxisSize: MainAxisSize.min, children: [
        Text(centavos == 100 ? '1' : '$centavos',
            style: const TextStyle(
                fontSize: 15, fontWeight: FontWeight.w900, color: tinta, height: 1)),
        Text(centavos == 100 ? 'real' : 'centavos',
            style: const TextStyle(fontSize: 8, color: tinta, height: 1)),
      ]),
    );
  }
}

class _ValorPosicional extends StatelessWidget {
  final List<String> numeros;
  const _ValorPosicional(this.numeros);

  @override
  Widget build(BuildContext context) {
    const borda = BorderSide(color: Color(0xFFD9D2FF), width: 2);
    Widget cab(String t) => Container(
          color: const Color(0xFFEDE9FF),
          padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
          child: Text(t, textAlign: TextAlign.center, style: const TextStyle(fontSize: 12)),
        );
    Widget cel(String t) => Container(
          decoration: const BoxDecoration(
              border: Border(top: borda, bottom: borda, left: borda, right: borda)),
          padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
          child: Text(t, textAlign: TextAlign.center, style: const TextStyle(fontSize: 22)),
        );
    return Table(
      defaultColumnWidth: const IntrinsicColumnWidth(),
      children: [
        TableRow(children: [cab('Unidades'), const SizedBox(), cab('décimos'), cab('centésimos')]),
        for (final n in numeros)
          () {
            final partes = n.split(',');
            final f = partes.length > 1 ? partes[1] : '';
            return TableRow(children: [
              cel(partes[0]),
              const Padding(
                padding: EdgeInsets.symmetric(horizontal: 2),
                child: Text(',', textAlign: TextAlign.center, style: TextStyle(fontSize: 28)),
              ),
              cel(f.isNotEmpty ? f[0] : ''),
              cel(f.length > 1 ? f[1] : ''),
            ]);
          }(),
      ],
    );
  }
}
