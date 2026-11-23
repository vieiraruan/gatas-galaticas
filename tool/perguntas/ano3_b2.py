"""3º ano · 2º bimestre."""
from base import desafio, fill, ligar, mc, missao, ordem, separar, tf

MISSOES = {
    # ------------------------------------------------------------ Português
    "a3-b2-portugues-u1-m1": missao(
        [
            ("1️⃣", "**Monossílaba**: 1 sílaba (**pé**, **sol**). **Dissílaba**: 2 sílabas (**ca-sa**)."),
            ("3️⃣", "**Trissílaba**: 3 sílabas (**ja-ne-la**). **Polissílaba**: 4 ou mais (**bor-bo-le-ta**)."),
            ("👏", "Bata palmas para contar as sílabas!"),
        ],
        [
            separar("Classifique pelo número de sílabas", ["Monossílaba", "Dissílaba", "Trissílaba", "Polissílaba"],
                    [("mar", 0), ("flor", 0), ("bola", 1), ("livro", 1), ("sapato", 2), ("caneta", 2), ("telefone", 3), ("hipopótamo", 3)],
                    "Conte as sílabas batendo palmas."),
            mc("**ELEFANTE** é...", ["polissílaba", "trissílaba", "dissílaba"], "E-LE-FAN-TE: 4 sílabas.", "🐘"),
            mc("**PÃO** é...", ["monossílaba", "dissílaba", "trissílaba"], "Uma sílaba só.", "🍞"),
            mc("**ESCOLA** é...", ["trissílaba", "dissílaba", "polissílaba"], "ES-CO-LA: 3 sílabas.", "🏫"),
            mc("Qual palavra é **dissílaba**?", ["GATO", "SOL", "MACACO"], "GA-TO: 2 sílabas.", "🐱"),
            tf("**Borboleta** tem 4 sílabas.", True, "BOR-BO-LE-TA."),
        ],
    ),
    "a3-b2-portugues-u1-m2": missao(
        [
            ("💪", "A **sílaba tônica** é a que falamos com **mais força**."),
            ("📣", "Chame a palavra como se estivesse longe: **ca-FÉ!**, **ME-sa!**, **LÂM-pa-da!**"),
            ("🔙", "Contando de trás para frente: **última** (oxítona), **penúltima** (paroxítona), **antepenúltima** (proparoxítona)."),
        ],
        [
            mc("Qual é a sílaba tônica de **CAFÉ**?", ["FÉ", "CA"], "ca-**FÉ**.", "☕"),
            mc("Qual é a sílaba tônica de **MESA**?", ["ME", "SA"], "**ME**-sa.", "🪑"),
            mc("Qual é a sílaba tônica de **LÂMPADA**?", ["LÂM", "PA", "DA"], "**LÂM**-pa-da.", "💡"),
            mc("Qual é a sílaba tônica de **JANELA**?", ["NE", "JA", "LA"], "ja-**NE**-la.", "🪟"),
            mc("Qual é a sílaba tônica de **TATU**?", ["TU", "TA"], "ta-**TU**.", "🐾"),
            separar("Onde está a força?", ["Última sílaba (oxítona)", "Penúltima (paroxítona)", "Antepenúltima (proparoxítona)"],
                    [("sofá", 0), ("jacaré", 0), ("bola", 1), ("menino", 1), ("pássaro", 2), ("música", 2)],
                    "Conte de trás para frente."),
        ],
    ),
    "a3-b2-portugues-u1-m3": missao(
        [
            ("🔍", "Algumas palavras **perderam o acento**! Vamos devolver?"),
            ("☕", "Acento agudo (**´**): som **aberto** — café, sofá, pé. Acento circunflexo (**^**): som **fechado** — vovô, você, ônibus."),
            ("🧩", "Monossílabos tônicos terminados em **a, e, o** levam acento: **pá**, **pé**, **pó**, **já**, **nó**."),
        ],
        [
            mc("Qual está escrita **certa**?", ["café", "cafe", "cafê"], "Som aberto: **café**.", "☕"),
            mc("Qual está escrita **certa**?", ["sofá", "sofa", "sôfa"], "**sofá**.", "🛋️"),
            mc("Qual está escrita **certa**?", ["vovô", "vôvo", "vovo"], "O avô é **vovô**, com som fechado.", "👴"),
            mc("Qual está escrita **certa**?", ["você", "vocé", "voce"], "Som fechado: **você**.", "🫵"),
            mc("Qual está escrita **certa** (a parte do corpo)?", ["pé", "pe", "pê"], "**pé**, som aberto.", "🦶"),
            mc("Qual está escrita **certa**?", ["ônibus", "onibus", "ónibus"], "**ônibus**, com circunflexo.", "🚌"),
            tf("**Vovó** e **vovô** são palavras diferentes.", True, "Vovó (avó) e vovô (avô): o acento muda o sentido!"),
        ],
    ),
    # ------------------------------------------------------------ Matemática
    "a3-b2-matematica-u1-m1": missao(
        [
            ("⚡", "**Cálculo relâmpago**: resolva de cabeça!"),
            ("🧠", "Dica: **38 + 20** → 38 + 2 dezenas = **58**."),
            ("🔟", "Dica: **45 − 9** → 45 − 10 + 1 = **36**."),
        ],
        [
            mc("**38 + 20** = ?", ["58", "40", "318"], "38 + 20 = **58**.", "⚡"),
            mc("**45 − 9** = ?", ["36", "34", "54"], "45 − 10 + 1 = **36**.", "⚡"),
            mc("**50 + 50** = ?", ["100", "55", "1.000"], "5 dezenas + 5 dezenas.", "⚡"),
            mc("**99 + 1** = ?", ["100", "910", "98"], "**100**!", "⚡"),
            mc("**200 + 300** = ?", ["500", "230", "5.000"], "2 centenas + 3 centenas.", "⚡"),
            mc("**70 − 25** = ?", ["45", "55", "35"], "70 − 20 − 5 = **45**.", "⚡"),
            mc("**125 + 75** = ?", ["200", "190", "210"], "125 + 75 = **200**.", "⚡"),
        ],
    ),
    "a3-b2-matematica-u1-m2": missao(
        [
            ("🍉", "Na **feira**, há problemas de **comparar** e de **completar**."),
            ("⚖️", "**Comparar**: Quantos a mais? Quantos a menos? → subtraímos."),
            ("🧩", "**Completar**: Quanto falta para...? → também subtraímos!"),
        ],
        [
            mc("A barraca tem **48 laranjas** e **30 limões**. Quantas laranjas **a mais**?", ["18", "78", "28"], "48 − 30 = **18**.", "🍊"),
            mc("Dona Rosa quer **100 ovos**. Já tem **65**. Quantos **faltam**?", ["35", "45", "165"], "100 − 65 = **35**.", "🥚"),
            mc("Zé vendeu **120 bananas** de manhã e **85** à tarde. Quantas vendeu?", ["205", "35", "195"], "120 + 85 = **205**.", "🍌"),
            mc("A melancia pesa **8 kg** e o melão **3 kg**. Quanto a melancia pesa **a mais**?", ["5 kg", "11 kg", "3 kg"], "8 − 3 = **5 kg**.", "🍉"),
            mc("Uma caixa tinha **250 tomates**. Sobraram **90**. Quantos foram vendidos?", ["160", "340", "150"], "250 − 90 = **160**.", "🍅"),
            tf("**Quanto falta** é uma pergunta que resolvemos com subtração.", True, "O total menos o que já tem."),
        ],
    ),
    "a3-b2-matematica-u1-m3": missao(
        [
            ("🏪", "Você é o **caixa da loja**!"),
            ("🧾", "Some os preços e, se o cliente pagar com mais, calcule o **troco**."),
            ("💵", "**Troco = dinheiro pago − preço total**."),
        ],
        [
            mc("Caderno **R$ 12** + lápis **R$ 3**. Quanto deu?", ["R$ 15", "R$ 9", "R$ 123"], "12 + 3 = **15**.", "🧾"),
            mc("A compra deu **R$ 15**. O cliente pagou com **R$ 20**. Qual o troco?", ["R$ 5", "R$ 35", "R$ 15"], "20 − 15 = **5**.", "💵"),
            mc("Bola **R$ 28**. Pagou com **R$ 50**. Qual o troco?", ["R$ 22", "R$ 78", "R$ 32"], "50 − 28 = **22**.", "⚽"),
            mc("Boneca **R$ 45** + carrinho **R$ 30**. Quanto deu?", ["R$ 75", "R$ 15", "R$ 70"], "45 + 30 = **75**.", "🧸"),
            mc("A compra deu **R$ 75**. Pagou com **R$ 100**. Qual o troco?", ["R$ 25", "R$ 35", "R$ 175"], "100 − 75 = **25**.", "💰"),
            {"tipo": "escolha", "pergunta": "Quanto dinheiro o cliente deu?", "opcoes": ["R$ 35", "R$ 30", "R$ 25"], "correta": 0, "embaralhar": True,
             "visuais": [{"tipo": "dinheiro", "valores": [2000, 1000, 500]}], "explicacao": "20 + 10 + 5 = **35 reais**."},
        ],
    ),
    # ------------------------------------------------------------ Ciências
    "a3-b2-ciencias-u1-m1": missao(
        [
            ("🐶", "Os animais têm o corpo coberto por coisas diferentes."),
            ("🐦", "**Pelos**: mamíferos (cachorro, gato). **Penas**: aves (galinha, papagaio)."),
            ("🐟", "**Escamas**: peixes e répteis (cobra, lagarto). **Pele nua e úmida**: anfíbios (sapo). **Carapaça**: tartaruga."),
        ],
        [
            separar("Pelos, penas ou escamas?", ["Pelos", "Penas", "Escamas"],
                    [("cachorro", 0), ("coelho", 0), ("onça", 0), ("galinha", 1), ("papagaio", 1), ("tubarão", 2), ("cobra", 2), ("lagarto", 2)],
                    "A cobertura do corpo ajuda a classificar."),
            mc("Que animal tem o corpo coberto de **penas**?", ["Pato", "Gato", "Peixe"], "Aves têm **penas**.", "🦆"),
            mc("O **sapo** tem a pele...", ["nua e úmida", "cheia de penas", "coberta de pelos"], "Anfíbios têm pele **úmida**.", "🐸"),
            mc("O que cobre o corpo da **tartaruga**?", ["Uma carapaça (casco)", "Penas", "Pelos"], "A carapaça protege.", "🐢"),
            tf("Todos os mamíferos têm pelos.", True, "Até a baleia tem alguns pelinhos quando nasce!"),
        ],
    ),
    "a3-b2-ciencias-u1-m2": missao(
        [
            ("🦋", "A **borboleta** passa por grandes mudanças: é a **metamorfose**."),
            ("🥚", "**Ovo** → **lagarta** (come muitas folhas) → **pupa** (dentro do casulo/crisálida) → **borboleta**."),
            ("🔄", "A borboleta põe ovos e o **ciclo de vida** recomeça."),
        ],
        [
            ordem("Coloque o ciclo da borboleta na ordem", ["Ovo", "Lagarta", "Pupa (crisálida)", "Borboleta"], "É a metamorfose."),
            ordem("Coloque o ciclo do sapo na ordem", ["Ovo", "Girino", "Girino com patas", "Sapo adulto"], "O sapo também tem metamorfose."),
            mc("O que a **lagarta** faz muito?", ["Come folhas", "Voa longe", "Põe ovos"], "Ela come para crescer.", "🐛"),
            mc("Como se chama a grande mudança da lagarta para borboleta?", ["Metamorfose", "Fotossíntese", "Evaporação"], "**Metamorfose**.", "🦋"),
            ordem("Coloque o ciclo de vida humano na ordem", ["Nascer", "Crescer", "Tornar-se adulto", "Envelhecer"], "Todos os seres vivos têm ciclo de vida."),
            tf("O filhote do sapo se chama girino.", True, "Ele vive na água e respira por brânquias."),
        ],
    ),
    "a3-b2-ciencias-u1-m3": missao(
        [
            ("🐄", "**Herbívoros** comem plantas: vaca, cavalo, coelho."),
            ("🦁", "**Carnívoros** comem outros animais: leão, tubarão, onça."),
            ("🐻", "**Onívoros** comem plantas **e** animais: urso, porco, galinha e nós, humanos!"),
        ],
        [
            separar("O que eles comem?", ["Herbívoro", "Carnívoro", "Onívoro"],
                    [("vaca", 0), ("girafa", 0), ("leão", 1), ("tubarão", 1), ("urso", 2), ("ser humano", 2)],
                    "Plantas, carne ou os dois."),
            mc("O **coelho** come cenoura e capim. Ele é...", ["herbívoro", "carnívoro", "onívoro"], "Só plantas: **herbívoro**.", "🐰"),
            mc("A **onça** caça outros animais. Ela é...", ["carnívora", "herbívora", "onívora"], "Come carne: **carnívora**.", "🐆"),
            mc("O **porco** come de tudo: restos, frutas, insetos. Ele é...", ["onívoro", "herbívoro", "carnívoro"], "Come de tudo: **onívoro**.", "🐷"),
            tf("O ser humano é onívoro.", True, "Comemos vegetais e carne."),
            fill("Animal que come só plantas é ___.", ["herbívoro", "carnívoro", "onívoro"], "**Herbívoro**."),
        ],
    ),
    # ------------------------------------------------------------ Ciências Humanas (História)
    "a3-b2-humanas-u1-m1": missao(
        [
            ("🏛️", "**Patrimônio** é o que um povo valoriza e quer guardar para o futuro."),
            ("⛪", "**Material**: o que podemos tocar — igrejas, museus, monumentos, casarões."),
            ("💃", "**Imaterial**: saberes, festas, danças e músicas — **frevo**, **capoeira**, **samba de roda**, **ofício das baianas de acarajé**."),
        ],
        [
            separar("Material ou imaterial?", ["Material", "Imaterial"],
                    [("igreja antiga", 0), ("museu", 0), ("estátua da praça", 0), ("frevo", 1), ("capoeira", 1), ("samba de roda", 1)],
                    "Material se toca; imaterial se pratica e se aprende."),
            mc("A **capoeira** é um patrimônio...", ["imaterial", "material", "de metal"], "É uma prática cultural.", "🤸"),
            mc("Um **casarão antigo** é um patrimônio...", ["material", "imaterial", "invisível"], "Podemos tocar.", "🏚️"),
            mc("Por que preservar o patrimônio?", ["Para guardar a história e a cultura", "Para derrubar depois", "Não precisa"], "Ele conta quem somos.", "📜"),
            tf("Uma festa tradicional pode ser patrimônio.", True, "É patrimônio **imaterial**."),
        ],
    ),
    "a3-b2-humanas-u1-m2": missao(
        [
            ("🪧", "Muitas ruas têm **nomes de pessoas**: **Rua Santos Dumont**, **Avenida Princesa Isabel**."),
            ("🎖️", "É uma forma de **homenagear** pessoas importantes para a cidade ou o país."),
            ("📅", "Também há ruas com nomes de **datas** (Rua 7 de Setembro) e **lugares**."),
        ],
        [
            mc("Por que uma rua recebe o nome de uma pessoa?", ["Para homenageá-la", "Porque ela mora lá", "Por sorteio"], "É uma **homenagem**.", "🪧"),
            mc("**Santos Dumont** foi um famoso...", ["inventor e aviador brasileiro", "jogador de futebol", "cantor de rock"], "Ele é conhecido como **pai da aviação**.", "✈️"),
            mc("A **Rua 7 de Setembro** homenageia...", ["a Independência do Brasil", "o aniversário do prefeito", "o dia das crianças"], "7 de setembro de 1822.", "🇧🇷"),
            mc("Onde podemos descobrir quem foi a pessoa do nome da rua?", ["Em livros, sites e com moradores antigos", "Em receitas", "No relógio"], "Pesquise em **fontes**!", "🔎"),
            tf("Os nomes das ruas podem contar a história de uma cidade.", True, "Eles guardam memórias."),
        ],
    ),
    "a3-b2-humanas-u1-m3": missao(
        [
            ("📸", "Toda cidade tem **monumentos** e **prédios antigos**."),
            ("🗿", "Pode ser uma **estátua**, uma **igreja**, uma **estação de trem** ou um **casarão**."),
            ("📝", "Ao fotografar, descubra: **o nome**, **quando foi construído** e **por que é importante**."),
            desafio("fotografe com um adulto um monumento ou prédio antigo da sua cidade e descubra o nome e a história dele."),
        ],
        [
            mc("O que é um **monumento**?", ["Uma construção ou estátua que lembra algo importante", "Um tipo de comida", "Uma brincadeira"], "Monumentos guardam **memórias**.", "🗿"),
            mc("Qual informação ajuda a conhecer o patrimônio?", ["Quando e por que foi construído", "A cor do céu no dia", "O preço do ingresso do cinema"], "A **história** dele!", "📝"),
            mc("Como devemos tratar monumentos?", ["Cuidar e não pichar", "Riscar com nosso nome", "Subir e quebrar"], "São de **todos**.", "🤝"),
            tf("Uma estação de trem antiga pode ser patrimônio da cidade.", True, "Ela conta a história dos transportes."),
            fill("Pichar um monumento é ___ o patrimônio.", ["estragar", "cuidar", "proteger"], "Pichar **estraga**."),
        ],
    ),
    # ------------------------------------------------------------ Ciências Humanas (Geografia)
    "a3-b2-humanas-u2-m1": missao(
        [
            ("🏞️", "**Paisagem** é tudo o que vemos num lugar."),
            ("🌳", "**Natural**: quase sem mudança humana — floresta, praia deserta, cachoeira."),
            ("🏙️", "**Modificada** (cultural): o ser humano mudou — cidade, plantação, estrada, ponte."),
        ],
        [
            separar("Paisagem natural ou modificada?", ["Natural", "Modificada"],
                    [("floresta fechada", 0), ("cachoeira na mata", 0), ("deserto", 0), ("cidade com prédios", 1), ("plantação de soja", 1), ("estrada", 1)],
                    "Onde o ser humano mudou, a paisagem é modificada."),
            mc("Uma praia com prédios e calçadão é uma paisagem...", ["modificada", "natural", "invisível"], "Houve construções humanas.", "🏖️"),
            mc("O que mostra que uma paisagem foi **modificada**?", ["Casas, ruas e plantações", "Só árvores nativas", "Só um rio na mata"], "Sinais da ação humana.", "🏘️"),
            tf("Uma plantação é uma paisagem modificada.", True, "O ser humano plantou ali."),
            fill("Tudo o que vemos num lugar é a ___.", ["paisagem", "receita", "música"], "**Paisagem**."),
        ],
    ),
    "a3-b2-humanas-u2-m2": missao(
        [
            ("🌾", "Os alimentos vêm do **campo**."),
            ("🚜", "**Agricultura**: plantar (arroz, feijão, frutas). **Pecuária**: criar animais (vaca, galinha, porco)."),
            ("🌰", "**Extrativismo**: retirar da natureza (castanha, açaí, peixe do rio)."),
        ],
        [
            ligar([("arroz", "agricultura"), ("leite", "pecuária"), ("castanha-do-pará", "extrativismo")], "Ligue o alimento à atividade"),
            ligar([("ovo", "granja"), ("alface", "horta"), ("açaí", "floresta"), ("queijo", "fazenda de gado leiteiro")], "Ligue o alimento ao lugar"),
            mc("O **leite** vem da...", ["pecuária", "mineração", "pesca"], "Criação de vacas.", "🥛"),
            mc("Colher **açaí** na floresta é...", ["extrativismo", "pecuária", "indústria"], "Retirar da natureza.", "🫐"),
            ordem("Do campo à mesa: coloque na ordem", ["Plantar o feijão", "Colher", "Transportar para o mercado", "Cozinhar e comer"], "O caminho do alimento."),
        ],
    ),
    "a3-b2-humanas-u2-m3": missao(
        [
            ("🌳", "As paisagens **mudam com o tempo**."),
            ("🏘️", "Uma **floresta** pode virar **sítio**, depois **vila** e depois **cidade**."),
            ("⚠️", "Essas mudanças trazem moradias e empregos, mas também podem causar **desmatamento** e **poluição**."),
        ],
        [
            ordem("Coloque a transformação na ordem", ["Floresta", "Algumas árvores cortadas e um sítio", "Uma vila com casas", "Uma cidade com prédios"], "A paisagem foi sendo modificada."),
            mc("O que acontece com os animais quando a floresta vira cidade?", ["Perdem o lugar onde vivem", "Ganham mais espaço", "Nada muda"], "Eles perdem o **habitat**.", "🐒"),
            mc("Uma mudança **boa** para a cidade crescendo seria...", ["Criar parques e plantar árvores", "Jogar esgoto no rio", "Derrubar toda a mata"], "Crescer cuidando da natureza.", "🌳"),
            tf("As paisagens podem mudar por ação humana.", True, "Construções, plantações, estradas..."),
            fill("Cortar muitas árvores de uma floresta é ___.", ["desmatamento", "reflorestamento", "jardinagem"], "**Desmatamento**."),
        ],
    ),
    # ------------------------------------------------------------ Ética
    "a3-b2-etica-u1-m1": missao(
        [
            ("📒", "Uma **agenda** ajuda a **organizar** o dia."),
            ("⏰", "Anote: horário da escola, lição de casa, tempo de brincar, tarefas de casa."),
            ("✅", "Primeiro as **obrigações**, depois o **lazer**: assim sobra tempo para tudo!"),
        ],
        [
            ordem("Organize a tarde de Caio", ["Almoçar", "Fazer a lição de casa", "Arrumar a mochila", "Brincar no parque", "Jantar"], "Obrigações primeiro, depois diversão."),
            mc("Para que serve uma agenda?", ["Organizar tarefas e compromissos", "Desenhar só", "Esconder coisas"], "Ela ajuda a **lembrar**.", "📒"),
            mc("Tenho lição e quero brincar. O que fazer primeiro?", ["A lição", "Brincar até dormir", "Nenhum dos dois"], "Depois da lição, brincar com tranquilidade!", "📚"),
            separar("Obrigação ou lazer?", ["Obrigação", "Lazer"],
                    [("lição de casa", 0), ("arrumar o quarto", 0), ("escovar os dentes", 0), ("andar de bicicleta", 1), ("ver desenho", 1)],
                    "As duas coisas são importantes!"),
            tf("Organizar o tempo ajuda a fazer tudo sem correria.", True, "Planejar é bom!"),
        ],
    ),
    "a3-b2-etica-u1-m2": missao(
        [
            ("🎒", "**Responsabilidade** é cuidar do que é **nosso dever**."),
            ("🧸", "Cabe à criança: guardar os brinquedos, cuidar do material, fazer a lição, cumprir combinados."),
            ("🧑", "Algumas coisas cabem aos **adultos**: pagar contas, dirigir, cozinhar no fogão."),
        ],
        [
            separar("De quem é a responsabilidade?", ["Da criança", "Do adulto"],
                    [("arrumar a mochila", 0), ("guardar os brinquedos", 0), ("fazer a lição", 0), ("pagar a conta de luz", 1), ("dirigir o carro", 1), ("levar ao médico", 1)],
                    "Cada um tem suas responsabilidades."),
            mc("Esqueci a lição em casa. De quem é a responsabilidade?", ["Minha", "Da professora", "Do cachorro"], "Arrumar a mochila é **meu** dever.", "🎒"),
            mc("Peguei o livro emprestado da biblioteca. O que é responsável?", ["Cuidar e devolver no prazo", "Rabiscar", "Perder"], "Cuidar do que é de todos.", "📚"),
            mc("Combinei de alimentar o peixinho. O que fazer?", ["Alimentar todo dia, como combinado", "Esquecer", "Dar comida de cachorro"], "Cumprir o combinado!", "🐠"),
            tf("Cuidar do próprio material é uma responsabilidade da criança.", True, "Seu material, seu cuidado."),
        ],
    ),
    "a3-b2-etica-u1-m3": missao(
        [
            ("🦸", "Você vai ser o **ajudante oficial** de casa por **5 dias**!"),
            ("🧺", "Escolha uma tarefa: pôr a mesa, regar as plantas, dar comida ao pet, guardar os sapatos..."),
            ("📅", "Marque cada dia que cumprir a tarefa."),
            desafio("escolha uma tarefa de casa com um adulto, faça todos os dias por 5 dias e marque num papel cada dia cumprido."),
        ],
        [
            mc("Qual é uma boa tarefa para o ajudante?", ["Pôr a mesa para o jantar", "Usar o fogão sozinho", "Mexer na tomada"], "Uma tarefa segura e útil!", "🍽️"),
            mc("Por que ajudar nas tarefas de casa?", ["Porque a casa é de todos", "Para ganhar dinheiro sempre", "Não precisa ajudar"], "Todos colaboram.", "🏠"),
            mc("Num dia você esqueceu a tarefa. O que fazer?", ["Fazer quando lembrar e continuar no dia seguinte", "Desistir de tudo", "Culpar alguém"], "Recomeçar faz parte!", "🔁"),
            tf("Cumprir uma tarefa todos os dias desenvolve responsabilidade.", True, "Hábito se treina!"),
            fill("Quem cumpre o que combinou é ___.", ["responsável", "esquecido", "preguiçoso"], "**Responsável**."),
        ],
    ),
    # ------------------------------------------------------------ Inglês
    "a3-b2-ingles-u1-m1": missao(
        [
            ("👕", "**Clothes** = roupas!"),
            ("👗", "**T-shirt** = camiseta · **shorts** = bermuda · **dress** = vestido · **skirt** = saia"),
            ("👟", "**shoes** = sapatos · **jacket** = jaqueta · **cap** = boné · **socks** = meias"),
        ],
        [
            mc("Dress up: **put on the T-shirt**! Qual roupa?", ["👕", "👗", "🧥"], "T-shirt = **camiseta**.", None),
            mc("Dress up: **put on the dress**! Qual roupa?", ["👗", "🩳", "🧢"], "dress = **vestido**.", None),
            mc("Dress up: **put on the jacket**! Qual roupa?", ["🧥", "👕", "🧦"], "jacket = **jaqueta**.", None),
            mc("Dress up: **put on the shoes**! Qual roupa?", ["👟", "🧢", "👗"], "shoes = **sapatos**.", None),
            mc("**I'm wearing a cap.** O que a pessoa está usando?", ["Um boné", "Uma saia", "Meias"], "cap = **boné**.", "🧢"),
        ],
    ),
    "a3-b2-ingles-u1-m2": missao(
        [
            ("☀️", "**It's hot!** (Está quente!) → shorts, T-shirt, cap."),
            ("❄️", "**It's cold!** (Está frio!) → jacket, scarf (cachecol), boots (botas)."),
            ("🌧️", "**It's rainy!** → raincoat (capa de chuva), umbrella (guarda-chuva)."),
        ],
        [
            separar("Hot or cold?", ["Hot ☀️", "Cold ❄️"],
                    [("shorts", 0), ("T-shirt", 0), ("cap", 0), ("jacket", 1), ("scarf", 1), ("boots", 1)],
                    "Roupa leve no calor, roupa quente no frio."),
            mc("**It's cold.** What do you wear?", ["A jacket", "Shorts", "A swimsuit"], "No frio, **jaqueta**.", "❄️"),
            mc("**It's hot.** What do you wear?", ["Shorts and a T-shirt", "A scarf and boots", "A jacket"], "No calor, roupa leve.", "☀️"),
            mc("**It's rainy.** What do you need?", ["An umbrella", "Sunglasses", "A swimsuit"], "Na chuva, **guarda-chuva**.", "☂️"),
            tf("**scarf** quer dizer cachecol.", True, "scarf = cachecol."),
        ],
    ),
    "a3-b2-ingles-u1-m3": missao(
        [
            ("🔗", "Vamos ligar as palavras às roupas!"),
            ("👖", "**pants** = calça · **sweater** = suéter · **pajamas** = pijama"),
            ("🧦", "Revise: T-shirt, shorts, dress, skirt, shoes, socks, jacket, cap."),
        ],
        [
            ligar([("T-shirt", "👕"), ("dress", "👗"), ("shorts", "🩳"), ("socks", "🧦")], "Ligue a palavra à roupa"),
            ligar([("pants", "👖"), ("cap", "🧢"), ("jacket", "🧥"), ("shoes", "👟")], "Ligue a palavra à roupa"),
            mc("Como se diz **calça** em inglês?", ["pants", "shorts", "skirt"], "calça = **pants**.", "👖"),
            mc("O que vestimos para dormir?", ["pajamas", "jacket", "cap"], "**pajamas** = pijama.", "😴"),
            fill("I'm wearing red ___. 🧦", ["socks", "dress", "cap"], "🧦 = **socks**."),
        ],
    ),
}
