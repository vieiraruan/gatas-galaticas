import 'dart:async';
import 'dart:math';

import 'package:flutter/scheduler.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:material_ui/material_ui.dart';

import '../componentes/nave.dart';
import '../componentes/tema.dart';
import '../logica/labirinto.dart';
import '../logica/minijogos.dart';
import '../logica/regras.dart';
import '../modelos/conteudo.dart';
import '../providers.dart';

/// Pausa entre missões: a criança escolhe um minijogo (todos opcionais).
Future<void> mostrarPausa(
  BuildContext context, {
  required String perfilId,
  required String planetaId,
  required int indice,
}) {
  return showModalBottomSheet<void>(
    context: context,
    backgroundColor: Cores.espacoMeio,
    isScrollControlled: true,
    shape: const RoundedRectangleBorder(
      borderRadius: BorderRadius.vertical(top: Radius.circular(24)),
    ),
    builder: (c) => SafeArea(
      child: SingleChildScrollView(
        padding: const EdgeInsets.fromLTRB(16, 16, 16, 10),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            const Text(
              '🛋️ Hora da pausa!',
              style: TextStyle(color: Colors.white, fontSize: 22, fontWeight: FontWeight.w900),
            ),
            const Text(
              'Escolha um jogo rápido para descansar a cabeça.',
              textAlign: TextAlign.center,
              style: TextStyle(color: Cores.textoClaro),
            ),
            const SizedBox(height: 12),
            for (final j in Minijogo.values)
              Card(
                color: Colors.white.withValues(alpha: 0.08),
                child: ListTile(
                  leading: Text(j.emoji, style: const TextStyle(fontSize: 30)),
                  title: Text(
                    j.nome,
                    style: const TextStyle(color: Colors.white, fontWeight: FontWeight.w900),
                  ),
                  subtitle: Text(j.descricao, style: const TextStyle(color: Cores.textoClaro)),
                  onTap: () {
                    Navigator.pop(c);
                    context.go(
                      j == Minijogo.labirinto
                          ? '/c/$perfilId/p/$planetaId/labirinto/$indice'
                          : '/c/$perfilId/p/$planetaId/pausa/${j.name}/$indice',
                    );
                  },
                ),
              ),
            TextButton(
              onPressed: () => Navigator.pop(c),
              child: const Text('Agora não', style: TextStyle(color: Cores.textoClaro)),
            ),
          ],
        ),
      ),
    ),
  );
}

/// A nave que a criança montou, já virada para a direita. Antes da
/// primeira peça, um foguete provisório.
Widget naveDaCrianca(Sessao s, double tamanho) {
  final pecas = s.progresso.pecas;
  if (pecas.isEmpty) {
    return Transform.rotate(
      angle: pi / 4,
      child: Text('🚀', style: TextStyle(fontSize: tamanho * 0.8, height: 1)),
    );
  }
  return Transform.rotate(
    angle: pi / 2,
    child: NaveGatistica(pecas: pecas, tamanho: tamanho, fantasmas: false),
  );
}

/// Um minijogo da pausa. `indice` é o nó (missão) que acabou de ser jogado.
class TelaMinijogo extends ConsumerStatefulWidget {
  final String perfilId;
  final String planetaId;
  final int indice;
  final Minijogo jogo;
  const TelaMinijogo({
    super.key,
    required this.perfilId,
    required this.planetaId,
    required this.indice,
    required this.jogo,
  });

  @override
  ConsumerState<TelaMinijogo> createState() => _TelaMinijogoState();
}

class _TelaMinijogoState extends ConsumerState<TelaMinijogo> {
  // Monta o jogo uma vez só: gravar a recompensa recarrega a sessão, e
  // isso não pode reiniciar a partida nem esconder o placar.
  Widget? _jogo;

  @override
  Widget build(BuildContext context) {
    final sessao = ref.watch(sessaoProvider(widget.perfilId));
    if (_jogo == null && sessao.hasValue) _jogo = _montar(sessao.value);
    return Scaffold(
      backgroundColor: Cores.espaco,
      body:
          _jogo ??
          (sessao.hasError
              ? Center(child: Text('Erro: ${sessao.error}'))
              : const Center(child: CircularProgressIndicator())),
    );
  }

  Widget _montar(Sessao? s) {
    final p = s?.planeta(widget.planetaId);
    if (s == null || p == null) {
      return const Center(
        child: Text('Jogo não encontrado.', style: TextStyle(color: Colors.white)),
      );
    }
    final r = s.regras(p);
    final i = widget.indice;
    final no = i >= 0 && i < r.nos.length ? r.nos[i] : null;
    final recentes = no == null ? const <Missao>[] : missoesDoNo(no);
    final ids = recentes.map((m) => m.id).toSet();
    final anteriores = [
      for (final pl in s.bimestre.planetas)
        for (final n in s.regras(pl).nos)
          if (n is NoMissao && s.regras(pl).estrelas(n) > 0 && !ids.contains(n.missao.id)) n.missao,
    ];
    final rnd = ref.read(aleatorioProvider);
    final desafios =
        desafiosDeLembranca(anteriores: anteriores, recentes: recentes, rnd: rnd, quantidade: 12)
            // Na cauda as respostas aparecem no mapa: só textos curtos.
            .where((d) => d.visuais.isEmpty && d.opcoes.every((o) => o.length <= 14))
            .toList();
    return _Moldura(
      sessao: s,
      planeta: p,
      setor: no == null ? -1 : setorDoNo(no),
      jogo: widget.jogo,
      rnd: rnd,
      desafios: desafios,
    );
  }
}

/// Cabeçalho, placar final e gravação da recompensa, comuns aos jogos.
class _Moldura extends ConsumerStatefulWidget {
  final Sessao sessao;
  final Planeta planeta;
  final Minijogo jogo;
  final Random rnd;
  final List<DesafioPorta> desafios;
  final int setor;
  const _Moldura({
    required this.setor,
    required this.sessao,
    required this.planeta,
    required this.jogo,
    required this.rnd,
    required this.desafios,
  });

  @override
  ConsumerState<_Moldura> createState() => _MolduraState();
}

class _MolduraState extends ConsumerState<_Moldura> {
  int _rodada = 0;
  ({int pontos, int peixinhos, String frase})? _fim;
  bool _travado = false; // evita que o último toque do jogo aperte um botão

  void _voltar() =>
      context.go('/c/${widget.sessao.perfil.id}/p/${widget.planeta.id}/s/${widget.setor}');

  Future<void> _terminar(int pontos, String frase) async {
    final peixinhos = (peixinhosDoMinijogo(pontos) * widget.sessao.nivel.multiplicador).round();
    setState(() {
      _fim = (pontos: pontos, peixinhos: peixinhos, frase: frase);
      _travado = true;
    });
    Timer(const Duration(milliseconds: 900), () {
      if (mounted) setState(() => _travado = false);
    });
    // Conta como uma pausa do dia (mesmo registro do labirinto).
    await ref
        .read(acoesProvider)
        .concluirLabirinto(
          perfilId: widget.sessao.perfil.id,
          xp: (3 * widget.sessao.nivel.multiplicador).round(),
          peixinhos: peixinhos,
        );
  }

  @override
  Widget build(BuildContext context) {
    final s = widget.sessao;
    Widget nave(double t) => naveDaCrianca(s, t);
    final jogo = switch (widget.jogo) {
      Minijogo.patrulha => _JogoPatrulha(
        key: ValueKey(_rodada),
        ano: s.perfil.ano,
        rnd: widget.rnd,
        nave: nave,
        fim: _terminar,
      ),
      Minijogo.cauda => _JogoCauda(
        key: ValueKey(_rodada),
        ano: s.perfil.ano,
        rnd: widget.rnd,
        desafios: widget.desafios,
        fim: _terminar,
      ),
      _ => _JogoTravessia(
        key: ValueKey(_rodada),
        ano: s.perfil.ano,
        rnd: widget.rnd,
        nave: nave,
        fim: _terminar,
      ),
    };
    return FundoEspacial(
      child: SafeArea(
        child: Stack(
          children: [
            Column(
              children: [
                Padding(
                  padding: const EdgeInsets.fromLTRB(8, 6, 14, 0),
                  child: Row(
                    children: [
                      IconButton(
                        tooltip: 'Sair do jogo',
                        color: Colors.white,
                        icon: const Icon(Icons.close),
                        onPressed: _voltar,
                      ),
                      Expanded(
                        child: Text(
                          '${widget.jogo.emoji} ${widget.jogo.nome.toUpperCase()}',
                          style: const TextStyle(
                            color: Cores.ciano,
                            fontSize: 15,
                            fontWeight: FontWeight.w900,
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
                Expanded(child: _fim == null ? jogo : const SizedBox()),
              ],
            ),
            if (_fim != null) _placar(_fim!),
          ],
        ),
      ),
    );
  }

  Widget _placar(({int pontos, int peixinhos, String frase}) f) => IgnorePointer(
    ignoring: _travado,
    child: Center(
      child: Container(
        margin: const EdgeInsets.all(24),
        padding: const EdgeInsets.all(22),
        decoration: BoxDecoration(color: Cores.espacoMeio, borderRadius: BorderRadius.circular(24)),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Text(widget.jogo.emoji, style: const TextStyle(fontSize: 64)),
            Text(
              f.frase,
              textAlign: TextAlign.center,
              style: const TextStyle(
                color: Color(0xFFFFB100),
                fontSize: 22,
                fontWeight: FontWeight.w900,
              ),
            ),
            const SizedBox(height: 10),
            Text(
              '⭐ ${f.pontos} pontos   ·   🐟 ${f.peixinhos}',
              style: const TextStyle(
                color: Colors.white,
                fontSize: 19,
                fontWeight: FontWeight.w900,
              ),
            ),
            const SizedBox(height: 20),
            Botao3D(
              cor: widget.planeta.cor,
              corSombra: widget.planeta.corEscura,
              texto: 'PRÓXIMA MISSÃO ➜',
              onPressed: _voltar,
            ),
            const SizedBox(height: 10),
            Botao3D.branco(
              texto: '🔁 JOGAR DE NOVO',
              onPressed: () => setState(() {
                _fim = null;
                _rodada++;
              }),
            ),
          ],
        ),
      ),
    ),
  );
}

typedef _Fim = Future<void> Function(int pontos, String frase);

/// Laço de animação comum: chama `passo(dt)` a cada quadro.
mixin _Laco<T extends StatefulWidget> on State<T>, SingleTickerProviderStateMixin<T> {
  late final Ticker _ticker;
  Duration _ultimo = Duration.zero;
  bool _encerrado = false;

  void passo(double dt);

  @override
  void initState() {
    super.initState();
    _ticker = createTicker((agora) {
      final dt = ((agora - _ultimo).inMicroseconds / 1e6).clamp(0.0, 0.05);
      _ultimo = agora;
      if (_encerrado) return;
      setState(() => passo(dt));
    })..start();
  }

  void encerrar() {
    _encerrado = true;
    _ticker.stop();
  }

  @override
  void dispose() {
    _ticker.dispose();
    super.dispose();
  }
}

// ---------------------------------------------------------------------------
// Patrulha da Luz

class _JogoPatrulha extends StatefulWidget {
  final int ano;
  final Random rnd;
  final Widget Function(double) nave;
  final _Fim fim;
  const _JogoPatrulha({
    super.key,
    required this.ano,
    required this.rnd,
    required this.nave,
    required this.fim,
  });

  @override
  State<_JogoPatrulha> createState() => _JogoPatrulhaState();
}

class _JogoPatrulhaState extends State<_JogoPatrulha> with SingleTickerProviderStateMixin, _Laco {
  late final Patrulha _j = Patrulha(widget.ano, widget.rnd);

  @override
  void passo(double dt) {
    _j.passo(dt);
    if (_j.acabou) {
      encerrar();
      widget.fim(
        _j.acesos,
        _j.escudos > 0
            ? 'Patrulha completa! ${_j.acesos} drones reacesos!'
            : 'Escudos no fim, mas ${_j.acesos} drones voltaram a brilhar!',
      );
    }
  }

  @override
  Widget build(BuildContext context) => Column(
    children: [
      Padding(
        padding: const EdgeInsets.symmetric(horizontal: 18, vertical: 4),
        child: Row(
          children: [
            Text('🛡️' * _j.escudos, style: const TextStyle(fontSize: 18)),
            const Spacer(),
            Text(
              '✨ ${_j.acesos}   ⏱️ ${max(0, (_j.duracao - _j.tempo).ceil())}s',
              style: const TextStyle(color: Colors.white, fontWeight: FontWeight.w900),
            ),
          ],
        ),
      ),
      const Padding(
        padding: EdgeInsets.only(bottom: 4),
        child: Text(
          'Arraste para cima e para baixo. A luz sai sozinha!',
          style: TextStyle(color: Cores.textoClaro, fontSize: 13),
        ),
      ),
      Expanded(
        child: LayoutBuilder(
          builder: (context, c) {
            final w = c.maxWidth, h = c.maxHeight;
            final t = min(w, h) * 0.12;
            return GestureDetector(
              behavior: HitTestBehavior.opaque,
              onPanUpdate: (d) => _j.moverPara(d.localPosition.dy / h),
              onTapDown: (d) => _j.moverPara(d.localPosition.dy / h),
              child: Stack(
                clipBehavior: Clip.hardEdge,
                children: [
                  Positioned.fill(child: CustomPaint(painter: _PintorPatrulha(_j))),
                  for (final d in _j.drones)
                    Positioned(
                      left: d.x * w - t / 2,
                      top: d.y * h - t / 2,
                      width: t,
                      height: t,
                      child: Center(
                        child: Opacity(
                          opacity: d.aceso ? (1 - d.brilho / 1.2).clamp(0, 1) : 1,
                          child: Text(
                            d.asteroide
                                ? '🪨'
                                : d.aceso
                                ? '🌟'
                                : '🌑',
                            style: TextStyle(fontSize: t * 0.7, height: 1),
                          ),
                        ),
                      ),
                    ),
                  Positioned(
                    left: Patrulha.naveX * w - t / 2,
                    top: _j.naveY * h - t / 2,
                    width: t,
                    height: t,
                    child: Opacity(
                      opacity: _j.invencivel > 0 && (_j.invencivel * 8).floor().isEven ? 0.35 : 1,
                      child: Center(child: widget.nave(t)),
                    ),
                  ),
                ],
              ),
            );
          },
        ),
      ),
    ],
  );
}

class _PintorPatrulha extends CustomPainter {
  final Patrulha j;
  _PintorPatrulha(this.j);

  @override
  void paint(Canvas canvas, Size size) {
    final p = Paint()
      ..color = Cores.ouro
      ..strokeWidth = 5
      ..strokeCap = StrokeCap.round;
    for (final r in j.raios) {
      final o = Offset(r.x * size.width, r.y * size.height);
      canvas.drawLine(o, o.translate(18, 0), p);
    }
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) => true;
}

// ---------------------------------------------------------------------------
// Cauda de Cometa

class _JogoCauda extends StatefulWidget {
  final int ano;
  final Random rnd;
  final List<DesafioPorta> desafios;
  final _Fim fim;
  const _JogoCauda({
    super.key,
    required this.ano,
    required this.rnd,
    required this.desafios,
    required this.fim,
  });

  @override
  State<_JogoCauda> createState() => _JogoCaudaState();
}

class _JogoCaudaState extends State<_JogoCauda> with SingleTickerProviderStateMixin, _Laco {
  late final Cauda _j = Cauda(widget.rnd, widget.desafios);
  late final double _intervalo = 1 / Cauda.velocidade(widget.ano);
  static const _duracao = 90.0; // segundos: a pausa tem fim
  double _acumulado = 0;
  double _tempo = 0;

  @override
  void passo(double dt) {
    _tempo += dt;
    if (_tempo >= _duracao) {
      encerrar();
      widget.fim(
        _j.pontos,
        'Tempo da pausa! Você acertou ${_j.acertos} e juntou ${_j.pontos} pontos.',
      );
      return;
    }
    _acumulado += dt;
    while (_acumulado >= _intervalo) {
      _acumulado -= _intervalo;
      _j.passo();
    }
    if (_j.bateu) {
      encerrar();
      widget.fim(
        _j.pontos,
        'A cauda ficou com ${_j.corpo.length} pedaços e você acertou ${_j.acertos}!',
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    final p = _j.pergunta;
    return Column(
      children: [
        Container(
          width: double.infinity,
          margin: const EdgeInsets.fromLTRB(14, 4, 14, 6),
          padding: const EdgeInsets.all(10),
          decoration: BoxDecoration(
            color: Colors.white.withValues(alpha: 0.1),
            borderRadius: BorderRadius.circular(14),
          ),
          child: Column(
            children: [
              Text(
                p == null
                    ? 'Pegue as estrelinhas ⭐ para crescer!'
                    : p.pergunta.replaceAll('**', '').replaceAll('{nome}', ''),
                textAlign: TextAlign.center,
                maxLines: 3,
                overflow: TextOverflow.ellipsis,
                style: const TextStyle(
                  color: Colors.white,
                  fontSize: 15,
                  fontWeight: FontWeight.w800,
                ),
              ),
              if (_j.retorno != null)
                Text(_j.retorno!, style: const TextStyle(color: Color(0xFFFFE9A8), fontSize: 13)),
              Text(
                '⭐ ${_j.pontos}   ✅ ${_j.acertos}   ⏱️ ${max(0, (_duracao - _tempo).ceil())}s',
                style: const TextStyle(color: Cores.textoClaro, fontSize: 13),
              ),
            ],
          ),
        ),
        Expanded(
          child: GestureDetector(
            behavior: HitTestBehavior.opaque,
            onPanEnd: (d) {
              final v = d.velocity.pixelsPerSecond;
              if (v.distance < 100) return;
              _j.virar(
                v.dx.abs() > v.dy.abs()
                    ? (v.dx > 0 ? Dir.direita : Dir.esquerda)
                    : (v.dy > 0 ? Dir.baixo : Dir.cima),
              );
            },
            child: Center(
              child: AspectRatio(
                aspectRatio: _j.colunas / _j.linhas,
                child: LayoutBuilder(
                  builder: (context, c) {
                    final t = c.maxWidth / _j.colunas;
                    Widget casa(Pos p, Widget w) =>
                        Positioned(left: p.x * t, top: p.y * t, width: t, height: t, child: w);
                    return Stack(
                      children: [
                        Positioned.fill(child: CustomPaint(painter: _PintorCauda(_j))),
                        for (final e in _j.estrelas)
                          casa(
                            e,
                            Center(
                              child: Text('⭐', style: TextStyle(fontSize: t * 0.6)),
                            ),
                          ),
                        for (final r in _j.respostas)
                          Positioned(
                            left: (r.pos.x - 0.6) * t,
                            top: r.pos.y * t,
                            width: t * 2.2,
                            height: t,
                            child: Center(
                              child: Container(
                                padding: const EdgeInsets.symmetric(horizontal: 4),
                                decoration: BoxDecoration(
                                  color: Cores.roxo,
                                  borderRadius: BorderRadius.circular(8),
                                ),
                                child: Text(
                                  r.texto,
                                  maxLines: 1,
                                  overflow: TextOverflow.ellipsis,
                                  style: TextStyle(
                                    color: Colors.white,
                                    fontSize: t * 0.34,
                                    fontWeight: FontWeight.w900,
                                  ),
                                ),
                              ),
                            ),
                          ),
                      ],
                    );
                  },
                ),
              ),
            ),
          ),
        ),
        _setas(),
        const SizedBox(height: 8),
      ],
    );
  }

  Widget _setas() {
    Widget b(IconData i, Dir d, String r) => IconButton(
      tooltip: r,
      iconSize: 34,
      color: Colors.white,
      icon: Icon(i),
      onPressed: () => _j.virar(d),
    );
    return Row(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        b(Icons.keyboard_arrow_left, Dir.esquerda, 'Esquerda'),
        b(Icons.keyboard_arrow_up, Dir.cima, 'Cima'),
        b(Icons.keyboard_arrow_down, Dir.baixo, 'Baixo'),
        b(Icons.keyboard_arrow_right, Dir.direita, 'Direita'),
      ],
    );
  }
}

class _PintorCauda extends CustomPainter {
  final Cauda j;
  _PintorCauda(this.j);

  @override
  void paint(Canvas canvas, Size size) {
    final t = size.width / j.colunas;
    canvas.drawRRect(
      RRect.fromRectAndRadius(Offset.zero & size, const Radius.circular(14)),
      Paint()..color = const Color(0xFF232A6E).withValues(alpha: 0.7),
    );
    final n = j.corpo.length;
    for (var i = n - 1; i >= 0; i--) {
      final p = j.corpo[i];
      final c = Offset((p.x + .5) * t, (p.y + .5) * t);
      if (i == 0) {
        canvas.drawCircle(c, t * 0.48, Paint()..color = Cores.ouro);
        canvas.drawCircle(c, t * 0.22, Paint()..color = Colors.white);
      } else {
        // Cauda vai do dourado ao azul, cada vez mais transparente.
        final f = i / n;
        canvas.drawCircle(
          c,
          t * (0.42 - 0.18 * f),
          Paint()..color = Color.lerp(Cores.ouro, Cores.ciano, f)!.withValues(alpha: 1 - 0.6 * f),
        );
      }
    }
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) => true;
}

// ---------------------------------------------------------------------------
// Travessia do Cinturão

class _JogoTravessia extends StatefulWidget {
  final int ano;
  final Random rnd;
  final Widget Function(double) nave;
  final _Fim fim;
  const _JogoTravessia({
    super.key,
    required this.ano,
    required this.rnd,
    required this.nave,
    required this.fim,
  });

  @override
  State<_JogoTravessia> createState() => _JogoTravessiaState();
}

class _JogoTravessiaState extends State<_JogoTravessia> with SingleTickerProviderStateMixin, _Laco {
  late final Travessia _j = Travessia(widget.ano, widget.rnd);

  @override
  void passo(double dt) {
    _j.passo(dt);
    if (_j.bateu) {
      encerrar();
      Timer(const Duration(milliseconds: 500), () {
        if (mounted) {
          widget.fim(_j.passagens * 2, 'Você cruzou ${_j.passagens} passagens do cinturão!');
        }
      });
    }
  }

  @override
  Widget build(BuildContext context) => GestureDetector(
    behavior: HitTestBehavior.opaque,
    onTapDown: (_) => setState(_j.tocar),
    child: LayoutBuilder(
      builder: (context, c) {
        final w = c.maxWidth, h = c.maxHeight;
        final t = h * Travessia.raio * 2.6;
        return Stack(
          clipBehavior: Clip.hardEdge,
          children: [
            Positioned.fill(child: CustomPaint(painter: _PintorTravessia(_j))),
            Positioned(
              left: Travessia.naveX * w - t / 2,
              top: _j.y * h - t / 2,
              width: t,
              height: t,
              child: Transform.rotate(
                angle: (_j.vy * 0.6).clamp(-0.5, 0.6),
                child: Center(
                  child: _j.bateu
                      ? Text('💫', style: TextStyle(fontSize: t * 0.8))
                      : widget.nave(t),
                ),
              ),
            ),
            Positioned(
              top: 10,
              left: 0,
              right: 0,
              child: Text(
                '${_j.passagens}',
                textAlign: TextAlign.center,
                style: const TextStyle(
                  color: Colors.white,
                  fontSize: 40,
                  fontWeight: FontWeight.w900,
                ),
              ),
            ),
            if (!_j.comecou)
              const Center(
                child: Padding(
                  padding: EdgeInsets.all(30),
                  child: Text(
                    'Toque na tela para a nave subir.\nPasse pelos buracos do cinturão!',
                    textAlign: TextAlign.center,
                    style: TextStyle(
                      color: Colors.white,
                      fontSize: 18,
                      fontWeight: FontWeight.w800,
                    ),
                  ),
                ),
              ),
          ],
        );
      },
    ),
  );
}

class _PintorTravessia extends CustomPainter {
  final Travessia j;
  _PintorTravessia(this.j);

  @override
  void paint(Canvas canvas, Size size) {
    final rocha = Paint()..color = const Color(0xFF8C6E5A);
    final borda = Paint()..color = const Color(0xFF6B5240);
    for (final c in j.colunas) {
      final x = c.x * size.width;
      final larg = size.width * 0.12;
      final topo = (c.centro - c.abertura / 2) * size.height;
      final base = (c.centro + c.abertura / 2) * size.height;
      // Cada coluna é uma pilha de rochas redondas.
      for (var y = topo - larg / 2; y > -larg; y -= larg * 0.8) {
        canvas.drawCircle(Offset(x, y), larg * 0.55, borda);
        canvas.drawCircle(Offset(x, y), larg * 0.47, rocha);
      }
      for (var y = base + larg / 2; y < size.height + larg; y += larg * 0.8) {
        canvas.drawCircle(Offset(x, y), larg * 0.55, borda);
        canvas.drawCircle(Offset(x, y), larg * 0.47, rocha);
      }
    }
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) => true;
}
