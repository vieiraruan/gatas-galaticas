import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:material_ui/material_ui.dart';

import '../componentes/gatos.dart';
import '../componentes/tema.dart';
import '../modelos/perfil.dart';
import '../providers.dart';

/// Cadastro (ou edição) de uma criança: nome, ano e gatinho capitão.
class TelaNovoPerfil extends ConsumerStatefulWidget {
  final String? perfilId;
  const TelaNovoPerfil({super.key, this.perfilId});

  @override
  ConsumerState<TelaNovoPerfil> createState() => _TelaNovoPerfilState();
}

class _TelaNovoPerfilState extends ConsumerState<TelaNovoPerfil> {
  final _nome = TextEditingController();
  int? _ano;
  String _gato = gatos.first.id;
  PerfilCrianca? _original;
  bool _carregado = false;

  bool get _valido => _nome.text.trim().isNotEmpty && _ano != null;

  @override
  void dispose() {
    _nome.dispose();
    super.dispose();
  }

  void _carregar(List<PerfilCrianca> perfis) {
    if (_carregado) return;
    _carregado = true;
    final p = perfis.where((p) => p.id == widget.perfilId).firstOrNull;
    if (p != null) {
      _original = p;
      _nome.text = p.nome;
      _ano = p.ano;
      _gato = p.gato;
    }
  }

  Future<void> _salvar() async {
    final nome = _nome.text.trim();
    final perfil = _original?.copyWith(
            nome: nome[0].toUpperCase() + nome.substring(1), ano: _ano, gato: _gato) ??
        PerfilCrianca(
          id: DateTime.now().microsecondsSinceEpoch.toString(),
          nome: nome[0].toUpperCase() + nome.substring(1),
          ano: _ano!,
          gato: _gato,
        );
    await ref.read(acoesProvider).salvarPerfil(perfil);
    if (mounted) context.go(_original == null ? '/' : '/c/${perfil.id}');
  }

  @override
  Widget build(BuildContext context) {
    final perfis = ref.watch(perfisProvider).value;
    if (perfis != null) _carregar(perfis);
    const rotulo = TextStyle(fontSize: 16, color: Cores.textoClaro, fontWeight: FontWeight.w900);
    return Scaffold(
      body: FundoEspacial(
        child: SafeArea(
          child: ListView(
            padding: const EdgeInsets.fromLTRB(20, 8, 20, 32),
            children: [
              Align(
                alignment: Alignment.centerLeft,
                child: IconButton(
                  tooltip: 'Voltar',
                  icon: const Icon(Icons.arrow_back, color: Colors.white),
                  onPressed: () => context.go(_original == null ? '/' : '/c/${_original!.id}'),
                ),
              ),
              const Text('🧑‍🚀', textAlign: TextAlign.center, style: TextStyle(fontSize: 60)),
              Text(_original == null ? 'Olá, astronauta!' : 'Editar astronauta',
                  textAlign: TextAlign.center,
                  style: const TextStyle(
                      fontSize: 28, fontWeight: FontWeight.w900, color: Cores.ouro)),
              const SizedBox(height: 20),
              const Text('QUAL É O SEU NOME?', style: rotulo),
              const SizedBox(height: 8),
              TextField(
                key: const Key('campoNome'),
                controller: _nome,
                maxLength: 20,
                textCapitalization: TextCapitalization.words,
                style: const TextStyle(fontSize: 22, fontWeight: FontWeight.w900),
                decoration: InputDecoration(
                  counterText: '',
                  filled: true,
                  fillColor: Colors.white,
                  hintText: 'Digite o nome',
                  border: OutlineInputBorder(borderRadius: BorderRadius.circular(16)),
                ),
                onChanged: (_) => setState(() {}),
              ),
              const SizedBox(height: 20),
              const Text('EM QUE ANO VOCÊ ESTÁ?', style: rotulo),
              const SizedBox(height: 8),
              Row(
                children: [
                  for (var a = 1; a <= 5; a++)
                    Expanded(
                      child: Padding(
                        padding: const EdgeInsets.symmetric(horizontal: 3),
                        child: _BotaoAno(
                          ano: a,
                          escolhido: _ano == a,
                          onTap: () => setState(() => _ano = a),
                        ),
                      ),
                    ),
                ],
              ),
              const SizedBox(height: 20),
              const Text('QUEM VAI COMANDAR A NAVE?', style: rotulo),
              const SizedBox(height: 8),
              GridView.count(
                shrinkWrap: true,
                physics: const NeverScrollableScrollPhysics(),
                crossAxisCount: 3,
                mainAxisSpacing: 10,
                crossAxisSpacing: 10,
                childAspectRatio: 0.72,
                children: [
                  for (final g in gatos)
                    GestureDetector(
                      onTap: () => setState(() => _gato = g.id),
                      child: Container(
                        padding: const EdgeInsets.all(6),
                        decoration: BoxDecoration(
                          color: _gato == g.id ? const Color(0xFFEEEBFF) : Colors.white,
                          borderRadius: BorderRadius.circular(20),
                          border: Border.all(
                              color: _gato == g.id ? Cores.roxo : Cores.linha, width: 3),
                        ),
                        child: Column(
                          mainAxisAlignment: MainAxisAlignment.center,
                          children: [
                            AvatarGato(g.id, tamanho: 58),
                            Text(g.nome,
                                textAlign: TextAlign.center,
                                style: const TextStyle(fontSize: 13, fontWeight: FontWeight.w900)),
                            Text(g.descricao,
                                textAlign: TextAlign.center,
                                maxLines: 2,
                                overflow: TextOverflow.ellipsis,
                                style: const TextStyle(fontSize: 10, color: Cores.apagado)),
                          ],
                        ),
                      ),
                    ),
                ],
              ),
              const SizedBox(height: 24),
              Botao3D.ouro(
                texto: _original == null ? '🚀 DECOLAR!' : 'SALVAR',
                onPressed: _valido ? _salvar : null,
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class _BotaoAno extends StatelessWidget {
  final int ano;
  final bool escolhido;
  final VoidCallback onTap;
  const _BotaoAno({required this.ano, required this.escolhido, required this.onTap});

  @override
  Widget build(BuildContext context) {
    return Semantics(
      button: true,
      selected: escolhido,
      label: '$anoº ano',
      child: GestureDetector(
        onTap: onTap,
        child: Container(
          height: 64,
          alignment: Alignment.center,
          decoration: BoxDecoration(
            color: escolhido ? Cores.ouro : Colors.white,
            borderRadius: BorderRadius.circular(16),
            border: Border.all(color: escolhido ? Cores.ouroEscuro : Cores.linha, width: 3),
          ),
          child: Column(mainAxisAlignment: MainAxisAlignment.center, children: [
            Text('$anoº',
                style: const TextStyle(fontSize: 22, fontWeight: FontWeight.w900)),
            const Text('ano', style: TextStyle(fontSize: 12)),
          ]),
        ),
      ),
    );
  }
}
