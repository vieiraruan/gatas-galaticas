"""3º ano · 3º bimestre."""
from base import desafio, fill, ligar, mc, missao, ordem, separar, tf

MISSOES = {
    # ------------------------------------------------------------ Português
    "a3-b3-portugues-u1-m1": missao(
        [
            ("🏷️", "**Substantivo** dá nome às coisas, pessoas, animais e lugares: **gato**, **Ana**, **escola**."),
            ("🎨", "**Adjetivo** dá característica ao substantivo: gato **preto**, casa **grande**."),
            ("🏃", "**Verbo** indica ação: **correr**, **pular**, **comer**, **dormir**."),
        ],
        [
            separar("Classifique as palavras", ["Substantivo", "Adjetivo", "Verbo"],
                    [("cachorro", 0), ("mesa", 0), ("bonito", 1), ("alto", 1), ("correr", 2), ("cantar", 2)],
                    "Nome, característica ou ação."),
            mc("Em **O menino feliz pulou**, qual é o **verbo**?", ["pulou", "menino", "feliz"], "Pulou é a **ação**.", "🦘"),
            mc("Em **A flor vermelha cresceu**, qual é o **adjetivo**?", ["vermelha", "flor", "cresceu"], "Vermelha é a **característica**.", "🌹"),
            mc("Em **O gato dorme no sofá**, qual é o **substantivo**?", ["gato", "dorme", "no"], "Gato é o **nome** do animal.", "🐱"),
            fill("O cachorro ___ no quintal.", ["latiu", "bonito", "casa"], "Falta um **verbo**: latiu."),
            fill("Ganhei uma bola ___.", ["nova", "correr", "menino"], "Falta um **adjetivo**: nova."),
        ],
    ),
    "a3-b3-portugues-u1-m2": missao(
        [
            ("👾", "Vamos **descrever um monstro** com **adjetivos**!"),
            ("🟢", "O monstro **Glub** é **verde**, **peludo**, **gigante** e muito **simpático**."),
            ("✨", "Adjetivos deixam o texto mais **rico** e fácil de imaginar."),
        ],
        [
            mc("Qual palavra é um **adjetivo** para o Glub?", ["peludo", "monstro", "pular"], "Peludo é **característica**.", "👾"),
            mc("O Glub é enorme. Qual adjetivo tem **sentido parecido**?", ["gigante", "minúsculo", "pequeno"], "Enorme = **gigante**.", "📏"),
            mc("Qual é o **contrário** de **simpático**?", ["antipático", "gentil", "legal"], "Antipático é o oposto.", "😠"),
            separar("Esses adjetivos descrevem o Glub?", ["Descreve o Glub", "Não descreve"],
                    [("verde", 0), ("peludo", 0), ("gigante", 0), ("minúsculo", 1), ("careca", 1)],
                    "Glub é verde, peludo e gigante."),
            fill("O monstro tinha olhos ___ e brilhantes.", ["amarelos", "comer", "cadeira"], "Falta um **adjetivo**."),
            tf("**Simpático** é um adjetivo.", True, "Dá uma característica."),
        ],
    ),
    "a3-b3-portugues-u1-m3": missao(
        [
            ("💬", "Num **diálogo**, os **dois-pontos (:)** anunciam que alguém vai falar."),
            ("➖", "O **travessão (—)** aparece no começo da fala do personagem."),
            ("📖", "**A mãe perguntou:** \n**— Você fez a lição?** \n**— Fiz sim! — respondeu Lia.**"),
        ],
        [
            fill("O professor disse___ — Bom dia, turma!", [":", "?", "!"], "Antes da fala: **dois-pontos**."),
            mc("Para que serve o **travessão** no diálogo?", ["Marcar o começo da fala do personagem", "Terminar a história", "Fazer uma conta"], "Ele mostra **quem fala**.", "➖"),
            mc("Em **— Fiz sim! — respondeu Lia.**, quem está falando?", ["Lia", "A mãe", "O narrador"], "**respondeu Lia**.", "👧"),
            mc("Qual frase está pontuada **certa**?", ["Pedro gritou: — Gol!", "Pedro gritou — Gol:", "Pedro: gritou Gol —"], "Dois-pontos e depois travessão.", "⚽"),
            ordem("Monte o diálogo", ["O gato perguntou:", "— Tem peixe hoje?", "— Tem sim! — disse o dono."], "Anúncio, fala, resposta."),
            tf("No diálogo, cada fala nova começa numa linha com travessão.", True, "Assim sabemos que mudou quem fala."),
        ],
    ),
    # ------------------------------------------------------------ Matemática
    "a3-b3-matematica-u1-m1": missao(
        [
            ("🥋", "**Tabuada ninja**: acerte em sequência e ganhe faixas!"),
            ("✖️", "Tabuadas do **2, 3, 4, 5 e 10**."),
            ("💡", "Dica: a do **10** é só pôr um zero: 10 × 7 = **70**. A do **5** termina em **0** ou **5**."),
        ],
        [
            mc("**3 × 4** = ?", ["12", "7", "14"], "3 × 4 = **12**.", "🥋"),
            mc("**5 × 6** = ?", ["30", "11", "35"], "5 × 6 = **30**.", "🥋"),
            mc("**10 × 8** = ?", ["80", "18", "108"], "10 × 8 = **80**.", "🥋"),
            mc("**4 × 7** = ?", ["28", "24", "32"], "4 × 7 = **28**.", "🥋"),
            mc("**2 × 9** = ?", ["18", "11", "29"], "Dobro de 9 = **18**.", "🥋"),
            mc("**3 × 8** = ?", ["24", "21", "27"], "3 × 8 = **24**.", "🥋"),
            mc("**5 × 9** = ?", ["45", "40", "54"], "5 × 9 = **45**.", "🥋"),
            fill("4 × ___ = 20", ["5", "4", "6"], "4 × **5** = 20."),
        ],
    ),
    "a3-b3-matematica-u1-m2": missao(
        [
            ("🍕", "**Dividir** é repartir em **partes iguais**."),
            ("➗", "**12 pedaços para 4 amigos** → 12 ÷ 4 = **3** para cada um."),
            ("🍪", "Às vezes **sobra**: **13 biscoitos para 4** → 3 para cada e sobra **1** (resto)."),
        ],
        [
            mc("**8 pedaços** de pizza para **2 amigos**. Quanto cada um?", ["4", "6", "16"], "8 ÷ 2 = **4**.", "🍕"),
            mc("**15 balas** para **3 crianças**. Quantas cada uma?", ["5", "3", "12"], "15 ÷ 3 = **5**.", "🍬"),
            mc("**20 figurinhas** para **4 amigos**. Quantas cada um?", ["5", "4", "16"], "20 ÷ 4 = **5**.", "🃏"),
            mc("**13 biscoitos** para **4 crianças**. Quanto **sobra**?", ["1", "3", "0"], "4 × 3 = 12; sobra **1**.", "🍪"),
            mc("**10 lápis** para **3 alunos**. Quanto sobra?", ["1", "3", "0"], "3 × 3 = 9; sobra **1**.", "✏️"),
            mc("**18 ÷ 3** = ?", ["6", "5", "15"], "3 × 6 = 18.", "➗"),
            tf("Quando a divisão é exata, o resto é zero.", True, "Não sobra nada."),
        ],
    ),
    "a3-b3-matematica-u1-m3": missao(
        [
            ("✂️", "**Metade**: dividir por 2. **Terça parte**: dividir por 3. **Quarta parte**: dividir por 4."),
            ("🖐️", "**Quinta parte**: dividir por 5. **Décima parte**: dividir por 10."),
            ("🍫", "A quarta parte de 12 é **12 ÷ 4 = 3**."),
        ],
        [
            ligar([("metade de 20", "10"), ("terça parte de 9", "3"), ("quarta parte de 16", "4"), ("décima parte de 50", "5")], "Ligue a parte ao resultado"),
            ligar([("metade de 14", "7"), ("terça parte de 18", "6"), ("quinta parte de 40", "8"), ("décima parte de 90", "9")], "Ligue a parte ao resultado"),
            mc("Qual é a **quarta parte** de **20**?", ["5", "4", "10"], "20 ÷ 4 = **5**.", "🍰"),
            mc("Qual é a **quinta parte** de **25**?", ["5", "20", "10"], "25 ÷ 5 = **5**.", "🖐️"),
            mc("Uma barra de chocolate tem **12** quadradinhos. Comi a **terça parte**. Quantos comi?", ["4", "3", "9"], "12 ÷ 3 = **4**.", "🍫"),
            tf("A metade de 30 é 15.", True, "30 ÷ 2 = 15."),
        ],
    ),
    "a3-b3-matematica-u2-m1": missao(
        [
            ("📏", "Cada medida tem seu **instrumento**."),
            ("⚖️", "**Régua/fita métrica**: comprimento (cm, m). **Balança**: massa (g, kg). **Copo medidor**: capacidade (mL, L)."),
            ("⏰", "**Relógio**: tempo (horas, minutos). **Termômetro**: temperatura (°C)."),
        ],
        [
            ligar([("régua", "comprimento"), ("balança", "massa"), ("copo medidor", "capacidade"), ("relógio", "tempo")], "Ligue o instrumento ao que ele mede"),
            mc("Para saber quanto **pesa** a melancia, uso...", ["balança", "régua", "relógio"], "Massa = **balança**.", "🍉"),
            mc("Para medir o **comprimento** da mesa, uso...", ["fita métrica", "copo medidor", "termômetro"], "Comprimento = **fita métrica**.", "📏"),
            mc("Para medir **meio litro de leite**, uso...", ["copo medidor", "balança de banheiro", "régua"], "Capacidade = **copo medidor**.", "🥛"),
            mc("Para saber se estou com **febre**, uso...", ["termômetro", "régua", "balança"], "Temperatura = **termômetro**.", "🌡️"),
            mc("Qual unidade usamos para medir **massa**?", ["quilograma (kg)", "metro (m)", "litro (L)"], "Massa em **kg** ou **g**.", "⚖️"),
        ],
    ),
    "a3-b3-matematica-u2-m2": missao(
        [
            ("🫗", "**1 litro (L) = 1000 mililitros (mL)**."),
            ("🥤", "Um copo de **250 mL**: **4 copos** enchem **1 litro**!"),
            ("➕", "250 + 250 + 250 + 250 = **1000 mL**."),
        ],
        [
            mc("Quantos copos de **250 mL** enchem **1 litro**?", ["4", "2", "10"], "4 × 250 = 1000.", "🥤"),
            mc("**2 copos** de 250 mL dão quantos mL?", ["500 mL", "250 mL", "1000 mL"], "250 + 250 = **500**.", "🥛"),
            mc("**500 mL** é o mesmo que...", ["meio litro", "1 litro", "2 litros"], "Metade de 1000.", "🫗"),
            mc("Uma jarra de **2 litros** precisa de quantos copos de 250 mL?", ["8", "4", "6"], "2 × 4 = **8**.", "🏺"),
            mc("Quantos mL tem **1 litro**?", ["1000", "100", "10"], "**1000 mL**.", "🧪"),
            tf("Uma garrafa de 2 litros tem mais líquido que uma de 600 mL.", True, "2 L = 2000 mL."),
        ],
    ),
    "a3-b3-matematica-u2-m3": missao(
        [
            ("⚖️", "As **embalagens** mostram a **massa**: **1 kg** de arroz, **500 g** de macarrão, **200 g** de biscoito."),
            ("🔢", "**1 kg = 1000 g**."),
            ("📦", "Compare as embalagens de casa: qual é a mais pesada?"),
            desafio("junte 4 embalagens de alimentos em casa, leia a massa de cada uma e organize da mais leve para a mais pesada."),
        ],
        [
            ordem("Da mais leve para a mais pesada", ["Biscoito: 200 g", "Macarrão: 500 g", "Arroz: 1 kg", "Feijão: 2 kg"], "200 g < 500 g < 1000 g < 2000 g."),
            mc("Quantos gramas há em **1 kg**?", ["1000 g", "100 g", "10 g"], "1 kg = **1000 g**.", "⚖️"),
            mc("O que pesa mais: **1 kg de algodão** ou **1 kg de ferro**?", ["Os dois pesam igual", "O ferro", "O algodão"], "Os dois têm **1 kg**!", "🤔"),
            mc("**2 pacotes de 500 g** pesam juntos...", ["1 kg", "500 g", "2 kg"], "500 + 500 = 1000 g = **1 kg**.", "📦"),
            tf("Um pacote de 500 g pesa a metade de 1 kg.", True, "1000 ÷ 2 = 500."),
        ],
    ),
    # ------------------------------------------------------------ Ciências
    "a3-b3-ciencias-u1-m1": missao(
        [
            ("🌍", "A Terra tem formato quase **esférico**, como uma bola."),
            ("🌐", "O **globo terrestre** é a representação mais parecida com a Terra. O **mapa-múndi** mostra tudo no plano."),
            ("💧", "Cerca de **3 partes em 4** da superfície da Terra são **água** (oceanos). O resto são **continentes**."),
        ],
        [
            mc("Qual é o formato da Terra?", ["Quase uma esfera", "Plana como uma mesa", "Um cubo"], "A Terra é quase **esférica**.", "🌍"),
            mc("No globo, o **azul** representa...", ["a água (oceanos e mares)", "as florestas", "as cidades"], "Azul = **água**.", "🌊"),
            mc("Há mais **água** ou **terra** na superfície do planeta?", ["Água", "Terra", "Os dois iguais"], "Cerca de **3/4** é água.", "💧"),
            mc("Em qual continente fica o Brasil?", ["América do Sul", "Europa", "Ásia"], "**América do Sul**.", "🇧🇷"),
            ligar([("globo", "representa a Terra como esfera"), ("mapa-múndi", "mostra a Terra no plano"), ("oceano", "grande porção de água salgada")], "Ligue o termo ao significado"),
            tf("O maior oceano do mundo é o Pacífico.", True, "O **Oceano Pacífico** é o maior."),
        ],
    ),
    "a3-b3-ciencias-u1-m2": missao(
        [
            ("☀️", "O **Sol** é uma **estrela** e ilumina o dia."),
            ("🌙", "A **Lua** pode ser vista à **noite** e, às vezes, também **de dia**!"),
            ("⭐", "As **estrelas** e alguns **planetas** (como Vênus) aparecem à noite, quando o céu escurece."),
        ],
        [
            separar("Quando podemos ver?", ["De dia", "À noite", "Pode aparecer de dia e à noite"],
                    [("Sol", 0), ("estrelas", 1), ("planeta Vênus brilhando", 1), ("Lua", 2)],
                    "A Lua pode aparecer de dia também."),
            mc("O Sol é...", ["uma estrela", "um planeta", "uma lua"], "O Sol é uma **estrela**.", "☀️"),
            mc("Por que não vemos as estrelas de dia?", ["A luz do Sol é muito forte", "Elas somem", "Elas dormem"], "O brilho do Sol esconde as estrelas.", "✨"),
            mc("A Lua tem luz própria?", ["Não, ela reflete a luz do Sol", "Sim, ela tem lâmpadas", "Sim, ela pega fogo"], "Ela **reflete** a luz do Sol.", "🌙"),
            tf("Às vezes dá para ver a Lua durante o dia.", True, "Olhe para o céu de manhã!"),
            fill("A Terra é um ___.", ["planeta", "estrela", "satélite"], "A Terra é um **planeta**."),
        ],
    ),
    "a3-b3-ciencias-u1-m3": missao(
        [
            ("🔭", "Seja um **observador do céu**!"),
            ("🌓", "Olhe para a Lua por **3 noites** e desenhe o formato. Ela vai **mudar** um pouquinho a cada noite."),
            ("📅", "Anote a **data** e a **hora** de cada observação, como os cientistas."),
            desafio("observe a Lua por 3 noites, com um adulto, e desenhe o formato dela em cada noite, com a data."),
        ],
        [
            mc("O que um cientista anota ao observar a Lua?", ["Data, hora e formato", "Só a cor da roupa", "Nada"], "Registrar é importante.", "📝"),
            mc("Por que a Lua parece mudar de formato?", ["Vemos partes diferentes iluminadas pelo Sol", "Ela encolhe de verdade", "Alguém pinta a Lua"], "São as **fases da Lua**.", "🌓"),
            mc("Qual fase mostra a Lua **toda redonda e iluminada**?", ["Cheia", "Nova", "Minguante"], "**Lua cheia**.", "🌕"),
            ordem("Coloque as fases na ordem", ["🌑 Nova", "🌓 Crescente", "🌕 Cheia", "🌗 Minguante"], "O ciclo da Lua."),
            tf("A Lua gira ao redor da Terra.", True, "Ela é o **satélite natural** da Terra."),
        ],
    ),
    # ------------------------------------------------------------ Ciências Humanas (História)
    "a3-b3-humanas-u1-m1": missao(
        [
            ("🏙️", "Na **cidade**: muitos prédios, trânsito, comércio, fábricas e escritórios."),
            ("🌾", "No **campo**: plantações, criação de animais, casas mais distantes umas das outras."),
            ("🤝", "Campo e cidade **dependem um do outro**: o campo produz alimentos; a cidade produz máquinas e serviços."),
        ],
        [
            separar("Campo ou cidade?", ["Campo", "Cidade"],
                    [("plantação de milho", 0), ("ordenhar vacas", 0), ("trator", 0), ("metrô", 1), ("shopping", 1), ("prédios altos", 1)],
                    "Cada espaço tem suas atividades."),
            mc("De onde vêm a maior parte dos alimentos?", ["Do campo", "Do shopping", "Do metrô"], "O **campo** produz alimentos.", "🌽"),
            mc("O trator usado no campo é fabricado...", ["numa fábrica, geralmente na cidade", "na plantação", "no rio"], "Campo e cidade se ajudam.", "🚜"),
            mc("Onde costuma haver **mais trânsito**?", ["Na cidade", "No campo", "No meio da floresta"], "Muitos carros na **cidade**.", "🚗"),
            tf("O campo e a cidade dependem um do outro.", True, "Trocam produtos e serviços."),
        ],
    ),
    "a3-b3-humanas-u1-m2": missao(
        [
            ("⏳", "O **trabalho** e o **lazer** mudaram ao longo do tempo."),
            ("📮", "Antes havia **acendedor de lampiões**, **leiteiro** que entregava de casa em casa, **telefonista**."),
            ("🎮", "O lazer também mudou: **rádio** → **TV** → **videogame** e **internet**. Mas **pipa** e **pega-pega** continuam!"),
        ],
        [
            ligar([("acendedor de lampiões", "postes de luz elétrica"), ("telefonista", "chamadas automáticas"), ("datilógrafo", "digitação no computador"), ("rádio novela", "série na TV")], "Ligue o antes ao hoje"),
            mc("Qual brincadeira **continua** desde antigamente?", ["Pipa", "Videogame", "Tablet"], "A **pipa** é muito antiga!", "🪁"),
            mc("O **leiteiro** entregava leite de casa em casa. Hoje compramos leite...", ["no mercado", "na farmácia", "no banco"], "Hoje está no **mercado**.", "🥛"),
            mc("Antes da TV, as famílias se reuniam para ouvir...", ["o rádio", "o celular", "a internet"], "O **rádio** era o centro da sala.", "📻"),
            tf("Algumas profissões deixaram de existir e outras surgiram.", True, "Hoje há programadores, youtubers..."),
        ],
    ),
    "a3-b3-humanas-u1-m3": missao(
        [
            ("🏘️", "**Comunidades** são grupos de pessoas que vivem num mesmo lugar e compartilham costumes."),
            ("🛶", "**Vila Ribeira** (beira de rio): as pessoas pescam, andam de barco e a escola fica do outro lado do rio."),
            ("🏙️", "**Bairro Centro** (cidade grande): as pessoas andam de ônibus, trabalham em lojas e escritórios."),
        ],
        [
            mc("Como as crianças da **Vila Ribeira** vão à escola?", ["De barco", "De metrô", "De avião"], "A escola fica do outro lado do rio.", "🛶"),
            mc("Qual trabalho é comum na **Vila Ribeira**?", ["Pesca", "Escritório no 20º andar", "Metroviário"], "Eles vivem perto do rio.", "🎣"),
            mc("Qual transporte é comum no **Bairro Centro**?", ["Ônibus", "Canoa", "Carroça de boi"], "Na cidade grande, **ônibus**.", "🚌"),
            separar("Vila Ribeira ou Bairro Centro?", ["Vila Ribeira", "Bairro Centro"],
                    [("barco", 0), ("pesca", 0), ("casa sobre palafitas", 0), ("semáforo", 1), ("prédio comercial", 1)],
                    "Cada comunidade tem seu modo de vida."),
            tf("Comunidades diferentes têm modos de vida diferentes, e todos merecem respeito.", True, "Diversidade!"),
        ],
    ),
    # ------------------------------------------------------------ Ciências Humanas (Geografia)
    "a3-b3-humanas-u2-m1": missao(
        [
            ("🗺️", "Os mapas usam **símbolos** para representar as coisas."),
            ("🔑", "A **legenda** explica o que cada símbolo significa."),
            ("🏥", "Exemplos: ✚ = hospital · 🏫 = escola · 🌳 = praça · 〰️ azul = rio."),
        ],
        [
            ligar([("✚", "hospital"), ("🏫", "escola"), ("🌳", "praça"), ("⛪", "igreja")], "Decifre a legenda"),
            ligar([("linha azul", "rio"), ("mancha verde", "área verde"), ("linha preta grossa", "estrada"), ("quadradinho vermelho", "casa")], "Decifre a legenda"),
            mc("Para que serve a **legenda** de um mapa?", ["Explicar os símbolos", "Mostrar o preço", "Contar uma piada"], "Sem legenda, não entendemos o mapa.", "🔑"),
            mc("No mapa, um **rio** geralmente é desenhado com a cor...", ["azul", "vermelha", "preta"], "Água = **azul**.", "🌊"),
            tf("Símbolos de mapa podem ser desenhos simples.", True, "Assim o mapa fica fácil de ler."),
        ],
    ),
    "a3-b3-humanas-u2-m2": missao(
        [
            ("✏️", "Agora **você** vai criar símbolos para o mapa do bairro!"),
            ("🎨", "Um bom símbolo é **simples**, **fácil de entender** e **diferente** dos outros."),
            ("📋", "Depois, coloque todos na **legenda**."),
        ],
        [
            mc("Qual seria um bom símbolo para **padaria**?", ["🥖 um pãozinho", "🚗 um carro", "🐟 um peixe"], "O símbolo deve lembrar o lugar.", "🥖"),
            mc("Qual seria um bom símbolo para **ponto de ônibus**?", ["🚌 um ônibus", "🌳 uma árvore", "📚 um livro"], "Fácil de reconhecer!", "🚌"),
            mc("Qual seria um bom símbolo para **biblioteca**?", ["📚 livros", "⚽ bola", "🍕 pizza"], "Livros = biblioteca.", "📚"),
            mc("Dois lugares diferentes podem ter o **mesmo** símbolo?", ["Não, senão confunde", "Sim, sempre", "Só se forem vizinhos"], "Cada símbolo deve ser **único**.", "🚫"),
            tf("Todo símbolo criado deve aparecer na legenda.", True, "Assim todos entendem o mapa."),
        ],
    ),
    "a3-b3-humanas-u2-m3": missao(
        [
            ("📷", "A **foto aérea** (tirada de cima, de avião ou drone) mostra o lugar **como ele é**, com cores reais."),
            ("🗺️", "O **mapa** é um **desenho** simplificado, com **símbolos**, **legenda** e **nomes de ruas**."),
            ("🔍", "Os dois mostram o lugar **visto de cima**."),
        ],
        [
            separar("Foto aérea ou mapa?", ["Foto aérea", "Mapa"],
                    [("mostra telhados e carros de verdade", 0), ("tem cores reais das árvores", 0), ("tem legenda", 1), ("tem nomes das ruas escritos", 1), ("usa símbolos simples", 1)],
                    "A foto mostra o real; o mapa simplifica."),
            mc("Qual dos dois tem **legenda**?", ["O mapa", "A foto aérea", "Nenhum"], "O **mapa** usa legenda.", "🔑"),
            mc("O que os dois têm em comum?", ["Mostram o lugar visto de cima", "Mostram o lugar de lado", "São feitos com tinta"], "Visão **vertical**.", "🦅"),
            mc("Para tirar uma **foto aérea**, podemos usar...", ["um drone", "um microscópio", "uma lupa"], "Drones voam e fotografam.", "🚁"),
            tf("O mapa é uma representação simplificada do lugar.", True, "Mostra o mais importante."),
        ],
    ),
    # ------------------------------------------------------------ Ética
    "a3-b3-etica-u1-m1": missao(
        [
            ("😄", "**Brincadeira** é quando **todos se divertem** juntos."),
            ("😢", "**Bullying** é quando alguém é **zombado, excluído ou agredido de propósito e várias vezes**."),
            ("🛑", "Se só um ri e o outro sofre, **não é brincadeira**!"),
        ],
        [
            separar("Brincadeira ou bullying?", ["Brincadeira", "Bullying"],
                    [("todos jogando pega-pega e rindo", 0), ("contar piada que todos acham graça", 0), ("apelidar o colega todo dia e ele chora", 1), ("nunca deixar a mesma pessoa brincar", 1), ("empurrar alguém toda vez no recreio", 1)],
                    "Bullying machuca e se repete."),
            mc("O que é **bullying**?", ["Agredir ou zombar de alguém de propósito, várias vezes", "Uma brincadeira em que todos riem", "Um esporte"], "Bullying **não é brincadeira**.", "🛑"),
            mc("Como saber se é brincadeira?", ["Todos estão se divertindo", "Só eu estou rindo", "Alguém está chorando"], "Brincadeira é boa para **todos**.", "😄"),
            tf("Bullying pode acontecer também pela internet.", True, "Chama-se **cyberbullying**."),
            fill("Apelidos que machucam são ___.", ["bullying", "elogios", "brincadeira de todos"], "Isso é **bullying**."),
        ],
    ),
    "a3-b3-etica-u1-m2": missao(
        [
            ("👀", "Você viu um colega sendo **excluído** ou **zombado**. O que fazer?"),
            ("🤝", "**Não participe**, **acolha** o colega e **conte a um adulto** (professor, família)."),
            ("💪", "Contar não é **dedurar**: é **proteger** alguém."),
        ],
        [
            mc("Colegas não deixam a Ju brincar e riem dela. O que fazer?", ["Chamar a Ju para brincar e contar à professora", "Rir junto", "Fingir que não viu"], "Acolher e pedir ajuda.", "🤝"),
            mc("Alguém posta foto zombando de um colega no grupo. O que fazer?", ["Não compartilhar e avisar um adulto", "Compartilhar", "Comentar rindo"], "Não espalhe!", "📱"),
            mc("Contar para um adulto sobre bullying é...", ["um jeito de proteger o colega", "dedurar", "proibido"], "É **coragem** e **cuidado**.", "🛡️"),
            separar("Ajuda ou piora?", ["Ajuda", "Piora"],
                    [("acolher quem sofre", 0), ("contar a um adulto", 0), ("dizer pare com firmeza", 0), ("rir junto", 1), ("espalhar a fofoca", 1)],
                    "Todos podem ajudar a acabar com o bullying."),
            tf("Quem assiste ao bullying e não faz nada também pode ajudar mudando de atitude.", True, "Todos podem fazer a diferença."),
        ],
    ),
    "a3-b3-etica-u1-m3": missao(
        [
            ("🕊️", "Vamos criar um **cartaz da paz** contra o bullying!"),
            ("🖍️", "Use frases curtas: **Respeito é para todos!** · **Aqui ninguém fica de fora!**"),
            ("🎨", "Desenhos coloridos ajudam a mensagem a chamar a atenção."),
            desafio("crie um cartaz contra o bullying com uma frase e um desenho e mostre para sua família ou turma."),
        ],
        [
            mc("Qual frase é boa para o cartaz?", ["Respeito é para todos!", "Quem é diferente fica de fora!", "Rir dos outros é legal!"], "Uma mensagem **positiva**.", "🕊️"),
            mc("Para que serve um cartaz?", ["Passar uma mensagem para muitas pessoas", "Guardar comida", "Medir a sala"], "Ele **comunica**.", "📢"),
            mc("O que deixa um cartaz mais chamativo?", ["Letras grandes e cores", "Letras minúsculas e apagadas", "Nenhum desenho e nenhuma cor"], "Fácil de ler de longe!", "🎨"),
            tf("Um cartaz pode ajudar a turma a pensar sobre respeito.", True, "Mensagens fazem pensar."),
            fill("No nosso cartaz, ninguém fica de ___!", ["fora", "dentro", "pé"], "**Aqui ninguém fica de fora!**"),
        ],
    ),
    # ------------------------------------------------------------ Inglês
    "a3-b3-ingles-u1-m1": missao(
        [
            ("🐱", "**Where is the cat?** = Onde está o gato?"),
            ("📦", "**in** = dentro · **on** = em cima · **under** = embaixo"),
            ("🛏️", "**The cat is under the bed.** = O gato está embaixo da cama."),
        ],
        [
            mc("**The cat is in the box.** Onde está o gato?", ["Dentro da caixa", "Em cima da caixa", "Embaixo da caixa"], "in = **dentro**.", "📦"),
            mc("**The cat is on the table.** Onde está o gato?", ["Em cima da mesa", "Embaixo da mesa", "Dentro da mesa"], "on = **em cima**.", "🐱"),
            mc("**The cat is under the chair.** Onde está o gato?", ["Embaixo da cadeira", "Em cima da cadeira", "Dentro da cadeira"], "under = **embaixo**.", "🪑"),
            ligar([("in", "dentro"), ("on", "em cima"), ("under", "embaixo")], "Ligue a palavra ao significado"),
            fill("The ball is ___ the bed. (embaixo)", ["under", "on", "in"], "embaixo = **under**."),
            fill("The book is ___ the bag. (dentro)", ["in", "on", "under"], "dentro = **in**."),
        ],
    ),
    "a3-b3-ingles-u1-m2": missao(
        [
            ("🏠", "**My house** (minha casa) tem vários **rooms** (cômodos)."),
            ("🛏️", "**bedroom** = quarto · **kitchen** = cozinha · **bathroom** = banheiro · **living room** = sala"),
            ("🛋️", "Objetos: **bed** (cama), **sofa**, **stove** (fogão), **shower** (chuveiro), **fridge** (geladeira)."),
        ],
        [
            separar("Room by room", ["bedroom", "kitchen", "bathroom", "living room"],
                    [("bed", 0), ("pillow", 0), ("stove", 1), ("fridge", 1), ("shower", 2), ("toothbrush", 2), ("sofa", 3), ("TV", 3)],
                    "Cada objeto no seu cômodo."),
            mc("Onde fica a **fridge**?", ["kitchen", "bedroom", "bathroom"], "Geladeira = cozinha.", "🧊"),
            mc("Onde fica a **bed**?", ["bedroom", "kitchen", "living room"], "Cama = quarto.", "🛏️"),
            mc("O que é **bathroom**?", ["Banheiro", "Quarto", "Cozinha"], "bathroom = **banheiro**.", "🛁"),
            ligar([("bedroom", "quarto"), ("kitchen", "cozinha"), ("bathroom", "banheiro"), ("living room", "sala")], "Ligue o cômodo ao significado"),
        ],
    ),
    "a3-b3-ingles-u1-m3": missao(
        [
            ("📖", "Leia e encontre os objetos na casa!"),
            ("🏠", "**The TV is in the living room. The cat is on the sofa. The ball is under the bed. The cake is in the kitchen.**"),
            ("🔍", "Use **in**, **on** e **under** para achar tudo."),
        ],
        [
            mc("Where is the TV?", ["In the living room", "In the bathroom", "Under the bed"], "**The TV is in the living room.**", "📺"),
            mc("Where is the cat?", ["On the sofa", "In the kitchen", "Under the bed"], "**The cat is on the sofa.**", "🐱"),
            mc("Where is the ball?", ["Under the bed", "On the sofa", "In the kitchen"], "**The ball is under the bed.**", "⚽"),
            mc("Where is the cake?", ["In the kitchen", "In the bedroom", "On the TV"], "**The cake is in the kitchen.**", "🎂"),
            tf("**The cat is on the sofa** quer dizer que o gato está em cima do sofá.", True, "on = em cima."),
        ],
    ),
}
