import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:material_ui/material_ui.dart';

import '../componentes/gatos.dart';
import '../componentes/tema.dart';
import '../modelos/perfil.dart';
import '../providers.dart';

/// "Quem vai decolar?": escolha da criança.
class TelaPerfis extends ConsumerWidget {
  const TelaPerfis({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final perfis = ref.watch(perfisProvider);
    return Scaffold(
      body: FundoEspacial(
        child: SafeArea(
          child: ListView(
            padding: const EdgeInsets.fromLTRB(20, 24, 20, 32),
            children: [
              const Text('🚀', textAlign: TextAlign.center, style: TextStyle(fontSize: 56)),
              const Text('Galáxia do Saber',
                  textAlign: TextAlign.center,
                  style: TextStyle(
                      fontSize: 30, fontWeight: FontWeight.w900, color: Colors.white)),
              const SizedBox(height: 6),
              const Text('Quem vai decolar hoje?',
                  textAlign: TextAlign.center,
                  style: TextStyle(fontSize: 18, color: Cores.textoClaro)),
              const SizedBox(height: 10),
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [for (final g in gatos) AvatarGato(g.id, tamanho: 38)],
              ),
              const SizedBox(height: 24),
              perfis.when(
                loading: () => const Center(child: CircularProgressIndicator()),
                error: (e, _) => Text('Erro: $e', style: const TextStyle(color: Colors.white)),
                data: (lista) => GridView.count(
                  shrinkWrap: true,
                  physics: const NeverScrollableScrollPhysics(),
                  crossAxisCount: 2,
                  mainAxisSpacing: 14,
                  crossAxisSpacing: 14,
                  childAspectRatio: 0.95,
                  children: [
                    for (final p in lista) _CartaoPerfil(p),
                    _CartaoNovo(onTap: () => context.go('/novo-perfil')),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class _CartaoPerfil extends ConsumerWidget {
  final PerfilCrianca perfil;
  const _CartaoPerfil(this.perfil);

  Future<void> _remover(BuildContext context, WidgetRef ref) async {
    final ok = await showDialog<bool>(
      context: context,
      builder: (c) => AlertDialog(
        title: Text('Remover ${perfil.nome}?'),
        content: const Text('Todo o progresso desta criança será apagado.'),
        actions: [
          TextButton(onPressed: () => Navigator.pop(c, false), child: const Text('Cancelar')),
          TextButton(onPressed: () => Navigator.pop(c, true), child: const Text('Remover')),
        ],
      ),
    );
    if (ok == true) await ref.read(acoesProvider).removerPerfil(perfil.id);
  }

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    return Material(
      color: Colors.white,
      borderRadius: BorderRadius.circular(24),
      child: InkWell(
        borderRadius: BorderRadius.circular(24),
        onTap: () {
          ref.read(bimestreEscolhidoProvider.notifier).limpar();
          context.go('/c/${perfil.id}');
        },
        onLongPress: () => _remover(context, ref),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            AvatarGato(perfil.gato, tamanho: 76),
            const SizedBox(height: 8),
            Text(perfil.nome,
                style: const TextStyle(fontSize: 20, fontWeight: FontWeight.w900)),
            Text('${perfil.ano}º ano',
                style: const TextStyle(fontSize: 15, color: Cores.apagado)),
          ],
        ),
      ),
    );
  }
}

class _CartaoNovo extends StatelessWidget {
  final VoidCallback onTap;
  const _CartaoNovo({required this.onTap});

  @override
  Widget build(BuildContext context) {
    return Material(
      color: Colors.white.withValues(alpha: 0.08),
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(24),
        side: const BorderSide(color: Cores.textoClaro, width: 2),
      ),
      child: InkWell(
        borderRadius: BorderRadius.circular(24),
        onTap: onTap,
        child: const Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text('🧑‍🚀', style: TextStyle(fontSize: 50)),
            SizedBox(height: 8),
            Text('Novo astronauta',
                textAlign: TextAlign.center,
                style: TextStyle(
                    fontSize: 17, fontWeight: FontWeight.w900, color: Colors.white)),
          ],
        ),
      ),
    );
  }
}
