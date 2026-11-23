"""5º ano · 1º bimestre."""
from base import desafio, fill, ligar, mc, missao, ordem, separar, tf

MISSOES = {
    # ------------------------------------------------------------ Português
    "a5-b1-portugues-u1-m1": missao(
        [
            ("🔤", "Algumas letras têm sons parecidos: **S/Z**, **X/CH**, **G/J**."),
            ("📏", "Dicas: palavras com **-esa** de origem (princesa, francesa) usam **S**; **-ez/-eza** de qualidade (beleza, rapidez) usam **Z**."),
            ("👀", "Muitas vezes só a **memória visual** ajuda: leia bastante e consulte o dicionário!"),
        ],
        [
            fill("A prince___a morava num castelo. 👸", ["s", "z"], "Feminino de título com **-esa**: princesa."),
            fill("Que bele___a de pôr do sol! 🌅", ["z", "s"], "Qualidade de belo: **beleza**."),
            fill("O ___uchu é um legume verde. 🥒", ["ch", "x"], "**Chuchu**, com CH."),
            fill("Coloque a roupa na cai___a. 📦", ["x", "ch"], "Depois de ditongo (ai) usamos **X**: caixa."),
            fill("A ___irafa tem o pescoço comprido. 🦒", ["g", "j"], "**Girafa**, com G."),
            fill("Arrumei a lo___a de brinquedos. 🏪", ["j", "g"], "**Loja**, com J."),
            separar("Escrita certa ou errada?", ["Certa", "Errada"],
                    [("rapidez", 0), ("enxada", 0), ("viagem", 0), ("rapides", 1), ("enchada", 1), ("viajem (substantivo)", 1)],
                    "Substantivo **viagem** com G; o verbo é **viajem** com J."),
            tf("Depois de **EN-**, geralmente usamos **X**: enxame, enxergar.", True, "Exceção famosa: **encher** (vem de cheio)."),
        ],
    ),
    "a5-b1-portugues-u1-m2": missao(
        [
            ("🎯", "A **sílaba tônica** é a mais forte. Ela define a regra do acento."),
            ("🔺", "**Proparoxítonas** (tônica na antepenúltima) são **todas acentuadas**: **lâm**-pa-da, **mé**-di-co."),
            ("📌", "**Oxítonas** (tônica na última) terminadas em **a, e, o, em** levam acento: so-**fá**, ca-**fé**, a-**vô**, tam-**bém**."),
        ],
        [
            mc("Qual palavra está acentuada **corretamente**?", ["lâmpada", "lampáda", "lampada"], "Proparoxítona: sempre acentuada.", "💡"),
            mc("Qual palavra está acentuada **corretamente**?", ["café", "cafe", "cáfe"], "Oxítona terminada em **e**.", "☕"),
            mc("Por que **médico** tem acento?", ["Porque é proparoxítona", "Porque é oxítona terminada em o", "Porque termina em co"], "**MÉ**-di-co: tônica na antepenúltima.", "🩺"),
            mc("Por que **sofá** tem acento?", ["É oxítona terminada em a", "É proparoxítona", "Toda palavra com f tem acento"], "so-**FÁ**: oxítona terminada em **a**.", "🛋️"),
            separar("Classifique pela sílaba tônica", ["Oxítona", "Paroxítona", "Proparoxítona"],
                    [("jacaré", 0), ("parabéns", 0), ("casa", 1), ("lápis", 1), ("pássaro", 2), ("música", 2)],
                    "Contamos de trás para frente: última, penúltima, antepenúltima."),
            tf("**Caju** precisa de acento.", False, "Oxítona terminada em **u** não leva acento."),
            fill("A palavra **árvore** é ___.", ["proparoxítona", "oxítona", "monossílaba"], "**ÁR**-vo-re."),
        ],
    ),
    "a5-b1-portugues-u1-m3": missao(
        [
            ("🪢", "Algumas palavras têm **grafia irregular**: não há regra, é preciso **memorizar**."),
            ("📚", "Exemplos: **exceção**, **excesso**, **bicicleta**, **cabeleireiro**, **mendigo**, **privilégio**."),
            ("🔎", "Na dúvida, consulte o **dicionário**."),
        ],
        [
            fill("Toda regra tem uma ex___eção.", ["c", "s", "ss"], "**Exceção**, com **XC**."),
            fill("Fui de bici___leta à escola. 🚲", ["c", "s", "qu"], "**Bicicleta**."),
            fill("O cabelei___eiro cortou meu cabelo. 💇", ["r", "rr", "l"], "**Cabeleireiro**: cabe-lei-rei-ro."),
            fill("Comer doce em ex___esso faz mal. 🍬", ["c", "s", "ç"], "**Excesso**."),
            mc("Qual palavra está escrita **certa**?", ["privilégio", "previlégio", "privilégeo"], "**Privilégio**.", "✅"),
            mc("Qual palavra está escrita **certa**?", ["beneficente", "beneficiente", "benificente"], "**Beneficente** (sem i depois do c).", "✅"),
            mc("Qual palavra está escrita **certa**?", ["mendigo", "mendingo", "mindigo"], "**Mendigo**, sem N antes do G.", "✅"),
            tf("Palavras de grafia irregular sempre seguem uma regra.", False, "Por isso precisamos **memorizar** e consultar."),
        ],
    ),
    # ------------------------------------------------------------ Matemática
    "a5-b1-matematica-u1-m1": missao(
        [
            ("🏟️", "Agora vamos até as **centenas de milhar**: **458.230** → quatrocentos e cinquenta e oito **mil**, duzentos e trinta."),
            ("🔢", "As **classes** têm 3 ordens: **unidades simples** (U, D, C) e **milhares** (UM, DM, CM)."),
            ("⚖️", "Para comparar, conte os algarismos e compare da **esquerda para a direita**."),
        ],
        [
            ordem("Do menor para o maior", ["98.765", "100.001", "345.120", "354.012"], "Compare classe por classe."),
            ordem("Do maior para o menor", ["900.000", "809.999", "800.900", "89.999"], "900 mil > 809 mil > 800 mil > 89 mil."),
            mc("Como se lê **507.040**?", ["Quinhentos e sete mil e quarenta", "Cinquenta mil setecentos e quatro", "Quinhentos e setenta mil e quatro"], "507 mil + 40.", "🔢"),
            mc("Em **638.492**, quanto vale o **6**?", ["600.000", "60.000", "6.000"], "6 centenas de milhar.", "🔍"),
            mc("Qual é o **maior** número?", ["410.000", "401.999", "399.999"], "410 mil é o maior.", "⚖️"),
            fill("O sucessor de 199.999 é ___.", ["200.000", "199.998", "1.000.000"], "199.999 + 1 = **200.000**."),
            mc("Arredondando **348.700** para a centena de milhar mais próxima, temos...", ["300.000", "400.000", "350.000"], "48.700 é menos que 50 mil: fica **300.000**.", "🎯"),
        ],
    ),
    "a5-b1-matematica-u1-m2": missao(
        [
            ("🛒", "Preços usam **números decimais**: **R$ 3,75** = 3 reais e 75 centavos."),
            ("➕", "Para somar decimais, alinhe a **vírgula** embaixo da vírgula."),
            ("🪙", "**100 centavos = 1 real**. Então 0,50 + 0,50 = 1,00."),
        ],
        [
            mc("Pão **R$ 4,50** + leite **R$ 5,25**. Quanto deu?", ["R$ 9,75", "R$ 9,57", "R$ 10,75"], "4,50 + 5,25 = **9,75**.", "🛒"),
            mc("Maçã **R$ 2,30** + banana **R$ 1,80**. Quanto deu?", ["R$ 4,10", "R$ 3,10", "R$ 4,01"], "2,30 + 1,80 = **4,10**.", "🍎"),
            mc("Paguei **R$ 10,00** por algo de **R$ 6,40**. Qual é o troco?", ["R$ 3,60", "R$ 4,60", "R$ 3,40"], "10,00 − 6,40 = **3,60**.", "💵"),
            {"tipo": "escolha", "pergunta": "Quanto dinheiro tem aqui?", "opcoes": ["R$ 7,50", "R$ 7,05", "R$ 5,70"], "correta": 0, "embaralhar": True,
             "visuais": [{"tipo": "dinheiro", "valores": [500, 200, 50]}], "explicacao": "5 + 2 + 0,50 = **7,50**."},
            mc("Qual é **mais caro**?", ["R$ 12,09", "R$ 12,00", "R$ 11,99"], "12,09 > 12,00 > 11,99.", "🏷️"),
            fill("R$ 0,75 + R$ 0,25 = ___", ["R$ 1,00", "R$ 0,100", "R$ 0,95"], "75 + 25 = 100 centavos = **1 real**."),
            tf("**R$ 2,5** e **R$ 2,50** valem a mesma coisa.", True, "2,5 = 2,50: dois reais e cinquenta centavos."),
        ],
    ),
    "a5-b1-matematica-u1-m3": missao(
        [
            ("✖️", "Para multiplicar dinheiro: **3 × R$ 2,50** = R$ 7,50."),
            ("➗", "Para dividir: **R$ 12,00 ÷ 4** = R$ 3,00 para cada um."),
            ("💡", "Dica: transforme em centavos se ajudar. R$ 2,50 = 250 centavos; 3 × 250 = 750 = R$ 7,50."),
        ],
        [
            mc("Um picolé custa **R$ 2,50**. Quanto custam **4**?", ["R$ 10,00", "R$ 8,50", "R$ 6,50"], "4 × 2,50 = **10,00**.", "🍦"),
            mc("Uma caneta custa **R$ 1,20**. Quanto custam **5**?", ["R$ 6,00", "R$ 5,20", "R$ 6,20"], "5 × 1,20 = **6,00**.", "🖊️"),
            mc("**R$ 15,00** divididos igualmente entre **3** amigos. Quanto cada um recebe?", ["R$ 5,00", "R$ 4,50", "R$ 3,00"], "15 ÷ 3 = **5**.", "🤝"),
            mc("Uma pizza de **R$ 36,00** dividida entre **4** pessoas. Quanto cada uma paga?", ["R$ 9,00", "R$ 8,00", "R$ 12,00"], "36 ÷ 4 = **9**.", "🍕"),
            mc("Um caderno custa **R$ 7,90**. Quanto custam **2**?", ["R$ 15,80", "R$ 14,80", "R$ 15,18"], "2 × 7,90 = **15,80**.", "📓"),
            mc("**R$ 10,00** divididos entre **4** irmãos. Quanto cada um recebe?", ["R$ 2,50", "R$ 2,00", "R$ 4,00"], "10 ÷ 4 = **2,50**.", "👫"),
            tf("**10 × R$ 0,50 = R$ 5,00**.", True, "10 moedas de 50 centavos = 5 reais."),
        ],
    ),
    # ------------------------------------------------------------ Ciências
    "a5-b1-ciencias-u1-m1": missao(
        [
            ("🌊", "Objetos **menos densos** que a água **flutuam**; **mais densos** **afundam**."),
            ("🪵", "A **madeira** e o **isopor** flutuam. Uma **pedra** e uma **moeda** afundam."),
            ("🚢", "Navios de aço flutuam por causa do **formato**: eles têm muito ar dentro!"),
        ],
        [
            separar("Afunda ou flutua na água?", ["Flutua", "Afunda"],
                    [("rolha", 0), ("isopor", 0), ("folha seca", 0), ("prego", 1), ("pedra", 1), ("moeda", 1)],
                    "Depende da **densidade** do material."),
            mc("Por que o navio de aço flutua?", ["Por causa do formato com muito ar dentro", "Porque o aço é leve", "Porque o mar é raso"], "O formato muda a densidade do conjunto.", "🚢"),
            mc("Uma bolinha de massinha afunda. Se a moldarmos como um barquinho...", ["ela pode flutuar", "afunda mais rápido", "derrete"], "O formato faz diferença!", "⛵"),
            mc("O **óleo** fica por cima da água porque é...", ["menos denso", "mais denso", "mais quente sempre"], "Menos denso fica por cima.", "🫗"),
            tf("Um ovo afunda em água doce, mas pode flutuar em água bem salgada.", True, "O sal deixa a água mais densa."),
            mc("O **metal** é bom condutor de...", ["calor e eletricidade", "som apenas", "nada"], "Por isso as panelas são de metal e os fios elétricos de cobre.", "🔌"),
        ],
    ),
    "a5-b1-ciencias-u1-m2": missao(
        [
            ("☀️", "O Sol aquece a água de rios e mares: ela **evapora** e sobe como vapor."),
            ("☁️", "No alto, o vapor esfria e **condensa**, formando as **nuvens**."),
            ("🌧️", "As gotas ficam pesadas e caem: **precipitação** (chuva). A água volta aos rios e infiltra no solo. As **plantas** também liberam vapor (**transpiração**)."),
        ],
        [
            ordem("Coloque o ciclo da água na ordem", ["Evaporação", "Condensação", "Precipitação", "Infiltração e escoamento"], "A água circula sem parar."),
            mc("A água vira vapor com o calor do Sol. Isso é...", ["evaporação", "condensação", "solidificação"], "Líquido → gasoso: **evaporação**.", "☀️"),
            mc("O vapor esfria e forma gotinhas nas nuvens. Isso é...", ["condensação", "evaporação", "fusão"], "Gasoso → líquido: **condensação**.", "☁️"),
            mc("A chuva, o granizo e a neve são formas de...", ["precipitação", "evaporação", "infiltração"], "A água **cai** das nuvens.", "🌧️"),
            mc("Como as florestas ajudam no ciclo da água?", ["Liberam vapor pela transpiração das plantas", "Bebem toda a chuva e secam o ar", "Não participam"], "A Amazônia forma **rios voadores** de umidade!", "🌳"),
            ligar([("sólido → líquido", "fusão"), ("líquido → gasoso", "evaporação"), ("gasoso → líquido", "condensação"), ("líquido → sólido", "solidificação")], "Ligue a mudança de estado ao nome"),
            tf("A água do planeta está sempre circulando.", True, "É o **ciclo da água**."),
        ],
    ),
    "a5-b1-ciencias-u1-m3": missao(
        [
            ("🧲", "O **ímã** atrai alguns metais, como o **ferro** e o **aço** (que tem ferro)."),
            ("🥤", "Ele **não** atrai plástico, madeira, vidro, papel nem **alumínio** (latinha)."),
            ("🧭", "A **bússola** tem uma agulha imantada que aponta para o **norte** magnético."),
        ],
        [
            separar("O ímã atrai?", ["Atrai", "Não atrai"],
                    [("prego de ferro", 0), ("clipe de aço", 0), ("tampinha de aço", 0), ("borracha", 1), ("lápis de madeira", 1), ("latinha de alumínio", 1)],
                    "O ímã atrai materiais com **ferro**."),
            mc("O ímã atrai uma **latinha de alumínio**?", ["Não", "Sim", "Só de noite"], "Alumínio não é atraído pelo ímã.", "🥫"),
            mc("Para separar pregos misturados com areia, uso...", ["um ímã", "uma peneira de pano", "água quente"], "O ímã puxa os pregos de ferro.", "🧲"),
            mc("Qual instrumento usa um ímã para orientar viajantes?", ["Bússola", "Termômetro", "Balança"], "A agulha da **bússola** é imantada.", "🧭"),
            tf("Dois ímãs podem se atrair ou se repelir, dependendo dos polos.", True, "Polos iguais se repelem; diferentes se atraem."),
            fill("O ímã atrai objetos que têm ___.", ["ferro", "plástico", "vidro"], "**Ferro** (e aço)."),
        ],
    ),
    # ------------------------------------------------------------ Ciências Humanas (História)
    "a5-b1-humanas-u1-m1": missao(
        [
            ("🏺", "Os **povos antigos** deixaram criações que usamos até hoje."),
            ("🔺", "**Egípcios**: pirâmides, papiro, calendário de 365 dias. **Gregos**: democracia, Olimpíadas, teatro."),
            ("🪶", "**Povos indígenas** do Brasil: cultivo da mandioca, cerâmica, conhecimento de plantas medicinais."),
        ],
        [
            ligar([("egípcios", "pirâmides"), ("gregos", "Jogos Olímpicos"), ("indígenas", "cultivo da mandioca"), ("romanos", "aquedutos")], "Ligue o povo à criação"),
            ligar([("papiro", "egípcios"), ("democracia", "gregos"), ("cerâmica marajoara", "indígenas"), ("algarismos 0 a 9", "indianos e árabes")], "Ligue a criação ao povo"),
            mc("Onde nasceram os **Jogos Olímpicos**?", ["Grécia Antiga", "Egito Antigo", "China Antiga"], "Em Olímpia, na **Grécia**.", "🏅"),
            mc("Que material os egípcios usavam para escrever?", ["Papiro", "Papel sulfite", "Tablet"], "Feito de uma planta do rio Nilo.", "📜"),
            tf("Os povos indígenas do Brasil já cultivavam plantas antes da chegada dos europeus.", True, "Mandioca, milho, amendoim..."),
        ],
    ),
    "a5-b1-humanas-u1-m2": missao(
        [
            ("🏞️", "Muitas civilizações antigas surgiram **perto de grandes rios**."),
            ("🌊", "Os **egípcios** viviam às margens do **Nilo**. Os **mesopotâmicos**, entre os rios **Tigre** e **Eufrates**."),
            ("🌾", "Os rios davam **água**, **peixes**, **terra fértil** e serviam de **caminho** para barcos."),
        ],
        [
            mc("Por que os povos antigos se fixavam perto de rios?", ["Água, terra fértil e transporte", "Para fugir da água", "Porque não havia outros lugares"], "O rio era a fonte da vida.", "🏞️"),
            mc("Qual rio foi essencial para o **Egito Antigo**?", ["Nilo", "Amazonas", "São Francisco"], "O Egito é um **presente do Nilo**.", "🔺"),
            mc("A **Mesopotâmia** ficava entre quais rios?", ["Tigre e Eufrates", "Nilo e Amazonas", "Tietê e Paraná"], "Mesopotâmia = **terra entre rios**.", "🗺️"),
            mc("As cheias do Nilo deixavam a terra...", ["fértil para plantar", "seca e rachada", "cheia de sal"], "Deixavam um lodo cheio de nutrientes.", "🌾"),
            tf("Muitas cidades do Brasil também nasceram perto de rios.", True, "Manaus, Belém, São Paulo (Tietê)..."),
        ],
    ),
    "a5-b1-humanas-u1-m3": missao(
        [
            ("🛕", "As **religiões e crenças** foram muito importantes para os povos antigos."),
            ("🔺", "Os **egípcios** acreditavam na vida após a morte e construíam pirâmides como túmulos dos faraós."),
            ("🏛️", "Os **gregos** tinham muitos deuses e construíam templos, como o **Partenon**. As crenças ajudavam a formar a **identidade** de cada povo."),
        ],
        [
            mc("Para que os egípcios construíam as pirâmides?", ["Como túmulos dos faraós", "Como escolas", "Como mercados"], "Eles acreditavam na vida após a morte.", "🔺"),
            mc("Os gregos antigos acreditavam em...", ["muitos deuses", "nenhum deus", "um único deus"], "Zeus, Atena, Poseidon...", "⚡"),
            mc("O **Partenon** era um templo de qual povo?", ["Gregos", "Egípcios", "Incas"], "Fica em **Atenas**.", "🏛️"),
            mc("Como as crenças ajudavam os povos antigos?", ["Davam sentido à vida e uniam as pessoas", "Atrapalhavam tudo", "Não tinham importância"], "Formavam a **identidade** do povo.", "🤝"),
            tf("Devemos respeitar as diferentes religiões e crenças.", True, "No Brasil, a liberdade religiosa é um direito."),
        ],
    ),
    # ------------------------------------------------------------ Ciências Humanas (Geografia)
    "a5-b1-humanas-u2-m1": missao(
        [
            ("📊", "O **IBGE** conta a população do Brasil no **Censo**."),
            ("🏙️", "Cidades fictícias do estado: **Vila Azul 120.000**, **Pedra Alta 45.000**, **Rio Claro 80.000**, **Serra Verde 15.000** habitantes."),
            ("📈", "Tabelas e gráficos ajudam a **comparar** os dados."),
        ],
        [
            mc("Qual cidade tem a **maior** população?", ["Vila Azul", "Rio Claro", "Pedra Alta"], "**120.000** habitantes.", "🏙️"),
            mc("Qual cidade tem a **menor** população?", ["Serra Verde", "Pedra Alta", "Rio Claro"], "**15.000** habitantes.", "🏡"),
            mc("Quantos habitantes **a mais** tem Rio Claro que Pedra Alta?", ["35.000", "125.000", "45.000"], "80.000 − 45.000 = **35.000**.", "🧮"),
            ordem("Da menor para a maior população", ["Serra Verde: 15.000", "Pedra Alta: 45.000", "Rio Claro: 80.000", "Vila Azul: 120.000"], "15 mil < 45 mil < 80 mil < 120 mil."),
            mc("Qual instituto faz o **Censo** no Brasil?", ["IBGE", "INSS", "ECA"], "**Instituto Brasileiro de Geografia e Estatística**.", "📋"),
            tf("O Censo conta quantas pessoas vivem no país.", True, "E também como elas vivem."),
        ],
    ),
    "a5-b1-humanas-u2-m2": missao(
        [
            ("🇧🇷", "A população brasileira é muito **diversa**."),
            ("🧑🏽‍🤝‍🧑🏻", "Somos formados por **indígenas**, **africanos e afrodescendentes**, **europeus**, **asiáticos** e muitos outros."),
            ("⚖️", "Ainda existem **desigualdades** e **racismo**. Combater o preconceito é dever de todos."),
        ],
        [
            mc("Qual frase descreve a população brasileira?", ["Muito diversa, formada por vários povos", "Toda igual", "Formada por um só povo"], "Somos um país **diverso**.", "🌈"),
            mc("O que é **racismo**?", ["Discriminar alguém pela cor da pele ou origem", "Uma corrida de carros", "Uma brincadeira legal"], "Racismo é **crime** no Brasil.", "🚫"),
            mc("Qual atitude combate o preconceito?", ["Respeitar e valorizar as diferenças", "Fazer piadas sobre a cor de alguém", "Excluir quem é diferente"], "Respeito e valorização.", "🤝"),
            separar("Atitude de respeito ou de preconceito?", ["Respeito", "Preconceito"],
                    [("conhecer outras culturas", 0), ("valorizar a história africana e indígena", 0), ("convidar todos para brincar", 0), ("apelidar pela cor da pele", 1), ("excluir pelo sotaque", 1)],
                    "A diversidade é a riqueza do Brasil."),
            tf("No Brasil, racismo é crime.", True, "Está previsto em lei."),
        ],
    ),
    "a5-b1-humanas-u2-m3": missao(
        [
            ("🗺️", "**Densidade demográfica** = número de habitantes ÷ área (hab/km²)."),
            ("🏙️", "Regiões **muito povoadas** têm muitas pessoas num espaço pequeno, como o **Sudeste**."),
            ("🌳", "Regiões **pouco povoadas** têm poucas pessoas num espaço grande, como o **Norte** (Amazônia)."),
        ],
        [
            mc("Qual região do Brasil é a **mais povoada**?", ["Sudeste", "Norte", "Centro-Oeste"], "SP, RJ e MG concentram muita gente.", "🏙️"),
            mc("Qual região tem a **menor densidade** demográfica?", ["Norte", "Sudeste", "Sul"], "Área enorme e poucas pessoas.", "🌳"),
            mc("Uma cidade tem **10.000** habitantes em **100 km²**. Qual é a densidade?", ["100 hab/km²", "1.000 hab/km²", "10 hab/km²"], "10.000 ÷ 100 = **100**.", "🧮"),
            mc("Cidade A: 500 hab/km². Cidade B: 20 hab/km². Qual é mais povoada?", ["Cidade A", "Cidade B", "Iguais"], "Mais pessoas por km².", "⚖️"),
            tf("Uma região grande sempre tem mais habitantes.", False, "O Norte é enorme, mas tem poucos habitantes."),
            fill("Pessoas por km² é a densidade ___.", ["demográfica", "do ar", "da água"], "Densidade **demográfica**."),
        ],
    ),
    # ------------------------------------------------------------ Ética
    "a5-b1-etica-u1-m1": missao(
        [
            ("🏛️", "**Cidadão** é quem tem **direitos e deveres** na sociedade."),
            ("🤝", "**Bem comum** é o que é bom para **todos**: ruas limpas, escola boa, natureza protegida."),
            ("🌱", "Atitudes cidadãs pensam no **coletivo**, não só em si mesmo."),
        ],
        [
            separar("Ajuda ou prejudica o bem comum?", ["Ajuda", "Prejudica"],
                    [("devolver um livro da biblioteca no prazo", 0), ("respeitar a faixa de pedestres", 0), ("economizar água", 0), ("pichar um monumento", 1), ("furar a fila", 1), ("jogar lixo no rio", 1)],
                    "Cidadania é pensar em todos."),
            mc("Você achou uma carteira com documentos na rua. O que fazer?", ["Entregar a um adulto ou à polícia para devolver", "Ficar com ela", "Jogar fora"], "Honestidade é cidadania.", "👛"),
            mc("A praça do bairro está suja. Qual atitude é cidadã?", ["Organizar com a comunidade e avisar a prefeitura", "Sujar mais", "Reclamar e não fazer nada"], "Participar faz diferença.", "🧹"),
            mc("O que é **bem comum**?", ["O que é bom para todos", "O que é bom só para mim", "Uma marca de roupa"], "Bem comum = **de todos**.", "🌍"),
            tf("Crianças também são cidadãs.", True, "Têm direitos e deveres conforme a idade."),
        ],
    ),
    "a5-b1-etica-u1-m2": missao(
        [
            ("🗳️", "Numa **assembleia**, a turma discute e decide junto."),
            ("📋", "Etapas: apresentar o **tema**, ouvir as **propostas**, **debater**, **votar** e respeitar o **resultado**."),
            ("🙋", "Todos têm direito de falar e votar. A **maioria** decide, mas a minoria é respeitada."),
        ],
        [
            ordem("Coloque as etapas da votação na ordem", ["Apresentar o tema", "Ouvir as propostas", "Debater as ideias", "Votar", "Contar os votos e anunciar o resultado"], "É assim que funciona a democracia."),
            mc("Na votação do passeio: **Zoológico 14**, **Museu 9**, **Parque 5**. Qual ganhou?", ["Zoológico", "Museu", "Parque"], "14 é a maioria.", "🦁"),
            mc("Quantos alunos votaram?", ["28", "23", "14"], "14 + 9 + 5 = **28**.", "🧮"),
            mc("Sua proposta perdeu. O que fazer?", ["Respeitar o resultado", "Brigar com os colegas", "Não ir ao passeio para sempre"], "Respeitar a decisão da maioria é democrático.", "🤝"),
            tf("Numa assembleia, todos podem dar sua opinião.", True, "Todos têm voz."),
            fill("O governo em que o povo escolhe pelo voto se chama ___.", ["democracia", "monarquia absoluta", "ditadura"], "**Democracia**."),
        ],
    ),
    "a5-b1-etica-u1-m3": missao(
        [
            ("🏘️", "Você pode **propor melhorias** para o seu bairro!"),
            ("📝", "Uma boa proposta diz: **o problema**, **a solução**, **quem pode ajudar** e **por que é importante**."),
            ("🎙️", "Fale com clareza e educação."),
            desafio("observe seu bairro com um adulto, escolha um problema e grave um áudio ou vídeo com a sua proposta de melhoria."),
        ],
        [
            ordem("Organize a proposta", ["Apresentar o problema", "Explicar por que é importante", "Propor uma solução", "Dizer quem pode ajudar"], "Uma proposta bem organizada convence mais."),
            mc("Qual é uma proposta **clara**?", ["Colocar lixeiras na praça Central, que vive suja", "Melhorar tudo", "Fazer alguma coisa"], "Diz **o quê** e **onde**.", "💡"),
            mc("Quem pode ajudar a consertar uma calçada quebrada?", ["A prefeitura", "O carteiro", "O dono da padaria"], "Calçadas públicas são cuidadas pela **prefeitura**.", "🏛️"),
            mc("Qual argumento mostra **por que** a proposta é importante?", ["Muitos idosos tropeçam ali", "Eu acho feio", "Porque sim"], "Bons argumentos mostram o benefício para todos.", "🧓"),
            tf("Propor melhorias para o bairro é uma forma de participação cidadã.", True, "Cidadania é participar!"),
        ],
    ),
    # ------------------------------------------------------------ Inglês
    "a5-b1-ingles-u1-m1": missao(
        [
            ("🎬", "O **present continuous** mostra o que está acontecendo **agora**."),
            ("📖", "**I am reading.** (Eu estou lendo.) · **She is playing.** (Ela está brincando.) · **They are running.** (Eles estão correndo.)"),
            ("❓", "**What is she doing?** = O que ela está fazendo?"),
        ],
        [
            mc("What is she doing? 👧📖", ["She is reading.", "She is swimming.", "She is sleeping."], "📖 = **reading**.", None),
            mc("What is he doing? 👦⚽", ["He is playing football.", "He is cooking.", "He is singing."], "⚽ = **playing football**.", None),
            mc("What are they doing? 🏊🏊", ["They are swimming.", "They are eating.", "They are writing."], "🏊 = **swimming**.", None),
            mc("What is she doing? 👩‍🍳", ["She is cooking.", "She is running.", "She is reading."], "👩‍🍳 = **cooking**.", None),
            mc("O que quer dizer **I am sleeping**?", ["Eu estou dormindo.", "Eu durmo cedo.", "Eu vou dormir."], "**am + sleeping** = estou dormindo.", "😴"),
            fill("He ___ singing. 🎤", ["is", "are", "am"], "He/She/It → **is**."),
            fill("They ___ dancing. 💃🕺", ["are", "is", "am"], "They/We/You → **are**."),
        ],
    ),
    "a5-b1-ingles-u1-m2": missao(
        [
            ("➕", "Para formar o **-ing**, geralmente só acrescentamos: **read → reading**, **play → playing**."),
            ("✂️", "Se terminar em **e**, tiramos o e: **dance → dancing**, **write → writing**."),
            ("✌️", "Alguns dobram a última letra: **run → running**, **swim → swimming**, **sit → sitting**."),
        ],
        [
            ligar([("read", "reading"), ("dance", "dancing"), ("run", "running"), ("play", "playing")], "Ligue o verbo à forma com -ing"),
            mc("Qual é o **-ing** de **write**?", ["writing", "writeing", "writting"], "Tira o **e**: writing.", "✍️"),
            mc("Qual é o **-ing** de **swim**?", ["swimming", "swiming", "swimeing"], "Dobra o **m**: swimming.", "🏊"),
            mc("Qual é o **-ing** de **eat**?", ["eating", "eatting", "eateing"], "Só acrescenta: eating.", "🍽️"),
            separar("Como formar o -ing?", ["Só acrescenta -ing", "Tira o e", "Dobra a letra"],
                    [("sing", 0), ("jump", 0), ("make", 1), ("ride", 1), ("sit", 2), ("run", 2)],
                    "singing, jumping · making, riding · sitting, running."),
            fill("I am ___ a book. (ler)", ["reading", "readding", "read"], "**reading**."),
        ],
    ),
    "a5-b1-ingles-u1-m3": missao(
        [
            ("🎙️", "**Right now I'm...** = Agora mesmo eu estou..."),
            ("📱", "Exemplos: **Right now I'm studying English. I'm sitting on the sofa. My cat is sleeping.**"),
            ("🗣️", "Use **I'm** (= I am) + verbo com **-ing**."),
            desafio("grave um áudio dizendo 3 coisas que você e sua família estão fazendo agora, em inglês. Exemplo: Right now I'm drawing."),
        ],
        [
            mc("Como dizer **Agora eu estou desenhando**?", ["Right now I'm drawing.", "Right now I draw yesterday.", "I drawing now am."], "**I'm drawing**.", "🎨"),
            mc("Como dizer **Minha mãe está cozinhando**?", ["My mom is cooking.", "My mom are cooking.", "My mom cooking is."], "**is cooking**.", "👩‍🍳"),
            mc("O que quer dizer **I'm**?", ["I am", "I was", "I will"], "I'm = **I am**.", "💬"),
            ordem("Monte a frase", ["Right now", "I'm", "listening", "to music."], "**Right now I'm listening to music.**"),
            fill("Right now my dog ___ sleeping. 🐶", ["is", "are", "am"], "My dog = he/it → **is**."),
            tf("**We are playing** quer dizer nós estamos brincando.", True, "We are + playing."),
        ],
    ),
}
