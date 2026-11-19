import 'package:material_ui/material_ui.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';

import '../../models/perfil.dart';
import '../../providers.dart';

/// Tela inicial: "Quem vai jogar?" com os perfis das crianças.
class TelaPerfis extends ConsumerWidget {
  const TelaPerfis({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final perfis = ref.watch(perfisProvider);
    return Scaffold(
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(24),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              const SizedBox(height: 16),
              Text('Trilha do Saber',
                  textAlign: TextAlign.center,
                  style: Theme.of(context).textTheme.headlineMedium?.copyWith(
                      fontWeight: FontWeight.w800,
                      color: Theme.of(context).colorScheme.primary)),
              const SizedBox(height: 8),
              Text('Quem vai jogar?',
                  textAlign: TextAlign.center,
                  style: Theme.of(context).textTheme.titleLarge),
              const SizedBox(height: 24),
              Expanded(
                child: perfis.when(
                  loading: () =>
                      const Center(child: CircularProgressIndicator()),
                  error: (e, _) =>
                      Center(child: Text('Erro ao carregar perfis: $e')),
                  data: (lista) => GridView.count(
                    crossAxisCount: 2,
                    mainAxisSpacing: 16,
                    crossAxisSpacing: 16,
                    children: [
                      for (final p in lista) _CartaoPerfil(perfil: p),
                      _CartaoAdicionar(
                          onTap: () => context.go('/novo-perfil')),
                    ],
                  ),
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

  const _CartaoPerfil({required this.perfil});

  Future<void> _confirmarRemocao(BuildContext context, WidgetRef ref) async {
    final ok = await showDialog<bool>(
      context: context,
      builder: (context) => AlertDialog(
        title: Text('Remover ${perfil.nome}?'),
        content: const Text('O progresso desta criança será apagado.'),
        actions: [
          TextButton(
              onPressed: () => Navigator.pop(context, false),
              child: const Text('Cancelar')),
          TextButton(
              onPressed: () => Navigator.pop(context, true),
              child: const Text('Remover')),
        ],
      ),
    );
    if (ok == true) await ref.read(acoesProvider).removerPerfil(perfil.id);
  }

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    return Card(
      color: Colors.white,
      child: InkWell(
        borderRadius: BorderRadius.circular(20),
        onTap: () => context.go('/perfil/${perfil.id}'),
        onLongPress: () => _confirmarRemocao(context, ref),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(perfil.avatar, style: const TextStyle(fontSize: 56)),
            const SizedBox(height: 8),
            Text(perfil.nome,
                style: Theme.of(context)
                    .textTheme
                    .titleMedium
                    ?.copyWith(fontWeight: FontWeight.bold)),
            Text('${perfil.ano}º ano'),
          ],
        ),
      ),
    );
  }
}

class _CartaoAdicionar extends StatelessWidget {
  final VoidCallback onTap;

  const _CartaoAdicionar({required this.onTap});

  @override
  Widget build(BuildContext context) {
    final cor = Theme.of(context).colorScheme.primary;
    return Card(
      color: cor.withValues(alpha: 0.08),
      child: InkWell(
        borderRadius: BorderRadius.circular(20),
        onTap: onTap,
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(Icons.add_circle, size: 56, color: cor),
            const SizedBox(height: 8),
            Text('Adicionar criança',
                textAlign: TextAlign.center,
                style: TextStyle(color: cor, fontWeight: FontWeight.bold)),
          ],
        ),
      ),
    );
  }
}
