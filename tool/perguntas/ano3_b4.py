"""3º ano · 4º bimestre."""
from base import desafio, fill, ligar, mc, missao, ordem, separar, tf

MISSOES = {
    # ------------------------------------------------------------ Português
    "a3-b4-portugues-u1-m1": missao(
        [
            ("🎂", "A **receita** é um texto que ensina a fazer algo, passo a passo."),
            ("📝", "Ela tem duas partes: **ingredientes** (o que usar) e **modo de preparo** (como fazer)."),
            ("🔢", "A **ordem** dos passos é muito importante. Se trocar, o bolo não dá certo!"),
        ],
        [
            ordem("Coloque a receita de bolo na ordem", ["Separar os ingredientes", "Misturar ovos, açúcar e farinha", "Colocar a massa na forma", "Assar no forno", "Esperar esfriar e servir"],
                  "Primeiro separamos, depois misturamos, assamos e servimos."),
            ordem("Coloque os passos do suco de laranja na ordem", ["Lavar as laranjas", "Cortar ao meio", "Espremer", "Servir no copo"],
                  "Lavar, cortar, espremer e servir."),
            separar("Ingrediente ou modo de preparo?", ["Ingredientes", "Modo de preparo"],
                    [("2 ovos", 0), ("1 xícara de leite", 0), ("3 xícaras de farinha", 0), ("Bata tudo no liquidificador", 1), ("Asse por 40 minutos", 1)],
                    "Ingredientes dizem **o que** usar. O modo de preparo diz **como** fazer."),
            mc("Para que serve uma receita?", ["Ensinar a preparar um prato", "Contar uma aventura", "Dar notícias do jornal"], "A receita é um texto **instrucional**.", "📖"),
            mc("Em **Asse por 40 minutos**, a palavra **asse** dá uma...", ["ordem (instrução)", "pergunta", "rima"], "Os verbos da receita dão instruções: **misture, asse, sirva**.", "🔥"),
            fill("Na receita, a lista do que vamos usar se chama ___.", ["ingredientes", "personagens", "título"], "A lista de **ingredientes** vem primeiro."),
            tf("A ordem dos passos de uma receita não importa.", False, "Se a ordem mudar, a receita pode dar errado."),
        ],
    ),
    "a3-b4-portugues-u1-m2": missao(
        [
            ("📔", "O **diário** é onde contamos o que aconteceu no nosso dia."),
            ("🚀", "Leia: **Querido diário, hoje a nave pousou num planeta azul. Encontramos um lago brilhante e coletamos pedras. Estou cansada, mas muito feliz! — Capitã Luna**"),
            ("💡", "A **ideia principal** é o assunto mais importante: a nave **pousou e explorou** um planeta novo."),
        ],
        [
            mc("Qual é a **ideia principal** do diário da Capitã Luna?", ["A exploração de um planeta novo", "Uma receita de bolo", "Uma briga na nave"], "O texto conta a chegada e a exploração do planeta.", "🪐"),
            mc("Quem escreveu o diário?", ["A Capitã Luna", "O lago", "Um robô"], "Ela assina no final: **Capitã Luna**.", "👩‍🚀"),
            mc("Como a capitã se sentia no fim do dia?", ["Cansada, mas feliz", "Triste e com medo", "Com fome e brava"], "Ela escreveu: **cansada, mas muito feliz**.", "😊"),
            mc("O que a tripulação coletou?", ["Pedras", "Flores", "Peixes"], "Eles **coletaram pedras**.", "🪨"),
            tf("O diário costuma ser escrito em primeira pessoa (eu, nós).", True, "Quem escreve conta o que **ele mesmo** viveu."),
            fill("Um diário geralmente começa com ___.", ["Querido diário", "Era uma vez", "Ingredientes"], "**Querido diário** é o começo mais comum."),
            separar("Isso é de diário ou de receita?", ["Diário", "Receita"],
                    [("Hoje eu fui à praia.", 0), ("Querido diário,", 0), ("Misture a farinha.", 1), ("Asse por 30 minutos.", 1)],
                    "O diário conta o dia. A receita dá instruções."),
        ],
    ),
    "a3-b4-portugues-u1-m3": missao(
        [
            ("✉️", "A **carta pessoal** tem partes: **local e data**, **saudação**, **mensagem**, **despedida** e **assinatura**."),
            ("👋", "Exemplo de saudação: **Querida Sofia,**. Exemplo de despedida: **Um abraço,**."),
            ("📮", "No envelope vai o **endereço** de quem vai receber."),
            desafio("escreva uma carta para um amigo ou parente, peça para um adulto ler e tire uma foto."),
        ],
        [
            ordem("Coloque as partes da carta na ordem", ["São Paulo, 23 de novembro", "Querida Sofia,", "Estou com saudade! Na escola aprendi...", "Um abraço,", "Lucas"],
                  "Local e data, saudação, mensagem, despedida e assinatura."),
            mc("Qual destas é uma **saudação**?", ["Querido vovô,", "Beijos,", "Rio, 3 de maio"], "A saudação cumprimenta quem vai ler.", "👋"),
            mc("Qual destas é uma **despedida**?", ["Com carinho,", "Querida Ana,", "Belo Horizonte, 10 de junho"], "A despedida vem antes da assinatura.", "💌"),
            mc("Onde vai o nome de quem escreveu a carta?", ["No final, na assinatura", "No começo, antes da data", "No meio da mensagem"], "A **assinatura** fica no fim.", "✍️"),
            tf("Para a carta chegar, o envelope precisa do endereço.", True, "O carteiro usa o **endereço** para entregar."),
            fill("Na carta, a parte que fala **onde** e **quando** foi escrita é o local e a ___.", ["data", "assinatura", "saudação"], "Exemplo: **Recife, 5 de abril**."),
        ],
    ),
    # ------------------------------------------------------------ Matemática
    "a3-b4-matematica-u1-m1": missao(
        [
            ("🗺️", "O **croqui** é um desenho simples de um lugar visto de cima, como um mapa."),
            ("🧭", "Para descrever caminhos usamos: **siga em frente**, **vire à direita**, **vire à esquerda**."),
            ("🏫", "Exemplo: **Saia de casa, siga em frente 2 quarteirões e vire à direita. A escola fica na esquina.**"),
        ],
        [
            mc("O que é um croqui?", ["Um desenho simples de um lugar visto de cima", "Uma receita", "Um tipo de relógio"], "É como um mapa feito à mão.", "🗺️"),
            mc("Saindo de casa: a padaria fica **à direita** e a farmácia **à esquerda**. Virei à esquerda. Onde vou chegar?", ["Na farmácia", "Na padaria", "Na escola"], "Esquerda → **farmácia**.", "💊"),
            mc("Estou de frente para a escola. Viro de costas. A escola fica...", ["atrás de mim", "na minha frente", "à minha direita"], "Virando de costas, ela fica **atrás**.", "🏫"),
            ordem("Coloque o caminho até a escola na ordem", ["Sair de casa", "Seguir em frente 2 quarteirões", "Virar à direita", "Chegar na escola"], "Os comandos do caminho seguem uma ordem."),
            mc("A praça fica **entre** a igreja e o mercado. Andando da igreja até o mercado, passo...", ["pela praça", "pelo rio", "pelo hospital"], "Entre = no meio do caminho.", "🌳"),
            tf("Um croqui pode mostrar o caminho de casa até a escola.", True, "Ele ajuda a planejar trajetos."),
            fill("Para não ir pela esquerda, eu viro à ___.", ["direita", "frente", "baixo"], "O contrário de esquerda é **direita**."),
        ],
    ),
    "a3-b4-matematica-u1-m2": missao(
        [
            ("🧊", "Figuras espaciais têm **faces** (lados planos), **arestas** (linhas onde as faces se encontram) e **vértices** (pontas)."),
            ("🎲", "O **cubo** (como o dado) tem **6 faces**, **12 arestas** e **8 vértices**."),
            ("🔺", "A **pirâmide de base quadrada** tem **5 faces**: 4 triângulos e 1 quadrado."),
        ],
        [
            mc("Quantas **faces** tem um cubo?", ["6", "4", "8"], "Conte os lados de um dado: **6 faces**.", "🎲"),
            mc("Quantos **vértices** tem um cubo?", ["8", "6", "12"], "São **8 pontas**: 4 em cima e 4 embaixo.", "🧊"),
            mc("Quantas **arestas** tem um cubo?", ["12", "8", "6"], "4 em cima + 4 embaixo + 4 em pé = **12**.", "📦"),
            mc("Quantas faces tem uma **pirâmide de base quadrada**?", ["5", "4", "6"], "1 quadrado + 4 triângulos = **5 faces**.", "🔺"),
            mc("Qual figura **rola** com facilidade?", ["Esfera", "Cubo", "Pirâmide"], "A **esfera** é toda arredondada, como a bola.", "⚽"),
            ligar([("dado", "cubo"), ("bola", "esfera"), ("lata de milho", "cilindro"), ("casquinha de sorvete", "cone")],
                  "Ligue o objeto à figura espacial"),
            separar("Tem só superfície plana ou tem parte arredondada?", ["Só faces planas", "Tem parte arredondada"],
                    [("cubo", 0), ("pirâmide", 0), ("caixa de sapato", 0), ("esfera", 1), ("cilindro", 1), ("cone", 1)],
                    "Cilindro, cone e esfera têm partes arredondadas e rolam."),
            tf("Vértice é a ponta onde as arestas se encontram.", True, "Os vértices são os **cantinhos** da figura."),
        ],
    ),
    "a3-b4-matematica-u1-m3": missao(
        [
            ("👯", "Figuras **congruentes** são **gêmeas**: têm a mesma forma e o mesmo tamanho."),
            ("🔄", "Mesmo se uma estiver **girada** ou **virada**, continuam congruentes."),
            ("📐", "Se o tamanho for diferente, **não** são congruentes, mesmo com a mesma forma."),
        ],
        [
            ligar([("🟥 quadrado de 2 cm", "🟥 quadrado de 2 cm girado"), ("🔺 triângulo de 3 cm", "🔻 triângulo de 3 cm virado"), ("⚪ círculo de 4 cm", "⚪ outro círculo de 4 cm")],
                  "Ligue as figuras gêmeas (congruentes)"),
            mc("Quando duas figuras são **congruentes**?", ["Mesma forma e mesmo tamanho", "Mesma cor", "Mesma forma, tamanhos diferentes"], "Forma e tamanho iguais.", "👯"),
            mc("Um quadrado de **3 cm** e um de **5 cm** são congruentes?", ["Não, os tamanhos são diferentes", "Sim, são quadrados", "Sim, se forem da mesma cor"], "Precisa ter o **mesmo tamanho** também.", "🟦"),
            tf("Se eu girar um triângulo, ele continua congruente ao original.", True, "Girar não muda a forma nem o tamanho."),
            mc("Quantos **lados** tem um triângulo?", ["3", "4", "5"], "Tri = três.", "🔺"),
            mc("Quantos **vértices** tem um quadrado?", ["4", "3", "6"], "Quatro cantinhos.", "🟥"),
            ligar([("triângulo", "3 lados"), ("quadrado", "4 lados"), ("pentágono", "5 lados"), ("hexágono", "6 lados")],
                  "Ligue o polígono ao número de lados"),
        ],
    ),
    "a3-b4-matematica-u2-m1": missao(
        [
            ("🕒", "No **relógio de ponteiros**, o ponteiro **pequeno** mostra a **hora** e o **grande** mostra os **minutos**."),
            ("🔝", "Ponteiro grande no **12** = hora exata (**em ponto**). No **6** = **e meia**."),
            ("📟", "No relógio **digital**, 3 e meia aparece assim: **03:30**."),
        ],
        [
            mc("Que horas o relógio marca?", ["3 horas", "12 horas", "6 horas"], "Ponteiro pequeno no 3, grande no 12: **3 horas em ponto**.", "🕒"),
            mc("Que horas o relógio marca?", ["9 horas", "12 e 45", "3 horas"], "Ponteiro pequeno no 9: **9 horas**.", "🕘"),
            mc("Que horas o relógio marca?", ["1 e meia", "6 horas", "1 hora"], "Pequeno entre 1 e 2, grande no 6: **1 e meia**.", "🕜"),
            mc("Como aparece **7 e meia** no relógio digital?", ["07:30", "07:00", "07:60"], "Meia hora = **30 minutos**.", "📟"),
            mc("Uma hora tem quantos minutos?", ["60", "30", "100"], "**60 minutos** = 1 hora.", "⏰"),
            ligar([("🕐", "1:00"), ("🕓", "4:00"), ("🕖", "7:00"), ("🕙", "10:00")], "Ligue o relógio à hora digital"),
            mc("O filme começou às **2 horas** e durou **2 horas**. A que horas acabou?", ["4 horas", "2 horas", "6 horas"], "2 + 2 = **4 horas**.", "🎬"),
            tf("O ponteiro pequeno mostra os minutos.", False, "O **pequeno** mostra a hora. O **grande** mostra os minutos."),
        ],
    ),
    "a3-b4-matematica-u2-m2": missao(
        [
            ("🎲", "Um dado tem **6 faces**: os resultados possíveis são **1, 2, 3, 4, 5 e 6**."),
            ("🪙", "Numa moeda, os resultados possíveis são **cara** ou **coroa**."),
            ("📈", "Num saco com **mais** bolas de uma cor, essa cor é **mais provável** de sair."),
        ],
        [
            mc("Quantos resultados possíveis tem um dado comum?", ["6", "2", "12"], "1, 2, 3, 4, 5 e 6.", "🎲"),
            mc("Jogando uma moeda, quais são os resultados possíveis?", ["Cara ou coroa", "Só cara", "1 a 6"], "A moeda tem dois lados.", "🪙"),
            mc("Num dado, sair um número **par** ou **ímpar**: qual tem mais chance?", ["As duas chances são iguais", "Par", "Ímpar"], "Pares: 2, 4, 6. Ímpares: 1, 3, 5. **3 e 3**.", "⚖️"),
            mc("Saco com **5 bolas vermelhas, 2 azuis e 1 verde**. Qual cor é **mais provável**?", ["Vermelha", "Azul", "Verde"], "Há mais bolas vermelhas.", "🔴"),
            mc("No mesmo saco, qual cor é **menos provável**?", ["Verde", "Vermelha", "Azul"], "Só há **1** verde.", "🟢"),
            tf("Num dado comum, é impossível sair o número 0.", True, "O dado vai de **1 a 6**."),
            separar("No dado comum, esse resultado é possível ou impossível?", ["Possível", "Impossível"],
                    [("sair 4", 0), ("sair um número menor que 3", 0), ("sair 6", 0), ("sair 8", 1), ("sair 0", 1)],
                    "Só é possível o que está entre 1 e 6."),
        ],
    ),
    "a3-b4-matematica-u2-m3": missao(
        [
            ("📊", "O **gráfico de barras** mostra quantidades: quanto mais alta a barra, maior o número."),
            ("⚽", "Esporte preferido da turma: **Futebol 9**, **Vôlei 5**, **Natação 7**, **Basquete 3**."),
            ("📋", "Uma **tabela** também organiza dados em linhas e colunas."),
        ],
        [
            mc("Qual é o esporte preferido da turma?", ["Futebol", "Natação", "Vôlei"], "Futebol tem a barra mais alta: **9**.", "⚽"),
            mc("Qual esporte teve menos votos?", ["Basquete", "Vôlei", "Natação"], "Basquete teve **3**.", "🏀"),
            mc("Quantos alunos a mais preferem natação do que vôlei?", ["2", "12", "7"], "7 − 5 = **2**.", "🏊"),
            mc("Quantos alunos votaram ao todo?", ["24", "21", "19"], "9 + 5 + 7 + 3 = **24**.", "🧮"),
            ordem("Do esporte com mais votos ao com menos", ["⚽ Futebol: 9", "🏊 Natação: 7", "🏐 Vôlei: 5", "🏀 Basquete: 3"], "9 > 7 > 5 > 3."),
            mc("Futebol teve quantos votos a mais que basquete?", ["6", "12", "3"], "9 − 3 = **6**.", "📊"),
            tf("Num gráfico de barras, a barra mais baixa é a de maior valor.", False, "A barra mais **alta** tem o maior valor."),
        ],
    ),
    # ------------------------------------------------------------ Ciências
    "a3-b4-ciencias-u1-m1": missao(
        [
            ("🏖️", "Solo **arenoso**: tem muita areia, é solto e a água passa **rápido**."),
            ("🏺", "Solo **argiloso**: tem muita argila (barro), é grudento e segura a água. Usado para fazer **tijolos e potes**."),
            ("🌱", "Solo **humífero**: escuro, cheio de restos de plantas e animais (**húmus**). Ótimo para **plantar**!"),
        ],
        [
            mc("Solo **escuro**, cheio de folhas e restos de plantas. Qual é?", ["Humífero", "Arenoso", "Argiloso"], "O **húmus** deixa o solo escuro e fértil.", "🌱"),
            mc("Solo **grudento** que serve para fazer tijolos e vasos. Qual é?", ["Argiloso", "Humífero", "Arenoso"], "A **argila** é modelável.", "🏺"),
            mc("Solo **solto** onde a água passa bem rápido. Qual é?", ["Arenoso", "Argiloso", "Humífero"], "A **areia** tem grãos grandes e soltos.", "🏖️"),
            mc("Qual solo é melhor para uma **horta**?", ["Humífero", "Arenoso", "Argiloso"], "O humífero tem muitos nutrientes.", "🥕"),
            ligar([("arenoso", "areia"), ("argiloso", "barro"), ("humífero", "húmus")], "Ligue o solo ao que ele tem mais"),
            tf("As minhocas ajudam a deixar o solo fofo e fértil.", True, "Elas cavam túneis e misturam o solo."),
            fill("O solo bom para fazer tijolos é o ___.", ["argiloso", "arenoso", "humífero"], "A argila endurece quando seca ou é queimada."),
        ],
    ),
    "a3-b4-ciencias-u1-m2": missao(
        [
            ("🧪", "Experimento: colocamos **areia**, **argila** e **terra com húmus** em três filtros e jogamos água."),
            ("💨", "Na **areia** a água passa **muito rápido**: o solo é **permeável**."),
            ("🐌", "Na **argila** a água passa **bem devagar** ou quase não passa: o solo é **pouco permeável**."),
        ],
        [
            mc("Em qual solo a água passou **mais rápido**?", ["Arenoso", "Argiloso", "Humífero"], "A areia tem espaços grandes entre os grãos.", "💨"),
            mc("Em qual solo a água passou **mais devagar**?", ["Argiloso", "Arenoso", "Humífero"], "A argila tem grãos bem pequenos e juntinhos.", "🐌"),
            ordem("Do solo onde a água passa mais rápido ao mais devagar", ["Arenoso", "Humífero", "Argiloso"], "Areia > húmus > argila."),
            mc("Por que a água **empoça** no barro depois da chuva?", ["O solo argiloso segura a água", "O barro é quente", "A água fica com medo"], "A argila deixa a água passar pouco.", "🌧️"),
            tf("Solo permeável é aquele que deixa a água passar.", True, "Permeável = deixa passar."),
            fill("Num experimento, precisamos usar a mesma quantidade de ___ em cada filtro.", ["água", "suco", "tinta"], "Para comparar direito, mudamos só o tipo de solo."),
        ],
    ),
    "a3-b4-ciencias-u1-m3": missao(
        [
            ("🚜", "O solo é usado na **agricultura**: plantar alimentos como arroz, feijão e milho."),
            ("🏗️", "Também é usado nas **construções**: casas, prédios e estradas."),
            ("⛏️", "Na **mineração**, tiramos do solo minérios como ferro e ouro."),
        ],
        [
            ligar([("plantação de milho", "agricultura"), ("prédio novo", "construção"), ("tirar ferro do chão", "mineração"), ("criação de vacas", "pecuária")],
                  "Ligue a atividade ao uso do solo"),
            mc("Plantar feijão é um uso do solo na...", ["agricultura", "mineração", "construção"], "**Agricultura** é o cultivo de plantas.", "🌾"),
            mc("Tirar ouro da terra é...", ["mineração", "agricultura", "pecuária"], "**Mineração** retira minérios do solo.", "⛏️"),
            mc("O que pode acontecer com o solo sem árvores na chuva forte?", ["A terra é levada (erosão)", "Fica mais fértil", "Nada acontece"], "Sem raízes, a água leva a terra: é a **erosão**.", "🌧️"),
            tf("Cobrir o solo com plantas ajuda a protegê-lo.", True, "As raízes seguram a terra."),
            separar("Ajuda ou prejudica o solo?", ["Ajuda", "Prejudica"],
                    [("plantar árvores", 0), ("adubo natural", 0), ("revezar plantações", 0), ("queimadas", 1), ("lixo enterrado", 1), ("desmatar tudo", 1)],
                    "Cuidar do solo garante alimentos no futuro."),
        ],
    ),
    # ------------------------------------------------------------ Ciências Humanas (História)
    "a3-b4-humanas-u1-m1": missao(
        [
            ("🏙️", "Toda cidade tem **prédios públicos**, que servem a toda a população."),
            ("🏥", "**Hospital** e **posto de saúde** cuidam da saúde. **Escola** ensina. **Prefeitura** administra a cidade."),
            ("🚒", "O **corpo de bombeiros** salva pessoas, e a **biblioteca** empresta livros."),
        ],
        [
            ligar([("hospital", "cuidar da saúde"), ("escola", "ensinar"), ("prefeitura", "administrar a cidade"), ("biblioteca", "emprestar livros")],
                  "Ligue o prédio público à sua função"),
            mc("Machucou o pé jogando bola. Para onde ir?", ["Posto de saúde ou hospital", "Biblioteca", "Prefeitura"], "Saúde = **posto** ou **hospital**.", "🦶"),
            mc("Onde trabalha o prefeito?", ["Na prefeitura", "No mercado", "Na padaria"], "A **prefeitura** cuida da cidade.", "🏛️"),
            mc("Quero ler um livro sem comprar. Aonde vou?", ["Biblioteca pública", "Hospital", "Delegacia"], "A **biblioteca** empresta livros.", "📚"),
            separar("Separe os lugares", ["Prédio público", "Outro lugar"],
                    [("escola pública", 0), ("posto de saúde", 0), ("corpo de bombeiros", 0), ("loja de brinquedos", 1), ("minha casa", 1)],
                    "Prédios públicos atendem toda a população."),
            tf("A praça é um espaço que todos podem usar.", True, "A praça é **pública**."),
        ],
    ),
    "a3-b4-humanas-u1-m2": missao(
        [
            ("🏡", "Espaço **privado** pertence a uma pessoa ou empresa: **minha casa**, **uma loja**."),
            ("🌳", "Espaço **público** é de todos: **praça**, **rua**, **escola pública**, **parque**."),
            ("🌲", "**Áreas de conservação** são espaços públicos que protegem a natureza, como os parques nacionais."),
        ],
        [
            separar("Público ou privado?", ["Público", "Privado"],
                    [("praça", 0), ("rua", 0), ("parque nacional", 0), ("hospital público", 0), ("minha casa", 1), ("loja de roupas", 1), ("casa do vizinho", 1)],
                    "Público é de todos. Privado tem dono."),
            mc("A **rua** é um espaço...", ["público", "privado", "secreto"], "Todos podem usar a rua.", "🛣️"),
            mc("A casa da família de Ana é um espaço...", ["privado", "público", "de conservação"], "Só entra quem a família deixa.", "🏠"),
            mc("Para que serve uma **área de conservação**?", ["Proteger a natureza", "Construir prédios", "Jogar lixo"], "Ela protege plantas, animais e rios.", "🌲"),
            tf("Um mercado é um espaço privado, mesmo aberto ao público.", True, "Ele tem **dono**, mas recebe clientes."),
            fill("O parque da cidade é um espaço ___.", ["público", "privado", "particular"], "É de todos os moradores."),
        ],
    ),
    "a3-b4-humanas-u1-m3": missao(
        [
            ("🤝", "O que é **público** é de **todos**: por isso todos devem cuidar."),
            ("🚮", "Não riscar paredes, jogar lixo na lixeira e não quebrar brinquedos da praça."),
            ("📢", "Se algo estiver estragado, podemos **avisar a prefeitura**."),
        ],
        [
            separar("Essa atitude cuida ou estraga?", ["Cuida", "Estraga"],
                    [("jogar lixo na lixeira", 0), ("respeitar a fila", 0), ("avisar sobre um buraco", 0), ("pichar o muro da escola", 1), ("arrancar as flores do jardim", 1), ("quebrar o balanço", 1)],
                    "Cuidar do que é de todos é ser **cidadão**."),
            mc("O balanço da praça quebrou. O que fazer?", ["Avisar a prefeitura", "Quebrar o resto", "Fingir que não viu"], "A prefeitura cuida das praças.", "🛝"),
            mc("Na biblioteca, como tratar os livros?", ["Com cuidado, sem rasgar", "Riscando", "Levando sem devolver"], "Outras pessoas vão ler depois.", "📚"),
            tf("Riscar a carteira da escola não tem problema porque não é minha.", False, "É de todos e outros alunos vão usar."),
            fill("Quem cuida dos espaços públicos é ___.", ["todo mundo", "ninguém", "só o prefeito"], "Cada um faz a sua parte."),
        ],
    ),
    # ------------------------------------------------------------ Ciências Humanas (Geografia)
    "a3-b4-humanas-u2-m1": missao(
        [
            ("♻️", "Na **coleta seletiva**, separamos o lixo reciclável por cor."),
            ("🟦", "**Azul** = papel · **Vermelho** = plástico · **Verde** = vidro · **Amarelo** = metal"),
            ("🟫", "**Marrom** = orgânico (restos de comida), que pode virar adubo."),
        ],
        [
            separar("Separe o lixo", ["🟦 Papel", "🟥 Plástico", "🟩 Vidro", "🟨 Metal"],
                    [("jornal", 0), ("caixa de papelão", 0), ("garrafa PET", 1), ("sacolinha", 1), ("pote de vidro", 2), ("garrafa de vidro", 2), ("lata de refrigerante", 3), ("tampinha de metal", 3)],
                    "Cada material vai na lixeira da sua cor."),
            mc("Casca de banana vai em qual lixeira?", ["Marrom (orgânico)", "Azul (papel)", "Verde (vidro)"], "Restos de comida são **orgânicos**.", "🍌"),
            mc("Lata de suco vai na lixeira...", ["amarela", "azul", "verde"], "Lata é **metal** = amarela.", "🥫"),
            ligar([("azul", "papel"), ("vermelho", "plástico"), ("verde", "vidro"), ("amarelo", "metal")], "Ligue a cor ao material"),
            tf("Reciclar diminui o lixo e economiza recursos da natureza.", True, "O material é usado de novo."),
        ],
    ),
    "a3-b4-humanas-u2-m2": missao(
        [
            ("💧", "Usamos água para **beber, cozinhar, tomar banho, limpar** e também na **agricultura** e nas **fábricas**."),
            ("🚿", "Um banho de **15 minutos** pode gastar mais de **100 litros** de água!"),
            ("🪣", "Pequenas atitudes economizam muita água."),
        ],
        [
            separar("Economiza ou desperdiça água?", ["Economiza", "Desperdiça"],
                    [("banho de 5 minutos", 0), ("balde para lavar o carro", 0), ("reaproveitar água da chuva", 0), ("lavar a calçada com mangueira", 1), ("torneira pingando", 1), ("escovar dentes com a torneira aberta", 1)],
                    "Usar só o necessário é economizar."),
            mc("Qual forma gasta **menos** água para lavar o carro?", ["Com balde e pano", "Com mangueira aberta", "Na chuva forte"], "O balde controla a água usada.", "🚗"),
            mc("Uma torneira pingando o dia todo...", ["desperdiça muitos litros", "não gasta nada", "economiza água"], "Gota a gota, vai muita água!", "🚰"),
            mc("Onde se usa **mais** água no Brasil?", ["Na agricultura (irrigação)", "Nos aquários", "Nas piscinas"], "A irrigação das plantações usa a maior parte.", "🌾"),
            tf("A água da chuva pode ser guardada para regar plantas.", True, "Isso se chama **reaproveitar** a água."),
            fill("Para economizar, fecho a torneira enquanto ___ os dentes.", ["escovo", "como", "durmo"], "Torneira fechada durante a escovação."),
        ],
    ),
    "a3-b4-humanas-u2-m3": missao(
        [
            ("🕵️", "Hoje você é um **detetive do desperdício**!"),
            ("💡", "Procure em casa: luz acesa sem ninguém, TV ligada sozinha, torneira pingando, banho longo."),
            ("📝", "Para cada desperdício, pense numa **solução**."),
            desafio("procure em casa um desperdício de água ou energia, conte para um adulto e combinem juntos uma solução."),
        ],
        [
            ligar([("luz acesa sem ninguém", "apagar ao sair"), ("torneira pingando", "chamar alguém para consertar"), ("banho muito longo", "banho mais rápido"), ("TV ligada sem ninguém", "desligar a TV")],
                  "Ligue o desperdício à solução"),
            mc("A geladeira fica aberta enquanto você pensa no que comer. Isso...", ["gasta energia", "economiza energia", "não muda nada"], "Decida antes e abra rapidinho.", "🧊"),
            mc("Qual atitude economiza energia?", ["Usar a luz do sol de dia", "Deixar o carregador na tomada sempre", "Acender todas as luzes"], "A luz do sol é de graça!", "☀️"),
            tf("Um bom detetive do desperdício propõe soluções.", True, "Encontrar o problema e resolver!"),
            fill("Ao sair do quarto, eu ___ a luz.", ["apago", "acendo", "pinto"], "Apagar a luz economiza energia."),
        ],
    ),
    # ------------------------------------------------------------ Ética
    "a3-b4-etica-u1-m1": missao(
        [
            ("🤔", "**Necessidade** é o que precisamos para viver bem: comida, água, casa, roupa, escola, saúde."),
            ("🎁", "**Desejo** é o que queremos, mas dá para viver sem: brinquedo novo, videogame, doces."),
            ("💰", "Antes de comprar, pergunte: **eu preciso ou eu quero?**"),
        ],
        [
            separar("Preciso ou quero?", ["Preciso (necessidade)", "Quero (desejo)"],
                    [("água", 0), ("comida", 0), ("remédio quando estou doente", 0), ("casaco no frio", 0), ("videogame novo", 1), ("tênis que pisca", 1), ("figurinhas", 1), ("pirulito", 1)],
                    "Necessidades vêm primeiro. Desejos podem esperar."),
            mc("Qual destas é uma **necessidade**?", ["Ter onde morar", "Ter o celular mais novo", "Ter 10 bonecas"], "Moradia é necessidade.", "🏠"),
            mc("Seu tênis ainda está bom, mas você viu um novo bonito. Ele é...", ["um desejo", "uma necessidade", "um remédio"], "Você **quer**, mas **não precisa** agora.", "👟"),
            mc("Antes de comprar algo, uma boa pergunta é...", ["Eu preciso ou eu quero?", "Qual é a cor?", "Quem tem mais?"], "Assim fazemos um consumo **consciente**.", "💭"),
            tf("Comprar tudo o que quero sempre é consumo consciente.", False, "Consumo consciente é pensar antes de comprar."),
            fill("Juntar dinheiro para comprar algo depois se chama ___.", ["poupar", "gastar", "perder"], "**Poupar** é guardar para depois."),
        ],
    ),
    "a3-b4-etica-u1-m2": missao(
        [
            ("🤝", "Alguns desafios só dá para vencer **em equipe**."),
            ("🗣️", "Numa equipe, cada um **ouve** o outro, **divide tarefas** e **ajuda** quem precisa."),
            ("🧩", "Exemplo: para montar um quebra-cabeça gigante, um separa as bordas, outro as cores e todos encaixam juntos."),
        ],
        [
            mc("A turma vai montar um cartaz. O que é trabalhar em equipe?", ["Dividir tarefas e ajudar uns aos outros", "Um faz tudo sozinho", "Cada um briga pela sua ideia"], "Todos participam!", "🖍️"),
            mc("Um colega não entendeu a tarefa. O que fazer?", ["Explicar com paciência", "Rir dele", "Deixar ele de fora"], "Ajudar faz a equipe crescer.", "🫂"),
            mc("Duas ideias diferentes no grupo. Como resolver?", ["Conversar e escolher juntos", "Quem grita mais ganha", "Desistir"], "Ouvir e decidir juntos.", "🗳️"),
            separar("Isso ajuda ou atrapalha a equipe?", ["Ajuda", "Atrapalha"],
                    [("ouvir o colega", 0), ("dividir o material", 0), ("dar a vez", 0), ("pegar tudo para si", 1), ("não deixar ninguém falar", 1)],
                    "Cooperar é pensar no grupo."),
            ordem("Como a equipe monta o quebra-cabeça?", ["Combinar quem faz o quê", "Separar as peças da borda", "Montar a borda juntos", "Completar o meio juntos"], "Planejar, dividir e fazer juntos."),
            tf("Numa equipe, todas as pessoas são importantes.", True, "Cada um contribui de um jeito."),
        ],
    ),
    "a3-b4-etica-u1-m3": missao(
        [
            ("🧸", "Tem brinquedo que você **não usa mais**? Ele pode alegrar outra criança!"),
            ("🔁", "**Trocar** e **doar** dá nova vida às coisas e diminui o lixo."),
            ("🙂", "O brinquedo deve estar **inteiro e limpo** para trocar ou doar."),
            desafio("escolha com um adulto um brinquedo que você não usa e combine uma troca com um amigo ou uma doação."),
        ],
        [
            mc("Qual brinquedo é bom para doar?", ["Um carrinho inteiro e limpo", "Um boneco quebrado e sujo", "Um jogo sem peças"], "Doe o que você gostaria de receber.", "🚗"),
            mc("Por que trocar brinquedos é bom?", ["Brincamos com coisas novas sem comprar", "Para ficar com tudo", "Para jogar no lixo"], "Trocar economiza e diverte!", "🔁"),
            mc("Para combinar uma troca, o que fazer primeiro?", ["Conversar e ver se os dois concordam", "Pegar sem pedir", "Esconder o brinquedo"], "Troca boa é quando **os dois** concordam.", "🗣️"),
            tf("Doar brinquedos que não uso pode alegrar outra criança.", True, "Compartilhar faz bem!"),
            fill("Dar algo para alguém sem pedir nada em troca é ___.", ["doar", "vender", "emprestar"], "**Doar** é dar de presente."),
        ],
    ),
    # ------------------------------------------------------------ Inglês
    "a3-b4-ingles-u1-m1": missao(
        [
            ("😊", "**How do you feel?** = Como você se sente?"),
            ("😀", "**happy** = feliz · **sad** = triste · **angry** = bravo"),
            ("😴", "**tired** = cansado · **scared** = com medo · **hungry** = com fome"),
        ],
        [
            ligar([("happy", "😀"), ("sad", "😢"), ("angry", "😠"), ("tired", "😴")], "Ligue a emoção à carinha"),
            ligar([("scared", "😱"), ("hungry", "🤤"), ("surprised", "😮"), ("sick", "🤒")], "Ligue a emoção à carinha"),
            mc("Como se diz **feliz** em inglês?", ["happy", "sad", "tired"], "Feliz = **happy**.", "😀"),
            mc("**I am sad.** Como a pessoa está?", ["Triste", "Feliz", "Brava"], "Sad = **triste**.", "😢"),
            mc("Depois de correr muito, você fica...", ["tired", "happy", "hungry"], "Cansado = **tired**.", "🏃"),
            fill("I am ___. I want to eat! 🍕", ["hungry", "sad", "angry"], "Com fome = **hungry**."),
            tf("**angry** quer dizer bravo.", True, "Angry = bravo, zangado."),
        ],
    ),
    "a3-b4-ingles-u1-m2": missao(
        [
            ("🏃", "Vamos aprender **ações** em inglês!"),
            ("🦘", "**run** = correr · **jump** = pular · **swim** = nadar"),
            ("💃", "**dance** = dançar · **sing** = cantar · **fly** = voar"),
        ],
        [
            ligar([("run", "🏃"), ("jump", "🦘"), ("swim", "🏊"), ("dance", "💃")], "Ligue a ação ao desenho"),
            mc("O peixe sabe **swim**. O que ele faz?", ["Nada", "Voa", "Pula corda"], "Swim = **nadar**.", "🐟"),
            mc("O pássaro sabe **fly**. O que ele faz?", ["Voa", "Nada", "Canta ópera"], "Fly = **voar**.", "🐦"),
            mc("Como se diz **cantar** em inglês?", ["sing", "swim", "sleep"], "Cantar = **sing**.", "🎤"),
            mc("**Jump!** O que você deve fazer?", ["Pular", "Correr", "Sentar"], "Jump = **pular**.", "🦘"),
            separar("Separe as palavras", ["Ação (verbo)", "Emoção"],
                    [("run", 0), ("swim", 0), ("dance", 0), ("happy", 1), ("sad", 1), ("tired", 1)],
                    "Verbos são ações. Happy, sad e tired são emoções."),
        ],
    ),
    "a3-b4-ingles-u1-m3": missao(
        [
            ("💪", "**I can** = eu consigo / eu sei."),
            ("🦘", "**I can jump!** = Eu sei pular! · **I can swim!** = Eu sei nadar!"),
            ("🙅", "**I can't** = eu não consigo. **I can't fly!** = Eu não sei voar!"),
            desafio("fale 3 frases com **I can** sobre você (por exemplo, I can run!) e peça para um adulto gravar."),
        ],
        [
            mc("O que quer dizer **I can dance**?", ["Eu sei dançar", "Eu não sei dançar", "Eu quero comer"], "I can = eu sei / consigo.", "💃"),
            mc("Uma pessoa não sabe voar. Ela diz...", ["I can't fly.", "I can fly.", "I am fly."], "**can't** = não consigo.", "🛫"),
            mc("Como dizer **Eu sei nadar**?", ["I can swim.", "I can sing.", "I can't swim."], "Nadar = **swim**.", "🏊"),
            fill("A fish ___ swim. 🐟", ["can", "can't", "is"], "O peixe **sabe** nadar: **can**."),
            fill("A dog ___ fly. 🐶", ["can't", "can", "is"], "O cachorro **não** voa: **can't**."),
            tf("**I can run** quer dizer eu sei correr.", True, "Run = correr."),
        ],
    ),
}
