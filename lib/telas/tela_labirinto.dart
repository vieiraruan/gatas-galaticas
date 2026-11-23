import 'dart:async';
import 'dart:math';

import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:material_ui/material_ui.dart';

import '../componentes/fala.dart';
import '../componentes/gatos.dart';
import '../componentes/tema.dart';
import '../componentes/texto_rico.dart';
import '../componentes/visuais.dart';
import '../logica/labirinto.dart';
import '../logica/regras.dart';
import '../modelos/conteudo.dart';
import '../providers.dart';

/// Labirinto Orbital: pausa opcional depois de uma missão.
/// `indice` é o nó (missão) que a criança acabou de jogar.
class TelaLabirinto extends ConsumerWidget {
  final String perfilId;
  final String planetaId;
  final int indice;
  const TelaLabirinto(
      {super.key, required this.perfilId, required this.planetaId, required this.indice});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    // Lê a sessão uma vez: gravar o resultado não deve recriar o labirinto.
    final pronto = ref.watch(sessaoProvider(perfilId).select((a) => a.whenData((s) => s != null)));
    return Scaffold(
      backgroundColor: Cores.espaco,
      body: pronto.when(
        skipLoadingOnReload: true,
        loading: () => const Center(child: CircularProgressIndicator()),
        error: (e, _) => Center(child: Text('Erro: $e')),
        data: (_) {
          final s = ref.read(sessaoProvider(perfilId)).value;
          final p = s?.planeta(planetaId);
          if (s == null || p == null) {
            return const Center(
                child: Text('Labirinto não encontrado.', style: TextStyle(color: Colors.white)));
          }
          final r = s.regras(p);
          final no = indice >= 0 && indice < r.nos.length ? r.nos[indice] : null;
          final recentes = no == null ? const <Missao>[] : missoesDoNo(no);
          final ids = recentes.map((m) => m.id).toSet();
          // Missões já feitas no bimestre (com estrela), menos a de agora.
          final anteriores = [
            for (final pl in s.bimestre.planetas)
              for (final n in s.regras(pl).nos)
                if (n is NoMissao && s.regras(pl).estrelas(n) > 0 && !ids.contains(n.missao.id))
                  n.missao
          ];
          return _Jogo(
            sessao: s,
            planeta: p,
            estrelasMissao: no == null ? 0 : r.estrelas(no),
            anteriores: anteriores,
            recentes: recentes,
          );
        },
      ),
    );
  }
}

class _Jogo extends ConsumerStatefulWidget {
  final Sessao sessao;
  final Planeta planeta;
  final int estrelasMissao;
  final List<Missao> anteriores;
  final List<Missao> recentes;
  const _Jogo({
    required this.sessao,
    required this.planeta,
    required this.estrelasMissao,
    required this.anteriores,
    required this.recentes,
  });

  @override
  ConsumerState<_Jogo> createState() => _JogoState();
}

class _JogoState extends ConsumerState<_Jogo> {
  late final Random _rnd = ref.read(aleatorioProvider);
  late final Fala _fala = ref.read(falaProvider);
  late final bool _calmo = widget.sessao.labirintosHoje == 0;
  late final ConfigLabirinto _cfg =
      ConfigLabirinto.doAno(widget.sessao.perfil.ano, calmo: _calmo);
  late final Labirinto _lab = Labirinto.gerar(_cfg, _rnd);
  late final Poder _poder = poderDaGata(widget.sessao.perfil.gato);
  late int _usos = usosDoPoder(widget.estrelasMissao);
  late final List<DesafioPorta> _desafios = desafiosDeLembranca(
      anteriores: widget.anteriores, recentes: widget.recentes, rnd: _rnd);
  int _desafio = 0;

  late Pos _gata = _lab.inicio;
  late Pos _seguro = _lab.inicio;
  final DateTime _inicio = DateTime.now();
  Timer? _relogio;
  int _peixes = 0;
  int _toques = 0;
  bool _ocupado = false; // pergunta, respiro ou novelo
  bool _invasao = false;
  bool _passagem = false;
  DateTime _charmeAte = DateTime(0);
  List<Pos> _rota = const [];
  String? _aviso;
  Timer? _avisoTimer;
  ({int xp, int peixinhos, bool bonus, int segundos})? _fim;

  String get _nome => widget.sessao.perfil.nome;

  @override
  void initState() {
    super.initState();
    _fala; // guarda a voz para poder parar no dispose
    if (_lab.aspiradores.isNotEmpty) {
      _relogio = Timer.periodic(const Duration(milliseconds: 750), (_) => _tique());
    }
    WidgetsBinding.instance.addPostFrameCallback((_) => _avisar(
        _calmo
            ? 'Modo respiro: sem pressa. Leve a gata até a cápsula 🛸'
            : 'Leve a gata até a cápsula de fuga 🛸',
        segundos: 4));
  }

  @override
  void dispose() {
    _relogio?.cancel();
    _avisoTimer?.cancel();
    _fala.parar();
    super.dispose();
  }

  void _avisar(String t, {int segundos = 3}) {
    if (!mounted) return;
    _avisoTimer?.cancel();
    setState(() => _aviso = t);
    _avisoTimer = Timer(Duration(seconds: segundos), () {
      if (mounted) setState(() => _aviso = null);
    });
  }

  void _mostrarRota(int segundos) {
    setState(() => _rota = _lab.caminho(_gata, _lab.saida));
    Timer(Duration(seconds: segundos), () {
      if (mounted) setState(() => _rota = const []);
    });
  }

  // -------------------------------------------------------------------------
  // Regras do movimento

  void _tique() {
    if (_fim != null || _ocupado || DateTime.now().isBefore(_charmeAte)) return;
    setState(() {
      for (final a in _lab.aspiradores) {
        a.andar();
      }
    });
    _conferirAspirador();
  }

  void _conferirAspirador() {
    if (!_lab.aspiradores.any((a) => a.pos == _gata)) return;
    _toques++;
    setState(() => _gata = _seguro);
    _avisar('🤖 Um aspirador levou a gata de volta. Tudo bem, tente de novo!');
    if (_toques % 3 == 0) {
      _avisar('✨ A tripulação mandou uma seta de ajuda!');
      _mostrarRota(3);
    }
  }

  Future<void> _mover(Dir d) async {
    if (_fim != null || _ocupado) return;
    final q = _gata.mover(d);
    if (!_lab.dentro(q)) return;
    final atravessa = !_lab.aberto(_gata, d);
    if (atravessa && !_passagem) return;

    switch (_lab.itens[q]) {
      case Item.poca:
        _avisar('💧 A gata não quer molhar as patinhas! Procure outro caminho.');
        return;
      case Item.porta:
        final abriu = await _abrirPorta();
        if (!abriu || !mounted) return;
        _lab.itens.remove(q);
        _seguro = q;
      case Item.novelo:
        _lab.itens.remove(q);
        _ocupado = true;
        _avisar('🧶 Enroscou no novelo! Só um instante...', segundos: 2);
        Timer(const Duration(milliseconds: 1200), () {
          if (mounted) setState(() => _ocupado = false);
        });
      case Item.peixe:
        _lab.itens.remove(q);
        _peixes++;
      case Item.respiro:
        _lab.itens.remove(q);
      case null:
        break;
    }
    if (atravessa) _passagem = false;
    setState(() => _gata = q);
    _conferirAspirador();
    if (_gata == _lab.saida) {
      await _terminar();
    } else if (_lab.itens[q] == null && q == _respiroEm) {
      _respiroEm = null;
      await _oferecerRespiro();
    }
  }

  // A janela de respiro some do mapa quando a gata pisa nela.
  late Pos? _respiroEm = _lab.itens.entries
      .where((e) => e.value == Item.respiro)
      .map((e) => e.key)
      .firstOrNull;

  void _usarPoder() {
    if (_usos <= 0 || _fim != null || _ocupado) return;
    setState(() => _usos--);
    switch (_poder) {
      case Poder.olharSoberano:
        _mostrarRota(3);
      case Poder.invasaoRapida:
        _invasao = true;
        _avisar('💻 Próxima porta hackeada!');
      case Poder.charmeFatal:
        _charmeAte = DateTime.now().add(const Duration(seconds: 4));
        _avisar('💖 Os aspiradores pararam para um carinho!');
      case Poder.passagemSecreta:
        _passagem = true;
        _avisar('🕳️ Escolha uma parede para atravessar.');
      case Poder.miadoSonico:
        bool perto(Pos p) => (p.x - _gata.x).abs() + (p.y - _gata.y).abs() <= 2;
        setState(() {
          _lab.itens.removeWhere(
              (p, i) => (i == Item.poca || i == Item.novelo) && perto(p));
          _lab.aspiradores.removeWhere((a) => perto(a.pos));
        });
        _avisar('📣 MIAAAU! O caminho ficou livre.');
    }
  }

  Future<bool> _abrirPorta() async {
    if (_invasao) {
      _invasao = false;
      _avisar('💻 Porta aberta pela hacker!');
      return true;
    }
    if (_desafios.isEmpty) return true;
    _ocupado = true;
    final ok = await showDialog<bool>(
      context: context,
      barrierDismissible: false,
      builder: (_) => _PortaCodigo(
        proxima: () => _desafios[_desafio++ % _desafios.length],
        nome: _nome,
        falarSozinho: widget.sessao.perfil.ano <= 2,
        cor: widget.planeta.cor,
      ),
    );
    _ocupado = false;
    return ok ?? false;
  }

  Future<void> _oferecerRespiro() async {
    _ocupado = true;
    await showDialog<void>(context: context, builder: (_) => const _JanelaRespiro());
    _ocupado = false;
  }

  Future<void> _terminar() async {
    _relogio?.cancel();
    final seg = DateTime.now().difference(_inicio).inSeconds;
    final bonus = _cfg.segundosBonus > 0 && seg <= _cfg.segundosBonus;
    final g = recompensaLabirinto(
        peixesPegos: _peixes, bonusTempo: bonus, multiplicador: widget.sessao.nivel.multiplicador);
    setState(() => _fim = (xp: g.xp, peixinhos: g.peixinhos, bonus: bonus, segundos: seg));
    await ref.read(acoesProvider).concluirLabirinto(
        perfilId: widget.sessao.perfil.id, xp: g.xp, peixinhos: g.peixinhos);
  }

  void _voltar() => context.go('/c/${widget.sessao.perfil.id}/p/${widget.planeta.id}');

  // -------------------------------------------------------------------------
  // Tela

  @override
  Widget build(BuildContext context) {
    if (_fim != null) return _telaFinal();
    return FundoEspacial(
      child: SafeArea(
        child: Column(children: [
          Padding(
            padding: const EdgeInsets.fromLTRB(8, 6, 14, 0),
            child: Row(children: [
              IconButton(
                  tooltip: 'Pular o labirinto',
                  color: Colors.white,
                  icon: const Icon(Icons.close),
                  onPressed: _voltar),
              const Expanded(
                child: Text('🌌 LABIRINTO ORBITAL',
                    style: TextStyle(color: Cores.ciano, fontSize: 15, fontWeight: FontWeight.w900)),
              ),
              Text('🐟 $_peixes',
                  style: const TextStyle(color: Colors.white, fontSize: 17, fontWeight: FontWeight.w900)),
            ]),
          ),
          SizedBox(
            height: 44,
            child: Center(
              child: AnimatedOpacity(
                opacity: _aviso == null ? 0 : 1,
                duration: const Duration(milliseconds: 250),
                child: Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 16),
                  child: Text(_aviso ?? '',
                      textAlign: TextAlign.center,
                      style: const TextStyle(color: Color(0xFFFFE9A8), fontSize: 15)),
                ),
              ),
            ),
          ),
          Expanded(
            child: Padding(
              padding: const EdgeInsets.symmetric(horizontal: 12),
              child: GestureDetector(
                onPanEnd: (d) {
                  final v = d.velocity.pixelsPerSecond;
                  if (v.distance < 120) return;
                  _mover(v.dx.abs() > v.dy.abs()
                      ? (v.dx > 0 ? Dir.direita : Dir.esquerda)
                      : (v.dy > 0 ? Dir.baixo : Dir.cima));
                },
                child: Center(child: AspectRatio(aspectRatio: 1, child: _tabuleiro())),
              ),
            ),
          ),
          const SizedBox(height: 8),
          _controles(),
          const SizedBox(height: 10),
        ]),
      ),
    );
  }

  Widget _tabuleiro() => LayoutBuilder(builder: (context, c) {
        final t = c.maxWidth / _lab.lado;
        Widget naCasa(Pos p, Widget w, {Key? key, bool animar = false}) => animar
            ? AnimatedPositioned(
                key: key,
                duration: const Duration(milliseconds: 180),
                curve: Curves.easeOut,
                left: p.x * t,
                top: p.y * t,
                width: t,
                height: t,
                child: w)
            : Positioned(key: key, left: p.x * t, top: p.y * t, width: t, height: t, child: w);
        Widget emoji(String e) => Center(
            child: Text(e, style: TextStyle(fontSize: t * 0.55, height: 1)));
        return Stack(children: [
          Positioned.fill(child: CustomPaint(painter: _Pintor(_lab, _rota, widget.planeta.cor))),
          naCasa(_lab.saida, emoji('🛸')),
          for (final e in _lab.itens.entries)
            naCasa(
                e.key,
                emoji(switch (e.value) {
                  Item.porta => '🚪',
                  Item.poca => '💧',
                  Item.novelo => '🧶',
                  Item.peixe => '🐟',
                  Item.respiro => '🪟',
                })),
          for (var i = 0; i < _lab.aspiradores.length; i++)
            naCasa(_lab.aspiradores[i].pos,
                emoji(DateTime.now().isBefore(_charmeAte) ? '😍' : '🤖'),
                key: ValueKey('asp$i'), animar: true),
          naCasa(
              _gata,
              Padding(
                padding: EdgeInsets.all(t * 0.08),
                child: AvatarGato(widget.sessao.perfil.gato, tamanho: t * 0.84),
              ),
              key: const ValueKey('gata'),
              animar: true),
        ]);
      });

  Widget _controles() {
    Widget seta(IconData i, Dir d, String rotulo) => Padding(
          padding: const EdgeInsets.all(3),
          child: Material(
            color: Colors.white.withValues(alpha: 0.12),
            shape: const CircleBorder(),
            child: IconButton(
              tooltip: rotulo,
              iconSize: 34,
              color: Colors.white,
              icon: Icon(i),
              onPressed: () => _mover(d),
            ),
          ),
        );
    return Row(mainAxisAlignment: MainAxisAlignment.spaceEvenly, children: [
      Column(mainAxisSize: MainAxisSize.min, children: [
        seta(Icons.keyboard_arrow_up, Dir.cima, 'Cima'),
        Row(mainAxisSize: MainAxisSize.min, children: [
          seta(Icons.keyboard_arrow_left, Dir.esquerda, 'Esquerda'),
          const SizedBox(width: 50),
          seta(Icons.keyboard_arrow_right, Dir.direita, 'Direita'),
        ]),
        seta(Icons.keyboard_arrow_down, Dir.baixo, 'Baixo'),
      ]),
      SizedBox(
        width: 140,
        child: Column(mainAxisSize: MainAxisSize.min, children: [
          Text(_poder.nome,
              textAlign: TextAlign.center,
              style: const TextStyle(color: Colors.white, fontWeight: FontWeight.w900)),
          Text(_poder.descricao,
              textAlign: TextAlign.center,
              style: const TextStyle(color: Cores.textoClaro, fontSize: 12)),
          const SizedBox(height: 6),
          Botao3D.ouro(
            texto: '${_poder.emoji} ×$_usos',
            altura: 48,
            onPressed: _usos > 0 ? _usarPoder : null,
          ),
        ]),
      ),
    ]);
  }

  Widget _telaFinal() {
    final f = _fim!;
    return FundoEspacial(
      child: SafeArea(
        child: ListView(padding: const EdgeInsets.fromLTRB(20, 40, 20, 30), children: [
          const Text('🛸', textAlign: TextAlign.center, style: TextStyle(fontSize: 80)),
          const Text('Você escapou do Labirinto Orbital!',
              textAlign: TextAlign.center,
              style: TextStyle(color: Color(0xFFFFB100), fontSize: 26, fontWeight: FontWeight.w900)),
          const SizedBox(height: 8),
          Text('Mente descansada, $_nome. Bora para a próxima missão? 😺',
              textAlign: TextAlign.center,
              style: const TextStyle(color: Color(0xFFC9CFF5), fontSize: 18)),
          const SizedBox(height: 20),
          Text('⚡${f.xp} XP   ·   🐟${f.peixinhos} peixinhos',
              textAlign: TextAlign.center,
              style: const TextStyle(color: Colors.white, fontSize: 22, fontWeight: FontWeight.w900)),
          if (f.bonus)
            const Padding(
              padding: EdgeInsets.only(top: 6),
              child: Text('⏱️ Bônus de rapidez!',
                  textAlign: TextAlign.center, style: TextStyle(color: Cores.ouro, fontSize: 16)),
            ),
          const SizedBox(height: 26),
          Botao3D(
              cor: widget.planeta.cor,
              corSombra: widget.planeta.corEscura,
              texto: 'PRÓXIMA MISSÃO ➜',
              onPressed: _voltar),
        ]),
      ),
    );
  }
}

/// Paredes do labirinto e a seta de ajuda.
class _Pintor extends CustomPainter {
  final Labirinto lab;
  final List<Pos> rota;
  final Color cor;
  _Pintor(this.lab, this.rota, this.cor);

  @override
  void paint(Canvas canvas, Size size) {
    final t = size.width / lab.lado;
    canvas.drawRRect(
        RRect.fromRectAndRadius(Offset.zero & size, const Radius.circular(14)),
        Paint()..color = const Color(0xFF232A6E).withValues(alpha: 0.75));
    // Brilho na cápsula de fuga, para a saída se destacar no escuro.
    canvas.drawCircle(
        Offset((lab.saida.x + .5) * t, (lab.saida.y + .5) * t),
        t * 0.42,
        Paint()..color = Cores.ouro.withValues(alpha: 0.35));
    if (rota.length > 1) {
      final caminho = Path()..moveTo((rota.first.x + .5) * t, (rota.first.y + .5) * t);
      for (final p in rota.skip(1)) {
        caminho.lineTo((p.x + .5) * t, (p.y + .5) * t);
      }
      canvas.drawPath(
          caminho,
          Paint()
            ..color = Cores.ouro.withValues(alpha: 0.7)
            ..style = PaintingStyle.stroke
            ..strokeWidth = t * 0.18
            ..strokeCap = StrokeCap.round
            ..strokeJoin = StrokeJoin.round);
    }
    final parede = Paint()
      ..color = Cores.ciano.withValues(alpha: 0.85)
      ..strokeWidth = max(3, t * 0.09)
      ..strokeCap = StrokeCap.round;
    for (var y = 0; y < lab.lado; y++) {
      for (var x = 0; x < lab.lado; x++) {
        final p = Pos(x, y);
        final l = x * t, tp = y * t, r = (x + 1) * t, b = (y + 1) * t;
        if (!lab.aberto(p, Dir.cima)) canvas.drawLine(Offset(l, tp), Offset(r, tp), parede);
        if (!lab.aberto(p, Dir.esquerda)) canvas.drawLine(Offset(l, tp), Offset(l, b), parede);
        if (x == lab.lado - 1 && !lab.aberto(p, Dir.direita)) {
          canvas.drawLine(Offset(r, tp), Offset(r, b), parede);
        }
        if (y == lab.lado - 1 && !lab.aberto(p, Dir.baixo)) {
          canvas.drawLine(Offset(l, b), Offset(r, b), parede);
        }
      }
    }
  }

  @override
  bool shouldRepaint(covariant _Pintor old) => true;
}

/// Porta-código: uma pergunta de lembrança. Errou, vê a resposta e tenta
/// outra; na terceira tentativa a porta abre de qualquer jeito.
class _PortaCodigo extends ConsumerStatefulWidget {
  final DesafioPorta Function() proxima;
  final String nome;
  final bool falarSozinho;
  final Color cor;
  const _PortaCodigo(
      {required this.proxima, required this.nome, required this.falarSozinho, required this.cor});

  @override
  ConsumerState<_PortaCodigo> createState() => _PortaCodigoState();
}

class _PortaCodigoState extends ConsumerState<_PortaCodigo> {
  late DesafioPorta _d = widget.proxima();
  int _tentativas = 1;
  int? _escolha;

  @override
  void initState() {
    super.initState();
    if (widget.falarSozinho) _falar();
  }

  void _falar() => ref.read(falaProvider).falar(
      '${_d.pergunta.replaceAll('**', '').replaceAll('{nome}', widget.nome)}. ${_d.opcoes.join('. ')}');

  @override
  Widget build(BuildContext context) {
    final respondeu = _escolha != null;
    final acertou = _escolha == _d.correta;
    return AlertDialog(
      backgroundColor: Colors.white,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(22)),
      title: Row(children: [
        const Text('🚪 ', style: TextStyle(fontSize: 26)),
        const Expanded(
          child: Text('PORTA-CÓDIGO',
              style: TextStyle(fontWeight: FontWeight.w900, fontSize: 18)),
        ),
        IconButton(tooltip: 'Ouvir', icon: const Text('🔊'), onPressed: _falar),
      ]),
      content: SingleChildScrollView(
        child: Column(mainAxisSize: MainAxisSize.min, children: [
          const Text('Lembra disso? Responda para abrir a porta.',
              style: TextStyle(color: Cores.apagado, fontSize: 13)),
          const SizedBox(height: 10),
          TextoRico(_d.pergunta,
              nome: widget.nome,
              alinhamento: TextAlign.center,
              estilo: const TextStyle(fontSize: 18, fontWeight: FontWeight.w800, height: 1.35)),
          Visuais(_d.visuais, nome: widget.nome),
          const SizedBox(height: 12),
          for (var i = 0; i < _d.opcoes.length; i++)
            Padding(
              padding: const EdgeInsets.only(bottom: 8),
              child: Botao3D(
                texto: _d.opcoes[i],
                cor: !respondeu
                    ? Colors.white
                    : i == _d.correta
                        ? Cores.certo
                        : i == _escolha
                            ? Cores.errado
                            : Colors.white,
                corSombra: Cores.linha,
                corTexto: respondeu && (i == _d.correta || i == _escolha)
                    ? Colors.white
                    : Cores.tinta,
                onPressed: respondeu ? null : () => setState(() => _escolha = i),
              ),
            ),
          if (respondeu) ...[
            Text(acertou ? '✅ Isso aí! A porta abriu.' : 'Quase! A resposta certa está em verde.',
                textAlign: TextAlign.center,
                style: TextStyle(
                    color: acertou ? const Color(0xFF3B8A00) : const Color(0xFFC92B2B),
                    fontWeight: FontWeight.w900)),
            if (!acertou && _d.explicacao != null)
              Padding(
                padding: const EdgeInsets.only(top: 6),
                child: TextoRico(_d.explicacao!,
                    nome: widget.nome,
                    alinhamento: TextAlign.center,
                    estilo: const TextStyle(fontSize: 14)),
              ),
            const SizedBox(height: 12),
            if (acertou || _tentativas >= 3)
              Botao3D(
                cor: widget.cor,
                texto: acertou ? 'PASSAR ➜' : 'A PORTA VIU SEU ESFORÇO ➜',
                onPressed: () => Navigator.pop(context, true),
              )
            else
              Botao3D.branco(
                texto: '🔁 OUTRA PERGUNTA',
                onPressed: () => setState(() {
                  _d = widget.proxima();
                  _tentativas++;
                  _escolha = null;
                  if (widget.falarSozinho) _falar();
                }),
              ),
          ],
        ]),
      ),
    );
  }
}

/// Janela da nave: três respirações guiadas, sempre opcional.
class _JanelaRespiro extends StatefulWidget {
  const _JanelaRespiro();

  @override
  State<_JanelaRespiro> createState() => _JanelaRespiroState();
}

class _JanelaRespiroState extends State<_JanelaRespiro> with SingleTickerProviderStateMixin {
  late final AnimationController _c =
      AnimationController(vsync: this, duration: const Duration(seconds: 8));
  bool _respirando = false;
  int _voltas = 0;

  @override
  void initState() {
    super.initState();
    _c.addStatusListener((s) {
      if (s != AnimationStatus.completed) return;
      if (++_voltas < 3) {
        _c.forward(from: 0);
      } else {
        setState(() => _respirando = false);
      }
    });
  }

  @override
  void dispose() {
    _c.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) => AlertDialog(
        backgroundColor: Cores.espacoMeio,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(22)),
        content: Column(mainAxisSize: MainAxisSize.min, children: [
          const Text('🪟 Janela da nave',
              style: TextStyle(color: Colors.white, fontSize: 20, fontWeight: FontWeight.w900)),
          const SizedBox(height: 6),
          Text(
              _voltas >= 3
                  ? 'Prontinho. A mente está leve como uma estrela. ✨'
                  : 'Quer respirar com as estrelas? Inspire quando ela crescer e solte quando ela diminuir.',
              textAlign: TextAlign.center,
              style: const TextStyle(color: Cores.textoClaro)),
          const SizedBox(height: 16),
          SizedBox(
            height: 140,
            child: AnimatedBuilder(
              animation: _c,
              builder: (_, _) {
                final v = _c.value;
                final cresce = v < 0.5;
                final escala = 0.55 + 0.6 * (cresce ? v * 2 : (1 - v) * 2);
                return Column(children: [
                  Transform.scale(
                      scale: escala, child: const Text('⭐', style: TextStyle(fontSize: 90))),
                  if (_respirando)
                    Text(cresce ? 'Inspira...' : 'Solta...',
                        style: const TextStyle(color: Colors.white, fontSize: 16)),
                ]);
              },
            ),
          ),
          const SizedBox(height: 10),
          if (!_respirando && _voltas < 3)
            Botao3D.ouro(
                texto: 'RESPIRAR 3 VEZES',
                onPressed: () {
                  setState(() => _respirando = true);
                  _c.forward(from: 0);
                }),
          const SizedBox(height: 8),
          Botao3D.branco(
              texto: _voltas >= 3 ? 'SEGUIR VIAGEM ➜' : 'AGORA NÃO',
              onPressed: () => Navigator.pop(context)),
        ]),
      );
}
