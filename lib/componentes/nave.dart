import 'dart:math';

import 'package:material_ui/material_ui.dart';

/// Desenho da Nave Gatística. Peças construídas aparecem coloridas; as que
/// faltam aparecem como contorno apagado (se `fantasmas`), para a criança
/// ver o que ainda falta.
class NaveGatistica extends StatelessWidget {
  final Set<String> pecas;
  final double tamanho;
  final bool fantasmas;
  final String? destaque;

  const NaveGatistica({
    super.key,
    required this.pecas,
    this.tamanho = 200,
    this.fantasmas = true,
    this.destaque,
  });

  @override
  Widget build(BuildContext context) => Semantics(
        label: 'Nave Gatística com ${pecas.length} peças',
        child: CustomPaint(
          size: Size(tamanho, tamanho * 1.2),
          painter: _PintorNave(pecas, fantasmas, destaque),
        ),
      );
}

class _PintorNave extends CustomPainter {
  final Set<String> pecas;
  final bool fantasmas;
  final String? destaque;
  _PintorNave(this.pecas, this.fantasmas, this.destaque);

  @override
  void paint(Canvas canvas, Size size) {
    final u = size.width / 100;
    canvas.save();
    canvas.scale(u);

    final fantasma = Paint()
      ..color = Colors.white.withValues(alpha: 0.22)
      ..style = PaintingStyle.stroke
      ..strokeWidth = 0.9;

    void parte(String id, void Function(bool feita) desenhar) {
      final feita = pecas.contains(id);
      if (!feita && !fantasmas) return;
      desenhar(feita);
      if (destaque == id) {
        // brilho na peça recém-construída
        canvas.drawCircle(
            const Offset(50, 60),
            52,
            Paint()
              ..color = const Color(0x33FFE066)
              ..maskFilter = const MaskFilter.blur(BlurStyle.normal, 6));
      }
    }

    Paint cheio(Color c) => Paint()..color = c;
    Paint traco(Color c, double w) => Paint()
      ..color = c
      ..style = PaintingStyle.stroke
      ..strokeWidth = w
      ..strokeCap = StrokeCap.round;

    void forma(Path path, bool feita, Color cor, {Color? borda}) {
      if (feita) {
        canvas.drawPath(path, cheio(cor));
        if (borda != null) canvas.drawPath(path, traco(borda, 1.2));
      } else {
        canvas.drawPath(path, fantasma);
      }
    }

    // Escudo (bolha atrás de tudo)
    parte('escudo', (f) {
      if (f) {
        canvas.drawCircle(const Offset(50, 60), 48, cheio(const Color(0x1A7FD3FF)));
        canvas.drawCircle(const Offset(50, 60), 48, traco(const Color(0x997FD3FF), 1.4));
      } else {
        canvas.drawCircle(const Offset(50, 60), 48, fantasma);
      }
    });

    // Painéis solares
    for (final lado in [-1, 1]) {
      parte('paineis', (f) {
        final x = lado < 0 ? 1.0 : 85.0;
        final r = RRect.fromRectAndRadius(Rect.fromLTWH(x, 64, 14, 9), const Radius.circular(1.5));
        if (f) {
          canvas.drawRRect(r, cheio(const Color(0xFF2B6CD9)));
          final grade = traco(const Color(0xFF9CC4FF), 0.6);
          canvas.drawLine(Offset(x + 4.7, 64), Offset(x + 4.7, 73), grade);
          canvas.drawLine(Offset(x + 9.3, 64), Offset(x + 9.3, 73), grade);
          canvas.drawLine(Offset(x, 68.5), Offset(x + 14, 68.5), grade);
        } else {
          canvas.drawRRect(r, fantasma);
        }
      });
    }

    // Propulsores nas pontas das asas
    for (final lado in [-1, 1]) {
      parte('propulsores', (f) {
        final x = lado < 0 ? 10.0 : 84.0;
        final r = RRect.fromRectAndRadius(Rect.fromLTWH(x, 76, 6, 15), const Radius.circular(3));
        if (f) {
          canvas.drawRRect(r, cheio(const Color(0xFF8A90B8)));
          final chama = Path()
            ..moveTo(x + 1, 91)
            ..lineTo(x + 3, 98)
            ..lineTo(x + 5, 91)
            ..close();
          canvas.drawPath(chama, cheio(const Color(0xFF7FD3FF)));
        } else {
          canvas.drawRRect(r, fantasma);
        }
      });
    }

    // Asas
    parte('asaEsquerda', (f) {
      final p = Path()
        ..moveTo(35, 56)
        ..lineTo(13, 82)
        ..lineTo(14, 86)
        ..lineTo(35, 80)
        ..close();
      forma(p, f, const Color(0xFFFF8FB1), borda: const Color(0xFFD9577F));
    });
    parte('asaDireita', (f) {
      final p = Path()
        ..moveTo(65, 56)
        ..lineTo(87, 82)
        ..lineTo(86, 86)
        ..lineTo(65, 80)
        ..close();
      forma(p, f, const Color(0xFFFF8FB1), borda: const Color(0xFFD9577F));
    });

    // Cauda de gato
    parte('cauda', (f) {
      final p = Path()
        ..moveTo(62, 84)
        ..quadraticBezierTo(82, 96, 74, 112)
        ..quadraticBezierTo(71, 117, 68, 113);
      canvas.drawPath(p, f ? traco(const Color(0xFFB79CFF), 3.4) : fantasma);
    });

    // Motor e chama
    parte('motor', (f) {
      final bocal = Path()
        ..moveTo(40, 82)
        ..lineTo(60, 82)
        ..lineTo(56, 90)
        ..lineTo(44, 90)
        ..close();
      forma(bocal, f, const Color(0xFF6B7096));
      if (f) {
        final chama = Path()
          ..moveTo(44, 90)
          ..quadraticBezierTo(50, 116, 56, 90)
          ..close();
        canvas.drawPath(chama, cheio(const Color(0xFFFF9F1C)));
        final miolo = Path()
          ..moveTo(47, 90)
          ..quadraticBezierTo(50, 104, 53, 90)
          ..close();
        canvas.drawPath(miolo, cheio(const Color(0xFFFFE066)));
      }
    });

    // Casco
    parte('casco', (f) {
      final p = Path()
        ..moveTo(50, 12)
        ..cubicTo(67, 22, 70, 52, 66, 82)
        ..lineTo(34, 82)
        ..cubicTo(30, 52, 33, 22, 50, 12)
        ..close();
      if (f) {
        canvas.drawPath(
            p,
            Paint()
              ..shader = const LinearGradient(
                colors: [Color(0xFFE9E4FF), Color(0xFFB7A8F5)],
              ).createShader(const Rect.fromLTWH(30, 12, 40, 70)));
        canvas.drawPath(p, traco(const Color(0xFF7C5CFF), 1.4));
      } else {
        canvas.drawPath(p, fantasma);
      }
    });

    // Orelhas-antena
    parte('orelhas', (f) {
      final esq = Path()
        ..moveTo(40, 24)
        ..lineTo(36, 6)
        ..lineTo(48, 16)
        ..close();
      final dir = Path()
        ..moveTo(60, 24)
        ..lineTo(64, 6)
        ..lineTo(52, 16)
        ..close();
      forma(esq, f, const Color(0xFFB7A8F5), borda: const Color(0xFF7C5CFF));
      forma(dir, f, const Color(0xFFB7A8F5), borda: const Color(0xFF7C5CFF));
      if (f) {
        canvas.drawCircle(const Offset(36, 6), 1.8, cheio(const Color(0xFFFF4B8B)));
        canvas.drawCircle(const Offset(64, 6), 1.8, cheio(const Color(0xFFFF4B8B)));
      }
    });

    // Anel de dobra
    parte('anel', (f) {
      final r = Rect.fromCenter(center: const Offset(50, 62), width: 92, height: 16);
      if (f) {
        canvas.drawOval(r, traco(const Color(0xFFFFC800), 2.4));
        canvas.drawOval(r.deflate(2.5), traco(const Color(0x66FFC800), 1));
      } else {
        canvas.drawOval(r, fantasma);
      }
    });

    // Bandeira
    parte('bandeira', (f) {
      if (f) {
        canvas.drawLine(const Offset(50, 13), const Offset(50, 0), traco(const Color(0xFFDDDDDD), 1));
        final b = Path()
          ..moveTo(50, 0.5)
          ..lineTo(61, 3)
          ..lineTo(50, 6)
          ..close();
        canvas.drawPath(b, cheio(const Color(0xFFFF4B4B)));
        canvas.drawCircle(const Offset(54, 3.2), 1, cheio(Colors.white));
      } else {
        canvas.drawLine(const Offset(50, 13), const Offset(50, 0), fantasma);
      }
    });

    // Radar
    parte('radar', (f) {
      final arco = Rect.fromCircle(center: const Offset(70, 36), radius: 6);
      if (f) {
        canvas.drawLine(const Offset(64, 40), const Offset(70, 36), traco(const Color(0xFFAAAAAA), 1));
        canvas.drawArc(arco, -pi * 0.9, pi * 0.9, false, traco(const Color(0xFF19B394), 2));
        canvas.drawCircle(const Offset(70, 36), 1.2, cheio(const Color(0xFF19B394)));
      } else {
        canvas.drawArc(arco, -pi * 0.9, pi * 0.9, false, fantasma);
      }
    });

    // Cabine com a silhueta de um gatinho
    parte('cabine', (f) {
      if (f) {
        canvas.drawCircle(const Offset(50, 37), 9, cheio(const Color(0xFF7FD3FF)));
        canvas.drawCircle(const Offset(50, 37), 9, traco(const Color(0xFF1C8FE0), 1.2));
        final gato = Path()
          ..moveTo(45, 42)
          ..lineTo(45, 34)
          ..lineTo(46.5, 31)
          ..lineTo(48, 34)
          ..lineTo(52, 34)
          ..lineTo(53.5, 31)
          ..lineTo(55, 34)
          ..lineTo(55, 42)
          ..close();
        canvas.drawPath(gato, cheio(const Color(0xFF233070)));
        canvas.drawCircle(const Offset(48, 37), 0.8, cheio(const Color(0xFFB9D84A)));
        canvas.drawCircle(const Offset(52, 37), 0.8, cheio(const Color(0xFFB9D84A)));
        canvas.drawCircle(const Offset(47, 34), 2, cheio(const Color(0x66FFFFFF)));
      } else {
        canvas.drawCircle(const Offset(50, 37), 9, fantasma);
      }
    });

    // Faróis olho-de-gato
    parte('farois', (f) {
      for (final x in [43.0, 57.0]) {
        if (f) {
          canvas.drawOval(Rect.fromCenter(center: Offset(x, 52), width: 6, height: 5),
              cheio(const Color(0xFFFFE066)));
          canvas.drawOval(Rect.fromCenter(center: Offset(x, 52), width: 1.6, height: 4.4),
              cheio(const Color(0xFF3C3C3C)));
        } else {
          canvas.drawOval(Rect.fromCenter(center: Offset(x, 52), width: 6, height: 5), fantasma);
        }
      }
    });

    // Núcleo de salto
    parte('nucleo', (f) {
      if (f) {
        canvas.drawCircle(
            const Offset(50, 64),
            6,
            Paint()
              ..shader = const RadialGradient(
                colors: [Color(0xFFFFFFFF), Color(0xFFCE82FF), Color(0xFF5A3FD6)],
              ).createShader(Rect.fromCircle(center: const Offset(50, 64), radius: 6)));
      } else {
        canvas.drawCircle(const Offset(50, 64), 6, fantasma);
      }
    });

    // Janelas
    parte('janelas', (f) {
      for (final x in [41.0, 59.0]) {
        if (f) {
          canvas.drawCircle(Offset(x, 74), 2.6, cheio(const Color(0xFF7FD3FF)));
          canvas.drawCircle(Offset(x, 74), 2.6, traco(const Color(0xFF5A3FD6), 0.8));
        } else {
          canvas.drawCircle(Offset(x, 74), 2.6, fantasma);
        }
      }
    });

    canvas.restore();
  }

  @override
  bool shouldRepaint(_PintorNave old) =>
      old.pecas.length != pecas.length || old.destaque != destaque || old.fantasmas != fantasmas;
}
