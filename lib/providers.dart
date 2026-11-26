import 'dart:math';

import 'package:flutter/services.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:shared_preferences/shared_preferences.dart';

import 'dados/repositorios.dart';
import 'logica/nave.dart';
import 'logica/regras.dart';
import 'modelos/conteudo.dart';
import 'modelos/perfil.dart';
import 'modelos/progresso.dart';
import 'modelos/rotina.dart';

/// Preenchido em main() com `overrideWithValue`.
final prefsProvider = Provider<SharedPreferences>(
    (ref) => throw UnimplementedError('prefsProvider precisa de override'));

/// Relógio e sorteio injetáveis (os testes fixam a data e a sorte).
final relogioProvider = Provider<DateTime Function()>((ref) => DateTime.now);
final aleatorioProvider = Provider<Random>((ref) => Random());

final repositorioPerfisProvider = Provider<RepositorioPerfis>(
    (ref) => RepositorioPerfisLocal(ref.watch(prefsProvider)));
final repositorioProgressoProvider = Provider<RepositorioProgresso>(
    (ref) => RepositorioProgressoLocal(ref.watch(prefsProvider)));
final repositorioPaisProvider = Provider<RepositorioPais>(
    (ref) => RepositorioPaisLocal(ref.watch(prefsProvider)));
final repositorioConteudoProvider = Provider<RepositorioConteudo>(
    (ref) => RepositorioConteudoAssets(rootBundle));

final perfisProvider = FutureProvider<List<PerfilCrianca>>(
    (ref) => ref.watch(repositorioPerfisProvider).listar());

final niveisProvider = FutureProvider<List<Nivel>>(
    (ref) => ref.watch(repositorioConteudoProvider).niveis());

final conteudoProvider = FutureProvider.family<ConteudoAno, int>(
    (ref, ano) => ref.watch(repositorioConteudoProvider).ano(ano));

final progressoProvider = FutureProvider.family<Progresso, String>(
    (ref, id) => ref.watch(repositorioProgressoProvider).carregar(id));

final rotinaProvider = FutureProvider.family<Rotina, String>(
    (ref, id) => ref.watch(repositorioPaisProvider).rotina(id));

final pinProvider =
    FutureProvider<String?>((ref) => ref.watch(repositorioPaisProvider).pin());

/// Área dos pais destrancada (vale até sair dela ou fechar o app).
class PaisLiberado extends Notifier<bool> {
  @override
  bool build() => false;
  void liberar() => state = true;
  void trancar() => state = false;
}

final paisLiberadoProvider = NotifierProvider<PaisLiberado, bool>(PaisLiberado.new);

/// Bimestre que a criança está vendo (começa no do calendário).
class BimestreEscolhido extends Notifier<int?> {
  @override
  int? build() => null;
  void escolher(int b) => state = b;
  void limpar() => state = null;
}

final bimestreEscolhidoProvider =
    NotifierProvider<BimestreEscolhido, int?>(BimestreEscolhido.new);

/// Tudo que as telas de uma criança precisam.
class Sessao {
  final PerfilCrianca perfil;
  final ConteudoAno conteudo;
  final Progresso progresso;
  final List<Nivel> niveis;
  final DateTime hoje;
  final int bimestreVisto;
  final Rotina rotina;

  Sessao({
    required this.perfil,
    required this.conteudo,
    required this.progresso,
    required this.niveis,
    required this.hoje,
    required this.bimestreVisto,
    this.rotina = Rotina.vazia,
  });

  Nivel get nivel =>
      niveis.firstWhere((n) => n.id == perfil.nivel, orElse: () => niveis.first);
  int get bimestreAtual => bimestreDoCalendario(hoje);
  bool bimestreAberto(int n) => n <= bimestreAtual;
  BimestreConteudo get bimestre =>
      conteudo.bimestre(bimestreVisto) ?? conteudo.bimestres.first;
  int get xpHoje => progresso.xpPorDia[chaveDia(hoje)] ?? 0;
  int get labirintosHoje => progresso.labirintosPorDia[chaveDia(hoje)] ?? 0;
  int get sequencia => sequenciaDias(progresso.xpPorDia, hoje);

  Planeta? planeta(String id) {
    for (final b in conteudo.bimestres) {
      for (final p in b.planetas) {
        if (p.id == id) return p;
      }
    }
    return null;
  }

  RegrasPlaneta regras(Planeta p) => RegrasPlaneta(p, progresso, perfil.nivel);

  List<MissaoDoDia> get missoesHoje => missoesDoDia(
        conteudo: conteudo,
        bimestre: bimestre,
        progresso: progresso,
        nivel: perfil.nivel,
        hoje: hoje,
        rotina: rotina,
        bimestreAtual: bimestreAtual,
      );

  /// Provas dos próximos 21 dias.
  List<Prova> get provasProximas => rotina.proximas(hoje, dentroDeDias: 21);

  /// Planetas (do conteúdo) dos bimestres já abertos.
  Iterable<Planeta> get planetasAbertos => conteudo.bimestres
      .where((b) => bimestreAberto(b.numero))
      .expand((b) => b.planetas);

  /// Setor (assunto) pelo id, em qualquer bimestre.
  ({Planeta planeta, int setor, int bimestre})? setorPorId(String id) {
    for (final b in conteudo.bimestres) {
      for (final p in b.planetas) {
        for (var i = 0; i < p.setores.length; i++) {
          if (p.setores[i].id == id) return (planeta: p, setor: i, bimestre: b.numero);
        }
      }
    }
    return null;
  }

  Prova? prova(String id) => rotina.provas.where((p) => p.id == id).firstOrNull;

  /// Nó de treino de uma prova (assuntos da matéria, ou o bimestre todo).
  NoTreino? treino(Prova prova) {
    final setores = <Setor>[];
    Planeta? planeta;
    for (final a in prova.assuntos) {
      final x = setorPorId(a);
      if (x == null) continue;
      planeta ??= x.planeta;
      setores.add(x.planeta.setores[x.setor]);
    }
    if (planeta == null) {
      planeta = planetaDaDisciplina(bimestre, prova.materia);
      if (planeta == null) return null;
      setores.addAll(planeta.setores);
    }
    final no = NoTreino(planeta, setores, prova.id);
    return emBreve(no) ? null : no;
  }
}

final sessaoProvider =
    FutureProvider.family<Sessao?, String>((ref, perfilId) async {
  final perfis = await ref.watch(perfisProvider.future);
  final perfil = perfis.where((p) => p.id == perfilId).firstOrNull;
  if (perfil == null) return null;
  final hoje = ref.watch(relogioProvider)();
  final escolhido = ref.watch(bimestreEscolhidoProvider);
  return Sessao(
    perfil: perfil,
    conteudo: await ref.watch(conteudoProvider(perfil.ano).future),
    progresso: await ref.watch(progressoProvider(perfilId).future),
    niveis: await ref.watch(niveisProvider.future),
    hoje: hoje,
    bimestreVisto: escolhido ?? bimestreDoCalendario(hoje),
    rotina: await ref.watch(rotinaProvider(perfilId).future),
  );
});

/// Ações que gravam dados e avisam as telas.
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
    ref.invalidate(rotinaProvider(id));
  }

  Future<void> salvarRotina(String perfilId, Rotina rotina) async {
    await ref.read(repositorioPaisProvider).salvarRotina(perfilId, rotina);
    ref.invalidate(rotinaProvider(perfilId));
  }

  Future<void> salvarPin(String? pin) async {
    await ref.read(repositorioPaisProvider).salvarPin(pin);
    ref.invalidate(pinProvider);
  }

  /// Constrói uma peça da nave. Devolve false se não deu.
  Future<bool> construirPeca(String perfilId, PecaNave peca) async {
    var ok = false;
    await _alterar(perfilId, (p) {
      final novo = comPecaConstruida(p, peca);
      ok = novo != null;
      return novo ?? p;
    });
    return ok;
  }

  /// Marca que a prova surpresa do dia já foi oferecida.
  Future<void> marcarSurpresa(String perfilId) => _alterar(perfilId, (p) {
        final dia = chaveDia(ref.read(relogioProvider)());
        return p.copyWith(
            surpresasPorDia: {...p.surpresasPorDia, dia: (p.surpresasPorDia[dia] ?? 0) + 1});
      });

  Future<Progresso> _alterar(
      String perfilId, Progresso Function(Progresso) f) async {
    final repo = ref.read(repositorioProgressoProvider);
    final novo = f(await repo.carregar(perfilId));
    await repo.salvar(perfilId, novo);
    ref.invalidate(progressoProvider(perfilId));
    return novo;
  }

  /// Registra o fim de uma partida e devolve o progresso novo.
  Future<Progresso> concluirPartida({
    required String perfilId,
    required String nivel,
    required String noId,
    required int estrelas,
    required int xp,
    required int peixinhos,
    Map<String, int> suprimentos = const {},
    Map<String, int> acertos = const {},
    Map<String, int> respostas = const {},
    Map<String, int> medalhas = const {},
    (String chave, int valor)? sequencia,
  }) =>
      _alterar(perfilId, (p) {
        final k = Progresso.chave(nivel, noId);
        final dia = chaveDia(ref.read(relogioProvider)());
        return p.copyWith(
          xp: p.xp + xp,
          peixinhos: p.peixinhos + peixinhos,
          xpPorDia: {...p.xpPorDia, dia: (p.xpPorDia[dia] ?? 0) + xp},
          estrelas: {...p.estrelas, k: max(p.estrelas[k] ?? 0, estrelas)},
          jogadas: {...p.jogadas, k: (p.jogadas[k] ?? 0) + 1},
          suprimentos: somar(p.suprimentos, suprimentos),
          acertosPorMateria: somar(p.acertosPorMateria, acertos),
          respostasPorMateria: somar(p.respostasPorMateria, respostas),
          medalhas: somar(p.medalhas, medalhas),
          sequencias: sequencia == null
              ? null
              : {...p.sequencias, sequencia.$1: sequencia.$2},
        );
      });

  /// Registra um Labirinto Orbital concluído (não mexe nas estrelas).
  Future<void> concluirLabirinto({
    required String perfilId,
    required int xp,
    required int peixinhos,
  }) =>
      _alterar(perfilId, (p) {
        final dia = chaveDia(ref.read(relogioProvider)());
        return p.copyWith(
          xp: p.xp + xp,
          peixinhos: p.peixinhos + peixinhos,
          xpPorDia: {...p.xpPorDia, dia: (p.xpPorDia[dia] ?? 0) + xp},
          labirintosPorDia: {
            ...p.labirintosPorDia,
            dia: (p.labirintosPorDia[dia] ?? 0) + 1
          },
        );
      });

  Future<void> abrirCapsula({
    required String perfilId,
    required String nivel,
    required String noId,
    required int peixinhos,
  }) =>
      _alterar(
          perfilId,
          (p) => p.copyWith(
                peixinhos: p.peixinhos + peixinhos,
                capsulas: {...p.capsulas, Progresso.chave(nivel, noId)},
              ));
}

final acoesProvider = Provider<Acoes>((ref) => Acoes(ref));
