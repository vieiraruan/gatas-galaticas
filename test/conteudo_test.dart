import 'dart:convert';
import 'dart:io';
import 'dart:math';

import 'package:flutter_test/flutter_test.dart';
import 'package:trilha_do_saber/logica/regras.dart';
import 'package:trilha_do_saber/modelos/conteudo.dart';

ConteudoAno carregar(int ano) => ConteudoAno.fromJson(
    jsonDecode(File('assets/conteudo/ano_$ano.json').readAsStringSync())
        as Map<String, dynamic>);

List<Nivel> niveis() => (jsonDecode(File('assets/conteudo/niveis.json').readAsStringSync())
        as List)
    .map((n) => Nivel.fromJson(n as Map<String, dynamic>))
    .toList();

void main() {
  test('os 5 anos carregam com 4 bimestres e planetas', () {
    for (var ano = 1; ano <= 5; ano++) {
      final c = carregar(ano);
      expect(c.ano, ano);
      expect(c.bimestres.map((b) => b.numero), [1, 2, 3, 4]);
      for (final b in c.bimestres) {
        expect(b.planetas, isNotEmpty, reason: 'ano $ano bim ${b.numero}');
      }
      expect(c.rodizio[1], contains('portugues'));
    }
  });

  test('4º bimestre do 4º ano traz a Galáxia do Bernardo completa', () {
    final b = carregar(4).bimestre(4)!;
    expect(b.planetas.map((p) => p.nome), [
      'Planeta Letrônico',
      'Planeta Numerópolis',
      'Planeta Cosmociência',
      'Planeta Gaia',
      'Nebulosa da Poesia',
      'Planeta Big Ben',
    ]);
    final missoes = b.planetas.expand((p) => p.missoes).toList();
    expect(missoes.length, 44);
    expect(missoes.every((m) => !m.emBreve && m.briefing.isNotEmpty), isTrue);
  });

  test('todas as perguntas da Galáxia são válidas', () {
    expect(validarBimestre(carregar(4).bimestre(4)!), greaterThan(500));
  });

  test('banco de perguntas do 4º bimestre (1º, 2º, 3º e 5º ano) completo e válido', () {
    for (final ano in [1, 2, 3, 5]) {
      final b = carregar(ano).bimestre(4)!;
      expect(b.planetas.map((p) => p.id.split('-').last),
          ['portugues', 'matematica', 'ciencias', 'humanas', 'etica', 'ingles']);
      final missoes = b.planetas.expand((p) => p.missoes).toList();
      expect(missoes.length, 24, reason: 'ano $ano');
      for (final m in missoes) {
        expect(m.emBreve, isFalse, reason: m.id);
        expect(m.briefing, isNotEmpty, reason: m.id);
        expect(m.exercicios.length, greaterThanOrEqualTo(5), reason: m.id);
      }
      expect(validarBimestre(b), greaterThan(140));
    }
  });

  test('ajuste ao nível mantém a resposta certa e corta opções', () {
    final ns = niveis();
    final facil = ns.first;
    final rnd = Random(1);
    final b = carregar(4).bimestre(4)!;
    for (final m in b.planetas.expand((p) => p.missoes)) {
      for (final e in m.exercicios.whereType<Escolha>()) {
        final a = adaptar(e, facil, rnd) as Escolha;
        expect(a.respostaCerta, e.respostaCerta);
        if (e.embaralhar) expect(a.opcoes.length, lessThanOrEqualTo(facil.opcoes));
      }
    }
  });

  test('partida tem o número de perguntas do nível', () {
    final ns = niveis();
    final p = carregar(4).bimestre(4)!.planetas[1]; // Matemática
    final nos = nosDoPlaneta(p);
    for (final n in ns) {
      expect(montarPartida(nos.first, n, Random(2)).length, n.perguntasMissao);
      expect(montarPartida(nos.last, n, Random(2)).length, n.perguntasChefao);
    }
  });
}

/// Confere cada pergunta do bimestre e devolve quantas são.
int validarBimestre(BimestreConteudo b) {
  var total = 0;
  final ids = <String>{};
  for (final p in b.planetas) {
    for (final m in p.missoes) {
      expect(ids.add(m.id), isTrue, reason: 'id repetido ${m.id}');
      for (final e in [...m.exercicios, ...m.exerciciosDesafio]) {
        total++;
        switch (e) {
          case Escolha():
            expect(e.correta, inInclusiveRange(0, e.opcoes.length - 1));
            expect(e.opcoes.toSet().length, e.opcoes.length, reason: e.pergunta);
          case Completar():
            expect(e.pergunta, contains('___'));
            expect(e.opcoes.length, greaterThan(1));
            expect(e.opcoes.toSet().length, e.opcoes.length, reason: e.pergunta);
          case Ordenar():
            expect(e.itens.length, greaterThan(1));
          case Ligar():
            expect(e.pares.length, greaterThan(1));
            expect(e.pares.map((x) => x.$1).toSet().length, e.pares.length, reason: e.pergunta);
            expect(e.pares.map((x) => x.$2).toSet().length, e.pares.length, reason: e.pergunta);
          case Separar():
            expect(e.itens.every((i) => i.grupo < e.grupos.length), isTrue);
          case VerdadeiroFalso():
            break;
        }
      }
    }
  }
  return total;
}
