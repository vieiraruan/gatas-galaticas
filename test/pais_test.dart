import 'dart:convert';
import 'dart:math';

import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:material_ui/material_ui.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:trilha_do_saber/app.dart';
import 'package:trilha_do_saber/componentes/exercicios.dart';
import 'package:trilha_do_saber/componentes/fala.dart';
import 'package:trilha_do_saber/providers.dart';

import 'fluxo_app_test.dart' show ConteudoDoDisco, FalaMuda;

Future<void> tocar(WidgetTester tester, Finder f) async {
  await tester.ensureVisible(f);
  await tester.pumpAndSettle();
  await tester.tap(f);
  await tester.pumpAndSettle();
}

void main() {
  testWidgets('pais: PIN, horário, prova e acompanhamento; criança treina e constrói a nave',
      (tester) async {
    tester.view.physicalSize = const Size(1080, 2400);
    tester.view.devicePixelRatio = 2.5;
    addTearDown(tester.view.reset);

    SharedPreferences.setMockInitialValues({
      'pais_pin': '1234',
      'perfis': jsonEncode([
        {'id': 'ana', 'nome': 'Ana', 'ano': 4, 'gato': 'luna'}
      ]),
      'progresso_ana': jsonEncode({
        'xp': 40,
        'xpPorDia': {'2026-11-23': 40},
        'suprimentos': {'matematica': 5, 'portugues': 4},
        'acertosPorMateria': {'matematica': 7},
        'respostasPorMateria': {'matematica': 10},
      }),
    });
    final prefs = await SharedPreferences.getInstance();

    await tester.pumpWidget(ProviderScope(
      overrides: [
        prefsProvider.overrideWithValue(prefs),
        relogioProvider.overrideWithValue(() => DateTime(2026, 11, 24, 10)), // terça
        aleatorioProvider.overrideWithValue(Random(5)),
        falaProvider.overrideWithValue(FalaMuda() as Fala),
        repositorioConteudoProvider.overrideWithValue(ConteudoDoDisco()),
      ],
      child: const AppGalaxia(),
    ));
    await tester.pumpAndSettle();

    // PIN errado, depois o certo.
    await tocar(tester, find.text('🔐 Área dos pais'));
    expect(find.text('Digite o PIN dos pais'), findsOneWidget);
    for (final t in ['9', '9', '9', '9']) {
      await tester.tap(find.byKey(Key('tecla$t')));
      await tester.pumpAndSettle();
    }
    expect(find.text('PIN errado. Tente de novo.'), findsOneWidget);
    for (final t in ['1', '2', '3', '4']) {
      await tester.tap(find.byKey(Key('tecla$t')));
      await tester.pumpAndSettle();
    }
    expect(find.text('Seus filhos'), findsOneWidget);
    await tocar(tester, find.text('Ana · 4º ano'));

    // Acompanhamento.
    expect(find.text('Resumo'), findsOneWidget);
    expect(find.text('70% de acertos'), findsOneWidget);

    // Horário: terça tem Inglês.
    await tocar(tester, find.text('🏫 Horário'));
    await tocar(tester, find.byKey(const Key('aula2ingles')));
    await tocar(tester, find.text('SALVAR HORÁRIO'));
    final rotina = jsonDecode(prefs.getString('rotina_ana')!) as Map<String, dynamic>;
    expect(rotina['horario'], {
      '2': ['ingles']
    });

    // Prova de Matemática sobre Frações, daqui a 7 dias.
    await tocar(tester, find.text('📝 Provas'));
    await tocar(tester, find.text('➕ NOVA PROVA'));
    await tester.scrollUntilVisible(find.byKey(const Key('assuntoa4b4-mat-s2')), 200,
        scrollable: find.byType(Scrollable).last);
    await tocar(tester, find.byKey(const Key('assuntoa4b4-mat-s2')));
    await tester.scrollUntilVisible(find.text('SALVAR PROVA'), 200,
        scrollable: find.byType(Scrollable).last);
    await tocar(tester, find.text('SALVAR PROVA'));
    final provas = (jsonDecode(prefs.getString('rotina_ana')!) as Map)['provas'] as List;
    expect(provas.single['materia'], 'matematica');
    expect(provas.single['data'], '2026-12-01');
    expect(provas.single['assuntos'], ['a4b4-mat-s2']);

    // A criança vê a prova, a aula do dia e treina.
    await tocar(tester, find.text('▶ Jogar'));
    expect(find.text('📝 Prova de Matemática em 7 dias'), findsOneWidget);
    expect(find.text('🏫 Hoje tem aula de: Inglês'), findsOneWidget);
    expect(find.text('📝 Prova em 7 dias'), findsWidgets); // missão do dia priorizada
    await tocar(tester, find.text('🎯 TREINAR PARA A PROVA'));
    expect(find.byType(VistaExercicio), findsOneWidget);
    await tocar(tester, find.byTooltip('Sair da missão'));

    // Hangar: constrói o casco.
    await tocar(tester, find.text('NAVE GATÍSTICA'));
    expect(find.text('🛠️ Hangar da Nave Gatística'), findsOneWidget);
    await tocar(tester, find.text('CONSTRUIR').first);
    await tester.pump(const Duration(seconds: 2));
    final prog = jsonDecode(prefs.getString('progresso_ana')!) as Map<String, dynamic>;
    expect(prog['pecas'], ['casco']);
    expect((prog['suprimentos'] as Map)['matematica'], 2);
  });
}
