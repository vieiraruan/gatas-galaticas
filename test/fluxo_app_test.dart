import 'dart:convert';
import 'dart:io';
import 'dart:math';

import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:material_ui/material_ui.dart';
import 'package:shared_preferences/shared_preferences.dart';
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
  testWidgets('cadastra criança do 4º ano e vence uma missão de Matemática', (tester) async {
    tester.view.physicalSize = const Size(1080, 2400);
    tester.view.devicePixelRatio = 2.5;
    addTearDown(tester.view.reset);

    SharedPreferences.setMockInitialValues({});
    final prefs = await SharedPreferences.getInstance();
    final fala = FalaMuda();

    await tester.pumpWidget(
      ProviderScope(
        overrides: [
          prefsProvider.overrideWithValue(prefs),
          relogioProvider.overrideWithValue(() => DateTime(2026, 11, 19, 10)),
          aleatorioProvider.overrideWithValue(Random(3)),
          falaProvider.overrideWithValue(fala),
          repositorioConteudoProvider.overrideWithValue(ConteudoDoDisco()),
        ],
        child: const AppGalaxia(),
      ),
    );
    await tester.pumpAndSettle();

    expect(find.text('Quem vai decolar hoje?'), findsOneWidget);
    await tester.tap(find.textContaining('Novo astronauta'));
    await tester.pumpAndSettle();

    // Os pais criam o PIN (duas vezes) antes de cadastrar.
    expect(find.text('Crie um PIN de 4 números'), findsOneWidget);
    for (var vez = 0; vez < 2; vez++) {
      for (final t in ['1', '9', '8', '4']) {
        await tester.tap(find.byKey(Key('tecla$t')));
        await tester.pumpAndSettle();
      }
    }
    expect(prefs.getString('pais_pin'), '1984');

    await tester.enterText(find.byKey(const Key('campoNome')), 'bernardo');
    await tester.tap(find.text('4º'));
    await tester.tap(find.text('Nala Pudinzinha'));
    await tester.pump();
    await tester.tap(find.text('🚀 CADASTRAR'));
    await tester.pumpAndSettle();
    expect(find.text('Bernardo · 4º ano'), findsOneWidget); // lista dos pais
    await tester.tap(find.byTooltip('Sair da área dos pais'));
    await tester.pumpAndSettle();

    await tester.tap(find.text('Bernardo'));
    await tester.pumpAndSettle();
    expect(find.text('Universo do 4º ano'), findsOneWidget);
    expect(find.text('MISSÕES DE HOJE'), findsOneWidget);

    // Matéria = galáxia, assunto = planeta.
    await tester.scrollUntilVisible(
      find.text('Galáxia dos Números'),
      300,
      scrollable: find.byType(Scrollable).first,
    );
    await tester.ensureVisible(find.text('Galáxia dos Números'));
    await tester.pumpAndSettle();
    await tester.tap(find.text('Galáxia dos Números'));
    await tester.pumpAndSettle();
    expect(find.text('Frações'), findsOneWidget);
    await tester.ensureVisible(find.text('Divisão'));
    await tester.pumpAndSettle();
    await tester.tap(find.text('Divisão'));
    await tester.pumpAndSettle();
    expect(find.text('Problemas de divisão'), findsOneWidget);
    expect(find.text('Noção de fração'), findsNothing); // outro planeta
    await tester.tap(find.text('Exata ou não exata'));
    await tester.pumpAndSettle();
    await tester.tap(find.text('🚀 DECOLAR'));
    await tester.pumpAndSettle();

    // Briefing com leitura em voz alta.
    expect(find.textContaining('BRIEFING DA MISSÃO'), findsOneWidget);
    await tester.tap(find.text('🔊 OUVIR'));
    expect(fala.falas, isNotEmpty);
    while (find.text('PRÓXIMO ➜').evaluate().isNotEmpty) {
      await tester.tap(find.text('PRÓXIMO ➜'));
      await tester.pumpAndSettle();
    }
    await tester.tap(find.text('🚀 COMEÇAR'));
    await tester.pumpAndSettle();

    // Responde sempre a primeira opção até acabar (erros voltam no fim).
    var reacoes = 0;
    for (var rodada = 0; rodada < 20; rodada++) {
      if (find.text('Missão cumprida!').evaluate().isNotEmpty) break;
      if (find.text('💪 ACEITO O DESAFIO!').evaluate().isNotEmpty) {
        await tester.tap(find.text('💪 ACEITO O DESAFIO!'));
        await tester.pumpAndSettle();
      }
      final opcao = find.byWidgetPredicate(
        (w) => w.key is ValueKey && '${(w.key as ValueKey).value}'.startsWith('opcao'),
      );
      await tester.tap(opcao.first);
      await tester.pump();
      await tester.tap(find.text('VERIFICAR'));
      await tester.pump(const Duration(milliseconds: 200));
      // Carinha de gato pulando na tela a cada resposta.
      if (find.byKey(const Key('reacaoGato')).evaluate().isNotEmpty) reacoes++;
      await tester.pumpAndSettle();
      await tester.tap(find.text('CONTINUAR'));
      await tester.pumpAndSettle();
    }
    expect(find.text('Missão cumprida!'), findsOneWidget);
    expect(reacoes, greaterThan(0));
    expect(find.text('SUPRIMENTOS PARA A NAVE GATÍSTICA'), findsOneWidget);

    final progresso = jsonDecode(
      prefs.getString('progresso_${jsonDecode(prefs.getString('perfis')!)[0]['id']}')!,
    ) as Map<String, dynamic>;
    expect(progresso['xp'], greaterThan(0));
    expect((progresso['estrelas'] as Map).keys.single, 'f:a4b4-m11');
    expect((progresso['suprimentos'] as Map)['matematica'], greaterThan(0));
    expect((progresso['respostasPorMateria'] as Map)['matematica'], greaterThan(0));

    // Pausa opcional: o menu lista os 4 minijogos; abre o Labirinto Orbital
    // e pular volta ao mapa.
    await tester.scrollUntilVisible(find.text('🛋️ HORA DA PAUSA'), 200,
        scrollable: find.byType(Scrollable).first);
    await tester.tap(find.text('🛋️ HORA DA PAUSA'));
    await tester.pumpAndSettle();
    for (final nome in [
      'Labirinto Orbital',
      'Patrulha da Luz',
      'Cauda de Cometa',
      'Travessia do Cinturão',
    ]) {
      expect(find.text(nome), findsOneWidget);
    }
    await tester.tap(find.text('Labirinto Orbital'));
    await tester.pumpAndSettle();
    expect(find.text('🌌 LABIRINTO ORBITAL'), findsOneWidget);
    expect(find.text('Invasão Rápida'), findsOneWidget); // poder da Nala
    await tester.tap(find.byTooltip('Direita'));
    await tester.tap(find.byTooltip('Baixo'));
    await tester.pumpAndSettle();
    await tester.tap(find.byTooltip('Pular o labirinto'));
    await tester.pumpAndSettle();
    expect(find.text('Divisão com 2 algarismos'), findsOneWidget);
  });
}
