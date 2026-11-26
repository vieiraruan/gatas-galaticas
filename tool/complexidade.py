"""Complexidade cognitiva (1 a 4) e medalha de cada exercício.

Níveis da trilha 2.1.0 (niveis_complexidade):
1 reconhecer, 2 compreender, 3 aplicar, 4 analisar e criar.

Um exercício pode trazer "complexidade" e "medalha" escritos no banco
(helper `nivel()` em tool/perguntas/base.py). Quando não traz, estimamos
pelo tipo e pelo texto da pergunta. Exercícios "de desafio" da Galáxia
contam como nível 3.
"""
import re

_DETETIVE = ("erro", "errad", "corrij", "corrige", "precisa mudar", "revisor")
_EXPLICADOR = ("por que", "por quê", "explique", "justifique")
_CONTEXTO = ("r$", "comprou", "pagou", "troco", "cada", "receita", "você tem", "quanto custa",
             "quantos", "quantas", "km", "metros", " m ", "horas", "minutos", "kg", "litros",
             "pessoas", "dobro", "triplo", "metade", "sobra", "ficou com", "dividid")


def _texto(e):
    q = e.get("pergunta", "")
    q = re.sub(r"\[\[[^\]]*\]\]", " ", q)
    return q.replace("**", "").lower()


def estimar(e):
    """Devolve (complexidade, medalha) estimadas para um exercício."""
    q = _texto(e)
    tipo = e.get("tipo")
    numeros = len(re.findall(r"\d+(?:[.,]\d+)?", q))
    if any(k in q for k in _DETETIVE):
        return 4, "detetive"
    if any(k in q for k in _EXPLICADOR):
        return 2, "explicador"
    if tipo == "escolha" and numeros >= 2 and any(k in q for k in _CONTEXTO):
        return 3, None
    if tipo == "escolha" and len(q) > 110:
        return 3, None
    if tipo in ("separar", "ligar", "ordenar"):
        return 2, None
    return 1, None


def marcar(exercicios, padrao=None):
    for e in exercicios:
        c, medalha = estimar(e)
        if padrao is not None:
            c = max(c, padrao)
        e.setdefault("complexidade", c)
        if medalha and "medalha" not in e:
            e["medalha"] = medalha


def marcar_planetas(planetas):
    for p in planetas:
        for s in p["setores"]:
            for m in s["missoes"]:
                marcar(m.get("exercicios", []))
                marcar(m.get("exerciciosDesafio", []), padrao=3)


def niveis_do_app(niveis_galaxia, niveis_complexidade):
    """Junta os níveis do app (forma) com os níveis de complexidade da trilha."""
    por_app = {n["nivel_app"]: n for n in niveis_complexidade}
    out = []
    for n in niveis_galaxia:
        n = dict(n)
        c = por_app.get(n["id"])
        if c:
            n["complexidade"] = c["nivel"]
            n["nomeComplexidade"] = c["nome"]
            n["mistura"] = {k: v for k, v in c["mistura_por_nivel"].items()}
            n["incentivos"] = c["incentivos"]
        out.append(n)
    return out
