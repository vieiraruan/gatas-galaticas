import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:material_ui/material_ui.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:trilha_do_saber/app.dart';
import 'package:trilha_do_saber/providers.dart';

void main() {
  testWidgets('cadastra criança, faz a missão do dia e ganha estrelas',
      (tester) async {
    tester.view.physicalSize = const Size(1080, 2400);
    tester.view.devicePixelRatio = 2.5;
    addTearDown(tester.view.reset);

    SharedPreferences.setMockInitialValues({});
    final prefs = await SharedPreferences.getInstance();

    await tester.pumpWidget(ProviderScope(
      overrides: [
        prefsProvider.overrideWithValue(prefs),
        relogioProvider.overrideWithValue(() => DateTime(2026, 11, 19, 10)),
      ],
      child: const AppAprender(),
    ));
    await tester.pumpAndSettle();

    expect(find.text('Quem vai jogar?'), findsOneWidget);
    await tester.tap(find.text('Adicionar criança'));
    await tester.pumpAndSettle();

    await tester.enterText(find.byKey(const Key('campoNome')), 'Ana');
    await tester.tap(find.text('1º ano'));
    await tester.pump();
    await tester.tap(find.text('Salvar'));
    await tester.pumpAndSettle();

    expect(find.text('Ana'), findsOneWidget);
    await tester.tap(find.text('Ana'));
    await tester.pumpAndSettle();

    // 4º bimestre do 1º ano (novembro): primeira missão é "Eu e minha família".
    expect(find.text('Missão do dia'), findsOneWidget);
    await tester.tap(find.text('Começar'));
    await tester.pumpAndSettle();

    // Responde certo as 3 perguntas.
    for (final resposta in ['Avó', 'Na casa', 'Primo']) {
      await tester.tap(find.text(resposta));
      await tester.pumpAndSettle();
      expect(find.text('Muito bem! 🎉'), findsOneWidget);
      await tester.tap(find.byType(FilledButton));
      await tester.pumpAndSettle();
    }

    expect(find.text('Missão concluída!'), findsOneWidget);
    expect(find.text('Você acertou 3 de 3 perguntas.'), findsOneWidget);
    await tester.tap(find.text('Voltar para a trilha'));
    await tester.pumpAndSettle();

    expect(find.text('Missão de hoje concluída! ✅'), findsOneWidget);
    expect(find.text('3'), findsWidgets); // estrelas
  });
}
