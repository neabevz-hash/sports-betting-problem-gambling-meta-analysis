# Калибровка вслепую, часть 3

Калибровка вслепую, часть 3: записи 301–400 из 400. Это случайные 400 записей из 7728 в списке к отбору финального поиска 2026-10-18 (зерно 20261018, порядок случайный). **Меток ИИ здесь нет.** Размечайте в любом порядке и в несколько заходов. Когда закончите все части, скажите: я проверю, что всё размечено, и закоммичу файлы до того, как открою метки ИИ.

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

### 301 · R5922

**Abnormal returns in an efficient market? Statistical and economic weak form efficiency of online sports betting in European soccer**

2016 · Aaltodoc (Aalto University) · dissertation · en

Online sports betting markets have expanded significantly during the recent decade. At the same time, due to their apparent similarities with traditional financial markets, the academic literature has perceived sports betting markets as a suitable empirical setting for different tests of efficiency. Employing a data set more extensive than in any previous relevant study, this thesis investigates weak form efficiency of online sports betting in European soccer between seasons 2009 and 2014 from two perspectives: statistical and economic. The statistical tests examine whether subjective probability indicated by average market odds is an unbiased estimator of objective outcome probability. Economic tests, representing the stricter tests of efficiency, inspect whether any betting strategy yields positive returns, utilizing highest odds quoted in the market. The statistical tests find clear evidence of a persistent favorite-longshot bias and hence of statistical weak form betting market inefficiency. On the aggregate level, both the linear and logit regression models reveal that as the subjective probability of an outcome increases, the objective probability increases more than implied by market efficiency. On the individual odds level, the technique that sorts odds into groups based on subjective probability discovers that the deviations between subjective and objective probability occur on both perimeters of the odds spectrum, not in the middle of it. Thus, in a statistical sense, the betting market appears to be weak form inefficient at high respective low probabilities, while being efficient in between. The economic tests give a more ambiguous view on weak form efficiency. When considering all the matches in the sample, neither the tobit regression model nor any of the naïve strategies show chances for profitable betting, while some of the odds groups with highest subjective probability demonstrate moderately positive returns. When only including matches with a positive expected value and simulating the associated returns, the sophisticated strategy based on quasi-arbitrage yields no profits, but the strategy that takes into account the favorite-longshot bias generates consistent profits. Therefore, the betting market seems to be inefficient also in an economic sense. The study concludes that the European online sports betting market in soccer is weak form inefficient. The results are consistent with the earlier literature in terms of statistical efficiency but not in terms of economic efficiency. Due to the lower bookmaker margins in the current market, it is shown that well known statistical biases now also lead to economic inefficiency. The study provides two explanations for the persistence of these inefficiencies: institutional arrangements and market immaturity. Since sports betting markets are not yet as sophisticated as many financial markets, they provide attractive investment opportunities for sharp bettors.

**Решение:** -2 статистическая эффективность рынка ставок на английский футбол

---

### 302 · R1930

**Score Predictor: Predição de Resultados no Futebol Usando Programação Lógica**

2025 · Anais do VI Workshop Brasileiro de Lógica (WBL 2025) · article, conference-paper · pt · https://doi.org/10.5753/wbl.2025.8333

O Score Predictor é um sistema de previsão de resultados de partidas de futebol, desenvolvido em Prolog e testado durante o Campeonato Brasileiro de 2024. Seu objetivo é apoiar decisões em apostas esportivas, estimando probabilidades de vitória, empate e derrota com base em um modelo lógico-estatístico. O sistema utiliza dados de um banco especializado e permite a inserção de parâmetros adicionais por meio de um menu interativo. A modelagem combina fatores estatísticos e contextuais, permitindo inferências automatizadas. Os testes realizados demonstraram desempenho satisfatório na previsão dos resultados. A proposta evidencia a viabilidade do uso de lógica declarativa em aplicações de análise esportiva.

**Решение:** -2 логическое программирование на Prolog для прогнозирования исходов матчей

---

### 303 · R8585

**NFL betting market efficiency, divisional rivals, and profitable strategies**

RePEc: Research Papers in Economics · article · https://doi.org/10.1108/sef-11-2018-0354.html?utm_source=repec&utm_medium=feed&utm_campaign=repec

Purpose - This paper aims to examine market inefficiencies in the National Football League (NFL) betting market from the 2003 season to the 2016 season. Design/methodology/approach - The author examines the impact that division rivals and previously known determinants of inefficiencies have on the current NFL gambling market. Findings - The results show that games against division rivals have a lower chance of the home team covering the spread and the chance the game will result in an over. This result demonstrates that the sportsbooks underestimate the familiarity that teams have with each other’s players, coaches and tendencies from playing each other twice per year. Moreover, using this result in conjunction with previous known inefficiencies, the author puts forth a model to test out of sample predictions. The results from these tests show profitable strategies in the point spread and totals market with a win rate of nearly 57 per cent. Originality/value - Overall, this paper demonstrates inefficiencies in the NFL betting market that future bettors may be able to take advantage of.

**Решение:** -2 эффективность рынка ставок на матчи дивизионных соперников в НФЛ

---

### 304 · R6905

**Internet Gambling: Current Research Findings and Implications**

2012 · Cross Connect (Southern Cross University) · review, book · en · https://doi.org/10.1007/978-1-4614-3390-3

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 монография / обзор исследований интернет-гемблинга

---

### 305 · R6381

**A neurocognitive examination of impulsivity, inhibitory control and decision making in problem gambling**

2014

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? нейрокогнитивное исследование проблемных игроков, нет аннотации, проверить полный текст

---

### 306 · R1776

**Sports Betting And Legal Implications In India: The Regulation Of Gambling And Match-Fixing In Sports**

2025 · International Journal of Research Pedagogy and Technology in Education & Movement Sciences · article · en

Sports betting in India have grown significantly with the rise of digital platforms, yet it remains largely unregulated under national law. The lack of a unified legal framework has led to illegal betting networks and match-fixing scandals, affecting the integrity of Indian sports. This paper examines the existing legal landscape, key match-fixing cases, and regulatory challenges. It also explores global best practices and proposes reforms, including a centralized legal structure, stricter monitoring mechanisms, and player protection policies to ensure fair and transparent sports betting regulations in India.

**Решение:** -1 правовой анализ регулирования ставок и договорных матчей в Индии

---

### 307 · R2319

**Examining the causal pathways from impulsivity to disordered gambling in online sports betting**

2024 · Peer Community In Registered Reports · journalarticle, review, article · en · https://doi.org/10.24072/pci.rr.100574

A recommendation of: Anne Jacob, Mohsen Joshanloo, Robert Czernecka, Anja Kräplin, Impulsivity and online sports betting behaviour: Untangling the causal relationship (ISPO study) http://dx.doi.org/10.23668/psycharchives.14372

**Решение:** -1 рецензия / рекомендация на зарегистрированный отчет по импульсивности и ставкам

---

### 308 · R5168

**Sports Bettors: A Systematic Review**

2018 · Journal of Gambling Issues · article, review, journal-article · en · https://doi.org/10.4309//jgi.2018.38.11

Sports betting is associated with problematic gambling behaviours. However, little is known about the profile of sports bettors. Also, it is still unclear if there are useful abilities in sports betting. This systematic review aims to describe gambling habits and cognitions of sports bettors, and determine the roles of chance and skill in sports betting. Addressing the chance and skill distinction in sports betting would be helpful to identify which of sports bettors' cognitions are erroneous. Out of 991 studies identified in the databanks, 31 met the inclusion criteria of this review. Results indicate that these studies are mostly conducted with male samples aged from 30 to 50 years. These gamblers bet many times per week, with weekly averages ranging from 100 to 200$ CAD. Five studies examined the roles of chance and skill in sports betting, among which three showed that sports bettors perform better than chance in predicting results accurately, but they do not win more money than they would with a random selection, due to the structure of the game. The 11 studies that focused on cognitions indicate that sports bettors overestimate the influence of skill on the outcome of the game. These results support the need to further study the role of cognitions in the behaviours of sports bettors. It also offers insights concerning the distinction between chance and skill in sports betting.RésuméLes paris sportifs sont associés à des comportements de jeu problématiques. Cependant, on sait peu de choses sur le profil des parieurs sportifs. De plus, il est difficile de statuer si certaines habiletés seraient utiles dans les paris sportifs. Cette revue systématique vise à décrire les habitudes de jeu, les cognitions des parieurs sportifs, et à déterminer le rôle du hasard et des habiletés dans ces paris. Examiner la distinction entre le hasard et les habiletés aux paris sportifs serait utile afin de déterminer quelles cognitions entretenues par les parieurs sportifs sont erronées . Sur 991 études repérées dans les banques de données, 31 répondaient aux critères d’inclusion de cette revue. Les résultats indiquent que ces études sont principalement menées auprès d’échantillons masculins âgés de 30 à 50 ans. Ces joueurs parient plusieurs fois par semaine et misent en moyenne de 100 $ à 200 $ CA par semaine. Cinq études ont examiné les rôles du hasard et des habiletés dans les paris sportifs, parmi lesquels trois ont montré que les parieurs sportifs prédisent mieux les résultats sportifs que le hasard, mais ils ne gagnent pas plus d’argent qu’avec une sélection aléatoire, en raison de la structure du jeu. Les onze études portant sur les cognitions indiquent que les parieurs sportifs surestiment l’influence des habiletés sur l’issue du jeu. Ces résultats confirment la nécessité d’approfondir le rôle des cognitions dans les comportements des parieurs sportifs. Ils donnent également des pistes sur la distinction entre le hasard et les habiletés dans les paris sportifs.

**Решение:** -1 систематический обзор характеристик спортивных беттеров

---

### 309 · R3950

**Structural characteristics of fixed-odds sports betting products.**

2021 · Journal of behavioral addictions · article, journal article, review · eng · https://doi.org/10.1556/2006.2021.00008

Abstract Background and aims A literature exists on the structural characteristics of electronic gambling machines (EGMs), which are design innovations that can promote spending excessive time and money on these games. Fixed-odds sports betting products, where bettors place sports bets against a bookmaker, have also seen significant innovations in recent years. Despite some differences between these gambling products, similar structural characteristics could also be relevant to sports betting. The aim was to review previous research on contemporary fixed-odds sports betting products, and to identify whether structural characteristics from the EGM literature are also relevant to sports betting. Methods Structural characteristics uncovered by two influential reviews of EGMs were identified, and their relevance to fixed-odds sports betting products discussed via a narrative review. Results Structural characteristics of payout interval and potential betting frequency (in-play betting), multiplier potential (accumulators, complex bets, multis), win probability and payout ratio (all bets), bettor involvement (custom sports betting products, cash out), skill required (all bets), and near-misses (accumulators, complex bets, multis) were all identified in modern fixed-odds sports betting products. Discussion and conclusions Fixed-odds sports betting products have increasingly incorporated structural characteristics previously found in EGMs. Future research could further assess the extent to which these structural characteristics contribute to fixed-odds sports bettors spending excessive amounts of time and money while betting. These findings can help guide further sports betting research, contribute to an improved understanding of the potential universality of gambling product design, and inform policy.

**Решение:** -1 систематический обзор структурных характеристик ставок с фиксированными коэффициентами

---

### 310 · R6858

**Sport in Europa: Autonomie und Kommerzialisierung – einige Aspekte vorweg**

2012 · Edition HWWI · part of book or chapter of book, book-chapter · de · https://doi.org/10.15460/hup.213.1561

Die Autonomie des Sports, die verfassungsrechtlich verbrieft ist, wird durch das Gemeinschaftsrecht der EU nicht konsequent respektiert. So wird beklagt, dass die notwendige Kooperation der Verbände im Sport nicht hinreichend berücksichtigt wird. Hier setzen die Referenten des 9. Internationalen Hamburger Symposiums „Sport und Ökonomie“ an, wenn sie rechtliche und ökonomische Fragen um Sportgroßveranstaltungen aufgreifen und Vorschläge zur Stellung des Sports im europäischen Rahmen diskutieren. Aufgezeigt wird , dass der sogenannte Sport ökonomisch geprägt wird, was noch keine angemessene Entsprechung auf europäischer Ebene gefunden hat. Das wird zum Beispiel bei Sportwetten und dem Glücksspielmonopol deutlich. Der Band wird die durch das EU-Weißbuch Sport und die Entschließung des Bundestages zum Sport in Europa entstandene Debatte weiter beleben. The autonomy of sport which is constitutionally recognised is not consistently respected by EU law. There are complaints that the necessary cooperation of the federations in sport is not sufficiently taken into account. This is where the speakers of the 9th International Hamburg Symposium "Sport and Economics" come in when they address legal and economic questions about major sporting events and discuss proposals on the status of sport in the European context. It shows that sport is economically shaped, which has not yet found an adequate equivalent at European level. This is evident, for example, in sports betting and the gambling monopoly. The volume will further stimulate the debate created by the EU White Paper on Sport and the Bundestag resolution on sport in Europe.

**Решение:** -1 вводная статья сборника о коммерциализации европейского спорта

---

### 311 · R7790

**Price Setting in the NBA Gambling Market: Tests of the Levitt Model of Sportsbook Behavior**

2008 · International Journal of Sport Finance · journalarticle, article · en · https://doi.org/10.1177/155862350800300302

Levitt (2004) suggested that sportsbooks do not set prices in the NFL to clear markets, as was commonly assumed, but set prices to maximize profits. This paper uses actual betting data from four sportsbooks to test the Levitt (2004) hypothesis in the NBA. For a sample of the 2004-05 to 2006-07 seasons, it is shown that favorites receive a disproportionate share of NBA pointspread bets. In addition, the percentage of bets the favorite receives increases with each additional point of the pointspread. In the totals market, it is shown that overs receive a much higher percentage of bets compared to unders and the percentage bet on the over increases with each point of the total. Unlike the NFL, however, taking a contrarian position and betting against public sentiment is not found to win more often than implied by efficiency.

**Решение:** -2 тестирование модели ценообразования букмекеров Левитта в НБА

---

### 312 · R7165

**US Collegiate Athletics**

2011 · ASSER international sports law series · review, book-chapter · en · https://doi.org/10.1007/978-90-6704-799-9_54

This book looks at the Law and Policy on Betting and Sport in many countries around the world––sport is a global phenomenon––providing a very useful and valuable comparative survey on a subject that is so vital for safeguarding and preserving the integrity of those sports in which betting is legally allowed.The country reports show how sports-related betting is organized in the country concerned, also from a historical and policy perspective (national Lotteries Act; state run/state licensed lotteries and/or private operators; how the licensing system for public operators works; state supervisory mechanisms, etc.), and contain a treatment of the national case law. These keywords were added by machine and not by the authors. This process is experimental and the keywords may be updated as the learning algorithm improves.

**Решение:** -1 правовой обзор студенческого спорта и ставок в США

---

### 313 · R2054

**APOSTAS ESPORTIVAS, LAVAGEM DE CAPITAIS E O CRIME ORGANIZADO**

2025 · Direito e Humanidades · article, journalarticle, journal-article · und · https://doi.org/10.13037/dh.n30.9811

The growth of sports betting in recent years presents significant challenges, particularly regarding money laundering and the infiltration of organized crime. This article analyzes how betting platforms, often unregulated, are utilized to facilitate illegal activities, including money laundering. Additionally, the complexity of the relationship between gambling regulation and corruption is highlighted, underscoring the need for a robust approach that considers the transnational nature of betting operations. The research discusses the vulnerabilities of the sector, proposes regulatory improvements, and emphasizes the importance of effective international cooperation to address associated risks.

**Решение:** -1 юридический анализ спортивных ставок, отмывания денег и оргпреступности

---

### 314 · R7226

**我国体育彩票问题彩民现状调查——以上海、广州、郑州、沈阳、成都为例**

2011 · Acta Scientiarum Naturalium Universitatis Sunyatseni · article · zh

彩票机构要承担和履行更多的社会责任,发扬彩票发行的正面影响、遏制负面影响,其中很重要的一点就是对问题彩民、潜在问题彩民进行有效的甄别与救助。研究初步制定出了适合我国国情的问题彩民甄别量表,通过对5个城市的调查较全面地了解了我国体育彩票问题彩民的现状,并在调查基础上提出了对策建议：完善体育彩票游戏规则;加大体育彩票公益宣传力度;加强对彩民购彩的正确引导;构建彩民救助机制。

**Решение:** + количественный опрос игроков спортивной лотереи в 5 городах Китая с инструментом скрининга проблемной игры

---

### 315 · R5341

**Gambling and sport**

2017 · Routledge eBooks · book-chapter · en · https://doi.org/10.4324/9781315184739-11

Gambling is nearly as old as civilization itself. The significance of gambling, and particularly sports gambling, in modern society is apparent to even the most casual observer. Laws forbidding gambling by the masses on workdays were designed to keep people working rather than wagering. Just as gambling and gambling regulation went hand-in-hand, so did gambling and sports. Some ambiguity is inherent in all definitions of gambling, including statutory definitions. Even trading in the stock market has been used as an example of a form of legal gambling. In the United States, there is no shortage of federal and state legislation designed to prohibit or control gambling, including sports gambling. Every state has laws banning or regulating gambling, and all but one have laws which criminalize sports gambling. Some professional teams have even banned gambling by players during team flights. Season-long fantasy sports gambling did more than jump-start the growth of sports gambling in the 1980s and 1990s.

**Решение:** -1 академический обзор связей между спортом и гемблингом

---

### 316 · R7321

**Sports betting – International sports betting services**

2011

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 глава серии по международному спортивному праву

---

### 317 · R5958

**2016年“公益体彩 快乐操场”报名开始啦——河南省体彩中心将再为省内25所学校捐赠体育器材**

2016 · 少林与太极 · article · zh

5月26日上午,＂公益体彩快乐操场＂2016年河南省启动仪式在河南省体育彩票管理中心举行,＂公益体彩快乐操场＂报名工作也正式拉开帷幕。据河南省体育彩票管理中心副主任韩宇、主任助理董小卫介绍,今年河南省体彩中心将对河南省25所公立小学进行捐赠,每所受捐赠的小学将获得价值2万元的＂公益体彩快乐操场＂的免费体育器材。

**Решение:** -6 новостная заметка о благотворительной передаче спортивного инвентаря

---

### 318 · R6705

**Problem gambling among international and domestic university students in Australia: who is at risk?**

2013 · Journal of gambling studies · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1007/s10899-012-9309-x

Young people are a high risk group for gambling problems and university (college) students fall into that category. Given the high accessibility of gambling in Australia and its association with entertainment, students from overseas countries, particularly those where gambling is restricted or illegal, may be particularly vulnerable. This study examines problem gambling and its correlates among international and domestic university students using a sample of 836 domestic students (286 males; 546 females); and 764 international students (369 males; 396 females) at three Australian universities. Our findings indicate that although most students gamble infrequently, around 5 % of students are problem gamblers, a proportion higher than that in the general adult population. Popular gambling choices include games known to be associated with risk (cards, horse races, sports betting, casino games, and gaming machines) as well as lotto/scratch tickets. Males are more likely to be problem gamblers than females, and almost 10 % of male international students could be classified as problem gamblers. Hierarchical regression analysis showed that male gender, international student status, financial stress, negative affect and frequency of gambling on sports, horses/dogs, table games, casino gaming machines, internet casino games and bingo all significantly predicted problem gambling. Results from this study could inform gambling-education programs in universities as they indicate which groups are more vulnerable and specify which games pose more risk of problem gambling.

**Решение:** + количественное исследование 1600 студентов в Австралии с измерением проблемного гемблинга и ставок на спорт

---

### 319 · R8150

**发行“农基彩”如何?**

2004 · 人民政坛 · article · zh

人大、政协两会的召开,让群众看到了希望的曙光,但仅靠政府的力量要解决好农村的事是远远不够的,特别是农村公共基础设施建设。建议以省为单位,像销售体育彩票、福利彩票那样,每天销售农村公共基础设施建设彩票(农基彩),集聚全社会的力量加上政府的力量来解决给予农民国民待遇的问题。

**Решение:** -6 предложение о выпуске лотереи на сельскую инфраструктуру, не спорт

---

### 320 · R1595

**Sports betting, alcohol problems follow similar trajectories: Study**

2025 · Alcoholism & Drug Abuse Weekly · article, journalarticle, journal-article · en · https://doi.org/10.1002/adaw.34447

Research evidence continues to suggest that sports bettors carry an elevated risk of alcohol‐related problems, with a newly published longitudinal study showing similar trajectories between gambling frequency and alcohol problems. There is even some evidence that problematic drinking levels are more prevalent among sports gamblers than among gamblers who don't wager on sports.

**Решение:** -1 новостной дайджест о связи между ставками на спорт и алкоголем

---

### 321 · R5810

**A Markovian Approach**

2016

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -2 марковские модели в спортивной аналитике без опроса людей

---

### 322 · R1603

**More frequent use of live sports-betting features is associated with increased risk of gambling harm: evidence from a case- control design**

2025 · PsyArXiv · preprint, posted-content · en · https://doi.org/10.31234/osf.io/je38f_v1

BackgroundMany theories of gambling harm propose that interactive design features of sports-betting platforms confer risk of harm by enabling cyclical patterns of repeated gambling engagement. This exploratory study investigated whether such features were used more frequently by people at higher risk of gambling harm relative to a demographically matched lower-risk control group.MethodsThis study used a case-control design to compare a group of 85 people at higher risk of gambling harm (PGSI 5+) with an age- and gender-matched control group at lower risk of harm (n = 84, PGSI 0-4). We compared the frequency with which groups self-reported using in-play betting, instant cash-out, multi and micro bets, social betting, and viewing live-streamed events within a betting app.ResultsThe higher-risk group reported more frequent use of in-play betting and instant cash-out and were more likely to report streaming live sporting events within a betting app. Higher-risk participants were also more likely to make an immediate deposit to qualify for a marketing offer, and both groups reported being more likely to make risky bets when using bonus funds. We observed no group differences in the frequency of use of multis, micro-bets, or social betting.ConclusionsOur findings were broadly consistent with the theory that design features of modern betting platforms contribute to gambling harm by facilitating continuous engagement. A notable finding was that in-app streaming of live events was more common among people at higher risk of gambling harm, consistent with a novel prediction made by the motivating theory.

**Решение:** -5 исследование дизайна случай-контроль по степени риска гемблинга

---

### 323 · R6961

**Assessing corporate social responsibility in China's sports lottery administration and its influence on consumption behavior.**

2012 · Journal of gambling studies · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1007/s10899-011-9270-0

The purpose of this study was to identify and examine consumer perception of corporate social responsibility (CSR) in China's sports lottery industry, and the effect of perceived CSR initiatives on sports lottery consumption behavior. Research participants (N = 4,980), selected based on a computer-generated, randomly stratified multistage sampling process, comprised Chinese residents who had purchased sports lottery tickets in the past 12 months. They completed a questionnaire that was derived from a qualitative research process. A factor analysis extracted two factors associated with perceptions of CSR in China's sports lottery administration: Regulatory and Prevention Responsibilities and Product Development Responsibility. Logistic regression analyses revealed that these two factors were influential of consumer behavior (i.e., relative and absolute expenditure, purchasing frequency, and time commitment). This study represents an initial effort to understand the dimensions of perceived CSR associated with Chinese sports lottery. The findings signify the importance of enforcing CSR in sports lottery administration.

**Решение:** ? опрос 4980 покупателей спортивной лотереи о КСО и потреблении, проверить наличие инструмента PG в полном тексте

---

### 324 · R7030

**Predicting the outcomes of tennis matches using a low-level point model**

2012 · IMA Journal of Management Mathematics · article · en · https://doi.org/10.1093/imaman/dps010

Quantitative analysis in tennis has become more important in recent years with the introduction of online betting exchanges. In this paper, the probability of winning a match in tennis is derived hierarchically starting from the probability of each player winning a point on their serve. Under the assumption that each point is identically and independently distributed, the probability of each player winning a point when serving and when returning serve is derived using player statistics. These probabilities can be used to calculate probabilities of winning a game, a set and consequently the match from any point in a live game. Simulated results are then tested against real-world data and compared against existing models in the literature.

**Решение:** -2 вероятностная модель прогнозирования теннисных матчей на бирже ставок

---

### 325 · R6029

**The eSports Trojan Horse: Twitch and Streaming Futures**

2015 · Journal For Virtual Worlds Research · journal-article · https://doi.org/10.4101/jvwr.v8i2.7176

This paper argues that one potential future in gaming and virtual reality can be found in streaming media and technology. The streaming space of Twitch.tv is both “real” and “virtual”, blurring the boundaries between the game space, social networks, and face-to-face communication. Streaming ruptures a hard distinction between the real and virtual worlds. Scholars of virtual spaces need to take seriously streaming media as a site of research, and the affordances of streaming as networked, mobile, and curated. Twitch represents a space for unpacking the social and commercial realizations of an emergent streaming culture. Virtual world research needs to continue to push the boundaries of research into games and gaming culture. We argue that an important part of that future involves the liminal space of streaming and eSports between the real and the virtual.

**Решение:** -6 медиаисследование стриминговой платформы Twitch, не гемблинг

---

### 326 · R0504

**Diamond Exchange New ID ₥₥ +91-7891725783 ₥₥ Online betting ID provider In Mangaluru**

2026 · ResearchHub Technologies, Inc. · casereport, report · und · https://doi.org/10.55277/researchhub.itv65p39

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -7 коммерческий спам на ResearchHub

---

### 327 · R4447

**Market Efficiency and the Setting of Salaries for NBA Daily Fantasy on FanDuel and Draft Kings**

2020 · The Journal of Prediction Markets · article, journal-article · en · https://doi.org/10.5750/jpm.v14i2.1813

The market for daily fantasy sports for the NBA is examined with respect to efficiency when pricing player salaries for the games. Simple factors such as home court advantage, rest, and opponent are shown to significantly effect performance beyond posted salaries in the respective markets. In addition, a “hot hand” effect is found in that players that exceed expectations in previous games are shown to outperform salary-based expectations in the next contest. These factors yield a rejection of market efficiency as it relates to salaries in the marketplace. Legal ramifications for these contests as games of skill are examined.

**Решение:** -2 эффективность рынка и установление зарплат в NBA Daily Fantasy без опроса людей

---

### 328 · R1281

**Shared and Distinct Neural Signatures of Cue-Induced Response in Substance and Behavioral Addictions: A Coordinate-Based Neuroimaging Meta-Analysis**

2026 · medRxiv · preprint · https://doi.org/10.64898/2026.01.23.26344591

Abstract As the global burden of addiction intensifies, the neurobiological commonalities and distinctions between substance use disorders (SUDs) and behavioral addictions (BAs) remain poorly characterized. This coordinate-based meta-analysis of 59 fMRI articles (n = 2,951) mapped the neural signatures of visual cue-reactivity across the addictive disorders. Our results revealed a universal core network shared by SUDs and BAs centered in the bilateral opercular inferior frontal gyrus, suggesting a shared disruption in inhibitory control. Distinctively, SUDs exhibited a stronger recruitment of a subcortical salience pathway, with greater involvement of the left thalamus ventral anterior nucleus than BAs, potentially reflecting pharmacologically amplified bottom-up salience attribution. Notably, recovery-related patterns diverged in the left medial superior frontal gyrus. Alcohol use disorder was associated with neural restoration, whereas heroin use disorder showed neural decompensation. These neural signatures establish a rigorous neurobiological basis for differentiating substance and behavioral phenotypes, supporting tailored circuit-based precision treatments.

**Решение:** -1 нейровизуализационный fMRI-метаанализ поведенческих и химических зависимостей

---

### 329 · R5975

**American Ski Resort Architecture, Style, Experience by Margaret Supplee Smith (review)**

2015 · review

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 рецензия на книгу об архитектуре горнолыжных курортов, не гемблинг

---

### 330 · R4801

**Análisis de la Industria del Juego: el sector de las Apuestas Deportivas Online. Nuevas oportunidades de negocio: Marketplaces, Tipsters y Fondos de Inversión de Apuestas Deportivas**

2019 · dissertation · es

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 анализ индустрии онлайн-ставок и новых бизнес-моделей

---

### 331 · R0695

**Xavier Breuil, Le FC Metz et la sidérurgie. De la rivalité sportive au sponsoring (1932-2007)**

2026 · Industrias Culturais (Universidade de Coimbra) · review · fr

Ce livre est indéniablement celui d’un historien reconnu par ses pairs, notamment par les chercheurs en sciences sociales qui travaillent sur le football. Auteur de plusieurs ouvrages qui traitent de l’histoire du ballon rond sous différents prismes tels que le football corporatif, le football féminin ou les paris sportifs, les derniers travaux publiés de Xavier Breuil étaient consacrés à un autre domaine : la société Les Laminoirs à froid de Thionville, spécialisée dans les pièces pour cycl...

**Решение:** -6 исторический очерк футбольного клуба Мец, не гемблинг

---

### 332 · R1487

**Sports Betting Expansion in Brazil: Impacts on Psychiatric Health**

2025 · International Neuropsychiatric Disease Journal · article, journalarticle, journal-article · en · https://doi.org/10.9734/indj/2025/v22i5509

This article presents a psychiatric analysis of the rapid growth of online betting (bets) in Brazil and its connections to the political structure of the country. Current data indicate that approximately 30% of Brazilians, mainly young men, have engaged in online bets, with alarming consequences for public health, such as unpayable debts and a fifteen-fold increase in suicide risk among gamblers. The landscape of sports betting in Brazil has undergone significant changes over the decades, and concurrently, modern society has experienced substantial shifts in digital inclusion. Within this context, the bets market has exhibited remarkable growth in the country, driven by easy access to platforms and instant payment methods, which has turned anyone with a cell phone and internet access into a potential customer. However, health policies have not kept pace with this growth, transforming bettors into potential victims of psychiatric disorders across a broad spectrum. It is important to highlight that the treatment of gambling-related disorders is multifactorial, including therapeutic techniques (CBT, motivational interviewing, group therapy, psychoeducation and family support), in addition to the use of pharmacological strategies. This study aims to investigate the correlation between the expansion of this market and the potential harm to psychiatric health caused by betting addiction, like Suicide Related to Financial Losses, severe depression, self-destructive behavior, acute psychotic episodes or dissociative states and comorbidities with substance use and personality disorders. For the reserch, it was included scientific articles and journalistic reports published in Portuguese and English, using as databases the Diagnostic and Statistical Manual of Mental Disorders, Fifth Edition (DSM-5), the International Classification of Diseases, Eleventh Edition (ICD-11), as well as national and international scientific journals accessed through Google Scholar, since 1994 until 2025; older references was used for historical context.

**Решение:** -1 психиатрический обзор расширения рынка онлайн-ставок в Бразилии

---

### 333 · R3718

**Game on! The opportunities and risks of single-game sports betting in Canada**

2021 · The Conversation Media Group Ltd · article, other, posted-content · en · https://doi.org/10.64628/aam.vvaxxqmun

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 аналитический комментарий о легализации одиночных ставок в Канаде

---

### 334 · R8025

**대학생들의 스포츠토토에 대한 인식 및 구매행동에 관한 연구**

2006 · 한국스포츠산업경영학회지 · article · ko

이 연구는 스포츠토토 활성화를 위해 대학생들의 복권에 대한 인식과 스포츠토토 구매행동을 살펴보아 스포츠토토 마케팅의 기초자료를 제시하는데 목적을 가지고 설문조사를 통해 다음과 같은 결론을 도출하였다. 복권에 대한 사행성과 도박성에 대하여 참여경험이 있는 조사자가 미 경험자보다 낮게 나타났으며, 즐거움, 공익성 취미에 대하여 긍정적으로 인지하는 것으로 나타나 참여하는 사람이 그렇지 않은 사람보다 긍정적인 이미지를 가지고 있어 이미지 제고를 위해선 경험의 제공이 필요하다. 참여 유형별로 문항간의 상관관계 결과에서 즐거움과 중독성의 상반된 이미지 요인에 대하여 둘 다 높은 수준에서 상관관계를 개별적으로 인식하고 있는 것으로 나타나 부정적 이미지 제거를 위한 방안과 긍정적 이미지의 강화를 위한 방안이 이원적으로 따로 진행되어야 함을 시사한다. 스포츠토토의 참여이유는 스포츠에 대한 관심과 높은 당첨확률에 대한 기대가 가장 많은 것으로 나타나 현재와 같이 스포츠토토를 기존의 스포츠와 연계 내지 동일시하는 홍보 전략이 유효한 것으로 판단되고 당첨 확률의 가능성을 부각시켜 대학생들로 하여금 사행성보다는 스포츠여가로서의 가능성 있는 건전한 배팅게임으로의 이미지를 강화시켜야 할 것으로 판단된다. 본 결과에서는 판매량중 축구가 가장 높게 나타났으나 수시로 구매자의 종목과 방식에 대한 요구를 조사하여 그 결괴에 따라 종목과 방식을 적용하는 구조적인 조사 경로를 확보하여야 할 것으로 사료된다. 긍정적인 이미지제고는 서비스 요인에서도 고려되어야 하기 때문에 광고는 가장 선호하는 홍보수단인 스포츠신문에 집중하여야 할 것이며 마감시간 변경등의 불편사항을 감소시키고 인터넷 이용과정을 공시하여 이용횟수를 늘려나가는 것이 이미지 제고에 영향을 주는 것으로 판단된다. 결론적으로 참여유도가 이미지 제고에 직접적인 상관이 있으므로 서비스요인을 고려하여 참여를 유도하면서 이미지 요인에 대하여 이원적인 이미지 제고전략을 시행하여야 한다.

**Решение:** ? опрос студентов о покупке Sports Toto, проверить опросник PG в полном тексте

---

### 335 · R8254

**Discussion on the Form and Characteristics of Modern Soccer Betting**

2002 · article · en

Modern soccer betting originated England, it the form of Odds, Point Spread,Spread and Pond. Odds of Modern soccer betting was main widely accepted in Europe, it more wager composition; Point Spread was main widely accepted in Asia, it' s the main way of underground wager ball; Betting Pond had the characteristics of social and negative function small, but strongly collecting funds, the soccer lottery ticket in our country and many nations in the world all adopted the method of the Betting pondto assign the cash award.

**Решение:** -1 описательный обзор форм и характеристик футбольных ставок

---

### 336 · R4911

**Everyone Knows The Spread: The Increasing Popularity of Sports Gambling Media**

2019 · Digital Scholarship - UNLV (University of Nevada Reno) · conference-paper · en

Sports gambling is increasing its footprint in the television, radio and social media landscapes following the repeal of the Professional and Amateur Sports Protection Act (PASPA), but the topic has been present in more alternative media for decades. Media companies like The Action Network and Covers, who are solely dedicated to sports betting, are the products of social and technological changes that have helped sanitize and popularize the sports gambling industry. This study provides a content analysis of print, radio, podcast, television, video, and website media from the 1970s to present day to show the progression from statistics-heavy periodicals to entertaining podcasts and tweets dedicated to sports betting. Sports gambling increasing its presence into popular media is a reflection of the positive cultural change that gambling as a whole has gone through in the last three decades.

**Решение:** -1 правовой анализ распространения спортивных ставок после решения Верховного суда

---

### 337 · R1940

**Relationship between Socio-Demographic Factors and Sports Betting among Football Fans in Satellite Television Football Viewing Centres in Osogbo, Osun State, Nigeria**

2025 · International Journal of Innovative Research and Development · article, journalarticle, review · und · https://doi.org/10.24940/ijird/2025/v14/i7/jul25012

Sports betting makes an incursion into the nooks and crannies of society and propagates capitalism in some ways. As such, it has shown far-reaching negative implications on the individual, family, community and society. The habitual betting problem affects a quantifiable extent of youth players and may show in both mental and physical conditions. Despite this, there is a dearth of studies on sports betting; specifically, a Descriptive survey research design was adopted. A simple random sampling technique was used to select the respondents, while a self-developed questionnaire was used for data collection. Descriptive statistics, including frequency counts and percentages, and the inferential Pearson product-moment correlation coefficient, were used to test the hypotheses. This study, therefore, examined the relationship between socio-demographic factors and betting in sports among football fans in satellite television football viewing centres in Osogbo, Osun State. The results revealed a significant positive relationship between peer influence and sports betting among football fans in satellite television football viewing centres in Osogbo, Osun State. The results also revealed that age relations did not have a significant positive relationship with sports betting among football fans in satellite television football viewing centres in Osogbo, Osun State (r = 0.028, p &gt; 0.05). Furthermore, educational level had a significant positive relationship with sports betting among football fans in satellite television football viewing centres (r = 0.368, p &lt; 0.05). Occupation did not have a significant positive relationship with sports betting among football fans in satellite television football viewing centres (r = 0.192, p &gt; 0.05). Gender had a significant positive relationship with sports betting among football fans in satellite television football viewing centres (r = 0.468, p &lt; 0.05). The findings of this study revealed that educational level and gender had a significant positive relationship with sports betting among football fans in satellite television football viewing centres in Osogbo, while age relations and occupation did not. The government and other relevant stakeholders should therefore ensure that fans in satellite television football viewing centres in Osogbo are enlightened on the negative consequences of sports betting.

**Решение:** ? опрос футбольных болельщиков о ставках на спорт, проверить наличие инструмента PG в полном тексте

---

### 338 · R1386

**APOSTAS ESPORTIVAS E JOGOS DE AZAR: DESAFIOS ÉTICOS E LEGAIS À LUZ DA DOUTRINA DE AGAMBEN**

2025 · Dialética eBooks · part of book or chapter of book, book-chapter · pt · https://doi.org/10.48021/978-65-270-5421-4-c20

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 философско-правовой анализ ставок в свете доктрины Агамбена

---

### 339 · R3676

**The concept of manipulation in sports competitions**

2021 · ANCIENT LAND · article, other literature type · en · https://doi.org/10.36719/2706-6185/03/15-19

Knowing the negative effect of sports manipulation for the sport and society, as well as the problems that is facing the Macolin Convention in its ratification, I decided to do this research in order investigate the phenomenon of match-fixing, controversial issues about the online gambling and potential effect of ratifycation of the convention and its entry into force. I was totally surprised when I found out so many International business law issues are covered in this topic. The sports betting markets are similar to the stock market, where odds movement de- pends on the performance of the teams and players. The insider trading is similar to the match-fixing, where a pre-match information for the result is used in order to achieve a great profit. Memorandums of understanding between betting companies, sports governing bodies and public authorities are used to cover the lack of regulation in this area. In the same time there is a need of acceleration of negotiations for the ratification of the convention due to the spreading of the phenomenon of sports manipulation. Key words: major manipulations, harmful aspects, existing problems, legalizing sports gambling, ethics of sports

**Решение:** -2 юридический и теоретический анализ понятия манипуляции спортивными соревнованиями

---

### 340 · R5648

**INDEX**

2016 · Lexington Books · part of book or chapter of book · und · https://doi.org/10.5771/9781498504898-301

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 справочный аппарат книги (предметный указатель)

---

### 341 · R3160

**Surface Water and Groundwater in a Changing Environment**

2023 · International Journal of Technology and Engineering Studies · article · en · https://doi.org/10.20469/ijtes.9.40004

Discover unparalleled betting experiences with IDBET, your go-to destination for top-tier sports betting and thrilling casino games. Enjoy secure transactions, generous bonuses, and a wide variety of betting options tailored to elevate your gaming journey. Join IDBET today for the ultimate online betting adventure.

**Решение:** -7 коммерческий спам / захваченный научный журнал

---

### 342 · R6962

**Dimensions of problem gambling behavior associated with purchasing sports lottery.**

2012 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-011-9243-3

Sport gambling is a major segment of the sport industry. Although various forms of sport gambling may help generate revenues, increase governmental tax income, and advance social and economic development, it has the potential to cause social, family, and individual problems, thus imposing cost and burden to a community. In recent years, problem gambling associated with purchasing sports lottery has gradually emerged as a major social issue in China. Problem gambling is often referred as all patterns of gambling behavior that compromise, disrupt, or damage personal, family, or vocational pursuits (Lesieur, 1988). From this perspective, pathological gambling can be regarded as a sub-category, or one end of a continuum, of gambling-related problems. The term of problem gambling can also be used to denote a level of gambling, ranging from an early stage of on-site problems to compulsive or pathological gambling as diagnosed by applying the DSM-IV diagnostic instrument (Moore, 2002; Raylu &amp; Oei, 2002; Rosenthal, 1989; Volberg, 2001). When people refer to problem gambling, it typically means subclinical level of gambling problems. While many studies have been conducted on general problem gambling, few have focused on issues that are primarily caused by sports betting. Furthermore, previous studies on problem gambling have mainly been conducted in western countries, such as the U.S., Australia, Britain, and Canada; research findings from these studies are limited in their applicability to China due to historical, social, and cultural differences. For instance, the government-run sports lottery in China has existed for merely 20 years and because of the absence of other gambling forms in mainland China, sports lottery is the primary outlet of gambling with a large participation rate among Chinese residents. Understanding the fundamental issues caused by sports lottery is precursor to formulating effective strategies for prevention, intervention, or even rehabilitation. The purpose of this study was to identify and examine the dimensions of problem gambling behaviors associated with purchasing sports lottery in China. This was accomplished through the development and validation of the initial Scale of Assessing Problem Gambling (SAPG). The SAPG was initially developed through conducing a comprehensive review of literature (e.g., Custer, 1982; Lesieur &amp; Blume, 1987), conducting open-ended interviews of gamblers (n = 20), administrators of sports lottery programs (n = 40), and retail store managers (n = 20), and summarizing telephone transcripts of a hotline for problem gambling. Through these procedures, a total of 45 items were identified, which was submitted to a panel of experts in gambling research or administration (n = 9) for a test of content validity. A total of 32 items were retained and phrased into a Likert 5-point scale. A survey packet was prepared that contained an informed consent letter, the SAPG items, and demographic variables. Research participants (N = 4,991) were Chinese residents who have purchased sports lottery tickets in the past 12 month. Test administration was carried out in five large cities (Shenyang, Shanghai, Guangzhou, Chengdu and Zhengzhou) with population ranging from 7 million to 15 million. These cities represented the largest lottery market in five geographical regions of China. Within each city, a computer-generated, randomly stratified multistage sampling method was used to survey one out of 10 thousands of local adult population. Following the survey packet, one-on-one interviews was conducted at retailing stores of sports lottery by trained investigators. A total of 5,450 interviews were conducted, and 4,991 participants were willing to complete the survey, representing a response rate of 92%. A sports lottery ticket was used as an incentive to complete the study. Of the respondents, 77.3% were male and 22.7% female. In terms of occupation, 39.1% were professionals,, 20.4% unemployed or retired, 19.3% peasant workers, 12.1% private business owners, and 8.5% students or others. A majority of the participants (i.e., 93%) ranged in age between 20 and 60 years old. Due to the exploratory nature of this study, the total sample was randomly split into two halves (Lattin, Carroll, and Green 2003). The first half was used for conducting an EFA and the second half for a CFA. Both EFA and CFA were examined using weighted least-square means and variance adjusted (WLSMV) estimates, following the procedures in Mplus 5.12 (Muthen and Muthen, 2006). The ‘goodness-of-fit’ approach was adopted to determine the number of factors in the EFA (Fabrigar et al. 1999). An EFA with Geomin for oblique rotation revealed that a four-factor solution was optimal (RMSEA=.04, TLI=.99, CFI=.96), including Harmful Behaviors (9 items), Compulsive Disorders (6 items), Over Expectation (2 items), and Depression Sign (2 items). All factors had low to moderate inter-item correlation (.18-.69). As the EFA findings were data driven, an in-depth examination of content interpretability of the factors revealed that the Harmful Behavior factor contained two distinct concepts and should thus be split into two factors: Social Consequence (4 items) and Financial Consequence (5 items). In the CFA, the five-factor model showed good fit to the data (RMSEA = .050, TLI=.978, and CFI=.922). All factors again showed low to moderate inter-item correlation with each other (.29-.60). Conducting a comparison with the original four-factor structure (RMSEA = .052, TLI=.976, and CFI=.915), the level of model fit for the five-factor structure was significantly (p &lt; .05) superior (χ24 = 65.03). As the Over Expectation and Depression Sign factors had only two items, they were of mediocre composite reliability coefficients (.60 and .72) and AVE values (.41 and .43). The composite reliability coefficients for the remaining three factors were greater than .80 and AVE values greater than .50, respectively, indicating good convergent validity. Consequently, the SAPG scale with a total of 19 items under five factors (i.e., Social Consequence, Financial Consequence, Harmful Behavior, Compulsive Disorder, and Depression Sign) was formulated with good measurement properties to assess problem gambling of sports lottery consumers in China. This study represents an initial effort to understand the dimensions of problem gambling associated with Chinese sports lottery. The developed scale may be adopted by researchers and practitioners to examine problem gambling behaviors and develop effective prevention and intervention procedures based on tangible evidence. With proper adaption, modification, and validation, the SAPG has the potential to be adopted in other socio-cultural contexts, such as North America, where behavioral problems associated with sport gambling likely exist among sport gamblers and yet, few specific measurement tools are available.

**Решение:** + количественный опрос 4991 покупателя спортивной лотереи в 5 городах Китая с валидацией шкалы SAPG

---

### 343 · R2458

**Shrouded Sin Taxes**

2024 · arXiv (Cornell University) · article, preprint, preprint/article · en · https://doi.org/10.48550/arxiv.2409.01493

Strategic shrouding of taxes by profit-maximizing firms can impair the effectiveness of corrective taxes. This paper explores tax shrouding and its consequences after the introduction of a digital sin tax designed to discourage harmful overconsumption of online sports betting in Germany. In response to the tax reform, most firms strategically shroud the tax, i.e., exclude tax surcharges from posted prices. Using an extensive novel panel data set on online betting odds, I causally estimate the effect of the tax on consumer betting prices. Consumers bear, on average, 76% of the tax burden. There is considerable and long-lasting heterogeneity in effects conditional on shrouding practices. Firms that shroud taxes can pass 90% of the tax onto consumers, while the pass-through rate is 16% for firms that directly post tax-inclusive prices. To understand the results' underlying mechanisms and policy implications, I propose an optimal corrective taxation model where oligopolistic firms compete on base prices and can shroud additive taxes. Tax shrouding is only attainable in equilibrium if (some) consumers underreact to shrouded attributes. According to the theoretical predictions, the empirically identified heterogeneity suggests that strategic tax shrouding significantly attenuates the positive corrective welfare effects of the tax. The results prompt regulating shrouding practices in the context of corrective taxation.

**Решение:** -2 эконометрический анализ скрытых налогов на ставки в Германии

---

### 344 · R8006

**Beating the Odds: Arbitrage and Wining Strategies in the Football Betting Market**

2006

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -2 анализ арбитражных стратегий на рынках футбольных ставок

---

### 345 · R1395

**Psychotherapeutic Support for Concerned Significant Others Impacted by Gambling Disorder**

2025 · Journal of Health Service Psychology · journalarticle, article · en · https://doi.org/10.1007/s42843-025-00139-1

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 клиническое руководство / обзор психотерапевтической помощи близким игроков

---

### 346 · R4966

**스포츠토토의 재구매 의도에 영향을 미치는 요인에 관한 연구**

2019 · The Academic Society of Global Business Administration · article · ko

스포츠토토는 스포츠를 매개로 한 ‘승부 참여형 게임’으로 국민의 여가선용, 지방재정과 체육재정 등 공공재정 조달, 국민체육복지에 크게 기여하고 있다. 본 연구는 스포츠토토의 이해수준, 구매동기, 그리고 만족도와 재구매 의도 간의 영향 관계를 규명하여 스포츠토토의 구매 활성화를 위한 실질적인 방안을 마련하는 데 목적을 두고 있다. 연구결과, 첫째, 스포츠토토에 대한 이해수준은 긍정적인 인식과 구매동기에 긍정적인 영향을 미치는 것으로 나타났다. 둘째, 스포츠토토에 대한 긍정적 인식과 구매동기는 스포츠토토의 구매만족에 긍정적인 영향을 미치는 것으로 나타났다. 셋째, 스포츠토토에 대한 구매만족이 재구매 의도에 긍정적인 영향을 미치는 것으로 나타났다. 마지막으로 스포츠토토 대한 긍정적 인식과 구매동기가 재구매 의도에 미치는 영향 관계에서 구매만족이 매개역할을 하는 것으로 나타 났다. 본 연구를 통하여 스포츠토토를 활성화하기 위하여 스포츠토토에 대한 긍정적 인식 제고와 구매동기 자극이 고객만족에 연계되도록 함으로써 재구매의향을 향상시킬 수 있음을 시사한다고할 수 있다.

**Решение:** -3 исследование факторов повторной покупки Sports Toto без инструмента PG

---

### 347 · R3780

**Neke odrednice kockanja kod srednjoškolskih uĉenika**

2021 · Sveučilište u Zadru. Odjel za psihologiju. · master thesis · hrv · https://repozitorij.unizd.hr/islandora/object/unizd:5829/datastream/PDF

Gambling has become an integral part of growing up and adolescents are considered the most vulnerable group when it comes to gambling. As gambling is considered a risky behavior, various factors contribute to its development. Individual factors include various emotional and psychological characteristics of the individual. Environmental factors include sociodemographic, family and peer factors. The aim of this study was to examine the prevalence of risk and the intensity of gambling in high school students, as well as differences with regard to gender and age, i.e. whether high school students attend lower or upper grade. Furthermore, the relationship between school success and gambling intensity in high school students will be examined. In addition, it will be analyzed the relationship between individual (impulsiveness), family (perception of family relationships, i.e., perception of mother-father relationship) and peer (peer pressure) factors with a global measure of risk for the development of psychosocial consequences associated with gambling. In the research were 157 (44%) girls and 198 (56%) boys, students of the first, second, third and fourth grade of high school, as well as students of vocational four-year and vocational three-year schools in the city od Split, whose average age was 16.49. Boys and girls differ in the intensity of playing particular games of chance. Boys, unlike girls, are more likely to go to sportsbooks, to participate in virtual horse races and online gambling. But girls, unlike boys, more often buy scratchcards and pay for lottery tickets. Boys score higher results in examining a global risk measure for the development of psychosocial consequences of gambling than girls. High school students who perform worse in school are more likely to participate in the following gambling activities: sports betting, slot machine games, electronic roulette, croupier roulette, casino games, virtual horse racing and online gambling, and to score higher results on a subscale that examines the global risk measurement of the development of psychosocial consequences of gambling and vice versa. High school students who have more pronounced psychosocial consequences of gambling are more susceptible to peer pressure and more impulsive, also they perceive less of their father's support and their father is more compliant in their upbringing. Other examined differences and correlations were not determined. Kockanje je postalo sastavni dio odrastanja, a adolescenti se smatraju najranjivijom skupinom. Kako kockanje spada u rizično ponašanje, njegovu razvoju pridonose razni čimbenici. U individualne čimbenike ubrajamo razna emocionalna i psihološka obilježja pojedinca, a u okolinske čimbenike ubrajamo sociodemografske, obiteljske i vršnjačke čimbenike. Cilj ovog istraživanja bio je ispitati zastupljenost te intenzitet kockanja kod srednjoškolskih učenika, kao i razlike s obzirom na spol i dob, tj. pohađaju li srednjoškolski učenici niži ili viši razred. Zatim, cilj je bio ispitati odnos školskog uspjeha i intenziteta kockanja kod srednjoškolskih učenika kao i odnos individualnih (impulzivnost), obiteljskih (percepcija obiteljskih odnosa, tj. percepcija odnosa s majkom i ocem) i vršnjačkih (vršnjački pritisak) čimbenika s globalnom mjerom rizičnosti za razvoj psihosocijalnih posljedica povezanih s kockanjem. U istraživanju je sudjelovalo 157 (44%) djevojaka i 198 (56%) mladića koji su učenici prvih, drugih, trećih i četvrtih razreda gimnazije, strukovne četverogodišnje i strukovne trogodišnje srednje škole na području grada Splita čija je prosjeĉna dob 16.49 godina. Mladići, za razliku od djevojaka, češće odlaze u sportske kladionice, češće sudjeluju u virtualnim utrkama konja i internetskom kockanju. No, djevojke, za razliku od mladića, češće kupuju jednokratne srećke i uplaćuju loto listiće. Mladići postižu više rezultate u ispitivanju globalne mjere rizičnosti za razvoj psihosocijalnih posljedica kockanja od djevojaka. Srednjoškolski učenici koji postižu lošiji školski uspjeh češće sudjeluju u sljedećim kockarskim aktivnostima: sportskim kladionicama, igrama na automatima, elektronskom ruletu, ruletu s krupijeom, igrama u kasinu, virtualnim utrkama konja i internetskom kockanju te postižu veće rezultate na subskali koja ispituje globalnu mjeru rizičnosti za razvoj psihosocijalnih posljedica kockanja i obratno. Srednjoškolski učenici koji imaju izraženije psihosocijalne posljedice kockanja podložniji su vršnjačkom pritisku, impulzivniji su, roditelji ih više kontroliraju te percipiraju manje očeve podrške i otac im je popustljiviji u odgoju. Ostale ispitivane razlike i povezanosti nisu utvrđene.

**Решение:** + количественное исследование хорватских старшеклассников, ставки на спорт, шкала риска последствий гемблинга

---

### 348 · R1234

**Rentabilidad y eficiencia en los mercados de apuestas deportivas: el caso del Club Atlético Osasuna**

2026 · Academica-e (Universidad Pública de Navarra) · dissertation · es

El presente TFG analiza la eficiencia y rentabilidad del mercado de apuestas deportivas en los partidos del Club Atlético Osasuna, con el objetivo de estudiar el comportamiento de las principales casas de apuestas, identificar los factores en la rentabilidad del apostante y determinar la existencia de posibles estrategias de apuestas sistemáticas rentables. Para ello, se analizan las cuotas ofrecidas por Bet365, Pinnacle y William Hill en los partidos de liga disputados por Osasuna entre las temporadas 2019/20 y 2024/25. Una vez procesados y depurados los datos, tras un laborioso proceso de recopilación y tratamiento manual de determinadas variables, los resultados respaldan la literatura previa y muestran que el mercado de apuestas deportivas se caracteriza por un elevado grado de eficiencia. Aun así, existen pequeñas ineficiencias capaces de generar rentabilidades limitadas. Del mismo modo, el margen aplicado por las operadoras constituye un factor relevante en la rentabilidad del apostante, observándose un aumento de este a medida que incrementa la incertidumbre y avanza la temporada.

**Решение:** -2 анализ букмекерских линий и эффективности рынка на матчах Осасуны

---

### 349 · R6192

**Daily Fantasy sites engage in a legal war for survival**

2015 · CUNY Academic Works (City University of New York) · dissertation · en

Over the past two years, the world has changed its perception of daily fantasy sports. FanDuel and DraftKings have taken the world by storm, making huge profits off even the casual fans desire to win money everyday, instead of just once at the end of a season. Lawmakers have noticed and are eager to regulate the business or ban it altogether, as seen in New York. What was once a weekend hobby is now a multi-billion dollar business. A business lawmakers say is just another form of gambling and doesn't require skill.

**Решение:** -1 диссертация: правовые споры вокруг регулирования дейли фэнтези

---

### 350 · R4405

**Gambling formats, involvement, and problem gambling: which types of gambling are more risky?**

2020 · BMC public health · article, journal article, journalarticle · eng · https://doi.org/10.1186/s12889-020-08822-2

Abstract Background The recognition of problem gambling as a public health issue has increased as the availability of gambling expands. Research has found that some formats of gambling are more closely linked to problem gambling than others. Conflicting evidence, however, has emerged, suggesting that the most important consideration is involvement (i.e., number of gambling formats an individual participates in). This debate has important implications for the regulation of gambling formats and for the allocation of problem gambling prevention and treatment services. Method Analyses utilized the Baseline General Population Survey (BGPS) and the Baseline Online Panel Survey (BOPS) of Massachusettscollected in 2013–2014. The BGPS contains a representative sample of 9523 Massachusetts adults and the BOPS contains a sample of 5046 Massachusetts adults. All participants were administered the same comprehensive survey of their past year gambling behavior and problem gambling symptomology. Only those who gambled regularly in the past 12 months ( n = 5852) were included. The Problem and Pathological Gambling Measure was used to classify gambling behavior. Within the sample, there were 446 problem gamblers. We assessed: 1) whether some gambling formats are more related to problem gambling; 2) whether problem gambling is positively related to high involvement in gambling; 3) the relationship between involvement in gambling and intensity of gambling; and 4) whether gambling formats mediate the relationship between gambling involvement and problem gambling. Results Groups of monthly gamblers participating in casino gambling, bingo, and sports betting contained a higher proportion of problem gamblers. High gambling involvement was also positively associated with problem gambling; however, a large minority of gamblers experienced problems when engaging in only one or two forms of gambling. Gambling involvement was also positively associated with intensity of gambling. Therefore, intensity of gambling may be partly driving the relationship between involvement and problem gambling. Specific gambling formats mediated the relationship between involvement and problem gambling. Conclusions The gambling format an individual participates in is connected to whether an individual is likely to experience problem gambling. We also found that the level of involvement (and its relationship to intensity) may affect the likelihood that an individual will experience problematic gambling behavior. Ultimately, the type of gambling format an individual partakes in does mediate the relationship between problem gambling and involvement. In Massachusetts, participating in casino gambling was more closely associated with problem gambling than other formats across all levels of involvement.

**Решение:** + репрезентативный опрос 14500 взрослых жителей Массачусетса с инструментом PPGM и выделением ставок на спорт

---

### 351 · R4332

**THE MORAL AND ECONOMICAL FACTORS THAT IMPACT THE LIKELIHOOD OF A STATE LEGALIZING SPORTS GAMBLING: AN INDEPTH STUDY OF THE EFFECT OF NATIVE AMERICAN CASINOS AND STATE DEFICITS**

2020 · article · en

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 политологический анализ факторов легализации ставок штатами

---

### 352 · R8239

**NOT FOR CITATION OR CIRCULATION WITHOUT PERMISSION OF THE AUTHORS CHEATS AT PLAY: THE SOCIAL ORGANIZATION OF VIDEO LOTTERY TERMINAL FRAUD Working Draft**

2002

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 мошенничество на видеолотерейных терминалах (VLT), нет ставок на спорт

---

### 353 · R0465

**Gambling in Senegal: Sociodemographic, Clinical, and Risk Factors in an International Perspective**

2026 · Open Journal of Psychiatry · article · https://doi.org/10.4236/ojpsych.2026.162008

Background and Aims: Gambling-related disorders are increasingly recognized as a public health concern, particularly in low- and middle-income countries where regulatory frameworks remain limited. This study aimed to assess the prevalence, patterns, and severity of gambling-related problems among gamblers in Senegal. Methods: A descriptive and analytical cross-sectional study was conducted from March 1 to May 30, 2023, across the entire territory of Senegal. A multistage sampling strategy was used, involving the selection of 20 districts, three gambling venues per district, and ten gamblers per venue. Gambling-related problems were assessed using the Canadian Problem Gambling Index (CPGI). Data were collected through face-to-face interviews using KoboToolbox and analyzed with Epi Info, R, and SPSS. Results: A total of 813 gamblers were included, of whom 97.2% were male. The mean age was 42.8 ± 15.3 years old. Severe gambling dependence was observed in 59.3% of participants, while 29.0% were classified as moderate-risk gamblers. PMU betting and sports betting were the most frequently practiced gambling activities. Nearly half of the participants reported psychoactive substance use, predominantly tobacco. Virtual gambling emerged as a major factor associated with excessive gambling behavior. Conclusions: The prevalence of problem gambling among gamblers in Senegal is markedly higher than that reported in Western countries. These findings highlight the urgent need to strengthen regulatory measures, develop national prevention programs, and integrate the management of gambling disorders into public health policies.

**Решение:** + количественное исследование 813 игроков в Сенегале, ставки на спорт, инструмент CPGI

---

### 354 · R8394

**Nonexclusive patent, know-how, process and copyrights license to manufacture, sell and lease video game machines, including the ECOM, Probe and Mark II models, exclusively for sale in Nevada, and worldwide for use in the race and sports book wagering business if licensor elects not to participate.**

1996 · RoyaltyStat · text/ · https://doi.org/10.34675/l22960

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 патентный лицензионный договор, не исследование

---

### 355 · R8103

**Who's In? The Bona Fide Future of Office Pools**

2004 · Gaming Law Review · article, journalarticle · eng · https://doi.org/10.1089/1092188041427247

ARE OFFICE POOLS LEGAL? In most instances, they are illegal. Ironically enough, however, office pools are “probably the most respectable form of illegal gambling . . . .”1 If you are like many Americans, events like the Super Bowl and the NCAA Men’s Basketball Tournament are opportunities not only to down a few snacks and alcoholic refreshments, but to gamble a few dollars in the good ol’ office pool. In a typical office pool, participants are asked to ante-up a dollar and make their best guesses as to which team(s) will win, with the entire monetary amount invested in the pool going to the individual who guesses the majority of winners in the bracket.2 Every year, in offices nationwide, some enterprising individual is sending out “March Madness” e-mails soliciting others to “join in on the fun” or standing by the water fountain encouraging coworkers to “join in, it’s only a few bucks.” Sports events in America are a massive business; some estimate that sports comprise a $212 billion a year industry.3 Adding to that amount, sports wagering in America is estimated to be in the billions of dollars each year.4 Furthermore, sports wagering is quite popular from the nation’s factories to its boardrooms.5 The NCAA Men’s Basketball Tournament is the nation’s largest betting event of the year, with estimates of $2.5 billion being wagered on office pools.6 However, as we all enjoy the camaraderie and challenge involved in filling out our brackets, we should not lose sight of the fact that the games we are watching could be fixed.7 Throughout history, sports wagering in America has witnessed professional sports personalities such as “Shoeless Joe” Jackson, Denny McLain, and Pete Rose suspended for gambling.8 While professional and collegiate

**Решение:** -1 юридический анализ законности офисных спортивных пулов

---

### 356 · R4800

**New Jersey Beat The Spread: Murphy v. National Collegiate Athletic Association And The Demise Of PASPA Allows For States To Experiment In Regulating The Rapidly Evolving Sports Gambling Industry**

2019 · University of Pittsburgh Law Review · article, journal-article · en · https://doi.org/10.5195/lawreview.2018.604

n/a

**Решение:** -1 правовой анализ решения Верховного суда США Murphy v. NCAA

---

### 357 · R6736

**Information Efficiency in High-Frequency Betting Markets**

2013 · The Oxford Handbook of the Economics of Gambling · other literature type, part of book or chapter of book, reference-entry · en · https://doi.org/10.1093/oxfordhb/9780199797912.013.0012

The betting industry has been transformed by the Internet. Growth of person-to-person betting, mediated through online betting exchanges, has been a key element of this transformation. Betting exchanges enable traders to either back (buy) or lay (sell) bets on a wide range of sporting events. Such continuously operating online betting markets have ensured the transition of the use of high-frequency data (sub-daily sampling) from the financial setting into the betting market context. This chapter reviews recent academic research on the topic of information efficiency in high-frequency, in-play football betting markets. Several studies have reported evidence violating weak-form information efficiency, in the form of a favorite-longshot bias in in-play betting prices. However, there is evidence in the literature in favor of semi-strong form information efficiency. One study reports interesting evidence in support of strong-form information efficiency. As in-play betting markets continue to develop, driven by further improvements in computing power, parallel growth is anticipated in research on information transfer and price formation in financial markets, an exciting new arena for academic study.

**Решение:** -1 глава академического справочника по экономике рынков ставок

---

### 358 · R5535

**Factors that influence children's gambling attitudes and consumption intentions: lessons for gambling harm prevention research, policies and advocacy strategies.**

2017 · Harm reduction journal · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1186/s12954-017-0136-3

BACKGROUND: Harmful gambling is a public health issue that affects not only adults but also children. With the development of a range of new gambling products, and the marketing for these products, children are potentially exposed to gambling more than ever before. While there have been many calls to develop strategies which protect children from harmful gambling products, very little is known about the factors that may influence children's attitudes towards these products. This study aimed to explore children's gambling attitudes and consumption intentions and the range of consumer socialisation factors that may influence these attitudes and behaviours. METHODS: Children aged 8 to 16 years old (n = 48) were interviewed in Melbourne, Australia. A semi-structured interview format included activities with children and open-ended questions. We explored children's perceptions of the popularity of different gambling products, their current engagement with gambling, and their future gambling consumption intentions. We used thematic analysis to explore children's narratives with a focus on the range of socialising factors that may shape children's gambling attitudes and perceptions. RESULTS: Three key themes emerged from the data. First, children's perceptions of the popularity of different products were shaped by what they had seen or heard about these products, whether through family activities, the media (and in particular marketing) of gambling products, and/or the alignment of gambling products with sport. Second, children's gambling behaviours were influenced by family members and culturally valued events. Third, many children indicated consumption intentions towards sports betting. This was due to four key factors: (1) the alignment of gambling with culturally valued activities; (2) their perceived knowledge about sport; (3) the marketing and advertising of gambling products (and in particular sports betting); and (4) the influence of friends and family. CONCLUSIONS: This study indicates that there is a range of socialisation factors, particularly family and the media (predominantly via marketing), which may be positively shaping children's gambling attitudes, behaviours and consumption intentions. There is a need for governments to develop effective policies and regulations to reduce children's exposure to gambling products and ensure they are protected from the harms associated with gambling.

**Решение:** -2 качественное исследование факторов отношения детей к гемблингу

---

### 359 · R6259

**스포츠 경기 조작 실태 관련 법적 고찰을 통한 비리척결 개선방안**

2015 · 스포츠엔터테인먼트와 법 (JSEL) · article · ko

이 연구는 스포츠정신의 훼손과 스포츠의 생명인 공정성을 무너뜨리고 수많은 스포츠팬들의 애정과 신뢰를 배반하는 스포츠 경기조작 실태에 대한 고찰을 통하여 스포츠경기조작에 대한 개선방 안탐색을 하는데 목적이 있다. 이를 위하여 본 연구는 2010년 3월부터 2014년 12월까지 각 종목별 스포츠 경기조작 선행연구와 판례의 내용을 분석하였다. 본 연구의 내용은 첫째, 각 종목별 스포츠 경기조작 실태를 알아보았고, 둘째, 스포츠 경기조작에 대한 원인을 알아보았으며, 마지막으로 스포츠경기조작 근절에 대한 개선방안을 탐색해 보았다. 스포츠 경기조작실태는 운동경기 선수·감독·심판이 부정한 청탁과 재산상의 이익을 받는 스포츠 경기조작의 형태가 있었으며, 그로 인하여 선수가 고의로 경기에 지고, 자신의 팀이 진다는 고액의 불법 스포츠토토 베팅이 있었다. 스포츠 경기조작이 반복되는 원인은 불법 스포츠토토의 고액의 배당금 · 열악한 환경과 낮은 처우 · 엘리트선수에게 왜곡된 스포츠 교육 · 부상과 슬럼프 · 스포츠 윤리 교육의 부재 이다. 스포츠 경기조작에 대한 개선방안탐색은 부정방지 예방 교육 · 강력한 처벌의 국민체육진흥법 시행 · 불법 스포츠도박 사이트의 단속 · 스포츠 경기조작에 대한 수사 강화 · 스포츠 공정위 등을 통한 체계적인 관리 · 열악한 환경 처우개선 등이다.

**Решение:** -1 правовой анализ противодействия договорным матчам в Корее

---

### 360 · R8101

**Legalized gambling and crime in Canada.**

2004 · Psychological reports · journal article, journalarticle, article · eng · https://doi.org/10.2466/pr0.95.3.747-753

In the 10 provinces and 2 territories of Canada in 2000, but not in 1990, the total number of types of gambling activities was positively associated with rates of robbery (p<.05). Controls for other social variables did not eliminate these associations. With so many correlations in the present study the likelihood of a Type I error was quite large. Alpha was adjusted to control that likelihood. Statistical analysis now required even stronger evidence before concluding that there were significant relationships between crime and gambling variables or among gambling variables. In the 10 provinces of Canada in 1999/2000, the total numbers of electronic gambling machines for each province was associated with rates of theft over $5000 (p<.01). In 1990 there were positive associations found for burglary with off-track betting and race/sportsbooks; motor vehicle theft with off-track betting, and race/sportsbooks; rate of theft with casinos; quarter horse racing with thoroughbred racing. In 2000 there were positive associations for robbery with casinos and slot machines; casinos with slot machines; scratch tickets with raffles, break-open tickets, sports tickets, and charitable bingo; raffles with break-open tickets, sports tickets, and charitable bingo; break-open tickets with sports tickets; charitable bingo with break-open tickets and sports tickets.

**Решение:** -2 экологический корреляционный анализ преступности и игорного бизнеса по провинциям Канады

---

### 361 · R2133

**Hybrid Neural Network Approach for Customer Churn Prediction in Web Services**

2025 · International Russian Automation Conference (RusAutoCon) · conference, conference-paper · en · https://doi.org/10.1109/rusautocon65989.2025.11177285

Customer churn remains a significant challenge for web services, especially in competitive domains like online betting, where user retention directly drives revenue. Existing models often fail to account for complex interactions of users and social influences that shape churn decisions. This paper proposes a hybrid approach that combines convolutional layers for pattern detection, recurrent structures for time-based analysis, and graph-based techniques to model implicit user connections. A key feature of our method is the Churn Prediction Index (CPI), a tailored metric derived from engagement cycles, enhancing the identification of at-risk users. Our process involves careful data preparation, including normalization and time aggregation, alongside feature design using statistical distributions to reflect user activity. We also build a user interaction graph based on behavioral similarities. Tested on real-world data from a prominent betting platform, the model achieves a ROC-AUC of 0.94 and an F1-score of 0.67, surpassing baseline methods by 10—36%. A/B testing demonstrated a 2.5-fold increase in reactivated users, proving its value for retention strategies. This work offers a scalable, practical tool for web services seeking to curb churn by blending temporal and relational insights.

**Решение:** -2 нейросетевая модель оттока клиентов букмекерской компании без опроса людей

---

### 362 · R6462

**Marketing turístico na saúde oferta hoteleira na cidade de Coimbra: estudo de caso**

2014

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 маркетинг оздоровительного туризма в отелях Коимбры, не гемблинг

---

### 363 · R7051

**Influence Factors of Intention of the Female Purchaser of Sports Lottery——Comparison between Female Consumers and Female Non-consumers**

2012 · Beijing Tiyu Daxue xuebao · article · en

Based on the questionnaire and interview,influence factors of purchase intention were compared between 404 female consumers' in sports lottery and 610 female non-consumers' which divided into higher and lower intention groups.The main results show purchasing cognitive can distinguish effectively female consumers from female non-consumers with higher and lower intention.Female consumers' purchasing cognitive score is the highest,female non-consumers' with higher purchase intention second and female non-consumers' with lower intention is the lowest.Whether or not families purchase lottery is an important factor distinguishing female non-consumers' risk appetite and external information function.Female non-consumers' risk appetite score and external information function score whose families purchase lottery are higher significantly than female non-consumers' whose families don't purchase lottery.Whether or not families purchase lottery can effective distinguishing female economic utility,and the female economic utility score whose families purchase lottery is higher significantly than female non-consumers' whose families don't purchase lottery.The education level may influence female consumer's economic utility,the score of which becomes lower with the rise in education.Finally,some marketing proposals are made for female purchase lottery.

**Решение:** -3 опрос факторов намерения покупки спортивной лотереи женщинами без инструмента PG

---

### 364 · R1874

**Sports Gambling Experiences and Behaviors at a U.S. Public University**

2025 · SSRN Electronic Journal · article, posted-content, preprint · en · https://doi.org/10.2139/ssrn.5147879

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? исследование опыта и поведения спортивных ставок в университете США, нет аннотации, проверить полный текст

---

### 365 · R2619

**Sports Gambling Cultivation**

2024 · Routledge eBooks · part of book or chapter of book, book-chapter · en · https://doi.org/10.4324/9781315673929-5

In 2018, the United States Supreme Court overturned the Professional and Amateur Sports Protection Act (PASPA) and deemed the act unconstitutional. This decision opened the proverbial floodgates for legalized sports gambling, increasing advertising while transforming the contemporary sport-media landscape. Consumers have been bombarded with new in-game graphics, targeted advertising, gambling language, and constant gambling-specific content. Today’s sport-media landscape is being redefined by pervasive and near-ubiquitous sport-gambling promotion, advertising, in-game discussion, and conversation woven into the fabric of mediated sport coverage. In this chapter, we conceptualize this shift toward the formation of the contemporary sports-gambling-media industrial complex. This shift is creating an environment that promotes, engages, and ultimately normalizes sports betting. Examining this through the lens of cultivation theory, our exploration of this sports gambling and media convergence examines two primary promotional strategies for consumer engagement: traditional advertising and integrated marketing. We explore each, placing emphasis on integrative marketing as a new and strategic method through which gambling companies connect with, appeal to, influence, and ultimately recruit new consumers through subliminal and coercive means. We consider the theoretical and practical impacts this convergence has on sport coverage, consumers, and the broader sport-media landscape.

**Решение:** -1 теория культивации в контексте рекламы ставок на спорт

---

### 366 · R1237

**The sports gambling novice experience: an autoethnography of a woman bettor**

2026 · Sport Management Review · article, journalarticle, journal-article · en · https://doi.org/10.1080/14413523.2026.2620213

ABSTRACT Guided by scholarship on fandom, gendered leisure, and sports gambling, this study examines a woman’s novice experience with legalized sports betting in North America. Employing an analytic autoethnography, the study documents the lead author’s first-time engagement with sports betting during the 2024–2025 National Football League season and playoffs. Data were collected through structured, reflexive journaling across weekly wagers placed on two major online sportsbooks, and an iterative coding analysis led to five interrelated themes: (1) emotional volatility across wins, losses, and near-misses; (2) platform design as both an enabler and barrier to participation; (3) shifting social dynamics and inclusion within a male-dominated betting culture; (4) a learning trajectory from hesitant newcomer to confident participant; and (5) financial decision-making as an ongoing negotiation of risk, responsibility, and confidence. Findings demonstrate that while novice sports betting exposes women to emotional strain and escalating risk, it can also function as a mechanism for legitimacy and inclusion within contemporary sport fandom. The study extends gendered understandings of sports betting beyond male-centric narratives and offers empirical insight into how novice bettors navigate sports betting. Practically, the findings suggest that sportsbooks should implement novice-oriented onboarding programs that combine betting education with emotional regulation and financial risk-management tools to reduce harm while fostering sustainable engagement.

**Решение:** -2 автоэтнография / качественное исследование личного опыта ставок без опроса

---

### 367 · R5908

**Fantasy Sports No. 2: The Bandit of Barbel Bay by Sam Bosma**

2016 · Bulletin of the Center for Children's Books./Bulletin of the Center for Children's Books · article, review, book-review · en · https://doi.org/10.1353/bcc.2016.0769

Reviewed by: Fantasy Sports No. 2: The Bandit of Barbel Bay by Sam Bosma April Spisak Bosma, Sam Fantasy Sports No. 2: The Bandit of Barbel Bay; written and illus. by Sam Bosma. Nobrow, 2016 56p (Fantasy Sports) ISBN 978-1-910620-10-6 $19.95 R Gr. 5-12 In Fantasy Sports No. 1 (BCCB 9/15), Wiz, a wizard apprentice, and Mug, an enormous hulk of a tomb raider, changed lives through basketball. No one expected them to bond, but it's clear in this second graphic-novel outing that they are closer than ever, traveling peacefully until their treasure is stolen; the only way to get it back is to win a volleyball tournament. Along the way, several questions come up about the actual nobility of the mages for whom they work, and Wiz has increasing qualms about her role in the world and whether she has aligned herself with the right folks. This is anything but a repeat of the first volume, with layers of character development making this a deeper venture, and an evolving bond between Wiz and Mug results in different dynamics between the two than in the first volume. The manga-inspired illustrations sizzle with action and drama; changing relationship to panel structure helps control pace, and an otherworldly range of colors are both discordant and inviting. A third book, which hints suggest will feature golf, can't come soon enough. Copyright © 2016 The Board of Trustees of the University of Illinois

**Решение:** -6 рецензия на детский комикс 'Fantasy Sports', не гемблинг

---

### 368 · R1674

**Regulacion y tributacion de las apuestas deportivas en Europa**

2025 · BURJC Digital (King Juan Carlos University) · dissertation · es

Trabajo Fin de Grado leído en la Universidad Rey Juan Carlos en el curso académico 2024/2025. Directores/as: Paola Plaza Casado

**Решение:** -1 дипломная работа: регулирование и налогообложение ставок в Европе

---

### 369 · R2969

**Explaining the effect of economic strain on online illegal sports betting: Empirical application of Agnew\'s general strain theory**

2023 · DOAJ (DOAJ: Directory of Open Access Journals) · article · fa

Betting on various sports competitions, gambling and crimes related to this field, due to the popularity of youth in team sports, especially football, has established its position as a facilitator channel in providing a windfall income. The high importance of sports in different countries, the wide range of sports and the attention of different groups to sports events have led to increased awareness of the sports betting industry to sports competitions. The main purpose of this study is to investigate the effect of economic strains on the involvement of individuals in illegal sports gambling. For this purpose, using 447 sample of male citizens of Bandar Anzali, Rasht, Lahijan, Rudsar and Langrud cities, which were selected by convenient sampling method, the research hypotheses were examined. The study found that objective economic strains have a significant effect on online illegal sport gambling with mediation of subjective strain, negative emotions, and deviant motivations. The socio-economic status (SES) of Respondents moderates the relationships between general strain model and illegal gambling.

**Решение:** ? опрос 447 мужчин в Иране о ставках на спорт, проверить наличие инструмента PG в полном тексте

---

### 370 · R3307

**Do You Need the Machine? Tipping in Canada Is Unconscious (Part II).**

2022 · Canadian journal of science, mathematics and technology education = Revue canadienne de l'enseignement des sciences, des mathematiques et de la technologie · journal article, journalarticle, article · eng · https://doi.org/10.1007/s42330-022-00220-7

While recovering from a major personal tipping point (see Part I), I was still able to keep on the lookout for Canadian mathematics education matters. After all, if Canadian mathematics education matters, Canadian mathematics education matters. In doing so, I ran into a number of other financial problems. Everywhere I turned was a financial problem: from tipping in the sharing (or platform) economy; to spending your way to savings with credit cards; the proliferation of sportsbooks and online casinos; trying to reconcile the Canadian cost of living with the seemingly high accepted standard level of consumption; and the outrageous fee to take $20 out of my very own bank account. Each taken on their own, I clearly have some financial problems. Taken together, I contend that 'Egan's Financial Problems', albeit unconventional, could, one day, be the impetus for financial education and literacy leaving math class and becoming a class of its own in Canadian schools. Until then, I guess we go with the School of Hard Knocks for our financial education.

**Решение:** -6 эссе об образовании и культуре чаевых, не гемблинг

---

### 371 · R6233

**The Ever-Growing Influence of Fantasy Sports**

2015 · Clio s Psyche · article, journalarticle, journal-article · en · https://doi.org/10.70763/49cbb75927723efba3b4c108ed4a12f3

With every passing year, the number of Americans participating in the playing of fantasy sports increases dramatically. From fantasy football, basketball, soccer, and every sport in between, some 33.5 million people around the nation (finance.yahoo.com, 2012) are taking the reins of their personal fantasy sports teams with the hopes of being victorious over their adversaries. These players encompass a wide variety of individuals from many walks of life, but it is through their mutual participation in fantasy games that all of these participants are able to experience an assortment of emotions that they may both relish and detest.

**Решение:** -1 культурологическое / психоисторическое эссе о росте популярности фэнтези-спорта

---

### 372 · R7857

**Odds fluctuations and potential trading profit for popular betting events**

2007 · 59 · dissertation · en

Traditionally, to make money on sports betting, one should have a high knowledge about the teams involved, and some luck. With the introduction of online betting exchanges, one can take the role o ...

**Решение:** -2 модели рынков / торговые стратегии на бирже ставок

---

### 373 · R5893

**Predictors of Fan Entitlement in Three Fandoms**

2016

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 исследование чувства права у фанатов различных фандомов, не гемблинг

---

### 374 · R0844

**Betting on the State: Sports Gambling Legalization and Municipal Borrowing Costs**

2026 · Elsevier BV · article, posted-content, preprint · und · https://doi.org/10.2139/ssrn.6502360

I estimate the effect of online sports betting legalization on U.S. state government borrowing costs in the municipal bond market. Using a stacked difference-in-differences design with secondary market bond-month observations, I find that legalization reduces bond yield spreads by 6 to 10 basis points. This effect is robust across three alternative spread measures, holds under alternative control group definitions and on a propensity-score-matched sample of bonds, and emerges gradually over the quarters following legalization. Mechanism evidence suggests a positive net fiscal effect: legalization increases state tax revenue, including an average of $53 million in annual dedicated sports betting tax collections for the treated state, while state expenditure on health, police, welfare, and hospitals does not change significantly.

**Решение:** -2 эконометрический анализ доходности муниципальных облигаций без опроса людей

---

### 375 · R1835

**Duty of care, data science, and gambling harm: A scoping review of risk assessment models**

2025 · Computers in Human Behavior Reports · article · en · https://doi.org/10.1016/j.chbr.2025.100644

Duty of care policies mandate gambling operators to identify problematic gambling behaviours amongst their customers. Online operators often employ risk detection algorithms to accomplish this task. This scoping review focuses on how such data science applications can perform from a duty of care perspective. In line with the PRISMA guidelines for scoping reviews, we systematically retrieved academic studies, reports, and industry initiatives that used statistical methodologies to predict, model, or forecast gambling behaviour. The final sample consists of 31 academic studies published between 2015 and 2025, and 11 commercial solutions. Our analysis focuses on three critical stages of model development: 1) selection of estimation data; 2) decisions related to the model estimation process; and 3) assessment and interpretation of prediction model results. Models vary in terms of predictors, dependent variables, methodological approaches and assessment. Most models attempt to identify harm that has already occurred rather than forecasting future harm. Data are typically aggregated despite higher granularity in original datasets. Measures to assess the prediction ability of models are not optimal. Industry funding or involvement is prevalent in model development. Currently, risk assessment algorithms do not function pre-emptively and are unlikely to capture the full extent of harm occurring in digital gambling. As such, their usability within the duty of care framework remains limited. Ways forward would entail openness and standardisation in terms of choice of variables, forecasting horizons, assessment of methods, and evaluation of results to improve models and regulatory oversight. • Behavioural consumer data are leveraged by gambling operators to track consumers. • Consumer data can be used for duty of care purposes to identify harmful gambling. • Existing commercial risk assessment models cannot be evaluated due to lack of openness. • Research using data science methods to identify harm varies in methodologies. • In their current form, risk detection models cannot reliably prevent gambling harm.

**Решение:** -1 обзор литературы по долгу заботы операторов и минимизации вреда

---

### 376 · R2050

**Sports Gambling Apps: A Severe Concern for Indian Society**

2025 · figshare · article, other literature type, journalarticle/journal contribution · und · https://doi.org/10.6084/m9.figshare.30062698

Social issues are multifaceted challenges that impact individuals, communities, and societies, often stemming from economic, cultural, and behavioral factors. One emerging concern is the rapid growth of sports gambling apps, which have transformed betting into an accessible, technology-driven activity. These mobile applications allow users to wager on a wide range of sporting events through features such as money-line bets, point spreads, proposition bets, and live in-play betting. While gambling apps provide convenience and entertainment, they also raise significant social concerns, including addiction, financial instability, underage participation, and mental health risks. The widespread promotion of these platforms and their immersive features intensify the potential harms, making them a subject of public debate and policy scrutiny. Addressing this issue requires balancing economic benefits with social responsibility through regulation, awareness, and support systems to mitigate negative consequences and safeguard community well-being.

**Решение:** -1 аналитический комментарий о вреде приложений спортивного беттинга в Индии

---

### 377 · R0060

**Home bias and investor sentiment: Evidence from a quasi-experimental financial market**

2026 · International Review of Financial Analysis · article · en · https://doi.org/10.1016/j.irfa.2026.105331

We use the sports betting market as a real-world market laboratory to study the home bias in individuals’ behavior. In contrast to traditional financial markets, where institutional frictions and the joint hypothesis problem confound explanations of the home bias, the sports betting market’s quasi-experimental features enable us to cleanly test whether preferential betting on home teams reflects informational advantages or behavioral forces. We find that individuals systematically favor local teams, domestic teams, and teams featuring players from their home country. This home bias does not yield superior performance but distorts individuals’ portfolios, generating welfare costs of similar magnitude to those in the stock market. Our findings help strengthen the foundation of behavioral explanations of the home bias in similar market environments.

**Решение:** -2 модель финансовой экономики / хоум-баяс на данных ставок без опроса людей

---

### 378 · R1204

**The Federal Gap in Sports Betting**

2026 · bepress Legal Repository · article

The modern sports betting market has outgrown the legal framework that governs it. Drawing on examples from the NBA, this article highlights four areas in which federal legislation is needed: player specific proposition bets, the rise of bettor harassment directed at players and coaches, the absence of a centralized public reporting and oversight structure, and the growing use of prediction market or event contract labeling to evade ordinary gambling regulation. This article contends that Congress should adopt a federal floor for sports betting that restricts the bet types most susceptible to manipulation, requires uniform reporting and oversight, imposes anti-harassment obligations on sportsbooks, and closes loopholes that allow sports betting to be marketed under alternative labels.

**Решение:** -1 правовой анализ федерального законодательства США о ставках

---

### 379 · R7253

**Are bets with the odds of 3.1 more likely than bets with the odds of 21/10? How odds in sports betting are perceived as probabilistic information.**

2011 · article · en

Aim: Chance, risk and uncertainty are expressed in various formats for decision-makers in everyday-life. In the sports-betting market the probabilities for different outcomes (e.g., Barcelona FC will beat Arsenal FC, Lee Westwood will win the 2011 Open Championship) are reflected by odds, which also determine the amount of money that consumers of betting products (henceforth punters) will receive if their bets turn out to be successful. Typically, odds are fixed and set in advance by betting firms that have proven to be extremely accurate in this task (Forrest et al., 2005; Deschamps, 2008). In Europe odds are generally expressed in either decimals (e.g., 1.61) or fractional numbers (e.g., 8/13), where the latter format is restricted to be used in the UK and Ireland. As odds can be easily converted into implicit probabilities, they may be seen as rare examples of highly predictive probabilistic forecasts. Punters are an ideal group to study when it comes to learn about how people understand and consider quantitative measures of chance, because they are not only exposed to probabilistic information but also they put their own money at stake when making decisions and, accordingly, they should be motivated to avoid judgmental biases. Surprisingly, there is limited research on the ability of punters. Thus, the aim of this paper is to empirically address the questions: Do punters realistically perceive odds? Does the presentation format affect how realistically odds are perceived? Method: 68 punters responded to a web-based questionnaire where they evaluated two randomly presented sets of 10 bets involving different odds. The sets were identical except for the format (= within-subjects design): set A had bets with decimal-odds, while set B had bets with fraction-odds. The odds reflected 10 different levels and were sampled from a season of English Premier League Football matches. For each of the 20 bets, the participants were asked to imagine 100 such bets and estimate how many that would come true. In connection, they also reported their confidence on a 7-points scale and provided an interval for the given estimate. Results: Across the ten different bets, the estimates of the mean participant were somewhat realistic, although there were systematic deviations from the true implicit probabilities. The deviations were linked to the presentation format in that the participants, on average, tended to underestimate bets with odds expressed as decimals and overestimate bets with odds as fractional numbers (M=-3.69 vs. 4.49). Greater confidence was also associated with the former format. Conclusions: Consistent with prior research on the perception of probabilistic information (e.g., Gigerenzer 2002), the perception of the odds was affected by the presentation format. Though the difference between the formats could be due to psychometrical aspects, we attribute it to the fact that the Swedish punters are more familiar with the decimal-format. The most surprising finding was that the punters underestimated the probabilities when odds were presented as decimals. We see three tentative explanations for this finding: (1) punters truly underestimate probabilities, (2) our participants deliberately adjusted their probability estimates so that they included the take-out-rate of the betting firms (betting firms adjust their odds so that they will make a profit of x%), (3) our participants assessed probabilities that were well calibrated to their prior experiences but failed to understand that the prior experience is biased by the take-out-rate of the betting firms. The questions of (i) whether or not the format-difference is caused by familiarity and (ii) why probabilities are underestimated with the decimal format are explored in two follow up studies with similar designs.

**Решение:** -3 когнитивный эксперимент по восприятию форматов коэффициентов без инструмента PG

---

### 380 · R7781

**Possession in good faith of illicit money for sports lottery——As seen from Stolen Money of Handan Agricultural Bank**

2008 · Wuhan Ti-Yuan xuebao · article · en

Possession in good faith is an important civil law to protect the owner.There have been diputes over whether illicit money can be used in possession in good faith.This study holds that possession in good faith is applicable for illicit money for sports lottery.If the issuer of the sports lottery does not know it is illicit money and has printed the lottery,even if the purchaser has paid with illicit money,the issuer is not obliged to return the money.Or else,the money should be returned.

**Решение:** -1 гражданско-правовой анализ владения похищенными деньгами при покупке лотереи

---

### 381 · R3914

**An Overview of the Economics of Sports Gambling and an Introduction to the Symposium**

2021 · Eastern Economic Journal · article, other literature type, editorial · eng · https://doi.org/10.1057/s41302-020-00182-4

Gambling likely predates recorded history. The casting of lots (from which we get the modern term “lottery”) is mentioned both in the Old and New Testaments of the Bible, most famously when Roman soldiers cast lots for the clothes of Jesus during his crucifixion. In Greek mythology, Hades, Poseidon, and Zeus divided the heavens, the seas, and the underworld through a game of chance. Organized sports also have a long history. The Ancient Olympic Games date back to 776 BCE and persisted until 394 AD. The Circus Maximum in Rome, the home of horse and chariot racing events as well as gladiatorial contests for over one thousand years, was originally constructed around 500 BCE, and the Colosseum in Rome began hosting sporting events including gladiator fights in 80 AD. Variations of the ball game Pitz were played in Mesoamerica for nearly 3000 years beginning as early as 1400 BCE (Matheson 2019). Given the prevalence of both sporting contests and gambling across many ancient civilizations, it is natural to conclude that the combined activity of sports gambling also has a long history. And, indeed it is widely reported that gambling was a popular activity at the Olympics and other ancient Panhellenic events in Greece and at the racing and fighting contests in ancient Rome. Problems associated with gambling were also widely reported. As early as 388 BCE, the boxer Eupolus of Thessaly was known to have paid opponents to throw fights in the Olympics. Rampant gambling in Rome led Caesar Augustus (c. BCE 20) to limit the activity to only a week-long festival called “Saturnalia” celebrated around the time of the winter solstice, while Emperor Commodus (AD 192) turned the royal palace into a casino and bankrupted the Roman Empire along the way (Matheson et al. 2018). Just as in the modern day, gambling was often looked down upon by societal leaders in antiquity. Horace (Ode III., 24; 23 BCE) wrote, “The young Roman is no longer devoted to the manly habits of riding and hunting; his skills seem to develop more in

**Решение:** -1 введение в сборник по экономике ставок на спорт

---

### 382 · R5877

**Youth Gambling in Croatia - Frequency of Gambling and the Occurrence of Problem Gambling**

2016 · Kriminologija & socijalna integracija : časopis za kriminologiju, penologiju i poremećaje u ponašanju · article, other literature type, journal-article · en · https://doi.org/10.31299/ksi.24.2.3

The main aim of this study was to explore the frequency of gambling and gambling-related problems among Croatian high school students. The specific objectives have been to explore gender differences, and differences in the frequency and severity of gambling problems regarding grade/age and type of school program. The study included n=2.702 high school students from all for grades and all three types of high school programs (3- and 4-year vocational/professional schools, and grammar schools) from 7 cities (Zagreb, Osijek, Rijeka, Split, Vinkovci, Slavonski Brod and Koprivnica) with equal representation of boys (n=1.330, 49.2%) and girls (n=1.372, 50.8%). The respondents’ mean age was Mage = 16.51 (SDage=1.17). The following instruments were used: Questionnaire on general socio-demographic data, Gambling activities questionnaire (Ricijaš, Dodig, Huić, &amp; Kranželić, 2011) and the Canadian Adolescent Gambling Inventory - CAGI (Tremblay, Stinchfield, Wiebe, &amp; Wynne, 2010). Results show that the lifetime prevalence of gambling among Croatian high-school students is 72.9%. The most prevalent games of chance are sports betting and lottery games, with sports betting being the most frequent of these activities. As much as 12.9% adolescents have already developed serious adverse gambling related consequences. Boys have significantly higher problem gambling rates than girls, while the effects of differences regarding the type of school and grade/age are relatively low. The results provide important baseline data for future research, interventions design, and for the improvement of social policy and legislation.

**Решение:** + количественное исследование 2702 хорватских старшеклассников, ставки на спорт, инструмент CAGI

---

### 383 · R6602

**Spatial Heterogeneity of Chinese Sports Lottery Sales and Driving Factors based ESDA-GWR**

2013 · Journal of Tianjin University Science and Technology · article · en

ports lottery has been playing a tremendous role in China's sports undertaking,social public welfare as well as public service,but it is developing with imbalance and big gaps among different provinces and regions.This study tried to dig into the spatial heterogeneity of China's Sports Lottery Sales and their driving factors by analyzing the Sports Lottery Sale amounts in different provinces between 1997 and 2012 as well as relevant provincial social development indexes in 2012 through exploratory special data analysis(ESDA)and geographically weighted regression(GWR)with the help of software like OpenGeoDa and ArcGIS10.The results from the analysis indicated that Sports Lottery Sales in the 31 provinces and regions are characteristic of distinctive spatial agglomeration,the degree of which remains relatively stable after it has gone up first and down sharply and up again;It's obvious that sports lottery operates on a territory oligopolistic market with the eastern costal provinces the most flourishing and prosperous in its sales;The logistic GWR model constructed demonstrates a high value of goodness of fit and thus can explain significantly the spatial heterogeneity of the Sports Lottery Sales among different provinces and regions in China.

**Решение:** -2 пространственный эконометрический анализ продаж спортивной лотереи

---

### 384 · R6714

**Testing the efficiency of an 'in-play' sports betting market: A Monte Carlo approach**

2013 · The University of Queensland, UQ Business School · thesis, article · en · https://api.library.uq.edu.au/view/UQ:322081

In this study, we develop a Monte Carlo simulation technique for estimating the probability of victory at any stage in the first or second innings. This model is then used to test market efficiency in the Betfair ‘in-play’ market for one-day international cricket matches. We find strong evidence of overreaction in the first innings. A trading strategy of betting on the batting team after the fall of a wicket under strict trading restriction results in a profit of 20.8% that is significant at the 1% level. We also find some evidence of underreaction in the second innings although it is less economically and statistically significant than the first innings overreaction. We also implement a series of more sophisticated strategies that aim to exploit any systematic mispricing throughout a match independent of the reaction to a particular ball. Trades are placed when the discrepancy between the probability of victory implied by current market odds differs substantially from the odds estimated by our Monte Carlo simulation. We document a number of trading strategies that yield large statistically significant positive returns in both the first and second innings, suggesting that inefficiencies exist in the ‘in-play’ market. We also use our Monte Carlo simulation technique to develop a rain rule alternative to the current Duckworth-Lewis system. Our method preserves the probability of victory across rain delays by resetting the target score such that the probability of the batting team winning the match after the rain delay is the same as it was prior to the interruption. Our method also outperforms prior models at predicting the winner of the match in the majority of situations.

**Решение:** -2 анализ эффективности рынка лайв-ставок методом Монте-Карло

---

### 385 · R8477

**Ritual in Complex and Tribal Societies**

1979 · Current Anthropology · https://doi.org/10.1086/202334

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 антропология ритуалов в племенных обществах, не гемблинг

---

### 386 · R0691

**Affect Regulation Motives for Gambling and Gambling Engagement: A Two-Year Random-Intercept Cross-Lagged Panel Model.**

2026 · International gambling studies · journal article, journalarticle, article · eng · https://doi.org/10.1080/14459795.2026.2683629

ABSTRACT The present study investigated how affect regulation motives for gambling relate to gambling frequency over a two-year period, with particular attention to differences between individuals who gamble on sports and those who gamble but not on sports. Participants were recruited from a nonprobability internet panel from two sources: a large cross-section of adults matched and weighted to US Census norms and a specific oversample of sports-gambling adults (Baseline N = 1,760). Analyzing five waves of data collected over 2 years, we found robust between-person associations: Higher gambling frequency corresponded with stronger affect regulation motives. Contrary to expectations, both coping and enhancement motives were strongly related to gambling frequency in sports gamblers, suggesting that this group may be more broadly motivated to gamble for affect regulation. At the within-person level, three consistent findings emerged across groups: (1) coping and enhancement motives were strongly correlated within timepoints, (2) gambling frequency was stable over time, and (3) elevated enhancement motives at a given time point predicted increases in gambling frequency 6 months later.

**Решение:** ? продольный опрос спортивных беттеров N=1760, проверить наличие инструмента PG в полном тексте

---

### 387 · R1861

**Analiza porównawcza zużycia wody w bliźniaczych krytych pływalniach w województwie śląskim, w Polsce**

2025 · INSTAL · article · en · https://doi.org/10.36119/15.2025.2.5

Swimming pools, due to their specific nature, are sports facilities for which demand is highest for water of a quality subject to restrictive regulations. The objective of this study is to provide a detailed characterisation of the structure of water consumption in three ‘twin’ swimming pool facilities located in Poland, in the Silesian Voivodeship. Each of the analysed facilities includes a sports pool, a recreational pool with water attractions, a water slide, a whirlpool and a children’s paddling pool. The findings of this study demonstrate a strong correlation between water consumption and the type of users and water management practices employed. In particular, it was found that recreational pools with water attractions (slides, whirlpools) used significantly more water than traditional sports pools. The findings of this case study offer a valuable foundation for the development of strategies aimed at enhancing the efficiency of water management in swimming pool facilities.

**Решение:** -6 сравнительный анализ расхода воды в плавательных бассейнах, не гемблинг

---

### 388 · R2772

**BEAT GOES ON FOR U.S. SPORTSBOOKS IN MAY**

2023 · Gaming Law Review · journalarticle, article · en · https://doi.org/10.1089/glr2.2023.0021

In what has been a run extending for nearly a full 12 months, U.S. sportsbooks continued getting the better of the public and fashioned the third monthly hold of 11% or higher to complete the fifth full year of state-by-state commercial sports wagering in the post-PASPA (Professional and Amateur Sports Protection Act) era.

**Решение:** -1 отраслевой аналитический отчет по доходам букмекеров США за май

---

### 389 · R1764

**Evolving Challenges in Sports Governance: Investigating Future Pathways For Addressing Persistent Issues like Match Fixing And Inequality**

2025 · Zenodo (CERN European Organization for Nuclear Research) · article, journalarticle/ · und · https://doi.org/10.5281/zenodo.19694712

The nature of sports governance has been subject to changing challenges that jeopardize the integrity, inclusivity and sustainability of sporting ecosystems worldwide. Such problems as match-fixing and gender inequality are discussed in this article as they negatively affect fair play and equal participation. Based on recent statistics, such as the 2024 Integrity Report of Sportradar, which found that suspicious matches decreased 17% but continued to be widespread in new leagues, and UNESCO findings that women were still underrepresented in the position of federation chair (only 30% of the major federations had women as federation chair), the study points to structural issues increased through commercialisation, globalisation and online betting. The analysis shows that the gaps are: legislative fragmentation in anti-corruption initiatives, cultural biases that persist in providing gender inequalities, and the lack of multi-stakeholder coordination through a qualitative desk-based literature review regarding 2023-2025 on the topic: UN Women, Sport for Generation Equality Initiative and the governance frameworks established by the Council of Europe. Reforms such as the gender parity of the IOC at Paris 2024 and suggested International Council Governance suggest opportunities. Suggestions include standardized international guidelines on integrity checking, mandatory gender balance in decision making entities as well as technology use in transparency mechanisms. Focusing on the priority of the political desire and the ways of collaboration, sports governance will be able to develop to guarantee the preservation of the ethical standards, _x000D_ the empowerment of the various voices, and the ability of sport to create societal unity and human progress. This study highlights the sense of urgency to implement adaptive changes to overcome dynamic threats, to promote a robust future of global sport.

**Решение:** -1 анализ проблем спортивного управления и нелегальных ставок

---

### 390 · R6575

**Das Suchtpotenzial von Glücksspielen unter besonderer Berücksichtigung von (Online-) Sportwetten**

2013 · Nomos Verlagsgesellschaft mbH & Co. KG eBooks · book-chapter · de · https://doi.org/10.5771/9783845244464-31

Spätestens seit der Unterzeichnung des neuen Glücksspielstaatsvertrags im Dezember 2011 herrscht im milliardenschweren deutschen Sportwettenmarkt Goldgräberstimmung. Mit der kontrollierten Öffnung für private Anbieter hat die Politik aus der Rechtsprechung des Bundesverfassungsgerichts und des Europäischen Gerichtshofs Konsequenzen gezogen. Abzuwarten bleibt, ob damit nun tatsächlich Rechtssicherheit einkehrt. Denn nach wie vor ist streitig, ob die Vergabe einer begrenzten Anzahl von Lizenzen sachlich begründet werden kann und der Forderung nach einer kohärenten Regulierung ausreichend Rechnung getragen wird. Im Kontext dieser Rechtsfragen hat sich zwischenzeitlich der organisierte Sport positioniert und sich dabei auch intensiv mit den Suchgefahren sowie den Risiken manipulativer Eingriffe befasst. Ob der aktuelle Betrugstatbestand des deutschen Strafrechts tatsächlich alle strafwürdig erscheinenden Formen der Manipulation sportlicher Wettbewerbe hinreichend erfasst oder es nicht vielmehr gilt, Strafbarkeitslücken zu schließen, wird weiterhin intensiv diskutiert. In den Beiträgen des vorliegenden Tagungsbandes zum wfv-Sportrechtsseminar 2011 mit dem Thema „Das Recht der Sportwette und des Wettbetruges“ werden diese Fragen von herausragenden Referenten erörtert.

**Решение:** -1 правовой и теоретический анализ потенциала зависимости ставок в Германии

---

### 391 · R6776

**Larceny Games: Sports Gambling, Game Fixing and the FBI**

2013 · Medical Entomology and Zoology · book · en

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 книга / расследование ФБР о договорных матчах и ставках

---

### 392 · R8022

**云南彩民再次中取“7星彩”500万大奖**

2006 · 青年与社会：中 · article · zh

体育彩票已在云南开出了94注500万大奖500万!3注500万!7月21日,体育彩票7星彩玩法又创造了3位500万中奖者。这3注500万分别被云南、河南、湖北的彩民的中取。至此,云南彩民在2006年中已中取了10注7星彩的特等奖,其中7注均是足额的500万,云南彩民已累计中取了94注体育彩票的500万大奖。本期是7星彩第06084期,开奖号码是7950867,这个看似

**Решение:** -4 тиражная лотерея 7-star в провинции Юньнань, нет ставок на спорт

---

### 393 · R4431

**Mathematics, Statistics, and Sports**

2020 · Mathematics in mind · other literature type, part of book or chapter of book, book-chapter · en · https://doi.org/10.1007/978-3-030-59177-9_6

This chapter defines and discusses several basic terms related to the topic of teaching mathematics and statistics, i.e., mathematics, mathematics pedagogy, statistics, statistics pedagogy, mathematics and statistics, mathematics anxiety and statistics anxiety, information, pop culture and its relationship to mathematics and statistics, games, sports, sports wagering, and the most popular sports in North America (American football, basketball, and major league ball). It addresses how sports information can provide the basis for mathematical and statistical problem-solving with selected examples.

**Решение:** -6 педагогика математики и статистики на примерах из спорта, не гемблинг

---

### 394 · R1193

**RESTRICTING SPORTSBOOK and GAMBLING ADVERTISING WITHIN FIRST AMENDMENT COMMERCIAL FREE SPEECH PROTECTIONS**

2026 · Gaming Law Review · article, journalarticle, editorial · en · https://doi.org/10.1177/25725300261469372

This article examines how the proliferation of legalized sports gambling and ubiquitous sportsbook advertising, now a fixture of broadcasts and live events, warrants targeted First Amendment restrictions on commercial speech to protect public health and safety. Recent studies show that these ads harm average sports fans by heightening problem gambling, while normalizing addictive behaviors among impressionable young viewers. Under the Central Hudson framework (1980), lawmakers can impose narrowly tailored limits such as time/place/manner bans on in-game ads, mandatory addiction-risk disclosures, and age-targeted safeguards that advance substantial government interests without unconstitutionally restricting speech, mirroring successful precedents for tobacco and alcohol advertising.

**Решение:** -1 правовой анализ ограничений рекламы букмекеров в контексте Первой поправки

---

### 395 · R6632

**Sports Communication and Modern Technology**

2013 · International Journal of Physical Education Fitness and Sports · article · en · https://doi.org/10.26524/13110

The best place to see the new world of communication may be the sports field. It encompasses some of the best in journalism, broadcasting, electronic communication, marketing, advertising, public relations, visual communication and new media. The stakes for understanding communicative practices may be even greater at the professional level. Especially because professional sports are inextricably linked to the media that broadcast, report, and opine about the games, it is next to impossible to escape the influence of professional sports. Live sporting events more available through satellite providers and Internet feeds, or that fantasy sports have produced an entire industry that is dependent on, but also separate from, sports themselves, or that community officials often insist that the key to urban development or city pride is to invest in a professional sports franchise and/or arena, or that player salaries continue to rise, often driving up the cost of attendance along with them. There are many other features to add to this list. What is critical, once again, is that communication practices are essential to the success of professional sports from expressions of collective identity found at live events to the images produced by sports media to the importance granted to sports in the vitality of a community.

**Решение:** -6 спортивная медиакоммуникация и современные технологии, не гемблинг

---

### 396 · R2058

**O Tigrinho vai às Escolas? : percepções docentes sobre apostas online no ensino médio em Porto Alegre**

2025 · Lume (Universidade Federal do Rio Grande do Sul) · dissertation · pt

Nas últimas décadas, a indústria de apostas online expandiu-se e diversificou-se, desenvolvendo diferentes plataformas e formatos de jogabilidade, como as apostas esportivas e cassinos virtuais. A expansão das apostas online no Brasil atingiu a população brasileira de forma ampla e multifacetada, especialmente na última década. Nesse contexto, este trabalho pretendeu contribuir com o campo das ciências sociais ao investigar um nicho específico, as apostas online entre estudantes do ensino médio, a partir das percepções de docentes em escolas públicas de Porto Alegre, RS. Como referencial teórico são mobilizados os conceitos de alea (Caillois, 2017), ação social (Weber, 1984) e habitus (Bordieu, 2008). Para o desenvolvimento da pesquisa, adotou-se uma abordagem qualitativa interpretativa, utilizando o método de Análise de Conteúdo de Bardin (2006), aplicada a cinco entrevistas semiestruturadas com docentes atuantes no ensino médio de Porto Alegre. A partir de um mapeamento das categorias mais recorrentes nas falas dos docentes, identificaram-se quatro temáticas predominantes: "presença das apostas em sala", "motivações dos alunos", "impactos pedagógicos e emocionais" e "respostas institucionais". Os resultados revelam que o envolvimento de estudantes com apostas online configura-se como prática social atravessada por desigualdades, expectativas de mobilidade e novas formas de socialização. As percepções docentes indicam que o fenômeno desafia o papel tradicional da escola, ao introduzir valores pautados na sorte, no risco e na busca de ganhos imediatos. A análise evidencia que as apostas online operam como expressão contemporânea das incertezas estruturais vividas pela juventude, especialmente em contextos de vulnerabilidade, e apontam para a necessidade de políticas institucionais orientadas que abordem criticamente o tema no ambiente escolar.

**Решение:** -2 качественное исследование: интервью с 10 учителями о восприятии ставок школьниками

---

### 397 · R2474

**Heuristics in highly competitive game: evidence from the fantasy National Hockey League**

2024 · Movement & Sport Sciences - Science & Motricité · article, journalarticle · en · https://doi.org/10.1051/sm/2024006

Recent findings in behavioral economics have shown that an individual may not always act optimally and rationally in their decision-making. However, these findings have come mainly from laboratory conditions, and as such, they need to be verified under real circumstances. This paper examines the presence of heuristics in the environment of fantasy sports. The data come from a fantasy league based on the National Hockey League in the season of 2015–16. Its users come mainly from the Czech Republic. The results show a moderately strong presence of representativeness. Nevertheless, there are also manifestations of not always prioritizing point-maximizing strategies, for example in the higher demand for hockey players of the same nationality as that of the users. However, the main factor influencing the demand is still the athletes’ performance. This study’s findings hold implications for fantasy sports, prompting fantasy sports participants to strategically adjust squad selection. For platforms, it suggests user experience enhancements and algorithmic adjustments to guide optimal decision-making, enriching overall engagement. Additionally, the research contributes to decision-making theory by validating behavioral economics in the real world, emphasizing context-specific biases, and advocating for an integrated understanding of heuristics and rational factors in decision environments.

**Решение:** -3 поведение пользователей фэнтези-спорта без инструмента PG

---

### 398 · R4046

**Fantasy Sports Games By PowerPlay Systems**

2021 · Zenodo (CERN European Organization for Nuclear Research) · article, journalarticle/ · en · https://doi.org/10.5281/zenodo.5647061

You can decide how many winners there will be and how often they win. You can make it super easy or very difficult to win prizes/jackpots. http://powerplaysystems.com/

**Решение:** -7 коммерческий спам на Zenodo

---

### 399 · R1376

**Apuestas y Deportes: Influencia de los pronósticos deportivos en la sociedad ecuatoriana**

2025 · Mawil Publicaciones de Ecuador, 2025 · book · es · https://doi.org/10.26820/978-9942-654-94-6

Apuestas online: un síntoma de época Por Faro Digital Faro Digital es una organización social que busca fomentar una ciudadanía digital reflexiva y crítica desde Argentina, con una perspectiva que abarca lo local, lo regional y lo global. Nuestra labor se enfoca en la educación y la comunicación para, por un lado, crear espacios de diálogo y reflexión sobre la convivencia con las plataformas digitales; por otro lado, y a través de campañas y contenidos, buscamos concientizar sobre los riesgos y oportunidades que surgen al habitar los territorios digitales. Nos enfocamos especialmente en infancias, juventudes y sus relaciones con las tecnologias, promoviendo el desarrollo de herramientas de cuidado que permitan a las comunidades ejercer sus derechos. Lo digital atraviesa nuestras vidas de manera profunda, en tanto territorios sociales (Moyano, 2022) en donde nos informamos, comunicamos, vinculamos y construimos sentido y subjetividad respecto al mundo y la realidad. Nuestra misión es abordar esos desafíos desde la diversidad de realidades y contextos. En un territorio como Latinoamérica, cargado de historias, contradicciones y potencial transformador, el conocimiento se revela como una clave para forjar un futuro más justo e inclusivo. Este prologo propone un enfoque integral y desde lo relacional de los vinculos que sostenemos con (y entre) las tecnologías de la informacion y comunicacion (Passeron, 2023) para comprender un fenómeno social creciente: las apuestas online, particularmente entre las adolescencias y las juventudes. Desde Argentina hacia Ecuador, queremos tender un puente de reflexión para entender cómo el mundo digital afecta nuestras prácticas culturales, en el contexto de la denominada "economía de la atención" y a partir del fenómeno de la monetización de nuestros cuerpos, imaginarios y subjetividades. Las apuestas online como practica cultural Las apuestas online, disponibles (al igual que todas las plataformas) las 24 horas del día, los 7 días de la semana, se han convertido en una actividad masiva, especialmente entre las adolescencias. En los talleres que brindamos en escuelas, clubes y organizaciones sociales, observamos la preeminencia de las apuestas deportivas, un fenómeno que se presenta como una actividad naturalizada, no vergonzosa y con un marcado "valor social". Entre varones jovenes, en particular, estas prácticas refuerzan dinámicas grupales y sentidos de pertenencia vinculados al conocimiento del deporte, especialmente el fútbol: ligas, tácticas, equipos y jugadores. Sin embargo, las mujeres también apuestan, siendo un fenómeno que trasciende el género, edades y contextos socioculturales. Muchos jovenes describen la "adrenalina" como un elemento central en la experiencia de apostar, alimentada por la posibilidad de ganar o perder todo. Utilizan billeteras virtuales como método de pago y frecuentemente adoptan actitudes de riesgo que se resumen en frases como "voy allin" o "juego a fondo", convirtiendo a esta en una práctica legítima y popular. Eventos de gran magnitud, como el Mundial Qatar 2022 o la Copa América 2024, han funcionado como puertas de entrada a estas prácticas, impulsadas por una maquinaria publicitaria omnipresente (que funciona como elemento "normalizador") y que incluye a influencers, ídolos deportivos, periodistas y otros referentes juveniles. La economía de la atención El auge de las apuestas online no viene de la nada. Esta práctica social y cultural se inserta dentro de un ecosistema digital en donde predominan plataformas diseñadas para captar y retener nuestra atención. Las tecnologías no son en sí ni buenas ni malas, pero tampoco neutras (Sibilia, 2023). Traen consigo valores, estilos de vida e intenciones desde su diseno. Las digitales, mediante sus sistemas algorítmicos, procesan y dan sentido a los millones de datos que dia a dia usuarios y usuarias dejamos en dichos entornos. Las notificaciones, las gratificaciones instantaneas y las recompensas visibles (como likes, visualizaciones o comentarios) se convierten así en los principales motores (en clave de horizonte pero también en clave performativa) que guían las interacciones que la ciudadanía mantiene con dichas tecnologías. Las apuestas online emergen, entonces, como una extensión natural de estas lógicas. Son una expresión concreta del mandato de la inmediatez, donde la promesa de ganar (o perder) dinero en cuestión de segundos resulta irresistiblemente seductora para quienes estan ya habituados a estos ciclos de estimulo y respuesta. En este ecosistema, el dinero deja de ser visto como un recurso tangible y estable, transformandose en un numero abstracto en una pantalla que, como las métricas de las redes sociales, parece cobrar significado solo cuando está en movimiento. La idea de "dejarlo quieto" se percibe como una pérdida potencial, reforzando un paradigma de accion constante, donde el flujo continuo se asocia con exito y progreso. Esta logica de movimiento (Baricco, 2018) como valor se encuentra también en las plataformas de redes sociales digitales en donde cada publicacion puede alcanzar determinados likes, vistas, comentarios, etc. Estos modos de funcionamiento y las practicas que generan no solo alteran nuestra relacion con el dinero, sino tambien con el tiempo. Vivimos en un presente continuo, marcado por la urgencia de actuar y la imposibilidad de esperar. Las recompensas inmediatas reconfiguran nuestra paciencia y nuestras expectativas, llevando a muchos jóvenes a adoptar comportamientos de alto riesgo, como las apuestas, con la esperanza de obtener gratificaciones rápidas. Las apuestas online son la manifestación mas visible de esta economía de la atencion, donde no solo se comercializan productos o servicios, sino tambien nuestras emociones, nuestras decisiones y, en ultima instancia, nuestras vidas. La transformación del dinero en un simbolo dinámico, que debe moverse para "tener valor", refleja cómo este modelo económico nos empuja a internalizar una narrativa de constante productividad, consumo y riesgo. La cuantificacion y monetización de la vida cotidiana Comprender el modelo de funcionamiento de las plataformas digitales es fundamental para poder analizar las maneras en que nos afectan y reconfiguran nuestras maneras de ser, pensar y dar valor a las cosas. Decimos que las apuestas no son un problema aislado, ya que forman parte de un ecosistema que premia la inmediatez, prioriza el flujo continuo y monetiza nuestros imaginarios, cuerpos y subjetividades. Esto es, nos habituamos a interactuar con plataformas en donde cada acción que realizamos tiene que tener una recompensa o gratificación; y que, a su vez, nos dejan ante la gran paradoja contemporánea: que si queremos, podemos, pero que a su vez necesitamos de la valoración de los demás. Esto sucede por lo que advierte Sibilia (2024), quien describe la forma en que se dio un desplazamiento del suelo moral de lo social. Pasamos de una modernidad en donde primaba el "deber ser" (hipocrita en palabras de la investigadora) al cinismo del "si quiero, puedo" o "yo me lo merezco". Como muestra de esto basta reconocer los discursos que se promueven cada vez mas en las arenas digitales juveniles, en donde predomina el concepto de "plata fácil". Estos manifiestos de época, envasados en stories, shorts o tik-tok's encuentran eco en las adolescencias que ven en lo digital una plataforma para poder ganar dinero desde casa y casi sin esfuerzo, a través de practicas como el trading, la venta de imágenes o mismo las apuestas. Las apuestas no son nuevas, Internet no es nuevo, las publicidades no son nuevas, las adolescencias y las juventu des no son nuevas, la ludopatía no es nueva: ¿que nos preocupa?, ¿por que ahora? Estos fenomenos son parte de una transformación cultural más profunda, donde las nociones de valor, tiempo y esfuerzo están mediadas por dinámicas hipermonetizadas. En este escenario, la confianza se vuelve un tema central, cuestionando qué se valora y cómo se construyen las relaciones económicas y sociales en nuestros vínculos cotidianos con (y entre) las plataformas digitales. Dirá Sibilia (2024): "aunque este drama parezca causado por las tecnologias digitales, ellas integran cambios historicos en los modos de vivir que se fueron gestando a lo largo de décadas y terminaron produciendo una reconfiguración tanto espacio temporal como moral" (p. 90). En este escenario, es crucial fomentar un enfoque crítico y reflexivo que permita comprender cómo estas dinámicas afectan no solo a las juventudes, sino a la sociedad en su conjunto. Las plataformas digitales, lejos de ser neutras, están imbricadas en procesos históricos y culturales que moldean nuestras decisiones y formas de relacionarnos, Desde Faro Digital, proponemos construir colectivamente herramientas de cuidado y estrategias educativas que habiliten a las comunidades a ejercer sus derechos en los territorios digitales, promoviendo un uso consciente y transformador de la tecnología. Es un llamado a imaginar alternativas más justas e inclusivas para el presente y para el futuro.

**Решение:** -1 коллективная монография / эссе о влиянии ставок в Эквадоре

---

### 400 · R0502

**PHISHING EM PLATAFORMAS DE APOSTAS ONLINE: DETECÇÃO POR PLUGIN DE NAVEGADOR**

2026 · Revista Tecnológica da Fatec Americana · journalarticle, article, journal-article · pt · https://doi.org/10.47283/9d3hze31

This article analyzes the growth of phishing attacks on online betting platforms in Brazil and proposes a preventive solution through a browser plugin. Fraudulent websites exploit user trust via page cloning, pop-ups, and malware, compromising sensitive information and transaction security. The hypothesis is that a plugin capable of analyzing domain reputation, SSL certificates, redirects, and download links can significantly reduce fraud risk. Three real phishing cases were examined, revealing technical and behavioral patterns that guided the tool’s development and validation. Results show that the proposed solution effectively mitigates attacks, enhances user protection, and strengthens trust in online betting platforms, contributing to a safer digital ecosystem

**Решение:** -6 информационная безопасность: обнаружение фишинга браузерным плагином
