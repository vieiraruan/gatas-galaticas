# Trilha do Saber

App educacional (iOS e Android) para o Ensino Fundamental 1 (1º ao 5º ano).
Cada criança tem um perfil ligado ao seu ano escolar e segue uma trilha
dividida em 4 bimestres, com uma missão nova por dia.

> "Trilha do Saber" é um nome provisório.

## Rodando

Requer Flutter 3.50 ou mais novo.

```bash
flutter pub get
flutter run          # com um emulador ou celular conectado
flutter test         # testes de regras e do fluxo principal
```

## Arquitetura

| Parte | Escolha |
|---|---|
| Estado | Riverpod (`lib/providers.dart`) |
| Navegação | go_router (`lib/app.dart`) |
| Dados da criança e progresso | Só no aparelho, com shared_preferences, atrás das interfaces em `lib/data/repositorios.dart` (para trocar por nuvem depois) |
| Conteúdo pedagógico | JSON por ano em `assets/curriculo/` ([formato](docs/formato_curriculo.md)) |
| Regras da trilha | `lib/logic/regras_trilha.dart` (bimestre do calendário, missão do dia, sequência de dias, estrelas) |

### Telas
- `features/profiles`: "Quem vai jogar?" e cadastro da criança (nome, ano, avatar). Segurar o cartão remove o perfil.
- `features/track`: trilha do ano com estrelas, dias seguidos, missão do dia e os 4 bimestres.
- `features/mission`: perguntas de múltipla escolha com retorno imediato e 1 a 3 estrelas.

### Regras da missão diária
- Bimestre pelo calendário: fev–abr 1º, mai–jul 2º, ago–set 3º, out–dez 4º (janeiro conta como 1º).
- Bimestres futuros ficam fechados; anteriores ficam abertos para recuperar.
- Dentro do bimestre as missões seguem em ordem, e a criança libera 1 missão nova por dia (`missoesNovasPorDia`).
- Missões concluídas podem ser refeitas para melhorar as estrelas.
