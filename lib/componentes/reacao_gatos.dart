import 'dart:math';

import 'package:material_ui/material_ui.dart';

const carinhasAcerto = ['😺', '😸', '😻', '😽'];
const carinhasErro = ['😿', '🙀', '😾'];

/// Carinhas de gato que pulam na tela a cada acerto ou erro.
/// Troque `disparo` (um contador) para disparar uma nova reação.
class ReacaoGatos extends StatefulWidget {
  final int disparo;
  final bool acerto;
  final Random aleatorio;
  const ReacaoGatos(
      {super.key, required this.disparo, required this.acerto, required this.aleatorio});

  @override
  State<ReacaoGatos> createState() => _ReacaoGatosState();
}

class _ReacaoGatosState extends State<ReacaoGatos> with SingleTickerProviderStateMixin {
  late final _anim =
      AnimationController(vsync: this, duration: const Duration(milliseconds: 1300));
  String _principal = '😺';
  List<({String e, double x, double atraso})> _pequenas = const [];

  @override
  void didUpdateWidget(ReacaoGatos old) {
    super.didUpdateWidget(old);
    if (widget.disparo != old.disparo && widget.disparo > 0) _disparar();
  }

  void _disparar() {
    final rnd = widget.aleatorio;
    final lista = widget.acerto ? carinhasAcerto : carinhasErro;
    _principal = lista[rnd.nextInt(lista.length)];
    _pequenas = [
      for (var i = 0; i < (widget.acerto ? 6 : 3); i++)
        (e: lista[rnd.nextInt(lista.length)], x: rnd.nextDouble() * 2 - 1, atraso: rnd.nextDouble() * 0.3)
    ];
    _anim.forward(from: 0);
  }

  @override
  void dispose() {
    _anim.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return IgnorePointer(
      child: AnimatedBuilder(
        animation: _anim,
        builder: (context, _) {
          final t = _anim.value;
          if (!_anim.isAnimating) return const SizedBox.shrink();
          // pulo: cresce rápido, balança e some
          final escala = t < 0.25
              ? Curves.elasticOut.transform(t / 0.25) * 1.0
              : 1.0 + sin(t * 14) * 0.03;
          final opacidade = t < 0.75 ? 1.0 : (1 - (t - 0.75) / 0.25);
          final balanco = widget.acerto ? sin(t * 10) * 0.12 : sin(t * 30) * 0.08 * (1 - t);
          return Stack(children: [
            for (final p in _pequenas)
              Builder(builder: (context) {
                final tt = ((t - p.atraso) / (1 - p.atraso)).clamp(0.0, 1.0);
                return Align(
                  alignment: Alignment(p.x * 0.8, 0.3 - tt * (widget.acerto ? 1.2 : 0.4)),
                  child: Opacity(
                    opacity: (1 - tt).clamp(0.0, 1.0),
                    child: Text(p.e, style: const TextStyle(fontSize: 34)),
                  ),
                );
              }),
            Align(
              alignment: const Alignment(0, -0.35),
              child: Opacity(
                opacity: opacidade.clamp(0.0, 1.0),
                child: Transform.rotate(
                  angle: balanco,
                  child: Transform.scale(
                    scale: escala,
                    child: Text(_principal,
                        key: const Key('reacaoGato'), style: const TextStyle(fontSize: 120)),
                  ),
                ),
              ),
            ),
          ]);
        },
      ),
    );
  }
}
