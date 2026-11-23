"""1º ano · 1º bimestre."""
from base import desafio, fill, ligar, mc, missao, ordem, separar, tf

MISSOES = {
    # ------------------------------------------------------------ Português
    "a1-b1-portugues-u1-m1": missao(
        [
            ("✍️", "O nosso **nome** é escrito com **letras**."),
            ("🅰️", "**ANA** tem 3 letras: **A**, **N**, **A**. Começa com **A**."),
            ("👀", "Escrevemos da **esquerda** para a **direita**. Escreva seu nome no papel, {nome}!"),
        ],
        [
            mc("Com qual letra começa o nome **BIA**?", ["B", "I", "A"], "BIA começa com **B**.", "👧"),
            mc("Com qual letra começa o nome **LUCAS**?", ["L", "C", "S"], "LUCAS começa com **L**.", "👦"),
            mc("Quantas letras tem o nome **ANA**?", ["3", "2", "4"], "A-N-A: **3 letras**.", "🔢"),
            mc("Qual letra **termina** o nome **DAVI**?", ["I", "D", "A"], "D-A-V-**I**.", "🧒"),
            ligar([("MARIA", "M"), ("PEDRO", "P"), ("SOFIA", "S"), ("TOMÁS", "T")], "Ligue o nome à primeira letra"),
            mc("Qual nome começa com a mesma letra de **GABI**?", ["GUSTAVO", "BRUNO", "IGOR"], "GABI e GUSTAVO começam com **G**.", "🔤"),
            tf("Nomes de pessoas começam com letra maiúscula.", True, "Escrevemos **Ana**, **Léo**, com a primeira letra grande."),
            fill("Lemos e escrevemos da esquerda para a ___.", ["direita", "esquerda", "baixo"], "Da **esquerda** para a **direita**."),
        ],
    ),
    "a1-b1-portugues-u1-m2": missao(
        [
            ("🚂", "O **alfabeto** tem **26 letras**, sempre na mesma ordem."),
            ("🔤", "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"),
            ("🎶", "Cante o ABC para lembrar a ordem!"),
        ],
        [
            ordem("Coloque os vagões na ordem do alfabeto", ["A", "B", "C", "D"], "A, B, C, D."),
            ordem("Coloque os vagões na ordem do alfabeto", ["E", "F", "G", "H"], "E, F, G, H."),
            ordem("Coloque os vagões na ordem do alfabeto", ["M", "N", "O", "P"], "M, N, O, P."),
            mc("Qual letra vem **depois** do **B**?", ["C", "A", "D"], "A, B, **C**.", "🚃"),
            mc("Qual letra vem **antes** do **F**?", ["E", "G", "D"], "**E**, F.", "🚃"),
            mc("Qual é a **primeira** letra do alfabeto?", ["A", "Z", "B"], "O alfabeto começa com **A**.", "🅰️"),
            mc("Qual é a **última** letra do alfabeto?", ["Z", "X", "Y"], "O alfabeto termina com **Z**.", "🏁"),
            fill("A, B, ___, D", ["C", "E", "F"], "Falta o **C**."),
            tf("O alfabeto tem 26 letras.", True, "De A até Z são **26 letras**."),
        ],
    ),
    "a1-b1-portugues-u1-m3": missao(
        [
            ("🔤", "**Letras** servem para escrever palavras: **A, B, C...**"),
            ("🔢", "**Números** servem para contar: **1, 2, 3...**"),
            ("❓", "Há também **sinais**, como **+**, **?** e **!**"),
        ],
        [
            separar("Letra ou número?", ["Letra", "Número"],
                    [("A", 0), ("M", 0), ("R", 0), ("3", 1), ("7", 1), ("9", 1)],
                    "Letras escrevem palavras. Números contam."),
            separar("Letra, número ou sinal?", ["Letra", "Número", "Sinal"],
                    [("B", 0), ("L", 0), ("5", 1), ("2", 1), ("+", 2), ("?", 2)],
                    "**+** e **?** são sinais."),
            mc("Qual destes é um **número**?", ["8", "S", "O"], "**8** é número.", "🔢"),
            mc("Qual destes é uma **letra**?", ["E", "4", "!"], "**E** é letra.", "🔤"),
            mc("O que usamos para escrever o nome **LIA**?", ["Letras", "Números", "Sinais"], "Nomes são escritos com **letras**.", "✍️"),
            tf("O **0** (zero) é uma letra.", False, "O **0** é número. A letra parecida é o **O**."),
            fill("Para contar os brinquedos usamos os ___.", ["números", "sinais", "nomes"], "Contamos com **números**."),
        ],
    ),
    # ------------------------------------------------------------ Matemática
    "a1-b1-matematica-u1-m1": missao(
        [
            ("🐟", "Para **contar**, apontamos um de cada vez: 1, 2, 3..."),
            ("👉", "Não podemos pular nenhum nem contar o mesmo duas vezes."),
            ("🔢", "O **último número** que falamos é o total."),
        ],
        [
            mc("Quantos peixinhos? 🐟🐟🐟", ["3", "2", "4"], "1, 2, 3: **3 peixinhos**.", None),
            mc("Quantos peixinhos? 🐟🐟🐟🐟🐟", ["5", "4", "6"], "Contando: **5**.", None),
            mc("Quantas estrelas? ⭐⭐⭐⭐⭐⭐⭐", ["7", "6", "8"], "Contando: **7**.", None),
            mc("Quantas bolas? ⚽⚽⚽⚽⚽⚽⚽⚽⚽⚽", ["10", "9", "8"], "Contando: **10**.", None),
            mc("Quantos patos? 🦆🦆🦆🦆", ["4", "3", "5"], "Contando: **4**.", None),
            ordem("Coloque os números na ordem", ["1", "2", "3", "4", "5"], "Contamos 1, 2, 3, 4, 5."),
            fill("Depois do 9 vem o ___.", ["10", "8", "11"], "9, **10**."),
            mc("Na fila, quem está em **1º lugar** é...", ["o primeiro da fila", "o último da fila", "o do meio"], "**1º** = primeiro.", "🏁"),
        ],
    ),
    "a1-b1-matematica-u1-m2": missao(
        [
            ("⚖️", "Para saber quem tem **mais**, contamos os dois grupos."),
            ("🍎", "🍎🍎🍎 tem **3**. 🍎 tem **1**. O primeiro grupo tem **mais**."),
            ("🔍", "O grupo com **menos** é o que tem o número menor."),
        ],
        [
            mc("Quem tem **mais**? Lia: 🍓🍓🍓🍓 · Rui: 🍓🍓", ["Lia", "Rui", "Os dois iguais"], "4 é mais que 2.", None),
            mc("Quem tem **menos**? Ana: 🎈🎈🎈 · Bia: 🎈🎈🎈🎈🎈", ["Ana", "Bia", "Os dois iguais"], "3 é menos que 5.", None),
            mc("Quem tem **mais**? Gato: 🐟🐟🐟 · Urso: 🐟🐟🐟", ["Os dois iguais", "Gato", "Urso"], "3 e 3: **iguais**.", None),
            mc("Qual número é **maior**?", ["8", "5", "3"], "8 é o maior.", "🔢"),
            mc("Qual número é **menor**?", ["2", "6", "9"], "2 é o menor.", "🔢"),
            ordem("Do menor para o maior", ["1", "4", "7", "10"], "1 < 4 < 7 < 10."),
            tf("**6** é maior que **4**.", True, "6 vem depois de 4 na contagem."),
            mc("Sem contar, qual pote parece ter **mais** balas? 🍬 ou 🍬🍬🍬🍬🍬🍬🍬🍬", ["O segundo", "O primeiro", "Iguais"], "Estimar é dar um palpite olhando.", None),
        ],
    ),
    "a1-b1-matematica-u1-m3": missao(
        [
            ("🧸", "Podemos **organizar** os brinquedos de vários jeitos."),
            ("🎨", "Por **cor**: os vermelhos juntos, os azuis juntos."),
            ("📏", "Por **forma** ou por **tamanho**: grandes de um lado, pequenos do outro."),
        ],
        [
            separar("Separe por cor", ["🔴 Vermelho", "🔵 Azul"],
                    [("🍎 maçã", 0), ("🚗 carro vermelho", 0), ("🍓 morango", 0), ("💙 coração azul", 1), ("🫐 mirtilo", 1), ("🐳 baleia azul", 1)],
                    "Coisas vermelhas de um lado, azuis do outro."),
            separar("Separe por tamanho", ["Grande", "Pequeno"],
                    [("🐘 elefante", 0), ("🦒 girafa", 0), ("🐜 formiga", 1), ("🐭 ratinho", 1)],
                    "Elefante e girafa são grandes. Formiga e rato são pequenos."),
            separar("Separe por forma", ["Redondo", "Quadrado"],
                    [("⚽ bola", 0), ("🍊 laranja", 0), ("🪙 moeda", 0), ("🎁 caixa de presente", 1), ("🧊 cubo de gelo", 1)],
                    "Bola, laranja e moeda são redondas."),
            mc("Qual **não** combina com os outros? 🍎 🍓 🍒 🚗", ["🚗", "🍎", "🍓"], "Os outros são frutas.", None),
            mc("Qual **não** combina? 🐶 🐱 🐰 ✏️", ["✏️", "🐶", "🐰"], "Os outros são animais.", None),
            tf("Podemos separar brinquedos pela cor.", True, "Cor é um jeito de organizar."),
        ],
    ),
    # ------------------------------------------------------------ Ciências
    "a1-b1-ciencias-u1-m1": missao(
        [
            ("🧍", "Nosso corpo tem **cabeça**, **tronco**, **braços** e **pernas**."),
            ("🙂", "Na cabeça ficam os **olhos**, o **nariz**, a **boca** e as **orelhas**."),
            ("✋", "Nas pontas dos braços estão as **mãos**. Nas pontas das pernas, os **pés**."),
        ],
        [
            mc("Onde ficam os **olhos**?", ["Na cabeça", "Na perna", "No pé"], "Os olhos ficam no rosto, na cabeça.", "👀"),
            mc("O que fica na ponta do braço?", ["A mão", "O pé", "O nariz"], "No fim do braço está a **mão**.", "✋"),
            mc("O que fica na ponta da perna?", ["O pé", "A mão", "A orelha"], "No fim da perna está o **pé**.", "🦶"),
            separar("Fica na cabeça ou não?", ["Na cabeça", "Fora da cabeça"],
                    [("olhos", 0), ("nariz", 0), ("boca", 0), ("orelhas", 0), ("joelho", 1), ("barriga", 1)],
                    "Joelho fica na perna e barriga no tronco."),
            ordem("De cima para baixo no corpo", ["cabeça", "tronco", "pernas", "pés"], "Cabeça em cima, pés embaixo."),
            mc("Quantas mãos nós temos?", ["2", "1", "5"], "Uma **direita** e uma **esquerda**.", "🙌"),
            fill("Cada mão tem 5 ___.", ["dedos", "olhos", "pés"], "São **5 dedos** em cada mão."),
        ],
    ),
    "a1-b1-ciencias-u1-m2": missao(
        [
            ("👀", "Com os **olhos** vemos. Com as **orelhas** ouvimos."),
            ("👃", "Com o **nariz** sentimos cheiros. Com a **língua** sentimos o gosto."),
            ("✋", "Com a **pele** sentimos se algo é quente, frio, liso ou áspero."),
        ],
        [
            ligar([("olhos", "ver"), ("nariz", "cheirar"), ("orelhas", "ouvir"), ("língua", "sentir o gosto")], "Ligue a parte do corpo à função"),
            mc("Com o que sentimos o cheiro da flor?", ["Nariz", "Orelha", "Joelho"], "Cheiramos com o **nariz**.", "🌸"),
            mc("Com o que ouvimos a música?", ["Orelhas", "Olhos", "Mãos"], "Ouvimos com as **orelhas**.", "🎵"),
            mc("Com o que vemos o arco-íris?", ["Olhos", "Nariz", "Boca"], "Vemos com os **olhos**.", "🌈"),
            mc("Como sabemos que o sorvete é gelado?", ["Pela pele e pela boca", "Pelas orelhas", "Pelo cabelo"], "A pele e a boca sentem o frio.", "🍦"),
            mc("Com o que sentimos que o limão é azedo?", ["Língua", "Olhos", "Pés"], "A **língua** sente o gosto.", "🍋"),
            tf("Usamos as pernas para andar e correr.", True, "As **pernas** nos levam de um lugar a outro."),
        ],
    ),
    "a1-b1-ciencias-u1-m3": missao(
        [
            ("🧑‍🤝‍🧑", "As pessoas são **diferentes**: cor da pele, dos olhos, tipo de cabelo, altura."),
            ("🌈", "Ser diferente é **normal** e deixa o mundo mais bonito."),
            ("🤝", "Todas as pessoas merecem **respeito**."),
            desafio("desenhe você e um amigo num papel. Depois conte para um adulto o que é parecido e o que é diferente entre vocês."),
        ],
        [
            mc("Léo tem cabelo cacheado e Ana tem cabelo liso. Isso quer dizer que...", ["as pessoas são diferentes, e tudo bem", "um dos dois está errado", "eles não podem ser amigos"], "Diferenças são normais!", "💇"),
            mc("Um colega usa óculos. O que fazer?", ["Respeitar e brincar junto", "Rir dele", "Não brincar com ele"], "Respeito sempre.", "👓"),
            separar("O que pode ser diferente entre as pessoas?", ["Pode ser diferente", "Todo mundo tem"],
                    [("cor dos olhos", 0), ("tipo de cabelo", 0), ("altura", 0), ("coração", 1), ("sentimentos", 1)],
                    "Somos diferentes por fora, mas todos temos coração e sentimentos."),
            tf("Todas as pessoas merecem respeito.", True, "Sempre!"),
            tf("Só existe um jeito certo de ser.", False, "Cada pessoa tem o seu jeito."),
            fill("Ser diferente é ___.", ["normal", "errado", "feio"], "Ser diferente é **normal**."),
        ],
    ),
    # ------------------------------------------------------------ Ciências Humanas (História)
    "a1-b1-humanas-u1-m1": missao(
        [
            ("👶", "Quando nascemos, somos **bebês**. Depois crescemos!"),
            ("🧒", "O bebê vira **criança**, depois **adolescente**, depois **adulto**, depois **idoso**."),
            ("📸", "Uma **linha do tempo** mostra as coisas na ordem em que aconteceram."),
        ],
        [
            ordem("Coloque a vida de uma pessoa na ordem", ["👶 bebê", "🧒 criança", "🧑 adolescente", "🧔 adulto", "👴 idoso"], "Crescemos e mudamos com o tempo."),
            ordem("Coloque na ordem como o bebê aprende", ["Mama no peito ou na mamadeira", "Engatinha", "Dá os primeiros passos", "Corre e pula"], "Primeiro engatinhamos, depois andamos e corremos."),
            mc("O que vem **depois** de bebê?", ["Criança", "Idoso", "Adulto"], "Bebê → **criança**.", "🧒"),
            mc("Quem é mais velho?", ["👴 Vovô", "👶 Bebê", "🧒 Criança"], "O vovô viveu mais tempo.", None),
            tf("Todo mundo já foi bebê um dia.", True, "Até o vovô já foi bebê!"),
            fill("Com o tempo, nós ___.", ["crescemos", "encolhemos", "sumimos"], "Nós **crescemos** e mudamos."),
        ],
    ),
    "a1-b1-humanas-u1-m2": missao(
        [
            ("📸", "**Fotos** guardam **lembranças** do passado."),
            ("👨‍👩‍👧", "A família pode contar histórias de quando você era **bebê**."),
            ("🎙️", "Lembranças fazem parte da **nossa história**."),
            desafio("veja com a família uma foto de quando você era bebê e peça para alguém contar uma lembrança desse tempo. Grave o áudio!"),
        ],
        [
            mc("Para que servem as fotos antigas?", ["Para lembrar do passado", "Para cozinhar", "Para medir"], "Fotos guardam **lembranças**.", "📸"),
            mc("Quem pode contar como você era quando bebê?", ["A família", "Um desconhecido", "O cachorro do vizinho"], "A família viu você crescer.", "👨‍👩‍👧"),
            mc("Numa foto de bebê, provavelmente você estava...", ["no colo ou no berço", "dirigindo um carro", "indo trabalhar"], "Bebês ficam no colo e no berço.", "👶"),
            tf("Lembranças fazem parte da nossa história.", True, "Cada lembrança conta um pedaço da nossa vida."),
            fill("A foto de quando eu era bebê é do ___.", ["passado", "futuro", "amanhã"], "Ela mostra o **passado**."),
        ],
    ),
    "a1-b1-humanas-u1-m3": missao(
        [
            ("👶", "**Antes**, quando eu era bebê, eu **mamava**, **engatinhava** e usava **fralda**."),
            ("🧒", "**Agora**, eu **ando**, **falo**, **como sozinho** e **vou à escola**."),
            ("🔁", "Comparar **antes** e **agora** mostra como mudamos."),
        ],
        [
            separar("Antes (bebê) ou agora?", ["Antes (bebê)", "Agora"],
                    [("usava fralda", 0), ("mamava", 0), ("engatinhava", 0), ("vou à escola", 1), ("corro e pulo", 1), ("falo frases", 1)],
                    "Crescemos e aprendemos muitas coisas novas."),
            mc("O que um **bebê** faz?", ["Engatinha", "Vai à escola sozinho", "Lê livros"], "O bebê ainda **engatinha**.", "👶"),
            mc("O que você faz **agora** que não fazia quando bebê?", ["Andar de bicicleta", "Usar fralda", "Só mamar"], "Você aprendeu muitas coisas!", "🚲"),
            tf("Quando eu era bebê, eu já sabia ler.", False, "Bebês ainda não sabem ler."),
            fill("Quando eu era bebê, eu dormia no ___.", ["berço", "ônibus", "telhado"], "Bebês dormem no **berço**."),
        ],
    ),
    # ------------------------------------------------------------ Ciências Humanas (Geografia)
    "a1-b1-humanas-u2-m1": missao(
        [
            ("🏠", "As pessoas moram em **moradias** de muitos tipos."),
            ("🏢", "**Casa**, **apartamento** (num prédio), **palafita** (casa sobre a água, em cima de estacas)."),
            ("🛖", "A **oca** é a moradia tradicional de alguns povos indígenas."),
        ],
        [
            mc("Casa construída sobre estacas, em cima da água:", ["Palafita", "Apartamento", "Oca"], "A **palafita** fica acima da água.", "🌊"),
            mc("Moradia dentro de um prédio alto:", ["Apartamento", "Oca", "Palafita"], "O **apartamento** fica num prédio.", "🏢"),
            mc("Moradia tradicional de povos indígenas:", ["Oca", "Apartamento", "Palafita"], "A **oca** é feita de madeira e palha.", "🛖"),
            ligar([("🏢", "apartamento"), ("🛖", "oca"), ("🏠", "casa"), ("⛺", "barraca")], "Ligue a imagem ao tipo de moradia"),
            tf("Todas as pessoas moram no mesmo tipo de casa.", False, "Existem muitos tipos de moradia."),
            fill("Quem mora num prédio mora num ___.", ["apartamento", "barco", "oca"], "Prédio tem **apartamentos**."),
        ],
    ),
    "a1-b1-humanas-u2-m2": missao(
        [
            ("🏡", "A **casa** é o lugar onde moramos com a família."),
            ("🏫", "A **escola** é onde aprendemos e fazemos amigos."),
            ("🛣️", "No **caminho** de casa até a escola passamos por ruas, praças e lojas."),
            desafio("desenhe sua casa e o caminho até a escola. Mostre para um adulto o que você vê no caminho."),
        ],
        [
            mc("Onde aprendemos a ler e escrever?", ["Na escola", "No mercado", "No posto de gasolina"], "Na **escola** aprendemos muita coisa.", "🏫"),
            mc("Onde dormimos todas as noites?", ["Em casa", "Na escola", "Na praça"], "Dormimos em **casa**.", "🛏️"),
            separar("Fica na casa ou na escola?", ["Casa", "Escola"],
                    [("minha cama", 0), ("o fogão da família", 0), ("a sala de aula", 1), ("o quadro da professora", 1), ("o pátio do recreio", 1)],
                    "Cada lugar tem suas coisas."),
            mc("Ao atravessar a rua no caminho da escola, devemos...", ["olhar para os dois lados e ir com um adulto", "correr sem olhar", "brincar no meio da rua"], "Segurança em primeiro lugar!", "🚸"),
            tf("O caminho de casa até a escola pode passar por uma praça.", True, "Cada caminho é diferente."),
        ],
    ),
    "a1-b1-humanas-u2-m3": missao(
        [
            ("🛋️", "A casa tem **cômodos**: **sala**, **quarto**, **cozinha** e **banheiro**."),
            ("🍳", "Na **cozinha** preparamos a comida. No **quarto** dormimos."),
            ("🛁", "No **banheiro** tomamos banho. Na **sala** conversamos e vemos TV."),
        ],
        [
            separar("Em qual cômodo fica?", ["Cozinha", "Quarto", "Banheiro"],
                    [("fogão", 0), ("geladeira", 0), ("cama", 1), ("guarda-roupa", 1), ("chuveiro", 2), ("escova de dentes", 2)],
                    "Cada objeto tem o seu cômodo."),
            ligar([("sofá", "sala"), ("cama", "quarto"), ("fogão", "cozinha"), ("chuveiro", "banheiro")], "Ligue o objeto ao cômodo"),
            mc("Onde fica a **geladeira**?", ["Na cozinha", "No banheiro", "No quarto"], "A geladeira guarda os alimentos na **cozinha**.", "🧊"),
            mc("Onde tomamos banho?", ["No banheiro", "Na sala", "Na cozinha"], "No **banheiro**.", "🚿"),
            tf("A cama fica na cozinha.", False, "A cama fica no **quarto**."),
        ],
    ),
    # ------------------------------------------------------------ Ética
    "a1-b1-etica-u1-m1": missao(
        [
            ("😀", "Todos nós sentimos **emoções**: **alegria**, **tristeza**, **raiva** e **medo**."),
            ("😢", "Não existe emoção errada. O importante é **saber o nome** do que sentimos."),
            ("🗣️", "Quando sabemos o nome, fica mais fácil **contar** para alguém."),
        ],
        [
            ligar([("😀", "alegria"), ("😢", "tristeza"), ("😠", "raiva"), ("😨", "medo")], "Ligue a carinha à emoção"),
            mc("Qual carinha mostra **alegria**?", ["😀", "😢", "😠"], "Sorriso = **alegria**.", None),
            mc("Qual carinha mostra **medo**?", ["😨", "😀", "😴"], "Olhos arregalados = **medo**.", None),
            mc("Qual carinha mostra **tristeza**?", ["😢", "😀", "😠"], "Lágrima = **tristeza**.", None),
            tf("Sentir raiva às vezes é normal.", True, "Todo mundo sente. O importante é não machucar ninguém."),
            fill("Quando choro porque perdi meu brinquedo, sinto ___.", ["tristeza", "alegria", "fome"], "Perder algo nos deixa **tristes**."),
        ],
    ),
    "a1-b1-etica-u1-m2": missao(
        [
            ("🎂", "As situações fazem a gente sentir emoções diferentes."),
            ("🎁", "Ganhar um presente traz **alegria**. Um trovão forte pode dar **medo**."),
            ("🤗", "Se você vir alguém triste, pode **ajudar** ou **chamar um adulto**."),
        ],
        [
            mc("Tom ganhou um cachorrinho. Como ele se sente?", ["Alegre", "Triste", "Com raiva"], "Ganhar um bichinho traz **alegria**.", "🐶"),
            mc("Lia quebrou o brinquedo preferido. Como ela se sente?", ["Triste", "Alegre", "Com sono"], "Perder algo querido dá **tristeza**.", "🧸"),
            mc("Caio ouviu um trovão muito alto à noite. Como ele se sente?", ["Com medo", "Alegre", "Com fome"], "Barulhos fortes podem dar **medo**.", "⛈️"),
            mc("Um colega pegou o lápis de Bia sem pedir. Como ela pode se sentir?", ["Com raiva", "Com sono", "Alegre"], "Ela pode sentir **raiva**. Pode dizer: **Por favor, me devolve**.", "✏️"),
            mc("Quando estou com medo, o que posso fazer?", ["Pedir ajuda a um adulto", "Ficar sozinho e não contar", "Gritar com todo mundo"], "Pedir ajuda é corajoso!", "🤗"),
            tf("Contar como me sinto ajuda os outros a me entenderem.", True, "Falar sobre emoções ajuda muito."),
        ],
    ),
    "a1-b1-etica-u1-m3": missao(
        [
            ("🎙️", "Hoje você vai contar **como se sente**."),
            ("💬", "Você pode dizer: **Hoje eu me sinto feliz, porque brinquei com meu amigo.**"),
            ("❤️", "Todas as emoções podem ser contadas."),
            desafio("conte para alguém da família como você se sentiu hoje e por quê. Peça para gravar o áudio."),
        ],
        [
            mc("Como podemos contar o que sentimos?", ["Hoje eu me sinto... porque...", "Não falar nada", "Fazer careta e sair correndo"], "Diga a emoção e o motivo.", "💬"),
            mc("Para quem posso contar como me sinto?", ["Família, professora e amigos", "Ninguém", "Só para o espelho"], "Pessoas de confiança gostam de ouvir.", "👨‍👩‍👧"),
            mc("Qual frase mostra o **motivo** da emoção?", ["Estou feliz porque ganhei um abraço.", "Estou feliz.", "Feliz."], "A palavra **porque** mostra o motivo.", "🤗"),
            tf("Só podemos contar quando estamos felizes.", False, "Podemos contar todas as emoções."),
            fill("Hoje eu me sinto ___ porque brinquei no parque.", ["feliz", "triste", "com medo"], "Brincar no parque deixa **feliz**!"),
        ],
    ),
    # ------------------------------------------------------------ Inglês
    "a1-b1-ingles-u1-m1": missao(
        [
            ("👋", "Em inglês, quando **chegamos**, dizemos **Hello!** ou **Hi!** (olá, oi)."),
            ("🚪", "Quando **vamos embora**, dizemos **Bye!** ou **Goodbye!** (tchau)."),
            ("😊", "Vamos treinar: **Hello, teacher!** · **Bye, mom!**"),
        ],
        [
            mc("Você chegou na escola. O que diz?", ["Hello!", "Bye!", "Goodbye!"], "Chegando: **Hello!**", "🏫"),
            mc("Você está indo embora da festa. O que diz?", ["Bye!", "Hello!", "Hi!"], "Saindo: **Bye!**", "🎈"),
            separar("Chegando ou saindo?", ["Chegando 👋", "Saindo 🚪"],
                    [("Hello!", 0), ("Hi!", 0), ("Bye!", 1), ("Goodbye!", 1)],
                    "Hello e Hi = olá. Bye e Goodbye = tchau."),
            ligar([("Hello", "olá"), ("Hi", "oi"), ("Bye", "tchau")], "Ligue a palavra ao significado"),
            tf("**Hi** quer dizer oi.", True, "Hi = oi!"),
            fill("___! See you tomorrow! (Tchau! Até amanhã!)", ["Bye", "Hello", "Hi"], "Despedida = **Bye**."),
        ],
    ),
    "a1-b1-ingles-u1-m2": missao(
        [
            ("❓", "**What's your name?** = Qual é o seu nome?"),
            ("🙋", "**My name is...** = Meu nome é... Exemplo: **My name is {nome}!**"),
            ("🗣️", "Repita em voz alta: **Hello! My name is {nome}.**"),
            desafio("diga em voz alta **Hello! My name is...** com o seu nome e peça para um adulto gravar."),
        ],
        [
            mc("O que quer dizer **What's your name?**", ["Qual é o seu nome?", "Quantos anos você tem?", "Onde você mora?"], "name = nome.", "❓"),
            mc("Como dizer **Meu nome é Ana**?", ["My name is Ana.", "Bye, Ana.", "What's Ana?"], "**My name is** = meu nome é.", "🙋"),
            mc("Alguém pergunta **What's your name?**. O que responder?", ["My name is Leo.", "Goodbye!", "Hello, name!"], "Responda com **My name is...**", "💬"),
            ordem("Monte a frase: Meu nome é Bia", ["My", "name", "is", "Bia."], "**My name is Bia.**"),
            tf("**name** quer dizer nome.", True, "name = nome."),
        ],
    ),
    "a1-b1-ingles-u1-m3": missao(
        [
            ("🌅", "De **manhã**: **Good morning!** (bom dia)"),
            ("🌤️", "De **tarde**: **Good afternoon!** (boa tarde)"),
            ("🌙", "De **noite**: **Good evening!** (boa noite, ao chegar) e **Good night!** (boa noite, ao dormir)"),
        ],
        [
            mc("Você acordou e encontrou a mamãe. O que diz?", ["Good morning!", "Good night!", "Good afternoon!"], "De manhã: **Good morning!**", "🌅"),
            mc("Hora de dormir. O que diz?", ["Good night!", "Good morning!", "Hello!"], "Antes de dormir: **Good night!**", "🛏️"),
            mc("Depois do almoço, você chega na casa da vovó. O que diz?", ["Good afternoon!", "Good night!", "Good morning!"], "À tarde: **Good afternoon!**", "🌤️"),
            ligar([("Good morning", "bom dia"), ("Good afternoon", "boa tarde"), ("Good night", "boa noite")], "Ligue o cumprimento ao significado"),
            ordem("Coloque na ordem do dia", ["Good morning!", "Good afternoon!", "Good night!"], "Manhã, tarde e noite."),
            tf("**Good morning** quer dizer boa noite.", False, "Good morning = **bom dia**."),
        ],
    ),
}
