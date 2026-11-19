import 'dart:convert';
import 'dart:io';

import 'package:flutter_test/flutter_test.dart';
import 'package:trilha_do_saber/logic/regras_trilha.dart';
import 'package:trilha_do_saber/models/curriculo.dart';
import 'package:trilha_do_saber/models/progresso.dart';

TrilhaAno carregar(int ano) => TrilhaAno.fromJson(
    jsonDecode(File('assets/curriculo/ano_$ano.json').readAsStringSync())
        as Map<String, dynamic>);

void main() {
  test('todos os anos de 1 a 5 têm 4 bimestres com missões válidas', () {
    for (var ano = 1; ano <= 5; ano++) {
      final t = carregar(ano);
      expect(t.ano, ano);
      expect(t.bimestres.map((b) => b.numero), [1, 2, 3, 4]);
      for (final b in t.bimestres) {
        expect(b.missoes, isNotEmpty);
        for (final m in b.missoes) {
          expect(m.questoes, isNotEmpty);
        }
      }
    }
  });

  test('bimestre do calendário', () {
    expect(bimestreDoCalendario(DateTime(2026, 2, 10)), 1);
    expect(bimestreDoCalendario(DateTime(2026, 6, 1)), 2);
    expect(bimestreDoCalendario(DateTime(2026, 8, 20)), 3);
    expect(bimestreDoCalendario(DateTime(2026, 11, 19)), 4);
  });

  group('missão do dia', () {
    final trilha = carregar(1);
    final b4 = trilha.bimestre(4)!;
    final hoje = DateTime(2026, 11, 19, 10);

    test('sem progresso: primeira missão do bimestre atual', () {
      final r = RegrasTrilha(
          trilha: trilha, progresso: Progresso.vazio, hoje: hoje);
      expect(r.missaoDoDia!.id, b4.missoes.first.id);
      expect(r.status(b4, b4.missoes[0]), StatusMissao.disponivel);
      expect(r.status(b4, b4.missoes[1]), StatusMissao.bloqueada);
    });

    test('depois de concluir uma hoje, a próxima fica para amanhã', () {
      final p = Progresso({
        b4.missoes[0].id: MissaoConcluida(
            missaoId: b4.missoes[0].id, data: hoje, estrelas: 3),
      });
      final r = RegrasTrilha(trilha: trilha, progresso: p, hoje: hoje);
      expect(r.status(b4, b4.missoes[0]), StatusMissao.concluida);
      expect(r.status(b4, b4.missoes[1]), StatusMissao.amanha);

      final amanha = RegrasTrilha(
          trilha: trilha,
          progresso: p,
          hoje: hoje.add(const Duration(days: 1)));
      expect(amanha.status(b4, b4.missoes[1]), StatusMissao.disponivel);
    });

    test('bimestres futuros ficam bloqueados', () {
      final r = RegrasTrilha(
          trilha: trilha,
          progresso: Progresso.vazio,
          hoje: DateTime(2026, 3, 1));
      final b2 = trilha.bimestre(2)!;
      expect(r.status(b2, b2.missoes.first), StatusMissao.bloqueada);
    });

    test('bimestre atual completo: recupera bimestres anteriores', () {
      final p = Progresso({
        for (final m in b4.missoes)
          m.id: MissaoConcluida(
              missaoId: m.id, data: DateTime(2026, 11, 1), estrelas: 2),
      });
      final r = RegrasTrilha(trilha: trilha, progresso: p, hoje: hoje);
      expect(r.missaoDoDia!.id, trilha.bimestre(1)!.missoes.first.id);
    });
  });

  test('sequência de dias seguidos', () {
    final trilha = carregar(1);
    MissaoConcluida em(String id, int dia) => MissaoConcluida(
        missaoId: id, data: DateTime(2026, 11, dia, 9), estrelas: 1);
    final p = Progresso({
      'a': em('a', 16),
      'b': em('b', 17),
      'c': em('c', 18),
      'd': em('d', 14),
    });
    expect(
        RegrasTrilha(trilha: trilha, progresso: p, hoje: DateTime(2026, 11, 19))
            .sequenciaDias,
        3);
    expect(
        RegrasTrilha(trilha: trilha, progresso: p, hoje: DateTime(2026, 11, 21))
            .sequenciaDias,
        0);
  });

  test('estrelas por acertos', () {
    expect(estrelasPorAcertos(3, 3), 3);
    expect(estrelasPorAcertos(2, 3), 2);
    expect(estrelasPorAcertos(1, 3), 1);
  });
}
