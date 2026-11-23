import 'dart:async';
import 'dart:math';

import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:material_ui/material_ui.dart';

import '../componentes/exercicios.dart';
import '../componentes/fala.dart';
import '../componentes/gatos.dart';
import '../componentes/hud.dart';
import '../componentes/tema.dart';
import '../componentes/texto_rico.dart';
import '../componentes/visuais.dart';
import '../logica/regras.dart';
import '../modelos/conteudo.dart';
import '../providers.dart';

/// Uma partida: briefing → perguntas → resultado.
class TelaPartida extends ConsumerWidget {
  final String perfilId;
  final String planetaId;
  final int indice;
  const TelaPartida(
      {super.key, required this.perfilId, required this.planetaId, required this.indice});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    // Lê a sessão uma vez: gravar o resultado não deve recriar a partida.
    final sessao = ref.watch(sessaoProvider(perfilId).select((a) => a.whenData((s) => s != null)));
    return Scaffold(
      backgroundColor: Colors.white,
      body: sessao.when(
        skipLoadingOnReload: true,
        loading: () => const Center(child: CircularProgressIndicator()),
        error: (e, _) => Center(child: Text('Erro: $e')),
        data: (_) {
          final s = ref.read(sessaoProvider(perfilId)).value;
          final p = s?.planeta(planetaId);
          if (s == null || p == null) return const Center(child: Text('Missão não encontrada.'));
          final r = s.regras(p);
          if (indice < 0 || indice >= r.nos.length) {
            return const Center(child: Text('Missão não encontrada.'));
          }
          final no = r.nos[indice];
          if (emBreve(no) || no is NoCapsula || r.bloqueado(indice)) {
            return _Aviso(
              texto: emBreve(no)
                  ? '🛠️ Esta missão ainda está em construção.'
                  : '🔒 Esta missão ainda não foi liberada.',
              onVoltar: () => context.go('/c/$perfilId/p/$planetaId'),
            );
          }
          return _Partida(sessao: s, planeta: p, no: no, indice: indice);
        },
      ),
    );
  }
}

class _Aviso extends StatelessWidget {
  final String texto;
  final VoidCallback onVoltar;
  const _Aviso({required this.texto, required this.onVoltar});

  @override
  Widget build(BuildContext context) => SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(24),
          child: Column(mainAxisAlignment: MainAxisAlignment.center, children: [
            Text(texto, textAlign: TextAlign.center, style: const TextStyle(fontSize: 20)),
            const SizedBox(height: 20),
            Botao3D(texto: 'VOLTAR', onPressed: onVoltar),
          ]),
        ),
      );
}

enum _Fase { briefing, pergunta, fim }

class _Item {
  final Exercicio e;
  final bool revanche;
  _Item(this.e, this.revanche);
}

const _elogios = [
  'Miau-ravilha!', 'Mandou bem!', 'Isso aí!', 'Show!', 'Perfeito!', 'Arrasou!', 'Craque!', 'Decolou!'
];
const _incentivos = ['Quase lá!', 'Tudo bem errar!', 'Vamos aprender juntos!'];

class _Partida extends ConsumerStatefulWidget {
  final Sessao sessao;
  final Planeta planeta;
  final No no;
  final int indice;
  const _Partida(
      {required this.sessao, required this.planeta, required this.no, required this.indice});

  @override
  ConsumerState<_Partida> createState() => _PartidaState();
}

class _PartidaState extends ConsumerState<_Partida> {
  late Random _rnd;
  late List<_Item> _lista;
  late int _base;
  late List<CartaoBriefing> _briefing;
  _Fase _fase = _Fase.briefing;
  int _cartao = 0;
  int _i = 0;
  int _primeira = 0;
  int _combo = 0;
  int _vidaChefao = 0;
  Resposta? _resposta;
  String _tituloRetorno = '';
  bool _bloqueado = false;
  Timer? _relogio;
  int _restante = 0;
  late DateTime _inicio;
  late final Fala _fala = ref.read(falaProvider);
  _Final? _final;

  Sessao get s => widget.sessao;
  Nivel get nivel => s.nivel;
  String get nome => s.perfil.nome;
  bool get chefao => widget.no is NoChefao;

  @override
  void initState() {
    super.initState();
    _comecar();
  }

  void _comecar() {
    _rnd = ref.read(aleatorioProvider);
    final lista = montarPartida(widget.no, nivel, _rnd);
    _lista = [for (final e in lista) _Item(e, false)];
    _base = _lista.length;
    _vidaChefao = _base;
    final no = widget.no;
    _briefing = no is NoMissao ? no.missao.briefing : const [];
    _fase = _briefing.isEmpty ? _Fase.pergunta : _Fase.briefing;
    _cartao = 0;
    _i = 0;
    _primeira = 0;
    _combo = 0;
    _resposta = null;
    _bloqueado = false;
    _final = null;
    _inicio = DateTime.now();
    if (_fase == _Fase.pergunta) _iniciarRelogio();
  }

  @override
  void dispose() {
    _relogio?.cancel();
    _fala.parar();
    super.dispose();
  }

  bool get _comTempo {
    final e = _lista[_i].e;
    return nivel.tempoSegundos > 0 && (e is! Ligar && e is! Separar);
  }

  void _iniciarRelogio() {
    _relogio?.cancel();
    if (!_comTempo) return;
    _restante = nivel.tempoSegundos;
    _relogio = Timer.periodic(const Duration(seconds: 1), (t) {
      if (!mounted) return;
      setState(() => _restante--);
      if (_restante <= 0) {
        t.cancel();
        if (_resposta == null) {
          final e = _lista[_i].e;
          _responder(Resposta(false,
              respostaCerta: respostaCertaDe(e),
              explicacao: e.explicacao,
              nota: '⛽ O combustível acabou! Tente ser mais rápido na próxima.'));
        }
      }
    });
  }

  void _falar(String texto) => _fala.falar(TextoRico.paraFala(texto, nome));

  void _responder(Resposta r) {
    _relogio?.cancel();
    final item = _lista[_i];
    final primeiraVez = _i < _base;
    setState(() {
      _bloqueado = true;
      _resposta = r;
      if (r.certa) {
        _combo++;
        if (primeiraVez && r.semErros) _primeira++;
        if (chefao) _vidaChefao = max(0, _vidaChefao - 1);
        _tituloRetorno = (item.e is Ligar || item.e is Separar)
            ? 'Missão cumprida! 👏'
            : '${([..._elogios, 'Isso aí, $nome!']..shuffle(_rnd)).first}'
                '${_combo >= 3 ? ' 🔥 $_combo seguidas!' : ''}';
      } else {
        _combo = 0;
        final revanches = _lista.where((x) => x.revanche).length;
        if (chefao || (!item.revanche && revanches < 3)) {
          _lista.add(_Item(item.e, true));
        }
        _tituloRetorno = chefao
            ? 'O chefão se defendeu! 🛡️'
            : (List.of(_incentivos)..shuffle(_rnd)).first;
      }
    });
  }

  Future<void> _proxima() async {
    if (_i + 1 < _lista.length) {
      setState(() {
        _i++;
        _resposta = null;
        _bloqueado = false;
      });
      _iniciarRelogio();
      return;
    }
    await _terminar();
  }

  Future<void> _terminar() async {
    final estrelas = estrelasPorAcerto(_primeira, _base);
    final ganho = recompensa(widget.no, estrelas, nivel);
    final antes = s.progresso;
    final hojeAntes = s.xpHoje;
    setState(() {
      _fase = _Fase.fim;
      _final = _Final(
        estrelas: estrelas,
        xp: ganho.xp,
        peixinhos: ganho.peixinhos,
        acerto: _base == 0 ? 0 : (_primeira * 100 / _base).round(),
        tempo: DateTime.now().difference(_inicio),
        subiuNivel: nivelJogador(antes.xp + ganho.xp) > nivelJogador(antes.xp),
        novoNivel: nivelJogador(antes.xp + ganho.xp),
        novaPatente: patente(antes.xp + ganho.xp),
        bateuMeta: hojeAntes < metaXpDia && hojeAntes + ganho.xp >= metaXpDia,
      );
    });
    await ref.read(acoesProvider).concluirPartida(
          perfilId: s.perfil.id,
          nivel: s.perfil.nivel,
          noId: widget.no.id,
          estrelas: estrelas,
          xp: ganho.xp,
          peixinhos: ganho.peixinhos,
        );
  }

  void _sair() {
    if (_fase == _Fase.pergunta && _i > 0) {
      showModalBottomSheet<void>(
        context: context,
        backgroundColor: Cores.erradoClaro,
        builder: (c) => SafeArea(
          child: Padding(
            padding: const EdgeInsets.all(18),
            child: Column(mainAxisSize: MainAxisSize.min, children: [
              const Text('Abandonar a missão? 🙀',
                  style: TextStyle(fontSize: 22, fontWeight: FontWeight.w900, color: Color(0xFFC92B2B))),
              const SizedBox(height: 6),
              const Text('Você vai perder o progresso desta missão.'),
              const SizedBox(height: 14),
              Botao3D(texto: 'CONTINUAR A MISSÃO', onPressed: () => Navigator.pop(c)),
              const SizedBox(height: 8),
              Botao3D.branco(
                  texto: 'VOLTAR PARA A NAVE',
                  onPressed: () {
                    Navigator.pop(c);
                    _voltar();
                  }),
            ]),
          ),
        ),
      );
      return;
    }
    _voltar();
  }

  void _voltar() => context.go('/c/${s.perfil.id}/p/${widget.planeta.id}');

  @override
  Widget build(BuildContext context) {
    if (_fase == _Fase.fim) return _telaFinal();
    final p = widget.planeta;
    final pct = _fase == _Fase.briefing ? 0.0 : _i / _lista.length;
    return SafeArea(
      child: Column(children: [
        Padding(
          padding: const EdgeInsets.fromLTRB(8, 8, 14, 0),
          child: Row(children: [
            IconButton(
                tooltip: 'Sair da missão', icon: const Icon(Icons.close), onPressed: _sair),
            Expanded(child: BarraProgresso(valor: pct, cor: p.cor, altura: 18)),
            SizedBox(
              width: 50,
              child: Text(_combo >= 2 ? '🔥$_combo' : '',
                  textAlign: TextAlign.right,
                  style: const TextStyle(
                      color: Color(0xFFFF9600), fontSize: 17, fontWeight: FontWeight.w900)),
            ),
          ]),
        ),
        Padding(
          padding: const EdgeInsets.fromLTRB(18, 4, 18, 4),
          child: Row(children: [
            Expanded(
              child: Text('🚀 ${p.nome.toUpperCase()}',
                  style: TextStyle(color: p.corEscura, fontSize: 13, fontWeight: FontWeight.w900)),
            ),
            Container(
              padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),
              decoration: BoxDecoration(color: nivel.cor, borderRadius: BorderRadius.circular(10)),
              child: Text('${nivel.emoji} ${nivel.nome}',
                  style: const TextStyle(color: Colors.white, fontSize: 12, fontWeight: FontWeight.w900)),
            ),
          ]),
        ),
        if (chefao && _fase == _Fase.pergunta) _barraChefao(p),
        if (_fase == _Fase.pergunta && _comTempo && _resposta == null)
          Padding(
            padding: const EdgeInsets.fromLTRB(18, 2, 18, 4),
            child: Row(children: [
              Text('⛽ $_restante s', style: const TextStyle(fontWeight: FontWeight.w900)),
              const SizedBox(width: 8),
              Expanded(
                child: BarraProgresso(
                    valor: _restante / nivel.tempoSegundos, cor: const Color(0xFFFF9600), altura: 8),
              ),
            ]),
          ),
        Expanded(child: _fase == _Fase.briefing ? _telaBriefing(p) : _telaPergunta(p)),
        if (_resposta != null) _painelRetorno(),
      ]),
    );
  }

  Widget _barraChefao(Planeta p) => Container(
        margin: const EdgeInsets.fromLTRB(18, 4, 18, 6),
        padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
        decoration: BoxDecoration(color: const Color(0xFF2B2B2B), borderRadius: BorderRadius.circular(18)),
        child: Row(children: [
          Text(p.chefaoEmoji, style: const TextStyle(fontSize: 38)),
          const SizedBox(width: 10),
          Expanded(
            child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              const Text('CHEFÃO', style: TextStyle(color: Colors.white70, fontSize: 11)),
              Text(p.chefaoNome,
                  style: const TextStyle(color: Colors.white, fontWeight: FontWeight.w900)),
              const SizedBox(height: 4),
              BarraProgresso(
                  valor: _base == 0 ? 0 : _vidaChefao / _base,
                  cor: const Color(0xFFFF4B4B),
                  fundo: const Color(0xFF555555),
                  altura: 12),
            ]),
          ),
          const SizedBox(width: 10),
          Text('❤️ $_vidaChefao',
              style: const TextStyle(color: Colors.white, fontWeight: FontWeight.w900)),
        ]),
      );

  Widget _telaBriefing(Planeta p) {
    final c = _briefing[_cartao];
    final ultimo = _cartao == _briefing.length - 1;
    final jaJogou = s.progresso.jogadasDe(s.perfil.nivel, widget.no.id) > 0;
    return ListView(padding: const EdgeInsets.fromLTRB(18, 6, 18, 24), children: [
      Text('📡 BRIEFING DA MISSÃO · ${widget.no.rotulo.toUpperCase()}',
          style: TextStyle(color: p.cor, fontSize: 13, fontWeight: FontWeight.w900)),
      const SizedBox(height: 10),
      Container(
        padding: const EdgeInsets.fromLTRB(18, 22, 18, 22),
        decoration: BoxDecoration(
          color: Colors.white,
          borderRadius: BorderRadius.circular(22),
          border: Border.all(color: Cores.linha, width: 2),
          boxShadow: const [BoxShadow(color: Cores.linha, offset: Offset(0, 5))],
        ),
        child: Column(children: [
          Text(c.emoji, style: const TextStyle(fontSize: 64)),
          const SizedBox(height: 12),
          TextoRico(c.texto,
              nome: nome,
              alinhamento: TextAlign.center,
              estilo: const TextStyle(fontSize: 20, height: 1.45, fontWeight: FontWeight.w800)),
          Visuais(c.visuais, nome: nome),
        ]),
      ),
      const SizedBox(height: 14),
      Row(mainAxisAlignment: MainAxisAlignment.center, children: [
        for (var i = 0; i < _briefing.length; i++)
          Container(
            width: 10,
            height: 10,
            margin: const EdgeInsets.symmetric(horizontal: 3),
            decoration: BoxDecoration(
                shape: BoxShape.circle, color: i <= _cartao ? p.cor : Cores.linha),
          ),
      ]),
      const SizedBox(height: 14),
      Row(children: [
        Expanded(flex: 2, child: Botao3D.branco(texto: '🔊 OUVIR', onPressed: () => _falar(c.texto))),
        const SizedBox(width: 10),
        Expanded(
          flex: 3,
          child: Botao3D(
            cor: p.cor,
            corSombra: p.corEscura,
            texto: ultimo ? '🚀 COMEÇAR' : 'PRÓXIMO ➜',
            onPressed: () {
              _fala.parar();
              setState(() {
                if (ultimo) {
                  _fase = _Fase.pergunta;
                } else {
                  _cartao++;
                }
              });
              if (ultimo) _iniciarRelogio();
            },
          ),
        ),
      ]),
      if (_cartao == 0 && jaJogou) ...[
        const SizedBox(height: 10),
        Botao3D.branco(
          texto: 'PULAR BRIEFING',
          onPressed: () {
            setState(() => _fase = _Fase.pergunta);
            _iniciarRelogio();
          },
        ),
      ],
    ]);
  }

  Widget _telaPergunta(Planeta p) {
    final item = _lista[_i];
    const rotulos = {
      Escolha: 'Escolha a resposta certa',
      VerdadeiroFalso: 'Verdadeiro ou falso?',
      Completar: 'Complete a frase',
      Ordenar: 'Coloque em ordem',
      Ligar: 'Ligue os pares',
      Separar: 'Separe nos grupos',
    };
    return ListView(padding: const EdgeInsets.fromLTRB(18, 6, 18, 24), children: [
      Text(
        (item.revanche ? '🔁 Revanche: tente de novo' : rotulos[item.e.runtimeType]!).toUpperCase(),
        style: TextStyle(color: p.cor, fontSize: 13, fontWeight: FontWeight.w900),
      ),
      const SizedBox(height: 8),
      VistaExercicio(
        key: ValueKey('ex$_i'),
        exercicio: item.e,
        nome: nome,
        mascote: AvatarGato(s.perfil.gato, tamanho: 48),
        bloqueado: _bloqueado,
        aleatorio: _rnd,
        onResposta: _responder,
        onOuvir: () => _falar(item.e.pergunta),
      ),
    ]);
  }

  Widget _painelRetorno() {
    final r = _resposta!;
    final ok = r.certa;
    final corTexto = ok ? const Color(0xFF2A8A3E) : const Color(0xFFB12A2A);
    return Container(
      width: double.infinity,
      constraints: BoxConstraints(maxHeight: MediaQuery.sizeOf(context).height * 0.55),
      color: ok ? Cores.certoClaro : Cores.erradoClaro,
      padding: const EdgeInsets.fromLTRB(18, 14, 18, 16),
      child: SingleChildScrollView(
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Text('${ok ? '✅' : '💡'} $_tituloRetorno',
              style: TextStyle(fontSize: 22, fontWeight: FontWeight.w900, color: corTexto)),
          if (!ok && (r.respostaCerta ?? '').isNotEmpty)
            Padding(
              padding: const EdgeInsets.only(top: 6),
              child: TextoRico('**Resposta certa:** ${r.respostaCerta}',
                  nome: nome, estilo: TextStyle(fontSize: 17, color: corTexto)),
            ),
          if (r.nota != null)
            Padding(
              padding: const EdgeInsets.only(top: 6),
              child: Text(r.nota!, style: TextStyle(fontSize: 17, color: corTexto)),
            ),
          if (r.explicacao != null)
            Padding(
              padding: const EdgeInsets.only(top: 6),
              child: TextoRico(r.explicacao!,
                  nome: nome, estilo: TextStyle(fontSize: 17, color: corTexto, height: 1.45)),
            ),
          const SizedBox(height: 12),
          Botao3D(
            texto: 'CONTINUAR',
            cor: ok ? const Color(0xFF3DBE5A) : Cores.errado,
            corSombra: ok ? const Color(0xFF2A9A44) : const Color(0xFFD63434),
            onPressed: _proxima,
          ),
        ]),
      ),
    );
  }

  Widget _telaFinal() {
    final f = _final!;
    final p = widget.planeta;
    final proximoNivel = () {
      final i = s.niveis.indexWhere((n) => n.id == nivel.id);
      return i + 1 < s.niveis.length ? s.niveis[i + 1] : null;
    }();
    final seg = f.tempo.inSeconds;
    Widget cartao(String titulo, String valor, Color cor) => Expanded(
          child: Container(
            decoration: BoxDecoration(
              border: Border.all(color: cor, width: 2),
              borderRadius: BorderRadius.circular(16),
            ),
            clipBehavior: Clip.antiAlias,
            child: Column(children: [
              Container(
                width: double.infinity,
                color: cor,
                padding: const EdgeInsets.all(4),
                child: Text(titulo,
                    textAlign: TextAlign.center,
                    style: const TextStyle(color: Colors.white, fontSize: 12, fontWeight: FontWeight.w900)),
              ),
              Padding(
                padding: const EdgeInsets.symmetric(vertical: 10),
                child: Text(valor,
                    style: TextStyle(color: cor, fontSize: 21, fontWeight: FontWeight.w900)),
              ),
            ]),
          ),
        );
    Widget aviso(String t) => Container(
          width: double.infinity,
          margin: const EdgeInsets.only(top: 12),
          padding: const EdgeInsets.all(10),
          decoration: BoxDecoration(
              color: const Color(0xFFFFF4CC), borderRadius: BorderRadius.circular(14)),
          child: Text(t,
              textAlign: TextAlign.center,
              style: const TextStyle(color: Color(0xFF7A5A00), fontSize: 16)),
        );
    return FundoEspacial(
      child: SafeArea(
        child: ListView(padding: const EdgeInsets.fromLTRB(20, 30, 20, 30), children: [
          Text(chefao ? '👑' : f.estrelas == 3 ? '🏆' : '🚀',
              textAlign: TextAlign.center, style: const TextStyle(fontSize: 80)),
          Text(chefao ? 'Você derrotou o ${p.chefaoNome}!' : 'Missão cumprida!',
              textAlign: TextAlign.center,
              style: const TextStyle(color: Color(0xFFFFB100), fontSize: 28, fontWeight: FontWeight.w900)),
          Text.rich(
            TextSpan(children: [
              for (var i = 0; i < 3; i++)
                TextSpan(
                    text: '★',
                    style: TextStyle(color: i < f.estrelas ? Cores.ouro : const Color(0xFF2E3780))),
            ]),
            textAlign: TextAlign.center,
            style: const TextStyle(fontSize: 54, letterSpacing: 8),
          ),
          Text(
            f.estrelas == 3
                ? 'Perfeito, $nome! A tripulação está miando de alegria! 😻'
                : f.estrelas == 2
                    ? 'Muito bem! Falta pouco para 3 estrelas!'
                    : 'Missão completa! Jogue de novo para ganhar mais estrelas. 💪',
            textAlign: TextAlign.center,
            style: const TextStyle(color: Color(0xFFC9CFF5), fontSize: 18),
          ),
          if (chefao)
            aviso('🏅 ${p.nome} conquistado no nível ${nivel.emoji} ${nivel.nome}!'
                '${proximoNivel != null ? '\nQue tal tentar o nível ${proximoNivel.emoji} ${proximoNivel.nome}?' : '\nVocê é um verdadeiro Gênio do Universo! 🌌'}'),
          if (f.subiuNivel) aviso('⬆️ Subiu para o nível ${f.novoNivel}: ${f.novaPatente}!'),
          if (f.bateuMeta) aviso('🎯 Meta do dia batida!'),
          const SizedBox(height: 18),
          Row(children: [
            cartao('XP', '⚡${f.xp}', Cores.ouro),
            const SizedBox(width: 10),
            cartao('PEIXINHOS', '🐟${f.peixinhos}', Cores.azulAcao),
            const SizedBox(width: 10),
            cartao('ACERTOS', '${f.acerto}%', const Color(0xFF3DBE5A)),
          ]),
          const SizedBox(height: 8),
          Text('⏱️ ${seg ~/ 60}:${(seg % 60).toString().padLeft(2, '0')} · ${nivel.emoji} ${nivel.nome}',
              textAlign: TextAlign.center, style: const TextStyle(color: Cores.textoClaro)),
          const SizedBox(height: 22),
          if (!chefao) ...[
            const Text('Quer dar uma pausa antes da próxima missão?',
                textAlign: TextAlign.center, style: TextStyle(color: Color(0xFFC9CFF5))),
            const SizedBox(height: 8),
            Botao3D.ouro(
                texto: '🌌 LABIRINTO ORBITAL',
                onPressed: () => context.go(
                    '/c/${s.perfil.id}/p/${widget.planeta.id}/labirinto/${widget.indice}')),
            const SizedBox(height: 10),
          ],
          Botao3D(cor: p.cor, corSombra: p.corEscura, texto: 'VOLTAR PARA A NAVE', onPressed: _voltar),
          if (f.estrelas < 3) ...[
            const SizedBox(height: 10),
            Botao3D.branco(texto: '🔁 JOGAR DE NOVO', onPressed: () => setState(_comecar)),
          ],
        ]),
      ),
    );
  }
}

class _Final {
  final int estrelas;
  final int xp;
  final int peixinhos;
  final int acerto;
  final Duration tempo;
  final bool subiuNivel;
  final int novoNivel;
  final String novaPatente;
  final bool bateuMeta;

  _Final({
    required this.estrelas,
    required this.xp,
    required this.peixinhos,
    required this.acerto,
    required this.tempo,
    required this.subiuNivel,
    required this.novoNivel,
    required this.novaPatente,
    required this.bateuMeta,
  });
}
