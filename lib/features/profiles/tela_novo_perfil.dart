import 'package:material_ui/material_ui.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';

import '../../models/perfil.dart';
import '../../providers.dart';

/// Cadastro de uma criança: nome, ano escolar e avatar.
class TelaNovoPerfil extends ConsumerStatefulWidget {
  const TelaNovoPerfil({super.key});

  @override
  ConsumerState<TelaNovoPerfil> createState() => _TelaNovoPerfilState();
}

class _TelaNovoPerfilState extends ConsumerState<TelaNovoPerfil> {
  final _nome = TextEditingController();
  int? _ano;
  String _avatar = avataresDisponiveis.first;
  bool _salvando = false;

  bool get _valido => _nome.text.trim().isNotEmpty && _ano != null;

  @override
  void dispose() {
    _nome.dispose();
    super.dispose();
  }

  Future<void> _salvar() async {
    setState(() => _salvando = true);
    final perfil = PerfilCrianca(
      id: DateTime.now().microsecondsSinceEpoch.toString(),
      nome: _nome.text.trim(),
      ano: _ano!,
      avatar: _avatar,
    );
    await ref.read(acoesProvider).salvarPerfil(perfil);
    if (mounted) context.go('/');
  }

  @override
  Widget build(BuildContext context) {
    final titulo = Theme.of(context).textTheme.titleMedium;
    return Scaffold(
      appBar: AppBar(title: const Text('Nova criança')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: [
          Text('Nome', style: titulo),
          const SizedBox(height: 8),
          TextField(
            key: const Key('campoNome'),
            controller: _nome,
            textCapitalization: TextCapitalization.words,
            decoration: const InputDecoration(
              hintText: 'Como a criança se chama?',
              border: OutlineInputBorder(),
            ),
            onChanged: (_) => setState(() {}),
          ),
          const SizedBox(height: 24),
          Text('Ano escolar', style: titulo),
          const SizedBox(height: 8),
          Wrap(
            spacing: 8,
            runSpacing: 8,
            children: [
              for (var ano = 1; ano <= 5; ano++)
                ChoiceChip(
                  label: Text('$anoº ano'),
                  selected: _ano == ano,
                  onSelected: (_) => setState(() => _ano = ano),
                ),
            ],
          ),
          const SizedBox(height: 24),
          Text('Escolha um avatar', style: titulo),
          const SizedBox(height: 8),
          Wrap(
            spacing: 12,
            runSpacing: 12,
            children: [
              for (final a in avataresDisponiveis)
                GestureDetector(
                  onTap: () => setState(() => _avatar = a),
                  child: Container(
                    padding: const EdgeInsets.all(8),
                    decoration: BoxDecoration(
                      shape: BoxShape.circle,
                      color: _avatar == a
                          ? Theme.of(context).colorScheme.primaryContainer
                          : Colors.transparent,
                    ),
                    child: Text(a, style: const TextStyle(fontSize: 40)),
                  ),
                ),
            ],
          ),
          const SizedBox(height: 32),
          FilledButton(
            onPressed: _valido && !_salvando ? _salvar : null,
            child: const Text('Salvar'),
          ),
        ],
      ),
    );
  }
}
