import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:material_ui/material_ui.dart';

import '../componentes/astros.dart';
import '../componentes/hud.dart';
import '../componentes/tema.dart';
import '../logica/regras.dart';
import '../modelos/conteudo.dart';
import '../providers.dart';

/// Uma galáxia (matéria): os planetas (assuntos) do ano, bimestre a
/// bimestre, e a estação do chefão no fim de cada bimestre.
class TelaGalaxia extends ConsumerWidget {
  final String perfilId;
  final String materia;
  const TelaGalaxia({super.key, required this.perfilId, required this.materia});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final sessao = ref.watch(sessaoProvider(perfilId));
    return Scaffold(
      body: FundoEspacial(
        child: sessao.when(
          skipLoadingOnReload: true,
          loading: () => const Center(child: CircularProgressIndicator()),
          error: (e, _) => Center(child: Text('Erro: $e')),
          data: (s) {
            final partes = s == null ? const [] : partesDaGalaxia(s.conteudo, materia);
            if (s == null || partes.isEmpty) {
              return const Center(
                  child: Text('Galáxia não encontrada.', style: TextStyle(color: Colors.white)));
            }
            return _Mapa(s: s, materia: materia);
          },
        ),
      ),
    );
  }
}

class _Mapa extends StatefulWidget {
  final Sessao s;
  final String materia;
  const _Mapa({required this.s, required this.materia});

  @override
  State<_Mapa> createState() => _MapaState();
}

class _MapaState extends State<_Mapa> {
  final _chaveAtual = GlobalKey();

  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addPostFrameCallback((_) {
      final c = _chaveAtual.currentContext;
      final ro = c?.findRenderObject();
      if (c != null && ro is RenderBox && ro.hasSize) Scrollable.ensureVisible(c, alignment: 0.1);
    });
  }

  @override
  Widget build(BuildContext context) {
    final s = widget.s;
    final info = galaxiaDe(widget.materia);
    final partes = partesDaGalaxia(s.conteudo, widget.materia);
    final cor = partes.first.planeta.cor;
    final escura = partes.first.planeta.corEscura;
    final provas = s.provasProximas.where((p) => p.materia == widget.materia).toList();
    var ganhas = 0, maximo = 0;
    for (final x in partes) {
      if (!s.bimestreAberto(x.bimestre.numero)) continue;
      final r = s.regras(x.planeta).resumo;
      ganhas += r.ganhas;
      maximo += r.maximo;
    }
    final filhos = <Widget>[];
    var k = 0;
    for (final x in partes) {
      final aberto = s.bimestreAberto(x.bimestre.numero);
      final r = s.regras(x.planeta);
      filhos.add(Padding(
        key: x.bimestre.numero == s.bimestreAtual ? _chaveAtual : null,
        padding: const EdgeInsets.fromLTRB(4, 18, 4, 8),
        child: Text(
          '${x.bimestre.numero}º BIMESTRE${aberto ? (x.bimestre.numero == s.bimestreAtual ? ' · AGORA' : '') : ' · 🔒 ABRE DEPOIS'}',
          textAlign: TextAlign.center,
          style: const TextStyle(color: Cores.textoClaro, fontWeight: FontWeight.w900),
        ),
      ));
      for (var i = 0; i < x.planeta.setores.length; i++) {
        final setor = x.planeta.setores[i];
        final prova = provas.where((p) => p.assuntos.contains(setor.id)).firstOrNull;
        filhos.add(_CartaoPlaneta(
          planeta: x.planeta,
          setor: setor,
          resumo: r.resumoDoSetor(i),
          aberto: aberto,
          temConteudo: r.indicesDoSetor(i).any((j) => !emBreve(r.nos[j]) && r.nos[j] is! NoCapsula),
          deslocamento: [0.0, 24, 0, -24][k++ % 4].toDouble(),
          prova: prova == null
              ? null
              : '📝 Cai na prova de ${prova.data.day.toString().padLeft(2, '0')}/${prova.data.month.toString().padLeft(2, '0')}',
          onTap: () {
            if (!aberto) {
              _avisar(context, 'Este planeta abre no ${x.bimestre.numero}º bimestre. 🔒');
              return;
            }
            context.go('/c/${s.perfil.id}/p/${x.planeta.id}/s/$i');
          },
        ));
      }
      filhos.add(_CartaoChefao(
        planeta: x.planeta,
        aberto: aberto,
        vencido: r.resumo.chefao,
        onTap: () {
          if (!aberto) {
            _avisar(context, 'Esta estação abre no ${x.bimestre.numero}º bimestre. 🔒');
            return;
          }
          context.go('/c/${s.perfil.id}/p/${x.planeta.id}/s/-1');
        },
      ));
    }
    return Column(children: [
      Container(
        color: cor,
        padding: EdgeInsets.fromLTRB(4, MediaQuery.paddingOf(context).top + 4, 14, 12),
        child: Row(children: [
          IconButton(
            tooltip: 'Voltar para o universo',
            icon: const Icon(Icons.arrow_back, color: Colors.white),
            onPressed: () => context.go('/c/${s.perfil.id}'),
          ),
          DesenhoGalaxia(cor: Colors.white, emoji: info.emoji, tamanho: 48),
          const SizedBox(width: 8),
          Expanded(
            child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              Text(info.nome,
                  style: const TextStyle(color: Colors.white, fontSize: 20, fontWeight: FontWeight.w900)),
              Text('${nomesMaterias[widget.materia]} · ⭐ $ganhas/$maximo',
                  style: const TextStyle(color: Colors.white, fontSize: 13)),
              const SizedBox(height: 4),
              BarraProgresso(
                  valor: maximo == 0 ? 0 : ganhas / maximo,
                  cor: Colors.white,
                  fundo: escura,
                  altura: 8),
            ]),
          ),
        ]),
      ),
      Expanded(
        // Coluna (e não ListView) para dar para rolar até o bimestre atual.
        child: SingleChildScrollView(
          padding: const EdgeInsets.fromLTRB(16, 4, 16, 40),
          child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
            const SizedBox(height: 10),
            const Text('Cada planeta é um assunto. Toque para explorar!',
                textAlign: TextAlign.center, style: TextStyle(color: Color(0xFFC9CFF5))),
            ...filhos,
          ]),
        ),
      ),
    ]);
  }

  void _avisar(BuildContext context, String texto) => ScaffoldMessenger.of(context)
    ..hideCurrentSnackBar()
    ..showSnackBar(SnackBar(content: Text(texto)));
}

class _CartaoPlaneta extends StatelessWidget {
  final Planeta planeta;
  final Setor setor;
  final ({int ganhas, int maximo, int feitas, int total}) resumo;
  final bool aberto;
  final bool temConteudo;
  final double deslocamento;
  final String? prova;
  final VoidCallback onTap;

  const _CartaoPlaneta({
    required this.planeta,
    required this.setor,
    required this.resumo,
    required this.aberto,
    required this.temConteudo,
    required this.deslocamento,
    required this.prova,
    required this.onTap,
  });

  @override
  Widget build(BuildContext context) {
    final completo = resumo.total > 0 && resumo.feitas == resumo.total;
    return Padding(
      padding: EdgeInsets.only(
          bottom: 10, left: deslocamento > 0 ? deslocamento : 0, right: deslocamento < 0 ? -deslocamento : 0),
      child: Semantics(
        button: true,
        label: setor.titulo,
        child: GestureDetector(
          onTap: onTap,
          child: Opacity(
            opacity: aberto ? 1 : 0.55,
            child: Container(
              padding: const EdgeInsets.all(10),
              decoration: BoxDecoration(
                color: const Color(0xFF151A4A),
                borderRadius: BorderRadius.circular(22),
                border: Border.all(
                    color: prova != null ? Cores.ouro : (aberto ? planeta.cor : Colors.white24),
                    width: 3),
              ),
              child: Row(children: [
                Stack(clipBehavior: Clip.none, children: [
                  DesenhoPlaneta(cor: planeta.cor, semente: setor.id, tamanho: 74, apagado: !aberto),
                  if (completo)
                    const Positioned(right: 0, top: 0, child: Text('🏅', style: TextStyle(fontSize: 22))),
                  if (!aberto)
                    const Positioned.fill(
                        child: Center(child: Text('🔒', style: TextStyle(fontSize: 24)))),
                ]),
                const SizedBox(width: 10),
                Expanded(
                  child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                    Text(setor.titulo,
                        style: const TextStyle(
                            fontSize: 17, fontWeight: FontWeight.w900, color: Colors.white)),
                    if (setor.subtitulo.isNotEmpty)
                      Text(setor.subtitulo,
                          maxLines: 2,
                          overflow: TextOverflow.ellipsis,
                          style: const TextStyle(fontSize: 10, color: Cores.textoClaro)),
                    const SizedBox(height: 5),
                    if (temConteudo) ...[
                      BarraProgresso(
                          valor: resumo.maximo == 0 ? 0 : resumo.ganhas / resumo.maximo,
                          cor: planeta.cor,
                          altura: 8),
                      const SizedBox(height: 3),
                      Text('⭐ ${resumo.ganhas}/${resumo.maximo} · ${resumo.feitas}/${resumo.total} missões',
                          style: const TextStyle(fontSize: 12, color: Cores.ouro)),
                    ] else
                      const Text('🛠️ Missões em construção',
                          style: TextStyle(fontSize: 12, color: Cores.ouro)),
                    if (prova != null)
                      Text(prova!,
                          style: const TextStyle(
                              fontSize: 12, color: Cores.ouro, fontWeight: FontWeight.w900)),
                  ]),
                ),
              ]),
            ),
          ),
        ),
      ),
    );
  }
}

class _CartaoChefao extends StatelessWidget {
  final Planeta planeta;
  final bool aberto;
  final bool vencido;
  final VoidCallback onTap;
  const _CartaoChefao(
      {required this.planeta, required this.aberto, required this.vencido, required this.onTap});

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 6),
      child: GestureDetector(
        onTap: onTap,
        child: Opacity(
          opacity: aberto ? 1 : 0.55,
          child: Container(
            padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
            decoration: BoxDecoration(
              gradient: const LinearGradient(colors: [Color(0xFF5B1468), Color(0xFF2A0733)]),
              borderRadius: BorderRadius.circular(18),
            ),
            child: Row(children: [
              Text(planeta.chefaoEmoji, style: const TextStyle(fontSize: 34)),
              const SizedBox(width: 10),
              Expanded(
                child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                  const Text('ESTAÇÃO DO CHEFÃO',
                      style: TextStyle(color: Colors.white70, fontSize: 11, fontWeight: FontWeight.w900)),
                  Text(planeta.chefaoNome,
                      style: const TextStyle(color: Colors.white, fontSize: 16, fontWeight: FontWeight.w900)),
                ]),
              ),
              Text(vencido ? '👑' : (aberto ? '⚔️' : '🔒'), style: const TextStyle(fontSize: 26)),
            ]),
          ),
        ),
      ),
    );
  }
}
