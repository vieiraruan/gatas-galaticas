"""Monta assets/conteudo/ano_N.json (1º ao 5º ano).

Fontes:
- trilhas/trilhas_ef1_bncc.json: estrutura da BNCC (bimestre, disciplina,
  unidade e modelos de missão). Missões sem perguntas aparecem como "em breve".
- galaxia.json (gerado por tool/extrair_galaxia.js a partir da Galáxia do
  Saber): conteúdo completo, usado no 4º bimestre do 4º ano.

Uso: python3 tool/montar_conteudo.py <trilhas_ef1_bncc.json> <galaxia.json> assets/conteudo
"""
import json
import os
import sys

# Planetas das disciplinas da BNCC, no estilo da Galáxia.
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
    "historia": dict(nome="Planeta Memória", nomeCurto="História", emoji="🏛️",
                     cor="#E0802B", corEscura="#B05F17", corClara="#FFF0E0",
                     chefao={"emoji": "🦖", "nome": "Dino do Tempo"}, decoracao=["⏳", "📜", "🏺", "🛰️"]),
    "geografia": dict(nome="Planeta Gaia", nomeCurto="Geografia", emoji="🌎",
                      cor="#2E9E4F", corEscura="#1F7438", corClara="#E6F6EA",
                      chefao={"emoji": "🌋", "nome": "Vulcão Bagunçado"}, decoracao=["🗺️", "🧭", "🌾", "🛰️"]),
}
EMOJI_TIPO = {
    "quiz": "❓", "arrastar_soltar": "🧲", "ligar_pares": "🔗", "ordenar": "🔢",
    "contagem": "🧮", "ditado": "✍️", "leitura": "📖", "gravacao_voz": "🎤",
    "mini_jogo": "🎮", "desenho": "🎨", "desafio_offline": "🏃",
}


def planeta_bncc(ano, bim, disc, nomes):
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
                        "briefing": [],
                        "exercicios": [],
                    }
                    for m in u["missoes"]
                ],
            }
            for u in disc["unidades"]
        ],
    }


def planetas_galaxia(galaxia, ano, bim):
    pre = f"a{ano}b{bim}-"
    out = []
    for p in galaxia["planetas"]:
        p = json.loads(json.dumps(p))
        p["id"] = pre + p["id"]
        for s in p["setores"]:
            s["id"] = pre + s["id"]
            for m in s["missoes"]:
                m["id"] = pre + m["id"]
        out.append(p)
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
                planetas = [planeta_bncc(ano, b["numero"], d, nomes) for d in b["disciplinas"]]
                origem = "BNCC (estrutura)"
            conteudo["bimestres"].append({
                "numero": b["numero"],
                "titulo": f"{b['numero']}º bimestre",
                "origem": origem,
                "planetas": planetas,
            })
        with open(os.path.join(destino, f"ano_{ano}.json"), "w", encoding="utf-8") as f:
            json.dump(conteudo, f, ensure_ascii=False, separators=(",", ":"))
    with open(os.path.join(destino, "niveis.json"), "w", encoding="utf-8") as f:
        json.dump(galaxia["niveis"], f, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main(*sys.argv[1:4])
