# Калибровка вслепую, часть 2

Калибровка вслепую, часть 2: записи 151–300 из 400. Это случайные 400 записей из 7728 в списке к отбору финального поиска 2026-10-18 (зерно 20261018, порядок случайный). **Меток ИИ здесь нет.** Размечайте в любом порядке и в несколько заходов. Когда закончите все части, скажите: я проверю, что всё размечено, и закоммичу файлы до того, как открою метки ИИ.

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

### 151 · R6175

**The implied volatility of a sports game**

2015 · https://doi.org/10.1515/jqas-2014-0095

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -2 моделирование подразумеваемой волатильности в спортивных матчах

---

### 152 · R3865

**Why Do Individuals Engage in In-Play Sports Betting? A Qualitative Interview Study.**

2021 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-020-09968-9

Abstract Increasing technological advancements and changing consumer behavior has resulted in individuals having access to a wider range of online gambling markets and sporting events than ever before. Sports betting in real time has been aided by the accessibility of smartphone devices. Consequently, the popularity of live sports betting (i.e., ‘in-play’ betting) has spread across Europe and around the rest of world. The aim of the present exploratory study was to examine attitudes and opinions towards online sports betting. Qualitative interviews were conducted with 17 males and 2 females aged between 21 and 32 years. Participants were asked a range of semi-structured interview questions based on pre-determined topic areas. Socio-demographic data were collected and the Problem Gambling Severity Index (PGSI) was used to assess problem gambling. The data were analyzed using thematic analysis in order to identify themes. Analysis of the transcripts identified several notable areas including the ease of engaging in in-play sports betting, motivations for engaging in in-play sports betting (including increased excitement, demonstrating knowledge/skill and response to live odds), and different reasons for using the ‘cash-out’ feature. The findings will contribute to the design of future research investigating in-play sports betting behaviours.

**Решение:** -2 качественное феноменологическое исследование лайв-ставок без опроса

---

### 153 · R4650

**Recall and awareness of gambling advertising and sponsorship in sport in the UK: a study of young people and adults.**

2019 · Harm reduction journal · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1186/s12954-019-0291-9

BACKGROUND: The impact of gambling advertisements shown during sporting events on young people is an important public health issue. While extensive research has taken place in Australia, there is still only a limited understanding of this issue in the United Kingdom (UK). METHOD: A mixed methods study was conducted with 71 family groups comprised of 99 young people (8-16 years) and 71 adults recruited at six sites across South London, England (May-July 2018). Interviewer-assisted surveys investigated recall and awareness of sports betting brands using interviews and a magnet placement board activity developed in Australia. Quantitative data were analysed using descriptive statistics, with qualitative data interpreted using thematic analysis techniques. RESULTS: Just under half of young people (n = 46, 46%) and more than two thirds of adults (n = 49, 71%) were able, unprompted, to name at least one gambling brand. Boys had a significantly higher recall of brands than girls, as did young people who watched a lot of football on television. Almost two thirds of young people (n = 63, 63%) correctly placed one or more shirt sponsor magnets next to the corresponding football team, and 30% (n = 30) correctly placed three or more sponsors magnets next to the corresponding football team. Just under two thirds of adults (n = 44, 62%) correctly placed one or more shirt sponsors magnets next to the corresponding football team. Young people recalled seeing gambling advertising on television (n = 78), technology/screens (n = 49), and in association with sports teams (n = 43). Adults recalled seeing advertising on television (n = 56), on technology/screens (n = 37), in sports stadiums (n = 34), and in betting venues (n = 34). Over three quarters of young people (n = 74 out of 95 responses, 78%) and 86% of adults (n = 59 out of 69 responses) thought that betting had become a normal part of sport. CONCLUSION: In order to reduce the exposure of young people to gambling advertising, policymakers in the UK should consider comprehensive approaches, similar to those applied in tobacco control, which cover all forms of advertising, including promotion and sponsorship.

**Решение:** -3 исследование узнаваемости рекламы ставок без инструмента проблемной игры

---

### 154 · R7727

**Fantasy sports communities on the internet**

2008 · Michigan State University · doctoral thesis, text/dissertation · und · https://doi.org/10.25335/m5gt5ft2p

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? диссертация об интернет-сообществах фэнтези-спорта, нет аннотации, проверить полный текст

---

### 155 · R7424

**Challenges & directions in distributed event-based systems for a web-scale enterprise**

2010 · ACM International Conference on Distributed Event-Based Systems (DEBS) · article, conference object, journalarticle · en · https://doi.org/10.1145/1827418.1827447

Betfair is the world's leading online betting exchange, a concept it has pioneered. This presentation will describe how Betfair has used distributed event-based systems to meet its continuous technology challenge - to manage the explosive growth in transaction numbers and the cost of each transaction whilst offering the very best service to its customers, the business, its partners and regulators. The speaker will outline the role he sees distributed event-based systems playing in the future in dynamic & reactive, web-scale transaction processing systems.

**Решение:** -2 распределенные событийно-ориентированные системы для бирж ставок

---

### 156 · R3280

**Moderating Effects of Herding Bias on the Relationship Between Parental Monitoring and Problem Gambling of Youths.**

2022 · Journal of gambling studies · journal article, journalarticle, article · eng · https://doi.org/10.1007/s10899-021-10061-y

One critical issue in problem gambling is its variation as a function of psychosocial factors. We used empirical data from Nigerian youth Soccer gamblers (N = 238) to explore gambling herding bias as a moderator of the relationship between parental monitoring and problem gambling. Specifically, examine how changes in parental monitoring influence changes in problem gambling, and how this influence is a function of levels of herding bias. Hayes PROCESS macro analysis results revealed that increase in parental monitoring was associated with decrease in problem gambling, whereas increase in herding bias was associated with increase in problem gambling. Herding bias positively moderated the relationship between parental monitoring and problem gambling such that, for respondents who had high and moderate herding bias scores, the relationship between parental monitoring and problem gambling was positive and strong, whereas, for repondents with low herding bias scores, the relationship between parental monitoring and problem gambling was negative. The present study reaffirms the negative and positive influences of parental monitoring and herding bias, respectively, on problem gambling among youths.

**Решение:** + количественное исследование нигерийских футбольных беттеров, измерена проблемная игра

---

### 157 · R1046

**Final R analysis code: Payment preferences and related sports betting behavior**

2026 · OSF Preprints (OSF Preprints) · preprint

Final R source code and documentation accompanying the accepted Journal of Gambling Studies article, Payment preferences and related sports betting behavior: A secondary analysis of player data from an online sports gambling operator. This release contains five R scripts and a README. Raw transactional data cannot be shared due to data use restrictions. See the README for input filenames and execution instructions.

**Решение:** -3 данные оператора / транзакции без инструмента проблемной игры

---

### 158 · R0514

**৳ +91-7297856580 ৳ Trusted online betting id free In Chandigarh**

2026 · ResearchHub Technologies, Inc. · casereport, report · und · https://doi.org/10.55277/researchhub.2p54f95p

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -7 коммерческий спам на ResearchHub

---

### 159 · R2452

**Fantasy Cricket Team Generator**

2024 · SSRN Electronic Journal · preprint · en · https://doi.org/10.2139/ssrn.4977691

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -2 генератор составов в фэнтези-крикете без опроса людей

---

### 160 · R8313

**接轨 错轨 转轨——三看全运**

2001 · 体育博览 · article · zh

中国古人以九为阳数之最,全运,在风风雨雨中已经走到第九届;四十不惑,五十而知天命,全运,如今就走在不惑与知天命之间。新世纪之初,我们又该如何审视这个独具中国特色的庞然大物呢?接轨:成功的市场动作与一流的科技、环保有句民谣叫“东西南北中,发财到广东”。早在14年前的第六届全运会上,广东人就敢为天下先,创下不少中国第一:第一次不要国家拨款而由地方政府自筹资金,第一次发行体育彩票,第一次有了指定产品和吉祥物专利权。14年过后,广东人自然要做得更好。为了九运集资,组委会专门成立粤兴公司以减少中间环节。将全部资源重新定位包装,对所有有形、无形资源都进行了立体全方位的开发、拍

**Решение:** -6 журналистская статья о Спартакиаде народов КНР, не гемблинг

---

### 161 · R2502

**Does Smart Money Believe in the Hot Hand? Evidence From Daily Fantasy Baseball**

2024 · American Behavioral Scientist · article, journalarticle, journal-article · en · https://doi.org/10.1177/00027642241235828

The behavior of informed traders, or “smart money,” in sports betting markets has long been of interest to researchers. In this paper, we focus specifically on the behavior of smart money in Major League Baseball (MLB) daily fantasy sports (DFS) contests to determine whether they avoid cognitive-behavioral biases to increase their expected earnings. Specifically, we investigate whether smart money avoids the hot hand bias, where individuals tend to overestimate the likelihood of success for players on a hot streak. Using a dataset of MLB DFS contests, we find that winning lineups have lower usage rates for players exhibiting the hot hand compared to losing lineups. This suggests that smart money identifies and fades the hot hand strategy to increase their expected earnings.

**Решение:** -2 анализ рыночного поведения и когнитивных искажений в DFS без опроса людей

---

### 162 · R0708

**Gambling Disorder and Suicide Risk: A Critical Gap in Psychiatric Assessment Guidelines.**

2026 · Journal of gambling studies · journal article, review, journalarticle · eng · https://doi.org/10.1007/s10899-026-10511-5

The rapid expansion of online gambling platforms - fueled by smartphone accessibility, legalized sports betting, and novel prediction markets - has thrust gambling disorder (GD) into the spotlight. This commentary outlines the growing public health implications of GD, emphasizing the alarming association with suicidality. Suicidal ideation and suicide attempts are common in this population, and suicide is a leading cause of death among those with GD as well. Despite these risks, national physician guidelines lack standardized recommendations for suicidality screening in this population. Current screening and treatment gaps are reviewed across key U.S. institutions and the current treatment landscape, including emerging pharmacologic interventions, is summarized. While behavioral therapies remain the standard of care, the rise in digital gambling necessitates urgent interdisciplinary efforts to update clinical practice. Psychiatric organizations must develop consensus guidelines that integrate suicide risk screening into routine GD assessment. Without timely identification and targeted interventions, the growing population affected by GD will continue to face unrecognized and untreated suicide risk within a rapidly evolving digital landscape.

**Решение:** -1 клинический комментарий / эссе о суицидальном риске при расстройстве гемблинга

---

### 163 · R5016

**Diagnostico empresarial, plan de mejoramiento y plan de impacto de la Empresa Seapto S.A.**

2018 · dissertation · es

En Colombia, las empresas enfocadas a ofrecer servicios han presentado un constante crecimiento gracias a la evolucion tecnologica a partir de los anos 90’ y el aprovechamiento de las mismas, lo cual creo un desarrollo constante en todas las actividades economicas del pais; por consiguiente se genero un incremento en las ofertas de los servicios a base de la tecnologia en cada departamento, con tal sentido se busca hacer la vida de las personas un poco mas facil con respecto a ofrecer servicios de base tecnologica. La empresa Seapto SA, la cual tiene una red de servicios ofrecida en el departamento del Tolima, esta aprovecho desde su creacion las necesidades de su poblacion objetivo con la finalidad de desarrollar servicios innovadores con la ayuda de las tecnologias de informacion y comunicacion, basadas principalmente en la oferta de juegos de azar; evolucionando a traves del tiempo con el ofrecimiento de apuestas deportivas, corresponsal bancaria, recaudo de facturas, giros nacionales, etc. Segun los procesos ejecutados por la empresa durante un tiempo considerable se tomo la decision de desarrollar un estudio investigativo a traves de un Diagnostico Empresarial, con el cual se logren detectar fortalezas y debilidades de la empresa en su funcionamiento completo por cada una de las areas; de igual manera desarrollar un plan de mejora general que permita contrarrestar las debilidades detectadas en el proceso anterior y para el final desarrollar e implementar un plan de impacto que permita generar un incremento en su demanda potencial. Se debe tener en cuenta que este trabajo servira como una guia futura para la empresa y que no se Seapto SA estableceran costos, valores o precios en los apartados necesarios tales como el plan de impacto, principalmente por los cambios constantes en los precios de las productos y servicios ofrecidos por las empresas Colombianas.

**Решение:** -1 бизнес-план и диагностика компании Seapto S.A.

---

### 164 · R8281

**Expekt - A study of Expekt.com from a strategic point of view**

2001 · Gothenburg University Publications Electronic Archive (Gothenburg University) · article · en

The discussion during the last few years about the importance of working with strategy has been in some ways neglected because of the entrance of Internet. This issue has intrigued us and so we asked ourselves the question, what has happened with the traditional strategic business models that the business community for so many years have been using? \n\nMichael Porter created one of the most traditional business strategy models during the eighties. It became increasingly interesting for us to uncover if his theories still have a value in today's Internet economy. With this background in mind, we have formulated the following problems: In general, to what extent, are the existing strategic schools pertaining to the e-business companies? Specifically, is the strategic framework by Michael Porter suitable for the Internet based e-businesses? If this is not the case, might there be a need to complement Porters theory with other approaches?\n\nWe have chosen to answer our stated questions by following the start up process of one e-commerce business in United States. The company is called Expekt.com and they are in the beginning of their expansion as a startup. Expekt.com's business idea is to provide the market with comprehensive interactive online betting services on the Internet. We have taken an active part with them during their entrance into the US market \n\nTherefore we have decided to answer our problem questions by gathering data in two ways: From our own observations through the initial process of Expekt.com into the United States, and from interviews made with each market's manager for Sweden, Norway, Denmark, Finland and Germany.\n\nThe conclusions from this thesis are integrated with the issue that Porters theory of five-forces fulfills a very important purpose for e-commerce, but yet the theory needs to be complement by other strategic approaches to make it functionally viable for Expekt.com and other e-commerce companies.

**Решение:** -1 стратегический менеджмент букмекерской компании Expekt.com

---

### 165 · R5520

**Improving Employment Opportunities for Formerly Displaced Youth in Northern Uganda**

2017 · OpenDocs (Institute of Development Studies) · article · en

The national youth (persons between 18 and 30 years of age) unemployment rate in Uganda currently stands at 19.7 per cent, and a significant proportion are returned, formerly displaced youth, displaced as a result of the Lord’s Resistance Army (LRA) civil war in the northern part of the country. Despite resettlement, youth in these communities continue to be marginalised by post-conflict reconstruction \nprogramming. In the absence of effective government initiatives, displaced youth have come up with self-identified income-generating activities outside socially accepted norms, including prostitution, gambling, sports betting and contemporary dancing. Improving youth employment opportunities will require the Ugandan government to involve young people more closely in policy formulation, implementation and evaluation; broaden the current definition of employment and localise national \npolicies to address the needs of displaced communities in northern Uganda.

**Решение:** -6 программа занятости перемещенной молодежи в Уганде, не гемблинг

---

### 166 · R5358

**Is Medicine Use for Nervousness Associated with Adolescent At-Risk or Problem Gambling?**

2017 · European Addiction Research · article · en · https://doi.org/10.1159/000479001

OBJECTIVE: To examine the association between adolescent at-risk or problem gambling (ARPG) and medicine used to treat nervousness in a large-scale nationally representative sample of Italian adolescents. STUDY DESIGN: Data from the 2013/2014 Health Behaviour in School-aged Children Survey was used for cross-sectional analyses (a sample of 20,791 15-year-old students). Self-administered questionnaires were completed by a representative sample of high-school students. Respondents' ARPG, use of medicine for nervousness and potential confounding factors were assessed. Multilevel logistic regression analyses were used to test the association between medicine use to treat nervousness and ARPG. RESULTS: The overall prevalence of adolescents reporting medicine use for nervousness in the last month was 6.3%. The odds of ARPG were 3 times higher among adolescents who used medicine for nervousness compared to that among adolescents who did not take such medicine (OR 2.96, 95% CI 2.07-4.25). Importantly, the association between medicine used to treat nervousness and ARPG did not vary significantly when viewed in light of psychological symptoms. CONCLUSIONS: Medicine use to treat nervousness is associated with increased risk of gambling-related harm.

**Решение:** ? национальный опрос итальянских подростков с инструментом PG, проверить выделение ставок на спорт в полном тексте

---

### 167 · R3283

**Impact of wagering inducements on the gambling behaviors of on-line gamblers: A longitudinal study based on gambling tracking data.**

2022 · Addiction (Abingdon, England) · article, journal article, observational study · eng · https://doi.org/10.1111/add.15665

Abstract Aims To estimate whether the use of wagering inducements has a significant impact on the gambling behaviors of on‐line gamblers and describe this temporal relation under naturalistic conditions. Design This longitudinal observational study is part of the second stage of the Screening for Excessive Gambling Behaviors on the Internet (EDEIN) research program. Setting Gambling tracking data from the French national on‐line gambling authority (poker, horse race betting and sports betting) and from the French national lottery operator (lotteries and scratch games). Participants A total of 9306 gamblers who played poker, horse race or sports betting and 5682 gamblers who played lotteries and scratch games completed an on‐line survey. The gender ratio was largely male (between 87.1% and 92.9% for poker, horse race betting and sports betting, and equal to 65.1% for lotteries). Median age ranged from 35 (sports betting) to 53 (horse race betting and lotteries). Measurements The survey used the Problem Gambling Severity Index (PGSI) to determine the status of the gamblers (at‐risk or not). Gambling tracking data included weekly gambling intensity (wagers, deposits), gambling frequency (number of gambling days), proxies of at‐risk gambling behaviors (chasing and breadth of involvement) and use of wagering inducements. Findings The use of wagering inducements was associated with an increase of gambling intensity [β between −0.06 (−0.08; –0.05) and 0.57 (0.54; 0.60)], gambling frequency [β between 0.12 (0.10; 0.18) and 0.29 (0.28; 0.31)] and at‐risk gambling behaviors [odds ratio between 1.32 (1.16; 1.50) and 4.82 (4.61; 5.05)] at the same week of their use. This effect was stronger for at‐risk gambling behaviors and at‐risk gamblers. Conclusions Wagering inducements may represent a risk factor for developing or exacerbating gambling problems.

**Решение:** + лонгитюдное исследование свыше 9000 спортивных беттеров и игроков с PGSI

---

### 168 · R6795

**Sales Volume Prediction of the Sports Lottery Based on ARIMA Model——Taking Shanghai as an Example**

2013 · Sport Science Research · article · en

Prediction of the sales volume of the sports lottery in future may provide scientific reference for the design of the sports lottery products and marketing promotion.Taking Shanghai as an example and using the model of ARIMA,the paper makes a time series analysis of the monthly sales data of Shanghai sports lottery from January 2009 to March 2013.It predicts the sales volume of Shanghai sports lottery in the years of 2013-2015 and makes an analysis of the growth trend of the sales volume of Shanghai sports lottery.

**Решение:** -2 модель ARIMA для прогнозирования объема продаж спортивной лотереи

---

### 169 · R1598

**A Genetic Algorithm for Optimizing Fantasy Football Trades with Playoff Biasing**

2025 · arXiv (Cornell University) · article, preprint, journalarticle · und · https://doi.org/10.48550/arxiv.2511.17535

Fantasy football leagues involve strategic player trades to optimize team performance. However, identifying optimal trades is complex due to varying player projections, positional needs, and league-specific scoring. Existing approaches focus on team selection or lineup optimization, but automated trade generation remains underexplored. In this paper, an algorithm that generates optimal trades, biasing toward improved playoff performance while maintaining apparent fairness for negotiation is explored. We introduce a genetic algorithm for fantasy football trade optimization, building on existing frameworks for team selection and lineup generation. The algorithm initializes with single-player trades, evolves through custom mutations (add/remove players, combine trades, exchange players, add from other trades, and spawn new trades), and uses team-specific elitism to preserve diversity. The cost function incorporates a playoff-weighted gain for the user's team (while maintaining apparent fairness), opponent gain, and fairness penalty. Integration with ESPN data sources enables real-time projections for all positions, including kickers and defenses. On a 12-team ESPN league (Week 8, 2025), the algorithm generated trades that upgraded the projected point totals of both the trade initiator and trade partner by nearly 3 fantasy points per week ensuring positive gains for both teams. The algorithm demonstrates effective trade optimization, with potential extensions to other fantasy sports or combinatorial problems requiring temporal biasing. Open-source implementation enables practical use and further research.

**Решение:** -2 генетический алгоритм для обменов игроками в фэнтези-футболе

---

### 170 · R2792

**Gambling Before and During the COVID-19 Pandemic Among European Regular Sports Bettors: An Empirical Study Using Behavioral Tracking Data.**

2023 · International journal of mental health and addiction · article, journal article, journalarticle · eng · https://doi.org/10.1007/s11469-020-00327-8

Abstract The novel coronavirus-2019 (COVID-19) pandemic has had major impacts on most societies worldwide including the cancelation and postponement of sports events. This has had a major impact on the sports betting industry. The present study is first to investigate the behavior of a sample of online sports bettors before and after COVID-19 measures were put in place by European governments. The authors were given access to the player data by a large European online gambling operator comprising players from Sweden, Germany, Finland, and Norway. The behavioral change of the sports bettors before March 7 and after March 7 (2020) was computed. All sports bettors who placed at least one wager in at least 5 calendar weeks out of the 10 possible calendar weeks between January 1 and March 7 ( n = 5396) were included in the analysis. Results showed statistically significant reductions among sports bettors wagering in online casinos. This indicates that there was no conversion of money spent from sports betting to online casino games, at least for this particular online gambling operator. The findings suggest that there was a significant decrease in the amount of money wagered by sports bettors during the COVID-19 pandemic (compared with before it) and that sports bettors did not switch to playing more online casino games and that there was also a significant reduction in playing online casino games among sports bettors.

**Решение:** -3 транзакционные данные оператора о спортивных ставках без опросника PG

---

### 171 · R3891

**New bi-partisan bill proposes expansion of sports betting outside tribal casinos in Washington state**

2021 · Q13 FOX · article · en

The bill would make sports betting legal in card rooms and race tracks – and not just on tribal land.

**Решение:** -1 новостная заметка о законопроекте по ставкам на спорт

---

### 172 · R0733

**Gambling and screening for gambling problems in high school students before and after legal gambling age: associations with gender and gambling-related attitudes.**

2026 · Frontiers in public health · journal article, journalarticle, review · eng · https://doi.org/10.3389/fpubh.2026.1805134

Introduction Adolescence is a period associated with increased risk of gambling problems. Although strict age limits should apply in modern digital gambling platforms, gambling in minors remains a challenge. The present study aimed to study high school students’ gambling both before and after the legal gambling age, and to study associations between gambling-related attitudes and screening positive for problem gambling. Materials and methods The study is based on a digital survey which was distributed by teachers to high school students in Lund, Sweden, in April/May, 2025 ( n = 528). Self-reported history of gambling was reported for each form of gambling, and problem gambling was screened for using the three-item NODS-CLiP and combined with demographic data and gambling attitudes. Risk factors for screening positive for problem gambling were studied in multivariate logistic regression analyses, including gender and age, measures of gambling-related attitudes, and each separate gambling form. Results A positive screen for problem gambling (NODS-CLiP &amp;gt;0) was seen in 16% at age 16, 15% at age 17, and 27% at age 18–19, in total among 31% of boys and 4% of girls. Gambling on online casino was reported by 41% if 18 + years and by 20% if below 18 years of age, and sports betting by 32 and 21% before and after 18 years of age, respectively. Screening positive for problem gambling was more common in case of parental acceptance of gambling, hiding gambling from parents, and liberal attitudes towards gambling policy, and in the multivariate analysis, problem gambling was significantly associated with online casino, sports betting, and gambling within videogames. Conclusion In the present high school survey, gambling was very common, even before legal gambling age. Participants commonly screened positive for problem gambling, with a large risk increase in boys, and most strongly associated with online casino, sports betting, and gambling within videogames. Society-level policy interventions, as well as individual prevention targeting gambling attitudes, are called for.

**Решение:** + количественное исследование 528 шведских старшеклассников, ставки на спорт, скрининг NODS-CLiP

---

### 173 · R4899

**Machine Learning in Football Betting: Prediction of Match Results Based on Player Characteristics**

2019 · Applied Sciences · article, journal-article · en · https://doi.org/10.3390/app10010046

In recent times, football (soccer) has aroused an increasing amount of attention across continents and entered unexpected dimensions. In this course, the number of bookmakers, who offer the opportunity to bet on the outcome of football games, expanded enormously, which was further strengthened by the development of the world wide web. In this context, one could generate positive returns over time by betting based on a strategy which successfully identifies overvalued betting odds. Due to the large number of matches around the globe, football matches in particular have great potential for such a betting strategy. This paper utilizes machine learning to forecast the outcome of football games based on match and player attributes. A simulation study which includes all matches of the five greatest European football leagues and the corresponding second leagues between 2006 and 2018 revealed that an ensemble strategy achieves statistically and economically significant returns of 1.58% per match. Furthermore, the combination of different machine learning algorithms could neither be outperformed by the individual machine learning approaches nor by a linear regression model or naive betting strategies, such as always betting on the victory of the home team.

**Решение:** -2 машинное обучение для прогнозирования результатов футбольных матчей

---

### 174 · R7162

**Segmenting Motivation: An Analysis of Fantasy Baseball Motives and Mediated Sport Consumption**

2011 · Sport Marketing Quarterly · journalarticle, article · en · https://doi.org/10.1177/106169341102000302

Fantasy sport consumer behavior research is a burgeoning area of inquiry as this growing segment of sport fans exhibits unconventional, yet robust media consumption habits. In addition, consumer motivation and market segmentation represent core principles within the study of marketing, yet the integration of these two essential concepts with regard to sport consumers is limited. The purpose of this study was to explore fantasy baseball motives, develop a motive-based taxonomy of users, and quantify the differences between segments through an examination of mediated sport consumption. An exploratory hierarchal cluster analysis with a subsequent K-means analysis was conducted to determine the number of segments. Additionally, a MANOVA was performed to ascertain behavioral differences between the motive-based clusters. Four distinct segments emerged with statistically significant differences between each with regard to mediated consumption intentions. The following paper addresses theoretical and practical implications for academics and practitioners. Future research is also suggested.

**Решение:** -3 опрос мотивов участников фэнтези-бейсбола без инструмента PG

---

### 175 · R5200

**Duckwort–Lewis run out?**

2018 · ANZIAM Journal · article · en · https://doi.org/10.21914/anziamj.v57i0.10477

In one-day cricket matches the two competing teams have the same number of overs, typically 50, and the highest scoring team wins, with ties possible but unusual. If the match is interrupted, then the Duckworthâ€“Lewis method is accepted by the International Cricket Council as the algorithm for deciding the result. In 2007, John Turner suggested an alternative method, named the Player Specific Method, that models the performance of batters against different types of bowlers and the remaining time in an innings, and then uses computer simulation to generate an ensemble of possible scores. Then, either the mean value of these scores is used to determine the winning team, or a probability is assigned to one of the teams winning. This method is illustrated for the one-day match between Australia and Sri Lanka at the MCG on 22nd February 2008, and its feasibility as an alternative to the Duckworthâ€“Lewis method is discussed. References F. Duckworth and T. Lewis. Duckworth Lewis: the method and the men behind it. SportsBooks Ltd, 2011. S. E. Stern. The Duckworth–Lewis–Stern method: extending the Duckworth–Lewis methodology to deal with modern scoring rates. J. Oper. Res. Soc. 67(12):1469–1480, 2016. doi:10.1057/jors.2016.30 J. Piotto Duckworth Lewis, Run Out? Honours thesis, University of Adelaide, 2008. Sambit Bai. ESPN Cricinfo. http://www.espncricinfo.com/ The R Project for Statistical Computing. Vienna, Austria, 2013. http://www.R-project.org/ T. W. Yee. The VGAM package for categorical data analysis. J. Stat. Softw. 32:1–34, 2010. doi:10.18637/jss.v032.i10

**Решение:** -6 алгоритм подсчета очков в крикете при дожде, не гемблинг

---

### 176 · R4002

**INTERVIEW: THE IMPACT OF COVID-19 AND THE EVOLVING GAMING LANDSCAPE**

2021 · Gaming Law Review · editorial · en · https://doi.org/10.1089/glr2.2021.29024.srk

Gaming Law ReviewVol. 25, No. 6 InterviewsINTERVIEW: THE IMPACT OF COVID-19 AND THE EVOLVING GAMING LANDSCAPESteve Ruddock and Sue SchneiderSteve RuddockSteve Ruddock is the editor-in-chief of Gaming Law Review.Search for more papers by this author and Sue SchneiderSue Schneider is the vice president of growth and strategy, Americas, at Sports Betting Community (SBC).Search for more papers by this authorPublished Online:10 Aug 2021https://doi.org/10.1089/glr2.2021.29024.srkAboutSectionsView articleView Full TextPDF/EPUB Permissions & CitationsPermissionsDownload CitationsTrack CitationsAdd to favorites Back To Publication ShareShare onFacebookXLinked InRedditEmail View articleFiguresReferencesRelatedDetails Volume 25Issue 6Aug 2021 InformationCopyright 2021, Mary Ann Liebert, Inc., publishersTo cite this article:Steve Ruddock and Sue Schneider.INTERVIEW: THE IMPACT OF COVID-19 AND THE EVOLVING GAMING LANDSCAPE.Gaming Law Review.Aug 2021.271-274.http://doi.org/10.1089/glr2.2021.29024.srkPublished in Volume: 25 Issue 6: August 10, 2021KeywordsCOVID-19casino gamblinginternet gamblingsports bettingPDF download

**Решение:** -1 интервью с экспертами об эволюции гемблинга во время пандемии

---

### 177 · R5183

**Methods Cases Submission for Consideration Case Title The use of different qualitative methodologies in analysing online sports betting adverts**

2018

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -2 качественная методология анализа рекламы ставок без опроса людей

---

### 178 · R7000

**P-76 - Evaluation of an Italian sample of gamblers with dannon ainhold gambling scale: preliminary study**

2012 · European Psychiatry · article, conference-abstract · en · https://doi.org/10.1016/s0924-9338(12)74243-8

Introduction Pathological gambling (PG) disorder occurs when a person gambles repetitively despite severe negative effects on important aspects of life. PG tends to be a heterogonous disorder in which patients differ with respect to type and intensity of gambling behavior, psychiatric comorbidity, family history, age at onset and gender. Gamblers may accordingly be classified into three subtypes: the “impulsive”, “obsessive-compulsive” and “addicted” subtypes. Aims to characterize a sample of Italian PG pathological gamblers and assess the prevalence of the various gambling subtypes in this population. Methods 52 outpatients (44 men, 9 women), diagnosed with PG according to DSM IV-TR and SOGS criteria, were administered the Dannon Ainhold Gambling Scale (DAGS), which assesses the presence of the disorder and is useful for patient subtyping. Results 37 gamblers enrolled in our study played one specific kind of game, while 15 played multiple games. 30 patients played slot machines, 18 sport betting, 11 casino and card games, 14 bingo and scratch cards. According to DAGS, 5 (9,6%) patients belonged to the “addicted” subtype, 4 (7,7%) to the “obsessive-compulsive” subtype and 9 (17,3%) to the “impulsive” subtype. 15 (28,8%) gamblers were classified as “addicted-impulsive” subtype, 10 (19,2%) as “addicted-obsessive-impulsive” subtype, while 9 (17,3%) did not belong to any specific subtype though they displayed a tendency for one of the subtypes. Conclusion DAGS allows to identify three major subtypes of gamblers and also considers possible combinations between the different subtypes. An evaluation of these aspects could be useful in treatment options based on patient subtype.

**Решение:** -5 клиническая выборка амбулаторных пациентов с патологическим гемблингом

---

### 179 · R4103

**DEUSTO Social Impact Briefings No. 4 (2019)**

2020 · Impacto social · book · en · https://doi.org/10.18543/dsib-4(2020)

This fourth edition of the DSIB presents the main results of the research carried out under four broad-based projects jointly developed by researchers and actors involved in topics of great social relevance such as responsible gambling, Cooperative-Intelligent transport Systems, gender dimension of alcohol addiction and support and care for victims of trafficking for sexual exploitation. This issue comprises the following four briefings: 1. What would sports betting advertising be like if it were handled more responsibly? will analyse the structure of sports betting advertising, in an attempt to understand whether such advertising could become a public health issue. This briefing examines different works that have led to scientific publications and presents their main conclusions as well as the major recommendations for gambling companies and regulators. 2. How can artificial intelligence reduce road traffic accidents and prevent congestion? This briefing seeks to present the benefits of the TIMON system for optimising traffic management and urban transport network operations in cities, directly supporting transport managers in their decision-making processes for transport operations. 3. Gender inequalities in matters of drug addiction: how does alcoholism really affect women? aims to study the phenomenon of drug dependence from a gender perspective. This involves identifying what kind of socio-cultural and psychological representations are involved in women, according to their gender role, so that they develop a series of risk factors for them, both for the beginning of consumption and in its continuity. In addition, the research team proposes guidelines for a specialized care for women in this area, in order to increase the effectiveness of required interventions. 4. Key points for supporting and accompanying victims and survivors of human trafficking for sexual exploitation is intended as a working document for specialists involved in the prevention and detection of cases and in support and care for victims. It seeks to fill the current gaps and meet the needs of women victims of trafficking providing a better response to their situations.

**Решение:** -1 институциональный аналитический отчет / брифинг Deusto

---

### 180 · R3847

**Rediseño de la arquitectura del software y reimplementación de una página web**

2021 · Universitat Politècnica de València · bachelor thesis · esl/spa · https://riunet.upv.es/handle/10251/174796

[ES] El proyecto consiste en el rediseño e implementación desde cero del sistema de gestión de contenido de una página de apuestas deportivas y juegos de casinos. La finalidad de este proyecto es hacer de una renovación completa de la página actual con un menor coste de mantenimiento, una mayor modularidad, y que permita una correcta implementación de prueba. Asimismo, el sistema debe facilitar la modificación de cualquier contenido que aparezca en la página en función del idioma y la geolocalización del usuario, así como dar la posibilidad a los administradores de previsualizar previamente cualquier cambio para no interferir en el tráfico habitual de la plataforma. Para poder lograr dichos objetivos se estudiará el sistema actual para poder realizar una correcta definición de una arquitectura hexagonal con la aplicación de principios de diseño software SOLID, además de hacer uso del framework PHP Symfony.

**Решение:** -6 ИТ-бакалаврская работа: редизайн веб-сайта букмекерской компании

---

### 181 · R4940

**Get ENGAGED: Results of NCPG 2018 National Survey of Gambling Attitudes & Experiences**

2019 · Digital Scholarship - UNLV (University of Nevada Reno) · conference-paper · en

The National Survey of Gambling Attitudes and Gambling Experiences (NGAGE) is the largest published survey of gambling participation and problems in the US. This unprecedented look into how Americans gamble, what they gamble, how they think about it in every state. Includes a special focus on sports gambling. Presenters will review the findings and implications for everyone involved in gambling issues.

**Решение:** + национальный опрос США NGAGE 2018 о распространенности гемблинга и проблемной игры со ставками на спорт

---

### 182 · R7558

**Las apuestas deportivas y el juego on-line: estado actual de la cuestión**

2009 · Revista Aranzadi de derecho de deporte y entretenimiento · article · es

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 правовой обзор правового статуса онлайн-ставок в Испании

---

### 183 · R2480

**Identificação e Categorização de Reclamações em Comentários sobre Empresas do Ramo de Apostas Esportivas**

2024 · Anais da XIX Escola Regional de Banco de Dados (ERBD 2024) · article, conference-paper, proceedings-article · pt · https://doi.org/10.5753/erbd.2024.238765

Uma parte significativa dos comentários em perfis de empresas de apostas esportivas referem-se a reclamações e problemas reportados pelos clientes. O presente trabalho testou métodos de aprendizado supervisionado para classificar comentários como reclamações em dados coletados do Instagram, sendo escolhido o modelo SVM. Técnicas de modelagem de tópicos foram aplicadas nos comentários classificados como reclamações, e foi selecionado o algoritmo GSDMM, tornando possível obter os principais problemas relatados pelos usuários. Os modelos selecionados foram implementados em um protótipo online que permite a inserção e análise de novos comentários.

**Решение:** -2 анализ комментариев в соцсетях методом опорных векторов без опроса людей

---

### 184 · R7343

**Football matches and acute cardiac events: potential effects of a complex psychosocial phenomenon on cardiovascular health**

2011 · International Journal of Epidemiology · article · en · https://doi.org/10.1093/ije/dyr060

Football is a highly popular sport in many countries worldwide. Debate about the association of acute cardiovascular events with watching thrilling football matches goes on. In the latest contribution, Barone-Adesi et al.1 reviewed the literature on the issue and concluded that spectators are at negligibly increased or no particular cardiovascular risk whatsoever. However, a body of evidence clearly suggests the opposite. With the jury still out, we are awaiting eventual reports on the phenomenon during the World Cup in South Africa. Although a recently published research with systematic review1 and accompanying commentary2 favours the hypothesis that the association between football matches and cardiovascular incidents, if any, is not important, a general overlook of published studies suggests that this should perhaps not be the final conclusion. Among four studies of hospital admissions for acute cardiovascular diseases,1,3–5 two reported no association with the timing of football matches.1,4 In contrast, admissions for myocardial infarction were increased in England for 2 days after the penalty elimination of the national team.3 In the only prospective and otherwise methodologically superior German study,5 a 2.7-fold increase in the incidence of cardiac emergencies was observed when the national team played; the risk was particularly pronounced in men and among patients with pre-existing coronary disease, and peaked ~2 h after the start of the match. More convincingly, among seven studies on cardiovascular mortality,6–12 four found an increased mortality, particularly for men,6,10–12 and one found such a trend in a match with a penalty shoot-out decision.8 A completely opposite association was observed during the 1998 World Cup when, in the finals, France defeated Brazil and the number of deaths from myocardial infarction on that day in France was decreased, particularly among men.9 The second French study, referring to the 1996 European championship, was the only research showing no association of football events with cardiovascular mortality whatsoever.7 Acute emotional stress, the leading culprit for cardiovascular events occurring during watching football, through sympathetic arousal, provokes biomechanical, prothrombotic and vasoconstrictive triggering mechanisms,13 and doubles the risk of myocardial infarction for ~2 h after the exposure.14 Lateralization of brain activity during emotional strain facilitates the development of ventricular arrhythmias, especially in those with pre-existing heart disease.15,16 In the aforementioned German study,5 an impressive 3.1-fold increase in incidence of cardiac arrhythmias causing major symptoms correlated with national team matches. A proarrhythmic effect of emotional upset may provide the first mechanism of increased cardiovascular mortality. Acute emotional stress induces enhanced inflammatory and vasoconstrictive processes,17,18 which have been associated with the general prediction of a coronary incident.19 Time course and dynamics of this inducible response have not been established as yet, but the result could be a several hours-to-days delayed increase in individual vulnerability. Similar delayed vulnerability, induced by alcohol consumed on weekend days, could be a possible contributing mechanism for a slight Monday increase in the cardiovascular risk.20 Watching football is a situation when superimposition of triggers like excessive smoking, coffee consumption, binge drinking, heavy meals, drug use or having less sleep may enhance emotional upset and multiply the risk.1,5,6,21–23 The triggers may concurrently facilitate the onset of a cardiac event, or may worsen the outcome when event occurs. The latter may be the second underlying mechanism for the increased cardiovascular mortality during football matches. Women could be more prone to emotional triggering of myocardial infarction14,23,24 and Takotsubo cardiomyopathy.25–28 Conversely, in the majority of studies, increased rates of cardiovascular incidents during football matches were observed exclusively or more apparently in men.3,5,6,10–12 The most plausible impression is that the link lies in men's greater interest and emotional involvement. Occasionally, we read or hear about tragic incidents when an excited husband gets carried away and violates his wife or throws a TV through the window because of a lost or ‘bad’ game, or because the wife was ironing in front of the TV, etc. A recent research on police reports of family violence on days when American professional football matches were played has shown that an unexpected loss in match where the home team was, with relative certainty, predicted to win, increases the home male-on-female violence by 8%. The violence occurs mainly after the match is over, and the effect on violence rates is more than twice as large for games against a traditional rival team in comparison with a non-rival team or when the team is still in a playoff contention.29 This could be the tip of the iceberg. Many more domestic arguments induced by watching a match probably do not escalate to the level of physical violence, but surely induce strong emotional upset. Betting is usually less emotionally intense than gambling, but the excitement may rise with a profound loss or win. Gambling has been implicated as a trigger of apical ballooning syndrome26 and ventricular arrhythmias.30 US casinos were recognized as an ambient of an increased cardiovascular risk and were supplied with automatic defibrillators, which proved useful and life saving.31 The sport betting industry has rapidly increased worldwide, at least partly spurred by the economic crisis. Even people who do not routinely follow sports look for some extra income, and we cannot exclude betting as a trigger of a small proportion of events, especially during the games with unexpected results or sudden turnovers. The majority of available studies is retrospective, observational and with diverse methodology regarding the hazard periods, the number of matches evaluated, diagnostic criteria and cardiovascular endpoints. Only the German study accounted for some chronobiological and meteorological confounders; barometric pressure, Tuesday and Sunday were positively associated, whereas Saturday was negatively associated with the matches.5 Short-term fluctuation in air pollutants may additionally confound the association,32 but match-associated emotional upset along with concomitant situational triggers probably highly outweighs environmental factors. Emotional stress-induced inflammatory and vasoconstrictive response may produce an increase in plaque, blood or myocardial vulnerability with a certain lag. Stress associated with family violence, commonly occurring after the matches,29 may be an additional cause for a delay in effect, as observed for 2 days4 and 12 h after the match.5 In contrast to the opinion expressed in a recent review,1 perhaps prospective investigation of other hazard periods may reveal detectable associations. Left ventricular ballooning syndrome, whose clinical presentation cannot be distinguishable from an acute coronary syndrome, is commonly precipitated by a stressful event and its diagnosis is based on the absence of obstructive atherosclerosis on coronary angiography.27,28 None of the studies on association of cardiac emergencies with football matches included data on coronary angiography, and left ventricular ballooning syndromes, misinterpreted as myocardial infarctions, might have contributed to the excess incidence in some studies. A number of factors may influence both the magnitude of audience and the intensity of individual emotional involvement or response. Whether a team is still in competition, duration of ‘resolving’ period, penalty shots, traditional rivalry, fans’ attachment to a particular team and importance of a match or football in the region are some of them. Violence-prone men seem to be more drawn to watch the match when the home team is expected to win, while the home violence rises by 1% for each per cent of increase in number of households watching the match.29 Bauman and colleagues proposed that, compared with Europeans, higher rates of motivational deficiency disorder could make Australians less susceptible to stress associated with watching football.4 Chronic emotional disorders, such as anxiety, depression, anger and affective disorders, or general psychological profile may indeed influence the psychophysiological response. For example, healthy hostile individuals may have heightened or prolonged cardiovascular and neuroendocrine responses to acute mental stress,33 whereas in patients with advanced coronary disease, hostility correlates with emotional stress-induced increases in sympathetic activation and inflammation.34 The association between watching football matches and hospital admissions for acute cardiovascular diseases is still questionable. Evidence on increased cardiovascular mortality appears more convincing, and may be linked to proarrhythmic effect of emotional stress and multiple triggering circumstances. At present, the most plausible conclusion is that watching football sometimes brings an additional risk of a cardiovascular event for some people. Recommendations for preventive measures could be warranted only in limited and defined populations such as hostile individuals with vulnerable coronary disease. A before-the-match and clear-minded consideration of possibility that their team may lose, taking enhanced regular anti-anginal or additional anxiolytic medication, and avoidance of concomitant triggers, alcohol and drugs in particular, could be a reasonable way of watching important matches for such patients. However, even when a match starts, cardiovascular risk and consequences cannot be predicted because of multiple interactions among the course of match, individual and circumstantial factors. Such complex psychosocial phenomena are primarily upsetting for male fans, but atypical and exaggerated behaviour may affect many others. So, is it ‘just a game’?

**Решение:** -6 исследование кардиоваскулярных событий при просмотре футбола, не гемблинг

---

### 185 · R3563

**The impact of weather on betting outcomes and market behaviour in the NCAA football totals market**

2022 · Applied Economics Letters · article · en · https://doi.org/10.1080/13504851.2022.2146651

ABSTRACT Sports betting markets are an attractive setting to evaluate the degree to which publicly available information is efficiently incorporated into asset prices. Weather information represents one category of potentially undervalued public data, and we assess its impact on wagering outcomes and market behaviour in American college football. We uncover statistically significant effects of weather characteristics on totals market outcomes, indicating that the market does not appropriately assimilate this data into its forecasts. We also demonstrate that weather characteristics are not statistically significant predictors of totals market line movement magnitude. Together, these results suggest the market systematically undervalues weather data. We then develop simple wagering strategies utilizing only three weather characteristics and illustrate the ability to profit.

**Решение:** -2 эконометрический анализ влияния погодных условий на котировки ставок

---

### 186 · R1304

**Mapping the Emotional and Psychological Dimensions of Fantasy Sports Betting: A Bibliometric Analysis**

2025 · Journal of Gambling Issues · article, journalarticle, journal-article · und · https://doi.org/10.4309/nvnl4582

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 библиометрический анализ научной литературы по фэнтези-спорту

---

### 187 · R4453

**Análisis descriptivo del juego patológico en la Unidad de Conductas Adictivas de Orihuela**

2020 · Libro Comunicaciones · article, other literature type, conference-paper · es · https://doi.org/10.17579/sepd2020p101

DESCRIPCIÓN DE LOS OBJETIVOS Describir el perfil de paciente que acude a tratamiento a la UCA de Orihuela con diagnóstico de juego patológico y las comorbilidades que presenta. MATERIAL Y MÉTODOS Los participantes (n=33) fueron 31 hombres y 2 mujeres, con edad media de 41,6. Todos acudieron a la UCA en busca de tratamiento entre enero y marzo de 2020 y cumplían criterios diagnósticos de Juego Patológico. Se les realizó una entrevista semiestructurada en la que se recogieron datos demográficos, motivo de consulta, TUS (excepto hábito tabáquico), antecedentes psicopatológicos, tipo de juego e historia de ideación o intentos autolíticos. RESULTADOS Y CONCLUSIONES Resultados: El 93,9% son hombres. El motivo de consulta fue el juego en el 51,5% y otras adicciones en el resto. El 60% usaba máquinas tragaperras (juego tradicional) y el resto a nuevas formas: online (18,2%), salones de juego (12,1%), apuestas deportivas (6,1%). El 42,4% tenía antecedentes psicopatológicos. Las patologías comórbidas fueron depresión (15,2%), ansiedad (12,1%), esquizofrenia (9,1%), trastorno bipolar (9,1%) y TDAH (3%). El 63,6% consumía sustancias; en concreto, alcohol (60,6%), cocaína (30,3%) y cannabis (9,1%). Se observó policonsumo en el 30,3% de la muestra, siendo el alcohol y la cocaína la combinación más frecuente (24,2%). El 6,1% tenía antecedentes de ideación autolítica y el 6,1% había realizado algún intento. Conclusiones: A pesar del aumento del juego entre los jóvenes, parece que el perfil de jugador que usa las nuevas formas de juego no está llegando a la UCA; esto pone de relieve la necesidad de una mejora en la detección y derivación de este tipo de población. Además, las comorbilidades son frecuentes en los pacientes con juego patológico que buscan tratamiento. Limitaciones del estudio: se necesita ampliar la muestra para poder llegar a más conclusiones pero el estudio tuvo que detenerse tras la irrupción del Covid-19.

**Решение:** -5 клиническая выборка пациентов наркологической клиники с патологическим гемблингом

---

### 188 · R2396

**Examining the sustainable leisure and business values in sporting events and lottery analyses development**

2024 · Journal of Infrastructure Policy and Development · article, journalarticle · en · https://doi.org/10.24294/jipd.v8i12.8787

Purpose: This study aims to clarify the meaning of sport analysis, explore the contributions derived from sporting event analysts, and highlights the importance of responsible sport gambling. It also investigates how sustainable practices can be integrated into sports analysis to enhance social well-being. Design/methodology/approach: Secondary text data from government documents, news articles, and website information were extracted by searching keywords such as sports lottery and sports analysis in traditional Chinese, and then analyzed to establish the research framework and scope. Subsequently, 18 interviews were conducted with stakeholders to gain deeper insights. Findings: The content analyses reveals that sport analysis tends to be sport data science. Sporting event analysts may contribute to improving the performance of players or a team, enhancing spectator sports, and increasing sports lottery revenues. In the leisure aspect, the professionalism of sporting event analysts not only increases epistemic and entertainment values in spectator sports but also boosts engagement with sport lotteries. To ensure these enhancements remain beneficial, it is vital to emphasize responsible sport gambling and sustainable practices that protect vulnerable groups and promote long-term health benefits for those involved in sports. The integration of sustainable practices in sport analysis and the expertise of sporting event analysts can significantly advance economic and social development by generating funds through sport lottery industry for athlete programs, sports infrastructure, and educational initiatives, aligning with multiple Sustainable Development Goals. Additionally, the professionalism of these analysts may enhance public understanding and engagement of sports, promoting increased participation in sports, reducing healthcare costs, and contributing to the development of a healthier and more resilient society. Originality: Emphasizing responsible sports gambling is essential to the sustainability of sports lotteries and the role of sporting event analysts.

**Решение:** -1 анализ вторичных источников и документов о спортивной аналитике

---

### 189 · R1786

**Which indicators matter? Using performance indicators to predict in-game success-related events in association football**

2025 · Int. J. Comput. Sci. Sport · journalarticle, article · en · https://doi.org/10.2478/ijcss-2025-0011

Abstract This study evaluates the predictive power of common performance indicators (PIs) in soccer for success- or scoring-related events (SREs) such as shots, corner kicks, and box entries. Using data from 102 Bundesliga matches, we applied five machine learning methods to assess how well 28 widely used PIs (e.g., passes, ball possession time, opponents outplayed) within a past time span (up to 15 minutes) predict an SRE in a future window (up to 15 minutes). We ranked PIs based on the mean Matthews Correlation Coefficient. Results show PI Dangerousity best predicts SRE Goal and SRE ShotTaken , while PI EntriesAttaThird is strongest for SRE Cornerkick , SRE EntryAttaThird , and SRE EntryOppBox . PI Dangerousity and PI SuccPassAttThird consistently rank in the Top 9, highlighting their predictive strength. Combining PI OutplayedOpp and PI TacklingsWon over a five-minute input window improves goal prediction within three minutes, outperforming random guessing by 6%. PIs based on rare events, such as goals and corner kicks, are less effective for SRE prediction, whereas those capturing frequent actions (e.g., final-third possession, Dangerousity, outplayed opponents) perform better. These findings highlight the value of in-game data for short-term event prediction and its potential applications in quantifying match momentum, optimizing live betting odds, and improving performance analysis.

**Решение:** -2 машинное обучение для прогнозирования событий в футбольных матчах

---

### 190 · R1640

**Access to Gambling Services among Vulnerable Population: Implications of Online Sports Betting for Sustainable Development in Nigeria**

2025 · Modern Geográfia · article, journalarticle, review · en · https://doi.org/10.15170/mg.2025.20.03.01

Information and communication technology has increased access to gambling services and made it highly prevalent among youths. The youthful population in Nigeria is constantly confronted with several negative psychological implications of betting. Using a survey method for primary data collection, this study examined access, determinants, and patronage of online sports betting among 300 respondents. The results show that most respondents were young adults within the 18–28 age category. The majority were male and had attained tertiary-level education. About 79% of the respondents were students with an income level below N30,000.00. Additionally, 51.7% of the respondents had engaged in some form of online betting to earn money or gain other benefits, while 48.3% had not. This study indicates that online betting is quite popular, and physical access to betting locations is relatively easy for most respondents.

**Решение:** ? опрос 300 молодых людей в Нигерии о ставках на спорт, проверить наличие инструмента PG в полном тексте

---

### 191 · R1266

**Betting on Performance: Sports Betting Legalization and NBA Player Performance Relative to Sportsbook Expectations**

2026 · Scholarship @ Claremont (The Claremont Colleges) · dissertation

This paper presents some of the first empirical work examining how the legality of sports betting markets affects the relationship between player performance and sportsbook expectations and adds to a small but growing body of research on how legal sports betting changes player behavior. To achieve this, this paper evaluates the effect legalization of mobile sports betting has on NBA player performance relative to prominent sportsbook proposition line (or “prop line”) expectations. To determine that effect and assess whether these betting expectations impact player behaviors, a player-game level dataset is used that links FanDuel closing over/under lines to real game data for 178 NBA players across five different statistical categories. The dataset spans three distinct player positions (center, guard and forward) and covers games from the 2022 to the 2025 seasons. Using a difference-in-differences model, and exploiting staggered state-level legalization timing, the results show that players in legal markets deviate more from their prop line expectations, though not in any consistent direction. The primary outcome was the absolute value of the deviation between game performance and the FanDuel closing line (AbsDev). StatDiff measured the directional difference between real game performance and the closing line. Betting legality was associated with a statistically significant increase in AbsDev across three main specifications (beta range 0.266-0.396, all p < 0.05). Player performance in legalized markets deviated further from applicable prop lines in both directions without a consistent directional bias. This effect was most pronounced in the points market (beta = 0.665, p = 0.020), specifically with centers and forwards. For example, Dennis Schroder, who was traded to five different teams from 2022-2025 in markets that both offered and did not offer legalized betting, provides additional evidence and support for the conclusions in this paper.

**Решение:** -2 эконометрический анализ показателей игроков НБА и букмекерских спредов

---

### 192 · R4279

**Match-fixing under the state monopoly sports betting system: a case study of the 2011 K-League scandal**

2020 · Crime Law and Social Change · article, journal-article · en · https://doi.org/10.1007/s10611-020-09888-0

This paper examines the characteristics of match-fixing under the state monopoly sports betting system, particularly focusing on the case of the 2011 K-League scandal. Drawing from policy documentation and interview data, this study explores the precipitating factors that underpin large-scale match-fixing in South Korea. The results of the analysis reveal that first, the financial stability of the legal, monopoly betting operator attracts match-fixers for manipulation due to its guaranteed payouts. Second, the legal betting system that only offers traditional products (e.g., final match results) required fixers to mobilize a larger number of players, increasing the size of the scandal. Third, within the small community of footballers, the networks based on school ties, and the training camp culture made it easier for fixers with soccer-playing backgrounds to mobilize many active players. Finally, the follow-up measures after the scandal only targeted illegal betting operators or individual player immorality, which allowed the government to continue to play a dual role as both the operator of the sports gambling business and the protector of sport integrity.

**Решение:** -2 анализ матчей и выявление договорных игр в футболе

---

### 193 · R2209

**BGH: Sportwetten im Internet III**

2024 · Computer und Recht · article · de · https://doi.org/10.9785/cr-2024-401218

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 судебное решение высшей судебной инстанции Германии по онлайн-ставкам

---

### 194 · R1695

**Bullshit Sweepstakes**

2025 · SSRN Electronic Journal · preprint · en · https://doi.org/10.2139/ssrn.5466928

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 правовое эссе о регулировании рекламных конкурсов и свипстейков

---

### 195 · R1894

**Countermeasures Against Online Soccer Gambling Crimes By Surabaya Police**

2025 · Asian Journal of Social and Humanities · journalarticle, article · en · https://doi.org/10.59888/ajosh.v3i4.481

Gambling poses a significant threat to societal norms and can impede national progress on both material and spiritual fronts. Consequently, a rational approach is imperative in addressing this issue, which includes robust law enforcement policies and the prosecution of offenders. This research delves into the Surabaya City Police's efforts to combat online soccer gambling and seeks to analyze the modus operandi of suspects involved in such activities, as well as the challenges and obstacles encountered by the Cyber Unit III of the Surabaya City Police Criminal Investigation Unit. Employing a qualitative descriptive exploratory methodology, this study utilizes primary and secondary data gathered through observation, interviews, and document analysis. The findings of this research are anticipated to serve as a valuable resource for understanding the complexities of combating online gambling and to inform strategies for enhancing police effectiveness in responding to public reports of this illicit activity.

**Решение:** -1 криминологический анализ правоприменительной практики полиции против нелегальных ставок

---

### 196 · R7255

**Strategic vs nonstrategic gambling: characteristics of pathological gamblers based on gambling preference.**

2011 · Annals of clinical psychiatry : official journal of the American Academy of Clinical Psychiatrists · article, journal article, research support, n.i.h., extramural · eng · https://doi.org/10.1177/104012371102300204

BACKGROUND: Although prior studies have examined various clinical characteristics of pathological gambling (PG), limited data exist regarding the clinical correlates of PG based on preferred forms of gambling. METHODS: We grouped patients meeting DSM-IV criteria for pathological gambling into 3 categories of preferred forms of gambling: strategic (eg, cards, dice, sports betting, stock market), nonstrategic (eg, slots, video poker, pull tabs), or both. We then compared the groups' clinical characteristics, gambling severity (using the Yale-Brown Obsessive Compulsive Scale Modified for Pathological Gambling, the Clinical Global Impression-Severity scale, and time and money spent gambling) and psychiatric comorbidity. RESULTS: The 440 patients included in this sample (54.1% females; mean age 47.69±11.36 years) comprised the following groups: strategic (n = 56; 12.7%), nonstrategic (n = 200; 45.5%), or both (n = 184; 41.8%). Nonstrategic gamblers were significantly more likely to be older and female. Money spent gambling, frequency of gambling, gambling severity, and comorbid disorders did not differ significantly among groups. CONCLUSIONS: These preliminary results suggest that preferred form of gambling may be associated with certain age groups and sexes but is not associated with any specific clinical differences.

**Решение:** -5 клиническая выборка пациентов, соответствующих критериям патологического гемблинга DSM-IV

---

### 197 · R5848

**Fixed matches in Portugal – myths, perceptions and attitudes: a study focusing on referees and fans**

2016 · Mundos Sociais, Iscte-Instituto Universitário de Lisboa · article · spa · https://revistas.rcaap.pt/sociologiapp/article/view/7159

El artículo presenta datos sobre opiniones y percepción de los árbitros del fútbol portugués y los hinchas sobre la manipulación de resultados, uno de los principales problemas del fútbol mundial. Los analistas suelen vincular el problema con el crimen organizado y las apuestas deportivas. En Portugal, sin embargo, los escándalos del pasado indican que la manipulación se conectaría más con el interés deportivo, el tráfico de influencias y el soborno de los directivos y actores institucionales. En la opinión pública, los árbitros aparecen como el grupo más sospechoso y denunciado. A través de una encuesta a los miembros de la Asociación Portuguesa de Árbitros de Fútbol (APAF) y a simpatizantes agrupados en diferentes asociaciones, el artículo confirma empíricamente hipótesis de la narrativa oficial sobre el arreglo de partidos, como la existencia de oferta de prostitutas a los árbitros. Sin embargo, muestra una perspectiva más amplia del fenómeno que va más allá de la esfera de las apuestas y el crimen organizado. Entrevistas en profundidad a informantes clave se llevaron a cabo para confirmar y ampliar los resultados. L’article présente des données sur les opinions et les perceptions des arbitres de football portugais et des supporteurs sur la manipulation des résultats, un des principaux problèmes du football à travers le monde. Les analystes lient souvent le problème avec le crime organisé et les paris sportifs. Cependant, au Portugal, les scandales récents indiquent que la manipulation serait principalement liée aux intérêts sportifs, au trafic d’influence et à la corruption des gestionnaires et des fonctionnaires. Au sein de l’opinion publique, les arbitres sont perçus comme étant le groupe le plus suspect et dénoncé. Grâce à des enquêtes à des membres de l’Associação Portuguesa de Árbitros de Futebol (APAF) et des partisans, l’article confirme empiriquement une hypothèse du récit officiel des matches truqués, comme l’existence d’offres de prostituées aux arbitres. Toutefois, il montre une perspective plus large du phénomène qui va au-delà de la sphère des paris et du crime organisé. Des entretiens approfondis avec des informateurs clés ont été effectués pour confirmer et amplifier les résultats. O artigo apresenta dados sobre opiniões e perceções dos árbitros do futebol português e dos adeptos sobre a manipulação de resultados, um dos principais problemas do futebol mundial. Os analistas vinculam o problema com o crime organizado e as apostas desportivas. No entanto, em Portugal, os escândalos de anos anteriores indicam que a manipulação estaria conectada com o interesse desportivo, o tráfico de influências e o suborno de diretores e atores institucionais. Para a opinião pública, os árbitros são o coletivo mais suspeito e denunciado. Através dum inquérito a membros da Associação Portuguesa de Árbitros de Futebol (APAF) e adeptos membros de diferentes associações, o artigo confirma empiricamente hipóteses da narrativa oficial sobre a combinação de resultados, como a existência de oferta de prostitutas. Não entanto, o trabalho apresenta uma perspetiva mais abrangente, que vai além do mundo do crime organizado e das apostas. Entrevistas em profundidade a informantes chave foram realizadas para confirmar e ampliar os resultados. The paper presents data about opinions and perception of Portuguese football referees and supporters about manipulation of results, ones of the main problems of football worldwide. Analysts often link the problem with organized crime and sporting betting. In Portugal, however, recent scandals indicate that manipulation would be mostly connected with sporting interest, influence peddling and bribing from managers and officials. In the public opinion, referees appear as the most suspicious and denounced group. Through surveys of members of the Portuguese Football Referees Association (APAF) and supporters, the paper empirically confirms some assumptions of the official match-fixing narrative, like the existence of offers of prostitutes to referees. Nevertheless, it shows a wider perspective of the phenomenon that goes beyond the betting sphere and organized crime. In depth interviews to key informants were carried out to confirm and extend the results.

**Решение:** -2 исследование восприятия договорных матчей судьями и игроками

---

### 198 · R8110

**Lottery playing amongst youth: implications for prevention and social policy.**

2004 · Journal of gambling studies · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1023/b:jogs.0000022306.72513.7c

Factors associated with lottery ticket purchases, accessibility of lottery products, and lottery playing behaviour amongst 1,072 youth (ages 10-18 years old, mean age 14 years-old) was examined. Playing the lottery was found to be the most popular gambling activity with youth reporting playing all forms of lottery tickets including draws, scratch tickets, and sports lottery tickets. Youth reported beginning to play the lottery at age 12, with scratch ticket participation being amongst the most highly reported type of lottery activity with the youngest age of onset. The vast majority of youth are aware of the legal age to purchase tickets although many believed that there should be no age requirement to purchase any form of lottery ticket. Youth, regardless of their age, reported few if any difficulties in purchasing lottery tickets. Moreover, a third of underage youth reported going to the store specifically to purchase lottery tickets with this behaviour increasing with the age of the participant. This research confirms previous findings that lottery tickets are highly accessible to underage youth despite legal prohibitions. The results provide valuable information that can be subsequently used in the development of responsible social policy and youth gambling prevention programs

**Решение:** ? опрос молодежи о лотереях и спортивных лотереях, проверить наличие опросника PG в полном тексте

---

### 199 · R0613

**Electronic gambling engagement and psychosocial outcomes among students at the University of Ibadan, Nigeria: a theory of planned behavior perspective.**

2026 · BMC public health · journal article, journalarticle, review · eng · https://doi.org/10.1186/s12889-026-27689-3

BACKGROUND AND AIMS: The proliferation of electronic gambling in Nigeria presents a significant public health concern among youths facing economic adversity. This study applied the Theory of Planned Behavior (TPB) to investigate the socio-cognitive drivers and self-reported psychosocial consequences of electronic gambling engagement among students at the University of Ibadan. Electronic gambling is defined here as any gambling activity conducted through electronic devices, including mobile phones, laptops, and computers, encompassing mobile sports betting applications, web-based casino platforms, and online poker. METHODS: A descriptive cross-sectional survey design was employed. Data were collected from 403 undergraduate and postgraduate students at the University of Ibadan using stratified random sampling and a structured self-administered questionnaire adapted from validated instruments. Analyses included descriptive statistics, scale reliability assessment, and binary logistic regression. RESULTS: The lifetime prevalence of electronic gambling was 49.6%. Positive attitudes toward gambling, subjective norms involving peer approval, and perceived behavioral control were all significant predictors of gambling engagement (p < .001). Economic hardship was the strongest predictor in the model (OR = 3.06). Among participants who reported gambling, 50.9% reported increased stress and anxiety, 48.6% reported financial strain, and 42.6% reported negative academic consequences. PRACTICAL IMPLICATIONS: University health and counseling services should integrate validated gambling screening tools into routine student health assessments. Interventions should address both the economic motivations and the cognitive distortions sustaining gambling engagement. Prevention campaigns should target the specific TPB constructs validated in this study. Institutional policy must also address the structural driver of economic hardship through expanded work-study programs and student financial support initiatives.

**Решение:** ? опрос 403 студентов в Нигерии об онлайн-ставках, проверить наличие инструмента PG в полном тексте

---

### 200 · R7559

**Las apuestas mutuas: un ejemplo de cómo las apuestas deportivas pueden, venciendo el fraude, contribuir de manera definitiva a la financiación de las estructuras deportivas y a la industria del deporte-espectáculo sobre las que se sustentan**

2009 · Revista Aranzadi de derecho de deporte y entretenimiento · article · es

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 юридическая статья о тотализаторе и финансировании спорта

---

### 201 · R8074

**Mode of spending of sports lottery welfare fund in China**

2005 · journal of physical education · article · en

By carrying out statistical analysis on sports lottery issuance revenue in China all these years, the authors considered that target deviation exists in the spending of sports lottery welfare funds in China: firstly, the fund has been spent more on rich units than on poor units; secondly, the result of spending is not noticeable. Based on such an analysis coupled with the modes of spending of sports lottery welfare fund in foreign countries, the authors re-orientated the mode of spending of sports lottery welfare fund in China: Meeting the need for interest of other welfare undertakings by handing over the fund to the Ministry of Finance can not only be acceptance to the public but also meet the need for developing sports undertakings.

**Решение:** -1 анализ распределения средств лотерейного фонда в Китае

---

### 202 · R8137

**Sports Betting with Bookies Based on Picks Provided by Persons/Operations Who Charge a Fee and/or a Percentage of the Amount of Winnings**

2004 · Gaming Law Review · article, journalarticle, journal-article · en · https://doi.org/10.1089/glr.2004.8.371

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 правовой анализ операций с нелегальными букмекерами

---

### 203 · R5685

**The Fantasy Sport Industry: Games Within the Games**

2016 · International Journal of Sport Communication · article · en · https://doi.org/10.1123/ijsc.2016-0056

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 рецензия / обзор индустрии фэнтези-спорта

---

### 204 · R0765

**Gender Bias in Athletic Performance Evaluations: How Sport Stereotypicality and Causal Mechanisms Shape Betting Behavior**

2026 · Open Science Framework · studyregistration/pre-registration, other · https://doi.org/10.17605/osf.io/ejkvp

This study examines whether gender bias influences betting judgments of athletes. Using an online vignette-based survey, participants read descriptions of athletes varying by gender, sport type (male-typed vs. female-typed vs neutral), biological mechanisms vs. effort, and skill level, then rate the appeal and risk of betting on each athlete. The purpose is to investigate whether female athletes, particularly those competing in male-typed sports or possessing a biological advantage, are judged more harshly than male athletes with equivalent skill. It is expected that female athletes in male-typed sports will receive higher risk and lower appeal ratings, that biological advantage will intensify these penalties, and that skill level will have the largest overall effect on judgments. The study also explores whether individual differences in gender essentialism and ambivalent sexism predict the degree of bias shown, alongside demographic variables such as participant gender, sports familiarity, ethnicity, and education level. Findings are expected to demonstrate that gender stereotypes extend into sports betting judgments, with female athletes being systematically undervalued relative to equally skilled male athletes. This has broader implications for understanding how gender bias operates in commercial and public perceptions of sport.

**Решение:** -3 эксперимент по гендерным стереотипам при оценке ставок без инструмента PG

---

### 205 · R5752

**Betting on the Blockchain: Applying Design Science to Develop a Smart Contract Solution for a New Business Model of the Betting Industry**

2016 · Copenhagen Business School · master thesis · eng · https://research.cbs.dk/en/studentProjects/c9df1ab9-54c0-4001-9015-1ed7138949b0

The potential to decentralize industries by combining the blockchain with smart contracts is currently gaining recognition worldwide. The collaboration of these emerging technologies enables a unique opportunity to create new business ventures. Continuously, businesses across the spectrum are exploring new ways to adopt these technologies. In order to exploit the potential of this combination, our thesis aims to use smart contracts and blockchain technology to develop a new artifact in the form of a prototype. In this research, we will focus on a global industry, namely the online betting industry, to identify how smart contracts and blockchain technology can further evolve the online betting industry’s current business model. Thus, we will merge existing literature and knowledge on the online betting industry, blockchain technology, and smart contracts to develop a peer-to-peer based solution. We will utilize a design science approach to design, build, and evaluate the proposed blockchain solution to demonstrate its feasibility and utility. By using this approach, our thesis evolves current research. The research seeks to identify the gap between smart contracts, blockchain technology and the online betting industry. The end result being an alternative business model, which demonstrate how smart contracts and the blockchain can be used to: 1. Establish a peer-to-peer betting solution, which facilitates the betting process between users, 2. Create and evaluate a solution, which illustrates the potential of an alternative business model, and 3. Provide recommendations based on qualitative feedback from the evaluation of constructed scenarios, which enables further development of the utilization of smart contracts and blockchain technology. Overall, this study seeks to contribute knowledge to the smart contracts and blockchain field, which despite the recent increases in interest, remains a relatively unexplored area.

**Решение:** -6 ИТ-магистерская диссертация по смарт-контрактам и блокчейну

---

### 206 · R6712

**Historia Sportu**

2013 · https://doi.org/10.1080/09523367.2013.765728

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 исторический очерк развития спорта, не гемблинг

---

### 207 · R4007

**The History and Evolution of the Fantasy Sport Voice: An Oral Account of the Major Aspects Forming the Fantasy Sports and Gaming Association**

2021 · The International Journal of the History of Sport · article, journal-article · en · https://doi.org/10.1080/09523367.2021.1876675

Abstract The growth of the fantasy sport industry has been nothing short of extraordinary. With estimates of 500,000 in the mid-1990s, to a current North American consumer estimate of 59.3 million, the industry has evolved quickly and with quite a force. Historical roots date fantasy activity back to the 1950s and 1960s. Since then, this industry has seen many phases of growth, expansion, trials, and tribulations. For many years, the Fantasy Sports Trade Association (FSTA) has served as ‘the voice’ for the industry in many matters, as its members and professional associations strived for legitimacy, legality, and longevity in creating professional careers. The FSTA has invited major (and minor) players to join as one association and attend semi-annual conferences to collaborate, learn, share, and grow the industry as a whole. Fighting off player strikes, gambling law, and incredible growth of daily fantasy sport operation, this organization has guided industry professionals throughout. This article provides an historical account of the formation of the organization responsible for holding this flourishing industry together and growing as one. Data were gathered from oral accounts of key events in the life of this organization.

**Решение:** -1 устная история торговой ассоциации фэнтези-спорта

---

### 208 · R1873

**The metaverse and sport fandom: revolutionising sport consumption**

2025 · Sport in Society · journalarticle, editorial · en · https://doi.org/10.1080/17430437.2025.2573289

Abstract This article explores the potential transformative impact of the metaverse on sport consumption. While traditional sport environments cultivate a sense of communitas and liminality, where attendees experience unity and solidarity, the digital shift is redefining these dynamics. The metaverse offers new ways for sport consumers to engage, experience, and enter into an exchange. We present a model that conceptualises the multifaceted elements reshaping how sport is consumed, while also providing a framework to critically assess the implications of this transformation. We address both the opportunities and challenges presented with the expansion of virtual sport consumption and highlight legal and ethical concerns such as data privacy and security, online harassment and the escalating normalisation of sport betting.

**Решение:** -1 концептуальная статья о метаверсе и потреблении спорта

---

### 209 · R2845

**The Sociological Implications of Football Betting and the Birth of Deviant Behaviour among Youths in the South–South Geo-Political Zone of Nigeria**

2023 · Research on humanities and social sciences · article, journalarticle, other literature type · en · https://doi.org/10.7176/rhss/13-12-09

Las apuestas de fútbol se han convertido erróneamente en una fuente de sustento para millones de jóvenes nigerianos, independientemente del hecho de que se considere una actividad ignominiosa que debe ser rechazada por todos. Además, este estudio examinó las implicaciones sociológicas de las apuestas de fútbol y el nacimiento del comportamiento desviado entre los jóvenes en la zona geopolítica sur-sur de Nigeria. Se formularon tres preguntas de investigación para guiar y lograr los objetivos del estudio. Se adoptó el diseño de la investigación de la encuesta y se seleccionó una muestra total de 1200 encuestados a través de una técnica de muestreo intencional. La teoría del intercambio social de George Homans proporcionó la base teórica para el estudio. Entre los hallazgos, el estudio mostró que las apuestas de fútbol se han convertido en una empresa comercial encantadora y que cientos de miles de jóvenes nigerianos en la actualidad lo ven como una alternativa viable para satisfacer sus necesidades. El estudio también reveló que las apuestas de fútbol se han vuelto adictivas y, por lo tanto, están aumentando la tasa de desviación en la sociedad. Basado en esto, el estudio concluyó que como un fenómeno adictivo, cada mano debe estar en la cubierta para frenar el caso de un creciente comportamiento desviado entre los jóvenes nigerianos. Además, el estudio recomendó, entre otros, que cualquier acuerdo dirigido a reducir las consecuencias perjudiciales de las apuestas de fútbol debe estar bien pensado y debe estar en línea con los objetivos de salud pública. Además, el gobierno debe intensificar los esfuerzos para organizar seminarios para reducir el patrocinio de las apuestas por parte de los jóvenes nigerianos, los supuestos líderes del mañana. Finalmente, los padres deben proporcionar una reorientación digna para alentar a sus pupilos a renunciar a las apuestas, así como contratar psicólogos y consejeros para ayudar. Les paris sur le football sont devenus à tort une source de revenus pour des millions de jeunes nigérians, indépendamment du fait qu'ils sont considérés comme une activité ignominieuse qui devrait être évitée par tout le monde. Suite à cela, cette étude a examiné les implications sociologiques des paris sur le football et la naissance de comportements déviants chez les jeunes de la zone géopolitique sud-sud du Nigeria. Trois questions de recherche ont été formulées pour guider et atteindre les objectifs de l'étude. Le plan de recherche de l'enquête a été adopté et un échantillon total de 1 200 répondants a été sélectionné par le biais d'une technique d'échantillonnage ciblée. La théorie de l'échange social de George Homans a fourni le fondement théorique de l'étude. Parmi les résultats, l'étude a montré que les paris sur le football sont devenus une entreprise commerciale florissante et enchanteresse et que des centaines de milliers de jeunes Nigérians y voient actuellement une alternative viable pour subvenir à leurs besoins. L'étude a également révélé que les paris sur le football sont devenus addictifs et augmentent donc le taux de déviance dans la société. Sur cette base, l'étude a conclu que, en tant que phénomène addictif, chaque main doit être sur le pont pour freiner le cas d'un comportement déviant croissant chez les jeunes nigérians. Suite à cela, l'étude a recommandé, entre autres, que tout arrangement visant à réduire les conséquences néfastes des paris sur le football soit bien pensé et, doit être conforme aux objectifs de santé publique. En outre, le gouvernement devrait intensifier ses efforts pour organiser des séminaires pour réduire le parrainage des paris par les jeunes nigérians, les dirigeants supposés de demain. Enfin, les parents doivent fournir une réorientation digne pour encourager leurs pupilles à abandonner les paris ainsi que d'embaucher des psychologues et des conseillers pour aider. Football betting has erroneously become a source of livelihood for millions of Nigerian youths, regardless of the fact that it is viewed as an ignominious activity that should be shunned by all and sundry.Sequel to this, this study examined the sociological implications of football betting and the birth of deviant behaviour among youths in the south-south geo-political zone of Nigeria.Three research questions were formulated to guide and attain the objectives of the study.Survey research design was adopted and a total sample of 1200 respondent was selected through purposive sampling technique.The Social exchange theory of George Homans provided the theoretical underpinning for the study.Among the findings, the study showed that football betting has become a money-spinning, enchanting business enterprise and hundreds of thousands of young Nigerians at present view it as a viable alternative to provide for their necessities.The study also revealed that football betting has become addictive and is therefore increasing the rate of deviance in the society.Based on this, the study concluded th

**Решение:** ? опрос 1200 нигерийских молодых людей о ставках на футбол, проверить наличие инструмента PG в полном тексте

---

### 210 · R5880

**Daily Fantasy Sports & Internet Poker Winning Battles, But Losing War**

2016 · Gaming Law Review and Economics · article, journalarticle, journal-article · en · https://doi.org/10.1089/glre.2016.2042

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 юридический анализ статуса дейли фэнтези и онлайн-покера

---

### 211 · R6869

**The Role of Surprise: Understanding Over- and Underreactions in Prediction Markets**

2012

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -2 модели рынков прогнозов без опроса людей

---

### 212 · R5826

**Understanding the convergence of markets in online sports betting**

2016 · International Review for the Sociology of Sport · article, journalarticle, journal-article · en · https://doi.org/10.1177/1012690216680602

Betting on sports via online platforms has rapidly become a popular form of gambling in many countries. Despite the growing body of research investigating the psychosocial and individual psychological factors determining gambling behaviour, much less attention has been devoted to understanding the market characteristics of online sports betting and its intersection with products from adjacent industries. From an economic convergence perspective, the present paper explores the integration of online sports betting within the digital, sporting and gambling sectors, examining how data markets, eSports, virtual sports, social gaming, immersive reality tools, sports media, sport sponsorship, fantasy sports, in-venue and in-stadium betting, poker and trading are all converging around betting activity. Through this convergence process, it is argued that internet-based sports gambling is colonizing different forms of entertainment, and expanding marketing opportunities, as well as raising psychosocial concerns about the influence of such an integration process.

**Решение:** -1 социологический анализ конвергенции рынков ставок и смежных продуктов

---

### 213 · R2628

**Online gambling: Mental health implications and how to curb the emerging menace**

2024 · Indian Journal of Psychiatry · article · en · https://doi.org/10.4103/indianjpsychiatry.indianjpsychiatry_915_24

BACKGROUND Gambling is the act of playing a game or taking a risky action for money or a desired outcome. India has a history of gambling embedded in its tradition – from the epic Mahabharata to the long-standing tradition of gambling during Diwali. Common forms of gambling in Indian culture include teen patti, satta, matka, and cock-fights. However, with massive, rather complete penetration of smartphones in almost every household, online gambling has become a new rage. Various modes of online gambling include gaming (casino, poker, bingo), betting (sports, fantasy, betting), and lotteries. A simple online search reveals close to 30 online betting apps in India. India’s online gambling market is estimated to have 12.17 million users and is expected to grow by 8.5% a year. Illegal gambling has approximately 60 billion dollar market in India.[1] PSYCHIATRIC ISSUES – NOSOLOGY, ETIOLOGY, AND COMORBIDITY Gambling disorder has found nosological validity in both DSM-5 and ICD-11 and has been categorized as a “behavioral addiction” rather than “impulse control disorder” in previous versions. ICD-11 also includes a qualifier for “predominantly online” following diagnosis of gambling disorder. Those who are emotionally vulnerable, dissocial, or impulsive are more prone to develop pathological gambling. The former resort to gambling to relieve negative emotional states (negative reinforcement), while the latter enjoy the “high” (positive reinforcement) associated with gambling.[2] There is additional contribution of cognitive distortions like “gambler’s fallacy” (a series of independent events are connected and the probability of an event changes based on what happened before), near-miss effect (where a loss is perceived as close to win), and illusion of control (one may be able to control events over which one does not have control). Existing research data have implicated ventral and medial prefrontal cortex, anterior cingulate cortex, striatum, amygdala, hippocampus, and insula.[2] Dysfunctions in these regions could be related to sensitivity to reward and excitement and emotional problems. Studies have shown that more than 90% of those with pathological gambling have a psychiatric disorder and more than 60% have three or more comorbid psychiatric disorders. Substance use disorders, impulse control disorders, and mood and anxiety disorders are the most common comorbidities.[2] DOES ONLINE GAMBLING POSE A GREATER RISK THAN OFFLINE GAMBLING? There is already preliminary evidence pointing to the elevated risk of problem gambling among online gamblers. Some of the reasons include increased availability and accessibility, anonymity, and potential for lower expenditure. Online gambling is more popular among young users who are more impulsive in nature. The mobile apps keep improving their interface to make it more attractive to youngsters. One novel feature is in-play betting where one can place bets during the game based on small events like who will get the next wicket or corner kick. There is a shorter delay between wager, outcome, and reward, and this poses the greatest risk.[3,4] MENTAL HEALTH CONSEQUENCES OF ONLINE GAMBLING Those having pathological gambling usually seek help due to financial, legal, or social consequences. Multiple stressors often lead to worsening of mood symptoms and suicidal crisis. Heavy financial debt has been independently linked to suicide despite adjusting for mood symptoms. Online rummy-related suicides in Tamil Nadu (TN) led the government to form an expert committee, which led to the formation of a new act in 2023.[5] LEGAL ASPECTS OF ONLINE GAMBLING The laws on gambling are enacted by each state individually. The Public Gambling Act, 1867 has been adopted by many states with modifications. Most of the state gaming laws have been framed in the pre-Internet era and prohibit gambling in “physical premises” only. States of Sikkim, Nagaland, Andhra Pradesh (AP), Telangana, and TN have laws for online gambling. Mostly state laws have exemptions for games of skill and limit legal restrictions to games of chances. Games of chance are typically those where placing bets do not require any skill, practice does not increase chances of winning, and all events are unique and independent. Examples include bingo, roulette, lottery, and slot machines. Games of skill are those games in which the element of skill is more than the element of chance and the chances of winning improve with practice. Examples include games based on team selection/strategy, soccer, chess, and board games. Games of cards like rummy are considered as games of skills in some states but are banned in TN. States of AP and Telangana prohibit all activities in relation to online gambling including skill games. TN prohibits online rummy and poker also in addition to obvious games of chance like lottery. In April 2023, the Union Ministry of Electronics and Information Technology (MeitY) proposed that independent self-regulatory bodies will verify whether an online real money game is to be made available to the general public or not. Although advertisements across all print media are prohibited as per most state laws, many apps resort to online advertisements including ambush marketing. Most of the state gaming laws do not impose social responsibility like age-gating, self-exclusion, and provisions to regulate the content, duration, and targeted audience of advertisements. TN act prohibits banks and payment gateways from processing any transfer of funds for online gaming. TREATMENT STRATEGIES Psychosocial interventions like gamblers’ anonymous, cognitive behavior therapy and motivational interviewing are helpful in pathological gambling. Pharmacological agents that are useful include naltrexone (with comorbid alcoholism), N-acetyl cysteine (with comorbid smoking), and SSRIs and mood stabilizers (in comorbid mood disorders).[2] THE WAY FORWARD Apart from the adverse consequences on mental health, illegal betting apps pose a serious threat to the country’s economy. Predatory betting platforms lure customers with enticements like “no GST” and “no TDS” and evade existing tax and IT laws. To pay-off losses from such betting apps, many youth resort to informal borrowing channels and get caught in a vicious debt trap. There are also issues of data breach and money laundering. They also cause massive loss in tax revenue to the government. Recently, MeitY blocked 174 betting apps under the IT Act. The Central Consumer Protection Authority issued a recent advisory warning strict action against endorsement of online betting and gambling by celebrities and influencers. The ministry should take appropriate steps to ensure registration of online betting apps. Regulation of payment gateways in relation to online gambling is another important step. There are two major issues which need to be worked out by the stakeholders. First, the gray area between games of skill and games of chance needs to be clearly sorted out. Many a time, certain states have banned certain apps, but they challenged the ban in court and won the argument on the premise that a game of skill was being “wrongly victimized”. Second, a central law which uniformly guides all state laws in this regard would be helpful to reduce ambiguity between so many variations in gambling laws across states. This would also help in framing the necessary guidelines to be followed by all betting apps in order to be eligible to operate in India. Online gambling has several far-reaching consequences not only for the mental health of the youth but also for the financial growth and prosperity of the country and needs to be reined in for the benefit of both.

**Решение:** -1 обзор ментального здоровья и регулирования онлайн-гемблинга в Индии

---

### 214 · R5899

**Siena Research Institute Poll: May 2016 Siena New York Poll**

2016 · Roper Center for Public Opinion Research · other/study · https://doi.org/10.25940/roper-31097880

Direction of New York State (1); direction of country (1); opinion of people and institutions in public life (9); 2016 election for U.S. Senator (1); 2016 election for President (1); Hillary Clinton vs. Donald Trump (1); vote to re-elect Governor Andrew Cuomo (1); Andrew Cuomo job performance as Governor (1); Andrew Cuomo policies as ethical or not (1); preferred political party to control State Senate (1); important issues for Governor and State Legislature to act on (7); corruption in state government (4); view on State Legislature becoming full-time with outside employment banned (1); how will recent corruption scandals affect your vote to re-elect state legislators (2); optimism that the Governor and Legislature will enact anti-corruption legislation (1); support or oppose ride sharing companies, Uber (1); legalize daily fantasy sports companies, FanDuel/Draftkings (1).

**Решение:** -3 политический опрос об отношении к легализации фэнтези-спорта без инструмента PG

---

### 215 · R3881

**Tze Leung Lai and Anna Choi's contribution to the Discussion of ‘Testing by betting: A strategy for statistical and scientific communication’ by Glenn Shafer**

2021 · Journal of the Royal Statistical Society: Series A (Statistics in Society) · https://doi.org/10.1111/rssa.12662

Comments on an article by Glenn Shafer (see record 2021-44219-001). It is exciting to follow Glenn Shafer's investigations into forecasting, betting, reasoning with uncertainty and foundational issues in probability, beginning with his 1973 PhD thesis at Princeton and culminating in Shafer on the Dempster-Shafer theory of belief functions, and its evolution during the past five decades to the present paper on betting scores and game-theoretic probability. Betting scores are particularly relevant in this momentous year of intensive global search for COVID19 vaccines and treatments, and upcoming presidential and congressional elections in the United States, about which pundits keep giving time-varying forecasts of the outcomes while betting markets on presidential election odds have been particularly active, similar to online sports betting markets. (PsycInfo Database Record (c) 2022 APA, all rights reserved)

**Решение:** -6 дискуссия по философии математической статистики, не гемблинг

---

### 216 · R2869

**The Martingale Index: A Measure of Self-Deception**

2023 · SSRN Electronic Journal · preprint · en · https://doi.org/10.2139/ssrn.4488359

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? The Martingale Index, нет аннотации, проверить полный текст

---

### 217 · R3887

**An agent-based model of a betting exchange via a single-threaded and object-oriented implementation**

2021 · Social Science Research Network · article, other literature type, posted-content · en · https://doi.org/10.2139/ssrn.3874192

The sports betting industry attracts millions of participants to gamble on a wide variety of sports across&lt;br&gt;the world. Horse racing is inextricably linked to gambling, and one of the most popular methods of&lt;br&gt;placing bets is via a betting exchange, such as Betfair. A population of bettors will have a diverse&lt;br&gt;range of beliefs, opinions, and experiences to help guide them to the bets they want to place. These&lt;br&gt;prior beliefs are then converted to likelihoods, represented by betting odds, of certain outcomes occurring&lt;br&gt;during a sporting event, either before it has started or while it is running, the latter known as in-play&lt;br&gt;betting. Trading a bet through an exchange involves matching a back bet and a lay bet together to form&lt;br&gt;a near zero-sum game, where one bettor’s profit is another bettor’s loss without taking into account&lt;br&gt;the exchange’s commission fees. This mechanism allows various possible strategies for a bettor to turn&lt;br&gt;a profit gambling on a horse race, with automated betting agents proven to be a popular method of&lt;br&gt;discovering and exploiting strategies. Creating and training these programs requires huge quantities of&lt;br&gt;data, and since horse racing is the most lucrative sports betting market, historical data can be very&lt;br&gt;expensive to obtain and time-consuming to understand. This thesis presents an implementation of a&lt;br&gt;possible solution to this issue, as an alternative to historical data. The Bristol Betting Exchange (BBE),&lt;br&gt;a novel proposal for sports betting research devised by Cliff (2021) [8], is a model simulation of a betting&lt;br&gt;exchange, that is composed of a population of automated betting agents, as well as a horse race simulator&lt;br&gt;that produces compelling horse race scenarios. My version of the BBE is entirely written in the Python&lt;br&gt;3 programming language, is single-threaded and provides a simple Command-Line-Interface, all to aid&lt;br&gt;accessibility for future researchers who may be non-expert programmers. I also designed and developed&lt;br&gt;a prototype, cloud-based version of this implementation that can reduce computational cost for users&lt;br&gt;and increase the speed of generating large datasets via the use of multiple virtual machines provided&lt;br&gt;by Amazon Web Services. Future work to improve this implementation will include making it even&lt;br&gt;more accessible, through possible deployment of a cloud application with a web-based Graphical User&lt;br&gt;Interface as a controller, as well as rigorous analysis to compare simulated data against its historical&lt;br&gt;counterpart.

**Решение:** -2 агентная модель биржи ставок без опроса людей

---

### 218 · R3499

**Using "Markers of Harm" to Track Risky Gambling in Two Cohorts of Online Sports Bettors.**

2022 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-021-10097-0

Online gambling poses novel risks for problem gambling, but also unique opportunities to detect and intervene with at-risk users. A consortium of gambling companies recently committed to using nine behavioral "Markers of Harm'' that can be calculated with online user data to estimate risk for gambling-related harm. The current study evaluates these markers in two independent samples of sports bettors, collected ten years apart. We find over a two-year period that most users never had high enough overall risk scores to indicate that they would have received an intervention. This observation is partly due to characteristics of our samples that are associated with lower risk for gambling-related harm, but might also be due to overly high risk thresholds or flaws in the design of some markers. Users with higher average risk scores had more intraindividual variability in risk scores. Younger age and male gender were not associated with higher average risk scores. The most active users were more likely than other users to have ever exceeded risk thresholds. Several risk scores significantly predicted proxies of gambling-related harm (e.g., account closure). Overall, the current Markers of Harm system has some correctable limitations that future risk detection systems should consider adopting.

**Решение:** -3 поведенческие маркеры вреда на данных оператора без опросника проблемной игры

---

### 219 · R7014

**Non)Gambling Corruption in Sports**

2012

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 коррупция в спорте без гемблинга

---

### 220 · R5376

**The influence of marketing on the sports betting attitudes and consumption behaviours of young men: implications for harm reduction and prevention strategies.**

2017 · Harm reduction journal · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1186/s12954-017-0131-8

BACKGROUND: Gambling can cause significant health and social harms for individuals, their families, and communities. While many studies have explored the individual factors that may lead to and minimise harmful gambling, there is still limited knowledge about the broader range of factors that may contribute to gambling harm. There are significant regulations to prevent the marketing of some forms of gambling but comparatively limited regulations relating to the marketing of newer forms of online gambling such as sports betting. There is a need for better information about how marketing strategies may be shaping betting attitudes and behaviours and the range of policy and regulatory responses that may help to prevent the risky or harmful consumption of these products. METHODS: We conducted qualitative, semi-structured interviews with 50 Australian men (aged 20-37 years) who gambled on sports. We explored their attitudes and opinions regarding sports betting marketing, the embedding of marketing within sports and other non-gambling community environments, and the implications this had for the normalisation of betting. RESULTS: Our findings indicate that most of the environments in which participants reported seeing or hearing betting advertisements were not in environments specifically designed for betting. Participants described that the saturation of marketing for betting products, including through sports-based commentary and sports programming, normalised betting. Participants described that the inducements offered by the industry were effective marketing strategies in getting themselves and other young men to bet on sports. Inducements were also linked with feelings of greater control over betting outcomes and stimulated some individuals to sign up with more than one betting provider. CONCLUSIONS: This research suggests that marketing plays a strong role in the normalisation of gambling in sports. This has the potential to increase the risks and subsequent harms associated with these products. Legislators must begin to consider the cultural lag between an evolving gambling landscape, which supports sophisticated marketing strategies, and effective policies and practices which aim to reduce and prevent gambling harm.

**Решение:** -2 качественное исследование влияния маркетинга на ставки среди молодежи

---

### 221 · R5549

**Routes to Fandom Discovery and Expression of Fan Identity in Furry , Anime , and Fantasy Sport**

2017

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 исследование фан-сообществ фурри, аниме и фэнтези-спорта, не гемблинг

---

### 222 · R3893

**A global take on legal aspects of fantasy sports**

2021 · The International Sports Law Journal · article, journal-article · en · https://doi.org/10.1007/s40318-021-00199-7

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 глобальный обзор правовых аспектов фэнтези-спорта

---

### 223 · R6984

**Optimal Mark-Up and Arbitrages in the Betting Market**

2012 · SSRN Electronic Journal · preprint · en · https://doi.org/10.2139/ssrn.2199035

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -2 анализ маржи букмекеров и арбитража на рынках ставок

---

### 224 · R2201

**Τυπολογία του ψηφιακού μάρκετινγκ στον τομέα των αθλητικών στοιχημάτων και τυχερών παιχνιδιών. Βιβλιογραφική ανασκόπηση**

2025 · Πανεπιστήμιο Πελοποννήσου · other/μεταπτυχιακή διπλωματική εργασία · el · https://doi.org/10.26263/amitos-2540

Σκοπός της μεταπτυχιακής διπλωματικής εργασίας (ΜΔΕ) ήταν η κριτική σύνθεση της ακαδημαϊκής βιβλιογραφίας για την αξιολόγηση του τρόπου με τον οποίο οι στρατηγικές – τυπολογίες του ψηφιακού μάρκετινγκ λειτουργούν εντός των συγκεκριμένων περιορισμών και ευκαιριών του κλάδου των τυχερών παιχνιδιών. Η παρούσα ΜΔΕ υιοθέτησε μια αφηγηματική προσέγγιση βιβλιογραφικής ανασκόπησης, οργανώνοντας την υπάρχουσα έρευνα θεματικά γύρω από τις στρατηγικές ψηφιακού μάρκετινγκ και τη σημασία τους στο πλαίσιο των αθλητικών στοιχημάτων και τυχερών παιχνιδιών. Στόχοι της έρευνας ήταν: (α) να αναλύσει πώς χρησιμοποιούνται οι διάφορες προσεγγίσεις ψηφιακού μάρκετινγκ από τους φορείς εκμετάλλευσης τυχερών παιχνιδιών, (β) να προσδιορίσει τις συμπεριφορικές, ηθικές και ρυθμιστικές επιπτώσεις αυτών των στρατηγικών, και (γ) να παράσχει συστάσεις για τη μελλοντική έρευνα και την ανάπτυξη πολιτικής. Για την εκπλήρωση των παραπάνω στόχων, η εργασία διερεύνησε τα ακόλουθα ερευνητικά ερωτήματα: (1) ποιες στρατηγικές ψηφιακού μάρκετινγκ χρησιμοποιούνται συνήθως στον κλάδο των τυχερών παιχνιδιών και των αθλητικών στοιχημάτων, (2) πώς αυτές οι στρατηγικές επηρεάζουν τη συμπεριφορά και τη δέσμευση των καταναλωτών, (3) ποιες ηθικές και κανονιστικές προκλήσεις συνδέονται με το ψηφιακό μάρκετινγκ σε αυτό το πλαίσιο και (4) ποια κενά υπάρχουν στη βιβλιογραφία και πώς μπορεί να τα αντιμετωπίσει η μελλοντική έρευνα. Τα αποτελέσματα της συνδυαστικής προσέγγισης της έρευνας έδειξαν ότι η προώθηση των θεωρητικών προσεγγίσεων σε συνδυασμό με την ενσωμάτωση των στρατηγικών – τυπολογιών του ψηφιακού μάρκετινγκ εμπλουτίζουν την κατανόηση της συμπεριφοράς των καταναλωτών στα πλαίσια των τυχερών παιχνιδιών. Πρακτικά, αυτές οι γνώσεις προσδίδουν στρατηγική κατεύθυνση στους φορείς εκμετάλλευσης τυχερών παιχνιδιών για την ανάπτυξη πιο ηθικά ευθυγραμμισμένων και αποτελεσματικών καμπανιών μάρκετινγκ, δίνοντας έμφαση στο εξατομικευμένο, υπεύθυνο και ελκυστικό διαφημιστικό περιεχόμενο που σέβεται την ευημερία των καταναλωτών και τη συμμόρφωση με τις κανονιστικές διατάξεις.

**Решение:** -1 нарративный литературный обзор цифрового маркетинга ставок

---

### 225 · R0832

**The Prototype Willingness Model of Sports Betting: A Yearlong Within-Person Study of Young Adults.**

2026 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-026-10477-4

Burgeoning evidence of sports betting harms among young adults highlights the need to refine our understanding of psychosocial processes driving sports betting behavior. This study longitudinally examined sports betting patterns over time within the Prototype Willingness Model (PWM), a dual-process behavioral model comprised of both a reasoned and socially reactive component. Participants included 210 18-29 year olds (77.1% male; mean age 24.5) who reported placing at least two sports bets in the past month (at screening). Participants reported past two-week sports betting frequency (i.e., number of sports bets placed) and PWM cognitions (i.e., attitudes, normative perceptions, perceived vulnerability, prototype similarity, intentions, willingness) on 26 biweekly surveys covering a year-long study period. Findings generally support the PWM's application to sports betting at the within-person level for the reasoned and social reaction pathways. When attitudes and perceived friend approval of sports betting were higher than usual, participants reported greater intentions to sports bet. When prototype similarity and perceived friend engagement in sports betting were higher than usual, participants reported greater willingness to sports bet. Subsequently, intentions and willingness predicted sports betting frequency, reflecting mediation processes. This study provides foundational evidence for the development of adaptive prevention and intervention strategies - grounded in the PWM framework - to address the cognitive processes that facilitate risky sports betting behavior.

**Решение:** ? продольный опрос 210 молодых спортивных беттеров, проверить наличие инструмента PG в полном тексте

---

### 226 · R5534

**What the rise of daily fantasy sports will mean for problem gambling**

2017 · The Conversation Media Group Ltd · article, other, posted-content · en · https://doi.org/10.64628/aa.wamptdmrw

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 аналитический комментарий о последствиях дейли фэнтези для проблемного гемблинга

---

### 227 · R5441

**To i?nvesti?gate the relati?onshi?p between the moti?vati?on to watch sport and the moti?vati?on to bet i?n those who parti?ci?pate i?n sport betti?ng**

2017 · Niğde Üniversitesi Açık Erişim Sistemi · dissertation · tr

Bu araştırmada spor bahisi oynayan seyircilerin seyretme güdüleri ile bahis oynama motivasyonları arasındaki ilişkilerin incelenmesi amaçlanmıştır. Betimsel yöntem ve ilişkisel tarama modelinin kullanıldığı bu çalışma, toplanılan veriler anket yöntemiyle elde edilmiştir. Araştırmanın örneklem grubunu Niğde ilinde yaşayan spor bahis oyunlarına katılan spor müsabakaları izleyen seyircilerden oluşmuştur. Bahis oynayan spor müsabaka seyircileri hakkında kayıtlı bir veri bulunmadığından anket dağıtımı sırasında katılımcıların bahis oyunlarına katılıp katılmadıkları sorularak örneklem grubu oluşturulmuştur. 345 adet anket dağıtılmıştır ve doğru doldurulan 327 anket değerlendirilmeye alınmıştır. Araştırmada, veri toplama aracı olarak 4 ana bölümden oluşan bir anket kullanılmıştır. Birinci bölümünde Polat ve Yalçın (2017) tarafından geliştirilen, 7'li likelt şeklinde ve 25 maddeden oluşan Spor Seyircileri için Dışsal Güdü Ölçeği, ikinci bölümünde yine (Polat ve Yalçın, 2017) tarafından geliştirilen, 7'li likelt şeklinde ve 21 maddeden oluşan Spor Seyircileri İçin İçsel Güdü Ölçeği, üçüncü bölümde (Chantal, Vallerand ve Vallieres, 1994) tarafından geliştirilen ve (Karlı, 2008) tarafından Türkçe'ye uyarlanan, 5'lilikelt şeklinde ve 28 maddeden oluşan Bahis Güdülenme Ölçeği, dördüncü bölümde ise kişisel bilgi formu yer almaktadır. Verilerin analizinde SPSS paket programı kullanılmıştır. Öncelikle değişkenlere ait Kolmogov-Smirno ve Shapiro-Wilk normallik dağılım istatistiği yapılmıştır (Tablo 3.1). Elde edilen sonuçlara dayanak tüm hipotez testleri için nonparametrik test kararı alınmıştır. Sonrasında bazı tanımlayıcı istatistiklere ilişkin yüzde frekans dağılımları, ortalama ve yaygınlık sonuçları verilmiştir. Gruplar arası ikili kategorik karşılaştırmalar için Mann Whitney U testi, çoklu kategorik karşılaştırmalar için ise Kruskall Wallis H testi yapılmıştır. Ayrıca sürekli veri niteliğindeki bağımsız değişkenler ve ölçüm araçları alt boyutları arası ilişkiler için Spearman Kolerasyon Analizinden yararlanılmıştır. Elde edilen bulgular sonucunda bağımsız değişkenlerin (cinsiyet, yaş, aylık ortalama gelir, spor müsabakası için aylık ortalama harcama, bahis oynanan branş, bahis oynama süresi, bahis oynamak için aylık ortalama harcama, aktif spor yapma durumu, bir branş takımı tutma, taraftarlık düzeyi) bahis motivasyonu, spor müsabakalarını dışsal seyretme sebepleri ve spor müsabakalarını içsel seyretme sebeplerinden bazılarını etkilediği söylenebilir. Ayrıca bahis oynama motivasyonu arttıkça seyretme güdülerinin de arttığı söylenebilir.

**Решение:** ? опрос спортивных беттеров о мотивах, проверить наличие опросника PG в полном тексте

---

### 228 · R6428

**Jalgpalliennustuse koefitsientide reaalajaline mudel pakkumiseks ennustusportaalidele. Model for Offering Bookmakers Live In-play Football Betting Odds**

2014

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -2 модель коэффициентов футбольных прогнозов в реальном времени

---

### 229 · R5884

**The Mainstreaming of Fantasy Sport**

2016 · other · en · https://doi.org/10.5040/9781666993677.ch-012

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 аналитическая глава книги о мейнстримизации фэнтези-спорта

---

### 230 · R3241

**US sports betting to grow despite California rejection**

2022 · Emerald expert briefings · report, report-component · en · https://doi.org/10.1108/oxan-db274026

Significance The outcome has dashed gaming industry hopes that California, the most populous US state, would join more than 35 others that have legalised sports betting since a 2018 Supreme Court ruling made it possible. The higher-profile measure, Proposition 27, was the most expensive in California’s history; combined spending by the two sides totalled more than USD400mn. Impacts The growing popularity of women's sports will create a new market segment for sports betting. AI-driven data analytics will allow innovation that leads to customised betting for fan segments and eventually individuals. The metaverse will open up new opportunities, many as yet unimaginable, for the gamification of sports betting.

**Решение:** -1 отраслевой аналитический обзор рынка спортивных ставок в США

---

### 231 · R5935

**Fantasy sports across the pond**

2016 · Lexington Books · part of book or chapter of book · eng · https://pub.uni-bielefeld.de/record/2943266

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 глава книги о сравнительном анализе фэнтези-спорта в США и Великобритании

---

### 232 · R7242

**Sports Betting in Norway: Law and Policy**

2011 · ASSER international sports law series · other literature type, part of book or chapter of book, review · en · https://doi.org/10.1007/978-90-6704-799-9_37

This book looks at the Law and Policy on Betting and Sport in many countries around the world––sport is a global phenomenon—providing a very useful and valuable comparative survey on a subject that is so vital for safeguarding and preserving the integrity of those sports in which betting is legally allowed.The country reports show how sports-related betting is organized in the country concerned, also from a historical and policy perspective (national Lotteries Act; state run/state licensed lotteries and/or private operators; how the licensing system for public operators works; state supervisory mechanisms, etc.) and contain a treatment of the national case law. These keywords were added by machine and not by the authors. This process is experimental and the keywords may be updated as the learning algorithm improves.

**Решение:** -1 правовой анализ норвежского законодательства о ставках

---

### 233 · R3006

**A social selection mechanism for sports betting market**

2023 · Decision Support Systems · article, journalarticle, journal-article · en · https://doi.org/10.1016/j.dss.2023.114119

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -2 социальный механизм отбора на рынках ставок без аннотации

---

### 234 · R0682

**Sports Betting Across Borders: Spatial Spillovers, Credit Distress, and Fiscal Externalities**

2026 · Staff reports · article, casereport, report · und · https://doi.org/10.59576/sr.1184

Since the 2018 Murphy v. NCAA decision, 38 states have legalized mobile sports betting. We study effects on betting and consumer credit, emphasizing spatial spillovers across state lines. Using consumer spending data and an extended two-way fixed effects framework that separately identifies direct and spillover effects, we find that legalization increases total sportsbook spending roughly tenfold and take-up by 3.1 percentage points. Counties in non-legal states within 15 miles of a legal state experience spillover spending equal to roughly 14 percent of the direct effect, with these spillovers declining to roughly zero by 60 miles. Using the New York Fed Consumer Credit Panel, we find that median credit scores decline by roughly 1 point and overall delinquency rises 0.3 percentage points from a 10.7 percent base, with spillover delinquency rising nearly 0.2 percentage points. Under-40 auto loan delinquency increases by half a percentage point and credit card delinquency by one percentage point, driving the overall increase in delinquency. Scaling the population-level delinquency effect by take-up yields implied delinquency increases of roughly 10 percentage points among induced bettors. We conclude with a policy simulation which reveals that spillovers create a fiscal asymmetry: states that have not legalized bear costs from cross-border betting without capturing tax revenue, giving high exposure states a stronger case for legalization. This incentive is increasing in states that have higher pre-legalization betting activity, population centers near legal states, and a younger population. Methodologically, we show that ignoring spatial spillovers can contribute to attenuated estimates and an under-count of the affected population.

**Решение:** -2 эконометрический анализ кредитных данных и транзакций без опроса людей

---

### 235 · R6418

**The Right to Use One's Image for Betting Services**

2014 · SSRN Electronic Journal · article, other literature type, preprint · en · https://doi.org/10.2139/ssrn.3148820

Greek law treats the right to one’s name as a special manifestation of the personality right and a breach thereof as an infringement of the personality right as a whole. The right of every natural or legal person to its name includes the right-holder’s power to decide if and when to allow the use of its name by a third party. This right has personal as well as financial aspects. The financial aspects of the right contain also the right-holder’s power for commercial exploitation. Therefore the use of the name of a sports club or an athlete by a sport betting services provider should always follow the permission of the right-holder. An explicit legislative recognition of the commercial aspects of this right would help solve many contemporary problems faced by the sport sector.

**Решение:** -1 правовой анализ использования прав на изображение в ставках

---

### 236 · R5101

**La eficacia de los contratos online de apuestas deportivas amañadas**

2018 · Revista Aranzadi de derecho de deporte y entretenimiento · article · es

espanolEl presente trabajo trata de analizar, desde el punto de vista del Derecho privado, las consecuencias que para los contratos de apuestas y las partes implicadas en ellos pueden tener los amanos en competiciones deportivas. Esto incluye los contratos en los que participan los propios implicados en los eventos deportivos, asi como los que conocen la existencia del amano. Igualmente estudiaremos los efectos que tendra frente a contratantes de buena fe, que desconocian la existencia del amano. Especial atencion prestaremos a las habituales clausulas que se incluyen en las condiciones generales de las empresas del sector para anular aquellas apuestas sobre eventos deportivos que tengan visos de tener algun tipo de irregularidad. EnglishThis paper work tries to analyze, from the point of view of the private Law, the consequences that for the contracts of bets and the parts implied in them can have the fixings in sports competitions. This includes the contracts in which those involved in sporting events participate, as well as those who know the existence of the match. We will also study the effects it will have on contractors of good faith, who were unaware of the existence of the match. Special attention will be paid to the usual clauses that are included in the general conditions of companies in the sector to cancel those bets on sporting events that are likely to have some kind of irregularity.

**Решение:** -1 юридический анализ договоров ставок при договорных матчах

---

### 237 · R3287

**The Negro Leagues Were Major Leagues: Historians Reappraise Black Baseball**

2022 · Pennsylvania history · article · en · https://doi.org/10.5325/pennhistory.89.1.0135

In 2020 Negro League Baseball commemorated the centennial of Rube Foster's organizing the Negro National League. Established in Kansas City, Missouri, on February 13, 1920, the Negro National League (NNL) took the final step to corral all the history and sporting assets of African American baseball into an organized league platform that would propel the sport into a greater appreciation among baseball fans but also put added pressure on national Jim Crow attitudes about integration. Since the 1960s baseball Hall of Famers, including former Negro Leaguer Jackie Robinson, had been calling for the inclusion of NNL players in the Hall of Fame in Cooperstown. They knew that a century of interracial play and intra-racial competition displayed some of the best players the game has ever seen or heard about in segregated America. The result was Satchel Paige's induction in 1971. But critics of the accomplishments of NNL players still held Jim Crow attitudes and racist perspectives of African American and Latinx players' abilities covering more than a century in the game.Todd Peterson has edited a book that addresses all the criticisms of Negro League baseball and, with supreme research and evidence, attacks racist platforms that have kept NNL history in a second-class status of the American pastime. The book is divided into two parts with chapters written by some of the best baseball writers and historians working today. In Part 1 seven chapters analyze the data providing evidence of African American play. Topics include “Baseball Is the Music of Mathematics” (Larry Lester); “The Case for the Negro Leagues” (Peterson); “Measuring Equality: A Statistical Comparison of the Negro Leagues to the Major Leagues Based on the 1925 Season” (Richard J. Puerzer); “Gray Area: Homestead vs. the Minor Leagues” (Scott Simkus); “The Color of Money: Salaries and Performances in Pre- and Post-Integration Baseball” (Michael Haupert); “Winning in the Crucible of White-Hot Competition” (Jefferey Williams); and “Top Ten Reasons Why the Negro League Should Be Declared a Major League” (Ted Knorr).Opponents to including Negro League play as equal to Major League play often claimed that game-by-game stats for the Negro Leagues did not exist; therefore, they could not be evaluated and measured against Major League play. That objection is exposed in part 1 as inaccurate, as authors compare head-to-head play, compensation, batting stats, and winning percentages for players in both the NNL and MLB. In some of the analysis, such as compensation, Haupert shows what Negro League players would have made in salary based on the rubric used by Major Leagues. But most of the critical conversation had been around head-to-head play between Negro and white players. Each writer takes a stab at this evidence. Williams sums it up, stating, “Rube Foster's formation of the Negro National League in 1920 was the turning point in the history of black baseball. Before the NNL began operation, black teams had gone 90–121–9 against white big league clubs.” He further stated the impact the NNL had on Negro League play: “From the inception of the NNL through 1948, Negro Leagues teams went 206–163–10 against big league all-star teams” (75). This point harnesses Peterson's conclusion that the Negro Leagues were Major League baseball.Part 2 focuses on case studies of people, places, teams, persons, and new perspectives on the road to integration and the evolution of Negro League on integration in the Major Leagues. Chapters in this section are as follows: “Hotel Resorts and the Emergence of the Black Baseball Professional: Riverine and Maritime Communities, 1867–1890” (James E. Brunson III); “Leading Off: The Cuban Giants” (Tony Kissel); “Rube Foster: Negro League Giant” (Robert C. Cottrell); “John Donaldson: Restoring the Legacy of Segregated Baseball's Greatest Pitcher” (Pete Gorton); “The Measure of Failure: Atlanta Baseball and Community Development in the 1930s and 1970s” (Thomas Aiello); “Changing the Way They Do Business: Jackie Robinson, Integration and the Origins of Organizational Culture in Organized Baseball” (Michael Lomax); “Separate but Unequal” (Philip J. Lowry); and “Monuments: The Shaping of Negro Leagues Public Memory” (Josh Howard). Part 2 provides a chronology of Negro baseball and comparisons of the game in the post–Jackie Robinson era. Brunson's chapter about regional Negro baseball as an extension of clubs, resorts, barbers, and caterers' enterprises is an open door to African American sociocultural dynamics at an earlier time. Kissell's chapter about the Cuban Giants establishes a history of interracial play during the nineteenth century. Cottrell's biography of Rube Foster shows that neither Foster nor any other Negro League players were complete mysteries to Major League players and the press.The Negro Leagues Were the Major Leagues is very well researched and thought-provoking in the topics the editor chose to present. The argument that Negro League Baseball was a Major League sport is based on the criteria that baseball guardians had set. Peterson et al. used reliable sources to address the criteria with sources such as newspaper accounts, books, periodicals, electronic sources, film, oral histories, interviews, and public records. The backdrop of Negro League baseball has been the racial attitudes in America that impacted many aspects of baseball life. W.E.B. Du Bois acknowledged in his monumental work The Souls of Black Folk that “the problem of the twentieth century is the problem of the color line.” Efforts to integrate baseball or even just play against white teams were kept at arm's-length. In the era of Jack Johnson, white fears of black sporting superiority challenged white notions of racial hegemony. Boxing was popular but baseball was defining of America. Negro baseball teams wanted to advance the status of the sport and organize a league.Baseball is a sport that relies on statistics that make for a great part of the game. This book has come at a time when the game is more reliant on metrics and fans are seeing these metrics in fantasy sports betting and other forms of fan enjoyment. Now because of this book many new applications of Negro League games can be applied. No longer can a lack of statistical information be used as an excuse to restrict the Negro League game or its players from greater appreciation in baseball's history. The Major Leagues are still used as the measure for the quality of the Negro League game, but the Negro League is never used as the measure for the Major League game. This notion that white sport and society are superior to African American sport and society prevents a true understanding of the sport and those who participated in it. Since the publication of this book Negro baseball has had its statistical history integrated into the MLB game. MLB.com writer Anthony Castrovince wrote in December 2020 that “MLB Commissioner Ray Manfred bestowed Major League status upon seven professional Negro Leagues that operated between 1920 and 1948. The decision means that the approximately 3,400 players of the Negro Leagues during this time period are officially considered Major Leaguers, with their stats and records becoming a part of Major League history.” The Negro Leagues Were the Major Leagues is a must read for anyone interested in Negro League history and a greater understanding of its value to the American pastime.

**Решение:** -6 история бейсбола / негритянские лиги, не гемблинг

---

### 238 · R6815

**運動彩券交易之資料採礦分析; Data Mining on Sport Lottery Transactions**

2013 · dissertation · zh

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -3 интеллектуальный анализ транзакционных данных спортивной лотереи

---

### 239 · R7236

**Modelado de los resultados de partidos de fútbol y de las ineficiencias en los mercados de apuesta**

2011 · bachelor thesis, other literature type · esl/spa · https://hdl.handle.net/10016/13740

Las apuestas deportivas están cobrando gran importancia en la actualidad. Este Proyecto Fin de Carrera surge para abordar esta problemática, enfocado al fútbol, que tiene como objetivo la estimación de la probabilidad de que gane un equipo un partido. Si la estimación difiere de los valores establecidos por las casas de apuestas, siendo los segundos menos precisos, es posible que obtengamos retornos positivos. Desarrollaremos un modelo con el que obtendremos las tasas de ataque, defensa y factor de casa y, a partir de estos parámetros, se estiman las probabilidades de ganar del equipo local, el visitante o el empate. Nos valdremos del Criterio de Kelly para llevar a cabo las apuestas. Nos centraremos en casas de intercambio que operan en internet: Betfair, Miapuesta y Bet365. Aplicaremos nuestro modelo a la Liga BBVA 2010-2011 y a las casas de apuestas indicadas.

**Решение:** -2 моделирование исходов матчей и неэффективности букмекерских рынков

---

### 240 · R0791

**Probability Models and Optimization of Strategies in Sports Betting**

2026 · U svìtì matematiki. · journalarticle, article, journal-article · https://doi.org/10.17721/1029-4171.2026/1.7

The article explores the mathematical basis of the functioning of the sports betting market, which, in the conditions of intensive media promotion, is mistakenly interpreted by the mass consciousness as a sphere of random success. The focus is on the discrepancy between the marketing image of "easy profit" and the objective mathematical reality, which is based on deterministic algorithms for ensuring the profitability of bookmaker organizations. The aim of the article is to analyze the key mathematical tools that explain the nature of sports betting: bookmaker's margin, expected value (EV), variance, Cayley criterion and Poisson distribution. It is shown how the margin ensures a stable profit for the company, EV allows you to determine the "value" of the bet, variance describes the level of risk and uncertainty, and Cayley criterion gives the optimal formula for the size of the bet. The use of the Poisson distribution is considered as an example of statistical prediction of results in football. The results of the study prove that a mathematical approach can make betting more rational, but does not eliminate the bookmaker's systemic advantage. Prospects for further research lie in combining classical probability models with modern machine learning methods, as well as in an interdisciplinary analysis of the impact of advertising and psychological factors on player behavior.

**Решение:** -2 вероятностные модели и оптимизация стратегий в ставках

---

### 241 · R4535

**Behavioral Markers of Risky Daily Fantasy Sports Play**

2020 · Journal of Sport and Social Issues · article, journalarticle, journal-article · en · https://doi.org/10.1177/0193723520919819

To understand the natural groups of daily fantasy sports (DFS) players and their associated problematic play, we obtained DFS participation records for 11,130 DFS players from a leading provider. A cluster analysis suggested four player clusters. Cluster 4 included a single highly successful player (i.e., an outlier). Players in Cluster 1 had shorter playing durations than players in Clusters 2 and 3 and picked riskier contests than players in Cluster 3. Players in Cluster 2 picked riskier contests than players in Cluster 3 and had longer playing durations than players in Cluster 1. Players in Cluster 3 experienced greater financial DFS success than others. This suggests that measures of DFS involvement can identify natural DFS player groups with distinct problematic play experiences.

**Решение:** -3 данные оператора о транзакциях игроков без опросника проблемной игры

---

### 242 · R6480

**Betting on State Equality: How the Expanded Equal Sovereignty Doctrine Applies to the Commerce Clause and Signals the Demise of the Professional and Amateur Sports Protection Act**

2014 · bepress Legal Repository · article · en

In recent years, the U.S. Supreme Court revived the long-dormant equal sovereignty doctrine, which states that the federal government cannot enact legislation that renders states unequal in power, dignity, and authority. Although the doctrine historically applied only in the context of states entering the Union, in the 2013 case Shelby County v. Holder, the Supreme Court broadened the doctrine’s scope, holding that the doctrine applied to all disparate treatment of states. As such, the revived equal sovereignty doctrine leaves federal statutes—such as the Professional and Amateur Sports Protection Act (“PASPA”), which prohibits state-sanctioned casino sports gambling in all states except for Nevada—on uncertain constitutional grounds. Contrary to a recent Third Circuit holding, this Note argues that PASPA’s disparate treatment of states violates the equal sovereignty doctrine. Under an approach developed by this Note, which requires Congress to demonstrate that disparate treatment of states is sufficiently related to the problem that the statute seeks to address, this Note contends that PASPA violates the equal sovereignty doctrine because the exemption of Nevada is not reasonably related to the national problem of sports gambling, which PASPA seeks to address. Importantly, adopting this approach would harmonize the Supreme Court’s Commerce Clause jurisprudence with its recently expanded equal sovereignty doctrine analysis.

**Решение:** -1 конституционно-правовой анализ равенства штатов и закона PASPA

---

### 243 · R8157

**The prevalence of sport gambling in NCAA Division III student-athletes**

2003 · Cardinal Scholar (Ball State University) · dissertation · en

There is no abstract available for this research paper.

**Решение:** ? исследование распространенности ставок у студентов-спортсменов, нет аннотации, проверить полный текст

---

### 244 · R7655

**지방의 재정자주권 확보를 위한 레저세의 확대개편방안**

2009 · 한국지방자치연구 · article · ko

본 연구는 레저세가 지방세로서 존치되어야하는 합당한 이유와 함께, 지역세원으로써의 역할을 보다 공고히 할 수 있도록 레저세의 과세대상을 확대 개편하는 방안을 고찰하는데 목적이 있다. 카지노와 스포츠토토, 관광자원 및 지역자원이 과세 확대대상으로 고려되었으며, 이들을 대상으로 응익성과 세수 신장성, 지역성이라는 세 가지 기준 하에 세원 적정성 평가를 실시하였다. 그 결과 레저세 확대개편방안 세 가지를 제시할 수 있었다. 대안1은 기존의 레저세 과세대상에 카지노와 스포츠토토를 과세대상으로 추가하는 것으로 그로 인한 세수효과는 전국적으로 9,107억원 정도로 예상할 수 있다. 대안2는 대안1에 관광자원을 과세대상으로 편입시키는 것으로, 부가가치세 중 관광관련 항목을 중심으로 세수효과를 측정하였다. 그 효과는 1조 6,097억원으로 세 가지 대안 중 신장성이 가장 높으며, 가장 큰 세원이 될 것으로 예상되었다. 대안3은 장기적인 대안으로서 대안2에 지역자원을 과세대상으로 추가하는 것이다. 이는 현재의 지역개발세를 레저세로 통합하는 방안이다. 세수효과는 1조 7,868억원으로 지역개발세의 세수가 미미하여 대안 1이나 2보다는 세수규모가 크게 늘지 않았다. 그러나 지역특성을 살린 세원을 발굴하여 과세자주권을 확보하기 위해서는 대안3이 합리적일 것으로 판단되었다.

**Решение:** -1 налоговая и бюджетная политика в отношении игорного бизнеса

---

### 245 · R2213

**Evaluation System and Empirical Test of the Communication Effect of Responsibility Lottery in China Sports Lottery**

2024 · Health Science and Management · article, journal-article · en · https://doi.org/10.62091/hsm2024023

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? эмпирический тест эффекта коммуникации спортлото, нет аннотации, проверить полный текст

---

### 246 · R2269

**Optimizing Fantasy Sports Team Selection with Deep Reinforcement Learning**

2024 · COMAD/CODS · article, conference object, preprint · en · https://doi.org/10.1145/3703323.3703743

Fantasy sports, particularly fantasy cricket, have garnered immense popularity in India in recent years, offering enthusiasts the opportunity to engage in strategic team-building and compete based on the real-world performance of professional athletes. In this paper, we address the challenge of optimizing fantasy cricket team selection using reinforcement learning (RL) techniques. By framing the team creation process as a sequential decision-making problem, we aim to develop a model that can adaptively select players to maximize the team's potential performance. Our approach leverages historical player data to train RL algorithms, which then predict future performance and optimize team composition. This not only represents a huge business opportunity by enabling more accurate predictions of high-performing teams but also enhances the overall user experience. Through empirical evaluation and comparison with traditional fantasy team drafting methods, we demonstrate the effectiveness of RL in constructing competitive fantasy teams. Our results show that RL-based strategies provide valuable insights into player selection in fantasy sports. 8 Pages including references, Accepted to CODS-COMAD 2024 conference

**Решение:** -2 алгоритм глубокого обучения с подкреплением для фэнтези-крикета

---

### 247 · R7701

**Appendix: Topics for Presentations, Discussions, and Papers**

2008 · other · en · https://doi.org/10.1017/cbo9780511804151.021

Accountability of bloggers – A blog is a Web site containing analyses, opinions, and sometimes hyperlinks. What is the accountability of the owner of the blog for this material? Carnivore's use by the FBI – Carnivore is an investigative device used to monitor e-mail and other electronic communications by means of “packet sniffing.” It has raised privacy concerns. Computer viruses – Programs that enter a computer through trickery or stealth, infecting it and usually corrupting its data and/or affecting its operation. Credit card fraud online – Often involves “spoofing” (see Web spoofing) to obtain personal information that will enable illicit use of a credit card. Cybersquatting – Usually involves investing in domain names that might in turn be sold to companies for a higher price than was originally paid. Data mining – The practice of sifting through large amounts of data in search of information that might be used for commercial purposes, for example, to target potential customers. Dating on the Internet – Involves using the Internet to find and make contact with other people for romantic purposes. The anonymity afforded by the Internet can make this a dangerous activity, however. Fake ID manufacture and sale with computers – Involves use of Internet technology to sell fake identification cards (e.g., drivers' licenses). These are often described by the online sales sites as “novelty” cards to avoid criminal liability for their sale. Gambling on the Internet – Involves wagering on sports events or games of chance. This activity often involves offshore sites and runs the risk of inauthentic practices that make the odds of winning (or being paid off) much less than they are at a physical casino or sports facility.

**Решение:** -6 приложение к учебнику: темы для обсуждения и эссе, не гемблинг

---

### 248 · R1531

**Not all traders gamble, but some gamblers trade: a latent class analysis of trading and gambling behaviors among retail investors.**

2025 · Public health · article, journal article, journalarticle · eng · https://doi.org/10.1016/j.puhe.2025.105742

OBJECTIVES: This study aimed to identify subgroups of retail investors based on their engagement in trading and gambling activities, and to examine differences in involvement, demographics, substance use, impulsivity, cognitive biases, problem gambling, and disordered trading. STUDY DESIGN: Cross-sectional, population-based study using panel data. Quota sampling and post-stratification weights were applied using data from a prior population-based random digital dial telephone survey. METHODS: Data were collected from 1,429 Spanish adults (aged 18-64). Participants reported involvement in trading of 8 financial instruments (e.g., cryptocurrencies, stocks, ETFs) and 12 gambling (e.g., lotteries, sports betting) and gambling-like activities (e.g., loot boxes, skin betting). 28.6 % of respondents engaged in non-professional trading. RESULTS: Using weighted latent class analysis we identified three distinct subgroups of retail investors: crypto-traders (52.4 %), focused on cryptocurrency trading with minimal gambling; stock-traders (32 %), involved in stocks/ETFs and lotteries, and gambling-traders (15.6 %), heavily involved in high-risk trading and various gambling activities. Although gambling-traders were not the highest investors in terms of trading volume, this class exhibited the highest frequency of trading and gambling, impulsivity, gambling-related cognitive biases, rates of disordered trading, and illicit substance use. 24.9 % of gambling-traders scored for problem gambling (PGSI≥8), compared to 0.5 % of crypto-traders and 3.5 % of stock-traders. CONCLUSIONS: Not all retail investors seem to extend their gambling behaviors to financial markets; however, those with higher impulsive traits and gambling-related cognitive biases tend to combine trading with gambling. This combination is strongly associated with problem gambling and disordered trading.

**Решение:** + количественное исследование розничных инвесторов и игроков, ставки на спорт, PGSI

---

### 249 · R2472

**Problem Gambling and Suicidal Behaviours in Young Adult men in Ghana: A Moderated Mediation Model of Psychological Distress and Social Support : Journal of Gambling Studies.**

2024 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-024-10305-7

Problem gambling has been recognised as an important public health issue because of its harmful consequences at the personal, interpersonal, and societal levels. There is a proliferation of gambling activities in Ghana owing to increased access to the internet, soaring smartphone penetration, and an influx of sports betting companies. Yet, very little research has addressed the harm associated with problem gambling in Ghana. This study assessed if the effect of problem gambling severity on suicidal behaviours (ideation, planning, and attempts) through psychological distress is contingent on the level of perceived social support. A total of 350 young adult men in the Greater Accra Region of Ghana provided the data for the current analysis. The data were analysed using a moderated mediation approach. The results showed that psychological distress is an important intervening mechanism through which problem gambling severity influences suicidality. In addition, the positive association between psychological distress and suicidal behaviours was found to be conditional on the levels of perceived social support. In other words, our results showed that problem gambling may first trigger episodes of psychological distress, which, in turn, can lead to suicidality among problem gamblers who report low to moderate levels of perceived social support. Our findings suggest that young adult problem gamblers require higher levels of social support from family, friends, and significant others to prevent those experiencing psychological distress from engaging in suicidal behaviours.

**Решение:** ? опрос молодых мужчин в Гане с измерением тяжести проблемной игры, проверить выделение ставок на спорт в полном тексте

---

### 250 · R6704

**Work Hard, Play Hard: a Qualitative Analysis of How Fantasy Sports Affect Organizational Commitment**

2013 · article · en

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -2 качественный анализ влияния фэнтези-спорта на организационную приверженность

---

### 251 · R8311

**从“彩票没有概率”说起—关于彩票概率的讨论**

2001 · 数学通报 · article · zh

历史上,概率论是从博弈问题的讨论发展起来的,现在概率在许多领域都有广泛的应用,其中包括彩票的问题,这是很显然的.本文想从概率论的角度对中国体育彩票概率问题作一点简单的分析,以澄清当前社会上彩票热中出现的各种说法,端正心态,防止彩票过热可能出现的弊病,并且让具有高中数学知识的读者重温代数中排列组合的应用.为了方便阅读,首先对中国体育彩票设计的中奖办法作一简要的说明.

**Решение:** -2 математический анализ вероятностей в лотерее

---

### 252 · R6168

**Prediktion av matchresultat i engelska Premier League**

2015 · KTH Publication Database DiVA (KTH Royal Institute of Technology) · bachelor thesis, dissertation · sv · http://urn.kb.se/resolve?urn=urn:nbn:se:umu:diva-107140

To predict a soccer game in advance is something that has been done by most people. If the prediction is the result of an advanced mathematical formula or just ha pure guess done on your favorite team is very different. Since the computer power in recent years has greatly improved the number of mathematical approaches has increased and it is especially the computational heavy models that have increased in number. In this thesis the Pi-rating system is used it gives each team a home and away rating that describe how good/bad they are compared to the average competing team. As an extension of the original Pi-rating model, in this thesis time series analysis is used to predict future values of the teams rating, three different methods are tested and they are simple moving average, simple exponential smoothing and an ARIMA-model. A solution to how new teams that did not play in the league last year should be handled is also suggested. Finally a breath discussion and test of different investment methods that can be applied on the final model to be used on the sport betting market. The results show that the greatest returns on the calibration data is achieved when Kelly’s formula is used as an investment method on an ARIMA(0,1,1)-model, but when this strategy is used outside calibration data, the result shows a very low profit and the method fails to give a stable long term return, which from an investment point of view is not desirable. The conclusion is that this method is not in itself good enough to provide a safe return but is a good foundation that can be expanded to take more factors into account, and then hopefully give bigger and more stable winnings. Att i förväg försöka förutsäga vilket lag som kommer vinna i en fotbollsmatch har nog de flesta försökt sig på någon gång. Att gissa och att faktiskt försöka att analysera båda lagens förutsättningar är två väldigt olika metoder att komma fram till sitt resultat. I och med att datorkraften de senaste åren kraftigt förbättrats har det också kommit fler och framför allt tyngre matematiska modeller för att skatta utfallet av matcher. I detta examensarbete används Pi-ratingsystemet som går ut på att varje lag får en rating för hur bra man är på hemma- respektive bortaplan. Som en utveckling av den ursprungliga Pi-rating modellen används det i detta arbete tre olika modeller för att prediktera lagens framtida rating. Modellerna som används är enkelt glidande medelvärde, enkel exponentiell utjämning och en ARIMA-modell. En lösning på hur nya lag som inte spelade i ligan föregående år ska behandlas föreslås också. Avslutningsvis diskuteras olika investeringsmetoder som kan användas för att använda resultat från modellerna på marknaden för vadslagning. Resultatet visar att en spelstrategi som utnyttjat Kellys formel ger störst avkastning för kalibreringsdatat. När denna strategi används på matcher utanför kalibreringsåren visar resultatet på en mycket låg vinst och framför allt att vinsten under lång tid är negativ, vilket från en investeringssyn inte är något man önskar. Sammanfattningsvis är denna metod inte i sig själv tillräckligt bra för att ge en säker avkastning men är en bra grund som kan byggas ut för att ta hänsyn till fler faktorer och då ge möjlighet till stabilare och mer långsiktiga vinster.

**Решение:** -2 модель прогнозирования результатов матчей английской Премьер-лиги

---

### 253 · R6582

**New and efficient conditional e-payment systems with transferability**

2013 · Future Generation Computer Systems · article, journalarticle · en · https://doi.org/10.1016/j.future.2013.07.015

Conditional e-payments (or e-cash) allow the user to anonymously cash a bank-issued e-coin at a future time if and only if a certain agreed-upon public condition is satisfied, which are useful in plenty of applications such as prediction markets, anonymous online betting, and securities trading. In this paper, we propose a new and efficient conditional e-payment system based on Chen etal.s restrictive partially blind signature scheme. Compared to the existing conditional e-payment schemes [2,5,6], our construction requires neither the inefficient cut-and-choose techniques nor the complicated knowledge proof protocols and thus has lower computation and communication complexity. Another significant contribution of this paper is a conditional e-payment system with transferability which allows the coin to be further transferred anonymously by a chain of payees. We propose a new conditional e-payment scheme with transferability.Our scheme allows the coin to be transferred anonymously by a chain of payees.Our scheme does not require inefficient cut-and-choose techniques.Our scheme has lower computation and communication complexity.

**Решение:** -6 криптографический протокол электронных платежей, не гемблинг

---

### 254 · R5635

**Bookmaker Margins and Favourite-Longshot Bias in Football Prediction Markets**

2017 · SSRN Electronic Journal · article, other literature type, preprint · en · https://doi.org/10.2139/ssrn.3035848

In this article we discuss bookmaker margins embedded in odds for "1X2" bets in the European football betting markets operated by bookmakers. Bookmaker margins are adjustments applied to fair odds, for the purpose of ensuring profits and compensation for risks undertaken, and to cover overall operational costs. They are observable on a per match basis as the excess of the sum of the reciprocals of odds over one, which is popularly referred to as overround. In this article we study the margins from a risk point of view. We derive the expression for the expected variance of a portfolio of bets, in order to study risk-based determinants of margins. Risk of a portfolio of bets is shown to be particularly sensitive to the presence of low probability bets (longshots). We propose a new, risk-based measure for quantifying balancedness of a match. Using this measure along with the standard entropy measure, we investigate variations of overrounds between matches of different levels of balancedness. Our analysis shows that there is no a convincing empirical evidence that overall overrounds are dependent on the match balancedness. Similarly, the study of variations of overrounds by the levels of disagreement in probabilities between different bookmakers, does not show any significant interdependence. On the other hand, our study confirms the pervasiveness of a well known Favourite-Longshot Bias (FLB) in the European football betting markets. The odds have been more favourable for bets on favourites than for longshots. These conclusions suggest that margins are determined on a match-per-match basis. Long odds on longshots are being adjusted more aggressively downwards than short odds on favourites, while overall margins are being kept roughly at bookmaker-specific target levels. Empirical studies were performed using the historical data on 116,150 football matches, containing results and odds from 13 major bookmakers. The data set covers 19 major European football divisions during the last 17 years. Using this rich and recent data set, we also investigated the time evolution of overall margins, and variations of margins between the different bookmakers and football divisions.

**Решение:** -2 маржа букмекеров и favourite-longshot bias в футбольных прогнозах

---

### 255 · R3666

**Odds analytics in sports betting**

2022 · Πανεπιστήμιο Πειραιώς · /, master thesis · el · https://doi.org/10.26267/unipi_dione/2134

Ο τζόγος αποτελεί μια από τις παλαιότερες δραστηριότητες της ανθρωπότητας, όπως αποδεικνύεται από διάφορα χειρόγραφα ανακαλύφθηκαν σε ιστορικούς χώρους σε όλο τον κόσμο. Αυτά περιλαμβάνουν παιχνίδια με ζάρια, παιχνίδια τράπουλας, λαχεία και στοιχήματα, με τα πρώτα να χρονολογούνται από το 3000 π.Χ. Τα τελευταία χρόνια, ο διαδικτυακός τζόγος έχει γίνει μια από τις μεγαλύτερες αγορές παγκοσμίως, φτάνοντας τα 57,54 δισεκατομμύρια δολάρια. Αυτό με τη σειρά του είχε ως αποτέλεσμα την ουσιαστική αλλαγή στη νομοθεσία και τις επιχειρηματικές στρατηγικές προκειμένου να προσεγγιστούν ακόμη περισσότεροι πελάτες. Ωστόσο, είναι σημαντικό να συνειδητοποιήσουμε ότι ο τζόγος – σε οποιαδήποτε μορφή – μπορεί επίσης να επιφέρει ανεπιθύμητα αποτελέσματα όπως εθισμό και χρηματικής απώλεια. Εδώ, παρουσιάζουμε μια μέθοδο για τη μεγιστοποίηση κερδών στο διαδίκτυο, υπολογίζοντας τις αποδόσεις και ελαχιστοποιώντας τη γκανιότα σε διάφορους ιστότοπους. Τα αποτελέσματά μας δείχνουν ότι – σε μεγάλο βαθμό – η γκανιότα μειώνεται ενώ τα κέρδη παραμένουν σταθερά τα τελευταία χρόνια. Δείχνουμε επίσης ότι το arbitrage συμβαίνει αρκετά συχνά, με πιθανότητα 1/7. Ελπίζουμε ότι παρέχοντας αυτά τα ευρήματα, μελλοντικοί χρήστες μπορούν να λάβουν πιο ενημερωμένες αποφάσεις σχετικά με τη στοιχηματική τους δραστηριότητά και να αποτρέψουν τις ανεπιθύμητες συνέπειες που προκύπτουν από τα διαδικτυακά παιχνίδια. Gambling is one of humanity’s oldest pastimes as evidenced by various manuscripts and artefacts discovered at historical sites across the world. These include dice games, card games, lottery tickets, and event betting, with the former dating back to 3000BC. In more recent times, online gambling has become one of the largest markets globally, reaching 57.54 billion dollars. This in turn has resulted in a substantial shift in legislation, logistics, and business strategies in order to reach even more clients. However, it is important to realize that gambling – whether physical or online – can also bring about undesirable outcomes in the form of addiction and monetary loss. Here, we demonstrate a method – through programming applications – for maximizing profits when betting online by calculating the odds and minimizing rake across various websites. Our results show that – largely – rake has been decreasing while profits remain stable across recent years; we also show that arbitrage can occur more reliably than generally believed, with a probability of 1/7 of total betting events. We hope that by providing these findings, future users can make more informed decisions regarding their gambling activity and prevent undesirable consequences stemming from online games.

**Решение:** -1 аналитический обзор методов аналитики коэффициентов в ставках

---

### 256 · R6101

**Mafias, sport et paris : les liaisons dangereuses**

2015 · Reflets et perspectives de la vie économique · article · fr · https://doi.org/10.3917/rpve.543.0013

La manipulation des compétitions sportives est le nouveau fléau qui menace la pérennité du sport professionnel à l’échelle mondiale. Phénomène encore méconnu du grand public, la menace des matchs truqués s’est affirmée brutalement avec l’explosion des paris sportifs et d’Internet, c’est-à-dire réellement il y a une petite dizaine d’années. Le sport n’a donc pas eu le temps d’anticiper et subit de plein fouet les conséquences de cette situation. Aujourd’hui, le Crime organisé utilise le sport et les paris comme un vecteur de diversification de ses activités traditionnelles, comme le trafic de stupéfiants, le racket et la prostitution. Les parades existent mais elles sont difficiles à mettre en œuvre dans un contexte international où les paradis de jeux et les intérêts privés imposent encore souvent leur loi. L’objet de cet article est de décrire, à travers un exemple concret, celui du « Calcioscommesse » en Italie, la complexité des affaires de trucage des compétitions sportives.

**Решение:** -1 аналитическая статья о договорных матчах и мафии в спорте

---

### 257 · R3994

**Victorian population gambling and health study (2018-19)**

2021 · Figshare · report, report/report · en · https://doi.org/10.25946/14842902

This report details results from a large general population survey on gambling participation, gambling problems and gambling-related harm in the state of Victoria Australia conducted between September 2018 and January 2019. The purpose of the survey is to inform future research, policy, treatment and prevention efforts. This survey aimed to distinguish itself from past gambling-prevalence surveys by adopting new methods and measures to better reflect a growing trend to explore gambling behaviour as a public health issue. Past prevalence surveys have had the principal purposes of understanding patterns and trends in gambling participation, including participation by product (e.g., casino games, sports betting, etc.), as well as producing a headline rate of problem gambling in the adult population; which is sometimes referred to as disordered gambling in clinical contexts. This survey was constructed for this purpose too, although it adds new elements that better align the investigation to the public health approach by virtue of considering gambling-harm in the community at large. Browne et al. (2016) produced a report on gambling-related harm in Victoria that found a large quantum of harm was being experienced by gamblers who were not likely diagnosable with the mental health condition of disordered gambling. This report provides a population-representative sample replicating these results, and providing estimates on how gambling-harms are distributed throughout the Victorian community.

**Решение:** + репрезентативный опрос населения штата Виктория о гемблинге и проблемной игре со ставками на спорт

---

### 258 · R0811

**SANAL KUMAR BAĞIMLILIĞINDA HARCAMA DAVRANIŞININ PSİKOLOJİSİ**

2026 · Bookarion Journal of Social Sciences · article · https://doi.org/10.64734/bjss.2-1-03

Çevrimiçi kumar platformlarının son on yılda gösterdiği hızlı büyüme, harcama davranışının psikolojik temellerinin yeniden incelenmesini zorunlu kılmaktadır. Bu derleme, sanal (çevrimiçi) kumar ortamlarının; bahis siteleri, sanal slot makineleri, canlı casino uygulamaları, spor bahis platformları ve oyun içi kumar benzeri mekanikler (loot box), bağımlılık yapıcı harcama davranışını hangi bilişsel, duygusal ve tasarımsal mekanizmalar aracılığıyla şekillendirdiğini güncel literatür (2013-2026 yılları arasında yayımlanmış 39 kaynak) temelinde ele almaktadır. Çalışma, kumar araştırmalarında geleneksel olarak kabul gören kişi-ürün-çevre üçlüsünden hareketle, sanal ortama özgü tasarım unsurlarının bu üçlüyü nasıl yeniden şekillendirdiğini tartışmaktadır. Bulgular; kayıp kovalama ve realizasyon etkisi, kontrol yanılsaması, alışkanlık oluşumu, görsel-işitsel ipuçlarının yarattığı daldırma (immersion) hissi ve platform/ürün tasarımının davranışsal ekonomiye dayalı unsurlarının harcama kararlarını sistematik biçimde etkilediğini göstermektedir. Ayrıca genç erkekler, üniversite öğrencileri, kadınlar ve oyun içi mikro-ödeme sistemlerine (loot box) maruz kalan gençler gibi risk gruplarının özgül savunmasızlıkları, kumar bozukluğunun psikiyatrik komorbiditesi ve intihar riskiyle ilişkisi tartışılmaktadır. Tarihsel süreklilik de ele alınarak, kumarın kurumsallaşmış hâlinden dijital ve mobil platformlara uzanan evrimi özetlenmektedir. Son bölümde önleme, çevrimiçi bilişsel-davranışçı tedavi yaklaşımları ve alanın metodolojik sınırlılıkları değerlendirilmekte, gelecek araştırmalara yönelik öneriler sunulmaktadır.

**Решение:** -1 обзор литературы по психологии трат в онлайн-гемблинге

---

### 259 · R1744

**Sports Betting And Gambling Problems Among University Student-Athletes**

2025 · Zenodo · article, journalarticle/ · und · https://doi.org/10.5281/zenodo.15663047

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? исследование проблемного гемблинга среди студентов-спортсменов, нет аннотации, проверить полный текст

---

### 260 · R8295

**Online Sports Gambling-Regulation or Prohibition?**

2001 · Journal of Legal Aspects of Sport · article, journal-article · en · https://doi.org/10.1123/jlas.11.2.99

may conceive to be injurious to the public health, morals, or welfare, even though the state has not sought to regulate their use" (Darby, p.114).Thus, there is case precedent that would enable Congress, where it so inclined, to pass legislation prohibiting all gambling activity.On the other hand, gambling proponents argue in favor of continuing to regulate gambling rather than enacting a federal law banning all Internet and/or sports gambling activity.The following section summarizes arguments made (a) in support of state or federal laws that would legalize but regulate these segments of the industry, and (b) in support of federal law seeking to prohibit such gambling activities.A.The case for legalization with governmental regulationOpponents of prohibition assert that an outright ban on sport and/or Internet gambling could simply encourage illegal gambling and other un-scrupulous activities.As stated by Frank Miller, the former director of the Washington State Gambling Commission and former president of the North American Gaming Regulators Association, "[o]ne might ask how it is possible to fashion an enforcement mechanism in an environment where prohibition will not work.The answer is, prohibition promotes unlawful activity, and regulation removes it" (Kailus, 1999(Kailus, , p.1045)).From this perspective, the government would be futilely at-tempting to prohibit an otherwise prosperous industry with great market demand.Six primary arguments support the case for legalizing online sports gambling in a regulated fashion.

**Решение:** -1 правовой анализ регулирования или запрета спортивных ставок

---

### 261 · R2681

**Aspectos de marketing que influyen en la motivación intrínseca y extrínseca para hacer apuestas online**

2024 · IROCAMM-International Review Of Communication And Marketing Mix · article · es · https://doi.org/10.12795/irocamm.2024.v07.i01.05

Las plataformas de apuestas deportivas en línea incursionaron en el mercado colombiano a partir del año 2017, obteniendo una alta aceptación por quienes son seguidores de algún deporte en específico. Su introducción estuvo acompañada de una estrategia de comunicación amplia en diferentes medios de comunicación. Esta investigación busca determinar los aspectos que influyen en la motivación intrínseca y extrínseca para hacer apuestas en línea. Para esto, se desarrolló un estudio descriptivo y se aplicó un cuestionario a 419 hombres entre los 18 y 40 años que realizan de forma periódica apuestas deportivas online. A partir de un análisis por medio de ecuaciones estructurales, los resultados sugieren que las estrategias publicitarias, las acciones de la marca en la página web o app y los aspectos para tener en cuenta al apostar influyen en la motivación intrínseca; mientras que las estrategias publicitarias, las acciones de la marca en la página web o app influyen en la motivación extrínseca. Esta investigación contribuye al mayor conocimiento de este fenómeno en el contexto latinoamericano y promueve el desarrollo de investigaciones futuras.

**Решение:** ? опрос 419 спортивных беттеров о мотивах ставок, проверить наличие инструмента PG в полном тексте

---

### 262 · R2799

**Gambling and COVID-19: Swedish national gambling data from a state-owned gambling sports and casino operator.**

2023 · Journal of behavioral addictions · article, other literature type, journal article · eng · https://doi.org/10.1556/2006.2022.00089

Abstract Background and aims The lockdown of sports and gambling venues during the coronavirus disease 2019 (COVID-19) pandemic caused a fear of increased gambling on other online gambling types, with a risk for transfer to more addictive gambling than otherwise. This study aimed to estimate changes in gambling activity during COVID-19-affected periods among all gamblers at a Swedish state-owned gambling operator and to analyse observable sex differences. Methods This study included gambling tracking data from the Swedish state-owned gambling operator Svenska Spel Sports &amp; Casino (sports betting, online bingo, casino and poker). All individuals ( n = 616,245) who gambled at least once from February 10 to July 19, 2020, were included. The study period was divided into four periods according to their expected level of COVID-19 impact on gambling opportunities: one pre-COVID period and three COVID-affected periods (sports cancellation, emerging return of sports, substantial return of sports). Results Sports betting experienced an apparent decrease, followed by a gradual normalization and an end level substantially below prepandemic levels. For online bingo, gambling levels increased upon sports interruption and then decreased with the return to normality in sports events but remained higher than baseline levels. We observed a similar trend for online poker during the interruption of sports, but with a lower level than baseline levels when sports events normalized. We noticed a trend favouring online casinos during the sports interruption period regarding gambling intensity but not wagering levels. Discussion and conclusions Dramatic changes in the content of the gambling market may divert some gamblers to other gambling types, but maintained effects could not be demonstrated.

**Решение:** -3 данные государственного игорного оператора без опросника проблемной игры

---

### 263 · R3216

**The Effect of the COVID-19 Pandemic on Sports Betting Tipsters as Professional Bettors: A Qualitative Interview Study**

2023 · Sustainability · article, journalarticle, journal-article · en · https://doi.org/10.3390/su15097729

Although the COVID-19 pandemic impacted individuals who bet on sports, sports betting tipsters (SBTs; i.e., individuals who provide professional tips on the outcome of sporting events) were arguably among the most affected groups. Consequently, the aim of the present study was to explore how SBTs in Turkey were affected by the COVID-19 pandemic, including alternate forms of gambling engagement (e.g., e-sports betting). Semi-structured interviews were conducted with 85 SBTs aged between 20 and 48 years. The data were analyzed using thematic analysis to identify common themes. Based on the qualitative analysis, four themes emerged: (i) the meaning and role of sports betting, (ii) the effects of the pandemic on life and sports betting, (iii) comparing e-sports betting vs. traditional sports betting, and (iv) possible sports betting behavior if the pandemic continues. SBTs reported experiencing psychological distress as a result of the COVID-19 pandemic’s cancellation of sporting events. More specifically, SBTs reported a sense of emptiness because of the lack of sports betting. Furthermore, SBT reported suffering a loss of income and turning to e-sports betting during the pandemic. However, the majority of SBTs did not find betting on e-sports as exciting as traditional betting but reported they would continue to engage in e-sports betting if traditional sports betting was not available. The findings of this study can contribute to a better understanding of the impact of SBTs on individuals and further provide practical implications for policymakers to promote a safe, sustainable, and long-term growth of the sports betting industry in Turkey.

**Решение:** -2 качественное исследование спортивных типстеров во время пандемии

---

### 264 · R3121

**40 years of legal sports betting in Australia points to risks for US gamblers – and tips for regulators**

2023 · The Conversation Media Group Ltd · article, other, posted-content · en · https://doi.org/10.64628/aai.wn75fx3qw

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 аналитический историко-правовой комментарий об опыте регулирования ставок в Австралии

---

### 265 · R4475

**BETTING INDUSTRY: IMPACT AND MOTIVATION**

2020 · RePEc: Research Papers in Economics · article · en · https://doaj.org/article/644efdabb0204b4ab78b14bc906a775b

In the European space as well as in Romania, the sports betting industry is a regulated one and has a major impact, whether we are talking about an economic impact, or a social or psychological one. Our intention was to observe the impact that this industry has on sports and fans. The aim of this article was to present some of the results of a quantitative research based on a sample of subjects who frequent bookmakers. We wanted to observe their behavior as fans and see if we can identify a common profile of the Romanian bettor in his relations with society, family and sport or his favorite team and also to observe the economic impact of the sports betting industry on sport.

**Решение:** ? количественный опрос румынских спортивных беттеров, проверить наличие инструмента PG в полном тексте

---

### 266 · R0881

**The Statistical Profitability of Social Media Sports Betting Influencers: Evidence from the Nigerian Market**

2026 · arXiv (Cornell University) · article, preprint, journalarticle · und · https://doi.org/10.48550/arxiv.2604.08251

This study examines whether following popular Nigerian sports betting influencers on social media is a financially sound strategy. To avoid the survivorship bias that occurs when influencers only share their winning bets, we tracked 5, 467 pre-match betting slips from three prominent tipsters on X (formerly Twitter) and Telegram. We verified the outcomes against official Stake.com records, resulting in a final dataset covering approximately $4.8 million in tracked bets. We analyzed raw performance, assessed risk based on odds sizes, and applied four common staking strategies (Flat, Inverse, Square Root, and Fixed Return) to simulate realistic follower outcomes. The results show a sharp contrast between the wealth these influencers display online and the actual financial results. The influencers themselves collectively lost 25.24% on their promoted bets, while a follower who staked the same amount on every tip would lose 38.27% on their investment. Across all tested strategies, following these influencers consistently led to significant financial losses. These findings raise serious consumer protection concerns in Nigeria's expanding gambling market.

**Решение:** -2 анализ доходности прогнозов типстеров в соцсетях без опроса людей

---

### 267 · R2677

**Analysis of Indonesian Intelligence as Transnational Crime of Football Gambling**

2024 · Eduvest - Journal Of Universal Studies · journalarticle, article · en · https://doi.org/10.59188/eduvest.v4i9.3795

Football gambling is a global phenomenon that not only impacts economic, but also social and legal aspects. As a sport that is very popular in the world, it does not rule out the possibility of the involvement of various parties from various countries in this crime, thus becoming a serious problem in the form of transnational crime. Gambling is an act that has been considered criminal according to various laws and regulations that apply in many countries in the world. In Indonesia, although gambling is prohibited, this practice remains widespread, especially through online platforms that are difficult to control by law enforcement officials. In Indonesia, gambling is considered an illegal act and is regulated in the Criminal Code (KUHP). Article 303 of the Criminal Code prohibits all forms of gambling and provides criminal sanctions for gambling offenders. This research aims to analyze Indonesia's vulnerability to the transnational crime of football gambling. This research uses a qualitative method by conducting in-depth analysis based on data and news found based on the theory of vulnerability in Indonesia. The results show that there are several main factors that increase Indonesia's vulnerability to transnational football gambling.

**Решение:** -1 криминологический анализ транснациональной преступности и футбольного тотализатора

---

### 268 · R5335

**Enhancing crowd wisdom using measures of diversity computed from social media data**

2017 · IEEE/WIC/ACM International Conference on Web Intelligence · article, conference object, other literature type · en · https://doi.org/10.1145/3106426.3106491

"Wisdom of Crowds" (WoC) refers to a form of collective intelligence in which the aggregate judgment of a group of individuals is, in most instances, superior to that of any one group member. For a crowd to be wise, its members must possess diverse knowledge and viewpoints. Such diversity leads to uncorrelated judgment errors that cancel out in aggregate. Yet despite the fact that diversity is known to be an essential ingredient in WoC, little research aims to measure and exploit diversity in human social systems for the purpose of maximizing crowd intelligence. Here we quantify the diversity of a group of individuals through semantic analysis of their social media (Twitter) communications. Focusing on the domain of fantasy sports, we show that virtual crowds of fantasy team owners selected based on the diversity of their tweet content can outperform both non-diverse and randomly sampled crowds. Our results suggest a new approach for intelligent crowd assembly in which measures of diversity extracted from online social media communications can guide the selection of crowd members. These results have implications for numerous domains that utilize aggregated judgments - from consumer reviews, to econometrics, to geopolitical forecasting and intelligence analysis.

**Решение:** -2 модель коллективного разума из твиттера для прогнозирования матчей без опроса людей

---

### 269 · R5246

**Social Media and Motivational Complexities Associated in Promoting Professional Soccer Engagement**

2018 · Advances in IT standards and standardization research (AISSR) book series/Advances in IT standards and standardization research series · part of book or chapter of book, book-chapter · en · https://doi.org/10.4018/978-1-5225-7214-5.ch014

The purpose of this chapter is to examine and determine factors that lead to increased television ratings for soccer in the U.S. Undoubtedly, the topic of fantasy sports and the various roles it plays with types of fan involvement and their need for enhanced engagement with a complex social media landscape has intrigued scholars from a number of disciplines. How the various motivational factors, both intrinsically and extrinsically, impact the degree of fan involvement and loyalty have been investigated several times. The overall results have been mixed to say the least. The current chapter primarily focuses on fantasy soccer participation, involvement in soccer, presence of a local professional team, and social media interaction. After providing a brief history of soccer television ratings in the U.S., a conceptual model based on these factors is developed and explained. The factors of this conceptual model are tested through statistical analysis.

**Решение:** -1 аналитическая глава книги о маркетинге и вовлечении болельщиков

---

### 270 · R0595

**Prevalence and Risk Factors of Addictive and Potentially Addictive Behaviors in Swiss Adults: A Population-Based Study**

2026 · Journal of General Internal Medicine · article · en · https://doi.org/10.1007/s11606-026-10371-0

BACKGROUND AND AIMS: Modern environments expose individuals to stimuli that may promote seemingly harmless, yet potentially addictive behaviors. This study investigated the prevalence, co-occurrence, and risk factors of substance and non-substance addictive behaviors in adults to better inform clinical practice and screening strategies. METHODS: Data were collected from the Specchio digital cohort in Geneva, Switzerland (2023-2024). Addictive and potentially addictive behaviors included smoking, recreational drug use, binge drinking, gambling, excessive leisure screen use, and sugar-sweetened beverage consumption. Analysis included post-stratified prevalence rates, sex- and age-adjusted logistic regression for risk factors, and upset plots for behavioral co-occurrence patterns. RESULTS: Among 4575 participants (mean age 52 years; 59.3% female), smoking had the highest prevalence (15.7%, 95% CI 14.0-17.5), followed by binge drinking (12.3%), gambling (9.9%), excessive screen time (9.7%), sugar-sweetened beverage consumption (9.6%), and recreational drug use (5.8%). While smoking alone was most common (21.1%), substance-related behaviors frequently co-occurred (4.3%). Males showed higher odds across all behaviors, particularly gambling (adjusted odds ratio (aOR) = 2.18, 95% CI 1.76-2.70), binge drinking (aOR = 2.10, 95% CI 1.73-2.55), and recreational drug use (aOR = 2.08, 95% CI 1.55-2.79). Socioeconomic disadvantage strongly correlated with gambling (aOR = 2.34, 95% CI 1.89-2.90) and sugar-sweetened beverage consumption (aOR = 1.83, 95% CI 1.41-2.37). Lower psychological well-being was significantly associated with excessive screen time (aOR = 1.79, 95% CI 1.36-2.36), sugar-sweetened beverage consumption (aOR = 1.46, 95% CI 1.01-2.13), and smoking (aOR = 1.43, 95% CI 1.20-1.71). CONCLUSIONS: This study reveals distinct patterns of addictive and potentially addictive behaviors and identifies key risk factors: male sex, lower socioeconomic status, and poor psychological well-being. These findings emphasize the need for targeted prevention strategies and systematic primary care screening, including for new potentially addictive behaviors such as screen time or the consumption of sugar-sweetened beverages.

**Решение:** ? когортный опрос населения о гемблинге, проверить наличие инструмента PG и выделение ставок на спорт в полном тексте

---

### 271 · R7527

**Market efficiency and the NHL totals betting market: Is there an under bias?**

2010 · Economics bulletin · article · en · http://www.accessecon.com/Pubs/EB/2010/Volume30/EB-10-V30-I4-P287.pdf

Sports betting and racetrack markets continue to be utilized by academic researchers to provide insights into theories relating to more complex speculative markets. Previous investigations have focused on testing the efficient markets hypotheses and behavioral biases of the participants. This paper investigates the market efficiency of the National Hockey League (NHL) goal totals over/under betting market. The market is found to be inefficient and simple wagering strategies are identified that result in profitable returns.

**Решение:** -2 эффективность рынка ставок на тоталы в НХЛ

---

### 272 · R8057

**Företagsvärdering : En fallstudie av Unibet**

2005 · Jonkoping University Library (Jönköping University) · dissertation · en

Problem: The online betting industry has erased the importance of national borders and opened up the world, which has lead to a more diversified perspective of the company. In this master thesis we wanted to broaden and develop the topic of corporate valuation with regard to the on-line gambling industry. In order to do that, a case study of the on-line betting firm Unibet and its core betting activities has been carried out. Purpose: The study aims to identify factors in the strategic, SWOT and financial analysis that will be used in the cash flow valuation model in order to derive the company value. Method: A case study has been chosen to collect empirical data to our study. Conclusion: A cash flow valuation in different scenarios was carried out. With the assumptions made in the “probable” scenario a value of approximately GBP 85 million was reached, which was significantly lower than the listed value. This is mainly due to the fact that we believe that the increased competition will make it difficult for Unibet to maintain its strong growth in sales in the future. The assumptions have been based on the information gained from the strategic analysis, the SWOT analysis and the development in financial ratios.

**Решение:** -2 корпоративная финансовая оценка компании Unibet

---

### 273 · R2381

**Match predictions in soccer: Machine learning vs. Poisson approaches**

2024 · arXiv (Cornell University) · article, part of book or chapter of book, preprint · en · https://doi.org/10.48550/arxiv.2408.08331

Predicting the results of soccer matches is of great interest. This is not only due to the popularity of the sport and the joy of private "betting rounds", but also due to the large sports betting market. Where previously expert knowledge and intuition were used, today there are models that analyze large amounts of data and make predictions based on them. In addition to Poisson models, approaches that belong to the machine learning (ML) category are increasingly being used. These include, for example, neural network or random forest models, which are compared in this article with each other as well as with Poisson models with regard to single-match prediction. In each case, the match results of a season are used as the data basis. The analysis is carried out for 5 European top leagues. A statistical analysis shows that the performance levels of the teams do not change systematically during a season. In order to characterize performance levels as accurately as possible, all match results, except from the match to be predicted, can be used as features with equal weighting. It can be seen that both, the exact choice of features and the choice of model, have only a minor influence on the prediction quality. Possible improvements in match prediction are discussed. 10 pages, 1 figure

**Решение:** -2 машинное обучение против пуассоновской модели для прогнозов футбола

---

### 274 · R1712

**Author response of: Impulsivity and online sports betting behavior: Untangling the causal relationship. Round#1**

2025 · Peer Community In Registered Reports · journalarticle, review, journal-article · en · https://doi.org/10.24072/pci.rr.100996.ar1

A recommendation of: Anne Jacob, Mohsen Joshanloo, Robert Czernecka, Anja Kräplin Impulsivity and online sports betting behavior: Untangling the causal relationship https://pada.psycharchives.org/bitstream/ed85321f-28e5-42dd-8f97-cf1cfce9e5d8

**Решение:** -1 рецензия / ответ авторов на зарегистрированный отчет

---

### 275 · R6798

**The Feasibility Research of the Issue of Chinese Super League Lottery In China**

2013 · Sports Research and Education · review, article · en

At present,the voice to the issuance of the super quizzes sports lottery is higher and higher from all walks of life.This paper elaborates the necessity and feasibility about the release of Chinese Super League lottery by the questionnaire survey method and literature.The problems met probably and how to construct the credibility of the Chinese Super League lottery were discussed in this research.The reasonable suggestions were put forward on designing reasonable methods of playing Chinese Super League lottery and changing the super league management mechanism in order to promote and protect our super sports lottery health issue.

**Решение:** -3 опрос о целесообразности выпуска лотереи Суперлиги Китая без инструмента PG

---

### 276 · R7757

**C.B.C. Distribution and Marketing, Inc., v. Major League Baseball Advanced Media, L.P., 505 F.3d 818 (8th Cir. 2007)**

2008 · International Journal of Sport Communication · article · en · https://doi.org/10.1123/ijsc.1.2.241

CBC Distribution and Marketing, Inc. (CBC), operator of CDMsports.com (CDM), offering fantasy-sports products and services, brought this action against Major League Baseball Advanced Media, L.P. (MLBAM), to establish its right to use without license the names and, inherently crucial for fantasy-sports operators, statistical records of Major League Baseball (MLB) players. MLBAM, the interactive media and Internet company of MLB, counterclaimed that CBC’s fantasy-baseball products violated MLB players’ rights of publicity, which were licensed through the MLB Players’ Association (MLBPA) to MLBAM. The MLBPA intervened in the suit, joining in MLBAM’s claims and further asserting a breach-of-contract claim against CBC. The district court granted summary judgment to CBC—see C.B.C. Distribution and Marketing, Inc. v. Major League Baseball Advanced Media, L.P., 443 F. Supp. 2d 1077 (E.D. Mo. 2006)—and MLBAM and the MLBPA appealed.

**Решение:** -1 юридический анализ судебного дела о правах на данные игроков в фэнтези-спорте

---

### 277 · R5013

**Why do some soccer bettors lose more money than others?**

2018 · Journal of Behavioral and Experimental Finance · article, journal-article · en · https://doi.org/10.1016/j.jbef.2018.01.010

Why do some soccer bettors lose more money than others? In an efficient prediction market, each gambler should break-even before costs (but losing a constant amount after costs, reflecting the bookmaker’s margin). Previous empirical studies across numerous sports betting markets show that bets on longshots tend to lose more than bets on favourites (favourite-longshot bias). We use 163,992 soccer odds from ten European leagues to test plausible hypotheses around why some soccer bettors lose more money than others. Are soccer bettors with above average losses simply biased, or are their losses driven by betting on events that are inherently unpredictable? We confirm the existence of favourite-longshot bias in soccer in this sample, but find another surprising feature of betting on longshots. As measured by the Brier score, bookmakers’ odds were better predictors of longshots than favourites, suggesting another potential channel whereby bettors’ preference for betting on longshots may cost them dearly.\ud \ud

**Решение:** -2 анализ 163992 букмекерских коэффициентов без опроса людей

---

### 278 · R7657

**An Analytic Recall of the Sports Lottery Legislation in China**

2009 · Journal of Hunan University of Commerce · article · en

Since 1994,sports lottery business has been developing very fast.Though we have made great achievements in this field,there are some problems like 4.20 Incident in Hubei province,and case of sports lottery in Shenzhen,which have aroused our attention and meditation.Certainly,many causes lead to the cases,among which the postponed legislation apparently blocks the development of it.Therefore,it’s necessary to give an analytic recall of the sports lottery legislation in the expectation of regularizing and standardizing the lottery market.

**Решение:** -1 правовой анализ законодательства о спортивной лотерее в Китае

---

### 279 · R6357

**Modelling prices of in-play football betting**

2014 · Lund University Publications Student Papers (Lund University) · other · en

Odds in sports betting can be seen as a price on a nancial contract. This Master thesis is a study of live odds in football matches. Movements and transactions in live odds from 1114 matches are investigated using a high frequency data set. The prices are then modeled using a Poisson distribution, and used to create a trading strategy.

**Решение:** -2 моделирование котировок лайв-ставок на футбол без опроса людей

---

### 280 · R0817

**Navigating the Impact of NIL on College Sports Betting**

2026 · Digital Scholarship - UNLV (University of Nevada Reno) · conference-paper

The study investigates whether U.S. college football betting markets have fully incorporated new financial disparities created by Name, Image, and Likeness (NIL) collective funding. After the 2021 policy changes that allowed athletes to earn from NIL deals, donor-backed collectives and subscription models rapidly emerged, giving some schools much stronger funding positions that can attract better talent. The core question is whether these funding gaps were accurately reflected in setting point spreads or whether there have been exploitable inefficiencies. Using data from 55 large public universities in the major conferences for the 2023–2024 seasons, we estimate collective funding from public revenue and contribution data and link it to game-level point spreads and results. Point spreads are strong predictors of outcomes, but funding ratios for home teams are also significant, especially when the home team is favored and the game is not at a neutral site. This implies that collective funding offers additional explanatory power beyond the line. Betting simulations show that visiting teams, particularly underdogs in games where the home team’s funding advantage is small or negative, outperform the spread at abnormal rates. We conclude that markets have not fully adjusted to the NIL-driven funding landscape, and that systematic use of collective funding information can identify profitable wagering opportunities, at least while NIL structures remain in flux.

**Решение:** -2 анализ влияния выплат спортсменам (NIL) на котировки студенческого футбола

---

### 281 · R0637

**Help-seeking for gambling problems following expansion of Ontario's online gambling market and legalization of single-event sports betting.**

2026 · CMAJ : Canadian Medical Association journal = journal de l'Association medicale canadienne · article, journal article, journalarticle · eng · https://doi.org/10.1503/cmaj.251894

BACKGROUND: Online gambling and sports betting have recently been legalized and expanded in North America. We aimed to evaluate long-term changes in the frequency of gambling-related helpline contacts in the province of Ontario following the launch of a government-operated online gambling platform (PlayOLG) in January 2015 and the expansion of private online gambling, including single-event sports betting, in April 2022. METHODS: We conducted an interrupted time-series analysis of contacts with Ontario's free 24-hour mental health and addictions helpline (ConnexOntario) between January 2012 and September 2025. We used segmented linear regression to compare immediate, gradual, and overall changes in monthly rates of gambling-related contacts after gambling expansion in January 2015 and April 2022 overall and by age and gender subgroups. RESULTS: Over 13 years, ConnexOntario received 745 716 contacts, including 37 087 (5.0%, mean age 39 yr, 68.2% men) related to gambling. The mean monthly rate of gambling-related contacts per 1 000 000 individuals aged 15 years and older was stable over time before the launch of PlayOLG (13.4); the rate increased after Play-OLG's launch (17.0) and further increased following privatization (26.2). Compared with the scenario in which PlayOLG never launched, the estimated effect was 9.3 (95% confidence interval [CI] 1.04 to 17.5) additional monthly contacts per million individuals aged 15 years and older in February 2022 (an approximately 80.7% increase). Compared with the scenario in which neither PlayOLG nor private online gambling was allowed, the estimated effect was 20.8 (95% CI 8.5 to 33.2) additional monthly contacts per million individuals aged 15 years and older in September 2025 (an approximately 198.3% increase). Increases in gambling-related contacts occurred almost exclusively in adolescent boys and men aged 15 to 44 years. Compared with no private online gambling, and no private online gambling or PlayOLG, gambling-related contacts in adolescent boys and men aged 15 to 24 years were estimated to have increased by 144% and 337.8%, respectively. INTERPRETATION: The introduction of online gambling and subsequent privatization with single-event sports betting were each associated with substantial increases in gambling-related helpline contacts, specifically in adolescent boys and young men, suggesting increased gambling problems, care-seeking, or both. This underscores the need to strengthen preventive measures and treatment access.

**Решение:** -5 выборка обратившихся за помощью на helpline по проблемному гемблингу

---

### 282 · R5516

**Implications of Sports Betting In Kenya: Impact of Robust Growth of the Sports Betting Industry**

2017 · dissertation · en

Project Report Submitted to the Chandaria School of Business in Partial Fulfillment of the Requirement for the Degree of Global Executive of Masters in Business Administration (GeMBA)

**Решение:** ? исследование последствий ставок на спорт в Кении, нет аннотации, проверить полный текст

---

### 283 · R6665

**Motion Synthesis for Sports Using Unobtrusive Lightweight Body‐Worn and Environment Sensing**

2013 · Computer Graphics Forum · article, journalarticle · en · https://doi.org/10.1111/cgf.12143

Abstract The ability to accurately achieve performance capture of athlete motion during competitive play in near real‐time promises to revolutionize not only broadcast sports graphics visualization and commentary, but also potentially performance analysis, sports medicine, fantasy sports and wagering. In this paper, we present a highly portable, non‐intrusive approach for synthesizing human athlete motion in competitive game‐play with lightweight instrumentation of both the athlete and field of play. Our data‐driven puppetry technique relies on a pre‐captured database of short segments of motion capture data to construct a motion graph augmented with interpolated motions and speed variations. An athlete's performed motion is synthesized by finding a related action sequence through the motion graph using a sparse set of measurements from the performance, acquired from both worn inertial and global location sensors. We demonstrate the efficacy of our approach in a challenging application scenario, with a high‐performance tennis athlete wearing one or more lightweight body‐worn accelerometers and a single overhead camera providing the athlete's global position and orientation data. However, the approach is flexible in both the number and variety of input sensor data used. The technique can also be adopted for searching a motion graph efficiently in linear time in alternative applications.

**Решение:** -6 компьютерная графика / синтез движений с датчиков, не гемблинг

---

### 284 · R1126

**From Murphy to Monopolies: Rethinking State Online Sports Betting Regulation**

2026 · Columbia Business Law Review · article, journalarticle, journal-article · und · https://doi.org/10.52214/cblr.v2025i2.14673

Since the Supreme Court’s decision in Murphy v. NCAA invalidated the Professional and Amateur Sports Protection Act, states have assumed exclusive authority over the regulation of sports betting. This decentralization has produced a highly fragmented regulatory landscape, particularly in the online sports betting market, where some states permit robust competition among numerous operators while others affirmatively sanction monopolies or highly concentrated markets. These state-level choices interact with an already concentrated national market dominated by DraftKings and FanDuel, creating significant variation in consumer choice, pricing, and regulatory outcomes across jurisdictions. This Note examines the sources and consequences of market power in online sports betting, distinguishing between naturally occurring national concentration and state-created intra-state market power. It situates state-sanctioned monopolies within the broader theoretical framework of “justified monopolies,” drawing comparisons to industries such as alcohol distribution, pharmaceuticals, telecommunications, and securities markets. Although proponents argue that monopolistic regulation can generate higher tax revenues, enhance consumer protection, and promote long-term innovation, this Note contends that online sports betting does not satisfy the conditions necessary to justify such market concentration. This Note argues that competitive online sports betting markets are better suited to advancing consumer welfare and regulatory goals than state-level monopolies. It further suggests that the current patchwork of state regimes risks distorting consumer behavior, reducing effective competition, and undermining potential gains from innovation. Drawing on the regulatory logic of Regulation National Market System in U.S. securities law, the Note proposes that competition—rather than state-imposed exclusivity—offers a more effective and adaptable framework for regulating online sports betting in the post-Murphy era.

**Решение:** -1 правовой анализ законов о монополиях в онлайн-ставках после отмены PASPA

---

### 285 · R0045

**Price Discovery Across Political Prediction Markets: Evidence From The 2024 U.S. Presidential Election**

2026 · SSRN Electronic Journal · preprint · https://doi.org/10.2139/ssrn.6624604

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 политические рынки предсказаний, нет ставок на спорт

---

### 286 · R6248

**Predictive power of fantasy sports data for soccer forecasting**

2015 · International Journal of Data Mining Modelling and Management · article, other literature type, journalarticle · en · https://doi.org/10.1504/ijdmmm.2015.069247

We analyse data from 5,000 competitors who participated in an online soccer managerial game which revolved around the English Premier League (EPL). We show that competitors incorporate into their decisions relevant information about the outcome of a soccer match. Furthermore, forecasts based on managerial game data are significantly better than random forecasts, forecasts based on relative frequency, and forecasts based on teams' attendance, but worse than bookmaker odds. Our work provides an evidence that crowds poses significant amount of information for the match outcome prediction.

**Решение:** -2 прогностическая способность данных фэнтези-спорта для футбольных прогнозов

---

### 287 · R5768

**Gambling, Saving, and Lumpy Expenditures: Sports Betting in Uganda (Final Report)**

2016 · eScholarship, University of California · article · und · https://escholarship.org/content/qt8jg73293/qt8jg73293.pdf

Demand for large and indivisible, or “lumpy”, expenditures creates need for liquid- ity. For people in developing countries, acquiring this liquidity often requires choosing among high-cost strategies. I conduct a study with 1,715 bettors in Kampala, Uganda, to show that sports betting is being used as an alternative to conventional liquidity generation strategies such as saving or credit. First, I document that, despite ex- pected losses of 35-50%, participants view betting as a likely source of liquidity for desired lumpy expenditures and use a natural experiment to show that this is not just cheap talk: winnings increase both the size and likelihood of making such expendi- tures. Second, I use a randomized field experiment to show that provision of a simple commitment-savings technology causes a 26% reduction in a revealed preference mea- sure of betting demand. I then conduct two lab-in-the-field experiments to isolate the role of betting as a mode of liquidity generation. Increasing the salience of a desired lumpy expenditure causes an increase in betting demand by 17.2%, and a budgeting exercise decreases betting demand by 34.9% for people who learn that they could save more than previously believed. Back-of-the-envelope calculations suggest that betting to create liquidity may be a rational response for people with low ability to save.

**Решение:** ? исследование 1715 спортивных беттеров в Уганде, проверить наличие инструмента PG в полном тексте

---

### 288 · R5095

**Applying Corporate Political Activity (CPA) analysis to Australian gambling industry submissions against regulation of television sports betting advertising.**

2018 · PloS one · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1371/journal.pone.0205654

AIMS: This research aimed to assess the application to the gambling industry, of Corporate Political Activity (CPA) analysis previously developed from public health research on tobacco industry interactions with political institutions and previously applied to the alcohol industry, but not the gambling industry. BACKGROUND: A growing body of literature has confirmed how public interest outcomes are frequently opposed by vested interests. This research focused on gambling industry submissions to a 2013 Australian Parliamentary inquiry into sports betting advertising. Gambling advertising became highly controversial following deregulation of sports betting advertising in Australia subsequent to the 2008 Australian High Court Betfair challenge. The dramatic increase in gambling advertising during sporting event broadcasts at children's viewing times and on new interactive technology, sparked public concerns. A series of national regulatory reviews followed and the gambling industry was actively involved in opposing further regulation. METHOD: The research used a corporate political activity (CPA) framework of analysis developed by UK tobacco public health researchers, which identified strategies and tactics used internationally by the tobacco industry, to broker pro-tobacco public policy outcomes. Testing the application of this CPA framework to gambling pro-industry strategies/tactics, this research focused on gambling industry submissions to the 2013 Australian Parliamentary Committee Inquiry. RESULTS: Like the tobacco industry, the research found the gambling industry used identified strategies and tactics, some new tactics and a new strategy of 'Corporate Social Responsibility', promoting 'responsible' industry practices and pre-emptive establishment of internal 'responsibility' units/practices. Despite public concerns regarding sports betting advertising, the gambling industry reinforced individual choice/blame for harms and claimed it acted responsibly. It did this using strategies identified in the tobacco industry CPA framework: information strategy (and shaping the evidence base); financial incentive strategy; constituency building strategy; policy substitution strategy; legal strategy; and constituency fragmentation and destabilization strategy. CONCLUSION: Similar to the CPA analysis applied to tobacco and alcohol industries, the research demonstrated the usefulness of the CPA taxonomy for analyzing and documenting pre-emptive industry policy strategies and tactics, exposing gambling industry efforts to maintain industry self-regulation via voluntary codes and avoid more government regulation. Cross-sectoral application of the framework signals great potential for use of CPA by policymakers and public health advocates as a tool in the analysis of corporate industry arguments/discourses.

**Решение:** -2 анализ документов и политической активности игорной индустрии без опроса людей

---

### 289 · R6892

**THE IMPACT OF SENTIMENT ON POINT SPREADS IN THE COLLEGE FOOTBALL WAGERING MARKET**

2012 · The Journal of Prediction Markets · article, journal-article · en · https://doi.org/10.5750/jpm.v2i1.433

This paper investigates whether sentimental bettors affect the point-spread-formation process in the college football wagering market, as well as whether this market is efficient. Following Avery and Chevalier (1999), this study focuses solely on sources of sentiment that have natural analogues in the stock market, such as predictions of so-called experts, momentum in teams’ performances, teams that are highly visible, and teams with high fan avidity. Sentiment relating to expert picks, even though the picks are uninformative, nonetheless is related to intraweek changes in spreads. Also, bettors’ sentiment for recent performance against the spread, for teams in major conferences, and for teams with high fan avidity appears to be related to spreads moving during the week. However, betting strategies designed to exploit any anticipated sentimental betting are marginally profitable at best, suggesting that rational arbitrageurs serve to correct most biases in spreads.The authors express thanks to Bruno Deschamps, Michael Hertzel, Michael Lemmon, J. Spencer Martin, Federico Nardari, Rodney Paul, and Mukunthan Santhanakrishnan for careful feedback and thoughtful suggestions. The authors are also grateful for comments from seminar participants at the UC Riverside Conference on Growth of Gambling and Prediction Markets, at the Financial Management Association meetings in Toronto, at Arizona State University, and at Montana State University. Greg Durham expresses a special thanks to Jim Harmon for providing historical data related to the Harmon Forecast. (The authors are responsible for any outstanding errors in this paper.)

**Решение:** -2 влияние сентимента на спреды на рынке ставок на студенческий футбол

---

### 290 · R7079

**“妙手”还是“恶手”？**

2012 · 围棋天地 · article · zh

近期，“围棋Toto”成为韩国棋界最热门的话题。各大围棋网站随处可以看到棋迷的争论，以及持各种观点的职业棋手公开表态。 所谓“围棋Toto”，就是围棋和体育博彩以一种正当的名义相结合的活动组织，就像大家所熟知的足球博彩。

**Решение:** -1 публицистический комментарий о введении тотализатора в го

---

### 291 · R2807

**Young Women Sports Bettors in the United Kingdom: An Overlooked Demographic?**

2023 · Emerald Group Publishing Limited eBooks · part of book or chapter of book, book-chapter · en · https://doi.org/10.1108/s1476-285420230000018010

Abstract Despite increasingly persuasive women-focused marketing of gambling products, there has only been limited investigation around women sports betting. Men remain the focus of much of the conversation about sports betting as they have generally been found to be the most active sports bettors and the most at risk of experiencing harms associated with their behaviour. This chapter aims to fill this gap by exploring the characteristics of young women sports bettors in the United Kingdom and the relationship between sports betting and the experience of gambling harms. To do this, we created two models of analysis. Our analysis is based on data from the first wave (2019) of the Emerging Adults Gambling Survey (EAGS) dataset (n = 3,549). The EAGS is a non-probability longitudinal survey that includes individuals between the ages of 16 and 24 who were residents in Britain at the time of data collection. Firstly, we examined the associations between women sports bettors and several factors identified as important predictors of sports betting. Secondly, we sought to understand the relationship between women's sports betting and the harms associated with this activity. From these models, we found that women's sports betting was most reliably predicted according to fandom and peer influence. We also found that women sports bettors were more at risk of experiencing harms associated with difficulties with family and friends than women gamblers using other products.

**Решение:** + количественное исследование молодых женщин, делающих ставки на спорт, n=3549, измерение вреда и проблемной игры

---

### 292 · R6792

**Slicing Big Data**

2013 · AoIR Selected Papers of Internet Research · article · en

Big Data presents many challenges related to volume, whether one is interested in studying past datasets or, even more problematically, attempting to work with live streams of data. The most obvious challenge, in a ‘noisy’ environment such as contemporary social media, is to collect the pertinent information; be that information for a specific study, tweets which can inform emergency services or other responders to an ongoing crisis, or give an advantage to those involved in prediction markets. Often, such a process is iterative, with keywords and hashtags changing with the passage of time, and both collection and analytic methodologies need to be continually adapted to respond to this changing information. While many of the data sets collected and analyzed are pre-formed, that is they are built around a particular keyword, hashtag, or set of authors, they still contain a large volume of information, much of which is unnecessary for the current purpose and/or potentially useful for future projects. Accordingly, this panel considers methods for separating and combining data to optimize big data research and report findings to stakeholders. The first paper considers possible coding mechanisms for incoming tweets during a crisis, taking a large stream of incoming tweets and selecting which of those need to be immediately placed in front of responders, for manual filtering and possible action. The paper suggests two solutions for this, content analysis and user profiling. In the former case, aspects of the tweet are assigned a score to assess its likely relationship to the topic at hand, and the urgency of the information, whilst the latter attempts to identify those users who are either serving as amplifiers of information or are known as an authoritative source. Through these techniques, the information contained in a large dataset could be filtered down to match the expected capacity of emergency responders, and knowledge as to the core keywords or hashtags relating to the current event is constantly refined for future data collection. The second paper is also concerned with identifying significant tweets, but in this case tweets relevant to particular prediction market; tennis betting. As increasing numbers of professional sports men and women create Twitter accounts to communicate with their fans, information is being shared regarding injuries, form and emotions which have the potential to impact on future results. As has already been demonstrated with leading US sports, such information is extremely valuable. Tennis, as with American Football (NFL) and Baseball (MLB) has paid subscription services which manually filter incoming news sources, including tweets, for information valuable to gamblers, gambling operators, and fantasy sports players. However, whilst such services are still niche operations, much of the value of information is lost by the time it reaches one of these services. The paper thus considers how information could be filtered from twitter user lists and hash tag or keyword monitoring, assessing the value of the source, information, and the prediction markets to which it may relate. The third paper examines methods for collecting Twitter data and following changes in an ongoing, dynamic social movement, such as the Occupy Wall Street movement. It involves the development of technical infrastructure to collect and make the tweets available for exploration and analysis. A strategy to respond to changes in the social movement is also required or the resulting tweets will only reflect the discussions and strategies the movement used at the time the keyword list is created — in a way, keyword creation is part strategy and part art. In this paper we describe strategies for the creation of a social media archive, specifically tweets related to the Occupy Wall Street movement, and methods for continuing to adapt data collection strategies as the movement’s presence in Twitter changes over time. We also discuss the opportunities and methods to extract data smaller slices of data from an archive of social media data to support a multitude of research projects in multiple fields of study. The common theme amongst these papers is that of constructing a data set, filtering it for a specific purpose, and then using the resulting information to aid in future data collection. The intention is that through the papers presented, and subsequent discussion, the panel will inform the wider research community not only on the objectives and limitations of data collection, live analytics, and filtering, but also on current and in-development methodologies that could be adopted by those working with such datasets, and how such approaches could be customized depending on the project stakeholders.

**Решение:** -6 методология работы с большими данными твиттера, не гемблинг

---

### 293 · R2665

**Seniors and Gambling**

2024 · Elsevier BV · posted-content, preprint · en · https://doi.org/10.2139/ssrn.4770475

Online sports gambling is increasing at a rapid pace. This is due to changes in the law allowing online betting, the prolific increase of online platforms, and aggressive marketing campaigns. Sports betting is legal in 38 states and Washington, D.C. as of March 2024. The elderly population is especially at risk for this platform as they do not need to leave their homes.

**Решение:** -1 аналитический комментарий об уязвимости пожилых людей перед ставками

---

### 294 · R1574

**The Perceptions and Receptiveness to Responsible Gambling by College Men who Sports Bet: A Focus Group Study**

2025 · UNLV Gaming Research & Review Journal · journalarticle, article · en · https://doi.org/10.9741/2327-8455.1501

Responsible Gambling (RG) includes prevention messages aimed at mitigating harms. Research examining the experiences of college students who sports bet is lacking, hindering efforts to tailor messaging to college students. This qualitative study explored how college men who sports bet perceive and respond to existing RG messages, gathering their feedback on the characteristics of messages they find effective. Online focus groups were conducted with college men who sports bet (N = 12) using a semi-structured interview guide. The discussions were recorded, transcribed, and analyzed using an open coding Thematic Analysis approach. Codes were independently identified and analyzed resulting in 12 sub-themes that were consolidated into 4 primary themes. Themes included 1) stakeholder perspectives on RG such as their conceptualization of RG, 2) acknowledgment of RG including their awareness of RG, 3) reproval of operator practices and RG messaging through their negative perceptions and insufficient sentiments of existing RG, and 4) desired RG messaging improvements including through personalized feedback. The findings provide valuable insights into the views of college men who sports bet regarding RG messages, offering guidance for developing more effective and tailored RG strategies for this demographic.

**Решение:** -2 качественное фокус-групповое исследование восприятия ответственной игры студентами

---

### 295 · R1211

**Australia’s proposed gambling reforms may be good for industry, but not for public health**

2026 · Health Promotion International · article · en · https://doi.org/10.1093/heapro/daag057

Gambling industry harms are a major global public health concern (Van Schalkwyk et al. 2021, Thomas et al. 2023a, Cowlishaw et al. 2025). They contribute to financial hardship, family violence, relationship breakdown, and, in severe cases, suicide (Marionneau et al. 2023). The rapid expansion of online betting and the embedding of gambling within sport and digital environments have intensified exposure and normalized participation (Forrest 2025, Mcgrane et al. 2025, Yeola et al. 2025). Central to this normalization are pervasive marketing systems that saturate everyday media and cultural environments (Pitt et al. 2024, McCarthy et al. 2026). These strategies consistently associate gambling with excitement, mateship, and sporting identity, reframing a high-risk product as an ordinary leisure activity (Coffey et al. 2026). Digital platforms and data-driven marketing extend this reach globally, while ‘dark nudges’ and inducement marketing amplify risks and harms (Mcgarrigle et al. 2026). Evidence shows that early and repeated exposure positively shapes gambling attitudes and promotes gambling as a normalized behaviour for young people (Nyemcsok et al. 2021, Thomas et al. 2023b, Royce et al. 2025). Despite this evidence, regulatory responses continue to prioritize industry interests over public health (Thomas et al. 2023a). Few jurisdictions have implemented comprehensive reforms explicitly aimed at protecting young people from commercial gambling practices (Constandt and De Jans 2024, Aonso-Diego et al. 2025). Most policy responses remain fragmented, incremental, and are arguably shaped through ongoing negotiation with industry actors (Van Schalkwyk and Cassidy 2024, Van Schalkwyk and Cassidy 2025). Even where major public inquiries have called for evidence-based reform, governments have failed to act (Thomas et al. 2023b). The Australian Government’s recent response to a comprehensive parliamentary inquiry into online gambling exemplifies this pattern, presented as significant progress but falling short of the structural reform required to address the drivers of harm. In 2022, growing concern about the normalization of gambling, especially through sport, prompted a cross party parliamentary inquiry into online gambling in Australia, chaired by the late Peta Murphy MP (Standing Committee on Social Policy and Legal Affairs 2022). Referred by the Minister for Social Services, the inquiry in the House of Representatives examined the full scope of online gambling—from products and advertising to regulation and support services. Its terms of reference were broadened early to adopt more inclusive, non-stigmatising language, shifting from ‘problem gamblers’ to ‘lived experience of gambling harm’. The inquiry received 161 submissions and 26 exhibits, and held 13 public hearings with a range of stakeholders, including the gambling industry, broadcasters, sporting codes, health organizations, academics and those with lived experience of gambling harm (together with some family members) (Standing Committee on Social Policy and Legal Affairs 2022). The resulting report ‘You win some, you lose more: Online gambling and its impacts on those experiencing gambling harm’ (which became widely known as the ‘Murphy Report’) set out a comprehensive suite of public health recommendations to prevent gambling harm (Standing Committee on Social Policy and Legal Affairs 2023). The 31 recommendations of the report included a phased in complete tobacco style ban on gambling advertising; a national regulator focused on harm reduction; stronger consumer protection measures such as banning inducements; and formal recognition of gambling as a public health issue. The Murphy Report quickly became a focal point for advocacy, with researchers, lived experience experts, politicians and the media drawing on its findings to call for meaningful online gambling reform (Cannane 2025, Daniel 2025, Australian Medical Association 2026, Pocock 2026). It also triggered pushback from groups with vested interests, who mobilized against key recommendations particularly in relation to the report’s recommendation for a full, phased in advertising ban. Industry stakeholders argued that tighter regulation would drive consumers to offshore and illegal gambling markets (Responsible Wagering Australia 2025), undermine the viability of free-to-air television (Free TV Australia 2023), and affect funding for grassroots and professional sport (Baum 2023). The Australian Government's response to the inquiry was due within six months (Chaney 2026). However, sustained delays and the absence of a substantive response drew criticism over industry influence, reliance on unevidenced statistics, and repeated appeals of ‘complexity’ to justify inaction (Cannane 2024b, Barlow 2026). On 2 April 2026, more than 1000 days after the release of the Murphy Report, the Government finally responded, announcing its planned reforms on the Thursday before the Easter long weekend—when media and political scrutiny are typically reduced, and amid intense media focus on escalating tensions with Iran. While claiming ‘strong action to protect Australians, particularly children and young people, from the harms of gambling’, the response fell short of the Murphy Report’s 31 recommendations, instead advancing a range of partial and individual responsibility measures (Prime Minister of Australia 2026). These included reducing television advertising caps (from 8 to 3 ads per hour between 6 am and 8.30 pm), restricted radio advertising during school drop-off and pick-up times, removal of gambling promotions from sports uniforms and stadiums, bans on celebrities and athletes appearing in advertising, and limits on digital gambling advertising unless users were logged in, over 18, and able to opt out of marketing. Importantly, these measures still need to progress through the parliamentary legislative process, where they will continue to face parliamentary scrutiny and stakeholder pressure. The Government has sought to present its position as signalling action and a step forward. But the measures involved also carry the hallmarks of political compromise, and avoidance of direct confrontation with powerful commercial actors who derive substantial revenue from gambling advertising and sponsorship. Arguing that ‘the solutions aren’t always just to ban things’ and that the Government had ‘got it right,’ the Prime Minister presented the reforms as a measured response to competing public expectations—one that preserved the ability to ‘have a punt’ while offering opt-out protections for those who wished to avoid exposure to marketing (Barlow 2026). In subsequent media interviews, senior government ministers stated that ‘pressure was brought to bear from all sides’ (Barlow 2026), highlighting the contested political environment in which the decisions were made and the influence of the views of those with political access. After reviewing the evidence, the Murphy Report concluded that ‘partial bans on gambling advertising do not work.’ (Standing Committee on Social Policy and Legal Affairs 2023, iv). By taking a partial approach, the Australian Government signalled its willingness to preserve large segments of the gambling marketing ecosystem, sustaining the industry’s capacity to promote its products in highly visible and sophisticated ways. The advertising ‘cap’ continues to normalize and legitimise gambling, and there is no clear evidence that the 8.30 pm cut off accurately reflects young peoples’ media viewing patterns, with studies showing that they continue to watch television after this time (Thomas et al. 2018, Cannane 2024a). Crucially, rather than reducing exposure to advertising, partial bans simply continue and redistribute it. In a context where gambling is already embedded across sport, media, and digital environments, limiting select channels will not meaningfully reduce overall exposure. By targeting only certain forms of advertising (and even those in a limited manner), the proposed reforms risk accelerating a shift to less visible, less regulated tactics. Tobacco control provides a clear precedent. Partial bans drove the expansion of special offers, creative packaging, and other forms of indirect promotion that proved just as influential as traditional advertising (Henriksen 2012, Ling et al. 2022). These risks are amplified in contemporary marketing environments. While the Australian reforms restrict some advertising and introduce opt-out mechanisms, some of the industry’s most powerful marketing tools are left untouched, such as influencer marketing which is highly appealing to young people (Pitt et al. 2024); algorithmic targeting (Parker et al. 2024); and inducements (linked to increased uptake and riskier betting) (Ó Ceallaigh et al. 2025). We can predict that marketing spend will also shift into less regulated spaces—such as podcasts which are widely consumed by younger audiences, and are increasingly attractive to advertisers (Taylor 2024; Brooks et al. 2022). Host-read promotions in podcasts also blur the line between content and advertising, carrying heightened persuasive influence, and are difficult to opt out from (Moe 2023, Wang and Chan-Olmsted 2024). On the basis of experience from this and other areas, we can safely predict that there will be further innovative approaches to marketing. More broadly, while framed as protective, measures such as online opt-outs and logged-in advertising restrictions shift responsibility onto individuals to manage exposure. These approaches are constrained by the complexity and limited transparency of digital advertising systems, which may reduce their capacity to meaningfully limit exposure (Goodwin 2022). Partial bans must be understood within the political economy that shapes regulatory decision making. Despite strong evidence and broad support for full implementation of the Murphy Report, the Government’s response reflects political compromise, raising serious concerns about the role of vested interests in shaping outcomes on major public health issues. As the literature on the commercial determinants of health demonstrates, harmful industries seek to actively shape policies to protect and extend their market power (Hawkins et al. 2012, Herzog-Hawelka and Gupta 2023, Miller et al. 2023, Watts et al. 2023). In this context, partial bans are not simply weak policies, they can indicate regulatory capture, creating the appearance of meaningful intervention while leaving the underlying drivers of harm intact. Indeed, by complying with limited restrictions, industries can also position themselves as part of the solution to the problems that they have caused. Such measures risk stabilizing and legitimizing harmful systems, compounded by the Government’s failure to follow the Murphy Report’s recommendation to establish a National Regulator with ‘the sole purpose of reducing harm and with responsibility for all licencing and regulation’ (Standing Committee on Social Policy and Legal Affairs 2023, xix). Effective reform requires comprehensive restrictions and strong, independent oversight. Without both, regulation remains fragmented, weak, and vulnerable to industry influence. The Murphy Report has been widely recognised as a comprehensive, evidence-based blueprint for preventing online gambling harm. The recommendations from the report have been backed by sustained advocacy from politicians, public health experts, and community groups, alongside strong public support for decisive action to protect children and young people. Meaningful gambling reform is both justified and expected. The Government’s delayed and partial response to the report should be the stimulus for further pressure and accountability for gambling reform. Limited advertising restrictions combined with the refusal to establish a National Regulator leave critical gaps that industry can readily exploit. This approach risks a familiar public health failure—when regulation lags behind industry innovation, harm persists. Without comprehensive reform, advertising will continue, and gambling will continue to be normalized for young people. Anything less than full implementation of the recommendations of the Murphy Report allows the problem to evolve faster than the policy designed to address it. None declared. S.T. has received funding for gambling research from the Australian Research Council, Victorian Responsible Gambling Foundation, VicHealth, Healthway, NSW Office of Responsible Gambling, Department of Social Services, ACT Gambling and Racing Commission, Healthway, and Deakin University. She holds the position of Editor-in-Chief for Health Promotion International. H.P. has received funding for gambling research from the Australian Research Council, Victorian Responsible Gambling Foundation, VicHealth, NSW Office of Responsible Gambling, Department of Social Services, ACT Gambling and Racing Commission, and Deakin University. She is a member of the Editorial Board for Health Promotion International. S.M. has received funding for gambling research from the Victorian Responsible Gambling Foundation, VicHealth, Department of Social Services, ACT Gambling and Racing Commission, and Deakin University. She is the social media coordinator for Health Promotion International. M.D. has received funding for gambling research from the Australian Research Council, Victorian Responsible Gambling Foundation, Healthway, ACT Gambling and Racing Commission. He is the Chair of the Editorial Boards for Health Promotion International.

**Решение:** -1 экспертный комментарий о реформах регулирования гемблинга в Австралии

---

### 296 · R3862

**Developing a Simulated Microcosm of a Contemporary Betting Exchange for the Discovery of Transferable and Profitable Algorithmic Betting Strategies**

2021 · Social Science Research Network · article, other literature type, preprint · en · https://doi.org/10.2139/ssrn.3879677

Since the dotcom boom of the early 2000s the betting industry has been transformed by the rise of betting exchanges, from a market dominated solely by traditional bookmakers, to one in which punters have a variety of wagering options. These exchanges bring together populations of bettors with varying and opposing views in the same way as traditional exchanges operating within the world's major financial markets. As a result the rise of algorithmic trading within the financial markets has been similarly observed within betting markets. The design and implementation of new financial trading algorithms is an arduous task due to the difficulty in obtaining high-quality data that can be used to evaluate a strategies' performance. As such Synthetic Data Generators (SGDs), such as Cliff's Bristol Stock Exchange (2012), have been developed to provide a test-bed in which researchers can develop trading algorithms and investigate market dynamics. This thesis therefore describes the design, implementation, and subsequent evaluation, of a novel asynchronous implementation of the Bristol Betting Exchange (BBE), the rationale and high-level design of which can be found in Cliff 2021. BBE provides an agent-based simulation model of a contemporary sports-betting exchange which will enable both researchers and industrial users to develop algorithmic betting agents and investigate previously unexplored betting market dynamics.

**Решение:** -2 компьютерная симуляция микроструктуры биржи ставок

---

### 297 · R8151

**西南地区“体育彩票杯”钓赛鸣锣**

2004 · 钓鱼 · article · ja

由贵州省钓鱼十办会主办的“体育彩票杯“西南地区钓鱼邀请赛于6月25—27日在贵州省贵阳市举行，来自重庆、四川、云南、广西和贵州的40支代表队120人参加了比赛，这是贵州历年来规模最大的一次地区性钓鱼比赛。经过激烈拼搏，龙王恨贵阳钓鱼俱乐部一队勇夺团体冠军，四川能汇队、四川先锋队、四川雅安一队、贵州遵义一队、贵阳海霸渔具行队获团体第2-6名，张明鑫、彭小光、查必清分获手竿钓鲫鱼、手竿钓混合鱼、抛竿钓三个赛项的第一名。

**Решение:** -6 новостная заметка о соревнованиях по спортивной рыбалке, не гемблинг

---

### 298 · R5729

**Wygrane w grach hazardowych w polskim podatku dochodowym od osób fizycznych**

2016 · Roczniki Nauk Prawnych · article · pl · https://doi.org/10.18290/rnp.2016.26.2-3

Charging income tax on winnings from gambling games is one of the most frequently used forms of deriving income from gambling by the state and local government units, with very diverse solutions applied in this respect. In Poland, the taxation of winnings mostly depends on the country in which games are organised – i.e. whether it is a European Union Member State, a State of the European Economic Area or a different State. The other criterion behind the amount of the tax burden is a type of game in which the winnings were obtained. Although more and more people make a stable profit from online gambling, mainly poker and sport wagering, tax law regulations do not differentiate, however, between the tax situation of professional and occasional players.

**Решение:** -1 юридический анализ налогообложения выигрышей в азартных играх в Польше

---

### 299 · R3992

**Graded Exposure Therapy for Online Mobile Smartphone Sports Betting Addiction: A Case Series Report.**

2021 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-021-10006-5

Advances in technology and increased usage of electronic mobile devices over the past decade have changed the way gamblers engage with online gambling. The convenience of mobile electronic devices is understood to be a major contributor to the increase of online gambling, which in turn has been implicated in the growth of sports betting. Emerging evidence suggests several sources of differentiation between mobile and other online gambling, which have important psychological implications. Given the inherent differences, we cannot conclude that evidence for the effectiveness of treatment for non-smartphone problem gambling (PG) automatically translates to online smartphone sports betting PG. The aim of this study, therefore, was to describe the feasibility and preliminary effectiveness of cue exposure therapy (CET) to treat individuals presenting to a community-based PG therapy service with an online smartphone sports betting addiction, using a case series design. Six men (21-42 years old) received up to 10 weekly 60-min manualised CET sessions. Outcome measures were gambling harm, gambling urge, gambling cognitions, psychological distress, and functional impairment. All six participants completed a course of CET averaging 8.33 sessions (SD = 1.75) and reported improvement across each of the outcome measures. Psychological distress scores had reduced to the non-clinical range for all six participants and five participants scored below the cut offs for PG and functional impairment at 1 month follow up. The findings provide preliminary proof of concept evidence for the feasibility and efficacy of CET for online smartphone sports betting addiction.

**Решение:** -5 клиническая серия случаев терапии зависимости от мобильных спортивных ставок

---

### 300 · R4044

**Gambling and military Service: Characteristics, comorbidity, and problem severity in an epidemiological sample.**

2021 · Addictive behaviors · article, journal article, journalarticle · eng · https://doi.org/10.1016/j.addbeh.2020.106725

Active military members and veterans both show elevated risk of Gambling Disorder. However, research comparing these groups to civilians in epidemiological samples is sparse. There is also some research suggesting that there is a stronger association between military service and poor mental outcomes for women. The current study applies bivariate analyses and generalized linear modelling predicting Problem Gambling Severity Index scores to a representative, complex survey sample of 2176 New Jersey adult residents. The results show that problem gambling scores for past and current military service members were more than double that of the civilian participants after controlling for relevant demographic and behavioral characteristics. Additionally, the relationship between problem gambling scores and military service was significantly stronger for women than men. Bivariate analyses indicated that active military service members scored higher on the Problem Gambling Severity Index, indicated greater weekly participation in online gambling, lottery, electronic gambling machine, and sports betting, and nearly 20 times the rate of suicidal ideation compared with civilians. Additional regression analysis show that among military service members problem gambling scores were associated with suicidal ideation, tobacco use, and substance use problems. The results are discussed in the context of a period of expansion of online gambling opportunities. Constrained options for leisure coupled with the high propensity for risk taking among military service members and the relative ease of concealing online gambling on base may expose military service members to disproportionately higher risk of Gambling Disorder.

**Решение:** + репрезентативный опрос 2176 жителей с оценкой PGSI и ставок на спорт у военных и гражданских
