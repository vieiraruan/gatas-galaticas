"""Atalhos para escrever missões (mesmo espírito da Galáxia do Saber).

Marcação de texto: **negrito**, \\n, [[3/4]] e {nome}.
Em `mc` e `fill` a PRIMEIRA opção é a certa (o app embaralha).
"""


def mc(pergunta, opcoes, explicacao=None, emoji=None, dica=None):
    e = {"tipo": "escolha", "pergunta": pergunta, "opcoes": opcoes, "correta": 0, "embaralhar": True}
    if emoji:
        e["visuais"] = [{"tipo": "emoji", "texto": emoji, "tamanho": 56}]
    if dica:
        e["dica"] = dica
    if explicacao:
        e["explicacao"] = explicacao
    return e


def tf(pergunta, resposta, explicacao=None):
    return {"tipo": "verdadeiroFalso", "pergunta": pergunta, "resposta": resposta, "explicacao": explicacao}


def fill(frase, opcoes, explicacao=None):
    assert "___" in frase, frase
    return {"tipo": "completar", "pergunta": frase, "opcoes": opcoes, "explicacao": explicacao}


def ordem(pergunta, itens, explicacao=None):
    return {"tipo": "ordenar", "pergunta": pergunta, "itens": itens, "explicacao": explicacao}


def ligar(pares, pergunta="Toque nos pares que combinam"):
    return {"tipo": "ligar", "pergunta": pergunta, "pares": [list(p) for p in pares]}


def separar(pergunta, grupos, itens, explicacao=None):
    """itens: lista de (texto, índice do grupo)."""
    return {"tipo": "separar", "pergunta": pergunta, "grupos": grupos,
            "itens": [{"texto": t, "grupo": g} for t, g in itens], "explicacao": explicacao}


def missao(briefing, exercicios):
    """briefing: lista de (emoji, texto)."""
    return {"briefing": [{"emoji": e, "texto": t} for e, t in briefing], "exercicios": exercicios}


def desafio(texto):
    """Cartão final para missões que pedem uma atividade fora da tela."""
    return ("🏡", "**Desafio com um adulto:** " + texto)


def nivel(n, exercicio, medalha=None):
    """Marca a complexidade (1 reconhecer, 2 compreender, 3 aplicar, 4 analisar
    e criar) e, se houver, a medalha (detetive, explicador, inventor)."""
    exercicio["complexidade"] = n
    if medalha:
        exercicio["medalha"] = medalha
    return exercicio
