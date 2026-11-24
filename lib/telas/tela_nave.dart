import 'dart:math';

import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:material_ui/material_ui.dart';

import '../componentes/hud.dart';
import '../componentes/nave.dart';
import '../componentes/reacao_gatos.dart';
import '../componentes/tema.dart';
import '../logica/nave.dart';
import '../providers.dart';

/// Hangar da Nave Gatística: estoque de suprimentos e peças para construir.
class TelaNave extends ConsumerStatefulWidget {
  final String perfilId;
  const TelaNave({super.key, required this.perfilId});

  @override
  ConsumerState<TelaNave> createState() => _TelaNaveState();
}

class _TelaNaveState extends ConsumerState<TelaNave> {
  String? _ultima;
  int _disparo = 0;
  final _rnd = Random();

  Future<void> _construir(Sessao s, PecaNave peca) async {
    final etapasAntes = etapasCompletas(s.progresso.pecas);
    final ok = await ref.read(acoesProvider).construirPeca(s.perfil.id, peca);
    if (!ok || !mounted) return;
    setState(() {
      _ultima = peca.id;
      _disparo++;
    });
    final pecas = {...s.progresso.pecas, peca.id};
    if (etapasCompletas(pecas) > etapasAntes) {
      final etapa = etapasCompletas(pecas);
      await showDialog<void>(
        context: context,
        builder: (c) => Dialog(
          backgroundColor: Cores.espaco,
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(24)),
          child: Padding(
            padding: const EdgeInsets.all(22),
            child: Column(mainAxisSize: MainAxisSize.min, children: [
              Text(navePronta(pecas) ? 'A Nave Gatística está pronta!' : 'Etapa $etapa completa!',
                  textAlign: TextAlign.center,
                  style: const TextStyle(color: Cores.ouro, fontSize: 24, fontWeight: FontWeight.w900)),
              const SizedBox(height: 8),
              NaveGatistica(pecas: pecas, tamanho: 150, fantasmas: false),
              const SizedBox(height: 8),
              Text(
                navePronta(pecas)
                    ? 'Motor de salto ligado! Quando você passar de ano, a nave leva a tripulação para o Universo do ${s.perfil.ano + 1}º ano. 🌀😻'
                    : '${etapasNave[etapa - 1]} concluída! Agora começa a etapa ${etapa + 1}: ${etapasNave[etapa]}.',
                textAlign: TextAlign.center,
                style: const TextStyle(color: Colors.white, fontSize: 17),
              ),
              const SizedBox(height: 16),
              Botao3D.ouro(texto: 'MIAU-RAVILHA!', onPressed: () => Navigator.pop(c)),
            ]),
          ),
        ),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    final sessao = ref.watch(sessaoProvider(widget.perfilId));
    return Scaffold(
      body: FundoEspacial(
        child: sessao.when(
          skipLoadingOnReload: true,
          loading: () => const Center(child: CircularProgressIndicator()),
          error: (e, _) => Center(child: Text('Erro: $e')),
          data: (s) => s == null
              ? const Center(child: Text('Astronauta não encontrado.'))
              : Stack(children: [
                  _conteudo(context, s),
                  Positioned.fill(
                      child: ReacaoGatos(disparo: _disparo, acerto: true, aleatorio: _rnd)),
                ]),
        ),
      ),
    );
  }

  Widget _conteudo(BuildContext context, Sessao s) {
    final pecas = s.progresso.pecas;
    final estoque = s.progresso.suprimentos;
    final etapa = etapaAtual(pecas);
    return Column(children: [
      Hud(sessao: s),
      Expanded(
        child: ListView(
          padding: const EdgeInsets.fromLTRB(16, 8, 16, 40),
          children: [
            Align(
              alignment: Alignment.centerLeft,
              child: IconButton(
                tooltip: 'Voltar para o universo',
                icon: const Icon(Icons.arrow_back, color: Colors.white),
                onPressed: () => context.go('/c/${s.perfil.id}'),
              ),
            ),
            const Text('🛠️ Hangar da Nave Gatística',
                textAlign: TextAlign.center,
                style: TextStyle(color: Colors.white, fontSize: 24, fontWeight: FontWeight.w900)),
            const SizedBox(height: 4),
            Text(
              navePronta(pecas)
                  ? 'A nave está pronta para levar a tripulação ao próximo universo!'
                  : 'Cada missão rende suprimentos da matéria. Junte e construa as peças!',
              textAlign: TextAlign.center,
              style: const TextStyle(color: Color(0xFFC9CFF5), fontSize: 15),
            ),
            const SizedBox(height: 10),
            Center(child: NaveGatistica(pecas: pecas, tamanho: 210, destaque: _ultima)),
            const SizedBox(height: 6),
            BarraProgresso(valor: pecas.length / pecasNave.length, cor: Cores.ciano, altura: 12),
            const SizedBox(height: 4),
            Text('${pecas.length}/${pecasNave.length} peças',
                textAlign: TextAlign.center, style: const TextStyle(color: Cores.textoClaro)),
            const SizedBox(height: 14),
            const Text('SUPRIMENTOS', textAlign: TextAlign.center, style: TextStyle(color: Cores.textoClaro)),
            const SizedBox(height: 6),
            Wrap(
              alignment: WrapAlignment.center,
              spacing: 8,
              runSpacing: 8,
              children: [
                for (final sup in suprimentos)
                  Container(
                    width: 104,
                    padding: const EdgeInsets.symmetric(vertical: 8, horizontal: 6),
                    decoration: BoxDecoration(
                      color: Colors.white.withValues(alpha: 0.08),
                      borderRadius: BorderRadius.circular(14),
                      border: Border.all(color: Colors.white24),
                    ),
                    child: Column(children: [
                      Text('${sup.emoji} ${estoque[sup.materia] ?? 0}',
                          style: const TextStyle(
                              color: Colors.white, fontSize: 18, fontWeight: FontWeight.w900)),
                      Text(sup.nome,
                          textAlign: TextAlign.center,
                          style: const TextStyle(color: Cores.textoClaro, fontSize: 11)),
                    ]),
                  ),
              ],
            ),
            for (var e = 1; e <= etapasNave.length; e++) ...[
              const SizedBox(height: 18),
              Text(
                'ETAPA $e · ${etapasNave[e - 1].toUpperCase()}'
                '${e < etapa ? ' ✅' : e > etapa ? ' 🔒' : ''}',
                textAlign: TextAlign.center,
                style: TextStyle(
                    color: e == etapa ? Cores.ouro : Cores.textoClaro, fontWeight: FontWeight.w900),
              ),
              const SizedBox(height: 6),
              for (final peca in pecasNave.where((p) => p.etapa == e))
                _CartaoPeca(
                  peca: peca,
                  feita: pecas.contains(peca.id),
                  liberada: pecaLiberada(peca, pecas),
                  podePagar: podePagar(peca, estoque),
                  estoque: estoque,
                  onConstruir: () => _construir(s, peca),
                ),
            ],
          ],
        ),
      ),
    ]);
  }
}

class _CartaoPeca extends StatelessWidget {
  final PecaNave peca;
  final bool feita;
  final bool liberada;
  final bool podePagar;
  final Map<String, int> estoque;
  final VoidCallback onConstruir;

  const _CartaoPeca({
    required this.peca,
    required this.feita,
    required this.liberada,
    required this.podePagar,
    required this.estoque,
    required this.onConstruir,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: const EdgeInsets.only(bottom: 8),
      padding: const EdgeInsets.all(10),
      decoration: BoxDecoration(
        color: feita ? const Color(0xFF1E3A2A) : const Color(0xFF151A4A),
        borderRadius: BorderRadius.circular(16),
        border: Border.all(
            color: feita
                ? Cores.certo
                : liberada && podePagar
                    ? Cores.ouro
                    : Colors.white24,
            width: 2),
      ),
      child: Row(children: [
        Text(peca.emoji, style: const TextStyle(fontSize: 30)),
        const SizedBox(width: 10),
        Expanded(
          child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Text(peca.nome,
                style: const TextStyle(color: Colors.white, fontSize: 16, fontWeight: FontWeight.w900)),
            Wrap(spacing: 8, children: [
              for (final c in peca.custo.entries)
                Text(
                    feita
                        ? '${suprimentoDe(c.key).emoji} ${c.value}'
                        : '${suprimentoDe(c.key).emoji} ${estoque[c.key] ?? 0}/${c.value}',
                    style: TextStyle(
                        color: feita || (estoque[c.key] ?? 0) >= c.value
                            ? Cores.certoClaro
                            : const Color(0xFFFFB3B3),
                        fontSize: 13,
                        fontWeight: FontWeight.w900)),
            ]),
          ]),
        ),
        if (feita)
          const Text('✅', style: TextStyle(fontSize: 24))
        else if (liberada)
          SizedBox(
            width: 112,
            child: Botao3D.ouro(
              texto: 'CONSTRUIR',
              altura: 42,
              onPressed: podePagar ? onConstruir : null,
            ),
          )
        else
          const Text('🔒', style: TextStyle(fontSize: 22)),
      ]),
    );
  }
}
