# Galáxia do Saber

App educacional (iOS e Android) para o Ensino Fundamental 1 (1º ao 5º ano),
baseado no material interativo "Galáxia do Saber" feito para o Bernardo.

Cada criança tem um perfil (nome, ano e um gatinho capitão da tripulação),
cadastrado pelos pais, e entra no **universo** do seu ano. Cada matéria é uma
**galáxia** e cada assunto (unidade) é um **planeta**, com missões, revisão 🏆
e cápsula de peixinhos 📦. No fim de cada bimestre da galáxia há a **estação
do chefão**. As missões rendem suprimentos para construir a **Nave Gatística**.

No conteúdo (JSON), uma "galáxia" é o conjunto de `planetas` da mesma matéria
nos 4 bimestres, e cada "planeta" do app é um `setor` desse JSON.

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
- **Missões de hoje:** provas marcadas pelos pais passam na frente; depois as matérias que têm aula no dia (horário dos pais) ou o rodízio da BNCC.
- **Bimestre:** o do calendário escolar (fev–abr 1º, mai–jul 2º, ago–set 3º, out–dez 4º). Planetas dos bimestres anteriores ficam abertos; os dos próximos, trancados.
- **Nave Gatística** (`lib/logica/nave.dart`): cada missão rende suprimentos da matéria (💎 Português, ⚙️ Matemática, 🔋 Ciências, 🗺️ Humanas, 💖 Ética, 📡 Inglês). Eles constroem 16 peças em 4 etapas; com a nave pronta, a tripulação está pronta para o universo do próximo ano.
- **Carinhas dos gatos:** a cada acerto ou erro uma carinha de gato pula na tela (😺😸😻😽 ou 😿🙀😾).
- **Desafios no meio da missão:** às vezes aparece um desafio relâmpago (responder em 25 s) ou da sequência (3 acertos seguidos), que vale suprimentos extras.
- **Prova surpresa:** no máximo uma por dia, pode aparecer no fim de uma missão, com 3 perguntas de missões já feitas (de matérias diferentes) e suprimento em dobro por acerto.
- **Área dos pais** (PIN de 4 números): cadastrar e editar filhos, horário das aulas de cada dia, provas (matéria, data, assuntos e recados) com treino e contagem regressiva para a criança, e acompanhamento (XP dos últimos 7 dias, acertos por matéria, preparação para as provas e missões que precisam de reforço).
- **Dados:** só no aparelho (shared_preferences), atrás de interfaces em `lib/dados/` para trocar por nuvem depois.

## Conteúdo

- 4º ano, 4º bimestre: conteúdo completo da Galáxia (6 planetas, 44 missões, mais de 500 perguntas).
- Todos os outros bimestres do 1º ao 5º ano: banco de perguntas próprio em `tool/perguntas/` (mais de 400 missões e 2.500 perguntas), seguindo a trilha da BNCC.

Formato e como regerar: [docs/formato_conteudo.md](docs/formato_conteudo.md).

## Código

| Pasta | O que tem |
|---|---|
| `lib/modelos` | conteúdo, perfil e progresso |
| `lib/logica/regras.dart` | caminho do planeta, bloqueios, missões do dia, montagem da partida, XP |
| `lib/dados` | repositórios (local) |
| `lib/logica/nave.dart` | suprimentos e peças da Nave Gatística |
| `lib/modelos/rotina.dart` | horário das aulas e provas (área dos pais) |
| `lib/telas` | perfis, área dos pais, universo, galáxia, planeta, partida (com treino e prova surpresa), nave, labirinto |
| `lib/componentes` | tema, HUD, gatos, carinhas de reação, desenhos de galáxia, planeta e nave, textos com frações, visuais e os 6 exercícios |
| `tool/` | extração da Galáxia e montagem do conteúdo |
