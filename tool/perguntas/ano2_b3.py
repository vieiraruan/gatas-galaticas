"""2º ano · 3º bimestre."""
from base import desafio, fill, ligar, mc, missao, ordem, separar, tf

MISSOES = {
    # ------------------------------------------------------------ Português
    "a2-b3-portugues-u1-m1": missao(
        [
            ("⏺️", "**Ponto final (.)**: termina uma frase que **conta** algo. **O gato dormiu.**"),
            ("❓", "**Ponto de interrogação (?)**: faz uma **pergunta**. **Você viu o gato?**"),
            ("❗", "**Ponto de exclamação (!)**: mostra **emoção** (alegria, susto, surpresa). **Que gato lindo!**"),
        ],
        [
            fill("Qual é o seu nome___", ["?", ".", "!"], "É uma **pergunta**."),
            fill("Que susto___", ["!", "?", "."], "Mostra **emoção**."),
            fill("Hoje está chovendo___", [".", "?", "!"], "Conta algo: **ponto final**."),
            fill("Você gosta de sorvete___", ["?", "!", "."], "É uma **pergunta**."),
            fill("Uau, ganhei um presente___", ["!", "?", "."], "Alegria: **exclamação**."),
            ligar([(".", "conta algo"), ("?", "pergunta"), ("!", "mostra emoção")], "Ligue o sinal ao uso"),
            tf("Toda frase começa com letra maiúscula.", True, "**O** gato, **V**ocê, **Q**ue..."),
        ],
    ),
    "a2-b3-portugues-u1-m2": missao(
        [
            ("🧩", "Uma **frase** tem palavras numa **ordem** que faz sentido."),
            ("🔠", "A frase começa com **letra maiúscula** e termina com **ponto**."),
            ("😵", "**gato o bola a pegou** não faz sentido. **O gato pegou a bola.** faz!"),
        ],
        [
            ordem("Arrume a frase", ["O", "gato", "pegou", "a bola."], "**O gato pegou a bola.**"),
            ordem("Arrume a frase", ["A", "menina", "come", "uma maçã."], "**A menina come uma maçã.**"),
            ordem("Arrume a frase", ["Nós", "vamos", "à", "praia."], "**Nós vamos à praia.**"),
            ordem("Arrume a pergunta", ["Você", "quer", "brincar", "comigo?"], "**Você quer brincar comigo?**"),
            mc("Qual frase está **certa**?", ["O sol está quente.", "o sol está quente", "O sol está quente"], "Maiúscula no começo e ponto no fim.", "☀️"),
            mc("Qual frase está **certa**?", ["Meu cachorro late alto.", "meu Cachorro late alto.", "Meu cachorro late alto"], "Começa com maiúscula e termina com ponto.", "🐶"),
        ],
    ),
    "a2-b3-portugues-u1-m3": missao(
        [
            ("📝", "O **bilhete** é uma mensagem curta."),
            ("👵", "Ele tem: **saudação** (Querida vovó,), **mensagem** e **assinatura** (o nome de quem escreveu)."),
            ("💌", "**Querida vovó, obrigada pelo bolo! Estava delicioso. Beijos, Bia.**"),
        ],
        [
            mc("No bilhete da Bia, qual é a **saudação**?", ["Querida vovó,", "Beijos, Bia.", "Estava delicioso."], "A saudação **cumprimenta**.", "👋"),
            mc("Quem **escreveu** o bilhete?", ["Bia", "A vovó", "O bolo"], "A assinatura é **Bia**.", "✍️"),
            mc("Para quem é o bilhete?", ["Para a vovó", "Para a professora", "Para o cachorro"], "**Querida vovó**.", "👵"),
            mc("Qual é a **mensagem** do bilhete?", ["Obrigada pelo bolo, estava delicioso.", "Querida vovó,", "Bia."], "A mensagem é o que se quer dizer.", "💌"),
            ordem("Monte o bilhete", ["Querido papai,", "Fui brincar na casa da Ana.", "Volto às 5 horas.", "Beijos, Léo."], "Saudação, mensagem e assinatura."),
            tf("O bilhete é um texto longo, com muitas páginas.", False, "O bilhete é **curto**."),
        ],
    ),
    # ------------------------------------------------------------ Matemática
    "a2-b3-matematica-u1-m1": missao(
        [
            ("🍪", "**Grupos iguais** podem ser contados com a **multiplicação**."),
            ("✖️", "🍪🍪 🍪🍪 🍪🍪 = **3 grupos de 2** = **3 × 2 = 6**."),
            ("➕", "É o mesmo que somar: 2 + 2 + 2 = 6."),
        ],
        [
            mc("🍎🍎 🍎🍎 🍎🍎 🍎🍎 — Quantos grupos de 2?", ["4 × 2 = 8", "2 × 2 = 4", "4 + 2 = 6"], "4 grupos de 2 = **8**.", None),
            mc("⭐⭐⭐ ⭐⭐⭐ — Quanto é?", ["2 × 3 = 6", "3 × 3 = 9", "2 + 3 = 5"], "2 grupos de 3 = **6**.", None),
            mc("**5 × 2** = ?", ["10", "7", "52"], "2 + 2 + 2 + 2 + 2 = **10**.", "✖️"),
            mc("**3 × 4** = ?", ["12", "7", "34"], "4 + 4 + 4 = **12**.", "✖️"),
            mc("Uma bicicleta tem 2 rodas. Quantas rodas têm **4 bicicletas**?", ["8", "6", "42"], "4 × 2 = **8**.", "🚲"),
            mc("Cada mão tem 5 dedos. Quantos dedos em **3 mãos**?", ["15", "8", "10"], "3 × 5 = **15**.", "🖐️"),
            fill("4 + 4 + 4 + 4 + 4 = 5 × ___", ["4", "5", "20"], "5 grupos de **4**."),
        ],
    ),
    "a2-b3-matematica-u1-m2": missao(
        [
            ("✌️", "**Dobro** é **duas vezes** o número: o dobro de 4 é **8**."),
            ("✂️", "**Metade** é dividir em **2 partes iguais**: a metade de 10 é **5**."),
            ("3️⃣", "**Triplo** é três vezes: o triplo de 3 é **9**. **Terça parte** é dividir em 3: a terça parte de 9 é **3**."),
        ],
        [
            mc("Qual é o **dobro** de **6**?", ["12", "3", "8"], "6 + 6 = **12**.", "✌️"),
            mc("Qual é a **metade** de **8**?", ["4", "16", "2"], "8 dividido em 2 = **4**.", "✂️"),
            mc("Qual é o **triplo** de **4**?", ["12", "8", "7"], "4 + 4 + 4 = **12**.", "3️⃣"),
            mc("Qual é a **terça parte** de **12**?", ["4", "6", "36"], "12 dividido em 3 = **4**.", "🍰"),
            mc("Lia tem **5 figurinhas**. Rui tem o **dobro**. Quantas Rui tem?", ["10", "7", "3"], "5 + 5 = **10**.", "🃏"),
            mc("Uma pizza tem **8 pedaços**. Comemos a **metade**. Quantos pedaços comemos?", ["4", "2", "6"], "8 ÷ 2 = **4**.", "🍕"),
            ligar([("dobro de 3", "6"), ("metade de 6", "3"), ("triplo de 2", "6 pedrinhas"), ("metade de 20", "10")], "Ligue a conta ao resultado"),
        ],
    ),
    "a2-b3-matematica-u1-m3": missao(
        [
            ("💵", "Notas e moedas podem ser **trocadas** por outras de **mesmo valor**."),
            ("🪙", "Uma nota de **R$ 2** = **2 moedas de R$ 1**. Uma nota de **R$ 10** = **2 notas de R$ 5**."),
            ("💰", "Uma moeda de **R$ 1** = **2 moedas de 50 centavos**."),
        ],
        [
            mc("Uma nota de **R$ 10** vale quantas notas de **R$ 5**?", ["2", "5", "10"], "5 + 5 = **10**.", "💵"),
            mc("Uma nota de **R$ 5** vale quantas moedas de **R$ 1**?", ["5", "2", "1"], "1 + 1 + 1 + 1 + 1 = **5**.", "🪙"),
            mc("Uma moeda de **R$ 1** vale quantas moedas de **50 centavos**?", ["2", "5", "50"], "50 + 50 = **100 centavos**.", "🪙"),
            mc("Uma nota de **R$ 20** vale quantas notas de **R$ 10**?", ["2", "10", "20"], "10 + 10 = **20**.", "💵"),
            {"tipo": "escolha", "pergunta": "Quanto dinheiro tem aqui?", "opcoes": ["R$ 10", "R$ 7", "R$ 12"], "correta": 0, "embaralhar": True,
             "visuais": [{"tipo": "dinheiro", "valores": [500, 200, 200, 100]}], "explicacao": "5 + 2 + 2 + 1 = **10 reais**."},
            {"tipo": "escolha", "pergunta": "Quanto dinheiro tem aqui?", "opcoes": ["R$ 15", "R$ 13", "R$ 25"], "correta": 0, "embaralhar": True,
             "visuais": [{"tipo": "dinheiro", "valores": [1000, 500]}], "explicacao": "10 + 5 = **15 reais**."},
            tf("Duas notas de R$ 50 valem o mesmo que uma de R$ 100.", True, "50 + 50 = 100."),
        ],
    ),
    # ------------------------------------------------------------ Ciências
    "a2-b3-ciencias-u1-m1": missao(
        [
            ("🌱", "A planta tem **raiz**, **caule**, **folhas**, **flores** e **frutos**."),
            ("🪴", "A **raiz** fica na terra e puxa a **água**. O **caule** sustenta a planta e leva a água."),
            ("🍃", "As **folhas** fazem o alimento com a **luz**. A **flor** vira **fruto**, e o fruto guarda as **sementes**."),
        ],
        [
            ligar([("raiz", "puxa água da terra"), ("caule", "sustenta a planta"), ("folha", "faz o alimento com a luz"), ("fruto", "guarda as sementes")], "Ligue a parte à função"),
            ordem("Da parte mais baixa à mais alta da árvore", ["raiz", "caule (tronco)", "galhos", "folhas"], "De baixo para cima."),
            mc("Qual parte da planta fica **embaixo da terra**?", ["Raiz", "Flor", "Folha"], "A **raiz**.", "🥕"),
            mc("A **cenoura** que comemos é qual parte da planta?", ["Raiz", "Folha", "Flor"], "Cenoura é **raiz**!", "🥕"),
            mc("A **alface** que comemos é qual parte da planta?", ["Folha", "Raiz", "Fruto"], "Alface é **folha**.", "🥬"),
            tf("A maçã é o fruto da macieira.", True, "E dentro estão as sementes."),
        ],
    ),
    "a2-b3-ciencias-u1-m2": missao(
        [
            ("🫘", "Vamos plantar um **feijão no algodão**!"),
            ("💧", "Coloque algodão **úmido** num copo, ponha o feijão e deixe perto da **luz**."),
            ("📸", "Em poucos dias, a **raiz** aparece; depois, o **caule** e as **folhas**!"),
            desafio("plante um feijão no algodão molhado e tire uma foto por dia, durante 7 dias."),
        ],
        [
            mc("O que sai **primeiro** do feijão?", ["A raiz", "A flor", "O fruto"], "A raiz aparece primeiro.", "🌱"),
            ordem("Coloque o crescimento na ordem", ["Semente de feijão", "Sai a raiz", "Sai o caulezinho", "Aparecem as folhas"], "A planta vai crescendo."),
            mc("O algodão deve ficar...", ["úmido", "seco", "pegando fogo"], "A semente precisa de **água**.", "💧"),
            mc("Onde deixar o copo?", ["Perto da janela, com luz", "Dentro do armário escuro", "Na geladeira"], "A planta precisa de **luz**.", "☀️"),
            tf("Uma semente pode virar uma planta nova.", True, "A semente guarda uma plantinha!"),
        ],
    ),
    "a2-b3-ciencias-u1-m3": missao(
        [
            ("🌞", "As plantas precisam de **água**, **luz**, **ar** e **nutrientes** do solo."),
            ("🥀", "**Sem água**, a planta **murcha** e seca."),
            ("🌑", "**Sem luz**, ela fica **amarelada**, fraca e comprida, procurando a luz."),
        ],
        [
            mc("O que acontece com uma planta **sem água**?", ["Murcha e seca", "Cresce mais", "Fica azul"], "Sem água, ela **murcha**.", "🥀"),
            mc("O que acontece com uma planta **no escuro** por muitos dias?", ["Fica amarelada e fraca", "Fica mais verde", "Dá muitas flores"], "Sem luz, não faz alimento.", "🌑"),
            separar("A planta precisa ou não?", ["Precisa", "Não precisa"],
                    [("água", 0), ("luz", 0), ("ar", 0), ("terra com nutrientes", 0), ("refrigerante", 1), ("música alta", 1)],
                    "Água, luz, ar e nutrientes."),
            mc("Por que regamos as plantas?", ["Porque elas precisam de água", "Para limpar as folhas só", "Para afogar as formigas"], "A água é essencial.", "🚿"),
            tf("Os animais também precisam de água para viver.", True, "Todos os seres vivos precisam de água."),
        ],
    ),
    # ------------------------------------------------------------ Ciências Humanas (História)
    "a2-b3-humanas-u1-m1": missao(
        [
            ("📄", "**Documentos** registram informações importantes sobre nós."),
            ("👶", "A **certidão de nascimento** mostra quando e onde nascemos e quem são nossos pais."),
            ("💉", "A **carteira de vacinação** registra as vacinas. O **RG** (identidade) mostra quem somos."),
        ],
        [
            ligar([("certidão de nascimento", "quando e onde nasci"), ("carteira de vacinação", "vacinas que tomei"), ("RG", "identidade com foto")], "Ligue o documento ao que ele mostra"),
            mc("Qual é o **primeiro** documento de uma pessoa?", ["Certidão de nascimento", "Carteira de motorista", "Passaporte"], "Ela é feita quando o bebê nasce.", "👶"),
            mc("Para saber se você tomou a vacina, olhamos...", ["a carteira de vacinação", "a certidão de casamento", "o boletim"], "Ela guarda todas as vacinas.", "💉"),
            mc("Qual documento tem **foto** e mostra quem somos?", ["RG (identidade)", "Certidão de nascimento", "Receita de bolo"], "O **RG**.", "🪪"),
            tf("Documentos contam parte da nossa história.", True, "São **fontes** sobre a nossa vida."),
        ],
    ),
    "a2-b3-humanas-u1-m2": missao(
        [
            ("🧸", "Algumas famílias **guardam objetos antigos**: o brinquedo do papai, a xícara da bisavó, uma foto..."),
            ("📜", "Esses objetos contam **histórias** e trazem **memórias**."),
            ("🎙️", "Pergunte: **De quem era? Quando foi usado? Por que foi guardado?**"),
            desafio("escolha com a família um objeto antigo guardado em casa e grave um áudio contando a história dele."),
        ],
        [
            mc("Por que as famílias guardam objetos antigos?", ["Para lembrar de histórias e pessoas queridas", "Porque são novos", "Para jogar fora depois"], "Eles guardam **memórias**.", "📦"),
            mc("Qual pergunta ajuda a descobrir a história do objeto?", ["De quem era esse objeto?", "Qual é o preço da gasolina?", "Que dia é hoje?"], "Comece por **quem** usou.", "❓"),
            mc("Um objeto antigo pode ser uma fonte...", ["histórica", "de energia", "de água"], "Objetos são **fontes históricas**.", "🏺"),
            tf("Um brinquedo do vovô pode contar como as crianças brincavam antigamente.", True, "Objetos falam do passado!"),
            fill("Objetos guardados com carinho trazem ___.", ["memórias", "sujeira", "chuva"], "**Memórias**."),
        ],
    ),
    "a2-b3-humanas-u1-m3": missao(
        [
            ("🤔", "Por que guardamos alguns objetos e descartamos outros?"),
            ("💛", "Guardamos o que tem **valor de memória** (uma foto, a primeira roupinha) ou que ainda é **útil**."),
            ("♻️", "Descartamos ou **doamos** o que não usamos mais, de forma correta."),
        ],
        [
            separar("Guardar ou descartar/doar?", ["Guardar", "Descartar ou doar"],
                    [("foto do casamento dos avós", 0), ("certidão de nascimento", 0), ("primeiro desenho do bebê", 0), ("roupa que não serve mais", 1), ("caixa de pizza usada", 1), ("brinquedo que ninguém usa", 1)],
                    "Guardamos memórias e documentos; doamos o que pode servir a outros."),
            mc("Por que guardar a **certidão de nascimento**?", ["É um documento importante", "Porque é bonita", "Para fazer origami"], "Documentos devem ser guardados.", "📄"),
            mc("Uma roupa que não serve mais, mas está boa, pode ser...", ["doada", "queimada", "jogada no rio"], "Doar ajuda outras pessoas.", "👕"),
            tf("Objetos com memórias da família podem ser guardados por muitos anos.", True, "E passados de geração em geração."),
            fill("Brinquedos em bom estado que não usamos podemos ___.", ["doar", "quebrar", "esconder"], "**Doar**!"),
        ],
    ),
    # ------------------------------------------------------------ Ciências Humanas (Geografia)
    "a2-b3-humanas-u2-m1": missao(
        [
            ("🦅", "Visto **de cima** (visão **vertical**), um objeto parece diferente!"),
            ("⚪", "Um **copo** visto de cima parece um **círculo**. Uma **mesa quadrada** parece um **quadrado**."),
            ("📐", "Visto **de lado e de cima ao mesmo tempo** é a visão **oblíqua**."),
        ],
        [
            mc("Um **copo** visto de cima parece...", ["um círculo", "um triângulo", "uma estrela"], "Vemos só a **boca redonda**.", "🥛"),
            mc("Uma **caixa de sapatos** vista de cima parece...", ["um retângulo", "um círculo", "um triângulo"], "A tampa é retangular.", "📦"),
            mc("Uma **bola** vista de cima parece...", ["um círculo", "um quadrado", "uma linha"], "De qualquer lado, um **círculo**.", "⚽"),
            mc("Quem vê as coisas de cima, como num mapa?", ["Um passarinho voando", "Uma formiga no chão", "Um peixe no rio"], "O pássaro tem a visão **vertical**.", "🐦"),
            ligar([("copo", "círculo"), ("livro", "retângulo"), ("dado", "quadrado")], "Ligue o objeto à forma vista de cima"),
            tf("Mapas e plantas mostram os lugares vistos de cima.", True, "É a **visão vertical**."),
        ],
    ),
    "a2-b3-humanas-u2-m2": missao(
        [
            ("🏫", "A **planta da sala** mostra a sala vista de cima."),
            ("🚪", "Nela aparecem a **porta**, as **janelas**, as **mesas**, o **quadro** e a **mesa da professora**."),
            ("🔑", "A **legenda** explica os símbolos: ▭ = mesa, 🚪 = porta."),
        ],
        [
            mc("Na planta da sala, os objetos aparecem...", ["vistos de cima", "vistos de lado", "em 3D"], "Planta = visão **de cima**.", "🗺️"),
            mc("Para que serve a **legenda** de uma planta?", ["Explicar o que cada símbolo significa", "Enfeitar", "Mostrar a hora"], "A legenda traduz os símbolos.", "🔑"),
            mc("A mesa da professora fica perto do quadro. Na planta, ela aparece...", ["perto do desenho do quadro", "do lado de fora da sala", "no teto"], "A planta mostra a **posição** real.", "🧑‍🏫"),
            separar("Aparece na planta da sala?", ["Aparece", "Não aparece"],
                    [("porta", 0), ("janelas", 0), ("carteiras", 0), ("o cheiro da merenda", 1), ("a música do recreio", 1)],
                    "A planta mostra objetos e lugares."),
            tf("Numa planta, uma mesa redonda é desenhada como um círculo.", True, "Vista de cima, ela é redonda."),
        ],
    ),
    "a2-b3-humanas-u2-m3": missao(
        [
            ("🏗️", "A **maquete** é uma **miniatura** de um lugar, feita com caixas e sucata."),
            ("🛏️", "Para o **quarto**: uma caixa grande é o quarto, caixinhas viram **cama**, **armário** e **mesa**."),
            ("📐", "Os objetos devem ficar nas **mesmas posições** do quarto de verdade."),
            desafio("faça uma maquete do seu quarto com caixas e sucata, junto com um adulto, e tire uma foto."),
        ],
        [
            mc("O que é uma maquete?", ["Uma miniatura de um lugar", "Uma receita", "Um tipo de dança"], "Uma **miniatura**.", "🏗️"),
            mc("Com o que podemos fazer uma maquete?", ["Caixas, papel e sucata", "Água e sabão", "Areia molhada só"], "Sucata é ótima!", "📦"),
            mc("Se a cama fica perto da janela no quarto de verdade, na maquete ela fica...", ["perto da janela também", "longe de tudo", "em cima do armário"], "A maquete copia as **posições**.", "🛏️"),
            tf("A maquete é menor que o lugar de verdade.", True, "É uma **miniatura**."),
            fill("Uma caixinha de fósforo pode virar uma ___ na maquete.", ["cama", "rua de verdade", "árvore gigante"], "Use a imaginação!"),
        ],
    ),
    # ------------------------------------------------------------ Ética
    "a2-b3-etica-u1-m1": missao(
        [
            ("👛", "Você achou uma **carteira** no chão da escola. De quem será?"),
            ("✋", "O que **não é nosso** deve ser **devolvido** ao dono."),
            ("🧑‍🏫", "Se não souber de quem é, entregue a um **adulto** (professora, secretaria)."),
        ],
        [
            mc("Achei uma carteira no pátio. O que fazer?", ["Entregar para a professora", "Ficar com ela", "Esconder no armário"], "Devolver é ser **honesto**.", "👛"),
            mc("Achei um estojo com o nome do Léo. O que fazer?", ["Devolver para o Léo", "Pegar as canetas", "Jogar fora"], "O nome mostra o dono!", "✏️"),
            mc("O caixa da padaria deu troco a mais. O que fazer?", ["Avisar e devolver", "Ficar quieto", "Sair correndo"], "Honestidade também vale com dinheiro.", "🪙"),
            tf("Ficar com algo que achamos e sabemos de quem é é honesto.", False, "O honesto é **devolver**."),
            fill("Quem devolve o que não é seu é ___.", ["honesto", "malvado", "preguiçoso"], "**Honesto**."),
        ],
    ),
    "a2-b3-etica-u1-m2": missao(
        [
            ("😬", "Todo mundo **erra** às vezes. O importante é **assumir** o erro."),
            ("🙏", "Passos: **reconhecer** o erro, **pedir desculpas**, **consertar** (se der) e **aprender**."),
            ("🏺", "Exemplo: quebrei o vaso → conto a verdade → peço desculpas → ajudo a limpar."),
        ],
        [
            ordem("Errei, e agora? Coloque os passos na ordem", ["Reconhecer que errei", "Contar a verdade", "Pedir desculpas", "Ajudar a consertar"], "Assumir e consertar."),
            ordem("Derrubei suco no caderno da colega. O que fazer?", ["Parar e ver o que aconteceu", "Pedir desculpas", "Ajudar a secar o caderno"], "Assumir o erro e ajudar."),
            mc("Quebrei o brinquedo do meu irmão sem querer. O que fazer?", ["Contar e pedir desculpas", "Esconder o brinquedo", "Dizer que foi o cachorro"], "Assumir é corajoso.", "🧸"),
            mc("Por que é bom assumir os erros?", ["As pessoas confiam mais em nós", "Para levar bronca à toa", "Não é bom"], "Assumir gera **confiança**.", "🤝"),
            tf("Errar faz parte de aprender.", True, "Erramos e aprendemos."),
        ],
    ),
    "a2-b3-etica-u1-m3": missao(
        [
            ("📖", "Leia: **Tom comeu o último biscoito e disse à irmã que tinha sido o gato. A mãe brigou com o gato. Depois, a verdade apareceu e todos ficaram chateados com Tom.**"),
            ("🤥", "A **mentira** pode prejudicar outras pessoas (e até o gato!)."),
            ("✅", "Falar a **verdade** mantém a **confiança**."),
        ],
        [
            mc("Qual foi a mentira de Tom?", ["Disse que o gato comeu o biscoito", "Disse que estava com fome", "Disse que gosta de biscoito"], "Ele culpou o **gato**.", "🐱"),
            mc("Quem foi prejudicado pela mentira?", ["O gato, que levou a bronca", "Ninguém", "O biscoito"], "O gato foi culpado sem ter feito nada.", "😿"),
            mc("O que aconteceu quando a verdade apareceu?", ["Todos ficaram chateados com Tom", "Tom ganhou um prêmio", "Nada"], "A mentira quebra a confiança.", "😞"),
            mc("O que Tom deveria ter feito?", ["Dizer a verdade", "Culpar a irmã", "Esconder o pacote"], "**Verdade** sempre.", "✅"),
            tf("Quando mentimos, as pessoas podem parar de confiar em nós.", True, "A confiança é preciosa."),
        ],
    ),
    # ------------------------------------------------------------ Inglês
    "a2-b3-ingles-u1-m1": missao(
        [
            ("🔢", "Números de **11 a 20** em inglês!"),
            ("1️⃣", "**eleven** (11), **twelve** (12), **thirteen** (13), **fourteen** (14), **fifteen** (15)"),
            ("2️⃣", "**sixteen** (16), **seventeen** (17), **eighteen** (18), **nineteen** (19), **twenty** (20)"),
        ],
        [
            mc("How many balls? ⚽⚽⚽⚽⚽⚽⚽⚽⚽⚽⚽⚽", ["twelve", "eleven", "twenty"], "12 = **twelve**.", None),
            mc("How many stars? ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐", ["fifteen", "fourteen", "sixteen"], "15 = **fifteen**.", None),
            mc("Qual número é **twenty**?", ["20", "12", "2"], "twenty = **20**.", "🔢"),
            mc("Qual número é **eleven**?", ["11", "7", "17"], "eleven = **11**.", "🔢"),
            ligar([("thirteen", "13"), ("sixteen", "16"), ("eighteen", "18"), ("nineteen", "19")], "Ligue o número em inglês ao algarismo"),
            fill("10 + 4 = ___", ["fourteen", "forty", "four"], "14 = **fourteen**."),
        ],
    ),
    "a2-b3-ingles-u1-m2": missao(
        [
            ("🧸", "**Toys** = brinquedos!"),
            ("⚽", "**ball** = bola · **doll** = boneca · **car** = carrinho · **kite** = pipa"),
            ("🧩", "**teddy bear** = ursinho · **puzzle** = quebra-cabeça · **My favorite toy is...** = Meu brinquedo favorito é..."),
        ],
        [
            mc("**My favorite toy is a kite.** Qual brinquedo?", ["🪁", "⚽", "🧸"], "kite = **pipa**.", None),
            mc("**My favorite toy is a ball.** Qual brinquedo?", ["⚽", "🪀", "🚗"], "ball = **bola**.", None),
            mc("**My favorite toy is a teddy bear.** Qual brinquedo?", ["🧸", "🪁", "🧩"], "teddy bear = **ursinho**.", None),
            ligar([("doll", "🪆"), ("car", "🚗"), ("puzzle", "🧩"), ("kite", "🪁")], "Ligue o brinquedo ao nome"),
            mc("O que quer dizer **My favorite toy**?", ["Meu brinquedo favorito", "Minha cor favorita", "Meu amigo"], "toy = brinquedo.", "💛"),
        ],
    ),
    "a2-b3-ingles-u1-m3": missao(
        [
            ("📏", "Vamos montar a **number line** (reta numérica) de 11 a 20!"),
            ("🔢", "eleven, twelve, thirteen, fourteen, fifteen..."),
            ("➡️", "...sixteen, seventeen, eighteen, nineteen, twenty!"),
        ],
        [
            ordem("Put in order", ["eleven", "twelve", "thirteen", "fourteen", "fifteen"], "11, 12, 13, 14, 15."),
            ordem("Put in order", ["sixteen", "seventeen", "eighteen", "nineteen", "twenty"], "16, 17, 18, 19, 20."),
            ordem("Put in order", ["twelve", "fifteen", "seventeen", "twenty"], "12, 15, 17, 20."),
            mc("What comes after **nineteen**?", ["twenty", "eighteen", "eleven"], "19 → **20**.", "➡️"),
            mc("What comes before **fourteen**?", ["thirteen", "fifteen", "forty"], "**13** → 14.", "⬅️"),
        ],
    ),
}
