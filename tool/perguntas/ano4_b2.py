"""4º ano · 2º bimestre."""
from base import desafio, fill, ligar, mc, missao, ordem, separar, tf

MISSOES = {
    # ------------------------------------------------------------ Português
    "a4-b2-portugues-u1-m1": missao(
        [
            ("📌", "**Paroxítonas** (tônica na penúltima) levam acento quando terminam em **i(s)**, **l**, **r**, **x**, **ão(s)**, **um**..."),
            ("✏️", "**lá**-pis, **fá**-cil, a-**çú**-car, **ór**-gão, **tá**-xi."),
            ("🚫", "Paroxítonas terminadas em **a, e, o, em** **não** levam acento: **ca**-sa, **me**-sa, **i**-tem."),
        ],
        [
            mc("Qual está escrita **certa**?", ["lápis", "lapis", "lapís"], "Paroxítona terminada em **is**.", "✏️"),
            mc("Qual está escrita **certa**?", ["fácil", "facil", "facíl"], "Paroxítona terminada em **l**.", "😌"),
            mc("Qual está escrita **certa**?", ["açúcar", "açucar", "açucár"], "Paroxítona terminada em **r**.", "🍬"),
            mc("Qual está escrita **certa**?", ["órgão", "orgão", "orgâo"], "Paroxítona terminada em **ão**.", "🎹"),
            mc("Qual está escrita **certa**?", ["táxi", "taxi", "taxí"], "Paroxítona terminada em **i**.", "🚕"),
            mc("Por que **mesa** NÃO tem acento?", ["É paroxítona terminada em a", "É oxítona", "Porque é curta"], "Paroxítonas terminadas em **a** não levam acento.", "🪑"),
            tf("**Útil** é paroxítona terminada em **l** e leva acento.", True, "**Ú**-til."),
        ],
    ),
    "a4-b2-portugues-u1-m2": missao(
        [
            ("📝", "A **vírgula** separa itens de uma **enumeração**: **Comprei maçã, banana, uva e pera.**"),
            ("📣", "Separa o **vocativo** (quem é chamado): **Ana, venha aqui!**"),
            ("ℹ️", "Separa o **aposto** (explicação): **Rex, o meu cachorro, adora correr.**"),
        ],
        [
            mc("Onde vão as vírgulas? **Levei lápis borracha régua e cola.**", ["Levei lápis, borracha, régua e cola.", "Levei, lápis borracha régua, e cola.", "Levei lápis borracha, régua, e, cola."], "Vírgula entre os itens; antes do **e** não precisa.", "🎒"),
            mc("Qual frase usa vírgula no **vocativo**?", ["Pedro, feche a porta.", "Pedro feche, a porta.", "Pedro feche a, porta."], "**Pedro** está sendo chamado.", "🚪"),
            mc("Qual frase tem **aposto**?", ["Brasília, a capital do Brasil, é moderna.", "Brasília é moderna.", "Eu fui a Brasília."], "**a capital do Brasil** explica o que é Brasília.", "🏛️"),
            mc("Na frase **Mãe, posso brincar?**, a palavra **Mãe** é...", ["vocativo", "aposto", "verbo"], "É quem está sendo **chamado**.", "👩"),
            fill("Gosto de pizza___ sorvete e bolo.", [",", ".", "?"], "Enumeração: **vírgula**."),
            tf("Em enumerações, normalmente não se usa vírgula antes do **e**.", True, "**maçã, banana e uva**."),
        ],
    ),
    "a4-b2-portugues-u1-m3": missao(
        [
            ("🔍", "Hoje você é **revisor de texto**: procura e corrige erros!"),
            ("📄", "Texto: **ontem eu fui no parque com meu primo. nós brincamo muito e voltamos cansados**"),
            ("✅", "Confira: **letra maiúscula**, **pontuação** e **ortografia**."),
        ],
        [
            mc("Qual erro há em **ontem eu fui no parque**?", ["Falta letra maiúscula no começo", "Falta acento em parque", "Não há erro"], "Frase começa com **maiúscula**: Ontem.", "🔠"),
            mc("Como corrigir **nós brincamo muito**?", ["nós brincamos muito", "nós brincamu muito", "nós brincou muito"], "Nós **brincamos**.", "✏️"),
            mc("O que falta no fim de **voltamos cansados**?", ["Um ponto final", "Uma vírgula", "Um travessão"], "Toda frase precisa terminar com pontuação.", "⏺️"),
            mc("Qual versão está toda **correta**?", ["Ontem eu fui ao parque com meu primo. Nós brincamos muito e voltamos cansados.", "ontem eu fui ao parque com meu primo nós brincamos muito", "Ontem eu fui ao parque com meu primo, nós brincamo muito."], "Maiúsculas, pontuação e ortografia certas.", "🏆"),
            mc("Qual palavra está escrita **errada**?", ["exemplo → ezemplo", "casa", "escola"], "O certo é **exemplo**, com X.", "🔍"),
            tf("Revisar o texto antes de entregar ajuda a encontrar erros.", True, "Todo bom escritor revisa!"),
        ],
    ),
    # ------------------------------------------------------------ Matemática
    "a4-b2-matematica-u1-m1": missao(
        [
            ("🧩", "Alguns problemas têm **mais de uma etapa**."),
            ("1️⃣", "Leia com calma, descubra **o que se pede** e resolva **uma parte de cada vez**."),
            ("🛒", "Ex.: **Tinha R$ 100, gastei R$ 35 e R$ 20. Quanto sobrou?** → 35 + 20 = 55; 100 − 55 = **45**."),
        ],
        [
            mc("Tinha **R$ 100**. Gastei **R$ 35** e **R$ 20**. Quanto sobrou?", ["R$ 45", "R$ 55", "R$ 65"], "35 + 20 = 55; 100 − 55 = **45**.", "💵"),
            mc("Um ônibus saiu com **42** pessoas. Desceram **15** e subiram **8**. Quantas ficaram?", ["35", "49", "27"], "42 − 15 = 27; 27 + 8 = **35**.", "🚌"),
            mc("Ana tem **250** figurinhas e Bia tem **120** a mais. Quantas têm juntas?", ["620", "370", "500"], "Bia: 370. Juntas: 250 + 370 = **620**.", "🃏"),
            mc("Uma escola tem **328** meninos e **295** meninas. Faltaram **47**. Quantos vieram?", ["576", "623", "670"], "328 + 295 = 623; 623 − 47 = **576**.", "🏫"),
            mc("Comprei **3 cadernos de R$ 12**. Paguei com **R$ 50**. Qual o troco?", ["R$ 14", "R$ 36", "R$ 38"], "3 × 12 = 36; 50 − 36 = **14**.", "📓"),
            tf("Em problemas com várias etapas, resolvemos uma parte de cada vez.", True, "Passo a passo!"),
        ],
    ),
    "a4-b2-matematica-u1-m2": missao(
        [
            ("🔁", "A **adição** e a **subtração** são operações **inversas**: uma desfaz a outra."),
            ("✅", "**Prova real**: 345 + 128 = 473 → confira: 473 − 128 = **345** ✔️"),
            ("✖️", "A **multiplicação** e a **divisão** também são inversas: 6 × 7 = 42 → 42 ÷ 7 = 6."),
        ],
        [
            mc("Fiz **520 − 180 = 340**. Qual conta confere?", ["340 + 180 = 520", "340 − 180 = 160", "520 + 180 = 700"], "Somamos o resultado ao que foi tirado.", "✅"),
            mc("Fiz **8 × 9 = 72**. Qual conta confere?", ["72 ÷ 9 = 8", "72 + 9 = 81", "72 − 8 = 64"], "A divisão desfaz a multiplicação.", "✅"),
            mc("**456 + 237 = 693**. A prova real mostra que...", ["está certo, pois 693 − 237 = 456", "está errado", "não dá para conferir"], "693 − 237 = 456 ✔️", "🔍"),
            mc("**300 − 125 = 185**? Faça a prova real.", ["Errado: 185 + 125 = 310", "Certo", "Não dá para saber"], "O certo é **175**.", "❌"),
            mc("Qual é a operação inversa da **divisão**?", ["Multiplicação", "Adição", "Subtração"], "Elas se desfazem.", "🔁"),
            tf("Para conferir uma adição, podemos usar uma subtração.", True, "É a **prova real**."),
        ],
    ),
    "a4-b2-matematica-u1-m3": missao(
        [
            ("⚖️", "A balança **equilibrada** tem o **mesmo valor** dos dois lados."),
            ("❓", "**25 + ? = 40** → qual número equilibra? 40 − 25 = **15**."),
            ("🔁", "Use a **operação inversa** para descobrir o termo desconhecido."),
        ],
        [
            fill("25 + ___ = 40", ["15", "65", "25"], "40 − 25 = **15**."),
            fill("___ − 30 = 50", ["80", "20", "50"], "50 + 30 = **80**."),
            fill("6 × ___ = 48", ["8", "6", "42"], "48 ÷ 6 = **8**."),
            fill("___ ÷ 4 = 9", ["36", "13", "5"], "9 × 4 = **36**."),
            fill("100 + 50 = 120 + ___", ["30", "50", "150"], "150 = 120 + **30**."),
            mc("Um lado da balança tem **3 pesos de 10 kg**. O outro tem **20 kg** e **?**. Quanto falta para equilibrar?", ["10 kg", "30 kg", "20 kg"], "30 = 20 + **10**.", "⚖️"),
        ],
    ),
    "a4-b2-matematica-u2-m1": missao(
        [
            ("🌱", "Numa horta, as mudas ficam em **fileiras** e **colunas**: é uma **organização retangular**."),
            ("✖️", "**5 fileiras com 8 mudas** = 5 × 8 = **40 mudas**."),
            ("🧮", "Não precisa contar uma a uma: **multiplique**!"),
        ],
        [
            mc("Horta com **6 fileiras** de **7 mudas**. Quantas mudas?", ["42", "13", "48"], "6 × 7 = **42**.", "🌱"),
            mc("Um auditório tem **12 fileiras** de **10 cadeiras**. Quantas cadeiras?", ["120", "22", "110"], "12 × 10 = **120**.", "🪑"),
            mc("Uma caixa de ovos tem **3 fileiras** de **4**. E **5 caixas**?", ["60", "12", "17"], "3 × 4 = 12; 12 × 5 = **60**.", "🥚"),
            mc("Um muro tem **9 fileiras** de **15 tijolos**. Quantos tijolos?", ["135", "24", "125"], "9 × 15 = **135**.", "🧱"),
            mc("Se **1 pacote** tem **6 biscoitos**, **4 pacotes** têm **24**. Quantos em **8 pacotes**?", ["48", "32", "30"], "O dobro de pacotes, o dobro de biscoitos.", "🍪"),
            tf("Para contar mudas em fileiras iguais, podemos multiplicar.", True, "Fileiras × colunas."),
        ],
    ),
    "a4-b2-matematica-u2-m2": missao(
        [
            ("🚌", "**Excursão!** Cada ônibus leva **40 alunos**."),
            ("➗", "**130 alunos ÷ 40** = 3 ônibus cheios e **sobram 10**."),
            ("🤔", "Os 10 alunos que sobram **não podem ficar**: precisamos de **mais 1 ônibus**, total **4**."),
        ],
        [
            mc("**130 alunos**, ônibus de **40**. Quantos ônibus são necessários?", ["4", "3", "5"], "3 cheios + 1 para os 10 que sobram.", "🚌"),
            mc("**96 alunos** em grupos de **12**. Quantos grupos?", ["8", "7", "9"], "96 ÷ 12 = **8**.", "👥"),
            mc("**150 figurinhas** em pacotes de **25**. Quantos pacotes?", ["6", "5", "7"], "150 ÷ 25 = **6**.", "🃏"),
            mc("**50 bolos** em caixas de **12**. Quantas caixas **cheias**? Quantos sobram?", ["4 cheias e sobram 2", "5 cheias", "4 cheias e sobram 4"], "12 × 4 = 48; sobram **2**.", "🎂"),
            mc("**84 lápis** para **14 alunos**. Quantos cada um?", ["6", "7", "5"], "84 ÷ 14 = **6**.", "✏️"),
            tf("Às vezes o resto da divisão obriga a usar mais um grupo.", True, "Ninguém fica para trás!"),
        ],
    ),
    "a4-b2-matematica-u2-m3": missao(
        [
            ("👕", "Com **3 camisetas** e **2 bermudas**, quantos **conjuntos** diferentes dá para montar?"),
            ("✖️", "Cada camiseta combina com cada bermuda: **3 × 2 = 6** combinações."),
            ("🍦", "Vale para sorvetes, lanches, roupas... **multiplique as opções**!"),
        ],
        [
            mc("**3 camisetas** e **2 bermudas**. Quantas combinações?", ["6", "5", "9"], "3 × 2 = **6**.", "👕"),
            mc("**4 sabores** de sorvete e **3 coberturas**. Quantas combinações?", ["12", "7", "16"], "4 × 3 = **12**.", "🍦"),
            mc("**2 tipos de pão** e **5 recheios**. Quantos sanduíches diferentes?", ["10", "7", "25"], "2 × 5 = **10**.", "🥪"),
            mc("**5 camisetas** e **4 calças**. Quantos conjuntos?", ["20", "9", "25"], "5 × 4 = **20**.", "👖"),
            mc("**3 entradas**, **2 pratos** e **2 sobremesas**. Quantos cardápios?", ["12", "7", "6"], "3 × 2 × 2 = **12**.", "🍽️"),
            tf("Para contar combinações, multiplicamos as opções.", True, "Princípio da contagem!"),
        ],
    ),
    # ------------------------------------------------------------ Ciências
    "a4-b2-ciencias-u1-m1": missao(
        [
            ("🌿", "A **cadeia alimentar** mostra **quem come quem**."),
            ("➡️", "Ela começa sempre num **produtor** (planta): **capim → gafanhoto → sapo → cobra → gavião**."),
            ("🍄", "Os **decompositores** (fungos e bactérias) transformam restos em nutrientes para o solo."),
        ],
        [
            ordem("Monte a cadeia alimentar", ["Capim", "Gafanhoto", "Sapo", "Cobra"], "Do produtor ao último consumidor."),
            ordem("Monte a cadeia alimentar do mar", ["Algas", "Peixe pequeno", "Peixe grande", "Tubarão"], "Começa nas algas."),
            ordem("Monte a cadeia alimentar", ["Folhas", "Lagarta", "Passarinho", "Gavião"], "Plantas → herbívoros → carnívoros."),
            mc("Toda cadeia alimentar começa com...", ["um produtor (planta)", "um carnívoro", "um decompositor"], "As plantas produzem o próprio alimento.", "🌱"),
            mc("Se todos os sapos sumissem da cadeia **capim → gafanhoto → sapo → cobra**, o que aconteceria?", ["Os gafanhotos aumentariam e as cobras teriam menos comida", "Nada mudaria", "O capim cresceria sem parar sem motivo"], "Tudo está ligado!", "⚠️"),
        ],
    ),
    "a4-b2-ciencias-u1-m2": missao(
        [
            ("🌻", "**Produtores**: fazem o próprio alimento com luz do Sol (plantas, algas)."),
            ("🐰", "**Consumidores**: comem outros seres vivos (herbívoros, carnívoros, onívoros)."),
            ("🍄", "**Decompositores**: fungos e bactérias que decompõem restos de seres vivos."),
        ],
        [
            separar("Qual é o papel na cadeia?", ["Produtor", "Consumidor", "Decompositor"],
                    [("árvore", 0), ("capim", 0), ("alga", 0), ("coelho", 1), ("onça", 1), ("ser humano", 1), ("cogumelo", 2), ("bactéria do solo", 2)],
                    "Produz, consome ou decompõe."),
            mc("Por que as plantas são **produtoras**?", ["Fazem o próprio alimento com a luz", "Comem insetos", "Decompõem folhas"], "É a **fotossíntese**.", "☀️"),
            mc("O que os decompositores fazem?", ["Transformam restos em nutrientes", "Caçam animais", "Fazem fotossíntese"], "Eles **reciclam** a natureza.", "🍄"),
            mc("A energia da cadeia alimentar vem, no começo, do...", ["Sol", "tubarão", "solo apenas"], "O Sol alimenta os produtores.", "☀️"),
            tf("Sem decompositores, os restos de seres vivos se acumulariam.", True, "Eles são essenciais."),
        ],
    ),
    "a4-b2-ciencias-u1-m3": missao(
        [
            ("🍌", "Na **composteira**, restos de frutas e verduras viram **adubo**."),
            ("🍄", "Quem faz isso são os **decompositores**: fungos, bactérias e também minhocas."),
            ("📅", "Com o tempo, as cascas **escurecem**, **amolecem** e **diminuem**."),
            desafio("com um adulto, coloque cascas de frutas num pote com terra e observe por uma semana. Anote as mudanças a cada dia."),
        ],
        [
            mc("O que acontece com as cascas na composteira?", ["Se decompõem e viram adubo", "Ficam iguais para sempre", "Viram plástico"], "Decomposição!", "🍂"),
            mc("Quem decompõe os restos?", ["Fungos e bactérias", "Pássaros", "Peixes"], "Os **decompositores**.", "🦠"),
            mc("Para que serve o adubo da composteira?", ["Deixar a terra mais fértil para as plantas", "Fazer tinta", "Nada"], "Adubo natural!", "🌱"),
            separar("Pode ir para a composteira?", ["Pode", "Não pode"],
                    [("casca de banana", 0), ("borra de café", 0), ("folhas secas", 0), ("plástico", 1), ("vidro", 1), ("pilha", 1)],
                    "Só restos orgânicos vegetais."),
            tf("A compostagem diminui o lixo que vai para os aterros.", True, "Bom para o planeta!"),
        ],
    ),
    # ------------------------------------------------------------ Ciências Humanas (História)
    "a4-b2-humanas-u1-m1": missao(
        [
            ("📸", "Comparando fotos **antigas** e **atuais**, vemos como a cidade **mudou**."),
            ("🚋", "Bondes viraram ônibus e metrôs; casas viraram prédios; ruas de terra foram asfaltadas."),
            ("🏛️", "Alguns lugares **permanecem**: igrejas antigas, praças, estações."),
        ],
        [
            ligar([("bonde", "ônibus e metrô"), ("rua de paralelepípedo", "rua asfaltada"), ("casarão", "prédio de apartamentos"), ("armazém", "supermercado")], "Ligue o antes ao hoje"),
            mc("Por que as cidades mudam?", ["Crescem e as necessidades das pessoas mudam", "Por acaso", "Elas nunca mudam"], "Mais pessoas, novas tecnologias.", "🏙️"),
            mc("Uma igreja de 200 anos que continua igual é um exemplo de...", ["permanência", "mudança", "demolição"], "Ela **permanece**.", "⛪"),
            mc("O crescimento das cidades pode trazer...", ["mais empregos, mas também trânsito e poluição", "só coisas boas", "só coisas ruins"], "Há lados bons e desafios.", "⚖️"),
            tf("Fotos antigas são fontes para conhecer a história da cidade.", True, "Fontes **visuais**."),
        ],
    ),
    "a4-b2-humanas-u1-m2": missao(
        [
            ("🌾", "No **campo**, o ser humano também transforma a natureza."),
            ("🚜", "Desmata para plantar, cria pastos, constrói **represas** e **estradas**, usa **irrigação**."),
            ("🌳", "É possível produzir **cuidando**: reflorestar, preservar nascentes, fazer rotação de culturas."),
        ],
        [
            separar("Intervenção humana no campo ou elemento natural?", ["Feito pelo ser humano", "Natural"],
                    [("plantação de soja", 0), ("represa", 0), ("cerca de arame", 0), ("rio", 1), ("mata nativa", 1), ("morro", 1)],
                    "Veja o que foi construído ou plantado."),
            mc("Para que serve a **irrigação**?", ["Levar água às plantações", "Secar o rio", "Afastar os pássaros"], "Água para plantar.", "💧"),
            mc("Qual prática ajuda a preservar a natureza no campo?", ["Proteger as matas perto dos rios", "Queimar o pasto todo ano", "Derrubar tudo"], "As **matas ciliares** protegem os rios.", "🌳"),
            mc("Desmatar para criar pasto pode causar...", ["erosão e perda de animais nativos", "mais chuva sempre", "mais florestas"], "Impactos ambientais.", "⚠️"),
            tf("O campo também é uma paisagem modificada pelo ser humano.", True, "Plantações e pastos são modificações."),
        ],
    ),
    "a4-b2-humanas-u1-m3": missao(
        [
            ("🖼️", "Muitas famílias guardam **fotos antigas** da cidade."),
            ("👵", "Avós e tios podem contar **como era** o lugar e o que mudou."),
            ("🔎", "Também há fotos em **museus**, **bibliotecas** e **sites da prefeitura**."),
            desafio("busque com a família uma foto antiga da cidade (no álbum ou na internet) e compare com como o lugar está hoje."),
        ],
        [
            mc("Onde encontrar fotos antigas da cidade?", ["Álbuns de família, museus e arquivos públicos", "Só em revistas de moda", "Em lugar nenhum"], "Há muitas fontes!", "🖼️"),
            mc("Ao comparar a foto antiga com hoje, observamos...", ["o que mudou e o que permaneceu", "só a cor do céu", "o preço das coisas"], "Mudanças e permanências.", "🔍"),
            mc("Uma boa pergunta para a vovó sobre a foto é...", ["Como era este lugar quando você era criança?", "Qual é sua senha?", "Quer pizza?"], "Ela é uma **fonte oral**.", "👵"),
            tf("Uma foto antiga é uma fonte histórica.", True, "Fonte **visual**."),
            fill("O que continua igual com o tempo é uma ___.", ["permanência", "mudança", "invenção"], "**Permanência**."),
        ],
    ),
    # ------------------------------------------------------------ Ciências Humanas (Geografia)
    "a4-b2-humanas-u2-m1": missao(
        [
            ("🏘️", "Você mora num **bairro**, que faz parte de um **município** (cidade)."),
            ("🗺️", "O município faz parte de um **estado**; o estado, de uma **região**; e a região, do **país**: o **Brasil**."),
            ("🇧🇷", "O Brasil tem **26 estados** e o **Distrito Federal**, divididos em **5 regiões**."),
        ],
        [
            ordem("Do menor para o maior", ["Bairro", "Município", "Estado", "Região", "País"], "Um dentro do outro."),
            mc("Quantas **regiões** tem o Brasil?", ["5", "26", "3"], "Norte, Nordeste, Centro-Oeste, Sudeste e Sul.", "🗺️"),
            mc("Quantos **estados** tem o Brasil (além do DF)?", ["26", "5", "27"], "26 estados + o Distrito Federal.", "🇧🇷"),
            mc("Onde fica **Brasília**, a capital do país?", ["No Distrito Federal", "Em São Paulo", "No Rio de Janeiro"], "**Distrito Federal**, região Centro-Oeste.", "🏛️"),
            ligar([("Bahia", "Nordeste"), ("Amazonas", "Norte"), ("Paraná", "Sul"), ("Minas Gerais", "Sudeste")], "Ligue o estado à região"),
        ],
    ),
    "a4-b2-humanas-u2-m2": missao(
        [
            ("🏛️", "No **município**, o **prefeito** administra a cidade: escolas, postos de saúde, ruas."),
            ("🗳️", "Os **vereadores**, na **Câmara Municipal**, fazem as **leis** da cidade e **fiscalizam** o prefeito."),
            ("👥", "Os **conselhos** (de saúde, educação, tutelar) ajudam a cuidar de áreas específicas com a população."),
        ],
        [
            ligar([("prefeito", "administra a cidade"), ("vereadores", "fazem as leis municipais"), ("Conselho Tutelar", "protege os direitos das crianças"), ("eleitores", "escolhem os governantes pelo voto")], "Ligue quem decide à função"),
            mc("Quem faz as **leis do município**?", ["Os vereadores", "O presidente", "O diretor da escola"], "Na **Câmara Municipal**.", "📜"),
            mc("Quem escolhe o prefeito e os vereadores?", ["Os eleitores, pelo voto", "Sorteio", "O prefeito anterior"], "Eleições a cada 4 anos.", "🗳️"),
            mc("Onde trabalham os vereadores?", ["Na Câmara Municipal", "No hospital", "Na padaria"], "Na **Câmara**.", "🏛️"),
            tf("O prefeito cuida de serviços como escolas municipais e postos de saúde.", True, "Ele administra o município."),
        ],
    ),
    "a4-b2-humanas-u2-m3": missao(
        [
            ("🧩", "Vamos montar o **quebra-cabeça do Brasil**!"),
            ("🗺️", "**Norte**: a maior, com a Amazônia. **Nordeste**: 9 estados. **Centro-Oeste**: Pantanal e Brasília."),
            ("🏙️", "**Sudeste**: a mais populosa (SP, RJ, MG, ES). **Sul**: a menor (PR, SC, RS)."),
        ],
        [
            separar("Em qual região fica?", ["Norte", "Nordeste", "Sudeste", "Sul"],
                    [("Pará", 0), ("Amazonas", 0), ("Pernambuco", 1), ("Ceará", 1), ("São Paulo", 2), ("Espírito Santo", 2), ("Santa Catarina", 3), ("Rio Grande do Sul", 3)],
                    "Monte o mapa das regiões."),
            mc("Qual é a **maior** região em área?", ["Norte", "Sul", "Sudeste"], "A região **Norte**.", "🌳"),
            mc("Qual região tem **mais estados**?", ["Nordeste", "Sul", "Centro-Oeste"], "O Nordeste tem **9 estados**.", "🌴"),
            mc("O **Pantanal** fica principalmente em qual região?", ["Centro-Oeste", "Sul", "Nordeste"], "MT e MS, no **Centro-Oeste**.", "🐊"),
            mc("Qual é a região **mais populosa**?", ["Sudeste", "Norte", "Centro-Oeste"], "SP, RJ e MG têm muitos habitantes.", "🏙️"),
        ],
    ),
    # ------------------------------------------------------------ Ética
    "a4-b2-etica-u1-m1": missao(
        [
            ("🔒", "Na internet, alguns dados **não devem ser compartilhados**: **endereço**, **telefone**, **escola**, **senhas**, **fotos de documentos**."),
            ("🕵️", "Nem todo mundo é quem diz ser na internet."),
            ("🧑", "Na dúvida, **pergunte a um adulto de confiança** antes de postar."),
        ],
        [
            separar("Posso compartilhar na internet?", ["Pode (com cuidado)", "Não compartilhe"],
                    [("meu desenho favorito", 0), ("minha cor preferida", 0), ("meu endereço", 1), ("minha senha", 1), ("telefone de casa", 1), ("nome da minha escola", 1)],
                    "Dados pessoais ficam protegidos."),
            mc("Alguém que você não conhece pede sua senha no jogo. O que fazer?", ["Não dar e avisar um adulto", "Dar a senha", "Mandar a senha da mãe"], "Senha é **secreta**.", "🔑"),
            mc("Um desconhecido no jogo online quer saber onde você mora. O que fazer?", ["Não responder e contar a um adulto", "Responder", "Mandar uma foto da casa"], "Proteja seus dados.", "🏠"),
            tf("Fotos postadas na internet podem ser copiadas por outras pessoas.", True, "Pense antes de postar."),
            fill("Minha senha é ___.", ["secreta", "pública", "para todos"], "Senha é **secreta**."),
        ],
    ),
    "a4-b2-etica-u1-m2": missao(
        [
            ("💬", "Nas redes, do outro lado da tela há **uma pessoa** com sentimentos."),
            ("🤗", "Antes de comentar, pense: **eu diria isso pessoalmente?** É **verdade**? É **gentil**?"),
            ("🚫", "Comentários que ofendem, xingam ou espalham boatos **machucam**."),
        ],
        [
            mc("Um colega postou um desenho. Qual comentário é gentil?", ["Que lindo! Adorei as cores.", "Que feio!", "Desenho de bebê."], "Elogie com sinceridade.", "🎨"),
            mc("Você não gostou de um vídeo. O que fazer?", ["Não comentar ou dar uma opinião com respeito", "Xingar o autor", "Espalhar que ele é chato"], "Discordar com **respeito**.", "📹"),
            mc("Recebeu uma notícia estranha. Antes de compartilhar...", ["verifico se é verdade", "compartilho rápido", "aumento a história"], "Cuidado com **notícias falsas**.", "📰"),
            separar("Comentário respeitoso ou ofensivo?", ["Respeitoso", "Ofensivo"],
                    [("Parabéns pelo gol!", 0), ("Eu pensei diferente, mas respeito.", 0), ("Você é ridículo.", 1), ("Ninguém gosta de você.", 1)],
                    "As palavras na internet também machucam."),
            tf("Na internet devemos ser tão educados quanto pessoalmente.", True, "Respeito em todo lugar."),
        ],
    ),
    "a4-b2-etica-u1-m3": missao(
        [
            ("📱", "Usar telas o tempo todo pode atrapalhar o **sono**, os **estudos** e as **brincadeiras**."),
            ("⏳", "Um **combinado de tela** define **quando**, **quanto** e **onde** usar."),
            ("🛌", "Exemplos: sem celular na mesa e uma hora antes de dormir."),
            desafio("crie com a sua família 3 regras de uso do celular e do tablet e coloque num papel na geladeira."),
        ],
        [
            mc("Qual é um bom combinado de tela?", ["Sem celular durante as refeições", "Celular a noite toda na cama", "Usar o tempo todo"], "Refeição é hora de conversar.", "🍽️"),
            mc("Por que evitar telas antes de dormir?", ["Atrapalham o sono", "Deixam a gente com mais sono", "Não faz diferença"], "A luz da tela atrapalha o sono.", "😴"),
            mc("Qual atividade é boa para trocar pela tela?", ["Brincar ao ar livre", "Olhar outra tela", "Ficar parado"], "Movimento faz bem!", "⚽"),
            tf("Combinados de tela devem ser feitos com a família.", True, "Todos participam e todos cumprem."),
            fill("Um combinado de tela define quando, quanto e ___ usar.", ["onde", "quem é chato", "por quê não"], "Quando, quanto e **onde**."),
        ],
    ),
    # ------------------------------------------------------------ Inglês
    "a4-b2-ingles-u1-m1": missao(
        [
            ("🧭", "**Follow the directions!** Siga as instruções."),
            ("⬅️", "**Turn left** = vire à esquerda · **Turn right** = vire à direita"),
            ("⬆️", "**Go straight** = siga em frente · **Stop** = pare"),
        ],
        [
            mc("**Turn left!** Para onde virar?", ["⬅️ Esquerda", "➡️ Direita", "⬆️ Em frente"], "left = **esquerda**.", "🧭"),
            mc("**Turn right!** Para onde virar?", ["➡️ Direita", "⬅️ Esquerda", "⬇️ Para trás"], "right = **direita**.", "🧭"),
            mc("**Go straight!** O que fazer?", ["Seguir em frente", "Virar à esquerda", "Parar"], "straight = **em frente**.", "⬆️"),
            ordem("Follow: go straight, turn right, stop", ["⬆️ Go straight", "➡️ Turn right", "🛑 Stop"], "Em frente, direita, pare."),
            ligar([("turn left", "vire à esquerda"), ("turn right", "vire à direita"), ("go straight", "siga em frente"), ("stop", "pare")], "Ligue a instrução ao significado"),
        ],
    ),
    "a4-b2-ingles-u1-m2": missao(
        [
            ("🏙️", "**Places in town** (lugares da cidade)."),
            ("🏫", "**school** = escola · **park** = parque · **hospital** = hospital · **supermarket** = supermercado"),
            ("🏦", "**bakery** = padaria · **library** = biblioteca · **bank** = banco · **pharmacy** = farmácia"),
        ],
        [
            ligar([("school", "🏫"), ("hospital", "🏥"), ("park", "🌳"), ("supermarket", "🛒")], "Ligue o lugar ao nome"),
            ligar([("bakery", "padaria"), ("library", "biblioteca"), ("bank", "banco"), ("pharmacy", "farmácia")], "Ligue o lugar ao significado"),
            mc("O que é **library**?", ["Biblioteca", "Livraria de doces", "Laboratório"], "library = **biblioteca** (cuidado: não é livraria!).", "📚"),
            mc("Como se diz **padaria** em inglês?", ["bakery", "bank", "park"], "padaria = **bakery**.", "🥖"),
            tf("**hospital** se escreve igual em inglês e português.", True, "Só a pronúncia muda."),
        ],
    ),
    "a4-b2-ingles-u1-m3": missao(
        [
            ("❓", "**Where can I buy bread?** = Onde posso comprar pão?"),
            ("🥖", "**At the bakery!** = Na padaria!"),
            ("💊", "Medicine → **pharmacy** · Books to borrow → **library** · Food → **supermarket**"),
        ],
        [
            mc("Where can I buy **bread**?", ["At the bakery", "At the bank", "At the school"], "Pão = **bakery**.", "🥖"),
            mc("Where can I buy **medicine**?", ["At the pharmacy", "At the park", "At the library"], "Remédio = **pharmacy**.", "💊"),
            mc("Where can I **borrow books**?", ["At the library", "At the hospital", "At the bakery"], "Emprestar livros = **library**.", "📚"),
            mc("Where can I **play football**?", ["At the park", "At the pharmacy", "At the bank"], "Jogar bola = **park**.", "⚽"),
            mc("I'm sick. Where do I go?", ["To the hospital", "To the supermarket", "To the bakery"], "Doente = **hospital**.", "🏥"),
        ],
    ),
}
