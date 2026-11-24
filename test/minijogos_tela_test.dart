import 'dart:convert';
import 'dart:io';
import 'dart:math';

import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:material_ui/material_ui.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:go_router/go_router.dart';
import 'package:trilha_do_saber/app.dart';
import 'package:trilha_do_saber/componentes/fala.dart';
import 'package:trilha_do_saber/dados/repositorios.dart';
import 'package:trilha_do_saber/modelos/conteudo.dart';
import 'package:trilha_do_saber/providers.dart';

class FalaMuda extends Fala {
  final falas = <String>[];
  @override
  Future<void> falar(String texto) async => falas.add(texto);
  @override
  Future<void> parar() async {}
}

/// Lê o conteúdo direto do disco (o rootBundle usa isolate para arquivos
/// grandes, o que trava o relógio falso dos testes de widget).
class ConteudoDoDisco implements RepositorioConteudo {
  @override
  Future<ConteudoAno> ano(int ano) async => ConteudoAno.fromJson(
    jsonDecode(File('assets/conteudo/ano_$ano.json').readAsStringSync()) as Map<String, dynamic>,
  );
  @override
  Future<List<Nivel>> niveis() async =>
      (jsonDecode(File('assets/conteudo/niveis.json').readAsStringSync()) as List)
          .map((n) => Nivel.fromJson(n as Map<String, dynamic>))
          .toList();
}

void main() {
  for (final jogo in ['travessia', 'patrulha', 'cauda']) {
    testWidgets('$jogo termina e mostra o placar', (tester) async {
      tester.view.physicalSize = const Size(1080, 2400);
      tester.view.devicePixelRatio = 2.5;
      addTearDown(tester.view.reset);
      SharedPreferences.setMockInitialValues({
        'perfis': jsonEncode([
          {'id': 'x1', 'nome': 'Bia', 'ano': 4, 'gato': 'luna', 'nivel': 'f', 'som': true},
        ]),
        'progresso_x1': jsonEncode({
          'xp': 0,
          'peixinhos': 0,
          'estrelas': {'f:a4b4-m11': 3, 'f:a4b4-p11': 2},
        }),
      });
      final prefs = await SharedPreferences.getInstance();
      final app = AppGalaxia();
      await tester.pumpWidget(
        ProviderScope(
          overrides: [
            prefsProvider.overrideWithValue(prefs),
            relogioProvider.overrideWithValue(() => DateTime(2026, 11, 19, 10)),
            aleatorioProvider.overrideWithValue(Random(3)),
            falaProvider.overrideWithValue(FalaMuda()),
            repositorioConteudoProvider.overrideWithValue(ConteudoDoDisco()),
          ],
          child: app,
        ),
      );
      await tester.pumpAndSettle();
      final ctx = tester.element(find.byType(Navigator).first);
      // Como no app: a pausa abre por cima do mapa do planeta.
      GoRouter.of(ctx).go('/c/x1/p/a4b4-mat');
      await tester.pumpAndSettle();
      GoRouter.of(ctx).go('/c/x1/p/a4b4-mat/pausa/$jogo/1');
      for (var i = 0; i < 10; i++) {
        await tester.pump(const Duration(milliseconds: 100));
      }
      expect(find.textContaining('PRÓXIMA MISSÃO'), findsNothing);
      if (jogo == 'travessia') await tester.tapAt(const Offset(216, 600));
      // Joga sozinho até acabar (no máximo 2 minutos de jogo).
      for (var i = 0; i < 2400 && find.textContaining('PRÓXIMA MISSÃO').evaluate().isEmpty; i++) {
        await tester.pump(const Duration(milliseconds: 50));
      }
      expect(find.textContaining('PRÓXIMA MISSÃO'), findsOneWidget);
      for (var i = 0; i < 30; i++) {
        await tester.pump(const Duration(milliseconds: 100));
      }
      expect(find.textContaining('PRÓXIMA MISSÃO'), findsOneWidget, reason: 'placar continua');
      final p = jsonDecode(prefs.getString('progresso_x1')!) as Map<String, dynamic>;
      expect(p['peixinhos'], greaterThan(0));
      await tester.tap(find.byTooltip('Sair do jogo'));
      await tester.pumpAndSettle();
    });
  }
}
