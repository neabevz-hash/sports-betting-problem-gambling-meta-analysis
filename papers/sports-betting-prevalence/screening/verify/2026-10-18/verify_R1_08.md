# Проверка с метками ИИ, часть 8

Записи 1051–1200 из 1525, с метками обеих моделей над строкой решения. Модели согласны и вы тоже — поставьте `=`; иначе свой код (`+`, `?` или `-`, причина не нужна). Если модели разошлись, `=` не годится — нужен ваш код. Решаете вы.

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

### 1051 · R5531

**4th International Conference on Behavioral Addictions February 20-22, 2017 Haifa, Israel.**

2017 · Journal of Behavioral Addictions · journalarticle · https://doi.org/10.1556/jba.6.2017.suppl.1

While concerns about online gambling behavior exist, the involved psychological mechanisms and playing patterns across digital media and locations remain unclear. This study provides information from a nationally representative sample of 1841 adult Belgian respondents. Theoretically, the study contributes by introducing the concept of habit strength as a predictor of gambling behavior. Habit strength is viewed as complementary to gambling predictors that are derived from the Theory of Planned Behavior. Structural equation modeling indicates that both habit strength and perceived friend/family gambling behavior (norms) were associated with online gambling intent, which in turn contributed to an increase in problem gambling. Moreover, habit strength predicted problem gambling both directly and indirectly via intent to play online or spend over 20 Euro. Results further show that online gambling is quite prevalent, but that gambling applications differ in their digital and physical location pattern. For example, sports betting is often done via mobile devices. This study shows that complementary concepts from communications research (habit) and public health (theory of planned behavior) can be used to successfully predict gambling behavior. The relationship between online gambling and problem gambling indicates a need for policy makers and researchers to consider harm reduction in this new online environment.

**ИИ:** + · обе модели · опрос населения об азартных играх · Conference abstract: nationally representative Belgian survey (n=1841) measuring problem gambling and gambling activities, including sports betting.

**Решение:** =

---

### 1052 · R5551

**Youth Gambling Related Problems and Perception of Parental Behaviour**

2017

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; a youth gambling problems survey could measure sports betting and problem gambling.

**Решение:** =

---

### 1053 · R5560

**Introduction**

2017 · Edward Elgar Publishing · part of book or chapter of book · und · https://doi.org/10.4337/9781785364556.00006

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: Introduction chapter of an Edward Elgar edited book, with no abstract; almost certainly not an empirical survey.); Sonnet ? (нет аннотации: Book chapter "Introduction" (Edward Elgar, 2017) with no abstract; title is uninformative, likely an edited-volume introduction, but the topic can't be determined.)

**Решение:** -

---

### 1054 · R5561

**Examining the Role of (Un)Conscious Determinants in Online Gambling: Complementing the Theory of Planned Behavior With the Concept of Habit**

2017 · Research portal (Tilburg University) · conference-paper · en

While concerns about online gambling behavior exist, the involved psychological mechanisms and playing patterns across digital media and locations remain unclear. This study provides information from a nationally representative sample of 1841 adult Belgian respondents. Theoretically, the study contributes by introducing the concept of habit strength as a predictor of gambling behavior. Habit strength is viewed as complementary to gambling predictors that are derived from the Theory of Planned Behavior. Structural equation modeling indicates that both habit strength and perceived friend/family gambling behavior (norms) were associated with online gambling intent, which in turn contributed to an increase in problem gambling. Moreover, habit strength predicted problem gambling both directly and indirectly via intent to play online or spend over 20 Euro. Results further show that online gambling is quite prevalent, but that gambling applications differ in their digital and physical location pattern. For example, sports betting is often done via mobile devices. This study shows that complementary concepts from communications research (habit) and public health (theory of planned behavior) can be used to successfully predict gambling behavior. The relationship between online gambling and problem gambling indicates a need for policy makers and researchers to consider harm reduction in this new online environment.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Nationally representative Belgian sample; measured problem gambling and gambling activities including sports betting.

**Решение:** =

---

### 1055 · R5581

**Don ’ t Tell Me What To Do ! An Examination of Consumer Reactance to Daily Fantasy Sport Regulatory Restrictions**

2017

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Probably a survey of daily fantasy sports players' reactions to regulation; no abstract, so problem-gambling measurement can't be ruled out.

**Решение:** =

---

### 1056 · R5593

**Public attitudes towards gambling product harm and harm reduction strategies: an online study of 16-88 year olds in Victoria, Australia.**

2017 · Harm reduction journal · article, journal article, case-report · eng · https://doi.org/10.1186/s12954-017-0173-y

BACKGROUND: Gambling has quickly emerged as an important global public health issue. With new technologies used to develop high intensity gambling products and promotions aimed at driving consumption, public health organisations and researchers, community groups, and politicians have argued for a range of regulatory and education measures aimed at reducing gambling harm. However, there has been limited research seeking to understand community perceptions of the harms associated with gambling products and environments, and the level of community support for strategies designed to prevent and reduce gambling harm. METHODS: An online study of 500 adolescents and adults (aged 16 and over) was conducted with a representative sample (by age and gender) of individuals who were current residents in the state of Victoria, Australia. Participants were asked a range of questions about their own gambling behaviours, with the Problem Gambling Severity Index (PGSI) used as a measure of problem gambling. Participants were asked about their perceptions of harms associated with electronic gambling machines (EGMs), sports betting, horse betting, and casino gambling. They were also asked about the extent to which they agreed or disagreed with gambling harm reduction strategies related to marketing and promotions, restrictions on gambling products and venues, and public education campaigns. Quantitative data were analysed using descriptive statistics and paired t tests, with thematic analysis used to interpret qualitative responses to open-ended questionnaire items. RESULTS: More than one third (n = 201, 40.2%) of participants were at risk of experiencing some level of harm from gambling (PGSI ≥ 1), with 83 participants (16.6%) recording scores that indicated problem gambling (PGSI ≥ 8). One in five participants gambled on EGMs at least monthly (n = 100, 20.0%). Those who gambled on sports did so frequently, with nearly 1 in 5 gambling on sport at least once a month (n = 87, 17.4%). Over half of the sample rated casino gambling and EGMs as very harmful, while one third rated these forms of gambling as extremely harmful. Over one third of the sample rated horse and sports betting as very harmful, with one in five rating these products as extremely harmful. There was strong agreement with the need to ban gambling advertising during children's viewing hours, during sporting matches and at sporting venues. The majority of participants agreed with reducing and restricting EGMs, and providing more public education for both adults and children about the negative consequences from gambling. CONCLUSIONS: The findings suggest a strong perception in the Victorian community that gambling products are harmful. While governments have been reluctant to implement a comprehensive approach to reducing gambling harm, this study reveals significant community support for a range of harm reduction and prevention measures associated with gambling products. Public health practitioners can use this evidence in advocating for a comprehensive public health approach to reducing the harms associated with gambling promotions and products.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Representative online survey of Victorians that measured PGSI and sports betting frequency; PG among sports bettors may be reportable.

**Решение:** =

---

### 1057 · R5610

**Gender differences among adolescent gamblers**

2017 · Personality and Individual Differences · article · en · https://doi.org/10.1016/j.paid.2017.12.031

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; an adolescent gambler survey could have measured sports betting and problem gambling.

**Решение:** =

---

### 1058 · R5611

**A New Player in the Game: Examining Differences in Motives and Consumption between Traditional, Hybrid, and Daily Fantasy Sport Users**

2017 · Sport Marketing Quarterly · article, journalarticle, journal-article · en · https://doi.org/10.1177/106169341702600303

Due in part to a $200 million advertising campaign, daily fantasy sport (DFS) participation exploded in 2015 With faster payouts and unlimited lineup options, the activity has added to an already thriving fantasy sports industry However, little is known about the distinct attitudes and behaviors that drive DFS participants The current study examined 511 participants who played DFS-only, traditional, season-long fantasy football (TFS), and those who played both activities for motive and behavioral differences Results indicated statistically significant motive scores differences across the groups as it relates to the factors of gambling, social interaction , and competition while escape and entertainment scores showed no difference Media consumption differences were also found between the groups as those who played DFS in any form consumed more traditional broadcast and new media.

**ИИ:** разошлись — Opus -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: A sport-marketing survey of DFS and traditional fantasy players covering motives and media use only; it gives no sign of a problem-gambling instrument.); Sonnet ? (неясно, измеряли ли проблемную игру: DFS player survey (n=511) on motives and consumption; abstract doesn't mention a problem-gambling instrument, though one may have been used as a covariate.)

**Решение:** ?

---

### 1059 · R5624

**Entity Sports Betting and the Future of Gambling as Recreation**

2017 · article · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: No abstract. The title reads like a conceptual piece, but empirical sports betting data can't be ruled out.); Sonnet -1 (обзор, комментарий, теоретическая, правовая или регуляторная работа: Title suggests a legal/policy or commentary piece on sports betting's future; no abstract, likely not empirical.)

**Решение:** ?

---

### 1060 · R5631

**Povezanost problematičnog kockanja mladih i njihovog doživljaja roditeljskog ponašanja**

2017 · University of Zagreb. University of Zagreb, Faculty of Education and Rehabilitation Sciences · master thesis, dissertation · hr · https://www.bib.irb.hr/885011

Temeljni je cilj ovog diplomskog rada istražiti postoje li razlike u percepciji obitelji i roditeljskog ponašanja s obzirom na razinu izraženosti problema povezanih s kockanjem. Specifični ciljevi su istražiti koje aktivnosti kockanja prevladavaju kod mladih i u kojoj su mjeri razvili štetne psihosocijalne posljedice, utvrditi postojanje rodne razlike u učestalosti kockanja i razvoju štetnih psihosocijalnih posljedica, kao i utvrditi doživljaj atmosfere u obitelji kod mladića, te njihovu procjenu roditeljskog ponašanja. U okviru znanstveno-istraživačkog projekta "Roditeljska percepcija kockanja mladih", čije se aktivnosti provode na Edukacijsko-rehabilitacijskom fakultetu u sklopu šireg projekta "Kockanje mladih u Hrvatskoj", pod voditeljstvom izv.prof.dr.sc. Nevena Ricijaša, provedeno je istraživanje na kojem se temelji ovaj diplomski rad. Sudjelovanje u istraživanju bilo je dobrovoljno i anonimno, a provedeno je na uzorku od ukupno 1061 učenika od prvog do završnog razreda različitih srednjoškolskih usmjerenja, iz dva najveća hrvatska grada - Zagreba i Splita. Raspon dobi sudionika kreće se od 14 do 20 godina, a njihova prosječna dob iznosi Mdob=16,18 godina (SD=1,214). Za ostvarenje postavljenih ciljeva korišten je instrumentarij koji se sastoji od Upitnika o općim i sociodemografskim podacima, Skale kvalitete obiteljskih interakcija - KOBI, Upitnika roditeljskog ponašanja - URP29, Upitnika aktivnosti kockanja te Ukupne mjere ozbiljnosti problema povezanih s kockanjem (General Problem Severity Subscale-GPSS), kao dio Kanadskog upitnika kockanja mladih (Canadian Adolescent Gambling Inventory- CAGI) Rezultati istraživanja pokazali su da mladi u velikoj mjeri kockaju, s time da najviše igraju sportske kladionice i lutrijske igre, te da je značajan dio njih razvio probleme povezane s kockanjem. Što se tiče obitelji, pokazalo se da mladići doživljavaju atmosferu u svojoj obitelji pozitivnom te pozitivno procjenjuju roditeljsko ponašanje. U ispitivanju razlika, pokazalo se da ne postoje statistički značajne razlike u doživljaju atmosfere u vlastitoj obitelji kod mladića, s obzirom na izraženost problema povezanih s kockanjem. Međutim, kod ispitivanja razlika u procjeni roditeljskog ponašanja, rezultati ukazuju da mladići koji su razvili ozbiljne posljedice povezane s kockanjem procjenjuju manje roditeljske podrške od strane majke, te više restriktivne kontrole kod oba roditelja, u usporedbi s onim mladićima koji nisu razvili probleme povezane s kockanjem. Roditeljsko ponašanje ispitivalo se kroz tri dimenzije koje uključuju roditeljsku podršku, restriktivnu kontrolu i popustljivost. Provedeno istraživanje nije pokazalo statistički značajne razlike na dimenziji popustljivosti između mladića, s obzirom na izraženost problema povezanih s kockanjem. The main aim of this study was to determine the differences in perception of family and parental behavior amongst male adolescents who experienced problem gambling and the ones who haven't. Specific goals were to investigate which gambling activities are most common amongst youth and the development of harmful psychosocial consequences, explore possible gender differences, and determine male adolescents perception of their family and parental behaviour. The research is a part of study "Parental Perception of Youth Gambling", whose activities are being carried out by the Faculty of Education and Rehabilitation, within the wider project "Youth gambling in Croatia". Leader of this project is Neven Ricijaš, PhD. Participation in this study was completely anonymous and voluntary. The research was conducted on a sample of 1061 students from various high schools in two largest cities in Croatia - Zagreb and Split. The age range of participants ranges from 14-19 years, with an average age 16,18. To acomplish the main aims of this study, instruments that have been used are: A questionnare of basic sociodemographic characteristcs, The Quality of Family Interaction Scale, Parental Behaviour Questionnaire, Gambling Activity Questionnaire and General Problem Severity Subscale-GPSS, as a part of the Canadian Adolescent Gambling Inventory (CAGI) The results showed that adolescents gamble to a great extent, with the most frequent games being sports betting and lottery games. Furthermore, a significant amount of them developed gambling related issues. Regarding family, results showed that male adolescents positively assess their family and parenting behavior. When it comes to differences between male adolescents who experienced problem gambling and the ones who haven't, results show that there are no statistically significant differences in their perception of family. However, when we talk about differences in parental behavior, the results indicate that male adolescents who have developed serious gambling related problems, evaluate less parental suport from their mothers and more restrictive control from both of their parents. Parental behavior was examined through three dimensions th

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Croatian high-school survey (n=1061) that measured gambling activities, sports betting most common, and problem gambling with the CAGI GPSS.

**Решение:** =

---

### 1061 · R5632

**Les paris sportifs, un jeu d’enfants**

2017 · article · fr

Les paris sportifs attirent de plus en plus un public jeune, parfois mineur. Le manque de controle sur l’acces aux jeux et le matraquage publicitaire ...

**ИИ:** ? · обе модели · другое · French article on young people and minors betting on sports; the abstract is cut off, so it may be commentary or a survey.

**Решение:** =

---

### 1062 · R5633

**Economic Recession Affects Gambling Participation But Not Problematic Gambling: Results from a Population-Based Follow-up Study**

2017 · Frontiers in Psychology · article · en · https://doi.org/10.3389/fpsyg.2017.01247

In October 2008, Iceland experienced the fastest and deepest financial crisis recorded in modern times when all three major banks went bankrupt in less than 2 weeks. The purpose of this follow-up study is to examine potential changes in participation in 12 different gambling types and in problem gambling before (time 1; year 2007) and after (time 2; year 2011) the economic collapse in 2008. The time between the first and second wave of data collection was 3.5 years. In total, 1,531 participants took part in the study, 688 males and 843 females. There was a considerable increase in past year gambling behavior from 2007 to 2011, mostly due to increased participation in lotto (National lotto and Viking lotto) but also in bingo, monthly lotteries (class lotteries with at least monthly draw) and scratch tickets. Only EGMs (electronic gaming machines) participation declined significantly between the two timepoints. Examining past year problematic gambling figures revealed that there were no changes in the prevalence figures between the year 2007 (1.2%) and 2011 (1.1%). Further examination revealed that those who reported financial difficulties due to the recession were more likely to buy lotto- or scratch tickets during the recession than those who were not financially affected by the crisis. These findings remained after controlling for background variables and baseline gambling activity (gambling in 2007). Overall, the findings of the follow-up study suggest that when people are experiencing financial difficulties during economic recessions, the possibility to improve their financial situation by winning large jackpots with low initial stakes becomes more enticing.

**ИИ:** + · обе модели · опрос населения об азартных играх · Icelandic population-based survey measured 12 gambling types, likely including sports betting, and problem gambling prevalence.

**Решение:** =

---

### 1063 · R5638

**남자 중·고등학생의 불법 스포츠도박 실태 조사**

2017 · review

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Korean survey of illegal sports gambling among male secondary students; no abstract, so problem-gambling measurement unknown.

**Решение:** =

---

### 1064 · R5639

**A Study on Social Structural Approach for problem solving of Korean Sports Gambling Addiction**

2017 · Journal of Education & Culture · article, journal-article · en · https://doi.org/10.24159/joec.2017.23.5.63

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; title on Korean sports gambling addiction may be conceptual, but an empirical survey can't be ruled out.

**Решение:** =

---

### 1065 · R5640

**남자 중 · 고등학생의 불법 스포츠도박 실태 조사**

2017 · article · ko

The purpose of the study was to investigate the status quo of the illegal sport gambling of male middle and high school students. To collect data, a survey with 719 middle and high school was conducted in Seoul, Kyeonggi province, and Chungnam province. The survey was to investigate subjects experiences on illegal gambling, gambling experiences, irrational gambling belief, sport participation, experience of exercise gambling, and tendency of exercise gambling addiction. The results show that first, 3.5% of middle and high school have been involved in illegal sport gambling, and 12.0% of them plan to continue to regain the losses. Second, there was a difference in type of gambling experiences of high school students, and the motive of the gambling was to make money. Students who experienced illegal gambling have more irrational gambling belief than those who have no experiences. Third, sport participation of those who experienced has no difference than those who have no experience in Fourth, with gambling experiences have higher exercise betting experiences than those who are without gambling experiences. Exercise betting tendency was higher than those with illegal gambling experiences. In sum, male middle and high school students illegal gambling involvement does not seem to be different with gamblers involvement. Therefore, it is highly possible that students gambling continues to adult gambling. In this regard, it is necessary for schools and families to educate the with gambling addiction not to be involved in gambling, and fundamentally reinforcement on the rules handling students gambling participation is needed to prevent gambling problems.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of 719 male students on illegal sports gambling; it measured gambling addiction tendency, but the instrument isn't named.

**Решение:** =

---

### 1066 · R5651

**PART IV. THE INSTITUTIONAL PERSPECTIVE**

2016 · Lexington Books · part of book or chapter of book · und · https://doi.org/10.5771/9781498504898-215

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: Section heading of an edited book with no abstract; it is a part divider, not a quantitative study of bettors.); Sonnet ? (нет аннотации: Book part title only ("Institutional Perspective"), no abstract; likely a policy/institutional chapter but content unknown, so cannot confirm exclusion.)

**Решение:** -

---

### 1067 · R5652

**PART V. FOR THE LOVE OF THE FANTASY GAME**

2016 · Lexington Books · part of book or chapter of book · und · https://doi.org/10.5771/9781498504898-255

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Book section on fantasy sports with no abstract; it might contain surveys of fantasy players, but problem gambling measurement is unknown.

**Решение:** =

---

### 1068 · R5656

**The demand for sports lottery in Ghana (a case study of the Kumasi Metropolis)**

2016

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; probably an economic demand study, but it may have surveyed sports lottery players in Kumasi. Problem gambling measurement unknown.

**Решение:** =

---

### 1069 · R5657

**The Demand For Sports Lottery: Evidence from the City of Kumasi in Ghana**

2016 · The Journal of Gambling Business and Economics · article, journal-article · en · https://doi.org/10.5750/jgbe.v10i2.1173

Formalised sports lottery is fast becoming a craze in Ghana, especially amongst the male populace. There is however no documented research on the demand for this product as well as its effects on the population and economy of Ghana as a whole. This study sought to investigate the factors that influence the demand for sports lottery in Ghana. Based on the expected utility hypothesis, a model was constructed using a binary logistic regression to analyse the characteristics that influence the demand for sports lottery in Ghana. Four hundred respondents were employed in this study where it was realized that 92% out of the about 96% males engaged in sports lottery in Ghana were within the age bracket of 21-40 years. Furthermore, 53.6% of those engaged in sports lottery were reported to be unemployed. Price, gender, age, employment status, monthly income and whether a person has won a bet before were discovered to be significant factors of the demand for sports lottery in Ghana. The study also realized that online lotteries were such as MyBet and Supabet were the most preferred to the offline lottery offered by the National Lottery Authority. Therefore the NLA must redesign their product to meet the demand preferences of the patrons.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Survey of 400 sports lottery/online betting participants in Ghana on demand factors; abstract does not say whether problem gambling was measured.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Survey of 400 respondents on sports lottery demand drivers in Ghana; no problem-gambling instrument is mentioned, only demand factors like price, income and age.)

**Решение:** ?

---

### 1070 · R5658

**FANS WHO BET AGAINST THEIR FAVORITE TEAMS 2 An Investigation of Highly Identified Fans Who Bet Against their Favorite Teams Highlights**

2016 · review

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; title suggests an empirical study of sports bettors, but it is unclear whether problem gambling was measured.

**Решение:** =

---

### 1071 · R5665

**Sportwetten im Stargames Casino**

2016 · article · de

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the title suggests an operator or promotional piece about sports betting at an online casino, but this can't be confirmed.

**Решение:** =

---

### 1072 · R5666

**An Explanation of Sports Betting among Students of Rasht Universities from the Perspective of Akers Social Learning Theory**

2016 · article · en

The main objective of this paper is to explain the process of engagement of individuals in sports betting. Hence, the hypotheses were tested by collecting the necessary data through distributing questionnaires among a sample of 272 students of the universities of the city of Rasht. The Akers theory of social learning was applied. The findings of the study indicate that there is a significant negative correlation between aspects of social learning theory, i.e. differential association, differential reinforcements, imitation and definition and consumption level and inclination towards sports betting of the respondents. Also the regression model of the research showed that the conceptual aspects of the social learning theory can predict 0.41 of variations of consumption level of sports betting and 0.47 percent of variations of inclination towards sports betting. Also the respondents who are engaged in betting in extreme and pathological forms have received higher level of social and environmental impacts compared to the occasional professional gamblers and non-gamblers. In general, The findings of this research indicate that the level of participation of students in betting activities and the level of their tendency towards such activities take place in the social milieu and any change in the behavioral patterns stemming from social context in the first place requires introduction of suitable cultural patterns and in the second place it needs preventive and supportive programs for the target groups.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Student survey on sports betting that classifies "pathological" bettors; unclear whether a validated problem-gambling instrument was used.

**Решение:** =

---

### 1073 · R5675

**Is There A Relationship between Participation in Gambling Activities and Participation in High-Risk Stock Trading?**

2016 · The Journal of Gambling Business and Economics · article · en · https://doi.org/10.5750/jgbe.v9i3.1034

The purpose of the present study was to investigate whether or not there is an association between engaging in traditional forms of gambling and engaging in high-risk stock trading and, if so, to examine game play patterns of high-risk stock traders, as well as identify any socio-demographic similarities or differences between the two groups. Logistic regressions on data from two large Canadian data sets were undertaken to examine which variables best differentiate traditional gamblers from high-risk stock traders. The results indicate that high-risk stock traders have a higher frequency of gambling, engage in a larger range of gambling activities, and are more likely to be problem gamblers. Additionally, the type of gambling activities that high-risk stock traders participate in suggests that they are a sub-group of skill-based gamblers who also prefer gambling on casino table games, sports betting, dog and horse race betting, and games of skill for money over chance based games such as electronic gaming machines, bingo, and instant win tickets. High-risk stock traders, compared to traditional gamblers were more likely to be male, have a higher income, be better educated, and to be of Asian or “other” descent, not be divorced, widowed or separated, and be self-employed or employed full-time. However, unlike other skill-based gamblers, high-risk stock traders tended to be older rather than younger, and had a high income rather than a low income.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Two large Canadian gambling datasets measuring participation by activity, including sports betting, and problem gambling status; full text may cross-tabulate.

**Решение:** =

---

### 1074 · R5676

**Gambling disorders, gambling type preferences, and psychiatric comorbidity among the Thai general population: Results of the 2013 National Mental Health Survey**

2016 · Journal of Behavioral Addictions · article · en · https://doi.org/10.1556/2006.5.2016.066

Background and aims To estimate the prevalence of problem and pathological gambling, gender and age-group differences in gambling types, and comorbidities with other psychiatric disorders among the Thai general population. Methods Analysis was conducted on 4,727 participants of Thailand's 2013 National Mental Health Survey, a multistage stratified cluster survey, using the Composite International Diagnostic Interview. Diagnoses of problem and pathological gambling and other psychiatric disorders were based on the DSM-IV-TR criteria with the following additional criteria for gamblers: more than 10 lifetime gambling episodes and a single year loss of at least 365 USD from gambling. Results The estimated lifetime prevalence rates of pathological and problem gambling were 0.90% [95% confidence interval (CI): 0.51-1.29] and 1.14% (95% CI: 0.58-1.70), respectively. The most popular type of gambling was playing lotteries [69.5%, standard error (SE) = 1.9], the prevalence of which was significantly higher among females and older age groups. The most common psychiatric disorders seen among pathological gamblers were alcohol abuse (57.4%), nicotine dependence (49.5%), and any drug use disorder (16.2%). Pathological gambling was highly prevalent among those who ever experienced major depressive episodes (5.5%), any drug dependence (5.1%), and intermittent explosive disorder (4.8%). The association between pathological gambling was strongest with a history of major depressive episode [adjusted odds ratio (AOR) = 10.4, 95% CI: 2.80-38.4]. Conclusion The study confirms the recognition of gambling disorders as a public health concern in Thailand and suggests a need for culturally specific preventive measures for pathological gamblers and those with a history of substance use disorders or major depression.

**ИИ:** + · обе модели · опрос населения об азартных играх · Thai national survey using CIDI DSM-IV problem/pathological gambling diagnoses plus gambling type preferences; football betting likely among the types.

**Решение:** =

---

### 1075 · R5677

**CGA Research Summit: 2016 Research**

2016 · Canadian Gaming Association · external research report, other literature type, other/technical report · en · https://doi.org/10.11575/prism/33088

The overall objective of this research was to provide insight into how Canadian casinos can improve the overall offer to not only keep their current visitors returning, but to also appeal to those who are not currently visiting. Includes: Section A. Casino Attitudes and Participation; Section B. Lottery Participation; Section C. Barrier and Motivators Analysis; Section D. Slot Play; Section E. Future State of Casinos; Section F. Sports Betting an Betting Landscape and Future State.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Industry consumer survey that includes a sports betting section; the abstract does not say whether a problem-gambling instrument was used.

**Решение:** =

---

### 1076 · R5678

**A DÖNTÉSEK LÉLEKTANÁNAK BEMUTATÁSA EGY LABDARÚGÓ TIPPJÁTÉK PÉLDÁJÁN KERESZTÜL = THE PSYCHOLOGY OF DECISION MAKING THROUGH A SOCCER BETTING GAME**

2016 · Repository of the Academy's Library (Library of the Hungarian Academy of Sciences) · article · hu · https://doi.org/10.18531/studia.mundi.2016.03.02.26-44

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: No abstract; Hungarian study of decision-making in a soccer betting game. Unclear whether real-money betting or a PG measure was involved.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Hungarian paper using a soccer tipping game to illustrate decision-making psychology; it is unlikely to measure problem gambling or report prevalence among bettors.)

**Решение:** ?

---

### 1077 · R5683

**Fantasy Gaming on Steroids? Contrasting Fantasy Sport Participation by Daily Fantasy Sport Participation**

2016 · Communication & Sport · article, journalarticle, review · en · https://doi.org/10.1177/2167479516644445

The fantasy sport industry has grown rapidly in the past decade, now boasting 56 million participants in North America alone. More recently, the ascent of fantasy sport appears directly attributable to the rise of new websites offering daily/weekly fantasy games. This study surveys 438 fantasy participants—some who play traditional fantasy sports and others who participate in daily fantasy sports along with traditional forms of fantasy offerings. Results reveal that motivations for play do not differ between traditional and daily participants, yet the two sets of respondents differed in terms of media consumption, economic commitment, and perceptions of games being skill versus chance based. Ramifications are offered not only based on the differences in financial investment but also regarding the seeming downturn in motivations for traditional fantasy sport participation.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of 438 daily fantasy sports players focused on motives, media use and spending; abstract doesn't say whether problem gambling was measured.

**Решение:** =

---

### 1078 · R5686

**UK FOBT RESEARCH 2007 BRITISH GAMBLING PREVALENCE SURVEY SECONDARY STUDY**

2016 · review

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Secondary analysis of 2007 BGPS (measured activities and PGSI/DSM-IV); FOBT focus, but may report problem gambling by activity.

**Решение:** =

---

### 1079 · R5694

**Fantasy sports and the changing sports media industry: Media, players, and society**

2016 · article · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; media-focused fantasy sports volume, chapters might include player surveys with gambling measures, though unlikely.

**Решение:** =

---

### 1080 · R5700

**Problem gambling and the five‐factor model of personality: a large population‐based study**

2016 · Addiction · article · en · https://doi.org/10.1111/add.13388

BACKGROUND AND AIMS: Knowledge of the personality characteristics of individuals who develop gambling problems is important for designing targeted prevention efforts. Previous studies of the relationship between the five-factor model of personality and gambling problems were based on small samples not representative of the general population. We estimated differences in neuroticism, extroversion, intellect, agreeableness and conscientiousness between non-problem gamblers and individuals with low, moderate and severe gambling problems. DESIGN: Cross-sectional survey. SETTING: Norway. PARTICIPANTS: A total of 10 081 (51.5% female) individuals aged 16-74 years (mean age 46.5 years). MEASURES: The Problem Gambling Severity Index, The Mini-International Personality Item Pool and demographic variables. Differences between groups of gamblers were analysed by ordinary least-squares regression models separately for each personality trait adjusting for gender, age, cohabitation, level of education and work status. FINDINGS: Gamblers with low, moderate and severe levels of gambling problems differed significantly from non-problem gamblers in neuroticism (b = 0.16, 0.34 and 0.66, respectively, all P < 0.001) and conscientiousness (b = -0.13, -0.28 and -0.44, respectively, all P < 0.001). Moderate and severe problem gamblers differed from non-problem gamblers in agreeableness (b = -0.21, P < 0.001 and b = -0.20, P = 0.028, respectively). In addition, gambling problems were much more prevalent among men than women, and more prevalent among those who live alone, individuals without tertiary education and among those who are unemployed or on disability pension. CONCLUSIONS: A higher level of problem gambling severity appears to be associated with higher scores on neuroticism, and with lower scores on conscientiousness and agreeableness in the Mini-International Personality Item Pool.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Large Norwegian population survey using PGSI; the abstract does not say whether sports betting participation was measured.

**Решение:** =

---

### 1081 · R5701

**Activités et types de jeux reliés aux problèmes de consommation de substances chez les jeunes**

2016 · Drogues santé et société · article · fr · https://doi.org/10.7202/1035556ar

La consommation de substances psychoactives (SPA) et la participation à des jeux de hasard et d’argent (JHA) font partie des conduites à risque à l’adolescence. Certaines études montrent que le fait de jouer à des JHA et celui d’éprouver des problèmes de JHA sont associés aux problèmes de consommation de SPA chez les jeunes, mais elles documentent peu quelles activités (nature et quantité) et types de JHA (Internet ou non-Internet) sont plus spécifiquement reliés aux problèmes de consommation de SPA à l’adolescence. Les travaux de la présente étude visent à explorer les liens entre les activités de JHA, le nombre de JHA et les types de JHA d’une part, et les SPA consommées ainsi que la gravité de la consommation de SPA, d’autre part. Pour ce faire, une étude a été réalisée entre 2007 et 2009 auprès de 1 870 élèves de la 3e à la 5e année du secondaire, âgés de 14 à 18 ans. Un questionnaire sur les habitudes de JHA (DSM-IV-MR-J) et un autre sur la consommation de SPA (DEP-ADO) leur ont été administrés. Les résultats montrent notamment que les jeunes polyconsommateurs (alcool et cannabis) s’adonnent aux JHA dans une proportion plus élevée que les consommateurs d’alcool seulement. Aussi, le fait de jouer avec des appareils de loterie vidéo (ALV) semble être associé à une gravité plus importante de la consommation de SPA que les autres activités de JHA. Par ailleurs, une gravité plus élevée de la consommation de SPA est manifestée chez ceux qui s’adonnent à un plus grand nombre d’activités de JHA différentes. Les jeunes jouant avec les ALV et ceux faisant des paris sportifs s’adonnent à un nombre moyen de JHA différents plus important. Enfin, les joueurs Internet de l’échantillon présentent des problèmes de consommation de SPA plus graves que les joueurs non-Internet. Les implications cliniques de ces résultats sont discutées.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Survey of 1,870 adolescents using DSM-IV-MR-J that measured gambling activities, including sports betting (paris sportifs).

**Решение:** =

---

### 1082 · R5708

**Loyalty Typologies and Consumer Choice Factors in the Online Sports-Betting Industry: An Explorative Study into the Italian Regulated Market**

2016 · International Journal of Marketing Studies · article, journal-article · en · https://doi.org/10.5539/ijms.v8n5p1

&lt;p&gt;The paper analyses the loyalty typologies and consumer choice factors in the regulated online sports-betting industry. From the methodological viewpoint an empirical investigation has been carried out through the administration of a questionnaire towards customers who make sports bets on online gambling sites in the Italian regulated market. We have found that, in keeping with consumers’ behaviour “regularities” which normally characterize frequently purchased consumer goods markets, the number of customers who are exclusively loyal to one gambling website is rather limited and that, therefore, online bettors mostly adopt a “multi-brand” buying behaviour. In the markets in which this behaviour pattern emerges, customer loyalty programs appear less efficacious in increasing market penetration of the companies with respect to the firms’ decisions on marketing mix-inputs that influence consumer choice of purchasing. The empirical investigation has therefore permitted us to single out the factors that influence the decision to bet at one online gambling site over another, and to show how the importance of these factors varies in relation to the different degree of the gamblers loyalty. The results are then applied to marketing strategies of the online gambling operators.&lt;/p&gt;

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Questionnaire survey of Italian online sports bettors with a marketing focus; the abstract doesn't say whether a problem-gambling instrument was used.

**Решение:** =

---

### 1083 · R5709

**Daily Fantasy Sports**

2016 · Gaming Law Review and Economics · article, journalarticle, journal-article · en · https://doi.org/10.1089/glre.2016.2056

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: No abstract; the title mentions daily fantasy sports, but this legal journal mostly publishes regulatory commentary, so an empirical PG survey is unlikely.); Sonnet -1 (обзор, комментарий, теоретическая, правовая или регуляторная работа: Gaming Law Review and Economics 2016 piece titled "Daily Fantasy Sports" is likely a legal/regulatory commentary, not an empirical survey; no abstract available.)

**Решение:** ?

---

### 1084 · R5715

**Daily Fantasy Sports**

2016 · book · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Book with no abstract and a generic DFS title; may be a strategy or legal book, but empirical content cannot be ruled out.

**Решение:** =

---

### 1085 · R5716

**Daily Fantasy Sports**

2016

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the title "Daily Fantasy Sports" fits the topic but doesn't say whether this is an empirical survey or a legal/commentary piece.

**Решение:** =

---

### 1086 · R5735

**Gambling and football : epidemiological research on gambling participation and problem gambling among adult football players in Iceland**

2016 · article · en

There is not much known about the gambling behaviour of Icelandic football players. Aims of the current study were to examine the prevalence of total gambling participation and problem gambling among Icelandic football players, to examine if Icelandic football players have been involved in behaviour that could possibly be related to game fixing and to examine players attitudes towards banning coaches and players to gamble on games the Icelandic championship. Participants were 725, of which 75% were men and 25% were women. Mean age of participants was 23.2 (sd=4.3). Past year gambling participation was 66%; men (78%) gambled significantly more than women (29%). Gambling participation was 76%- 79% in all men’s divisions but one, in Inkasso-deildin gambling participation was 66%. About 32% of women in 1st division had gambled and about 16% in women’s Pepsi-deild. The most popular gambling activity was sports gambling, and then came the lottery, poker, scratch tickets, and Electronic Gambling Machines. Problem gambling was evaluated with Problem Gambling Severity Index PGSI and 9.6% of participants were problem gamblers. Players who gambled more frequently on football on foreign websites were significantly associated with gambling on their own team. Interestingly, about 23% of participants knew about other players or coaches that had gambled on matches involving their own team, but only 7% of players said they gambled on their own team in a match, and 2% had gambled on in-play events in matches involving their own team. Problem gambling was significantly associated with thinking that KSI should not ban players and coaches from gambling on Icelandic matches. This study indicates that match fixing might possibly be a problem in Icelandic football and that players might need education on the possible risk that follows such behaviour.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Survey of Icelandic football players that measured sports betting participation and problem gambling with the PGSI.

**Решение:** =

---

### 1087 · R5739

**An examination of internet and land-based gambling among adolescents in three Canadian provinces: results from the youth gambling survey (YGS).**

2016 · BMC public health · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1186/s12889-016-2933-0

BACKGROUND: With the rapid proliferation of new gambling technology and online gambling opportunities, there is a concern that online gambling could have a significant impact on public health, particularly for adolescents. The aim of this study is to examine online and land-based gambling behaviour among adolescents in 3 Canadian provinces (Ontario, Newfoundland and Labrador, Saskatchewan) prior to the implementation of legalized online gambling. METHODS: Data are from 10,035 students in grades 9 to 12 who responded to the 2012-2013 Youth Gambling Survey (YGS) supplement, a questionnaire administered as part of the Canadian Youth Smoking Survey (YSS, 2012) in 3 provinces: Newfoundland and Labrador (n = 2,588), Ontario (n = 3,892), and Saskatchewan (n = 3,555). RESULTS: Overall, 41.6% of adolescents (35.9% of females and 47.4% of males) had gambled in the past 3 months. 9.4% of adolescents had gambled online in the past 3 months alone (3.7% of females and 15.3% of males). The most popular form of online gambling was online sports betting. Adolescents also engaged in online simulated gambling including internet poker (9.1%) and simulated gambling on Facebook (9.0%). Few adolescents participated in online gambling exclusively and online gamblers were more likely than land-based gamblers to engage in multiple forms of gambling. A higher proportion of adolescent online gamblers scored "high" or "low to moderate" in problem gambling severity compared to land-based only gamblers. CONCLUSIONS: Despite restrictions on online gambling at the time of the study, adolescents were engaging in online gambling at a significantly higher rate than has been previously found. Adolescents were also using technology such as video games to gamble and free online gambling simulations.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Adolescent survey measured online sports betting and problem gambling severity (likely CAGI); may report PG among sports bettors.

**Решение:** =

---

### 1088 · R5740

**Exploratory analysis of determinants of demand for Sports betting in Ghana**

2016 · Unpublished · other/ · https://doi.org/10.13140/rg.2.1.2529.1125

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; possibly a survey of Ghanaian sports bettors on demand determinants, but unclear whether problem gambling was measured.

**Решение:** =

---

### 1089 · R5748

**Gambling and the Sports Betting Industry**

2016 · SAGE Publications Ltd eBooks · part of book or chapter of book, book-chapter · en · https://doi.org/10.4135/9781473919761.n21

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: A book chapter on the sports betting industry with no abstract; it is very likely a descriptive overview, not a survey of bettors.); Sonnet ? (нет аннотации: Book chapter with no abstract; likely overview of the industry (probably non-empirical), but content can't be verified from the title alone.)

**Решение:** ?

---

### 1090 · R5751

**Socio Economic Effects of Gambling: Evidence from Kampala City, Uganda**

2016 · RePEc: Research Papers in Economics · other literature type, review, text/text · en · https://doi.org/10.22004/ag.econ.234554

Since the year 2000, the gambling industry in Uganda has experienced a rapid increase in activity, with various new modes and facilities being introduced. The proliferation of gambling has seen the industry diversify from the early forms of gambling like casino gambling and national lotteries to new modes like sports betting and online betting among other forms. Regarding gambling related tax revenues, the industry has equally grown at an unprecedented rate, with tax collections growing from UGX 0.24 billion in 2002/3 to UGX 11.1 billion in 2013/14. While this growth in tax revenue is a welcome development, there is still considerable concern about the potential for the gambling sector to cause harm in form of addictions, loss of savings, idleness and increased crime. Hence, as the gambling industry continues to grow in popularity and prevalence, a well-founded understanding of its operations and socio economic implications is imperative. This study sought to fill this void by investigating three questions: 1) What is the level of participation in the gambling industry in Kampala city?; 2) How does gambling affect various aspects of welfare and the economy and 3) What is the adequacy and effectiveness of the current regulatory framework in regulating the gambling sector?. Based on a household survey conducted in Kampala city in April 2015, we find that approximately one in every four adults had engaged in some form of gambling in the twelve months preceding the survey. Age, income, employment status and gender are major determinants in gambling participation. Additionally, we find that, on average, the poorest in society spend a higher proportion of their personal income on gambling compared to their richer counterparts. Gambling also has the greatest displacement effect on household necessities and savings and has to some extent led to problem gambling. In terms of revenue, the percentage contribution of the gambling industry to total revenue is still low (0.15% in 2013/14) but growing. Furthermore, qualitative evidence revealed that many facets of the law relating to lottery and gaming have become obsolete and are not sensitive to the new modes of gambling and the unprecedented growth of the industry. Similarly, the regulatory body (National Lotteries Board) has substantial capacity problems and limited statutory powers and is not always able to effectively exercise its mandate herein inhibiting its ability to comprehensively regulate the gambling industry. On the policy front, we propose that the public should be protected from over stimulation of latent gambling through limitation of gambling opportunities: by imposing tighter restrictions on advertising; tighter restrictions on entry into gambling establishments, based on age; and limitation of opening hours among others. In congruence, parliament should expedite the passage of the Lottery and Gaming Bill (2013) into law to empower the National Lotteries Board with more statutory powers and provide a basis for addressing capacity and financial challenges that they currently face. In line with this, there is a need to minimize the negative social and economic impacts of gambling by promoting responsible gambling and providing support and counselling to problem gamblers.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Kampala household gambling survey that mentions sports betting and problem gambling; unclear whether a screening instrument was used.

**Решение:** =

---

### 1091 · R5755

**Prevalence of Problem Gambling Among Adolescents: A Comparison Across Modes of Access, Gambling Activities, and Levels of Severity**

2016 · Journal of Gambling Studies · article · en · https://doi.org/10.1007/s10899-016-9652-4

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · No abstract, but the title points to adolescent problem-gambling prevalence compared by gambling activity, which likely includes sports betting.

**Решение:** =

---

### 1092 · R5760

**Gambling among European professional athletes. Prevalence and associated factors.**

2016 · Journal of addictive diseases · journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1080/10550887.2016.1177807

In Europe, the prevalence of gambling disorders in the general population ranges from 0.15 to 6.6%. Professional athletes are known for having risk factors for addictive behaviors, such as young age or sensation seeking, though no study has yet tried to evaluate the prevalence of gambling and gambling disorders among this specific population. The goals of this study were to estimate the prevalence of gambling, problematic or not, among European professional athletes and to explore the factors that are associated with gambling practice and gambling problems in professional athletes. A self-completion questionnaire was specifically designed for this study. The questionnaires were distributed by European Union athletes to professional ice hockey, rugby, handball, basketball, football, indoor football, volleyball, and cricket teams in Spain, France, Greece, Ireland, Italy, Sweden, and the United Kingdom. Socio-demographic variables (age, sex, education, marital and parental status, sport, country of birth, and country of practice), variables linked to gambling (gambling habits, screening of gambling problems with the Lie/Bet questionnaire, and gambling related cognitions), and impulsive behavior data (urgency, premeditation, perseverance, and sensation seeking [UPPS]-Short Form questionnaire) were gathered. There were 1,236 questionnaires filled out. The percentage of professional athletes that had gambled at least once during the previous year was 56.6%. The prevalence of problem gambling, current or past, was 8.2%. A certain number of variables were associated with the gambling status. In particular, betting on one's own team (OR = 4.1, CI95% [1.5-11.5]), betting online (OR = 2.9, CI95% [1.6-5.4]), gambling regularly (OR = 4.0, CI95% [2.1-7.6]), and having a high positive urgency score (OR = 1.5, CI95% [1.3-1.7]) were associated with gambling problems, current or past, among professional athletes. Professional athletes are particularly exposed to both gambling and problem gambling.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Survey of professional athletes measuring gambling habits including sports betting (own team) and problem gambling via Lie/Bet.

**Решение:** =

---

### 1093 · R5762

**The state of the online sport betting industry in South Africa**

2016

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; title suggests an industry analysis, but it could be a thesis that surveyed South African online sports bettors.

**Решение:** =

---

### 1094 · R5765

**Clustering Finnish Gambler Profiles Based on the Money and Time Consumed in Gambling Activities.**

2016 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-015-9556-8

Gambling involves consumption of gamblers' money and time. Gamblers are a heterogeneous group, and in addition to grouping gamblers based on personality factors, it is also important to find different gambler profiles with respect to their gambling behavior. Using the nationally representative survey 'Finnish Gambling 2011' (N = 4484), this article studies the subtypes of Finnish gamblers based on the frequency of gambling and the amounts of money and time used in different gambling forms. Cluster analysis reveals six profiles of gamblers, from infrequent gamblers to omnivorous gamblers. In the further analysis of the clusters, it was found that the highest problem gambling prevalence was in the groups of sport betting + electronic gaming machine gamblers and omnivorous gamblers, which were also both dominated by men. Certain gambling consumption patterns and risk factors for problem gambling are related to both socio-demographic backgrounds of the gamblers as well as the structural and situational characteristics of the games. The results have implications for the prevention of problem gambling, as some consumption patterns may be connected with the probability of developing gambling problems.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Nationally representative Finnish survey; reports problem gambling prevalence across gambler clusters, including sport betting groups.

**Решение:** =

---

### 1095 · R5767

**Gambling, Saving, and Lumpy Expenditures: Sports Betting in Uganda**

2016

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; likely an economics survey of Ugandan sports bettors, and it is unclear whether a problem-gambling instrument was used.

**Решение:** =

---

### 1096 · R5775

**A Case of Mistaken Identity? A Comparison of Professional and Amateur Problem Gamblers.**

2016 · Journal of gambling studies · article, comparative study, journal article · eng · https://doi.org/10.1007/s10899-015-9531-4

Professional gamblers are more likely than amateur gamblers to meet criteria for problem gambling but minimal research has examined their gambling behavior and its consequences. This study compared gambling behavior, problem gambling symptoms, related harms, recognition, and help-seeking among problem semi/professional gamblers (PPGs/PSPGs) and problem amateur gamblers (PAGs). Surveys completed by 57 self-identified professional gamblers, 311 semi-professional gamblers and 4226 amateur gamblers were analysed. PPGs/PSPGs were significantly more likely than PAGs to be male, younger, never married, speak a language other than English at home, and have higher psychological distress, compared to PAGs. PPGs/PSPGs were more likely to gamble more frequently on many skills-based forms, but most also participated in several chance-based forms. PPGs'/PSPGs' most common problematic gambling form was electronic gaming machines and they were more likely to have problems with sports betting than PAGs. Most PPGs/PSPGs reported coming out behind on all gambling forms over the previous year. PPGs/PSPGs were more likely than PAGs to report chasing losses and numerous detrimental financial gambling consequences. This group's self-identification as PPGs/PSPGs is clearly inaccurate and perhaps a means to avoid stigma, elevate status and support problem denial. PPGs/PSPGs may represent an extreme example of gamblers with erroneous cognitions and beliefs who lack the required discipline and skill to be successful professional gamblers. The findings identify a group of problem gamblers who may benefit from interventions to dispel their mistaken self-identity, and emphasize the need for more rigorous confirmation of professional gambler status in future research.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Large survey of gamblers measured problem gambling and sports betting participation; full text may report problem gambling by activity.

**Решение:** =

---

### 1097 · R5776

**Demographic, Behavioural and Normative Risk Factors for Gambling Problems Amongst Sports Bettors.**

2016 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-015-9571-9

Abstract Sports betting is growing exponentially, is heavily marketed and successfully targets young adult males. Associated gambling problems are increasing. Therefore, understanding risk factors for problem gambling amongst sports bettors is an increasingly important area of research to inform the appropriate design and targeting of public health and treatment interventions. This study aimed to identify demographic, behavioural and normative risk factors for gambling problems amongst sports bettors. An online survey of 639 Australian sports bettors using online, telephone and retail betting channels was conducted. Results indicated that vulnerable sports bettors for higher risk gambling are those who are young, male, single, educated, and employed full-time or a full-time student. Risk of problem gambling was also found to increase with greater frequency and expenditure on sports betting, greater diversity of gambling involvement, and with more impulsive responses to betting opportunities, including in-play live action betting. Normative influences from media advertising and from significant others were also associated with greater problem gambling risk. The results of this study can inform a suite of intervention, protection and treatment initiatives targeted especially at young male adults and adolescents that can help to limit the harm from this gambling form.

**ИИ:** + · обе модели · беттеры + инструмент · Online survey of 639 Australian sports bettors that assessed problem gambling risk (likely PGSI).

**Решение:** =

---

### 1098 · R5777

**Risk Factors for Gambling Problems: An Analysis by Gender.**

2016 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-015-9548-8

Abstract Differences in problem gambling rates between males and females suggest that associated risk factors vary by gender. Previous combined analyses of male and female gambling may have obscured these distinctions. This study aimed to develop separate risk factor models for gambling problems for males and for females, and identify gender-based similarities and differences. It analysed data from the largest prevalence study in Victoria Australia ( N = 15,000). Analyses determined factors differentiating non-problem from at-risk gamblers separately for women and men, then compared genders using interaction terms. Separate multivariate analyses determined significant results when controlling for all others. Variables included demographics, gambling behaviour, gambling motivations, money management, and mental and physical health. Significant predictors of at-risk status amongst female gamblers included: 18–24 years old, not speaking English at home, living in a group household, unemployed or not in the workforce, gambling on private betting, electronic gaming machines (EGMs), scratch tickets or bingo, and gambling for reasons other than social reasons, to win money or for general entertainment. For males, risk factors included: 18–24 years old, not speaking English at home, low education, living in a group household, unemployed or not in the workforce, gambling on EGMs, table games, races, sports or lotteries, and gambling for reasons other than social reasons, to win money or for general entertainment. High risk groups requiring appropriate interventions comprise young adults, especially males; middle-aged female EGM gamblers; non-English speaking populations; frequent EGM, table games, race and sports gamblers; and gamblers motivated by escape.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Victorian prevalence survey data (N=15,000), likely PGSI-based at-risk status, with sports betting as a predictor by gender.

**Решение:** =

---

### 1099 · R5778

**Sports Bettors’ Responses to Sports-Embedded Gambling Promotions: Comparisons Amongst PGSI Groups**

2016 · Digital Scholarship - UNLV (University of Nevada Reno) · conference-paper · en

Televised sporting events now contain a plethora of gambling and sports betting promotions, including logos, signage, advertising, sponsored segments and celebrity endorsement. This presentation focuses on how sports bettors respond to these promotions, drawing on research findings from Australia.\nA first study examined sports bettors’ responses to these promotions, and whether this varied with problem gambling severity. Surveys with 544 Queensland sports bettors indicated that problem gamblers had highest approval of, felt most encouragement to gamble, and had been influenced to gamble most from these promotions, compared to non-problem and at-risk gamblers. Problem gamblers were also more influenced to bet on sports by contextual factors, particularly certain bet types and promotional appeals.\nA second study used a conjoint design to measure responses to 20 simulated promotions amongst 611 regular sports bettors, non-regular sports bettors and non-sports bettors. Type of bet had more utility than type of commentator, type of message appeal and type of promotion. For type of bet, novelty risk-free bets were more enticing than micro-bets, exotic bets and traditional bets. After the risk-free bet, problem gamblers were distinguished from other PGSI groups by greater attraction to micro-bets.\nThe research contributes to understanding how responses to sports-embedded gambling promotions vary with problem gambling severity. It can inform policy developments and future research on sports betting advertising, behaviour and associated gambling problems.\nFinancial support for this study was provided by the Queensland Department of Justice and Attorney General.

**ИИ:** + · обе модели · беттеры + инструмент · Conference paper surveying 544 Queensland sports bettors, grouped by PGSI; the problem-gambling proportion is likely reportable.

**Решение:** =

---

### 1100 · R5783

**Fantasy Sports and Gambling: A Comparison of Antecedent Traits and Motivations**

2016 · Developments in marketing science: proceedings of the Academy of Marketing Science · other literature type, part of book or chapter of book, book-chapter · en · https://doi.org/10.1007/978-3-319-26647-3_122

Fantasy sports have witnessed remarkable growth in the USA and around the world. While most fantasy sports players prefer free leagues, pay-to-play (P2P) fantasy sport contests are growing in popularity, with 46.9 % of players paying league participation fees (FSTA 2014). The nature of P2P fantasy sports, with its focus on entry fees, uncertain outcomes, and cash prizes, leads many to classify fantasy sports as a form of gambling. The trend toward P2P fantasy sports also raises questions regarding the nature of fantasy sports players and their motivations.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Probably a survey comparing fantasy sports players' traits and motivations with gamblers'; the abstract doesn't say if a problem-gambling instrument was used.

**Решение:** =

---

### 1101 · R5794

**A dangerous cocktail: Alcohol consumption increases suicidal ideations among problem gamblers in the general population**

2016 · Addictive Behaviors · article · en · https://doi.org/10.1016/j.addbeh.2015.12.017

The current research examined whether alcohol consumption exacerbates suicidal ideations among gamblers in the general population. While prior research suggests problem gambling severity and excessive alcohol consumption are unique predictors of suicidal behaviors, the extant literature as almost exclusively focused on gamblers in treatment. This represents a significant gap in the literature as less than 10% of gamblers seek treatment. Furthermore, gamblers in treatment are not representative of gamblers in the general population, precluding a simple generalization of research findings. We address this gap using data obtained from the Canadian Community Health Survey (Cycle 4.1)--a cross-sectional national survey that assesses health-related information among the Canadian population. To this end, we conducted a moderation analysis with problem gambling severity as the independent variable, weekly alcohol consumption as the moderator variable and suicidal ideations (in the past 12 months) as the dependent variable. The results found that alcohol consumption alone did not reliably predict suicidal ideation among gamblers who did not gamble problematically. However, as predicted, the odds of suicidal ideation were greatest among problem gamblers who frequently consumed alcohol. Thus, it may behoove policy makers to re-visit the availability of alcohol in gambling venues. Moreover, responsible gambling-oriented education initiatives may be advanced by informing gamblers about the increased risk of suicidal ideations when problematic gambling is combined with frequent alcohol consumption.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Secondary analysis of national CCHS 4.1 with CPGI; unclear whether sports betting participation is reported among gamblers.

**Решение:** =

---

### 1102 · R5797

**Adolescents’ perceptions of parental influences on commercial and simulated gambling activities**

2016 · International Gambling Studies · article, review · en · https://doi.org/10.1080/14459795.2016.1220611

Parents can have a major influence on young people’s access to and participation in gambling activities. However, with the rise of digital online gambling, there is greater potential for young people to freely explore and engage in gambling activities without parental oversight. This study examined perceived parental influences on adolescents’ gambling activities, including differences in these influences across commercial and simulated types of activities, and the association between parental influences and problem gambling symptoms. A survey of 824 adolescents from 3 secondary schools was conducted. The results indicated that financial gambling was usually facilitated by a parent, particularly for scratch tickets and sports betting. Simulated gambling activities, such as social casino games, tended to be reported as being unsupervised by parents. Young people’s perceptions of parents’ measures to limit, restrict or oversee online and electronic activities were not significantly associated with youth simulated gambling. Their perceptions of parental influences were not significant predictors of problem gambling behaviours. This study underscores the need to examine potential differences in how adolescents develop an understanding of different gambling activities without parental influences, and adds to the continuing debate on the necessity of regulation and other countermeasures to limit young people’s access to simulated gambling activities.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Adolescent survey that measured sports betting participation and problem gambling symptoms; may report problem gambling among sports bettors.

**Решение:** =

---

### 1103 · R5801

**Changes in risky gambling prevalence among a New Zealand population cohort**

2016 · International Gambling Studies · article · en · https://doi.org/10.1080/14459795.2016.1183033

Evidence suggests that problem gambling is an unstable state where gamblers move into and out of risk over time. This article looks at longitudinal changes in risky gambling and the factors associated with an increased risk (measured by the Problem Gambling Severity Index [PGSI]) in the current New Zealand context, which has experienced a doubling of the electronic gaming machine (EGM) market over the last two decades. Respondents from a nationally representative baseline sample (n = 2672) were recontacted two years later to assess changes in gambling behaviours. Among the 901 respondents reached at follow-up, average gambling risk increased over time, and the prevalence of those who had at least some level of gambling risk (i.e. low-risk or greater) more than doubled (from 4.7% to 12.4%). The majority (80.2%) of those who were at risk at follow-up had not been at risk at baseline. Multivariate linear regression analyses show that the predictors of low to moderate increased risk include Pacific ethnicity; high neighbourhood deprivation status; baseline frequent, continuous gambler type; baseline PGSI status; and playing EGMs. These findings highlight the need to develop theories of gambling addiction trajectories and to identify the earliest point along the trajectory where public health interventions should occur.

**ИИ:** + · обе модели · опрос населения об азартных играх · Nationally representative NZ cohort using PGSI with gambling activities measured; the full text may show sports betting participation alongside problem gambling.

**Решение:** =

---

### 1104 · R5808

**Similarities and Differences Between Daily Fantasy Sports Users and Traditional Fantasy Sports Users & Recommendations for the Industry**

2016 · article · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the title points to a comparison of DFS users that may have used a problem-gambling screen; full text needed.

**Решение:** =

---

### 1105 · R5822

**Life events and problem gambling severity: A prospective study of adult gamblers.**

2016 · Psychology of Addictive Behaviors · article · en · https://doi.org/10.1037/adb0000227

Several studies have shown that gambling problems are cyclical but few have empirically investigated factors that are associated with change. The purpose of this article is to prospectively examine associations between life events and problem gambling severity in a cohort of gamblers. Occurrence of life events and gambling problem severity were assessed 3 times over a period of 2 years in a cohort of nonproblem and problem gamblers (N = 179) drawn from a representative sample derived from a population survey. Cross-lagged analyses revealed that cumulative number of life events were associated with an increase in severity of problem gambling 12 months later. Regression analyses showed that significant life events in several domains, for example, "change in sleeping habits," "accidental injury or illness" or "retirement," are likely to be associated over time to the increase or the continuation of risky gambling habits. This study's findings on the potential negative influence of cumulative number of life events, or of specific ones, are informative for secondary prevention and treatment. (PsycINFO Database Record

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Gambler cohort from a population survey, with problem gambling severity measured; unclear whether sports betting participation was recorded.

**Решение:** =

---

### 1106 · R5827

**Economic Analysis on the Purchasing of Sports Lottery**

2016 · review

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: Title only, tagged as a review: an economic analysis of sports lottery purchasing, with no sign of a problem-gambling measure.); Sonnet ? (нет аннотации: No abstract; sports lottery purchasing study could be a survey of buyers or just economic/sales analysis. Problem gambling measurement unknown.)

**Решение:** ?

---

### 1107 · R5831

**Game On: Past Year Gambling, Gambling-Related Problems, and Fantasy Sports Gambling Among College Athletes and Non-athletes.**

2016 · Journal of gambling studies · article, comparative study, journal article · eng · https://doi.org/10.1007/s10899-015-9561-y

College students experience higher rates of gambling-related problems than most other population segments, including the general population. Although Division I (D1) athletes often have more at stake than the average student if and when they gamble (e.g., the potential to lose their athletic eligibility), relatively few studies have assessed the gambling behavior of this population and none have specifically assessed fantasy sports gambling. We conducted a study to examine gambling behavior (past-year gambling, gambling-related problems, and fantasy sport gambling) among a sample (N = 692) of college students at a private religiously affiliated university in the Southwest US. The sample for our study was unique in that approximately 30 % of the participants were D1 athletes. We compared the gambling behavior among three groups based on the athlete status: D1 athletes, club/intramural/recreational (CIR) athletes, and non-athletes (NAs). Compared to females in our sample, males observed higher rates of past year gambling, fantasy sports participation, fantasy sports gambling, and gambling-related problems. Among males, we found that CIR athletes observed the highest rates of past year gambling and fantasy sports participation and D1 athletes observed higher rates than NAs. We did not find differences in fantasy sport gambling and past year gambling-related problems based on athlete status in males or females.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Student survey measuring fantasy sports gambling and gambling-related problems (likely a screening instrument); could report problem gambling among fantasy sports gamblers.

**Решение:** =

---

### 1108 · R5832

**Sports Betting - Tipster Platform**

2016

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: Title suggests a betting-tips software platform project; no sign of a survey of people or a problem-gambling measure.); Sonnet ? (нет аннотации: No abstract; title "Sports Betting - Tipster Platform" is about sports betting but could be a product description or a study, so full text is needed.)

**Решение:** -

---

### 1109 · R5836

**The university of sydneySocial-Economic Impacts of Sports Betting on Ugandan Youth. The case of Mbale Youth .**

2016 · The Journal of Gambling Business and Economics · article, journal-article · en · https://doi.org/10.5750/jgbe.v10i2.1205

Sports betting activities, particularly among youth, is increasing rapidly in Ugandan. The aim of this study was to determine the motivation for sports betting among Ugandan youth, and the social economic impact of this form of gambling. In a cross sectional quantitative research design, a questionnaire data was obtained from a sample of 181 youth attending betting houses in the Mbale district. Results indicated that that most youths were motivated by the desire to win money. Findings also revealed that Ugandan youth socially and economically benefited from sports betting. The study concludes by recommending that even if findings do not show the negative impacts of gambling on youth, there is need for stricter laws to avert any future negative implications.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Questionnaire survey of 181 youth sports bettors in Uganda; abstract covers motives and impacts but doesn't say whether a problem-gambling instrument was used.

**Решение:** =

---

### 1110 · R5838

**A Baseline Study of Past-Year Problem Gambling Prevalence Among Ohioans**

2016 · Journal of Gambling Issues · article · en · https://doi.org/10.4309/jgi.2016.34.3

Historically, the scope of legalized gambling was limited in Ohio, but everything changed when a new constitutional amendment allowed four casinos to open. To better understand the impact of gambling expansion, a household survey was commissioned to determine the baseline estimate of problem gambling behaviours in the state before casinos opened. Participants were selected through multi-stage probability sampling, with over 3,500 respondents completing valid surveys. Nearly 60% of Ohioans gambled in the past year, but the statewide prevalence of problem gambling was relatively low; only 1.4% of persons scored high enough on the Problem Gambling Severity Index to be classified as a potential problem gambler (score >3). Regional estimates of problem gambling were highest for Franklin and Hamilton counties (both 5.0%) and lowest for Lucas and Cuyahoga counties (3.2% and 2.1%, respectively). Exploratory logistic regression modelling found that race, employment, education, family history of problem gambling, and feelings of depression increased the odds of being a problem gambler. Results will inform the discussion about current gambling problems and enable policy makers to design prevention strategies.La présente étude portait sur la relation entre le prix des billets de loterie instantanée (à gratter) et la « récupération des pertes » dans un seul épisode de jeu. Pendant plusieurs mois, chaque fois qu’un billet de loterie instantanée était acheté (N = 1081), les commis de dépanneur consignaient le sexe des joueurs et le prix des billets de loterie instantanée, et indiquaient si le consommateur avait acheté un autre billet avant de quitter les lieux. L’analyse de régression logistique a montré une corrélation importante entre le prix des billets et le rachat (rapport de cotes = 0,842, p < 0,0001), ce qui suggère que la récupération au cours d’un même épisode de jeu est courante pour les billets de loterie instantanée à plus bas prix et que de plus faibles coûts ne réduisent pas nécessairement les risques.

**ИИ:** + · обе модели · опрос населения об азартных играх · Statewide Ohio household gambling prevalence survey using PGSI; activity participation tables likely include sports betting. The French abstract text belongs to another article.

**Решение:** =

---

### 1111 · R5842

**Chapter Seventeen: ESPN and the Fantasy Sport Experience**

2016 · Peter Lang eBooks · book-chapter · en · https://doi.org/10.3726/978-1-4539-1500-4/32

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: Media-studies book chapter on ESPN and fantasy sport with no abstract; unlikely to measure problem gambling, but the title alone can't confirm that.); Sonnet -6 (не про азартные игры или «ставка/лотерея» в другом смысле: Book chapter on ESPN and fantasy sport experience, likely media studies. Nothing suggests a gambling or problem-gambling survey.)

**Решение:** ?

---

### 1112 · R5846

**Apuesta y gana: casas de apuestas deportivas on-line**

2016 · Personal computer & Internet · article · es

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: Consumer tech-magazine article about online sports betting sites; not an empirical study of people.); Sonnet ? (нет аннотации: No abstract; the title (online sports betting houses) fits the topic, but it is likely a non-empirical magazine piece. Full text needed to check.)

**Решение:** ?

---

### 1113 · R5850

**Gambling and Sports**

2016 · article · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract is available, and the title "Gambling and Sports" is broad enough to fit an eligible survey; the full text is needed to decide.

**Решение:** =

---

### 1114 · R5854

**Household financial decision making**

2016 · Stirling Online Research Repository (University of Stirling) · dissertation · en

Households are nowadays required to make financial decisions of increasing complexity in an increasing number of domains. This thesis explores psychological mechanisms, behavior change interventions, and potential inhibitory factors underlying wise household financial decisions in the domains of gambling advertising and mutual fund investing. In-depth investigations of these two domains were chosen to balance the depth of topic coverage versus the wide breadth of modern financial decision making. UK soccer gambling advertising was investigated via two observational studies and a range of online experiments. The experiments found that soccer fans struggle to form coherent expectations for the complex bets featuring in UK soccer gambling advertising. Mutual fund investors have to balance a number of cues in their investment choices. Normatively, mutual fund investors should minimize fees. However, a number of investors choose to maximize past returns instead. Three chapters investigate how mutual fund fees and financial percentage returns are psychologically processed, in order to uncover beneficial behavior change interventions. Many participants processed percentages additively, rather than follow the correct multiplicative strategy. Both percentages and corresponding “small” currency amounts were associated with systematic biases. Participant responses were closest to the normative strategy when either past returns were framed as a “small” currency amount, or when fees were framed as a 10 year currency amount. “Some people invest based on past performance, but funds with low fees have the highest future results” was the most effective disclaimer at nudging fee-sensitivity against the real world status quo, “Past performance does not predict future results.”

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Thesis with online experiments on soccer fans and soccer betting advertising; may have measured PGSI among bettors, but the abstract doesn't say.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Thesis on financial decision making; soccer gambling advertising experiments on bet expectations, no problem-gambling instrument evident.)

**Решение:** -

---

### 1115 · R5861

**Online Sports Betting in Greece: An Empirical Investigation**

2016 · EUROPEAN RESEARCH STUDIES JOURNAL · article, review, journal-article · en · https://doi.org/10.35808/ersj/502

JEL Classification: C21, L83, L86 1. Introduction Undisputable the development of communication technologies (ICT) brought with it new forms of online commerce. The advent of digital technology coupled with the enormous potential applications of the web, caused substantial changes in the global gambling industry. Online gambling constitutes one of the most dynamic, promising and rapidly changing businesses around the world. Despite the large volume of studies and internet databases on gambling there is almost nothing known empirically about gambling and its problems in Greece (Griffiths, 2009). Internet gambling is a relatively under-researched area (Griffiths and Parke, 2010). In its first part, the present study, reports some numerical features of the e-gambling commerce internationally and describes its current situation and future trends. At the same time, it presents an overview of the online gaming sector in Greece, highlighting critical legislative shifts and upcoming trends, which will definitely alter the gambling scene in the country. In the second part, the study examines the relationship between the characteristics of the internet sports betting sites and the sports bettors in Greece. The findings of the study, may guide key stake holders, including entrepreneurs, policy makers, regulators, researchers, treatment providers, and industry groups, in forming an appropriate response to internet sports betting in Greece. Data concerning punters' attitudes towards online sports betting, made available through links (banners) on relevant sports betting websites and forums accessible by active sports bettors in Greece. A recent survey showed that internet gambling is still a relatively low prevalence phenomenon (Wardle et al., 2007), making it difficult for someone to present an accurate picture of the characteristics of internet gamblers and their health. Most papers dealing with the gambling issue attempt to establish the active sportsbettors profile and shed light on their motivations, preferences and characteristics in the online sports betting field. 2. E-gambling categories and future trends The European Commission (2012) used the following definition for online gambling services: "Online gambling services are any service which involves wagering a stake with monetary value in games of chance, including lotteries and betting transactions that are provided at a distance, by electronic means and at the request of a recipient of services. " Due to its embryonic development, there have, and continue to be, several terminologies used to define digitized commercial gambling e.g. remote gambling, e-gaming, e-gambling, internet gambling, online gambling, online gaming, interactive gambling and virtual gambling etc. All these terminologies are assessed as equivalent under the scope of this research. Desktop computers, laptops, net books, smart phones, tablets, internet capable mobile phones, interactive televisions, video game consoles are included in a an expanding list of devices that can support e-gambling commerce or interactive gambling (News agents Association, 2011). According to KPMG (2010), the online gaming market is composed of a number of different types of games, with its own business models and technology. They include: Sports Betting, Online Poker, Casino Games, Online Bingo and Online Lottery. Although online gaming now accounts for only a small share of the total worldwide market, it has proven to be one of the fastest growing sectors over the past several years (Christian Capital Advisors, 2006). By the end of 1996 it is estimated that about 15 online sites accepted wagers, increasing to over 200 by the end of 1997, 650 by the end of 1999 and 1,800 by the end of 2002 (Schwartz, 2006). H2 Gambling Capital (2012) put the size of the online gambling industry at about 24.6bn [euro] in 2011, while the EU gambling market represented the 45% of the world market share (European Commission, 2012). …

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Online survey of active Greek sports bettors on attitudes and betting-site characteristics; the abstract does not say whether a problem-gambling instrument was used.

**Решение:** =

---

### 1116 · R5870

**Análisis sobre el aumento de las apuestas deportivas en adolescentes estudiantes y las conductas de riesgo asociadas**

2016 · Actividad física y deporte: ciencia y profesión · review, article · es

espanolEl objetivo principal era el de analizar la prevalencia de juegos y apuestas deportivas en estudiantes de Bachillerato, ademas de determinar si estas conductas estaban ligadas a otros comportamientos de riesgo. Tambien estudiamos las diferencias entre jovenes deportistas y no deportistas, al igual que entre hombres y mujeres. Como muestra se escogieron 120 alumnos, con edades comprendidas entre 16-19 anos, pertenecientes a 1o y 2o de Bachillerato de un colegio de Torrent (Valencia). Para analizar los comportamientos y conductas de los jovenes se diseno un test Ad hoc, creado en base al test SOGS (South OaksGamblingScreen). Ya que los datos fueron obtenidos por la encuesta pasada por el autor, el primer analisis fue descriptivo. Mediante el software SPSS se utilizaron formulas chi-cuadrado y U de Whitney para encontrar posibles correlaciones. 61 alumnos habian realizado alguna vez una apuesta deportiva, con una frecuencia de juego alta, pues un 43,5% apostaban a diario o semanalmente. Tambien se encontro significativo (P=0,05) que los que practicaban algun deporte participaban mas en apuestas y con mayor frecuencia en juegos de azar que los no deportistas. Se evidencia la necesidad de instaurar programas formativos que puedan guiar a los jovenes a superar esta nueva adiccion. EnglishThe main objective was to analyze the prevalence of sports betting games among high school students, and to determine whether these behaviors were linked to other risky behaviors. We also studied the differences between young athletes and non-athletes, as well as between men and women. As sample, 120 students were chosen, aged 16-19, belonging to 1st and 2nd year Bachelor inTorrent (Valencia). To analyze the conduct and behavior of young people an Ad hoc test created based on the SOGS (South Oaks Gambling Screen) was designed. Since data were obtained by the author through a survey, the first analysis was descriptive. Using SPSS software chi-square formulas and Whitney U were used to find possible correlations. 61 students had ever had a sports bet with a high frequency of play, as 43.5% bet on a daily or weekly basis. We also found significant (P ≤ 0.05) than those who practiced more involved in sports betting and most often in gambling than non-athletes. The necessity to establish training programs that can guide young people to overcome this new addiction is evidence

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Student survey with 61 sports bettors; used an ad hoc questionnaire based on SOGS. It's unclear whether a problem-gambling case definition was applied.

**Решение:** =

---

### 1117 · R5871

**Gambling among Teenagers in Bjelovar-Bilogora County (Croatia)**

2016 · University of Zagreb University Computing Centre (SRCE) · article · en · https://hrcak.srce.hr/160020

IntroductionGambling is one of the mankind's oldest activities for fun. The term gambling refers to investing something valuable into an event with uncertain outcome for the chance of winning money or prizes. Main characteristics of gambling are taking a risk and uncertainty of outcome [1]. Today we are witnessing the explosion of legal gambling, more and more casinos, lottery and betting shops are opening every day. According to the Croatian law, gambling games are divided into four main groups: Lottery tickets, casino games, betting games and slot machines [2]. The law clearly defines 18 years as the age limit for gambling. It prohibits anyone under the age of 18 to enter the casino, to gamble at casinos or at any other gambling or betting facilities, and requires staff to check ID to any participants. The conviction for breaking any of aforementioned law propositions is a fine between 50.000,00 and 500.000,00 kunas. [3]. Nevertheless, despite the 18 year age limit, gambling opportunities are widely and easily accessible and also available for high school students. Poverty and economic crisis also contributes to spreading of gambling and thoughts of earning some easy money, but it can lead to a harmful addiction with gambling. The previous research has shown that problem gambling is a constellation of more connected issues such as risk behaviours, alcohol and substance abuse. The consequences of problem gambling are as harmful as substance abuse, and by the epidemiological trends we are witnessing, one is to expect a rise in problem gambling if no successful prevention actions take place in near future [4-6].The research on gambling in Croatia is still limited, and there are only few studies conducted among children and adolescents. The study among adolescents revealed that 83% of them have gambled at least once in their lives; 19.0% of them gambled on sports events at least once in a week, on the internet (22.8%) and on slot machines (6.2%). Their reasons for taking part in gambling are money, fun with friends, and close friend who gambles as well. One third of children report that their parents are aware of their gambling activities, and 20-30% of them also gamble, especially fathers. Vocational high school students are more likely to gamble than students from general high schools [7].Study by Koic et al conducted among the last year high school students showed that 38.5% of boys and 11.7% girls gamble, boys mostly at betting shops (42%), girls at Bingo (33%). Vocational school students gamble the most, and medical high school students the least. Students think of gambling as a way to have a good time (28.2% boys and 15.5% girls). Large number of students (68%) knows a person with a gambling problem, and almost all (97%) of the students know about gambling addiction. They (22% girls and 38% boys) also think they have enough information on problem gambling, and even more of them (62.9%) think they do not need additional education about gambling problems [8].Other research among high school students report that 75% of the students have gambled at least once in their lives; mosdy on sports events and lottery. Almost half of them who gamble (47.1%) bet on sports events and 38.5% of them do it few times a week. Internet gambling is done by fewer students (7.7%) but half of those who do it, do it every day (53%). They found that men are more likely to develop gambling problems, but did not found that any specific type of high school (general vs vocational high school) was related to gambling rates [9].Results from the ESPAD study done in Croatia among youth of 16 years of age show that 61% of boys and 89% of girls that age never played on slot machines, 8.6% of them do it at least once a week, and 4.4% of boys do it almost daily [10].Pilot study conducted among older adolescents, university students in Zadar show that 7.1% of university students bet on sport events, 11.5% have a partner who gambles, and 12. …

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Teen gambling survey in Croatia, where sports betting is common; the abstract only covers the introduction, so whether a PG instrument was used is unclear.

**Решение:** =

---

### 1118 · R5874

**Parent’s perception of their children gambling**

2016 · Journal of Behavioral Addictions · conference object · eng · https://www.bib.irb.hr/810191

Background and aim: Although legal age for gambling in Croatia is 18, approximately 80% of adolescents reported having gambled at least once in their lifetime on regulated activities, 19% regularly bet on sport results and as much as 12, 3% have already developed severe psychosocial consequences related to gambling (Ricijas & Dodig, 2014). Additionally, adolescents’ self-reports also suggest parental tacit acceptance of their gambling behavior (Ricijas et al., 2011). Therefore, the aim of this study is to explore parental perception of their children gambling (frequency and gambling related problems) and to compare it to children’s self-report. Method: Research is being conducted from October to December 2015 with expected sample of approximately N=400 parents and their adolescent children (age range from 14 to 19). The following instruments are being used: (1) Questionnaire on basic socio-demographic characteristics, (2) Gambling Activities Questionnaire and (3) Canadian Adolescent Gambling Inventory – CAGI (Tremblay et al., 2010). Results: The analysis will be based on matched pairs (parents and their children) in order to verify the hypothesis that parental perception of their children’s gambling is significantly different compared to their self-report. Furthermore, this paper will also address the effect of child’s gender with regards to parental perception of their gambling. The results will be interpreted in relation to social and economic circumstances in Croatia, emphasizing the significance of availability, accessibility and general acceptance of gambling, especially sports betting. Conclusion: These results will have significant practical implications in developing evidence-based preventive and treatment programs for young people.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Adolescent survey measuring gambling activities (sports betting emphasized) and problem gambling with the CAGI screening instrument; conference abstract.

**Решение:** =

---

### 1119 · R5875

**Predictors of adverse gambling related consequences among adolescent boys**

2016 · Children and Youth Services Review · article · en · https://doi.org/10.1016/j.childyouth.2016.06.008

Although gambling is illegal for minors, adolescents do gamble and even higher proportions of adolescents than adults are at risk to become problem gamblers. Moreover, many adolescents suffer from a wide range of gambling related harms, and this study sought to examine what predicts different adverse consequences of adolescent gambling. Our aim was to test whether various cognitive, motivational and behavioural factors were associated with psychosocial consequences and loss of control, and with interpersonal and financial consequences of gambling, as measured by the Canadian Adolescent Gambling Inventory, the only instrument developed specifically for use on adolescents. The data was collected on a convenience sample of 1330 male Croatian students (Mage=16.58, SDage=1.16) from all three types of secondary education in Croatia. Results show that a high proportion of adolescents gamble, and that almost half of them are either at risk or can already be considered problem gamblers. Sport betting, VLT machines and betting on virtual horse races were the most frequent gambling activities for Croatian high-school boys. Hierarchical regression models showed that psychosocial consequences and loss of control can be predicted by higher frequency of gambling, previous experience with winning money and a specific motivation to earn money gambling, to become a better gambler and with having a drive to continue gambling after winning. On the other hand, interpersonal and financial consequences were predicted again by a higher frequency of gambling, the motive to be a better gambler and the drive to continue gambling after winning, but also by specific motivation to relax and feel better. Having more cognitive distortions, specifically having poorer understanding of chance and probabilities and more superstitious beliefs, as well as engagement in general risky and antisocial behaviour also predicted more interpersonal and financial consequences. Findings are discussed in the context of practical implications for prevention programs of adolescent gambling.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Survey of Croatian adolescent boys; sports betting participation measured and problem gambling classified with the CAGI.

**Решение:** =

---

### 1120 · R5885

**Obilježja kockanja roditelja zagrebačkih srednjoškolaca**

2016 · University of Zagreb. University of Zagreb, Faculty of Education and Rehabilitation Sciences · master thesis, dissertation · hr · https://urn.nsk.hr/urn:nbn:hr:158:711910

The main goal of this paper is to gain insight into the activities of gambling, the severity of the problem gambling and attitudes of parents towards gambling and potential gender differences. This research is an integral part of the wider sub-project called "Parental perception of youth gambling", which is carried out in the context of many years of scientific research project "Gambling of young people in Croatia," whose leader is doc. dr. sc Neven Ricijaš. The study was conducted on a sample of 105 parents (M = 40, Z = 65) of high school students in Ivanic Grad. Participation in the survey was anonymous on the basis of previously made codes. The study was conducted in groups, at parent-teacher meetings in schools, and on the paper-pencil principle.For the purpose of this research paper, some parts of the instruments were used from a comprehensive battery of instruments of the questionnaire for the parents: : The questionnaire on general and socio-demographic data, The attitude scale towards gambling, Gambling activities questionnaire and Questionnaire South Oaks Gambling Screen (SOGS). The survey results show that most parents gambled at least once in their lives as confirmed by the data about playing lotto (72.4%), one-off lottery tickets (52.4%) and sports betting (15.2%). The survey identified gender differences with regard to the frequency of gambling, as well as differences with respect to the specific type of games of chance, on the way that fathers are gambling more often than mothers, whereas both genders mostly play lotto but very rear roulette at the casino. In line with expectations, the results indicate that the majority of parents (90.7%) do not have significant problems with gambling, that is, nine of them experience gambling problems. The survey confirmed predominantly negative attitudes towards gambling with both parents, but there was not found significant gender difference. Temeljni cilj rada je stjecanje uvida u aktivnosti kockanja, izraženost problema povezanih s kockanjem te stavove roditelja prema kockanju kao i eventualne rodne razlike. Ovo istraživanje sastavni je dio šireg podprojekta pod nazivom "Roditeljska percepcija kockanja mladih", a koji se provodi u okviru višegodišnjeg znanstveno-istraživačkog projekta "Kockanje mladih u Hrvatskoj" čiji je voditelj doc.dr. sc. Neven Ricijaš. Istraživanje je provedeno na uzorku od ukupno 105 roditelja (M=40, Ž=65) srednjoškolaca u Ivanić Gradu. Sudjelovanje u istraživanju bilo je anonimno temeljem prethodno sastavljene šifre. Istraživanje je provedeno grupno, na roditeljskim sastancima u školama, a po principu papir-olovka. Iz sveobuhvatne baterije instrumenata u upitniku za roditelje, za potrebe ovog istraživanja korišten je dio instrumentarija: Upitnik o općim i socio-demografskim podacima, Skala stavova o kockanju, Upitnik aktivnosti kockanja i Upitnik South Oaks Gambling Screen (SOGS). Rezultati istraživanja pokazuju kako je većina roditelja kockala barem jednom u životu što potvrđuju podaci o igranju lota (72,4%), jednokratnih srećki (52,4%) i sportskog klađenja (15,2%). Istraživanjem su utvrđene razlike po spolu s obzirom na učestalost kockanja, kao i razlike s obzirom na specifičnu vrstu igara na sreću, na način da očevi kockaju češće od majki, pri čemu je najzastupljenije igranje lota, a najmanje prisutno igranje ruleta u kasinu kod oba roditelja. Sukladno očekivanom, rezultati upućuju kako većina roditelja (90,7%) nema izražene probleme s kockanjem, odnosno, za njih devetero su utvrđeni problemi s kockanjem. Istraživanjem su potvrđeni pretežito negativni stavovi o kockanju kod oba roditelja, a značajnije razlike po spolu nije bilo.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Survey of parents measured sports betting participation (15.2%) and SOGS problem gambling; could report problem gambling among sports bettors.

**Решение:** =

---

### 1121 · R5892

**Subtyping Gambling Acitivities: Case of Korca City, Albania**

2016 · European Journal of Multidisciplinary Studies · article · en · https://doi.org/10.26417/ejms.v1i3.p73-81

Gambling research has grown dramatically over the past 2-3 decades, however a lack of consensus regarding the risk factors and gambling etiology related to youth problem gambling still remain. So a better understanding of the nature of youth problem gambling could help us to clarify the etiology of gambling problems. Understanding gambling subtypes is necessary to improve our understanding of the etiology of problem gambling. The prediction of problem gambling is related with the participation in gambling activities. It is necessary to obtain a structure of gambling activities, in order to better understand gambling related problems and to treat problems in a more specified manner. The aim of the study was to determine the appropriate structure of gambling activities using factor analysis in a confirmatory framework. Students are a particularly interesting population in which to study gambling. The research utilized a cross-sectional design and self-report questionnaires. The study concludes that the two-factor solution better represents the chance-and skill-based gambling activities. The first factor is most strongly associated with chance-based activities (lottery, bingo, scratch cards). The second factor is most strongly associated with activities that require some degree of skill (poker, roulette, sport bet, racing, etc. ).

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Student survey measured participation in activities including sports betting and focused on youth problem gambling; whether a PG instrument was used is unclear.

**Решение:** =

---

### 1122 · R5902

**The Problem of Gambling Addiction — Sports Betting Shops in Mostar**

2016 · Obnovljeni život : časopis za filozofiju i religijske znanosti · article · hr

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the title points to sports betting shops and gambling addiction in Mostar, possibly a survey. The full text is needed.

**Решение:** =

---

### 1123 · R5914

**Sociodemographic Correlates and Morbidity in Lottery Gamblers: Results from a Population Survey.**

2016 · Journal of gambling studies · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1007/s10899-015-9534-1

The aim of the current study was to examine the socio-demographic correlates, the association of mental and physical illness, and the prevalence of pathological gambling among three groups (1) those with lottery gambling only (2) those with lottery and other types of gambling and (3) those with other types of gambling only-such as playing cards, sports betting, horse racing, casino gambling etc. Data was used from a nationwide cross-sectional epidemiological nationally representative survey of the resident (Singapore Citizens and Permanent Residents) population in Singapore of 6616 Singaporean adults aged 18 years and older. All respondents were administered the South Oaks Gambling Screen to screen for pathological gambling. The diagnoses of mental disorders were established using the Composite International Diagnostic Interview and relevant socio-demographic data was collected using a structured questionnaire. Lottery gambling was by far the most popular form of gambling in Singapore, with 83.5 % of those who had ever gambled indicating that they had participated in lottery gambling. Those who participated in lottery gambling alone were more likely to belong to the older age group (as compared to the 18-35 years age group), be of Indian ethnicity, have a secondary or vocational education, and earn a lower income as compared to the other two groups. Our findings that those with pure lottery gambling were significantly less likely to be pathological gamblers and had significantly lower odds of psychiatric and physical morbidity as compared to the other two groups are unique and need further research.

**ИИ:** + · обе модели · опрос населения об азартных играх · Nationally representative Singapore survey using SOGS; sports betting measured among gambling types; activity breakdown likely.

**Решение:** =

---

### 1124 · R5915

**Gambling Motives in a Representative Swedish Sample of Risk Gamblers.**

2016 · Journal of gambling studies · journal article, journalarticle, article · eng · https://doi.org/10.1007/s10899-016-9607-9

Motives for gambling have been shown to be associated with gambling involvement, and hence important in the understanding of the etiology of problem gambling. The aim of this study was to describe differences in gambling motives in different subgroups of lifetime risk gamblers, categorized by: age, gender, alcohol- and drug habits and type of game preferred, when considering the level of risk gambling. A random Swedish sample (n = 19,530) was screened for risk gambling, using the Lie/Bet questionnaire. The study sample (n = 257) consisted of the respondents screening positive on Lie/Bet and completing a postal questionnaire about gambling and motives for gambling (measured with the NODS-PERC and the RGQ respectively). When considering the level of risk gambling, motives for gambling were not associated with gender, whereas younger persons gambled for the challenge more often than did older participants. Card/Casino and Sport gamblers played to a greater extent for social and challenge reasons then did Lotto/Bingo-gamblers. EGM-gamblers played more for coping reasons than did Lotto/Bingo gamblers. However, this association turned non-significant when considering the level of risk gambling. Moderate risk gamblers played for the challenge and coping reasons to a greater extent than low risk gamblers motives for gambling differ across subgroups of preferred game and between gamblers with low and moderate risk. The level of risk gambling is intertwined with motives for gambling and should be considered when examining gambling reasons.

**ИИ:** разошлись — Opus -5 (выборка набрана по проблемам с игрой: лечение, горячая линия, самоисключение, сравнение проблемных игроков с контролем: The analysed sample includes only Lie/Bet-positive risk gamblers, so it cannot give the prevalence of problem gambling among sports bettors in general.); Sonnet ? (другое: Swedish population screen (Lie/Bet) but analysed sample is only screen-positive risk gamblers; sport gamblers compared by risk level (NODS-PERC), so usable figures are possible but unclear.)

**Решение:** ?

---

### 1125 · R5924

**Media Bets. El impacto digital sobre los jugadores y empresas de apuestas deportivas**

2016 · Universitat Jaume I · bachelor thesis, dissertation · es · http://hdl.handle.net/10234/163898

Treball de Final de Grau en Periodisme. Codi: PE0932. Curs acadèmic 2015-2016

**ИИ:** ? · обе модели · нет аннотации · Journalism bachelor thesis on sports bettors and betting firms; no abstract, so it's unclear whether bettors were surveyed with a PG instrument.

**Решение:** =

---

### 1126 · R5930

**Substance use and gambling among children in juvenile detention (diagnostic) centres in the Czech Republic**

2016 · Digital Repository (National Repository of Grey Literature) · dissertation · cs

Background: Various studies describe the emergence of addiction as a negative interplay of bio- psycho- social factors. It was found that children and adolescents who get into diagnos- tic institutions are exposed to multiple factors that increase the likelihood of developing problematic behaviours, substance abuse and gambling than the general population. It is thus likely that in the future they will be more vulnerable to addiction than the general population. Objectives: Main goals of this research were to provide an overview of the situation of sub- stance abuse among children and adolescents in diagnostic institutes in the Czech Republic and to compare selected data with results of the European School Survey Project on Alcohol and Other Drugs of 2011 (ESPAD). Another objective was to find the specifics of drug abuse and gambling in clients of diagnostic centres in different parts of the Czech Republic. Methods: Data for this study were collected by the interviewer using a questionnaire, which was inspired by the questionnaire from the ESPAD survey and was also extended to include issues related to gambling. Data were processed by descriptive analysis in MS Excel. Results: The results show that boys use addictive substances and play betting games more often than girls. Daily smoking was...

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Questionnaire survey of youth in detention centres with ESPAD-based gambling questions; unclear whether a PG screen and sports betting were measured.

**Решение:** =

---

### 1127 · R5939

**Online and sports betting**

2016 · article · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the title fits sports betting, but it could be a report chapter, a review or an empirical study.

**Решение:** =

---

### 1128 · R5944

**European football clubs and football betting among the youths in Nigeria**

2016 · Soccer and Society · article, journal-article · en · https://doi.org/10.1080/14660970.2016.1267625

European football clubs are very popular social realities in Nigeria. Their existence and activities shape social relations, process and outcomes of well-being as well as socio-economic and policy orthodoxies. Unfortunately, social trajectories of well-being, economic ramifications and policies remain poorly understood in Nigeria. What some people are aware of is the popularity of the clubs and not the intensification of associated implications and policy remits in existential environments of their social spaces. This is particularly important as the domains of European football clubs’ presence in developing countries, especially Nigeria, are largely nascent and haphazard. Against this background, this article examined the phenomenon of football betting as an ancillary of European football clubs’ presence among the youths in Nigeria. This article makes important contribution to understanding of ways European football identities are interlinked to the increased popularity of betting syndicates especially in Sub-Saharan Africa. Research questions engaged include; what is the pattern involved in football betting among the youths? What are the factors facilitating football betting among the youths and What are the perceived developmental implications relative to well-being and social health in Nigeria? The Social Exchange theoretical tradition was adopted as theoretical framework. Data collection triangulated quantitative method (questionnaires) and qualitative methods. Relevant findings were made and valid conclusions were reached and presented in this article.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Questionnaire survey of young football bettors in Nigeria; the abstract doesn't say whether a problem-gambling instrument was used.

**Решение:** =

---

### 1129 · R5945

**Las apuestas deportivas online: una aproximación sectorial**

2016 · Dialnet (Universidad de la Rioja) · article · es

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: Title ('a sectoral approach') points to an industry/economic analysis of online sports betting, not a survey using a problem-gambling instrument.); Sonnet ? (нет аннотации: No abstract; the title ("online sports betting: a sector approach") suggests a sector overview, but it could include survey data on problem gambling.)

**Решение:** ?

---

### 1130 · R5949

**Electronic transactions in web pages of online betting : profile of Greek internet betting player**

2016 · Νημερτής · dissertation · gr

Η παρούσα διπλωματική εργασία εκπονήθηκε με στόχο να περιγράψει τις ηλεκτρονικές συναλλαγές που λαμβάνουν χώρα στο διαδίκτυο και συγκεκριμένα σε ιστοσελίδες εταιρειών τυχερών παιχνιδιών και στοιχηματισμού, αλλά και να διερευνήσει τον τρόπο με τον οποίο ποντάρουν οι Έλληνες παίκτες στο διαδικτυακό στοίχημα αναλύοντας το προφίλ τους όσο γίνεται πληρέστερα. Γίνεται ανάλυση των ηλεκτρονικών συναλλαγών, αναφέροντας τους τρόπους τους οποίους μπορεί να χρησιμοποιήσει ένας παίκτης για να κάνει κατάθεση ή ανάληψη από ιστοσελίδες διαδικτυακού στοιχηματισμού και να παίξει στοίχημα σε αυτές τις εταιρείες ηλεκτρονικού τζόγου. Επίσης γίνεται ανάλυση των μεθόδων που χρησιμοποιούνται έτσι ώστε να διασφαλιστεί η ασφάλεια των συναλλαγών μέσω διαδικτύου και συγκεκριμένα στις εταιρείες διαδικτυακού στοιχηματισμού. Επιπλέον γίνεται αναφορά στο νομικό πλαίσιο που διέπει το χώρο του διαδικτυακού στοιχηματισμού στην Ελλάδα. Η έρευνα που έγινε αφορά τις συνήθειες και τον τρόπο παιχνιδιού Ελλήνων οι οποίοι στοιχηματίζουν στο διαδίκτυο. Τα αποτελέσματα έδειξαν ότι οι παίκτες, οι οποίοι στην πλειοψηφία τους είναι άνδρες νεαρής σχετικά ηλικίας, εμπιστεύονται τις διαδικτυακές στοιχηματικές εταιρείες, νιώθουν ασφάλεια όταν συναλλάσονται με αυτές, στοιχηματίζουν με αρκετά μεγάλη συχνότητα στα αγαπημένα τους αθλήματα και προσδοκούν σε κέρδη με λογικές αποδόσεις αλλά ενώ γνωρίζουν το σωστό τρόπο παιχνιδιού παρασύρονται αρκετές φορές.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Thesis surveying Greek online sports bettors on their habits; the abstract doesn't say whether a problem-gambling instrument was used.

**Решение:** =

---

### 1131 · R5950

**Ηλεκτρονικές συναλλαγές σε σελίδες διαδικτυακού στοιχηματισμού : προφίλ του Έλληνα παίκτη διαδικτυακού στοιχήματος**

2016 · article · el

This thesis has been prepared in order to describe the electronic transactions that take place on the internet and specifically gaming companies websites and betting, and to investigate how the Greek players wager at online betting analyzing their profile as it gets better . An analysis of electronic transactions, stating the means which may be used by a player to make a deposit or withdraw from online gambling sites and play bet on these online gambling companies. Also an analysis of the methods used in order to ensure the security of transactions over the Internet and in particular to online gambling companies. Further reference is made to the legal framework governing the area of online gambling in Greece. The survey relates to the habits and the way the Greeks play who gamble online. The results showed that the players, who are mostly men young of age, trust the online betting companies feel secure when transactions are done with them, bet relatively frequently in their favorite sports and expect to profit with reasonable returns but while knowing the right game mode lured several times.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Greek thesis surveying online sports bettors on habits and trust; the abstract does not say whether a problem-gambling instrument was used.

**Решение:** =

---

### 1132 · R5951

**Ηλεκτρονικές συναλλαγές σε σελίδες διαδικτυακού στοιχηματισμού : προφίλ του Έλληνα παίκτη διαδικτυακού στοιχήματος**

2016 · review

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Greek thesis-like record profiling Greek online bettors; no abstract, unclear whether a problem-gambling instrument was used.

**Решение:** =

---

### 1133 · R5978

**Do Bettors Correctly Perceive Odds? Three Studies of How Bettors Interpret Betting Odds as Probabilistic Information**

2015 · Journal of Behavioral Decision Making · review, article, journal-article · en · https://doi.org/10.1002/bdm.1851

Abstract This paper reports on three studies investigating how accurately bettors (=people who regularly bet on sports events) interpret the probabilistic information implied by betting odds. All studies were based on data collected by web surveys prompting a total of 186 experienced bettors to convert sets of representative odds into frequency judgments. Bayesian statistical methods were used to analyze the data. From the results, the following conclusions were made: (i) On the whole, the bettors produced well‐calibrated judgments, indicating that they have realistic perceptions of odds. (ii) Bettors were unable to consciously adjust judgments for different margins. (iii) Although their interval judgments often covered the estimates implied by the odds, the bettors tended to overestimate the variation of expected profitable bets between months. The results are consistent with prior research showing that people tend to make accurate probability judgments when faced with tasks characterized by constant and clear feedback. Copyright © 2015 John Wiley &amp; Sons, Ltd.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Web surveys of 186 experienced sports bettors on how they perceive odds; abstract doesn't say whether a problem-gambling screen was used.

**Решение:** =

---

### 1134 · R5985

**A Betting Experience Based on User Behaviour**

2015

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the title suggests designing a betting platform around user behaviour, and a problem-gambling survey can't be ruled out.

**Решение:** =

---

### 1135 · R5986

**Adaptation study of the Turkish version of the Gambling-Related Cognitions Scale (GRCS-T).**

2015 · Journal of gambling studies · article, journal article, validation study · eng · https://doi.org/10.1007/s10899-013-9414-5

Abstract This study aimed to adapt and to test the validity and the reliability of the Turkish version of the Gambling-Related Cognitions Scale (GRCS-T) that was developed by Raylu and Oei (Addiction 99(6):757–769, 2004a). The significance of erroneous cognitions in the development and the maintenance of gambling problems, the importance of promoting gambling research in different cultures, and the limited information about the gambling individuals in Turkey due to limited gambling research interest inspired the present study. The sample consisted of 354 voluntary male participants who were above age 17 and betting on sports and horse races selected through convenience sampling in betting terminals. The results of the confirmatory factor analysis following the original scale’s five factor structure indicated a good fit for the data. The analyses were carried out with 21 items due to relatively inadequate psychometric properties of two GRCS-T items. Correlational analyses and group comparison tests supported the concurrent and the criterion validity of the GRCS-T. Cronbach’s alpha coefficient for the whole scale was 0.84 whereas the coefficients ranged between 0.52 and 0.78 for the subscales of GRCS-T. The findings suggesting that GRCS-T is a valid and reliable instrument to identify gambling cognitions in Turkish samples are discussed considering the possible influence of the sample make-up and cultural texture within the limitations of the present study and in the light of the relevant literature.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Turkish sample of sports and horse race bettors; criterion validity tests suggest a problem-gambling screen, but the abstract doesn't name one.

**Решение:** =

---

### 1136 · R6008

**Navike kockanja srednjoškolaca u dvije urbane sredine u Bosni i Hercegovini**

2015 · Socijalne teme : Časopis za pitanja socijalnog rada i srodnih znanosti · article · bos · https://hrcak.srce.hr/177306

The aim of this paper is to get insight in gambling habits of adolescents in urban areas of Bosnia and Herzeegovina, and confirm the precentage of adolescents which are in risk or have already developed gambling problems. The study included 1036 students, from first to final grade of high school, vocational and vocational-technical high school programs. It was assumed that most high school students gamble on sports betting, then the lottery games of chance and slot machine clubs, while other kinds are less common and that there are differences in gambling activities considering age so that older adolescents gamble more intense and frequent. The survey showed that 70% of high school students gambled at least once in their life. The young usually play sports betting, gamble online for money and play TV bingo, while less than a tenth of students go to casino on a weekly basis, which indicates the severity of the gambling population. Cilj ovog rada bio je dobiti uvid u navike kockanje adolescenata u urbanim sredinama BiH, te utvrditi udio adolescenata koji su u riziku razviti, ili su već razvili, probleme s kockanjem. U istraživanju je sudjelovalo 1036 učenika, od prvog do završnog razreda gimnazijskog, stručnog i stručno-tehničkog srednjoškolskog programa. Pretpostavilo se da srednjoškolci najviše kockaju u sportskim kladionicama, zatim u lutrijskim igrama na sreću i automat klubovima, dok su ostale vrste manje zastupljene, te da postoje razlike u kockarskim aktivnostima s obzirom na dob na način da stariji maloljetnici kockaju intenzivnije i učestalije. Istraživanje je pokazalo da je skoro 70% srednjoškolaca barem jedanput u životu kockalo. Mladi najčešće igraju sportske kladionice, kockaju na internetu za novac i igraju TV bingo, dok manje od desetine učenika odlazi u casino na sedmičnom nivou što nam govori o ozbiljnosti kockanja ove populacije.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · High school survey (n=1036) measured sports betting and the share at risk or with gambling problems; the instrument isn't named.

**Решение:** =

---

### 1137 · R6009

**Gambling Habits of Adolescents in two Urban Areas of Bosnia and Herzegovina**

2015 · review

The aim of this paper is to get insight in gambling habits of adolescents in urban areas of Bosnia and Herzeegovina, and confirm the precentage of adolescents which are in risk or have already developed gambling problems. The study included 1036 students, from first to final grade of high school, vocational and vocational-technical high school programs. It was assumed that most high school students gamble on sports betting, then the lottery games of chance and slot machine clubs, while other kinds are less common and that there are differences in gambling activities considering age so that older adolescents gamble more intense and frequent. The survey showed that 70% of high school students gambled at least once in their life. The young usually play sports betting, gamble online for money and play TV bingo, while less than a tenth of students go to casino on a weekly basis, which indicates the severity of the gambling population.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Adolescent survey (n=1036) measuring sports betting participation and at-risk/problem gambling; instrument unnamed but implied. Tagged 'Review' yet empirical.

**Решение:** =

---

### 1138 · R6032

**Il comportamento dei consumatori nelle scelte di acquisto on line: un’analisi del settore delle scommesse sportive in Italia**

2015 · article · it · https://doi.org/10.2382/82990

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Italian consumer-behaviour study of online sports bettors with no abstract; it may be a bettor survey, but problem-gambling measurement is unknown.

**Решение:** =

---

### 1139 · R6033

**On Consumer Behaviour and Customer On Line Purchasing Motivation: An Empirical Investigation into the Sports-Betting Industry in Italy**

2015 · Economia dei Servizi · article · en · https://doi.org/10.2382/82990:y:2015:i:1:p:17-40

In the last few years, the increase in the use of the Internet and the development of web based technologies have brought about significant changes in consumer behaviour in Italy in a multiplicity of industrial and service sectors. This has also come about in one of the main service industries in terms of sales, namely that of regulated gambling. The laws legalizing on-line betting beginning in 2007 are in fact facilitating the transfer of a relevant part of gambling sales from the traditional channel of distribution, of a physical type, to the digital type, particularly in the sports-betting segment. The aim of the work is to analyse in what way the Internet has influenced consumer behaviour in the sports-betting industry in Italy, by redefining the traditional distribution channels. From the methodological viewpoint for the purpose of the analysis, in addition to the processing of a series of data deriving from indirect sources, an empirical investigation is carried out on a consumer sample gambling on legal sportsbetting sites in Italy. The analysis has permitted identifying structural features of electronic distribution channels, which favour the purchase of sports bets via Internet, and to understand in what way they influence the various stages of consumer behaviour.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of Italian online sports bettors focused on consumer purchasing behaviour; abstract doesn't say whether a problem-gambling instrument was used.

**Решение:** =

---

### 1140 · R6039

**Heuristic and analytic processing in online sports betting.**

2015 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-013-9438-x

This article presents the results of two studies that examine the occurrence of heuristic (i.e., intuitive and fast) and analytic (i.e., deliberate and slow) processes among people who engage in online sports betting on a regular basis. The first study was qualitative and was conducted with a convenience sample of 12 regular online sports gamblers who described the processes by which they arrive at a sports betting decision. The results of this study showed that betting online on sports events involves a mix of heuristic and analytic processes. The second study consisted in a survey of 161 online sports gamblers where performance in terms of monetary gains, experience in online sports betting, propensity to collect and analyze relevant information prior to betting, and use of bookmaker odds were measured. This study showed that heuristic and analytic processes act as mediators of the relationship between experience and performance. The findings stemming of these two studies give some insights into gamblers' modes of thinking and behaviors in an online sports betting context and show the value of the dual mediation process model for research that looks at gambling activities from a judgment and decision making perspective.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of 161 online sports bettors; the abstract lists no problem-gambling measure, but one may appear in the sample description.

**Решение:** =

---

### 1141 · R6048

**Individual, Family and Peer Variables Associated with Adolescent Sports Betting in Croatia**

2015 · Journal of Behavioral Addictions · conference object, article · en · https://www.bib.irb.hr/755857

Today’s generation of young people in Croatia is the first growing up in a society where gambling is widespread, available and often socially accepted. Despite the fact that all types of gambling are prohibited for minors, they participate in these activities to a large extent, sports betting being one of the most represented games, especially among boys (Ricijas, et al. 2011.). Therefore, this research was conducted on a sample of N=1, 330 male high-school students from seven Croatian cities with the main objective to explore individual, family and peer variables associated with adolescent sports betting. In order to meet this goal, an extensive battery of instruments was used: (1) Questionnaire on basic socio-demographic characteristics, (2) Gambling activities questionnaire, (3) Canadian adolescents gambling inventory - CAGI (Tremblay et al., 2010.), (4) Motivation for gambling checklist, (5) Gambling beliefs scale, (6) Risk and delinquent behavior questionnaire (Atlanta et al., 2005.). The results show that boys who bet more intensely have developed more serious psychosocial consequences, are more motivated for gambling, and are more prone to cognitive distortions and normative beliefs related to gambling. Additionally, they are more likely to have parents who participate in games of chance and who are familiar with their gambling. The results will be interpreted in relation to the existing social circumstances and in the context of prevention/treatment interventions.

**ИИ:** + · обе модели · беттеры + инструмент · Survey of 1,330 adolescent boys on sports betting that used the CAGI, which includes a problem-gambling severity subscale.

**Решение:** =

---

### 1142 · R6049

**National estimates of Australian gambling prevalence: f indings from a dual‐frame omnibus survey**

2015 · Addiction · article · en · https://doi.org/10.1111/add.13176

BACKGROUND, AIMS AND DESIGN: The increase in mobile telephone-only households may be a source of bias for traditional landline gambling prevalence surveys. Aims were to: (1) identify Australian gambling participation and problem gambling prevalence using a dual-frame (50% landline and 50% mobile telephone) computer-assisted telephone interviewing methodology; (2) explore the predictors of sample frame and telephone status; and (3) explore the degree to which sample frame and telephone status moderate the relationships between respondent characteristics and problem gambling. SETTING AND PARTICIPANTS: A total of 2000 adult respondents residing in Australia were interviewed from March to April 2013. MEASUREMENTS: Participation in multiple gambling activities and Problem Gambling Severity Index (PGSI). FINDINGS: Estimates were: gambling participation [63.9%, 95% confidence interval (CI) = 61.4-66.3], problem gambling (0.4%, 95% CI = 0.2-0.8), moderate-risk gambling (1.9%, 95% CI = 1.3-2.6) and low-risk gambling (3.0%, 95% CI = 2.2-4.0). Relative to the landline frame, the mobile frame was more likely to gamble on horse/greyhound races [odds ratio (OR) = 1.4], casino table games (OR = 5.0), sporting events (OR = 2.2), private games (OR = 1.9) and the internet (OR = 6.5); less likely to gamble on lotteries (OR = 0.6); and more likely to gamble on five or more activities (OR = 2.4), display problem gambling (OR = 6.4) and endorse PGSI items (OR = 2.4-6.1). Only casino table gambling (OR = 2.9) and internet gambling (OR = 3.5) independently predicted mobile frame membership. Telephone status (landline frame versus mobile dual users and mobile-only users) displayed similar findings. Finally, sample frame and/or telephone status moderated the relationship between gender, relationship status, health and problem gambling (OR = 2.9-7.6). CONCLUSION: Given expected future increases in the mobile telephone-only population, best practice in population gambling research should use dual frame sampling methodologies (at least 50% landline and 50% mobile telephone) for telephone interviewing.

**ИИ:** + · обе модели · опрос населения об азартных играх · National Australian prevalence survey measuring sports betting participation and PGSI; it could report problem gambling among sports bettors.

**Решение:** =

---

### 1143 · R6050

**Non è vero, però... Calcio e superstizione: dalla superstizione del capitano a quella nella pratica del Totocalcio e delle scommesse sportive**

2015 · Institutional Research Information System University of Turin (University of Turin) · book-chapter · it

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: Italian book chapter on football superstition and Totocalcio/sports betting; looks like a cultural essay, unlikely to use a problem-gambling instrument.); Sonnet ? (нет аннотации: Italian chapter on superstition in football and Totocalcio/sports betting; no abstract, unclear whether it is empirical or measured problem gambling.)

**Решение:** ?

---

### 1144 · R6054

**The Risks of Online Gambling for Younger Males: Insights from Czech National Surveys**

2015 · review, article · en

Live online betting has the potential to become a universal tool for gambling with a high potential for problems thanks to its broad availability (temporal, local, financial, and social) and the flexibility in the ways of treating and gaining rewards.Gambling, generally, has a whole system of specific characteristics and mechanisms. There are some common phenomena, like chasing loses, belief in the possibility for betterment, and searching. However, there are many types of gambling. Each type of gambling has specific, attractive features. Sport gamblers, slot machine players, poker players, casino players - these are the groups of people who have slightly different perspectives on gambling and its positives and negatives; they have different motivations for gambling (conscious and unconscious). In an online environment, gambling becomes more accessible and also more flexible in terms of the game features offered to players. With online gambling, there has also emerged a new type of gambling – live online betting. At first glance it may seem to be just another form of gambling. However, live online betting is more flexible and multifunctional, and it can be handled in different ways. The game can be immediate or long-term, social or solitary, expert or thoughtless, adrenaline or relaxation. From this point of view, live online betting may expose more people to gambling and possibly trap them with addiction or problems.

**ИИ:** ? · обе модели · другое · Abstract reads like a commentary on live betting, but the title cites Czech national surveys, which may have measured problem gambling by activity.

**Решение:** =

---

### 1145 · R6055

**Las apuestas deportivas en jóvenes y adolescentes: nuevas formas de juego**

2015 · Dialnet (Universidad de la Rioja) · article · es

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; title on sports betting in youth and adolescents could be a survey that measured problem gambling, or a commentary.

**Решение:** =

---

### 1146 · R6060

**Convergence of gambling and gaming in digital media**

2015 · Acquire (CQUniversity) · report · en

This project aimed to examine the following research questions provided by the Victorian Responsible Gambling Foundation:Are gaming and gambling converging, in what ways and to what extent? To what extent are young people being exposed to gambling-like content through games? What influence do gambling-like elements and simulated gambling in games have on young people's gambling behaviour? What are the likely long term consequences for young people exposed to gambling-like experiences through gaming? How are gambling-like games marketed and promoted to young people, and what impact does this marketing have?Literature review Are gaming and gambling converging, in what ways and to what extent? It is clear that the products within gaming and gambling industries are converging in multiple ways.Convergence of gambling and gaming in digital media Gainsbury, King, Abarbanel, Delfabbro & Hing Victorian Responsible Gambling Foundation Page 12 Gambling games allow young people to engage with gambling without spending money.These games may increase their confidence in winning at gambling, perception of personal skill and their risk taking within gambling. For some young people, playing gambling games may substitute for or reduce gambling, particularly if gambling-themed games are viewed to be as fun and enjoyable as gambling for a lower (or no) cost. Currently, there is no firm evidence on the consequences of gambling-themed games for young people.The impact is likely to differ based on young people's individual characteristics and other factors in their psycho-social environment.How are gambling-like games marketed and promoted to young people, and what impact does this marketing have? The lack of age restrictions on gambling-themed games means that advertisements for these may be viewed by young people. Research from broader public health fields indicates that young people are vulnerable to the impacts of marketing. Content Analysis of Advertisements Present in Social Media and General Internet Use Screen-shots of advertisements for gambling and gambling-themed games were collected by 20 student participants recruited from the University of Adelaide's School of Psychology over one week based on their typical Internet and social media use. This study used a content analysis to map the textual and visual content of the different advertisements.Coding was independently conducted by two researchers. The majority of captured advertisements were for gambling-themed games played on social network services (SNS), with about one third of advertisements for Internet gambling products and a small number for tournament or competition, live venue gambling, and stand-alone games. The majority of advertisements came from companies that are not regulated in Australia. Nearly three quarters of advertisements were captured during Facebook use, with a small number from Twitter, Instagram, and YouTube. The most advertised game type was slots, followed by race/sports betting, general casino, poker, blackjack, video poker, and bingo. The visual display of advertisements typically featured: bright colours, character images of young adults, cartoon animal characters, gambling activities, sporting activities, references to popular culture and references to Las Vegas. Marketing techniques typically used included: calls to action (such as "Play Game," "Install Now," or "Download") and game and location specific language (e.g., pokies).Benefits

**ИИ:** ? · обе модели · другое · Multi-component report; the abstract is truncated and may include a youth survey of gambling activities with a PGSI-type measure. Needs full-text check.

**Решение:** =

---

### 1147 · R6061

**The interaction between gambling activities and modes of access: a comparison of Internet-only, land-based only, and mixed-mode gamblers.**

2015 · Addictive behaviors · article, comparative study, journal article · eng · https://doi.org/10.1016/j.addbeh.2014.09.023

Research suggests that Internet-based gambling includes risk factors that may increase gambling problems. The current study aimed to investigate subgroups of gamblers to identify the potential harms associated with various forms and modes of gambling. An online survey was completed by 4,594 respondents identified as Internet-only (IG), land-based only (LBGs), or mixed-mode (MMG) gamblers based on self-reported gambling behaviour in the last 12months. Results showed significant socio-demographic differences between groups, with the LBGs being the oldest and MMGs the youngest. MMGs engaged in the greatest variety of gambling forms, had the highest average problem gambling severity scores, and were more likely to attribute problems to sports betting than the other groups. IGs were involved in the lowest number of divergent gambling activities, most likely to gamble frequently on sports and races, and attribute problems to these forms. Compared to the other groups, LBs had a higher proportion of problem gamblers than IGs and were most likely to play electronic gaming machines weekly, with this form of gambling contributing to problems at a substantially greater rate. This study confirms the importance of considering gambling involvement across subgroups of Internet or land-based gamblers. There is a need to consider the interaction between forms and modes of gambling to advance our understanding of the potential risk of mode of gambling to contribute to problems.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Online survey of 4,594 gamblers that measured problem gambling severity and sports betting participation; it may report PG by activity.

**Решение:** =

---

### 1148 · R6062

**Who bets on sports? Some further empirical evidence using German data**

2015 · International Review for the Sociology of Sport · article, journalarticle, review · en · https://doi.org/10.1177/1012690215597650

Given the rapid expansion of the German sports-betting market and recent changes in market regulations, it is interesting to reexamine the socioeconomic profile of German sports bettors: Who bets on sports? In order to analyse this question, this study used an online survey to collect data on sports-betting behaviour ( N =634). It modelled participation in sports betting by means of a logit model that recovers determinants of a person’s propensity to participate in sports betting. Results show that the typical sports-bettor is 32 years old and male, has a low household income, is highly interested in sports, and is willing to take risks.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · German online survey of sports-betting participation; the abstract doesn't say whether a problem-gambling instrument was used.

**Решение:** =

---

### 1149 · R6063

**The link between competitive sports and gambling behaviors among youths.**

2015 · The American journal on addictions · journal article · eng · https://doi.org/10.1111/ajad.12189

This study examines the association between physical activities and gambling, making a distinction between two characteristics of the former: intensity level and type (competitive/non-competitive). 316 adolescents from four high schools in Israel completed questionnaires. For males, participation in competitive athletic sports was associated with gambling frequency and problem gambling. For females, participation in competitive athletic sports was associated only with gambling frequency. Both types of physical activity and gender are important when analyzing the association between gambling and sporting activities. Youths involved in competitive sports are at greater risk for gambling involvement. (Am J Addict 2015;24:200-202).

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Adolescent survey measured problem gambling; unclear whether sports betting participation (e.g., Toto/Winner) was assessed.

**Решение:** =

---

### 1150 · R6064

**The Social and Psychological Impacts of Gambling in the Cree Communities of Northern Québec**

2015 · Journal of Gambling Studies · article · en · https://doi.org/10.1007/s10899-015-9553-y

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; likely a community gambling survey that may have used a PG screen and recorded gambling activities including sports betting.

**Решение:** =

---

### 1151 · R6076

**Einfluss der wahrgenommenen Verfügbarkeit von Glücksspielangeboten und des Kontakts mit Glücksspielwerbung auf das Glücksspielverhalten im jungen Erwachsenenalter**

2015 · Suchttherapie · article · de · https://doi.org/10.1055/s-0035-1557563

Einleitung: Untersucht wird der Einfluss der wahrgenommenen Verfügbarkeit von Glücksspielangeboten und des Kontakts mit Glücksspielwerbung auf das Glücksspielverhalten im jungen Erwachsenenalter. Methoden: Querschnittliche Befragung von 4.617 Schüler/innen aus Berufsschulen und Gymnasien in Schleswig-Holstein und Nordrhein-Westfalen (mittleres Alter = 18,7 Jahre; Range = 13 bis 25 Jahre). Die Erhebung erfolgte mittels Papierfragebogen zwischen Februar und Juli 2014. Die wahrgenommene Verfügbarkeit von Spielangeboten wurde über die Quantität der Glücksspielmöglichkeiten im Alltag einer Person und die Entfernung zwischen dem Wohnort und der nächsten Glücksspielmöglichkeit erfasst. Der Kontakt mit Glücksspielwerbung wurde über individuelle Kontakthäufigkeiten zu sowie die korrekte Markenerkennung von 10 Glücksspielwerbungen erhoben. Outcomes waren die Lebenszeit- und 12-Monatsprävalenz des Glücksspielens, die Glücksspielhäufigkeit sowie problematisches Glücksspiel nach dem South Oaks Gambling Screen (SOGS). Ergebnisse: Etwa ein Drittel der Stichprobe (32,2%) spielte im letzten Jahr privat um Geld, für kommerzielle Glücksspiele lag die Quote bei 42,3% (kombiniert: 52,1%). Regelmäßiges, mindestens monatliches privates Spielen um Geld fand sich bei 10,7% der Befragten, regelmäßiges Glücksspielen bei kommerziellen Anbietern wurde von 18,4% bestätigt, die meisten davon nutzten Sportwetten oder Geldspielautomaten. Von denjenigen, die im letzten Jahr um Geld gespielt hatten, erfüllten 9,8% das Kriterium für problematisches Spielen. Alle Glücksspieloutcomes waren signifikant positiv mit der wahrgenommenen Verfügbarkeit von Glücksspielangeboten und dem Kontakt mit Glücksspielwerbung assoziiert, auch nach Kontrolle einer Reihe von Störvariablen wie z.B. dem Alter, dem Geschlecht, dem sozioökonomischen Status, dem Glücksspielverhalten innerhalb der Familie sowie dem Erlebnishunger. Diskussion: Spielen um Geld ist im jungen Erwachsenenalter eine häufige Freizeitbeschäftigung. Die wahrgenommene Verfügbarkeit von Glücksspielangeboten und der Kontakt mit Glücksspielwerbung sind im Querschnitt mit der Lebenszeit-, der 12-Monatsprävalenz, der Glücksspielhäufigkeit sowie dem problematischen Glücksspiel assoziiert. Längsschnittliche Studien müssen diese ersten Befunde bestätigen. Förderhinweis: Ministerium für Soziales, Gesundheit, Wissenschaft und Gleichstellung des Landes Schleswig-Holstein.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Student survey (n=4,617) measuring sports betting participation and SOGS problem gambling; may report SOGS results by gambling activity.

**Решение:** =

---

### 1152 · R6077

**Glücksspielgesetzgebung in Deutschland und Glücksspielverhalten der Bevölkerung**

2015 · SUCHT - Zeitschrift für Wissenschaft und Praxis / Journal of Addiction Research and Practice · article · de · https://doi.org/10.1024/0939-5911.a000345

Zielsetzung: Bewirkt die Vergabe von 48 Sportwetten- und Online-Casino-Lizenzen sowie die Lockerung von Werberestriktionen in Schleswig-Holstein (SH) Veränderungen des Glückspielverhaltens der Bevölkerung? Methodik: Wiederholte Querschnittsbefragung repräsentativer Stichproben (≥ 16 Jahre) aus SH vs. dem übrigen Bundesgebiet. Vor (2012) und nach (2013) der Lizenzvergabe wurden jeweils 1.000 Personen in den beiden Untersuchungsregionen interviewt. Ergebnisse: 2012 betrug die 12-Monats-Prävalenz des Glücksspiels in SH 39,3%, in den übrigen Bundesländern 36,9% (p > 0,05). Im Jahr 2013 lag der Unterschied bei 39,0% vs. 33,6% (p < 0,05), vornehmlich aufgrund einer häufigeren Teilnahme an Lotterien in SH. Eine signifikante Interaktion zwischen Befragungsregion und Zeit zeigte sich jedoch nicht. Auf Ebene einzelner Glücksspiele ergaben sich ebenfalls keine unterschiedlichen Entwicklungen über die Zeit, allein der Anteil der Poker-Spielenden hatte in SH einen stärkeren Rückgang als in den anderen Bundesländern (p < 0,05). Keine Unterschiede fanden sich bei der Teilnahme an Glücksspielen im Internet und bei der Prävalenz des pathologischen Spielens. Schlussfolgerungen: Obwohl die 12-Monats-Prävalenz des Glücksspiels 2013 in SH bedeutsam höher lag als im übrigen Bundesgebiet, lässt sich aus den vorliegenden Daten keine spielfördernde Auswirkung der veränderten rechtlichen Rahmenbedingungen in SH auf das Glücksspielverhalten der Bevölkerung ableiten.

**ИИ:** + · обе модели · опрос населения об азартных играх · Representative population surveys in Germany measuring participation in individual gambling activities (including sports betting) and prevalence of pathological gambling.

**Решение:** =

---

### 1153 · R6082

**Characteristics and help-seeking behaviors of Internet gamblers based on most problematic mode of gambling.**

2015 · Journal of medical Internet research · comparative study, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.2196/jmir.3781

Previous studies of problem Internet gamblers have failed to distinguish whether their problem gambling relates to Internet or land-based gambling modes. Therefore, characteristics and help-seeking behaviors of people whose gambling problems relate specifically to Internet gambling are unknown, but could inform the optimal alignment of treatment and support services with the needs and preferences of problem gamblers. This study aimed to compare (1) characteristics of problem Internet gamblers and problem land-based gamblers and (2) uptake of different types and modes of help between problem Internet gamblers and problem land-based gamblers. Hypothesis 1 was that problem Internet gamblers are less likely to seek help. Hypothesis 2 was that problem Internet gamblers are more likely to use online modes of help. A sample of 620 respondents meeting criteria for problem gambling was drawn from an online survey of 4594 Australian gamblers. Respondents were recruited through advertisements on gambling and gambling help websites, Facebook, and Google. Measures consisted of gambling participation; proportion of gambling on the Internet; most problematic mode of gambling; help seeking from 11 different sources of formal help, informal help, and self-help for gambling problems; psychological distress (Kessler 6); problem gambling severity (Problem Gambling Severity Index, PGSI); and demographics. Problem Internet gamblers were significantly more likely than problem land-based gamblers to be male (χ(2) 1=28.3, P<.001, φ=0.21), younger (t616.33=4.62, P<.001, d=0.37), have lower psychological distress (χ(2) 1=5.4, P=.02, φ=0.09), and experience problems with sports and race wagering (χ(2) 4=228.5, P<.001, φ=0.61). Uptake of help was significantly lower among problem Internet compared to problem land-based gamblers (χ(2) 1=6.9, P<.001, φ=0.11), including from face-to-face services, gambling helplines, online groups, self-exclusion from land-based venues, family or friends, and self-help strategies. Both problem Internet and problem land-based gamblers had similarly low use of online help. However, problem land-based gamblers (37.6%, 126/335) were significantly more likely to have sought land-based formal help compared to problem Internet gamblers (23.5%, 67/285; χ(2) 1=14.3, P<.001, φ=0.15). The findings suggest that more targeted and innovative efforts may be needed to increase use of gambling help by problem Internet gamblers. Alternatively, their lower PGSI and K6 scores suggest Internet problem gamblers may have less need for gambling-related help. This is the first known study to classify problem Internet gamblers as those whose problem gambling specifically relates to Internet gambling. Further research is needed to better understand why help-seeking rates are lower among Internet problem gamblers.

**ИИ:** ? · обе модели · другое · The analysis covers only problem gamblers, but it draws on a PGSI survey of 4594 gamblers that measured participation; the full text may report sports betting figures.

**Решение:** =

---

### 1154 · R6083

**Sports bettors' responses to sports-embedded gambling promotions: Implications for compulsive consumption**

2015 · Journal of Business Research · article, review, journal-article · en · https://doi.org/10.1016/j.jbusres.2015.03.003

AbstractCommercial arrangements between sport organizations and gambling operators are resulting in extensive promotion of gambling during televised sport. This study aims to explore sports bettors' responses to these promotions, and whether this varies with problem gambling severity. Surveys with 544 Australian sports bettors with varying degrees of problem gambling severity indicate that problem gamblers have highest approval of these promotions. Compared to non-problem and at-risk gamblers, problem gamblers also report most encouragement and influence to gamble from these promotions. Problem gamblers are also more influenced to sports bet by contextual factors, particularly certain bet types and promotional appeals. Three theories are discussed to explain these results — product involvement, cue induced craving and classical conditioning. Given the rapid growth of sports betting, increasing sports betting problems, and inability to avoid gambling advertising while watching televised sport, further research is critical to understand how sports-embedded gambling promotions impact on gambling consumption and problem gambling. Research is also important to inform policy, given that sports-embedded advertising is a controversial practice prompting recent changes to broadcasting codes of practice. This exploratory study provides some foundations and future directions to inform this research effort.

**ИИ:** + · обе модели · беттеры + инструмент · Survey of 544 Australian sports bettors grouped by problem gambling severity (non-problem, at-risk, problem), likely PGSI.

**Решение:** =

---

### 1155 · R6084

**Sports-Embedded Gambling Promotions: A Study of Exposure, Sports Betting Intention and Problem Gambling Amongst Adults**

2015 · International Journal of Mental Health and Addiction · article, review, journal-article · en · https://doi.org/10.1007/s11469-014-9519-9

Community, media and government concerns have emerged about promoting sports betting during televised sports broadcasts, which now contain betting operators’ logos, signage, websites, commentary and betting odds. Despite large television audiences being exposed, limited research has examined how these promotions shape gambling behaviour, particularly amongst problem gamblers. Underpinned by the Theory of Reasoned Action, this study explored whether exposure and attitude to gambling promotions during televised sport predict sports betting intention and whether this relationship varies with problem gambling severity. Surveys were conducted with 1,000 adults in Queensland, Australia. Strongest predictors of greater intended frequency of sports betting were higher problem gambling severity, previous sports betting participation, more frequent exposure to the promotions, and more positive attitudes towards them. Results suggest that the audience most likely to be stimulated by these promotions are problem gamblers because they have greatest exposure and a favourable disposition to them, and report they have maintained or worsened their problem sports betting behaviours. Policy and public health interventions may be needed to counter these pervasive media messages.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Survey of 1,000 Queensland adults measuring problem gambling severity (likely PGSI) and past sports betting participation.

**Решение:** =

---

### 1156 · R6087

**The social and gender in fantasy sports leagues**

2015 · Swinburne figshare (Swinburne University of Technology) · article · en

No description available

**ИИ:** ? · обе модели · нет аннотации · No abstract; a fantasy sports study is possibly relevant, but it is unclear whether money was wagered or problem gambling was measured.

**Решение:** =

---

### 1157 · R6092

**Gender differences in the associations of gambling activities and suicidal behaviors with problem gambling in a nationally representative French sample.**

2015 · Addictive behaviors · journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1016/j.addbeh.2015.01.011

The objectives of the present study are to describe gender differences in factors associated with moderate risk and problem gambling. Data were extracted from the 2010 Health Barometer, a large survey on a representative sample of the general population aged 15-85 years living in France (n=27,653), carried out by the National Institute for Health Promotion and Health Education. Data were collected between October 2009 and July 2010. A computer-assisted telephone interview system was used. The findings indicate that men are three times more likely to experience problems with gambling. Men and women have different patterns of gambling activities. Men were more involved with Rapido, internet gambling, sports and racetrack betting, poker, and casino tables, whereas women gambled more often on scratch games. Both men and women engaging in immediate reward games were significantly more likely to experience difficulties with gambling. This association, however, was stronger in women. Furthermore, suicidal ideation and behaviors were more likely to be associated with gambling problems in women as compared to men. The study underscores the importance of considering gender-related differences in the study of gambling behaviors.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · National French survey that measured problem gambling (moderate risk/problem) and participation in gambling activities, including sports betting.

**Решение:** =

---

### 1158 · R6093

**An Exploration into the College Students’ Adherence Behavior of Illegal Sports Gambling**

2015 · article · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the title describes a study of college students' illegal sports gambling, which could include a problem-gambling measure.

**Решение:** =

---

### 1159 · R6096

**Third-person perceptions of gambling sponsorship advertising**

2015 · Sport Business and Management An International Journal · article · en · https://doi.org/10.1108/sbm-04-2015-0015

Purpose – The purpose of this paper is to examine perceptual and behavioural components of the third-person effect for sport sponsorship marketing communications by legalised gambling companies. Specifically, this research examines judgements about the perceived influence of gambling sponsorship on self, children, and other adults. It also investigates behavioural reactions towards the censorship of gambling sponsorship, and intentions to gamble with sponsors. Design/methodology/approach – An online survey was fielded to a commercial consumer database and yielded 511 usable responses. Four hypotheses were tested to examine perceptions of the effects of gambling sponsorship on self and on others, and whether perceived differences in self/other effects influenced pro-censorship behaviours and gambling intentions. Findings – Findings reveal a range of responses to sport sponsorship by gambling companies. Some individuals view gambling sponsorship positively, they are anti-censorship, and happy to bet with sponsors. Others, who bet on sports, but have no particular allegiance to gambling sponsors, appear highly protective of children, and endorse censorship. Research limitations/implications – This study focused on the perceived impact of gambling sponsorship on other adults and on children. Future research may consider targeting more specific groups such as other sports fans, others engaged in online sports betting, or primary/secondary school age children. Originality/value – This study provides new insights on sponsorship effects, specifically public perceptions of gambling sponsorship advertising and their associated behavioural consequences.

**ИИ:** разошлись — Opus -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Consumer survey of perceptions of gambling sponsorship, censorship attitudes and gambling intentions; no problem-gambling instrument indicated.); Sonnet ? (неясно, измеряли ли проблемную игру: Online survey of 511 consumers including sports bettors on gambling sponsorship perceptions; abstract doesn't say whether a problem-gambling instrument was used.)

**Решение:** ?

---

### 1160 · R6099

**Patterns and trends in gambling participation in the Quebec population between 2009 and 2012**

2015 · Canadian Journal of Public Health · article · en · https://doi.org/10.17269/cjph.106.4854

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: No abstract. This looks like a Quebec population gambling survey (ENHJEU 2009/2012) covering participation by activity; problem-gambling measures likely but unconfirmed.); Sonnet + (опрос населения об азартных играх: Quebec population gambling survey 2009-2012; likely measured activity participation and problem gambling (CPGI), so activity tables may give problem gambling among sports bettors. No abstract.)

**Решение:** ?

---

### 1161 · R6109

**Live Online Betting: The Answer to Every Gambler´s Wish**

2015 · review, article · en

Compared to offline gambling forms, online gambling has been hypothesized to lead to a heightened risk of developing gambling pathology. Suggestions about who the risks apply to have varied. In light of the finding that online gambling and the associated financial difficulties are reported mostly by younger males, some hypotheses identify younger males as an at-risk group. An alternative possibility is that younger males simply display a trend that will emerge population-wide as online gambling proliferates. In this chapter, hypotheses about the population-wide and young-male-specific risks of online gambling are assessed using data from three nationwide Czech surveys. The hypotheses relating specifically to young men are, first, that young men are greater risk-takers who enjoy “practicing” in anonymous environments, and, second, that young men are more prone to overspending as a result of losing track of time during play.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Chapter analysing three Czech nationwide surveys on live online betting and gambling pathology; abstract doesn't say whether a problem-gambling instrument was used.

**Решение:** =

---

### 1162 · R6110

**A Study of Development and Validation of Sports Gambling Motivation Scale**

2015 · The Tourism Sciences Society of Korea · article, journalarticle, review · en · https://doi.org/10.17086/jts.2015.39.2.11.26

This study explored motivation clusters in sports gambling, and discusses gambling types. This research also identifies discriminant and convergent validity of a sports gambling motivation scale using exploratory factor analysis (EFA), reliability test, and confirmatory factor analysis (CFA), and criterion or predictive validity using correlation and multiple regression analysis. A sports gambling motivation scale was developed in the following manner: First, a 62 item pool was developed based on previous studies. Second, 48 items were selected following a focus group interview (FGI). Third, 38 items were choosen using Delphi survey and content validity was evaluated with content validity ration (CVR). Fourth, 28 items were generated from a pretest of 243 respondents. Finally, the data were collected from 760 sports gamblers and EFA was employed to identify underlying dimensions of sports gambling motivations. EFA identified five sports gambling motivation factors such as socialization, gaming, adventure, money, and relaxation.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of 760 sports gamblers. Criterion validity was tested, but the abstract doesn't say whether a problem-gambling screen was the criterion.

**Решение:** =

---

### 1163 · R6114

**PSIKOLOGI KOMUNIKASI DALAM PERILAKU PENYIMPANGAN SOSIAL PRAKTEK JUDI BOLA ONLINE YANG DILAKUKAN MAHASISWA FISIP UPN “VETERAN” YOGYAKARTA**

2015

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: Indonesian study of online football betting among university students; no abstract. Probably qualitative, but the method and any PG measure are unknown.); Sonnet -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: No abstract; the title points to a communication-psychology study of social deviance in student online football gambling. It is likely qualitative, with no problem-gambling instrument.)

**Решение:** -

---

### 1164 · R6121

**Classifying and Profiling Sports Lottery Gamblers: A Cluster Analysis Approach**

2015 · Social Behavior and Personality An International Journal · article, journal-article · en · https://doi.org/10.2224/sbp.2015.43.8.1299

We developed a typology of sports gamblers based on the Scale of Assessing Problem Gambling and then to describe the clusters we identified according to the demographic and behavioral characteristics of each. Participants ( N = 4,980) were Chinese sports lottery players selected using a multistage sampling procedure. All participants completed the survey. Through cluster analyses, we identified 5 distinctive clusters of sports gamblers: casual players, escalated players, at-risk players, compulsive players, and problem players. A profiling analysis revealed that these 5 clusters differed in both terms of demographic and behavioral characteristics. This typology of sports gamblers provides diagnostic information that can be used by regulatory institutions to develop relevant intervention programs.

**ИИ:** + · обе модели · беттеры + инструмент · Survey of 4,980 Chinese sports lottery players using the Scale of Assessing Problem Gambling; clusters include problem players.

**Решение:** =

---

### 1165 · R6122

**Classifying and Profiling Sports Lottery Gamblers: A Cluster Analysis Approach**

2015 · review, article · en · https://doi.org/10.2224/sbp.2015.43.8.1299–1318

We developed a typology of sports gamblers based on the Scale of Assessing Problem Gambling and then to describe the clusters we identified according to the demographic and behavioral characteristics of each. Participants ( N = 4,980) were Chinese sports lottery players selected using a multistage sampling procedure. All participants completed the survey. Through cluster analyses, we identified 5 distinctive clusters of sports gamblers: casual players, escalated players, at-risk players, compulsive players, and problem players. A profiling analysis revealed that these 5 clusters differed in both terms of demographic and behavioral characteristics. This typology of sports gamblers provides diagnostic information that can be used by regulatory institutions to develop relevant intervention programs.

**ИИ:** + · обе модели · беттеры + инструмент · Survey of 4,980 Chinese sports lottery players using the Scale of Assessing Problem Gambling. Empirical study despite the 'Review' record type; check the case definition in the full text.

**Решение:** =

---

### 1166 · R6126

**The Dark Side of Authenticity: Feeling "Real" While Gambling Interacts with Enhancement Motives to Predict Problematic Gambling Behavior.**

2015 · Journal of gambling studies · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1007/s10899-014-9460-7

Engaging in activities that make people feel authentic or real is typically associated with a host of positive psychological and physiological outcomes (i.e., being authentic serves to increase well-being). In the current study, we tested the idea that authenticity might have a dark side among people engaged in an addictive or risky behavior (gambling). To test this possibility, we assessed gamblers (N = 61) who were betting on the National Hockey League playoff games at a sports bar. As predicted, people who felt authentic when gambling reported behavior associated with problem gambling (high frequency of betting) as well as problematic play (a big monetary loss and a big monetary win). Moreover, such behavior and gambling outcomes were particularly high among people who were motivated to gamble for the purpose of enhancement. The interaction of feeling authentic when betting and gambling for purposes of enhancing positive emotions proved especially troublesome for problematic forms of play. Implications of authenticity as a potential vulnerability factor for sports betting and other types of gambling are discussed.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of NHL sports bettors; outcomes look like betting frequency and wins/losses, but the abstract doesn't say whether a PG screen was also used.

**Решение:** =

---

### 1167 · R6132

**Sports betting becoming ‘normal’ – potentially leading to peer pressure and risky gambling**

2015

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the title could be a news item or commentary, but it could also report a survey of sports bettors on risky gambling.

**Решение:** =

---

### 1168 · R6138

**Fantasy Sports: A Growing Concern Among College Student-Athletes**

2015 · International Journal of Mental Health and Addiction · article, journal-article · en · https://doi.org/10.1007/s11469-015-9610-x

Participation in fantasy sports has become increasingly popular. Typical gambling activities such as poker, sports wagering and, sports lotteries, share many similar characteristics with fantasy sports playing. Research has shown that not only are college students more likely to partake in risky behaviors (gambling, alcohol and drug use), but those who partake in fantasy sports are also more likely to experience gambling-related problems. However, no published studies have examined the relationship between student-athletes and fantasy sports participation. Using data from the 2004, 2008 and 2012 National Collegiate Athletic Association (NCAA) studies assessing gambling behaviors and problems among U.S college student-athletes, this study aims to explore the prevalence and growth in fantasy sports among student-athletes. Further, it examines whether, in the 2012 study, student-athletes qualifying as at-risk or having gambling problems participate more often in fantasy sports. Overall a steady increase in fantasy sports participation (for money or fun) in college was found looking at these three cross-sectional studies. Additionally, approximately half of college student-athletes who qualified as at risk or having gambling problems were found to have participated in fantasy sports wagering.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · NCAA student-athlete surveys measured fantasy sports wagering and at-risk/problem gambling status; can probably link the two.

**Решение:** =

---

### 1169 · R6139

**/ ARTICLE / « ARJEL : Etude sur les joueurs en ligne (turfistes, parieurs sportifs, joueurs de poker) : « LE DESSOUS DES CARTES » (8 pages, septembre 2015) publié sur lescasinos.org du 17 septembre 2015.**

2015 · HAL (Le Centre pour la Communication Scientifique Directe) · other · fr

ARJEL, autorité de régulation des jeux d'argent en ligne, Coppolani/Martignoni/CENSURE, France, Paris, Lyon,2015

**ИИ:** ? · обе модели · другое · Website article on an ARJEL study of online sports bettors; probably account data, but unclear whether a problem-gambling instrument was used.

**Решение:** =

---

### 1170 · R6146

**Exploring the Fantasy World of Internet Gambling**

2015 · Journal of the Arkansas Academy of Science · article · en

This thesis explores the gambling activities arising from Fantasy Sports Leagues, in particular the gambling behavior of college students within these leagues. In my research, I investigated the development of the industry, the rules and surrounding internet gambling, and conducted a survey of college students over their Fantasy Sports behavior.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of college students' fantasy sports gambling behaviour; the abstract doesn't say whether a problem-gambling instrument was used.

**Решение:** =

---

### 1171 · R6152

**The “Pathological Gambling and Epidemiology” (PAGE) study program: design and fieldwork**

2015 · International Journal of Methods in Psychiatric Research · article · en · https://doi.org/10.1002/mpr.1458

The German federal states initiated the "Pathological Gambling and Epidemiology" (PAGE) program to evaluate the public health relevance of pathological gambling. The aim of PAGE was to estimate the prevalence of pathological gambling and cover the heterogenic presentation in the population with respect to comorbid substance use and mental disorders, risk and protective factors, course aspects, treatment utilization, triggering and maintenance factors of remission, and biological markers. This paper describes the methodological details of the study and reports basic prevalence data. Two sampling frames (landline and mobile telephone numbers) were used to generate a random sample from the general population consisting of 15,023 individuals (ages 14 to 64) completing a telephone interview. Additionally, high-risk populations have been approached in gambling locations, via media announcements, outpatient addiction services, debt counselors, probation assistants, self-help groups and specialized inpatient treatment facilities. The assessment included two steps: (1) a diagnostic interview comprising the gambling section of the Composite International Diagnostic Interview (CIDI) for case finding; (2) an in-depth clinical interview with participants reporting gambling problems. The in-depth clinical interview was completed by 594 participants, who were recruited from the general or high-risk populations. The program provides a rich epidemiological database which is available as a scientific use file.

**ИИ:** + · обе модели · опрос населения об азартных играх · German national prevalence survey (n=15,023) that used the CIDI diagnostic interview; the full text may include tables by gambling activity, such as sports betting.

**Решение:** =

---

### 1172 · R6162

**The Incorporation of the School Age Group of 16-18 Years Old in Gambling**

2015 · ILIRIA International Review · article · en · https://doi.org/10.21113/iir.v5i1.24

The scientific research of this paper focuses on the involvement of the school age group 16-18 years old in sports betting games impacted by beliefs on luck and social groups. For the collection of data literature is utilized, questionnaires are distributed and also focus groups were conducted. The assumptions of the assignment are: a) The involvement of school age group 16-18 years in sports betting games are manners learned from their comrades, b) The school age group 16-18 years old attribute to fate the participation in sports betting games. Over 64% of responses manifest that they have learned the rules from their companions. The revelations and questionnaire responses argue that over 45% of students in their classes play sports bets, and 34% think that the phenomena of sports betting depends on luck. The major part of this age group do not practice and believe in fortunate rituals or activities. The acquired data reflect that the extent of involvement of this age group is in substantial dimensions. We suggest that the decision-making bodies and service providers should develop strategies in order to reduce the phenomenon.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Questionnaire survey of 16-18-year-old students on sports betting, looking at luck beliefs and peer learning; the abstract names no problem-gambling instrument.

**Решение:** =

---

### 1173 · R6177

**Assessing the Risks Associated With Online Lottery and Casino Gambling: A Comparative Analysis of Players’ Individual Characteristics and Types of Gambling**

2015 · International Journal of Mental Health and Addiction · article · en · https://doi.org/10.1007/s11469-014-9531-0

Previous studies have found that online gambling operates in riskier betting conditions than offline gambling and attracts players with more demographic risk factors for gambling disorders. This study reveals that online lottery/casino players, compared to their offline counterparts, also have more psychographic risk factors such as a higher level of trust in the Internet, which could increase susceptibility to unscrupulous manipulation. By type of gambling, online casino players, as opposed to online lottery players, have a stronger tendency to thriftlessness and a lower degree of sociability, two psychographics that, in interaction with the riskier online betting conditions, could make online casino players particularly vulnerable. These findings suggest that governments’ policy/educational initiatives to prevent gambling disorders should be adapted to the specific levels of risk associated with each type of online gambling and their users’ profiles.

**ИИ:** разошлись — Opus -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Compares psychographics of online lottery and casino players; no sports betting and no problem-gambling instrument mentioned.); Sonnet ? (неясно, измеряли ли проблемную игру: Survey of online and offline lottery and casino players. The abstract doesn't say whether it used a problem-gambling instrument or measured sports betting, so the full text is needed.)

**Решение:** -

---

### 1174 · R6178

**Sports Betting and Other Risk Behaviour among Croatian High-School Students**

2015 · Hrvatska revija za rehabilitacijska istraživanja · article · hr · http://hrcak.srce.hr/index.php?show=clanak&id_clanak_jezik=221023

Sportsko klađenje vrlo je rasirena i dostupna igra na srecu u Hrvatskoj. Novija istraživanja prevalencije kockanja mladih, koja sve vise zaokupljaju interes strucnjaka u drustvenim znanostima, pokazuju znacajnu zastupljenost ovog ponasanja, dok teorijski modeli, ali i inozemna empirijska istraživanja, govore u prilog povezanosti kockanja s drugim oblicima rizicnog i delinkventnog ponasanja. Ciljevi ovog rada su utvrditi u kojoj mjeri se mladici u Hrvatskoj redovito klade na sportske rezultate, postoje li razlike u ucestalosti klađenja s obzirom na vrstu skole i dob, te manifestiraju li oni srednjoskolci koji se redovito klade i vise drugih oblika rizicnog/delinkventnog ponasanja. Istraživanje je provedeno na uzorku od n=1.330 mladica, srednjoskolaca (Mdob=16.58 ; SDdob=1.19) svih vrsta srednjih skola u 7 hrvatskih gradova. U radu je, uz Upitnik o opcim socio-demografskim podacima, koristen Upitnik aktivnosti kockanja (Ricijas i sur., 2011) te Upitnik rizicnog i delinkventnog ponasanja (Atlanta i sur., 2005). Rezultati pokazuju da se cak 36.6% srednjoskolaca redovito kladi na sportske rezultate, te je sportsko klađenje najucestaliji oblik kockanja kod mladih. Razlike s obzirom na vrstu skole postoje na nacin da se ucenici strukovnih cetverogodisnjih skola klade nesto cesce od ucenika gimnazija, dok razlike s obzirom na dob nisu dobivene, a ucestalije sportsko klađenje povezano je s ucestalijim igranjem drugih igara na srecu. Rezultati također jednoznacno pokazuju kako srednjoskolci koji se redovito klade manifestiraju i vise drugih oblika rizicnog/delinkventnog ponasanja, a efekti razlika najznacajniji su u podrucju rizicnog ponasanja vezanog uz skolu te konzumiranja sredstava ovisnosti. Rezultati su interpretirani u kontekstu drugih međunarodnih istraživanja, ali i s prakticnim implikacijama za osmisljavanje pravovremenih intervencija prema mladima u riziku.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of 1,330 Croatian male students on sports betting; only a gambling activity questionnaire is named. A problem-gambling screen (e.g., CAGI) may appear in full text.

**Решение:** =

---

### 1175 · R6179

**Sportsko klađenje i druga rizična ponašanja hrvatskih srednjoškolaca**

2015 · Hrvatska revija za rehabilitacijska istraživanja · article · hrv · https://hrcak.srce.hr/150117

Sports betting is a very widespread game of chance in Croatia. Contemporary research on youth gambling prevalence, which becomes of more interest in the social sciences, shows significant prevalence of this type of risk behaviour. Theoretical models, as well as empirical research, also indicate a correlation between gambling and other forms of risk/delinquent behavior. The aims of this paper are to determine the prevalence of regular sports betting among male high-school students in Croatia, differences in sports betting with regard to age and type of school, and differences in the manifestation of other risk/delinquent behavior with regard to frequency of sports betting. A study was conducted with 1,330 male high-school students (Mage=16.58; SD=1.19) from all three types of high schools in Croatia (in 7 cities/towns). The following instruments were used: Questionnaire on General Socio-Demographic Data; Gambling Activities Questionnaire (Ricijaš et al. 2011), as well as Risk and Delinquent Behaviour Questionnaire (Atlanta et al., 2005). Results show that 36.6% of male high-school students regularly bet on sports results, and sports betting is the most frequent games of chance played among young people. Students from four-year vocational high schools bet more often than gymnasium (university preparatory) students, while age differences were not found. Results also show a correlation between frequency of sports betting and frequency of playing other games of chance, while those students who bet more often also manifest more risk/ delinquent behaviour. The differences are significant on all subscales, but the effects are the greatest within school-related risk behaviour and consummation of alcohol/drugs. The results are interpreted in the context of other international research, but also with practical implications for creating prompt and well-timed interventions for youth at risk. Sportsko klađenje vrlo je raširena i dostupna igra na sreću u Hrvatskoj. Novija istraživanja prevalencije kockanja mladih, koja sve više zaokupljaju interes stručnjaka u društvenim znanostima, pokazuju značajnu zastupljenost ovog ponašanja, dok teorijski modeli, ali i inozemna empirijska istraživanja, govore u prilog povezanosti kockanja s drugim oblicima rizičnog i delinkventnog ponašanja. Ciljevi ovog rada su utvrditi u kojoj mjeri se mladići u Hrvatskoj redovito klade na sportske rezultate, postoje li razlike u učestalosti klađenja s obzirom na vrstu škole i dob, te manifestiraju li oni srednjoškolci koji se redovito klade i više drugih oblika rizičnog/delinkventnog ponašanja. Istraživanje je provedeno na uzorku od n=1.330 mladića, srednjoškolaca (M=16.58; SD=1.19) svih vrsta srednjih škola u 7 hrvatskih gradova. U radu je, uz Upitnik o općim socio-demografskim podacima, korišten Upitnik aktivnosti kockanja (Ricijaš i sur., 2011) te Upitnik rizičnog i delinkventnog ponašanja (Atlanta i sur., 2005). Rezultati pokazuju da se čak 36.6% srednjoškolaca redovito kladi na sportske rezultate, te je sportsko klađenje najučestaliji oblik kockanja kod mladih. Razlike s obzirom na vrstu škole postoje na način da se učenici strukovnih četverogodišnjih škola klade nešto češće od učenika gimnazija, dok razlike s obzirom na dob nisu dobivene, a učestalije sportsko klađenje povezano je s učestalijim igranjem drugih igara na sreću. Rezultati također jednoznačno pokazuju kako srednjoškolci koji se redovito klade manifestiraju i više drugih oblika rizičnog/delinkventnog ponašanja, a efekti razlika najznačajniji su u području rizičnog ponašanja vezanog uz školu te konzumiranja sredstava ovisnosti. Rezultati su interpretirani u kontekstu drugih međunarodnih istraživanja, ali i s praktičnim implikacijama za osmišljavanje pravovremenih intervencija prema mladima u riziku.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of 1,330 Croatian male students who bet on sports; listed instruments include no problem-gambling screen, though the wider project used CAGI.

**Решение:** =

---

### 1176 · R6185

**Unhealthy Gambling Amongst New Zealand Secondary School Students: An Exploration of Risk and Protective Factors**

2015 · International Journal of Mental Health and Addiction · article · en · https://doi.org/10.1007/s11469-015-9562-1

This study sought to determine the prevalence of gambling and unhealthy gambling behaviour and describe risk and protective factors associated with these behaviours amongst a nationally representative sample of New Zealand secondary school students ( n = 8,500). Factor analysis and item response theory were used to develop a model to provide a measure of ‘unhealthy gambling’. Logistic regressions and multiple logistic regression models were used to investigate associations between unhealthy gambling behaviour and selected outcomes. Approximately one-quarter (24.2 %) of students had gambled in the last year, and 4.8 % had two or more indicators of unhealthy gambling. Multivariate analyses found that unhealthy gambling was associated with four main factors: more accepting attitudes towards gambling ( p < 0.0001); gambling via gambling machines/casinos/track betting ( p = 0.0061); being worried about and/or trying to cut down on gambling ( p < 0.0001); and, having attempted suicide ( p = 0.0009). Unhealthy gambling is a significant health issue for young people in New Zealand. Ethnic and social inequalities were apparent and these disparities need to be addressed.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · National student survey with gambling activities; 'unhealthy gambling' uses a custom IRT-derived measure, so it may not be a standard instrument.

**Решение:** =

---

### 1177 · R6186

**Fantasy Sport**

2015 · Routledge eBooks · book-chapter · en · https://doi.org/10.4324/9780203114711.ch21

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Routledge book chapter on fantasy sport with no abstract; probably descriptive, but could include survey data on paid fantasy players.

**Решение:** =

---

### 1178 · R6189

**Explaining the intention to play and behavior of playing sports betting games of young Finnish adults : an application of the theory of planned behavior**

2015 · LUTPub (LUT University) · dissertation · en

The aim of this Master’s Thesis was to examine the determinants of intention and behavior of playing sports betting games in order to explain the intention to play in a more precise way and to be able to understand the behavior of playing. The theory of planned behavior was applied in explaining the intention of young Finnish adults aged 18 to 34. \nA quantitative research method was applied and an online survey was sent to the students of Lappeenranta University of Technology and to the subscribers of Urheilulehti in order to reach a sample that present the young population of Finland. The theory of the study focused on the theory of planned behavior and its antecedents, attitude towards behavior, subjective norms, perceived behavioral control as well as motivation. By analyzing the data, causal relationships were found through which the explanation of intention was possible. \nThe results showed that attitude towards playing, subjective norms, perceived behavioral control and motivation impact the formation of intention significantly. The results also indicated that intention impacts significantly to the playing frequency.

**ИИ:** разошлись — Opus -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Theory of planned behaviour survey of sports betting intentions and frequency; abstract mentions no problem-gambling instrument.); Sonnet ? (неясно, измеряли ли проблемную игру: Survey of young Finnish sports betting players using theory of planned behavior; abstract doesn't mention problem gambling measure, but one may be included as a covariate.)

**Решение:** ?

---

### 1179 · R6190

**Gambling frequency, gambling problems and concerned significant others of problem gamblers in Finland: Cross-sectional population studies in 2007 and 2011**

2015 · Scandinavian Journal of Public Health · article · en · https://doi.org/10.1177/1403494815569866

AIMS: This study compares past-year gambling frequency, gambling problems and concerned significant others (CSOs) of problem gamblers in Finland by age, from 2007 and 2011. METHODS: We used random sample data collected in 2007 (n = 4722) and 2011 (n = 4484). The data were weighted, based on gender, age and region of residence. We measured the past-year gambling frequency using a categorical variable, while gambling severity was measured with the South Oaks Gambling Screen. We identified CSOs by a single question including seven response options. Chi-Squared and Fisher's exact tests were used. RESULTS: Overall, the past-year gambling frequency change was statistically significant between 2007 and 2011. Among 18-64-year-old Finnish people, the proportion of non-gamblers decreased. Yet, among 15-17-year-old respondents, non-gambling increased and gambling problems decreased. Among 18-24 year olds, the proportion of close ones with gambling problems also decreased. On the other hand, the proportion of family members with gambling problems increased among the 50-64 year olds. CONCLUSIONS: The increase in adult gambling participation was mainly explained by infrequent gambling. The proportion of gambling problems from the gamblers' and CSOs' perspective remained unchanged, yet significant changes were observed within age groups. The short-term changes in under-age gambling problems were desirable. Future studies should explore the adaptation and access hypotheses alongside gambling problems.

**ИИ:** + · обе модели · опрос населения об азартных играх · Finnish national gambling prevalence surveys (2007, 2011) with SOGS; tables may report problem gambling by activity, including sports betting.

**Решение:** =

---

### 1180 · R6201

**Gambling Risk Amongst Adolescents: Evidence from a School-Based Survey in the Malaysian Setting**

2015 · Journal of Gambling Studies · article · en · https://doi.org/10.1007/s10899-015-9577-3

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · School-based adolescent gambling risk survey; likely used a problem-gambling screen and may report sports betting, but there is no abstract.

**Решение:** =

---

### 1181 · R6203

**ASSOCIATION FOR CONSUMER RESEARCH**

2015 · review

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: Generic conference-proceedings title with no abstract; search may have retrieved it for a betting-related paper, so check the full text.); Sonnet -6 (не про азартные игры или «ставка/лотерея» в другом смысле: Title is an organization name (Association for Consumer Research), no abstract, no indication of gambling or sports betting content.)

**Решение:** -

---

### 1182 · R6205

**Office-based sports gambling and pooling: Ethical dilemmas and worker productivity issues from fan and gender perspectives**

2015 · dissertation · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Dissertation on office sports betting pools; there is no abstract, so it is unclear whether a problem-gambling instrument was used.

**Решение:** =

---

### 1183 · R6206

**Pengaruh Motivasi dan Penggunaan Situs Judi Sepakbola OnlineTerhadap Pemenuhan Kebutuhan User(Studi pada Mahasiswa Ilmu Komunikasi Angkatan 2012 – 2014 FakultasIlmu Sosial dan Ilmu Politik Universitas Lampung)**

2015

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Indonesian thesis surveying students who bet on football online, framed around motivation and needs; no abstract, so a PG instrument can't be ruled out.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Indonesian student survey on motivation and need fulfilment from online football betting sites (uses-and-gratifications); no abstract, but a problem-gambling instrument is unlikely.)

**Решение:** -

---

### 1184 · R6210

**Is online betting behaviour gender based? : an analytical neuroscientific view of the online betting behaviour**

2015 · dissertation · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Dissertation on online betting by gender, no abstract; it may have surveyed online bettors with a problem-gambling measure.

**Решение:** =

---

### 1185 · R6211

**Predictor Variables of Online Sports Problem Gambling by College Fraternity Members**

2015 · ScholarWorks (Walden University) · dissertation · en

The quantitative study identified predictor variables of online sports problem gambling, as measured by the South Oaks Gambling Screen (SOGS) among fraternity students at major college universities. The data were composed of 125 college fraternity students from ages 18 to 25 years of age. The average SOGS score was 1.776 with a standard deviation of 1.93. A SOGS score of 5 or greater indicates a probable problem gambler. The study used the Blaszczynski and Nower (2002) pathways model to determine how fraternity students could become problem gamblers. A stepwise regression model was run in SPSS using multiple independent variables taken from the survey to determine which of the independent variables were significantly correlated with the dependent variable, SOGS score. The study found 5 independent variables to be statistically significant: family history of gambling, competitive wagering, tobacco use, placing a wager with a friend, and wagering with funds acquired by illicit means. These 5 variables hold an R-squared (adjusted) of .26, which means that about 26% of the variability in the SOGS scores can be accounted for by these 5 variables. The study results supported the hypothesis that a complex set of social, biological, and psychological factors may contribute to determine how fraternity students could become problem gamblers. This study identified multiple individuals and parties who would benefit from further research about the ill-effects of online sports gambling among fraternity students.

**ИИ:** + · обе модели · беттеры + инструмент · Dissertation surveying 125 fraternity students on online sports gambling, with problem gambling measured by SOGS (cut-off 5+).

**Решение:** =

---

### 1186 · R6231

**A Comparison of the Status, Legal, Economic, and Psychological Characteristics of Types of Adult Male Gamblers.**

2015 · Journal of gambling studies · article, comparative study, journal article · eng · https://doi.org/10.1007/s10899-014-9462-5

Gambling behavior is not a unique behavior. There are certain differences in behavior, gambling habits, gambling beliefs, and their reflection in psychosocial life. We have compared three groups of adult male gamblers—sports gamblers (n = 41), machine gamblers (n = 36), and poker gamblers (n = 35)—in regard to measures of personal status and legal-social characteristics. We found no difference between groups in terms of the length of gambling behavior, personal status, or age. We found no legal difference between groups in terms of the number of court cases for debt, stealing, or family court cases. In terms of economic circumstances, sports gamblers suffered more losses than the other groups (p < 0.0001). There were higher rates of bankruptcy among sports gamblers compared with machine gamblers (p < 0.01). Sports gamblers were more likely to borrow money from the black market compared with the other groups (p < 0.01). In terms of mental health, sports and machine gamblers had more suicidal thoughts and gestures than poker gamblers (p < 0.05), whereas the rate of suicide attempts was higher in machine gamblers compared with poker players (p < 0.05). Our results indicated higher vulnerability in sports gamblers in terms of economic problems compared with the other groups, whereas machine gamblers had vulnerability to suicidal thoughts and suicidal attempts compared with poker gamblers.

**ИИ:** ? · обе модели · другое · Compares sports, machine and poker gamblers; recruitment unclear, probably a clinical or treatment-seeking sample. No problem-gambling instrument stated.

**Решение:** =

---

### 1187 · R6232

**THE REALITY OF (DAILY) FANTASY SPORTS**

2015 · article · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract. The title is about daily fantasy sports and may be commentary, but an empirical study can't be ruled out.

**Решение:** =

---

### 1188 · R6238

**Glücksspielteilnahme und -probleme in Österreich**

2015 · Suchttherapie · article · de · https://doi.org/10.1055/s-0035-1557672

Einleitung: In Österreich gibt es seit vielen Jahren eine fachöffentliche Diskussion über einen angemessenen Spieler- und Jugendschutz beim Glücksspiel. Gleichzeitig liegen bislang vergleichsweise wenige epidemiologische Befunde über die Glücksspielteilnahme und -probleme der Bevölkerung vor. Methoden: In diesem Vortrag werden die Ergebnisse der bisherigen Repräsentativbefragungen zusammenfassend vorgestellt. Es handelt sich hierbei um zwei Erwachsenen-Befragungen (Kalke et al., 2011; IMAS, 2014) und eine jugendspezifische Erhebung (Ikrath & Rohrer, 2013). Eine neue Bevölkerungsumfrage mit der bislang größten Fallzahl (N = 10.000) wurde gerade abgeschlossen (Kalke & Wurst, 2015); diese Studie wird in Kooperation mit der Gesellschaft zur Erforschung stoffungebundener Süchte durchgeführt. Ergebnisse: Die bisher vorliegenden Ergebnisse zeigen, dass etwa 1% der erwachsenen Bevölkerung ein problematisches oder Pathologisches Glücksspielverhalten aufweist (Kalke et al., 2011). Von überdurchschnittlich hohen Problemprävalenzen sind dabei die 18- bis 35-Jährigen, Arbeitslose, gering Verdienende und Spieler mit häufiger Spielteilnahme und hohem Geldeinsatz betroffen. Die Prävalenz problematischen und Pathologischen Spielens ist unter den Automatenspielern am höchsten. Es folgen die Sportwetten und schon mit deutlichem Abstand die klassischen Kasinospiele. Einige dieser Befunde werden von der IMAS-Studie bestätigt. In der Befragung von Jugendlichen und jungen Erwachsenen zu ihrem Onlinespielverhalten zeigt sich, wie etabliert sowohl das Offline- als insbesondere auch das Online-Glücksspielangebot in den Lebenswelten 12- bis 24-Jähriger ist (Ikrath & Rohrer, 2013). Das Design und ggfs. erste Ergebnisse der gerade abgeschlossenen Befragung (2015) werden ebenfalls präsentiert. Diskussion: Epidemiologische Glücksspielforschung gewinnt in Österreich zunehmend an Bedeutung. Verschiedene Fragestellungen sind noch zu bearbeiten. Epidemiologische Daten können einen wichtigen Beitrag für eine empirisch orientierte Diskussion über einen effektiven Spieler- und Jugendschutz leisten.

**ИИ:** разошлись — Opus ? (другое: Conference talk summarising Austrian prevalence surveys that report problem gambling among sports bettors; it may also present new 2015 survey data, so mostly secondary.); Sonnet + (опрос населения об азартных играх: Austrian representative gambling surveys summarised; problem gambling prevalence reported by activity, including sports betting.)

**Решение:** ?

---

### 1189 · R6244

**Verbreitung von Sportwetten und glücksspielbezogenem Suchtverhalten in Sportvereinen: Eine Pilotstudie**

2015 · Suchttherapie · article · de · https://doi.org/10.1055/s-0035-1557639

Einleitung: Sportwetten erweisen sich aufgrund ihrer Verknüpfung mit sportlichen Interessen als besonders reizvoll für Personen, die selbst Sport treiben. Veranstaltungsmerkmale wie eine hohe Ereignisfrequenz und (vermeintliche) Kompetenzeinflüsse sind allerdings mit einem erhöhten Suchtpotenzial verbunden. Der Untersuchung lag die Zielsetzung zugrunde, erstmals empirische Daten zur Verbreitung von Sportwetten und glücksspielbezogenen Problemen in deutschen Sportvereinen zu erheben. Methoden: Von 294 Mitgliedern aus 21 Sportvereinen in Bremen und Kiel wurden Selbstangaben zur Teilnahme an verschiedenen Glücksspielen sowie DSM-IV-Kriterien für ein problematisches und Pathologisches Spielverhalten erhoben und mit repräsentativen Bevölkerungsdaten verglichen. Ergebnisse: 52,4% der Vereinsmitglieder haben in den vergangenen 12 Monaten Wetten auf Sportereignisse abgeschlossen, während sich nur 3,4% bzw. 6,0% der Allgemeinbevölkerung an Sportwetten beteiligt haben. Bei den Vereinsmitgliedern ist im Vergleich ebenfalls signifikant häufiger ein problematisches (5,3%) und pathologisches (3,5%) Spielverhalten festzustellen. Diskussion: Die Befunde stimmen mit internationalen Forschungsergebnissen überein und verdeutlichen die Notwendigkeit präventiver Maßnahmen, die sich gezielt an Sportvereine und deren Mitglieder richten.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Survey of sports club members that measured sports betting participation and problem gambling using DSM-IV criteria; 52.4% bet on sports.

**Решение:** =

---

### 1190 · R6245

**The Social Phenomenon of Football: Football Betting in Nigeria**

2015 · Miscellanea Anthropologica et Sociologica · article, other literature type, journal-article · en · https://doi.org/10.5604/20842937.1189811

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; sociological paper on football betting in Nigeria, could include a bettor survey with problem-gambling measure.

**Решение:** =

---

### 1191 · R6249

**Real-time Online Betting Analysis - The THMMY Case-Study**

2015

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; title may be a technical odds/data analysis or a study of a Greek student forum's bettors; can't tell.

**Решение:** =

---

### 1192 · R6255

**Influence of Fantasy Sport on Consumption Behavior**

2015 · Seoul National University Open Repository (Seoul National University) · dissertation · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; fantasy sport dissertation likely about sport consumption, but cash fantasy play and a problem-gambling measure can't be ruled out.

**Решение:** =

---

### 1193 · R6258

**불법 스포츠토토 실태와 개선방안탐색**

2015

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Korean study on illegal sports toto status and improvements; no abstract, may be policy paper or survey of bettors.

**Решение:** =

---

### 1194 · R6266

**Social Media, Facebook Games, and Fantasy Sport**

2014 · Palgrave Macmillan eBooks · book-chapter · en · https://doi.org/10.1057/9781137301420.0014

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Book chapter with no abstract; probably a descriptive overview, but it may include fantasy sports data with a problem-gambling measure.

**Решение:** =

---

### 1195 · R6268

**Glücksspiel**

2014 · Springer eBooks · book-chapter · de · https://doi.org/10.1007/978-3-658-05128-0_10

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · German book chapter titled 'Gambling' with no abstract; probably an overview, but empirical content can't be ruled out.

**Решение:** =

---

### 1196 · R6275

**Sports Betting and Free Bonus Bets**

2014 · article · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract. The title could mean a survey of bettors or a paper on betting strategy or markets; the full text is needed to tell.

**Решение:** =

---

### 1197 · R6283

**DIFFERENCE BETWEEN SPORTS BETTING AND GAMBLING ON THE ASPECT OF EDUCATIONAL LEVEL OF CITIZENS WHO ARE ACTIVE USERS OF THE GAMES OF CHANCE IN THE REPUBLIC OF MACEDONIA**

2014 · Facylty of Physical Education, Sport and Health · article, conference object, text/conference paper · en · https://doi.org/10.13140/2.1.2158.4007

With this work we want to give unpretentious contribution to the new and actual topic in our society, and we want to find a distinction between sport betting and gambling. Gambling is the waring of money or something of material value (referred to as "the stakes") on an vent with an uncertain outcome with the primary intent of winning additional money and/or material goods. Gambling thus requires three elements be present: consideration, chance and prize. Typically, the outcome of the wager is evident within a short period. Sports betting is the activity of predicting sports results and placing a wager on the outcome. It is generally considered to be a form of gambling. For this reason we are trying on the empirical way reaching out for clarification on this terminology and we ask our citizen who is active in “sports betting” and “gambling”. Republic of Macedonia today as a society can be in line “transitional the poetics of misery”. The probability of easy earning money is one of the motives of our citizens for sports betting, but not all our citizen expecting big earning, some are doing this as a fun or modern trend. From same reason is betting citizens from all ethnicity as a Macedonian, Albanian, Serb, Turk and Rome, less and more educational, people with less and more income.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Empirical survey of active sports bettors in Macedonia on motives and education; abstract does not mention a problem-gambling instrument.

**Решение:** =

---

### 1198 · R6284

**The impact of alexithymia on pathological gamblers' decision making: a preliminary study of gamblers recruited in "sportsbook" casinos.**

2014 · Cognitive and behavioral neurology : official journal of the Society for Behavioral and Cognitive Neurology · journal article, journalarticle, article · eng · https://doi.org/10.1097/wnn.0000000000000027

OBJECTIVE: We investigated whether alexithymia is at the root of the decision-making deficit classically reported in pathological gamblers. BACKGROUND: Alexithymia has been shown to be a recurrent personality trait of pathological gamblers and to impair the decision-making abilities of nonpathological gamblers, but no previous studies have investigated whether alexithymia significantly affects pathological gamblers' decision making. Although investigations of pathological gamblers typically have studied those seeking treatment, most pathological gamblers do not seek treatment. Thus, to study people representative of the general population of pathological gamblers, we conducted our study in "sportsbook" casinos with a small sample of gamblers who were not seeking treatment. METHODS: We recruited gamblers in sportsbooks and classified them based on their scores on the South Oaks Gambling Screen and the Toronto Alexithymia Scale: 3 groups of pathological gamblers (6 alexithymic, 8 possibly alexithymic, and 6 nonalexithymic) and 8 healthy controls. All of the participants completed an adaptation of the Iowa Gambling Task. RESULTS: The alexithymic group chose less advantageously on the task than the other groups. The severity of the deficit in decision-making abilities was related to the severity of alexithymia, even when we controlled for the effects of anxiety and depression. CONCLUSIONS: Our findings provide preliminary evidence that alexithymia might be a critical personality trait underlying pathological gamblers' decision-making deficits.

**ИИ:** разошлись — Opus ? (другое: Sportsbook gamblers classified with SOGS, but the design looks case-control (pathological gamblers vs controls); unclear whether screening counts are reported.); Sonnet -5 (выборка набрана по проблемам с игрой: лечение, горячая линия, самоисключение, сравнение проблемных игроков с контролем: Small case-control style study (20 pathological gamblers vs 8 controls) in sportsbook casinos, classified by SOGS; no sports-bettor prevalence reportable.)

**Решение:** -

---

### 1199 · R6292

**Accuracy of self-reported versus actual online gambling wins and losses.**

2014 · Psychological assessment · article, journal article, research support, n.i.h., extramural · eng · https://doi.org/10.1037/a0036428

This study is the first to compare the accuracy of self-reported with actual monetary outcomes of online fixed odds sports betting, live action sports betting, and online casino gambling at the individual level of analysis. Subscribers to bwin.party digital entertainment's online gambling service volunteered to respond to the Brief Bio-Social Gambling Screen and questions about their estimated gambling results on specific games for the last 3 or 12 months. We compared the estimated results of each subscriber with his or her actual betting results data. On average, between 34% and 40% of the participants expressed a favorable distortion of their gambling outcomes (i.e., they underestimated losses or overestimated gains) depending on the time period and game. The size of the discrepancy between actual and self-reported results was consistently associated with the self-reported presence of gambling-related problems. However, the specific direction of the reported discrepancy (i.e., favorable vs. unfavorable bias) was not associated with gambling-related problems.

**ИИ:** + · обе модели · беттеры + инструмент · Survey of bwin online subscribers who bet on sports, with the BBGS administered; could report problem gambling among sports bettors.

**Решение:** =

---

### 1200 · R6297

**Lifestyle and Health Risk Behaviours among Elbasan Students**

2014 · Open Access Macedonian Journal of Medical Sciences · article, review · en · https://doi.org/10.3889/oamjms.2014.092

Abstract AIM: The purpose of this study is: (1) to help monitor the Albanian students’ lifestyle, the way they spend their free time, the weight that studying, networks, screens and sports have in their life; (2) to assess their health risk behaviours, such as tobacco and drug use, weapon carrying and sports betting; (3) to identify differences in behaviour by gender, grade, socioeconomic and demographic status; (4) to understand the influence of parents on their children. METHOD: The study was conducted in May 2013, as a classroom survey of students in urban and rural schools of Elbasan. A questionnaire was distributed to the 8th to 12th grade students to be completed by them anonymously. RESULT: There are a low number of the students that are interested to books and study and meantime, a large number of them spend their free time in front of a screen or hanging out in bars with friends. Moreover, a considerable number of them are engaged in health risk behaviours. CONCLUSION: In students’ lifestyle exist serious problems and these data also provide inside into ways to shape a public health response. We need to change the way society views and treats these problems.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Classroom survey of adolescents that measured sports betting; the abstract doesn't say whether a problem-gambling instrument was used.

**Решение:** =
