# Galáxia do Saber

App educacional (iOS e Android) para o Ensino Fundamental 1 (1º ao 5º ano),
baseado no material interativo "Galáxia do Saber" feito para o Bernardo.

Cada criança tem um perfil (nome, ano e um gatinho capitão da tripulação) e
entra no bimestre atual do seu ano. As matérias são **planetas**, as unidades
são **setores**, e cada setor tem missões, revisão 🏆 e cápsula de peixinhos 📦.
No fim de cada planeta há um **chefão**.

## Rodando

Requer Flutter 3.50 ou mais novo.

```bash
flutter pub get
flutter run
flutter test
```

## Como funciona

- **Missão:** cartões de briefing (com 🔊 Ouvir) e depois perguntas de 6 tipos:
  múltipla escolha, verdadeiro ou falso, completar, ordenar, ligar pares e separar em grupos.
  Errou? Aparece a explicação e a pergunta volta no fim.
- **Níveis:** Fácil, Difícil, Expert e Gênio do Universo (30 s por pergunta). Cada nível tem estrelas próprias.
- **Recompensas:** XP com nível e patente (Cadete → Lenda da Galáxia), peixinhos, sequência de dias e meta de 30 XP por dia.
- **Missões de hoje:** seguem o rodízio da BNCC (Português e Matemática todo dia, mais Ciências, História ou Geografia).
- **Bimestre:** o do calendário escolar (fev–abr 1º, mai–jul 2º, ago–set 3º, out–dez 4º). Os anteriores ficam abertos.
- **Dados:** só no aparelho (shared_preferences), atrás de interfaces em `lib/dados/` para trocar por nuvem depois.

## Conteúdo

- 4º ano, 4º bimestre: conteúdo completo da Galáxia (6 planetas, 44 missões, mais de 500 perguntas).
- Demais anos e bimestres: estrutura da BNCC, com missões "em construção" até o conteúdo ser escrito.

Formato e como regerar: [docs/formato_conteudo.md](docs/formato_conteudo.md).

## Código

| Pasta | O que tem |
|---|---|
| `lib/modelos` | conteúdo, perfil e progresso |
| `lib/logica/regras.dart` | caminho do planeta, bloqueios, missões do dia, montagem da partida, XP |
| `lib/dados` | repositórios (local) |
| `lib/telas` | perfis, cadastro, galáxia, planeta, partida |
| `lib/componentes` | tema, HUD, gatos, textos com frações, visuais e os 6 exercícios |
| `tool/` | extração da Galáxia e montagem do conteúdo |
