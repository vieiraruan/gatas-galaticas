import 'dart:convert';
import 'dart:io';
import 'dart:math';

import 'package:flutter_test/flutter_test.dart';
import 'package:trilha_do_saber/logica/regras.dart';
import 'package:trilha_do_saber/modelos/conteudo.dart';

Exercicio _q(String id, int c) =>
    Escolha(pergunta: id, opcoes: const ['a', 'b']).comComplexidade(c);

void main() {
  testesNiveisAvancados();
  final banco = [
    for (var i = 0; i < 10; i++) _q('c1-$i', 1),
    for (var i = 0; i < 10; i++) _q('c2-$i', 2),
    for (var i = 0; i < 10; i++) _q('c3-$i', 3),
  ];

  test('mistura do nível decide a complexidade das perguntas', () {
    final r = sortearPorMistura(banco, {3: 60, 2: 30, 1: 10}, 10, Random(1));
    final cont = <int, int>{};
    for (final e in r) {
      cont[e.complexidade] = (cont[e.complexidade] ?? 0) + 1;
    }
    expect(cont, {3: 6, 2: 3, 1: 1});
    expect(r.toSet().length, 10);
  });

  test('Fácil só traz perguntas de reconhecer', () {
    final r = sortearPorMistura(banco, {1: 100}, 5, Random(2));
    expect(r.every((e) => e.complexidade == 1), isTrue);
  });

  test('sem perguntas difíceis, completa com as mais próximas', () {
    final r = sortearPorMistura(banco, {4: 50, 3: 30, 2: 20}, 10, Random(3));
    expect(r.length, 10);
    expect(r.where((e) => e.complexidade == 3).length, 8);
  });

  test('convite para subir: 80% em 2 missões seguidas, depois recomeça', () {
    var r = avaliarConvite(0, 90);
    expect((r.sequencia, r.convidar), (1, false));
    r = avaliarConvite(r.sequencia, 80);
    expect((r.sequencia, r.convidar), (0, true));
    r = avaliarConvite(1, 70);
    expect((r.sequencia, r.convidar), (0, false));
  });

  test('níveis trazem complexidade, mistura e incentivos', () {
    final j = jsonDecode(File('assets/conteudo/niveis.json').readAsStringSync()) as List;
    final niveis = [for (final n in j) Nivel.fromJson(n as Map<String, dynamic>)];
    expect([for (final n in niveis) n.complexidade], [1, 2, 3, 4]);
    for (final n in niveis) {
      expect(n.mistura.values.fold(0, (a, b) => a + b), 100, reason: n.id);
      expect(n.incentivosAcerto, isNotEmpty);
      expect(n.incentivosErro, isNotEmpty);
    }
  });

  test('perguntas do banco chegam com complexidade e medalhas', () {
    final j = jsonDecode(File('assets/conteudo/ano_3.json').readAsStringSync());
    final ano = ConteudoAno.fromJson(j as Map<String, dynamic>);
    final todas = [
      for (final b in ano.bimestres)
        for (final p in b.planetas)
          for (final s in p.setores)
            for (final m in s.missoes) ...m.exercicios
    ];
    final cs = {for (final e in todas) e.complexidade};
    expect(cs.containsAll([1, 2, 3]), isTrue);
    expect(todas.any((e) => e.medalha != null), isTrue);
  });
}

void _todasAsMissoesTemNiveis3e4(int anoNumero) {
  final j = jsonDecode(File('assets/conteudo/ano_$anoNumero.json').readAsStringSync());
  final ano = ConteudoAno.fromJson(j as Map<String, dynamic>);
  for (final b in ano.bimestres) {
    for (final p in b.planetas) {
      for (final s in p.setores) {
        for (final m in s.missoes) {
          final cs = {for (final e in [...m.exercicios, ...m.exerciciosDesafio]) e.complexidade};
          expect(cs.containsAll([3, 4]), isTrue, reason: m.id);
        }
      }
    }
  }
}

// Anos que já têm perguntas de aplicar (3) e analisar e criar (4) em todas as missões.
const anosComNiveisAvancados = [4];

void testesNiveisAvancados() {
  for (final a in anosComNiveisAvancados) {
    test('$aº ano: todas as missões têm perguntas de níveis 3 e 4', () => _todasAsMissoesTemNiveis3e4(a));
  }
}
