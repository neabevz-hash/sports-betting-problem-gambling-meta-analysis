# Калибровка вслепую, часть 1

Калибровка вслепую, часть 1: записи 1–150 из 400. Это случайные 400 записей из 7728 в списке к отбору финального поиска 2026-10-18 (зерно 20261018, порядок случайный). **Меток ИИ здесь нет.** Размечайте в любом порядке и в несколько заходов. Когда закончите все части, скажите: я проверю, что всё размечено, и закоммичу файлы до того, как открою метки ИИ.

**Как размечать.** Под каждой записью есть строка **Решение:** — допишите в неё код, после кода можно оставить заметку.

| Код | Что значит |
| --- | --- |
| `+` | включить: количественное исследование людей, где есть те, кто ставит на спорт (в том числе fantasy sports, киберспорт, спортивные лотереи на исходы матчей), и измерена проблемная игра (PGSI, SOGS, DSM-скрининги, интервью); или опрос населения об азартных играх с инструментом проблемной игры |
| `?` | не уверен — в сомнениях выбирайте это: лишний полный текст дешевле пропущенного исследования |
| `-1` | исключить: обзор, комментарий, теоретическая, правовая или регуляторная работа |
| `-2` | исключить: качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи |
| `-3` | исключить: нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора |
| `-4` | исключить: нет ставок на спорт: только скачки и бега, или ставки на спорт не измерялись вовсе |
| `-5` | исключить: выборка набрана по проблемам с игрой: лечение, горячая линия, самоисключение, сравнение проблемных игроков с контролем |
| `-6` | исключить: не про азартные игры или «ставка/лотерея» в другом смысле |
| `-7` | исключить: другое — напишите почему |

Пример: `**Решение:** -3 только частота ставок`. Символы `+ ? -` и цифры одинаковы на русской и английской раскладке.

**Что ищем:** долю проблемной игры среди тех, кто ставит на спорт. Она часто лежит в таблице с описанием выборки, а аннотация о ней молчит. Опрос беттеров, где не сказано, измеряли ли проблемную игру, — `?`. Опрос игроков или населения с инструментом проблемной игры, где неясно, спрашивали ли про ставки на спорт, — тоже `?`. Подробно — протокол, §8.

---

### 1 · R7880

**Against the Spread**

2007 · dissertation · en · https://doi.org/10.31390/gradschool_theses.3410

A sports-betting handicapper must determine his morality in a post-Katrina New Orleans without morals.

**Решение:** -6 художественное произведение о Новом Орлеане

---

### 2 · R7265

**To examine the effect of advocacy levels of sports consumers who participate in football betting games on betting behaviors**

2011 · Niğde Üniversitesi Açık Erişim Sistemi · dissertation · tr

Sosyal Bilimler Enstitüsü, Beden Eğitimi ve Spor Ana Bilim Dalı, Beden Eğitimi ve Spor Bilim Dalı

**Решение:** ? опрос футбольных беттеров, в аннотации нет данных об инструменте

---

### 3 · R2195

**Reaction to new information in live football betting markets**

2025 · Digital Repository (National Repository of Grey Literature) · dissertation · en

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -2 модели рынков live-ставок на футбол

---

### 4 · R3389

**Best PowerdFS Live-Play Fantasy Sports Platform**

2022 · Zenodo (CERN European Organization for Nuclear Research) · article, journalarticle/ · en · https://doi.org/10.5281/zenodo.6325981

Experience live-play fantasy sports games where you have the Power to control your team’s destiny. You can earn Power Tokens by signing up to Defy Games, entering certain contests, participating in contests with Power Token prizes, and by participating in other special offers. Power Tokens are the basis of our reward system and are like arcade tokens that you can use to enter contests.

**Решение:** -7 спам PowerdFS на Zenodo

---

### 5 · R7247

**U.S. Professional Athletics**

2011 · ASSER international sports law series · book-chapter · en · https://doi.org/10.1007/978-90-6704-799-9_56

This book looks at the Law and Policy on Betting and Sport in many countries around the world—sport is a global phenomenon—providing a very useful and valuable comparative survey on a subject that is so vital for safeguarding and preserving the integrity of those sports in which betting is legally allowed. The country reports show how sports-related betting is organized in the country concerned, also from a historical and policy perspective (national Lotteries Act; state run/state licensed lotteries and/or private operators; how the licensing system for public operators works; state supervisory mechanisms, etc.), and contain a treatment of the national case law. These keywords were added by machine and not by the authors. This process is experimental and the keywords may be updated as the learning algorithm improves.

**Решение:** -1 глава книги о праве и студенческом спорте

---

### 6 · R0898

**Consumer Responses to Sports Betting Taxation and Wagering Restrictions**

2026 · Elsevier BV · posted-content, preprint · https://doi.org/10.2139/ssrn.7479080

Several U.S. states have recently revised the structure of their sports wagering taxes, and others have restricted the wager types that legal sportsbooks may offer. Both policies have been argued to push consumers toward unregulated offshore operators, but this claim has rarely been tested. This study examined consumer responses to each using a within-subjects scenario experiment with 1,013 active online sports bettors across thirty-two states with legal online wagering. Respondents evaluated four escalating per-bet fees, two reductions in offered odds, and three withdrawals of a wager type, and reported the action they would most likely take in each case. Generalized estimating equations showed that per-bet taxes strongly reduce legal-market participation, with the share continuing to wager unchanged falling from 46.1% to 17.4% and the share abandoning the wager rising from 5.6% to 20.5%. The associated increase in offshore substitution was statistically significant but small, and equivalence testing bounded it below five percentage points. Withdrawal of a wager type produced a larger offshore response than any fee tested, regardless of which product was withdrawn, and extended to bettors with no prior offshore experience. The findings suggest that a per-wager fee should be modeled as a demandreducing instrument whose burden falls on low-stake wagers and that product restrictions carry significant offshore displacement.

**Решение:** ? эксперимент по налогам на ставки, проверить наличие шкалы PG

---

### 7 · R7937

**A Study on the Development and Changes of the Sports Lottery in China**

2007 · Journal of Japan Society of Sports Industry · article, other literature type, journal-article · en · https://doi.org/10.5997/sposun.17.2_25

Since the formation of the People's Republic of China, all kinds of lottery had been prohibited in the country as representing a corrupt practice of capitalism. But the Reform Openness policy and the Socialism Market Economy proposed by Deng Xiaoping permitted the introduction of the Sports Lottery in some Chinese provinces from 1984. The purpose of the Sports Lottery was to provide funds, which were necessary to hold different large-scale sports competitions and to build large-sized sport facilities. It was from 1994 that the Chinese government established a formal and national scale system of Sports Lottery. In 1995, the Chinese government promulgated three general plans related to sports ports Industry Development Program", "Olympic Games Program" and "National Fitness Promotion Program". At present, those three general plans still play a basic role in deciding the Chinese sports policy. According to the "S ports Industry Development Program", promotion of sports industries that meet the Socialist Market Economic System guarantees the realization of two other Programs in providing financial security. In this context, the Sports Lottery enables acquisition of the funds which are necessary for promotion of sports in all levels and at the same time it brings the development of different kinds of sports markets and sport businesses. Till now, 60% of the profit of a Chinese sports lottery have been used for "National Fitness Program" and 40% for "Olympic Games Program". Today, the Chinese sports lottery takes a role in providing an important source of revenue which supports the activity that the government performs in order to not only promote Chinese sports policies at all levels but also to develop and keep active the sports industry in expanding sports related markets. It will play a huge role in realizing Chinese sports strategic objectives for 21 century.

**Решение:** -1 политика и реформа спортивной лотереи Китая

---

### 8 · R4550

**Categorization of Qualifying Football Clubs for European Cups with Backpropagating Artificial Neural Networks**

2020 · DergiPark (Istanbul University) · article · en · https://dergipark.org.tr/tr/pub/jscai/issue/56697/832287

European cups are the most popular and most profitable football organization in the world. The participation of football clubs in the Champions League and the Europa League is, therefore, a matter of interest to all parts of society. In this respect, this paper uses backpropagating ANNs to understand the capability of categorizing football clubs from Italy, England, and Spain. The sample consists of 10 years of data from Seri A, English Premier League, and La Liga — and teams categorized as qualified and unqualified. As a result of the test, backpropagating ANN classifies the clubs with 92.7 percent accuracy. Our model correctly categorized 40 of 51 qualified teams in our test dataset—that is approximately 78 percent accuracy. However, our backpropagating ANN provides more significant accuracy while predicting unqualified teams, that is approximately 98.5 percent. The probable reason for lower accuracy in the categorization of qualified teams might be underrepresentation in the dataset and lack of variable diversity. The success of ANNs implies that it could be interesting to integrate ANNs into an online betting platform to develop solutions for more complex events by introducing more data. The application of other machine learning approaches will contribute to the literature and provide an opportunity to compare methods.

**Решение:** -2 модель выхода клубов в Лигу чемпионов

---

### 9 · R4921

**Gambling in Greenlandic adolescents.**

2019 · International journal of circumpolar health · journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1080/22423982.2019.1577094

Gambling has never been investigated in Greenlandic adolescents. High prevalence of gambling problems and a relation to other addictive behaviours has been found in adult Greenlanders. Greenlandic adolescents are daily exposed to gambling, for example, by selling lottery tickets, through advertises and electronic devices. The aim of this study is to investigate how Greenlandic adolescents perceive gambling, and to pilot test the Lie/Bet screening-instrument.Ten semi-structured focus group interviews were conducted for 31 adolescents, aged 12-16, from 3 schools in Nuuk, Greenland.The 31 adolescents have experiences with gambling. Whether they define a game as gambling depends on: 1) Whether the game is about playing with or about money, 2) whether the game is about earning items, 3) the gain/loss, 4) who they lose money to, and 5) the purpose. If the purpose is to have fun, it is not necessarily seen as gambling. None mentioned bingo as gambling, arguing that bingo is about having fun. Two recent trends were found to have reached Greenland: The close link between sports and gambling, and skin-betting. Additionally, the Lie/Bet screen was, with slight modifications, found to be useful as a screening-instrument among Greenlandic adolescents and it is proposed to be used in future studies.

**Решение:** ? фокус-группы и пилот скрининга Lie/Bet среди подростков

---

### 10 · R5275

**5 MONEY LAUNDERING, SPORTS BETTING AND GAMBLING**

2018 · Agenda Publishing eBooks · book-chapter · https://doi.org/10.3366/9781911116448-006

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 глава книги об отмывании денег через ставки

---

### 11 · R7332

**Health/Functioning Characteristics, Gambling Behaviors, and Gambling-Related Motivations in Adolescents Stratified by Gambling Problem Severity: Findings from a High School Survey**

2011 · American Journal on Addictions · article · en · https://doi.org/10.1111/j.1521-0391.2011.00180.x

In adults, different levels of gambling problem severity are differentially associated with measures of health and general functioning, gambling behaviors, and gambling-related motivations. Here we present data from a survey of 2,484 Connecticut high school students, and investigate the data stratifying by gambling problem severity based on DSM-IV criteria for pathological gambling. Problem/pathological gambling was associated with a range of negative functions; for example, poor academic performance, substance use, dysphoria/depression, and aggression. These findings suggest a need for improved interventions related to adolescent gambling and a need for additional research into the relationship (eg, mediating factors) between gambling and risk and protective behaviors.

**Решение:** + опрос 2484 школьников, критерии DSM-IV, ставки на спорт

---

### 12 · R1431

**Todo mundo no bolso das bets**

2025 · Universidade de São Paulo. Agência de Bibliotecas e Coleções Digitais · doctoral thesis, dissertation · und · https://doi.org/10.11606/003305707

"Todo mundo no bolso das bets" é um filme que investiga a rápida expansão do mercado de apostas esportivas online no Brasil, que, entre a legalização em 2018 e a regulamentação em 2025, transformou-se em um dos maiores do mundo. A obra analisa como esse crescimento ocorreu em um cenário de lacunas regulatórias e intensa atuação publicitária das plataformas de iGaming*, que difundiram o discurso do "jogo responsável" sem impedir o avanço de impactos sociais significativos, como endividamento, adoecimento psicológico e práticas de risco. A partir de entrevistas com especialistas, entidades de saúde, representantes do setor e jogadores, o filme retrata as camadas de vulnerabilidade às quais os apostadores brasileiros foram expostos ao formarem seus hábitos sem proteção institucional. O documentário busca contribuir para o debate público ao registrar tensões entre governo, mercado e população, revelando como o país enfrenta as consequências sociais, econômicas e emocionais dessa nova cultura de jogatina

**Решение:** -2 магистерская работа / документальный фильм о рынке ставок

---

### 13 · R7683

**Research on Legal System of Chinese Sports Lottery**

2009 · The Journal of Sports and Entertainment Law · article, journal-article · en · https://doi.org/10.19051/kasel.2009.12.4.149

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 правовое регулирование спортивной лотереи в Китае

---

### 14 · R2367

**Propuesta de reglamentación de las casas de apuestas deportivas en el Perú según la ley 31557: protección al consumidor y mejora en la recaudación tributaria**

2024 · LA Referencia (Red Federada de Repositorios Institucionales de Publicaciones Científicas) · dissertation · es

Las casas de apuestas es un tipo de negocio que se ha extendido de manera global, Perú no es la excepción y en ese contexto hace algunos años han surgido iniciativas por parte del gobierno mediante la ley 31557 y su modificatoria mediante ley 31806 de poder reglamentar dicho tipo de negocios, con la finalidad de proteger a los consumidores, supervisar la legalidad de las operaciones de estos negocios, así como aprovechar la oportunidad de poder obtener una mayor recaudación tributaria. En ese contexto surgió la inquietud de poder abordar esta problemática de una manera completa, para lo cual se recurrió a una exhaustiva revisión bibliográfica (realizada en los Capítulos II y III, así como en Anexos 2, 3 y 4), así como la aplicación de una encuesta validada (Anexo 5 y resultados en Capítulo IV) a una muestra de 86 personas, a fin de medir las variables reglamentación de las casas de apuestas deportivas (independiente) así como la variable recaudación tributaria (variable dependiente). La conclusión es que ambas variables en cada una de las dimensiones desarrolladas son muy importantes (50%) o importantes (22%) para los consumidores, por lo cual se hace necesaria ya la reglamentación e intervención del gobierno mediante entidades como MINCETUR, SUNAT e INDECOPI, que garanticen un correcto funcionamiento de estos negocios, protejan a los consumidores que realizan apuestas deportivas (asegure el pago de premios y prevenir ludopatía), así como servir de mecanismo que ayude por ejemplo a mejorar la tributación tanto de los negocios de casas de apuestas.

**Решение:** -6 исследование на крысах, нейробиология

---

### 15 · R8041

**Researching on the Basic Legislation Principles of Chinese Sport Lottery**

2005 · article · en

The law case on sport lottery was called one trouble fallen, another.Lacking of full and systematic sport lottery law contribute to these incidents. The author makes a simple research on the basic principle of sport lottery legislation in China by literature, interviewing experts, which is possible to provide some references for sport lottery legislation.

**Решение:** -7 спам Energy Bet на Zenodo

---

### 16 · R0829

**miR-10a-5p as a critical molecular regulator of dopaminergic impulsivity in the nucleus accumbens**

2026 · bioRxiv (Cold Spring Harbor Laboratory) · preprint · https://doi.org/10.64898/2026.07.20.739499

Abstract Impulsive-compulsive disorders (ICDs), including pathological gambling, hypersexuality, and compulsive buying, are frequently precipitated by dopamine D2/3 receptor agonists such as pramipexole (PPX), yet the molecular mechanisms that confer individual vulnerability remain poorly understood. Impulsive choice, a core dimension of ICDs, is modulated by dopaminergic signaling within corticostriatal circuits, but the microRNAs (miRs) that potentially translate this signaling into persistent behavioral change have not been identified. Here, we combined a delay discounting task (DDT) with high-throughput miR sequencing in the dorsal striatum and nucleus accumbens (NAcc) of rats stratified by baseline impulsivity and subchronic PPX treatment. PPX increased impulsive choice selectively in low- and mid-impulsive rats, whereas high-impulsive rats remained unaffected, consistent with a ceiling effect. Among the differentially expressed miRs, miR-10a-5p emerged as the strongest candidate: it was constitutively elevated in high-impulsive rats and upregulated by PPX in low- and mid-impulsive animals in both regions, thereby paralleling the trait-dependent behavioral effect of the drug. In vivo viral-mediated overexpression of miR-10a-5p confirmed its predicted downregulation of the PI3K–AKT–mTOR and BDNF pathways in the striatum, and, critically, overexpression restricted to the NAcc, but not the dorsal striatum, was sufficient to increase impulsive choice, recapitulating the pro-impulsive effect of PPX. These findings identify miR-10a-5p as a critical molecular regulator of impulsivity through its activity in the NAcc, providing a mechanistic link between dopaminergic perturbation, trait vulnerability, and ICDs, and opening new avenues for the development of miR-directed therapeutic strategies for these disorders.

**Решение:** -1 права спортсменов на данные, спортивное право

---

### 17 · R5888

**Energy Bet – Neue Sportwetten Plattform**

2016 · article · en

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -2 качественное исследование мотивов ставок в Сингапуре

---

### 18 · R2810

**Data Ownership, Athlete Rights and the Global Sports Gambling Industry**

2023 · Emerald Group Publishing Limited eBooks · part of book or chapter of book, book-chapter · en · https://doi.org/10.1108/s1476-285420230000018004

Abstract This chapter examines the shifting significance of data ownership and athlete rights as they pertain to the growth and expansion of the global sports gambling industry. It provides a nuanced overview of the ‘datafication’ of society, tracing how the omnipresent embrace of digital technologies has expediated new forms of organisational, political and corporate surveillance from which concerns over privacy, rights to ownership and the misuse of personal data arise. The chapter moves on to discuss how the extraction and trade of data has revolutionised how elite sport is performed, manufactured, broadcast and consumed, shedding critical light on the role of the gambling industry in the exchange of human data as a market commodity. These insights inform a series of socio-legal and ethical questions about the relationships between athlete data and the sports gambling industry for the purpose of signposting emerging issues and opportunities for critical sociological research and intervention.

**Решение:** -2 качественное исследование восприятия рекламы ставок детьми

---

### 19 · R2669

**Deviance, Discourses, and Everyday Rationalities of Sports Betting in Singapore**

2024 · Sociology Compass · article, journalarticle, journal-article · en · https://doi.org/10.1111/soc4.70007

ABSTRACT More liberal regulations and technological advances have spurred the growth of sports betting around the world. Given its long‐standing association with various social ills, how do sports bettors justify their gambling activities? This paper looks into the guiding principles and everyday practices of sports betting participants in Singapore. Based on qualitative research, it argues that sports bettors distinguish their activities by following a distinctive rationality that we call “benevolent play.” This concept refers to gambling practices where goodwill and charity serve as a justification for the potential of losing their bets and for their continued participation in sports betting. Apart from latching on the use of regulated gambling by state‐affiliated agencies to support development programs and charitable causes, benevolent play also emphasizes the sense of agency (football knowledge) and emotional investment (“play”) that sports bettors wage on their teams and communities. Generally, this study will contribute to the understanding of gambling culture and the larger discussions on deviance and social control.

**Решение:** -2 теоретическая модель поведения покупателей лотерей

---

### 20 · R5536

**What do children observe and learn from televised sports betting advertisements? A qualitative study among Australian children.**

2017 · Australian and New Zealand journal of public health · article, journal article, journalarticle · eng · https://doi.org/10.1111/1753-6405.12728

OBJECTIVE: To explore children's awareness of sports betting advertising and how this advertising may influence children's attitudes, product knowledge and desire to try sports betting. METHODS: Semi-structured qualitative interviews were conducted with 48 children (8-16 years) from Melbourne, Victoria. The interview schedule explored children's recall and interpretations of sports betting advertising, strategies within advertisements that may appeal to children, children's product knowledge and understanding of betting terminology, and factors that may encourage gambling. Interviews were transcribed and thematic analysis was conducted. RESULTS: Children recalled in detail sports betting advertisements that they had seen, with humour the most engaging appeal strategy. They were also able to describe other specific appeal strategies and link these strategies to betting brands. Many children described how advertisements demonstrated how someone would place a bet, with some children recalling the detailed technical language associated with betting. CONCLUSIONS: Children had detailed recall of sports betting advertisements and an extensive knowledge of sports betting products and terminology. Implications for public health: To protect children from the potential harms associated with sports betting, governments should consider changing regulations and implementing evidence-based education campaigns to counter the positive messages children receive from the sports betting industry.

**Решение:** -1 комментарий 1987 года о спортивных ставках и медиа

---

### 21 · R7831

**Economic Research on Consumer’s Behavior in Sport Lottery Market**

2008 · Sichuan Sports Science · article · en

This paper using the prospect theory of behavior economic to analyze the behavior of consumers in sport lottery and research the effection of consumer s motivation in sport lottery,and some suggestion on issuance are put forward in the paper.

**Решение:** -1 бразильская диссертация по классификации азартных игр

---

### 22 · R8448

**Sports gambling and the media.**

1987

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 тестирование программного обеспечения сайта ParionsWeb

---

### 23 · R2056

**Categorização regulatória de produtos estigmatizados o caso das apostas esportivas online de cota fixa e cassinos online no Brasil**

2025 · LA Referencia (Red Federada de Repositorios Institucionales de Publicaciones Científicas) · dissertation · pt

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 кризисные коммуникации при сбое приложения ESPN Fantasy

---

### 24 · R6837

**Projet automatisation du test technique de non-régression comptable**

2012 · HAL (Le Centre pour la Communication Scientifique Directe) · dissertation · fr

Ce mémoire a été réalisé au sein de la Française Des Jeux (FDJ), entreprise publique française ayant le monopole de la loterie, des jeux de grattage et de tirage en ligne sur tout le territoire. En plus de ces activités, la société a décidé depuis le début de l'année 2009 de lancer un site de jeux en ligne pour les paris sportifs : ParionsWeb 1. Le projet est appelé Modern Buy. La Française Des Jeux a fait appel à une société externe d'édition logicielle basée en Grande-Bretagne, nommée Laverock von Schoultz Limited (LVS), pour le développement de cette application de jeux en ligne. Cette société a depuis été rachetée par la Française Des Jeux. LVS s'occupe uniquement de la partie développement. Les autres métiers liés au projet tels que le marketing, les études, la gestion de projet, l'intégration, la qualification, la recette et la mise en production ont été alloués à des ressources internes. La partie intégration, qualification technique, mise en production et maintenance est assurée par l'équipe Homologation et Maîtrise Opérationnelle des Applications (HMOA) Multimédia Sport. À chaque livraison, le chef de projet HMOA et son équipe prennent en charge l'application pour vérifier l'adéquation du produit développé par rapport aux exigences. Le projet est basé sur le modèle du cycle en V 2

**Решение:** -2 качественное исследование студентов о спортивных ставках

---

### 25 · R5230

**Fantasy Breakdown: A Case Study on Organizational Crisis Communication and Stakeholder Reaction During Mass Product Failure**

2018 · International Journal of Sport Communication · article · en · https://doi.org/10.1123/ijsc.2018-0090

On the first Sunday of the National Football League’s 2016–17 season, a technical issue caused ESPN’s fantasy-football website and mobile application to fail. ESPN’s product failure is no small problem and represented a major organizational crisis; with 7.1 million unique users, ESPN represents the largest provider of a multi-billion-dollar fantasy-sport industry. This case study examined ESPN’s organizational communication strategy, as well as the stakeholder responses surrounding the failure of ESPN’s fantasy-football website and application on the most anticipated day of the fantasy-sport season. Using content analysis and partnering with a social media data insights company, the study examined social media messages from both the organizational and consumer side of this fantasy-sport product failure. Through ampling 1,542 social media messages from a population of 11,881 unique comments via Twitter, the reactive nature of ESPN’s messages and the direct responses from its consumers was ascertained.

**Решение:** -2 модель неэффективности рынка ставок на футбол

---

### 26 · R4967

**남자 대학생의 도박 경험에 관한 질적 연구 - 스포츠토토를 중심으로 -**

2019 · 융합정보논문지(구 중소기업융합학회논문지) · article · ko

본 연구의 목적은 남자 대학생들의 스포츠토토 도박을 통해 겪게 되는 경험과 그들이 당면하고 있는 문제를 파악하여 남자 대학생 도박중독의 예방 및 회복 프로그램에 기초자료를 제공하고자 시도하였다. 본연구의 참여자들 은 8명의 남자 대학생으로 심층 인터뷰 한 자료를 Colaizzi의 현상학적 연구방법에 따라 분석하였다. 연구결과 경험 의 범주는 4개로 바다로 달려가는 바람처럼, 회한으로 흐르는 눈물, 수면 아래로 잠긴 삶, 꿈을 꾸는 날엔 으로 도출되었다. 본 연구를 통해 스포츠토토는 접근성이 용이하고 흥미 유발적인 요소가 많지만, 일반 도박자들과 마찬 가지로 자기 통제력을 상실한 채 중독에 빠질 위험이 크다는 것이 드러났다. 그렇지만 도박 기간이 짧은 대학생이 경제적 자금 조달의 한계점으로 현실을 자각할 경우 도박중독 위험으로부터 비교적 빠르게 격리될 수 있다고 본다. 따라서 스포츠를 좋아하는 대학생들을 위한 도박 예방교육과 상담이 필요할 것으로 생각된다.

**Решение:** -1 сравнительный анализ регуляторной политики штатов

---

### 27 · R8430

**The degree of inefficiencyin the football betting market**

1991

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 модели спонсорства спортивных клубов букмекерами

---

### 28 · R0770

**ESTRUTURAS DE PODER E DIFERENCIAÇÃO ESTATAL: JOGOS DE APOSTA E MOBILIDADE URBANA EM PERSPECTIVA COMPARADA**

2026 · Cadernos de Estudos Interdisciplinares · peerreview/, review, article · pt · https://doi.org/10.5281/zenodo.19616828

Este artigo analisa a atuação seletiva do Estado brasileiro no tratamento de atividades funcionalmente semelhantes que operam nas fronteiras entre legalidade, informalidade e regulação. A partir de uma abordagem comparativa, o estudo examina dois pares de casos: o contraste entre a repressão histórica ao jogo do bicho e a regulamentação das apostas esportivas online, e a criminalização dos transportes alternativos por vans em comparação com a posterior regulação das plataformas digitais de transporte individual. Ancorado na literatura de políticas públicas, burocracia e economia política do Estado, o artigo argumenta que as diferenças observadas não decorrem principalmente de critérios técnicos, jurídicos ou morais, mas de estruturas de poder que condicionam a capacidade dos atores de influenciar processos decisórios. Metodologicamente, trata-se de um estudo bibliográfico e exploratório, baseado na revisão crítica da literatura e na reconstrução histórica dos enquadramentos institucionais atribuídos a cada atividade. Os resultados indicam que práticas associadas a atores com menor capacidade de organização e influência institucional tendem a ser objeto de repressão seletiva e ilegalidade persistente, enquanto aquelas articuladas por agentes economicamente organizados e politicamente conectados são mais frequentemente incorporadas ao ordenamento jurídico por meio da regulação. O artigo contribui para o debate sobre seletividade estatal ao evidenciar como a legalidade é produzida e estabilizada a partir de disputas políticas e assimetrias de poder. Este artículo analiza la actuación selectiva del Estado brasileño en el tratamiento de actividades funcionalmente similares que operan en los límites entre legalidad, informalidad y regulación. A partir de un enfoque comparativo, el estudio examina dos pares de casos: la represión histórica del jogo do bicho frente a la regulación de las apuestas deportivas en línea, y la criminalización del transporte alternativo por vans en contraste con la posterior regulación de las plataformas digitales de transporte individual. Basado en la literatura sobre políticas públicas, burocracia y economía política del Estado, el artículo sostiene que las diferencias observadas no se explican principalmente por criterios técnicos, jurídicos o morales, sino por estructuras de poder que condicionan la capacidad de los actores para influir en los procesos decisorios. Metodológicamente, se trata de un estudio bibliográfico y exploratorio, sustentado en la revisión crítica de la literatura y en el análisis histórico de los marcos regulatorios. Los resultados indican que las actividades asociadas a actores con menor capacidad de influencia institucional tienden a permanecer bajo regímenes de represión selectiva, mientras que aquellas vinculadas a actores organizados y políticamente conectados son más propensas a ser incorporadas mediante la regulación. El artículo contribuye al debate sobre la selectividad estatal al destacar el carácter político de la producción de la legalidad. This article examines the selective action of the Brazilian state in dealing with functionally similar activities operating at the boundaries between legality, informality, and regulation. Using a comparative approach, the study analyzes two pairs of cases: the historical repression of the jogo do bicho and the regulation of online sports betting, and the criminalization of informal van transportation compared to the subsequent regulation of digital ride-hailing platforms. Drawing on the literature on public policy, bureaucracy, and political economy, the article argues that the observed differences are not primarily driven by technical, legal, or moral criteria, but by power structures shaping actors’ capacity to influence decision-making processes. Methodologically, the study is based on a bibliographic and exploratory review, combining theoretical contributions with historical analyses of regulatory trajectories. The findings suggest that activities associated with actors lacking institutional influence tend to remain under selective repression and persistent illegality, whereas those linked to organized and politically connected actors are more likely to be incorporated through regulation. The article contributes to debates on state selectivity by showing how legality is politically constructed and stabilized through power asymmetries.

**Решение:** -2 математика азартных игр, вероятности

---

### 29 · R2527

**A Parallel Assessment of Non-Gambling-Based and Gambling-Based Sponsorships of Sports Properties**

2024 · The Journal of Gambling Business and Economics · article, journalarticle, journal-article · en · https://doi.org/10.5750/jgbe.v16i2.2083

The current study examines the congruence, or lack thereof, of the relationships as identified in two earlier studies: one that addressed sports-based sponsorship and the other that focused on sports gambling. Study one identified a general model of the sports sponsorship environment based upon an array of benefits derived by four categories of beneficiaries that are directly impacted by the sponsorship of a sports entity (i.e., team, athlete, sports venue, and so on). The four categories of beneficiaries were identified as sponsors, sports, spectators, and society-at-large. The original model further examined the interactions among the four categories of beneficiaries while delineating 12 directional linkages and 159 potential benefits. The second study focused on the results emanating from a recent Supreme Court of the United States (SCOTUS) ruling that declared the Professional and Amateur Sports Protection Act (PASPA) to be unconstitutional. That ruling allowed American gambling organizations to become more involved in sports betting, and consequently, they have become engaged in the sponsorship of a variety of sports entities. A similar analysis to the one used in traditional sports sponsorship documented 14 groups of beneficiaries and 201 benefits. The current study, which delineated 215 benefits, extends the previous research by integrating these complementary streams within an overarching sponsorship model. Results demonstrate that the sponsorship environment is more complex than previous research has shown, and several contributions that are both theoretical and managerial in scope are articulated.

**Решение:** -6 антропологическая диссертация о ритуалах в Тибете

---

### 30 · R7947

**Probability Guide to Gambling: The Mathematics of Dice, Slots, Roulette, Baccarat, Blackjack, Poker, Lottery and Sport Bets**

2006 · PhilPapers (PhilPapers Foundation) · book · en

Over the past two decades, gamblers have begun taking mathematics into account more seriously than ever before. While probability theory is the only rigorous theory modeling the uncertainty, even though in idealized conditions, numerical probabilities are viewed not only as mere mathematical information, but also as a decision-making criterion, especially in gambling. This book presents the mathematics underlying the major games of chance and provides a precise account of the odds associated with all gaming events. It begins by explaining in simple terms the meaning of the concept of probability for the layman and goes on to become an enlightening journey through the mathematics of chance, randomness and risk. It then continues with the basics of discrete probability, combinatorics and counting arguments for those interested in the supporting mathematics. These mathematic sections may be skipped by readers who do not have a minimal background in mathematics; these readers can skip directly to the Guide to Numerical Results to pick the odds and recommendations they need for the desired gaming situation. Doing so is possible due to the organization of that chapter, in which the results are listed at the end of each section, mostly in the form of tables. The chapter titled The Mathematics of Games of Chance presents these games not only as a good application field for probability theory, but also in terms of human actions where probability-based strategies can be tried to achieve favorable results. Through suggestive examples, the reader can see what are the experiments, events and probability fields in games of chance and how probability calculus works there. The main portion of this work is a collection of probability results for each type of game. Each game s section is packed with formulas and tables. Each section also contains a description of the game, a classification of the gaming events and the applicable probability calculations. The primary goal of this work is to allow the reader to quickly find the odds for a specific gaming situation, in order to improve his or her betting/gaming decisions. Every type of gaming event is tabulated in a logical, consistent and comprehensive manner. The complete methodology and complete or partial calculations are shown to teach players how to calculate probability for any situation, for every stage of the game for any game. Here, readers can find the real odds, returned by precise mathematical formulas and not by partial simulations that most software uses. Collections of odds are presented, as well as strategic recommendations based on those odds, where necessary, for each type of gaming situation. The book contains much new and original material that has not been published previously and provides great coverage of probabilities for the following games of chance: Dice, Slots, Roulette, Baccarat, Blackjack, Texas Hold em Poker, Lottery and Sport Bets. Most of games of chance are predisposed to probability-based decisions. This is why the approach is not an exclusively statistical one, but analytical: every gaming event is taken as an individual applied probability problem to solve. A special chapter defines the probability-based strategy and mathematically shows why such strategy is theoretically optimal."

**Решение:** -1 юридический комментарий о праве вето спортивных лиг

---

### 31 · R7386

**Power, charisma, and ritual curing in a Tibetan community in India**

2010 · cIRcle (University of British Columbia) · other literature type, thesis, text/text · en · https://doi.org/10.14288/1.0097119

This dissertation is concerned with the ways in which Tibetans living in Dharmsala, Northern India, react to events such as illness, personal distress, and misfortune, when they perceive such events as disturbances to a given social and moral order and as evidence of "spirit attack". To re-establish the order, the context moves/widens from a concern with an afflicted individual to include more general political issues and finally focuses on the legitimation of authority. Dharmsala Tibetans live in a hierarchical society and subscribe to a hierarchical cosmos. The ideology places responsibility upon humans for aligning this hierarchy and prescribes the legitimate means by which the hierarchy may be ascended. Two efficient causes of illnesses result in spirit attack: (1) the first attributes spirit attack to human violation of hierarchical tenets; (2) the second, to the illegitimate status ambitions of evil spirits. The logic of the ritual cure addresses the resolution of status ambiguities. Successful ritual cures are appreciated in terms of two idioms denoting two aspects of charismatic authority. When the spirit attack results from human violation of hierarchical tenets, the patient's cure is contingent upon his or her unsystematically acquired power (rlung-rta). When the second efficient cause obtains and evil spirits are responsible for the attack, the patient's cure depends upon the outcome of a duel between an exorcist and the spirit(s), and the successful cure is described in terms of systematically acquired power (dbang). These idioms serve not only to legitimate status in Tibetan society, but also to rationalize hierarchical ascent. In addition to ritual curing, the idioms are employed in assessing the outcomes of events such as sports, gambling, and weather-making. Where the idioms overlap moral ambiguities emerge. The two idioms are discernible in much of Tibetan history where they focus upon the legitimation of succession to charismatic office. The idiom of unsystematically acquired power appears to predominate in the present refugee context.

**Решение:** -2 эффективность рынков прогнозов NFL

---

### 32 · R1532

**Can Sports Leagues "Veto" Certain Online Sports Betting Wagers?**

2025 · eYLS (Yale Law School) · article

This comment will argue, in light of three Horseracing Integrity and Safety Act (HISA)-related Circuit Court cases and new guidance from the Supreme Court on the private nondelegation doctrine, that HISA provides a workable framework to resolve whether sports leagues can engage in rulemaking to prevent certain kinds of bets from taking place. Specifically, the Supreme Court and the Fifth, Sixth, and Eighth Circuits appear to have reached a large amount of common ground regarding the structure of the private nondelegation doctrine, and the Circuit Courts have found that much of HISA fits well within that structure. In light of that, this comment will contend that sports leagues can constitutionally stop gambling organizations from offering certain kinds of bets, but regulatory schemes that give leagues such power must also give federal or state agencies the ability to issue rules that can change, add to, or remove the leagues’ stipulations.

**Решение:** -1 исторический обзор спортивных ставок 1979 года

---

### 33 · R8221

**Longshots , Overconfidence and Efficiency on the Iowa Electronic Market ***

2002

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -2 вероятностная модель коэффициентов на футбол

---

### 34 · R6078

**Haftung der Verwaltung in Beruhensfällen am Beispiel der Regulierung von Sportwetten und Spielhallen unter dem GlüStV 2012**

2015 · Deutsches Verwaltungsblatt · article · de · https://doi.org/10.1515/dvbl-2015-1403

Article Haftung der Verwaltung in Beruhensfällen am Beispiel der Regulierung von Sportwetten und Spielhallen unter dem GlüStV 2012 was published on July 1, 2015 in the journal Deutsches Verwaltungsblatt (volume 130, issue 14).

**Решение:** -3 опрос киберспортсменов о спонсорстве без инструмента PG

---

### 35 · R1391

**Real-Time Football Match Prediction Platform**

2025 · ITM Web of Conferences · article, journalarticle, conference · en · https://doi.org/10.1051/itmconf/20257004003

The integration of real-time data into sports analytics has significantly enhanced the accuracy of football match predictions, which is vital for team management, tactical planning, and commercial applications *such as sports betting. This paper presents a Python-based platform for predicting football match outcomes by collecting and processing real-time data from the SofaScore website. The platform employs machine learning models, including Random Forest, Support Vector Machines (SVM), and Neural Networks, combined with feature engineering techniques, to generate accurate predictions. A user-friendly interface is also developed to facilitate easy access and analysis of this data. The platform’s real-time data updating mechanism ensures prediction accuracy, while the integration of multiple models through a Stacking method further enhances reliability. The platform’s innovative design addresses key challenges in sports analytics by providing a robust tool for data-driven decision-making. Future work will focus on enhancing model algorithms and incorporating more complex data sources, such as social media sentiment analysis, to further improve prediction accuracy.

**Решение:** ? опрос родителей и подростков о гемблинге, проверить шкалу PG

---

### 36 · R1028

**Beyond the Ban: A Regulatory Framework for Real-Money Gaming in India**

2026 · SSRN Electronic Journal · article, preprint · und · https://doi.org/10.2139/ssrn.6317538

&lt;span&gt; &lt;p&gt;&lt;span&gt;India’s fantasy sports and real‑money gaming ecosystem has long operated within a legal grey zone. Colonial‑era gambling legislation, particularly the Public Gambling Act of 1867, was designed to regulate physical betting houses and local wagering activities, not algorithm‑driven digital platforms operating across state and national borders. As online fantasy sports platforms scaled rapidly in the smartphone era, this structural mismatch between nineteenth‑century law and twenty-first-century technology became increasingly visible.&lt;/span&gt;&lt;/p&gt; &lt;p&gt;&lt;span&gt;In August 2025, the Government of India moved toward stronger restrictions on real‑money online gaming through the Promotion and Regulation of Online Gaming Bill, 2025. The policy shift was driven by legitimate concerns: mounting financial losses among users, rising evidence of addictive patterns among young players, allegations of opaque platform design, and fragmented state‑level regulation. However, while the risks associated with real‑money gaming are well documented, prohibition may not be the most effective long‑term response. Evidence from comparable markets suggests that outright bans often displace users toward offshore or illegal platforms where consumer protection is weaker and regulatory oversight is minimal.&lt;/span&gt;&lt;/p&gt; &lt;p&gt;&lt;span&gt;This paper argues that India would be better served by a robust national regulatory framework rather than broad prohibitory measures. The central policy question is not whether risks exist—they clearly do—but whether prohibition or regulation manages those risks more effectively. The paper proceeds by examining the legal foundations of fantasy gaming in India, analysing the rationale behind recent restrictions, evaluating the likely consequences of prohibition, and proposing a structured regulatory model tailored to the Indian context.&lt;/span&gt;&lt;/p&gt;&lt;/span&gt;

**Решение:** -1 немецкий сборник по уголовному праву и ставкам

---

### 37 · R5644

**ABOUT THE EDITORS AND CONTRIBUTORS**

2016 · Lexington Books · part of book or chapter of book · und · https://doi.org/10.5771/9781498504898-305

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 комментарий к скандалу со ставками в итальянском футболе

---

### 38 · R7312

**1853.5 The Baseball Press Emerges**

2011 · Base Ball A Journal of the Early Game · article · en · https://doi.org/10.3172/bb.5.1.106

"BASE BALL AT HOBOKEN: The first friendly game of the season, between the Gotham and Knickerbocker Base Ball Clubs was played on the grounds of the latter on the 5th inst. The game was commenced on Friday the 1st, but owing to the storm had to be postponed, the Knickerbockers making nine aces to two of the Gothams, the following is the score for both days." The Knicks won, 21-12, according to an abbreviated box score, which uses "No. of Outs" and not "Hands Lost" in the left-hand column, and "Runs," not "Aces," in the right-hand column. Paul Wendt estimates that this is the first certain Knick-rules box score known, and the first since the October 1845 games.1Henry Chadwick may have been baseball's most important writer in its early days, but he was not its first. That honor would go to William Cauldwell, who, like Chadwick, was born in 1824. "I can speak as a New York boy from away back," Cauldwell told the Mills Commission in 1905, "and in an all my experiences I had no knowledge of the prominence of a ball game called 'rounders.' I played ball in my native city from the time I was (to use an old time phrase) 'knee high to a mosquito' dating back to a period when Fourteenth Street was considered out of town."2Cauldwell would have played ball in lower Manhattan, near Crosby Street, for he went to primary school at the "High School for Males," at No. 36 Crosby near Broome Street. As editor of the weekly Sunday Mercury, Cauldwell made mention of baseball on May 1, 1853, and later that year devoted space to the Knickerbocker-Gotham match of July 5. These were the first press accounts of baseball games since various newspapers covered the three October 1845 contests between clubs from Brooklyn and New York.As Chadwick was not the first to cover baseball, neither was the New York Clipper. For decades after its debut number of April 30, 1853, the Clipper was never all about baseball, or even primarily so.3 Yet more than any other publication, it may be said to have transformed a boys' game into the national pastime. To place in context how the Clipper advanced the status of baseball, let's look at the sporting papers that paved its way.I suggest that three essential ingredients facilitate the growth of any localized game to national sport. First, gambling. Adults must care about the outcome, and their willingness to place a wager is a reasonable measure of their interest. As a game matures, investors and civic boosters may pool their interests in order to absorb a greater risk, placing their bets on the protracted success of a club or a ball grounds. Second, statistics. Whether merely game scores or primitive box scores, these numerical attachments to prose accounts accord a mantle of importance to the matches-an importance like that of trade or transport or government; in addition, quantifying the game's constituent parts further fuels the first mover of sport, gambling. Third, publicity. Regular press coverage is a necessary development to waftthe enthusiasm exhibited at a single contest, however it may have been fueled, to those only reading about it afterward, often at great distance from the event.Before baseball came to dominate the sporting scene in the last quarter of the 19th century, these three elements had previously advanced the popularity of other sports: the turf, the ring, sculling, cricket, and the pit (blood sports such as ratting, baiting, cockfighting, and dog-fighting). Whether the crowd drawn by the activity was low or genteel, the ingredients and the progression were similar. American sporting papers, beginning in the 1820s, paved the way for each sport to mature by providing records and prognostications related to events of interest to the sporting set and-underlying it all- the basis of a potential wager.Despite the nationwide surge of interest during the Jacksonian era in newspapers and magazines touching upon all topics-from politics to religion, from literature to commerce-sporting coverage lagged. …

**Решение:** -2 модель волатильности коэффициентов на Betfair

---

### 39 · R8476

**The Changing Structure of American Gambling in the Twentieth Century**

1979 · Journal of Social Issues · article · en · https://doi.org/10.1111/j.1540-4560.1979.tb01047.x

The author examines some of the factors that altered the economics and control of policy and numbers gambling, bookmaking, and casino gambling from 1900 to 1950. The factors include the emergence of black ghettoes after World War I and the consequent rise of blacks to controlling positions in numbers and policy banks; the changing ownership and activities of the national race and sports information service; the increasing use of the telephone for making sports bets; and the sudden wealth of bootleggers in the 1920's along with their growing involvement in gambling enterprises. The author concludes that these factors exercised a diverse and interrelated influence on the history of American gambling.

**Решение:** -6 финансовый кейс о хеджировании и деривативах

---

### 40 · R2379

**Ciência de Dados no futebol: Uma análise estatística das cotações de casas de apostas online**

2024 · Matemática e Estatística em Foco · article · pt

Football is one of the most popular sports in the world. Because of this, it is not uncommon to hear about thestatistics of this sports modality; the quotation or odds is one of them. The main objective of this work is toanalyze and generate insights from the odds of football matches in online bookmakers. Among the questionsanswered in this work are: Is there a winning bias for the home team? How do bookmakers make money? Howgood are the odds from bookmakers? How is the wisdom of the crowd related to sports betting? It will alsobe seen how statistical fallacies can arise during sports analysis and how people (fans, bettors and sponsors,among others) are exposed to random and high-impact events.

**Решение:** -3 поведенческие транзакции оператора без инструмента PG

---

### 41 · R5800

**Parents’ Perception of Youth Gambling and Other Risk Behaviors**

2016 · Digital Scholarship - UNLV (University of Nevada Reno) · article, conference object, conference-paper · en · http://www.library.unlv.edu/system/files/webform/ir/files/ppt_kranzelic_et_al_las_vegas_2016.pdf

Recently conducted national prevalence study of youth gambling in Croatia indicated high prevalence of adolescent gambling (especially sports betting), as well as perceived parental acceptance of such behavior (Ricijas et al, 2011). As international research suggest positive correlations between parental perception of gambling and other risk behaviors with the intensity of their childrens' participation in these behaviors (Meerkamper, Derevensky, Cutajar, 2008; Farrington, Loeber, Ttofi, 2011; Cambell et al, 2011), a new study on parental perception of gambling is currently being conducted, using two comparable perspectives - parents and their adolescent children.\nResearch is being conducted in two largest Croatian cities (Zagreb and Split) from October to December 2015 with expected sample of approximately N=400 parents and their adolescent children. The following instruments are being used: (1) Questionnaire on basic socio-demographic characteristics, (2) Parents as Partners Gambling Research Study (Derevensky, 2008) and (3) Gambling Activities Questionnaire.\nThe analysis will be based on matched pairs (parents and their children) in order to examine the hypothesis that parental and children’s perception of gambling and other risk behaviors, as well as perception of gambling accessibility in Croatia, significantly differs. Furthermore, this paper will also examine differences in parental knowledge about their children’s gambling activities compared to children’s self-report, with special emphasis on controlling the effects of child’s gender.\nResearch results will be considered in direction of providing guidelines for development and implementation of preventive and treatment interventions that engage both children and parents.

**Решение:** -1 экономика и налогообложение игорного сектора Вьетнама

---

### 42 · R7011

**Regulierung des deutschen Sportwettenmarktes in komparativer Perspektive – Glücksspielgesetze in der Europäischen Union**

2012 · Edition HWWI · part of book or chapter of book, book-chapter · de · https://doi.org/10.15460/hup.213.1564

Die Autonomie des Sports, die verfassungsrechtlich verbrieft ist, wird durch das Gemeinschaftsrecht der EU nicht konsequent respektiert. So wird beklagt, dass die notwendige Kooperation der Verbände im Sport nicht hinreichend berücksichtigt wird. Hier setzen die Referenten des 9. Internationalen Hamburger Symposiums „Sport und Ökonomie“ an, wenn sie rechtliche und ökonomische Fragen um Sportgroßveranstaltungen aufgreifen und Vorschläge zur Stellung des Sports im europäischen Rahmen diskutieren. Aufgezeigt wird , dass der sogenannte Sport ökonomisch geprägt wird, was noch keine angemessene Entsprechung auf europäischer Ebene gefunden hat. Das wird zum Beispiel bei Sportwetten und dem Glücksspielmonopol deutlich. Der Band wird die durch das EU-Weißbuch Sport und die Entschließung des Bundestages zum Sport in Europa entstandene Debatte weiter beleben. The autonomy of sport which is constitutionally recognised is not consistently respected by EU law. There are complaints that the necessary cooperation of the federations in sport is not sufficiently taken into account. This is where the speakers of the 9th International Hamburg Symposium "Sport and Economics" come in when they address legal and economic questions about major sporting events and discuss proposals on the status of sport in the European context. It shows that sport is economically shaped, which has not yet found an adequate equivalent at European level. This is evident, for example, in sports betting and the gambling monopoly. The volume will further stimulate the debate created by the EU White Paper on Sport and the Bundestag resolution on sport in Europe.

**Решение:** -3 опрос зрителей тхэквондо о намерении делать ставки, без PG

---

### 43 · R7564

**Multidisciplinary teamwork and home based technologies research with older adults**

2009 · Northumbria Research Link (Northumbria University) · conference-paper · en

Overview of the official 1win site for India: main facts about the bookmaker, available Indian registration options, verification documents, compact mobile app for Android and iOS with instructions on how to download and install on your gadget, sportsbook and types of casino games, as well as deposit and withdrawal methods. Find out more by going to our review. Start with a simple and straightforward registration and get +500% welcome bonus on your first deposit.

**Решение:** -7 спам прогнозов на спорт / tipster на Zenodo

---

### 44 · R2295

**Sports gambling creates a windfall, but raises questions of integrity – here are three lessons from historic sports-betting scandals**

2024 · The Conversation Media Group Ltd · article, other, posted-content · en · https://doi.org/10.64628/aai.sunqd4u5s

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -2 модель ставок на австрийский футбол

---

### 45 · R8038

**Corporate Valuation : A case study of Unibet**

2005 · Internationella Handelshögskolan · bachelor thesis, article · en · http://urn.kb.se/resolve?urn=urn:nbn:se:hj:diva-120

Problem: The online betting industry has erased the importance of national borders and opened up the world, which has lead to a more diversified perspective of the company. In this master thesis we wanted to broaden and develop the topic of corporate valuation with regard to the on-line gambling industry. In order to do that, a case study of the on-line betting firm Unibet and its core betting activities has been carried out. Purpose: The study aims to identify factors in the strategic, SWOT and financial analysis that will be used in the cash flow valuation model in order to derive the company value. Method: A case study has been chosen to collect empirical data to our study. Conclusion: A cash flow valuation in different scenarios was carried out. With the assumptions made in the “probable” scenario a value of approximately GBP 85 million was reached, which was significantly lower than the listed value. This is mainly due to the fact that we believe that the increased competition will make it difficult for Unibet to maintain its strong growth in sales in the future. The assumptions have been based on the information gained from the strategic analysis, the SWOT analysis and the development in financial ratios.

**Решение:** -2 диссертация о культуре ставок среди молодых мужчин

---

### 46 · R5296

**Analytical Tools: Arbitrage, mean reversion, risk arbitrage and the favorite-longshot bias**

2018 · World Scientific series in finance · book-chapter · en · https://doi.org/10.1142/9789813276505_0006

You can hedge bets as the odds change based on the current score and field position. My experience is that the sports betting market is more efficient than the financial markets, so therefore harder to beat. Of course, die hard efficient market types will like to forget that efficient markets has taken a severe beating in the 1987 and 2007-2009 stock market crashes. They simply cannot explain these events, nor the consistent high returns of some superior investors.

**Решение:** -1 анализ медиаконтента ESPN и рекламы ставок

---

### 47 · R4913

**Natural Groups of daily fantasy sports players**

2019 · Digital Scholarship - UNLV (University of Nevada Reno) · conference-paper · en

Abstract: Researchers use many different measures to quantify gambling involvement. Those studying different gambling environments can use these measures to partition the players into groups or subgroups. On DraftKings, the contests’ entry fees range from $0.10 to over $10,000. DraftKings’ customers can choose to enter as many or as few contests as they can afford. In this study, we examine a sample of DraftKings customers who made their first deposits to the site in August or September of 2014, calculating summary statistics based on activity during the 2014 NFL season. Using k-means cluster analysis with k = 4, we partitioned the sample separately by number of entries over the season and by average entry fees. Using these two partitions, we separated the sample into subgroups, and then compared the sizes, average profits/losses, and returns on investment of the subgroups. Over 80% of the sample was in the subgroup with the smallest average entry fees (roughly $14 or below) and smallest numbers of entries (roughly 200 or under). In this presentation, we will highlight differences between the subgroups, and then show ways we used the partitioning to draw conclusions about the sample and the population it was drawn from.

**Решение:** -1 эссе о спортивных ставках в Аргентине

---

### 48 · R0890

**Gender-specific risk factors for gambling-related suicidal ideation: Evidence from a help-seeking population**

2026 · Addictive Behaviors · article · en · https://doi.org/10.1016/j.addbeh.2026.108616

• Gambling-related suicidal ideation is prevalent amongst help-seekers. • Factors impacting the risk of gambling-related suicidal ideation differ across genders. • Gambling-related debt and lack of social support are risk factors for both genders. • At-risk alcohol consumption is a risk factor amongst women who gamble. • Help-seekers experience most harm from fast online gambling products. People suffering from gambling problems are at a heightened risk of suicidal behaviours and ideations. Emerging evidence suggests that gambling-related suicidality may be more common amongst women, those with gambling-related debt and those gambling with fast-paced products such as electronic gambling machines. This study aims to investigate associations between gambling-related suicidal ideations and risk factors using logistic regression analysis. The analyses are conducted separately for women and men. The data consisted of questionnaire responses from 2,800 help-seekers (1,746 men, 1,054 women), who enrolled in a Finnish online help service for gambling problems during 2019–2024. The survey focused on the following questionnaire measures: self-reported suicidal ideation (MARDS), problematic gambling products, gambling-related debt, at-risk alcohol use (AUDIT-C), problem gambling (NODS) and social support. 19.8 percent of all respondents reported suicidal ideation (25.5% of women, 16.4% of men). Both genders reported online EGMs, online casino products and land-based EGMs as causing most harm. However, we found no statistically significant associations between gambling products and suicidal ideation. Gambling-related debt was a significant risk factor for suicidal ideation for both genders. At-risk alcohol use was a risk factor for suicidality amongst women. Lack of social support was a risk factor for both genders. In conclusion, we found that risk factors for gambling-related suicidal ideation can differ across genders. Gambling-related debt can increase the risk of suicidality for both genders. Policy action is needed to prevent significant financial harm from gambling.

**Решение:** -5 выборка пациентов клиники лечения лудомании

---

### 49 · R8077

**A study of sports lottery knowing and purchase psychology based on SPA**

2005 · Journal of Zhejiang Normal University · review, article · en

A study of sports lottery and purchase psychology was conducted in the form of literature review and questionnaire in ten cities like Beijing, Shanghai, etc and in Zhejiang Normal University. The analysis of the data collected at random indicated that the subjects did not have adequate theoretical knowing of sport lottery as a whole and that their purposes of purchasing were combination of winning a prize and concerning about sports games. Therefore, moderate prize helps enhance the interest of buying lotteries, and meanwhile, it is necessary to promote and popularize the basic knowledge of sports lottery.

**Решение:** -2 статистическое выявление договорных матчей

---

### 50 · R6864

**Pathways to problem gambling: A summary of research from 2010-2012**

2012 · article · en

This study is a meta-analysis on the results of eight projects undertaken by the first author and his research team in Hong Kong and Macau. The purpose of the present meta-analysis was to understand the pathways development of recreational and problem gambling. These eight research projects were all qualitative studies on different groups of active gamblers, which included day-traders (N=16), elderly gamblers in public housing estates (N=25), working class women (N=15), young gamblers primarily interested in soccer-betting (N= 18), a group of gamblers with criminal background (N=11), female sex workers (N=20), male sex workers and taxi drivers (N=20) and working adults (N=20). All the participants were clinically interviewed by the first author, who is an experienced clinical psychologist or his assistants. The interviews were structured on the Diagnostic and Statistical Manual 4th edition, text revision (American Psychiatric Association, 2000). The questions covered the participant? developmental history, his/her recollections on the acquisition and maintenance of the gambling habits, his career and family development and the current state of gambling. In addition, personality tests and the Problem Gambling Severity Index ((Ferris & Wayne, 2001) will be given to the participants in order to assess their personality and gambling involvement. Results indicated that 25% of the participants can be classified as pathological gamblers. Most of the pathological gamblers came from the groups of sex workers and gamblers with criminal background. Further analysis on the participants? Background and history and their trajectory of gambling development demonstrate that the pathways development of problem gambling does not follow a linear model, whereby problem gambling is always preceded by recreational gambling. The current study clearly indicates that the basic differences between recreational and problem gambling are more qualitative than quantitative. When compared to recreational gamblers, pathological gamblers were found to have significant deficits in impulse control, which resulted in frequent chasing of losses, the preoccupation of gambling and the failure to pursue a law-abiding lifestyle. Further, most of the pathological gamblers show a general lack of adequate moral development. While the current study supports the claims of Volberg (2002) and Blaszczynski and Nower (2002) model, it proposes a new model that focuses the subjective experiences of gambling and the influences of one? work and social environment.

**Решение:** + опрос активных игроков, футбольные беттеры, DSM-IV и PGSI

---

### 51 · R1209

**OPTIMIZING STATE REVENUE THROUGH REGULATORY REFORM IN VIETNAM’S GAMING AND LOTTERY SECTOR**

2026 · Acta Innovations · article · https://doi.org/10.62441/actainnovations.vi.818

This article examines the determinants of state budget revenue from the prize-winning gaming sector in Vietnam, which encompasses traditional and computerized lotteries, casinos, sports betting, and electronic games for foreigners. As emerging markets actively seek to diversify their fiscal streams, the gaming sector presents a significant yet complex opportunity. Historically dominated by traditional lotteries, the Vietnamese gaming market has undergone a structural transformation toward controlled liberalization, designed to capture capital that previously flowed to informal markets. Utilizing a provincial panel data approach, this study analyzes how regulatory shifts and economic factors influence tax receipts across 63 provinces over the period from 2015 to 2025. The empirical analysis employs both Fixed Effects (FE) and Random Effects (RE) models to test the impact of specific drivers, including gross regional domestic product (GRDP), regulatory changes, and geographic market competition. The results provide strong evidence that income elasticity is a primary driver of sector growth, with a 1% increase in GRDP per capita associated with a 0.654% increase in gaming revenue within the preferred Fixed Effects model. Furthermore, regulatory liberalization, such as the introduction of modern lottery formats and casino pilots, yields a quantifiable fiscal benefit by increasing localized revenue. Conversely, increased geographic competition negatively impacts provincial gaming revenue, causing revenue attrition. Ultimately, optimizing state revenue requires a delicate balance between market liberalization and social cost management. The study concludes by proposing strategic policy recommendations, including product diversification, harmonized tax structures, geographic zoning optimization, and digital framework integration, to enhance long-term fiscal yields.

**Решение:** -1 социологическая книга о спортивном беттинге

---

### 52 · R6420

**A Study on Structural Relationship among Motivation of Viewing, Taekwondo Image,Taekwondo Identification and Taekwondo Loyalty in the Audience of 2013 World Taekwondo Grand Prix Final**

2014 · Journal of Sport and Leisure Studies · article · en · https://doi.org/10.51979/kssls.2014.08.57.407

The purpose of this study is to examine structural correlation among motivation of viewing, Taekwondo image, Taekwondo identification and Taekwondo loyalty in the audience of 2013 World Taekwondo Grand Prix Final. To attain the goal of this paper, among the audience of ``2013 World Taekwondo Grand Prix Final``, 350 persons who were high school students or older were selected as the subjects of this study, and then, a survey was conducted to them. For sampling, the convenience sampling method was employed, and for responding to the questionnaire, self-administration was used. Among the questionnaire sheets collected, 28 sheets that had been answered unfaithfully, responded omissively, answered duplicatively, or responded unreliably in general were excluded from the subjects of analysis, and then, the rest 322 sheets usable for the analysis were finally selected as valid samples. For data processing, both PASW 18.0 and AMOS 18.0 were utilized to investigate the goodness-of-fit of the model through confirmatory factor analysis, reliability analysis, correlation analysis, and structural equation model analysis and then verify each individual hypothesis. Based on the hypotheses, the study has drawn the following results: first of all, eustress and group affiliation, the subfactors of motivation of viewing, were had a positive effects on their Taekwondo image, but betting on sport had a negative effects on their Taekwondo image, and both aesthetics and vicarious achievement had no significant effects on Taekwondo image. Second, Taekwondo image had a positive effects on Taekwondo identification. Third, Taekwondo image had a positive effects on Taekwondo loyalty. Lastly, Taekwondo identification had a positive effects on Taekwondo loyalty.

**Решение:** -3 анализ сообщений на форуме беттеров без инструмента PG

---

### 53 · R8286

**Informationseffizienz im Markt für Sportwetten: Der österreichische Markt für Online-Fußballwetten**

2001 · Institutional Repository (IHS Vienna) · report

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 статья о манипулировании спортивными результатами

---

### 54 · R6464

**Risk Regulation and Behaviour among Consumers of Alcohol, Drugs and Nicotine**

2014 · European Journal of Risk Regulation · https://doi.org/10.1017/s1867299x00003913

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -2 математическая вероятность выигрыша в лотерею

---

### 55 · R4779

**Weapons sales**

2019 · ABC-Clio · part of book or chapter of book · eng · https://hdl.handle.net/10807/134728

While many international corporations have benefited from the global economy and distribution of information, globalization has also had serious negative consequences. This important reference work offers students and general readers a critical understanding of how technology, governments, political unrest, war, and economic strife contribute to an increase in global crime. This A–Z encyclopedia covers key people, events, and organizations and includes key documents that will help readers to understand the numerous problems created by the many transnational crimes that are growing in severity and frequency around the world. Entries address perpetrators and their methods; victims; who really profits; and law enforcement responses. In addition to cyber theft and sales of weapons and narcotics, the set provides a detailed look at global crimes not typically covered, such as corruption, fraudulent medicine, illegal sports betting, organ trafficking, maritime piracy, trafficking in cultural property, and wildlife and forest crime. Although some historical events and people are included, the focus is on recent and contemporary topics.

**Решение:** -7 спам tipster сервиса на Zenodo

---

### 56 · R0006

**Deportes y prácticas democráticas en América Latina**

2026 · Memoria Académica (Facultad de Humanidades y Ciencias de la Educación, Universidad Nacional de La Plata) · book · es

Tabla de contenidos: Prólogo / Wanderley Marchi Júnior. Prácticas deportivas y sociedad: claves para su comprensión en las coyunturas regionales / Jorge Ricardo Saraví, Alejo Levoratti, Débora Paola Di Domizio, Daniela Negri. Acceso democrático al deporte y al ejercicio físico: la desigualdad social como barrera / Renato Francisco Rodrigues Marques. Ensamblajes socioecológicos para analizar políticas públicas de educación, deporte y salud de una manera "más que humana" / Rodrigo Soto-Lagos. El fútbol como territorio de luchas colectivas / Verónica Moreira. Desmontando la ceguera formativa del deporte. El papel de la educación deportiva física escolar / Mariana Sarni. El deporte en la formación superior: de objeto-cosa a objeto-multidimensional situado / Osvaldo Omar Ron. Políticas públicas en los países de América Latina: convergencias y divergencias / Fernando Augusto Starepravo. Deportes, prácticas democráticas y sociedad en México / Oswaldo Gurrola. Enfoque de investigación en las prácticas y subjetividad deportiva / Gabriel Armando Cachorro. Miradas antropológicas sobre los deportes y las prácticas deportivas en Brasil / Mariane da Silva Pisani. Educación física, identidades transgénero, intersexual y no binaria en los deportes / Lorena Irene Berdula. El deporte y la competencia deportiva como arena pública. Anotaciones para el debate sobre la relación deporte, competencia y ética / Liber Benítez. Entre la investigación y la extensión. Debates emergentes en los estudios sociales del deporte / Julia Hang. Apuntes para pensarlos diálogos entre universidad-territorio-feminismo en Uruguay: el caso del fútbol femenino / Martina Pastorino. Deporte y literatura: líneas de fuga para la resistencia y subversión de los cuerpos / Daniel Zambaglione. La investigación como recurso para desvelar y aprender sobre nuestra sociedad en la relación entre el deporte, los medios de comunicación y las tecnologías / Cristiano Mezzaroba. Diversión, riesgo y dinero: jóvenes y apuestas deportivas on line en Argentina / Juan Branz. ¿Tecnologías para qué? / Nemesia Hijós. El deporte en la Red Social Global: perspectivas del Sur y el compromiso de la Sociología Pública / Billy Graeff. Deporte y progresismo en el Uruguay. Entre las políticas de alto rendimiento y los deportistas clasificados a Tokio 2020+1 / Bruno Mora. Producción y trasmisión de conocimientos en los estudios sociales del deporte. Enfoques, saberes, instituciones y especialistas / Pablo Scharagrodsky..

**Решение:** ? опрос финансового риска инвесторов и беттеров, проверить PGSI

---

### 57 · R7585

**Educational Administration and History: The State of the Field**

2009

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? опрос игроков на Prolific, PGSI и транзакции, проверить спорт

---

### 58 · R1042

**Constructing Mediated Betting Discourse: A Typology of Responsible Gambling Language Identified Through ESPN's Sports Wagering Shows.**

2026 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-025-10437-4

Media play an integral part in the presentation of information surrounding gambling, and thus, it is important to consider the sharing of such details to inform and educate about suggested participation in sports wagering. This study analyzes discourse during ESPN's dedicated sports betting program, ESPN Bet Live (formerly Daily Wager), to produce a typology of responsible mediated gambling language offered by on-air talent and through visual graphics to an active gambling audience. Analysis of 45 episodes aired during the men's and women's NCAA basketball tournaments between 2021 and 2024 revealed four broad categories- announcer transparency, bet certainty, bookmaking education, and investment terminology- and four distinct types of evidence- X's & O's, traditional statistics, betting statistics, and non-scientific. Announcers rarely communicated specific responsible gambling recommendations but offered justification primarily through analysis of game play and traditional statistics. As media coverage of sports betting hurdles beyond journalistic responsibility of reporting scandals to the integration of gambling information and recommendations, it is incumbent upon sports media to present wagering information in a responsible manner.

**Решение:** ? опрос корейских спортсменов о ставках, проверить шкалу PG

---

### 59 · R5377

**Young men’s gambling : the influence of socio-cultural and marketing factors**

2017 · Figshare · dissertation · en

This study explored the influence of socio-cultural and marketing factors on young men's sports betting attitudes and behaviours. The findings show a range of factors that appear to significantly influence the way gambling has become part of the normal practices associated with sport for young men and their peers.

**Решение:** -6 книга о современной легкой атлетике

---

### 60 · R1262

**Integrity at Stake: Statistical Detection of Anomalous In-Play Betting in Football**

2026 · arXiv (Cornell University) · article, preprint, preprint/article · und · https://doi.org/10.48550/arxiv.2605.30209

Match-fixing undermines the integrity of sport by eroding public trust and threatening the financial sustainability of clubs and leagues. The expansion of sports betting markets has created new incentives and opportunities for manipulation, calling for rigorous, data-driven monitoring tools. Football, which accounts for the largest share of global betting turnover, remains particularly exposed: integrity reports continue to flag several suspicious matches, with past scandals in Italy and Turkey underlining the problem's persistence. This study uses high-frequency in-play (live) betting data from the Italian Serie B (seasons 2018/19--2020/21) to explore statistical approaches for detecting unusual betting behaviour. A state-space modelling framework is employed to describe standard betting market dynamics and to predict expected betting volumes conditional on match characteristics. Deviations from these expectations can then be analysed using outlier detection techniques to identify potentially suspicious betting activities. The results demonstrate how statistical modelling can contribute to the early identification of unusual betting patterns, thereby supporting integrity assurance in in-play sports betting markets.

**Решение:** -1 анализ запрета онлайн-ставок в Бразилии

---

### 61 · R6481

**Gambling and Problem Gambling in the United States: Changes Between 1999 and 2013**

2014 · Journal of Gambling Studies · article · en · https://doi.org/10.1007/s10899-014-9471-4

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** + национальный опрос США 1999 и 2013, DIS-IV / SOGS, ставки на спорт

---

### 62 · R1921

**Sports Betting**

2025 · Routledge eBooks · book, monograph · en · https://doi.org/10.4324/9781003479918

This is the first book to focus on sports betting from a sociological perspective. Drawing on multi-stage sociological research, it deepens our understanding of an increasingly significant aspect of the contemporary sport industry. The book examines how bettors engage in sports betting – why they perceive it to be attractive, what betting represents to them and how they know how to bet or how they do so – describing the social phenomenon of betting and placing it within a broader cultural context. Drawing on original empirical research, it uses a practice theory that makes it possible to see in the actions of individuals both the influence of and the impact they have on culture, lifestyle and technology. With sports betting an increasingly controversial subject in wider society, this analysis helps us to understand betting as a complex phenomenon with connections to other areas of social life and how to better understand its impacts and how to mitigate its potential social harms. This is a fascinating read for anyone with an interest in the sociology of sport, sport business, economy, psychology, gambling, sociology, cultural studies, social anthropology or social policy.

**Решение:** -2 математическое моделирование фэнтези-крикета

---

### 63 · R7286

**Message Boards and the Fantasy Sport Experience**

2011 · International Journal of Sport Communication · article · en · https://doi.org/10.1123/ijsc.4.2.233

Fantasy sport joins competition, sport knowledge, and socialization into one interactive sport activity. This research specifically focuses on the socialization aspects of the activity. This analysis addresses overall satisfaction in fantasy sport, future intentions to return to the activity, and reasons why fantasy sport users (FSUs) do or do not use message boards. Data were collected from 322 FSUs in a questionnaire format using quantitative-scale items and qualitative open-ended questions. The results indicate 62.1% (n = 200) of the sample using message boards in their fantasy sport experience. Reasons for their use were based on the themes of logistical conversation, socializing, surveillance, and advice or opinion. FSUs chose not to use message boards for reasons based on no interest, information, time, and alternative options. Other results indicate that those using message boards have higher overall satisfaction and future use intentions than those not using message boards. This suggests that message boards enhance the fantasy sport experience.

**Решение:** -2 арбитраж на рынках спортивных ставок

---

### 64 · R1156

**A REGULAMENTAÇÃO DAS APOSTAS ESPORTIVAS E O RISCO DE MANIPULAÇÃO DE PARTIDAS DE FUTEBOL NO BRASIL**

2026 · Revista Tópicos. · article, journal-article · und · https://doi.org/10.70773/revistatopicos/784328851

A significativa ampliação do número de apostas esportivas no Brasil, ocasionada pelas plataformas digitais, tem revelado riscos à integridade das competições e à segurança da atividade. A possibilidade de manipulação em partidas de futebol e a atuação de organizações criminosas expõem fragilidades no atual modelo regulatório. Portanto, este estudo tem por objetivo analisar os desafios jurídicos e institucionais atinentes à regulação da atividade de apostas esportivas no Brasil, considerando, sobretudo, os riscos concretos de manipulação de resultados e corrupção desportiva. A metodologia adotada é de natureza qualitativa, exploratória e teórico-dogmática, com base em análise bibliográfica. Os resultados indicam a existência de um arcabouço normativo incipiente, marcado pela ausência de tipificação penal específica, pela fragilidade institucional na fiscalização das casas de apostas e pela carência de integração entre os órgãos reguladores. Verificou-se que os mecanismos atuais de repressão são insuficientes para enfrentar supostos esquemas de manipulação de resultados, exigindo um modelo de governança mais estruturado, preventivo e aparelhado. Também foi possível constatar a necessidade de adoção de medidas como educação preventiva, auditorias, compliance esportivo e cooperação internacional. Conclui-se que a regulamentação das apostas esportivas depende da articulação entre legislação, fiscalização e políticas públicas integradas, a fim de proteger a integridade do esporte e a confiança da sociedade no sistema.

**Решение:** -2 моделирование эффективности ставок на бейсбол

---

### 65 · R5954

**关于“七星彩”中奖问题的一点探讨**

2016 · 中学数学杂志：高中版 · article · zh

最近搬人新居后，发现小区门外有一个中国体育彩票的销售站．笔者在闲暇之余，也偶尔买几注“七星彩”彩票．因为笔者是学数学的，清楚其中的一些概率问题，所以，买彩票仅仅是玩玩而已，并不希望中什么大奖．但是，买一注“七星彩”彩票，中奖的概率到底有多大？这是一个纯数学问题，引起了笔者的兴趣．于是，在网上详细查阅了中奖规定后，做了一点探讨．

**Решение:** -1 анализ регуляторной политики гемблинга в армии США

---

### 66 · R5596

**PREMIUM betting tips predictions subscription**

2017 · html · article · en

On this page you buy premium subscription for sports betting tips, football, soccer, basketball and other sports.

**Решение:** + опрос 4989 индийских студентов, ставки на крикет/футбол, SOGS-RA

---

### 67 · R0713

**Balancing harm prevention and liberty preservation when implementing financial risk assessments for gambling in the United Kingdom: Insights from open banking data**

2026 · Addiction · article · en · https://doi.org/10.1111/add.70513

BACKGROUND AND AIMS: The United Kingdom (UK) and Dutch governments have recently implemented mandatory financial risk (affordability) assessments for online gambling as a harm prevention measure. Assessments should trigger at a level of gambling expenditure that strikes a balance between harm prevention (most at-risk consumers should surpass the threshold) and liberty preservation (most no-/lower-risk consumers should gamble below it), yet little empirical research exists to guide threshold setting. We aimed to demonstrate how research can inform the harm-prevention, liberty-preservation trade-off in this context and evaluate the UK's proposed implementation of financial risk assessments. DESIGN, SETTING AND PARTICIPANTS: We reanalysed a dataset that combines self-reported Problem Gambling Severity Index (PGSI) scores and open banking data from consumers who gamble (n = 424) to (1) simulate the impact of the UK's rolling 30-day £150 net-deposit (deposits minus withdrawals) threshold for financial risk assessments, and (2) identify optimal threshold values for these assessments under different circumstances. Participants were UK residents who had gambled in the past year, recruited via Prolific in April 2024. MEASUREMENTS: Participants completed a survey containing the PGSI and agreed to provide their past 12 months' banking records. FINDINGS: Over 12 months, two-thirds of at-risk (PGSI ≥1) and nearly half of no-/lower-risk participants crossed the UK's £150 threshold [area under the curve = 0.66, 95% confidence intervals (CIs) = 0.62-0.71], demonstrating a greater emphasis on harm prevention over liberty preservation. Increasing the value to £186.9 (95% CIs = £69.5-£401.7) slightly improved this balance, although £150 remained within the range of appropriate values. Optimising for harm prevention in our sample required lowering the threshold to £39.0 (95% CIs = £29.6-£58.8), while emphasising liberty preservation increased it to £716.5 (95% CIs = £508.5-£990.9). We found that using a more conservative definition of risk (≥2 PGSI harms) resulted in higher thresholds, and lower thresholds may be appropriate for younger adults (<30 years). Finally, our findings suggest that thresholds based on spending with all operators-rather than single operators as implemented in the UK-may be better able to differentiate at-risk from no-/lower-risk consumers, although the added benefit of this approach in our sample was marginal and further research is needed to confirm its value. CONCLUSIONS: The United Kingdom's £150 net-deposit threshold for financial risk assessments for online gambling may place more emphasis on harm prevention than liberty preservation. This study provides a methodological template for guiding the implementation of financial risk assessments for online gambling. Because our sample is not representative of the broader UK gambling population, our specific threshold estimates should be treated as provisional.

**Решение:** -3 опрос сотрудников об этике и соблюдении правил

---

### 68 · R5473

**The Actual Conditions and Task on Illegal Sport Gambling of the Korean School Elite Sports Athletes**

2017 · Korean Society for the Sociology of Sport · article, journal-article · en · https://doi.org/10.22173/jksss.2017.30.2.83

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -2 обучение с подкреплением в ставках на спорт

---

### 69 · R7597

**Contemporary athletics compendium**

2009 · Medical Entomology and Zoology · book · en

Preface Wrestling with Herpes: A Case Study Can Spectators' Mood be Manipulated & Maintained in a Losing Game?: Interaction Between Team Identification & Pre-Game Mood Why College Athletes Play Through Pain During Competition A Description & Comparison of Duties & Responsibilities of NCAA Division II Head Baseball & Football Coaches Identity Foreclosure? A Preliminary Investigation of Self-Complexity in Sport Risk Management Strategies at Division I Intercollegiate Football Stadiums: Do Spectators Perceive They Are Protected Against Terrorism? The Positive Relationship Between Sport Team Identification & Social Psychological Well-Being: Identification with Favorite Teams The Positive Relationship between Sport Team Identification & Social Psychological Well-being: Identification with Favorite Teams Versus Local Teams For Love of the Game: The Mediating Potential of Job Satisfaction of College Coaches Upon Career Satisfaction Steroids in Interscholastic Athletics: Does Reasonable Suspicion Exist? In Demand? Examining Sport Management Faculty Openings & Hires The Importance of Parent Physical Activity Levels & Their Expectations for Their Children's Health: A Path Analysis Negligent Marketing: What all Sport Marketers Should Know Investigating Fantasy Sport Participation Among College Students A Look at Academic Reform, Student Athlete Compensation & the Case for a New Classification of Student-Athlete Motivational Profiles of Sport Fans Attending Different Levels of Baseball Games Characteristics of Success in Men's Football & Men's Basketball at the Division I Level Alternative Dispute Resolution in Sport: A Conceptual Approach Just Not on My Turf: Student-Athletes' Perceptions of Homosexuality Identification with Multiple Sporting Teams: How Many Teams Do Sport Fans Follow? Motivations of International Student-Athletes to Participate in Intercollegiate Athletics Fundraising Responsibilities & Expectations of NCAA Division II Head Baseball & Football Coaches Athletic Administrators Perceptions of Work-Life Balance Policies: A Divisional Comparison The Impact of Playing Position on Perceptions of Horizontal Interpersonal Power in Sport Stress Factors in the Profession of Coaching: Assess Their Nature, Scope & Impact New Technology Holds Promise for the Future Application of Psychophysiological Methods for the Enhancement of Performance During Sport & Exercise Index.

**Решение:** -2 эффективность линий ставок на студенческий баскетбол

---

### 70 · R0624

**Brazil&amp;#39;s Ban On Online Betting And The Income That Does Not Return To The Market**

2026 · Elsevier BV · posted-content, preprint · https://doi.org/10.2139/ssrn.7529824

On 25 September 2026, Provisional Measure No. 1,394 prohibited the exploitation, offering and advertising of fixed-odds betting in Brazil, ending a regulated market that had operated since January 2025. This essay sets aside the polarised debate between economic freedom and public health to ask a prior, economic question: what happens to household income when it stops circulating through commerce, industry and services and begins to flow to betting platforms? Drawing on official data from the Central Bank of Brazil and the Ministry of Finance, and on estimates by the Celso Furtado Centre, the University of São Paulo's Made research centre, the National Confederation of Commerce and the Institute for Health Policy Studies, it distinguishes gross wagers from households' net loss, places that loss between a floor of roughly R$ 35 billion and a ceiling of R$ 62.5 billion for 2025, and traces where the retained revenue goes: modest tax collection, negligible formal employment, and profits that may be remitted abroad. It then confronts the classic 'mere transfer' objection of gambling economics and argues that, given the asymmetry of multipliers, the compromised nature of the bettor's choice and the externalities borne by third parties, the transfer is not neutral. The essay closes by examining the legal risks of the ban, including migration to illegal markets, compensation claims and the constitutional regime of provisional measures, and concludes that the measure's success will depend less on its text than on the State's capacity to prevent that income from merely changing address.

**Решение:** -1 правовой анализ ставок на футбол в Бразилии

---

### 71 · R3459

**Data Science Approach to predict the winning Fantasy Cricket Team Dream 11 Fantasy Sports**

2022 · arXiv (Cornell University) · article, preprint, journalarticle · en · https://doi.org/10.48550/arxiv.2209.06999

— The evolution of digital technology and the increasing popularity of sports inspired the innovators to take the experience of users with a proclivity towards sports to a whole new different level, by introducing Fantasy Sports Platforms (FSPs). The application of Data Science and Analytics is Ubiquitous in the Modern World. Data Science and Analytics opens doors to gain a deeper understanding and helps in the decision making process. We firmly believed that we could adopt Data Science to predict the winning fantasy cricket team on the FSP, Dream-11. We built a predictive model that predicts the performance of players in a prospective game. We used a combination of Greedy and Knapsack Algorithms to prescribe the combination of 11 players to create a fantasy cricket team that has the most significant statistical odds of finishing as the strongest team—thereby giving us a higher chance of winning the pot of bets on the Dream-11 FSP. We used PyCaret Python Library to help us understand and adopt the best Regressor Algorithm for our problem statement to make precise predictions. Further, we used Plotly Python Library to give us visual insights on the team, and player’s performances by accounting for the statistical, and subjective factors of a prospective game. The interactive plots help us to bolster the recommendations of our predictive model. You either win big, win small or lose your bet based on the performance of the player’s selected for your fantasy team in the prospective game, and our model increases the probability of you winning big.

**Решение:** ? опрос жителей Луизианы о гемблинге, проверить инструмент PG

---

### 72 · R5297

**Arbitrage**

2018 · World Scientific series in finance · book-chapter · en · https://doi.org/10.1142/9789813278790_0002

Arbitrage in its pure form is to construct a sure bet so that no matter the outcome, you either break even or turn a profit. Most observers say that arbitrage does not exist but actually it does in many instances because there are different financial markets for the same sports betting or financial security situation. This is because different people have different sets of information and beliefs. Let’s take the simplest case: either A or B wins. Let Oah be the odds given on the event that A wins from betting source h and Obi that for B winning from betting source i. With these UK odds, the odds are the total return per 1 unit bet. In comparison, US odds are UK odds −1 and their payoffs are US odds +1 = UK odds…

**Решение:** -2 математическая модель маржи букмекера

---

### 73 · R6681

**Testing efficiency in the major league of baseball sports betting market**

2013 · article · en

This paper describes how for a range of betting tactics the sports betting market of the major league of baseball is quite ecient and that on the long term almost no abnormal returns can be made. It shows that there is no underestimation present of the home eld or underdog chances as proven in papers on other sports betting markets. New methods, using minimum margins and weighting methods also do not result in abnormal returns. Also when using a probit model using readily available data no abnormal returns are found. Except when the Money Lines of bookmakers are included in the model. Using this a small prot can be made.

**Решение:** -1 глава книги о маркетинге и рекламе ставок

---

### 74 · R1427

**THE PROBLEM OF GAMING ADDICTION AMONG MILITARY PERSONNEL**

2025 · Научное мнение · article, journalarticle · und · https://doi.org/10.25807/22224378_2025_11_108

This article analyses the problem of gambling addiction, the historical aspects of its origins, the mechanisms of pathological gambling addiction, including its various stages and manifestations, and highlights the consequences of harmful gambling, particularly sports betting. The problem of gambling addiction among military personnel is specifically examined, and key prevention strategies are outlined.

**Решение:** -6 история бейсбола в США

---

### 75 · R8259

**Prospects of fantasy sports as a profitable sport marketing media [sic]**

2002 · dissertation · en

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -2 прогнозирование результатов матчей АПЛ

---

### 76 · R3018

**Statistics**

2023 · Chapman & Hall/CRC eBooks · book-chapter · en · https://doi.org/10.1201/9781003285816-15

Statistics is a branch of mathematics dealing with the collection, tabulation and interpretation of numerical data. There are specialist statistical software packages available such as GraphPad Prism, Minitab, Statistical Analysis Software (SAS), Statistical Package for the Social Sciences (SPSS) and R, for example. This chapter shows the reader how Python can be used to solve a wide range of statistical problems and is also useful in Data Science and Machine Learning. The first section covers simple linear regression and shows the linear relationship between carbon dioxide emissions and gross domestic product in the USA from 2000 to 2020. The second section is concerned with stochastic processes and Markov chains; directed graphs are plotted and convergence to steady states are illustrated with plots. The student&s;s t-test is discussed in the third section, and a simple two-sample t-test is applied to the heights of female and male students in a lecture. The final section introduces powerful Monte-Carlo simulations and a simple example is presented of gambling on a European roulette wheel, where it is clearly demonstrated that casinos and online betting companies always win in the long term, and why none of us should gamble.

**Решение:** -2 модель размещения рекламы букмекеров во время трансляций

---

### 77 · R1218

**Regulación de las apuestas deportivas en la literatura académica: Revisión de los debates más relevantes entre 2014 a 2026**

2026 · Repositorio Institucional (Pontificia Universidad Javeriana) · article · https://doi.org/10.71618/7kt6-jz58

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 регуляторный отчет о ставках в Австралии

---

### 78 · R5445

**Do High School Students in India Gamble? A Study of Problem Gambling and Its Correlates.**

2017 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-016-9651-5

Studies from the West suggest that significant numbers of high school students gamble, despite it being illegal in this age group. To date, there have been no studies on the prevalence of gambling among senior high school and higher secondary school students in India. This study reports point prevalence of gambling and its psychosocial correlates among high school students in the State of Kerala, India. 5043 high school students in the age group 15-19 years, from 73 schools, were selected by cluster random sampling from the district of Ernakulam, Kerala, South India. They completed questionnaires that assessed gambling, substance use, psychological distress, suicidality, and symptoms of Attention Deficit Hyperactivity Disorder (ADHD). Of a total of 4989 completed questionnaires, 1400 (27.9 %) high school students reported to have ever gambled and 353 (7.1 %) were problem gamblers. Of those who had ever gambled, 25.2 % were problem gamblers. Sports betting (betting on cricket and football) was the most popular form of gambling followed by the lottery. Problem gamblers when compared with non-problem gamblers and non-gamblers were significantly more likely to be male, have academic failures, have higher rates of lifetime alcohol and tobacco use, psychological distress, suicidality, history of sexual abuse and higher ADHD symptom scores. Gambling among adolescents in India deserves greater attention, as one in four students who ever gambled was a problem gambler and because of its association with a range of psychosocial variables.

**Решение:** + опрос индийских подростков, ставки на спорт, SOGS-RA

---

### 79 · R0845

**Frontline Employees and Responsible Gambling: How Internal Communication Shapes Compliance with RG Rules.**

2026 · Journal of gambling studies · journal article, article · eng · https://doi.org/10.1007/s10899-026-10501-7

Responsible gambling (RG) has become a core compliance expectation for gambling operators, yet little is known about frontline employees’ compliance with RG rules in morally tense contexts. Drawing on social information processing theory, this study examines how company-to-employee RG communication about internal RG policies and procedures relates to employees’ compliance with RG rules. Specifically, it focuses on two forms of RG communication: company-issued RG reports and company-provided RG training. Data were collected using a questionnaire from 844 employees working at sports lottery outlets operated by a provincial company in Southwest China (48.5% male), and were analyzed using structural equation modeling with bootstrapped tests of indirect effects. The results show that greater awareness of the company’s RG report is associated with higher compliance with RG rules among employees (β = 0.194, p < 0.001), and more frequent RG training is also associated with higher compliance (β = 0.326, p < 0.001). Employees’ judgment about RG mediates the effects of both report awareness and training on compliance. Contrary to our expectations, RG communication is associated with lower moral disengagement, and in turn predicts better compliance. The indirect effects through moral disengagement are therefore positive. These findings suggest that clear and frequent communication about RG can support large-scale improvements in compliance among frontline staff.

**Решение:** -3 опрос мотивов ставок среди футбольных фанатов без PG

---

### 80 · R1059

**Desenvolupament d'un Sistema de Predicció Esportiva Basat en Reinforcement Learning amb Visualització Web**

2026 · Dipòsit Digital de Documents de la UAB (Universitat Autònoma de Barcelona) · dissertation · ca

Plataforma web per a la predicció del rendiment de jugadors de La Liga orientada a fantasy football. El sistema integra un backend desenvolupat amb Django, una aplicació SPA en React i un model de predicció basat en Double Q-Learning implementat amb TensorFlow. L’arquitectura combina una base de dades SQLite amb fitxers CSV per a la gestió i enriquiment de dades. La plataforma permet generar prediccions de rendiment, comparatives entre jugadors i la creació d’equips òptims per jornada, oferint una eina interactiva i orientada a la presa de decisions en fantasy sports.

**Решение:** -2 анализ коэффициентов на теннисные матчи

---

### 81 · R6645

**INFORMATION AND IDIOSYNCRATIC RISK IN THE NCAA MEN’S BASKETBALL BETTING MARKET**

2013 · The Journal of Gambling Business and Economics · journal-article · https://doi.org/10.5750/jgbe.v5i3.572

Betting lines and scores from the 2009/10 college basketball season for 169 mid-major and major colleges are used to verify the efficiency hypothesis for the betting-market analogy to the CAPM-based market model. As in that model, the portion of the variance in the spreads that is unexplained by the betting lines is the idiosyncratic risk associated with a team’s games. The paper shows that this risk is due to team-specific and conference-specific informational and consistency-of-play factors that impact bettors’ decisions.

**Решение:** -1 правовой обзор легализации ставок в США после PASPA

---

### 82 · R7184

**On the Soccer Gambling's Judicial Application and Legislation**

2011

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -2 машинное обучение для прогнозирования исходов матчей НБА

---

### 83 · R4569

**Louisiana Survey 2019**

2019 · Civil War Book Review · article

The 2019 Louisiana Survey is the eighteenth in an annual series sponsored by the Reilly Center for Media & Public Affairs at Louisiana State University’s Manship School of Mass Communication. The mission of the Louisiana Survey is to establish benchmarks as well as to capture change in residents’ assessments of state government services. The survey is further dedicated to tracking public opinion on the contemporary policy issues that face the state. Each iteration of the Louisiana Survey contains core items designed to serve as barometers of public sentiment, including assessments of whether the state is heading in the right direction or wrong direction, perceptions about the most important problems facing the state, as well as evaluations of public revenue sources and spending priorities. In the 2019 Louisiana Survey, this core is supplemented by measures of support for compromise; support for increases in teacher pay, the minimum wage, and the gasoline tax; approval of major recent policy developments such as criminal justice reform and Medicaid expansion; and attitudes toward a number of social issues such as gun policy, marijuana legalization, and sports gambling. As part of an effort to ensure that the Louisiana Survey fulfills its public service mission, the research team solicited input about topics for the survey from members of the government and policy community across the political spectrum. Additionally, the research team drew upon expertise in public policy and polling from Louisiana State University faculty. These advisors provided invaluable insight into the design of the questionnaire and in identifying the contemporary policy questions that could most benefit from an understanding of the public’s views. While we are indebted to them for their time and contributions, they bear no responsibility for final decisions on the questionnaire, analysis, and interpretation presented in this report or any mistakes therein.

**Решение:** -6 физическая культура и спорт в школе

---

### 84 · R5052

**La peu glorieuse incertitude du parieur sportif**

2018 · INRIA a CCSD electronic archive server · article · fr

National audience

**Решение:** -2 моделирование рынков ставок на скачки и спорт

---

### 85 · R2431

**The second national study of interactive gambling in Australia (2019-20)**

2024 · CQUniversity · report, report/report · und · https://doi.org/10.25946/27139554

This study was commissioned by Gambling Research Australia to examine changes in interactive gambling since the first national Interactive Gambling Study (Hing et al., 2014a). The multi-stage study included: a literature review; environmental scan; National Telephone Survey (N = 15,000); National Online Survey of gamblers (N = 5,019); Longitudinal Cohort Study of respondents to both the 2012 and 2019 National Online Surveys (N = 437); interviews with 49 online gamblers; and compilation of gambling help service data. Only the National Telephone Survey was representative to the extent that it was weighted to standard population variables; all other samples were non-representative. Interactive gamblers were defined as adults (aged 18 years or over) who gambled with money or cryptocurrency online at least once in the past year, not excluding other modes of gambling, but excluding free play activities. The results of this study should be interpreted in accordance with the study’s limitations. These limitations are briefly summarised in this Abstract, with further details in the Executive Summary and the Discussion chapter. Based on the National Telephone Survey, the estimated prevalence of interactive gambling has doubled from 8.1 per cent in 2010/11 to 17.5 per cent in 2019. Estimates are highest for forms that can be legally provided – lotteries (10.1%), race betting (5.9%) and sports betting (5.8%). Nearly one-in-three gamblers (30.7%) were estimated to gamble online in 2019 compared to one-in-eight (12.6%) in 2010/11. Interactive gamblers are more likely to be male, younger, more educated and in a de facto relationship, have higher problem gambling scores, and gamble on more forms. In the non-representative National Online Survey, 47.1 per cent of interactive gamblers had used an illegal offshore gambling site in 2019, most commonly to gamble on instant scratch tickets (26.3%), EGMs (15.8%), casino games (15.7%), poker (15.0%), bingo (13.9%) and skin gambling (9.0%). Awareness of the illegality of offshore sites was low in this sample. Problem gambling amongst offshore bettors on sports, racing, novelty events, esports or daily fantasy sports (38.5%) was over three times higher than for non-offshore bettors (11.4%) in this sample. Offshore bettors reported placing about one-third of their bets offshore. Two-fifths of sports bettors (41.9%) placed in-play bets. Problem gambling amongst in-play bettors (33.8%) was nearly four times higher than non-in-play bettors (9.1%) in this sample. About half of in-play bets were reported to be placed on offshore sites. Based on the National Telephone Survey, gambling participation (all modes) has decreased from 64.3 per cent in 2010/11 to an estimated 56.9 per cent in 2019. However, there has been a statistically significant increase in problem gambling since 2010/11. The estimated prevalence of problem gambling has doubled from 0.6 per cent to 1.23 per cent in 2019, while estimates of moderate (3.1%) and low (6.6%) risk gambling rates have remained steady. Interactive gamblers are nearly three times more likely than non-interactive gamblers to be problem gamblers and about twice as likely to be at-risk gamblers. However, nearly half of interactive gamblers report that land-based gambling is the most problematic for them. Amongst interactive gamblers, higher problem gambling severity was predicted by being male, never married, of Aboriginal or Torres Strait Islander descent, speaking a non-English language at home, lower mental and physical health, participation in more gambling activities, greater exposure to wagering advertising and inducements, lower wellbeing, higher impulsivity and betting offshore. Based on the National Telephone Survey, an estimated 9.1 per cent of Australian adults reported at least one gambling-related harm to self and 6.0 per cent being harmed by another person’s gambling. Interactive gamblers were significantly more likely to experience at least one harm to self (34.0%) compared to non-interactive gamblers (15.6%). EGMs (27.5%) were reported to be the most harmful form amongst ‘harmed’ interactive gamblers, followed by race betting (17.1%), sports betting (15.3%) or lotteries (13.9%). Those identifying smartphones as their most harmful gambling mode more than doubled from 11.7 per cent in 2010/11 to 25.2 per cent in 2019. The Longitudinal Cohort Study found that the frequency of race betting and sports betting, rather than the proportion of online gambling, was the key driver of changes in harmful gambling over time in this sample. Nonetheless, increased engagement in online betting increases harmful gambling by enabling increased betting frequency. Interviewees highlighted key changes in interactive gambling, including its enhanced speed, convenience and appeal and an expansion of gambling inducements, push marketing, payment mechanisms and new betting options, as well as the banning of successful (less profitable) punters. Those who had soug

**Решение:** + 2-е австралийское исследование интерактивного гемблинга, PGSI по видам

---

### 86 · R8277

**Gambling Against the State: The State and the Legitimation of Gambling**

2001 · Current Sociology · article, journalarticle · en · https://doi.org/10.1177/0011392101495002

Gambling has come to be legitimated in many western countries since the reintroduction of lotteries as methods of revenue generation for the state in the 1960s and 1970s. Since then, state-sanctioned gambling opportunities have expanded to include casino games, sports betting, video lottery terminals, scratch and win games and others as governments seek to increase revenues. The article analyses the state’s role in the legitimation, expansion and marketing of gambling activities, and discusses the major cultural and ideological implications of this development. It argues that this legitimation must be seen in the context of broader social and economic forces related to the deregulation of markets. The legitimation of gambling illustrates the shift in social and economic morality away from the ‘rational’ basis of capitalism in Protestant ethics, and towards the deregulation of economic attitudes. While this shift suggests a further rationalizing of economic activity and attitudes, the analysis of the broader cultural implications illustrates the tension between the rational and irrational forces in late capitalism. The article focuses on developments in western countries, but state-sanctioned gambling is expanding in non-western countries as well.

**Решение:** -3 анализ данных оператора о ставках на спорт без опроса PG

---

### 87 · R6978

**Connection between Addictive Behavior and Investing on the Stock Market in Croatia**

2012 · review

INTRODUCTIONNon-substance addictive behaviour, especially pathological gambling and internet addiction are becoming an increasing interest in research and health policy. Similarities and differences between these addictions and addictions to psychoactive stuff have been the subject of numerous discussions.1 Profession still disputes as whether when we talk about non-substance addiction we talk about real addiction that includes pathophysiological processes at the biological level or we talk about impulse control disorder.2Internet addiction is characterized by excessive or poorly controlled preoccupations, aspirations or behaviour associated with the use of computers and internet access, which lead to difficulties in daily functioning. This disorder usually occurs in the late twenties or in the early thirties, ten years after the beginning of the use of computer. Psychiatric co-morbid conditions are common, particularly bipolar disorder, mood disruption, anxiety, impaired impulse control and the use of resources that make addiction.3,4According to the activities and the content of Internet-based applications together with data provided by the therapists who treated them, Internet addicts can be grouped into several subcategories: information addicts, computer game addicts, on-line communication addicts (e-mail, chat applications), cybersex addicts, gambling addicts and shopping addicts.2,5Pathological gambling is classified according to DSM-IV TR classification as an impulse control disorder, even though it shows considerable biological, behavioral, clinical and epidemiological similarities with psychoactive substance addiction. Due to increasing availability of gambling, online betting opportunities, investment and trading, frequency of pathological gambling has been in a constant rise nowadays.6,7Due to the fact that pathological gambling is one of the impulse control disorders, and online stock trading hasn't still been recognized as a distinct subtype of internet addiction, the aim of this study was to determine whether the respondents who spend their time investing in the stock market meet the addiction criteria according to DSM-IV TR classification of psychiatric disorders.MATERIALS AND METHODSThis survey was conducted on an anonymous convenient sample of 111 respondents by using a modified self-made IAT questionnaire. The survey was conducted during April 2009 via web portals Poslovni.hr and Moj Novac.hr. People who invest in the stock market and trade stocks online were invited to fill out this questionnaire. The questionnaire contained 13 questions: 3 questions about demographic indicators of the respondents, 3 questions about time spent in investing in the stock market and about frequency of monitoring developments in the stock market and 7 questions composed by DSM-IV criteria by which the existence of addiction is defined. (Appendix). Answers to questions about addictions were classified into two categories: no evidence of addiction and participants exhibited addiction, while the presence of addiction is divided into milder and heavier degree of addiction.Results have been presented in total numbers and percentages.RESULTSThere were 95 men (85,6%) out of 111 respondents who fully responded to the survey. Most of the respondents belonged to the age group of 35-45 years old (49/111; 44,1%), followed by the group of 25-35 years old (40/111; 36,0%), and then by the group of 45-55 years old (14/111; 12,6%), and only 8 of them were younger than 25 years old (7,2%). By level of education the most frequent were highly educated respondents (64/111; 57,7%), 16/111 or 13,5% had college, 30/111 (27,0%) had high school, and one respondent had only primary school.Data on the duration and frequency of investment are shown in Table 1 and include the questions 4-6 from the questionnaire. Majority of them, 106 or 95,5% invested for more than one year. Likewise, most of them daily follow the events (98/111; 88,3%), out of which most of the respondents spend 1-6 hours a day in such activities (63/111; 63,6%). …

**Решение:** -4 исследование зависимости от фондового рынка, без ставок на спорт

---

### 88 · R4683

**ROUNDTABLE DISCUSSION WITH THE EXPERTS: OFFICIAL SPORTS DATA AND SPORTS BETTING ROYALTIES**

2019 · Gaming Law Review · article, journal-article · en · https://doi.org/10.1089/glr2.2019.2343

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 статья о правах спортивных лиг на отчисления от ставок

---

### 89 · R4827

**Essays in microeconomics**

2019 · dissertation · en · https://doi.org/10.70675/e2b12d81z24b0z4533za6c7zda1ce77745b9

Essais en microéconomie Dans ce mémoire, j’étudie trois sujets de microéconomie : le ciblage, les jeux de hasard et l’épargne-retraite. Le premier chapitre, basé sur un travail conjoint avec Francis Bloch, examine une approche du ciblage basée sur le classement par les amis. Un planificateur social a pour objectif d’extraire un classement des individus en demandant à chaque individu de classer ses amis. Nous étudions comment la structure du réseau social de la communauté détermine la capacité du planificateur à extraire un classement véridique et efficace. Notre analyse souligne l’importance des amis communs. Le deuxième chapitre, basé sur un travail conjoint avec Joshua Blumenstock, étudie les paris sportifs en ligne, qui ont gagné en popularité au Kenya et dans d’autres pays d’Afrique orientale. Nous utilisons un vaste ensemble de données sur les transactions de paris sportifs pour prouver que les joueurs peuvent devenir trop confiants dans leur capacité à prédire le résultat des matchs. Nous soutenons que l’excès de confiance persiste parce que les joueurs surestiment la fréquence à laquelle leurs amis gagnent et parce que les joueurs surpondèrent les succès passés par rapport aux échecs passés. Dans le troisième et dernier chapitre, j’utilise une expérience de terrain pour étudier l’impact de la fourniture d’une calculatrice de retraite sur l’épargne-retraite à des employés d’une grande entreprise sud-africaine. La calculatrice fournit des projections de revenu de retraite et aide à contrer les perceptions erronées de la croissance exponentielle. Même si la plupart des employés épargnent toujours au taux minimum et que l’intervention a été organisé pour coïncider avec les augmentations de salaire, le calculateur n’a pas entraîné d’importantes augmentations de l’épargne.

**Решение:** -3 транзакционные данные онлайн-беттеров, когнитивные искажения без PG

---

### 90 · R5007

**Prevalence of gambling-related harm provides evidence for the prevention paradox**

2018 · Journal of Behavioral Addictions · article · en · https://doi.org/10.1556/2006.7.2018.41

Background The prevention paradox (PP) describes a situation in which a greater number of cases of a disease-state come from low-risk members of a population, because they are more prevalent than high-risk members. Past research has provided only tangential and disputed evidence to support the application of the PP to gambling-related harm. Aims To assess whether the PP applies to gambling, the prevalence of a large set (72) of diverse harmful consequences from gambling was examined across four risk categories for problem gambling, including no-risk, low-risk, moderate-risk, and problem-gambling. Methods Respondents who had gambled on non-lottery forms in the past 6 months completed an online survey (N = 1,524, 49.4% male). The data were weighted to the known prevalence of gambling problems in the Victorian community. Results The prevalence of gambling harms, including severe harms, was generally higher in the combined categories of lower risk categories compared to the high-risk problem-gambling category. There were some notable exceptions, however, for some severe and rare harms. Nevertheless, the majority of harms in the 72-item list, including serious harms such as needing temporary accommodation, emergency welfare assistance, experiencing separation or end of a relationship, loss of a job, needing to sell personal items, and experiencing domestic violence from gambling, were more commonly associated with lower risk gamblers. Conclusion Many significant harms are concentrated outside the ranks of gamblers with a severe mental health condition, which supports a public-health approach to ameliorating gambling-related harm.

**Решение:** + опрос 1524 нелотерейных игроков, категории риска PGSI

---

### 91 · R7764

**Odds and Odds Ratio**

2008 · https://doi.org/10.1002/9781118445112.stat03617

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 статистический анализ результатов спортивных соревнований

---

### 92 · R7981

**First Amendment as Last Resort: The Internet Gambling Industry’s Bid to Advertise in the United States**

2006 · bepress Legal Repository · article · en

Subsequent to sending its advertising warning, the DOJ took steps to curb Internet gambling advertising.15 Prosecutors have convened grand juries to inquire about the broadcast of such advertising, and most major American broadcasters and online media, including Clear Channel Communications, Infinity Broadcasting, Discovery Networks, Yahoo!, and Google, have stopped carrying the advertisements.16 This tactic is quite telling about the nature of the Internet gambling industry.17 Safely situated offshore, operators may avoid U.S. law while raking in billions of U.S. dollars per year.18 The popularity of Internet gambling, especially sports betting and poker, continues to grow.19 The DOJ's response seems to be that if it can't prosecute operators directly, it may go after those they do business with in the United States.20 an electronic sanctuary for illegal betting.To Internet betting operators everywhere, we have a simple message: 'You can't hide online and you can't hide offshore.'"Id. at 5-10 (citing Benjamin Weiser, 14 Facing Charges in First U.S. Action on Internet Betting, N.Y.TIMES, Mar. 5, 1998, at A1.At least one of the operators charged, Jay Cohen, was convicted and sentenced to twenty-one months in prison for his Internet gambling offense.Matt Richtel, An Industry That Dares Not Meet in the Country of Its Best Customers, N.

**Решение:** -1 корпоративный анализ операторов ставок

---

### 93 · R4316

**Juegos y apuestas recortó su inversión casi un 40% en el primer semestre de 2020**

2020 · Ipmark: Información de publicidad y marketing · article · es

La ONCE, uno de los 10 primeros anunciantes de Espana, lidero tambien la tabla de mayores inversores publicitarios del sector de Juegos y Apuestas del Estado, a una considerable distancia, ocupo la segunda posicion, seguida del posicion , seguida del portal apuestas deportivas 888 Sport. Pero ?que ha sucedido en los ultimos meses?

**Решение:** -1 исторический анализ игорного бизнеса

---

### 94 · R5061

**Leader wants states to research closely before jumping into sports betting**

2018 · Alcoholism & Drug Abuse Weekly · article, journal-article · en · https://doi.org/10.1002/adaw.31985

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -3 опрос студентов о потреблении алкоголя и ставках без PG

---

### 95 · R2168

**Electronic Screening, Brief Intervention, and Referral to Treatment (e-SBIRT) for Gambling Harm: A Mixed-methods Acceptability Study**

2025 · Journal of Gambling Studies · article · en · https://doi.org/10.1007/s10899-025-10424-9

Gambling harm is a significant public health burden, yet treatment uptake is low. Electronic screening, brief intervention, and referral to treatment (e-SBIRT) programmes have potential to increase uptake and improve treatment outcomes. However, no studies to date have investigated e-SBIRT in the context of gambling. We conducted a single-arm mixed-methods study of acceptability of e-SBIRT for gambling. Quantitative acceptability was indicated by users' perceived satisfaction, impact and helpfulness of the e-SBIRT. Qualitative acceptability was explored using semi-structured interviews. Participants (n = 63), pre-screened for gambling severity, reported high levels of satisfaction with the e-SBIRT, found it helpful, and were more likely to seek treatment. Participants with higher gambling severity scores found the e-SBIRT more acceptable and were more likely to seek treatment following the intervention. Qualitative feedback (n = 7) supported the e-SBIRT's acceptability. The present findings support the acceptability of e-SBIRT for gambling. Further research is required to refine the intervention and examine its effectiveness with those with gambling harm.

**Решение:** -5 сравнение пациентов клиники лечения гемблинга с контролем

---

### 96 · R0602

**Payment preferences and related sports betting behavior: A secondary analysis of player data from an online sports operator**

2026 · OSF Preprints (OSF Preprints) · preprint

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -7 спам онлайн-казино на Zenodo

---

### 97 · R6717

**Upset Prediction in College Football**

2013

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 литературоведческий анализ произведений о спорте

---

### 98 · R4873

**Zweiter Glücksspieländerungsstaatsvertrag: Welche Änderungen sind erforderlich?**

2019 · Springer eBooks · book-chapter · de · https://doi.org/10.1007/978-3-658-24972-4_19

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -2 магистерская диссертация по спортивному маркетингу

---

### 99 · R5506

**Big Data Analysis on Gambling Related News in South Korea**

2017 · IEEE International Congress on Big Data (BigData Congress) · article, conference object, journalarticle · en · https://doi.org/10.1109/bigdatacongress.2017.82

The purpose of this study is to understand the recognition of gambling industry through the semantic analysis of news data on lottery, sports betting, horse racing and casino that was reported between 1990 to 2015 in South Korea. This paper revealed the difference between journalists' intention and public's perception about news by analyzing the frequency and connectivity of news with framing and public's interest through semantic network analysis and explored the policy characteristics and innovation task. The result of analysis, news on lottery game mainly has been reported social issue related with win such as 'winning number', 'prize money', 'suspicion of manipulation' and etc. News on sports betting has been reported mandatory information related with business project and illegal site such as 'bidding', 'illegal site', 'sales target' and etc. News about horse racing has been reported the information about the business advertisement such as 'online race track' and 'promotion'. Lastly, casino related news has been reported 'major information' such as illegality', 'gambling place' and 'foreigner'. As a result of times series analysis, news about casino in the 1990s, news about lottery in the 2000s and news about horse racing in 2010s have been increased. Public's interest also has been moved to 'business scandal', 'winning game', 'citizens' campaign' and etc. Gambling related news has been classified by four types, 1. advertising publicity(horse racing), 2. mandatory information(sports betting), 3. social issue(public agenda, lottery), 4. major information(casino). We could get the insight that news can be formed a public agenda, when news is reported as a social issue with high frequency and public's interest like lottery related news.

**Решение:** -3 эксперимент по восприятию рекламы ставок без шкалы PG

---

### 100 · R6385

**Exploring the Relationship between Race and Sports Book Wagering Activity and Daily Slot and Table Game Play**

2014 · UNLV Gaming Research &amp; Review Journal · journal-article · https://doi.org/10.9741/2327-8455.1315

Using performance data from three Las Vegas hotel-casinos, time series regression models were employed to better understand the relationship between race and sports book wagering volumes, and slot and table game play. Variables representing both race and sports book wagering volumes failed to produce statistically significant effects in seven of twelve hypothesis tests, within models designed to explain the daily variation in slot and table game play. The results directly extend the work of Abarbanel, Lucas and Singh (2011) by examining the relationship between book wagering levels and table game play, and provide additional empirical tests of the Full Service Theory examined in Lucas (2013b). Casino operators and developers gain valuable insight related to the contribution of books to primary casino profit centers, and the methodological approach is readily adaptable to other leisure service businesses interested in estimating the contributions of one profit center to another.

**Решение:** -1 эссе о культуре азартных игр в спорте

---

### 101 · R7626

**Filipinos and the Reno Casino Experience**

2009 · Filipino American National Historical Society journal · article · en · https://doi.org/10.1353/fil.2009.a908135

Introduction FILIPINOS AND THE RENO CASINO EXPERIENCE• By Gilda Galope Lum 50 Gambling is on the rise, according to a Pricewaterhouse Coopers LLP report released on June 18, 2008. The global gambling revenue from casinos is expected to reach $155 billion annually by the year 2012. The Asia Pacific region is the fastest growing, but the U.S. is expected to remain the leader in gambling revenue by region.1 Gambling is a leading leisure activity worldwide, according to Desmond Lam, Assistant Professor ofMarketing at the University ofMacau.2 Chinese and Gambling In 2300 B.C., the Chinese recorded their first official account of the practice of gambling.3 "In fact, the very first accounts of gambling were recorded in China. According to a report by Access Asia Limited (2002), Keno (a form ofgambling product) was first played in China since 3,000 years ago. The basis of many oftoday's favorite card games such as blackjack and poker are also thought to have been invented in China. Gambling was very popular in ancient China and throughout Chinese history despite the fact that it was under strict regulatory controls and ban." 4 Filipinos and Gambling One of the most popular gambling games in the Philippines isjueteng, an illegal numbers game played in most provinces of the Philippines, involving the selection of a pair ofnumbers from a set of37 numbers. According to Emil Jurado, "Jueteng has been with us since pre-Spanish times. 5 In 1931, Professor Emory S. Bogardus, who was head of the sociology department at the University of Southern California, conducted a study of Filipino immigrant attitudes in the U.S. His study was based on interviews with Filipinos on the West Coast ofthe U.S., as well as from other parts ofthe U.S., from the Filipino press in the U.S., and from recent Filipino arrivals as well as from Filipinos who have been in the U.S. "...for a number ofyears." In his published report, Bogardus describes one Filipino immigrant attitude which he calls "personality disorganization...illustrated by the tendency to seek in his spare hours 'the places and companionships that can make him forget, even for a moment, that he has become a slave.' According to one ofthe Filipinos • Presented during the 12th National Biennial Conference and 25th Anniversary of the Filipino American National Historical Society in Anchorage, Alaska, July 3-5, 2008. 1 "Global gambling revenue to increase to $155 billion annually." ogpaper.com, 6/18/2008 2 Desmond Lam, "The Brief Chinese History of Gambling." 3 "Gambling Has Been Part of Human Culture for Thousands of Years." 4 Desmond Lam, "The Brief Chinese History of Gambling." 5 "Jueteng", Wikipedia. Filipino American National Historical Society Journal Volume 7 2009 51 who was interviewed in the Bogardus study, "Most of the Filipinos go to Chinese gambling houses because they have no other place to go." 6 • 7 In 1949, D. F. Gonzalo, a sociology student at the University of Southern California, reported that Filipino immigrants in America who gravitated to Chinese gambling dens were mainly unskilled, single young men who had no family or friends, nor "...any tangible aim in life." 8 In 1977, historian H. Brett Melendy mentioned that, during the 1930s, Filipino immigrants in California spent their leisure time attending and betting on sports events such prize fights and wrestling matches, or playing, poker, blackjack and dice, in Stockton and Reno. 9• 10 Purpose ofthis Paper In 1976, Felicia Campbell, an Associate Professor ofEnglish at the University of Nevada at Las Vegas, published an article on the positive effects of gambling and risk taking, using the research method of participant observation in casinos. In her article, Campbell states, "I have found gambling to be largely beneficial to the gambler, increasing rather than decreasing his efficiency. It stimulates, offers hope, and allows decision-making. The purpose ofthis paper is to describe some ofthe experiences ofFilipinos from various cities in Northern California who go to casinos in the Reno area What are some of the benefits they get from going to casinos? The research method used in this preliminary study was participant observation in the casinos. This paper is written from the viewpoint ofhuman...

**Решение:** -2 исследование стратегий спортивного маркетинга

---

### 102 · R2186

**Flutter Entertainment's Competitive Analysis**

2025 · Frontiers in Business Economics and Management · article, journalarticle · en · https://doi.org/10.54097/vv9rv667

This report provides a comprehensive competitive analysis of Flutter Entertainment plc, an international sports betting company headquartered in Ireland. Flutter Entertainment operates in over 100 countries worldwide, boasting well-known brands such as Sisal, FanDuel, Betfair, and Paddy Power. The report is structured into four main parts. Firstly, it outlines the company profile and status of Flutter Entertainment, highlighting its strong financial position and significant global presence. Secondly, it conducts a contextual analysis, examining internal strengths such as its portfolio of recognizable brands, global reach, and dedication to innovation, as well as external factors like market competition, regulatory changes, and technological advancements. The third part delves into Flutter's marketing communication strategy, discussing its use of advertising, online and social media, publicity, and corporate social responsibility (CSR) to engage with customers and build its reputation. Lastly, the report includes a peer analysis comparing Flutter Entertainment's financial performance with its top four competitors, emphasizing Flutter's position as a market leader. Despite facing fierce competition and regulatory challenges, Flutter Entertainment has demonstrated successful business strategies, including market expansion and product innovation, contributing to its long-term viability and success in the highly competitive online gaming industry.

**Решение:** -2 качественный анализ культуры ставок среди мужчин

---

### 103 · R6848

**The Relationship among Drinking Games, Binge Drinking and Gambling Activities in College Students**

2012 · Journal of alcohol and drug education · review, article · en

ABSTRACT A total of 293 college students completed a survey about binge drinking and gambling activities. Students who played the lottery once a week had lower binge drinking scores compared to students who played the lottery more than once a week and those students who never played the lottery. Similar patterns were also detected for students who engaged in sports-betting, card-playing, and games of skill. Students who met the criteria for binge drinking were likely to engage in sports-betting, video and regular poker, internet, office pools, and other games of skill compared to students who did not meet the criteria for binge drinking. Implications for collegiate prevention programs are discussed. Key Words: Drinking Games, Binge Drinking, Problem and Pathological Gambling ********** The co-occurrence of alcohol use and gambling activities has been well documented in college students (Ladouceur, Dube, & Bujold, 1994; Martens et al., 2009) and the general population (Walker, Clark, & Folk, 2010). Both alcohol use and gambling behavior is a source of great concern for the college population because of the potential health risks involved. Compared to college students without gambling problems, students with gambling problems are more likely to engage in unsafe behavior including greater use of alcohol, tobacco, marijuana, driving under the influence, and unsafe sex after drinking (Engall, Hunter, & Steinberg, 2004; LaBrie, Shaffer, LaPlante, & Weschler, 2003; Stuhldreher, Stuhldreher, & Forrest, 2007). The relationship between specific behaviors related to alcohol use, including drinking games and binge drinking, and the different types of gambling activities in a college population was investigated in the present study. Drinking games (DG) are popular on college campuses as self-reported participation in these games has been observed to be as high as 63% in at least one study (Borsari, Bergen-Cico, & Carey, 2003). DG often involve activities with rules governing the consumption of alcohol. College students who participate in these games tend to drink more often than students who do not participate in these games (Johnson, Hamilton, & Sheets, 1999). The adverse impact of DG includes heightened aggression, vandalism and driving under the influence (Borsari, 2004). Different possible motives for undergraduate engagement in DG have been described. It is believed that participation in these games has a social advantage for the college students as it helps in reducing shyness or inhibitions and facilitates friendships (Pederson, 1990). However, some studies have shown a negative correlation between social anxiety and participation in DG, with socially anxious individuals less likely to be involved in these games as they might avoid social situations altogether (Ham & Hope, 2006; Johnson, Wendell, & Hamilton, 1998). Other specific motives include playing for competition and thrills, fun and celebration, sexual manipulation and coping (Johnson & Sheets, 2004). Binge drinking (also known as HED or heavy episodic drinking) has been defined by the National Institute of Alcohol Abuse and Alcoholism (NIAAA) as a pattern of alcohol consumption which brings the blood alcohol concentration (BAC) to 0.08 gram percent and above. This BAC typically corresponds to consumption of five or more drinks in two hours for males and four or more drinks in two hours for females. Young adults showing signs of problem gambling behavior were found to be more likely to indulge in binge drinking (Walker, Clark & Folk, 2010). The prevalence of binge drinking has been reported to be as high as 40% in the college population (Wechsler, Lee, Nelson, & Kuo, 2002). College-age binge drinkers were more likely to engage in unprotected sex, suffer physical injuries and cognitive impairment and experience employment and inter-personal problems (Hanson & Engs, 1992; Weschler & Isaac, 1992). …

**Решение:** -1 анализ нормативно-правовой базы беттинга

---

### 104 · R0516

**৳ +91-7297856580 ৳ Trusted online betting id login In Coimbatore**

2026 · ResearchHub Technologies, Inc. · casereport, report · und · https://doi.org/10.55277/researchhub.fz0eseht

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -7 спам букмекерской конторы на Zenodo

---

### 105 · R1597

**The Mediating Role of Mental Health in the Relationship Between Gambling Severity and Suicidal Ideation: A Study with Clinical and General Population**

2025 · International Journal of Mental Health and Addiction · article · en · https://doi.org/10.1007/s11469-025-01503-4

Abstract Gambling is a public health problem that affects many people in many ways. One of the most serious effects is on people's mental health and suicidal ideation. This study has two main aims: 1) To analyse the differences between the clinical population (i.e., individuals with gambling disorder) and the general population in terms of gambling severity, suicidal ideation, and mental health; and 2) to test the mediating role of mental health in the relationship between gambling severity and suicidal ideation in people with gambling disorder and the general population. A total of 318 participants were included in the study: 153 gamblers undergoing treatment for gambling disorder ( M age = 44.38, SD = 12.48, 81% males) and 165 individuals from the general population ( M age = 47.57, SD = 13.52, 26.67% males). Two structural equation models were conducted to test the mediating role of mental health issues (i.e., depression, anxiety, hostility, somatisation, and obsessive–compulsive) in the relationship between gambling severity and suicidal ideation. The results show no significant differences in mental health between the population with gambling disorder and the general population. However, the relationship between gambling severity and suicidal ideation appears to be mediated by mental health, both in the clinical and general populations. Findings show the importance of addressing mental health to prevent suicidal ideation. Given the high prevalence of suicidal ideation in individuals with gambling disorder, the assessment and treatment of gambling problems and mental health is strongly recommended. Results also highlight the importance of transdiagnostic protocols that address mental health, with a particular focus on suicidal ideation.

**Решение:** -5 выборка лиц, обратившихся за помощью в связи с гемблингом

---

### 106 · R5099

**Pleasure Enclosure**

2018 · Shakespeare · article · en · https://doi.org/10.1080/17450918.2018.1455733

A paradigm shift for Marxist interpretation might substitute pleasure for ideology as the special product of Shakespeare’s theatre. Requiring analysis beyond market generalisations, specificities of self-expanding capital, especially compulsory competition, invite comparison of the new purpose-built theatres with the privatising land enclosures of the agrarian-capitalist revolution. For pleasures best paid in admission beforehand, as also seen for prostitution, theatre could gain productive potential through innovative competition with other pleasure producers – incorporating, competing with, or even poaching from London’s burgeoning alternative entertainments (brothels, gambling, animal sports, etc.). Aside from some negative, coercive outcomes reflecting the perceived “twin evils” of land enclosure and engrossment, theatre could also develop what Marx thought of as capitalism’s positive civilising trait: the ability to experience multiple pleasures. Brief historical episodes exemplify theatre’s becoming such an industry: rioting echoing anti-enclosure riots, a fenced structure at the Fortune theatre, increasing privatisation in Shakespearean brothel scenes, representations of boredom accompanying entertainment, scenes of pleasure choice, and a trend toward extreme miscellany leading to a radically disparate D’Avenant play in the Restoration. Self-valorising, entertainment logic is embodied in Shakespearean representations of mirth becoming “too much fun” – bubbles of entertainment value parallel to capital’s own intrinsic tendency of crisis and collapse.

**Решение:** -2 дискурс-анализ телевизионной рекламы ставок

---

### 107 · R1459

**Betting on the Future: How Legal Sports Gambling is Reshaping American Sports Industries**

2025 · The University of Texas at Austin · dissertation/thesis, thesis · en · https://doi.org/10.26153/tsw/60573

This thesis examines the structural and cultural transformation of the American sports and sports media industries following the 2018 repeal of the Professional and Amateur Sports Protection Act (PASPA). Once restricted to illicit markets, sports betting has emerged as a mainstream economic engine, generating significant revenue for professional leagues, individual franchises, broadcast networks, and state governments. Employing a mixed-methods approach, including legal analysis, economic data, and comparative media review, this study investigates how the legalization of sports gambling has altered fan engagement, media content, and sponsorship dynamics to become a significant driver of industry change. It further explores the ethical and regulatory implications of this evolution, particularly concerning addiction, corruption, and the increasing entanglement of public institutions with gambling enterprises via regulatory frameworks and revenue distribution. Ultimately, the study argues that legalized sports betting has initiated a comprehensive redefinition of the American sports experience—embedding financial risk into fandom and raising complex questions about integrity, equity, and the future of sport as public culture.

**Решение:** -3 CRM и удержание клиентов в онлайн-ставках без PG

---

### 108 · R3127

**The effect of articulation in sports posters on betting behavior**

2023 · Humanities and Social Sciences Communications · article, other literature type, text/ · en · https://doi.org/10.1057/s41599-023-01517-0

Abstract Several studies argue that sponsorship promotes and normalizes gambling behavior because commercial gambling providers (CGPs) act as sponsors for many sports entities. This study examines the effect of articulation on sports sponsorship, sincerity, and congruence as perceived by consumers and betting behavior by comparing a CGP brand with a congruent sponsor brand. Data were collected through an experiment combining the factor of the inter-subject type of sponsor (CGPs sponsor vs. congruence sponsor) and articulation (commercial articulation and no articulation) in 518 subjects from the United Kingdom. The analysis was performed using structural equation modeling and multi-group analysis. Subjects showed a greater willingness to bet when the CGP sponsor was perceived as congruent and sincere compared with congruent sponsorship, suggesting that this type of sponsor could encourage sports betting. However, the elimination of CGPs’ sponsorship is complex because of the significant funding they provide.

**Решение:** -2 математические модели букмекерства

---

### 109 · R4079

**Fantasy sports and beyond: Complementary digital experiences (CDXs) as innovations for enhancing fan experience**

2021 · Journal of Business Research · article, journal-article · en · https://doi.org/10.1016/j.jbusres.2021.05.037

Abstract The sports industry has eagerly embraced digital technologies that have the potential to create and nurture compelling fan experiences. In this study, we investigate how and why complementary digital experiences (CDXs)—touchpoints in the customer journey that affect the value of a core brand experience, transforming it into a technology-enhanced experience—enhance the sport fan’s experience and journey, and in what ways they may be limited. We root our inquiry in the fantasy football context and analyze data from 26 in-depth interviews to reach our findings, which explain the 5Cs of CDX (i.e., control, camaraderie, continuation, competition, and customization) as influential design elements in the innovation of digital touchpoints in the sports customer journey. Our study makes theoretical and practical contributions to the field of sports innovation, and joins conversations about fantasy football and digital touchpoints in the customer journey. In doing so, it creates bridges between these areas of scholarship.

**Решение:** -1 экономика спорта и регулирование беттинга

---

### 110 · R8210

**A strategic research on sustainble development of sports lottery tickets in Henan Province**

2003 · journal of physical education · article · en

Adopting the method of investication, questionnare, statistic, documentation and comparing analysis,the author analyzes systematically and studies present conditions, trend of development, and provides the game plan for solving the questions in the sustainble development. The studies show that it is necessary to perfect its structure which is suitable for socialistic market economy,and make it circulate under the law. Also,we should pay attention to the propaganda,correct people's attitudes and decorate market network of sports lottery tickets.Further more,it is also important to found the lottery club,vary its product and method, and lauch deeper advertising campaign.Through all these,the sports lottery tickets can be attractive to the public.

**Решение:** -1 судебная практика по спорам в сфере ставок

---

### 111 · R0669

**Gambling culture in elite female sports clubs in England**

2026 · Digital Scholarship - UNLV (University of Nevada Reno) · conference-paper

The study aimed to examine gambling culture in elite female sports clubs in England and explore how gambling is viewed and perceived by elite female athletes. 15 interviews were carried out with elite female athletes playing soccer (n=4), cricket (n=5) and rugby union (n=6). Thematic analysis was conducted and six major themes were identified: motives for gambling, normalisation of sports betting, opening up, education and support, gambling participation and gambling industry funding. Regarding main motives for gambling, interviewees believed female athletes might gamble due to their competitive nature as athletes or existing peer pressure in a club where a gambling culture exists. The analysis also revealed that gambling appeared to be a normalised activity for female athletes and that a gambling culture exists in female sports clubs. Although they believed gambling is more common in the men’s game, they are exposed to it everywhere in their lives, especially football betting and horse racing. They often have conversations around it, attend horse racing events together and are aware of gambling happening in other teams. They would face issues if they would open up about a gambling problem, with stigma around gambling, but being a female athlete making it even more challenging. Additionally, they believe there is need for education and support around the potential harms of gambling tailored for female athletes and not just around the corruption side of things.

**Решение:** ? лонгитюдное исследование гемблинга, нет аннотации, проверить

---

### 112 · R8195

**On the Market Operation of Computer Sports Lottery**

2003 · Sports Science Research · article · en

The development of computer sports lottery in China has achieved good results. But someproblems still exist. The paper analyses the starting, present situation and the prospects of computersports lottery in Shanghai and explores the key links of the maket operation of computer sports lottery.Some marteting measures are put forward.

**Решение:** -1 пособие / книга о ставках на спорт

---

### 113 · R0083

**Adicciones comportamentales: epidemiología, factores de riesgo, fenotipos y resultado terapéutico**

2026 · Universitat Autònoma de Barcelona · doctoral thesis · spa · https://hdl.handle.net/10803/697212

Introducción: El TJ y la AVJ, son dos de las modalidades de AC con mayor prevalencia en las sociedades industrializadas, mostrando un crecimiento alarmantemente en las últimas décadas. Además, son cuadros clínicos cuyas características están en transformación, en gran medida como resultado de la rápida aparición y evolución de nuevas plataformas en formato presencial y virtual. Ante este escenario, los objetivos principales son: a) identificar componentes biopsicosociales que actúan como factores de riesgo del TJ (en especial la adicción a las apuestas deportivas online [AADO]) y la adicción a los videojuegos online (AVJO); b) analizar los mecanismos subyacentes que contribuyen a la expresión fenotípica y endofenotípica de estos comportamientos adictivos y c) determinar las variables con capacidad predictiva a la respuesta al tratamiento mediante la terapia cognitiva conductual (TCC). Resultados: En términos generales, las muestras analizadas estuvieron compuestas mayoritariamente por hombres, solteros, con niveles educativos primarios o secundarios y estatus socioeconómico bajo. En el primer estudio, se observó que la prevalencia de AADO fue del 13.01%, casi cuatro veces superior a la de AVJO, que alcanzó un 3.82% en una muestra de 3.036 pacientes que consecutivamente acudieron a solicitar tratamiento por comportamientos adictivos. Además, se identificó una tendencia lineal creciente en la prevalencia de AADO entre el 2012 (8.6%) y el 2022 (15.5%), mientras que la AVJO mostró solo una ligera tendencia creciente, aunque no alcanzó la significación estadística. A nivel psicopatológico, los pacientes con AADO presentaron mayores niveles de depresión, ansiedad, ideación paranoide y malestar psicológico global, así como mayores índices de impulsividad, desregulación emocional y consumo de sustancias. El perfil de personalidad de este grupo de pacientes se caracterizó por una mayor búsqueda de novedades, mayor dependencia de la recompensa, mayor persistencia y menor evitación del daño. En el segundo estudio, que se realizó mediante análisis de redes, la autotrascendencia fue identificada como el nodo “puente” y el más relevante, seguido del síntoma DSM-5 A7 “mentiras para ocultar el grado de implicación en el juego”, en los pacientes con actos ilegales relacionados al trastorno de juego (AIRTJ). En contraste, con los pacientes sin AIRTJ, el nodo con mayor relevancia y que se identificó como “puente”, fue el síntoma DSM-5 A5 “apuesta cuando se siente estresado (deprimido, culpable o ansioso)”. El tercer estudio evidenció que el riesgo de recaída durante la TCC, aplicada a pacientes con AVJO fue superior en sujetos con puntuaciones más altas en sensibilidad interpersonal, hostilidad y persistencia. Asimismo, ser hombre y presentar un inicio del comportamiento adictivo más tardío aumentó la probabilidad de abandono del tratamiento, mientras que un bajo cumplimiento terapéutico se asoció a mayores niveles de ideación paranoide, dependencia de la recompensa y bajos niveles de cooperatividad. El cuarto estudio que se incluye como anexo en esta tesis doctoral evidenció que, en comparación con sujetos controles sin adicciones, el TJ se asocia directamente con una edad más joven, mayores niveles de impulsividad, mayores déficits a nivel neuropsicológico y un nivel más bajo de LEAP2. De igual modo, se identificaron vínculos indirectos-mediadores que destacaron el papel relevante de la impulsividad y el funcionamiento neuropsicológico en la predisposición al desarrollo del TJ. Conclusiones: Los resultados de los estudios que conforman esta tesis evidencian la heterogeneidad de las AC, así como la presencia de múltiples factores biopsicosociales que influyen en su desarrollo y mantenimiento. Asimismo, se identificaron perfiles diferenciados en los grupos de pacientes con TJ (en particular con AADO) y AVJO, caracterizados por variables sociodemográficas, psicopatológicas y rasgos de personalidad específicos que permiten comprender mejor los mecanismos subyacentes que configuran la expresión fenotípica propia de cada condición clínica. Introducció: El TJ i l'AVJ, són modalitats d'AC amb més prevalença a les societats industrialitzades, mostrant un creixement alarmantment en les darreres dècades. A més, són quadres clínics les característiques dels quals estan en transformació, en gran mesura com a resultat de la ràpida aparició i evolució de noves plataformes en format presencial i virtual. Davant d'aquest escenari, els objectius principals són: a) identificar components biopsicosocials que actuen com a factors de risc del TJ (especialment l'addicció a les apostes esportives en línia [AADO]) i l'addicció als videojocs en línia (AVJO); b) analitzar els mecanismes subjacents que contribueixen a lexpressió fenotípica i endofenotípica daquests comportaments addictius i c) determinar les variables amb capacitat predictiva a la resposta al tractament mitjançant la teràpia cognitiva conductual (TCC). Resultats: En termes generals, l

**Решение:** -5 пациенты с игровой зависимостью в наркологическом центре

---

### 114 · R3816

**Are esports bettors a new generation of harmed gamblers? A comparison with sports bettors on gambling involvement, problems, and harm.**

2021 · Journal of behavioral addictions · article, journal article, journalarticle · eng · https://doi.org/10.1556/2006.2021.00039

Abstract Background and aims Esports betting is expanding in popularity, yet little is known about who participates in this niche gambling activity. This study aimed to determine whether esports bettors are more vulnerable to harms and problems than gamblers engaged in traditional sports betting. Methods Data were collected from 298 regular esports bettors and 300 sports bettors (who regularly bet on traditional sports, but not esports). These groups were compared on demographics, gambling involvement, problem gambling, and gambling-related harms. Results Compared to sports bettors, esports bettors were more likely to be younger, university-educated, employed (lower income earners), and speak a non-English language at home. Esports bettors gambled on fewer traditional gambling activities in the last 12 months, but compared to sports bettors, gambled more frequently on some activities, were more likely to meet problem gambler criteria (64.8.% vs 17.3%), and experience at least one gambling-related harm (81.9% vs 45.3%). Being an esports bettor significantly predicted greater problem gambling severity and gambling-related harms. More frequent esports skin betting and skin gambling (on games of chance) were significant predictors of gambling problems amongst esports bettors. Discussion and conclusion The results provide preliminary evidence that esports bettors are more likely to experience gambling problems compared to their sports betting counterparts, potentially stemming from their involvement in emerging video-game related gambling products.

**Решение:** + опрос 298 киберспортивных и 300 спортивных беттеров, PGSI и вред

---

### 115 · R3813

**“Be Soft”: Irony, Postfeminism, and Masculine Positions in Swedish Sport Betting Commercials**

2021 · Men and Masculinities · article, journalarticle, journal-article · en · https://doi.org/10.1177/1097184x211012739

Gambling advertising usually draws heavily on gendered stereotypes, including portrayals of male gamblers as tough and successful. Meanwhile, representations of men in advertising have grown increasingly diverse, with emotional and sexualized men accompanying heroic, muscular portrayals. In this article, both these bodies of research are drawn upon to discuss a series of Swedish sports betting commercials which encourage the viewer to “bet hard” while also “being soft.” The celebration of “softness” is ambiguous but can be seen as referencing gendered, political discussions about men and masculinity. Engaging with hybrid masculinities theory, postfeminism, and discourses about gambling and betting, the article demonstrates that meanings around “softness” are ambiguous, ironic, and serve to normalize gambling by distancing it from discourses about addiction. The commercials represent a shift in gambling advertising, but the linking of men’s politics to gambling also represents a new complexity in narratives about “new,” or “soft,” men.

**Решение:** -6 антропологическое исследование ритуалов

---

### 116 · R6605

**To Play or Not to Play! Online Fantasy Football Consumption Motives and the Relationship with Attitude and Future Behavioural Intentions**

2013 · Mediterranean Journal of Social Sciences · article · en · https://doi.org/10.5901/mjss.2013.v4n14p201

The immense popularity of professional sports and fantasy football in particular, has brought fans to the Internet in search of ways to enjoy their favourite teams’ performances. The study investigates the underlying dimensions that influence online fantasy football motivation and the relationship with attitudes towards its usage and future behavioural intentions. A quantitative research approach was applied using a self-administered questionnaire and data was analysed from 193 respondents. Through factor analysis, a five-factor structure was established with eustress, achievement/reward, aesthetics, enjoyment and ease of use being identified as the primary motivational dimensions towards fantasy football. Positive correlations were reported along all five dimensions. In addition the linear regression analysis showed strong predictive relationship between the underlying motives with attitude. Positive and significant relationship were also found between attitude and future intentions to participate in fantasy football. The findings presented in this study may be explored further in other sports contexts. However, sports marketers may gain invaluable insight towards the development of a comprehensive strategy towards a fantasy sports’ marketing mix. Similarly, sports governing bodies may be empowered to formulate a national regulatory framework along the identified dimensions. DOI: 10.5901/mjss.2013.v4n14p201

**Решение:** -3 мотивы участия в фэнтези-футболе без инструмента PG

---

### 117 · R4454

**Covid-19’s impact on a sports league**

2020 · Routledge eBooks · book-chapter · en · https://doi.org/10.4324/9781003105916-24

In May 2018, the United States repealed the Professional and Amateur Sports Protection Act, thus allowing individual states the opportunity to offer their own form of regulated sport betting. Looking to capitalize on this change in law and aid in the progression of sport betting within the United States, the newly re-established XFL of 2020 decided to go all-in on a future destined to involve betting. The betting consumer was at the forefront of this new XFL. Floating betting lines during XFL game broadcasts gave sport fans in the United States a glimpse into the potential future of sport betting. However, soon after the league’s season debut, Covid-19 struck the globe. The XFL’s season was ultimately canceled and the league soon after folded due to the Covid-19 pandemic. This chapter will focus on how the XFL, as a league, embraced sport betting within its daily operations and the untimely impact Covid-19 had on its future.

**Решение:** -1 антимонопольное регулирование в спортивном беттинге

---

### 118 · R2221

**A Longitudinal Exploration of Sports Betting Dynamics among Adolescents and Emerging Adults in Flanders**

2024 · Lirias · article

status: Published

**Решение:** -3 эксперимент с рекламными сообщениями без шкалы PG

---

### 119 · R7169

**CRM aktivity online sázkových kanceláří**

2011 · dissertation · cs

This thesis deals with the use of customer relationship management elements among online bookmaker companies. This work analyzes, how the Internet bookmakers perceive the process of building relationships with customers, compares this perception at different bookmakers and then adds recommendations to optimize CRM in online betting compa-nies.

**Решение:** ? опрос студентов о распространенности ставок, проверить PG

---

### 120 · R1440

**Optimal Online Bookmaking for Binary Games**

2025 · IEEE International Symposium on Information Theory (ISIT) · article, conference object, preprint · und · https://doi.org/10.1109/isit63088.2025.11195494

In online betting, the bookmaker can update the payoffs it offers on a particular event many times before the event takes place, and the updated payoffs may depend on the bets accumulated thus far. We study the problem of bookmaking with the goal of maximizing the return in the worst-case, with respect to the gamblers' behavior and the event's outcome. We formalize this problem as the \emph{Optimal Online Bookmaking game}, and provide the exact solution for the binary case. To this end, we develop the optimal bookmaking strategy, which relies on a new technique called bi-balancing trees, that assures that the house loss is the same for all \emph{decisive} betting sequences, where the gambler bets all its money on a single outcome in each round.

**Решение:** -1 дебаты о мобильном гемблинге и политике

---

### 121 · R7111

**Contemporary Issues in Sports Economics: A Selection**

2011 · Edward Elgar Publishing eBooks · book, other literature type, part of book or chapter of book · en · https://doi.org/10.4337/9780857930385.00008

The development of sports economics has exploded in recent years, and this well-researched and relevant book explores some of the most critical themes. Contemporary Issues in Sports Economics examines topics that have previously received little attention in the literature, such as the determinants and social impacts of sports participation including the link to crime levels. The distinguished authors also discuss some of the less investigated aspects of professional team sports, including: • sports betting, financing and governance; • the impact of low scoring matches on competitive balance and fan appeal in European football; and • the effect on player transfers of a luxury tax on club payrolls in Major League Baseball.

**Решение:** -1 практическое руководство по ставкам

---

### 122 · R5647

**In re: Daily Fantasy Sports Marketing and Sales Practices Litigation; In re: DraftKings, Inc., Fantasy Sports Litigation; In re: Fanduel, Inc., Fantasy Sports Litigation Case No. MDL No. 2677, 2678, and 2679; 2016 U.S. Dist. LEXIS 13292 (Judicial Panel on Multidistrict Litigation, February 4, 2016)**

2016 · Gaming Law Review and Economics · article, journal-article · en · https://doi.org/10.1089/glre.2016.20416

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -2 фокус-группы с игроками о мерах защиты

---

### 123 · R1030

**Desporto, política social e pobreza em Portugal**

2026 · Movimento (Porto Alegre) · article, preprint · pt · https://doi.org/10.22456/1982-8918.148959

Esta investigação buscou examinar a configuração do financiamento e do gasto público das políticas desportivas destinadas à generalização da prática desportiva em Portugal, em especial aquelas que preveem vagas à população pobre do país. Os dados vinculados ao Programa Nacional de Desporto para Todos (PNDpT) foram nossa base empírica de estudo, e demonstraram que o Estado português participa de maneira tímida do orçamento do instituto Português do Desporto e Juventude (IPDJ), sendo as apostas esportivas e online a maior fonte de financiamento deste órgão. Sobre o PNDpT apontamos que a fatia orçamentária média do IPDJ em 2022 se limitou a 13% dos custos totais, o que tende a dificultar a expansão deste programa. Como reflexão, sugerimos que os recursos poderiam ser mais bem partilhados, pois enquanto o PNDpT consome a quantia módica de 2,5% do orçamento do IPDJ, as transferências para as federações desportivas avançam em 75%.

**Решение:** -1 финансовый и правовой обзор индустрии ставок

---

### 124 · R5925

**Paris Sportifs, comment vaincre la chance ? : les secrets des parieurs sportifs professionnels enfin dévoilés / Benoît Tréanton**

2016 · article · fr

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 социологический комментарий к рынку ставок

---

### 125 · R8287

**Sports, Gambling, and Government: America's First Social Compact?**

2001 · American Anthropologist · article, review · en · https://doi.org/10.1525/aa.2001.103.2.331

The presence of a 3,600‐year‐old ballcourt in the Mazatan region of Southern Mexico implies that a significant connection existed between ballcourts, competitive sport, and the emergence of the first ascriptive societies in Mesoamerica. We explore four likely connections between the Mesoamerican ballgame, rank society, and early government. These include gambling, playing the game, sponsorship of the game and its associated activities, and the effects of team sports on community identity. Ethnographic information from tribal societies is reviewed with respect to the social roles of competitive games and their effects on egalitarian society. We consider the idea that community identity, or communitas , can become embodied in a small group of people or individuals who sponsor sport, its associated rituals, and the construction of sporting facilities. These individuals may subsequently gain higher status within both their communities and their regions. This finding adds sport and competitive gaming to the growing list of processes that anthropologists should consider in exploring social transformations. [Mesoamerica, social complexity, ballgames, community identity]

**Решение:** -1 юридический анализ игорного законодательства

---

### 126 · R2460

**The Digital NBA: How the World's Savviest League Brings the Court to Our Couch**

2024 · Journal of Sport History · article · en · https://doi.org/10.5406/21558450.51.1.14

The National Basketball Association (NBA) is one of the youngest leagues in major professional American men's sports, yet it has quickly become a domestic success and global media behemoth. In The Digital NBA: How the World's Savviest League Brings the Court to Our Couch, Steven Secular demonstrates how the NBA maintains its media power through a mixture of media, technology, and marketing strategies. While most large-scale sports leagues and media firms have grown independently and then collaborated to seek mutual success, Secular argues that for the NBA, this relationship has increasingly evolved into an integrated, coherent system. Drawing on the literature of marketization and mediatization, Secular establishes the NBA as an illustration of the forces that enable the growth of our media environment as a whole. To describe the expanding sports media industry, Secular draws examples from the NBA's industrial, multinational legacy of production and dissemination. Analyses of five NBA sites highlight the league's operations, tactics, and investments: the event, venue, wires, office, and couch. Using NBA history and media industry analyses, Secular argues that the NBA has reinvented itself for a “multiplatform, post-network era” (14). He compares the NBA's global, multipronged platformization to that of companies like Netflix and HBO, adding the NBA to the list of more traditional “media” producers that emphasize efficient programming through platforms. These attempts at “pan-regional legibility” rely upon a balance between products aimed at local and global audiences—creating content that has “equivalence” across politico-economic boundaries (17).Chapter 1 investigates how the NBA imbues its live media productions with commercial sponsorships. Secular highlights the NBA's expansive team exhibition tours of the 1980s as a marketing technique intended to boost global demand for the league's television programming. He argues that the McDonald's Basketball Open (1987–1999) taught the league new approaches to marketing and sponsorship. Such events trained the NBA how to produce events for international audiences that blended local interests with “US sponsors and consumption patterns” (45). Since that time, the NBA has honed its ability to “create the most effectively globalized event,” positioning itself as a genuine multinational media conglomerate (46).The following chapter focuses on the NBA venue itself, and Secular addresses the role of Silicon Valley firms, the consumption of public funds, and immersive technology in the historical development of NBA arenas. For instance, using the example of Golden 1 Center in Sacramento, Secular explores the present moment and the future of NBA stadium development. With enormous video displays, distinctive mobile apps, and the introduction of virtual reality technology, the Golden 1 Center exemplifies the evolution of the sports stadium into a new media spectacle. But Secular notes that such spectacles rely on public subsidies and have profound ethical costs. With the NBA's digitization of basketball comes a race to remain new and fresh, sparking never-ending “advancements”: “cycles of obsolescence and exploitation that are used to ensure profitability for the few at the expense of the many” (81).In chapter 3, Secular examines the wires, cables, and satellite infrastructure that enable the worldwide mediatization of basketball. This chapter offers a crucial description of how the NBA's production arm, NBA Entertainment (NBAE), managed to establish control over its own media manufacturing and circulation as early as the mid-1980s. Secular argues that this groundwork supported a global media infrastructure that could easily incorporate advances in communication technologies. Throughout the 1990s and early 2000s, the NBA used bourgeoning technology to distribute its products, from NBA League Pass to NBA.com TV to the current NBA Content Network. Secular argues that through these distribution responsibilities, the NBA fortified its place among contemporary major media conglomerates.Secular's fourth chapter concentrates attention on the NBA's executive operations and league office. Here, Secular argues that during the reign of the NBA commissioner David Stern, the league office prioritized “television and its global interests above all, acting as media company first and a basketball league second” (112). Executive office decisions played major roles in the NBA's international strategy. Regional NBA satellite offices were built across the globe, allowing the league to expand international events and extend the NBA's market research and efforts toward local branding. One way the NBA managed to engage with fans across the world was through localized television programs—using the same television format over and over again throughout the world while making small, localized changes for each location. Secular frames this use of television formats through the lens of imperialism, suggesting that the league works “to blend US and non-US interests in such a way as to craft a more marketable ‘global identity’” (129). In this sense, power is accumulated through market research, and such information is then fed into the television programming machine for the commercial advantage of the league and its sponsors.Secular uses his final site, the couch, to examine NBA viewers’ home-viewing experiences and the “increasing number of opportunities for global direct-to-consumer programming” (136). During a moment when audiences are shifting away from linear, cable television programming, the NBA has shifted its priorities in order to follow its fans’ interest in social media and streaming options. In a media landscape with endless entertainment options, the NBA has endeavored to capture fans’ attention through a myriad of options for viewers: “the launch of a cable multiplex to enhance viewer choice, . . . online fantasy sport to drive an emerging dot-com ecosystem, and . . . the recent investment in betting and the NBABet Stream feed” (163). As the home-viewing experience has become more fragmented, the NBA attempts to captivate viewers through as many screens, apps, and services as possible. Secular's text impressively synthesizes recent media history and NBA history, demonstrating how the league has positioned itself in the twenty-first century and for decades to come.

**Решение:** -2 эконометрический анализ влияния ставок на сбережения

---

### 127 · R7704

**The Italian National Competition Authority clears the acquisition of a licence for collecting sports bets without remedies (Sisal Match point)**

2008 · e-Competitions Bulletin · article · en

The Italian National Competition Authority decision number 19034, issued on 23 October 2008, evaluates a case of dominant position in the gaming and gambling market. Sisal Match Point S.p.A.…

**Решение:** -1 книга по истории ставок на спорт

---

### 128 · R1749

**Effects of Fit Between Promotional Message and Regulatory Focus on Consumers’ Sports Betting Behavior: The Moderating Role of Consumers’ Familiarity**

2025 · UNLV Gaming Research & Review Journal · article, journalarticle, journal-article · en · https://doi.org/10.9741/2327-8455.1519

The sports gambling industry is an extremely competitive market. To attract more consumers, sports gambling platforms are primarily employing one of two customer acquisition strategies, namely ‘risk-free bet’ or ‘bonus money’ welcome offers. This research is built on regulatory fit theory to investigate the effectiveness of these two welcome offer strategies on consumers’ intentions to act on the offer. We further test the moderating effect of customers’ familiarity with online sports betting on their decision making. Findings of two experimental design studies demonstrate that the presence of regulatory fit between regulatory focus and promotional offers (i.e., message framing) positively affected the likelihood that consumers would exploit both promotional offers. In addition, for individuals with low familiarity with a product category, achieving a fit between their regulatory focus and the message framing positively moderated their likelihood of exploiting promotional offers.

**Решение:** ? локальный опрос жителей, нет аннотации, проверить PG

---

### 129 · R2083

**Gambling Addiction among University Students**

2025 · Education and human development · book-chapter · en · https://doi.org/10.5772/intechopen.1008726

The prevalence of gambling disorder (GD) among university students has risen over the past two decades. Factors, such as Age, Availability, Accessibility, Acceptability, and Advertisement (the “5 As”), favor gambling behavior in this population. Although limited information exists outside the U.S., global meta-analyses report a 10.2% prevalence of GD among university students. Evidence shows the disorder significantly impacts students’ health and academic performance, being linked to low grades, course dropouts, and academic misconduct. This chapter explores the prevalence, phases, and risk factors of GD and its effects on the student’s academic performance. We also briefly discuss the available prevention strategies for gambling among this population.

**Решение:** -3 эксперимент по ставкам в лаборатории без шкалы PG

---

### 130 · R4951

**Is real-money mobile gaming a form of gambling or video gaming?**

2019 · PsyArXiv · article, other literature type, preprint · en · https://doi.org/10.31234/osf.io/9wp5h

Several new mobile video games have recently hit the market which allow players to wager real-world money on their in-game performance. For example, players of Strike! eSports Bowling can bet up to $60 before playing each game of ten-pin bowling, in the hopes of winning up to $100 in cash should they beat their opponent. Similarly, players of Block Blitz can place real money wagers on the outcomes of the Tetris-style puzzle games that they play. In the same vein, players of Pro Pool can stake real money on the chance of beating their opponent in a simulated game of 8 ball pool, in the hopes of winning a large cash prize. Real money stakes on this game range from $0.60 to $30.A significant amount of recent research has dealt with the emergence of links between gambling and video games. This attention has focused on topics as diverse as loot boxes, skin gambling, and esports betting. However, real-money mobile gaming has received little scrutiny.

**Решение:** -1 статья о коррупции в спорте и праве

---

### 131 · R5839

**Matched Betting Earnings**

2016 · article · en

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -2 моделирование подразумеваемой волатильности ставок

---

### 132 · R1066

**‘Out of sight, out of mind’ - results of a focus group study on gamblers’ use and evaluation of player protection measures in Germany**

2026 · BMC Public Health · article · en · https://doi.org/10.1186/s12889-026-26892-6

BACKGROUND: The growing prevalence of gambling-related problems underscores the importance of effective player protection measures and highlights gambling addiction prevention as a critical public health challenge. However, the perspective of gamblers has so far rarely been taken into account in the development of player protection measures in Germany. Furthermore, research indicates that gamblers’ awareness and use of available information and support services for gambling problems are relatively low to moderate. METHODS: To address this gap, a focus group study was conducted with a total of 19 gamblers to gather in-depth information into their views on player protection measures. Participants were screened for problem gambling behaviour using the Problem Gambling Severity Index prior to the discussions. Using a structured interview guide, participants were asked about their awareness and assessment of player protection measures as defined in the State Treaty on Gambling. They also evaluated various examples of both online and offline player protection information and suggested potential improvements. The interviews were recorded, transcribed and analysed through qualitative content analysis. RESULTS: Information and messages on player protection were barely noticed and did not address the actual information needs of gamblers. Participants reported that their memories of responsible gambling messages were often vague and superficial, many were unaware of available counselling services. The critique highlighted issues such as poor visibility on websites, excessive text content and the preponderance of advertising vs. responsible gambling messages. The study identifies key improvements for responsible gambling (RG) communication: increasing RG visibility, using concise messaging, including social media and videos, implementing interactive tools and personalized feedback, and employing proactive warnings. RG content should be developed by independent organizations to increase credibility. CONCLUSION: Including gamblers in the development of player protection measures and messages, along with identifying their information needs, can contribute to the evidence-based discussion on player protection and enhance its effectiveness.

**Решение:** -2 качественное исследование мотивов live-ставок

---

### 133 · R5098

**How to Play Strategically in Fantasy Sports (and Win)**

2018

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -3 исследование влияния рекламы ставок без инструмента PG

---

### 134 · R6449

**Football, Gambling, and Money Laundering**

2014 · Springer eBooks · article, book · en · https://doi.org/10.1007/978-3-319-05609-8

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? исследование фэнтези-спорта, нет аннотации, проверить PG

---

### 135 · R3686

**Analysis of U.S. Sports Betting Numbers—August 2021**

2021 · Gaming Law Review · article, editorial, journal-article · en · https://doi.org/10.1089/glr2.2021.29046.glr

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 архитектура программных систем для беттинга

---

### 136 · R5481

**South Australia’s gambling tax highlights the regulatory mess of online betting**

2017 · The Conversation Media Group Ltd · article, other, posted-content · en · https://doi.org/10.64628/aa.qgg45uc39

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** + опрос подростков, стадное поведение и проблемный гемблинг (шкала PG)

---

### 137 · R6467

**Betting with the Enemy: Changes in Sports' Attitude Towards Sports Betting**

2014 · XVIII ISA World Congress of Sociology (July 13-19, 2014) · article · en

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 репозиторий кода и скриптов

---

### 138 · R2342

**O AMPARO LEGAL E A VULNERABILIDADE DO USÚARIO DIANTE DE JOGOS DE AZAR**

2024 · JNT - Facit Business and Technology Journal · other literature type, article · pt · https://doi.org/10.5281/zenodo.12554394

O presente artigo discute o tema dos jogos de azar e dos cassinos online, analisando suas implicâncias no âmbito do direito penal, assim como um iminente avanço dessa modalidade virtual alternativa aos cassinos físicos, alavancado principalmente no período da pandemia. O objetivo principal deste trabalho é demonstrar a vulnerabilidade do jogador diante de um possível processo contra casas de jogos. Desta maneira, o objetivo é apresentar a evolução da Constituição em termos de entendimentos jurisprudenciais em relação ao tema em questão. Dessa forma, a metodologia utilizada trata-se de uma pesquisa de revisão bibliográfica, com cunho descritivo e qualitativa. Além disso, os resultados desta pesquisa demonstram um grande aumento nos cassinos online e a preocupação das entidades em disciplinar a matéria. Ademais, foi concluído que o ordenamento jurídico brasileiro, conquanto possua dispositivos dispersos, caminha para a normatização das apostas esportivas, além dos cassinos presenciais e virtuais, à medida que a sociedade requer a tutela jurisdicional do Estado. Palavras-chave: Jogos de azar. Cassino online. Apostas esportivas. Regulamentação. Pandemia.

**Решение:** -7 спам реклама ставок на Zenodo

---

### 139 · R4134

**Fiche 26. Les paris sportifs**

2020 · Cairn.info · book-chapter · fr

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 программное обеспечение для генерации фэнтези-команд

---

### 140 · R4982

**The unintended emergence of a greed-led economic system**

2018 · Kybernetes · article, journalarticle · en · https://doi.org/10.1108/k-01-2018-0018

Purpose This paper aims to propose a new model of economic behaviour in which activities are led by greed rather than by the traditional formal rules of capitalism. Design/methodology/approach This paper relies on the empirical observation of bad practices that developed in synchrony during the collapse of the former communist economic system and the rise of global financial capitalism. Both were fuelled by greedy behaviour of asset grabbing, and paved the way to an emerging greed-led economic system. Findings First, microeconomic individual greedy behaviours that drive asset grabbing are identified, such as rigged or corrupt privatisation drives, subprime mortgage loans, Ponzi schemes, lending to insolvent clients, bad loan securitisation, stock options, fraudulent accounting and online betting on fixed matches. Then systematic changes in the traditional formal rules of capitalism that favour those having adopted a greedy strategy are pointed at; greedy behaviour is institutionalised when these capture the state and successfully lobby for rules change. Contrary to capitalism, systemic greed uses asset grabbing, instead of capital accumulation, as its major means for wealth maximisation without constraint, in a winner-take-all economy beneficial to oligarchs. Research limitations/implications The implications of this new systemic behaviour have implications for further economic modelling. Practical implications The emergence of systemic greed will have implications for the design of regulatory systems. Originality/value This paper proposes that a greed-controlled economy is replacing the traditional capitalist economy.

**Решение:** -1 статья о проведении Спартакиады народов Китая

---

### 141 · R4033

**Sherman’s Wrath: Sports Data’s Impending Collision with Antitrust Law**

2021 · Indiana Magazine of History (Indiana University) · article · en

run.Another example follows in the case of baseball pitchers, such as New York Mets National League Cy Young Award winner Jacob deGrom.16 As a dominant pitcher, deGrom has the ability to change the dynamic of any game and, as previously mentioned, the betting lines.17 In August 2018, deGrom and the Mets faced off against fellow all-star pitcher Cole Hamels and the Chicago Cubs.18 The game went into the tenth inning, at which time MLB suspended play due to inclement weather.19 When play picked up the next day, a Las Vegas sportsbook noticed the current odds did not account for deGrom's departure in favor of lackluster Mets relief pitcher Paul Sewald, who sported an abysmal 5.00 Earned Run Average.20 It is likely that many bets were placed on the Cubs at much better odds than there would have been had the pitching change been accounted for, and sportsbooks likely lost thousands of dollars as a result.21 Technology startups, such as Motus, have begun to gather this invaluable data.22 The MLB recently entered into an agreement to allow teams to monitor their pitcher's performance using the MotusTHROW training platform.23 The MotusTHROW sensor sits below the pitcher's Ulnar Collateral Ligament, measuring "peak valgus torque on the arm."24 The sensor not only has the ability to measure pitching velocity but can also measure pitcher fatigue, telling teams when it is time to make a switch on the mound.25 Access to this information is valuable for players, teams, and sportsbooks alike.It is exactly this kind of advanced data that gives rise to the markets analyzed in this Note.Both the MLB and the NBA have entered into non-exclusive partnerships with previously mentioned "official game data suppliers."26 While the NBA's official non-exclusive agreements are with the companies Sportradar and Genius Sports, 27 the MLB signed a non-exclusive deal with only Sportradar (with 16 See

**Решение:** -2 модель ставок на ежедневный фэнтези-бейсбол

---

### 142 · R1965

**The influence of sports betting sentiment on household savings**

2025 · Research Square · article, preprint, posted-content · und · https://doi.org/10.21203/rs.3.rs-7851656/v1

Abstract I use the Brazilian setting to investigate whether online searches on sports betting are a consistent measure of sports gambling sentiment and whether they can influence household savings. I find that searches are significantly concentrated on match days and during football season periods. I also document that the proportion of search volumes is negatively correlated with states’ GDP, HDI, and level of education. This finding indicates that poorer regions gamble more. Moreover, I report that online searches negatively predict future household savings at the country level. More specifically, the increase in online searches from a typical day with no football matches to a typical match day produces a decrease in national household savings of 2.0 MM BRL (400,000 USD) in the following four days. This influence is robust to a battery of tests. Overall, these results indicate that online searches are a consistent proxy for sports gambling sentiment and suggest that online sports betting is linked to negative economic outcomes at the country level. JEL Classification: D14, G51

**Решение:** -1 психиатрический комментарий к диагностике гемблинга

---

### 143 · R8436

**Sport and the British**

1990 · Oxford University Press eBooks · book · en · https://doi.org/10.1093/acprof:oso/9780192852298.001.0001

Abstract This history goes beyond the great names and moments to explain how British sport has changed since 1800, and what it has meant to ordinary people. It shows how the way we play reflects not just our lives as citizens of a predominantly urban and industrial world, but what is especially distinctive about British sport. Innovators in abandoning traditional, often brutal sports, and in establishing a code of ‘fair play’, the British were also pioneers in popular sports and in the promotion of organized spectator events. Modern media coverage of sport, gambling, violence, and attitudes towards it; nationalism; and the role of sport in sustaining male identity are also explored, and the book is rich in anecdotes, which it combines with a serious historical understanding of the subject at hand.

**Решение:** -1 бизнес-диагностика операторов ставок

---

### 144 · R5711

**Motives for gambling in sports betting among Gweru residents**

2016 · article · en

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 стратегический анализ индустрии беттинга

---

### 145 · R4532

**People’s Preference to Bet on Home Teams Even When Losing is Likely**

2020 · Journal of Emerging Investigators · article, journalarticle, review · en · https://doi.org/10.59720/19-035

One intriguing phenomenon is when people make bets that seem to go against their better judgement. This can be seen in sports betting. In this paper, we report a survey-driven study that investigates if people bet more on their home teams, both in scenarios where the team is leading and scenarios where the team is likely to lose. We asked participants to imagine betting with $10,000 on different scenarios. We compared how much they bet on their home teams versus how much they bet on neutral teams in the same circumstance. On average, participants bet slightly more on their home teams than a neutral team when their home team was leading. Participants, however, bet significantly more on their home teams than the neutral teams when their team was facing a large deficit. This study can help explain some more impulsive betting behaviors that might be due to information avoidance.

**Решение:** -1 политический отчет об азартных играх в Уганде

---

### 146 · R4448

**Corruption in the field of international and Russian sport**

2020 · Russian Journal of Legal Studies (Moscow) · article · en · https://doi.org/10.17816/rjls33992

The article is a response to the current scientific research of Professor S. V. Maksimov, dedicated to the problems of corruption in the field of international sports. Analyzing the conceptual apparatus, such categories as "sports competition", "organizer of sports competition", exploring the range of unofficial and official international sports events, the status of the organizers of international official sports competitions and paying attention to corruption factors in the activities of the International Olympic Committee, S. V. Maksimov, limited by the scope of his work, is forced to ignore the activities of international sports federations and national Olympic committees. The author fills this gap by analyzing the activities of the Russian Olympic Committee, the International swimming Federation, and the all-Russian swimming Federation. Supporting the thesis of S. V. Maksimov that athletes are the "weak side" of the Olympic movement, whose rights and legitimate interests are not properly guaranteed, the author identified the problems of mass sports in Russia, the difficulties of material and technical support for sports teams, the lack of funding for swimmers in the regions, the lack of sports schools and sports pools, flaws in the legislative regulation of assigning sports categories. Such problems are partly caused by corruption in Russian sports and generate injustice. The author agrees with S. V. Maksimov position that it is necessary to adopt a comprehensive UN Convention on sport and improve anti-corruption criminal law bans in the criminal code of the Russian Federation. It also seems appropriate to adopt the principles and provisions of the new Code of ethics of the International Olympic Committee, adopted in 2017, at the national and regional level.

**Решение:** + лонгитюдное исследование подростков, ставки на спорт и шкала PG

---

### 147 · R2077

**Fear of missing out’s mediating role in sensation-seeking and online betting intentions: impact of sales promotions**

2025 · Sport Business and Management An International Journal · article, journalarticle, review · en · https://doi.org/10.1108/sbm-05-2024-0054

Purpose This research investigates the complex relationships between individual psychological traits, the fear of missing out (FOMO) and sales promotions in the online sports betting industry. Specifically, it aims to comprehend how sensation-seeking, as a personality trait and FOMO influence the intention to engage in instant online sports betting under various sales promotions like win-bet boosting and lose-bet protecting. Design/methodology/approach An online survey was conducted with USA adults familiar with major online betting platforms. Participants were assigned to different promotional scenarios, and their responses were analyzed using partial least squares structural equation modeling (PLS-SEM). Findings The findings show that sensation-seeking positively affects betting intentions, with FOMO playing a partially mediating role. Sales promotions were found to negatively moderate the relationship between sensation-seeking and betting intention. Notably, the impact of FOMO on betting intention was stronger in the lose-bet protecting scenario than in the win-bet boosting scenario. Originality/value This research enriches existing literature by elucidating the nuanced interactions between sensation-seeking, FOMO and sales promotions in the context of online sports betting. The study offers practical insights for developing targeted marketing strategies, particularly for users inclined towards sensation-seeking.

**Решение:** -2 модель прогнозирования продаж спортивной лотереи

---

### 148 · R7484

**The Fantasy Sport Experience: Motivations, Satisfaction, and Future Intentions.**

2010 · article · en

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -2 алгоритмическая торговля на биржах спортивных ставок

---

### 149 · R5338

**The empirical effects of competition on third‐degree price discrimination in the presence of arbitrage**

2017 · Canadian Journal of Economics/Revue canadienne d économique · article · en · https://doi.org/10.1111/caje.12285

Abstract Since Borenstein and Holmes, a theoretical and empirical literature has emerged that examines the effects of competition on third‐degree price discrimination. Since transaction costs involved in conducting arbitrage are typically unobserved, empirical investigations in this area have largely been restricted to markets such as for air travel where arbitrage is difficult, if not impossible. Using an entirely novel dataset, this paper documents the effect of competition on price discrimination in the presence of arbitrage in the Canadian online sports betting market where prices for Canadian teams are higher than in the world market. I observe how the prices of Canadian teams change in real time in response to the presence of arbitrageurs that establish Canadian sportsbooks’ observable marginal opportunity costs. I exploit the existence of government betting outlets not subject to arbitrage to obtain reduced form counterfactual estimates of the extent to which competition affects price discrimination in the presence of arbitrage. In this new empirical environment, I find results consistent with the airline literature: competition reduces overall price dispersion and markups, but dispersion and markups shrink more for those in the “strong” market than the “weak” market.

**Решение:** -3 поведенческий трекинг онлайн-игроков без шкалы PG

---

### 150 · R2673

**XGBoost Learning of Dynamic Wager Placement for In-Play Betting on an Agent-Based Model of a Sports Betting Exchange**

2024 · Elsevier BV · posted-content, preprint · en · https://doi.org/10.2139/ssrn.4691617

We present first results from the use of XGBoost, a highly effective machine learning (ML) method, within the Bristol Betting Exchange (BBE), an open-source agent-based model (ABM) designed to simulate a contemporary sports-betting exchange with in-play betting during track-racing events such as horse races. We use the BBE ABM and its array of minimally-simple bettor-agents as a synthetic data generator which feeds into our XGBoost ML system, with the intention that XGboost discovers profitable dynamic betting strategies by learning from the more profitable bets made by the BBE bettor-agents. After this XGBoost training, which results in one or more decision trees, a bettor-agent with a betting strategy determined by the XGBoost-learned decision tree(s) is added to the BBE ABM and made to bet on a sequence of races under various conditions and betting-market scenarios, with profitability serving as the primary metric of comparison and evaluation. Our initial findings presented here show that XGBoost trained in this way can indeed learn profitable betting strategies, and can generalise to learn strategies that outperform each of the set of strategies used for creation of the training data. To foster further research and enhancements, the complete version of our extended BBE, including the XGBoost integration, has been made freely available as an open-source release on GitHub.

**Решение:** -1 новостной обзор законодательства о ставках на спорт
