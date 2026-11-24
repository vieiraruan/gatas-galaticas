import 'dart:math';

import '../modelos/progresso.dart';
import 'regras.dart';

/// Nave Gatística: cada missão rende suprimentos da matéria estudada, e os
/// suprimentos constroem as peças da nave em 4 etapas. Com as 4 etapas
/// prontas, a nave leva a tripulação ao universo do próximo ano.
/// Tudo aqui é puro (sem Flutter) para facilitar os testes.

class Suprimento {
  final String materia;
  final String nome;
  final String emoji;
  const Suprimento(this.materia, this.nome, this.emoji);
}

const suprimentos = [
  Suprimento('portugues', 'Cristais de Palavras', '💎'),
  Suprimento('matematica', 'Engrenagens', '⚙️'),
  Suprimento('ciencias', 'Células de Energia', '🔋'),
  Suprimento('humanas', 'Mapas Estelares', '🗺️'),
  Suprimento('etica', 'Corações de Coragem', '💖'),
  Suprimento('ingles', 'Antenas Tradutoras', '📡'),
];

Suprimento suprimentoDe(String materia) => suprimentos.firstWhere(
    (s) => s.materia == materia,
    orElse: () => Suprimento(materia, materia, '📦'));

class PecaNave {
  final String id;
  final String nome;
  final String emoji;
  final int etapa;
  final Map<String, int> custo;
  const PecaNave(this.id, this.nome, this.emoji, this.etapa, this.custo);
}

const etapasNave = [
  'Decolagem',
  'Voo estável',
  'Exploração',
  'Salto entre universos',
];

const pecasNave = [
  PecaNave('casco', 'Casco de Bigodes', '🛸', 1, {'matematica': 3, 'portugues': 3}),
  PecaNave('cabine', 'Cabine da Capitania', '🪟', 1, {'portugues': 3, 'ciencias': 2}),
  PecaNave('motor', 'Motor de Ronronar', '🔥', 1, {'ciencias': 3, 'matematica': 2}),
  PecaNave('orelhas', 'Antenas-Orelha', '📡', 1, {'ingles': 2, 'humanas': 2}),
  PecaNave('asaEsquerda', 'Asa Esquerda', '🪽', 2, {'matematica': 4, 'humanas': 3}),
  PecaNave('asaDireita', 'Asa Direita', '🪽', 2, {'portugues': 4, 'etica': 3}),
  PecaNave('farois', 'Faróis Olho-de-Gato', '💡', 2, {'ingles': 3, 'portugues': 3}),
  PecaNave('escudo', 'Escudo de Novelo', '🧶', 2, {'etica': 3, 'ciencias': 3}),
  PecaNave('propulsores', 'Propulsores Gêmeos', '🚀', 3, {'matematica': 5, 'ciencias': 4}),
  PecaNave('radar', 'Radar de Bigodes', '📻', 3, {'humanas': 4, 'ingles': 4}),
  PecaNave('janelas', 'Janelas Panorâmicas', '🔭', 3, {'portugues': 5, 'matematica': 4}),
  PecaNave('cauda', 'Cauda Estabilizadora', '🐈', 3, {'etica': 4, 'humanas': 4}),
  PecaNave('anel', 'Anel de Dobra Espacial', '💫', 4, {'matematica': 6, 'ciencias': 5}),
  PecaNave('paineis', 'Painéis Solares', '🔆', 4, {'ciencias': 5, 'portugues': 5}),
  PecaNave('bandeira', 'Bandeira da Tripulação', '🚩', 4, {'humanas': 5, 'etica': 5}),
  PecaNave('nucleo', 'Núcleo de Salto', '🌀', 4, {'portugues': 6, 'matematica': 6, 'ingles': 5}),
];

PecaNave? pecaPorId(String id) {
  for (final p in pecasNave) {
    if (p.id == id) return p;
  }
  return null;
}

/// Quantas etapas estão completas (0 a 4).
int etapasCompletas(Set<String> pecas) {
  var n = 0;
  for (var e = 1; e <= etapasNave.length; e++) {
    if (pecasNave.where((p) => p.etapa == e).every((p) => pecas.contains(p.id))) {
      n = e;
    } else {
      break;
    }
  }
  return n;
}

/// Etapa em construção (1 a 4), ou 5 quando a nave está pronta.
int etapaAtual(Set<String> pecas) => etapasCompletas(pecas) + 1;

bool navePronta(Set<String> pecas) => etapasCompletas(pecas) == etapasNave.length;

bool podePagar(PecaNave peca, Map<String, int> estoque) =>
    peca.custo.entries.every((c) => (estoque[c.key] ?? 0) >= c.value);

/// Peça liberada para construir: da etapa atual e ainda não feita.
bool pecaLiberada(PecaNave peca, Set<String> pecas) =>
    !pecas.contains(peca.id) && peca.etapa == etapaAtual(pecas);

/// Constrói a peça, se der. Devolve null se faltar suprimento ou etapa.
Progresso? comPecaConstruida(Progresso p, PecaNave peca) {
  if (!pecaLiberada(peca, p.pecas) || !podePagar(peca, p.suprimentos)) return null;
  return p.copyWith(
    suprimentos: {
      ...p.suprimentos,
      for (final c in peca.custo.entries) c.key: (p.suprimentos[c.key] ?? 0) - c.value,
    },
    pecas: {...p.pecas, peca.id},
  );
}

/// Suprimentos ganhos numa partida. Na primeira vez (ou quando melhora as
/// estrelas) rende cheio; repetir sem melhorar rende 1.
int suprimentosDaPartida(No no, int estrelas, {required bool melhorou}) {
  if (!melhorou) return 1;
  return switch (no) {
    NoMissao() => estrelas,
    NoRevisao() => estrelas + 1,
    NoChefao() => 5,
    NoTreino() => estrelas + 1,
    _ => max(1, estrelas),
  };
}

Map<String, int> somar(Map<String, int> a, Map<String, int> b) => {
      ...a,
      for (final e in b.entries) e.key: (a[e.key] ?? 0) + e.value,
    };
