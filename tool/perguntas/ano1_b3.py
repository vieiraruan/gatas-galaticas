"""1º ano · 3º bimestre."""
from base import desafio, fill, ligar, mc, missao, ordem, separar, tf

MISSOES = {
    # ------------------------------------------------------------ Português
    "a1-b3-portugues-u1-m1": missao(
        [
            ("✍️", "Para escrever uma palavra, fale **devagar** e pense em cada som."),
            ("🐱", "**G-A-T-O**: cada som tem uma letra."),
            ("🔤", "Escolha as letras certas para montar o nome da figura!"),
        ],
        [
            mc("Como se escreve o nome desta figura? 🐱", ["GATO", "GADO", "PATO"], "G-A-T-O.", None),
            mc("Como se escreve o nome desta figura? ☀️", ["SOL", "SAL", "SOM"], "S-O-L.", None),
            mc("Como se escreve o nome desta figura? 🦆", ["PATO", "BATO", "PITO"], "P-A-T-O.", None),
            mc("Como se escreve o nome desta figura? 🐸", ["SAPO", "SAGO", "ZAPO"], "S-A-P-O.", None),
            ordem("Monte a palavra 🦆", ["P", "A", "T", "O"], "**PATO**."),
            ordem("Monte a palavra 🦁", ["L", "E", "Ã", "O"], "**LEÃO**."),
            fill("U___A 🍇", ["V", "B", "F"], "**UVA**."),
        ],
    ),
    "a1-b3-portugues-u1-m2": missao(
        [
            ("␣", "Entre uma palavra e outra, deixamos um **espaço**."),
            ("😵", "**OGATOMIA** fica difícil de ler!"),
            ("😀", "Com espaços: **O GATO MIA**. Bem melhor!"),
        ],
        [
            mc("Como fica **OSOLBRILHA** com os espaços certos?", ["O SOL BRILHA", "OS OLBRI LHA", "O SOLBRI LHA"], "O · SOL · BRILHA.", "☀️"),
            mc("Como fica **EUGOSTODEBOLO** com os espaços certos?", ["EU GOSTO DE BOLO", "EUGOS TODE BOLO", "EU GOS TO DEBOLO"], "EU · GOSTO · DE · BOLO.", "🎂"),
            mc("Como fica **APATANADA** com os espaços certos?", ["A PATA NADA", "APA TANA DA", "A PATANA DA"], "A · PATA · NADA.", "🦆"),
            mc("Quantas palavras tem a frase **O CÃO LATE**?", ["3", "2", "8"], "O · CÃO · LATE: **3 palavras**.", "🐶"),
            mc("Quantas palavras tem a frase **A LUA É LINDA**?", ["4", "3", "11"], "A · LUA · É · LINDA.", "🌙"),
            tf("Entre as palavras de uma frase deixamos um espaço.", True, "O espaço separa as palavras."),
        ],
    ),
    "a1-b3-portugues-u1-m3": missao(
        [
            ("📖", "Agora você vai **ler sozinho**!"),
            ("👀", "Junte as letras e as sílabas: **CA** + **SA** = **CASA**."),
            ("🔗", "Leia a palavra e ligue à figura certa."),
        ],
        [
            ligar([("BOLA", "⚽"), ("CASA", "🏠"), ("PATO", "🦆"), ("LUA", "🌙")], "Leia e ligue à figura"),
            ligar([("PEIXE", "🐟"), ("UVA", "🍇"), ("FLOR", "🌸"), ("DADO", "🎲")], "Leia e ligue à figura"),
            mc("Leia: **MACACO**. Qual figura?", ["🐒", "🐘", "🐴"], "MA-CA-CO.", None),
            mc("Leia: **SAPATO**. Qual figura?", ["👞", "🧦", "🎩"], "SA-PA-TO.", None),
            mc("Leia: **BANANA**. Qual figura?", ["🍌", "🍎", "🍓"], "BA-NA-NA.", None),
            mc("Leia: **O GATO DORME**. O que o gato faz?", ["Dorme", "Come", "Corre"], "O gato **dorme**.", "😴"),
        ],
    ),
    # ------------------------------------------------------------ Matemática
    "a1-b3-matematica-u1-m1": missao(
        [
            ("➕", "**Juntar** é somar: 🍬🍬 + 🍬 = 🍬🍬🍬 (**2 + 1 = 3**)."),
            ("➖", "**Tirar** é subtrair: 🍎🍎🍎 tirando 🍎 = 🍎🍎 (**3 − 1 = 2**)."),
            ("✋", "Use os dedinhos para ajudar a contar!"),
        ],
        [
            mc("🍬🍬 + 🍬🍬🍬 = ?", ["5", "4", "6"], "2 + 3 = **5**.", None),
            mc("🍓🍓🍓🍓 + 🍓 = ?", ["5", "3", "6"], "4 + 1 = **5**.", None),
            mc("🍎🍎🍎🍎🍎 tirando 🍎🍎 = ?", ["3", "2", "7"], "5 − 2 = **3**.", None),
            mc("**4 + 4** = ?", ["8", "6", "9"], "4 + 4 = **8**.", "➕"),
            mc("**6 − 1** = ?", ["5", "7", "4"], "6 − 1 = **5**.", "➖"),
            mc("**5 + 5** = ?", ["10", "9", "55"], "5 + 5 = **10**.", "🖐️"),
            fill("3 + ___ = 5", ["2", "3", "8"], "3 + **2** = 5."),
        ],
    ),
    "a1-b3-matematica-u1-m2": missao(
        [
            ("🚜", "Bem-vindo à **fazenda**! Vamos resolver probleminhas."),
            ("🐔", "Leia com atenção: o problema pede para **juntar** ou para **tirar**?"),
            ("🧮", "Desenhe ou conte nos dedos se precisar."),
        ],
        [
            mc("Na fazenda há **3 vacas** e chegaram **2**. Quantas vacas agora?", ["5", "1", "6"], "3 + 2 = **5**.", "🐮"),
            mc("A galinha botou **6 ovos**. O fazendeiro pegou **2**. Quantos ficaram?", ["4", "8", "3"], "6 − 2 = **4**.", "🥚"),
            mc("Há **4 porcos** no chiqueiro e **4** no pasto. Quantos porcos ao todo?", ["8", "4", "6"], "4 + 4 = **8**.", "🐷"),
            mc("Havia **7 patos** no lago. **3** foram embora. Quantos ficaram?", ["4", "10", "3"], "7 − 3 = **4**.", "🦆"),
            mc("O cavalo comeu **5 cenouras** de manhã e **3** à tarde. Quantas comeu?", ["8", "2", "7"], "5 + 3 = **8**.", "🐴"),
            tf("**Chegaram mais** é um problema de juntar.", True, "Chegar mais = somar."),
        ],
    ),
    "a1-b3-matematica-u1-m3": missao(
        [
            ("⚽", "Muitos objetos parecem **figuras geométricas**."),
            ("📦", "A **bola** parece uma **esfera**. A **caixa** parece um **bloco retangular**. A **lata** parece um **cilindro**."),
            ("🔺", "Figuras **planas**: **círculo** ⚪, **quadrado** 🟥, **triângulo** 🔺, **retângulo** ▭."),
        ],
        [
            ligar([("bola", "esfera"), ("caixa de sapato", "bloco retangular"), ("lata", "cilindro"), ("chapéu de festa", "cone")], "Ligue o objeto à figura"),
            ligar([("⚪", "círculo"), ("🟥", "quadrado"), ("🔺", "triângulo")], "Ligue a figura ao nome"),
            mc("Quantos lados tem o **triângulo**?", ["3", "4", "0"], "Três lados.", "🔺"),
            mc("Qual figura **rola**?", ["Bola", "Caixa", "Dado"], "A bola é redonda.", "⚽"),
            mc("Qual objeto tem forma de **círculo**?", ["Moeda", "Livro", "Porta"], "A moeda é redonda.", "🪙"),
            tf("O quadrado tem 4 lados iguais.", True, "Quatro lados do mesmo tamanho."),
        ],
    ),
    # ------------------------------------------------------------ Ciências
    "a1-b3-ciencias-u1-m1": missao(
        [
            ("🪵", "Os objetos são feitos de **materiais**: **madeira**, **metal**, **plástico**, **vidro**, **papel**."),
            ("🥄", "A **colher** pode ser de metal. O **lápis** é de madeira. O **copo** pode ser de vidro."),
            ("📄", "O **caderno** é de papel. O **balde** é de plástico."),
        ],
        [
            separar("De que é feito?", ["Madeira", "Metal", "Plástico"],
                    [("lápis", 0), ("cadeira de madeira", 0), ("colher", 1), ("chave", 1), ("balde", 2), ("garrafa PET", 2)],
                    "Cada objeto tem o seu material."),
            separar("De que é feito?", ["Vidro", "Papel"],
                    [("janela", 0), ("copo de vidro", 0), ("caderno", 1), ("livro", 1), ("caixa de papelão", 1)],
                    "Vidro e papel são muito usados."),
            mc("O **livro** é feito de...", ["papel", "vidro", "metal"], "Livro = **papel**.", "📖"),
            mc("A **panela** costuma ser feita de...", ["metal", "papel", "madeira"], "Panela = **metal**.", "🍳"),
            tf("O lápis é feito de madeira.", True, "Madeira por fora e grafite dentro."),
        ],
    ),
    "a1-b3-ciencias-u1-m2": missao(
        [
            ("🪨", "**Duro**: não amassa fácil (pedra, colher). **Mole**: amassa fácil (algodão, massinha)."),
            ("🪟", "**Transparente**: dá para ver através (vidro da janela)."),
            ("🧽", "**Liso** ou **áspero**? **Leve** ou **pesado**? Os materiais têm características!"),
        ],
        [
            mc("Qual é **mole**?", ["Algodão", "Pedra", "Colher"], "O algodão amassa fácil.", "☁️"),
            mc("Qual é **duro**?", ["Pedra", "Travesseiro", "Massinha"], "A pedra não amassa.", "🪨"),
            mc("Qual é **transparente**?", ["Vidro da janela", "Porta de madeira", "Parede"], "Dá para ver através do vidro.", "🪟"),
            mc("Qual é **áspero**?", ["Lixa", "Vidro", "Seda"], "A lixa arranha!", "🧱"),
            separar("Duro ou mole?", ["Duro", "Mole"],
                    [("tijolo", 0), ("moeda", 0), ("almofada", 1), ("esponja", 1), ("pão fresco", 1)],
                    "Aperte para descobrir!"),
            tf("Uma pena é mais leve que uma pedra.", True, "A pena é bem leve."),
        ],
    ),
    "a1-b3-ciencias-u1-m3": missao(
        [
            ("🔍", "Vamos fazer uma **caça aos materiais** em casa!"),
            ("🧸", "Procure **3 objetos de plástico** e **3 de madeira**."),
            ("♻️", "Quando um objeto não serve mais, descarte no lugar certo ou **reaproveite**!"),
            desafio("ache em casa 3 objetos de plástico e 3 de madeira e mostre para um adulto."),
        ],
        [
            separar("Plástico ou madeira?", ["Plástico", "Madeira"],
                    [("pote de sorvete", 0), ("brinquedo de montar", 0), ("escova de dentes", 0), ("colher de pau", 1), ("prendedor de madeira", 1), ("tábua de cortar", 1)],
                    "Você achou esses em casa?"),
            mc("Um pote de plástico vazio pode ser...", ["reaproveitado para guardar coisas", "jogado no rio", "queimado"], "Reaproveitar ajuda o planeta.", "♻️"),
            mc("A colher de pau é feita de...", ["madeira", "plástico", "vidro"], "**Madeira**.", "🥄"),
            tf("Plástico deve ir para a lixeira de reciclável.", True, "Plástico pode ser reciclado."),
            fill("A mesa de madeira veio das ___.", ["árvores", "pedras", "nuvens"], "Madeira vem das **árvores**."),
        ],
    ),
    # ------------------------------------------------------------ Ciências Humanas (História)
    "a1-b3-humanas-u1-m1": missao(
        [
            ("🏠", "Em **casa** dormimos, tomamos banho e comemos com a família."),
            ("🏫", "Na **escola** aprendemos, lemos, brincamos no recreio e fazemos amigos."),
            ("🤔", "Algumas coisas acontecem nos **dois** lugares, como comer e brincar!"),
        ],
        [
            separar("Casa ou escola?", ["Casa", "Escola"],
                    [("cama", 0), ("chuveiro", 0), ("sofá", 0), ("quadro-negro", 1), ("carteira", 1), ("recreio", 1)],
                    "Cada lugar tem suas coisas."),
            mc("Onde fica a **sala de aula**?", ["Na escola", "Em casa", "No mercado"], "Na **escola**.", "🏫"),
            mc("Onde dormimos à noite?", ["Em casa", "Na escola", "No parque"], "Em **casa**.", "🛏️"),
            mc("O que podemos fazer em casa **e** na escola?", ["Comer e brincar", "Tomar banho de chuveiro", "Ter aula com a professora"], "Comemos e brincamos nos dois lugares!", "🍎"),
            tf("Na escola temos o recreio.", True, "Hora de brincar!"),
        ],
    ),
    "a1-b3-humanas-u1-m2": missao(
        [
            ("👩‍🏫", "Muitas pessoas **trabalham na escola**!"),
            ("📚", "A **professora** ensina. A **diretora** cuida da escola toda. A **merendeira** prepara a comida."),
            ("🧹", "O **porteiro** cuida da entrada e o pessoal da **limpeza** deixa tudo limpinho."),
        ],
        [
            ligar([("professora", "ensina"), ("merendeira", "prepara a merenda"), ("porteiro", "cuida da entrada"), ("diretora", "cuida da escola toda")], "Ligue quem trabalha na escola ao que faz"),
            mc("Quem prepara a **merenda**?", ["Merendeira", "Professora", "Porteiro"], "A **merendeira**.", "🍲"),
            mc("Quem **ensina** a ler e escrever?", ["Professora", "Porteiro", "Motorista"], "A **professora**.", "👩‍🏫"),
            mc("Como devemos tratar quem trabalha na escola?", ["Com respeito e educação", "Com grosseria", "Ignorar"], "Todos merecem respeito.", "🤝"),
            tf("Todas as pessoas que trabalham na escola são importantes.", True, "Cada uma ajuda de um jeito."),
        ],
    ),
    "a1-b3-humanas-u1-m3": missao(
        [
            ("🎒", "Todos temos **responsabilidades**: coisas que **cabem a nós** fazer."),
            ("📚", "Na escola: cuidar do material, fazer a lição, respeitar os colegas."),
            ("🤝", "Um bom colega **ajuda**, **divide** e **escuta**."),
        ],
        [
            separar("Atitude de bom colega?", ["Bom colega", "Não é legal"],
                    [("emprestar o lápis", 0), ("ajudar a guardar", 0), ("ouvir quem fala", 0), ("rasgar o caderno do outro", 1), ("rir de quem errou", 1)],
                    "Bons colegas cuidam uns dos outros."),
            mc("Qual é uma responsabilidade sua na escola?", ["Cuidar do meu material", "Dirigir o ônibus", "Fazer a merenda"], "Cuidar das suas coisas.", "🎒"),
            mc("Um colega não achou a borracha. O que fazer?", ["Emprestar a minha", "Esconder a minha", "Rir"], "Ajudar é atitude de bom colega.", "🧽"),
            mc("A professora está explicando. O que fazer?", ["Prestar atenção", "Conversar alto", "Sair correndo"], "Ouvir é respeitar.", "👂"),
            tf("Fazer a lição de casa é uma responsabilidade do aluno.", True, "É com você!"),
        ],
    ),
    # ------------------------------------------------------------ Ciências Humanas (Geografia)
    "a1-b3-humanas-u2-m1": missao(
        [
            ("🐰", "Ajude o **coelho** a chegar até a **cenoura**!"),
            ("⬆️", "Use as **setas**: ⬆️ para cima · ⬇️ para baixo · ⬅️ para a esquerda · ➡️ para a direita."),
            ("🥕", "Cada seta é **um passo**."),
        ],
        [
            mc("O coelho está **embaixo** da cenoura. Qual seta usar?", ["⬆️", "⬇️", "⬅️"], "Para subir: **⬆️**.", "🐰"),
            mc("A cenoura está à **direita** do coelho. Qual seta usar?", ["➡️", "⬅️", "⬇️"], "Para a direita: **➡️**.", "🥕"),
            mc("O coelho deu ➡️ ➡️ ➡️. Quantos passos para a direita?", ["3", "2", "1"], "Três setas = **3 passos**.", "🐾"),
            mc("O coelho deu ⬆️ e depois ⬇️. Onde ele ficou?", ["No mesmo lugar do começo", "Lá em cima", "Lá embaixo"], "Subiu e desceu: voltou!", "🔄"),
            mc("Qual caminho é **2 passos para a direita e 1 para cima**?", ["➡️ ➡️ ⬆️", "⬅️ ⬅️ ⬆️", "➡️ ⬇️ ⬇️"], "Direita, direita, cima.", "🐰"),
            tf("A seta ⬅️ leva para a esquerda.", True, "⬅️ = esquerda."),
        ],
    ),
    "a1-b3-humanas-u2-m2": missao(
        [
            ("📦", "**Dentro**: o brinquedo está na caixa. **Fora**: o brinquedo está ao lado da caixa."),
            ("🔝", "**Em cima** e **embaixo** · **perto** e **longe**."),
            ("👀", "Observe a cena com atenção!"),
        ],
        [
            mc("O peixe está no aquário. Ele está...", ["dentro", "fora", "em cima"], "O peixe vive **dentro** do aquário.", "🐠"),
            mc("O gato pulou da caixa para o chão. Agora ele está...", ["fora da caixa", "dentro da caixa", "embaixo da caixa"], "Saiu: está **fora**.", "📦"),
            mc("O pássaro está no ninho no alto da árvore. Ele está...", ["em cima da árvore", "embaixo da terra", "dentro da casa"], "Lá no **alto**.", "🐦"),
            mc("A Lua está ___ da Terra.", ["longe", "perto", "dentro"], "A Lua está muito **longe**.", "🌙"),
            separar("Dentro ou fora?", ["Dentro", "Fora"],
                    [("pé no sapato", 0), ("leite na geladeira", 0), ("carro na rua", 1), ("cachorro no quintal, fora da casinha", 1)],
                    "Dentro = no interior; fora = do lado de fora."),
            tf("A escova de dentes guardada no copo está dentro do copo.", True, "Guardada **dentro**."),
        ],
    ),
    "a1-b3-humanas-u2-m3": missao(
        [
            ("🧺", "Na história, a **Chapeuzinho** leva doces para a **vovó**."),
            ("🌲", "Ela sai de **casa**, passa pela **floresta**, atravessa a **ponte** e chega à **casa da vovó**."),
            ("🗺️", "Um **mapa** mostra o caminho visto de cima."),
            desafio("desenhe num papel o caminho da Chapeuzinho: casa, floresta, ponte e casa da vovó."),
        ],
        [
            ordem("Coloque o caminho da Chapeuzinho na ordem", ["Casa da Chapeuzinho", "Floresta", "Ponte", "Casa da vovó"], "Do começo ao fim do caminho."),
            mc("Onde a Chapeuzinho chega no fim do caminho?", ["Na casa da vovó", "Na escola", "No mercado"], "Na **casa da vovó**.", "🏡"),
            mc("O que a Chapeuzinho leva na cesta?", ["Doces para a vovó", "Pedras", "Livros da escola"], "Ela leva **doces**.", "🧺"),
            mc("Para que serve um mapa?", ["Mostrar caminhos e lugares", "Cozinhar", "Medir a febre"], "O **mapa** mostra o caminho.", "🗺️"),
            tf("No mapa, desenhamos os lugares vistos de cima.", True, "Como um passarinho vê!"),
        ],
    ),
    # ------------------------------------------------------------ Ética
    "a1-b3-etica-u1-m1": missao(
        [
            ("🤝", "**Combinados** são regras que a turma ou a família decidem juntas."),
            ("✅", "Exemplos: guardar os brinquedos, falar um de cada vez, não bater."),
            ("😊", "Seguir os combinados deixa todos mais felizes."),
        ],
        [
            separar("Pode ou não pode?", ["Pode ✅", "Não pode ❌"],
                    [("guardar os brinquedos", 0), ("esperar a vez", 0), ("pedir emprestado", 0), ("bater no colega", 1), ("gritar na sala", 1), ("rasgar o livro", 1)],
                    "Combinados ajudam todos."),
            mc("Qual é um bom combinado para a turma?", ["Falar um de cada vez", "Todo mundo gritar junto", "Jogar lixo no chão"], "Assim todos são ouvidos.", "🗣️"),
            mc("Quem faz os combinados da turma?", ["A turma, junto com a professora", "Só uma criança", "Ninguém"], "Combinado é feito **junto**.", "👩‍🏫"),
            tf("Os combinados servem para todos conviverem bem.", True, "É para isso que existem!"),
            fill("Depois de brincar, o combinado é ___ os brinquedos.", ["guardar", "jogar", "esconder"], "**Guardar**!"),
        ],
    ),
    "a1-b3-etica-u1-m2": missao(
        [
            ("⚽", "Imagine um jogo de futebol **sem regras**!"),
            ("😵", "Todo mundo pega a bola com a mão, ninguém sabe quem ganhou, todos brigam..."),
            ("📏", "As **regras** deixam o jogo **justo** e **divertido** para todos."),
        ],
        [
            mc("O que aconteceria num jogo **sem regras**?", ["Bagunça e brigas", "Todo mundo feliz e organizado", "Nada mudaria"], "Sem regras, ninguém se entende.", "😵"),
            mc("Para que servem as regras de um jogo?", ["Para o jogo ser justo para todos", "Para ninguém brincar", "Para um só ganhar sempre"], "Regras deixam o jogo **justo**.", "⚖️"),
            mc("No esconde-esconde, quem conta deve...", ["fechar os olhos", "espiar", "sair correndo"], "Sem espiar: é a regra!", "🙈"),
            mc("Perdi no jogo. O que fazer?", ["Parabenizar o amigo e jogar de novo", "Brigar", "Rasgar o jogo"], "Saber perder também é importante.", "🤝"),
            tf("Quando todos seguem as regras, o jogo fica mais divertido.", True, "Todos se divertem juntos!"),
        ],
    ),
    "a1-b3-etica-u1-m3": missao(
        [
            ("🏡", "Em casa também há **combinados**!"),
            ("🦷", "Exemplos: escovar os dentes antes de dormir, ajudar a pôr a mesa, guardar os sapatos."),
            ("🎙️", "Crie com a família um **combinado novo**!"),
            desafio("crie com sua família um combinado de casa e grave um áudio dizendo qual é."),
        ],
        [
            mc("Qual é um bom combinado de casa?", ["Guardar os brinquedos antes de dormir", "Deixar tudo no chão", "Pular no sofá de sapato"], "Ajuda a manter a casa arrumada.", "🧸"),
            mc("Quem deve seguir os combinados de casa?", ["Todos da família", "Só as crianças", "Só os adultos"], "Combinado vale para **todos**.", "👨‍👩‍👧"),
            mc("Se eu esquecer um combinado, o que fazer?", ["Pedir desculpas e lembrar da próxima vez", "Fingir que não existe", "Chorar"], "Todo mundo esquece às vezes.", "💭"),
            tf("Combinados de casa ajudam a família a viver bem.", True, "Com combinados, todos colaboram."),
            fill("Antes de dormir, eu ___ os dentes.", ["escovo", "pinto", "escondo"], "Escovar os dentes é um bom combinado!"),
        ],
    ),
    # ------------------------------------------------------------ Inglês
    "a1-b3-ingles-u1-m1": missao(
        [
            ("👨‍👩‍👧‍👦", "**My family** = minha família."),
            ("👩", "**mom** = mamãe · **dad** = papai · **brother** = irmão · **sister** = irmã"),
            ("👵", "**grandma** = vovó · **grandpa** = vovô · **baby** = bebê"),
        ],
        [
            ligar([("mom", "👩"), ("dad", "👨"), ("grandma", "👵"), ("grandpa", "👴")], "Ligue a palavra à figura"),
            ligar([("brother", "irmão"), ("sister", "irmã"), ("baby", "bebê")], "Ligue a palavra ao significado"),
            mc("Como se diz **vovó** em inglês?", ["grandma", "grandpa", "mom"], "Vovó = **grandma**.", "👵"),
            mc("Como se diz **irmão** em inglês?", ["brother", "sister", "dad"], "Irmão = **brother**.", "👦"),
            mc("O que é **dad**?", ["Papai", "Mamãe", "Vovô"], "dad = **papai**.", "👨"),
            tf("**sister** quer dizer irmã.", True, "sister = irmã."),
        ],
    ),
    "a1-b3-ingles-u1-m2": missao(
        [
            ("👂", "**This is my...** = Este(a) é meu/minha..."),
            ("👧", "**This is my sister.** = Esta é minha irmã."),
            ("👴", "**This is my grandpa.** = Este é meu vovô."),
        ],
        [
            mc("**This is my sister.** Quem é?", ["👧 irmã", "👦 irmão", "👵 vovó"], "sister = irmã.", "👂"),
            mc("**This is my grandpa.** Quem é?", ["👴 vovô", "👨 papai", "👶 bebê"], "grandpa = vovô.", "👂"),
            mc("**This is my mom.** Quem é?", ["👩 mamãe", "👵 vovó", "👧 irmã"], "mom = mamãe.", "👂"),
            mc("**This is my baby brother.** Quem é?", ["👶 irmãozinho bebê", "👴 vovô", "👨 papai"], "baby brother = irmãozinho bebê.", "👂"),
            mc("O que quer dizer **This is my dad**?", ["Este é meu papai.", "Este é meu cachorro.", "Esta é minha casa."], "dad = papai.", "👨"),
            fill("This is my ___. 👵", ["grandma", "brother", "dad"], "👵 = **grandma**."),
        ],
    ),
    "a1-b3-ingles-u1-m3": missao(
        [
            ("🌳", "Vamos desenhar a **family tree** (árvore da família)!"),
            ("🖍️", "Desenhe cada pessoa e diga em inglês: **mom, dad, brother, sister, grandma, grandpa**."),
            ("🎙️", "**This is my mom. This is my dad...**"),
            desafio("desenhe sua família e grave um áudio dizendo em inglês quem é cada um: This is my mom..."),
        ],
        [
            mc("Como apresentar a mamãe em inglês?", ["This is my mom.", "This is my dog.", "Hello, bye!"], "**This is my mom.**", "👩"),
            mc("Na árvore da família, os avós ficam...", ["em cima, como as raízes da família", "não aparecem", "embaixo de tudo, depois dos netos"], "Os avós vêm antes dos pais.", "🌳"),
            ligar([("👩", "mom"), ("👦", "brother"), ("👴", "grandpa")], "Ligue a figura ao nome em inglês"),
            mc("Como dizer **Esta é minha irmã**?", ["This is my sister.", "This is my brother.", "This is my grandma."], "irmã = **sister**.", "👧"),
            fill("This is my ___. 👨", ["dad", "mom", "sister"], "👨 = **dad**."),
        ],
    ),
}
