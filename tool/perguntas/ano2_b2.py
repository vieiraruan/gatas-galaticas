"""2º ano · 2º bimestre."""
from base import desafio, fill, ligar, mc, missao, ordem, separar, tf

MISSOES = {
    # ------------------------------------------------------------ Português
    "a2-b2-portugues-u1-m1": missao(
        [
            ("👂", "Algumas letras têm **sons parecidos**: **F/V**, **T/D**, **P/B**."),
            ("🔪", "**FACA** (de cortar) e **VACA** (o animal) mudam só uma letra!"),
            ("🎲", "**TATO** e **DADO**, **PATO** e **BATO**: escute com atenção."),
        ],
        [
            mc("Qual é o animal que dá leite? 🐮", ["VACA", "FACA"], "**V**ACA, com V.", None),
            mc("Qual usamos para cortar o pão? 🔪", ["FACA", "VACA"], "**F**ACA, com F.", None),
            mc("Qual jogamos no tabuleiro? 🎲", ["DADO", "TATO"], "**D**ADO, com D.", None),
            mc("Qual é a ave que nada no lago? 🦆", ["PATO", "BATO"], "**P**ATO, com P.", None),
            mc("Qual usamos no pé quando chove? 👢", ["BOTA", "POTA"], "**B**OTA, com B.", None),
            fill("A ___ACA pula na cerca. 🐮", ["V", "F"], "**VACA**."),
            ligar([("FACA", "🔪"), ("VACA", "🐮"), ("PATO", "🦆"), ("BOTA", "👢")], "Ligue a palavra à figura"),
        ],
    ),
    "a2-b2-portugues-u1-m2": missao(
        [
            ("〰️", "O **til (~)** deixa o som **nasal**, saindo pelo nariz: **mãe**, **pão**, **mão**."),
            ("🅼", "Antes de **P** e **B**, usamos **M**: **campo**, **sombra**, **tempo**."),
            ("🅽", "Antes das outras consoantes, usamos **N**: **canto**, **dente**, **mundo**."),
        ],
        [
            fill("M___E 👩", ["Ã", "A", "AN"], "**MÃE**, com til."),
            fill("CA___PO ⚽", ["M", "N", "~"], "Antes de **P** usamos **M**: CAMPO."),
            fill("CA___TO 🎤", ["N", "M", "~"], "Antes de **T** usamos **N**: CANTO."),
            fill("SO___BRA 🌳", ["M", "N", "~"], "Antes de **B** usamos **M**: SOMBRA."),
            fill("DE___TE 🦷", ["N", "M", "~"], "Antes de **T** usamos **N**: DENTE."),
            fill("P___O 🍞", ["Ã", "A", "AM"], "**PÃO**, com til."),
            tf("Antes de **P** e **B** escrevemos **M**.", True, "Ca**m**po, so**m**bra, te**m**po."),
        ],
    ),
    "a2-b2-portugues-u1-m3": missao(
        [
            ("✍️", "A **letra cursiva** é a letra de mão, com as letras **ligadas**."),
            ("➰", "Ela começa com a **letra minúscula** e segue sem tirar o lápis do papel."),
            ("📓", "Use o **caderno de caligrafia** para treinar!"),
            desafio("copie 5 palavras em letra cursiva no caderno (por exemplo: casa, bola, gato, sapo, lua) e tire uma foto."),
        ],
        [
            mc("Na letra cursiva, as letras ficam...", ["ligadas umas às outras", "separadas e grandes", "de cabeça para baixo"], "Elas se **ligam**.", "➰"),
            mc("Onde treinamos a letra cursiva?", ["No caderno de caligrafia", "Na parede", "Na mesa"], "No **caderno**.", "📓"),
            mc("Qual é uma boa postura para escrever?", ["Sentar com as costas retas e o caderno na mesa", "Deitar no chão", "Escrever em pé correndo"], "Postura ajuda a escrever bonito.", "🪑"),
            tf("Podemos escrever a mesma palavra em letra de forma e em letra cursiva.", True, "É a mesma palavra, com jeitos diferentes."),
            fill("A letra cursiva também é chamada de letra de ___.", ["mão", "pé", "máquina"], "Letra de **mão**."),
        ],
    ),
    # ------------------------------------------------------------ Matemática
    "a2-b2-matematica-u1-m1": missao(
        [
            ("🏎️", "Na **corrida do cálculo**, responda rápido de cabeça!"),
            ("🧠", "Dicas: **7 + 3 = 10** (amigos do 10). **8 + 8 = 16** (dobro)."),
            ("➖", "Para **15 − 5**, pense: 15 tira 5 = **10**."),
        ],
        [
            mc("**7 + 3** = ?", ["10", "9", "11"], "Amigos do 10!", "🏎️"),
            mc("**8 + 8** = ?", ["16", "14", "18"], "Dobro de 8.", "🏎️"),
            mc("**9 + 6** = ?", ["15", "14", "16"], "9 + 1 = 10, + 5 = **15**.", "🏎️"),
            mc("**15 − 5** = ?", ["10", "5", "20"], "Tira 5: **10**.", "🏎️"),
            mc("**12 − 4** = ?", ["8", "7", "9"], "12 − 2 = 10, − 2 = **8**.", "🏎️"),
            mc("**20 + 30** = ?", ["50", "23", "40"], "2 dezenas + 3 dezenas.", "🏎️"),
            fill("6 + ___ = 10", ["4", "5", "6"], "Amigos do 10: 6 e **4**."),
        ],
    ),
    "a2-b2-matematica-u1-m2": missao(
        [
            ("🛒", "No **mercadinho**, vamos resolver problemas!"),
            ("➕", "**Juntar** ou **ganhar mais**: somamos. **Tirar**, **gastar** ou **dar**: subtraímos."),
            ("⚖️", "**Quantos a mais?** Também usamos a subtração para comparar."),
        ],
        [
            mc("Comprei **12 laranjas** e **5 maçãs**. Quantas frutas?", ["17", "7", "15"], "12 + 5 = **17**.", "🍊"),
            mc("Havia **20 pães**. Vendeu **8**. Quantos sobraram?", ["12", "28", "10"], "20 − 8 = **12**.", "🥖"),
            mc("Lia tem **15 balas** e Rui tem **9**. Quantas Lia tem **a mais**?", ["6", "24", "5"], "15 − 9 = **6**.", "🍬"),
            mc("Uma caixa tem **24 ovos**. Quebraram **4**. Quantos inteiros?", ["20", "28", "18"], "24 − 4 = **20**.", "🥚"),
            mc("Tinha **R$ 10**. Ganhei **R$ 5**. Quanto tenho agora?", ["R$ 15", "R$ 5", "R$ 50"], "10 + 5 = **15**.", "💵"),
            tf("**Quantos sobraram?** é uma pergunta de subtração.", True, "Sobrar = tirar."),
        ],
    ),
    "a2-b2-matematica-u1-m3": missao(
        [
            ("🗺️", "A **planta** é o desenho de um lugar visto **de cima**."),
            ("🏴‍☠️", "Na **caça ao tesouro**, siga as instruções: **ande 3 passos**, **vire à direita**..."),
            ("🧭", "Preste atenção em **direita**, **esquerda**, **frente** e **atrás**."),
        ],
        [
            mc("Saí da porta da sala, andei em frente até o pátio e virei à **direita**. Na direita do pátio fica a biblioteca. Onde cheguei?", ["Na biblioteca", "No banheiro", "Na cozinha"], "Seguindo a instrução: **biblioteca**.", "📚"),
            mc("O tesouro está **atrás** da árvore. Estou na frente dela. O que faço?", ["Dou a volta na árvore", "Subo na árvore", "Fico parado"], "Atrás = do outro lado.", "🌳"),
            ordem("Coloque as instruções na ordem para chegar ao tesouro", ["Sair da sala", "Andar até o pátio", "Virar à esquerda", "Cavar embaixo do banco"], "Siga passo a passo."),
            mc("Na planta da escola, as coisas aparecem...", ["vistas de cima", "vistas de lado", "de cabeça para baixo"], "Planta = visão **de cima**.", "🗺️"),
            mc("Virei à direita duas vezes. Agora estou virado para...", ["trás (o lado oposto)", "a frente", "a esquerda"], "Duas viradas de um lado = meia-volta!", "🔄"),
            tf("Uma planta ajuda a encontrar lugares.", True, "Como um mapa!"),
        ],
    ),
    # ------------------------------------------------------------ Ciências
    "a2-b2-ciencias-u1-m1": missao(
        [
            ("🏠", "Dentro de casa também há **perigos** escondidos!"),
            ("🔌", "**Tomadas**, **fogão**, **facas**, **remédios** e **produtos de limpeza** precisam de cuidado."),
            ("🧑‍🍳", "Peça sempre a um **adulto** para usar essas coisas."),
        ],
        [
            separar("Perigoso ou seguro para brincar?", ["Perigoso ⚠️", "Seguro ✅"],
                    [("tomada", 0), ("faca", 0), ("panela no fogão", 0), ("remédio", 0), ("bola", 1), ("livro", 1), ("bloco de montar", 1)],
                    "Coisas perigosas ficam longe das crianças."),
            mc("Onde os remédios devem ficar?", ["Guardados longe das crianças", "No chão do quarto", "Na mochila"], "Só um adulto dá remédio.", "💊"),
            mc("O cabo da panela no fogão deve ficar...", ["virado para dentro", "virado para fora", "solto"], "Assim ninguém esbarra.", "🍳"),
            mc("Colocar o dedo na tomada é...", ["muito perigoso", "divertido", "seguro"], "Pode dar **choque**!", "🔌"),
            tf("Produtos de limpeza podem fazer mal se forem engolidos.", True, "Nunca coloque na boca!"),
        ],
    ),
    "a2-b2-ciencias-u1-m2": missao(
        [
            ("🛑", "Antes de fazer algo, pense: **é seguro?**"),
            ("🧴", "Nunca beba algo de uma **garrafa sem rótulo**: pode ser produto de limpeza."),
            ("🔥", "**Fósforos**, **isqueiros** e **velas** não são brinquedos."),
        ],
        [
            mc("Você achou fósforos na mesa. O que fazer?", ["Avisar um adulto e não mexer", "Acender para ver", "Guardar no bolso"], "Fogo não é brinquedo!", "🔥"),
            mc("Uma garrafa sem rótulo com líquido colorido. Pode beber?", ["Não, chamo um adulto", "Sim, deve ser suco", "Sim, se for gelado"], "Pode ser **produto perigoso**.", "🧴"),
            mc("A bola caiu na rua. O que fazer?", ["Pedir ajuda a um adulto", "Correr atrás sem olhar", "Pular na rua"], "Carros podem passar!", "⚽"),
            separar("Pode ou não pode?", ["Pode ✅", "Não pode ❌"],
                    [("usar cinto no carro", 0), ("andar de bicicleta com capacete", 0), ("brincar com fósforo", 1), ("subir na janela", 1), ("mexer no fio desencapado", 1)],
                    "Segurança em primeiro lugar."),
            tf("No carro, criança anda no banco de trás com cadeirinha ou cinto.", True, "É lei e é seguro!"),
        ],
    ),
    "a2-b2-ciencias-u1-m3": missao(
        [
            ("⚠️", "Alguns **símbolos** avisam sobre perigos."),
            ("⚡", "O **raio** avisa: **perigo de choque elétrico**. A **chama** avisa: **inflamável** (pega fogo fácil)."),
            ("☠️", "A **caveira** avisa: **veneno** (tóxico). Fique longe!"),
        ],
        [
            ligar([("⚡", "choque elétrico"), ("🔥", "pega fogo fácil"), ("☠️", "veneno"), ("⚠️", "atenção")], "Ligue o símbolo ao significado"),
            mc("Num poste aparece ⚡. O que significa?", ["Perigo de choque", "Lugar de brincar", "Sorveteria"], "Fique longe!", "⚡"),
            mc("Num frasco aparece ☠️. O que fazer?", ["Não mexer e chamar um adulto", "Abrir para cheirar", "Beber um pouquinho"], "Caveira = **veneno**.", "☠️"),
            mc("Num frasco de álcool aparece 🔥. Isso quer dizer que ele...", ["pega fogo fácil", "é gelado", "é doce"], "**Inflamável**.", "🔥"),
            tf("Símbolos de perigo servem para nos proteger.", True, "Eles avisam sem precisar ler!"),
        ],
    ),
    # ------------------------------------------------------------ Ciências Humanas (História)
    "a2-b2-humanas-u1-m1": missao(
        [
            ("📅", "Uma **linha do tempo** mostra a ordem em que as coisas acontecem."),
            ("⏮️", "**Antes**, **durante** e **depois**."),
            ("🗓️", "A semana tem uma ordem: **domingo, segunda, terça, quarta, quinta, sexta e sábado**."),
        ],
        [
            ordem("Coloque a semana de Lia na ordem", ["Segunda: aula de música", "Quarta: natação", "Sexta: visita à vovó", "Domingo: passeio no parque"], "Segunda, quarta, sexta e domingo."),
            ordem("Coloque o dia na ordem", ["Acordar", "Tomar café", "Ir à escola", "Almoçar", "Dormir"], "Do começo ao fim do dia."),
            mc("O que vem **depois** de quinta-feira?", ["Sexta-feira", "Quarta-feira", "Domingo"], "Quinta → **sexta**.", "📅"),
            mc("O que acontece **antes** de dormir?", ["Escovar os dentes", "Acordar", "Tomar café da manhã"], "Antes de dormir, escovamos os dentes.", "🪥"),
            tf("Ontem vem antes de hoje.", True, "Ontem → hoje → amanhã."),
            fill("Hoje é segunda. Amanhã será ___.", ["terça", "domingo", "sexta"], "Segunda → **terça**."),
        ],
    ),
    "a2-b2-humanas-u1-m2": missao(
        [
            ("⏰", "O **relógio** marca as **horas** do dia."),
            ("📅", "O **calendário** mostra os **dias**, as **semanas** e os **meses**."),
            ("📒", "A **agenda** serve para **anotar compromissos**."),
        ],
        [
            ligar([("relógio", "horas"), ("calendário", "dias e meses"), ("agenda", "compromissos")], "Ligue o marcador ao que ele mostra"),
            mc("Para saber que horas são, uso...", ["o relógio", "o calendário", "a régua"], "O **relógio**.", "⏰"),
            mc("Para saber quantos dias faltam para o Natal, uso...", ["o calendário", "o relógio", "a balança"], "O **calendário**.", "🎄"),
            mc("Para lembrar da festa da escola na sexta, anoto na...", ["agenda", "panela", "bola"], "Na **agenda**.", "📒"),
            mc("Quantos meses tem um ano?", ["12", "7", "30"], "De janeiro a dezembro.", "🗓️"),
            tf("Antigamente, as pessoas usavam o Sol para saber as horas.", True, "Existia até o **relógio de sol**!"),
        ],
    ),
    "a2-b2-humanas-u1-m3": missao(
        [
            ("📸", "Comparando fotos **antigas** e **atuais** do mesmo lugar, vemos o que **mudou** e o que **continua**."),
            ("⛪", "A **igreja** da praça pode ser a mesma de 100 anos atrás: ela **permanece**."),
            ("🚗", "A rua de terra virou asfalto e as carroças viraram carros: isso **mudou**."),
        ],
        [
            ligar([("carroça", "carro"), ("lampião", "poste de luz"), ("rua de terra", "rua asfaltada"), ("telefone de fio", "celular")], "Ligue o que existia antes ao que existe hoje"),
            mc("A igreja da foto antiga ainda está lá. Ela...", ["permaneceu", "mudou de cidade", "virou um carro"], "Algumas coisas **permanecem**.", "⛪"),
            mc("Na foto antiga, as pessoas andavam de bonde. Hoje andam de ônibus. Isso...", ["mudou", "permaneceu igual", "nunca existiu"], "O transporte **mudou**.", "🚋"),
            separar("Mudou ou continua igual?", ["Mudou", "Continua"],
                    [("as roupas das pessoas", 0), ("os meios de transporte", 0), ("a igreja antiga", 1), ("o rio que passa na cidade", 1)],
                    "Os lugares têm mudanças e permanências."),
            tf("Fotos antigas nos ajudam a conhecer o passado.", True, "Elas guardam memórias."),
        ],
    ),
    # ------------------------------------------------------------ Ciências Humanas (Geografia)
    "a2-b2-humanas-u2-m1": missao(
        [
            ("🚗", "Os meios de transporte andam por **terra**, **água** ou **ar**."),
            ("🚢", "**Terra**: carro, ônibus, trem, bicicleta. **Água**: barco, navio, canoa."),
            ("✈️", "**Ar**: avião, helicóptero, balão."),
        ],
        [
            separar("Terra, água ou ar?", ["Terra", "Água", "Ar"],
                    [("ônibus", 0), ("trem", 0), ("bicicleta", 0), ("navio", 1), ("canoa", 1), ("avião", 2), ("helicóptero", 2)],
                    "Cada transporte tem seu caminho."),
            mc("Qual transporte anda nos trilhos?", ["Trem", "Barco", "Avião"], "O **trem** anda nos trilhos.", "🚆"),
            mc("Para atravessar o rio sem ponte, uso...", ["um barco", "uma bicicleta", "um skate"], "Barco anda na **água**.", "🛶"),
            mc("Qual é o transporte mais rápido para outro país distante?", ["Avião", "Bicicleta", "Carroça"], "O **avião** é muito rápido.", "✈️"),
            tf("O metrô é um meio de transporte terrestre.", True, "Ele anda em trilhos, geralmente embaixo da terra."),
        ],
    ),
    "a2-b2-humanas-u2-m2": missao(
        [
            ("📻", "Os **meios de comunicação** também mudaram com o tempo."),
            ("✉️", "Antes: **cartas**, **telegramas**, **rádio**. Hoje: **celular**, **internet**, **mensagens**."),
            ("🏙️", "Os **lugares** também mudam: um sítio pode virar um bairro cheio de prédios."),
        ],
        [
            ligar([("carta", "mensagem no celular"), ("rádio de válvula", "fone de ouvido"), ("TV de tubo", "TV fina"), ("enciclopédia de papel", "pesquisa na internet")], "Ligue o antes ao depois"),
            mc("Antigamente, para falar com alguém longe, as pessoas...", ["escreviam cartas", "mandavam vídeos pelo celular", "usavam videochamada"], "As **cartas** demoravam dias!", "✉️"),
            mc("Hoje, a forma mais rápida de mandar uma mensagem é...", ["pelo celular ou internet", "pelo correio a cavalo", "por pombo-correio"], "Chega na hora!", "📱"),
            mc("Num lugar onde antes havia uma fazenda, hoje há prédios. O lugar...", ["mudou", "continua igual", "sumiu do mapa"], "Os lugares **se transformam**.", "🏢"),
            tf("O rádio é um meio de comunicação.", True, "Transmite notícias e músicas."),
        ],
    ),
    "a2-b2-humanas-u2-m3": missao(
        [
            ("🌞", "Algumas atividades acontecem **de dia**: escola, feira, banco."),
            ("🌙", "Outras funcionam **também à noite**: **hospital**, **farmácia de plantão**, **bombeiros**, **polícia**."),
            ("👷", "Muita gente **trabalha à noite** para cuidar da cidade enquanto dormimos."),
        ],
        [
            separar("Só de dia ou também à noite?", ["Geralmente só de dia", "Funciona também à noite"],
                    [("feira livre", 0), ("escola das crianças", 0), ("hospital", 1), ("bombeiros", 1), ("farmácia de plantão", 1)],
                    "Serviços de emergência funcionam 24 horas."),
            mc("Alguém passou mal de madrugada. Para onde ir?", ["Hospital", "Escola", "Feira"], "O **hospital** funciona dia e noite.", "🏥"),
            mc("Quem trabalha à noite para apagar incêndios?", ["Bombeiros", "Professores", "Feirantes"], "Os **bombeiros** estão sempre prontos.", "🚒"),
            mc("Quando as pessoas costumam dormir?", ["À noite", "Ao meio-dia", "Na hora do recreio"], "A **noite** é a hora do descanso.", "🌙"),
            tf("Algumas pessoas trabalham à noite.", True, "Médicos, enfermeiros, policiais, vigias..."),
        ],
    ),
    # ------------------------------------------------------------ Ética
    "a2-b2-etica-u1-m1": missao(
        [
            ("🤸", "Toda criança tem o direito de **brincar** e de **participar**."),
            ("♿", "Às vezes, é só **adaptar** a brincadeira: jogar sentado, usar uma bola com guizo, ir mais devagar."),
            ("💛", "**Incluir** é fazer todos se sentirem parte do grupo."),
        ],
        [
            mc("Um colega usa cadeira de rodas. O que fazer na brincadeira?", ["Adaptar para ele brincar junto", "Deixar ele de fora", "Mudar de lugar sem ele"], "Adaptar é **incluir**.", "♿"),
            mc("Uma colega não enxerga bem. Como incluir no jogo de bola?", ["Usar uma bola com guizo que faz som", "Não chamar ela", "Rir dela"], "O som ajuda a achar a bola.", "🔔"),
            mc("Um colega novo fala outra língua. O que fazer?", ["Ensinar a brincadeira com gestos", "Ignorar", "Mandar embora"], "Brincar não precisa de muitas palavras!", "🤝"),
            tf("Todas as crianças podem brincar juntas.", True, "Com um pouco de criatividade, todos participam."),
            fill("Fazer todos participarem é ___.", ["incluir", "excluir", "esconder"], "**Incluir**."),
        ],
    ),
    "a2-b2-etica-u1-m2": missao(
        [
            ("👯", "Duas pessoas podem ser **diferentes** e **iguais** ao mesmo tempo."),
            ("🧑🏾", "**Kauã** tem cabelo cacheado e usa óculos. **Mei** tem cabelo liso e não usa óculos."),
            ("❤️", "Mas os dois gostam de **desenhar**, estão no **2º ano** e **adoram cachorros**!"),
        ],
        [
            ligar([("cabelo de Kauã", "cacheado"), ("cabelo de Mei", "liso"), ("gosto dos dois", "desenhar"), ("ano escolar dos dois", "2º ano")], "Ligue sobre Kauã e Mei"),
            mc("O que Kauã e Mei têm de **igual**?", ["Os dois gostam de desenhar", "O tipo de cabelo", "Os dois usam óculos"], "Eles **adoram desenhar**.", "🎨"),
            mc("O que Kauã e Mei têm de **diferente**?", ["O tipo de cabelo", "O ano da escola", "O gosto por cachorros"], "Cabelo cacheado e liso.", "💇"),
            tf("Mesmo sendo diferentes, podemos ter muitas coisas em comum.", True, "Diferenças e semelhanças nos unem."),
            separar("Kauã e Mei: igual ou diferente?", ["Igual", "Diferente"],
                    [("gostam de cachorros", 0), ("estão no 2º ano", 0), ("usar óculos", 1), ("tipo de cabelo", 1)],
                    "Todos temos coisas iguais e diferentes."),
        ],
    ),
    "a2-b2-etica-u1-m3": missao(
        [
            ("🖍️", "Uma turma é feita de **crianças diferentes**: cores de pele, cabelos, alturas, jeitos."),
            ("🌈", "Essas diferenças deixam a turma **mais colorida** e **mais rica**."),
            ("🤝", "**Respeito** é tratar todo mundo bem, sem zombar das diferenças."),
            desafio("desenhe uma turma com crianças bem diferentes umas das outras e mostre para um adulto."),
        ],
        [
            mc("Por que uma turma com crianças diferentes é legal?", ["Cada um traz algo novo para aprender", "Porque é tudo igual", "Não é legal"], "A diversidade nos ensina muito.", "🌈"),
            mc("Um colega tem sotaque diferente. O que fazer?", ["Respeitar e conversar", "Imitar para zombar", "Não falar com ele"], "Sotaques mostram de onde viemos.", "🗣️"),
            mc("Qual atitude é **respeitosa**?", ["Elogiar o desenho do colega", "Apelidar pela aparência", "Rir do cabelo dele"], "Elogiar é gentil!", "👏"),
            tf("Zombar das diferenças machuca as pessoas.", True, "Respeito sempre."),
            fill("Tratar todos bem é ter ___.", ["respeito", "preguiça", "medo"], "**Respeito**."),
        ],
    ),
    # ------------------------------------------------------------ Inglês
    "a2-b2-ingles-u1-m1": missao(
        [
            ("🙋", "**Simon says**: faça só o que o Simon mandar!"),
            ("👤", "**head** = cabeça · **eyes** = olhos · **nose** = nariz · **mouth** = boca"),
            ("🖐️", "**hands** = mãos · **feet** = pés · **ears** = orelhas"),
        ],
        [
            mc("Simon says: **touch your nose**! 👃 Onde tocar?", ["No nariz", "Na boca", "No pé"], "nose = **nariz**.", "👃"),
            mc("Simon says: **touch your head**! Onde tocar?", ["Na cabeça", "Na mão", "No joelho"], "head = **cabeça**.", "🙆"),
            mc("Simon says: **touch your feet**! Onde tocar?", ["Nos pés", "Nas orelhas", "Nos olhos"], "feet = **pés**.", "🦶"),
            mc("Simon says: **close your eyes**! O que fechar?", ["Os olhos", "A boca", "As mãos"], "eyes = **olhos**.", "👀"),
            mc("Simon says: **clap your hands**! O que bater?", ["As mãos", "Os pés", "A cabeça"], "hands = **mãos**.", "👏"),
            tf("**mouth** quer dizer boca.", True, "mouth = boca."),
        ],
    ),
    "a2-b2-ingles-u1-m2": missao(
        [
            ("🤖", "Vamos dar nome às partes do **robô**!"),
            ("🏷️", "**head, eyes, nose, mouth, ears, arms, hands, legs, feet**"),
            ("🦵", "**arms** = braços · **legs** = pernas"),
        ],
        [
            ligar([("head", "👤 cabeça"), ("eyes", "👀 olhos"), ("mouth", "👄 boca"), ("ears", "👂 orelhas")], "Ligue a palavra à parte do corpo"),
            ligar([("hands", "🖐️ mãos"), ("feet", "🦶 pés"), ("arms", "💪 braços"), ("legs", "🦵 pernas")], "Ligue a palavra à parte do corpo"),
            mc("Como se diz **nariz** em inglês?", ["nose", "mouth", "ears"], "nariz = **nose**.", "👃"),
            mc("Como se diz **pernas** em inglês?", ["legs", "arms", "feet"], "pernas = **legs**.", "🦵"),
            mc("O robô tem 2 **eyes**. O que ele tem 2?", ["Olhos", "Narizes", "Bocas"], "eyes = olhos.", "🤖"),
        ],
    ),
    "a2-b2-ingles-u1-m3": missao(
        [
            ("🎵", "Cante e toque: **head, shoulders, knees and toes!**"),
            ("🙆", "**shoulders** = ombros · **knees** = joelhos · **toes** = dedos dos pés"),
            ("👀", "**eyes and ears and mouth and nose!**"),
            desafio("cante a música do corpo tocando cada parte que você fala, e peça para um adulto gravar."),
        ],
        [
            ordem("Coloque a música na ordem", ["head", "shoulders", "knees", "toes"], "Head, shoulders, knees and toes!"),
            mc("O que são **knees**?", ["Joelhos", "Ombros", "Orelhas"], "knees = **joelhos**.", "🦵"),
            mc("O que são **shoulders**?", ["Ombros", "Dedos dos pés", "Olhos"], "shoulders = **ombros**.", "🙆"),
            mc("O que são **toes**?", ["Dedos dos pés", "Joelhos", "Cabelo"], "toes = **dedos dos pés**.", "🦶"),
            ligar([("eyes", "olhos"), ("ears", "orelhas"), ("mouth", "boca"), ("nose", "nariz")], "Ligue a parte do corpo ao significado"),
        ],
    ),
}
