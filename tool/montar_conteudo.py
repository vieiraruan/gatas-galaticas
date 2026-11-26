"""Monta assets/conteudo/ano_N.json (1º ao 5º ano).

Fontes:
- trilhas/trilhas_ef1_bncc.json: estrutura da BNCC (bimestre, disciplina,
  unidade e modelos de missão). Missões sem perguntas aparecem como "em breve".
- tool/perguntas/anoN_bB.py: banco de perguntas (briefing + exercícios) por
  id de missão da trilha. Missões que não estão no banco ficam "em breve".
- galaxia.json (gerado por tool/extrair_galaxia.js a partir da Galáxia do
  Saber): conteúdo completo, usado no 4º bimestre do 4º ano.

Uso: python3 tool/montar_conteudo.py <trilhas_ef1_bncc.json> <galaxia.json> assets/conteudo
"""
import importlib.util
import json
import os
import sys

from complexidade import marcar_planetas, niveis_do_app

PERGUNTAS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "perguntas")
sys.path.insert(0, PERGUNTAS)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def banco(ano, bim):
    """Missões escritas em tool/perguntas/anoN_bB.py (id da BNCC -> briefing + exercícios)."""
    caminho = os.path.join(PERGUNTAS, f"ano{ano}_b{bim}.py")
    if not os.path.exists(caminho):
        return {}
    missoes = _modulo(caminho).MISSOES
    for mid, extras in avancadas(ano, bim).items():
        assert mid in missoes, f"pergunta avançada sem missão no banco: {mid}"
        missoes[mid]["exercicios"] = missoes[mid]["exercicios"] + extras
    return missoes


def _modulo(caminho):
    nome = os.path.splitext(os.path.basename(caminho))[0]
    spec = importlib.util.spec_from_file_location(nome, caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def avancadas(ano, bim):
    """Perguntas de níveis 3 e 4 em tool/perguntas/anoN_bB_avancado.py
    (AVANCADAS: id da missão -> lista de exercícios marcados com nivel())."""
    caminho = os.path.join(PERGUNTAS, f"ano{ano}_b{bim}_avancado.py")
    if not os.path.exists(caminho):
        return {}
    extras = _modulo(caminho).AVANCADAS
    for mid, lista in extras.items():
        for e in lista:
            assert e.get("complexidade") in (3, 4), f"{mid}: marque a complexidade com nivel()"
    return extras

# Planetas das disciplinas da escola, os mesmos da Galáxia do Saber.
PLANETAS = {
    "portugues": dict(nome="Planeta Letrônico", nomeCurto="Português", emoji="📚",
                      cor="#1C8FE0", corEscura="#136DB0", corClara="#E3F2FF",
                      chefao={"emoji": "🐀", "nome": "Ratão Embaralha-Letras"}, decoracao=["📚", "✏️", "🔤", "🛰️"]),
    "matematica": dict(nome="Planeta Numerópolis", nomeCurto="Matemática", emoji="🔢",
                       cor="#7C5CFF", corEscura="#5A3FD6", corClara="#EFEBFF",
                       chefao={"emoji": "🤖", "nome": "Robô Calculador"}, decoracao=["➕", "➗", "🛰️", "📐"]),
    "ciencias": dict(nome="Planeta Cosmociência", nomeCurto="Ciências", emoji="🔬",
                     cor="#19B394", corEscura="#0E8A70", corClara="#E3F8F2",
                     chefao={"emoji": "👽", "nome": "Alien Curioso"}, decoracao=["🪐", "⭐", "🌙", "🔭"]),
    "humanas": dict(nome="Planeta Gaia", nomeCurto="Humanas", emoji="🌎",
                    cor="#FF9F1C", corEscura="#D97F00", corClara="#FFF3E0",
                    chefao={"emoji": "☄️", "nome": "Cometa Gigante"}, decoracao=["🌾", "🏭", "📡", "🛰️"]),
    "etica": dict(nome="Nebulosa da Gentileza", nomeCurto="Ética", emoji="💗",
                  cor="#E85D9E", corEscura="#C03C7C", corClara="#FDE8F2",
                  chefao={"emoji": "👾", "nome": "Monstro do Silêncio"}, decoracao=["🌸", "🤝", "💗", "✨"]),
    "ingles": dict(nome="Planeta Big Ben", nomeCurto="Inglês", emoji="🇬🇧",
                   cor="#E5484D", corEscura="#B32D33", corClara="#FFE8E8",
                   chefao={"emoji": "⏰", "nome": "Relógio Maluco"}, decoracao=["🇬🇧", "⏰", "🍳", "🛰️"]),
}
EMOJI_TIPO = {
    "quiz": "❓", "arrastar_soltar": "🧲", "ligar_pares": "🔗", "ordenar": "🔢",
    "contagem": "🧮", "ditado": "✍️", "leitura": "📖", "gravacao_voz": "🎤",
    "mini_jogo": "🎮", "desenho": "🎨", "desafio_offline": "🏃",
}


def planeta_bncc(ano, bim, disc, nomes, perguntas):
    meta = PLANETAS[disc["disciplina_id"]]
    pid = f"a{ano}b{bim}-{disc['disciplina_id']}"
    return {
        "id": pid,
        "disciplina": nomes[disc["disciplina_id"]],
        **meta,
        "setores": [
            {
                "id": u["id"],
                "titulo": u["titulo"],
                "subtitulo": " · ".join(u.get("conteudos", [])[:3]).upper(),
                "habilidadesBncc": u.get("habilidades", []),
                "missoes": [
                    {
                        "id": m["id"],
                        "titulo": m["titulo"],
                        "emoji": EMOJI_TIPO.get(m["tipo"], "🚀"),
                        "descricao": m.get("descricao"),
                        "tipoBncc": m["tipo"],
                        "requerAdulto": m.get("requer_adulto", False),
                        "briefing": perguntas.get(m["id"], {}).get("briefing", []),
                        "exercicios": perguntas.get(m["id"], {}).get("exercicios", []),
                    }
                    for m in u["missoes"]
                ],
            }
            for u in disc["unidades"]
        ],
    }


def planetas_galaxia(galaxia, ano, bim):
    pre = f"a{ano}b{bim}-"
    extras = dict(avancadas(ano, bim))
    out = []
    for p in galaxia["planetas"]:
        p = json.loads(json.dumps(p))
        p["id"] = pre + p["id"]
        for s in p["setores"]:
            s["id"] = pre + s["id"]
            for m in s["missoes"]:
                m["id"] = pre + m["id"]
                m["exercicios"] = m.get("exercicios", []) + extras.pop(m["id"], [])
        out.append(p)
    assert not extras, f"perguntas avançadas sem missão na Galáxia: {sorted(extras)}"
    return out


def main(bncc_path, galaxia_path, destino):
    bncc = json.load(open(bncc_path, encoding="utf-8"))
    galaxia = json.load(open(galaxia_path, encoding="utf-8"))
    nomes = {d["id"]: d["nome"] for d in bncc["disciplinas"]}
    os.makedirs(destino, exist_ok=True)
    rodizio = bncc["regras_trilha"]["rodizio_diario"]
    for serie in bncc["series"]:
        ano = serie["ano"]
        conteudo = {
            "ano": ano,
            "titulo": serie["nome"],
            "rodizioDiario": rodizio,
            "bimestres": [],
        }
        for b in serie["bimestres"]:
            if ano == 4 and b["numero"] == 4:
                planetas = planetas_galaxia(galaxia, ano, 4)
                origem = "Galáxia do Saber"
            else:
                perguntas = banco(ano, b["numero"])
                planetas = [planeta_bncc(ano, b["numero"], d, nomes, perguntas) for d in b["disciplinas"]]
                ids = {m["id"] for p in planetas for s in p["setores"] for m in s["missoes"]}
                sobra = sorted(set(perguntas) - ids)
                assert not sobra, f"ids sem missão na trilha: {sobra}"
                origem = "BNCC + banco de perguntas" if perguntas else "BNCC (estrutura)"
            marcar_planetas(planetas)
            conteudo["bimestres"].append({
                "numero": b["numero"],
                "titulo": f"{b['numero']}º bimestre",
                "origem": origem,
                "planetas": planetas,
            })
        with open(os.path.join(destino, f"ano_{ano}.json"), "w", encoding="utf-8") as f:
            json.dump(conteudo, f, ensure_ascii=False, separators=(",", ":"))
    with open(os.path.join(destino, "niveis.json"), "w", encoding="utf-8") as f:
        json.dump(niveis_do_app(galaxia["niveis"], bncc["niveis_complexidade"]), f, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main(*sys.argv[1:4])
