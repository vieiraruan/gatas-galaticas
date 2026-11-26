# Formato do conteúdo

Cada ano tem um arquivo `assets/conteudo/ano_N.json`, gerado por
`tool/montar_conteudo.py` a partir de duas fontes:

1. **Trilha da BNCC** (`trilhas/trilhas_ef1_bncc.json`): define bimestres,
   disciplinas, unidades e modelos de missão. Missões sem perguntas aparecem
   no app como "em construção" 🛠️.
2. **Galáxia do Saber** (material interativo do Bernardo), extraída por
   `tool/extrair_galaxia.js`: conteúdo completo, usado no 4º bimestre do 4º ano.

Para regerar:

```bash
node tool/extrair_galaxia.js <galaxia.html> /tmp/galaxia.json
python3 tool/montar_conteudo.py docs/trilhas/trilhas_ef1_bncc.json /tmp/galaxia.json assets/conteudo
```

## Estrutura

```
ano → bimestres[] → planetas[] (disciplinas) → setores[] (unidades) → missoes[]
```

O app monta sozinho, em cada setor, a **revisão** 🏆 e a **cápsula** 📦, e no fim
de cada planeta o **chefão**.

```json
{
  "id": "a4b4-p11",
  "titulo": "Discurso",
  "emoji": "🎤",
  "briefing": [{ "emoji": "🎤", "texto": "O **DISCURSO** é ...", "visuais": [] }],
  "exercicios": [ ... ],
  "exerciciosDesafio": [ ... ]
}
```

`exerciciosDesafio` (opcional) é usado nos níveis Expert e Gênio (números maiores).

## Tipos de exercício

| tipo | campos |
|---|---|
| `escolha` | `pergunta`, `opcoes`, `correta` (índice), `embaralhar`, `visuais`, `dica`, `dicaVisuais`, `explicacao` |
| `verdadeiroFalso` | `pergunta`, `resposta` (true/false), `explicacao` |
| `completar` | `pergunta` com `___`, `opcoes` (a primeira é a certa), `explicacao` |
| `ordenar` | `pergunta`, `itens` (já na ordem certa), `explicacao` |
| `ligar` | `pergunta`, `pares` ([esquerda, direita]) |
| `separar` | `pergunta`, `grupos`, `itens` ([{texto, grupo}]), `explicacao` |

## Marcação de texto

`**negrito**`, `\n` para quebra de linha, `[[3/4]]` para fração empilhada e
`{nome}` para o nome da criança.

## Visuais

`svg` (desenho pronto), `svgs`, `emoji`, `caixa` (texto, poema ou destaque),
`comparar` (barras de frações), `grupos`, `tabuada`, `dinheiro` (centavos) e
`valorPosicional`.

## Regras importantes

- O `id` de uma missão **não deve mudar** depois de publicado: o progresso é salvo por ele.
- Os ids levam o prefixo do ano e bimestre (ex.: `a4b4-`) para não se repetirem.

## Complexidade e medalhas (trilha 2.1.0)

Cada exercício pode ter `complexidade` (1 reconhecer, 2 compreender, 3 aplicar,
4 analisar e criar) e `medalha` (`detetive`, `explicador`, `inventor`). No banco,
use `nivel(3, mc(...))` ou `nivel(4, tf(...), "detetive")` de `tool/perguntas/base.py`.
Sem marcação, `tool/complexidade.py` estima pelo tipo e pelo texto.

`niveis.json` junta os níveis do app (forma: opções, dicas, tempo) com os níveis
de complexidade da trilha: `complexidade`, `mistura` (% de perguntas por
complexidade) e `incentivos` (acerto, erro, convite). A partida sorteia as
perguntas pela `mistura`; se faltar pergunta de uma complexidade, completa com
a mais próxima. Depois de 2 erros seguidos entra um "aquecimento" mais simples;
com 80% de acerto em 2 missões seguidas da unidade, a criança é convidada a
subir de nível (nunca desce sozinha).
