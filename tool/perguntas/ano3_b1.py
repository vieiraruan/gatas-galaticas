"""3º ano · 1º bimestre."""
from base import desafio, fill, ligar, mc, missao, ordem, separar, tf

MISSOES = {
    # ------------------------------------------------------------ Português
    "a3-b1-portugues-u1-m1": missao(
        [
            ("🚗", "**R** e **RR** mudam o som e o sentido: **caro** (preço alto) e **carro** (veículo)."),
            ("🔤", "**RR** só aparece **entre duas vogais**: ca**rr**o, te**rr**a, ga**rr**afa."),
            ("🐭", "No **começo** da palavra, um **R** sozinho já tem som forte: **r**ato, **r**ua."),
        ],
        [
            fill("O ca___o do papai é vermelho. 🚗", ["rr", "r"], "Veículo = **carro**, com RR."),
            fill("Esse brinquedo é muito ca___o. 💰", ["r", "rr"], "Preço alto = **caro**, com R."),
            fill("A ga___afa de água. 🍾", ["rr", "r"], "**Garrafa**: som forte entre vogais = RR."),
            fill("O ___ato comeu o queijo. 🐭", ["r", "rr"], "No começo da palavra é só **R**: **rato**."),
            fill("A ba___ata fugiu da vassoura. 🪳", ["r", "rr"], "**Barata**: som fraco entre vogais = um R só."),
            fill("O cachorro co___eu no quintal. 🐶", ["rr", "r"], "**Correu**: som forte entre vogais."),
            separar("Qual palavra está escrita certa?", ["Certa", "Errada"],
                    [("terra", 0), ("barata", 0), ("rua", 0), ("rrua", 1), ("tera (chão)", 1)],
                    "RR nunca começa palavra."),
            tf("Palavras podem começar com **RR**.", False, "**RR** só aparece entre vogais."),
        ],
    ),
    "a3-b1-portugues-u1-m2": missao(
        [
            ("🔠", "**Dígrafo** são **duas letras** que fazem **um som só**."),
            ("🍃", "**LH**: fo**lh**a, ove**lh**a · **NH**: ni**nh**o, ara**nh**a · **CH**: **ch**uva, bi**ch**o"),
            ("👂", "Fale devagar e escute o som antes de escolher."),
        ],
        [
            fill("A fo___a caiu da árvore. 🍂", ["LH", "NH", "CH"], "**FOLHA**."),
            fill("O passarinho fez um ni___o. 🪺", ["NH", "LH", "CH"], "**NINHO**."),
            fill("Hoje vai ___over. 🌧️", ["CH", "LH", "NH"], "**CHOVER**."),
            fill("A ove___a tem lã. 🐑", ["LH", "NH", "CH"], "**OVELHA**."),
            fill("A ara___a fez a teia. 🕷️", ["NH", "LH", "CH"], "**ARANHA**."),
            fill("Eu bebo ___á quente. 🍵", ["CH", "NH", "LH"], "**CHÁ**."),
            separar("Separe pelo dígrafo", ["LH", "NH", "CH"],
                    [("milho", 0), ("coelho", 0), ("galinha", 1), ("banho", 1), ("chave", 2), ("bolacha", 2)],
                    "Cada par de letras faz um som só."),
            tf("Em **CHAVE**, as letras **C** e **H** fazem um som só.", True, "**CH** é dígrafo."),
        ],
    ),
    "a3-b1-portugues-u1-m3": missao(
        [
            ("📖", "**Ler com fluência** é ler sem tropeçar, no ritmo certo, respeitando a **pontuação**."),
            ("⏸️", "Na **vírgula** fazemos uma pausa curta. No **ponto final**, uma pausa maior."),
            ("❓", "Na **pergunta** a voz sobe. Na **exclamação** mostramos emoção!"),
            desafio("leia em voz alta um texto curto de um livro de que você goste, peça para um adulto gravar e marcar quanto tempo levou."),
        ],
        [
            mc("Onde fazemos uma **pausa maior** ao ler?", ["No ponto final", "Na vírgula", "No meio da palavra"], "O **ponto final** termina a frase.", "⏺️"),
            mc("Como lemos **Você vem amanhã?**", ["Com a voz subindo no final", "Gritando", "Sem parar"], "Perguntas terminam com a voz **subindo**.", "❓"),
            mc("Como lemos **Que susto!**", ["Com emoção", "Bem baixinho e sem emoção", "Como pergunta"], "A **exclamação** mostra emoção.", "❗"),
            mc("O que ajuda a ler com fluência?", ["Treinar a leitura várias vezes", "Ler pulando palavras", "Ler o mais rápido possível"], "Treinar deixa a leitura mais fácil.", "🔁"),
            ligar([(".", "pausa maior"), (",", "pausa curta"), ("?", "voz de pergunta"), ("!", "voz com emoção")], "Ligue o sinal ao jeito de ler"),
            tf("Ler com fluência é ler o mais rápido possível.", False, "É ler no **ritmo certo**, com entonação."),
        ],
    ),
    # ------------------------------------------------------------ Matemática
    "a3-b1-matematica-u1-m1": missao(
        [
            ("📏", "Na **reta numérica**, os números ficam em ordem, com a **mesma distância** entre eles."),
            ("➡️", "Quanto mais para a **direita**, **maior** o número."),
            ("🔟", "Numa reta de 100 em 100: 0, 100, 200, 300... O **250** fica bem no meio entre 200 e 300."),
        ],
        [
            mc("Na reta **0, 10, 20, __, 40**, qual número falta?", ["30", "25", "35"], "De 10 em 10: **30**.", "📏"),
            mc("Qual número fica **no meio** entre **200** e **300**?", ["250", "210", "290"], "200 + 50 = **250**.", "📍"),
            mc("Qual número fica **mais à direita** na reta?", ["1.500", "999", "1.050"], "O maior fica mais à direita: **1.500**.", "➡️"),
            mc("Na reta **1.000, 2.000, 3.000, __**, qual vem depois?", ["4.000", "3.100", "3.001"], "De 1.000 em 1.000.", "📏"),
            ordem("Posicione na reta, da esquerda para a direita", ["450", "1.200", "3.050", "9.999"], "Do menor para o maior."),
            mc("Qual número está **entre** 4.990 e 5.010?", ["5.000", "4.900", "5.100"], "**5.000** está entre os dois.", "🎯"),
            tf("Na reta numérica, o número 700 fica à esquerda do 600.", False, "700 é maior: fica à **direita**."),
        ],
    ),
    "a3-b1-matematica-u1-m2": missao(
        [
            ("🏗️", "**Decompor** é separar o número pelo valor de cada algarismo."),
            ("🔢", "**3.452 = 3.000 + 400 + 50 + 2**"),
            ("🧱", "3 unidades de **milhar**, 4 **centenas**, 5 **dezenas** e 2 **unidades**."),
        ],
        [
            mc("Decomponha **2.635**", ["2.000 + 600 + 30 + 5", "2 + 6 + 3 + 5", "200 + 60 + 3 + 5"], "Cada algarismo vale conforme a posição.", "🧩"),
            mc("Qual número é **4.000 + 700 + 20 + 1**?", ["4.721", "4.127", "47.201"], "4 milhares, 7 centenas, 2 dezenas, 1 unidade.", "🔢"),
            mc("Qual número é **5.000 + 80 + 3**?", ["5.083", "5.830", "583"], "Não há centenas: **5.083**.", "🔢"),
            mc("Em **7.249**, quanto vale o **7**?", ["7.000", "700", "7"], "O 7 está nas **unidades de milhar**.", "🔍"),
            mc("Em **7.249**, quanto vale o **4**?", ["40", "400", "4"], "O 4 está nas **dezenas**.", "🔍"),
            fill("6.000 + 300 + 9 = ___", ["6.309", "6.390", "639"], "Sem dezenas: **6.309**."),
            ligar([("1.000", "1 unidade de milhar"), ("100", "1 centena"), ("10", "1 dezena"), ("1", "1 unidade")], "Ligue o número ao nome"),
        ],
    ),
    "a3-b1-matematica-u1-m3": missao(
        [
            ("⚖️", "O sinal **=** é como uma **balança equilibrada**: os dois lados valem o mesmo."),
            ("🧮", "**8 + 5 = 10 + __** → do lado esquerdo temos 13. Então 10 + **3** = 13."),
            ("🔍", "Calcule um lado e descubra o que falta do outro."),
        ],
        [
            fill("8 + 5 = 10 + ___", ["3", "5", "13"], "8 + 5 = 13 e 10 + 3 = 13."),
            fill("6 + 6 = 10 + ___", ["2", "6", "12"], "6 + 6 = 12 = 10 + **2**."),
            fill("9 + 7 = 10 + ___", ["6", "7", "16"], "9 + 7 = 16 = 10 + **6**."),
            fill("20 + 15 = 30 + ___", ["5", "15", "35"], "35 = 30 + **5**."),
            fill("12 − 4 = 5 + ___", ["3", "4", "8"], "12 − 4 = 8 = 5 + **3**."),
            mc("Qual igualdade está **certa**?", ["7 + 3 = 5 + 5", "7 + 3 = 5 + 4", "7 + 3 = 6 + 6"], "10 = 10.", "⚖️"),
            tf("**4 + 9 = 9 + 4** é uma igualdade verdadeira.", True, "A ordem das parcelas não muda a soma."),
        ],
    ),
    # ------------------------------------------------------------ Ciências
    "a3-b1-ciencias-u1-m1": missao(
        [
            ("🥁", "Todo **som** é produzido por algo que **vibra** (treme muito rápido)."),
            ("🎸", "No violão, vibram as **cordas**. No tambor, vibra a **pele**. Na nossa voz, vibram as **pregas vocais** da garganta."),
            ("👂", "O som viaja pelo ar até as nossas **orelhas**."),
        ],
        [
            ligar([("violão", "cordas"), ("tambor", "pele esticada"), ("voz", "pregas vocais"), ("sino", "metal")], "Ligue o objeto ao que vibra"),
            mc("O que acontece quando tocamos a corda do violão?", ["Ela vibra e faz som", "Ela fica quieta", "Ela esquenta"], "A vibração produz o som.", "🎸"),
            mc("Coloque a mão na garganta e fale. O que você sente?", ["Uma vibração", "Frio", "Nada"], "As **pregas vocais** vibram.", "🗣️"),
            mc("Qual som é mais **forte** (alto)?", ["Uma buzina de caminhão", "Um sussurro", "Folhas balançando"], "A buzina é muito alta.", "📢"),
            separar("Som forte ou som fraco?", ["Forte", "Fraco"],
                    [("trovão", 0), ("sirene", 0), ("fogos de artifício", 0), ("cochicho", 1), ("tique-taque do relógio", 1), ("gato andando", 1)],
                    "Sons muito fortes podem fazer mal aos ouvidos."),
            tf("Ouvir música muito alta no fone pode prejudicar a audição.", True, "Proteja seus ouvidos!"),
        ],
    ),
    "a3-b1-ciencias-u1-m2": missao(
        [
            ("🪟", "**Transparente**: a luz passa e vemos tudo do outro lado (vidro da janela)."),
            ("🌫️", "**Translúcido**: a luz passa um pouco, mas a imagem fica embaçada (papel manteiga, vidro do box)."),
            ("🧱", "**Opaco**: a luz **não passa** (madeira, parede, papelão)."),
        ],
        [
            separar("A luz passa?", ["Transparente", "Translúcido", "Opaco"],
                    [("vidro da janela", 0), ("água limpa", 0), ("papel manteiga", 1), ("vidro jateado do box", 1), ("madeira", 2), ("papelão", 2)],
                    "Transparente: passa tudo. Translúcido: passa um pouco. Opaco: não passa."),
            mc("Uma porta de madeira é...", ["opaca", "transparente", "translúcida"], "A luz não atravessa a madeira.", "🚪"),
            mc("O vidro de um aquário é...", ["transparente", "opaco", "translúcido"], "Vemos os peixes direitinho!", "🐠"),
            mc("Que material forma **sombra** bem escura?", ["Opaco", "Transparente", "Nenhum"], "O opaco bloqueia toda a luz.", "🌑"),
            tf("Para enxergar bem, ler num lugar bem iluminado ajuda.", True, "Cuide da sua visão!"),
            fill("Um material que não deixa a luz passar é ___.", ["opaco", "transparente", "brilhante"], "**Opaco**."),
        ],
    ),
    "a3-b1-ciencias-u1-m3": missao(
        [
            ("🥫", "Vamos fazer um **telefone de lata** (ou de copos)!"),
            ("🧵", "Faça um furinho no fundo de dois copos, passe um **barbante** e dê um nó."),
            ("📞", "Com o fio **esticado**, a voz faz o barbante **vibrar** e o som chega ao outro copo!"),
            desafio("com um adulto, construa um telefone de copos e barbante. Teste falando baixinho e grave o teste."),
        ],
        [
            mc("Por onde o som viaja no telefone de lata?", ["Pelo barbante", "Pela luz", "Pelo chão"], "O barbante **vibra** e leva o som.", "🧵"),
            mc("Como o barbante deve ficar para funcionar bem?", ["Bem esticado", "Frouxo e enrolado", "Cortado"], "Esticado, ele vibra melhor.", "📏"),
            mc("Se alguém segurar o barbante no meio, o que acontece?", ["O som para de passar", "O som fica mais alto", "Nada muda"], "A vibração é interrompida.", "✋"),
            ordem("Coloque os passos na ordem", ["Furar o fundo dos copos", "Passar o barbante", "Dar um nó em cada ponta", "Esticar e falar"], "Construa com a ajuda de um adulto."),
            tf("O som pode viajar através de objetos sólidos, como o barbante.", True, "O som passa pelo ar, pela água e por sólidos."),
        ],
    ),
    # ------------------------------------------------------------ Ciências Humanas (História)
    "a3-b1-humanas-u1-m1": missao(
        [
            ("🏙️", "As cidades brasileiras foram formadas por **vários povos**."),
            ("🪶", "Os **povos indígenas** já viviam aqui. Os **africanos** foram trazidos à força e escravizados. Os **portugueses** colonizaram."),
            ("🧳", "Depois chegaram **imigrantes**: italianos, japoneses, alemães, árabes e muitos outros."),
        ],
        [
            mc("Quem já vivia no Brasil antes da chegada dos portugueses?", ["Os povos indígenas", "Os japoneses", "Os italianos"], "Os **indígenas** são os primeiros habitantes.", "🪶"),
            mc("Os africanos vieram para o Brasil...", ["trazidos à força e escravizados", "de férias", "para estudar"], "A escravidão foi uma grande injustiça da nossa história.", "⛓️"),
            mc("Pessoas que saem do seu país para viver em outro são...", ["imigrantes", "turistas", "astronautas"], "**Imigrantes**.", "🧳"),
            separar("Contribuições de cada povo", ["Indígenas", "Africanos", "Imigrantes"],
                    [("mandioca e rede de dormir", 0), ("palavras como pipoca e jabuti", 0), ("capoeira", 1), ("feijoada e acarajé", 1), ("pizza (italianos)", 2), ("sushi (japoneses)", 2)],
                    "Somos um povo formado por muitas culturas."),
            tf("A cultura brasileira é formada pela mistura de muitos povos.", True, "Essa mistura é a nossa riqueza."),
        ],
    ),
    "a3-b1-humanas-u1-m2": missao(
        [
            ("🔎", "**Fontes históricas** são tudo o que nos ajuda a conhecer o passado."),
            ("📜", "**Escritas**: cartas, jornais, documentos. **Orais**: histórias contadas pelas pessoas."),
            ("🖼️", "**Visuais**: fotos, pinturas. **Materiais**: objetos, roupas, construções."),
        ],
        [
            ligar([("carta antiga", "escrita"), ("relato do vovô", "oral"), ("fotografia", "visual"), ("panela de barro", "material")], "Ligue a fonte ao tipo"),
            ligar([("certidão de nascimento", "escrita"), ("entrevista gravada", "oral"), ("pintura", "visual"), ("moeda antiga", "material")], "Ligue a fonte ao tipo"),
            mc("Uma **foto da rua há 50 anos** é uma fonte...", ["visual", "oral", "material"], "Fotos são fontes **visuais**.", "📷"),
            mc("A vovó contando como era a escola dela é uma fonte...", ["oral", "escrita", "material"], "Histórias faladas são fontes **orais**.", "👵"),
            tf("Um brinquedo antigo pode ser uma fonte histórica.", True, "Objetos são fontes **materiais**."),
            fill("Um jornal antigo é uma fonte ___.", ["escrita", "oral", "sonora"], "Fonte **escrita**."),
        ],
    ),
    "a3-b1-humanas-u1-m3": missao(
        [
            ("🏘️", "As ruas também têm **história**! Elas mudam com o tempo."),
            ("👴", "Um vizinho que mora ali há muito tempo é uma ótima **fonte oral**."),
            ("❓", "Perguntas: **Como era a rua? Era de terra? Tinha mais árvores? O que mudou?**"),
            desafio("com um adulto, pergunte a um vizinho antigo como era a rua antigamente. Anote ou grave as respostas."),
        ],
        [
            mc("Quem é uma boa pessoa para contar a história da rua?", ["Um morador antigo", "Alguém que chegou ontem", "Um turista"], "Quem viveu ali há muito tempo sabe mais.", "👴"),
            mc("Qual é uma boa pergunta para o vizinho?", ["Como era a rua quando você chegou?", "Qual é o seu número de telefone?", "Você tem doce?"], "Pergunte sobre o **passado** da rua.", "❓"),
            mc("A rua era de **terra** e hoje é de **asfalto**. Isso mostra...", ["uma mudança ao longo do tempo", "que nada mudou", "que choveu"], "As ruas se **transformam**.", "🛣️"),
            separar("Comum antigamente ou hoje?", ["Antigamente", "Hoje"],
                    [("rua de terra", 0), ("carroça", 0), ("lampião", 0), ("asfalto", 1), ("semáforo", 1), ("poste de LED", 1)],
                    "Comparar antes e hoje mostra as mudanças."),
            tf("Conversar com moradores antigos ajuda a conhecer a história do lugar.", True, "Eles são **fontes orais**."),
        ],
    ),
    # ------------------------------------------------------------ Ciências Humanas (Geografia)
    "a3-b1-humanas-u2-m1": missao(
        [
            ("🌎", "Muitas coisas do nosso dia a dia vieram de **outros povos**."),
            ("🌽", "Dos **indígenas**: a **pipoca**, a **mandioca**, a **rede**, palavras como **capivara** e **Ipanema**."),
            ("🥁", "Dos **africanos**: o **samba**, a **capoeira**, o **acarajé**. Dos **portugueses**: a **língua portuguesa** e as **festas juninas**."),
        ],
        [
            ligar([("rede de dormir", "indígenas"), ("capoeira", "africanos"), ("língua portuguesa", "portugueses"), ("pizza", "italianos")], "Ligue à origem"),
            ligar([("mandioca", "indígenas"), ("acarajé", "africanos"), ("sushi", "japoneses"), ("bacalhau", "portugueses")], "Ligue a comida à origem"),
            mc("A palavra **capivara** veio de qual língua?", ["Tupi (indígena)", "Japonês", "Inglês"], "Muitas palavras vêm do **tupi**.", "🦫"),
            mc("O **samba** tem fortes raízes...", ["africanas", "japonesas", "alemãs"], "O samba nasceu da cultura **afro-brasileira**.", "🥁"),
            tf("A cultura brasileira tem heranças indígenas, africanas e europeias.", True, "E de muitos outros povos!"),
        ],
    ),
    "a3-b1-humanas-u2-m2": missao(
        [
            ("🏞️", "**Povos e comunidades tradicionais** vivem de um jeito ligado à natureza e às suas tradições."),
            ("🪶", "**Indígenas**: os primeiros povos do Brasil. **Quilombolas**: descendentes de africanos que formaram os **quilombos**."),
            ("🛶", "**Ribeirinhos** vivem à beira dos rios. **Caiçaras** vivem no litoral e vivem da pesca."),
        ],
        [
            ligar([("ribeirinhos", "à beira dos rios"), ("caiçaras", "no litoral"), ("quilombolas", "em quilombos"), ("indígenas", "em aldeias")], "Ligue o povo a onde vive"),
            mc("Quem vive à beira dos rios e usa barcos para se locomover?", ["Ribeirinhos", "Caiçaras", "Quilombolas"], "Os **ribeirinhos**, muito comuns na Amazônia.", "🛶"),
            mc("Quilombolas são descendentes de...", ["africanos que resistiram à escravidão", "imigrantes japoneses", "astronautas"], "Os **quilombos** eram lugares de liberdade.", "✊"),
            mc("Os caiçaras vivem principalmente da...", ["pesca", "mineração", "fábrica de carros"], "Eles vivem no **litoral**.", "🎣"),
            tf("Devemos respeitar os modos de vida dos povos tradicionais.", True, "Eles guardam saberes importantes."),
            fill("As moradias de um povo indígena formam uma ___.", ["aldeia", "fábrica", "avenida"], "Uma **aldeia**."),
        ],
    ),
    "a3-b1-humanas-u2-m3": missao(
        [
            ("📒", "Toda família tem uma **receita especial**: o bolo da vovó, a sopa do tio..."),
            ("👵", "As receitas guardam **histórias**: de onde vieram, quem ensinou, em que festas aparecem."),
            ("🎙️", "Receitas de família são **patrimônio** da nossa cultura."),
            desafio("escolha com um adulto uma receita da família e grave a história dela: quem ensinou, de onde veio e quando é feita."),
        ],
        [
            mc("Por que receitas de família são importantes?", ["Guardam histórias e tradições", "Só servem para matar a fome", "Não têm importância"], "Elas passam de geração em geração.", "📒"),
            mc("Qual pergunta ajuda a contar a história da receita?", ["Quem te ensinou essa receita?", "Quanto custa a panela?", "Qual é a cor do fogão?"], "Assim descobrimos a origem.", "❓"),
            mc("A receita passou da bisavó para a vovó e depois para a mamãe. Isso mostra...", ["uma tradição passada entre gerações", "uma receita nova", "uma receita de outro país"], "Uma **tradição** familiar.", "👩‍👧"),
            ordem("Organize a gravação", ["Dizer o nome da receita", "Contar quem ensinou", "Contar quando é feita", "Mostrar o prato pronto"], "Começo, meio e fim."),
            tf("Uma receita pode contar a história de uma família.", True, "Comida também é memória."),
        ],
    ),
    # ------------------------------------------------------------ Ética
    "a3-b1-etica-u1-m1": missao(
        [
            ("🚦", "Quando sentimos **raiva**, use o **semáforo das emoções**."),
            ("🔴", "**Vermelho: PARE.** Respire fundo e conte até 10."),
            ("🟡", "**Amarelo: PENSE.** O que aconteceu? O que posso fazer? **🟢 Verde: CONVERSE** e resolva."),
        ],
        [
            ordem("Coloque o semáforo das emoções na ordem", ["🔴 Parar e respirar", "🟡 Pensar no que aconteceu", "🟢 Conversar e resolver"], "Parar, pensar e conversar."),
            mc("No **vermelho** do semáforo, o que fazemos?", ["Paramos e respiramos", "Gritamos", "Saímos correndo"], "Primeiro **parar**.", "🔴"),
            mc("No **amarelo**, o que fazemos?", ["Pensamos no que aconteceu", "Empurramos", "Choramos para sempre"], "Hora de **pensar**.", "🟡"),
            mc("No **verde**, o que fazemos?", ["Conversamos para resolver", "Brigamos", "Ficamos de mal para sempre"], "Hora de **conversar**.", "🟢"),
            tf("Respirar fundo ajuda a acalmar a raiva.", True, "Respire devagar: inspira... expira..."),
            fill("Quando estou com raiva, primeiro eu ___.", ["paro", "bato", "grito"], "Primeiro **paro** e respiro."),
        ],
    ),
    "a3-b1-etica-u1-m2": missao(
        [
            ("⚽", "No recreio, Dani e Gui querem a **mesma bola**. Começa uma discussão."),
            ("🗣️", "Brigar não resolve. **Conversar**, **ouvir o outro** e **combinar** resolve!"),
            ("🤝", "Soluções: **revezar**, **brincar juntos**, **pedir ajuda a um adulto**."),
        ],
        [
            mc("Dani e Gui querem a mesma bola. Qual a melhor solução?", ["Revezar ou brincar juntos", "Puxar a bola com força", "Esconder a bola"], "Combinar é melhor que brigar.", "⚽"),
            mc("Um colega pisou no seu pé sem querer. O que fazer?", ["Aceitar as desculpas", "Pisar de volta", "Xingar"], "Foi sem querer: aceite as desculpas.", "🦶"),
            mc("Você esbarrou num colega e ele derrubou o lanche. O que fazer?", ["Pedir desculpas e ajudar", "Rir", "Fingir que não foi você"], "Pedir desculpas mostra respeito.", "🥪"),
            mc("A discussão ficou muito difícil. O que fazer?", ["Pedir ajuda a um adulto", "Bater", "Gritar mais alto"], "Um adulto pode ajudar a conversar.", "🧑‍🏫"),
            separar("Resolve ou piora o conflito?", ["Resolve", "Piora"],
                    [("ouvir o outro", 0), ("pedir desculpas", 0), ("revezar", 0), ("xingar", 1), ("empurrar", 1), ("fofocar", 1)],
                    "Diálogo resolve; agressão piora."),
        ],
    ),
    "a3-b1-etica-u1-m3": missao(
        [
            ("💬", "Podemos dizer o que sentimos **sem ofender**."),
            ("🧩", "Use a frase: **Eu me sinto... quando... Eu gostaria que...**"),
            ("🌟", "Exemplo: **Eu me sinto triste quando você não me chama para brincar. Eu gostaria de brincar junto.**"),
            desafio("grave uma frase dizendo como você se sentiu em alguma situação, usando **Eu me sinto... quando...**"),
        ],
        [
            mc("Qual frase é **respeitosa**?", ["Eu me sinto chateado quando você pega meu lápis sem pedir.", "Você é chato e mexe nas minhas coisas!", "Nunca mais falo com você!"], "Fale do que **você sente**, sem ofender.", "💬"),
            mc("Qual frase é **respeitosa**?", ["Eu fico triste quando riem de mim. Eu gostaria que parassem.", "Vocês são todos bobos!", "Vou contar para todo mundo!"], "Diga o que sente e o que gostaria.", "💬"),
            ordem("Monte a frase", ["Eu me sinto", "triste", "quando", "ninguém me ouve."], "**Eu me sinto triste quando ninguém me ouve.**"),
            tf("Falar do que sentimos ajuda a resolver conflitos.", True, "O outro entende melhor como você se sente."),
            fill("Eu me sinto feliz ___ meus amigos me ajudam.", ["quando", "nunca", "porém"], "**Eu me sinto... quando...**"),
        ],
    ),
    # ------------------------------------------------------------ Inglês
    "a3-b1-ingles-u1-m1": missao(
        [
            ("🚂", "**Days of the week** (dias da semana) em inglês começam com **letra maiúscula**!"),
            ("📅", "**Sunday** (domingo), **Monday** (segunda), **Tuesday** (terça), **Wednesday** (quarta)"),
            ("📅", "**Thursday** (quinta), **Friday** (sexta), **Saturday** (sábado)"),
        ],
        [
            ordem("Put the week train in order", ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], "Domingo a sábado."),
            ligar([("Monday", "segunda-feira"), ("Wednesday", "quarta-feira"), ("Friday", "sexta-feira"), ("Sunday", "domingo")], "Ligue o dia ao significado"),
            mc("O que é **Saturday**?", ["Sábado", "Domingo", "Segunda"], "Saturday = **sábado**.", "📅"),
            mc("Qual dia vem depois de **Monday**?", ["Tuesday", "Sunday", "Friday"], "Segunda → **terça (Tuesday)**.", "➡️"),
            mc("Como se diz **quinta-feira**?", ["Thursday", "Tuesday", "Wednesday"], "Quinta = **Thursday**.", "📅"),
            fill("Today is ___. I don't go to school! (domingo)", ["Sunday", "Monday", "Friday"], "Domingo = **Sunday**."),
        ],
    ),
    "a3-b1-ingles-u1-m2": missao(
        [
            ("🌦️", "**How's the weather?** = Como está o tempo?"),
            ("☀️", "**sunny** = ensolarado · **rainy** = chuvoso · **cloudy** = nublado"),
            ("💨", "**windy** = ventando · **snowy** = nevando · **hot** = quente · **cold** = frio"),
        ],
        [
            mc("How's the weather? ☀️", ["It's sunny.", "It's rainy.", "It's snowy."], "☀️ = **sunny**.", None),
            mc("How's the weather? 🌧️", ["It's rainy.", "It's sunny.", "It's windy."], "🌧️ = **rainy**.", None),
            mc("How's the weather? ☁️", ["It's cloudy.", "It's hot.", "It's snowy."], "☁️ = **cloudy**.", None),
            mc("How's the weather? 💨", ["It's windy.", "It's sunny.", "It's rainy."], "💨 = **windy**.", None),
            ligar([("sunny", "☀️"), ("rainy", "🌧️"), ("snowy", "❄️"), ("cloudy", "☁️")], "Ligue o tempo à figura"),
            mc("It's rainy! O que levar?", ["☂️ umbrella", "🕶️ sunglasses", "🩳 shorts"], "Na chuva, guarda-chuva (**umbrella**).", "☂️"),
        ],
    ),
    "a3-b1-ingles-u1-m3": missao(
        [
            ("📓", "Vamos fazer um **weather diary** (diário do tempo) em inglês!"),
            ("✍️", "Todo dia, olhe pela janela e escreva: **Monday: sunny ☀️**, **Tuesday: rainy 🌧️**..."),
            ("🔍", "No final, veja qual tempo apareceu mais!"),
            desafio("durante 5 dias, olhe o céu e escreva num papel o dia da semana e o tempo em inglês (sunny, rainy, cloudy, windy)."),
        ],
        [
            mc("Diário: **Monday: sunny · Tuesday: sunny · Wednesday: rainy**. Qual tempo apareceu mais?", ["sunny", "rainy", "windy"], "Sunny apareceu **2 vezes**.", "📓"),
            mc("Como escrever **Sexta: nublado**?", ["Friday: cloudy", "Friday: sunny", "Sunday: cloudy"], "Sexta = Friday, nublado = cloudy.", "☁️"),
            mc("Como escrever **Quarta: ventando**?", ["Wednesday: windy", "Wednesday: rainy", "Thursday: windy"], "Quarta = Wednesday, ventando = windy.", "💨"),
            fill("Thursday: ___ 🌧️", ["rainy", "sunny", "snowy"], "🌧️ = **rainy**."),
            tf("**It's hot** quer dizer está quente.", True, "hot = quente; cold = frio."),
        ],
    ),
}
