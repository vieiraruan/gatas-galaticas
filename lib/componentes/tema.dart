import 'package:material_ui/material_ui.dart';

/// Cores e estilos da Galáxia do Saber.
abstract final class Cores {
  static const espaco = Color(0xFF0B1030);
  static const espacoMeio = Color(0xFF1A1F5C);
  static const roxo = Color(0xFF7C5CFF);
  static const roxoEscuro = Color(0xFF5A3FD6);
  static const ouro = Color(0xFFFFC800);
  static const ouroEscuro = Color(0xFFD9A400);
  static const ciano = Color(0xFF7FD3FF);
  static const tinta = Color(0xFF3C3C3C);
  static const apagado = Color(0xFF8A8A8A);
  static const linha = Color(0xFFE5E5E5);
  static const certo = Color(0xFF58CC02);
  static const certoClaro = Color(0xFFD7FFB8);
  static const errado = Color(0xFFFF4B4B);
  static const erradoClaro = Color(0xFFFFDFE0);
  static const azulAcao = Color(0xFF1CB0F6);
  static const azulAcaoEscuro = Color(0xFF1899D6);
  static const textoClaro = Color(0xFFAEB6E8);
}

ThemeData temaGalaxia() {
  final base = ThemeData(
    useMaterial3: true,
    colorScheme: ColorScheme.fromSeed(
        seedColor: Cores.roxo, brightness: Brightness.light),
    scaffoldBackgroundColor: Cores.espaco,
  );
  return base.copyWith(
    textTheme: base.textTheme.apply(
      fontFamily: null,
      bodyColor: Cores.tinta,
      displayColor: Cores.tinta,
    ).copyWith(
      bodyMedium: base.textTheme.bodyMedium
          ?.copyWith(fontWeight: FontWeight.w700, fontSize: 16),
    ),
  );
}

/// Fundo estrelado do espaço.
class FundoEspacial extends StatelessWidget {
  final Widget child;
  const FundoEspacial({super.key, required this.child});

  @override
  Widget build(BuildContext context) {
    return DecoratedBox(
      decoration: const BoxDecoration(
        gradient: LinearGradient(
          begin: Alignment.topCenter,
          end: Alignment.bottomCenter,
          colors: [Cores.espaco, Cores.espacoMeio, Cores.espaco],
        ),
      ),
      child: CustomPaint(painter: _Estrelas(), child: child),
    );
  }
}

class _Estrelas extends CustomPainter {
  @override
  void paint(Canvas canvas, Size size) {
    final p = Paint()..color = Colors.white;
    // Pseudoaleatório fixo para as estrelas não pularem a cada quadro.
    var s = 7;
    double r() {
      s = (s * 1103515245 + 12345) & 0x7fffffff;
      return s / 0x7fffffff;
    }

    final n = (size.width * size.height / 5000).clamp(40, 400).toInt();
    for (var i = 0; i < n; i++) {
      p.color = Colors.white.withValues(alpha: 0.25 + r() * 0.6);
      canvas.drawCircle(
          Offset(r() * size.width, r() * size.height), 0.6 + r() * 1.4, p);
    }
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) => false;
}

/// Botão grosso com "degrau" embaixo, como na Galáxia.
class Botao3D extends StatefulWidget {
  final String texto;
  final VoidCallback? onPressed;
  final Color cor;
  final Color corSombra;
  final Color corTexto;
  final bool expandir;
  final double altura;

  const Botao3D({
    super.key,
    required this.texto,
    required this.onPressed,
    this.cor = Cores.azulAcao,
    this.corSombra = Cores.azulAcaoEscuro,
    this.corTexto = Colors.white,
    this.expandir = true,
    this.altura = 54,
  });

  const Botao3D.ouro({
    super.key,
    required this.texto,
    required this.onPressed,
    this.expandir = true,
    this.altura = 54,
  })  : cor = Cores.ouro,
        corSombra = Cores.ouroEscuro,
        corTexto = const Color(0xFF4A3500);

  const Botao3D.branco({
    super.key,
    required this.texto,
    required this.onPressed,
    this.expandir = true,
    this.altura = 54,
  })  : cor = Colors.white,
        corSombra = Cores.linha,
        corTexto = Cores.azulAcao;

  @override
  State<Botao3D> createState() => _Botao3DState();
}

class _Botao3DState extends State<Botao3D> {
  bool _apertado = false;

  @override
  Widget build(BuildContext context) {
    final ativo = widget.onPressed != null;
    final cor = ativo ? widget.cor : const Color(0xFFE5E5E5);
    final sombra = ativo ? widget.corSombra : const Color(0xFFCFCFCF);
    final desloc = _apertado ? 4.0 : 0.0;
    final botao = GestureDetector(
      onTapDown: ativo ? (_) => setState(() => _apertado = true) : null,
      onTapCancel: () => setState(() => _apertado = false),
      onTapUp: ativo
          ? (_) {
              setState(() => _apertado = false);
              widget.onPressed!();
            }
          : null,
      child: Semantics(
        button: true,
        enabled: ativo,
        label: widget.texto,
        child: SizedBox(
          height: widget.altura + 5,
          child: Stack(
            children: [
              Positioned(
                left: 0,
                right: 0,
                bottom: 0,
                height: widget.altura,
                child: DecoratedBox(
                  decoration: BoxDecoration(
                      color: sombra, borderRadius: BorderRadius.circular(16)),
                ),
              ),
              AnimatedPositioned(
                duration: const Duration(milliseconds: 60),
                left: 0,
                right: 0,
                top: desloc,
                height: widget.altura,
                child: Container(
                  alignment: Alignment.center,
                  padding: const EdgeInsets.symmetric(horizontal: 16),
                  decoration: BoxDecoration(
                    color: cor,
                    borderRadius: BorderRadius.circular(16),
                    border: widget.cor == Colors.white
                        ? Border.all(color: Cores.linha, width: 2)
                        : null,
                  ),
                  child: Text(
                    widget.texto,
                    textAlign: TextAlign.center,
                    style: TextStyle(
                      color: ativo ? widget.corTexto : const Color(0xFFAFAFAF),
                      fontSize: 17,
                      fontWeight: FontWeight.w900,
                      letterSpacing: 0.6,
                    ),
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
    return widget.expandir ? SizedBox(width: double.infinity, child: botao) : botao;
  }
}
