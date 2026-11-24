import 'dart:math';
import 'dart:ui' show Color;

import 'package:flutter_test/flutter_test.dart';
import 'package:trilha_do_saber/logica/regras.dart';
import 'package:trilha_do_saber/modelos/conteudo.dart';
import 'package:trilha_do_saber/modelos/progresso.dart';
import 'package:trilha_do_saber/modelos/rotina.dart';

const _q = Escolha(pergunta: 'q', opcoes: ['a', 'b']);

Missao m(String id, {bool vazia = false}) =>
    Missao(id: id, titulo: id, emoji: '⭐', exercicios: vazia ? const [] : const [_q]);

Planeta planeta(String id, List<Setor> setores) => Planeta(
      id: id,
      disciplina: 'Matemática',
      nomeCurto: 'Matemática',
      nome: 'Numerópolis',
      emoji: '🔢',
      cor: const Color(0xFF7C5CFF),
      corEscura: const Color(0xFF5A3FD6),
      corClara: const Color(0xFFEFEBFF),
      chefaoEmoji: '🤖',
      chefaoNome: 'Robô',
      decoracao: const [],
      setores: setores,
    );

Progresso com(Map<String, int> estrelas) => Progresso(estrelas: {
      for (final e in estrelas.entries) Progresso.chave('f', e.key): e.value,
    });

void main() {
  final p = planeta('a1b1-mat', [
    Setor('s1', 'Setor 1', '', [m('m1'), m('m2')]),
    Setor('s2', 'Setor 2', '', [m('m3', vazia: true), m('m4')]),
  ]);

  test('caminho: missões, revisão e cápsula por setor, chefão no fim', () {
    expect(nosDoPlaneta(p).map((n) => n.id), [
      'm1', 'm2', 's1-revisao', 's1-capsula',
      'm3', 'm4', 's2-revisao', 's2-capsula',
      'a1b1-mat-chefao',
    ]);
  });

  test('libera em ordem e pula missões em construção', () {
    var r = RegrasPlaneta(p, Progresso.vazio, 'f');
    expect(r.atual, 0);
    expect(r.bloqueado(0), isFalse);
    expect(r.bloqueado(1), isTrue);

    r = RegrasPlaneta(p, com({'m1': 3, 'm2': 2, 's1-revisao': 1}), 'f');
    expect(r.capsulaPronta(3), isTrue);
    expect(emBreve(r.nos[4]), isTrue); // m3 sem perguntas
    expect(r.atual, 5); // pula m3 e vai para m4
    expect(r.bloqueado(5), isFalse);
  });

  test('cada planeta (setor) libera sozinho; o chefão pede todos', () {
    final p2 = planeta('a1b1-mat', [
      Setor('s1', 'Setor 1', '', [m('m1'), m('m2')]),
      Setor('s2', 'Setor 2', '', [m('m3'), m('m4')]),
    ]);
    var r = RegrasPlaneta(p2, Progresso.vazio, 'f');
    expect(r.bloqueado(4), isFalse); // m3: primeiro do planeta 2
    expect(r.bloqueado(5), isTrue); // m4 depende de m3
    expect(r.bloqueado(r.indiceChefao), isTrue);
    expect(r.indicesDoSetor(1), [4, 5, 6, 7]);
    expect(r.atualDoSetor(1), 4);
    r = RegrasPlaneta(
        p2, com({'m1': 1, 'm2': 1, 's1-revisao': 1, 'm3': 1, 'm4': 1, 's2-revisao': 1}), 'f');
    expect(r.bloqueado(r.indiceChefao), isFalse);
    expect(r.resumoDoSetor(0).feitas, 3);
    expect(setorDoNo(r.nos.last), -1);
  });

  test('galáxias: matéria pelo id do planeta, nos 4 bimestres', () {
    expect(materiaDoPlaneta(p), 'matematica');
    final c = ConteudoAno(1, '1º', [
      BimestreConteudo(1, '1º', [planeta('a1b1-matematica', const [])]),
      BimestreConteudo(2, '2º', [planeta('a1b2-matematica', const [])]),
    ], const {});
    expect(partesDaGalaxia(c, 'matematica').map((x) => x.bimestre.numero), [1, 2]);
    expect(galaxiaDe('portugues').nome, 'Galáxia das Letras');
  });

  test('horário dos pais e provas mudam as missões do dia', () {
    final port = planeta('a1b1-portugues', [Setor('p', 'P', '', [m('p1')])]);
    final ing = planeta('a1b1-ingles', [Setor('i', 'I', '', [m('i1')])]);
    final mat = planeta('a1b1-mat', [
      Setor('fra', 'Frações', '', [m('f1')]),
      Setor('dec', 'Decimais', '', [m('d1')]),
    ]);
    final b = BimestreConteudo(1, '1º', [port, mat, ing]);
    final c = ConteudoAno(1, '1º ano', [b], {
      2: ['portugues', 'matematica'],
    });
    final terca = DateTime(2026, 11, 24);
    // Sem rotina: rodízio.
    var hoje = missoesDoDia(
        conteudo: c, bimestre: b, progresso: Progresso.vazio, nivel: 'f', hoje: terca);
    expect(hoje.first.planeta.id, 'a1b1-portugues');
    // Horário: terça tem Inglês.
    var rotina = const Rotina(horario: {
      2: ['ingles']
    });
    hoje = missoesDoDia(
        conteudo: c, bimestre: b, progresso: Progresso.vazio, nivel: 'f', hoje: terca, rotina: rotina);
    expect(hoje.first.planeta.id, 'a1b1-ingles');
    expect(hoje.first.motivo, '🏫 Teve aula hoje');
    // Prova de Matemática (Decimais) em 3 dias passa na frente.
    rotina = rotina.copyWith(provas: [
      Prova(id: 'x', materia: 'matematica', data: DateTime(2026, 11, 27), assuntos: const ['dec']),
    ]);
    hoje = missoesDoDia(
        conteudo: c, bimestre: b, progresso: Progresso.vazio, nivel: 'f', hoje: terca, rotina: rotina);
    expect(hoje.first.no.id, 'd1');
    expect(hoje.first.motivo, '📝 Prova em 3 dias');
    expect(hoje.length, 3);
    // Prova que já passou não conta.
    expect(rotina.proximas(DateTime(2026, 11, 28)), isEmpty);
  });

  test('prova surpresa usa missões já feitas, de matérias diferentes', () {
    final port = planeta('a1b1-portugues', [Setor('p', 'P', '', [m('p1'), m('p2')])]);
    final prog = com({'m1': 2, 'm2': 3, 'p1': 1});
    final no = montarSurpresa([p, port], prog, 'f', Random(1))!;
    expect(no.missoes.length, 3);
    expect(no.missoes.map((x) => x.id).toSet().containsAll(['p1']), isTrue);
    expect(montarSurpresa([p], Progresso.vazio, 'f', Random(1)), isNull);
    final hoje = DateTime(2026, 11, 24);
    final jaTeve = Progresso(surpresasPorDia: {chaveDia(hoje): 1});
    expect(List.generate(20, (_) => sortearSurpresa(jaTeve, hoje, Random())), everyElement(false));
  });

  test('desafio aparece no meio da missão, nunca no chefão', () {
    final r = RegrasPlaneta(p, Progresso.vazio, 'f');
    var achou = 0;
    for (var i = 0; i < 50; i++) {
      final d = sortearDesafio(r.nos.first, 6, Random(i));
      if (d == null) continue;
      achou++;
      expect(d.antesDe, inInclusiveRange(1, d.tipo == TipoDesafio.sequencia ? 3 : 5));
    }
    expect(achou, greaterThan(10));
    expect(sortearDesafio(r.nos.last, 8, Random(1)), isNull);
  });

  test('estrelas são separadas por nível', () {
    final r = RegrasPlaneta(p, com({'m1': 3}), 'd');
    expect(r.atual, 0);
  });

  test('missões do dia seguem o rodízio', () {
    final port = planeta('a1b1-portugues', [Setor('p', 'P', '', [m('p1')])]);
    final cien = planeta('a1b1-ciencias', [Setor('c', 'C', '', [m('c1')])]);
    final hist = planeta('a1b1-humanas', [Setor('h', 'H', '', [m('h1')])]);
    final b = BimestreConteudo(1, '1º', [hist, cien, p, port]);
    final c = ConteudoAno(1, '1º ano', [b], {
      4: ['portugues', 'matematica', 'ciencias'],
    });
    final quinta = DateTime(2026, 11, 19);
    final hoje = missoesDoDia(
        conteudo: c, bimestre: b, progresso: Progresso.vazio, nivel: 'f', hoje: quinta);
    expect(hoje.map((x) => x.planeta.id), ['a1b1-portugues', 'a1b1-mat', 'a1b1-ciencias']);
  });

  test('sequência, patente e estrelas', () {
    final xp = {'2026-11-17': 10, '2026-11-18': 20, '2026-11-19': 5, '2026-11-14': 9};
    expect(sequenciaDias(xp, DateTime(2026, 11, 19)), 3);
    expect(sequenciaDias(xp, DateTime(2026, 11, 20)), 3);
    expect(sequenciaDias(xp, DateTime(2026, 11, 21)), 0);
    expect(patente(0), 'Cadete');
    expect(patente(xpPorNivel * 2), 'Piloto');
    expect(estrelasPorAcerto(5, 5), 3);
    expect(estrelasPorAcerto(4, 5), 2);
    expect(estrelasPorAcerto(3, 5), 1);
    expect(bimestreDoCalendario(DateTime(2026, 11, 19)), 4);
  });
}
