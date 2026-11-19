import 'package:material_ui/material_ui.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';

import '../../logic/regras_trilha.dart';
import '../../models/curriculo.dart';
import '../../providers.dart';
import '../../ui/tema.dart';

/// Uma missão: perguntas de múltipla escolha, uma por vez, com retorno
/// imediato e estrelas no final.
class TelaMissao extends ConsumerWidget {
  final String perfilId;
  final String missaoId;

  const TelaMissao({super.key, required this.perfilId, required this.missaoId});

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
        Bimestre? bimestre;
        Missao? missao;
        for (final b in e?.trilha.bimestres ?? const <Bimestre>[]) {
          for (final m in b.missoes) {
            if (m.id == missaoId) {
              bimestre = b;
              missao = m;
            }
          }
        }
        if (e == null || bimestre == null || missao == null) {
          return Scaffold(
              appBar: AppBar(),
              body: const Center(child: Text('Missão não encontrada.')));
        }
        final status = e.regras.status(bimestre, missao);
        if (status == StatusMissao.bloqueada || status == StatusMissao.amanha) {
          return Scaffold(
            appBar: AppBar(),
            body: const Center(
                child: Text('Esta missão ainda não está liberada.')),
          );
        }
        return _Jogo(perfilId: perfilId, missao: missao);
      },
    );
  }
}

class _Jogo extends ConsumerStatefulWidget {
  final String perfilId;
  final Missao missao;

  const _Jogo({required this.perfilId, required this.missao});

  @override
  ConsumerState<_Jogo> createState() => _JogoState();
}

class _JogoState extends ConsumerState<_Jogo> {
  int _indice = 0;
  int _acertos = 0;
  int? _escolhida;
  int? _estrelasFinais;

  Questao get _questao => widget.missao.questoes[_indice];

  void _responder(int alternativa) {
    if (_escolhida != null) return;
    setState(() {
      _escolhida = alternativa;
      if (alternativa == _questao.correta) _acertos++;
    });
  }

  Future<void> _avancar() async {
    if (_indice + 1 < widget.missao.questoes.length) {
      setState(() {
        _indice++;
        _escolhida = null;
      });
      return;
    }
    final estrelas =
        estrelasPorAcertos(_acertos, widget.missao.questoes.length);
    // Fixa a tela de resultado antes de gravar, para ela não ser
    // trocada quando a trilha recarregar.
    setState(() => _estrelasFinais = estrelas);
    await ref.read(acoesProvider).concluirMissao(
          perfilId: widget.perfilId,
          missaoId: widget.missao.id,
          estrelas: estrelas,
        );
  }

  @override
  Widget build(BuildContext context) {
    final missao = widget.missao;
    final cor = corDoComponente(missao.componente);
    final total = missao.questoes.length;

    if (_estrelasFinais != null) {
      return _Resultado(
        acertos: _acertos,
        total: total,
        estrelas: _estrelasFinais!,
        onVoltar: () => context.go('/perfil/${widget.perfilId}'),
      );
    }

    final respondida = _escolhida != null;
    final acertou = _escolhida == _questao.correta;

    return Scaffold(
      appBar: AppBar(
        backgroundColor: cor,
        foregroundColor: Colors.white,
        title: Text(missao.titulo),
      ),
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(20),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              LinearProgressIndicator(
                value: (_indice + (respondida ? 1 : 0)) / total,
                color: cor,
                minHeight: 10,
                borderRadius: BorderRadius.circular(5),
              ),
              const SizedBox(height: 8),
              Text('Pergunta ${_indice + 1} de $total',
                  textAlign: TextAlign.center),
              const SizedBox(height: 24),
              Text(_questao.enunciado,
                  textAlign: TextAlign.center,
                  style: Theme.of(context)
                      .textTheme
                      .headlineSmall
                      ?.copyWith(fontWeight: FontWeight.bold)),
              const SizedBox(height: 24),
              for (var i = 0; i < _questao.alternativas.length; i++)
                Padding(
                  padding: const EdgeInsets.only(bottom: 12),
                  child: _BotaoAlternativa(
                    texto: _questao.alternativas[i],
                    estado: !respondida
                        ? _EstadoAlternativa.neutra
                        : i == _questao.correta
                            ? _EstadoAlternativa.certa
                            : i == _escolhida
                                ? _EstadoAlternativa.errada
                                : _EstadoAlternativa.apagada,
                    onTap: () => _responder(i),
                  ),
                ),
              const Spacer(),
              if (respondida) ...[
                Text(
                  acertou ? 'Muito bem! 🎉' : 'Quase! Veja a resposta certa.',
                  textAlign: TextAlign.center,
                  style: Theme.of(context).textTheme.titleLarge,
                ),
                if (_questao.explicacao != null)
                  Padding(
                    padding: const EdgeInsets.only(top: 4),
                    child: Text(_questao.explicacao!,
                        textAlign: TextAlign.center),
                  ),
                const SizedBox(height: 12),
                FilledButton(
                  onPressed: _avancar,
                  child: Text(_indice + 1 < total ? 'Continuar' : 'Terminar'),
                ),
              ],
            ],
          ),
        ),
      ),
    );
  }
}

enum _EstadoAlternativa { neutra, certa, errada, apagada }

class _BotaoAlternativa extends StatelessWidget {
  final String texto;
  final _EstadoAlternativa estado;
  final VoidCallback onTap;

  const _BotaoAlternativa(
      {required this.texto, required this.estado, required this.onTap});

  @override
  Widget build(BuildContext context) {
    final (Color fundo, Color borda) = switch (estado) {
      _EstadoAlternativa.neutra => (Colors.white, Colors.grey.shade300),
      _EstadoAlternativa.certa => (Colors.green.shade100, Colors.green),
      _EstadoAlternativa.errada => (Colors.red.shade100, Colors.red),
      _EstadoAlternativa.apagada => (Colors.white, Colors.grey.shade200),
    };
    return Material(
      color: fundo,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(16),
        side: BorderSide(color: borda, width: 2),
      ),
      child: InkWell(
        borderRadius: BorderRadius.circular(16),
        onTap: estado == _EstadoAlternativa.neutra ? onTap : null,
        child: Padding(
          padding: const EdgeInsets.symmetric(vertical: 18, horizontal: 16),
          child: Text(texto,
              textAlign: TextAlign.center,
              style: const TextStyle(fontSize: 20)),
        ),
      ),
    );
  }
}

class _Resultado extends StatelessWidget {
  final int acertos;
  final int total;
  final int estrelas;
  final VoidCallback onVoltar;

  const _Resultado({
    required this.acertos,
    required this.total,
    required this.estrelas,
    required this.onVoltar,
  });

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(24),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              Text('Missão concluída!',
                  textAlign: TextAlign.center,
                  style: Theme.of(context)
                      .textTheme
                      .headlineMedium
                      ?.copyWith(fontWeight: FontWeight.bold)),
              const SizedBox(height: 24),
              Text('${'⭐' * estrelas}${'☆' * (3 - estrelas)}',
                  textAlign: TextAlign.center,
                  style: const TextStyle(fontSize: 56)),
              const SizedBox(height: 16),
              Text('Você acertou $acertos de $total perguntas.',
                  textAlign: TextAlign.center,
                  style: Theme.of(context).textTheme.titleMedium),
              const SizedBox(height: 32),
              FilledButton(
                  onPressed: onVoltar, child: const Text('Voltar para a trilha')),
            ],
          ),
        ),
      ),
    );
  }
}
