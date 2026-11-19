"""Gera o conteúdo de EXEMPLO da trilha (assets/curriculo/ano_N.json).

Conteúdo provisório, baseado em habilidades da BNCC, só para o app ter
o que mostrar. Será substituído pelo currículo definitivo.
"""
import json
import os
import sys

# (ano) -> lista de 4 bimestres; cada bimestre: lista de missões
# missão: (componente, titulo, [bncc], [(enunciado, [alternativas], correta)])
P, M, C, H, G = "Língua Portuguesa", "Matemática", "Ciências", "História", "Geografia"

DADOS = {
    1: [
        [
            (P, "As vogais", ["EF01LP05"], [
                ("Qual destas letras é uma vogal?", ["B", "A", "M"], 1),
                ("Com qual vogal começa a palavra OVO?", ["O", "U", "E"], 0),
                ("Qual palavra começa com a letra I?", ["ILHA", "ALHO", "UVA"], 0),
            ]),
            (M, "Contando até 10", ["EF01MA01"], [
                ("Quantas estrelas há aqui? ⭐⭐⭐", ["2", "3", "4"], 1),
                ("Que número vem depois do 5?", ["4", "7", "6"], 2),
                ("Quantos dedos temos em uma mão?", ["5", "10", "4"], 0),
            ]),
        ],
        [
            (P, "Letras e sons", ["EF01LP07"], [
                ("Qual palavra começa com o mesmo som de BOLA?", ["BOTA", "MALA", "SAPO"], 0),
                ("Quantas letras tem a palavra GATO?", ["3", "4", "5"], 1),
                ("Qual destas palavras rima com PÃO?", ["MÃO", "PÉ", "SOL"], 0),
            ]),
            (M, "Juntar e somar", ["EF01MA08"], [
                ("2 + 1 = ?", ["3", "2", "4"], 0),
                ("Tenho 3 balas e ganhei mais 2. Quantas tenho agora?", ["4", "5", "6"], 1),
                ("4 + 4 = ?", ["7", "9", "8"], 2),
            ]),
        ],
        [
            (C, "Meu corpo", ["EF01CI02"], [
                ("Com que parte do corpo nós enxergamos?", ["Olhos", "Orelhas", "Nariz"], 0),
                ("Com que parte do corpo sentimos cheiros?", ["Mãos", "Nariz", "Pés"], 1),
                ("O que devemos fazer antes de comer?", ["Lavar as mãos", "Correr", "Dormir"], 0),
            ]),
            (M, "Tirar e subtrair", ["EF01MA08"], [
                ("5 - 1 = ?", ["3", "4", "6"], 1),
                ("Tinha 6 balões e 2 estouraram. Quantos sobraram?", ["4", "3", "8"], 0),
                ("10 - 5 = ?", ["4", "6", "5"], 2),
            ]),
        ],
        [
            (H, "Eu e minha família", ["EF01HI02"], [
                ("Quem é a mãe da nossa mãe?", ["Tia", "Avó", "Prima"], 1),
                ("Onde a família costuma morar?", ["Na casa", "Na escola", "No parque"], 0),
                ("O filho do nosso tio é nosso...", ["Irmão", "Primo", "Avô"], 1),
            ]),
            (M, "Formas geométricas", ["EF01MA13"], [
                ("Quantos lados tem um triângulo?", ["3", "4", "5"], 0),
                ("Qual forma parece uma bola?", ["Cubo", "Esfera", "Cone"], 1),
                ("Um quadrado tem quantos lados?", ["3", "5", "4"], 2),
            ]),
        ],
    ],
    2: [
        [
            (P, "Sílabas", ["EF02LP02"], [
                ("Quantas sílabas tem a palavra CA-SA?", ["1", "2", "3"], 1),
                ("Qual palavra tem 3 sílabas?", ["SAPATO", "PÉ", "BOLA"], 0),
                ("Qual é a primeira sílaba de MACACO?", ["CO", "MA", "CA"], 1),
            ]),
            (M, "Dezenas e unidades", ["EF02MA01"], [
                ("Quantas dezenas há no número 30?", ["3", "30", "0"], 0),
                ("Qual número tem 4 dezenas e 2 unidades?", ["24", "42", "6"], 1),
                ("Qual número é maior?", ["58", "85", "49"], 1),
            ]),
        ],
        [
            (P, "Ordem alfabética", ["EF02LP05"], [
                ("Qual letra vem depois do C?", ["B", "D", "E"], 1),
                ("Qual palavra vem primeiro no dicionário?", ["UVA", "ABACAXI", "MELÃO"], 1),
                ("Qual letra vem antes do M?", ["L", "N", "O"], 0),
            ]),
            (M, "Adição até 100", ["EF02MA05"], [
                ("23 + 14 = ?", ["37", "36", "47"], 0),
                ("40 + 30 = ?", ["60", "70", "80"], 1),
                ("15 + 15 = ?", ["25", "20", "30"], 2),
            ]),
        ],
        [
            (C, "Animais", ["EF02CI04"], [
                ("Qual animal vive na água?", ["Peixe", "Cachorro", "Galinha"], 0),
                ("Qual animal tem penas?", ["Gato", "Pato", "Vaca"], 1),
                ("O que a vaca come?", ["Capim", "Carne", "Peixe"], 0),
            ]),
            (M, "Subtração até 100", ["EF02MA06"], [
                ("50 - 20 = ?", ["20", "30", "40"], 1),
                ("38 - 15 = ?", ["23", "13", "33"], 0),
                ("Tinha 45 figurinhas e dei 5. Fiquei com...", ["50", "35", "40"], 2),
            ]),
        ],
        [
            (G, "Meu bairro", ["EF02GE01"], [
                ("Onde compramos remédios?", ["Farmácia", "Padaria", "Escola"], 0),
                ("Onde as crianças estudam?", ["Hospital", "Escola", "Mercado"], 1),
                ("Qual destes é um meio de transporte?", ["Ônibus", "Árvore", "Casa"], 0),
            ]),
            (M, "Medidas de tempo", ["EF02MA18"], [
                ("Quantos dias tem uma semana?", ["5", "7", "10"], 1),
                ("Qual dia vem depois de segunda-feira?", ["Domingo", "Quarta-feira", "Terça-feira"], 2),
                ("Quantos meses tem um ano?", ["12", "10", "7"], 0),
            ]),
        ],
    ],
    3: [
        [
            (P, "Substantivos", ["EF03LP08"], [
                ("Qual destas palavras é um nome de objeto?", ["Correr", "Mesa", "Bonito"], 1),
                ("Qual é um nome próprio?", ["cidade", "Brasil", "menino"], 1),
                ("O plural de FLOR é...", ["Flores", "Flors", "Floris"], 0),
            ]),
            (M, "Tabuada do 2 e do 3", ["EF03MA07"], [
                ("2 × 4 = ?", ["6", "8", "10"], 1),
                ("3 × 5 = ?", ["15", "12", "18"], 0),
                ("Cada bicicleta tem 2 rodas. Quantas rodas têm 6 bicicletas?", ["8", "10", "12"], 2),
            ]),
        ],
        [
            (P, "Adjetivos", ["EF03LP08"], [
                ("Na frase 'O gato preto dorme', qual palavra é o adjetivo?", ["gato", "preto", "dorme"], 1),
                ("Qual palavra descreve como algo é?", ["Alegre", "Pular", "Escola"], 0),
                ("O contrário de ALTO é...", ["Grande", "Baixo", "Largo"], 1),
            ]),
            (M, "Tabuada do 4 e do 5", ["EF03MA07"], [
                ("4 × 3 = ?", ["12", "7", "16"], 0),
                ("5 × 6 = ?", ["25", "35", "30"], 2),
                ("Uma mão tem 5 dedos. Quantos dedos há em 4 mãos?", ["20", "9", "25"], 0),
            ]),
        ],
        [
            (C, "Os seres vivos e o ambiente", ["EF03CI04"], [
                ("Do que as plantas precisam para viver?", ["Água e luz", "Só areia", "Plástico"], 0),
                ("Qual destes é um ser vivo?", ["Pedra", "Árvore", "Cadeira"], 1),
                ("Os animais que comem só plantas são chamados de...", ["Carnívoros", "Herbívoros", "Onívoros"], 1),
            ]),
            (M, "Divisão em partes iguais", ["EF03MA08"], [
                ("12 balas divididas entre 3 crianças. Cada uma fica com...", ["3", "4", "6"], 1),
                ("10 ÷ 2 = ?", ["5", "8", "4"], 0),
                ("A metade de 8 é...", ["2", "6", "4"], 2),
            ]),
        ],
        [
            (H, "A cidade e o campo", ["EF03HI03"], [
                ("Onde ficam as grandes plantações?", ["No campo", "No shopping", "Na praia"], 0),
                ("Qual atividade é mais comum na cidade?", ["Comércio", "Colheita de café", "Criação de gado"], 0),
                ("O alimento que comemos na cidade geralmente vem...", ["Do campo", "Da escola", "Do cinema"], 0),
            ]),
            (M, "Dinheiro", ["EF03MA24"], [
                ("Quanto é uma nota de 10 reais mais uma de 5 reais?", ["R$ 15", "R$ 12", "R$ 20"], 0),
                ("Um lanche custa R$ 7. Paguei com R$ 10. Qual é o troco?", ["R$ 2", "R$ 3", "R$ 4"], 1),
                ("Quantas moedas de R$ 1 formam R$ 5?", ["10", "2", "5"], 2),
            ]),
        ],
    ],
    4: [
        [
            (P, "Pontuação", ["EF04LP05"], [
                ("Que sinal usamos no final de uma pergunta?", ["!", "?", "."], 1),
                ("Que sinal mostra surpresa ou espanto?", ["!", ",", "?"], 0),
                ("Qual frase está pontuada corretamente?", ["Que dia lindo!", "Que dia lindo,", "Que dia, lindo"], 0),
            ]),
            (M, "Números até 10.000", ["EF04MA01"], [
                ("Como se escreve 'dois mil e quinze'?", ["2015", "2150", "20015"], 0),
                ("Qual é o valor do algarismo 7 em 3.742?", ["7", "70", "700"], 2),
                ("Qual número é maior?", ["4.099", "4.910", "4.190"], 1),
            ]),
        ],
        [
            (P, "Verbos", ["EF04LP07"], [
                ("Qual palavra é um verbo?", ["Correr", "Casa", "Feliz"], 0),
                ("Em 'Ontem eu brinquei', o verbo está no...", ["Presente", "Passado", "Futuro"], 1),
                ("Qual frase está no futuro?", ["Eu estudei", "Eu estudo", "Eu vou estudar"], 2),
            ]),
            (M, "Multiplicação", ["EF04MA06"], [
                ("12 × 3 = ?", ["36", "33", "15"], 0),
                ("25 × 4 = ?", ["90", "100", "125"], 1),
                ("Uma caixa tem 6 ovos. Quantos ovos há em 7 caixas?", ["13", "48", "42"], 2),
            ]),
        ],
        [
            (C, "Cadeias alimentares", ["EF04CI04"], [
                ("Quem produz o próprio alimento?", ["Plantas", "Leões", "Pessoas"], 0),
                ("Na cadeia capim → gafanhoto → sapo, quem come o gafanhoto?", ["Capim", "Sapo", "Ninguém"], 1),
                ("Fungos e bactérias que desfazem restos de seres vivos são...", ["Produtores", "Decompositores", "Predadores"], 1),
            ]),
            (M, "Frações", ["EF04MA09"], [
                ("Uma pizza dividida em 4 partes. Comi 1. Que fração comi?", ["1/4", "1/2", "4/1"], 0),
                ("Qual fração representa a metade?", ["1/3", "1/2", "2/3"], 1),
                ("Quanto é 1/2 de 20?", ["5", "15", "10"], 2),
            ]),
        ],
        [
            (G, "Regiões do Brasil", ["EF04GE11"], [
                ("Quantas regiões tem o Brasil?", ["4", "5", "6"], 1),
                ("Em qual região fica a maior parte da Floresta Amazônica?", ["Norte", "Sul", "Sudeste"], 0),
                ("Qual é a capital do Brasil?", ["Rio de Janeiro", "São Paulo", "Brasília"], 2),
            ]),
            (M, "Medidas de comprimento", ["EF04MA20"], [
                ("Quantos centímetros tem 1 metro?", ["10", "100", "1000"], 1),
                ("Quantos metros tem 1 quilômetro?", ["1000", "100", "10"], 0),
                ("Qual medida é mais adequada para a altura de uma porta?", ["Quilômetros", "Metros", "Milímetros"], 1),
            ]),
        ],
    ],
    5: [
        [
            (P, "Sinônimos e antônimos", ["EF05LP08"], [
                ("Qual é um sinônimo de CONTENTE?", ["Triste", "Alegre", "Bravo"], 1),
                ("Qual é o antônimo de RÁPIDO?", ["Lento", "Veloz", "Ligeiro"], 0),
                ("BONITO e BELO são palavras...", ["Antônimas", "Sinônimas", "Iguais na escrita"], 1),
            ]),
            (M, "Números decimais", ["EF05MA02"], [
                ("Como se lê 0,5?", ["Cinco décimos", "Cinco centésimos", "Cinquenta"], 0),
                ("Qual número é maior?", ["0,3", "0,25", "0,29"], 0),
                ("2,5 + 1,5 = ?", ["3,5", "4", "4,5"], 1),
            ]),
        ],
        [
            (P, "Tipos de texto", ["EF05LP15"], [
                ("Um texto que ensina a preparar um bolo é uma...", ["Receita", "Poesia", "Notícia"], 0),
                ("Um texto com versos e rimas geralmente é um...", ["Bilhete", "Poema", "Anúncio"], 1),
                ("Um texto que informa um fato recente é uma...", ["Fábula", "Notícia", "Lenda"], 1),
            ]),
            (M, "Porcentagem", ["EF05MA06"], [
                ("50% de 100 é...", ["25", "50", "75"], 1),
                ("25% é o mesmo que...", ["1/4", "1/2", "1/3"], 0),
                ("10% de 200 é...", ["2", "10", "20"], 2),
            ]),
        ],
        [
            (C, "Sistema solar", ["EF05CI11"], [
                ("Qual é a estrela do nosso sistema solar?", ["Lua", "Sol", "Marte"], 1),
                ("Qual planeta nós habitamos?", ["Terra", "Vênus", "Júpiter"], 0),
                ("O movimento da Terra em torno de si mesma causa...", ["As estações", "O dia e a noite", "As marés"], 1),
            ]),
            (M, "Área e perímetro", ["EF05MA19"], [
                ("Qual é o perímetro de um quadrado de lado 3 cm?", ["9 cm", "12 cm", "6 cm"], 1),
                ("Qual é a área de um retângulo de 4 cm por 2 cm?", ["8 cm²", "6 cm²", "12 cm²"], 0),
                ("Perímetro é a medida...", ["Do contorno", "Da superfície", "Do peso"], 0),
            ]),
        ],
        [
            (H, "Cidadania", ["EF05HI04"], [
                ("Votar para escolher governantes é um direito do...", ["Cidadão", "Turista", "Animal"], 0),
                ("Qual documento reúne as leis mais importantes do Brasil?", ["Dicionário", "Constituição", "Jornal"], 1),
                ("Respeitar as diferenças entre as pessoas é...", ["Opcional", "Proibido", "Um dever de todos"], 2),
            ]),
            (M, "Probabilidade", ["EF05MA22"], [
                ("Ao jogar uma moeda, quais resultados são possíveis?", ["Cara ou coroa", "Só cara", "1 a 6"], 0),
                ("Num dado comum, qual número NÃO pode sair?", ["1", "6", "7"], 2),
                ("Numa caixa com 9 bolas azuis e 1 vermelha, qual cor é mais provável sair?", ["Vermelha", "Azul", "Tanto faz"], 1),
            ]),
        ],
    ],
}


def main(destino):
    os.makedirs(destino, exist_ok=True)
    siglas = {P: "lp", M: "ma", C: "ci", H: "hi", G: "ge"}
    for ano, bimestres in DADOS.items():
        trilha = {
            "ano": ano,
            "titulo": f"{ano}º ano",
            "bimestres": [],
        }
        for nb, missoes in enumerate(bimestres, start=1):
            bimestre = {"numero": nb, "titulo": f"{nb}º bimestre", "missoes": []}
            for nm, (comp, titulo, bncc, questoes) in enumerate(missoes, start=1):
                for q in questoes:
                    assert 0 <= q[2] < len(q[1]), (ano, titulo, q)
                bimestre["missoes"].append({
                    "id": f"a{ano}-b{nb}-m{nm}-{siglas[comp]}",
                    "titulo": titulo,
                    "componente": comp,
                    "habilidadesBncc": bncc,
                    "questoes": [
                        {"enunciado": e, "alternativas": alts, "correta": c}
                        for e, alts, c in questoes
                    ],
                })
            trilha["bimestres"].append(bimestre)
        with open(os.path.join(destino, f"ano_{ano}.json"), "w", encoding="utf-8") as f:
            json.dump(trilha, f, ensure_ascii=False, indent=2)
            f.write("\n")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "assets/curriculo")
