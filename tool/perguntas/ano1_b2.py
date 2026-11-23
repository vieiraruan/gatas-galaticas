"""1º ano · 2º bimestre."""
from base import desafio, fill, ligar, mc, missao, ordem, separar, tf

MISSOES = {
    # ------------------------------------------------------------ Português
    "a1-b2-portugues-u1-m1": missao(
        [
            ("👏", "Toda palavra é feita de **pedacinhos**: as **sílabas**."),
            ("🐱", "Fale batendo palmas: **GA** 👏 **TO** 👏. GATO tem **2 sílabas**."),
            ("🦋", "**BOR** 👏 **BO** 👏 **LE** 👏 **TA** 👏: BORBOLETA tem **4 sílabas**!"),
        ],
        [
            mc("Bata palmas: **SOL**. Quantas sílabas?", ["1", "2", "3"], "**SOL**: uma palma só.", "☀️"),
            mc("Bata palmas: **BOLA**. Quantas sílabas?", ["2", "1", "3"], "**BO**-**LA**: 2 palmas.", "⚽"),
            mc("Bata palmas: **MACACO**. Quantas sílabas?", ["3", "2", "4"], "**MA**-**CA**-**CO**: 3 palmas.", "🐒"),
            mc("Bata palmas: **JACARÉ**. Quantas sílabas?", ["3", "4", "2"], "**JA**-**CA**-**RÉ**: 3 palmas.", "🐊"),
            mc("Bata palmas: **BORBOLETA**. Quantas sílabas?", ["4", "3", "5"], "**BOR**-**BO**-**LE**-**TA**: 4 palmas.", "🦋"),
            mc("Qual palavra tem **mais** sílabas?", ["HIPOPÓTAMO", "PATO", "MAR"], "HI-PO-PÓ-TA-MO: 5 sílabas!", "🦛"),
            separar("Separe pelo número de sílabas", ["1 sílaba", "2 sílabas"],
                    [("PÃO", 0), ("FLOR", 0), ("MAR", 0), ("CASA", 1), ("UVA", 1), ("DADO", 1)],
                    "Bata palmas para contar."),
        ],
    ),
    "a1-b2-portugues-u1-m2": missao(
        [
            ("👂", "Algumas palavras **começam com o mesmo som**."),
            ("🐝", "**BOLA**, **BOCA** e **BOTA** começam com **BO**."),
            ("🦆", "**PATO** e **PANELA** começam com **PA**."),
        ],
        [
            mc("Qual começa com o mesmo som de **BOLA**?", ["BOTA", "MALA", "GATO"], "**BO**-LA e **BO**-TA.", "⚽"),
            mc("Qual começa com o mesmo som de **PATO**?", ["PANELA", "SAPO", "DEDO"], "**PA**-TO e **PA**-NELA.", "🦆"),
            mc("Qual começa com o mesmo som de **MACACO**?", ["MALA", "BOLO", "FACA"], "**MA**-CACO e **MA**-LA.", "🐒"),
            mc("Qual começa com o mesmo som de **SAPO**?", ["SAPATO", "PATO", "RATO"], "**SA**-PO e **SA**-PATO.", "🐸"),
            mc("Qual **termina** com o mesmo som de **GATO**?", ["RATO", "GALO", "GAVETA"], "GA-**TO** e RA-**TO**.", "🐱"),
            ligar([("BOLA", "BOTA"), ("CAMA", "CAJU"), ("LUA", "LUVA"), ("FADA", "FACA")], "Ligue as palavras que começam igual"),
            tf("**DADO** e **DEDO** começam com a letra **D**.", True, "As duas começam com **D**."),
        ],
    ),
    "a1-b2-portugues-u1-m3": missao(
        [
            ("🧩", "Falta um pedaço da palavra! Qual **sílaba** completa?"),
            ("🐱", "**GA__** + **TO** = **GATO**"),
            ("👀", "Fale a palavra devagar e escute o pedaço que falta."),
        ],
        [
            fill("___TO 🐱", ["GA", "PA", "MA"], "**GA**-TO."),
            fill("BO___ ⚽", ["LA", "TA", "CA"], "BO-**LA**."),
            fill("CA___ 🏠", ["SA", "MA", "DA"], "CA-**SA**."),
            fill("___CA 🐮", ["VA", "FA", "MA"], "**VA**-CA."),
            fill("PI___CA 🍿", ["PO", "PA", "PE"], "PI-**PO**-CA."),
            fill("JA___RÉ 🐊", ["CA", "BA", "TA"], "JA-**CA**-RÉ."),
            fill("BA___NA 🍌", ["NA", "LA", "TA"], "BA-**NA**-NA."),
        ],
    ),
    # ------------------------------------------------------------ Matemática
    "a1-b2-matematica-u1-m1": missao(
        [
            ("🥢", "Contar muitos palitos fica mais fácil em **pacotinhos de 10**."),
            ("📦", "Cada pacotinho de 10 é uma **dezena**. Os palitos soltos são **unidades**."),
            ("🔢", "**2 pacotinhos e 3 soltos = 23**."),
        ],
        [
            mc("**1 pacotinho de 10** e **4 soltos**. Quantos palitos?", ["14", "41", "5"], "10 + 4 = **14**.", "🥢"),
            mc("**3 pacotinhos de 10** e **0 soltos**. Quantos palitos?", ["30", "3", "13"], "10 + 10 + 10 = **30**.", "📦"),
            mc("**2 pacotinhos de 10** e **5 soltos**. Quantos palitos?", ["25", "52", "7"], "20 + 5 = **25**.", "🥢"),
            mc("Quantas **dezenas** tem o número **40**?", ["4", "0", "40"], "40 = 4 pacotinhos de 10.", "📦"),
            mc("No número **37**, quantas **unidades** soltas?", ["7", "3", "10"], "37 = 3 dezenas e **7 unidades**.", "🔢"),
            fill("5 dezenas e 2 unidades = ___", ["52", "25", "7"], "50 + 2 = **52**."),
            tf("**10 unidades** formam **1 dezena**.", True, "Um pacotinho de 10!"),
        ],
    ),
    "a1-b2-matematica-u1-m2": missao(
        [
            ("🔢", "Os números seguem uma **ordem**: 1, 2, 3, 4, 5..."),
            ("➡️", "O número que vem **depois** é o **sucessor**. O que vem **antes** é o **antecessor**."),
            ("🔟", "Podemos contar de **10 em 10**: 10, 20, 30, 40..."),
        ],
        [
            ordem("Complete a sequência", ["11", "12", "13", "14", "15"], "De 1 em 1."),
            ordem("Complete a sequência", ["10", "20", "30", "40", "50"], "De 10 em 10."),
            ordem("Complete a sequência", ["27", "28", "29", "30"], "Depois do 29 vem o 30!"),
            mc("Qual vem **depois** do **19**?", ["20", "18", "29"], "19, **20**.", "➡️"),
            mc("Qual vem **antes** do **50**?", ["49", "51", "40"], "**49**, 50.", "⬅️"),
            fill("60, 70, ___, 90", ["80", "75", "71"], "De 10 em 10: **80**."),
            mc("Qual é o **maior** número?", ["99", "89", "98"], "99 é o maior aqui.", "🏆"),
        ],
    ),
    "a1-b2-matematica-u1-m3": missao(
        [
            ("🐱", "Vamos descobrir **onde está o gato**!"),
            ("⬆️", "**Em cima** e **embaixo** · **na frente** e **atrás**"),
            ("✋", "**Direita** e **esquerda**: a mão que você usa para escrever costuma ser a direita (para muitas pessoas)."),
        ],
        [
            mc("O gato está sobre a mesa. Ele está...", ["em cima da mesa", "embaixo da mesa", "atrás da mesa"], "**Sobre** = **em cima**.", "🐱"),
            mc("O gato se escondeu sob a cama. Ele está...", ["embaixo da cama", "em cima da cama", "dentro do armário"], "**Sob** = **embaixo**.", "🛏️"),
            mc("A bola está entre o gato e o cachorro. A bola está...", ["no meio", "atrás de todos", "em cima do gato"], "**Entre** = no meio.", "⚽"),
            mc("Na fila, Ana está **atrás** de Léo. Quem está na frente?", ["Léo", "Ana", "Ninguém"], "Se Ana está atrás, Léo está **na frente**.", "🧍"),
            mc("🐱 ⚽ — O gato está à ___ da bola.", ["esquerda", "direita", "em cima"], "Lendo da esquerda para a direita, o gato vem antes: está à **esquerda**.", None),
            mc("⚽ 🐱 — O gato está à ___ da bola.", ["direita", "esquerda", "embaixo"], "O gato vem depois: está à **direita**.", None),
            tf("Quando estou de frente para alguém, a minha direita fica do lado da esquerda dessa pessoa.", True, "É como um espelho!"),
        ],
    ),
    # ------------------------------------------------------------ Ciências
    "a1-b2-ciencias-u1-m1": missao(
        [
            ("🧼", "Lavar as mãos tira a **sujeira** e os **micróbios** que podem nos deixar doentes."),
            ("🕐", "Lave **antes de comer**, **depois de ir ao banheiro** e **ao chegar da rua**."),
            ("🎵", "Esfregue por **20 segundos**: dá para cantar parabéns duas vezes!"),
        ],
        [
            ordem("Coloque os passos de lavar as mãos na ordem", ["Molhar as mãos", "Passar sabonete", "Esfregar palmas, dedos e unhas", "Enxaguar", "Secar com a toalha"], "Molhar, ensaboar, esfregar, enxaguar e secar."),
            mc("Quando devemos lavar as mãos?", ["Antes de comer", "Só no domingo", "Nunca"], "Sempre antes das refeições!", "🍽️"),
            mc("O que o sabonete faz?", ["Ajuda a tirar sujeira e micróbios", "Deixa as mãos mais sujas", "Faz as mãos crescerem"], "Sabonete + esfregar = mãos limpas.", "🧼"),
            mc("Por quanto tempo esfregar as mãos?", ["Uns 20 segundos", "1 segundo", "1 hora"], "Cante **parabéns** duas vezes.", "⏱️"),
            tf("Depois de usar o banheiro, devo lavar as mãos.", True, "Sempre!"),
            fill("Depois de lavar, eu ___ as mãos com a toalha.", ["seco", "sujo", "molho"], "Por último, **secar**."),
        ],
    ),
    "a1-b2-ciencias-u1-m2": missao(
        [
            ("🥦", "**Hábitos saudáveis** ajudam o corpo a crescer forte."),
            ("💤", "Comer frutas e verduras, beber água, dormir bem, brincar e tomar banho."),
            ("🍭", "Comer muito doce, ficar o dia todo no celular e não escovar os dentes **fazem mal**."),
        ],
        [
            separar("Hábito bom ou ruim?", ["Faz bem 💪", "Faz mal 🙁"],
                    [("comer frutas", 0), ("beber água", 0), ("dormir cedo", 0), ("brincar ao ar livre", 0), ("comer doce toda hora", 1), ("não escovar os dentes", 1), ("ficar o dia todo na tela", 1)],
                    "Bons hábitos cuidam do corpo."),
            mc("Qual lanche é **mais saudável**?", ["Banana", "Pirulito", "Refrigerante"], "A **fruta** tem vitaminas.", "🍌"),
            mc("O que beber quando temos sede?", ["Água", "Refrigerante", "Café bem doce"], "**Água** é a melhor bebida.", "💧"),
            mc("Para crescer com saúde, uma criança deve...", ["dormir bem à noite", "dormir pouquinho", "ficar acordada até tarde"], "O sono ajuda a crescer.", "😴"),
            tf("Tomar banho todo dia é um hábito saudável.", True, "O banho tira a sujeira e o suor."),
        ],
    ),
    "a1-b2-ciencias-u1-m3": missao(
        [
            ("🪥", "Escovar os dentes evita **cáries** (buraquinhos) e mau hálito."),
            ("⏰", "Escove **depois de cada refeição** e **antes de dormir**."),
            ("😁", "Escove a frente, atrás e em cima dos dentes, e a **língua** também!"),
            desafio("escove os dentes depois de cada refeição durante um dia inteiro. Peça para um adulto ajudar a marcar num papel."),
        ],
        [
            mc("Quando escovar os dentes?", ["Depois das refeições e antes de dormir", "Só quando lembrar", "Uma vez por semana"], "Depois de comer e antes de dormir.", "🪥"),
            mc("O que pode acontecer se não escovarmos os dentes?", ["Cáries", "Os dentes ficam mais fortes", "Nada"], "Os restos de comida causam **cáries**.", "🦷"),
            mc("Além dos dentes, o que também escovamos?", ["A língua", "As orelhas", "O cabelo"], "A língua também guarda sujeirinha.", "👅"),
            ordem("Coloque a escovação na ordem", ["Colocar pouca pasta na escova", "Escovar todos os dentes", "Escovar a língua", "Enxaguar a boca"], "Uma escovação completa!"),
            tf("Comer muito doce sem escovar os dentes ajuda a ter cáries.", True, "O açúcar alimenta as bactérias."),
        ],
    ),
    # ------------------------------------------------------------ Ciências Humanas (História)
    "a1-b2-humanas-u1-m1": missao(
        [
            ("👨‍👩‍👧‍👦", "Existem **muitos jeitos de ser família**."),
            ("🏠", "Algumas têm pai e mãe; outras, só mãe ou só pai; outras, dois pais ou duas mães; outras são criadas pelos avós ou tios."),
            ("❤️", "O que faz uma família é o **amor** e o **cuidado**."),
        ],
        [
            mc("O que faz uma família?", ["Amor e cuidado entre as pessoas", "Ter muitos móveis", "Morar numa casa grande"], "Família é **amor e cuidado**.", "❤️"),
            mc("Bia mora com a avó e o tio. Isso é uma família?", ["Sim", "Não", "Só se tiver cachorro"], "Existem muitos jeitos de ser família.", "👵"),
            mc("Todas as famílias são iguais?", ["Não, cada família é de um jeito", "Sim, todas iguais", "Só as grandes"], "Cada família é única.", "🌈"),
            tf("Uma família pode ser grande ou pequena.", True, "Tamanho não importa."),
            tf("Só existe um tipo certo de família.", False, "Há muitos jeitos de ser família."),
            fill("Na família, as pessoas cuidam umas das ___.", ["outras", "plantas", "nuvens"], "Cuidam umas das **outras**."),
        ],
    ),
    "a1-b2-humanas-u1-m2": missao(
        [
            ("🖍️", "Vamos fazer um **retrato da família**!"),
            ("👨‍👩‍👧", "Desenhe as pessoas que moram com você e quem você ama."),
            ("🎙️", "Depois, diga o nome de cada pessoa."),
            desafio("desenhe sua família num papel e grave um áudio dizendo o nome de cada pessoa."),
        ],
        [
            mc("A mãe da sua mãe é sua...", ["avó", "irmã", "tia"], "Mãe da mãe = **avó**.", "👵"),
            mc("O irmão do seu pai é seu...", ["tio", "avô", "primo"], "Irmão do pai = **tio**.", "👨"),
            mc("O filho da sua tia é seu...", ["primo", "irmão", "avô"], "Filho da tia = **primo**.", "👦"),
            ligar([("mãe da mãe", "avó"), ("pai do pai", "avô"), ("irmã da mãe", "tia"), ("filha da tia", "prima")], "Ligue as pessoas da família"),
            tf("Animais de estimação também podem fazer parte da família.", True, "Muita gente considera o pet da família!"),
        ],
    ),
    "a1-b2-humanas-u1-m3": missao(
        [
            ("🧹", "Em casa, **todos podem ajudar** nas tarefas!"),
            ("🧸", "Criança também ajuda: guardar os brinquedos, levar o prato para a pia, arrumar a cama."),
            ("🤝", "Tarefa de casa não é de uma pessoa só: é de **todos**."),
        ],
        [
            separar("Quem pode fazer cada tarefa?", ["Criança pode ajudar", "Só um adulto (é perigoso)"],
                    [("guardar brinquedos", 0), ("pôr a mesa", 0), ("regar as plantas", 0), ("usar o fogão", 1), ("subir na escada alta", 1)],
                    "Crianças ajudam em muita coisa, mas fogão e escada são com adultos."),
            mc("Quem deve ajudar nas tarefas de casa?", ["Todos da família", "Só a mãe", "Ninguém"], "Em casa, **todos** ajudam!", "🏠"),
            mc("Qual tarefa uma criança pequena pode fazer?", ["Guardar os brinquedos", "Dirigir o carro", "Usar o fogão sozinha"], "Guardar os brinquedos é com você!", "🧸"),
            mc("Depois de comer, você pode...", ["levar o prato para a pia", "deixar o prato no sofá", "jogar o prato fora"], "Uma ajuda simples!", "🍽️"),
            tf("Só os adultos fazem tarefas em casa.", False, "As crianças também ajudam."),
        ],
    ),
    # ------------------------------------------------------------ Ciências Humanas (Geografia)
    "a1-b2-humanas-u2-m1": missao(
        [
            ("📋", "**Regras** ajudam todos a **conviver bem**."),
            ("🙋", "Na turma: levantar a mão para falar, esperar a vez, cuidar do material, respeitar os colegas."),
            ("🤝", "Quando todos seguem as regras, **todo mundo ganha**."),
        ],
        [
            separar("Ajuda ou atrapalha a turma?", ["Ajuda", "Atrapalha"],
                    [("levantar a mão para falar", 0), ("esperar a vez", 0), ("guardar o material", 0), ("gritar na sala", 1), ("empurrar na fila", 1), ("rabiscar o livro do colega", 1)],
                    "Regras ajudam a conviver."),
            mc("Quero falar na roda de conversa. O que faço?", ["Levanto a mão e espero", "Grito mais alto", "Interrompo todo mundo"], "Esperar a vez é respeito.", "🙋"),
            mc("Para que servem as regras da turma?", ["Para todos conviverem bem", "Para ninguém brincar", "Para deixar a sala bagunçada"], "Regras ajudam a **conviver**.", "📋"),
            tf("Respeitar os colegas é uma regra importante.", True, "Respeito sempre!"),
            fill("Depois de brincar, eu ___ os brinquedos.", ["guardo", "quebro", "escondo"], "Guardar é um combinado da turma."),
        ],
    ),
    "a1-b2-humanas-u2-m2": missao(
        [
            ("🌳", "A **praça** é um espaço **público**: de todo mundo!"),
            ("🛝", "Na praça podemos encontrar **escorregador**, **balanço**, **bancos**, **árvores** e **lixeiras**."),
            ("🧹", "Como é de todos, **todos devem cuidar**."),
        ],
        [
            separar("Tem na praça?", ["Costuma ter na praça", "Não fica na praça"],
                    [("escorregador", 0), ("balanço", 0), ("banco", 0), ("árvore", 0), ("geladeira", 1), ("cama", 1), ("fogão", 1)],
                    "Geladeira, cama e fogão ficam em casa."),
            mc("Para que serve a **lixeira** da praça?", ["Para jogar o lixo", "Para sentar", "Para brincar"], "Lixo na lixeira!", "🗑️"),
            mc("A praça é de quem?", ["De todos", "Só de uma pessoa", "De ninguém"], "Espaço **público** é de todos.", "🌳"),
            mc("Onde sentamos para descansar na praça?", ["No banco", "Na lixeira", "No poste"], "No **banco**!", "🪑"),
            tf("Devemos cuidar dos brinquedos da praça.", True, "Assim todos podem brincar."),
        ],
    ),
    "a1-b2-humanas-u2-m3": missao(
        [
            ("🪁", "Crianças do Brasil inteiro brincam, cada uma no seu lugar."),
            ("🏖️", "Na **praia**: castelo de areia. No **rio**: nadar e pescar. Na **cidade**: andar de bicicleta na praça."),
            ("🌾", "No **campo**: subir em árvore, empinar pipa no pasto."),
        ],
        [
            ligar([("castelo de areia", "praia"), ("pular no rio", "beira do rio"), ("subir em árvore", "campo"), ("andar de patinete", "calçada da cidade")], "Ligue a brincadeira ao lugar"),
            mc("Onde se brinca de **castelo de areia**?", ["Na praia", "No elevador", "Na cozinha"], "Na **praia**!", "🏖️"),
            mc("Qual brincadeira precisa de **vento**?", ["Empinar pipa", "Pega-pega", "Esconde-esconde"], "A pipa voa com o vento.", "🪁"),
            mc("Qual brincadeira dá para fazer em quase qualquer lugar?", ["Pega-pega", "Surfar", "Esquiar na neve"], "Só precisa de amigos e espaço!", "🏃"),
            tf("Crianças de lugares diferentes podem ter brincadeiras diferentes.", True, "Cada lugar tem suas brincadeiras."),
        ],
    ),
    # ------------------------------------------------------------ Ética
    "a1-b2-etica-u1-m1": missao(
        [
            ("✨", "Existem **palavras mágicas** que deixam todo mundo feliz!"),
            ("🙏", "**Por favor**: para pedir. **Obrigado(a)**: para agradecer."),
            ("😔", "**Desculpa**: quando erramos. **Com licença**: para passar ou interromper."),
        ],
        [
            mc("Você quer o lápis do colega. O que diz?", ["Por favor, me empresta?", "Me dá logo!", "Nada, pega e pronto"], "Para pedir: **por favor**.", "✏️"),
            mc("A vovó te deu um presente. O que diz?", ["Obrigado!", "Desculpa!", "Com licença!"], "Para agradecer: **obrigado(a)**.", "🎁"),
            mc("Você pisou no pé do amigo sem querer. O que diz?", ["Desculpa!", "Obrigado!", "Por favor!"], "Quando erramos: **desculpa**.", "🦶"),
            mc("Você precisa passar entre duas pessoas. O que diz?", ["Com licença!", "Sai da frente!", "Obrigado!"], "Para passar: **com licença**.", "🚶"),
            ligar([("pedir", "por favor"), ("agradecer", "obrigado"), ("errar", "desculpa"), ("passar", "com licença")], "Ligue a situação à palavra mágica"),
        ],
    ),
    "a1-b2-etica-u1-m2": missao(
        [
            ("🛝", "No escorregador, todos querem descer! Por isso fazemos **fila**."),
            ("⏳", "Quem chegou **primeiro** desce primeiro. Os outros **esperam a vez**."),
            ("😊", "Esperar a vez é **respeitar** os amigos."),
        ],
        [
            ordem("Ana chegou primeiro, depois Léo, depois Bia. Monte a fila do escorregador", ["Ana", "Léo", "Bia"], "Quem chega primeiro desce primeiro."),
            ordem("Monte a fila: Tom chegou por último, Lia chegou primeiro e Caio no meio", ["Lia", "Caio", "Tom"], "Lia, Caio e Tom."),
            mc("Chegou um amigo novo na fila. Onde ele fica?", ["No fim da fila", "Na frente de todos", "No meio, empurrando"], "Quem chega depois vai para o **fim**.", "🧍"),
            mc("Alguém furou a fila. O que fazer?", ["Avisar com calma que tem fila", "Empurrar", "Chorar e ir embora"], "Converse com calma.", "🗣️"),
            tf("Esperar a vez é uma forma de respeito.", True, "Todos têm a sua vez."),
        ],
    ),
    "a1-b2-etica-u1-m3": missao(
        [
            ("🤝", "Um **bom amigo** brinca junto, divide e ajuda."),
            ("💬", "Ele **ouve**, **conforta** quando o outro está triste e **pede desculpas** quando erra."),
            ("🚫", "Amigo de verdade não **machuca**, não **exclui** e não faz **fofoca**."),
        ],
        [
            separar("Atitude de bom amigo?", ["Bom amigo", "Não é de bom amigo"],
                    [("dividir o lanche", 0), ("chamar para brincar", 0), ("consolar quem chora", 0), ("rir de quem errou", 1), ("deixar alguém de fora", 1), ("pegar sem pedir", 1)],
                    "Bons amigos cuidam uns dos outros."),
            mc("Seu amigo caiu e está chorando. O que fazer?", ["Ajudar e perguntar se está bem", "Rir", "Ir embora"], "Amigos se ajudam.", "🤕"),
            mc("Você e seu amigo querem o mesmo brinquedo. O que fazer?", ["Revezar ou brincar juntos", "Puxar com força", "Esconder"], "Dividir é coisa de amigo.", "🧸"),
            tf("Um bom amigo pede desculpas quando erra.", True, "Todos erram. Amigos pedem desculpas."),
            fill("Um bom amigo ___ os brinquedos.", ["divide", "esconde", "quebra"], "Amigos **dividem**."),
        ],
    ),
    # ------------------------------------------------------------ Inglês
    "a1-b2-ingles-u1-m1": missao(
        [
            ("🎨", "Vamos aprender as **colors** (cores) em inglês!"),
            ("🔴", "**red** = vermelho · **blue** = azul · **yellow** = amarelo · **green** = verde"),
            ("🟠", "**orange** = laranja · **pink** = rosa · **black** = preto · **white** = branco"),
        ],
        [
            mc("Touch **red**!", ["🔴", "🔵", "🟢"], "red = **vermelho**.", None),
            mc("Touch **blue**!", ["🔵", "🟡", "🔴"], "blue = **azul**.", None),
            mc("Touch **yellow**!", ["🟡", "🟢", "🟣"], "yellow = **amarelo**.", None),
            mc("Touch **green**!", ["🟢", "🔴", "🔵"], "green = **verde**.", None),
            ligar([("red", "🍎"), ("yellow", "🍌"), ("green", "🥦"), ("orange", "🍊")], "Ligue a cor à fruta"),
            mc("O céu sem nuvens é...", ["blue", "red", "black"], "Céu azul = **blue**.", "🌤️"),
        ],
    ),
    "a1-b2-ingles-u1-m2": missao(
        [
            ("🔢", "Vamos contar em inglês: **one, two, three, four, five**!"),
            ("✋", "E mais: **six, seven, eight, nine, ten**!"),
            ("🎵", "Conte nos dedos: one, two, three..."),
        ],
        [
            mc("Count with me: 🍎🍎🍎", ["three", "two", "four"], "1, 2, 3 = **three**.", None),
            mc("Count with me: ⭐⭐⭐⭐⭐", ["five", "four", "six"], "**five** = 5.", None),
            mc("Count with me: 🐶🐶", ["two", "one", "three"], "**two** = 2.", None),
            mc("Count with me: 🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈", ["ten", "nine", "eight"], "**ten** = 10.", None),
            ordem("Put the numbers in order", ["one", "two", "three", "four", "five"], "1, 2, 3, 4, 5."),
            ligar([("one", "1"), ("four", "4"), ("seven", "7"), ("nine", "9")], "Ligue o número em inglês ao algarismo"),
        ],
    ),
    "a1-b2-ingles-u1-m3": missao(
        [
            ("🖌️", "**Paint by number**: cada número tem uma cor!"),
            ("1️⃣", "**one = red** 🔴 · **two = blue** 🔵 · **three = yellow** 🟡"),
            ("👂", "Ouça o número e escolha a cor certa."),
        ],
        [
            mc("Number **one** is...", ["red 🔴", "blue 🔵", "yellow 🟡"], "one = red.", "1️⃣"),
            mc("Number **two** is...", ["blue 🔵", "red 🔴", "green 🟢"], "two = blue.", "2️⃣"),
            mc("Number **three** is...", ["yellow 🟡", "blue 🔵", "red 🔴"], "three = yellow.", "3️⃣"),
            ligar([("one", "red"), ("two", "blue"), ("three", "yellow")], "Ligue o número à cor do desenho"),
            mc("Paint the sun **yellow**. Qual cor?", ["Amarelo", "Azul", "Verde"], "yellow = amarelo.", "☀️"),
            mc("Paint the grass **green**. Qual cor?", ["Verde", "Vermelho", "Rosa"], "green = verde.", "🌱"),
        ],
    ),
}
