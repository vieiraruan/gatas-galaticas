"""5º ano · 4º bimestre."""
from base import desafio, fill, ligar, mc, missao, ordem, separar, tf

MISSOES = {
    # ------------------------------------------------------------ Português
    "a5-b4-portugues-u1-m1": missao(
        [
            ("🔬", "Toda narrativa tem **elementos**: **personagens**, **tempo** (quando), **espaço** (onde), **enredo** (o que acontece) e **narrador** (quem conta)."),
            ("📖", "Leia: **Numa noite de inverno, na vila de Pedra Azul, a menina Iara encontrou um filhote de coruja caído. Ela o levou para casa, cuidou dele por uma semana e, quando ficou forte, a coruja voou de volta para a mata.**"),
            ("🎙️", "O narrador pode **participar** da história (1ª pessoa: **eu**) ou só **observar** (3ª pessoa: **ela**, **ele**)."),
        ],
        [
            mc("Na história de Iara, qual é o **espaço**?", ["A vila de Pedra Azul", "Numa noite de inverno", "Iara e a coruja"], "Espaço = **onde** acontece.", "🏘️"),
            mc("Qual é o **tempo** da história?", ["Numa noite de inverno", "A vila de Pedra Azul", "A mata"], "Tempo = **quando** acontece.", "🌙"),
            mc("Quem são os **personagens**?", ["Iara e a coruja", "A vila e a mata", "O inverno e a noite"], "Personagens são quem participa da história.", "🦉"),
            mc("O narrador dessa história é...", ["observador (3ª pessoa)", "personagem (1ª pessoa)", "não tem narrador"], "Ele conta usando **ela**: não participa.", "🎙️"),
            ordem("Coloque o enredo na ordem", ["Iara encontra o filhote caído", "Leva a coruja para casa", "Cuida dela por uma semana", "A coruja volta para a mata"],
                  "Situação inicial, desenvolvimento e desfecho."),
            ligar([("personagens", "quem"), ("tempo", "quando"), ("espaço", "onde"), ("enredo", "o que acontece")], "Ligue o elemento à pergunta que ele responde"),
            tf("**Eu acordei e vi o dragão** tem narrador-personagem.", True, "O uso de **eu** mostra narrador em 1ª pessoa."),
            fill("A parte final da história, em que o conflito se resolve, é o ___.", ["desfecho", "título", "narrador"], "O **desfecho** encerra a narrativa."),
        ],
    ),
    "a5-b4-portugues-u1-m2": missao(
        [
            ("💬", "**Discurso direto**: a fala do personagem aparece do jeito que ele falou, com **travessão** ou **aspas**."),
            ("➡️", "Exemplo direto: **Ana disse: — Estou com fome.**"),
            ("🔁", "**Discurso indireto**: o narrador conta o que o personagem disse. **Ana disse que estava com fome.**"),
        ],
        [
            mc("Transforme em indireto: **Pedro disse: — Eu vou à praia.**", ["Pedro disse que ia à praia.", "Pedro disse: eu vou à praia.", "— Vou à praia, disse Pedro."], "No indireto usamos **que** e mudamos **eu vou** para **ia**.", "🏖️"),
            mc("Transforme em indireto: **A professora perguntou: — Vocês fizeram a lição?**", ["A professora perguntou se eles tinham feito a lição.", "A professora perguntou: vocês fizeram?", "— Fizeram a lição? perguntou."], "Pergunta no indireto usa **se**.", "👩‍🏫"),
            mc("Qual frase está em **discurso direto**?", ["— Que dia lindo! exclamou Bia.", "Bia disse que o dia estava lindo.", "Bia achou o dia lindo."], "O **travessão** marca a fala direta.", "☀️"),
            separar("Direto ou indireto?", ["Discurso direto", "Discurso indireto"],
                    [("— Eu adoro ler! disse Caio.", 0), ("Mãe falou: \"Hora do banho!\"", 0), ("Caio disse que adorava ler.", 1), ("A mãe avisou que era hora do banho.", 1)],
                    "Travessão e aspas = direto. **disse que** = indireto."),
            fill("No discurso indireto, geralmente usamos a palavra ___ depois do verbo disse.", ["que", "travessão", "ontem"], "**Disse que...**"),
            tf("O travessão (—) é usado no discurso indireto.", False, "O travessão marca o discurso **direto**."),
        ],
    ),
    "a5-b4-portugues-u1-m3": missao(
        [
            ("📜", "O **poema** é organizado em **versos** (cada linha) e **estrofes** (grupos de versos)."),
            ("🎵", "Recursos poéticos: **rima** (sons iguais no fim), **ritmo** e **repetição**."),
            ("🎤", "**Declamar** é ler em voz alta com emoção, pausas e boa entonação."),
            desafio("escolha um poema de que você goste, ensaie e declame para a família. Peça para um adulto gravar o seu sarau."),
        ],
        [
            mc("Cada **linha** de um poema se chama...", ["verso", "estrofe", "parágrafo"], "Linha do poema = **verso**.", "📜"),
            mc("Um grupo de versos se chama...", ["estrofe", "capítulo", "título"], "Os versos formam **estrofes**.", "📄"),
            mc("Leia: **A lua no céu / brilha para mim / parece um chapéu / de puro marfim.** Quais palavras rimam com **céu**?", ["chapéu", "mim", "marfim"], "**céu** e **chapéu** terminam com o mesmo som.", "🌙"),
            mc("No poema da lua, quantos versos há?", ["4", "2", "1"], "São **4 versos** numa estrofe.", "🔢"),
            mc("O que ajuda a declamar bem?", ["Ler com calma, emoção e pausas", "Ler bem rápido sem parar", "Ler sussurrando de costas"], "Entonação e pausas dão vida ao poema.", "🎤"),
            tf("Todo poema precisa ter rima.", False, "Há poemas **sem rima** (versos livres)."),
            fill("Palavras com o mesmo som no final dos versos formam a ___.", ["rima", "estrofe", "prosa"], "Isso é **rima**."),
        ],
    ),
    # ------------------------------------------------------------ Matemática
    "a5-b4-matematica-u1-m1": missao(
        [
            ("📏", "**1 metro (m) = 100 centímetros (cm)**. **1 quilômetro (km) = 1000 metros**."),
            ("🥛", "**1 litro (L) = 1000 mililitros (mL)**."),
            ("⚖️", "**1 quilograma (kg) = 1000 gramas (g)**."),
        ],
        [
            mc("Quantos centímetros há em **3 metros**?", ["300 cm", "30 cm", "3000 cm"], "3 × 100 = **300 cm**.", "📏"),
            mc("Quantos mililitros há em **2 litros**?", ["2000 mL", "200 mL", "20 mL"], "2 × 1000 = **2000 mL**.", "🥛"),
            mc("**250 cm** são quantos metros?", ["2,5 m", "25 m", "0,25 m"], "250 ÷ 100 = **2,5 m**.", "📐"),
            mc("Quantos metros há em **4 km**?", ["4000 m", "400 m", "40 m"], "4 × 1000 = **4000 m**.", "🛣️"),
            mc("Meio litro de suco tem quantos mililitros?", ["500 mL", "50 mL", "5000 mL"], "[[1/2]] de 1000 = **500 mL**.", "🧃"),
            mc("Um pacote de **1,5 kg** tem quantos gramas?", ["1500 g", "150 g", "15 g"], "1,5 × 1000 = **1500 g**.", "📦"),
            ligar([("1 m", "100 cm"), ("1 L", "1000 mL"), ("1 kg", "1000 g"), ("1 km", "1000 m")], "Ligue as medidas equivalentes"),
            ordem("Do menor para o maior", ["50 cm", "1 m", "150 cm", "2 m"], "50 cm < 100 cm < 150 cm < 200 cm."),
        ],
    ),
    "a5-b4-matematica-u1-m2": missao(
        [
            ("🧱", "**Perímetro** é a medida do **contorno** de uma figura (a cerca do jardim)."),
            ("🟩", "**Área** é a medida da **superfície** de dentro (a grama do jardim)."),
            ("🔄", "Um jardim **4 × 2** e um **5 × 1** têm o **mesmo perímetro (12)**, mas áreas diferentes: **8** e **5**."),
        ],
        [
            mc("Qual é o perímetro de um retângulo de **4 m por 2 m**?", ["12 m", "8 m", "6 m"], "4 + 2 + 4 + 2 = **12 m**.", "🧱"),
            mc("Qual é a área de um retângulo de **4 m por 2 m**?", ["8 m²", "12 m²", "6 m²"], "4 × 2 = **8 m²**.", "🟩"),
            mc("Um quadrado tem lado **3 cm**. Qual é o perímetro?", ["12 cm", "9 cm", "6 cm"], "4 × 3 = **12 cm**.", "🟥"),
            mc("E a área desse quadrado de lado 3 cm?", ["9 cm²", "12 cm²", "6 cm²"], "3 × 3 = **9 cm²**.", "🟦"),
            mc("Jardins com **12 m de cerca**: qual tem **maior área**?", ["3 m × 3 m", "5 m × 1 m", "4 m × 2 m"], "Áreas: 9, 5 e 8. O **quadrado 3 × 3** ganha.", "🌻"),
            tf("Duas figuras com o mesmo perímetro sempre têm a mesma área.", False, "4 × 2 e 5 × 1 têm perímetro 12, mas áreas 8 e 5."),
            separar("Isso é perímetro ou área?", ["Perímetro (contorno)", "Área (superfície)"],
                    [("cerca do jardim", 0), ("rodapé da sala", 0), ("moldura do quadro", 0), ("grama do jardim", 1), ("piso da sala", 1), ("tinta da parede", 1)],
                    "Contorno = perímetro. O que cobre a superfície = área."),
        ],
    ),
    "a5-b4-matematica-u1-m3": missao(
        [
            ("🧊", "**Volume** é o espaço que um objeto ocupa."),
            ("📦", "Podemos medir o volume **contando cubinhos** iguais."),
            ("✖️", "Uma caixa de **3 cubos de comprimento, 2 de largura e 2 de altura** tem **3 × 2 × 2 = 12 cubos**."),
        ],
        [
            mc("Uma pilha tem **2 camadas** de **4 cubos** cada. Quantos cubos?", ["8", "6", "16"], "2 × 4 = **8 cubos**.", "🧊"),
            mc("Caixa com **3 × 3 × 1** cubinhos. Qual é o volume?", ["9 cubos", "7 cubos", "27 cubos"], "3 × 3 × 1 = **9**.", "📦"),
            mc("Caixa com **2 × 2 × 2** cubinhos. Qual é o volume?", ["8 cubos", "6 cubos", "4 cubos"], "2 × 2 × 2 = **8**.", "🎲"),
            mc("Caixa com **4 × 3 × 2** cubinhos. Qual é o volume?", ["24 cubos", "9 cubos", "12 cubos"], "4 × 3 = 12; 12 × 2 = **24**.", "🗃️"),
            mc("Uma caixa tem **5 cubos** por camada e **3 camadas**. Quantos cubos?", ["15", "8", "53"], "5 × 3 = **15**.", "🧱"),
            ordem("Da caixa com menor volume à maior", ["1 × 2 × 2 = 4", "2 × 2 × 2 = 8", "3 × 2 × 2 = 12", "3 × 3 × 2 = 18"], "4 < 8 < 12 < 18."),
            tf("Para achar o volume, multiplicamos comprimento × largura × altura.", True, "É o mesmo que contar todos os cubinhos."),
        ],
    ),
    "a5-b4-matematica-u2-m1": missao(
        [
            ("🎲", "**Espaço amostral** é a lista de **todos os resultados possíveis**. No dado: {1, 2, 3, 4, 5, 6}."),
            ("➗", "**Probabilidade** = casos favoráveis ÷ casos possíveis. Sair 5 no dado: [[1/6]]."),
            ("🪙", "Sair cara numa moeda: **1 em 2** = [[1/2]]."),
        ],
        [
            mc("Qual é a probabilidade de sair **cara** numa moeda?", ["[[1/2]]", "[[1/6]]", "[[2/1]]"], "1 caso favorável em 2 possíveis.", "🪙"),
            mc("Qual é a probabilidade de sair **4** num dado?", ["[[1/6]]", "[[1/4]]", "[[4/6]]"], "1 caso favorável em 6.", "🎲"),
            mc("Num dado, qual a probabilidade de sair número **par**?", ["[[3/6]]", "[[2/6]]", "[[1/6]]"], "Pares: 2, 4, 6 → 3 em 6 (= [[1/2]]).", "⚖️"),
            mc("Uma roleta tem **4 partes iguais**: 3 azuis e 1 vermelha. Probabilidade de cair no **azul**?", ["[[3/4]]", "[[1/4]]", "[[3/1]]"], "3 partes azuis em 4.", "🎡"),
            mc("Saco com **2 bolas verdes e 8 amarelas**. Probabilidade de tirar **verde**?", ["[[2/10]]", "[[2/8]]", "[[8/10]]"], "2 verdes em 10 bolas.", "🟢"),
            mc("Qual é o espaço amostral de uma moeda?", ["{cara, coroa}", "{1, 2, 3, 4, 5, 6}", "{cara}"], "São os dois lados.", "🪙"),
            tf("A probabilidade de sair 7 num dado comum é zero.", True, "É um evento **impossível**."),
        ],
    ),
    "a5-b4-matematica-u2-m2": missao(
        [
            ("📈", "O **gráfico de linhas** mostra como algo **muda ao longo do tempo**."),
            ("🌡️", "Temperatura da semana: **seg 22°**, **ter 25°**, **qua 28°**, **qui 24°**, **sex 20°**."),
            ("↗️", "Linha **subindo** = aumentou. Linha **descendo** = diminuiu."),
        ],
        [
            mc("Qual foi o dia **mais quente**?", ["Quarta", "Segunda", "Sexta"], "Quarta: **28°**, o ponto mais alto.", "🌡️"),
            mc("Qual foi o dia **mais frio**?", ["Sexta", "Segunda", "Terça"], "Sexta: **20°**.", "🥶"),
            mc("De segunda para quarta, a temperatura...", ["subiu", "desceu", "ficou igual"], "22° → 25° → 28°: **subiu**.", "↗️"),
            mc("De quarta para sexta, a temperatura...", ["desceu", "subiu", "ficou igual"], "28° → 24° → 20°: **desceu**.", "↘️"),
            mc("Quantos graus a temperatura subiu de segunda para quarta?", ["6°", "3°", "28°"], "28 − 22 = **6°**.", "🧮"),
            mc("Para mostrar o crescimento de uma planta mês a mês, o melhor gráfico é...", ["de linhas", "de setores (pizza)", "pictograma de frutas"], "Variação ao longo do tempo = **linhas**.", "🌱"),
            tf("No gráfico de linhas, uma linha reta e deitada mostra que o valor não mudou.", True, "Sem subir nem descer = **constante**."),
        ],
    ),
    "a5-b4-matematica-u2-m3": missao(
        [
            ("📋", "Uma **pesquisa** tem etapas: escolher a pergunta, coletar respostas, organizar em **tabela** e fazer o **gráfico**."),
            ("✍️", "Na **tabela**, cada linha é uma opção e a coluna mostra a quantidade (**frequência**)."),
            ("🗣️", "Depois, escrevemos uma **conclusão**: o que a pesquisa mostrou?"),
            desafio("pergunte a 10 pessoas qual é a fruta preferida, monte uma tabela e um gráfico de barras num papel e escreva uma conclusão."),
        ],
        [
            ordem("Coloque as etapas da pesquisa na ordem", ["Escolher a pergunta", "Coletar as respostas", "Organizar na tabela", "Fazer o gráfico", "Escrever a conclusão"], "Planejar, coletar, organizar, representar e concluir."),
            mc("Tabela: **Manga 4, Uva 3, Maçã 2, Banana 1**. Quantas pessoas responderam?", ["10", "4", "9"], "4 + 3 + 2 + 1 = **10**.", "🧮"),
            mc("Qual conclusão está correta para a tabela?", ["A manga é a fruta preferida", "A banana é a preferida", "Todos preferem uva"], "Manga teve mais votos: **4**.", "🥭"),
            mc("Que fração das pessoas prefere manga?", ["[[4/10]]", "[[1/4]]", "[[4/4]]"], "4 de 10 pessoas.", "🍕"),
            mc("Qual é uma boa pergunta de pesquisa?", ["Qual é o seu esporte preferido?", "Você é legal?", "Por quê?"], "Ela tem respostas que dá para contar.", "❓"),
            tf("Numa pesquisa, devemos anotar todas as respostas, mesmo as que não gostamos.", True, "A pesquisa precisa ser **honesta**."),
        ],
    ),
    # ------------------------------------------------------------ Ciências
    "a5-b4-ciencias-u1-m1": missao(
        [
            ("✨", "**Constelações** são grupos de estrelas que, vistos da Terra, parecem formar desenhos."),
            ("✝️", "O **Cruzeiro do Sul** tem 5 estrelas principais e aparece na **bandeira do Brasil**. Ele ajuda a achar o **sul**."),
            ("🏹", "Outras constelações famosas: **Órion** (as **Três Marias** fazem parte dela) e **Escorpião**."),
        ],
        [
            mc("O que é uma constelação?", ["Um grupo de estrelas que parece formar um desenho", "Um planeta muito grande", "Uma nuvem de chuva"], "Os povos ligavam as estrelas e imaginavam figuras.", "✨"),
            mc("Qual constelação ajuda a encontrar o **sul**?", ["Cruzeiro do Sul", "Escorpião", "Ursa Maior"], "O braço maior da cruz aponta para o sul.", "🧭"),
            mc("As **Três Marias** fazem parte de qual constelação?", ["Órion", "Cruzeiro do Sul", "Escorpião"], "São o **cinturão de Órion**.", "🏹"),
            mc("Onde aparece o Cruzeiro do Sul?", ["Na bandeira do Brasil", "Na bandeira dos EUA", "No mapa da Lua"], "Ele está no círculo azul da bandeira.", "🇧🇷"),
            tf("As estrelas de uma constelação estão todas bem pertinho umas das outras.", False, "Elas só **parecem** próximas vistas da Terra."),
            tf("Durante o dia as estrelas continuam no céu, mas a luz do Sol não deixa vê-las.", True, "O brilho do Sol esconde as outras estrelas."),
            fill("O Sol é uma ___.", ["estrela", "constelação", "lua"], "O Sol é a estrela mais próxima da Terra."),
        ],
    ),
    "a5-b4-ciencias-u1-m2": missao(
        [
            ("🌑", "A Lua **não tem luz própria**: ela reflete a luz do Sol."),
            ("🌓", "Conforme a Lua gira ao redor da Terra, vemos partes iluminadas diferentes: são as **fases da Lua**."),
            ("🔄", "A ordem é: **nova → crescente → cheia → minguante**. O ciclo dura cerca de **29 dias e meio**."),
        ],
        [
            ordem("Coloque as fases da Lua na ordem", ["🌑 Nova", "🌓 Quarto crescente", "🌕 Cheia", "🌗 Quarto minguante"], "Nova, crescente, cheia e minguante."),
            mc("Em qual fase vemos a Lua **toda iluminada**?", ["Cheia", "Nova", "Minguante"], "Lua cheia = disco inteiro brilhante.", "🌕"),
            mc("Em qual fase **quase não vemos** a Lua?", ["Nova", "Cheia", "Crescente"], "Na Lua nova, o lado iluminado fica virado para longe da Terra.", "🌑"),
            mc("Depois da Lua cheia vem a...", ["minguante", "nova", "crescente"], "Depois da cheia, a parte iluminada vai **diminuindo**.", "🌗"),
            mc("Por que a Lua brilha?", ["Reflete a luz do Sol", "Tem fogo dentro", "Tem lâmpadas"], "Ela é como um espelho da luz do Sol.", "☀️"),
            mc("Quanto tempo dura, mais ou menos, um ciclo completo das fases?", ["Cerca de um mês", "Um dia", "Um ano"], "Cerca de **29 dias e meio**.", "🗓️"),
            tf("A **rotação** da Terra, girando em torno de si mesma, causa o dia e a noite.", True, "Uma volta leva cerca de **24 horas**."),
        ],
    ),
    "a5-b4-ciencias-u1-m3": missao(
        [
            ("🔭", "**Lunetas** e **telescópios** usam lentes para ver coisas distantes, como a Lua e os planetas."),
            ("🪞", "O **periscópio** usa **dois espelhos** inclinados para ver por cima de obstáculos. Submarinos usam!"),
            ("↘️", "A luz bate no primeiro espelho, é **refletida** para o segundo e chega ao seu olho."),
            desafio("com um adulto, monte um periscópio com uma caixa comprida (de leite ou de pasta de dente), dois espelhinhos e fita. Use para espiar por cima de um muro ou sofá!"),
        ],
        [
            mc("Para que serve um periscópio?", ["Ver por cima de obstáculos", "Ouvir sons distantes", "Medir a temperatura"], "Os espelhos desviam a luz para o seu olho.", "🪞"),
            mc("Quantos espelhos tem um periscópio simples?", ["2", "1", "10"], "Um em cima e um embaixo.", "🔢"),
            mc("Como os espelhos ficam no periscópio?", ["Inclinados, um de frente para o outro", "Deitados no chão", "Virados para fora da caixa"], "Inclinados, para refletir a luz de um para o outro.", "📐"),
            mc("Qual instrumento usamos para observar as crateras da Lua?", ["Luneta ou telescópio", "Periscópio", "Termômetro"], "Lentes aumentam o que está longe.", "🔭"),
            tf("O espelho reflete a luz.", True, "Por isso vemos nossa imagem nele."),
            fill("O periscópio funciona porque os espelhos ___ a luz.", ["refletem", "apagam", "esquentam"], "A luz é **refletida** de um espelho para o outro."),
        ],
    ),
    # ------------------------------------------------------------ Ciências Humanas (História)
    "a5-b4-humanas-u1-m1": missao(
        [
            ("🏛️", "**Patrimônio** é aquilo que um povo valoriza e quer preservar para o futuro."),
            ("🧱", "**Material**: lugares e construções, como o **Cristo Redentor** e as **Pirâmides do Egito**."),
            ("🥁", "**Imaterial**: saberes e festas, como o **frevo**, a **capoeira** e o **samba de roda**."),
        ],
        [
            separar("Patrimônio material ou imaterial?", ["Material", "Imaterial"],
                    [("Cristo Redentor", 0), ("centro histórico de Ouro Preto", 0), ("Pirâmides do Egito", 0), ("capoeira", 1), ("frevo", 1), ("samba de roda", 1)],
                    "Material se pode tocar. Imaterial são saberes, festas e tradições."),
            mc("Em qual cidade fica o **Cristo Redentor**?", ["Rio de Janeiro", "Salvador", "Manaus"], "Ele fica no morro do Corcovado.", "🗽"),
            mc("O **frevo** é um patrimônio imaterial de qual estado?", ["Pernambuco", "Rio Grande do Sul", "Amazonas"], "O frevo nasceu em **Recife**, Pernambuco.", "☂️"),
            ligar([("Pirâmides de Gizé", "Egito"), ("Muralha da China", "China"), ("Machu Picchu", "Peru"), ("Coliseu", "Itália")], "Ligue o patrimônio ao país"),
            mc("Por que preservar patrimônios?", ["Para guardar a história e a cultura de um povo", "Para derrubar depois", "Porque são novos"], "Eles contam quem somos.", "📜"),
            tf("Uma receita tradicional pode ser patrimônio imaterial.", True, "Saberes e modos de fazer também são patrimônio."),
        ],
    ),
    "a5-b4-humanas-u1-m2": missao(
        [
            ("📰", "Sobre um mesmo assunto, as pessoas podem ter **opiniões diferentes**."),
            ("⚖️", "**Fato** é o que aconteceu e pode ser comprovado. **Opinião** é o que alguém pensa."),
            ("🤔", "Exemplo: **A prefeitura vai fechar a rua aos domingos para lazer.** Um morador acha ótimo; um comerciante teme perder clientes."),
        ],
        [
            separar("Fato ou opinião?", ["Fato", "Opinião"],
                    [("A rua será fechada aos domingos.", 0), ("O parque tem 50 árvores.", 0), ("Ontem choveu na cidade.", 0), ("Fechar a rua é a melhor ideia do mundo!", 1), ("O parque é o lugar mais bonito.", 1)],
                    "Fato se comprova. Opinião é o que alguém pensa."),
            mc("Por que o comerciante pode ser **contra** fechar a rua?", ["Teme perder clientes de carro", "Não gosta de domingo", "Quer mais carros na calçada"], "Cada pessoa vê o tema pelo seu ponto de vista.", "🏪"),
            mc("Por que um morador pode ser **a favor**?", ["Ganha um espaço para lazer e brincadeiras", "Quer mais trânsito", "Quer menos parques"], "Ele vê benefícios para a família.", "🚲"),
            mc("Para formar a nossa opinião sobre uma notícia, é bom...", ["ouvir os dois lados", "ler só o título", "acreditar em tudo"], "Conhecer pontos de vista diferentes ajuda a pensar.", "👂"),
            tf("Respeitar quem pensa diferente faz parte da vida em sociedade.", True, "Podemos discordar com respeito."),
            fill("A frase **Eu acho que...** geralmente mostra uma ___.", ["opinião", "fato", "data"], "**Eu acho** = opinião."),
        ],
    ),
    "a5-b4-humanas-u1-m3": missao(
        [
            ("🎥", "Hoje você é **guia turístico** da sua cidade!"),
            ("🏛️", "Escolha um **patrimônio** da cidade: uma igreja antiga, uma praça, uma festa, um prato típico."),
            ("🗣️", "Conte: **o que é**, **onde fica**, **por que é importante** e **uma curiosidade**."),
            desafio("grave com um adulto um vídeo curto apresentando um patrimônio da sua cidade, como um guia turístico."),
        ],
        [
            ordem("Organize a apresentação do guia", ["Cumprimentar o público", "Dizer o nome do patrimônio", "Contar onde fica e por que é importante", "Contar uma curiosidade", "Despedir-se"], "Começo, meio e fim."),
            mc("O que um bom guia turístico faz?", ["Fala com clareza e conta a história do lugar", "Fala de costas e baixinho", "Inventa coisas sem pesquisar"], "Pesquisar e falar bem é o segredo.", "🎤"),
            mc("Onde pesquisar sobre um patrimônio da cidade?", ["Em livros, sites oficiais e com moradores antigos", "Só na imaginação", "Em jogos de videogame"], "Use **fontes confiáveis**.", "🔎"),
            tf("Uma festa tradicional da cidade pode ser apresentada como patrimônio.", True, "Festas são patrimônio **imaterial**."),
            fill("Quem mostra os lugares e conta a história deles aos visitantes é o ___ turístico.", ["guia", "carteiro", "goleiro"], "O **guia** turístico."),
        ],
    ),
    # ------------------------------------------------------------ Ciências Humanas (Geografia)
    "a5-b4-humanas-u2-m1": missao(
        [
            ("🛰️", "**Satélites** tiram fotos da Terra lá do espaço."),
            ("🔍", "Comparando imagens de **épocas diferentes**, vemos como os lugares **mudaram**."),
            ("🌳", "Exemplo: em 2000, uma área era **floresta verde**; em 2020, virou **pasto** e **estrada**."),
        ],
        [
            ligar([("verde-escuro na imagem", "floresta"), ("azul", "rio ou lago"), ("cinza com linhas retas", "cidade"), ("marrom-claro em quadrados", "plantação ou pasto")],
                  "Ligue a cor da imagem de satélite ao que ela mostra"),
            mc("Em 2000 a imagem mostrava floresta. Em 2020, pasto. O que aconteceu?", ["Desmatamento", "Reflorestamento", "Nada mudou"], "A floresta foi derrubada.", "🪓"),
            mc("A mancha cinza da cidade ficou **maior** de uma imagem para outra. Isso mostra...", ["que a cidade cresceu", "que a cidade sumiu", "que choveu"], "A área urbana se **expandiu**.", "🏙️"),
            mc("Para que servem as imagens de satélite?", ["Acompanhar mudanças no ambiente", "Fazer bolo", "Medir a febre"], "Ajudam a monitorar florestas, rios e cidades.", "🛰️"),
            tf("Imagens de satélite ajudam a fiscalizar queimadas e desmatamento.", True, "O Brasil usa satélites para isso."),
            separar("A mudança na imagem é boa ou ruim para o ambiente?", ["Melhorou", "Piorou"],
                    [("área replantada ficou verde", 0), ("rio voltou a ficar azul e limpo", 0), ("floresta virou área queimada", 1), ("lago diminuiu muito", 1)],
                    "Comparar imagens mostra se o ambiente melhorou ou piorou."),
        ],
    ),
    "a5-b4-humanas-u2-m2": missao(
        [
            ("🏞️", "Um rio **limpo** tem água clara, peixes e plantas nas margens (**mata ciliar**)."),
            ("🏭", "Fontes de poluição: **esgoto sem tratamento**, **lixo**, **produtos químicos** de fábricas e **agrotóxicos**."),
            ("🚰", "O **tratamento de esgoto** e a **mata ciliar** ajudam o rio a ficar saudável."),
        ],
        [
            separar("Polui ou protege o rio?", ["Polui", "Protege"],
                    [("esgoto jogado sem tratamento", 0), ("lixo nas margens", 0), ("óleo de cozinha na pia", 0), ("estação de tratamento de esgoto", 1), ("mata ciliar preservada", 1), ("descartar óleo em ponto de coleta", 1)],
                    "Cuidar do rio é cuidar da água que bebemos."),
            mc("O que é **mata ciliar**?", ["A vegetação nas margens do rio", "Um tipo de peixe", "Uma fábrica"], "Ela protege o rio como os cílios protegem os olhos.", "🌿"),
            mc("Qual é o sinal de um rio **poluído**?", ["Água escura, mau cheiro e peixes mortos", "Água clara e peixes", "Plantas nas margens"], "A poluição tira o oxigênio da água.", "🐟"),
            mc("Onde jogar o óleo de cozinha usado?", ["Num ponto de coleta, dentro de uma garrafa", "Na pia", "No rio"], "1 litro de óleo pode poluir muitos litros de água.", "🫙"),
            tf("Esgoto tratado polui menos os rios.", True, "O tratamento limpa a água antes de devolvê-la ao rio."),
            fill("A vegetação que protege as margens dos rios é a mata ___.", ["ciliar", "atlântica", "fechada"], "**Mata ciliar**."),
        ],
    ),
    "a5-b4-humanas-u2-m3": missao(
        [
            ("✉️", "Cidadãos podem **participar** das decisões da cidade, por exemplo escrevendo à **prefeitura**."),
            ("📝", "Uma boa carta de proposta tem: **o problema**, **onde acontece**, **por que é importante** e **uma sugestão de solução**."),
            ("🙏", "Use linguagem **educada** e **formal**: **Prezado(a) prefeito(a),**... **Atenciosamente,**"),
            desafio("com um adulto, escolha um problema ambiental do bairro (lixo, falta de árvores, esgoto) e escreva uma carta à prefeitura com uma proposta."),
        ],
        [
            ordem("Organize a carta à prefeitura", ["Local e data", "Prezado(a) prefeito(a),", "Apresentar o problema e onde acontece", "Propor uma solução", "Atenciosamente, e assinatura"], "Estrutura de uma carta formal."),
            mc("Qual é o melhor começo para a carta?", ["Prezado prefeito,", "E aí, prefeito!", "Oi, beleza?"], "Carta à autoridade usa linguagem **formal**.", "✉️"),
            mc("Qual proposta é mais clara?", ["Instalar lixeiras na praça Central e fazer mutirão de limpeza", "Resolver tudo", "Fazer alguma coisa"], "Uma boa proposta é **específica**.", "💡"),
            mc("Por que escrever à prefeitura?", ["Para participar e ajudar a melhorar a cidade", "Para reclamar sem sugerir nada", "Para pedir um presente"], "É um exercício de **cidadania**.", "🏛️"),
            tf("Crianças também podem dar ideias para melhorar o bairro.", True, "Todo cidadão pode participar."),
            fill("Uma despedida formal para a carta é ___.", ["Atenciosamente", "Tchauzinho", "Fui!"], "**Atenciosamente** é formal."),
        ],
    ),
    # ------------------------------------------------------------ Ética
    "a5-b4-etica-u1-m1": missao(
        [
            ("🌟", "Um **sonho** é algo grande que queremos para a vida. Uma **meta** é um objetivo concreto."),
            ("🪜", "Para chegar lá, dividimos em **pequenos passos**."),
            ("🎯", "Exemplo: **sonho** de ser cientista → **meta**: ir bem em Ciências → **passos**: estudar todo dia, ler sobre o tema, fazer experimentos."),
        ],
        [
            ordem("Meta: ler um livro de 100 páginas em um mês. Ordene os passos", ["Escolher o livro", "Combinar quantas páginas ler por dia", "Ler um pouco todo dia", "Terminar o livro e contar o que achou"], "Planejar e fazer um pouco de cada vez."),
            ordem("Meta: aprender a andar de skate. Ordene os passos", ["Conseguir um skate e proteção", "Aprender a ficar em pé parado", "Dar os primeiros empurrões", "Treinar curvas"], "Do mais simples ao mais difícil."),
            mc("Qual é uma meta **clara**?", ["Ler 2 livros nas férias", "Ser bom", "Fazer coisas"], "Uma meta clara diz **o quê** e **quando**.", "🎯"),
            mc("Não conseguiu cumprir um passo da meta. O que fazer?", ["Rever o plano e tentar de novo", "Desistir para sempre", "Culpar os outros"], "Errar faz parte de aprender.", "🔁"),
            tf("Grandes sonhos podem ser alcançados com pequenos passos.", True, "Passo a passo se vai longe!"),
            fill("Um objetivo concreto que ajuda a chegar ao sonho é uma ___.", ["meta", "desculpa", "brincadeira"], "**Meta** é um objetivo concreto."),
        ],
    ),
    "a5-b4-etica-u1-m2": missao(
        [
            ("🌍", "**Sustentabilidade** é usar os recursos hoje sem faltar para o futuro."),
            ("♻️", "Os **3 Rs**: **Reduzir** (consumir menos), **Reutilizar** (usar de novo) e **Reciclar** (transformar)."),
            ("🚲", "Escolhas do dia a dia fazem diferença: ir de bicicleta, levar garrafinha, evitar desperdício."),
        ],
        [
            mc("Qual opção **polui menos** para ir a uma padaria perto de casa?", ["Ir a pé ou de bicicleta", "Ir de carro sozinho", "Pedir para um caminhão levar"], "Sem queimar combustível!", "🚲"),
            mc("Qual escolha gera **menos lixo**?", ["Levar uma garrafinha reutilizável", "Comprar garrafinha descartável todo dia", "Usar 3 copos plásticos por dia"], "Reutilizar diminui o lixo.", "🧴"),
            separar("Qual R é esse?", ["Reduzir", "Reutilizar", "Reciclar"],
                    [("comprar só o necessário", 0), ("banho mais curto", 0), ("usar pote de vidro como porta-lápis", 1), ("doar roupas", 1), ("separar latas para a coleta", 2), ("transformar garrafas PET em tecido", 2)],
                    "Reduzir é consumir menos; reutilizar é usar de novo; reciclar é transformar."),
            mc("Para as compras do mercado, o mais sustentável é...", ["Levar uma sacola retornável", "Pedir 10 sacolinhas plásticas", "Comprar sacola nova toda vez"], "A sacola retornável dura muito tempo.", "🛍️"),
            tf("Comprar produtos com menos embalagem ajuda o planeta.", True, "Menos embalagem = menos lixo."),
        ],
    ),
    "a5-b4-etica-u1-m3": missao(
        [
            ("💌", "Que tal escrever uma **carta para você mesmo no futuro**?"),
            ("🔮", "Conte **quem você é hoje**, do que gosta, seus **sonhos** e o que espera do **6º ano**."),
            ("📦", "Guarde a carta numa **cápsula do tempo** e abra no fim do 6º ano!"),
            desafio("escreva uma carta para o você do 6º ano, guarde num envelope fechado e combine com um adulto a data para abrir."),
        ],
        [
            mc("O que é bom escrever na carta para o futuro?", ["Meus gostos, sonhos e metas de hoje", "A senha do celular", "Só a data"], "Assim você vai ver o quanto mudou e cresceu.", "💭"),
            mc("Quando abrir a cápsula do tempo?", ["Na data combinada no futuro", "No dia seguinte", "Nunca"], "A graça é esperar!", "⏳"),
            mc("No 6º ano, muita coisa muda. Uma boa atitude é...", ["Estar aberto a aprender coisas novas", "Ter medo de tudo", "Não falar com ninguém"], "Mudanças trazem novas oportunidades.", "🚀"),
            ordem("Organize a carta", ["Data de hoje", "Querido eu do futuro,", "Quem sou eu hoje", "Meus sonhos e metas", "Assinatura"], "Data, saudação, conteúdo e assinatura."),
            tf("Refletir sobre os nossos sonhos ajuda a planejar o futuro.", True, "Pensar no futuro ajuda a fazer boas escolhas hoje."),
        ],
    ),
    # ------------------------------------------------------------ Inglês
    "a5-b4-ingles-u1-m1": missao(
        [
            ("📖", "**Story time!** Leia a história em inglês."),
            ("🐶", "**Max is a small brown dog. He lives in London with a girl called Emma. One day, Max runs to the park and finds a red ball. He is very happy!**"),
            ("💡", "Palavras úteis: **small** = pequeno · **brown** = marrom · **lives** = mora · **finds** = encontra"),
        ],
        [
            mc("Who is Max? (Quem é Max?)", ["A dog", "A cat", "A girl"], "**Max is a small brown dog.**", "🐶"),
            mc("Where does Max live? (Onde ele mora?)", ["London", "New York", "Paris"], "**He lives in London.**", "🇬🇧"),
            mc("What color is Max?", ["Brown", "Red", "Black"], "**brown** = marrom.", "🟫"),
            mc("What does Max find in the park?", ["A red ball", "A blue hat", "A big cat"], "**finds a red ball** = encontra uma bola vermelha.", "🔴"),
            mc("How does Max feel?", ["Happy", "Sad", "Angry"], "**He is very happy!**", "😀"),
            mc("Who is Emma?", ["The girl who lives with Max", "A dog in the park", "Max's ball"], "**a girl called Emma** = uma menina chamada Emma.", "👧"),
            tf("**small** quer dizer pequeno.", True, "small = pequeno. big = grande."),
        ],
    ),
    "a5-b4-ingles-u1-m2": missao(
        [
            ("🎬", "Toda história tem uma **ordem** de cenas: **first** (primeiro), **then** (depois), **finally** (por fim)."),
            ("🐶", "Lembra do Max? **First**, he runs to the park. **Then**, he finds a ball. **Finally**, he goes home with Emma."),
            ("🔢", "Palavras de ordem ajudam a entender a história."),
        ],
        [
            ordem("Put the story in order (coloque a história na ordem)", ["Max runs to the park.", "Max finds a red ball.", "Max plays with the ball.", "Max goes home with Emma."], "First, then, then, finally."),
            ordem("Put Emma's morning in order", ["Emma wakes up.", "She brushes her teeth.", "She eats breakfast.", "She goes to school."], "Acordar, escovar os dentes, tomar café e ir à escola."),
            mc("O que quer dizer **first**?", ["Primeiro", "Por fim", "Depois"], "first = **primeiro**.", "1️⃣"),
            mc("O que quer dizer **finally**?", ["Por fim", "Primeiro", "Amanhã"], "finally = **por fim, finalmente**.", "🏁"),
            ligar([("first", "primeiro"), ("then", "depois"), ("finally", "por fim"), ("the end", "fim")], "Ligue a palavra ao significado"),
            fill("___, Max goes home. (Por fim)", ["Finally", "First", "Then"], "Por fim = **Finally**."),
        ],
    ),
    "a5-b4-ingles-u1-m3": missao(
        [
            ("🎤", "Agora leia **em voz alta**!"),
            ("📖", "**Max is a small brown dog. He lives in London. He likes to play in the park.**"),
            ("🗣️", "Dicas de pronúncia: **dog** (dóg), **brown** (bráun), **London** (lândon), **park** (párk)."),
            desafio("leia o trecho do Max em voz alta, devagar e com capricho, e peça para um adulto gravar."),
        ],
        [
            mc("Leia em voz alta: **He likes to play.** O que significa?", ["Ele gosta de brincar.", "Ele gosta de dormir.", "Ele não gosta de brincar."], "likes = gosta · play = brincar.", "⚽"),
            mc("Como se pronuncia **brown**, mais ou menos?", ["bráun", "brôu-ne", "brunô"], "brown soa como **bráun**.", "🗣️"),
            mc("Ao ler em voz alta, o que ajuda?", ["Ler devagar e fazer pausa no ponto final", "Ler o mais rápido possível", "Pular as palavras difíceis"], "Pausas deixam a leitura clara.", "🎤"),
            ligar([("dog", "cachorro"), ("park", "parque"), ("small", "pequeno"), ("play", "brincar")], "Ligue as palavras da história ao significado"),
            tf("**He lives in London** quer dizer Ele mora em Londres.", True, "lives = mora."),
        ],
    ),
}
