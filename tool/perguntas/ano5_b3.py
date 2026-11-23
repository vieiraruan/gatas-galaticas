"""5º ano · 3º bimestre."""
from base import desafio, fill, ligar, mc, missao, ordem, separar, tf

MISSOES = {
    # ------------------------------------------------------------ Português
    "a5-b3-portugues-u1-m1": missao(
        [
            ("⏳", "Os **verbos** mostram **quando** a ação acontece."),
            ("📅", "**Passado**: ontem eu **joguei**. **Presente**: hoje eu **jogo**. **Futuro**: amanhã eu **jogarei** (ou **vou jogar**)."),
            ("🤝", "O verbo concorda com o sujeito: **eu canto**, **nós cantamos**, **eles cantam**."),
        ],
        [
            separar("Em que tempo está o verbo?", ["Passado", "Presente", "Futuro"],
                    [("Ontem choveu muito.", 0), ("Eu comi o bolo.", 0), ("Hoje estudo inglês.", 1), ("Ela dança agora.", 1), ("Amanhã viajaremos.", 2), ("Vou visitar a vovó.", 2)],
                    "Ontem, hoje, amanhã."),
            fill("Amanhã nós ___ ao museu.", ["iremos", "fomos", "íamos"], "**Amanhã** → futuro."),
            fill("Ontem eles ___ futebol.", ["jogaram", "jogam", "jogarão"], "**Ontem** → passado, plural."),
            mc("Qual frase está no **presente**?", ["O menino lê um gibi.", "O menino leu um gibi.", "O menino lerá um gibi."], "**lê** = agora.", "📖"),
            mc("Qual frase tem **concordância** certa?", ["Os alunos fizeram a tarefa.", "Os alunos fez a tarefa.", "Os aluno fizeram a tarefa."], "**alunos** → **fizeram**.", "✏️"),
            mc("Passe para o futuro: **Eu estudo.**", ["Eu estudarei.", "Eu estudei.", "Eu estudava."], "estudar → **estudarei**.", "🔮"),
            tf("Em **Nós cantamos ontem**, o verbo está no passado.", True, "**Ontem** indica passado."),
        ],
    ),
    "a5-b3-portugues-u1-m2": missao(
        [
            ("🔗", "**Conjunções** ligam ideias e mostram a relação entre elas."),
            ("🔄", "**mas** = oposição. **porque** = causa. **quando** = tempo. **se** = condição. **e** = adição."),
            ("📝", "**Quis brincar, mas choveu.** **Fiquei feliz porque ganhei.** **Se chover, levo guarda-chuva.**"),
        ],
        [
            fill("Estudei muito, ___ a prova estava difícil.", ["mas", "porque", "se"], "Ideia de **oposição**."),
            fill("Fui dormir cedo ___ estava cansado.", ["porque", "mas", "se"], "Ideia de **causa**."),
            fill("___ fizer sol, vamos à praia.", ["Se", "Mas", "Porque"], "Ideia de **condição**."),
            fill("Eu saí ___ o sinal tocou.", ["quando", "mas", "se"], "Ideia de **tempo**."),
            ligar([("mas", "oposição"), ("porque", "causa"), ("se", "condição"), ("quando", "tempo")], "Ligue a conjunção à ideia"),
            mc("Em **Corri muito e cheguei a tempo**, o **e** indica...", ["adição", "oposição", "condição"], "Soma duas ações.", "➕"),
            tf("A conjunção **mas** une ideias que se opõem.", True, "Queria ir, **mas** não pude."),
        ],
    ),
    "a5-b3-portugues-u1-m3": missao(
        [
            ("🌳", "**Primitiva**: palavra que dá origem a outras (**pedra**)."),
            ("🌿", "**Derivada**: formada a partir da primitiva com prefixo ou sufixo (**pedreiro**, **pedregulho**)."),
            ("🧩", "**Composta**: formada por duas palavras juntas (**girassol**, **guarda-chuva**, **passatempo**)."),
        ],
        [
            separar("Primitiva, derivada ou composta?", ["Primitiva", "Derivada", "Composta"],
                    [("flor", 0), ("mar", 0), ("floricultura", 1), ("marinheiro", 1), ("beija-flor", 2), ("guarda-roupa", 2)],
                    "Raiz, raiz + pedaço, ou duas palavras."),
            mc("**Girassol** é formado por...", ["gira + sol", "giras + sol", "girar + só"], "É uma palavra **composta**.", "🌻"),
            mc("Qual palavra é **derivada** de **livro**?", ["livraria", "lírio", "livre"], "livr(o) + **-aria**.", "📚"),
            mc("Qual é a palavra **primitiva** de **dentista**?", ["dente", "dentadura", "tista"], "dente → dent**ista**.", "🦷"),
            ligar([("pão", "padaria"), ("ferro", "ferreiro"), ("jornal", "jornalista"), ("leite", "leiteria")], "Ligue a primitiva à derivada"),
            tf("**Guarda-chuva** é uma palavra composta.", True, "guarda + chuva."),
            mc("Qual grupo forma uma **família de palavras**?", ["terra, terreno, enterrar", "terra, mar, sol", "casa, pato, bola"], "Todas vêm de **terra**.", "🌍"),
        ],
    ),
    # ------------------------------------------------------------ Matemática
    "a5-b3-matematica-u1-m1": missao(
        [
            ("⚖️", "Uma **igualdade** é como uma **balança equilibrada**: os dois lados valem o mesmo."),
            ("❓", "Em **? + 5 = 12**, o número que falta é **7**, porque 7 + 5 = 12."),
            ("🔁", "Se somarmos ou tirarmos o **mesmo valor** dos dois lados, a balança continua equilibrada."),
        ],
        [
            mc("**? + 8 = 15**. Quanto vale o ?", ["7", "23", "8"], "15 − 8 = **7**.", "⚖️"),
            mc("**20 − ? = 12**. Quanto vale o ?", ["8", "32", "12"], "20 − 8 = 12.", "🧮"),
            mc("**3 × ? = 18**. Quanto vale o ?", ["6", "15", "21"], "18 ÷ 3 = **6**.", "✖️"),
            mc("**? ÷ 4 = 5**. Quanto vale o ?", ["20", "9", "1"], "5 × 4 = **20**.", "➗"),
            mc("Uma balança tem **2 caixas iguais** de um lado e **10 kg** do outro. Cada caixa pesa...", ["5 kg", "10 kg", "20 kg"], "10 ÷ 2 = **5**.", "📦"),
            mc("**7 + 3 = 4 + ?**", ["6", "10", "3"], "Os dois lados valem 10.", "🟰"),
            tf("Se **10 = 10**, então **10 + 2 = 10 + 2**.", True, "Mesma operação dos dois lados mantém o equilíbrio."),
        ],
    ),
    "a5-b3-matematica-u1-m2": missao(
        [
            ("🍰", "Uma receita de bolo para **4 pessoas** usa **2 ovos** e **1 xícara de leite**."),
            ("✖️", "Para **8 pessoas** (o dobro), dobramos tudo: **4 ovos** e **2 xícaras**. Isso é **proporcionalidade**."),
            ("🍬", "**Partilha desigual**: 9 balas, e Ana ganha o **dobro** de Bia. Bia fica com 1 parte e Ana com 2: 3 partes de 3 balas. Bia **3**, Ana **6**."),
        ],
        [
            mc("Receita para 4 pessoas usa **2 ovos**. Para **8 pessoas**, quantos ovos?", ["4", "6", "2"], "O dobro de pessoas, o dobro de ovos.", "🥚"),
            mc("Receita para 2 pessoas usa **150 g** de farinha. Para **6 pessoas**?", ["450 g", "300 g", "600 g"], "O triplo: 150 × 3.", "🌾"),
            mc("Receita para 10 pessoas usa **4 copos** de suco. Para **5 pessoas**?", ["2 copos", "8 copos", "1 copo"], "Metade das pessoas, metade do suco.", "🧃"),
            mc("**1 pacote** tem **12** biscoitos. **3 pacotes** têm...", ["36", "15", "24"], "12 × 3.", "🍪"),
            mc("12 balas divididas entre Ana e Bia. Ana ganha o **dobro** de Bia. Quanto ganha Bia?", ["4", "6", "8"], "Bia 4 + Ana 8 = 12.", "🍬"),
            mc("Andando sempre na mesma velocidade, em **1 hora** um ônibus anda **60 km**. Em **3 horas**?", ["180 km", "63 km", "120 km"], "60 × 3.", "🚌"),
            tf("Se uma receita serve 3 pessoas, dobrar todos os ingredientes serve 6.", True, "Proporcionalidade!"),
        ],
    ),
    "a5-b3-matematica-u1-m3": missao(
        [
            ("🥪", "Na lanchonete há **3 sanduíches** e **2 sucos**. Quantos lanches diferentes dá para montar?"),
            ("✖️", "Cada sanduíche combina com cada suco: **3 × 2 = 6** combinações."),
            ("🌳", "Esse é o **princípio multiplicativo**: multiplique as opções de cada escolha."),
        ],
        [
            mc("**3** camisetas e **2** bermudas. Quantas roupas diferentes?", ["6", "5", "9"], "3 × 2 = **6**.", "👕"),
            mc("**4** sabores de sorvete e **2** tipos de casquinha. Quantas combinações?", ["8", "6", "16"], "4 × 2 = **8**.", "🍦"),
            mc("**2** sanduíches, **3** sucos e **2** sobremesas. Quantos lanches completos?", ["12", "7", "6"], "2 × 3 × 2 = **12**.", "🥪"),
            mc("Com os algarismos **1, 2 e 3**, sem repetir, quantos números de 2 algarismos?", ["6", "3", "9"], "12, 13, 21, 23, 31, 32.", "🔢"),
            mc("**5** pães e **1** recheio. Quantos sanduíches diferentes?", ["5", "6", "1"], "5 × 1 = **5**.", "🍞"),
            mc("Em quantas ordens diferentes **3 amigos** podem formar uma fila?", ["6", "3", "9"], "3 × 2 × 1 = **6**.", "🧍"),
            tf("Com 2 calças e 4 camisas dá para montar 8 roupas.", True, "2 × 4 = 8."),
        ],
    ),
    "a5-b3-matematica-u2-m1": missao(
        [
            ("🗺️", "O **plano cartesiano** tem duas retas: a **horizontal** e a **vertical**."),
            ("📍", "Um ponto é dado por um **par ordenado (x, y)**: primeiro andamos na **horizontal**, depois na **vertical**."),
            ("🚢", "O ponto **(3, 2)**: anda 3 para a direita e sobe 2. Igual à batalha naval!"),
        ],
        [
            mc("No ponto **(4, 1)**, quantos passos andamos na **horizontal**?", ["4", "1", "5"], "O primeiro número é **x** (horizontal).", "➡️"),
            mc("No ponto **(2, 5)**, quantos passos subimos?", ["5", "2", "7"], "O segundo número é **y** (vertical).", "⬆️"),
            mc("O ponto que fica na **origem** é...", ["(0, 0)", "(1, 1)", "(0, 1)"], "Onde as retas se cruzam.", "🎯"),
            mc("**(3, 2)** e **(2, 3)** são o mesmo ponto?", ["Não, a ordem importa", "Sim, sempre", "Só às vezes"], "Par **ordenado**!", "🔀"),
            mc("Um navio está em **(5, 0)**. Ele fica...", ["sobre a reta horizontal", "sobre a reta vertical", "fora do mapa"], "y = 0: não subiu nada.", "🚢"),
            mc("Saindo de **(1, 1)** e andando **2 para a direita**, chego em...", ["(3, 1)", "(1, 3)", "(2, 2)"], "Muda só o **x**: 1 + 2 = 3.", "🧭"),
            tf("No par (x, y), o x indica a posição na horizontal.", True, "Primeiro a horizontal, depois a vertical."),
        ],
    ),
    "a5-b3-matematica-u2-m2": missao(
        [
            ("📦", "A **planificação** é o sólido \"desmontado\" e aberto no papel."),
            ("🧊", "O **cubo** abre em **6 quadrados**. O **cilindro** em **2 círculos e 1 retângulo**. O **cone** em **1 círculo e um setor**."),
            ("🔺", "**Prismas** têm 2 bases iguais. **Pirâmides** têm 1 base e faces triangulares que se encontram num ponto."),
        ],
        [
            ligar([("cubo", "6 quadrados"), ("cilindro", "2 círculos e 1 retângulo"), ("cone", "1 círculo e 1 setor"), ("pirâmide de base quadrada", "1 quadrado e 4 triângulos")], "Ligue o sólido à planificação"),
            mc("Uma **lata de milho** tem forma de...", ["cilindro", "cone", "cubo"], "Dois círculos e um retângulo enrolado.", "🥫"),
            mc("Uma **casquinha de sorvete** tem forma de...", ["cone", "cilindro", "prisma"], "Ponta + base circular.", "🍦"),
            mc("Quantas faces tem um **cubo**?", ["6", "4", "8"], "Um dado tem 6 lados.", "🎲"),
            separar("Rola ou não rola?", ["Rola", "Não rola"],
                    [("cilindro", 0), ("cone", 0), ("esfera", 0), ("cubo", 1), ("pirâmide", 1), ("prisma", 1)],
                    "Superfícies arredondadas rolam."),
            tf("Uma pirâmide tem faces triangulares que se encontram num ponto (vértice).", True, "Como as pirâmides do Egito."),
            mc("Uma **caixa de sapato** tem forma de...", ["paralelepípedo (prisma)", "cone", "esfera"], "Faces retangulares.", "📦"),
        ],
    ),
    "a5-b3-matematica-u2-m3": missao(
        [
            ("🔍", "**Ampliar** é aumentar uma figura; **reduzir** é diminuir."),
            ("📐", "Numa ampliação correta, os **ângulos continuam iguais** e **todos os lados** crescem na mesma proporção."),
            ("🟦", "Um quadrado de lado 2 ampliado **2 vezes** vira um quadrado de lado **4**."),
        ],
        [
            mc("Um retângulo de **3 × 2** ampliado **2 vezes** fica...", ["6 × 4", "5 × 4", "6 × 2"], "Os dois lados dobram.", "🔍"),
            mc("Um quadrado de lado **8** reduzido à **metade** fica com lado...", ["4", "6", "16"], "8 ÷ 2 = **4**.", "🔎"),
            mc("Ao ampliar uma figura corretamente, os **ângulos**...", ["continuam iguais", "dobram", "somem"], "Só o tamanho muda, a forma não.", "📐"),
            mc("Uma foto de **10 × 15 cm** ampliada **3 vezes** fica...", ["30 × 45 cm", "13 × 18 cm", "30 × 15 cm"], "Multiplica os dois lados por 3.", "🖼️"),
            tf("Se só a largura de uma figura aumenta, ela fica deformada.", True, "Tem que aumentar tudo na mesma proporção."),
            mc("O **mapa** de uma cidade é uma...", ["redução da cidade", "ampliação da cidade", "cópia do mesmo tamanho"], "O mapa é bem menor que a cidade real.", "🗺️"),
        ],
    ),
    # ------------------------------------------------------------ Ciências
    "a5-b3-ciencias-u1-m1": missao(
        [
            ("👄", "A digestão começa na **boca**: os dentes mastigam e a saliva amolece o alimento."),
            ("🫃", "Depois o alimento passa pelo **esôfago**, chega ao **estômago** e vai para o **intestino delgado**, onde os nutrientes são absorvidos."),
            ("🚽", "No **intestino grosso** a água é absorvida e o que sobra vira fezes."),
        ],
        [
            ordem("A viagem do alimento:", ["boca", "esôfago", "estômago", "intestino delgado", "intestino grosso"], "É o **sistema digestório**."),
            mc("Onde a digestão **começa**?", ["na boca", "no estômago", "no intestino"], "Mastigação e saliva!", "👄"),
            mc("Os **nutrientes** passam para o sangue principalmente no...", ["intestino delgado", "esôfago", "nariz"], "Ele é longo e cheio de dobrinhas.", "🩸"),
            mc("O **esôfago** é...", ["o tubo que leva o alimento ao estômago", "um dente", "um órgão da respiração"], "Liga a boca ao estômago.", "🧪"),
            tf("Mastigar bem os alimentos ajuda na digestão.", True, "Pedaços pequenos são digeridos mais fácil."),
            mc("O **estômago** tem um suco que...", ["ajuda a quebrar os alimentos", "faz a gente enxergar", "bombeia sangue"], "O **suco gástrico**.", "🫃"),
        ],
    ),
    "a5-b3-ciencias-u1-m2": missao(
        [
            ("🍽️", "Um **prato equilibrado** tem vários grupos de alimentos."),
            ("🥗", "**Metade do prato**: verduras e legumes. **Um quarto**: arroz, batata ou massa (energia). **Um quarto**: feijão, ovo, carne ou peixe (construção)."),
            ("🍎", "Frutas e água completam. Doces, refrigerantes e frituras só **de vez em quando**."),
            desafio("monte com a família um prato equilibrado no almoço e tire uma foto. Ele tem metade de verduras e legumes?"),
        ],
        [
            separar("Em que grupo fica?", ["Energia", "Construção", "Proteção"],
                    [("arroz", 0), ("pão", 0), ("feijão", 1), ("ovo", 1), ("brócolis", 2), ("laranja", 2)],
                    "Energéticos, construtores e reguladores."),
            mc("Qual prato está mais **equilibrado**?", ["arroz, feijão, salada e frango", "batata frita e refrigerante", "só macarrão"], "Tem todos os grupos.", "🍽️"),
            mc("Alimentos **construtores** (proteínas) ajudam a...", ["formar músculos e crescer", "só dar sono", "estragar os dentes"], "Carne, ovo, feijão, leite.", "💪"),
            mc("Frutas e verduras ajudam a...", ["proteger o corpo com vitaminas", "deixar a gente doente", "tirar a fome para sempre"], "São **reguladores**.", "🥦"),
            mc("Qual bebida é a **melhor** para matar a sede?", ["água", "refrigerante", "suco de caixinha"], "Água é essencial!", "💧"),
            tf("Comer doces todos os dias, em grande quantidade, faz bem à saúde.", False, "Só de vez em quando."),
        ],
    ),
    "a5-b3-ciencias-u1-m3": missao(
        [
            ("🫁", "Os **pulmões** puxam o ar e pegam o **oxigênio**. Soltam o **gás carbônico** quando expiramos."),
            ("❤️", "O **coração** bombeia o **sangue**, que leva oxigênio e nutrientes para o corpo todo pelos **vasos sanguíneos**."),
            ("🏃", "Quando corremos, o corpo precisa de mais oxigênio: respiramos mais rápido e o coração bate mais forte."),
            desafio("coloque a mão no peito e conte os batimentos por 15 segundos. Depois pule por 1 minuto e conte de novo. O que mudou?"),
        ],
        [
            mc("Qual órgão **bombeia o sangue**?", ["coração", "pulmão", "estômago"], "Ele não para nunca!", "❤️"),
            mc("Nos pulmões, o sangue recebe...", ["oxigênio", "comida", "gás carbônico"], "E solta o gás carbônico.", "🫁"),
            mc("Por que o coração bate mais rápido quando corremos?", ["Os músculos precisam de mais oxigênio", "Porque está com medo", "Para fazer barulho"], "Mais sangue = mais oxigênio.", "🏃"),
            ligar([("coração", "bombeia sangue"), ("pulmões", "trocam gases"), ("vasos sanguíneos", "levam o sangue"), ("intestino delgado", "absorve nutrientes")], "Ligue o órgão à função"),
            mc("Ao **expirar** (soltar o ar), eliminamos...", ["gás carbônico", "oxigênio puro", "sangue"], "É o resto da respiração das células.", "💨"),
            tf("Os sistemas digestório, respiratório e circulatório trabalham juntos.", True, "O sangue leva nutrientes e oxigênio."),
        ],
    ),
    # ------------------------------------------------------------ Ciências Humanas (História)
    "a5-b3-humanas-u1-m1": missao(
        [
            ("🎨", "Antes da escrita, os povos faziam **pinturas rupestres** nas cavernas."),
            ("🏺", "Os egípcios criaram os **hieróglifos** (desenhos que eram palavras). Os fenícios criaram um dos primeiros **alfabetos**."),
            ("💻", "Depois vieram o **papel**, a **imprensa** de Gutenberg e, hoje, a **escrita digital**."),
        ],
        [
            ordem("Ordene a história da escrita:", ["pinturas rupestres", "hieróglifos", "alfabeto", "imprensa", "escrita digital"], "Do mais antigo ao mais novo."),
            mc("Os **hieróglifos** foram criados pelos...", ["egípcios", "japoneses", "brasileiros"], "No Antigo Egito.", "🏺"),
            mc("A **imprensa** de Gutenberg permitiu...", ["fazer muitas cópias de livros rápido", "mandar e-mails", "pintar cavernas"], "Antes, os livros eram copiados à mão.", "📚"),
            mc("As **pinturas rupestres** eram feitas em...", ["paredes de cavernas", "papel", "telas de computador"], "Há muitas na Serra da Capivara (PI).", "🖐️"),
            tf("A escrita ajudou a guardar a memória dos povos.", True, "Leis, histórias e contas ficaram registradas."),
            mc("Um exemplo de escrita **digital** é...", ["mensagem no celular", "tábua de argila", "pintura na caverna"], "Escrita em telas.", "📱"),
        ],
    ),
    "a5-b3-humanas-u1-m2": missao(
        [
            ("🗿", "**Monumentos**, **nomes de ruas** e **datas comemorativas** escolhem pessoas e fatos para serem lembrados."),
            ("🤔", "Quem escolhe? Governos, comunidades e grupos. Por isso alguns grupos foram **lembrados** e outros **esquecidos**."),
            ("✊", "Hoje há datas que valorizam histórias antes esquecidas, como o **Dia da Consciência Negra (20/11)** e o **Dia dos Povos Indígenas (19/4)**."),
            desafio("descubra com um adulto quem dá nome à rua da sua casa ou da escola. Por que essa pessoa foi homenageada?"),
        ],
        [
            mc("Um **monumento** serve para...", ["lembrar uma pessoa ou um fato", "enfeitar sem motivo", "atrapalhar o trânsito"], "É um marco da **memória**.", "🗿"),
            ligar([("20 de novembro", "Consciência Negra"), ("19 de abril", "Povos Indígenas"), ("7 de setembro", "Independência"), ("21 de abril", "Tiradentes")], "Ligue a data à homenagem"),
            mc("O **20 de novembro** lembra...", ["Zumbi dos Palmares e a luta contra a escravidão", "o descobrimento", "o Natal"], "Dia da Consciência Negra.", "✊"),
            mc("Por que algumas histórias ficaram **esquecidas** por muito tempo?", ["Quem contava a história escolhia o que lembrar", "Porque não aconteceram", "Porque eram chatas"], "A memória também é uma escolha.", "🤔"),
            tf("Nomes de ruas e praças são formas de homenagem.", True, "Contam quem a cidade quis lembrar."),
            mc("Um **museu** ajuda a...", ["preservar a memória", "esquecer o passado", "vender brinquedos"], "Guarda objetos e histórias.", "🏛️"),
        ],
    ),
    "a5-b3-humanas-u1-m3": missao(
        [
            ("📆", "Povos diferentes criaram **calendários** diferentes para contar o tempo."),
            ("🌙", "O calendário **islâmico** segue a **Lua**. O **chinês** combina Lua e Sol e tem animais para cada ano."),
            ("☀️", "Nosso calendário, o **gregoriano**, segue o **Sol**. Muitos povos indígenas contam o tempo pelas **chuvas, colheitas e estrelas**."),
        ],
        [
            ligar([("calendário gregoriano", "o Sol"), ("calendário islâmico", "a Lua"), ("calendário chinês", "animais do zodíaco"), ("muitos povos indígenas", "chuvas e colheitas")], "Ligue o calendário à forma de contar o tempo"),
            mc("O calendário que usamos no Brasil é o...", ["gregoriano", "maia", "lunar islâmico"], "Criado em 1582.", "📅"),
            mc("Um **ano** no nosso calendário é o tempo que a Terra leva para...", ["dar uma volta ao redor do Sol", "girar em torno de si", "a Lua mudar de fase"], "Cerca de **365 dias**.", "🌍"),
            mc("Um **século** tem...", ["100 anos", "10 anos", "1.000 anos"], "Década = 10, século = 100, milênio = 1.000.", "⏳"),
            ordem("Do menor para o maior período:", ["semana", "mês", "ano", "década", "século"], "Medidas de tempo."),
            tf("Todos os povos do mundo sempre usaram o mesmo calendário.", False, "Cada cultura tem o seu jeito."),
        ],
    ),
    # ------------------------------------------------------------ Ciências Humanas (Geografia)
    "a5-b3-humanas-u2-m1": missao(
        [
            ("🌾", "**Agropecuária** (setor primário): plantar e criar animais, tirar recursos da natureza."),
            ("🏭", "**Indústria** (setor secundário): transformar matérias-primas em produtos."),
            ("🛍️", "**Comércio e serviços** (setor terciário): vender, transportar, ensinar, cuidar da saúde."),
        ],
        [
            separar("Em que setor fica?", ["Agropecuária", "Indústria", "Comércio e serviços"],
                    [("criar gado", 0), ("plantar soja", 0), ("fábrica de sapatos", 1), ("montadora de carros", 1), ("supermercado", 2), ("professora", 2)],
                    "Primário, secundário e terciário."),
            mc("Uma **padaria** que vende pão faz parte do...", ["comércio", "agropecuária", "mineração"], "Ela **vende** produtos.", "🥖"),
            mc("Um **médico** trabalha no setor de...", ["serviços", "indústria", "agropecuária"], "Ele presta um serviço.", "🩺"),
            mc("A fábrica que transforma **algodão** em tecido é...", ["indústria", "comércio", "agropecuária"], "Transforma matéria-prima.", "🧵"),
            ordem("O caminho do suco de laranja:", ["plantar a laranja", "fábrica faz o suco", "mercado vende o suco"], "Agropecuária → indústria → comércio."),
            tf("Os três setores da economia dependem uns dos outros.", True, "Um fornece para o outro."),
        ],
    ),
    "a5-b3-humanas-u2-m2": missao(
        [
            ("⚡", "A energia elétrica é produzida em **usinas**."),
            ("💧", "**Hidrelétrica**: força da água dos rios (como Itaipu). **Eólica**: força do vento. **Solar**: luz do Sol."),
            ("🔥", "**Termelétrica**: queima carvão, petróleo ou gás. **Nuclear**: usa urânio."),
        ],
        [
            ligar([("hidrelétrica", "água"), ("eólica", "vento"), ("solar", "luz do Sol"), ("termelétrica", "queima de combustível")], "Ligue a usina à fonte"),
            mc("A maior parte da energia elétrica do Brasil vem de...", ["hidrelétricas", "usinas nucleares", "pilhas"], "O Brasil tem muitos rios.", "💧"),
            mc("**Itaipu** é uma usina...", ["hidrelétrica", "eólica", "solar"], "No Rio Paraná, entre Brasil e Paraguai.", "🌊"),
            mc("Os **cata-ventos gigantes** do Nordeste produzem energia...", ["eólica", "nuclear", "a carvão"], "O Nordeste tem muito vento.", "🌬️"),
            mc("**Painéis solares** no telhado transformam...", ["luz do Sol em eletricidade", "chuva em gelo", "vento em água"], "Energia solar.", "☀️"),
            tf("Economizar energia elétrica ajuda o meio ambiente.", True, "Menos usinas, menos impacto."),
        ],
    ),
    "a5-b3-humanas-u2-m3": missao(
        [
            ("♻️", "**Fontes renováveis** não acabam ou se renovam rápido: **Sol, vento, água, biomassa** (cana, restos de plantas)."),
            ("⛽", "**Fontes não renováveis** podem acabar e poluem mais: **petróleo, carvão mineral, gás natural, urânio**."),
            ("🌎", "Usar mais fontes renováveis ajuda a diminuir a **poluição** e o **aquecimento global**."),
        ],
        [
            separar("Renovável ou não renovável?", ["Renovável", "Não renovável"],
                    [("Sol", 0), ("vento", 0), ("água dos rios", 0), ("petróleo", 1), ("carvão mineral", 1), ("gás natural", 1)],
                    "Umas se renovam, outras acabam."),
            mc("Por que o **petróleo** é não renovável?", ["Leva milhões de anos para se formar", "Porque é líquido", "Porque é caro"], "Quando acabar, não volta logo.", "🛢️"),
            mc("A gasolina dos carros vem do...", ["petróleo", "vento", "Sol"], "É um derivado do petróleo.", "⛽"),
            mc("O **etanol** (álcool) dos carros no Brasil vem da...", ["cana-de-açúcar", "areia", "água do mar"], "Uma fonte **renovável**!", "🌾"),
            mc("Queimar carvão e petróleo...", ["polui o ar", "limpa o ar", "não muda nada"], "Solta gases poluentes.", "🏭"),
            tf("O vento é uma fonte de energia renovável.", True, "Ele não acaba!"),
        ],
    ),
    # ------------------------------------------------------------ Ética
    "a5-b3-etica-u1-m1": missao(
        [
            ("🚫", "**Preconceito** é julgar alguém antes de conhecer, por cor, origem, religião, corpo, gênero ou deficiência."),
            ("⚠️", "**Discriminação** é tratar a pessoa de forma pior por causa disso."),
            ("⚖️", "No Brasil, **racismo é crime**. Todos merecem respeito."),
        ],
        [
            mc("Um colega diz que outro não pode jogar porque é **menina**. Isso é...", ["preconceito", "uma regra justa", "uma brincadeira legal"], "Todos podem jogar.", "⚽"),
            mc("Rir do cabelo crespo de alguém é...", ["racismo e falta de respeito", "elogio", "normal"], "Cabelo crespo é bonito!", "💇🏾"),
            separar("Discriminação ou respeito?", ["Discriminação", "Respeito"],
                    [("excluir pelo sotaque", 0), ("zombar da religião", 0), ("apelido pela cor da pele", 0), ("ouvir o colega", 1), ("convidar para o grupo", 1), ("aprender sobre outra cultura", 1)],
                    "Diferenças não são defeitos."),
            mc("No Brasil, o **racismo** é...", ["crime previsto em lei", "permitido", "só falta de educação"], "Lei nº 7.716/1989.", "⚖️"),
            tf("Preconceito é julgar alguém sem conhecer.", True, "Pré + conceito: uma ideia antes de conhecer."),
            mc("Uma família acabou de chegar de outro país. O melhor é...", ["acolher e querer conhecer sua cultura", "ignorar", "rir do jeito de falar"], "A diversidade nos enriquece.", "🌍"),
        ],
    ),
    "a5-b3-etica-u1-m2": missao(
        [
            ("🌟", "Muitas **pessoas negras e indígenas** fizeram história no Brasil."),
            ("✊", "**Zumbi** e **Dandara** lideraram Palmares. **Machado de Assis** foi um grande escritor. **Carolina Maria de Jesus** escreveu **Quarto de Despejo**."),
            ("🌿", "**Raoni** defende a Amazônia. **Daniel Munduruku** escreve livros sobre os povos indígenas. **André Rebouças** foi engenheiro e abolicionista."),
        ],
        [
            mc("**Zumbi** e **Dandara** foram líderes do...", ["Quilombo dos Palmares", "Império Romano", "futebol"], "Lutaram pela liberdade.", "✊"),
            mc("**Machado de Assis** é famoso por ser...", ["escritor", "jogador", "cantor de rock"], "Fundou a Academia Brasileira de Letras.", "✍️"),
            mc("O cacique **Raoni** é conhecido por defender...", ["a floresta e os povos indígenas", "os carros", "os shoppings"], "Líder do povo Kayapó.", "🌳"),
            ligar([("Carolina Maria de Jesus", "escritora"), ("Daniel Munduruku", "escritor indígena"), ("André Rebouças", "engenheiro abolicionista"), ("Dandara", "guerreira de Palmares")], "Ligue a pessoa ao que ela fez"),
            tf("Conhecer personalidades negras e indígenas ajuda a valorizar a diversidade.", True, "São parte da nossa história."),
            mc("O livro **Quarto de Despejo** foi escrito por...", ["Carolina Maria de Jesus", "Machado de Assis", "Monteiro Lobato"], "Ela contou sua vida na favela.", "📔"),
        ],
    ),
    "a5-b3-etica-u1-m3": missao(
        [
            ("🦸", "Você viu alguém sofrendo **preconceito**. O que fazer?"),
            ("🤝", "**Fique ao lado** da pessoa, **não ria**, **diga que não está certo** e **conte a um adulto**."),
            ("🎙️", "Ser **aliado** é usar sua voz para defender o respeito."),
            desafio("grave com um adulto um áudio curto contando como você ajudaria um colega que sofreu preconceito."),
        ],
        [
            mc("Um colega é chamado por um apelido racista. Você...", ["apoia o colega e avisa um professor", "ri junto", "finge que não viu"], "Ser aliado faz diferença.", "🦸"),
            mc("O que dizer para quem sofreu preconceito?", ["\"Você não está sozinho. Isso não está certo.\"", "\"Foi só uma brincadeira.\"", "\"Ignora e pronto.\""], "Acolhimento.", "💬"),
            ordem("O que fazer, na ordem:", ["Não rir da situação", "Ficar ao lado da pessoa", "Dizer que aquilo não está certo", "Contar a um adulto"], "Passos de um aliado."),
            separar("Atitude de aliado ou não?", ["Aliado", "Não é aliado"],
                    [("defender com respeito", 0), ("chamar um adulto", 0), ("acolher a vítima", 0), ("filmar e espalhar", 1), ("rir junto", 1), ("aumentar a fofoca", 1)],
                    "Use sua voz para o bem."),
            tf("Contar a um adulto quando alguém sofre preconceito é \"dedurar\" à toa.", False, "É **proteger** quem está sofrendo."),
        ],
    ),
    # ------------------------------------------------------------ Inglês
    "a5-b3-ingles-u1-m1": missao(
        [
            ("🧑", "**Describing people**: **tall** (alto), **short** (baixo), **long hair** (cabelo comprido), **short hair** (cabelo curto)."),
            ("👀", "**blue eyes** (olhos azuis), **brown eyes** (olhos castanhos), **curly hair** (cabelo cacheado), **glasses** (óculos)."),
            ("🔎", "**Guess who!** Leia a descrição e descubra quem é."),
        ],
        [
            mc("**Tall** significa...", ["alto", "baixo", "magro"], "**tall** ≠ **short**.", "📏"),
            mc("**She has long hair.** significa...", ["Ela tem cabelo comprido.", "Ela tem cabelo curto.", "Ela tem olhos azuis."], "**long** = comprido.", "👩"),
            mc("**He has brown eyes.** Os olhos dele são...", ["castanhos", "azuis", "verdes"], "**brown** = marrom/castanho.", "👁️"),
            mc("**Tom is tall and has curly hair and glasses.** Quem é o Tom?", ["um menino alto, de cabelo cacheado e óculos", "um menino baixo e careca", "uma menina de cabelo liso"], "tall + curly hair + glasses.", "🤓"),
            ligar([("tall", "alto"), ("short", "baixo"), ("curly hair", "cabelo cacheado"), ("glasses", "óculos")], "Ligue a palavra à tradução"),
            mc("**Mia has blue eyes and short hair.** Que cor são os olhos de Mia?", ["azuis", "castanhos", "pretos"], "**blue** = azul.", "💙"),
        ],
    ),
    "a5-b3-ingles-u1-m2": missao(
        [
            ("✍️", "Use **He has** (ele tem) e **She has** (ela tem) para descrever."),
            ("🧩", "**She has green eyes.** **He has short black hair.**"),
            ("⚠️", "Para **I, you, we, they** usamos **have**: **I have brown hair.**"),
        ],
        [
            fill("She ___ long hair.", ["has", "have", "is"], "**She** → **has**."),
            fill("I ___ brown eyes.", ["have", "has", "am"], "**I** → **have**."),
            fill("He ___ glasses.", ["has", "have", "are"], "**He** → **has**."),
            ordem("Monte a frase:", ["She", "has", "blue", "eyes"], "She has blue eyes."),
            ordem("Monte a frase:", ["He", "has", "short", "black", "hair"], "Em inglês, a cor vem antes de **hair**."),
            mc("Como se diz **Ele tem cabelo cacheado**?", ["He has curly hair.", "He have curly hair.", "He is hair curly."], "**He has** + descrição.", "🧑‍🦱"),
            tf("Dizemos **They have** e não **They has**.", True, "**They** → **have**."),
        ],
    ),
    "a5-b3-ingles-u1-m3": missao(
        [
            ("👫", "Agora é sua vez: **describe a friend**!"),
            ("📝", "Exemplo: **My friend is Leo. He is tall. He has short brown hair and green eyes.**"),
            ("📸", "Escreva **3 frases** sobre um amigo e mostre a ele!"),
            desafio("escreva 3 frases em inglês descrevendo um amigo, faça um desenho dele e tire uma foto para mostrar."),
        ],
        [
            mc("**My friend is Leo.** significa...", ["Meu amigo é o Leo.", "Meu irmão é o Leo.", "Eu sou o Leo."], "**friend** = amigo.", "👦"),
            mc("Qual frase descreve uma amiga **baixa**?", ["She is short.", "She is tall.", "He is short."], "**She** + **short**.", "👧"),
            mc("Qual frase está **certa**?", ["He has green eyes.", "He have green eyes.", "He green has eyes."], "**He has**.", "💚"),
            ordem("Monte a frase:", ["My", "friend", "has", "long", "hair"], "My friend has long hair."),
            fill("Ana is my friend. ___ has curly hair.", ["She", "He", "They"], "Ana → **She**."),
            tf("**He is tall** descreve a altura da pessoa.", True, "**tall** = alto."),
        ],
    ),
}
