import 'dart:math';

import 'package:flutter_test/flutter_test.dart';
import 'package:trilha_do_saber/logica/labirinto.dart';
import 'package:trilha_do_saber/modelos/conteudo.dart';

void main() {
  test('tamanho cresce do 1º (5×5) ao 5º ano (9×9)', () {
    expect([for (var a = 1; a <= 5; a++) ConfigLabirinto.doAno(a).lado], [5, 6, 7, 8, 9]);
    expect(ConfigLabirinto.doAno(1).segundosBonus, 0);
    expect(ConfigLabirinto.doAno(4).segundosBonus, greaterThan(0));
  });

  test('modo calmo não tem aspiradores', () {
    expect(ConfigLabirinto.doAno(5, calmo: true).aspiradores, 0);
  });

  for (var ano = 1; ano <= 5; ano++) {
    test('labirintos do $anoº ano sempre têm saída e nada isolado', () {
      for (var semente = 0; semente < 40; semente++) {
        final c = ConfigLabirinto.doAno(ano);
        final lab = Labirinto.gerar(c, Random(semente));
        final pocas = {
          for (final e in lab.itens.entries)
            if (e.value == Item.poca) e.key
        };
        // A saída é alcançável sem passar por poças.
        expect(lab.caminho(lab.inicio, lab.saida, evitar: pocas), isNotEmpty);
        // Toda casa sem poça é alcançável.
        for (var y = 0; y < lab.lado; y++) {
          for (var x = 0; x < lab.lado; x++) {
            final p = Pos(x, y);
            if (pocas.contains(p)) continue;
            expect(lab.caminho(lab.inicio, p, evitar: pocas), isNotEmpty,
                reason: 'semente $semente casa $p');
          }
        }
        expect(lab.itens.values.where((i) => i == Item.porta).length, c.portas);
        expect(lab.itens.containsKey(lab.inicio), isFalse);
        expect(lab.itens.containsKey(lab.saida), isFalse);
        expect(lab.aspiradores.length, lessThanOrEqualTo(c.aspiradores));
        for (final a in lab.aspiradores) {
          expect(a.trilho.contains(lab.inicio), isFalse);
        }
      }
    });
  }

  test('aspirador patrulha ida e volta', () {
    final a = Aspirador(const [Pos(0, 0), Pos(1, 0), Pos(2, 0)]);
    final visitas = <Pos>[];
    for (var i = 0; i < 5; i++) {
      a.andar();
      visitas.add(a.pos);
    }
    expect(visitas, const [Pos(1, 0), Pos(2, 0), Pos(1, 0), Pos(0, 0), Pos(1, 0)]);
  });

  test('cada gata tem seu poder; 3 estrelas dão um uso extra', () {
    expect(poderDaGata('nala'), Poder.invasaoRapida);
    expect(poderDaGata('baguera'), Poder.miadoSonico);
    expect(poderDaGata('desconhecida'), Poder.olharSoberano);
    expect(usosDoPoder(2), 1);
    expect(usosDoPoder(3), 2);
  });

  test('portas relembram mais missões anteriores do que a recente', () {
    Missao m(String id, String q) => Missao(id: id, titulo: id, emoji: '⭐', exercicios: [
          Escolha(pergunta: q, opcoes: const ['certa', 'b', 'c', 'd', 'e'], explicacao: 'x'),
          VerdadeiroFalso('$q?', null, true),
          Ordenar('ignorada', null, const ['a', 'b']),
        ]);
    final d = desafiosDeLembranca(
        anteriores: [m('a', 'antiga1'), m('b', 'antiga2')],
        recentes: [m('c', 'nova')],
        rnd: Random(1),
        quantidade: 6);
    expect(d, hasLength(6));
    expect(d.where((x) => x.pergunta.startsWith('nova')).length, 2);
    for (final x in d) {
      expect(x.opcoes.length, lessThanOrEqualTo(3));
      expect(x.correta, inInclusiveRange(0, x.opcoes.length - 1));
      if (x.opcoes.length == 3) expect(x.opcoes[x.correta], 'certa');
    }
  });

  test('recompensa do labirinto é menor que a de uma missão', () {
    final r = recompensaLabirinto(peixesPegos: 4, bonusTempo: true, multiplicador: 1);
    expect(r.xp, 5);
    expect(r.peixinhos, 12);
  });
}
