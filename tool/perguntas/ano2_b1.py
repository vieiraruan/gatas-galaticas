"""2º ano · 1º bimestre."""
from base import desafio, fill, ligar, mc, missao, ordem, separar, tf

MISSOES = {
    # ------------------------------------------------------------ Português
    "a2-b1-portugues-u1-m1": missao(
        [
            ("🏭", "Na **fábrica de palavras**, trocamos uma **sílaba** e nasce uma palavra nova!"),
            ("🐱", "**GA**-TO → **PA**-TO → **MA**-TO → **RA**-TO"),
            ("🔁", "Também dá para trocar a última sílaba: BO-**LA** → BO-**CA** → BO-**TA**."),
        ],
        [
            mc("Troque **GA** por **PA** em **GATO**. Que palavra nasce?", ["PATO", "GALO", "MATO"], "**PA**-TO!", "🦆"),
            mc("Troque **BO** por **CO** em **BOLA**. Que palavra nasce?", ["COLA", "BOCA", "MOLA"], "**CO**-LA!", "🧴"),
            mc("Troque **LA** por **TA** em **BOLA**. Que palavra nasce?", ["BOTA", "BOCA", "LATA"], "BO-**TA**!", "👢"),
            mc("Troque **FA** por **VA** em **FACA**. Que palavra nasce?", ["VACA", "MACA", "FOCA"], "**VA**-CA!", "🐮"),
            ligar([("GATO", "PATO"), ("MALA", "SALA"), ("DADO", "LADO"), ("BICO", "RICO")], "Ligue as palavras que mudam só a primeira sílaba"),
            fill("___TO: é um bicho que rói queijo.", ["RA", "PA", "GA"], "**RA**-TO."),
            tf("Trocando **ME** por **LE** em **MESA**, formamos **LESA**, que é uma palavra que usamos muito.", False, "Nem toda troca forma uma palavra conhecida! Se trocarmos **ME** por **PE**, temos **PESA**."),
        ],
    ),
    "a2-b1-portugues-u1-m2": missao(
        [
            ("🧩", "Palavras são formadas por **sílabas**: **CA-VA-LO** tem 3 sílabas."),
            ("👏", "Bata palmas a cada sílaba: **BOR** 👏 **BO** 👏 **LE** 👏 **TA** 👏"),
            ("🔀", "Se as sílabas embaralharem, a palavra fica sem sentido. Vamos arrumar!"),
        ],
        [
            ordem("Forme a palavra 🐴", ["CA", "VA", "LO"], "**CAVALO**."),
            ordem("Forme a palavra 🦋", ["BOR", "BO", "LE", "TA"], "**BORBOLETA**."),
            ordem("Forme a palavra 🍿", ["PI", "PO", "CA"], "**PIPOCA**."),
            ordem("Forme a palavra 🐢", ["TAR", "TA", "RU", "GA"], "**TARTARUGA**."),
            ordem("Forme a palavra 🎈", ["BA", "LÃO"], "**BALÃO**."),
            mc("Quantas sílabas tem **SAPATO**?", ["3", "2", "4"], "SA-PA-TO: **3 sílabas**.", "👞"),
            mc("Quantas sílabas tem **PÉ**?", ["1", "2", "3"], "**PÉ**: só 1 sílaba.", "🦶"),
            mc("Qual palavra tem **4 sílabas**?", ["ABACAXI", "UVA", "MEL"], "A-BA-CA-XI.", "🍍"),
        ],
    ),
    "a2-b1-portugues-u1-m3": missao(
        [
            ("🅰️", "As **vogais** são **A, E, I, O, U**."),
            ("🔍", "**Toda sílaba tem pelo menos uma vogal!** CA-**SA**, **PRA**-TO, **U**-VA."),
            ("🔤", "As outras letras são **consoantes**: B, C, D, F, G..."),
        ],
        [
            fill("C___SA (onde moramos)", ["A", "B", "T"], "**CASA**: toda sílaba precisa de vogal."),
            fill("B___LA (de brincar)", ["O", "L", "P"], "**BOLA**."),
            fill("G___TO (o bichinho que mia)", ["A", "R", "M"], "**GATO**: toda sílaba precisa de vogal."),
            separar("Vogal ou consoante?", ["Vogal", "Consoante"],
                    [("A", 0), ("E", 0), ("I", 0), ("O", 0), ("U", 0), ("B", 1), ("M", 1), ("T", 1)],
                    "A, E, I, O, U são as vogais."),
            mc("Qual destas é uma **vogal**?", ["E", "R", "S"], "**E** é vogal.", "🔤"),
            mc("Qual sílaba está **certa**?", ["LU", "LT", "BR"], "**LU** tem vogal. As outras não!", "🧩"),
            tf("Toda sílaba tem pelo menos uma vogal.", True, "É a regra das sílabas."),
            mc("Quantas vogais tem o alfabeto?", ["5", "3", "26"], "A, E, I, O, U.", "🖐️"),
        ],
    ),
    # ------------------------------------------------------------ Matemática
    "a2-b1-matematica-u1-m1": missao(
        [
            ("🟨", "No **material dourado**: o **cubinho** vale **1** (unidade)."),
            ("📏", "A **barra** vale **10** (dezena): são 10 cubinhos juntos."),
            ("🟧", "A **placa** vale **100** (centena): são 10 barras juntas."),
        ],
        [
            mc("**2 placas, 3 barras e 4 cubinhos**. Que número é?", ["234", "432", "9"], "200 + 30 + 4 = **234**.", "🟧"),
            mc("**1 placa, 0 barras e 5 cubinhos**. Que número é?", ["105", "15", "150"], "100 + 0 + 5 = **105**.", "🟧"),
            mc("**4 barras e 6 cubinhos**. Que número é?", ["46", "64", "406"], "40 + 6 = **46**.", "📏"),
            mc("Quantas **barras** formam uma placa?", ["10", "100", "5"], "10 barras de 10 = **100**.", "🟧"),
            mc("No número **358**, quantas **centenas** há?", ["3", "5", "8"], "**3** centenas = 300.", "🔢"),
            mc("No número **358**, o **5** vale...", ["50", "5", "500"], "O 5 está nas dezenas: **50**.", "🔢"),
            ligar([("1 cubinho", "1"), ("1 barra", "10"), ("1 placa", "100")], "Ligue a peça ao valor"),
            fill("300 + 20 + 7 = ___", ["327", "372", "3207"], "3 centenas, 2 dezenas, 7 unidades."),
        ],
    ),
    "a2-b1-matematica-u1-m2": missao(
        [
            ("🔢", "Para comparar números de 3 algarismos, olhamos primeiro as **centenas**."),
            ("⚖️", "**412** é maior que **398**, porque 4 centenas é mais que 3 centenas."),
            ("👀", "Se as centenas forem iguais, olhamos as **dezenas**; depois, as **unidades**."),
        ],
        [
            ordem("Do menor para o maior", ["125", "251", "512", "521"], "125 < 251 < 512 < 521."),
            ordem("Do menor para o maior", ["309", "390", "903", "930"], "Compare as centenas primeiro."),
            ordem("Do maior para o menor", ["870", "807", "780", "708"], "870 > 807 > 780 > 708."),
            mc("Qual número é **maior**?", ["615", "561", "516"], "6 centenas é o maior.", "⚖️"),
            mc("Qual número é **menor**?", ["243", "247", "250"], "Mesma centena; 4 dezenas e 3 unidades é o menor.", "⚖️"),
            mc("Qual vem **logo depois** de **499**?", ["500", "490", "4100"], "499 + 1 = **500**.", "➡️"),
            fill("O número antes de 300 é ___.", ["299", "301", "200"], "300 − 1 = **299**."),
            tf("**1000** é maior que **999**.", True, "999 + 1 = 1000."),
        ],
    ),
    "a2-b1-matematica-u1-m3": missao(
        [
            ("🔁", "Uma **sequência** segue uma **regra**."),
            ("5️⃣", "**5, 10, 15, 20...** a regra é **somar 5** (de 5 em 5)."),
            ("⬇️", "**50, 40, 30...** a regra é **tirar 10**: é uma sequência **decrescente**."),
        ],
        [
            mc("Qual é a regra? **2, 4, 6, 8...**", ["De 2 em 2", "De 5 em 5", "De 10 em 10"], "Soma 2 a cada vez.", "🔁"),
            mc("Qual é a regra? **10, 20, 30, 40...**", ["De 10 em 10", "De 2 em 2", "De 1 em 1"], "Soma 10 a cada vez.", "🔁"),
            mc("Qual vem depois? **5, 10, 15, 20, ...**", ["25", "21", "30"], "20 + 5 = **25**.", "➡️"),
            mc("Qual vem depois? **100, 200, 300, ...**", ["400", "301", "310"], "De 100 em 100.", "➡️"),
            mc("Qual vem depois? **50, 45, 40, 35, ...**", ["30", "25", "40"], "Tira 5: **30**.", "⬇️"),
            fill("3, 6, 9, ___, 15", ["12", "10", "11"], "De 3 em 3: **12**."),
            separar("Crescente ou decrescente?", ["Crescente ⬆️", "Decrescente ⬇️"],
                    [("1, 3, 5, 7", 0), ("10, 20, 30", 0), ("90, 80, 70", 1), ("20, 15, 10", 1)],
                    "Crescente aumenta; decrescente diminui."),
        ],
    ),
    # ------------------------------------------------------------ Ciências
    "a2-b1-ciencias-u1-m1": missao(
        [
            ("🧱", "Os objetos são feitos de **materiais**: **metal**, **madeira**, **vidro**, **plástico**, **tecido**."),
            ("🔍", "Cada material tem **propriedades**: o vidro é **transparente**, o metal é **resistente**, o tecido é **macio**."),
            ("🤔", "Escolhemos o material pelo **uso**: janela de vidro para a luz passar!"),
        ],
        [
            mc("Qual o melhor material para uma **janela**?", ["Vidro", "Madeira", "Tecido"], "O vidro é **transparente**: deixa a luz passar.", "🪟"),
            mc("Qual o melhor material para uma **panela**?", ["Metal", "Papel", "Plástico fino"], "O metal aguenta o **calor** do fogão.", "🍳"),
            mc("Qual o melhor material para uma **toalha**?", ["Tecido", "Vidro", "Metal"], "O tecido é macio e **absorve** a água.", "🛁"),
            separar("De que material é feito?", ["Madeira", "Metal", "Vidro"],
                    [("lápis", 0), ("cadeira de escola", 0), ("prego", 1), ("moeda", 1), ("copo de vidro", 2), ("espelho", 2)],
                    "Cada objeto usa o material certo."),
            mc("Qual material **quebra** fácil se cair?", ["Vidro", "Borracha", "Tecido"], "Cuidado com o vidro!", "💔"),
            tf("O plástico pode ser usado para fazer brinquedos.", True, "O plástico é leve e colorido."),
            fill("A borracha é feita de um material que ___.", ["estica", "quebra fácil", "é transparente"], "A borracha é **elástica**."),
        ],
    ),
    "a2-b1-ciencias-u1-m2": missao(
        [
            ("⏳", "Com o tempo, os objetos **mudaram** e os materiais também."),
            ("🪵", "**Antigamente**, muitos brinquedos eram de **madeira** ou **pano**. **Hoje**, muitos são de **plástico**."),
            ("📞", "O telefone antigo era de **baquelite** e tinha fio. O celular de hoje tem **vidro** e **metal**."),
        ],
        [
            mc("Antigamente, as bonecas eram muitas vezes feitas de...", ["pano", "plástico", "vidro"], "As bonecas de **pano** eram comuns.", "🪆"),
            mc("Antigamente, o ferro de passar roupa era aquecido com...", ["brasas (carvão)", "eletricidade", "pilha"], "Colocavam **brasas** dentro do ferro.", "🔥"),
            mc("Para guardar água, antes muitas casas usavam a **moringa** de...", ["barro", "plástico", "isopor"], "O barro deixa a água fresquinha.", "🏺"),
            separar("Objeto antigo ou atual?", ["Antigo", "Atual"],
                    [("telefone de disco", 0), ("lamparina", 0), ("máquina de escrever", 0), ("celular", 1), ("tablet", 1), ("lâmpada de LED", 1)],
                    "Os objetos mudam com o tempo."),
            tf("Hoje muitos brinquedos são feitos de plástico.", True, "O plástico é barato e fácil de moldar."),
            fill("Antes da lâmpada elétrica, usavam ___ para iluminar.", ["velas", "celulares", "televisões"], "Velas e lamparinas."),
        ],
    ),
    "a2-b1-ciencias-u1-m3": missao(
        [
            ("♻️", "**Sucata** são materiais que iriam para o lixo: caixas, garrafas, tampinhas, rolos de papel."),
            ("🚗", "Com criatividade, a sucata vira **brinquedo**: carrinho de caixa, chocalho de garrafa!"),
            ("✂️", "Peça ajuda a um adulto para cortar e colar."),
            desafio("construa um brinquedo com sucata (caixas, garrafas, tampinhas) junto com um adulto e tire uma foto."),
        ],
        [
            mc("Com uma garrafa PET e grãos de arroz, que brinquedo dá para fazer?", ["Chocalho", "Bicicleta", "Bola de futebol"], "Os grãos fazem barulho dentro da garrafa!", "🪇"),
            mc("Com tampinhas de garrafa, dá para fazer...", ["rodas de carrinho", "uma televisão", "uma janela"], "Tampinhas viram **rodas**!", "🚗"),
            mc("Por que usar sucata é bom?", ["Diminui o lixo e reaproveita materiais", "Faz mais lixo", "Gasta mais dinheiro"], "Reaproveitar ajuda o planeta.", "🌍"),
            separar("Pode virar brinquedo de sucata?", ["Pode", "Não é sucata"],
                    [("caixa de leite", 0), ("rolo de papel higiênico", 0), ("tampinhas", 0), ("comida fresca", 1), ("remédio", 1)],
                    "Sucata limpa vira brinquedo."),
            tf("Para cortar a sucata, devo pedir ajuda a um adulto.", True, "Tesoura e estilete precisam de cuidado."),
        ],
    ),
    # ------------------------------------------------------------ Ciências Humanas (História)
    "a2-b1-humanas-u1-m1": missao(
        [
            ("👥", "Participamos de vários **grupos**: **família**, **escola**, **vizinhança**, **amigos**."),
            ("👨‍👩‍👧", "Na **família** estão pais, irmãos, avós, tios, primos."),
            ("🏫", "Na **escola** estão professores, colegas e funcionários."),
        ],
        [
            separar("Separe as pessoas pelos grupos", ["Família", "Escola"],
                    [("vovó", 0), ("primo", 0), ("tia", 0), ("professora", 1), ("colega de sala", 1), ("diretora", 1)],
                    "Cada pessoa faz parte de um grupo."),
            separar("Separe as pessoas pelos grupos", ["Vizinhança", "Família"],
                    [("moradora da casa ao lado", 0), ("dono da padaria da rua", 0), ("irmão", 1), ("avô", 1)],
                    "Vizinhos moram perto de nós."),
            mc("A mãe da sua mãe é sua...", ["avó", "tia", "prima"], "Mãe da mãe = **avó**.", "👵"),
            mc("O filho do seu tio é seu...", ["primo", "irmão", "avô"], "Filho do tio = **primo**.", "👦"),
            tf("Uma pessoa pode fazer parte de vários grupos.", True, "Você é da família, da escola e da vizinhança!"),
            fill("Os colegas da minha sala fazem parte do grupo da ___.", ["escola", "família", "padaria"], "Grupo da **escola**."),
        ],
    ),
    "a2-b1-humanas-u1-m2": missao(
        [
            ("🤝", "O que une as pessoas de um grupo? **Interesses**, **lugares** e **objetivos** em comum."),
            ("⚽", "O time de futebol se une pelo **esporte**. O coral se une pela **música**."),
            ("❤️", "A família se une pelo **carinho** e pelo **cuidado**."),
        ],
        [
            mc("O que une as pessoas de um **time de futebol**?", ["Jogar futebol juntas", "Ter o mesmo nome", "Morar na mesma casa"], "O **esporte** une o time.", "⚽"),
            mc("O que une as pessoas de um **coral**?", ["Cantar juntas", "Jogar bola", "Cozinhar"], "A **música** une o coral.", "🎶"),
            mc("O que une os alunos de uma turma?", ["Aprender juntos na mesma sala", "Ter a mesma altura", "Usar o mesmo sapato"], "Eles estudam juntos.", "🏫"),
            ligar([("time", "esporte"), ("coral", "música"), ("turma", "estudo"), ("família", "cuidado e carinho")], "Ligue o grupo ao que une as pessoas"),
            tf("Num grupo, todas as pessoas precisam ser iguais.", False, "As pessoas são diferentes, mas têm algo em comum."),
        ],
    ),
    "a2-b1-humanas-u1-m3": missao(
        [
            ("🎭", "Cada pessoa tem **papéis** diferentes na comunidade."),
            ("👩", "A mesma pessoa pode ser **mãe** em casa, **professora** na escola e **vizinha** na rua."),
            ("🧒", "Você também tem papéis: **filho(a)**, **aluno(a)**, **amigo(a)**!"),
        ],
        [
            ligar([("professora", "ensina os alunos"), ("aluno", "estuda e aprende"), ("médico", "cuida da saúde"), ("motorista", "dirige o ônibus")], "Ligue a pessoa ao papel"),
            mc("Na escola, qual é o papel da criança?", ["Aluno", "Diretor", "Motorista"], "Na escola você é **aluno(a)**.", "🎒"),
            mc("Em casa, qual papel você tem?", ["Filho(a)", "Cozinheiro do restaurante", "Policial"], "Em casa você é **filho(a)**.", "🏠"),
            mc("A tia Rosa é **dentista**. No consultório, o papel dela é...", ["cuidar dos dentes", "vender pão", "apagar incêndios"], "Dentista cuida dos **dentes**.", "🦷"),
            tf("Uma pessoa pode ter vários papéis.", True, "Mãe, professora, vizinha... tudo ao mesmo tempo!"),
        ],
    ),
    # ------------------------------------------------------------ Ciências Humanas (Geografia)
    "a2-b1-humanas-u2-m1": missao(
        [
            ("🏘️", "No **bairro Girassol** moram famílias que vieram de **vários lugares**."),
            ("🧳", "A família de **Jô** veio da **Bahia**. A de **Ken** veio do **Japão**. A de **Lúcia** sempre morou ali."),
            ("🚚", "Mudar de um lugar para outro para viver se chama **migração**."),
        ],
        [
            mc("De onde veio a família de **Ken**?", ["Japão", "Bahia", "Do próprio bairro"], "A família de Ken veio do **Japão**.", "🇯🇵"),
            mc("De onde veio a família de **Jô**?", ["Bahia", "Japão", "Itália"], "A família de Jô veio da **Bahia**.", "🌴"),
            mc("Qual família **sempre morou** no bairro?", ["A de Lúcia", "A de Ken", "A de Jô"], "Lúcia sempre morou ali.", "🏡"),
            mc("Mudar de cidade ou país para viver se chama...", ["migração", "viagem de férias", "mudança de roupa"], "**Migração**.", "🧳"),
            tf("Num bairro podem morar famílias vindas de lugares diferentes.", True, "Isso deixa o bairro mais rico em culturas."),
            fill("Pessoas que vêm de outro lugar trazem seus ___.", ["costumes", "sapatos velhos", "nomes de rua"], "Trazem comidas, festas e costumes."),
        ],
    ),
    "a2-b1-humanas-u2-m2": missao(
        [
            ("🎉", "O Brasil tem **festas e comidas** diferentes em cada região."),
            ("🌽", "**Festa junina** é muito forte no **Nordeste**. **Bumba meu boi** também!"),
            ("🧉", "No **Sul**, o **chimarrão**. No **Norte**, o **açaí** e o **tacacá**. No **Centro-Oeste**, o **pequi**."),
        ],
        [
            ligar([("chimarrão", "Sul"), ("açaí", "Norte"), ("pequi", "Centro-Oeste"), ("acarajé", "Nordeste")], "Ligue a comida à região"),
            mc("O **chimarrão** é muito tomado em qual região?", ["Sul", "Norte", "Nordeste"], "No **Sul** do Brasil.", "🧉"),
            mc("O **acarajé** é uma comida típica de qual estado?", ["Bahia", "Paraná", "Amazonas"], "O acarajé é **baiano**.", "🌶️"),
            mc("Qual festa tem quadrilha, fogueira e milho?", ["Festa junina", "Natal", "Carnaval"], "**Festa junina**!", "🔥"),
            tf("Todas as regiões do Brasil comem as mesmas comidas.", False, "Cada região tem seus sabores."),
        ],
    ),
    "a2-b1-humanas-u2-m3": missao(
        [
            ("👵", "Toda família tem uma **origem**: lugares onde os avós e bisavós nasceram."),
            ("🗺️", "No **mapa**, podemos marcar a cidade onde cada pessoa nasceu."),
            ("❓", "Pergunte: **Em que cidade você nasceu? Por que mudou?**"),
            desafio("pergunte aos seus avós (ou a um adulto da família) em que cidade eles nasceram e marque num mapa com um adulto."),
        ],
        [
            mc("Qual pergunta ajuda a descobrir a origem da família?", ["Em que cidade você nasceu?", "Qual é a sua cor preferida?", "Você gosta de sorvete?"], "Assim descobrimos de onde viemos.", "❓"),
            mc("Onde podemos marcar a cidade em que o vovô nasceu?", ["Num mapa", "Num relógio", "Numa receita"], "O **mapa** mostra os lugares.", "🗺️"),
            mc("O vovô nasceu em **Recife** e hoje mora em **São Paulo**. Ele...", ["migrou de uma cidade para outra", "nunca saiu de casa", "mora em Recife"], "Ele **migrou**.", "🧳"),
            tf("Conhecer a origem da família faz parte da nossa história.", True, "É a história de quem veio antes de nós."),
            fill("O lugar onde uma pessoa nasceu é a sua cidade ___.", ["natal", "nova", "grande"], "Cidade **natal**."),
        ],
    ),
    # ------------------------------------------------------------ Ética
    "a2-b1-etica-u1-m1": missao(
        [
            ("💞", "**Empatia** é se colocar **no lugar do outro** e imaginar como ele se sente."),
            ("😢", "Se um colega cai e se machuca, ele pode sentir **dor** e **vergonha**."),
            ("🤗", "Quando entendemos o outro, sabemos melhor **como ajudar**."),
        ],
        [
            mc("Pedro ficou de fora do time no recreio. Como ele deve se sentir?", ["Triste", "Muito feliz", "Com sono"], "Ficar de fora deixa a gente **triste**.", "⚽"),
            mc("Luana derrubou o lanche no chão. Como ela pode se sentir?", ["Chateada", "Animada", "Orgulhosa"], "Perder o lanche deixa **chateado**.", "🥪"),
            mc("Um colega novo chegou e não conhece ninguém. Como ele pode se sentir?", ["Tímido e sozinho", "Bravo com todos", "Com fome"], "Tudo é novo para ele.", "🎒"),
            mc("O que é **empatia**?", ["Imaginar como o outro se sente", "Pensar só em mim", "Ganhar sempre"], "Empatia = **se colocar no lugar do outro**.", "💞"),
            tf("Rir de quem caiu é um jeito de ter empatia.", False, "Empatia é ajudar e perguntar se está tudo bem."),
            fill("Se eu estivesse no lugar dele, eu me sentiria ___ também.", ["triste", "pizza", "azul"], "Se colocar no lugar do outro é **empatia**."),
        ],
    ),
    "a2-b1-etica-u1-m2": missao(
        [
            ("🙌", "**Gentileza** é fazer algo bom para o outro."),
            ("🤝", "Podemos **emprestar**, **ajudar a carregar**, **convidar para brincar** ou **consolar**."),
            ("🗣️", "Palavras gentis: **por favor**, **obrigado**, **com licença**, **desculpa**."),
        ],
        [
            mc("Um colega esqueceu o lápis. O que é gentil?", ["Emprestar um lápis", "Rir dele", "Esconder o seu"], "Emprestar é gentileza.", "✏️"),
            mc("A vovó está carregando muitas sacolas. O que fazer?", ["Ajudar a carregar", "Sair correndo", "Pedir doce"], "Ajudar é gentileza!", "🛍️"),
            mc("O colega novo está sozinho no recreio. O que fazer?", ["Convidar para brincar", "Ignorar", "Mandar ele embora"], "Convidar faz o outro se sentir bem.", "🤸"),
            separar("Gentil ou não gentil?", ["Gentil", "Não gentil"],
                    [("dizer obrigado", 0), ("pedir por favor", 0), ("ajudar a arrumar", 0), ("empurrar na fila", 1), ("pegar sem pedir", 1)],
                    "Gentileza gera gentileza."),
            fill("Quando alguém me ajuda, eu digo ___.", ["obrigado", "tanto faz", "sai daqui"], "**Obrigado(a)!**"),
        ],
    ),
    "a2-b1-etica-u1-m3": missao(
        [
            ("🌟", "Hoje você vai fazer um **ato de gentileza** em casa!"),
            ("🧹", "Ideias: ajudar a pôr a mesa, arrumar os brinquedos, fazer um desenho para alguém, dar um abraço."),
            ("🎙️", "Depois, conte como foi e como a pessoa se sentiu."),
            desafio("faça uma gentileza para alguém de casa e conte em áudio o que você fez e como a pessoa reagiu."),
        ],
        [
            mc("Qual destas é uma gentileza em casa?", ["Ajudar a pôr a mesa", "Deixar a toalha molhada na cama", "Fazer bagunça"], "Ajudar em casa é gentileza.", "🍽️"),
            mc("Como a pessoa se sente ao receber uma gentileza?", ["Feliz e querida", "Brava", "Com medo"], "Gentileza deixa as pessoas **felizes**.", "😊"),
            mc("Você fez um desenho para a vovó. Isso é...", ["uma gentileza", "uma bronca", "uma tarefa da escola"], "Presentes feitos com carinho são gentileza.", "🎨"),
            tf("Gentileza só vale para estranhos, não para a família.", False, "Gentileza vale para **todos**, começando em casa."),
            fill("Ser gentil deixa o outro ___.", ["feliz", "triste", "zangado"], "Gentileza espalha alegria."),
        ],
    ),
    # ------------------------------------------------------------ Inglês
    "a2-b1-ingles-u1-m1": missao(
        [
            ("🎒", "Vamos aprender os **objetos da escola** em inglês!"),
            ("✏️", "**pencil** = lápis · **book** = livro · **eraser** = borracha"),
            ("📏", "**bag** = mochila · **ruler** = régua · **pen** = caneta"),
        ],
        [
            mc("**What is this?** ✏️", ["It's a pencil.", "It's a book.", "It's a bag."], "✏️ = **pencil**.", None),
            mc("**What is this?** 📖", ["It's a book.", "It's a ruler.", "It's an eraser."], "📖 = **book**.", None),
            mc("**What is this?** 🎒", ["It's a bag.", "It's a pen.", "It's a pencil."], "🎒 = **bag**.", None),
            mc("**What is this?** 📏", ["It's a ruler.", "It's a book.", "It's a bag."], "📏 = **ruler**.", None),
            mc("O que quer dizer **What is this?**", ["O que é isto?", "Quem é você?", "Onde está?"], "What is this = **O que é isto?**", "❓"),
            fill("It's a ___. (É uma borracha.)", ["eraser", "pencil", "ruler"], "Borracha = **eraser**."),
        ],
    ),
    "a2-b1-ingles-u1-m2": missao(
        [
            ("🎒", "**Pack your bag!** = Arrume sua mochila!"),
            ("👂", "Coloque na mochila só o que a professora pedir: **pencil, book, ruler...**"),
            ("✅", "Lembre: **pencil** = lápis · **eraser** = borracha · **notebook** = caderno"),
        ],
        [
            separar("Pack your bag: put in **pencil, book, eraser**", ["Vai na mochila 🎒", "Fica fora"],
                    [("✏️ lápis", 0), ("📖 livro", 0), ("🧽 borracha", 0), ("🍕 pizza", 1), ("⚽ bola", 1)],
                    "Só o que foi pedido: pencil, book, eraser."),
            separar("Pack your bag: put in **ruler, pen, notebook**", ["Vai na mochila 🎒", "Fica fora"],
                    [("📏 régua", 0), ("🖊️ caneta", 0), ("📓 caderno", 0), ("📖 livro", 1), ("✏️ lápis", 1)],
                    "ruler = régua, pen = caneta, notebook = caderno."),
            mc("**Put the ruler in the bag.** O que colocar?", ["📏 A régua", "📖 O livro", "✏️ O lápis"], "ruler = **régua**.", "🎒"),
            mc("O que quer dizer **notebook** aqui na escola?", ["Caderno", "Livro", "Mochila"], "notebook = **caderno**.", "📓"),
            tf("**bag** quer dizer mochila.", True, "bag = bolsa ou mochila."),
        ],
    ),
    "a2-b1-ingles-u1-m3": missao(
        [
            ("🔗", "Vamos ligar a **palavra** à **figura**!"),
            ("📚", "Revise: **pencil ✏️ · book 📖 · eraser 🧽 · bag 🎒 · ruler 📏 · pen 🖊️**"),
            ("🖍️", "E mais: **crayon** 🖍️ = giz de cera · **scissors** ✂️ = tesoura"),
        ],
        [
            ligar([("pencil", "✏️"), ("book", "📖"), ("bag", "🎒"), ("ruler", "📏")], "Ligue a palavra à figura"),
            ligar([("eraser", "🧽"), ("pen", "🖊️"), ("crayon", "🖍️"), ("scissors", "✂️")], "Ligue a palavra à figura"),
            mc("Qual figura é **scissors**?", ["✂️", "📏", "🖊️"], "scissors = **tesoura**.", None),
            mc("Como se diz **giz de cera** em inglês?", ["crayon", "pencil", "eraser"], "giz de cera = **crayon**.", "🖍️"),
            fill("I have a red ___. 🖍️", ["crayon", "bag", "book"], "🖍️ = **crayon**."),
        ],
    ),
}
