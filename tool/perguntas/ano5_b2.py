"""5º ano · 2º bimestre."""
from base import desafio, fill, ligar, mc, missao, ordem, separar, tf

MISSOES = {
    # ------------------------------------------------------------ Português
    "a5-b2-portugues-u1-m1": missao(
        [
            ("🔀", "Uma mesma palavra pode ter **vários sentidos**. Isso se chama **polissemia**."),
            ("🥭", "**manga** é fruta, mas também é parte da camisa. **banco** é para sentar ou para guardar dinheiro."),
            ("🔎", "O **contexto** (as outras palavras da frase) mostra qual sentido vale."),
        ],
        [
            mc("**Arregacei a manga da camisa.** Aqui, manga é...", ["parte da roupa", "uma fruta", "um animal"], "O contexto é **camisa**.", "👕"),
            mc("**Fui ao banco pagar uma conta.** Banco é...", ["lugar que guarda dinheiro", "assento da praça", "banco de areia"], "Pagar conta → instituição.", "🏦"),
            mc("**A galinha perdeu uma pena.** Pena é...", ["parte que cobre as aves", "sentimento de dó", "castigo"], "Galinha tem **penas**.", "🪶"),
            mc("**Que pena que você não veio!** Pena é...", ["tristeza, lamento", "parte de ave", "caneta antiga"], "Expressa **lamento**.", "😢"),
            mc("**O jogador marcou um gol de cabeça.** Cabeça aqui é...", ["parte do corpo", "o chefe do grupo", "o começo da fila"], "Ele cabeceou a bola.", "⚽"),
            ligar([("Sentei no banco da praça.", "assento"), ("Guardei dinheiro no banco.", "instituição"), ("Comi uma manga doce.", "fruta"), ("Rasguei a manga da blusa.", "parte da roupa")], "Ligue a frase ao sentido"),
            tf("A palavra **cravo** pode ser uma flor ou um tempero.", True, "Mais um exemplo de polissemia."),
        ],
    ),
    "a5-b2-portugues-u1-m2": missao(
        [
            ("⏸️", "**Reticências (...)** mostram pausa, dúvida, suspense ou que a ideia continua."),
            ("💬", "**Aspas (\" \")** marcam a fala de alguém, uma citação ou uma palavra com sentido especial."),
            ("📎", "**Dois-pontos (:)** anunciam uma lista ou uma fala. **Ponto e vírgula (;)** separa partes longas. **Parênteses ( )** trazem uma explicação extra."),
        ],
        [
            mc("Em **Abri a porta e... nada!**, as reticências indicam...", ["suspense", "uma lista", "uma pergunta"], "A pausa cria **expectativa**.", "🚪"),
            mc("Em **Ela disse \"chego já\"**, as aspas marcam...", ["a fala de alguém", "um erro", "uma conta"], "As palavras são **dela**.", "💬"),
            mc("Em **Comprei três frutas: maçã, uva e pera.**, os dois-pontos...", ["anunciam uma lista", "terminam a frase", "indicam dúvida"], "Depois vem a **enumeração**.", "🍎"),
            mc("Em **Pelé (o Rei do Futebol) nasceu em Minas.**, os parênteses...", ["trazem uma explicação", "indicam pergunta", "marcam a fala"], "Informação **extra**.", "⚽"),
            fill("Mamãe avisou___ \"Hora do banho!\"", [":", "?", "..."], "Antes da fala, **dois-pontos**."),
            ligar([("...", "suspense ou dúvida"), ("\" \"", "citação"), (":", "anuncia lista"), ("( )", "explicação extra")], "Ligue o sinal à função"),
            tf("**Não sei... talvez eu vá.** As reticências mostram hesitação.", True, "A pessoa está em dúvida."),
        ],
    ),
    "a5-b2-portugues-u1-m3": missao(
        [
            ("🕵️", "Um bom leitor é um **detetive**: descobre o que o texto **não diz com todas as letras**. Isso é **inferência**."),
            ("📄", "Texto: **Lucas chegou ensopado, deixou o guarda-chuva quebrado na porta e pediu uma toalha.**"),
            ("💡", "O texto não fala de chuva, mas as **pistas** mostram que choveu e ventou forte."),
        ],
        [
            mc("No texto de Lucas, o que podemos **inferir**?", ["Estava chovendo forte", "Fazia sol", "Lucas estava na piscina de casa"], "Ensopado + guarda-chuva = **chuva**.", "🌧️"),
            mc("Por que o guarda-chuva estava quebrado?", ["Provavelmente ventou muito", "Lucas era muito alto", "Era de chocolate"], "Vento forte quebra guarda-chuvas.", "🌬️"),
            mc("**Ana olhou o relógio, pegou a mochila correndo e saiu sem tomar café.** Ana estava...", ["atrasada", "de férias", "dormindo"], "Pressa e relógio → **atraso**.", "⏰"),
            mc("**O cachorro abanava o rabo e pulava na porta quando ouviu o carro.** O cachorro estava...", ["feliz com a chegada do dono", "com medo do carro", "com sono"], "Abanar o rabo = alegria.", "🐕"),
            mc("**Bia fechou o livro, enxugou as lágrimas e suspirou.** O final do livro provavelmente era...", ["triste ou emocionante", "engraçado", "sem graça nenhuma"], "Lágrimas indicam **emoção**.", "📖"),
            tf("Inferir é descobrir algo usando pistas do texto.", True, "É ler **nas entrelinhas**."),
        ],
    ),
    # ------------------------------------------------------------ Matemática
    "a5-b2-matematica-u1-m1": missao(
        [
            ("👯", "**Frações equivalentes** representam a **mesma quantidade**: [[1/2]] = [[2/4]] = [[4/8]]."),
            ("✖️", "Para achar uma equivalente, **multiplique** (ou divida) o numerador e o denominador pelo **mesmo número**."),
            ("🍫", "**Fração imprópria** tem numerador maior que o denominador: [[5/4]] é mais que um inteiro."),
        ],
        [
            mc("Qual fração é equivalente a [[1/2]]?", ["[[3/6]]", "[[2/3]]", "[[1/4]]"], "1×3 / 2×3 = [[3/6]].", "👯"),
            mc("Qual fração é equivalente a [[2/3]]?", ["[[4/6]]", "[[2/6]]", "[[3/2]]"], "2×2 / 3×2 = [[4/6]].", "🔢"),
            mc("[[6/8]] simplificada fica...", ["[[3/4]]", "[[2/4]]", "[[6/4]]"], "Divida os dois por 2.", "✂️"),
            ligar([("[[1/2]]", "[[5/10]]"), ("[[1/3]]", "[[2/6]]"), ("[[1/4]]", "[[3/12]]"), ("[[3/5]]", "[[6/10]]")], "Ligue as frações gêmeas"),
            mc("Qual é uma fração **imprópria**?", ["[[7/4]]", "[[3/4]]", "[[1/4]]"], "7 > 4: passa de um inteiro.", "🍕"),
            fill("[[1/4]] = [[2/___]]", ["8", "6", "4"], "1×2 / 4×2 = [[2/8]]."),
            tf("[[4/4]] é igual a um inteiro.", True, "Todas as partes juntas."),
        ],
    ),
    "a5-b2-matematica-u1-m2": missao(
        [
            ("📏", "Na **reta numérica**, frações e decimais ficam entre os números inteiros."),
            ("🔟", "Entre 0 e 1, dividindo em 10 partes: 0,1 · 0,2 · 0,3 ... 0,9."),
            ("🎯", "[[1/2]] = **0,5** fica bem no **meio** entre 0 e 1. [[1/4]] = **0,25**, [[3/4]] = **0,75**."),
        ],
        [
            mc("Qual número fica **no meio** entre 0 e 1?", ["0,5", "0,1", "1,5"], "[[1/2]] = 0,5.", "🎯"),
            mc("[[1/4]] em decimal é...", ["0,25", "0,4", "1,4"], "1 ÷ 4 = 0,25.", "🔢"),
            mc("Qual número está **entre 1 e 2**?", ["1,7", "0,7", "2,7"], "1 < 1,7 < 2.", "📏"),
            ordem("Coloque na reta, do menor para o maior:", ["0,2", "[[1/2]]", "0,75", "1,25"], "0,2 < 0,5 < 0,75 < 1,25."),
            mc("[[3/10]] em decimal é...", ["0,3", "3,10", "0,03"], "Três décimos.", "🔟"),
            mc("Qual é **maior**: 0,8 ou [[3/4]]?", ["0,8", "[[3/4]]", "São iguais"], "[[3/4]] = 0,75 < 0,8.", "⚖️"),
            tf("**1,5** é o mesmo que um inteiro e meio.", True, "1 + 0,5."),
        ],
    ),
    "a5-b2-matematica-u1-m3": missao(
        [
            ("🏷️", "**Porcentagem (%)** é uma fração de 100: **10%** = [[10/100]] = [[1/10]]."),
            ("🧮", "**50%** = metade. **25%** = um quarto. **10%** = dividir por 10. **100%** = tudo."),
            ("🛍️", "**Desconto**: um tênis de R$ 100 com 20% de desconto sai por R$ 80."),
        ],
        [
            mc("**50%** de R$ 60 é...", ["R$ 30", "R$ 50", "R$ 6"], "Metade de 60.", "🛍️"),
            mc("**10%** de R$ 80 é...", ["R$ 8", "R$ 10", "R$ 70"], "80 ÷ 10 = 8.", "🔟"),
            mc("**25%** de R$ 40 é...", ["R$ 10", "R$ 25", "R$ 4"], "Um quarto de 40.", "🍰"),
            mc("Uma bola de **R$ 50** com **10%** de desconto sai por...", ["R$ 45", "R$ 40", "R$ 5"], "Desconto de 5 → 50 − 5 = **45**.", "⚽"),
            mc("Uma blusa de **R$ 40** está com **50% off**. Quanto vou pagar?", ["R$ 20", "R$ 30", "R$ 50"], "Metade de 40.", "👕"),
            ligar([("50%", "[[1/2]]"), ("25%", "[[1/4]]"), ("10%", "[[1/10]]"), ("100%", "o inteiro")], "Ligue a porcentagem à fração"),
            tf("**75%** é o mesmo que [[3/4]].", True, "75 de 100 = 3 de 4."),
        ],
    ),
    # ------------------------------------------------------------ Ciências
    "a5-b2-ciencias-u1-m1": missao(
        [
            ("💧", "Só uma pequena parte da água do planeta é **doce** e própria para beber. Ela é **preciosa**!"),
            ("🚿", "Banho longo, torneira pingando e lavar calçada com mangueira **desperdiçam** muita água."),
            ("🪣", "Fechar a torneira ao escovar os dentes, consertar vazamentos e reaproveitar água ajudam a **economizar**."),
        ],
        [
            mc("Qual atitude **economiza** água?", ["Fechar a torneira ao escovar os dentes", "Lavar a calçada com mangueira", "Banho de 30 minutos"], "A torneira aberta gasta litros!", "🪥"),
            mc("Uma torneira **pingando** o dia todo...", ["desperdiça muita água", "não gasta nada", "economiza energia"], "Gota a gota, litros por dia.", "🚰"),
            separar("Desperdício ou economia?", ["Desperdício", "Economia"],
                    [("mangueira na calçada", 0), ("vazamento sem conserto", 0), ("máquina de lavar meio vazia", 0), ("balde para lavar o carro", 1), ("banho curto", 1), ("reusar água da chuva", 1)],
                    "Pequenas atitudes fazem diferença."),
            mc("A maior parte da água da Terra está...", ["nos oceanos (salgada)", "nos rios", "nas garrafas"], "Só cerca de 3% é doce.", "🌊"),
            mc("A água usada para lavar roupa pode ser reaproveitada para...", ["lavar o quintal", "beber", "cozinhar"], "Reúso consciente!", "♻️"),
            tf("Água doce é um recurso que pode acabar se for mal usado.", True, "Por isso precisamos economizar."),
        ],
    ),
    "a5-b2-ciencias-u1-m2": missao(
        [
            ("➖", "**Reduzir**: consumir menos (levar sacola própria, evitar descartáveis)."),
            ("🔁", "**Reutilizar**: usar de novo de outro jeito (pote de vidro vira porta-lápis)."),
            ("♻️", "**Reciclar**: transformar o material em produto novo (garrafa PET vira tecido). Separe o lixo: azul papel, vermelho plástico, verde vidro, amarelo metal."),
        ],
        [
            separar("Reduzir, reutilizar ou reciclar?", ["Reduzir", "Reutilizar", "Reciclar"],
                    [("levar sacola de pano ao mercado", 0), ("apagar a luz ao sair", 0), ("pote de vidro vira vaso", 1), ("doar roupas que não servem", 1), ("latinha vira lata nova na fábrica", 2), ("papel velho vira papel novo", 2)],
                    "Os 3 Rs."),
            ligar([("papel", "azul"), ("plástico", "vermelho"), ("vidro", "verde"), ("metal", "amarelo")], "Ligue o material à cor da lixeira"),
            mc("Qual dos 3 Rs vem **primeiro** e é o mais importante?", ["Reduzir", "Reciclar", "Reutilizar"], "O melhor lixo é o que **não é produzido**.", "🥇"),
            mc("**Pilhas e baterias** devem ser descartadas...", ["em pontos de coleta especiais", "no lixo comum", "no rio"], "Têm substâncias tóxicas.", "🔋"),
            mc("Restos de comida podem virar adubo na...", ["composteira", "lixeira azul", "pia"], "**Compostagem**!", "🍂"),
            tf("Garrafas PET recicladas podem virar roupas.", True, "O plástico vira fibra de tecido."),
        ],
    ),
    "a5-b2-ciencias-u1-m3": missao(
        [
            ("🧾", "A **conta de água** mostra quantos **metros cúbicos (m³)** a casa gastou no mês. 1 m³ = **1.000 litros**."),
            ("📊", "Ela também mostra o consumo dos meses anteriores: dá para ver se a família gastou mais ou menos."),
            ("🎯", "Com metas simples, a família pode **economizar** água e dinheiro."),
            desafio("peça a um adulto a última conta de água. Encontrem quantos m³ foram gastos e combinem juntos uma meta para economizar no próximo mês."),
        ],
        [
            mc("**1 m³** de água tem quantos litros?", ["1.000", "100", "10"], "Uma caixa de 1 m de cada lado.", "🧊"),
            mc("Em janeiro a casa gastou **12 m³** e em fevereiro **10 m³**. O consumo...", ["diminuiu 2 m³", "aumentou 2 m³", "ficou igual"], "12 − 10 = **2**.", "📉"),
            mc("Se a família gasta **15 m³** e quer economizar **3 m³**, a meta é gastar...", ["12 m³", "18 m³", "3 m³"], "15 − 3 = **12**.", "🎯"),
            mc("Gastar menos água também ajuda a...", ["pagar uma conta menor", "chover mais", "esquentar o banho"], "Economia no bolso e no planeta.", "💰"),
            separar("Ajuda ou atrapalha a meta de economia?", ["Ajuda", "Atrapalha"],
                    [("consertar o vazamento", 0), ("juntar roupa para lavar de uma vez", 0), ("regar plantas de manhã cedo", 0), ("lavar louça com torneira aberta", 1), ("encher a piscina toda semana", 1), ("banho de meia hora", 1)],
                    "Toda a família pode ajudar."),
            tf("A conta de água mostra o consumo de meses anteriores.", True, "Assim dá para comparar."),
        ],
    ),
    # ------------------------------------------------------------ Ciências Humanas (História)
    "a5-b2-humanas-u1-m1": missao(
        [
            ("🏛️", "No Brasil, o poder é dividido em **três poderes**, que se equilibram."),
            ("📜", "**Legislativo** faz as **leis** (vereadores, deputados, senadores)."),
            ("🖋️", "**Executivo** governa e põe as leis em prática (prefeito, governador, presidente). **Judiciário** julga se as leis foram cumpridas (juízes)."),
        ],
        [
            ligar([("Legislativo", "faz as leis"), ("Executivo", "administra e governa"), ("Judiciário", "julga conflitos")], "Ligue o poder à função"),
            mc("O **prefeito** faz parte de qual poder?", ["Executivo", "Legislativo", "Judiciário"], "Ele administra a cidade.", "🏙️"),
            mc("Os **vereadores** fazem parte de qual poder?", ["Legislativo", "Executivo", "Judiciário"], "Fazem as leis da cidade.", "📜"),
            mc("Quem julga se alguém desobedeceu a uma lei?", ["um juiz", "o prefeito", "o vereador"], "O **Judiciário**.", "⚖️"),
            mc("Por que o poder é dividido em três?", ["Para ninguém mandar sozinho", "Para ter mais feriados", "Porque três é um número bonito"], "Um poder **fiscaliza** o outro.", "🤝"),
            tf("No Brasil, o povo escolhe o presidente pelo voto.", True, "É uma **democracia**."),
        ],
    ),
    "a5-b2-humanas-u1-m2": missao(
        [
            ("🧒", "O **ECA** (Estatuto da Criança e do Adolescente) é a lei que protege crianças e adolescentes."),
            ("📚", "Toda criança tem direito a **vida, saúde, educação, lazer, alimentação, família** e **proteção** contra violência."),
            ("🚫", "Criança **não deve trabalhar**: lugar de criança é na escola e brincando."),
        ],
        [
            mc("O **ECA** é uma lei que protege...", ["crianças e adolescentes", "apenas adultos", "só os animais"], "Estatuto da Criança e do Adolescente.", "🧒"),
            separar("É um direito da criança?", ["É direito", "Não é direito"],
                    [("estudar", 0), ("brincar", 0), ("ser cuidada pela família", 0), ("trabalhar numa fábrica", 1), ("sofrer castigo violento", 1), ("ficar sem vacina", 1)],
                    "O ECA protege as crianças."),
            mc("Se uma criança está sofrendo maus-tratos, podemos ligar para o...", ["Disque 100 ou Conselho Tutelar", "corpo de bombeiros apenas", "ninguém"], "Eles protegem os direitos da criança.", "📞"),
            mc("O direito à **educação** significa que toda criança deve...", ["estar na escola", "trabalhar cedo", "ficar em casa sempre"], "Escola é direito!", "🏫"),
            tf("Os direitos humanos valem para todas as pessoas, sem distinção.", True, "Cor, religião ou origem não importam."),
            mc("O **Conselho Tutelar** existe para...", ["proteger os direitos de crianças e adolescentes", "dar notas na escola", "construir estradas"], "Há um em cada cidade.", "🛡️"),
        ],
    ),
    "a5-b2-humanas-u1-m3": missao(
        [
            ("🙋", "**Cidadania** é ter **direitos** e cumprir **deveres** na sociedade."),
            ("🗳️", "Ser cidadão é votar (adultos), respeitar as leis, cuidar dos espaços públicos e ajudar a comunidade."),
            ("🌳", "Criança também pratica cidadania: não jogar lixo na rua, respeitar a fila, cuidar da escola."),
        ],
        [
            separar("Atitude cidadã ou não?", ["Cidadã", "Não cidadã"],
                    [("jogar lixo na lixeira", 0), ("respeitar a faixa de pedestres", 0), ("cuidar dos livros da biblioteca", 0), ("pichar a parede da escola", 1), ("furar a fila", 1), ("quebrar o brinquedo da praça", 1)],
                    "Direitos e deveres andam juntos."),
            mc("O **voto** é importante porque...", ["escolhemos quem vai governar", "ganhamos um prêmio", "acabam as leis"], "É assim na democracia.", "🗳️"),
            mc("A praça da cidade é um espaço **público**. Isso quer dizer que...", ["é de todos e todos devem cuidar", "não é de ninguém", "só o prefeito pode usar"], "O que é público é **nosso**.", "🌳"),
            mc("Um **dever** do cidadão é...", ["respeitar as leis", "fazer o que quiser", "não pagar nada"], "Deveres garantem a convivência.", "📜"),
            tf("Crianças também podem praticar a cidadania.", True, "Com pequenas atitudes todos os dias."),
            mc("Ver um buraco perigoso na rua e avisar a prefeitura é...", ["uma atitude cidadã", "falta de educação", "proibido"], "Cuidar da cidade é de todos.", "🚧"),
        ],
    ),
    # ------------------------------------------------------------ Ciências Humanas (Geografia)
    "a5-b2-humanas-u2-m1": missao(
        [
            ("🏙️", "As cidades têm **funções** principais, ligadas ao que mais se faz nelas."),
            ("⚓", "**Portuária**: tem porto para navios (Santos). **Turística**: recebe muitos visitantes (Gramado, Foz do Iguaçu)."),
            ("🏭", "**Industrial**: tem muitas fábricas. **Político-administrativa**: sede do governo (Brasília)."),
        ],
        [
            ligar([("cidade portuária", "navios e porto"), ("cidade turística", "muitos visitantes"), ("cidade industrial", "muitas fábricas"), ("capital federal", "sede do governo")], "Ligue o tipo de cidade à característica"),
            mc("**Brasília** é uma cidade com função...", ["político-administrativa", "portuária", "agrícola"], "Lá fica o governo federal.", "🏛️"),
            mc("**Santos (SP)** é famosa pelo seu...", ["porto", "deserto", "vulcão"], "Um dos maiores portos do Brasil.", "⚓"),
            mc("**Foz do Iguaçu** recebe muita gente por causa das...", ["cataratas", "fábricas", "minas"], "Uma cidade **turística**.", "🌊"),
            mc("Uma cidade com muitas fábricas de carros tem função...", ["industrial", "turística", "religiosa"], "Indústria!", "🚗"),
            tf("Uma cidade pode ter mais de uma função.", True, "O Rio é turístico, portuário e industrial."),
        ],
    ),
    "a5-b2-humanas-u2-m2": missao(
        [
            ("📈", "Muitas cidades brasileiras **cresceram rápido**, com pessoas vindas do campo."),
            ("🚦", "Sem planejamento surgem **problemas**: trânsito, poluição, enchentes, falta de moradia e de saneamento."),
            ("🌱", "Soluções: transporte público, áreas verdes, coleta de esgoto, moradia digna."),
        ],
        [
            mc("Um problema comum de cidades grandes é...", ["congestionamento", "falta de ruas", "excesso de florestas"], "Muitos carros e pouco transporte público.", "🚗"),
            mc("Por que acontecem **enchentes** nas cidades?", ["Chão asfaltado não absorve a chuva e há lixo nos bueiros", "Porque há muitas árvores", "Porque não chove"], "A água não tem para onde ir.", "🌧️"),
            separar("Problema ou solução urbana?", ["Problema", "Solução"],
                    [("poluição do ar", 0), ("esgoto a céu aberto", 0), ("falta de moradia", 0), ("metrô e ônibus", 1), ("parques e praças", 1), ("coleta seletiva", 1)],
                    "Planejar faz a cidade melhor."),
            mc("O **transporte público** ajuda porque...", ["leva muitas pessoas e tira carros da rua", "aumenta o trânsito", "polui mais"], "Um ônibus substitui muitos carros.", "🚌"),
            mc("**Saneamento básico** é...", ["água tratada, esgoto e coleta de lixo", "pintar as casas", "construir shoppings"], "Essencial para a saúde.", "🚰"),
            tf("Plantar árvores ajuda a deixar a cidade mais fresca.", True, "As árvores dão sombra e umidade."),
        ],
    ),
    "a5-b2-humanas-u2-m3": missao(
        [
            ("🕸️", "As cidades formam uma **rede**: estão ligadas por **estradas, ferrovias, rios, aviões** e **internet**."),
            ("🏙️", "Cidades **pequenas** dependem de cidades **maiores** para hospitais, universidades e grandes lojas."),
            ("🗺️", "Num **mapa de ligações**, as linhas mostram os caminhos entre as cidades."),
        ],
        [
            mc("Uma pessoa de uma cidade pequena vai à capital para...", ["consultar um médico especialista", "ver o pôr do sol de lá", "nada"], "Grandes cidades oferecem mais **serviços**.", "🏥"),
            mc("O que liga uma cidade à outra?", ["estradas, ferrovias e voos", "muros", "cercas"], "São as **vias de transporte**.", "🛣️"),
            mc("Num mapa, a cidade com **mais linhas** chegando é...", ["um centro importante da rede", "a menor cidade", "uma floresta"], "Muitas ligações = muita importância.", "🗺️"),
            mc("A **internet** também liga cidades porque...", ["leva informações e serviços rapidamente", "é uma estrada", "transporta caminhões"], "Uma rede de **comunicação**.", "🌐"),
            tf("As cidades vizinhas trocam produtos, serviços e trabalhadores.", True, "Por isso formam uma **rede urbana**."),
            mc("**Metrópole** é uma cidade...", ["muito grande e que influencia muitas outras", "bem pequena", "que só tem fazendas"], "Como São Paulo e Rio de Janeiro.", "🌆"),
        ],
    ),
    # ------------------------------------------------------------ Ética
    "a5-b2-etica-u1-m1": missao(
        [
            ("📰", "**Fake news** são notícias **falsas** feitas para enganar."),
            ("🚨", "Desconfie de manchetes **exageradas**, com muitos **!!!**, sem **autor**, sem **data** ou de site estranho."),
            ("✅", "Notícias confiáveis citam **fontes** e aparecem em vários veículos sérios."),
        ],
        [
            mc("Qual manchete parece **boato**?", ["URGENTE!!! Comer chocolate faz voar!!!", "Prefeitura anuncia vacinação na segunda-feira", "Escola abre inscrições para o ano que vem"], "Exagero e absurdo são sinais de alerta.", "🚨"),
            mc("Um sinal de notícia **confiável** é...", ["ter autor, data e fonte", "ter muitas exclamações", "pedir para repassar a todos"], "Confira quem escreveu e quando.", "✅"),
            separar("Sinal de confiança ou de alerta?", ["Confiança", "Alerta"],
                    [("nome do jornalista", 0), ("data da publicação", 0), ("site conhecido", 0), ("CAIXA ALTA e !!!", 1), ("\"repasse para todos!\"", 1), ("sem fonte nenhuma", 1)],
                    "Leia com olhos de detetive."),
            mc("Por que algumas pessoas criam fake news?", ["Para enganar, ganhar cliques ou prejudicar alguém", "Para ajudar a escola", "Por engano sempre"], "Por isso é importante checar.", "🤔"),
            tf("Uma notícia muito compartilhada é sempre verdadeira.", False, "Boatos também se espalham rápido!"),
            tf("Foto ou vídeo podem ser montados para enganar.", True, "Imagens também podem mentir."),
        ],
    ),
    "a5-b2-etica-u1-m2": missao(
        [
            ("🔍", "Antes de acreditar, faça a **checagem em 4 passos**."),
            ("1️⃣", "**Leia a notícia inteira**, não só o título. **Veja a fonte**: quem publicou?"),
            ("4️⃣", "**Procure em outros sites** confiáveis. **Pergunte a um adulto** de confiança."),
        ],
        [
            ordem("Ordene os passos da checagem:", ["Ler a notícia inteira", "Ver quem publicou", "Procurar em outros sites", "Conversar com um adulto"], "Ler → fonte → comparar → conversar."),
            mc("Ler **só o título** é perigoso porque...", ["o título pode enganar ou exagerar", "o título sempre mente", "o texto é desnecessário"], "Leia tudo!", "📰"),
            mc("Para confirmar uma notícia, é bom...", ["procurar em outros sites confiáveis", "acreditar no primeiro", "perguntar para quem mandou"], "Compare as fontes.", "🔎"),
            mc("Existem sites que fazem **checagem de fatos**. Eles servem para...", ["dizer se uma notícia é falsa ou verdadeira", "criar boatos", "vender jogos"], "São agências de checagem.", "✔️"),
            tf("Pedir ajuda a um adulto de confiança é parte da checagem.", True, "Duas cabeças pensam melhor."),
            mc("A data da notícia importa porque...", ["notícias antigas podem ser repassadas como se fossem novas", "não importa", "só notícias velhas são verdadeiras"], "Confira **quando** aconteceu.", "📅"),
        ],
    ),
    "a5-b2-etica-u1-m3": missao(
        [
            ("📲", "Chegou uma mensagem estranha no grupo da família? **Pare e pense** antes de compartilhar."),
            ("🛑", "Se não tem certeza, **não compartilhe**. Boatos podem assustar e prejudicar pessoas."),
            ("💬", "Você pode **avisar com educação** que a notícia é falsa."),
            desafio("com um adulto, escolha uma notícia na internet e façam juntos a checagem em 4 passos."),
        ],
        [
            mc("Recebeu: **\"Amanhã não vai ter aula em nenhuma escola do país!!! Repasse!\"**. O que fazer?", ["Checar com a escola antes de repassar", "Repassar para todos", "Faltar à aula"], "Confira na **fonte oficial**.", "🏫"),
            mc("Se descobrir que uma mensagem é falsa, você pode...", ["avisar com educação quem mandou", "xingar a pessoa", "mandar para mais gente"], "Respeito sempre.", "💬"),
            mc("Uma mensagem pede sua **senha** para ganhar um prêmio. Você...", ["não responde e avisa um adulto", "manda a senha", "manda para os amigos"], "Isso é **golpe**!", "🔐"),
            separar("Compartilhar ou não?", ["Pode compartilhar", "Não compartilhe"],
                    [("aviso oficial da escola", 0), ("notícia checada em vários sites", 0), ("foto do passeio com permissão", 0), ("boato sem fonte", 1), ("vídeo zombando de colega", 1), ("corrente que ameaça azar", 1)],
                    "Pense antes de clicar."),
            tf("Compartilhar uma fake news pode prejudicar outras pessoas.", True, "Boatos causam medo e confusão."),
            tf("Se todo mundo do grupo repassou, a notícia é verdadeira.", False, "Quantidade não é prova."),
        ],
    ),
    # ------------------------------------------------------------ Inglês
    "a5-b2-ingles-u1-m1": missao(
        [
            ("⚽", "**Sports**: soccer (futebol), basketball (basquete), volleyball (vôlei), tennis (tênis), swimming (natação)."),
            ("🎨", "**Hobbies**: reading (ler), drawing (desenhar), dancing (dançar), cooking (cozinhar)."),
            ("🎾", "Cada esporte usa um **equipamento**: racket (raquete), ball (bola), goggles (óculos de natação)."),
        ],
        [
            ligar([("soccer", "ball and goal"), ("tennis", "racket"), ("swimming", "goggles"), ("skateboarding", "skateboard")], "Ligue o esporte ao equipamento"),
            mc("**Basketball** em português é...", ["basquete", "beisebol", "vôlei"], "Bola na **cesta** (basket).", "🏀"),
            mc("**Soccer** é...", ["futebol", "tênis", "natação"], "Nos EUA, futebol se diz **soccer**.", "⚽"),
            mc("**Drawing** é o hobby de...", ["desenhar", "dançar", "dormir"], "draw = desenhar.", "🎨"),
            mc("Para jogar **tennis**, você precisa de um...", ["racket", "helmet", "goal"], "**racket** = raquete.", "🎾"),
            separar("Sport or hobby?", ["Sport", "Hobby"],
                    [("volleyball", 0), ("swimming", 0), ("basketball", 0), ("reading", 1), ("drawing", 1), ("cooking", 1)],
                    "Esportes e passatempos."),
        ],
    ),
    "a5-b2-ingles-u1-m2": missao(
        [
            ("💪", "**Can** = consegue/sabe fazer. **Can't** (cannot) = não consegue."),
            ("🏊", "**I can swim.** = Eu sei nadar. **She can't skate.** = Ela não sabe andar de skate."),
            ("❓", "**Can he swim?** → **Yes, he can.** / **No, he can't.**"),
        ],
        [
            mc("**I can swim.** significa...", ["Eu sei nadar.", "Eu não sei nadar.", "Eu quero nadar."], "**can** = sei/consigo.", "🏊"),
            mc("**She can't ride a bike.** significa...", ["Ela não sabe andar de bicicleta.", "Ela sabe andar de bicicleta.", "Ela tem uma bicicleta."], "**can't** = não consegue.", "🚲"),
            mc("**Can a fish fly?**", ["No, it can't.", "Yes, it can.", "Yes, it is."], "Peixe não voa!", "🐟"),
            mc("**Can a bird fly?**", ["Yes, it can.", "No, it can't.", "No, it is."], "Pássaros voam.", "🐦"),
            fill("A cat ___ climb trees.", ["can", "can't", "are"], "Gatos sobem em árvores!"),
            fill("A penguin ___ fly.", ["can't", "can", "is"], "Pinguins não voam, mas nadam!"),
            tf("**Can you dance?** pergunta se você sabe dançar.", True, "Can you...? = Você consegue...?"),
        ],
    ),
    "a5-b2-ingles-u1-m3": missao(
        [
            ("🌍", "Vamos conhecer **kids around the world**!"),
            ("🇯🇵", "**Yuki** is from Japan. She likes **origami** and she can play the **piano**."),
            ("🇺🇸", "**Jake** is from the USA. He likes **baseball**. **Amara** is from Kenya. She can **run** very fast."),
        ],
        [
            mc("Where is **Yuki** from?", ["Japan", "Kenya", "the USA"], "Yuki is from **Japan**.", "🇯🇵"),
            mc("What does **Jake** like?", ["baseball", "origami", "piano"], "He likes **baseball**.", "⚾"),
            mc("What can **Amara** do very well?", ["run fast", "play piano", "make origami"], "She can **run** very fast.", "🏃‍♀️"),
            mc("**Yuki can play the piano.** O que Yuki sabe fazer?", ["tocar piano", "jogar beisebol", "nadar"], "**play the piano** = tocar piano.", "🎹"),
            ligar([("Yuki", "Japan"), ("Jake", "the USA"), ("Amara", "Kenya")], "Ligue a criança ao país"),
            tf("**Origami** é a arte japonesa de dobrar papel.", True, "Muito popular no Japão!"),
        ],
    ),
}
