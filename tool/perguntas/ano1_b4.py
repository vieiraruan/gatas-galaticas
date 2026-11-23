"""1º ano · 4º bimestre."""
from base import desafio, fill, ligar, mc, missao, ordem, separar, tf

MISSOES = {
    # ------------------------------------------------------------ Português
    "a1-b4-portugues-u1-m1": missao(
        [
            ("🎵", "Palavras que **rimam** terminam com o **mesmo som**."),
            ("🐱", "**gato** rima com **pato**. Escute: ga-**TO**, pa-**TO**!"),
            ("✋", "**mão** rima com **pão** e com **feijão**."),
        ],
        [
            ligar([("mão", "pão"), ("gato", "pato"), ("bola", "cola"), ("janela", "panela")],
                  "Ligue as palavras que rimam"),
            ligar([("anel", "papel"), ("sapo", "trapo"), ("dedo", "medo"), ("rato", "sapato")],
                  "Ligue as palavras que rimam"),
            mc("Qual palavra rima com **GATO**?", ["PATO", "GALO", "BOLA"], "GA-TO e PA-TO terminam com o mesmo som: **TO**.", "🐱"),
            mc("Qual palavra rima com **PÃO**?", ["MÃO", "PÉ", "SOL"], "PÃO e MÃO terminam com **ÃO**.", "🍞"),
            mc("Qual palavra rima com **BOLA**?", ["COLA", "BALA", "BOTA"], "BO-LA e CO-LA terminam com **LA**.", "⚽"),
            mc("Qual palavra **NÃO** rima com **CANETA**?", ["LÁPIS", "BORBOLETA", "CHUPETA"], "CANETA, BORBOLETA e CHUPETA terminam com **ETA**. LÁPIS não!", "🖊️"),
            tf("**SAPO** rima com **TRAPO**.", True, "SA-PO e TRA-PO terminam com **PO**."),
            tf("**CASA** rima com **LUA**.", False, "CASA termina com **SA** e LUA termina com **UA**."),
            fill("O ratinho comeu o ___ que estava na mão.", ["pão", "bolo", "queijo"], "**mão** rima com **pão**!"),
        ],
    ),
    "a1-b4-portugues-u1-m2": missao(
        [
            ("🗣️", "**Parlenda** é um versinho que a gente fala brincando, com ritmo e rimas."),
            ("1️⃣", "Escute:\n**Um, dois, feijão com arroz.\nTrês, quatro, feijão no prato.**"),
            ("🎤", "Aperte 🔊 para ouvir e depois fale junto, bem alto!"),
            desafio("recite a parlenda para alguém da família e peça para gravar no celular."),
        ],
        [
            ordem("Coloque a parlenda na ordem:", ["Um, dois,", "feijão com arroz.", "Três, quatro,", "feijão no prato."],
                  "Um, dois, feijão com arroz. Três, quatro, feijão no prato."),
            fill("Um, dois, feijão com ___.", ["arroz", "pão", "leite"], "**dois** rima com **arroz**."),
            fill("Três, quatro, feijão no ___.", ["prato", "copo", "pote"], "**quatro** rima com **prato**."),
            fill("Cinco, seis, falar ___.", ["inglês", "baixinho", "alto"], "**seis** rima com **inglês**."),
            ordem("Coloque a parlenda na ordem:", ["Hoje é domingo,", "pede cachimbo.", "O cachimbo é de barro,", "bate no jarro."],
                  "Hoje é domingo, pede cachimbo. O cachimbo é de barro, bate no jarro."),
            fill("Hoje é domingo, pede ___.", ["cachimbo", "pipoca", "sorvete"], "**domingo** rima com **cachimbo**."),
            mc("Parlenda é…", ["Um versinho com ritmo para brincar", "Uma conta de somar", "Um tipo de desenho"], "A parlenda é falada brincando, com ritmo e rima.", "🗣️"),
            tf("Nas parlendas, muitas palavras rimam.", True, "As rimas deixam a parlenda gostosa de falar."),
        ],
    ),
    "a1-b4-portugues-u1-m3": missao(
        [
            ("🧺", "Uma **lista** ajuda a lembrar das coisas. Escrevemos um item embaixo do outro."),
            ("🍎", "Vamos fazer a lista do **piquenique**: só vai o que serve para o passeio!"),
            ("✉️", "Um **convite** diz **o quê**, **quando** e **onde** vai ser a festa."),
        ],
        [
            separar("Vai na cesta do piquenique?", ["🧺 Leva", "🚫 Não leva"],
                    [("🍎 Maçã", 0), ("🥪 Sanduíche", 0), ("🧃 Suco", 0), ("🛏️ Cama", 1), ("📺 Televisão", 1), ("🧻 Guardanapo", 0)],
                    "No piquenique vão comidas, bebidas e coisas leves para o passeio."),
            separar("É comida ou é brinquedo?", ["🍽️ Comida", "🧸 Brinquedo"],
                    [("🍌 Banana", 0), ("⚽ Bola", 1), ("🍞 Pão", 0), ("🪁 Pipa", 1), ("🧀 Queijo", 0), ("🪀 Ioiô", 1)],
                    "Uma lista organizada separa as coisas por tipo."),
            mc("Para que serve uma **lista**?", ["Para lembrar das coisas", "Para contar uma história", "Para cantar"], "A lista ajuda a não esquecer nada.", "📝"),
            mc("Em uma lista, os itens ficam…", ["Um embaixo do outro", "Todos misturados", "Desenhados no chão"], "Cada item numa linha deixa a lista fácil de ler.", "📋"),
            mc("O que um **convite** de aniversário precisa dizer?", ["O dia, a hora e o lugar", "A cor do bolo", "O nome do cachorro"], "Sem dia, hora e lugar ninguém chega na festa!", "🎂"),
            tf("Um aviso serve para informar alguma coisa importante.", True, "Ex.: \"Amanhã não haverá aula.\""),
            ordem("Arrume a lista de material na ordem da mochila:", ["1. Caderno", "2. Lápis", "3. Borracha"], "Listas podem ser numeradas: 1, 2, 3…"),
        ],
    ),
    # ------------------------------------------------------------ Matemática
    "a1-b4-matematica-u1-m1": missao(
        [
            ("🌅", "De **manhã** a gente acorda e toma café."),
            ("☀️", "À **tarde** brincamos e fazemos a lição."),
            ("🌙", "À **noite** jantamos e vamos **dormir**."),
        ],
        [
            ordem("Coloque o dia em ordem:", ["⏰ Acordar", "🎒 Ir para a escola", "🍽️ Jantar", "😴 Dormir"],
                  "Primeiro acordamos, depois vamos à escola, jantamos e dormimos."),
            ordem("Coloque em ordem:", ["🪥 Escovar os dentes", "👕 Vestir a roupa", "🥣 Tomar café"],
                  "Uma sequência possível da manhã."),
            ordem("O que vem primeiro?", ["🌅 Manhã", "☀️ Tarde", "🌙 Noite"], "Manhã, tarde e noite: é assim todo dia."),
            mc("O que fazemos **antes** de dormir?", ["Escovar os dentes", "Ir para a escola", "Acordar"], "Antes de dormir, escovamos os dentes.", "🪥"),
            mc("O que vem **depois** da tarde?", ["A noite", "A manhã", "O almoço de ontem"], "Depois da tarde chega a noite.", "🌙"),
            separar("Quando acontece?", ["🌅 Manhã", "🌙 Noite"],
                    [("Acordar ⏰", 0), ("Ver as estrelas ✨", 1), ("Tomar café da manhã 🥣", 0), ("Dormir 😴", 1)],
                    "Cada parte do dia tem suas atividades."),
            tf("A gente acorda à noite e dorme de manhã.", False, "Normalmente acordamos de manhã e dormimos à noite."),
        ],
    ),
    "a1-b4-matematica-u1-m2": missao(
        [
            ("📅", "A **semana** tem **7 dias**: domingo, segunda, terça, quarta, quinta, sexta e sábado."),
            ("🗓️", "O **ano** tem **12 meses**: de janeiro a dezembro."),
            ("✏️", "A data se escreve assim: **dia / mês / ano**. Exemplo: 25/12/2026."),
        ],
        [
            mc("Quantos dias tem uma semana?", ["7", "5", "10"], "Domingo, segunda, terça, quarta, quinta, sexta e sábado: 7 dias.", "📅"),
            mc("Que dia vem **depois** da segunda-feira?", ["Terça-feira", "Domingo", "Sexta-feira"], "Segunda, terça, quarta…", "📅"),
            mc("Que dia vem **antes** do sábado?", ["Sexta-feira", "Domingo", "Quarta-feira"], "…quinta, sexta, sábado.", "📅"),
            mc("Quantos meses tem um ano?", ["12", "7", "30"], "De janeiro a dezembro são 12 meses.", "🗓️"),
            mc("Qual é o **primeiro** mês do ano?", ["Janeiro", "Dezembro", "Março"], "O ano começa em janeiro.", "🎆"),
            mc("Em que mês é o **Natal**?", ["Dezembro", "Junho", "Abril"], "O Natal é no dia 25 de dezembro.", "🎄"),
            ordem("Coloque os dias em ordem:", ["Segunda", "Terça", "Quarta", "Quinta"], "Segunda, terça, quarta, quinta."),
            ordem("Coloque os meses em ordem:", ["Janeiro", "Fevereiro", "Março", "Abril"], "Janeiro, fevereiro, março, abril…"),
            tf("Sábado e domingo são o fim de semana.", True, "Em muitas escolas não tem aula no sábado e no domingo."),
            fill("Hoje é quarta-feira. Amanhã será ___.", ["quinta-feira", "terça-feira", "domingo"], "Depois da quarta vem a quinta."),
        ],
    ),
    "a1-b4-matematica-u1-m3": missao(
        [
            ("🎂", "No **calendário** podemos marcar os dias especiais, como os aniversários."),
            ("🔢", "Cada mês tem cerca de **30 dias**. Os números mostram os dias."),
            desafio("pegue um calendário e marque o aniversário de cada pessoa da família."),
        ],
        [
            mc("Para que serve o calendário?", ["Para ver os dias e os meses", "Para medir a altura", "Para pesar frutas"], "O calendário mostra os dias, as semanas e os meses.", "🗓️"),
            mc("Ana faz aniversário em **10 de maio**. Em que mês é a festa?", ["Maio", "Dezembro", "Janeiro"], "10 de maio: o mês é maio.", "🎂"),
            mc("Léo nasceu no dia **3**. Qual número marcamos no calendário?", ["3", "30", "13"], "Marcamos o dia 3.", "🎈"),
            tf("Todo mundo faz aniversário no mesmo dia.", False, "Cada pessoa tem o seu dia de aniversário."),
            ordem("Qual aniversário vem primeiro no ano?", ["🎂 Vovó: janeiro", "🎂 Papai: março", "🎂 Eu: julho"], "Janeiro vem antes de março, que vem antes de julho."),
            fill("Faço aniversário uma vez por ___.", ["ano", "dia", "semana"], "O aniversário acontece uma vez por ano."),
        ],
    ),
    "a1-b4-matematica-u2-m1": missao(
        [
            ("🪙", "No Brasil, o dinheiro é o **real**. Ele tem **moedas** e **notas** (cédulas)."),
            ("💵", "Uma nota de **R$ 2** vale o mesmo que **2 moedas de R$ 1**."),
            ("🧸", "Para comprar, juntamos o dinheiro até chegar no preço."),
        ],
        [
            {"tipo": "escolha", "pergunta": "Quanto dinheiro tem aqui?", "opcoes": ["R$ 3", "R$ 2", "R$ 5"], "correta": 0, "embaralhar": True,
             "visuais": [{"tipo": "dinheiro", "valores": [200, 100]}], "explicacao": "2 reais + 1 real = **3 reais**."},
            {"tipo": "escolha", "pergunta": "Quanto dinheiro tem aqui?", "opcoes": ["R$ 7", "R$ 5", "R$ 6"], "correta": 0, "embaralhar": True,
             "visuais": [{"tipo": "dinheiro", "valores": [500, 200]}], "explicacao": "5 reais + 2 reais = **7 reais**."},
            {"tipo": "escolha", "pergunta": "Quanto dinheiro tem aqui?", "opcoes": ["R$ 4", "R$ 3", "R$ 2"], "correta": 0, "embaralhar": True,
             "visuais": [{"tipo": "dinheiro", "valores": [200, 100, 100]}], "explicacao": "2 + 1 + 1 = **4 reais**."},
            mc("O carrinho custa **R$ 5**. Com qual dinheiro dá para pagar certinho?", ["Uma nota de R$ 5", "Uma moeda de R$ 1", "Uma nota de R$ 2"], "A nota de 5 reais paga o carrinho certinho.", "🚗"),
            mc("A bola custa **R$ 3**. Tenho **R$ 2**. Quanto falta?", ["R$ 1", "R$ 2", "R$ 5"], "2 + 1 = 3. Falta **1 real**.", "⚽"),
            mc("Quantas moedas de **R$ 1** valem uma nota de **R$ 2**?", ["2", "1", "5"], "1 + 1 = 2.", "🪙"),
            tf("Uma nota de R$ 10 vale mais que uma nota de R$ 5.", True, "10 é maior que 5."),
            separar("É moeda ou nota?", ["🪙 Moeda", "💵 Nota"],
                    [("R$ 1 redondinho", 0), ("R$ 10 de papel", 1), ("50 centavos", 0), ("R$ 20 de papel", 1)],
                    "Moedas são de metal e redondas; notas são de papel."),
        ],
    ),
    "a1-b4-matematica-u2-m2": missao(
        [
            ("✅", "**Com certeza** é o que vai acontecer sempre. Ex.: depois do dia vem a noite."),
            ("🤔", "**Talvez** é o que pode ou não acontecer. Ex.: chover amanhã."),
            ("🚫", "**Impossível** é o que nunca acontece. Ex.: um gato voar sozinho."),
        ],
        [
            separar("Vai acontecer?", ["✅ Com certeza", "🤔 Talvez", "🚫 Impossível"],
                    [("Depois de segunda vem terça", 0), ("Chover amanhã", 1), ("Um peixe andar de bicicleta", 2),
                     ("Ganhar um presente hoje", 1), ("O sol nascer amanhã", 0), ("Uma vaca voar", 2)],
                    "Algumas coisas são certas, outras podem acontecer e outras nunca acontecem."),
            mc("Jogar uma moeda e sair cara é…", ["Talvez", "Com certeza", "Impossível"], "Pode sair cara ou coroa: **talvez**.", "🪙"),
            mc("Um cachorro falar português é…", ["Impossível", "Com certeza", "Talvez"], "Cachorros latem, não falam!", "🐶"),
            mc("A noite chegar depois do dia é…", ["Com certeza", "Talvez", "Impossível"], "Isso acontece todos os dias.", "🌙"),
            mc("Tirar uma bola **azul** de uma caixa só com bolas **vermelhas** é…", ["Impossível", "Talvez", "Com certeza"], "Se só tem vermelhas, não dá para tirar azul.", "🔴"),
            tf("Comer sorvete amanhã é **talvez**.", True, "Pode acontecer ou não."),
        ],
    ),
    "a1-b4-matematica-u2-m3": missao(
        [
            ("📊", "O **gráfico de colunas** mostra quantos votos cada coisa ganhou."),
            ("📏", "A coluna **mais alta** é a que ganhou **mais votos**."),
            ("🍓", "A turma votou na fruta preferida: 🍌 5 votos, 🍎 3 votos, 🍓 7 votos."),
        ],
        [
            mc("🍌 5 votos · 🍎 3 votos · 🍓 7 votos.\nQual fruta ganhou?", ["🍓 Morango", "🍌 Banana", "🍎 Maçã"], "7 é o maior número: venceu o morango.", "📊"),
            mc("🍌 5 votos · 🍎 3 votos · 🍓 7 votos.\nQual teve **menos** votos?", ["🍎 Maçã", "🍓 Morango", "🍌 Banana"], "3 é o menor número.", "📊"),
            mc("🍌 5 votos · 🍎 3 votos.\nQuantos votos a banana teve a **mais** que a maçã?", ["2", "8", "3"], "5 − 3 = **2**.", "🍌"),
            mc("Num gráfico, a coluna mais **alta** mostra…", ["O que teve mais votos", "O que teve menos votos", "A cor preferida"], "Quanto mais votos, mais alta a coluna.", "📊"),
            mc("🐶 4 votos · 🐱 4 votos. O que aconteceu?", ["Empate", "O cachorro ganhou", "O gato ganhou"], "Mesmo número de votos é **empate**.", "🤝"),
            tf("Num gráfico de colunas, a coluna mais baixa é a que teve mais votos.", False, "A mais **alta** tem mais votos."),
            ordem("Ordene do que teve **mais** votos para o que teve **menos**: 🍓 7, 🍌 5, 🍎 3", ["🍓 Morango", "🍌 Banana", "🍎 Maçã"], "7, depois 5, depois 3."),
        ],
    ),
    # ------------------------------------------------------------ Ciências
    "a1-b4-ciencias-u1-m1": missao(
        [
            ("🌅", "De manhã o Sol **nasce** e aparece baixinho no céu."),
            ("☀️", "Perto do meio-dia o Sol fica **bem alto**."),
            ("🌇", "No fim da tarde o Sol **se põe** e depois chega a noite."),
        ],
        [
            ordem("Ordene o Sol ao longo do dia:", ["🌅 O Sol nasce", "☀️ O Sol fica bem alto", "🌇 O Sol se põe", "🌙 É noite"],
                  "O Sol nasce, sobe, se põe, e vem a noite."),
            ordem("Coloque em ordem:", ["🌅 Amanhecer", "☀️ Meio-dia", "🌇 Entardecer"], "Amanhecer, meio-dia e entardecer."),
            mc("Quando o Sol está **mais alto** no céu?", ["Perto do meio-dia", "À noite", "Bem cedinho"], "Ao meio-dia o Sol está lá no alto.", "☀️"),
            mc("O que vemos no céu à noite?", ["A Lua e as estrelas", "O Sol bem forte", "O arco-íris sempre"], "À noite aparecem a Lua e as estrelas.", "🌙"),
            tf("Quando o Sol se põe, logo começa a noite.", True, "Depois do pôr do sol escurece."),
            tf("Podemos olhar direto para o Sol sem problemas.", False, "Nunca olhe direto para o Sol: machuca os olhos!"),
        ],
    ),
    "a1-b4-ciencias-u1-m2": missao(
        [
            ("☀️", "Durante o **dia** tem a luz do Sol: brincamos, estudamos e trabalhamos."),
            ("🌙", "À **noite** fica escuro: é hora de descansar e dormir."),
            ("💤", "Dormir bem ajuda o corpo a crescer e a ficar forte!"),
        ],
        [
            separar("Dia ou noite?", ["☀️ Dia", "🌙 Noite"],
                    [("Ir para a escola 🎒", 0), ("Dormir 😴", 1), ("Brincar no parque 🛝", 0), ("Ver as estrelas ✨", 1),
                     ("Almoçar 🍽️", 0), ("Ver a Lua 🌕", 1)],
                    "Cada atividade tem seu momento."),
            mc("Quando é a melhor hora para dormir?", ["À noite", "Na hora do almoço", "Na hora da escola"], "A noite é o momento de descansar.", "😴"),
            mc("O que ilumina o dia?", ["O Sol", "A Lua", "A lanterna"], "A luz do dia vem do Sol.", "☀️"),
            mc("Por que dormimos?", ["Para descansar o corpo", "Para ficar com fome", "Para ficar cansados"], "Dormir recupera as energias.", "💤"),
            tf("À noite fica mais escuro porque não vemos o Sol.", True, "O Sol está iluminando o outro lado da Terra."),
            tf("As pessoas dormem só durante o dia.", False, "Normalmente dormimos à noite."),
        ],
    ),
    "a1-b4-ciencias-u1-m3": missao(
        [
            ("🦉", "Alguns animais ficam **acordados à noite**: a coruja, o morcego e o vaga-lume."),
            ("🐓", "Outros são **do dia**: o galo canta quando o Sol nasce, a borboleta voa de dia."),
            ("👀", "Os bichos da noite enxergam ou escutam muito bem no escuro."),
        ],
        [
            ligar([("🦉 Coruja", "🌙 Noite"), ("🐓 Galo", "☀️ Dia")], "Ligue o bicho ao período em que está mais ativo"),
            separar("Bicho do dia ou da noite?", ["☀️ Dia", "🌙 Noite"],
                    [("🦉 Coruja", 1), ("🐓 Galo", 0), ("🦇 Morcego", 1), ("🦋 Borboleta", 0), ("✨ Vaga-lume", 1), ("🐝 Abelha", 0)],
                    "Coruja, morcego e vaga-lume são da noite. Galo, borboleta e abelha, do dia."),
            mc("Qual animal canta quando o dia nasce?", ["🐓 Galo", "🦉 Coruja", "🦇 Morcego"], "O galo canta de manhãzinha: có-có-ri-có!", "🌅"),
            mc("Qual animal **brilha** no escuro?", ["✨ Vaga-lume", "🐶 Cachorro", "🐟 Peixe"], "O vaga-lume tem uma luzinha no corpo.", "🌙"),
            mc("Quando o morcego sai para voar?", ["À noite", "Ao meio-dia", "Nunca"], "O morcego é um animal noturno.", "🦇"),
            tf("A coruja dorme à noite e caça de dia.", False, "A coruja caça à noite."),
        ],
    ),
    # ------------------------------------------------------------ Ciências Humanas (História)
    "a1-b4-humanas-u1-m1": missao(
        [
            ("🪀", "Antigamente, as crianças brincavam de **pião**, **peteca**, **amarelinha** e **pipa**."),
            ("🎮", "Hoje também existem **videogame** e jogos no celular."),
            ("🤝", "Muitas brincadeiras antigas continuam divertidas até hoje!"),
        ],
        [
            separar("Brincadeira de antigamente ou de hoje?", ["👴 Antigamente", "📱 Hoje"],
                    [("🪀 Pião", 0), ("🎮 Videogame", 1), ("🏸 Peteca", 0), ("📱 Jogo no celular", 1), ("🪁 Pipa", 0), ("💻 Jogo no computador", 1)],
                    "Pião, peteca e pipa existem há muito tempo. Videogame e celular são de hoje."),
            ligar([("🪀 Pião", "gira no chão"), ("🪁 Pipa", "voa com o vento"), ("🏸 Peteca", "bate com a mão"), ("⚽ Bola", "chuta com o pé")],
                  "Ligue o brinquedo ao jeito de brincar"),
            mc("Qual destas brincadeiras o vovô podia brincar quando era criança?", ["Amarelinha", "Videogame", "Tablet"], "A amarelinha é bem antiga!", "👴"),
            mc("De que precisamos para brincar de **pipa**?", ["Vento", "Água", "Neve"], "A pipa sobe com o vento.", "🪁"),
            tf("Pular corda é uma brincadeira antiga que ainda brincamos hoje.", True, "Algumas brincadeiras passam de geração em geração."),
            tf("Há 100 anos as crianças já jogavam videogame.", False, "O videogame é uma invenção bem mais recente."),
        ],
    ),
    "a1-b4-humanas-u1-m2": missao(
        [
            ("👵", "Os adultos da família também foram crianças e têm muitas histórias para contar."),
            ("🎤", "Numa **entrevista** a gente faz perguntas e **escuta** com atenção."),
            desafio("pergunte a um adulto: \"Do que você brincava quando era criança?\" e peça para gravar a resposta."),
        ],
        [
            mc("Numa entrevista, o que fazemos?", ["Fazemos perguntas e escutamos", "Só falamos sem parar", "Dormimos"], "Perguntar e escutar com atenção!", "🎤"),
            mc("Qual é uma boa pergunta para a vovó?", ["Do que você brincava quando era criança?", "Qual é a cor do céu?", "Quanto é 1 + 1?"], "Assim aprendemos sobre o passado da família.", "👵"),
            ordem("Coloque a entrevista em ordem:", ["👋 Cumprimentar", "❓ Fazer a pergunta", "👂 Escutar a resposta", "🙏 Agradecer"],
                  "Cumprimentar, perguntar, escutar e agradecer."),
            tf("Os adultos também já foram crianças.", True, "E brincavam muito!"),
            tf("Durante a entrevista devemos interromper a pessoa toda hora.", False, "O bom entrevistador espera a pessoa terminar."),
        ],
    ),
    "a1-b4-humanas-u1-m3": missao(
        [
            ("🎉", "Festas são momentos de **celebrar** juntos com a família, a escola e os amigos."),
            ("🔥", "Na **festa junina** tem fogueira, bandeirinhas, quadrilha e pipoca."),
            ("🎂", "No **aniversário** tem bolo, velas e parabéns!"),
        ],
        [
            ligar([("🎂 Bolo com velas", "Aniversário"), ("🔥 Fogueira", "Festa junina"), ("🎄 Árvore enfeitada", "Natal"), ("🥚 Ovo de chocolate", "Páscoa")],
                  "Ligue o símbolo à festa"),
            mc("Em qual festa tem **quadrilha** e **bandeirinhas**?", ["Festa junina", "Aniversário", "Carnaval"], "A festa junina tem quadrilha e bandeirinhas.", "🎏"),
            mc("O que cantamos no aniversário?", ["Parabéns", "Ciranda", "Hino de Natal"], "Parabéns pra você!", "🎂"),
            mc("Qual festa usa **fantasias** e **confete**?", ["Carnaval", "Natal", "Páscoa"], "No carnaval tem fantasia e confete.", "🎭"),
            tf("O Natal acontece em dezembro.", True, "No dia 25 de dezembro."),
            separar("É festa da escola ou da família?", ["🏫 Escola", "🏠 Família"],
                    [("Festa junina da turma", 0), ("Aniversário da vovó", 1), ("Formatura", 0), ("Almoço de domingo", 1)],
                    "Celebramos em muitos lugares diferentes."),
        ],
    ),
    # ------------------------------------------------------------ Ciências Humanas (Geografia)
    "a1-b4-humanas-u2-m1": missao(
        [
            ("🥵", "No **calor** usamos roupas leves: camiseta, bermuda e boné."),
            ("🥶", "No **frio** usamos casaco, gorro e meia."),
            ("☔", "Na **chuva** usamos capa, galocha e guarda-chuva."),
        ],
        [
            separar("Que roupa usar?", ["🥵 Calor", "🥶 Frio", "☔ Chuva"],
                    [("🩳 Bermuda", 0), ("🧥 Casaco", 1), ("☂️ Guarda-chuva", 2), ("🧢 Boné", 0), ("🧣 Cachecol", 1), ("🥾 Galocha", 2)],
                    "A roupa certa ajuda o corpo a ficar confortável."),
            mc("Está chovendo forte. O que levar?", ["☂️ Guarda-chuva", "🕶️ Óculos de sol", "🩴 Chinelo de praia"], "O guarda-chuva protege da chuva.", "🌧️"),
            mc("Está muito frio. O que vestir?", ["🧥 Casaco", "🩳 Bermuda", "👙 Roupa de banho"], "O casaco esquenta o corpo.", "❄️"),
            mc("Dia de sol forte na praia. O que usar?", ["Protetor solar e boné", "Gorro e luva", "Capa de chuva"], "Protetor e boné protegem do sol.", "🏖️"),
            tf("No calor é bom tomar bastante água.", True, "Beber água ajuda o corpo no calor."),
            tf("No frio usamos bermuda e chinelo.", False, "No frio usamos roupas quentinhas."),
        ],
    ),
    "a1-b4-humanas-u2-m2": missao(
        [
            ("🏘️", "No bairro muitas pessoas **trabalham** para ajudar a comunidade."),
            ("🩺", "Cada profissão usa **instrumentos** de trabalho."),
            ("🙏", "Todos os trabalhos são importantes!"),
        ],
        [
            ligar([("👩‍⚕️ Médica", "🩺 Estetoscópio"), ("👨‍🍳 Cozinheiro", "🍳 Panela"), ("👩‍🏫 Professora", "📚 Livro"), ("👨‍🚒 Bombeiro", "🧯 Mangueira")],
                  "Ligue o profissional ao instrumento"),
            ligar([("💇 Cabeleireira", "✂️ Tesoura"), ("👨‍🌾 Agricultor", "🌱 Enxada"), ("📮 Carteiro", "✉️ Cartas"), ("🧑‍🔧 Mecânico", "🔧 Chave")],
                  "Ligue o profissional ao instrumento"),
            mc("Quem apaga incêndios?", ["Bombeiro", "Padeiro", "Carteiro"], "O bombeiro apaga o fogo e salva pessoas.", "🚒"),
            mc("Quem faz o pão?", ["Padeiro", "Dentista", "Motorista"], "O padeiro faz o pão bem cedinho.", "🥖"),
            mc("Quem cuida dos nossos dentes?", ["Dentista", "Pedreiro", "Pintor"], "O dentista cuida dos dentes.", "🦷"),
            tf("O gari ajuda a manter a rua limpa.", True, "O gari recolhe o lixo e varre as ruas."),
        ],
    ),
    "a1-b4-humanas-u2-m3": missao(
        [
            ("🌦️", "O **tempo** muda: tem dia de **sol**, de **chuva**, de **vento** e de **frio**."),
            ("🔎", "Olhando o céu podemos observar como está o tempo."),
            desafio("durante uma semana, olhe o céu todo dia e anote se fez sol ☀️, chuva 🌧️ ou frio 🥶."),
        ],
        [
            ligar([("☀️", "Sol"), ("🌧️", "Chuva"), ("🌬️", "Vento"), ("❄️", "Frio")], "Ligue o símbolo ao tempo"),
            mc("O céu está cheio de nuvens escuras. O que pode acontecer?", ["Chover", "Nevar doce", "Ficar sem céu"], "Nuvens escuras costumam trazer chuva.", "⛈️"),
            mc("As folhas das árvores estão balançando muito. Está…", ["Ventando", "Nevando", "De noite"], "O vento balança as folhas.", "🍃"),
            mc("Depois da chuva, às vezes aparece…", ["O arco-íris", "A neve", "A Lua cheia"], "Sol + gotinhas de chuva = arco-íris.", "🌈"),
            separar("Bom para fazer com sol ou com chuva?", ["☀️ Sol", "🌧️ Chuva"],
                    [("Ir à praia", 0), ("Pular nas poças de galocha", 1), ("Soltar pipa", 0), ("Ler um livro em casa", 1)],
                    "O tempo muda o que a gente faz."),
            tf("O tempo é sempre igual todos os dias.", False, "O tempo muda: tem dia de sol, chuva, vento…"),
        ],
    ),
}

MISSOES.update({
    # ------------------------------------------------------------ Ética
    "a1-b4-etica-u1-m1": missao(
        [
            ("🗑️", "Lixo tem lugar certo: a **lixeira**!"),
            ("🌳", "Lixo no chão suja a praça, entope bueiros e machuca os bichos."),
            ("💪", "Se cada um faz a sua parte, a praça fica **limpinha** para todo mundo."),
        ],
        [
            mc("Você terminou a pipoca na praça. Onde vai o saquinho?", ["Na lixeira", "No chão", "Na grama"], "Lixo vai na **lixeira**!", "🍿"),
            mc("Não tem lixeira perto. O que fazer?", ["Guardar o lixo e jogar depois", "Jogar no chão", "Esconder atrás da árvore"], "Guardamos e jogamos fora quando acharmos uma lixeira.", "🎒"),
            separar("Onde vai cada coisa?", ["Lixeira", "Pode ficar na praça"],
                    [("casca de banana", 0), ("papel de bala", 0), ("garrafa vazia", 0), ("banco", 1), ("árvore", 1), ("flor", 1)],
                    "Lixo na lixeira. O banco, a árvore e a flor são da praça!"),
            tf("Lixo no chão pode machucar os animais.", True, "Os bichos podem engolir ou se enroscar no lixo."),
            tf("Só o gari precisa cuidar da limpeza da praça.", False, "Cuidar da praça é tarefa de **todos**."),
            fill("Quando vejo lixo, eu jogo na ___.", ["lixeira", "rua", "piscina"], "Lugar de lixo é na **lixeira**."),
        ],
    ),
    "a1-b4-etica-u1-m2": missao(
        [
            ("💧", "A água limpa é **preciosa**. Não podemos desperdiçar!"),
            ("🪥", "Ao escovar os dentes, **feche a torneira**."),
            ("🚿", "Banho rápido também economiza água."),
        ],
        [
            mc("Enquanto escova os dentes, o que fazer com a torneira?", ["Fechar", "Deixar aberta", "Abrir mais"], "Torneira fechada economiza muita água.", "🪥"),
            mc("Viu uma torneira pingando na escola. O que fazer?", ["Avisar um adulto", "Fingir que não viu", "Abrir mais"], "Um adulto pode consertar ou fechar.", "🚰"),
            mc("Qual banho gasta **menos** água?", ["Banho rapidinho", "Banho de uma hora", "Banho com o chuveiro sempre ligado brincando"], "Banho rápido = menos água gasta.", "🚿"),
            separar("Economiza ou desperdiça?", ["Economiza", "Desperdiça"],
                    [("fechar a torneira", 0), ("banho rápido", 0), ("regar com regador", 0), ("torneira aberta sem usar", 1), ("brincar com a mangueira", 1)],
                    "Usar só o necessário é economizar."),
            tf("A água nunca vai acabar, então posso gastar à vontade.", False, "A água limpa pode faltar. Vamos cuidar!"),
        ],
    ),
    "a1-b4-etica-u1-m3": missao(
        [
            ("🦸", "Você é um **Guardião do Planeta**!"),
            ("💡", "Luz acesa sem ninguém no cômodo é **energia desperdiçada**."),
            ("👆", "Ao sair do quarto, apague a luz e desligue a TV que ninguém está vendo."),
            desafio("passe pela casa com um adulto e apague as luzes que ninguém está usando. Quantas você apagou?"),
        ],
        [
            mc("Saí do quarto e a luz ficou acesa. O que fazer?", ["Apagar a luz", "Deixar acesa", "Acender outra"], "Apagar a luz economiza energia.", "💡"),
            mc("A TV está ligada e ninguém está vendo. O que fazer?", ["Desligar", "Aumentar o volume", "Deixar ligada"], "TV ligada sem ninguém gasta energia.", "📺"),
            mc("De dia, com o sol entrando pela janela, precisamos de luz acesa?", ["Não, a luz do sol ilumina", "Sim, sempre", "Sim, todas as luzes"], "Abrir a janela e usar a luz do sol economiza energia.", "☀️"),
            tf("Apagar as luzes que ninguém usa ajuda o planeta.", True, "Economizar energia é cuidar do planeta."),
            fill("O Guardião do Planeta ___ a luz ao sair.", ["apaga", "acende", "quebra"], "Ele **apaga** a luz!"),
        ],
    ),
    # ------------------------------------------------------------ Inglês
    "a1-b4-ingles-u1-m1": missao(
        [
            ("🇬🇧", "Vamos aprender os **animais em inglês**!"),
            ("🐶", "**dog** = cachorro · **cat** = gato · **bird** = pássaro"),
            ("🐟", "**fish** = peixe · **cow** = vaca · **duck** = pato"),
        ],
        [
            ligar([("dog", "🐶"), ("cat", "🐱"), ("bird", "🐦"), ("fish", "🐟")], "Ligue a palavra ao animal"),
            ligar([("cow", "🐮"), ("duck", "🦆"), ("pig", "🐷"), ("horse", "🐴")], "Ligue a palavra ao animal"),
            mc("Como se diz **gato** em inglês?", ["cat", "dog", "cow"], "Gato = **cat**.", "🐱"),
            mc("Como se diz **cachorro** em inglês?", ["dog", "duck", "fish"], "Cachorro = **dog**.", "🐶"),
            mc("Qual animal é **fish**?", ["🐟", "🐦", "🐷"], "**fish** = peixe.", None),
            mc("Qual animal é **bird**?", ["🐦", "🐮", "🐱"], "**bird** = pássaro.", None),
            tf("**cow** quer dizer vaca.", True, "Cow = vaca. Moo!"),
        ],
    ),
    "a1-b4-ingles-u1-m2": missao(
        [
            ("🔊", "Os animais fazem sons! Em inglês eles também \"falam\"."),
            ("🐮", "A **cow** (vaca) faz **moo**. O **dog** (cachorro) faz **woof**."),
            ("🐱", "O **cat** (gato) faz **meow**. O **duck** (pato) faz **quack**."),
        ],
        [
            mc("Who says **moo**? (Quem faz moo?)", ["cow 🐮", "cat 🐱", "duck 🦆"], "A vaca faz **moo**!", "🔊"),
            mc("Who says **woof**?", ["dog 🐶", "cow 🐮", "fish 🐟"], "O cachorro faz **woof**!", "🔊"),
            mc("Who says **meow**?", ["cat 🐱", "dog 🐶", "pig 🐷"], "O gato faz **meow**!", "🔊"),
            mc("Who says **quack**?", ["duck 🦆", "cow 🐮", "cat 🐱"], "O pato faz **quack**!", "🔊"),
            ligar([("moo", "cow"), ("woof", "dog"), ("meow", "cat"), ("quack", "duck")], "Ligue o som ao animal"),
            tf("O **fish** (peixe) faz **woof**.", False, "Quem faz woof é o **dog**. O peixe não late!"),
        ],
    ),
    "a1-b4-ingles-u1-m3": missao(
        [
            ("🗣️", "Agora é a sua vez de **falar em inglês**!"),
            ("🐶", "Repita em voz alta: **dog** (dóg), **cat** (két), **bird** (bârd)."),
            ("🐮", "Mais: **cow** (cáu), **duck** (dâk), **fish** (fích)."),
            desafio("fale o nome de 5 animais em inglês para alguém da família e peça para gravar no celular."),
        ],
        [
            mc("Fale em voz alta: **dog**. Que animal é?", ["Cachorro", "Gato", "Peixe"], "Dog = cachorro.", "🐶"),
            mc("Fale em voz alta: **duck**. Que animal é?", ["Pato", "Vaca", "Pássaro"], "Duck = pato.", "🦆"),
            mc("Fale em voz alta: **horse**. Que animal é?", ["Cavalo", "Porco", "Gato"], "Horse = cavalo.", "🐴"),
            ligar([("🐱", "cat"), ("🐷", "pig"), ("🐦", "bird"), ("🐮", "cow")], "Ligue o animal ao nome em inglês"),
            fill("A vaca em inglês é ___.", ["cow", "cat", "dog"], "Vaca = **cow**."),
        ],
    ),
})
