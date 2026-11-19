import 'package:material_ui/material_ui.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';

import '../../logic/regras_trilha.dart';
import '../../models/curriculo.dart';
import '../../providers.dart';
import '../../ui/tema.dart';

/// Trilha do ano da criança: missão do dia e os quatro bimestres.
class TelaTrilha extends ConsumerWidget {
  final String perfilId;

  const TelaTrilha({super.key, required this.perfilId});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final estado = ref.watch(estadoTrilhaProvider(perfilId));
    return estado.when(
      skipLoadingOnReload: true,
      loading: () =>
          const Scaffold(body: Center(child: CircularProgressIndicator())),
      error: (e, _) =>
          Scaffold(appBar: AppBar(), body: Center(child: Text('Erro: $e'))),
      data: (e) {
        if (e == null) {
          return Scaffold(
              appBar: AppBar(),
              body: const Center(child: Text('Perfil não encontrado.')));
        }
        return _ConteudoTrilha(estado: e);
      },
    );
  }
}

class _ConteudoTrilha extends StatelessWidget {
  final EstadoTrilha estado;

  const _ConteudoTrilha({required this.estado});

  @override
  Widget build(BuildContext context) {
    final perfil = estado.perfil;
    final regras = estado.regras;
    return Scaffold(
      appBar: AppBar(
        leading: IconButton(
          tooltip: 'Trocar de criança',
          icon: const Icon(Icons.people),
          onPressed: () => context.go('/'),
        ),
        title: Text('${perfil.avatar}  ${perfil.nome} · ${perfil.ano}º ano'),
      ),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          Row(
            children: [
              _Indicador(
                  icone: '⭐',
                  valor: '${estado.progresso.totalEstrelas}',
                  rotulo: 'estrelas'),
              const SizedBox(width: 12),
              _Indicador(
                  icone: '🔥',
                  valor: '${regras.sequenciaDias}',
                  rotulo: regras.sequenciaDias == 1 ? 'dia seguido' : 'dias seguidos'),
            ],
          ),
          const SizedBox(height: 16),
          _CartaoMissaoDoDia(estado: estado),
          const SizedBox(height: 24),
          for (final b in estado.trilha.bimestres) ...[
            _SecaoBimestre(estado: estado, bimestre: b),
            const SizedBox(height: 16),
          ],
        ],
      ),
    );
  }
}

class _Indicador extends StatelessWidget {
  final String icone;
  final String valor;
  final String rotulo;

  const _Indicador(
      {required this.icone, required this.valor, required this.rotulo});

  @override
  Widget build(BuildContext context) {
    return Expanded(
      child: Card(
        color: Colors.white,
        child: Padding(
          padding: const EdgeInsets.symmetric(vertical: 12, horizontal: 16),
          child: Row(
            children: [
              Text(icone, style: const TextStyle(fontSize: 28)),
              const SizedBox(width: 8),
              Text(valor,
                  style: const TextStyle(
                      fontSize: 24, fontWeight: FontWeight.bold)),
              const SizedBox(width: 6),
              Flexible(child: Text(rotulo)),
            ],
          ),
        ),
      ),
    );
  }
}

class _CartaoMissaoDoDia extends StatelessWidget {
  final EstadoTrilha estado;

  const _CartaoMissaoDoDia({required this.estado});

  @override
  Widget build(BuildContext context) {
    final regras = estado.regras;
    final missao = regras.missaoDoDia;
    final cores = Theme.of(context).colorScheme;

    String titulo;
    String subtitulo;
    VoidCallback? acao;
    if (missao == null) {
      titulo = 'Trilha em dia! 🎉';
      subtitulo = 'Você concluiu todas as missões liberadas até agora.';
    } else if (!regras.podeFazerMissaoNova) {
      titulo = 'Missão de hoje concluída! ✅';
      subtitulo = 'Volte amanhã para a próxima: ${missao.titulo}.';
    } else {
      titulo = 'Missão do dia';
      subtitulo = '${missao.componente} · ${missao.titulo}';
      acao = () =>
          context.go('/perfil/${estado.perfil.id}/missao/${missao.id}');
    }

    return Card(
      color: cores.primary,
      child: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(titulo,
                style: Theme.of(context)
                    .textTheme
                    .titleLarge
                    ?.copyWith(color: cores.onPrimary, fontWeight: FontWeight.bold)),
            const SizedBox(height: 6),
            Text(subtitulo,
                style: TextStyle(color: cores.onPrimary, fontSize: 16)),
            if (acao != null) ...[
              const SizedBox(height: 16),
              FilledButton(
                style: FilledButton.styleFrom(
                    backgroundColor: cores.onPrimary,
                    foregroundColor: cores.primary),
                onPressed: acao,
                child: const Text('Começar'),
              ),
            ],
          ],
        ),
      ),
    );
  }
}

class _SecaoBimestre extends StatelessWidget {
  final EstadoTrilha estado;
  final Bimestre bimestre;

  const _SecaoBimestre({required this.estado, required this.bimestre});

  @override
  Widget build(BuildContext context) {
    final regras = estado.regras;
    final aberto = regras.bimestreAberto(bimestre.numero);
    final atual = regras.bimestreAtual == bimestre.numero;
    final feitas =
        bimestre.missoes.where((m) => estado.progresso.concluiu(m.id)).length;

    return Card(
      color: Colors.white,
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                Expanded(
                  child: Text(bimestre.titulo,
                      style: Theme.of(context)
                          .textTheme
                          .titleMedium
                          ?.copyWith(fontWeight: FontWeight.bold)),
                ),
                if (atual)
                  const Chip(label: Text('Agora'))
                else if (!aberto)
                  const Icon(Icons.lock, color: Colors.grey),
              ],
            ),
            Text('$feitas de ${bimestre.missoes.length} missões'),
            const SizedBox(height: 8),
            LinearProgressIndicator(
              value: bimestre.missoes.isEmpty
                  ? 0
                  : feitas / bimestre.missoes.length,
              minHeight: 8,
              borderRadius: BorderRadius.circular(4),
            ),
            const SizedBox(height: 8),
            for (final m in bimestre.missoes)
              _ItemMissao(
                estado: estado,
                missao: m,
                status: regras.status(bimestre, m),
              ),
          ],
        ),
      ),
    );
  }
}

class _ItemMissao extends StatelessWidget {
  final EstadoTrilha estado;
  final Missao missao;
  final StatusMissao status;

  const _ItemMissao(
      {required this.estado, required this.missao, required this.status});

  @override
  Widget build(BuildContext context) {
    final cor = corDoComponente(missao.componente);
    final estrelas = estado.progresso.concluidas[missao.id]?.estrelas ?? 0;
    final podeAbrir =
        status == StatusMissao.concluida || status == StatusMissao.disponivel;

    final Widget final_;
    switch (status) {
      case StatusMissao.concluida:
        final_ = Text('⭐' * estrelas);
      case StatusMissao.disponivel:
        final_ = const Icon(Icons.play_circle_fill, color: corPrimaria);
      case StatusMissao.amanha:
        final_ = const Text('amanhã');
      case StatusMissao.bloqueada:
        final_ = const Icon(Icons.lock_outline, color: Colors.grey);
    }

    return ListTile(
      contentPadding: EdgeInsets.zero,
      enabled: podeAbrir,
      leading: CircleAvatar(
        backgroundColor: podeAbrir ? cor : Colors.grey.shade300,
        child: Text(missao.componente.substring(0, 1),
            style: const TextStyle(
                color: Colors.white, fontWeight: FontWeight.bold)),
      ),
      title: Text(missao.titulo),
      subtitle: Text(missao.componente),
      trailing: final_,
      onTap: podeAbrir
          ? () => context.go('/perfil/${estado.perfil.id}/missao/${missao.id}')
          : null,
    );
  }
}
