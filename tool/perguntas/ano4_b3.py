"""4º ano · 3º bimestre."""
from base import desafio, fill, ligar, mc, missao, ordem, separar, tf

MISSOES = {
    # ------------------------------------------------------------ Português
    "a4-b3-portugues-u1-m1": missao(
        [
            ("🤝", "**Concordância**: as palavras combinam entre si em **número** (singular/plural) e **gênero** (masculino/feminino)."),
            ("📝", "**O gato preto dorme.** → **Os gatos pretos dormem.**"),
            ("👀", "O verbo concorda com quem faz a ação: **Eu corro, nós corremos, eles correm.**"),
        ],
        [
            mc("Qual frase está **certa**?", ["As meninas chegaram cedo.", "As menina chegou cedo.", "As meninas chegou cedo."], "**meninas** (plural) → **chegaram**.", "👧"),
            mc("Qual frase está **certa**?", ["Os livros novos estão na mesa.", "Os livro novo está na mesa.", "Os livros novo estão na mesa."], "Tudo no **plural**.", "📚"),
            fill("Nós ___ futebol no recreio.", ["jogamos", "joga", "jogam"], "**Nós** → **jogamos**."),
            fill("A blusa está muito ___.", ["bonita", "bonito", "bonitas"], "**blusa** é feminino singular."),
            fill("Os cachorros ___ alto.", ["latiram", "latiu", "latimos"], "**cachorros** (plural) → **latiram**."),
            mc("Passe para o plural: **O pássaro amarelo canta.**", ["Os pássaros amarelos cantam.", "Os pássaros amarelo canta.", "O pássaros amarelos cantam."], "Artigo, nome, adjetivo e verbo no plural.", "🐦"),
            tf("Na frase **As flores vermelhas murchou**, a concordância está correta.", False, "O certo é **murcharam**."),
        ],
    ),
    "a4-b3-portugues-u1-m2": missao(
        [
            ("🏭", "**Sufixo** é um pedacinho colocado no **fim** da palavra que forma uma palavra nova."),
            ("🔧", "**-eiro** indica profissão ou lugar: pão → **padeiro**, leite → **leiteiro**."),
            ("🐣", "**-inho/-zinho** diminui: casa → **casinha**. **-ão** aumenta: casa → **casarão**. **-mente** forma advérbios: rápido → **rapidamente**."),
        ],
        [
            mc("Quem trabalha com **pão** é o...", ["padeiro", "paneiro", "pãozinho"], "pão + **-eiro**.", "🥖"),
            mc("Quem conserta **sapatos** é o...", ["sapateiro", "sapatão", "sapatinho"], "sapato + **-eiro**.", "👞"),
            mc("O diminutivo de **pé** é...", ["pezinho", "pezão", "pedeiro"], "**-zinho** indica tamanho pequeno.", "🦶"),
            mc("Qual palavra indica algo **grande**?", ["narigão", "narizinho", "nariguinho"], "**-ão** é aumentativo.", "👃"),
            fill("Ele correu muito ___ (de rápido).", ["rapidamente", "rapidão", "rapideiro"], "rápido + **-mente**."),
            ligar([("jardim", "jardineiro"), ("leite", "leiteiro"), ("carta", "carteiro"), ("livro", "livraria")], "Ligue a palavra à palavra derivada"),
            tf("Em **felizmente**, o sufixo é **-mente**.", True, "feliz + **-mente**."),
        ],
    ),
    "a4-b3-portugues-u1-m3": missao(
        [
            ("🔁", "**Pronomes** substituem nomes para o texto não ficar repetitivo."),
            ("👤", "**Ana** chegou. **Ela** trouxe bolo. **Os meninos** jogaram. **Eles** venceram."),
            ("🎯", "Também usamos **o, a, os, as**: Vi **o filme** → Eu **o** vi. Encontrei **Maria** → Encontrei-**a**."),
        ],
        [
            mc("**Pedro** foi à escola. ___ levou a mochila.", ["Ele", "Ela", "Eles"], "**Pedro** → **ele**.", "🎒"),
            mc("**As meninas** dançaram. ___ estavam felizes.", ["Elas", "Ela", "Eles"], "Feminino plural → **elas**.", "💃"),
            mc("**Eu e meu irmão** fomos ao cinema. Troque por pronome:", ["Nós", "Eles", "Vocês"], "Eu + outra pessoa = **nós**.", "🎬"),
            fill("Comprei um livro e já ___ li todo.", ["o", "a", "os"], "**livro** (masculino singular) → **o**."),
            mc("Qual texto evita a repetição?", ["Lia tem uma gata. Ela adora a gata e cuida dela.", "Lia tem uma gata. Lia adora a gata e Lia cuida da gata.", "Lia tem uma gata. Lia Lia gata."], "O pronome **ela** substitui **Lia**.", "🐈"),
            ligar([("o menino", "ele"), ("a professora", "ela"), ("os avós", "eles"), ("as tias", "elas")], "Ligue o nome ao pronome"),
            tf("Na frase **Vi a lua e achei-a linda**, o **a** substitui **lua**.", True, "achei **a lua** linda."),
        ],
    ),
    # ------------------------------------------------------------ Matemática
    "a4-b3-matematica-u1-m1": missao(
        [
            ("🍕", "Uma **fração** mostra partes de um inteiro dividido em partes **iguais**."),
            ("🔢", "Em [[3/8]], o **8** (denominador) diz em quantas partes dividimos; o **3** (numerador), quantas pegamos."),
            ("🥇", "[[1/2]] = metade, [[1/4]] = um quarto, [[1/10]] = um décimo, [[1/100]] = um centésimo."),
        ],
        [
            mc("Uma pizza em **8** fatias. Você comeu **3**. Que fração comeu?", ["[[3/8]]", "[[8/3]]", "[[3/5]]"], "3 de 8 partes.", "🍕"),
            mc("Qual fração é **maior**?", ["[[1/2]]", "[[1/4]]", "[[1/8]]"], "Quanto menos partes, maior cada pedaço.", "⚖️"),
            mc("Metade de **20** balas é...", ["10", "5", "2"], "20 ÷ 2 = **10**.", "🍬"),
            mc("[[1/4]] de **12** é...", ["3", "4", "6"], "12 ÷ 4 = **3**.", "🧮"),
            mc("Qual fração é **igual** a [[1/2]]?", ["[[2/4]]", "[[1/3]]", "[[2/3]]"], "2 de 4 é metade.", "🟦"),
            ordem("Coloque da **menor** para a **maior**:", ["[[1/10]]", "[[1/5]]", "[[1/3]]", "[[1/2]]"], "Com numerador 1, maior denominador = menor parte."),
            tf("[[1/10]] lê-se **um décimo**.", True, "Décimo = uma de 10 partes."),
        ],
    ),
    "a4-b3-matematica-u1-m2": missao(
        [
            ("🪙", "**1 real = 100 centavos.** Por isso, 1 centavo é [[1/100]] do real."),
            ("🔟", "**0,1** = um décimo (10 centavos). **0,01** = um centésimo (1 centavo)."),
            ("💵", "**R$ 2,50** = 2 reais e 50 centavos = 2 inteiros e 50 centésimos."),
        ],
        [
            mc("**50 centavos** é que parte de 1 real?", ["metade", "um quarto", "um décimo"], "50 de 100 = **metade**.", "🪙"),
            mc("**R$ 0,25** são...", ["25 centavos", "25 reais", "2 reais e 5 centavos"], "0,25 = 25 centésimos.", "💰"),
            mc("Como se escreve **3 reais e 5 centavos**?", ["R$ 3,05", "R$ 3,5", "R$ 35,00"], "5 centavos = **0,05**.", "✍️"),
            mc("Qual valor é **maior**?", ["R$ 1,50", "R$ 1,05", "R$ 0,99"], "1,50 > 1,05 > 0,99.", "⚖️"),
            {"tipo": "escolha", "pergunta": "Quanto há aqui?", "opcoes": ["R$ 1,75", "R$ 1,57", "R$ 2,75"], "correta": 0, "embaralhar": True,
             "visuais": [{"tipo": "dinheiro", "valores": [100, 50, 25]}], "explicacao": "1 real + 50 + 25 centavos = **R$ 1,75**."},
            ligar([("0,5", "cinco décimos"), ("0,05", "cinco centésimos"), ("0,1", "um décimo"), ("0,01", "um centésimo")], "Ligue o número ao nome"),
            tf("**0,5** e **0,50** valem a mesma coisa.", True, "5 décimos = 50 centésimos."),
        ],
    ),
    "a4-b3-matematica-u1-m3": missao(
        [
            ("🛒", "Bem-vindo ao **Mercadinho** da nave! Some os preços e calcule o troco."),
            ("➕", "Para somar preços, alinhe a **vírgula**: R$ 2,50 + R$ 1,25 = **R$ 3,75**."),
            ("💸", "Troco = dinheiro dado − valor da compra."),
        ],
        [
            mc("Suco **R$ 2,50** + pão **R$ 1,25**. Total?", ["R$ 3,75", "R$ 3,25", "R$ 4,75"], "2,50 + 1,25 = **3,75**.", "🧃"),
            mc("Comprou algo de **R$ 7,50** e pagou com **R$ 10**. Troco?", ["R$ 2,50", "R$ 3,50", "R$ 2,00"], "10 − 7,50 = **2,50**.", "💵"),
            mc("**3** chicletes de **R$ 0,50**. Quanto custa?", ["R$ 1,50", "R$ 1,00", "R$ 3,50"], "3 × 0,50 = **1,50**.", "🍬"),
            mc("Você tem **R$ 5,00**. Qual destes dá para comprar?", ["Bolo de R$ 4,80", "Pizza de R$ 12,00", "Livro de R$ 6,50"], "4,80 é menor que 5,00.", "🎂"),
            {"tipo": "escolha", "pergunta": "Uma bala custa **R$ 0,75**. Este dinheiro dá para comprar quantas?", "opcoes": ["2", "1", "3"], "correta": 0, "embaralhar": True,
             "visuais": [{"tipo": "dinheiro", "valores": [100, 50]}], "explicacao": "Temos **R$ 1,50** = 0,75 + 0,75 → **2** balas."},
            mc("Maçã a **R$ 1,20** cada. Quanto custam **5**?", ["R$ 6,00", "R$ 5,20", "R$ 6,20"], "5 × 1,20 = **6,00**.", "🍎"),
            tf("**R$ 2,00** é o dobro de **R$ 1,00**.", True, "2 × 1 = 2."),
        ],
    ),
    "a4-b3-matematica-u2-m1": missao(
        [
            ("🌾", "**Perímetro** é a medida do **contorno** de uma figura."),
            ("📏", "Para calcular, **some todos os lados**."),
            ("🟩", "Um terreno retangular de 10 m por 5 m tem perímetro 10 + 5 + 10 + 5 = **30 m**."),
        ],
        [
            mc("Um quadrado tem lado de **4 m**. Qual o perímetro?", ["16 m", "8 m", "12 m"], "4 + 4 + 4 + 4 = **16 m**.", "🟥"),
            mc("Retângulo de **6 m** por **3 m**. Perímetro?", ["18 m", "9 m", "12 m"], "6 + 3 + 6 + 3 = **18 m**.", "🟦"),
            mc("Triângulo com lados de **5**, **5** e **4 cm**. Perímetro?", ["14 cm", "10 cm", "20 cm"], "5 + 5 + 4 = **14 cm**.", "🔺"),
            mc("Para cercar o sítio, preciso saber o...", ["perímetro", "peso", "volume"], "A cerca vai no **contorno**.", "🚧"),
            mc("Um quadrado tem perímetro **20 cm**. Quanto mede cada lado?", ["5 cm", "4 cm", "10 cm"], "20 ÷ 4 = **5 cm**.", "🔲"),
            fill("Perímetro é a soma de todos os ___ da figura.", ["lados", "cantos", "pontos"], "Some os **lados**."),
            tf("Um retângulo de 8 m por 2 m tem perímetro de 20 m.", True, "8 + 2 + 8 + 2 = 20."),
        ],
    ),
    "a4-b3-matematica-u2-m2": missao(
        [
            ("⬛", "**Área** é o tamanho da **superfície** de uma figura."),
            ("🔲", "Podemos medir a área **contando quadradinhos**."),
            ("✖️", "Num retângulo, basta multiplicar: 4 quadradinhos × 3 fileiras = **12 quadradinhos**."),
        ],
        [
            mc("Um retângulo com **5** quadradinhos em cada fileira e **2** fileiras tem área de...", ["10 quadradinhos", "7 quadradinhos", "14 quadradinhos"], "5 × 2 = **10**.", "🟩"),
            mc("Um quadrado de **3** por **3** quadradinhos tem área de...", ["9", "6", "12"], "3 × 3 = **9**.", "🟨"),
            mc("Para saber quanto piso colocar no chão, preciso da...", ["área", "temperatura", "perímetro"], "O piso cobre a **superfície**.", "🏠"),
            mc("Figura A tem área **12**, figura B tem área **8**. Qual é maior?", ["A", "B", "São iguais"], "12 > 8.", "⚖️"),
            mc("Um tapete de **4 m** por **2 m** tem área de...", ["8 m²", "6 m²", "12 m²"], "4 × 2 = **8 metros quadrados**.", "🧶"),
            separar("Área ou perímetro?", ["Área", "Perímetro"],
                    [("piso da sala", 0), ("grama do campo", 0), ("pintar a parede", 0), ("cerca do quintal", 1), ("rodapé da sala", 1), ("fita na borda do quadro", 1)],
                    "Superfície = área; contorno = perímetro."),
            tf("Duas figuras diferentes podem ter a mesma área.", True, "Um 4×3 e um 6×2 têm área 12."),
        ],
    ),
    "a4-b3-matematica-u2-m3": missao(
        [
            ("🌡️", "O **termômetro** mede a **temperatura** em **graus Celsius (°C)**."),
            ("🧊", "A água congela a **0 °C** e ferve a **100 °C**. Nosso corpo fica perto de **36,5 °C**."),
            ("⏰", "Também medimos o **tempo**: 1 hora = **60 minutos**, 1 minuto = **60 segundos**, 1 dia = **24 horas**."),
        ],
        [
            mc("A água **congela** a...", ["0 °C", "100 °C", "36 °C"], "Abaixo de 0 °C vira gelo.", "🧊"),
            mc("Qual temperatura indica **febre**?", ["38,5 °C", "36,5 °C", "20 °C"], "Acima de 37,5 °C é febre.", "🤒"),
            mc("De manhã fazia **18 °C** e à tarde **25 °C**. Quanto esquentou?", ["7 °C", "43 °C", "5 °C"], "25 − 18 = **7**.", "☀️"),
            mc("**1 hora e meia** tem quantos minutos?", ["90", "60", "130"], "60 + 30 = **90**.", "⏰"),
            mc("O filme começou às **14h** e durou **2 horas**. Terminou às...", ["16h", "12h", "15h"], "14 + 2 = **16h**.", "🎬"),
            ordem("Do mais **frio** para o mais **quente**:", ["−5 °C", "0 °C", "15 °C", "30 °C"], "Números negativos ficam abaixo do zero."),
            tf("Um dia tem 24 horas.", True, "A Terra dá uma volta em si mesma."),
        ],
    ),
    # ------------------------------------------------------------ Ciências
    "a4-b3-ciencias-u1-m1": missao(
        [
            ("🔬", "**Microrganismos** são seres vivos tão pequenos que só vemos com **microscópio**: bactérias, fungos e vírus."),
            ("😇", "Muitos são **amigos**: ajudam na digestão, decompõem restos e fazem iogurte e pão."),
            ("😈", "Alguns causam **doenças**, como gripe, cárie e diarreia."),
        ],
        [
            mc("Para ver bactérias, usamos o...", ["microscópio", "telescópio", "binóculo"], "Ele aumenta coisas muito pequenas.", "🔬"),
            mc("Qual destes é um microrganismo?", ["bactéria", "formiga", "minhoca"], "Formiga e minhoca vemos a olho nu.", "🦠"),
            mc("Qual doença é causada por **vírus**?", ["gripe", "fratura", "queimadura de sol"], "O vírus da gripe passa pelo ar.", "🤧"),
            mc("As bactérias da **boca** que comem açúcar podem causar...", ["cárie", "sarampo", "catapora"], "Por isso escovamos os dentes!", "🦷"),
            separar("Amigo ou vilão?", ["Amigo", "Vilão"],
                    [("bactéria do iogurte", 0), ("fermento do pão", 0), ("decompositor do solo", 0), ("vírus da gripe", 1), ("bactéria da cárie", 1), ("fungo da micose", 1)],
                    "Uns ajudam, outros causam doenças."),
            tf("Todos os microrganismos fazem mal à saúde.", False, "Muitos são úteis!"),
            tf("Existem bactérias no nosso intestino que ajudam na digestão.", True, "São a **flora intestinal**."),
        ],
    ),
    "a4-b3-ciencias-u1-m2": missao(
        [
            ("🍞", "O **fermento** biológico tem fungos minúsculos (leveduras) que soltam gás e fazem a massa do pão **crescer**."),
            ("🥛", "Bactérias transformam o leite em **iogurte** e **queijo**."),
            ("🍂", "Fungos e bactérias **decompõem** restos de plantas e animais e devolvem nutrientes ao solo."),
        ],
        [
            mc("O que faz a massa do pão crescer?", ["O fermento (leveduras)", "O sal", "O forno frio"], "As leveduras soltam **gás**.", "🍞"),
            mc("O iogurte é feito do leite com ajuda de...", ["bactérias", "vírus", "minhocas"], "Bactérias do bem!", "🥛"),
            mc("O **bolor** verde no pão velho é um...", ["fungo", "vírus", "inseto"], "É o fungo **mofo**.", "🦠"),
            mc("Por que a fruta estraga mais rápido fora da geladeira?", ["O calor ajuda os microrganismos a crescer", "O frio estraga a fruta", "A luz da geladeira"], "O frio deixa os micróbios lentos.", "🍌"),
            ligar([("pão", "fermento"), ("iogurte", "bactérias do leite"), ("adubo", "decompositores"), ("queijo", "coalho e bactérias")], "Ligue o produto ao microrganismo"),
            mc("Os **decompositores** são importantes porque...", ["devolvem nutrientes ao solo", "causam todas as doenças", "fazem fotossíntese"], "Eles **reciclam** a natureza.", "🍄"),
            tf("Alguns remédios, como a penicilina, vieram de um fungo.", True, "Descoberta de Alexander Fleming."),
        ],
    ),
    "a4-b3-ciencias-u1-m3": missao(
        [
            ("🧼", "**Lavar as mãos** com água e sabão é a melhor proteção contra muitos micróbios."),
            ("💉", "As **vacinas** treinam o corpo para se defender de doenças."),
            ("🍽️", "Lavar frutas e verduras, ferver ou filtrar a água e guardar alimentos na geladeira também protegem."),
            desafio("passe um pouco de tinta guache nas mãos, feche os olhos e \"lave\" as mãos por 20 segundos. Veja onde a tinta ficou: são os lugares que a gente esquece!"),
        ],
        [
            mc("Por quanto tempo devemos lavar as mãos?", ["Pelo menos 20 segundos", "1 segundo", "Só molhar"], "Esfregue bem, entre os dedos também.", "🧼"),
            mc("Para que servem as **vacinas**?", ["Ensinar o corpo a se defender", "Matar a fome", "Deixar a gente mais alto"], "Elas preparam as defesas do corpo.", "💉"),
            mc("Ao **tossir**, o certo é cobrir a boca com...", ["o braço (cotovelo)", "a mão aberta e depois pegar no corrimão", "nada"], "Assim os micróbios não vão para as mãos.", "🤧"),
            mc("A água para beber deve ser...", ["filtrada ou fervida", "do rio sem tratar", "de poça"], "Mata ou retira os micróbios.", "💧"),
            separar("Protege ou espalha micróbios?", ["Protege", "Espalha"],
                    [("lavar as mãos", 0), ("tomar vacina", 0), ("lavar frutas", 0), ("dividir a escova de dentes", 1), ("tossir nas mãos", 1), ("comer sem lavar as mãos", 1)],
                    "Higiene é proteção!"),
            tf("O caderno de vacinação deve ficar sempre em dia.", True, "Peça para um adulto conferir."),
        ],
    ),
    # ------------------------------------------------------------ Ciências Humanas (História)
    "a4-b3-humanas-u1-m1": missao(
        [
            ("📜", "Há muito tempo, as pessoas se comunicavam por **sinais de fumaça**, **tambores** e **mensageiros**."),
            ("✉️", "Depois vieram as **cartas** e o **correio**, o **telégrafo** e o **telefone**."),
            ("📱", "Hoje usamos **rádio**, **TV**, **internet** e **celular**: a mensagem chega em segundos!"),
        ],
        [
            ordem("Coloque na ordem em que surgiram:", ["pintura nas cavernas", "carta", "telefone", "celular"], "Das mais antigas às mais novas."),
            mc("Qual meio é o **mais rápido** para mandar uma mensagem hoje?", ["internet", "carta", "pombo-correio"], "Chega em segundos.", "💻"),
            mc("O **telégrafo** enviava mensagens por...", ["fios e código de pontos e traços", "pombos", "fumaça"], "Era o **código Morse**.", "📡"),
            mc("Antes do celular, para falar com alguém longe usava-se...", ["telefone fixo ou carta", "e-mail", "videochamada"], "Telefones fixos e cartas.", "☎️"),
            ligar([("carta", "correio"), ("notícia falada", "rádio"), ("vídeo", "televisão"), ("mensagem instantânea", "celular")], "Ligue a mensagem ao meio"),
            tf("Os povos indígenas também usavam sinais e tambores para se comunicar.", True, "E também a **oralidade**: histórias contadas."),
        ],
    ),
    "a4-b3-humanas-u1-m2": missao(
        [
            ("🛶", "No Brasil antigo, os **rios** eram as principais **estradas**: indígenas e bandeirantes viajavam de canoa."),
            ("🐴", "Depois vieram as **trilhas** de tropeiros com mulas, as **ferrovias** (trens) e as **rodovias**."),
            ("🏘️", "Muitas cidades nasceram **perto de rios**, de portos e de estações de trem."),
        ],
        [
            mc("Por que muitas cidades surgiram **perto dos rios**?", ["Água, alimento e transporte", "Porque não chovia", "Para fugir da água"], "O rio era fonte de vida e caminho.", "🏞️"),
            mc("Os **tropeiros** transportavam mercadorias usando...", ["mulas e cavalos", "aviões", "caminhões"], "Iam em tropas pelas trilhas.", "🐴"),
            mc("A **ferrovia** é o caminho do...", ["trem", "navio", "avião"], "Trilhos de ferro.", "🚂"),
            ordem("Da forma de transporte mais antiga para a mais nova no Brasil:", ["canoa", "mula", "trem", "avião"], "A tecnologia foi mudando."),
            separar("Transporte por água ou por terra?", ["Água", "Terra"],
                    [("canoa", 0), ("navio", 0), ("balsa", 0), ("carroça", 1), ("trem", 1), ("ônibus", 1)],
                    "Rios e mares, ou estradas e trilhos."),
            tf("Até hoje, na Amazônia, muita gente viaja de barco pelos rios.", True, "Os rios ainda são estradas lá."),
        ],
    ),
    "a4-b3-humanas-u1-m3": missao(
        [
            ("🕰️", "Os jeitos de **viajar** e de **se comunicar** mudaram muito com o tempo."),
            ("👵", "Seus avós talvez mandassem **cartas** e viajassem de **trem**. Hoje mandamos **áudios** e vamos de **carro** ou **avião**."),
            ("🔎", "Comparar **antes e agora** ajuda a entender a história."),
            desafio("pergunte a um avô, avó ou adulto mais velho: como era falar com alguém que morava longe quando ele era criança?"),
        ],
        [
            separar("Mais comum antes ou agora?", ["Antes", "Agora"],
                    [("carta escrita à mão", 0), ("telegrama", 0), ("carro de boi", 0), ("videochamada", 1), ("aplicativo de mensagem", 1), ("carro elétrico", 1)],
                    "Algumas coisas ficaram no passado."),
            mc("Uma viagem que levava **dias** de carroça hoje leva **horas** de carro. Por quê?", ["Estradas e veículos melhores", "As cidades ficaram mais perto", "O tempo passou mais rápido"], "A tecnologia encurta o tempo.", "🚗"),
            mc("O que **não mudou** com o tempo?", ["A vontade de falar com quem amamos", "O uso do telégrafo", "Viajar só de canoa"], "Os meios mudam, a necessidade fica.", "💛"),
            mc("Uma **fonte histórica** para saber como era antes pode ser...", ["uma foto antiga", "um jogo novo", "um desenho de amanhã"], "Fotos, cartas e objetos antigos contam a história.", "🖼️"),
            tf("Conversar com pessoas mais velhas é uma forma de aprender história.", True, "São **fontes orais**."),
            mc("O **rádio** foi muito importante porque...", ["levava notícias para muitas casas ao mesmo tempo", "mostrava vídeos", "mandava cartas"], "Antes da TV, a família ouvia rádio junta.", "📻"),
        ],
    ),
    # ------------------------------------------------------------ Ciências Humanas (Geografia)
    "a4-b3-humanas-u2-m1": missao(
        [
            ("🌱", "O alimento começa no **campo**: alguém planta, cuida e colhe."),
            ("🏭", "Depois pode ir para a **indústria**, que transforma (o trigo vira farinha, o leite vira queijo)."),
            ("🚚", "Por fim, é **transportado** até o **comércio**: feira, mercado e supermercado."),
        ],
        [
            ordem("O caminho do pão:", ["plantar o trigo", "moer o trigo em farinha", "padaria faz o pão", "você compra o pão"], "Campo → indústria → comércio → você."),
            mc("O **leite** vem do...", ["campo (fazenda)", "supermercado", "caminhão"], "O mercado só vende; quem produz é a fazenda.", "🐄"),
            mc("A fábrica que transforma laranja em suco faz parte da...", ["indústria", "agricultura", "pecuária"], "Ela **transforma** a matéria-prima.", "🍊"),
            ligar([("algodão", "camiseta"), ("cana-de-açúcar", "açúcar"), ("cacau", "chocolate"), ("trigo", "macarrão")], "Ligue a matéria-prima ao produto"),
            mc("Sem os **caminhoneiros**, o que aconteceria?", ["Os produtos não chegariam às cidades", "Choveria mais", "Nada mudaria"], "O transporte liga campo e cidade.", "🚚"),
            tf("Agricultura é criar animais e pecuária é plantar.", False, "É o contrário: **agricultura** planta, **pecuária** cria animais."),
        ],
    ),
    "a4-b3-humanas-u2-m2": missao(
        [
            ("🏡", "No **campo** (zona rural) há plantações, criações, sítios e fazendas, com casas mais distantes."),
            ("🏙️", "Na **cidade** (zona urbana) há prédios, ruas asfaltadas, lojas, fábricas e muita gente."),
            ("🔄", "Os dois lugares têm modos de vida e trabalhos diferentes."),
        ],
        [
            separar("Mais comum no campo ou na cidade?", ["Campo", "Cidade"],
                    [("plantação de milho", 0), ("curral", 0), ("trator", 0), ("prédio alto", 1), ("metrô", 1), ("shopping", 1)],
                    "Rural ou urbano."),
            mc("Um trabalho típico do **campo** é...", ["agricultor", "motorista de metrô", "vendedor de shopping"], "O agricultor cultiva a terra.", "👨‍🌾"),
            mc("**Zona urbana** é o mesmo que...", ["cidade", "campo", "floresta"], "Urbano vem de **urbe**, cidade.", "🏙️"),
            mc("Na cidade, em geral, há...", ["mais pessoas morando perto umas das outras", "mais plantações", "menos carros"], "As cidades são mais **povoadas**.", "👥"),
            tf("Hoje há internet e energia elétrica em muitas áreas do campo.", True, "O campo também se modernizou."),
            mc("**Êxodo rural** é quando as pessoas...", ["saem do campo para morar na cidade", "saem da cidade para viajar", "plantam na cidade"], "Aconteceu muito no Brasil no século passado.", "🚶"),
        ],
    ),
    "a4-b3-humanas-u2-m3": missao(
        [
            ("🤝", "O **campo** e a **cidade** dependem um do outro."),
            ("🥕", "O campo manda **alimentos** e **matérias-primas** para a cidade."),
            ("🔧", "A cidade manda **máquinas**, **remédios**, **roupas** e serviços como bancos e hospitais."),
        ],
        [
            separar("O que vai do campo para a cidade, e da cidade para o campo?", ["Campo → cidade", "Cidade → campo"],
                    [("frutas", 0), ("leite", 0), ("madeira", 0), ("trator", 1), ("remédio", 1), ("adubo industrializado", 1)],
                    "Uma troca de produtos."),
            mc("O agricultor precisa da cidade para...", ["comprar ferramentas e vender a colheita", "plantar o feijão", "fazer chover"], "Ele vende e compra na cidade.", "🛠️"),
            mc("A cidade precisa do campo principalmente para...", ["ter alimentos", "ter prédios", "ter semáforos"], "Comida vem do campo!", "🥦"),
            mc("Uma **feira livre** é um lugar onde...", ["produtos do campo são vendidos na cidade", "se fabricam carros", "só se vendem roupas"], "Campo e cidade se encontram.", "🧺"),
            tf("Se o campo parasse de produzir, a cidade teria falta de comida.", True, "Um precisa do outro."),
            mc("O que liga o campo à cidade?", ["estradas e transportes", "muros", "rios secos"], "Sem caminhos, não há troca.", "🛣️"),
        ],
    ),
    # ------------------------------------------------------------ Ética
    "a4-b3-etica-u1-m1": missao(
        [
            ("♿", "**Acessibilidade** é fazer os lugares e as coisas funcionarem para **todas** as pessoas."),
            ("🦯", "Rampas, elevadores, piso tátil, **Braille**, **Libras** e legendas ajudam pessoas com deficiência."),
            ("💛", "**Inclusão** é garantir que todos participem, cada um do seu jeito."),
        ],
        [
            mc("Para quem usa **cadeira de rodas**, o que ajuda a entrar na escola?", ["rampa", "escada alta", "porta estreita"], "Rampas e elevadores!", "♿"),
            mc("O **Braille** é um sistema de leitura para pessoas...", ["cegas", "surdas", "baixinhas"], "Lê-se com os **dedos**, por pontinhos.", "🔤"),
            mc("A **Libras** é a língua usada por muitas pessoas...", ["surdas", "cegas", "que usam muletas"], "Língua Brasileira de Sinais.", "🤟"),
            mc("O **piso tátil** (com relevo) no chão ajuda pessoas...", ["cegas a se guiarem", "a correr mais", "a não escorregar só na chuva"], "A bengala sente o caminho.", "🦯"),
            ligar([("rampa", "cadeira de rodas"), ("Braille", "pessoa cega"), ("Libras", "pessoa surda"), ("legenda no vídeo", "quem não escuta o som")], "Ligue o recurso a quem ele ajuda"),
            tf("Acessibilidade ajuda também idosos, gestantes e quem empurra carrinho de bebê.", True, "Fica melhor para todo mundo!"),
        ],
    ),
    "a4-b3-etica-u1-m2": missao(
        [
            ("🏫", "Uma **escola acessível** recebe todo mundo: alunos com deficiência, com jeitos diferentes de aprender."),
            ("🤝", "Incluir é **convidar** para brincar, **adaptar** a brincadeira e **perguntar** como ajudar."),
            ("🚫", "Excluir, rir ou fazer apelido magoa. Diferenças fazem parte da vida."),
            desafio("dê uma volta pela escola ou pela sua casa e anote: há degraus sem rampa? Algum lugar seria difícil para quem usa cadeira de rodas?"),
        ],
        [
            mc("Um colega usa cadeira de rodas e quer brincar de pega-pega. O que fazer?", ["Adaptar a brincadeira para ele participar", "Dizer que ele não pode", "Brincar escondido"], "Adaptar é incluir!", "🏃"),
            mc("Antes de ajudar uma pessoa com deficiência, o melhor é...", ["perguntar se ela quer ajuda", "empurrar sem falar nada", "fingir que não viu"], "Respeite a escolha dela.", "🙋"),
            mc("Um colega aprende mais devagar. Você...", ["tem paciência e ajuda se ele quiser", "ri dele", "não fala com ele"], "Cada um tem o seu tempo.", "🐢"),
            separar("Inclui ou exclui?", ["Inclui", "Exclui"],
                    [("chamar para o time", 0), ("explicar de novo com calma", 0), ("usar letra grande para quem enxerga pouco", 0), ("deixar de fora", 1), ("imitar para zombar", 1), ("dizer que não sabe brincar", 1)],
                    "Atitudes fazem a diferença."),
            tf("Toda criança tem direito de estudar na escola, com ou sem deficiência.", True, "É um **direito** garantido por lei."),
            mc("Uma escola acessível precisa de...", ["rampas, banheiros adaptados e respeito", "só escadas", "portas trancadas"], "Espaço e atitude.", "🏫"),
        ],
    ),
    "a4-b3-etica-u1-m3": missao(
        [
            ("🤟", "**Libras** é uma língua de verdade, com sinais feitos com as **mãos**, o **rosto** e o **corpo**."),
            ("🔤", "O **alfabeto manual** tem um sinal para cada letra: dá para **soletrar** o seu nome!"),
            ("👋", "Na comunidade surda, cada pessoa ganha um **sinal-nome**, um sinal especial só dela."),
            desafio("procure com um adulto um vídeo do alfabeto manual em Libras e aprenda a soletrar o seu nome, {nome}!"),
        ],
        [
            mc("Libras significa...", ["Língua Brasileira de Sinais", "Livro Brasileiro de Sons", "Letras Bonitas"], "É uma língua oficial do Brasil.", "🤟"),
            mc("Em Libras, além das mãos, usamos...", ["expressões do rosto e do corpo", "apenas a voz", "apenas papel"], "O rosto mostra emoção e sentido.", "😊"),
            mc("O **alfabeto manual** serve para...", ["soletrar nomes e palavras", "fazer contas", "cantar"], "Uma letra por sinal.", "🔤"),
            mc("O **sinal-nome** é...", ["um sinal especial que representa a pessoa", "o nome escrito no quadro", "um apelido maldoso"], "É dado pela comunidade surda.", "👋"),
            tf("Libras é igual em todos os países do mundo.", False, "Cada país tem a sua língua de sinais."),
            tf("Aprender Libras ajuda a incluir colegas surdos.", True, "Comunicação é inclusão!"),
        ],
    ),
    # ------------------------------------------------------------ Inglês
    "a4-b3-ingles-u1-m1": missao(
        [
            ("👩‍⚕️", "**Jobs** são profissões! **doctor** (médico), **teacher** (professor), **firefighter** (bombeiro)."),
            ("👨‍🍳", "**cook** (cozinheiro), **farmer** (agricultor), **police officer** (policial), **vet** (veterinário)."),
            ("🏥", "**Who works here?** = Quem trabalha aqui?"),
        ],
        [
            mc("Who works in a **hospital**?", ["doctor", "farmer", "teacher"], "**Doctor** = médico.", "🏥"),
            mc("Who works in a **school**?", ["teacher", "firefighter", "cook"], "**Teacher** = professor.", "🏫"),
            mc("Who works on a **farm**?", ["farmer", "vet", "doctor"], "**Farmer** = agricultor.", "🚜"),
            mc("Who works in a **restaurant** kitchen?", ["cook", "police officer", "teacher"], "**Cook** = cozinheiro.", "🍳"),
            ligar([("doctor", "médico"), ("teacher", "professor"), ("firefighter", "bombeiro"), ("vet", "veterinário")], "Ligue a profissão à tradução"),
            mc("**Firefighter** trabalha no...", ["fire station", "hospital", "school"], "Quartel dos bombeiros.", "🚒"),
        ],
    ),
    "a4-b3-ingles-u1-m2": missao(
        [
            ("🕵️", "Vamos adivinhar a profissão pelas pistas!"),
            ("💬", "**He/She helps sick animals.** → **vet**."),
            ("🔑", "**helps** = ajuda, **cooks** = cozinha, **teaches** = ensina, **drives** = dirige."),
        ],
        [
            mc("**She teaches children.** Who is she?", ["teacher", "cook", "farmer"], "**teaches** = ensina.", "👩‍🏫"),
            mc("**He helps sick animals.** Who is he?", ["vet", "pilot", "doctor"], "Animais doentes → **vet**.", "🐶"),
            mc("**She flies a plane.** Who is she?", ["pilot", "driver", "farmer"], "**Pilot** = piloto.", "✈️"),
            mc("**He drives a bus.** Who is he?", ["bus driver", "cook", "doctor"], "**Driver** = motorista.", "🚌"),
            mc("**She puts out fires.** Who is she?", ["firefighter", "teacher", "vet"], "Apaga incêndios!", "🔥"),
            mc("**He grows vegetables.** Who is he?", ["farmer", "police officer", "pilot"], "Cultiva vegetais.", "🥕"),
            tf("**Doctor** helps sick people.", True, "Médico ajuda pessoas doentes."),
        ],
    ),
    "a4-b3-ingles-u1-m3": missao(
        [
            ("🌟", "**I want to be a...** = Eu quero ser um(a)..."),
            ("🚀", "**I want to be an astronaut!** Antes de vogal usamos **an**: an astronaut, an artist."),
            ("❓", "**What do you want to be?** = O que você quer ser?"),
        ],
        [
            mc("Como se diz **Eu quero ser médico**?", ["I want to be a doctor.", "I am doctor want.", "I want a doctor be."], "**I want to be a** + profissão.", "🩺"),
            fill("I want to be ___ astronaut.", ["an", "a", "the"], "**astronaut** começa com vogal → **an**."),
            fill("I want to be ___ teacher.", ["a", "an", "is"], "**teacher** começa com consoante → **a**."),
            mc("**What do you want to be?** significa...", ["O que você quer ser?", "Onde você mora?", "Quantos anos você tem?"], "Pergunta sobre o futuro.", "❓"),
            ordem("Monte a frase:", ["I", "want", "to", "be", "a", "pilot"], "I want to be a pilot."),
            mc("**I want to be an artist.** O que a pessoa quer ser?", ["artista", "astronauta", "atleta"], "**artist** = artista.", "🎨"),
        ],
    ),
}
