import 'dart:math';

import 'package:flutter_test/flutter_test.dart';
import 'package:trilha_do_saber/logica/labirinto.dart';
import 'package:trilha_do_saber/logica/minijogos.dart';

void main() {
  group('Patrulha da Luz', () {
    test('raio acende drone e conta ponto', () {
      final j = Patrulha(4, Random(1));
      j.drones.add(Drone(0.4, 0.5, 0));
      j.moverPara(0.5);
      for (var i = 0; i < 40; i++) {
        j.passo(0.02);
      }
      expect(j.acesos, greaterThanOrEqualTo(1));
      expect(j.escudos, 3);
    });

    test('drone apagado na nave tira um escudo e dá um respiro', () {
      final j = Patrulha(4, Random(1));
      j.drones.add(Drone(Patrulha.naveX, 0.2, 0));
      j.moverPara(0.2);
      j.passo(0.01);
      expect(j.escudos, 2);
      j.drones.add(Drone(Patrulha.naveX, 0.2, 0));
      j.passo(0.01);
      expect(j.escudos, 2, reason: 'invencível logo depois de bater');
    });

    test('acaba no tempo', () {
      final j = Patrulha(1, Random(2), duracao: 1);
      for (var i = 0; i < 60; i++) {
        j.passo(0.02);
      }
      expect(j.acabou, isTrue);
    });
  });

  group('Cauda de Cometa', () {
    const d = DesafioPorta('2 + 2?', ['4', '5', '3'], 0, null);

    test('começa com 3 pedaços, pergunta e respostas no mapa', () {
      final j = Cauda(Random(3), const [d]);
      expect(j.corpo, hasLength(3));
      expect(j.pergunta, d);
      expect(j.respostas.where((r) => r.certa), hasLength(1));
      expect(j.estrelas, hasLength(3));
    });

    test('resposta certa faz crescer 3; errada mostra a certa', () {
      final j = Cauda(Random(3), const [d]);
      final cabeca = j.corpo.first;
      final frente = Pos(cabeca.x + 1, cabeca.y);
      j.estrelas.clear();
      j.respostas = [Resposta(frente, '4', true)];
      j.passo();
      expect(j.acertos, 1);
      expect(j.crescer, 3);
      final c2 = j.corpo.first;
      j.respostas = [Resposta(Pos(c2.x + 1, c2.y), '5', false)];
      j.passo();
      expect(j.erros, 1);
      expect(j.retorno, contains('4'));
    });

    test('não dá meia-volta e atravessa a borda', () {
      final j = Cauda(Random(3), const []);
      j.estrelas.clear();
      j.virar(Dir.esquerda);
      j.passo();
      expect(j.dir, Dir.direita);
      for (var i = 0; i < j.colunas; i++) {
        j.passo();
      }
      expect(j.bateu, isFalse);
    });

    test('bater na própria cauda encerra', () {
      final j = Cauda(Random(3), const []);
      j.estrelas.clear();
      j.crescer = 5;
      for (final d in [Dir.direita, Dir.direita, Dir.baixo, Dir.esquerda, Dir.cima]) {
        j.virar(d);
        j.passo();
      }
      expect(j.bateu, isTrue);
    });
  });

  group('Travessia do Cinturão', () {
    test('sem tocar, a nave cai e bate no chão', () {
      final j = Travessia(3, Random(4))..tocar();
      for (var i = 0; i < 300 && !j.bateu; i++) {
        j.passo(0.02);
      }
      expect(j.bateu, isTrue);
    });

    test('passagem é mais larga no 1º ano do que no 5º', () {
      expect(Travessia(1, Random(1)).abertura, greaterThan(Travessia(5, Random(1)).abertura));
    });

    test('voando no centro da passagem conta pontos', () {
      final j = Travessia(1, Random(5))..tocar();
      for (var i = 0; i < 1500 && !j.bateu; i++) {
        // Piloto automático: mira o centro da próxima passagem.
        final alvo = j.colunas.where((c) => c.x > Travessia.naveX - 0.1).firstOrNull?.centro ?? 0.5;
        if (j.y > alvo + 0.03 && j.vy > -0.1) j.tocar();
        j.passo(0.02);
      }
      expect(j.passagens, greaterThan(3));
    });
  });

  test('peixinhos do minijogo ficam entre 3 e 15', () {
    expect(peixinhosDoMinijogo(0), 3);
    expect(peixinhosDoMinijogo(9), 6);
    expect(peixinhosDoMinijogo(300), 15);
  });
}
