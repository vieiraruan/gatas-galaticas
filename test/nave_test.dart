import 'package:flutter_test/flutter_test.dart';
import 'package:trilha_do_saber/logica/nave.dart';
import 'package:trilha_do_saber/logica/regras.dart';
import 'package:trilha_do_saber/modelos/conteudo.dart';
import 'package:trilha_do_saber/modelos/progresso.dart';
import 'package:trilha_do_saber/modelos/rotina.dart';

void main() {
  test('16 peças em 4 etapas, com ids únicos e custos das 6 matérias', () {
    expect(pecasNave.length, 16);
    expect(pecasNave.map((p) => p.id).toSet().length, 16);
    for (var e = 1; e <= 4; e++) {
      expect(pecasNave.where((p) => p.etapa == e).length, 4);
    }
    final materias = {for (final p in pecasNave) ...p.custo.keys};
    expect(materias, {for (final s in suprimentos) s.materia});
  });

  test('constrói peça só da etapa atual e com suprimento suficiente', () {
    final casco = pecaPorId('casco')!;
    final asa = pecaPorId('asaEsquerda')!;
    var p = const Progresso(suprimentos: {'matematica': 10, 'portugues': 2, 'humanas': 9});
    expect(comPecaConstruida(p, casco), isNull); // falta português
    p = p.copyWith(suprimentos: {...p.suprimentos, 'portugues': 3});
    final depois = comPecaConstruida(p, casco)!;
    expect(depois.pecas, {'casco'});
    expect(depois.suprimentos['matematica'], 7);
    expect(depois.suprimentos['portugues'], 0);
    expect(comPecaConstruida(depois, casco), isNull); // já feita
    expect(comPecaConstruida(depois, asa), isNull); // etapa 2 ainda trancada
  });

  test('etapas completas e nave pronta', () {
    final todas = {for (final p in pecasNave) p.id};
    expect(etapasCompletas(const {}), 0);
    expect(etapaAtual(const {}), 1);
    final etapa1 = {for (final p in pecasNave.where((p) => p.etapa == 1)) p.id};
    expect(etapasCompletas(etapa1), 1);
    expect(etapaAtual(etapa1), 2);
    expect(navePronta(todas), isTrue);
  });

  test('suprimentos por partida: cheio quando melhora, 1 quando repete', () {
    const q = Escolha(pergunta: 'q', opcoes: ['a', 'b']);
    const setor = Setor('s', 'S', '', [Missao(id: 'm', titulo: 'm', emoji: '⭐', exercicios: [q])]);
    final missao = NoMissao(setor.missoes.first, setor, 0);
    expect(suprimentosDaPartida(missao, 3, melhorou: true), 3);
    expect(suprimentosDaPartida(missao, 3, melhorou: false), 1);
    expect(suprimentosDaPartida(NoRevisao(setor, 0), 2, melhorou: true), 3);
    expect(somar({'a': 1}, {'a': 2, 'b': 1}), {'a': 3, 'b': 1});
  });

  test('progresso e rotina sobrevivem ao JSON', () {
    final p = Progresso.fromJson(const Progresso(
      suprimentos: {'matematica': 4},
      pecas: {'casco'},
      acertosPorMateria: {'matematica': 3},
      respostasPorMateria: {'matematica': 5},
      surpresasPorDia: {'2026-11-24': 1},
    ).toJson());
    expect(p.suprimentos, {'matematica': 4});
    expect(p.pecas, {'casco'});
    expect(p.respostasPorMateria['matematica'], 5);
    expect(p.surpresasPorDia['2026-11-24'], 1);
    // JSON antigo (sem os campos novos) continua abrindo.
    expect(Progresso.fromJson({'xp': 10}).suprimentos, isEmpty);

    final r = Rotina.fromJson(Rotina(horario: const {
      1: ['portugues', 'matematica']
    }, provas: [
      Prova(id: '1', materia: 'ciencias', data: DateTime(2026, 12, 3), assuntos: const ['x'], observacao: 'Ler cap. 4'),
    ]).toJson());
    expect(r.horario[1], ['portugues', 'matematica']);
    expect(r.provas.single.data, DateTime(2026, 12, 3));
    expect(r.provas.single.observacao, 'Ler cap. 4');
    expect(r.provas.single.diasAte(DateTime(2026, 11, 30, 18)), 3);
  });
}
