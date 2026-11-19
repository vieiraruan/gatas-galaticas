# Formato do conteúdo da trilha

Cada ano escolar tem um arquivo `assets/curriculo/ano_N.json` (N de 1 a 5).
O conteúdo atual é **de exemplo**, gerado por `tool/gerar_curriculo.py`, e será
substituído pelo currículo definitivo.

```json
{
  "ano": 3,
  "titulo": "3º ano",
  "bimestres": [
    {
      "numero": 1,
      "titulo": "1º bimestre",
      "missoes": [
        {
          "id": "a3-b1-m1-lp",
          "titulo": "Substantivos",
          "componente": "Língua Portuguesa",
          "habilidadesBncc": ["EF03LP08"],
          "questoes": [
            {
              "enunciado": "Qual destas palavras é um nome de objeto?",
              "alternativas": ["Correr", "Mesa", "Bonito"],
              "correta": 1,
              "explicacao": "Opcional: aparece depois que a criança responde."
            }
          ]
        }
      ]
    }
  ]
}
```

Regras:
- `id` da missão precisa ser único e **não deve mudar** depois de publicado (o progresso da criança é salvo por ele).
- `componente`: um de `Língua Portuguesa`, `Matemática`, `Ciências`, `História`, `Geografia` (definem a cor na tela; outros valores ficam cinza).
- `correta` é o índice (começando em 0) da alternativa certa.
- As missões de um bimestre são feitas em ordem; a criança libera 1 missão nova por dia.
