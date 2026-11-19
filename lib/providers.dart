import 'package:flutter/services.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:shared_preferences/shared_preferences.dart';

import 'data/repositorios.dart';
import 'logic/regras_trilha.dart';
import 'models/curriculo.dart';
import 'models/perfil.dart';
import 'models/progresso.dart';

/// Preenchido em main() com `overrideWithValue`.
final prefsProvider = Provider<SharedPreferences>(
    (ref) => throw UnimplementedError('prefsProvider precisa de override'));

/// Relógio injetável (os testes trocam a data de "hoje").
final relogioProvider = Provider<DateTime Function()>((ref) => DateTime.now);

final repositorioPerfisProvider = Provider<RepositorioPerfis>(
    (ref) => RepositorioPerfisLocal(ref.watch(prefsProvider)));

final repositorioProgressoProvider = Provider<RepositorioProgresso>(
    (ref) => RepositorioProgressoLocal(ref.watch(prefsProvider)));

final repositorioCurriculoProvider = Provider<RepositorioCurriculo>(
    (ref) => RepositorioCurriculoAssets(rootBundle));

final perfisProvider = FutureProvider<List<PerfilCrianca>>(
    (ref) => ref.watch(repositorioPerfisProvider).listar());

final perfilProvider =
    FutureProvider.family<PerfilCrianca?, String>((ref, id) async {
  final perfis = await ref.watch(perfisProvider.future);
  for (final p in perfis) {
    if (p.id == id) return p;
  }
  return null;
});

final trilhaProvider = FutureProvider.family<TrilhaAno, int>(
    (ref, ano) => ref.watch(repositorioCurriculoProvider).trilha(ano));

final progressoProvider = FutureProvider.family<Progresso, String>(
    (ref, perfilId) =>
        ref.watch(repositorioProgressoProvider).carregar(perfilId));

/// Tudo que a tela da trilha precisa de uma vez.
class EstadoTrilha {
  final PerfilCrianca perfil;
  final TrilhaAno trilha;
  final RegrasTrilha regras;

  EstadoTrilha(this.perfil, this.trilha, this.regras);

  Progresso get progresso => regras.progresso;
}

final estadoTrilhaProvider =
    FutureProvider.family<EstadoTrilha?, String>((ref, perfilId) async {
  final perfil = await ref.watch(perfilProvider(perfilId).future);
  if (perfil == null) return null;
  final trilha = await ref.watch(trilhaProvider(perfil.ano).future);
  final progresso = await ref.watch(progressoProvider(perfilId).future);
  final hoje = ref.watch(relogioProvider)();
  return EstadoTrilha(
    perfil,
    trilha,
    RegrasTrilha(trilha: trilha, progresso: progresso, hoje: hoje),
  );
});

/// Ações que alteram dados. Depois de gravar, invalidam os providers
/// para as telas recarregarem.
class Acoes {
  final Ref ref;
  Acoes(this.ref);

  Future<void> salvarPerfil(PerfilCrianca perfil) async {
    await ref.read(repositorioPerfisProvider).salvar(perfil);
    ref.invalidate(perfisProvider);
  }

  Future<void> removerPerfil(String id) async {
    await ref.read(repositorioPerfisProvider).remover(id);
    ref.invalidate(perfisProvider);
    ref.invalidate(progressoProvider(id));
  }

  /// Registra o resultado de uma missão. Na primeira vez guarda a data
  /// (que conta para a missão do dia e a sequência). Ao refazer, só
  /// melhora as estrelas.
  Future<void> concluirMissao({
    required String perfilId,
    required String missaoId,
    required int estrelas,
  }) async {
    final repo = ref.read(repositorioProgressoProvider);
    final atual = await repo.carregar(perfilId);
    final anterior = atual.concluidas[missaoId];
    final novo = MissaoConcluida(
      missaoId: missaoId,
      data: anterior?.data ?? ref.read(relogioProvider)(),
      estrelas: anterior == null
          ? estrelas
          : (estrelas > anterior.estrelas ? estrelas : anterior.estrelas),
    );
    await repo.salvar(
        perfilId, Progresso({...atual.concluidas, missaoId: novo}));
    ref.invalidate(progressoProvider(perfilId));
  }
}

final acoesProvider = Provider<Acoes>((ref) => Acoes(ref));
