"""2º ano · 4º bimestre."""
from base import desafio, fill, ligar, mc, missao, ordem, separar, tf

MISSOES = {
    # ------------------------------------------------------------ Português
    "a2-b4-portugues-u1-m1": missao(
        [
            ("🔄", "**Contrários** (antônimos) são palavras de sentido **oposto**."),
            ("😀", "**feliz** é o contrário de **triste**. **alto** é o contrário de **baixo**."),
            ("✨", "Às vezes colocamos **in-** ou **im-** no começo: **feliz → infeliz**, **possível → impossível**."),
        ],
        [
            ligar([("alto", "baixo"), ("quente", "frio"), ("dia", "noite"), ("cheio", "vazio")],
                  "Ligue cada palavra ao seu contrário"),
            ligar([("feliz", "infeliz"), ("possível", "impossível"), ("certo", "errado"), ("abrir", "fechar")],
                  "Ligue cada palavra ao seu contrário"),
            mc("Qual é o contrário de **RÁPIDO**?", ["devagar", "veloz", "ligeiro"], "Rápido é o oposto de **devagar**.", "🐢"),
            mc("Qual é o contrário de **POSSÍVEL**?", ["impossível", "infeliz", "possivelmente"], "Colocamos **im-** na frente: **impossível**.", "🚫"),
            mc("Qual é o contrário de **LIMPO**?", ["sujo", "lavado", "novo"], "Limpo é o oposto de **sujo**.", "🧼"),
            fill("A girafa é alta e o rato é ___.", ["baixo", "comprido", "grande"], "Alto e **baixo** são contrários."),
            tf("**Grande** é o contrário de **enorme**.", False, "Grande e enorme têm sentido parecido. O contrário de grande é **pequeno**."),
            tf("**Paciente** é o contrário de **impaciente**.", True, "Colocamos **im-** na frente e o sentido fica oposto."),
            separar("Separe: é contrário de **feliz** ou de **alegre**... ou não?",
                    ["Contrário de feliz", "Parecido com feliz"],
                    [("triste", 0), ("infeliz", 0), ("contente", 1), ("alegre", 1)],
                    "Triste e infeliz são opostos. Contente e alegre têm sentido parecido."),
        ],
    ),
    "a2-b4-portugues-u1-m2": missao(
        [
            ("🐱", "**Diminutivo** mostra algo **pequeno**: gato → **gatinho**."),
            ("🐯", "**Aumentativo** mostra algo **grande**: gato → **gatão**."),
            ("🏠", "Outros exemplos: casa → **casinha** / **casarão**; boca → **boquinha** / **bocão**."),
        ],
        [
            mc("Qual é o **diminutivo** de **CASA**?", ["casinha", "casarão", "casal"], "Casa pequena é **casinha**.", "🏠"),
            mc("Qual é o **aumentativo** de **GATO**?", ["gatão", "gatinho", "gata"], "Gato grande é **gatão**.", "🐱"),
            mc("Qual é o **diminutivo** de **PÉ**?", ["pezinho", "pezão", "pedal"], "Pé pequeno é **pezinho**.", "🦶"),
            mc("Qual é o **aumentativo** de **CARRO**?", ["carrão", "carrinho", "carroça"], "Carro grande é **carrão**.", "🚗"),
            separar("Separe as palavras", ["Diminutivo (pequeno)", "Aumentativo (grande)"],
                    [("livrinho", 0), ("florzinha", 0), ("copinho", 0), ("livrão", 1), ("narigão", 1), ("bocão", 1)],
                    "**-inho / -zinho** deixam pequeno. **-ão** deixa grande."),
            ligar([("cachorro", "cachorrinho"), ("bola", "bolinha"), ("mão", "mãozinha"), ("flor", "florzinha")],
                  "Ligue a palavra ao seu diminutivo"),
            fill("O passarinho é um ___ pequeno.", ["pássaro", "pato", "papel"], "Passarinho é o diminutivo de **pássaro**."),
            tf("**Bocão** é o aumentativo de **boca**.", True, "Boca grande é **bocão**."),
        ],
    ),
    "a2-b4-portugues-u1-m3": missao(
        [
            ("📖", "Toda história tem um **problema** (algo que dá errado) e uma **solução** (como resolvem)."),
            ("🐶", "Leia: **Bolinha, o cachorro de Lia, sumiu no parque. Lia chamou, chamou... Então ouviu um latido atrás da árvore. Era Bolinha, brincando com uma bola!**"),
            ("🔍", "Qual era o problema? O cachorro **sumiu**. E a solução? Lia **ouviu o latido e achou o Bolinha**."),
        ],
        [
            mc("Na história de Lia, qual era o **problema**?", ["O cachorro sumiu", "Começou a chover", "Lia perdeu a bola"], "Bolinha sumiu no parque.", "🐶"),
            mc("Qual foi a **solução**?", ["Lia ouviu o latido e achou o Bolinha", "Lia foi para casa", "Lia comprou outro cachorro"], "Ela seguiu o latido e encontrou o cachorro.", "🌳"),
            mc("Onde estava o Bolinha?", ["Atrás da árvore", "Dentro de casa", "Na escola"], "O latido vinha de **trás da árvore**.", "🌳"),
            ordem("Coloque a história na ordem", ["Bolinha sumiu no parque.", "Lia chamou o cachorro.", "Lia ouviu um latido.", "Lia achou o Bolinha."],
                  "Começo (problema), meio (procura) e fim (solução)."),
            mc("Leia: **Tom queria pegar a pipa presa no telhado. Pediu ajuda ao vovô, que usou uma escada.** Qual era o problema?",
               ["A pipa ficou presa no telhado", "O vovô caiu", "A escada quebrou"], "A pipa estava **presa no telhado**.", "🪁"),
            mc("E como Tom resolveu o problema da pipa?", ["Pediu ajuda ao vovô, que usou uma escada", "Comprou uma pipa nova", "Desistiu da pipa"], "O vovô pegou a pipa com a **escada**.", "🪜"),
            tf("Toda história tem só começo, sem fim.", False, "As histórias têm **começo, meio e fim**."),
            fill("A parte em que tudo se resolve é a ___.", ["solução", "pergunta", "capa"], "No fim aparece a **solução** do problema."),
        ],
    ),
    # ------------------------------------------------------------ Matemática
    "a2-b4-matematica-u1-m1": missao(
        [
            ("📏", "A **régua** mede o comprimento em **centímetros** (cm)."),
            ("0️⃣", "Para medir, colocamos o **zero** da régua na ponta do objeto."),
            ("✏️", "Se o lápis vai do 0 até o 12, ele mede **12 cm**."),
        ],
        [
            mc("Um lápis começa no **0** e termina no **10** da régua. Quanto ele mede?", ["10 cm", "0 cm", "100 cm"], "Do 0 ao 10: **10 centímetros**.", "✏️"),
            mc("Onde colocamos a ponta do objeto para medir?", ["No zero da régua", "No meio da régua", "No fim da régua"], "Sempre começamos no **zero**.", "📏"),
            mc("Uma borracha vai do **0** ao **4**. Quanto mede?", ["4 cm", "5 cm", "3 cm"], "Do 0 ao 4: **4 cm**.", "🧽"),
            mc("Qual objeto é mais **comprido**?", ["Um lápis de 15 cm", "Uma borracha de 4 cm", "Um clipe de 3 cm"], "15 cm é maior que 4 cm e 3 cm.", "📐"),
            ordem("Do mais curto ao mais comprido", ["📎 clipe: 3 cm", "🧽 borracha: 5 cm", "✏️ lápis: 14 cm", "📏 régua: 30 cm"], "3 < 5 < 14 < 30."),
            mc("Um giz mede **8 cm** e outro mede **5 cm**. Quanto um é maior que o outro?", ["3 cm", "13 cm", "2 cm"], "8 − 5 = **3 cm**.", "🖍️"),
            tf("Para medir a sala de aula, a régua é o melhor instrumento.", False, "Para coisas grandes usamos a **fita métrica** ou a **trena**."),
            fill("Para medir um caderno usamos a ___.", ["régua", "balança", "xícara"], "A **régua** mede comprimentos pequenos."),
        ],
    ),
    "a2-b4-matematica-u1-m2": missao(
        [
            ("🗓️", "Um **mês** tem cerca de **30 dias**. Uma **semana** tem **7 dias**."),
            ("👉", "Para saber quantos dias faltam, contamos do dia de hoje até a data."),
            ("🎉", "Hoje é dia **5**. A festa é dia **9**. Contamos: 6, 7, 8, 9. Faltam **4 dias**!"),
        ],
        [
            mc("Hoje é dia **3**. O passeio é dia **7**. Quantos dias faltam?", ["4", "3", "10"], "7 − 3 = **4 dias**.", "🚌"),
            mc("Hoje é dia **10**. O aniversário é dia **15**. Quantos dias faltam?", ["5", "6", "25"], "15 − 10 = **5 dias**.", "🎂"),
            mc("Quantos dias tem uma **semana**?", ["7", "5", "30"], "Domingo a sábado: **7 dias**.", "📅"),
            mc("Hoje é **segunda-feira**. Que dia será daqui a **2 dias**?", ["quarta-feira", "terça-feira", "sexta-feira"], "Segunda → terça → **quarta**.", "📆"),
            ordem("Coloque os dias da semana na ordem", ["domingo", "segunda-feira", "terça-feira", "quarta-feira", "quinta-feira"], "A semana começa no domingo."),
            mc("Faltam **7 dias** para as férias. Quanto tempo é isso?", ["Uma semana", "Um mês", "Um ano"], "7 dias = **1 semana**.", "🏖️"),
            tf("Um ano tem 12 meses.", True, "De janeiro a dezembro: **12 meses**."),
            fill("Depois de dezembro vem ___.", ["janeiro", "novembro", "fevereiro"], "Dezembro é o último mês. Depois começa outro ano em **janeiro**."),
        ],
    ),
    "a2-b4-matematica-u1-m3": missao(
        [
            ("✋", "Podemos medir com o **palmo**: a distância do dedão até o dedinho com a mão aberta."),
            ("🤔", "O palmo do adulto é **maior** que o da criança. Por isso a medida muda!"),
            ("📏", "A **fita métrica** dá a mesma medida para todo mundo."),
            desafio("meça a mesa com o seu palmo e com o palmo de um adulto. Depois meça com uma fita métrica e compare."),
        ],
        [
            mc("Por que a mesa deu **mais palmos** para a criança?", ["O palmo da criança é menor", "A mesa cresceu", "A criança errou a conta"], "Com um palmo menor, precisamos de **mais palmos**.", "✋"),
            mc("Qual instrumento dá a **mesma medida** para todo mundo?", ["Fita métrica", "Palmo", "Pé"], "A fita métrica usa centímetros, que são iguais para todos.", "📏"),
            mc("A mesa mediu **6 palmos do papai** e **9 palmos da Bia**. Quem tem o palmo maior?", ["O papai", "A Bia", "Os dois iguais"], "Quem precisou de menos palmos tem o palmo **maior**.", "👨"),
            tf("O palmo de todas as pessoas tem o mesmo tamanho.", False, "Cada pessoa tem um palmo de tamanho diferente."),
            separar("Separe as formas de medir", ["Medida do corpo", "Instrumento de medida"],
                    [("palmo", 0), ("passo", 0), ("pé", 0), ("régua", 1), ("fita métrica", 1), ("trena", 1)],
                    "Palmo, passo e pé usam o corpo. Régua, fita e trena são instrumentos."),
            fill("Para medir o comprimento da sala, é bom usar a ___.", ["trena", "colher", "balança"], "A **trena** mede distâncias grandes."),
        ],
    ),
    "a2-b4-matematica-u2-m1": missao(
        [
            ("🎲", "Algumas coisas são **certas** de acontecer, outras são **impossíveis**."),
            ("🤞", "Entre elas, há o que é **provável** (pode acontecer muito) e **pouco provável** (quase nunca)."),
            ("☀️", "O sol nascer amanhã é **certo**. Um cachorro falar é **impossível**."),
        ],
        [
            separar("Separe as situações", ["Certo", "Impossível"],
                    [("O sol nascer amanhã", 0), ("Depois da segunda vem a terça", 0), ("Um peixe andar de bicicleta", 1), ("Uma vaca voar sozinha", 1)],
                    "O que sempre acontece é certo. O que nunca acontece é impossível."),
            mc("Num saco com **9 bolas azuis** e **1 vermelha**, qual cor é **mais provável** sair?", ["Azul", "Vermelha", "Verde"], "Há muito mais bolas azuis.", "🔵"),
            mc("Num saco só com **bolas amarelas**, tirar uma bola **verde** é...", ["Impossível", "Certo", "Muito provável"], "Não há bola verde no saco!", "🟡"),
            mc("Chover num dia de céu muito nublado é...", ["Provável", "Impossível", "Certo"], "Com nuvens escuras, a chuva é **provável**.", "🌧️"),
            mc("Ganhar um elefante de presente amanhã é...", ["Pouco provável", "Certo", "Muito provável"], "Quase nunca acontece!", "🐘"),
            tf("Jogando um dado comum, é impossível sair o número 7.", True, "O dado só tem números de **1 a 6**."),
            tf("Jogando uma moeda, é certo sair cara.", False, "Pode sair **cara ou coroa**."),
            fill("Um gato virar pássaro é ___.", ["impossível", "certo", "provável"], "Isso **nunca** acontece."),
        ],
    ),
    "a2-b4-matematica-u2-m2": missao(
        [
            ("📊", "O **gráfico de barras** mostra quantidades com barras."),
            ("📏", "Quanto **mais alta** a barra, **maior** a quantidade."),
            ("🍎", "Na turma: **Maçã = 6**, **Banana = 4**, **Uva = 8** crianças preferem cada fruta."),
        ],
        [
            mc("No gráfico das frutas, qual é a preferida? (Maçã 6, Banana 4, Uva 8)", ["Uva", "Maçã", "Banana"], "A barra da uva é a mais alta: **8**.", "🍇"),
            mc("Qual fruta teve **menos** votos? (Maçã 6, Banana 4, Uva 8)", ["Banana", "Uva", "Maçã"], "Banana teve só **4**.", "🍌"),
            mc("Quantas crianças preferem **maçã**?", ["6", "4", "8"], "A barra da maçã chega no **6**.", "🍎"),
            mc("Quantas crianças a mais preferem uva do que maçã?", ["2", "14", "4"], "8 − 6 = **2**.", "📊"),
            mc("Quantas crianças votaram ao todo? (6 + 4 + 8)", ["18", "16", "14"], "6 + 4 + 8 = **18**.", "🧮"),
            ordem("Da fruta com menos votos para a com mais", ["🍌 Banana: 4", "🍎 Maçã: 6", "🍇 Uva: 8"], "4 < 6 < 8."),
            tf("A barra mais baixa mostra a maior quantidade.", False, "A barra mais **alta** mostra a maior quantidade."),
        ],
    ),
    "a2-b4-matematica-u2-m3": missao(
        [
            ("🗣️", "Uma **pesquisa** é perguntar a várias pessoas e anotar as respostas."),
            ("✍️", "Anotamos com **risquinhos**: | | | = 3 votos."),
            ("📊", "Depois desenhamos uma barra para cada resposta."),
            desafio("pergunte a 5 pessoas qual é o animal preferido delas, anote com risquinhos e desenhe o gráfico num papel."),
        ],
        [
            mc("Na pesquisa, o **cachorro** teve | | | |. Quantos votos?", ["4", "3", "5"], "Cada risquinho é um voto: **4**.", "🐶"),
            mc("Perguntamos a **5 pessoas**. Cachorro teve **3** votos e gato o resto. Quantos votos teve o gato?", ["2", "3", "8"], "5 − 3 = **2**.", "🐱"),
            mc("O que fazemos **primeiro** numa pesquisa?", ["Fazemos a pergunta", "Desenhamos o gráfico", "Contamos as barras"], "Primeiro perguntamos, depois anotamos e por fim fazemos o gráfico.", "❓"),
            ordem("Coloque as etapas da pesquisa na ordem", ["Escolher a pergunta", "Perguntar às pessoas", "Anotar os votos", "Fazer o gráfico"], "Pergunta, coleta, anotação e gráfico."),
            mc("Resultado: Peixe 1, Gato 2, Cachorro 2. O que aconteceu?", ["Gato e cachorro empataram", "Peixe ganhou", "Ninguém votou"], "Gato e cachorro tiveram **2** votos cada.", "🤝"),
            tf("Num gráfico de pesquisa, cada animal tem a sua barra.", True, "Uma barra para cada resposta."),
        ],
    ),
    # ------------------------------------------------------------ Ciências
    "a2-b4-ciencias-u1-m1": missao(
        [
            ("☀️", "A **sombra** aparece quando algo bloqueia a luz do Sol."),
            ("🌅", "De **manhã** e no **fim da tarde**, o Sol está baixo: a sombra fica **comprida**."),
            ("🕛", "Perto do **meio-dia**, o Sol está alto: a sombra fica **curtinha**."),
        ],
        [
            mc("Quando a sombra fica **mais curta**?", ["Perto do meio-dia", "De manhã cedo", "No fim da tarde"], "Ao meio-dia o Sol está bem alto.", "🕛"),
            mc("Quando a sombra fica **comprida**?", ["De manhã cedo", "Ao meio-dia", "Nunca"], "Com o Sol baixo, a sombra se estica.", "🌅"),
            mc("O que é preciso para ter sombra?", ["Luz e um objeto na frente", "Só água", "Só vento"], "A luz bate no objeto e forma a sombra atrás dele.", "🔦"),
            ordem("Como a sombra muda de manhã até o meio-dia?", ["7h: sombra bem comprida", "9h: sombra média", "12h: sombra bem curta"], "O Sol sobe e a sombra encolhe."),
            tf("À noite, sem luz nenhuma, não vemos a nossa sombra.", True, "Sem luz não se forma sombra."),
            tf("A sombra fica sempre do mesmo tamanho o dia todo.", False, "Ela muda conforme a posição do Sol."),
            fill("A sombra se forma do lado ___ da luz.", ["oposto", "igual", "de cima"], "A sombra fica do lado **oposto** à luz."),
        ],
    ),
    "a2-b4-ciencias-u1-m2": missao(
        [
            ("📸", "Vamos ser **caça-sombras**!"),
            ("🌅", "De manhã, fique de costas para o Sol e veja sua sombra **comprida**."),
            ("🕛", "Ao meio-dia, olhe de novo: ela estará **curtinha**, quase embaixo dos pés."),
            desafio("peça para um adulto tirar uma foto da sua sombra de manhã e outra ao meio-dia. Compare as duas!"),
        ],
        [
            mc("Na foto das **8 horas**, como estava a sombra?", ["Comprida", "Curtinha", "Não tinha sombra"], "De manhã o Sol está baixo.", "🌅"),
            mc("Na foto do **meio-dia**, como estava a sombra?", ["Curtinha", "Comprida", "Azul"], "Ao meio-dia o Sol está alto.", "🕛"),
            mc("De costas para o Sol, onde fica a sua sombra?", ["Na sua frente", "Atrás de você", "Em cima de você"], "A sombra fica do lado oposto ao Sol.", "🧍"),
            tf("Ficar muito tempo no sol forte do meio-dia sem proteção faz mal.", True, "Use protetor solar, boné e beba água!", ),
            separar("O que nos protege do sol forte?", ["Protege", "Não protege"],
                    [("boné", 0), ("protetor solar", 0), ("sombra de árvore", 0), ("ficar no sol o dia todo", 1), ("esquecer a água", 1)],
                    "Boné, protetor e sombra protegem. Água também é importante!"),
        ],
    ),
    "a2-b4-ciencias-u1-m3": missao(
        [
            ("🌡️", "Alguns materiais **esquentam mais** no Sol do que outros."),
            ("🏖️", "Na praia, a **areia** esquenta muito mais rápido que a **água** do mar."),
            ("👕", "Roupa **escura** esquenta mais que roupa **clara**."),
        ],
        [
            mc("Ao meio-dia na praia, o que está **mais quente**?", ["A areia", "A água do mar", "As duas iguais"], "A areia esquenta mais rápido.", "🏖️"),
            mc("Qual camiseta esquenta mais no Sol?", ["A preta", "A branca", "As duas iguais"], "Cores escuras absorvem mais calor.", "👕"),
            mc("Num dia de muito calor, qual roupa é melhor?", ["Roupa clara e leve", "Casaco preto", "Blusa de lã"], "Roupa clara esquenta menos.", "☀️"),
            separar("Separe", ["Esquenta mais no Sol", "Esquenta menos no Sol"],
                    [("areia", 0), ("asfalto", 0), ("carro escuro", 0), ("água", 1), ("roupa branca", 1), ("sombra da árvore", 1)],
                    "Materiais escuros e a areia esquentam mais."),
            tf("Andar descalço no asfalto ao meio-dia pode queimar os pés.", True, "O asfalto escuro fica muito quente."),
            tf("Roupa branca esquenta mais que roupa preta.", False, "É o contrário: a preta esquenta mais."),
            fill("A cor que mais esquenta no sol é a ___.", ["preta", "branca", "amarela clara"], "Cores escuras absorvem mais luz e calor."),
        ],
    ),
    # ------------------------------------------------------------ Ciências Humanas (História)
    "a2-b4-humanas-u1-m1": missao(
        [
            ("👩‍🔧", "Na comunidade, cada pessoa faz um **trabalho** importante."),
            ("🍞", "O **padeiro** faz o pão. O **médico** cuida da saúde. A **professora** ensina."),
            ("🤝", "Uns precisam dos outros: todo trabalho ajuda alguém."),
        ],
        [
            ligar([("padeiro", "pão"), ("costureira", "roupa"), ("agricultor", "alimentos"), ("carteiro", "cartas")],
                  "Ligue o trabalhador ao que ele faz"),
            ligar([("médica", "cuida da saúde"), ("professor", "ensina"), ("bombeiro", "apaga incêndios"), ("gari", "limpa as ruas")],
                  "Ligue o trabalhador ao serviço"),
            mc("Quem conserta a torneira que está pingando?", ["Encanador", "Padeiro", "Pintor"], "O **encanador** cuida dos canos e torneiras.", "🔧"),
            mc("Quem dirige o ônibus da cidade?", ["Motorista", "Dentista", "Cozinheiro"], "O **motorista** leva as pessoas.", "🚌"),
            mc("Quem cuida dos dentes?", ["Dentista", "Veterinário", "Carteiro"], "O **dentista** cuida dos dentes.", "🦷"),
            tf("O veterinário cuida dos animais.", True, "Ele é o médico dos bichos."),
            fill("O ___ planta e colhe os alimentos.", ["agricultor", "piloto", "bombeiro"], "O **agricultor** trabalha no campo."),
        ],
    ),
    "a2-b4-humanas-u1-m2": missao(
        [
            ("🌳", "Muitos trabalhos usam coisas da **natureza**: madeira, água, terra, peixes."),
            ("⚠️", "Se usamos demais, a natureza **sofre**: rios sujos, florestas derrubadas."),
            ("♻️", "Dá para trabalhar **cuidando** da natureza: replantar árvores, não poluir."),
        ],
        [
            mc("Uma fábrica jogou sujeira no rio. O que acontece?", ["Os peixes ficam doentes", "O rio fica mais limpo", "Nada muda"], "A poluição faz mal aos animais e às pessoas.", "🏭"),
            mc("Qual atitude ajuda a natureza?", ["Replantar as árvores cortadas", "Cortar tudo e não plantar", "Jogar lixo no rio"], "Plantar de novo ajuda a floresta a voltar.", "🌱"),
            mc("O pescador que pesca demais pode...", ["acabar com os peixes do rio", "aumentar os peixes", "deixar o rio mais fundo"], "Pescar demais não dá tempo dos peixes nascerem.", "🎣"),
            separar("Esse trabalho cuida ou prejudica a natureza?", ["Cuida", "Prejudica"],
                    [("catador de recicláveis", 0), ("plantar mudas", 0), ("queimar a mata", 1), ("jogar esgoto no rio", 1)],
                    "Reciclar e plantar ajudam. Queimar e poluir prejudicam."),
            tf("O catador de materiais recicláveis ajuda o meio ambiente.", True, "Ele tira o lixo do caminho e faz o material ser usado de novo."),
            fill("Para fazer móveis, o marceneiro usa ___.", ["madeira", "leite", "areia da praia"], "A **madeira** vem das árvores."),
        ],
    ),
    "a2-b4-humanas-u1-m3": missao(
        [
            ("🎤", "Vamos fazer uma **entrevista**! É uma conversa com perguntas."),
            ("❓", "Boas perguntas: **Qual é o seu trabalho? O que você faz no dia? Do que mais gosta?**"),
            ("🙏", "Ouça com atenção e agradeça no final."),
            desafio("entreviste um adulto sobre o trabalho dele e peça para gravar a conversa no celular."),
        ],
        [
            mc("Qual é uma boa pergunta para a entrevista?", ["O que você faz no seu trabalho?", "Qual é a cor do céu?", "Quantos anos tem o gato?"], "A pergunta deve ser sobre o **trabalho** da pessoa.", "🎤"),
            mc("O que fazemos enquanto a pessoa responde?", ["Ouvimos com atenção", "Falamos junto", "Saímos correndo"], "Ouvir é a parte mais importante.", "👂"),
            ordem("Coloque a entrevista na ordem", ["Cumprimentar a pessoa", "Fazer as perguntas", "Ouvir as respostas", "Agradecer"], "Começa com bom-dia e termina com obrigado."),
            tf("No fim da entrevista, agradecemos à pessoa.", True, "Agradecer é educado!"),
            fill("Numa entrevista, quem faz as perguntas é o ___.", ["entrevistador", "padeiro", "cachorro"], "O **entrevistador** pergunta e o entrevistado responde."),
        ],
    ),
    # ------------------------------------------------------------ Ciências Humanas (Geografia)
    "a2-b4-humanas-u2-m1": missao(
        [
            ("🌿", "Muitas coisas de casa vêm da **natureza**."),
            ("🪵", "A **mesa** de madeira vem das **árvores**. O **leite** vem da **vaca**."),
            ("🧂", "O **sal** vem da água do **mar**. O **tijolo** vem do **barro**."),
        ],
        [
            ligar([("mesa de madeira", "árvore"), ("leite", "vaca"), ("sal", "mar"), ("tijolo", "barro")],
                  "Ligue o produto à origem"),
            ligar([("suco de laranja", "laranjeira"), ("lã", "ovelha"), ("mel", "abelha"), ("papel", "árvore")],
                  "Ligue o produto à origem"),
            mc("De onde vem o **ovo**?", ["Da galinha", "Da árvore", "Do mar"], "A **galinha** bota os ovos.", "🥚"),
            mc("De onde vem a **farinha de trigo**?", ["Da plantação de trigo", "Da vaca", "Da pedra"], "O **trigo** é uma planta.", "🌾"),
            separar("Vem de planta ou de animal?", ["Planta", "Animal"],
                    [("algodão", 0), ("arroz", 0), ("madeira", 0), ("leite", 1), ("mel", 1), ("ovo", 1)],
                    "Algodão, arroz e madeira vêm de plantas. Leite, mel e ovo vêm de animais."),
            tf("O papel é feito de árvores.", True, "Por isso é bom **reciclar** papel."),
        ],
    ),
    "a2-b4-humanas-u2-m2": missao(
        [
            ("💧", "A **água** é usada em todo lugar!"),
            ("🚜", "No **campo**: para regar plantações e dar de beber aos animais."),
            ("🏙️", "Na **cidade**: para beber, tomar banho, cozinhar e nas fábricas."),
        ],
        [
            separar("Uso da água: campo ou cidade?", ["Campo", "Cidade"],
                    [("regar a plantação", 0), ("dar água ao gado", 0), ("lavar a calçada do prédio", 1), ("encher a piscina do clube", 1)],
                    "No campo a água ajuda a plantar e criar animais."),
            mc("Para que o agricultor usa a água?", ["Para regar a plantação", "Para pintar a casa", "Para fazer fogo"], "Sem água as plantas não crescem.", "🌽"),
            mc("Qual uso da água é igual no campo e na cidade?", ["Beber e tomar banho", "Regar o milharal", "Lavar o trator"], "Todo mundo precisa **beber** e se **lavar**.", "🚿"),
            mc("Qual atitude **economiza** água?", ["Fechar a torneira ao escovar os dentes", "Tomar banho de uma hora", "Lavar a calçada com mangueira"], "Torneira fechada = água economizada.", "🪥"),
            tf("Podemos gastar água à vontade porque ela nunca acaba.", False, "A água limpa é preciosa e precisa ser cuidada."),
            fill("A água que bebemos precisa estar ___.", ["limpa", "suja", "salgada"], "Água **limpa** e tratada faz bem à saúde."),
        ],
    ),
    "a2-b4-humanas-u2-m3": missao(
        [
            ("🌎", "Podemos cuidar da natureza com **atitudes simples**."),
            ("🗑️", "Jogar lixo no **lixo**, **separar** o reciclável e **economizar** água e luz."),
            ("🌳", "Plantar árvores e não maltratar os animais também ajuda!"),
        ],
        [
            separar("Essa atitude ajuda ou prejudica?", ["Ajuda a natureza", "Prejudica a natureza"],
                    [("separar o lixo reciclável", 0), ("apagar a luz ao sair", 0), ("plantar uma árvore", 0), ("jogar lixo na rua", 1), ("deixar a torneira aberta", 1), ("queimar folhas", 1)],
                    "Pequenas atitudes fazem grande diferença."),
            mc("Você terminou o suco de caixinha. O que fazer?", ["Jogar no lixo reciclável", "Jogar no chão", "Jogar no rio"], "Caixinhas podem ser **recicladas**.", "🧃"),
            mc("Saí do quarto. O que faço com a luz?", ["Apago a luz", "Deixo acesa", "Acendo mais luzes"], "Economizar energia ajuda o planeta.", "💡"),
            mc("Qual é a cor da lixeira de **papel** na coleta seletiva?", ["Azul", "Vermelha", "Verde"], "Papel = **azul**. Plástico = vermelho. Vidro = verde. Metal = amarelo.", "🟦"),
            ligar([("papel", "azul"), ("plástico", "vermelho"), ("vidro", "verde"), ("metal", "amarelo")],
                  "Ligue o material à cor da lixeira"),
            tf("Reutilizar um pote de vidro ajuda a natureza.", True, "Usar de novo diminui o lixo."),
        ],
    ),
}

MISSOES.update({
    # ------------------------------------------------------------ Ética
    "a2-b4-etica-u1-m1": missao(
        [
            ("🐾", "Animais de estimação precisam de **cuidados todos os dias**."),
            ("🥣", "Eles precisam de **água** fresca, **comida**, **abrigo** (um cantinho protegido) e **carinho**."),
            ("🩺", "E também de **vacina** e visitas ao **veterinário**."),
        ],
        [
            separar("Do que o bichinho precisa?", ["Precisa", "Não precisa"],
                    [("água fresca", 0), ("comida", 0), ("abrigo", 0), ("carinho", 0), ("chocolate", 1), ("gritos", 1)],
                    "Chocolate faz mal a cães e gatos. Gritar assusta os animais."),
            mc("O pote de água do cachorro está vazio. O que fazer?", ["Colocar água fresca", "Esperar amanhã", "Dar refrigerante"], "Água fresca todos os dias!", "💧"),
            mc("Está chovendo forte. Onde o gato deve ficar?", ["Num lugar coberto e seco", "Na chuva", "No telhado"], "O animal precisa de **abrigo**.", "🏠"),
            mc("Quem cuida da saúde dos animais?", ["O veterinário", "O padeiro", "O carteiro"], "O **veterinário** é o médico dos bichos.", "🩺"),
            tf("Fazer carinho com cuidado faz bem ao animal.", True, "Os bichos gostam de carinho com delicadeza."),
            fill("Todo dia o bichinho precisa de água e ___.", ["comida", "brinquedo de pilha", "televisão"], "Água e **comida** todos os dias."),
        ],
    ),
    "a2-b4-etica-u1-m2": missao(
        [
            ("❤️", "Animais **sentem dor e medo**, igualzinho a nós."),
            ("🚫", "Bater, puxar o rabo, deixar sem comida ou abandonar são **maus-tratos**."),
            ("📣", "Se você vir um animal sendo maltratado, **conte para um adulto**."),
        ],
        [
            separar("Essa atitude cuida ou machuca?", ["Cuida", "Machuca"],
                    [("dar comida na hora certa", 0), ("levar ao veterinário", 0), ("brincar com cuidado", 0), ("puxar o rabo", 1), ("abandonar na rua", 1), ("jogar pedra", 1)],
                    "Animais merecem respeito e cuidado."),
            mc("Você viu alguém maltratando um cachorro. O que fazer?", ["Contar para um adulto", "Rir", "Ajudar a maltratar"], "Um adulto pode ajudar o animal.", "📣"),
            mc("A família vai viajar. O que fazer com o gato?", ["Deixar alguém cuidando dele", "Deixar sozinho sem comida", "Soltar na rua"], "Abandonar é maus-tratos.", "🐱"),
            tf("Animais sentem dor.", True, "Por isso nunca devemos machucá-los."),
            tf("Puxar o rabo do gato é uma brincadeira legal para ele.", False, "Dói e assusta o gato!"),
            fill("Abandonar um animal na rua é ___.", ["maus-tratos", "carinho", "cuidado"], "Abandonar é uma forma de **maus-tratos**."),
        ],
    ),
    "a2-b4-etica-u1-m3": missao(
        [
            ("🪴", "Plantas também são **seres vivos** e precisam de cuidado."),
            ("💧", "Elas precisam de **água**, **luz do sol** e **terra** boa."),
            ("⚠️", "Água demais também faz mal: regue só quando a terra estiver **seca**."),
            desafio("escolha uma planta da casa, regue quando a terra estiver seca e tire uma foto dela por uma semana."),
        ],
        [
            mc("Do que a planta precisa para viver?", ["Água, luz e terra", "Só escuridão", "Refrigerante"], "Água, luz do sol e terra boa.", "🌱"),
            mc("Quando devemos regar a planta?", ["Quando a terra estiver seca", "De hora em hora", "Nunca"], "Encoste o dedo na terra: se estiver seca, é hora de regar.", "👆"),
            mc("Onde a planta deve ficar?", ["Perto da luz", "Dentro do armário", "Na geladeira"], "A planta precisa de **luz** para se alimentar.", "☀️"),
            ordem("Como cuidar da planta?", ["Ver se a terra está seca", "Regar com o regador", "Deixar perto da luz", "Tirar foto para ver o crescimento"], "Observar, regar e acompanhar."),
            tf("Planta é um ser vivo.", True, "Ela nasce, cresce e precisa de cuidados."),
        ],
    ),
    # ------------------------------------------------------------ Inglês
    "a2-b4-ingles-u1-m1": missao(
        [
            ("🍓", "Vamos fazer uma **fruit salad** (salada de frutas) em inglês!"),
            ("🍎", "**apple** = maçã · **banana** = banana · **orange** = laranja"),
            ("🍇", "**grapes** = uvas · **strawberry** = morango · **watermelon** = melancia"),
        ],
        [
            ligar([("apple", "🍎"), ("banana", "🍌"), ("orange", "🍊"), ("grapes", "🍇")], "Ligue a fruta ao nome"),
            ligar([("strawberry", "🍓"), ("watermelon", "🍉"), ("pineapple", "🍍"), ("lemon", "🍋")], "Ligue a fruta ao nome"),
            mc("Como se diz **maçã** em inglês?", ["apple", "orange", "grapes"], "Maçã = **apple**.", "🍎"),
            mc("Qual fruta é **strawberry**?", ["🍓", "🍉", "🍌"], "Strawberry = morango.", None),
            mc("Qual fruta é **orange**?", ["🍊", "🍋", "🍎"], "Orange = laranja (e também a cor laranja!).", None),
            tf("**watermelon** quer dizer melancia.", True, "Water = água, melon = melão. Melancia tem muita água!"),
            fill("A uva em inglês é ___.", ["grapes", "apple", "lemon"], "Uvas = **grapes**."),
        ],
    ),
    "a2-b4-ingles-u1-m2": missao(
        [
            ("😋", "**I like** = eu gosto. **I don't like** = eu não gosto."),
            ("🍌", "**I like bananas!** = Eu gosto de bananas! 😀"),
            ("🥦", "**I don't like broccoli.** = Eu não gosto de brócolis. 😝"),
        ],
        [
            mc("**I like apples.** Que carinha combina?", ["😀 Gosto", "😝 Não gosto"], "**I like** = eu gosto.", "🍎"),
            mc("**I don't like onions.** Que carinha combina?", ["😝 Não gosto", "😀 Gosto"], "**I don't like** = eu não gosto.", "🧅"),
            mc("Como dizer **eu gosto de pizza**?", ["I like pizza.", "I don't like pizza.", "Pizza no."], "I like = eu gosto.", "🍕"),
            mc("O que quer dizer **yummy**?", ["Gostoso", "Nojento", "Gelado"], "Yummy = **gostoso**! Yucky = nojento.", "😋"),
            separar("Separe as frases", ["Gosto 😀", "Não gosto 😝"],
                    [("I like milk.", 0), ("I like grapes.", 0), ("I don't like carrots.", 1), ("I don't like fish.", 1)],
                    "**I like** = gosto. **I don't like** = não gosto."),
            tf("**I don't like** quer dizer eu gosto.", False, "**don't** deixa a frase negativa: eu **não** gosto."),
        ],
    ),
    "a2-b4-ingles-u1-m3": missao(
        [
            ("🌍", "Muitos países falam **inglês**. Cada um tem seu jeito de tomar **breakfast** (café da manhã)."),
            ("🇬🇧", "Na **Inglaterra**, um café famoso tem **ovos, feijão, salsicha e torrada**."),
            ("🇺🇸", "Nos **Estados Unidos**, muita gente come **pancakes** (panquecas) com xarope."),
        ],
        [
            mc("O que quer dizer **breakfast**?", ["Café da manhã", "Jantar", "Lanche da tarde"], "Breakfast = **café da manhã**.", "🍳"),
            mc("O que são **pancakes**?", ["Panquecas", "Sorvetes", "Saladas"], "Pancakes = panquecas.", "🥞"),
            ligar([("egg", "ovo"), ("milk", "leite"), ("bread", "pão"), ("juice", "suco")], "Ligue a comida ao nome em português"),
            mc("Em que país é comum comer **feijão no café da manhã**?", ["Inglaterra", "Japão", "Brasil"], "No café inglês tem feijão com molho!", "🇬🇧"),
            mc("Como dizer **leite** em inglês?", ["milk", "egg", "bread"], "Leite = **milk**.", "🥛"),
            tf("Todo mundo no mundo toma o mesmo café da manhã.", False, "Cada lugar tem seus costumes!"),
        ],
    ),
})
