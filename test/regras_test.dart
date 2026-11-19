import 'dart:ui' show Color;

import 'package:flutter_test/flutter_test.dart';
import 'package:trilha_do_saber/logica/regras.dart';
import 'package:trilha_do_saber/modelos/conteudo.dart';
import 'package:trilha_do_saber/modelos/progresso.dart';

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

  test('estrelas são separadas por nível', () {
    final r = RegrasPlaneta(p, com({'m1': 3}), 'd');
    expect(r.atual, 0);
  });

  test('missões do dia seguem o rodízio', () {
    final port = planeta('a1b1-portugues', [Setor('p', 'P', '', [m('p1')])]);
    final cien = planeta('a1b1-ciencias', [Setor('c', 'C', '', [m('c1')])]);
    final hist = planeta('a1b1-historia', [Setor('h', 'H', '', [m('h1')])]);
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
