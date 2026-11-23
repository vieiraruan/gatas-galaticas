"""4º ano · 1º bimestre."""
from base import desafio, fill, ligar, mc, missao, ordem, separar, tf

MISSOES = {
    # ------------------------------------------------------------ Português
    "a4-b1-portugues-u1-m1": missao(
        [
            ("🐟", "**Ditongo** é o encontro de **duas vogais na mesma sílaba**: p**ei**-xe, c**ai**-xa, **ou**-tro."),
            ("👂", "Na fala, às vezes o som some: falamos **pexe**, mas escrevemos **peixe**!"),
            ("✍️", "Fique de olho: **caixa**, **feira**, **louça**, **cenoura**, **beijo**."),
        ],
        [
            fill("O p___xe nada no rio. 🐟", ["ei", "e", "ai"], "Escrevemos **PEIXE**, com ditongo **EI**."),
            fill("Guardei tudo na c___xa. 📦", ["ai", "a", "ei"], "**CAIXA**, com **AI**."),
            fill("O coelho come cen___ra. 🥕", ["ou", "o", "u"], "**CENOURA**: ce-**NOU**-ra, com ditongo **OU**."),
            fill("Fui à f___ra comprar frutas. 🍎", ["ei", "e", "ai"], "**FEIRA**, com **EI**."),
            fill("Lavei a l___ça do jantar. 🍽️", ["ou", "o", "u"], "**LOUÇA**, com **OU**."),
            fill("Ganhei um b___jo da vovó. 😘", ["ei", "e", "ai"], "**BEIJO**, com **EI**."),
            mc("Qual palavra tem **ditongo**?", ["PEIXE", "BOLA", "CASA"], "**EI** na mesma sílaba: PEI-XE.", "🔍"),
            tf("Em **OUTRO**, as letras **O** e **U** ficam na mesma sílaba.", True, "**OU**-TRO: é um ditongo."),
        ],
    ),
    "a4-b1-portugues-u1-m2": missao(
        [
            ("📕", "No **dicionário**, as palavras estão em **ordem alfabética**."),
            ("🔤", "Se a primeira letra for igual, olhamos a **segunda**: **ca**ma vem antes de **ce**bola."),
            ("🤔", "Uma palavra pode ter **vários sentidos**. O **contexto** da frase mostra qual usar."),
        ],
        [
            ordem("Coloque em ordem alfabética", ["abacaxi", "banana", "caju", "damasco"], "A, B, C, D."),
            ordem("Coloque em ordem alfabética", ["cabelo", "cenoura", "cidade", "cobra"], "Olhe a segunda letra: a, e, i, o."),
            ordem("Coloque em ordem alfabética", ["mala", "maré", "mato", "mula"], "MAL, MAR, MAT, MUL."),
            mc("**A manga da camisa rasgou.** Aqui, **manga** é...", ["parte da roupa que cobre o braço", "uma fruta", "um animal"], "O contexto fala de **camisa**.", "👕"),
            mc("**Comi uma manga doce.** Aqui, **manga** é...", ["uma fruta", "parte da roupa", "um tipo de sapato"], "O contexto fala de **comer**.", "🥭"),
            mc("**O banco da praça é de madeira.** Aqui, **banco** é...", ["um assento", "lugar que guarda dinheiro", "um peixe"], "Na praça, banco é para **sentar**.", "🪑"),
            mc("Qual palavra vem **primeiro** no dicionário?", ["gato", "girafa", "gorila"], "GA vem antes de GI e GO.", "📕"),
        ],
    ),
    "a4-b1-portugues-u1-m3": missao(
        [
            ("📖", "Um **leitor fluente** lê com **ritmo**, **precisão** e **expressão**."),
            ("⏱️", "Ler de novo o mesmo texto deixa a leitura cada vez mais **rápida e bonita**."),
            ("🎭", "Mude a voz nos diálogos e respeite a pontuação."),
            desafio("leia um texto curto em voz alta e grave. Daqui a uma semana, leia de novo e compare as duas gravações!"),
        ],
        [
            mc("O que mostra que você está lendo com **expressão**?", ["Mudar a voz conforme a emoção do texto", "Ler tudo com a mesma voz", "Ler sem olhar o texto"], "Expressão é dar vida ao texto.", "🎭"),
            mc("Para melhorar a leitura, o que ajuda?", ["Ler o mesmo texto várias vezes", "Ler só uma vez", "Pular as palavras difíceis"], "A repetição treina a fluência.", "🔁"),
            mc("Ao encontrar uma palavra desconhecida, o que fazer?", ["Ler devagar por sílabas e procurar o sentido", "Desistir", "Inventar outra palavra"], "Sílaba por sílaba, e depois o dicionário.", "🔍"),
            ligar([("ritmo", "nem rápido demais, nem devagar demais"), ("precisão", "ler as palavras certas"), ("expressão", "ler com emoção")], "Ligue a habilidade ao significado"),
            tf("Gravar a leitura ajuda a perceber como melhorar.", True, "Ouvir a própria leitura ajuda muito."),
        ],
    ),
    # ------------------------------------------------------------ Matemática
    "a4-b1-matematica-u1-m1": missao(
        [
            ("🔢", "Números grandes são lidos em **classes**: **45.302** → quarenta e cinco **mil**, trezentos e dois."),
            ("📍", "O **ponto** separa os milhares: **12.500** = doze mil e quinhentos."),
            ("🏟️", "Um estádio pode ter **60.000** lugares: sessenta mil!"),
        ],
        [
            mc("Como se lê **12.500**?", ["Doze mil e quinhentos", "Cento e vinte e cinco", "Mil duzentos e cinquenta"], "12 mil + 500.", "🔢"),
            mc("Como se escreve **trinta e oito mil e quarenta**?", ["38.040", "38.400", "3.840"], "38 mil + 40 = **38.040**.", "✍️"),
            mc("Como se lê **70.006**?", ["Setenta mil e seis", "Setecentos e seis", "Sete mil e seis"], "70 mil + 6.", "🔢"),
            mc("Como se escreve **noventa e nove mil, novecentos e noventa e nove**?", ["99.999", "9.999", "999.999"], "O maior número de 5 algarismos.", "🏆"),
            mc("Como se lê **15.230**?", ["Quinze mil, duzentos e trinta", "Mil quinhentos e vinte e três", "Cento e cinquenta e dois mil"], "15 mil + 230.", "🔢"),
            fill("Vinte mil e cinco = ___", ["20.005", "20.050", "2.005"], "**20.005**."),
            tf("**10.000** se lê dez mil.", True, "10 milhares."),
        ],
    ),
    "a4-b1-matematica-u1-m2": missao(
        [
            ("🧩", "**Decompor** com potências de dez: **45.302 = 4 × 10.000 + 5 × 1.000 + 3 × 100 + 2**."),
            ("🔟", "As posições valem **1**, **10**, **100**, **1.000** e **10.000**."),
            ("0️⃣", "O **zero** guarda o lugar: em 45.302 não há dezenas."),
        ],
        [
            mc("Decomponha **27.164**", ["2 × 10.000 + 7 × 1.000 + 1 × 100 + 6 × 10 + 4", "2 + 7 + 1 + 6 + 4", "27 × 1.000 + 1 × 164"], "Cada algarismo vezes o valor da posição.", "🧩"),
            mc("Qual número é **6 × 10.000 + 3 × 100 + 8**?", ["60.308", "6.308", "63.008"], "Sem milhares e sem dezenas: **60.308**.", "🔢"),
            mc("Qual número é **9 × 1.000 + 4 × 10**?", ["9.040", "9.400", "94"], "9 milhares e 4 dezenas.", "🔢"),
            mc("Em **83.517**, o **3** vale...", ["3.000", "300", "30"], "O 3 está na unidade de milhar.", "🔍"),
            mc("Em **83.517**, o **8** vale...", ["80.000", "8.000", "800"], "O 8 está na dezena de milhar.", "🔍"),
            fill("5 × 10.000 + 2 × 1.000 + 7 × 10 = ___", ["52.070", "52.700", "5.270"], "50.000 + 2.000 + 70 = **52.070**."),
            ligar([("10.000", "dezena de milhar"), ("1.000", "unidade de milhar"), ("100", "centena"), ("10", "dezena")], "Ligue o valor ao nome da ordem"),
        ],
    ),
    "a4-b1-matematica-u1-m3": missao(
        [
            ("🦘", "**Múltiplos de 6** são os resultados da tabuada do 6: **0, 6, 12, 18, 24, 30...**"),
            ("✖️", "Um número é múltiplo de 6 se a divisão por 6 tem **resto zero**."),
            ("➗", "**20 ÷ 6 = 3** e sobra **2** (resto 2). Então 20 **não** é múltiplo de 6."),
        ],
        [
            separar("Pule só nos múltiplos de 6!", ["Múltiplo de 6", "Não é"],
                    [("12", 0), ("18", 0), ("30", 0), ("42", 0), ("14", 1), ("20", 1), ("33", 1)],
                    "Múltiplos de 6: 6, 12, 18, 24, 30, 36, 42..."),
            mc("Qual vem depois na sequência **6, 12, 18, 24, ...**?", ["30", "28", "36"], "24 + 6 = **30**.", "🦘"),
            mc("Qual é o resto de **20 ÷ 6**?", ["2", "3", "0"], "6 × 3 = 18; 20 − 18 = **2**.", "➗"),
            mc("Qual é o resto de **36 ÷ 6**?", ["0", "6", "1"], "6 × 6 = 36: resto **0**.", "➗"),
            mc("Qual número é múltiplo de **5**?", ["35", "32", "27"], "Múltiplos de 5 terminam em **0** ou **5**.", "🖐️"),
            mc("Qual número é múltiplo de **2** (par)?", ["48", "37", "51"], "Termina em 0, 2, 4, 6 ou 8.", "✌️"),
            tf("**25** é múltiplo de 6.", False, "25 ÷ 6 = 4 e sobra 1."),
        ],
    ),
    # ------------------------------------------------------------ Ciências
    "a4-b1-ciencias-u1-m1": missao(
        [
            ("🧊", "Algumas transformações **voltam atrás**: são **reversíveis**. O gelo derrete e a água pode congelar de novo."),
            ("🎂", "Outras **não voltam**: são **irreversíveis**. O bolo assado não volta a ser massa!"),
            ("🔥", "O **calor**, o **frio**, a **luz** e a **umidade** podem causar transformações."),
        ],
        [
            separar("Volta ou não volta?", ["Reversível (volta)", "Irreversível (não volta)"],
                    [("gelo derretendo", 0), ("água congelando", 0), ("chocolate derretendo", 0), ("bolo assando", 1), ("papel queimando", 1), ("ovo fritando", 1)],
                    "Mudanças de estado físico costumam voltar; cozinhar e queimar não."),
            mc("A massa de pão virou pão assado. Essa transformação é...", ["irreversível", "reversível", "imaginária"], "O pão não volta a ser massa.", "🍞"),
            mc("A água virou gelo no congelador. Essa transformação é...", ["reversível", "irreversível", "impossível"], "O gelo derrete e vira água de novo.", "🧊"),
            mc("O que faz a fruta **apodrecer** mais rápido?", ["Calor e umidade", "Geladeira", "Embalagem fechada no frio"], "Calor e umidade ajudam os fungos.", "🍌"),
            mc("Um prego de ferro na chuva fica **enferrujado**. Isso é...", ["irreversível", "reversível", "uma mistura"], "A ferrugem é uma transformação **química**.", "🔩"),
            tf("Derreter manteiga é uma transformação reversível.", True, "Na geladeira, ela endurece de novo."),
        ],
    ),
    "a4-b1-ciencias-u1-m2": missao(
        [
            ("🥛", "**Mistura** é quando juntamos dois ou mais materiais."),
            ("☕", "Em algumas misturas, não dá para ver as partes: **café com leite**, **água com açúcar**."),
            ("🫗", "Em outras, dá para ver as partes separadas: **água e óleo**, **areia e pedrinhas**."),
        ],
        [
            separar("Dá para ver as partes?", ["Não dá (uma fase)", "Dá (duas ou mais fases)"],
                    [("água com açúcar dissolvido", 0), ("café com leite", 0), ("suco em pó dissolvido", 0), ("água e óleo", 1), ("areia e pedras", 1), ("feijão com arroz cru", 1)],
                    "Quando dá para ver as partes, a mistura é **heterogênea**."),
            mc("Jogamos **óleo na água**. O que acontece?", ["O óleo fica por cima", "Eles se misturam totalmente", "O óleo some"], "Óleo e água **não se misturam**.", "🫗"),
            mc("Colocamos **sal na água** e mexemos. O que acontece?", ["O sal se dissolve", "O sal flutua", "A água vira gelo"], "O sal se **dissolve** na água.", "🧂"),
            mc("Como separar **areia da água**?", ["Com um filtro (como o de café)", "Com um ímã", "Soprando"], "O filtro segura a areia.", "☕"),
            mc("Qual destas **é** uma mistura?", ["Salada de frutas", "Uma pedra de gelo pura", "Uma colher de sal puro"], "Várias frutas juntas!", "🥗"),
            tf("O ar que respiramos é uma mistura de gases.", True, "Oxigênio, gás carbônico, nitrogênio..."),
        ],
    ),
    "a4-b1-ciencias-u1-m3": missao(
        [
            ("🧪", "A **cozinha** pode ser um **laboratório**!"),
            ("🍬", "Com o **calor**, o açúcar **derrete**, fica **marrom** e vira **caramelo**, com cheiro novo."),
            ("⚠️", "**Só com um adulto!** O caramelo fica muito quente."),
            desafio("com um adulto, aqueça um pouco de açúcar numa panela, observe as mudanças de cor e cheiro e desenhe o que viu."),
        ],
        [
            mc("O que acontece com o açúcar no fogo?", ["Derrete e fica marrom (caramelo)", "Vira gelo", "Fica azul"], "O calor transforma o açúcar.", "🍮"),
            mc("O caramelo pode voltar a ser açúcar branco?", ["Não, é irreversível", "Sim, é só esfriar", "Sim, é só soprar"], "Houve uma transformação **química**.", "🔁"),
            mc("Quais sinais mostram que houve transformação?", ["Mudança de cor e cheiro", "O açúcar continua igual", "A panela ficou nova"], "Cor e cheiro novos são pistas.", "👃"),
            ordem("Organize o experimento", ["Colocar açúcar na panela", "Aquecer com um adulto", "Observar a cor e o cheiro", "Registrar num desenho"], "Observar e registrar como um cientista."),
            tf("Experimentos com fogo devem ser feitos sempre com um adulto.", True, "Segurança em primeiro lugar!"),
        ],
    ),
    # ------------------------------------------------------------ Ciências Humanas (História)
    "a4-b1-humanas-u1-m1": missao(
        [
            ("🏹", "Há muito tempo, os seres humanos eram **nômades**: mudavam de lugar procurando comida."),
            ("🌾", "Depois aprenderam a **plantar** (agricultura) e a **criar animais** (pastoreio)."),
            ("🏙️", "Com isso, surgiram as **aldeias**, depois as **cidades** e, muito depois, as **indústrias**."),
        ],
        [
            ordem("Coloque os grandes marcos na ordem", ["Nomadismo (caça e coleta)", "Agricultura e pastoreio", "Primeiras cidades", "Indústrias e fábricas"], "Uma longa história de mudanças."),
            mc("O que os nômades faziam para comer?", ["Caçavam, pescavam e coletavam frutos", "Compravam no mercado", "Pediam comida por aplicativo"], "Eles viviam da **caça e coleta**.", "🏹"),
            mc("O que mudou com a **agricultura**?", ["As pessoas puderam ficar num lugar só", "Todos viraram nômades", "Acabou a comida"], "Plantar permitiu **fixar-se**.", "🌾"),
            mc("Quem faz a história?", ["Todos os seres humanos, com suas ações", "Só os reis", "Só os livros"], "A história é feita pela **ação humana**.", "🧑‍🤝‍🧑"),
            tf("As indústrias surgiram antes da agricultura.", False, "A agricultura veio muito antes."),
        ],
    ),
    "a4-b1-humanas-u1-m2": missao(
        [
            ("⛺", "**Nômade**: não tem moradia fixa, muda de lugar conforme a comida e o clima."),
            ("🏠", "**Sedentário**: vive num lugar fixo, com casa, plantação e criação."),
            ("🐪", "Ainda hoje existem povos nômades, como alguns grupos que vivem em desertos com seus rebanhos."),
        ],
        [
            separar("Nômade ou sedentário?", ["Nômade", "Sedentário"],
                    [("muda de lugar seguindo os animais", 0), ("vive em tendas que são desmontadas", 0), ("caça e coleta frutos", 0), ("planta milho perto de casa", 1), ("mora numa aldeia fixa", 1), ("guarda grãos em celeiros", 1)],
                    "O nômade se desloca; o sedentário se fixa."),
            mc("Por que os nômades mudavam de lugar?", ["Para encontrar comida e água", "Para passear", "Porque não gostavam de casa"], "Quando a comida acabava, era hora de ir.", "🚶"),
            mc("Qual moradia combina com a vida **nômade**?", ["Tenda fácil de desmontar", "Prédio de 20 andares", "Casa de tijolos"], "Precisa ser fácil de carregar.", "⛺"),
            tf("Hoje, a maioria das pessoas vive de forma sedentária.", True, "Moramos em lugares fixos."),
            fill("Quem vive sempre no mesmo lugar é ___.", ["sedentário", "nômade", "viajante"], "**Sedentário**."),
        ],
    ),
    "a4-b1-humanas-u1-m3": missao(
        [
            ("🌱", "Para **plantar**, é preciso **esperar** a planta crescer: semanas ou meses."),
            ("🏡", "Por isso, os agricultores precisavam **ficar perto** das plantações."),
            ("🏺", "Também passaram a **guardar** alimentos e a **trocar** o que sobrava. Assim nasceram as vilas."),
        ],
        [
            mc("Por que a agricultura fez as pessoas se **fixarem**?", ["Era preciso cuidar da plantação até a colheita", "As pessoas ficaram cansadas de andar", "Choveu muito"], "A plantação precisa de cuidado e tempo.", "🌱"),
            mc("Onde os primeiros agricultores preferiam morar?", ["Perto de rios", "No alto de vulcões", "No meio do deserto sem água"], "Rios dão água para as plantações.", "🏞️"),
            mc("O que faziam com os alimentos que **sobravam**?", ["Guardavam ou trocavam", "Jogavam fora sempre", "Enterravam para sempre"], "Surgiram o **armazenamento** e o **comércio**.", "🏺"),
            ordem("Coloque na ordem", ["Plantar as sementes", "Cuidar da plantação", "Colher", "Guardar e trocar o que sobra"], "O ciclo da agricultura."),
            tf("Ficar num lugar fixo ajudou a formar vilas e cidades.", True, "Muitas casas juntas formaram as primeiras vilas."),
        ],
    ),
    # ------------------------------------------------------------ Ciências Humanas (Geografia)
    "a4-b1-humanas-u2-m1": missao(
        [
            ("🗣️", "O português do Brasil tem muitas palavras de **origem indígena** (tupi) e **africana** (iorubá, quimbundo)."),
            ("🦜", "Indígenas: **abacaxi**, **jabuti**, **pipoca**, **tatu**, **Paraná**."),
            ("🥁", "Africanas: **caçula**, **cochilar**, **moleque**, **samba**, **quitanda**."),
        ],
        [
            separar("Origem indígena ou africana?", ["Indígena (tupi)", "Africana"],
                    [("abacaxi", 0), ("jabuti", 0), ("tatu", 0), ("caçula", 1), ("cochilar", 1), ("quitanda", 1)],
                    "Nossa língua mistura muitas origens."),
            ligar([("pipoca", "indígena"), ("moleque", "africana"), ("escola", "latina (portuguesa)")], "Ligue a palavra à origem"),
            mc("A palavra **caçula** (o filho mais novo) tem origem...", ["africana", "japonesa", "inglesa"], "Vem do **quimbundo**, língua africana.", "👶"),
            mc("A palavra **jabuti** tem origem...", ["indígena", "africana", "francesa"], "Vem do **tupi**.", "🐢"),
            tf("Muitos nomes de lugares do Brasil vêm de línguas indígenas.", True, "Paraná, Ipanema, Itaquera, Curitiba..."),
        ],
    ),
    "a4-b1-humanas-u2-m2": missao(
        [
            ("🗺️", "**Terras indígenas** são territórios onde povos indígenas vivem e preservam sua cultura. Muitas ficam na **Amazônia**."),
            ("✊", "**Comunidades quilombolas** são formadas por descendentes de africanos que resistiram à escravidão."),
            ("⚖️", "A **Constituição** garante o direito desses povos às suas terras."),
        ],
        [
            mc("Em qual região do Brasil está a **maior parte** das terras indígenas?", ["Norte (Amazônia)", "Sul", "Sudeste"], "A Amazônia tem as maiores terras indígenas.", "🌳"),
            mc("Quem vive nas **comunidades quilombolas**?", ["Descendentes de africanos que resistiram à escravidão", "Imigrantes europeus", "Turistas"], "Os quilombos eram espaços de liberdade.", "✊"),
            mc("Por que as terras indígenas são importantes?", ["Garantem o modo de vida e ajudam a preservar a floresta", "Servem para construir shoppings", "Não são importantes"], "Elas protegem culturas e a natureza.", "🌿"),
            mc("O **Parque Indígena do Xingu** fica em qual estado?", ["Mato Grosso", "Rio Grande do Sul", "Bahia"], "Fica no **Mato Grosso**.", "🗺️"),
            tf("A lei brasileira reconhece o direito dos povos indígenas às suas terras.", True, "Está na Constituição de 1988."),
        ],
    ),
    "a4-b1-humanas-u2-m3": missao(
        [
            ("➡️", "Num **mapa de fluxos**, as **setas** mostram de onde as pessoas saem e para onde vão."),
            ("🧳", "No século 20, muitos nordestinos migraram para **São Paulo** e **Rio de Janeiro** em busca de trabalho."),
            ("🌍", "Também chegaram imigrantes de outros países: **japoneses**, **italianos**, e hoje **venezuelanos**, **haitianos**, **bolivianos**..."),
        ],
        [
            mc("No mapa, uma **seta** do Nordeste para São Paulo mostra...", ["pessoas migrando do Nordeste para São Paulo", "um rio", "uma estrada de ferro"], "Setas indicam a **direção** do movimento.", "➡️"),
            mc("Uma seta **mais grossa** num mapa de fluxos significa...", ["mais pessoas migrando", "um caminho mais bonito", "menos pessoas"], "A espessura mostra a **quantidade**.", "📏"),
            mc("Por que muitas pessoas migram?", ["Em busca de trabalho e melhores condições", "Para colecionar mapas", "Sem motivo"], "Trabalho, segurança e família são motivos comuns.", "💼"),
            mc("Os imigrantes **japoneses** chegaram ao Brasil em 1908, principalmente em qual estado?", ["São Paulo", "Acre", "Piauí"], "Muitos foram trabalhar nas fazendas de café de **São Paulo**.", "🇯🇵"),
            tf("Migração é o movimento de pessoas de um lugar para outro.", True, "Pode ser dentro do país ou entre países."),
            fill("Quem chega de outro país para morar aqui é ___.", ["imigrante", "emigrante", "turista"], "Quem **chega** é **imigrante**."),
        ],
    ),
    # ------------------------------------------------------------ Ética
    "a4-b1-etica-u1-m1": missao(
        [
            ("📘", "O **ECA** (Estatuto da Criança e do Adolescente) é a lei que protege crianças e adolescentes no Brasil."),
            ("🏫", "Toda criança tem direito à **educação**, **saúde**, **alimentação**, **lazer** (brincar) e **proteção**."),
            ("🏠", "Também tem direito a **convivência familiar** e a ser tratada com **respeito**."),
        ],
        [
            ligar([("🏫 escola", "educação"), ("🩺 vacina", "saúde"), ("🛝 parquinho", "brincar"), ("🍲 refeição", "alimentação")], "Ligue a imagem ao direito"),
            mc("Ir à escola é um direito de...", ["educação", "lazer", "trabalho"], "Toda criança tem direito à **educação**.", "🏫"),
            mc("Tomar vacina é um direito de...", ["saúde", "transporte", "brincar"], "Vacina protege a **saúde**.", "💉"),
            mc("Como se chama a lei que protege as crianças?", ["ECA", "CNH", "CEP"], "**Estatuto da Criança e do Adolescente**.", "📘"),
            tf("Brincar é um direito da criança.", True, "O direito ao **lazer** está no ECA."),
            tf("Criança pode ser obrigada a trabalhar em vez de estudar.", False, "O trabalho infantil é **proibido**."),
        ],
    ),
    "a4-b1-etica-u1-m2": missao(
        [
            ("⚖️", "**Direitos e deveres andam juntos.**"),
            ("📚", "Tenho **direito** de estudar e o **dever** de fazer as tarefas e respeitar os colegas."),
            ("🤝", "Tenho direito de ser respeitado e o **dever** de respeitar os outros."),
        ],
        [
            separar("Direito ou dever?", ["Direito", "Dever"],
                    [("ir à escola", 0), ("ter atendimento médico", 0), ("brincar", 0), ("fazer a lição de casa", 1), ("respeitar os colegas", 1), ("cuidar do material", 1)],
                    "Direitos protegem; deveres mostram responsabilidade."),
            mc("Tenho direito a um ambiente limpo. Qual é o meu **dever**?", ["Não jogar lixo no chão", "Sujar à vontade", "Esperar alguém limpar"], "Cada direito vem com um dever.", "🧹"),
            mc("Tenho direito de falar na aula. Qual é o meu dever?", ["Ouvir quando o outro fala", "Falar mais alto que todos", "Nunca deixar ninguém falar"], "Respeitar a vez do outro.", "🗣️"),
            mc("Quem tem deveres?", ["Todas as pessoas, inclusive crianças", "Só os adultos", "Ninguém"], "Cada um, de acordo com a idade.", "🧑‍🤝‍🧑"),
            tf("Direitos e deveres andam juntos.", True, "Para ter direitos garantidos, todos cumprem seus deveres."),
        ],
    ),
    "a4-b1-etica-u1-m3": missao(
        [
            ("🛡️", "Quando uma criança precisa de ajuda, há pessoas e lugares para **proteger**."),
            ("👨‍👩‍👧", "A **família** e a **escola** são os primeiros a quem pedir ajuda."),
            ("📞", "O **Conselho Tutelar** protege os direitos das crianças. E o **Disque 100** recebe denúncias."),
        ],
        [
            mc("Uma criança está sendo maltratada. A quem pedir ajuda?", ["A um adulto de confiança ou ao Conselho Tutelar", "A ninguém", "A um desconhecido na internet"], "Sempre conte para um **adulto de confiança**.", "🛡️"),
            mc("Qual órgão protege os direitos das crianças na cidade?", ["Conselho Tutelar", "Corpo de Bombeiros", "Correios"], "O **Conselho Tutelar** cuida disso.", "🏛️"),
            mc("Um colega está sofrendo **bullying** na escola. O que fazer?", ["Contar para um professor", "Rir junto", "Fingir que não viu"], "A escola deve ajudar a resolver.", "🧑‍🏫"),
            mc("Qual número recebe denúncias de violação de direitos humanos?", ["Disque 100", "Disque 190 para pizza", "Disque 1234"], "O **Disque 100** é gratuito.", "📞"),
            tf("Pedir ajuda quando algo está errado é um ato de coragem.", True, "Você não está sozinho!"),
        ],
    ),
    # ------------------------------------------------------------ Inglês
    "a4-b1-ingles-u1-m1": missao(
        [
            ("⏰", "**My day** (meu dia) em inglês!"),
            ("🛏️", "**wake up** = acordar · **brush my teeth** = escovar os dentes · **have breakfast** = tomar café da manhã"),
            ("🏫", "**go to school** = ir à escola · **do homework** = fazer a lição · **go to bed** = ir dormir"),
        ],
        [
            ordem("Put my day in order", ["I wake up.", "I brush my teeth.", "I have breakfast.", "I go to school.", "I go to bed."], "Da manhã até a noite."),
            ligar([("wake up", "acordar"), ("have breakfast", "tomar café da manhã"), ("do homework", "fazer a lição"), ("go to bed", "ir dormir")], "Ligue a ação ao significado"),
            mc("O que quer dizer **I brush my teeth**?", ["Eu escovo os dentes", "Eu tomo banho", "Eu como"], "brush = escovar · teeth = dentes.", "🪥"),
            mc("Qual é a **última** coisa do dia?", ["I go to bed.", "I wake up.", "I have breakfast."], "Ir dormir: **go to bed**.", "🛏️"),
            fill("I ___ to school at 7. (Eu vou à escola às 7.)", ["go", "wake", "brush"], "ir = **go**."),
        ],
    ),
    "a4-b1-ingles-u1-m2": missao(
        [
            ("🕐", "**What time is it?** = Que horas são?"),
            ("⏰", "**It's three o'clock.** = São três horas (em ponto)."),
            ("🔢", "Revise: one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve."),
        ],
        [
            mc("What time is it? 🕒", ["It's three o'clock.", "It's nine o'clock.", "It's twelve o'clock."], "🕒 = 3 horas = **three**.", None),
            mc("What time is it? 🕖", ["It's seven o'clock.", "It's eleven o'clock.", "It's one o'clock."], "🕖 = 7 horas = **seven**.", None),
            mc("What time is it? 🕙", ["It's ten o'clock.", "It's two o'clock.", "It's six o'clock."], "🕙 = 10 horas = **ten**.", None),
            mc("What time is it? 🕛", ["It's twelve o'clock.", "It's eight o'clock.", "It's four o'clock."], "🕛 = 12 horas = **twelve**.", None),
            ligar([("🕐", "one o'clock"), ("🕔", "five o'clock"), ("🕗", "eight o'clock"), ("🕚", "eleven o'clock")], "Ligue o relógio à hora em inglês"),
            mc("O que quer dizer **What time is it?**", ["Que horas são?", "Que dia é hoje?", "Como está o tempo?"], "time = hora/tempo.", "⏰"),
        ],
    ),
    "a4-b1-ingles-u1-m3": missao(
        [
            ("📖", "Leia a rotina do Tom:"),
            ("👦", "**Tom wakes up at seven o'clock. He has breakfast with his mom. He goes to school by bus. After school, he plays football. He goes to bed at nine o'clock.**"),
            ("💡", "**by bus** = de ônibus · **after school** = depois da escola · **plays football** = joga futebol"),
        ],
        [
            mc("What time does Tom wake up?", ["At seven o'clock", "At nine o'clock", "At twelve o'clock"], "**Tom wakes up at seven o'clock.**", "⏰"),
            mc("Who does Tom have breakfast with?", ["His mom", "His dog", "His teacher"], "**with his mom** = com a mãe dele.", "👩"),
            mc("How does Tom go to school?", ["By bus", "By bike", "On foot"], "**by bus** = de ônibus.", "🚌"),
            mc("What does Tom do after school?", ["He plays football.", "He goes to bed.", "He wakes up."], "Depois da escola, ele **joga futebol**.", "⚽"),
            mc("What time does Tom go to bed?", ["At nine o'clock", "At seven o'clock", "At three o'clock"], "**at nine o'clock** = às nove.", "🛏️"),
            ordem("Put Tom's day in order", ["Tom wakes up.", "He has breakfast.", "He goes to school.", "He plays football.", "He goes to bed."], "A rotina do Tom."),
        ],
    ),
}
