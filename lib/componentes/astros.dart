import 'dart:math';

import 'package:material_ui/material_ui.dart';

/// Desenhos de galáxia (espiral) e planeta (esfera com anel ou crateras),
/// gerados a partir de uma cor e de uma semente, para cada matéria e assunto
/// terem um visual próprio.
class DesenhoGalaxia extends StatelessWidget {
  final Color cor;
  final double tamanho;
  final String emoji;
  const DesenhoGalaxia({super.key, required this.cor, required this.emoji, this.tamanho = 90});

  @override
  Widget build(BuildContext context) => SizedBox(
        width: tamanho,
        height: tamanho,
        child: Stack(alignment: Alignment.center, children: [
          CustomPaint(size: Size.square(tamanho), painter: _PintorGalaxia(cor)),
          Text(emoji, style: TextStyle(fontSize: tamanho * 0.3)),
        ]),
      );
}

class _PintorGalaxia extends CustomPainter {
  final Color cor;
  _PintorGalaxia(this.cor);

  @override
  void paint(Canvas canvas, Size size) {
    final c = size.center(Offset.zero);
    final r = size.width / 2;
    canvas.drawCircle(
        c,
        r * 0.95,
        Paint()
          ..shader = RadialGradient(colors: [
            cor.withValues(alpha: 0.55),
            cor.withValues(alpha: 0.12),
            Colors.transparent,
          ], stops: const [0, 0.6, 1])
              .createShader(Rect.fromCircle(center: c, radius: r)));
    final rnd = Random(cor.toARGB32());
    for (var braco = 0; braco < 3; braco++) {
      for (var i = 0; i < 46; i++) {
        final t = i / 46;
        final ang = braco * 2 * pi / 3 + t * 3.6;
        final dist = r * (0.12 + t * 0.78);
        final jit = (rnd.nextDouble() - 0.5) * r * 0.12;
        final p = c + Offset(cos(ang) * (dist + jit), sin(ang) * (dist + jit) * 0.8);
        canvas.drawCircle(
            p,
            (1 - t) * r * 0.05 + 0.8,
            Paint()
              ..color = Color.lerp(Colors.white, cor, t)!.withValues(alpha: 0.9 - t * 0.5));
      }
    }
    canvas.drawCircle(
        c,
        r * 0.22,
        Paint()
          ..color = Colors.white.withValues(alpha: 0.85)
          ..maskFilter = MaskFilter.blur(BlurStyle.normal, r * 0.12));
  }

  @override
  bool shouldRepaint(_PintorGalaxia old) => old.cor != cor;
}

class DesenhoPlaneta extends StatelessWidget {
  final Color cor;
  final String semente;
  final double tamanho;
  final bool apagado;
  const DesenhoPlaneta(
      {super.key, required this.cor, required this.semente, this.tamanho = 70, this.apagado = false});

  @override
  Widget build(BuildContext context) => CustomPaint(
        size: Size.square(tamanho),
        painter: _PintorPlaneta(cor, semente.hashCode, apagado),
      );
}

class _PintorPlaneta extends CustomPainter {
  final Color base;
  final int semente;
  final bool apagado;
  _PintorPlaneta(this.base, this.semente, this.apagado);

  @override
  void paint(Canvas canvas, Size size) {
    final rnd = Random(semente);
    final hsl = HSLColor.fromColor(base);
    var cor = hsl
        .withHue((hsl.hue + rnd.nextInt(70) - 35) % 360)
        .withLightness((hsl.lightness + rnd.nextDouble() * 0.2 - 0.05).clamp(0.3, 0.7))
        .toColor();
    if (apagado) cor = Color.lerp(cor, const Color(0xFF555A80), 0.75)!;
    final c = size.center(Offset.zero);
    final r = size.width * 0.34;
    final temAnel = rnd.nextBool();
    final anel = Rect.fromCenter(center: c, width: r * 3, height: r * 0.9);
    final inclinacao = (rnd.nextDouble() - 0.5) * 0.6;
    final pincelAnel = Paint()
      ..color = Color.lerp(cor, Colors.white, 0.5)!.withValues(alpha: 0.9)
      ..style = PaintingStyle.stroke
      ..strokeWidth = r * 0.16;

    void desenharAnel(bool frente) {
      canvas.save();
      canvas.translate(c.dx, c.dy);
      canvas.rotate(inclinacao);
      canvas.translate(-c.dx, -c.dy);
      canvas.drawArc(anel, frente ? 0 : pi, pi, false, pincelAnel);
      canvas.restore();
    }

    if (temAnel) desenharAnel(false);
    final esfera = Rect.fromCircle(center: c, radius: r);
    canvas.drawCircle(
        c,
        r,
        Paint()
          ..shader = RadialGradient(
            center: const Alignment(-0.4, -0.4),
            colors: [Color.lerp(cor, Colors.white, 0.45)!, cor, Color.lerp(cor, Colors.black, 0.45)!],
            stops: const [0, 0.55, 1],
          ).createShader(esfera));
    canvas.save();
    canvas.clipPath(Path()..addOval(esfera));
    if (rnd.nextBool()) {
      // faixas
      for (var i = 0; i < 3; i++) {
        final y = c.dy - r + r * 2 * (0.25 + i * 0.22 + rnd.nextDouble() * 0.05);
        canvas.drawRect(Rect.fromLTWH(c.dx - r, y, r * 2, r * 0.14),
            Paint()..color = Colors.white.withValues(alpha: 0.16));
      }
    } else {
      // crateras
      for (var i = 0; i < 4; i++) {
        final p = c + Offset((rnd.nextDouble() - 0.5) * r * 1.3, (rnd.nextDouble() - 0.5) * r * 1.3);
        canvas.drawCircle(p, r * (0.1 + rnd.nextDouble() * 0.14),
            Paint()..color = Colors.black.withValues(alpha: 0.16));
      }
    }
    canvas.restore();
    if (temAnel) desenharAnel(true);
  }

  @override
  bool shouldRepaint(_PintorPlaneta old) =>
      old.base != base || old.semente != semente || old.apagado != apagado;
}
