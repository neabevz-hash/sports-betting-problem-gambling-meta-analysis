# Проверка с метками ИИ, часть 10

Записи 1351–1500 из 1525, с метками обеих моделей над строкой решения. Модели согласны и вы тоже — поставьте `=`; иначе свой код (`+`, `?` или `-`, причина не нужна). Если модели разошлись, `=` не годится — нужен ваш код. Решаете вы. Последние 4 — калибровочные записи, где ваша слепая метка разошлась с правилом ИИ: она показана над метками.

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

### 1351 · R7377

**Differences in the Associations between Gambling Problem Severity and Psychiatric Disorders among Black and White Adults: Findings from the National Epidemiologic Survey on Alcohol and Related Conditions**

2010 · American Journal on Addictions · article · en · https://doi.org/10.1111/j.1521-0391.2010.00098.x

We examined differences in the associations of gambling problem severity and psychiatric disorders among a nationally representative sample of 32,316 black and white adults. Black respondents were more likely than white ones to exhibit problem or pathological gambling (PPG) and a stronger relationship between subsyndromal gambling and any mood disorder, hypomania, and any substance use disorder. Differences in the patterns of co-occurring disorders between syndromal and particularly subsyndromal levels of gambling in black and white respondents indicate the importance of considering race-related factors in mental health prevention and treatment strategies.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · NESARC national survey with a DSM-IV gambling measure; it's unclear whether participation in sports betting was recorded or reported.

**Решение:** =

---

### 1352 · R7378

**Gambling problem severity and psychiatric disorders among Hispanic and white adults: findings from a nationally representative sample**

2010 · Journal of Psychiatric Research · article · en · https://doi.org/10.1016/j.jpsychires.2010.07.010

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; likely NESARC national sample with DSM-IV gambling severity; unclear whether sports betting participation reported.

**Решение:** =

---

### 1353 · R7396

**Some Characteristics of Adolescent Gamblers in Croatia**

2010 · conference object · und

Games of chance, sports betting and other forms of gambling are a form of entertainment in everyday life. As such, they are very accessible and widespread in modern society. Potential players are, through numerous advertisments on expected gains, being invited to participate in these activities. However, it is also a behavior that can easily become an addiciton and therefore disturb social, family and professional functioning of an individual. In the past decade, gambling and gambling venues have increased. Although it is illegal for minors, the fact is that a growing number of adolescents are participating in different gambling activities (sports betting, casinos, card games ect.). Consequently, the data of foreign research (along with domestic practical experience) indicate a growing increase of problem as well as pathological gambling in the adolescent population. What is more, the age limit of first gambling has lowered and the harmful effects of gambling have become more serious and far-reaching. The results of forerign research show that gambling is often in comorbidity with other risk and antisocial behavior such as alcohol and drug abuse and delinquency. There has been no systematic research on this topic in Croatia. In this presentation, the authors will present the results of a pilot-study that will be conducted in March 2010. on a sample of about 300 high-school students in Zagreb from first to fourth grade of different educational orientation (three and four-year long vocational schools and high schools). The survey questionnaire will examine gambling habits, attitudes toward gambling and some personality traits and behavior characteristics among adolescents since the importance of these parameters in explainig this phenomenon has been shown in previous foreign researches. Also, one of the aims of this research is to determine corelation of gambling and other risk and antisocial behavior (alcohol and/or drug consumption, delinquent behavior) with some personality traits such as psychopathy, impulsivity and sensation seeking. This study is associated with the planning of a comprehensive study of gambling among Croatian adolescents.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Pilot survey of about 300 Croatian high-school students on gambling habits, including sports betting; the abstract doesn't say which problem-gambling instrument was used.

**Решение:** =

---

### 1354 · R7397

**Ocio, juegos de azar y apuestas deportivas**

2010 · Dialnet (Universidad de la Rioja) · article · es

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the title (leisure, gambling and sports betting) could fit an empirical survey or an essay.

**Решение:** =

---

### 1355 · R7428

**The actual condition of leisure sports club members' betting during a match and social-psychological, behavioral characteristics of sports betting addiction**

2010 · article · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; title suggests a survey of club members who bet on sports, looking at addiction characteristics, possibly using a PG screen.

**Решение:** =

---

### 1356 · R7430

**The analysis of relationships between gambling passion, gambling self efficacy, emotional intelligence on participation in sports betting**

2010 · The Korean Journal of Sport · article · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Probably a survey of Korean sports bettors; no abstract, so it is unclear whether a problem-gambling instrument was used.

**Решение:** =

---

### 1357 · R7434

**Taking the Points: The Socialization Process of a Sports Book “Regular”**

2010

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: No abstract; sports book regulars are relevant, but a study of their 'socialization process' is likely qualitative. Check the full text.); Sonnet -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: No abstract; title indicates an ethnographic or qualitative study of socialization into sports book regulars, unlikely to report problem gambling prevalence.)

**Решение:** -

---

### 1358 · R7445

**Internet gamblers: a latent class analysis of their behaviours and health experiences.**

2010 · Journal of gambling studies · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1007/s10899-010-9188-y

In order to learn about the behaviours and health experiences of people who gamble on the Internet, we conducted an international online survey with respondents recruited via gambling and gambling-related websites. The mean (SD) age of the 4,125 respondents completing the survey was 35.5 (11.8) years, with 79.1% being male and 68.8% UK residents. Respondents provided demographic details and completed validated psychometric screening instruments for problem gambling, mood disturbances, as well as alcohol and substance misuse, and history of deliberate self harm. We applied latent class analysis to respondents' patterns of regular online gambling activities, and identified subgroups of individuals who used the Internet to gamble in different ways (L (2) = 44.27, bootstrap P = 0.07). We termed the characteristic profiles as 'non-to-minimal gamblers'; 'sports bettors'; 'casino & sports gamblers'; 'lottery players'; and 'multi-activity gamblers'. Furthermore, these subgroups of respondents differed on other demographic and psychological dimensions, with significant inter-cluster differences in proportion of individuals scoring above threshold for problem gambling, mood disorders and substance misuse, and history of deliberate self harm (all Chi (2)s > 23.4, all P-values <0.001). The 'casino & sports' and 'multi-activity-gamblers' clusters had the highest prevalence of mental disorder. Internet gamblers appear to be heterogeneous but composed of several subgroups, differing markedly on both demographic and clinical characteristics.

**ИИ:** + · обе модели · беттеры + инструмент · Online gamblers survey using a problem-gambling screen; it reports problem gambling by latent class, including a 'sports bettors' class.

**Решение:** =

---

### 1359 · R7447

**Do youths gamble? You bet! A Swiss population-based study**

2010 · Swiss Medical Weekly · article · en · https://doi.org/10.4414/smw.2010.13074

OBJECTIVES: To establish the gambling prevalence among Swiss resident youths, to estimate the associations between gambling frequency and substance use, poor mental health and social support and to determine the correlation between gambling pattern and gambling frequency. METHODS: Cross-sectional population-based survey conducted in 2007. From 1233 eligible participants aged 15-24 years, adequate information was available for 1116 (582 males), distributed into: non- (n=577), occasional (n=388) and frequent gamblers (n=151). OUTCOME MEASURES: Substance use, social activities, presence of a reliable person among friends or family, psychological distress, major depression and gambling pattern. RESULTS: Overall, the 48.3% (n=539) of youths who had gambled during the previous year; were older and more likely to be male than non-gamblers. 13.5% (n=151) gambled at least weekly and could be differentiated from occasional gamblers on the basis of their gambling pattern. After controlling for gender, age and language area, occasional gamblers were significantly more likely to be occasional binge drinkers, whereas frequent gamblers were more likely to be daily smokers. CONCLUSION: Almost half of Swiss resident youths are involved in gambling. Both occasional and frequent gambling are associated with further health compromising behaviour. Practitioners dealing with young people should be aware that gambling is a behaviour that might be part of a more global risky behaviour framework.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Swiss youth population survey of gambling frequency and pattern; no problem-gambling instrument named, but the full text might include one.

**Решение:** =

---

### 1360 · R7451

**Forecasting in Financial and Sports Gambling Markets: Adaptive Drift Modeling**

2010 · Wiley eBooks · book, article, monograph · en · https://doi.org/10.1002/9780470880616

Preface. 1.Introduction. 1.1 Favorable Betting Scenarios. 1.2 Gambling Shocks. 1.3 The Dark Side of Sports: The Fixes. 2. Market Perspectives: Through a Glass Darkly. 2.1 Changing Paradigms. 2.2 Modeling Commentaries. 2.3 Sports Hedge Funds. 2.4 Gambling Markets: Prohibition, Repeal and Taxation. 2.5 Quantifying the Madness of Crowds in Sports Gambling Markets. 2.6 Statistical Shocks: Alias Variables. 3. Opacity and Present Day Variables. 3.1 Dilemmas between Social and Economic Efficiency. 3.2 Towards a More Visible Hidden Hand. 3.3 Hedge Funds and Galapagos. 3.4 Lotteries: Market for Losers. 4. Adaptive Modeling Concepts in Dynamic Markets. 4.1 Quant Funds and Algorithmic Trading. 4.2 Market Volatility and Fat-Trailed Distributions. 4.3 Adaptive ARMA(1,1) Drift Processes. 4.4 Time Varying Volatility. 5. Studies in Japanese Candlestick Charts. 5.1 Bullish and Bearish Patterns from Chartist Perspectives. 5.2 Black Monday. 5.3 A Matter of Alleged Insider Trading. 5.4 Commodity Bubbles and Volatility. 5.5 Short Selling. 5.6 Terrorist Attacks and the Markets. 5.7 A Hollywood Romance: Spiderman and Tinkerbell. 5.8 Copenhagen and Climate Change: Exxon Mobile Buys XTO Energy. 6. Pseudo Candlestick Graphics for Major League Baseball. 6.1 The 2008 World Series: Philadelphia Versus Tampa Bay. 6.2 The 2008 Chicago Cubs: Visions of 1908 Heroics. 6.3 A Strange Set of Coincidences: A Plate Umpire's Affinity for a Pitcher. 7. Single Equation Adaptive Drift Modeling. 7.1 Adaptive ARMA Processes. 7.2 Variable Selection: Identifying the Reduced Model. 7.3 Reduced Model Estimation: Single Equations. 7.4 Reduced Model Empirical Bayesian Estimation: Single Equations. 7.5 Single Equation Volatility Modeling: Adaptive GARCH Processes. 7.6 Modeling Monetary Growth Data. 7.7 Modeling GNP Deflator Growth. 8. Single Equation Modeling: Sports Gambling Markets. 8.1 Effects of Interactive Gambling Shocks. 8.2 End of an Era: Modeling Profile of the 1988-89 Los Angeles Lakers. 8.3 Spread Betting. 8.4 Modeling Profile of a Dream Team: The 1989-90 San Francisco 49ers. 8.5 Major League Baseball: A Data Intensive Game. 8.6 While Still Under the Curse: Modeling Profile of the 1990 Red Sox. 8.7 Portrait of Controversy: Modeling Profile of Roger Clemens with the 1990 Red Sox. 8.8 Pitcher of the Year in 1990: Modeling Profile of the Oakland's Bob Gibson. 9. Simultaneous Financial Time Series. 9.1 The Cruse of Higher Dimensionality. 9.2 From Candlesticks to Cointegration. 9.3 Cointegration in Terms of Autoregressive Processes. 9.4 Estimating Disequilibria through Factor Analysis. 9.5 Simultaneous Time Series: Adaptive Drift Modeling. 9.6 Simultaneous Time Series: Adaptive Volatility Modeling. 9.7 Exploratory Modeling: Marathon Oil Company. 9.8 The High Tech Bubble of 2000. 9.9 Twenty-Five Standard Deviation Moves. 9.10 The March 2009 Nadir. 10. Modeling Cointegrated Time Series Associated with NBA and NFL Games. 10.1 Modeling Transitions. 10.2 The 2007-08 NY Giants: As Unexpected as Katrina. 10.3 Misery for the Patriot Faithful. 10.4 The Pittsburgh Steelers in Super Bowl 2005. 10.6 Miami's First NBA Title: 2005-06. 10.7 The 2006-07 San Antonio Spurs: Unexpected Titlists. 10.8 Monitoring MBA Referee Performances. 11. Categorical Forecasting. 11.1 Fisher's Discriminant Function. 11.2 Bayesian Discriminant Analysis. 11.3 Logistic Regression Analysis. 11.4 Allocating Betting Monies in the Sports Gambling Markets. 12. Financial/Mathematical Illiteracy and Adolescent Problem Gambling: Epidemics More Damaging Than the 1918 Influenza Pandemic. 12.1 The Call for Financial/Mathematical Literacy in 21st Century America. 12.2 Data, Information and the Information Age. 12.3 The Companion Epidemic of Adolescent Problem Gambling. 12.4 Results of a Pilot Study on Adolescent Problem Gambling and Financial /Mathematical Literacy. 13. The Influenza Futures Markets. 13.1 Markets for Expert Information Retrieval. 13.2 Adaptive Seasonal Time Series Modeling. 13.3 Forecasting Weekly Influenza/Pneumonia Deaths. Index. List of Figures.

**ИИ:** разошлись — Opus ? (другое: Mostly a book on market forecasting, but chapter 12.4 reports a pilot study on adolescent problem gambling; screen and sports betting unknown.); Sonnet -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: Book on forecasting and modeling financial and sports betting markets; the adolescent problem gambling pilot chapter is minor, so the book is mainly market modeling.)

**Решение:** -

---

### 1361 · R7456

**Sociodemographic and Substance Use Correlates of Gambling Behavior in the Canadian General Population**

2010 · Journal of Addictive Diseases · article · en · https://doi.org/10.1080/10550887.2010.489447

This study describes sociodemographic and substance use correlates of gambling behaviors, measured among 9,481 past-year gamblers from the Canadian general population. Compared to non-problem gamblers in this study (N=8,035), the 98 problem gamblers who scored 8 or more points on the Canadian Problem Gambling Research Index were more likely to report being "drunk or high" while gambling (adjusted odds ratio [AOR]: 8.92; 95% confidence interval [CI]: 5.46,14.55; p<.001), to admit to having an alcohol or drug problem (AOR: 3.80; 95% CI:2.21,6.52; p<.001), and to use electronic gambling devices (AOR: 4.85; 95% CI: 3.08-7.66; p<.001).

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Canadian general population survey of past-year gamblers using CPGI and gambling activity correlates; sports betting likely among activities.

**Решение:** =

---

### 1362 · R7481

**Exploring youth gambling in Croatia – pilot research results**

2010 · conference object · und

There has been no systematic research about youth gambling in Croatia, although some problem behavior researches as well as clinical work with youth problem behaviors indicate that it is a growing and present issue. Within this context, a need for a scientific approach in exploring youth gambling in Croatia arose. A comprehensive research is planed for academic year 2010/2011 (with the financial support of Croatian Lottery), whereas in this paper the results of a pilot research conducted in the City of Zagreb will be presented. Research included 261 high-school students (58, 2% males and 41, 8% females), from three different types of school. The mean age of participants is 16, 51 years (SD=1, 15). Major aims of pilot research were to (1) explore gambling habits, (2) assess gambling risks and (3) to test different instruments in Croatian cultural context. Results show that sport betting, scratch cards, lottery and games of skills for money are the most frequent among Zagreb adolescents. Boys gamble more often than girls and their level of gambling risk is higher, whereas there are no differences in levels of gambling risks regarding type of school and age. Results also indicate more positive attitudes towards gambling among risk and problem gamblers. In accordance with other foreign researches, a strong correlation between problem gambling and other risk / delinquent behavior, as well as some psychopathic traits was found.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Survey of adolescents measuring sports betting participation and gambling risk/problem gambling levels with instruments being tested.

**Решение:** =

---

### 1363 · R7492

**Your Mother Should Know: A Comparison of Maternal and Paternal Attitudes and Behaviors Related to Gambling among Their Adolescent Children**

2010 · International Journal of Mental Health and Addiction · review, article · en · https://doi.org/10.1007/s11469-010-9279-0

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; parent survey on gambling attitudes and behaviours. Unclear whether sports betting participation or a problem-gambling screen was measured.

**Решение:** =

---

### 1364 · R7501

**Examining the psychological factors associated with fantasy sports participants**

2010

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; a 2010 survey of fantasy sports participants' psychological factors could include a problem-gambling measure, but may be non-money fantasy sports.

**Решение:** =

---

### 1365 · R7504

**Present state and tasks of the sport lottery ticket in China**

2010 · 神戸大学大学院人間発達環境学研究科研究紀要 · article · ja

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the title points to a descriptive overview of China's sports lottery, but it can't be ruled out without the full text.

**Решение:** =

---

### 1366 · R7505

**A Study on the Problems and Countermeasures of Sports Lotteries in China**

2010

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; title suggests a policy analysis of China's sports lottery, but it could include a survey of lottery players.

**Решение:** =

---

### 1367 · R7507

**Gambling in Brazil: Lifetime prevalences and socio-demographic correlates**

2010 · Psychiatry Research · article · en · https://doi.org/10.1016/j.psychres.2010.04.014

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** + · обе модели · опрос населения об азартных играх · No abstract; likely the Brazilian national household survey using SOGS, so activity-level problem gambling data are plausible.

**Решение:** =

---

### 1368 · R7508

**Las apuestas deportivas en Euskadi**

2010 · Dialnet (Universidad de la Rioja) · article · es

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Title on sports betting in the Basque Country with no abstract; could be a regulatory paper or an empirical survey.

**Решение:** =

---

### 1369 · R7512

**Understanding the impact of gambling with special reference to Thailand**

2010 · University of Birmingham Institutional Research Archive (University of Birmingham) · review, dissertation · en

This thesis mainly consists of three empirical chapters related to understanding the characteristics, economic impact and the demand for gambling in Thailand. Beginning with a review of the theoretical and empirical literature, this confirms that socio-economic and demographic data are important determinants of the level of gambling participation and gambling expenditure. A Logit model is then used to estimate the participation of gambling. The results suggest that the number games, such as the government lottery, the underground lottery, are popular among old gamblers whereas football betting is popular for adolescents. In the past, most casino customers were old gamblers, but at present the number of young gamblers who participate in casino has considerably increased. A Tobit model is employed to estimate the level of gambling frequency and gambling expenditure. The estimations reveal that there is a “supplementation effect” of casino on other gambling types and the effect also appears among the number games. The gambling expenditures on the number games are high in the group of gamblers who have undergraduate degree or lower while the expenditures on casino and football betting are high in the group of gamblers who have undergraduate degree. However, a higher education level leads to a lower level of gambling expenditures. The focus is then centred on the 2-3 digit lottery. The rational addiction model is tested for the case of the 2-3 digit lottery. In the addiction framework, the 2-3 digit lottery is found to be an addictive goods and the addiction is “myopic addiction”. This finding is confirmed by Instrumental Variable estimation.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Economics thesis on Thai gambling survey data covering football betting; problem-gambling screen not mentioned but the survey might include one.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Thai gambling economics thesis on participation, expenditure and rational addiction models; no problem-gambling screening instrument is mentioned.)

**Решение:** ?

---

### 1370 · R7522

**Gambling and Problem Gambling Across the Lifespan**

2010 · Journal of Gambling Studies · article · en · https://doi.org/10.1007/s10899-010-9195-z

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; likely a US national survey across age groups measuring problem gambling, possibly by activity including sports betting.

**Решение:** =

---

### 1371 · R7551

**체육진흥투표권 구매자의 도박열정과 도박자아효능감 및 정서지능의 관계**

2010 · 한국스포츠학회지 · article · ko

The purpose of this study was to investigated whether gambling passion and gambling self efficacy would be related to emotional intelligence to control sports lottery a kind of gambling and whether gambling self efficacy would mediate the relationship between passion and emotional intelligence. The subjects of this study were a total of 258 participants and completed an gambling passion scale, a gambling refusal self efficacy scale and emotional intelligence scale. The methods of the statistical analysis used in this study was the structure equation modeling, analysis by using SPSS PASW 17.0 and AMOS 7.0. As the results of the analysis, the findings of this study were as follows. First, obsessive passion factors not influences gambling self efficacy. Second, harmonious passion factors influences gambling self efficacy. Third, obsessive passion factors not influences emotional intelligence. Forth, harmonious passion factors influences emotional intelligence. Finally, gambling self efficacy factors influences emotional intelligence. Gambling self efficacy partially mediated the relationship between gambling passion and emotional intelligence

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Survey of Korean sports lottery (Sports Toto) buyers; listed scales are passion, self-efficacy and emotional intelligence; a problem-gambling screen isn't mentioned.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Survey of Korean sports lottery purchasers using gambling passion, refusal self-efficacy and emotional intelligence scales; no problem-gambling screening instrument apparent.)

**Решение:** ?

---

### 1372 · R7557

**Persistence in soccer betting : the effects of secondary knowledge, risks & earnings on youth gamblers decision to continue or quit.**

2009 · DR-NTU (Nanyang Technological University) · report · en

Soccer bettors believe that the information they encompass and their recent winning streak makes them skilled in predicting the outcomes of soccer matches. Thus they often naively choose to continue gambling, even when they are in deficit. This study investigated the effects of (a) the type of soccer knowledge (odds or background information) utilized, (b) amount of stake (high or low), (c) the reinforcement outcome (high profit, high loss, low profit and low loss) and (d) the effect of BIS and BAS personality on soccer bettor’s persistence in a betting scenario. 199 male undergraduates from Nanyang Technological University participated in this experimental study. The findings revealed that the type of soccer knowledge, amount of stake, degree of earnings, and the BAS Drive and Reward Responsiveness variables were not significant predictors of one’s decision to continue or quit gambling. However, the BIS and the BAS Fun Seeking scales proved to be significant predictors.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Experimental study of 199 male undergraduate soccer bettors; no problem-gambling instrument mentioned, though a screen like SOGS may have been used.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Experimental study of undergraduates' persistence in a hypothetical soccer betting scenario; measures BIS/BAS personality, no problem-gambling instrument reported.)

**Решение:** -

---

### 1373 · R7574

**Let the Preseason Begin: Want to Play?**

2009

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the vague title might be about fantasy sports or betting, so relevance can't be ruled out.

**Решение:** =

---

### 1374 · R7575

**A cross-sectional study of problem and pathological gambling in patients with schizophrenia/schizoaffective disorder.**

2009 · The Journal of clinical psychiatry · comparative study, journal article · eng · https://doi.org/10.4088/jcp.08m04359

Community data suggest frequent co-occurrence between schizophrenia/schizoaffective disorder and problem gambling. However, gambling behaviors in large samples of patients with schizophrenia/schizoaffective disorder have not been systematically examined to date. A sample of outpatient subjects (N = 337) diagnosed with either schizophrenia or schizoaffective disorder and who were treated in either the VA Connecticut Healthcare System or the Connecticut Mental Health Center was interviewed in order to examine the prevalence estimates and clinical correlates of problem and pathological gambling. Multinomial logistic regression models investigated clinically relevant measures in recreational or problem/pathological gamblers, as compared to nongamblers. Data were collected between June 2002 and November 2003. Sixty-five participants (19%) met criteria for past-year problem/pathological gambling, with 10% meeting criteria for pathological gambling. Significant correlates of problem and pathological gambling from multivariable models included greater alcohol use severity (P = .007), higher depression scores (P = .04), and more outpatient mental health care utilization (P = .03). Participants with problem/pathological gambling were more likely than recreational gamblers to gamble for excitement, gamble more frequently and heavily, and report either sports or card gambling as favorite. A substantial proportion of individuals in treatment for psychotic disorders report past-year gambling problems. Patients with co-occurring alcohol use problems and depression may be at particularly high risk. These findings suggest the need for improved prevention and treatment efforts related to problem/pathological gambling in individuals with psychotic disorders.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Outpatients with schizophrenia screened for problem gambling; sports gambling mentioned only as a favourite game, so participation data are unclear.

**Решение:** =

---

### 1375 · R7578

**Fantasy sport consumer behavior: An analysis of participant attitudes and behavioral intentions**

2009 · Scholarship & Creative Works - Digital UNC a service of University Libraries (University of Northern Colorado) · dissertation · en

Eddy, and Lori Braa.Thank you for the years of advice, entertainment, and companionship.Lastly, and most importantly, I would like to thank my beautiful and talented wife, Lori.There are no words to explain how much you mean to me and how much you helped in this process.Not only did you proofread nearly the entire document, but your patience, strength, and ability to keep me grounded are the reasons I was able to keep my sanity and survive.You give me the confidence to move mountains.

**ИИ:** разошлись — Opus -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: 2009 consumer-behaviour dissertation on fantasy sport attitudes and intentions; predates DFS, and no problem-gambling instrument is likely.); Sonnet ? (нет аннотации: Abstract is only acknowledgments text; a fantasy sport participant survey (2009) may or may not involve money or a problem-gambling measure, so full text is needed.)

**Решение:** ?

---

### 1376 · R7579

**Fantasy Sports Consumer Behavior : An Investigation into the Differing Consumption Modes of Fantasy Football Participants**

2009 · review

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract. The title points to consumer behaviour among fantasy football players, which probably didn't use a problem-gambling measure, but this can't be ruled out.

**Решение:** =

---

### 1377 · R7583

**Examining the trait and functional motive antecedents of four gambling activities: slot machines, skilled card games, sports betting, and promotional games**

2009 · Journal of Consumer Marketing · article, journal-article · en · https://doi.org/10.1108/07363760910940483

Purpose The purpose of this paper is to explore the functional motive and trait antecedents of four forms of gambling – slot machines, skilled card games, sports betting, and participating in marketing promotional games such as sweepstakes and contests. Design/methodology/approach A hierarchical model of motivation and personality (3M model) was employed to investigate the trait and functional motive antecedents of four gambling activities. Five motives for gambling were identified – money, excitement, social interaction, escape from problems, and self‐esteem enhancement. In addition, the effects of demographic variables (i.e. age, gender, and education) on four gambling types were examined. A total of 1,158 responses were collected from an online consumer panel. Findings The results suggest that the four forms of gambling have divergent motives, traits, and demographic profiles. Research limitations/implications Future research should further explore other possible traits in predicting different gambling activities (e.g. superstitious beliefs). Another limitation of the study is the online panel sample, which is somewhat older and more highly educated than the general public. Practical implications The findings will help marketers better segment the market based on unique profiles of personality traits, functional motives, and demographic variables associated with each gambling type and design communication strategies to reach the targeted consumers. Originality/value Previous researchers have neither investigated the functional motives for gambling nor compared the motives for divergent forms of gambling. This research employs a hierarchical model (3M model) to investigate the trait and functional motive predictors of multiple forms of gambling.

**ИИ:** разошлись — Opus -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Consumer panel survey of motives, traits and demographics for sports betting and other gambling; no problem-gambling instrument mentioned.); Sonnet ? (неясно, измеряли ли проблемную игру: Online panel survey (n=1,158) covering sports betting, focused on motives and traits; the abstract doesn't say whether problem gambling was measured.)

**Решение:** ?

---

### 1378 · R7588

**Behavior Characteristics of Sports Lottery Consumers in Shenyang Urban District and the Influencing Factors**

2009

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; survey of sports lottery consumers' behaviour, problem gambling measurement unknown.

**Решение:** =

---

### 1379 · R7591

**Internet Gambling, Health, Smoking and Alcohol Use: Findings from the 2007 British Gambling Prevalence Survey**

2009 · International Journal of Mental Health and Addiction · review, article · en · https://doi.org/10.1007/s11469-009-9246-9

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: No abstract; secondary analysis of 2007 BGPS (measured activities, DSM-IV/PGSI), may report sports betting and problem gambling.); Sonnet + (опрос населения об азартных играх: BGPS 2007 national survey (Griffiths et al. 2009) measured gambling activities and problem gambling; activity tables likely allow sports betting PG figures. Abstract missing, but the study is a survey.)

**Решение:** ?

---

### 1380 · R7592

**Investigation of Sports Lottery Consumption Market in Southwest Region**

2009 · Journal of Jianghan University · article · en

Based on the input(incentive),internal,external and output(response) factors,explores the formation and changes of sports lottery consumption in the southwest region by applying the methods of questionnaire and interview.Analyzes the consumers' characteristics of composition and behavior,obtains the factors restricting the consumption of the lottery.Proposes countermeasures and suggestions to solve the existing problems.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Questionnaire survey of sports lottery consumers focused on the market; the abstract doesn't say whether a problem-gambling instrument was used.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Questionnaire survey of sports lottery consumers' behaviour and consumption factors; no indication a problem-gambling instrument was used.)

**Решение:** ?

---

### 1381 · R7594

**The development of a multi-dimensional gambling accessibility scale.**

2009 · Journal of gambling studies · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1007/s10899-009-9144-x

The aim of the current study was to develop a scale of gambling accessibility that would have theoretical significance to exposure theory and also serve to highlight the accessibility risk factors for problem gambling. Scale items were generated from the Productivity Commission's (Australia's Gambling Industries: Report No. 10. AusInfo, Canberra, 1999) recommendations and tested on a group with high exposure to the gambling environment. In total, 533 gaming venue employees (aged 18-70 years; 67% women) completed a questionnaire that included six 13-item scales measuring accessibility across a range of gambling forms (gaming machines, keno, casino table games, lotteries, horse and dog racing, sports betting). Also included in the questionnaire was the Problem Gambling Severity Index (PGSI) along with measures of gambling frequency and expenditure. Principal components analysis indicated that a common three factor structure existed across all forms of gambling and these were labelled social accessibility, physical accessibility and cognitive accessibility. However, convergent validity was not demonstrated with inconsistent correlations between each subscale and measures of gambling behaviour. These results are discussed in light of exposure theory and the further development of a multi-dimensional measure of gambling accessibility.

**ИИ:** разошлись — Opus + (игроки, есть ставки на спорт и инструмент: Survey of 533 venue employees covering sports betting accessibility and gambling frequency by form, with PGSI; could report PG among sports bettors.); Sonnet ? (неясно, есть ли ставки на спорт: Survey of 533 gaming venue employees with PGSI and sports betting accessibility and frequency; unclear whether PG among sports bettors is reportable.)

**Решение:** ?

---

### 1382 · R7595

**Gambling, gambling activities, and problem gambling.**

2009 · Psychology of addictive behaviors : journal of the Society of Psychologists in Addictive Behaviors · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1037/a0014181

This research examined similarities and differences between gambling activities, with a particular focus on differences in gambling frequency and rates of problem gambling. The data were from population-based surveys conducted in Canada between 2001 and 2005. Adult respondents completed various versions of the Canadian Problem Gambling Index (CPGI), including the Problem Gambling Severity Index (PGSI). A factor analysis of the frequency with which different gambling activities were played documented the existence of two clear underlying factors. One factor was comprised of Internet gambling and betting on sports and horse races, and the other factor was comprised of lotteries, raffles, slots/Video Lottery Terminals (VLTs), and bingo. Factor one respondents were largely men; factor two respondents were more likely to be women and scored significantly lower on a measure of problem gambling. Additional analyses indicated that (1) frequency of play was significantly and positively related to problem gambling scores for all activities except raffles, (2) the relationship between problem gambling scores and frequency of play was particularly pronounced for slots/VLTs, (3) problem gambling scores were associated with playing a larger number of games, and (4) Internet and sports gambling had the highest conversion rates (proportion who have tried an activity who frequently play that activity).

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Canadian population surveys used the CPGI/PGSI and looked at problem gambling by activity, including sports betting.

**Решение:** =

---

### 1383 · R7600

**Kockanje u sportskim kladionicama - Pilot istraživanje među studentima Sveučilišta u Zadru**

2009 · Kriminologija & socijalna integracija : časopis za kriminologiju, penologiju i poremećaje u ponašanju · article · sr · https://hrcak.srce.hr/45268

Games of chance, united under name of gambling, are becaming more popular in the modern times, and the number of gamblers increases progresively with the decrease of economic power of people. According to inveterate views on gambling in sports betting is a “benign” form of games of chance. So this kind of “entertainment is being popularized mora and mora even through national media. However, for some of the gambler the game becomes the center of interests, because of gambling they neglect their work, styding and other activities. The individual control is being decreased even further by obsesively gambling everyday, and instead of entertaining the game starts to control people leading them to addiction. In this research we study some aspects of the role of betting in everyday life of students. The sample consisted of 113 questioned persons, and during the examination was used a questionnaire thai was mode for that purpose and theoretically measurs the freqvency of betting, some attitude and motivation. The research has confi rmend aur assumption that the games on chance are concerning because of their increase. It pointed to one unpredicted fact the largest number of students gamble because they are bored. In that way, the hedonism, as the primary cause of excessive alcohol consumation among the youth and one of the most signifi cantcauses of drug consumation, hasshown to be a key factor in students playing games on chance. Igre na sreću, objedinjene zajedničkim nazivom kockanje, sve su popularnije u moderno doba, a broj igrača raste progresivno sa slabljenjem ekonomske moći ljudi. Prema uvriježenim stajalištima klađenje u sportskim kladionicama je “benigni” oblik igara na sreću, pa se ova “zabava” i kroz državne medije sve više popularizira. No, za neke igrače klađenje postaje centar životnih interesa, zbog kockanja zapostavljaju posao, učenje i druge obveze, u slobodnom vremenu igra dominira nad drugim aktivnostima. Svakodnevno bavljenje igrom sve više smanjuje osobnu kontrolu, a umjesto zabave igra počinje vladati ljudima otvarajući put nastanku bolesti ovisnost. U ovome pilot istraživanju ispitali smo samo neke aspekte uloge klađenja u sportskim kladionicama u svakodnevnom životu studenata. Uzorak se sastojao od 113 ispitanika, a prilikom ispitivanja korišten je upitnik konstruiran u tu svrhu koji mjeri učestalost klađenja, određene stavove studenata, motivaciju za igranje i drugo. Istraživanje je potvrdilo osnovnu pretpostavku da se studenti relativno učestalo klade u sportskim kladionicama (na razini europskog prosjeka). Ukazalo je i na neočekivanu činjenicu da najveći broj studenata igra jer im je dosadno. Tako se hedonizam, kao glavni motiv prekomjernog pijenja alkohola kod mladeži i jedan od značajnih uzroka konzumiranja droga, pokazao ključnim faktorom u bavljenju igrama na sreću kod studenata.

**ИИ:** разошлись — Opus -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Pilot survey of 113 students' sports betting using a purpose-built questionnaire on frequency, attitudes and motives; no problem-gambling instrument reported.); Sonnet ? (неясно, измеряли ли проблемную игру: Pilot survey of 113 students on sports betting; questionnaire measured frequency, attitudes and motivation, but the abstract doesn't say whether a problem-gambling instrument was used.)

**Решение:** ?

---

### 1384 · R7604

**Profiling the Sport Consumption Attitudes and Behaviours of Fantasy Football Players**

2009 · review

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: There's no abstract; the title suggests sport-marketing profiling of fantasy football players' consumption, with no sign of a problem-gambling measure.); Sonnet ? (нет аннотации: No abstract; fantasy football player survey (2009) may involve money but likely sport consumption only; problem gambling measurement unclear.)

**Решение:** -

---

### 1385 · R7606

**Understanding experiences of fantasy sport participation**

2009 · Swinburne figshare (Swinburne University of Technology) · conference-paper · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; fantasy sport participation study, possibly qualitative or not money-based, but problem-gambling measurement cannot be ruled out.

**Решение:** =

---

### 1386 · R7617

**Disordered gambling, type of gambling and gambling involvement in the British Gambling Prevalence Survey 2007**

2009 · European Journal of Public Health · article · en · https://doi.org/10.1093/eurpub/ckp177

BACKGROUND: The purpose of this study was to examine the relationships between types of gambling and disordered gambling, with and without controlling for gambling involvement (i.e. the number of types of games with which respondents were involved during the past 12 months). METHODS: We completed a secondary data analysis of the 2007 British Gambling Prevalence Survey (BGPS), which collected data in England, Scotland and Wales between September 2006 and March 2007. The sample included 9003 residents, aged 16 or older, recruited from 10 144 randomly selected addresses. 5832 households contributed at least one participant. Post-facto weighting to produce a nationally representative sample yielded 8968 observations. The BGPS included four primary types of measures: participation in gambling (during the past 12 months and during the past 7 days), disordered gambling assessments, attitudes toward gambling and descriptive information. RESULTS: Statistically controlling for gambling involvement substantially reduced or eliminated all statistically significant relationships between types of gambling and disordered gambling. CONCLUSIONS: Gambling involvement is an important predictor of disordered gambling status. Our analysis indicates that greater gambling involvement better characterizes disordered gambling than does any specific type of gambling.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · BGPS 2007 secondary analysis of disordered gambling (DSM-IV/PGSI) by gambling type; BGPS types include sports and event betting.

**Решение:** =

---

### 1387 · R7625

**An analysis of sport gambling behaviour among university students : social psychology of sport**

2009 · African Journal for Physical Health Education Recreation and Dance · article · en · https://doi.org/10.4314/ajpherd.v15i4.47284

Gambling is probably as old as society, but recently formal betting on sport events has started making rapid inroads on the African continent. Political changes in South Africa in the past two decades have resulted in explosive growth of the gambling industry and increased gambling opportunities dramatically. Since casino gambling was legalized in South Africa in 1996, the gambling industry has become a fast-growing business offering a variety of gambling options to individuals. It now permeates almost every segment of society including the family, communities, media and government. Consequently, it is inevitable that university students will be exposed to gambling and its promotion on a daily basis through a variety of sources which include coverage in print and broadcast media, observation of the sale of lottery tickets, visits to the casino with friends or family and watching friends betting on sport events. The aim of this study was to extend previous research on gambling by empirically examining gambling behaviours of university students with the intention of contributing to a better understanding of their gambling behaviour and suggest preventative measures to reduce problems associated with gambling. A 22-item questionnaire, based on an extensive literature study of gambling as well as items obtained from the South Oaks Gambling Screen (SOGS) (Lesieur & Blume, 1987), was developed to investigate different aspects of gambling behaviour. Exploratory factor analysis was conducted on the items. The responses from the gambling questionnaire were subjected to principle axis factor analysis. Using a minimum eigenvalue of 1.0 and a varimax rotation, a total of 3 first order factors namely behaviour, escapism and motives were identified. The findings of the current study found that gambling is not a risk for most university students. However, it is important that addictive gamblers be identified and treated as their behaviour may have consequences not only for other students but also for the university.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Student sport gambling survey with a custom questionnaire that borrows SOGS items; unclear if a validated problem-gambling case definition was applied.

**Решение:** =

---

### 1388 · R7630

**Gambling and Professional Athletics**

2009

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the title could mean a survey of athletes' gambling or a commentary, so the full text is needed.

**Решение:** =

---

### 1389 · R7634

**Effects of conjunction fallacies in evaluating football bets.**

2009 · article · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: No abstract; probably a cognitive-bias experiment on judging football bets, and a problem-gambling measure is unlikely but can't be ruled out.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Title suggests a cognitive-bias study of evaluating football bets; likely no problem-gambling instrument. No abstract, so this is a judgment from the title.)

**Решение:** ?

---

### 1390 · R7636

**Prevention and Treatment (Sports Gambling Warning Signs)**

2009 · article · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: No abstract; the title points to an informational or encyclopedia-style piece on prevention and warning signs, not a survey.); Sonnet ? (нет аннотации: No abstract; the title suggests a prevention/warning-signs piece on sports gambling, probably non-empirical, but its content can't be confirmed.)

**Решение:** ?

---

### 1391 · R7645

**Fantasy Sports: History, Game Types, and Research**

2009 · article · en · https://doi.org/10.4324/9780203873670-31

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -1 (обзор, комментарий, теоретическая, правовая или регуляторная работа: The title points to a descriptive overview of fantasy sports history and game types, not an empirical survey measuring problem gambling.); Sonnet ? (нет аннотации: No abstract; title suggests a fantasy sports overview (likely a review), but it might report data on problem gambling among players.)

**Решение:** ?

---

### 1392 · R7662

**An investigation and analysis of the sports'lottery consumers'situation in Anhui province**

2009 · Liaoning tiyu ke-ji · article · en

This article takes the consumers of sports lottery as the object of study,which selected from some representative regions in Anhui province,and sums up their present situation through analyzing their constitution,psychology,behavior of consumer characteristics;and then proposes some suggestions for the development of sports lottery in Anhui province.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of sports lottery consumers looking at psychology and behaviour; the abstract doesn't say whether a problem-gambling instrument was used.

**Решение:** =

---

### 1393 · R7663

**Investigation and Analysis of Sports Gambling Attitudes,Behavior and Motivation of College Students in He'nan Province**

2009

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Survey of college students' sports gambling; no abstract, so unclear whether a problem-gambling instrument was used.

**Решение:** =

---

### 1394 · R7668

**Internet Gambling: Prevalence, Patterns, Problems, and Policy Options**

2009 · Open ULeth Scholarship (OPUS) (University of Lethbridge) · report · en

Beginning in the early to mid-1990s, as Internet access expanded into workplaces and private residences, gamblers in Western societies were introduced to a new realm of gambling opportunities, based on the Internet. Each of the traditional forms of gambling, widely available in land-based venues, soon appeared in electronic format over the Internet, and have since been easily accessible to any person with an Internet connection and means of electronically transferring money. Virtually mediated casino games, slot machines, bingos, lotteries, sports wagering, horse race betting, and skill games are all now readily accessible, with new forms of gambling and new ways of remote gambling (e.g., interactive television) continually being added. While Internet gambling is becoming a more socially acceptable and legally available activity, the expansion of Internet gambling is outpacing peoples' understanding of the phenomenon, as well as outpacing many of the laws that are supposed to regulate gambling activity. Consequently, we find ourselves in a situation where we have insufficient knowledge of online gambling, including the characteristics of gamblers, the dynamics of Internet gambling behavior, the potential link between Internet gambling and problem gambling, and the most appropriate regulatory and legislative stance to take with respect to Internet gambling. In light of persisting ambiguities and gaps in the existing academic and policy literature, the present report comprises one of the most thorough academic examinations of Internet gamblers to date. The first part of the report provides a context for the present investigation by providing a comprehensive review of the history of Internet gambling, the current worldwide situation, regulatory frameworks for Internet gambling in different jurisdictions, and concerns with Internet gambling. The second part of the report discusses results from two surveys. The first survey is a random digit dial (RDD) Telephone Survey of 8,498 Canadian adults conducted from January 2006 to June 2007 ('Canadian Telephone Survey'). The second survey is an online self-administered survey of 12,521 adults, from 105 countries, conducted from June to December 2007 ('International Online Survey'). These surveys collected information about people‟s demographic characteristics, land-based gambling behaviour, Internet gambling behaviour, stock market gambling, attitudes toward gambling, motivations for gambling on the Internet, gambling fallacies, and problem gambling as assessed by the Canadian Problem Gambling Index (CPGI). The International Online Survey also served as an intervention, as participants were provided with detailed feedback about their gambling behaviour relative to others, a projection of their yearly expenditures, explanations of why certain beliefs they held were gambling fallacies, their risk for becoming a problem gambler, their current score on the Canadian Problem Gambling Index (CPGI), Internet links to treatment resources, and a demonstration of how their predictive ability for random events is no better than chance, and how there is no relationship between their prediction confidence and prediction success.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Large Canadian and international surveys measuring gambling activities including sports wagering, with CPGI; full report likely shows problem gambling by activity.

**Решение:** =

---

### 1395 · R7674

**Persistence in soccer gambling : the effects of secondary knowledge, risks & earnings on youth gamblers decision to continue or quit**

2009

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; likely thesis on youth soccer bettors, could include problem-gambling screening.

**Решение:** =

---

### 1396 · R7675

**Sports betting - some psychosocial characteristic of different types of gamblers**

2009 · Socijalna psihijatrija · article · en

U ovom istraživanju bavili smo se ispitivanjem nekih karakteristika patoloskog sportskog klađenja. Istražili smo postoje li razlike između razlicitih kategorija kockara u impulzivnosti i traženju uzbuđenja, upotrebi psihoaktivnih sredstava te nekim ponasajnim aspektima sportskog klađenja. U istraživanju je sudjelovalo 95 muskih sudionika redovitih posjetitelja sportskih kladionica. Koristeci DSM-IV kriterije za poremecaj patoloskog kockanja podijelili smo sudionike u tri skupine: drustvene (do jedan zadovoljeni kriterij), rizicne (dva do cetiri zadovoljena kriterija) i moguce patoloske kockare (pet i vise zadovoljenih kriterija). Rezultati su pokazali da 10.5 % sudionika pripada kategoriji patoloskih kockara, a 42 % kategoriji rizicnih kockara. Patoloski i rizicni kockari se cesce klade, uplacuju vise novcane iznose za klađenje te sudjeluju u vecem broju kockarskih igara. Patoloski se kockari jos razlikuju od drustvenih u cescoj konzumaciji lakih droga. Razlika među skupinama nije se pokazala u konzumaciji cigareta niti alkohola. Patoloski i rizicni kockari postižu vise rezultate od drustvenih u impulzivnosti, ali nema razlike u odnosu na traženje uzbuđenja. Dobiveni rezultati su pokazali da među korisnicima sportskih kladionica ima znacajan broj ljudi poteskocama iz kruga patoloskog kockanja, sto ima implikacije za daljnja istraživanja i osmisljavanje preventivnih i kurativnih aktivnosti.

**ИИ:** + · обе модели · беттеры + инструмент · 95 regular sports betting shop visitors assessed with DSM-IV criteria; 10.5% possible pathological, 42% at-risk.

**Решение:** =

---

### 1397 · R7679

**GAMBLING IN SPORTS BETTING – PRELIMINARY RESEARCH AMONG STUDENTS ON UNIVERSITY OF ZADAR**

2009 · Kriminologija & socijalna integracija : časopis za kriminologiju, penologiju i poremećaje u ponašanju · article · hr

Igre na srecu objedinjene zajednickim nazivom kockanje, sve su popularnije u moderno doba, a broj igraca raste progresivno sa slabljenjem ekonomske moci ljudi. Prema uvriježenim stajalistima rijec je o benignom obliku igara na srecu, pa se ova zabava i kroz državne medije sve vise popularizira.No, za neke igrace klađenje postaje centar životnih interesa, zbog bavljenja igrom smanjuje se njihova osobna kontrola, a umjesto zabave igra pocinje vladati njime.na uzorku od 113 ispitanika ispitali smo važne aspekte igara na srecu (ucestalost, stavove, motivaciju i drugo). Istraživanje je potvrdilo hipotezu da se studenti relativno cesto klade, ali i na neocekivanu cinjenicu da veliki broj studenata to radi jer im je dosadno. Ovaj nalaz autori dodatno problematiziraju u svom radu.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Croatian student survey (n=113) on sports betting covering frequency, attitudes and motives; abstract doesn't say whether a problem-gambling instrument was used.

**Решение:** =

---

### 1398 · R7681

**พฤตกรรมการเลนพนนฟตบอลของนกศกษา: กรณศกษาสถาบนอดมศกษาแหงหนงในจงหวดขอนแกน**

2009 · RMUTP Research Journal Sciences and Technology · article · th · https://doi.org/10.14456/jrmutp.2009.13

บทคัดย่อการศึกษานี้มีวัตถุประสงค์เพื่อศึกษาพฤติกรรมการเล่นพนันฟุตบอลของนักศึกษาระดับอุดมศึกษา แห่งหนึ่งในจังหวัดขอนแก่น ผลการศึกษาพบว่า นักศึกษาเริ่มเล่นพนันฟุตบอลมาตั้งแต่สมัยเรียนในระดับ มัธยมศึกษา นอกจากที่ต้องการเชียร์ทีมฟุตบอลที่ตัวเองชื่นชอบเพื่อความสนุกสนานและตื่นเต้นในการติดตามชม การแข่งขันแล้ว ยังมีสาเหตุมาจากความอยากได้เงินเป็นปัจจัยหลัก เพื่อนำเงินไปเที่ยวสถานบันเทิง ซื้อของใช้ ฟุ่มเฟือยและราคาแพงตามสมัยนิยม ผลกระทบและปัญหาที่ใหญ่ที่สุดที่เกิดจากการเล่นพนันฟุตบอล คือ ปัญหา เรื่องการเงิน ซึ่งจะสร้างปัญหาต่อเนื่องไปยังปัญหาอื่น ๆ คือ ปัญหาความเครียดจากการเสียเงินพนัน ความเครียด ที่จะต้องหาเงินมาชำระถ้าเป็นหนี้ และปัญหาด้านสุขภาพจิตที่ต้องระแวงการถูกตามทวงหนี้ นอกจากนี้ยังมีปัญหา เรื่องความสัมพันธ์กับเพื่อนเปลี่ยนแปลงไป กล่าวคือ ผู้เล่นพนันฟุตบอลมักจะคุยกับเพื่อนน้อยลง ขาดเรียนบ่อย ครั้งขึ้น และอาจต้องหยุดพักการเรียน หากมีหนี้สินจำนวนมาก ๆคำสำคัญ : พนันฟุตบอล; พฤติกรรม; ขอนแก่น AbstractThe purpose of this study is to study the behaviors of undergraduate students in an institution in Khon Kaen province. The results showed that students began to gamble since they were at the secondary school. The causes of football gambling were not only from their desire to cheer up their favorite teams for enjoyment but also they wanted to gain more money that was highlighted as a main factor. This was because they would like to pay for their night life places or to luxurious dotain and expensive items. The main effect of the football gambling was financial problem which linked to endless problems such as stress and depression from losing the gambling, pressure from paying back the debt, having some mental problems and being afraid of being demanded to pay of a debt. Moreover, there were some problems on the relationship among friends because they skipped the classes and some might give up their study due to a huge amount of debt.Keywords : Football Gambling; Behavior; Khon Kaen

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Thai study of students who bet on football; the design looks descriptive or qualitative, and the abstract doesn't say whether a problem-gambling instrument was used.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Thai study of students' football gambling behaviour, causes and consequences; appears descriptive or qualitative, with no problem-gambling instrument mentioned.)

**Решение:** -

---

### 1399 · R7688

**스포츠 도박동기와 사회적응의 관계**

2009

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Korean study on sports gambling motives and social adjustment; probably a bettor survey, no abstract to tell whether problem gambling was measured.

**Решение:** =

---

### 1400 · R7690

**스포츠 도박동기와 사회적응의 관계**

2009 · article · ko

The purpose of this study was to examine into Sports Gambling Motives and Social Adaptation. the objects for the research are participants of cycling race, horse race samples of 321 questionnaires by convenience sampling is used as final research materials. The results by using frequency analysis, exploratory factor analysis, reliability analysis, multiple regression analysis with SPSS 15.0 are as follow; First, the Gambling Motives has influence on the addiction disposition. Second, the Gambling Motives has influence on the Social Adaptation. Third, the addiction disposition has influence on the Social Adaptation.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of cycling and horse race bettors; cycling may count as sports betting. It is unclear whether 'addiction disposition' was measured with a validated instrument.

**Решение:** =

---

### 1401 · R7692

**갬블링 열정척도를 통한 스포츠토토 이용객의 시장세분화 연구**

2009 · 관광연구저널 · article · ko

This study aims to segment Sports toto participants based on gambling passion scale(GPS) using a two-stage cluster analysis. To this end, surveys were conducted for Sports toto participants through both online and offline. The results of exploratory factor analysis indicate that the gambling passion of Sports toto participants was classified into obsessive passion(OP) and harmonious passion(HP) with high reliability. The GPS was also classified into three groups by using two stage cluster analysis based on GPS and respondents` characteristics: low-level gambling passion group, middle-level gambling passion group, and high-level gambling passion group. The results of one-way ANOVA reveal that there were significant differences among those three groups with respect to gambling motivation. The results also show that the mean value of Fun motivation factor received the highest evaluation, and the mean value of HP was much higher than that of OP, indicating that the Sport toto is likely to be perceived as one of leisure activities by its participants.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Survey of Sports Toto bettors using a gambling passion scale and motives; the abstract doesn't say whether a problem-gambling screen was used.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Survey of Sports Toto participants segmented by gambling passion scale and motivation; no problem-gambling screening instrument mentioned.)

**Решение:** ?

---

### 1402 · R7693

**Predictors of different types of recreational gambling among college students**

2008 · Rutgers University Community Repository (Rutgers University) · other literature type, thesis, review · en · https://doi.org/10.7282/t3f47pgq

The current study examined the prevalence, frequency, and predictors of gambling among young adult college students. Nine hundred and fourteen undergraduates from a Mid-Atlantic public university completed a survey to assess gambling behaviors and problems, along with various psychosocial factors that may account for gambling behaviors. Among the entire sample, 53% (n= 461) reported participating in some form of gambling activity during the past year. The most frequently endorsed gambling activity was playing board or card games for money, followed by playing the lottery, and betting on games of personal skill. In contrast to expectations, online gambling was not prevalent. Most student gamblers in this sample gambled for recreational reasons; only 2.5% and 1.5% fell in the problem or pathological range, respectively. Hierarchical regression analyses found different predictors for the two types of gambling, gaming activities and sports betting. Being male and high on novelty/excitement seeking were significantly related to the number of gaming activities participated in during the past year by college students. Binge drinking showed a strong trend as a predictor. For sports betting, being male accounted for the greatest amount of variance and binge drinking in the past year emerged as the only other significant predictor. Being Caucasian, however, showed a strong explanatory trend. Together, these findings provide valuable information about the predictors of college students' recreational gambling, which was found to represent the vast majority of all gambling behaviors among this sample of college students.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · College student survey measuring sports betting participation and problem/pathological gambling; may report PG among sports bettors.

**Решение:** =

---

### 1403 · R7703

**Problem Gambling - Pacific Islands Families Longitudinal Study: Final Report**

2008 · Tuwhera (Auckland University of Technology) · other · en

Background The Pacific Islands Families (PIF) study has been following a cohort of Pacific children since the year 2000. The purpose of this prospective study is to determine the pathways leading to optimal health, development and social outcomes for Pacific children and their families. Pacific peoples are at high risk for developing problem gambling (the highest risk of the ethnicities living in New Zealand) and have shown heterogeneous differences between the different Pacific cultures in relation to gambling. This highlights the need for significant further study in this area. The longitudinal cohort PIF study has offered a valuable and unique opportunity to study gambling and problem gambling within a Pacific family and child development context, allowing for sub-analyses of the major ethnic Pacific groups and the potential to begin identifying risk and protective factors in the development of problem gambling. In April 2006, the Gambling Research Centre at Auckland University of Technology was commissioned by the Ministry of Health to conduct the research project Problem Gambling - Pacific Islands Families Longitudinal Study. The purpose of this project was to enhance and add value to the existing PIF study by incorporating a substantial gambling component in the six-year data collection phase. Methodology A range of gambling-related questions was incorporated into the interview questionnaire protocols for mothers and fathers of the cohort children at the six-year data collection phase. The questions related to gambling participation and to having problems because of someone else’s gambling, and included problem gambling screens (Problem Gambling Severity Index [PGSI] for mothers and fathers, and South Oaks Gambling Screen - Revised [SOGS-R] for fathers only). All cohort parents (mothers and fathers) were invited to participate in the PIF study six-year assessment. In keeping with previous procedures, all participants were visited in their homes by gender- and ethnically-matched interviewers to complete the structured assessments. Results and discussion This study has significantly increased the knowledge around Pacific peoples’ gambling since the nature of the general population cohort has allowed for analyses to be performed by different Pacific ethnicities and other cultural and demographic variables, which is not usually possible in general population studies due to small Pacific participant sample sizes. Whilst the data in this report represent a cross-section in time, at the six-year data collection point for the cohort, the potential exists for gambling to continue to be a significant part of future data collection phases. This will allow for longitudinal analyses to explore the links between parental gambling and child development of gambling behaviours, as well as risk and protective factors for problem gambling amongst not only adults but also children as they progress through teenage years and into adulthood. It will also allow for exploration of changes over time in regard to gambling participation and problem gambling risk and protective factors. Gambling participation was lower amongst the participants in the cohort than would be expected though a bimodal distribution of gambling (low numbers of people gambling with those who do gamble reporting higher than average expenditure on gambling) was apparent, as was expected from previous national prevalence surveys. Thirty-six percent of all mothers and 30% of all fathers reported that they had gambled in the previous 12 months. Of the mothers and fathers who had gambled, Lotto was the form of gambling most played (89% mothers, 88% fathers) with much lower levels of participation in other forms of gambling. Gender differences were apparent for non-Lotto forms of gambling with mothers participating in Housie and Instant Kiwi gambling (both at 11%) and fathers participating in casino electronic gaming machine (20%), non-casino electronic gaming machine (15%) and Instant Kiwi (14%) gambling. The most preferred forms of gambling were Lotto (80% of gamblers) followed by Housie (9%) for mothers and Lotto (78%) followed by horse/dog race betting (6%) and sports betting at the TAB (5%) for fathers. Amongst those who gambled, four percent of mothers and 16% of fathers were classified as moderate risk or problem gamblers using the PGSI. Using the SOGS-R, 10% of fathers were classified as problem or probable pathological gamblers. Ethnicity appeared to be a key factor in mothers’ gambling but not for fathers. Tongan mothers were less likely to gamble than Samoan mothers; however, those who gambled were 2.4 times more likely to be classified as at risk/problem gamblers, indicating that Tongan mothers are at higher risk for developing problem gambling. Cultural orientation appeared to be related to gambling (in some cases, less gambling) both for mothers and fathers, though different orientations were associated with gambling for the different genders. Fathers who were in the higher total net weekly household income brackets (>$500) were more likely to gamble than fathers in the lower income bracket (<$501), whilst mothers with post-school qualifications were less likely to gamble (0.7 times) than mothers with no formal qualifications. Further gender differences were noted in terms of associations between gambling and health. For fathers both gambling and at risk/problem gambling were associated with psychological distress. Fathers who gambled were more likely to be perpetrators as well as victims of verbal aggression than fathers who did not gamble, with at risk/problem gambling also being associated with physical violence. These findings were not noted amongst mothers whereby at risk/problem gamblers were significantly less likely to perpetrate violence than non-problem gamblers. Not unexpectedly, smoking and alcohol consumption (particularly at higher/harmful levels) were associated with gambling (though not with at risk/problem gambling) both for mothers and fathers. In addition, mothers who drank alcohol were also more likely to have a weekly gambling expenditure in the upper quartile (≥$20) than mothers who did not drink, with increased frequency and amount of consumption associated with increased risk of higher gambling expenditure; this finding was not noted amongst fathers. In addition, a clear association was noted between higher (upper quartile) expenditure on gambling and being classified (PGSI) as a low risk/moderate risk/problem gambler with at risk/problem gambler classified mothers three times more likely, and at risk/problem gambler classified fathers six times more likely to spend in the upper quartile on gambling than non-problem gamblers. The problem gambling screens used (PGSI for mothers and fathers and SOGS-R for fathers only) showed very good internal consistency (reliability). There was good agreement between the PGSI and SOGS-R with 94% of fathers identified as problem gamblers by the SOGS-R also being classified as at risk/problem gamblers by the PGSI. In addition, questions related to lying about gambling and betting more than intended also associated well with the PGSI and SOGS-R within this Pacific cohort. The results suggest that the use of any of these problem gambling screens may be valid for use within a general Pacific population, though this would need to be further tested. Four percent of mothers and ten percent of fathers reported that they had experienced problems because of someone else’s gambling. The findings detailed in this report indicate that different gender and ethnic differences exist amongst Pacific people who should, therefore, not be considered as a homogeneous group. This has implications for service provision by organisations providing services for Pacific people as well as social marketing campaigns around gambling and problem gambling.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Cohort survey of Pacific parents measuring gambling participation including TAB sports betting, with PGSI and SOGS-R problem gambling screens.

**Решение:** =

---

### 1404 · R7716

**Glücksspielteilnahme und Glücksspielprobleme in Deutschland: Ergebnisse einer bundesweiten Repräsentativbefragung**

2008 · Suchttherapie · article, review · de · https://doi.org/10.1055/s-2008-1042440

Fragestellung: Es werden die Ergebnisse einer repräsentativen Befragung zum Glücksspielverhalten der in Deutschland lebenden Bevölkerung dargestellt. Methodik: Die Datenerhebung fand vom 17.11. bis zum 5.12.2006 statt und erfolgte mittels einer Telefon- und Onlinebefragung. Die ungewichtete Stichprobe umfasst 7.980 zufällig ausgewählte Personen (Telefonsample: N=3.999; Onlinesample: N=3.981) im Alter von 18 bis 65 Jahren. Ergebnisse: Im Laufe des zurückliegenden Jahres hatten 39,2% aller Befragten mindestens einmal an einem Glücksspiel teilgenommen. Lotto spielte genau ein Drittel der Gesamtstichprobe. Es folgen Rubbellose (11,6%), Glücksspirale (6,4%), Klassenlotterie und Sportwetten (jeweils 4,5%), Glücksspiel- und Geldautomaten (3,4%) und Casinospiele (2,7%). Bezogen auf die gesamte Stichprobe sind 0,64% von einem problematischen und 0,56% von einem pathologischen Spielverhalten betroffen. Besonders hohe Anteile pathologischer Spieler weisen die Gruppen der Automatenspieler (8,7%), Pferdewetter (6,7%) und Casinospieler (5,2%) auf. Des Weiteren sind insbesondere Befragte mit multipler Glücksspielteilnahme, männliche und junge Glücksspieler sowie Personen, deren Angehörige selbst ein Spielproblem aufweisen, überdurchschnittlich häufig von einem pathologischen Glücksspielverhalten betroffen. Schlussfolgerungen: Prävention- und Hilfemaßnahmen im Glücksspielbereich sollten sich insbesondere an die oben genannten Risikogruppen richten. Der Zugang zu Glücksspielen mit hohem Suchtpotenzial, insbesondere den Geld- und Glücksspielautomaten, sollte erschwert werden.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · German national representative survey measuring sports betting participation (4.5%) and problem/pathological gambling by activity group.

**Решение:** =

---

### 1405 · R7726

**An Analysis of Sports Lottery Buyers of Shanxi Province**

2008 · Journal of North University of China · review, article · en

This paper carries out a questionnaire survey in selected cities and counties of Shanxi,researches about the constitution of sports lottery buyers and their lottery-buying thoughts and behavior,compares with some results from other related surveys,analyses the present sports lottery buyers market of Shanxi,and puts forth some countermeasures and suggestions.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Questionnaire survey of Shanxi sports lottery buyers on buyer makeup and behaviour; market-focused, problem-gambling instrument not mentioned.

**Решение:** =

---

### 1406 · R7728

**Gambling Behavior Among College Student-Athletes**

2008 · Journal of Applied Sport Psychology · article · en · https://doi.org/10.1080/10413200802056685

Analyzing data from a representative sample of 20,739 U.S. college student-athletes, this study sought to determine whether certain student-athletes were more prone to frequent or problem gambling behavior. Relative to other studies of college students, a lower percentage of National Collegiate Athletic Association (NCAA) student-athletes reported gambling (males 62.4%, females 43%) and having gambling problems (males 4.3%, females 0.4%), but a high prevalence of weekly gambling was reported (males 13.0%, females 3.3%). Male student-athletes in high profile sports (e.g., baseball, football) were more likely to report a gambling-related problem compared to their counterparts in other sports (e.g., track & field, volleyball). Sports wagering remains a cause for concern. Only a very small number of student athletes reported major infractions such as attempting to alter the outcome of a game or sharing inside information. Future research should investigate why certain student-athletes are more prone to develop gambling problems.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · NCAA student-athlete survey that measured gambling problems and sports wagering; it may report problem-gambling rates among sports bettors.

**Решение:** =

---

### 1407 · R7737

**Sociodemographic Correlates of Internet Gambling: Findings from the 2007 British Gambling Prevalence Survey**

2008 · CyberPsychology & Behavior · journalarticle, review, article · en · https://doi.org/10.1089/cpb.2008.0196

This study provides the first analysis ever made of a representative national sample of Internet gamblers. Using participant data from the 2007 British Gambling Prevalence Survey (n = 9,003 adults aged 16 years and over), all participants who had gambled online, bet online, and/or used a betting exchange in the last 12 months (n = 476) were compared with all other gamblers who had not gambled via the Internet. Overall, results showed a number of significant sociodemographic differences between Internet gamblers and non-Internet gamblers. When compared to non-Internet gamblers, Internet gamblers were more likely to be male, relatively young adults, single, well educated, and in professional/managerial employment. Further analysis of DSM-IV scores showed that the problem gambling prevalence rate was significantly higher among Internet gamblers than among non-Internet gamblers. Results suggest that the medium of the Internet may be more likely to contribute to problem gambling than gambling in offline environments.

**ИИ:** + · обе модели · опрос населения об азартных играх · Analysis of the BGPS 2007 national prevalence survey using DSM-IV, covering online betting and betting exchanges; activity-level data likely.

**Решение:** =

---

### 1408 · R7738

**The Status of Sports Lottery Consumption Market and Countermeasures in the Southwest**

2008 · Journal of Xichang College · review, article · en

Based on the input(incentive),internal,external and output(response) factors,this paper explores the formation and changes of sports lottery ticket consumers in the southwestern region by applying the methods of questionnaire and literature review.This paper also analyzes the consumers’ characteristics and current market situation.Several countermeasures and suggestions are proposed to solve the existing problems.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Questionnaire survey of sports lottery consumers focused on the market; the abstract doesn't say whether a problem-gambling instrument was used.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Questionnaire study of sports lottery consumer market and marketing countermeasures; no sign of any problem-gambling instrument.)

**Решение:** ?

---

### 1409 · R7743

**Investigation on consumption behavior of sports lottery player in Qiqihar**

2008 · Journal of Science of Teachers' College and University · article · en

Through using the method of questionnaier investigation and mathematical statiscs,made investigation on consumption behavioe of sports lottery player in Qiqihar.The result show that the major group of consumer is the person aged at 20～40,middli and high education background,salary below average.Lottery player's consuming mind is comparatively mature.Sports lottery in Qiqihar has a better market.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Questionnaire survey of sports lottery players on consumption behaviour; the abstract doesn't say whether a problem-gambling instrument was used, but one seems unlikely.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Questionnaire on sports lottery buyers' demographics and consumption behavior in Qiqihar; no problem-gambling instrument is mentioned or likely.)

**Решение:** -

---

### 1410 · R7754

**The Hazards and Governance of Online Football Gambling in China**

2008

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: No abstract; the title points to a policy/governance discussion of online football gambling, with no sign of a survey or problem-gambling measure.); Sonnet ? (нет аннотации: No abstract; title suggests a policy/governance paper on online football gambling in China, but it might include survey data with problem-gambling measures.)

**Решение:** ?

---

### 1411 · R7756

**Article: Media Interactivity and Fantasy Sport**

2008

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; fantasy sport media-interactivity study, probably communication research, but can't confirm absence of a problem-gambling measure.

**Решение:** =

---

### 1412 · R7760

**Behavior modification: How fantasy sports impacts fan behavior**

2008

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; fantasy sports fan-behaviour study, a problem-gambling measure is unlikely but can't be ruled out from the title.

**Решение:** =

---

### 1413 · R7763

**Influence of Fantasy Sport on Consumption Behavior**

2008

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: With no abstract, the title points to a 2008 sport-marketing study of fantasy sport and sport consumption, likely with no problem-gambling measure.); Sonnet ? (нет аннотации: No abstract; fantasy sport consumption study likely marketing-focused, but could include a survey with problem gambling measure; full text check warranted.)

**Решение:** ?

---

### 1414 · R7768

**Factors Influencing Intention to Gamble Online**

2008 · Journal of the Association for Information Systems · journalarticle, review, article · en

The objective of this research was to validate a model on online gambling intention. Given that there are many forms of online gambling, this research focused on sports betting. We adopted the Technology Acceptance Model (TAM) as our research model. Additionally, we included subjective norm as an antecedent to online gambling intention. We tested the model using data collected from a questionnaire survey. We collected 212 returns from students in a Chinese tertiary institution. The results provide support for the six hypotheses proposed in our research. We discussed the implications of the results for industry practitioners and gambling counselors.

**ИИ:** разошлись — Opus -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Technology Acceptance Model survey of students' intention to bet on sports online; measures intention and its antecedents, no problem-gambling instrument.); Sonnet ? (неясно, измеряли ли проблемную игру: Questionnaire survey of 212 Chinese students on sports betting intention using TAM; abstract doesn't say whether problem gambling was measured, likely not.)

**Решение:** ?

---

### 1415 · R7784

**Gambling with their lives : college students and sports gambling**

2008 · Medical Entomology and Zoology · book · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; book or thesis on college students' sports gambling might include survey data with a problem-gambling measure.

**Решение:** =

---

### 1416 · R7791

**A national study of neighbourhood access to gambling opportunities and individual gambling behaviour.**

2008 · Journal of epidemiology and community health · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1136/jech.2007.068114

OBJECTIVE: To investigate associations between neighbourhood accessibility to gambling outlets (non-casino gaming machine locations, sports betting venues and casinos) and individual gambling behaviour in New Zealand. DESIGN: A Geographical Information Systems (GIS) measure of neighbourhood access to gambling venues. Two-level logistic regression models were fitted to examine the effects of neighbourhood access on individual gambling behaviour after controlling for potential individual- and neighbourhood-level confounding factors. SETTING: 38,350 neighbourhoods across New Zealand. PARTICIPANTS: 12,529 respondents of the 2002/03 New Zealand Health Survey. RESULTS: Compared with those living in the quartile of neighbourhoods with the furthest access to a gambling venue, residents living in the quartile of neighbourhoods with the closest access were more likely (adjusted for age, sex, socio-economic status at the individual-level and deprivation, urban/rural status at the neighbourhood-level) to be a gambler (OR 1.60, 95% CI 1.20 to 2.15) or problem gambler (OR 2.70, 95% CI 1.03 to 7.05). When examined independently, neighbourhood access to venues with non-casino gaming machines (gambling: OR 1.67, 95% CI 1.28 to 2.18; problem gambling: OR 2.71, 95% CI 1.45 to 5.07) and sports betting venues (gambling: OR 1.67, 95% CI 1.28 to 2.18; problem gambling: OR 2.71, 95% CI 1.45 to 5.07) were similarly related. CONCLUSIONS: Neighbourhood access to opportunities for gambling is related to gambling and problem gambling behaviour, and contributes substantially to neighbourhood inequalities in gambling over and above-individual level characteristics.

**ИИ:** разошлись — Opus ? (неясно, есть ли ставки на спорт: National health survey measuring gambling and problem gambling; unclear whether participation in individual activities, including sports betting, was recorded.); Sonnet + (опрос населения об азартных играх: NZ Health Survey population study measuring gambling and problem gambling; sports betting venue access examined, activity-level tables possible in full text.)

**Решение:** ?

---

### 1417 · R7805

**The Reality of Fantasy Sports: Transforming Fan Culture in the Digital Age**

2008 · PubMed · other literature type, text/, preprint · en · https://doi.org/10.21985/n2bb2t

~ 0.9). Additionally, the model was able to predict a highly synergistic combination of Trametinib (MEK inhibitor) and Omipalisib (PI3K inhibitor) for TNBC treatment, which incidentally was recently in phase I clinical trials for TNBC. Our choice of tree-based models over networks for greater interpretability also allowed us to further interrogate which specific kinases were highly predictive of cell sensitivity in each cancer type, and we saw confirmatory strong predictive power in the inhibition of MAPK, CDK, and STK kinases. Overall, these results suggest that kinome inhibition states of kinase inhibitor combinations are strongly predictive of cell line responses and have great potential for integration into computational drug screening pipelines. This approach may facilitate the identification of effective kinase inhibitor combinations and accelerate the development of novel cancer therapies, ultimately improving patient outcomes.

**ИИ:** ? · обе модели · нет аннотации · Abstract belongs to an unrelated cancer study; title on fantasy sports fan culture probably isn't a PG survey, but this can't be confirmed.

**Решение:** =

---

### 1418 · R7812

**Gl ü cksspielteilnahme und Gl ü cksspielprobleme in Deutschland: Ergebnisse einer bundesweiten Repr ä sentativbefragung Gambling and Gambling Problems in Germany: Results of a National Survey**

2008 · review

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** + · обе модели · опрос населения об азартных играх · German national representative survey of gambling participation and gambling problems, likely with activity-level data; it is tagged as a review but the title shows a survey.

**Решение:** =

---

### 1419 · R7839

**Research on Behavior and Structure of Sichuan Sports Lottery Consumers**

2008 · Luoyang Shifan Xueyuan xuebao · article · en

The statistic analysis on consumer behavior and structure concludes that the sports lottery consumers are mainly constituted by young or middle aged males,largely involving those of low income and lack of educational background,or those with blindness in consumption.The author further puts forth suggestion regarding enhanced publicity,reformed operational approaches and regulating market order.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of Sichuan sports lottery consumers focused on demographics and marketing; no problem-gambling instrument mentioned, and the lottery games covered are not specified.

**Решение:** =

---

### 1420 · R7845

**스포츠토토 구매특성에 따른 구매만족과 태도비교 및 재구매 의사에 미치는 영향**

2008 · article · ko

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Sports Toto buyer survey on satisfaction, attitude and repurchase intention; consumer-marketing focus, no problem-gambling instrument indicated.); Sonnet ? (нет аннотации: Korean Sports Toto purchaser survey on satisfaction, attitude and repurchase intention; no abstract, and a problem-gambling measure is unlikely but can't be ruled out.)

**Решение:** ?

---

### 1421 · R7846

**갬블링 열정 척도(GPS)를 통한 스포츠토토 구매자의 시장세분화 연구**

2008 · 한국호텔외식경영학회 학술발표논문집 · article · ko

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Survey of Sports Toto buyers segmented with the Gambling Passion Scale; no abstract, so unclear whether a problem-gambling instrument was also used.

**Решение:** =

---

### 1422 · R7847

**스포츠토토 참여와 스포츠관람행동의 관계에 관한 연구**

2008 · Seoul National University Open Repository (Seoul National University) · dissertation · ko

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Korean thesis on Sports Toto (sports betting) participation and spectating behaviour; no abstract, so unclear whether problem gambling was measured.

**Решение:** =

---

### 1423 · R7858

**FOR TENNIS ( BETTING ) ?**

2007

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Title fragment about tennis betting with no abstract; probably a markets/prediction paper, but the study type can't be confirmed.

**Решение:** =

---

### 1424 · R7859

**Gambling and alcohol use: trends in the state of New Mexico from 1996-1998.**

2007 · Journal of gambling studies · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1007/s10899-006-9051-3

Alcohol consumption and its relationship to gambling was examined in a statewide New Mexico survey in 1996 and 1998. Data regarding both drinking habits and gambling behavior were obtained from a stratified random sample of the adult population (N = 2674) across the entire State of New Mexico via phone survey. These surveys were carried out shortly after a period when New Mexico experienced an initial surge in the legalized gaming industry. Fifty-seven percent of survey respondents reported drinking in the past month, while 43.1% reported no drinking in the past 30 days. Results show that while the number of days in the past 30 that a person drinks is significantly correlated with some types of gambling behavior (e.g., in 1998, drinking more days was associated with more card gambling and sports gambling), it is the amount of alcohol consumed per occasion that is associated with more gambling behavior. For example, in both 1996 and 1998, drinking more per occasion was associated with more sports betting, dice gambling, number/lottery gambling, gambling using machines, and paper game gambling (e.g., pull tabs, punchboard). These results suggest that problem gambling behavior is not affected as much by the number of occasions on which one consumes alcohol, as by the amount of alcohol consumed per occasion.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Statewide adult survey measured sports betting; abstract mentions problem gambling but names no screening instrument.); Sonnet + (опрос населения об азартных играх: Statewide New Mexico phone survey of gambling by type including sports betting and alcohol; likely measured problem gambling, so activity-level figures may be reported.)

**Решение:** ?

---

### 1425 · R7862

**Pathologisches Glücksspiel in Deutschland: Spiel- und Bevölkerungsrisiken**

2007 · SUCHT - Zeitschrift für Wissenschaft und Praxis / Journal of Addiction Research and Practice · review, article · de · https://doi.org/10.1024/2007.05.06

Ziele: Abschätzung der »Bevölkerungsattraktivität« von Glücksspielen sowie der Prävalenz des Pathologischen Glücksspiels (PG) in Form von »Glücksspiel- und Bevölkerungsrisiken« Methodik: Die Stichprobe betrug 7.817 Respondenten zwischen 18 und 64 Jahren aus dem Epidemiologischen Suchtsurvey 2006. Lebenszeit- und 12-Monats-Prävalenz, präferiertes Glücksspiel und PG Diagnosen (DSM-IVTR) wurden mittels Fragebögen und telefonischen Interviews erfasst. Ergebnisse: 71,5 % der Deutschen haben schon einmal gespielt, 49,4 % innerhalb der letzten 12 Monate. Bei der »Bevölkerungsattraktivität« stehen die Spiele der Lottogruppe im Vordergrund (60,3 %), mit Abstand folgen Lotterien, Sportwetten, Casinospiele, Geldspielautomaten und illegales Glücksspiel. Das höchste »Glücksspielrisiko« zeigen Internetkartenspiele (7,0 %) und das kleine Spiel im Casino (6,7 %), die geringste Gefährdung besteht durch Lotto/Toto/Keno (0,1 %). Das »Bevölkerungsrisiko« für PG liegt bei knapp 0,2 % (etwa 103.000 Personen), mit etwa gleich großen Anteilen für Sportwetten, Casinospiele und Geldspielautomaten (0,05–0,06 %; 24.000–31.000) sowie mit Abstand für Lottospiele (0,02 %; 12.000). Unter Berücksichtigung der Differenzialdiagnose Manische Episode halbiert sich das Bevölkerungsrisiko (0,09 %; etwa 46.000). Schlussfolgerungen: Die Prävalenz für PG in Deutschland liegt für die erwachsene Bevölkerung im unteren Bereich europäischer Untersuchungen. Für präventive Maßnahmen sind die Unterschiede zwischen in »Glücksspielrisiko« und »Bevölkerungsrisiko« zu beachten.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · German population survey (n=7,817) using DSM-IV PG diagnoses; reports PG risk by game, including sports betting.

**Решение:** =

---

### 1426 · R7877

**British Gambling Prevalence Survey 2007**

2007 · Nottingham Trent University's Institutional Repository (Nottingham Trent Repository) · book · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** + · обе модели · опрос населения об азартных играх · National gambling prevalence survey (BGPS 2007) using DSM-IV and PGSI, with problem gambling broken down by activity, including sports betting.

**Решение:** =

---

### 1427 · R7883

**A national study on gambling among US college student-athletes.**

2007 · Journal of American college health : J of ACH · article, comparative study, journal article · eng · https://doi.org/10.3200/jach.56.2.93-100

OBJECTIVE: The authors examined the national prevalence of gambling problems and sports wagering among US college student-athletes. PARTICIPANTS: A national sample of 20,739 student-athletes participated in the study. METHODS: The authors used data from the first national survey of gambling among college athletes, conducted by the National Collegiate Athletic Association. RESULTS: Men (62.4%) consistently had higher past-year prevalence of gambling than did women (42.8%). The authors identified 4.3% of men and 0.4% of women as problem or pathological gamblers. Among the most popular forms of gambling were playing cards, lotteries, and games of skill, with male-to-female prevalence ratio ranging 1.3-5.6 across various gambling activities. Athletes in golf and lacrosse were more likely to report sports wagering than were other athletes. Athletes in gender-specific sports wagered more prevalently than did athletes in unisex sports. CONCLUSION: Gambling prevalence may be underestimated in this population because respondents' athletics eligibility is at stake. This study provides important baseline data for future cohorts of athletes.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · National survey of student-athletes measured sports wagering and problem/pathological gambling; may report PG among sports bettors.

**Решение:** =

---

### 1428 · R7890

**Aktive Spielsuchtprävention bei Lotterien und Sportwetten in Hamburg**

2007 · Prävention und Gesundheitsförderung · article · de · https://doi.org/10.1007/s11553-007-0078-9

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; likely describes a prevention programme for lotteries and sports betting, but it may contain survey data on bettors.

**Решение:** =

---

### 1429 · R7903

**Sports betting and other gambling in athletes, fans, and other college students.**

2007 · Research quarterly for exercise and sport · article, journal article, research support, n.i.h., extramural · eng · https://doi.org/10.1080/02701367.2007.10599425

Gambling on college and professional sports and the influence of attending colleges with differing levels of "sports interest" were examined among athletes, sports fans, and other students (N = 10,559) at 119 colleges in the United States using multilevel statistical analysis. Athletes and fans reported more sports gambling compared to other students, with no differences between athletes and fans. Male students were more likely to gamble than female students, but gender did not moderate the relationship between athletic participation and sports gambling. Students attending schools with a greater "sports interest" were more likely to gamble on college sports after adjusting for individual characteristics. Athletes, sports fans, and students attending schools with high "sports interest" are appropriate targets for prevention efforts.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Large college survey measuring sports gambling; abstract doesn't say whether a problem-gambling instrument was used.

**Решение:** =

---

### 1430 · R7916

**Investigation on Current Situation of Sports Lottery Consumer in Guangdong Province**

2007 · Journal of Physical Education Institute of Shanxi Normal University · article · en

Through using the method of questionnaire investigation and mathematical statistics,This paper made in on sports lottery market,comsuming behavior and the comsuming mind in Guangdong Provice.The result that the biggest group of consumer was the person aged at 18-45.middle and high school education background,salary average;The most of consumers have the better knowledges and motivations,their consuming mind is comperatively mature,and the mien is right.The advantageous and disadvantageous factors that influnence on theirs consuming behaviors.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Questionnaire survey of sports lottery consumers on behaviour and motivation; abstract doesn't say whether a problem-gambling instrument was used, though one seems unlikely.

**Решение:** =

---

### 1431 · R7920

**Gambling as an emerging health problem on campus.**

2007 · Journal of American college health : J of ACH · journal article, journalarticle, article · eng · https://doi.org/10.3200/jach.56.1.75-88

OBJECTIVE: The authors documented the prevalence of gambling and correlates to health among undergraduates. METHODS: The authors analyzed data from a health-habit questionnaire (gambling questions included) given to students enrolled in a university-required course. RESULTS: Gambling and problems with gambling were more frequent among men than women regardless of venue. Athletes more frequently bet on sports and played games of chance, had gambling debt, and sought help for gambling than did nonathletes. More than 50% of fraternity members gambled and had a higher prevalence of gambling debt than did other men. Several gambling practices were correlated with failure to use seatbelts, driving or riding with someone under the influence, and using drugs (including cigarettes). Twice as many students who had gambling problems reported considering or attempting suicide than did those who did not report gambling problems, and gambling was correlated with depression. CONCLUSION: These results indicate that gambling is correlated with high-risk health behaviors and indicates the need for intervention for college students with gambling problems.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Student survey measured sports betting and gambling problems, but it is unclear whether a validated problem-gambling instrument was used.

**Решение:** =

---

### 1432 · R7924

**Adolescent Gambling Behaviour, Attitudes, and Gambling Problems**

2007 · International Journal of Mental Health and Addiction · article · en · https://doi.org/10.1007/s11469-007-9117-1

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the title suggests an adolescent gambling survey that may have measured problem gambling and sports betting.

**Решение:** =

---

### 1433 · R7928

**Gambling behavior of student-athletes and a student cohort: what are the odds?**

2007 · Journal of gambling studies · article, comparative study, journal article · eng · https://doi.org/10.1007/s10899-006-9043-3

This study investigated the prevalence of gambling, gambling related NCAA violations, and disordered gambling in student-athletes (n = 736) with a comparison cohort of students (n = 1,071) at four universities. Student-athletes reported similar rates of gambling frequency, use of a bookmaker, and disordered gambling as students. After accounting for demographic differences, student-athletes were less likely to engage in sports wagering than students. Several risk factors for disordered gambling were identified, including being male and reporting at least one parent with a history of gambling problems. These findings suggest that problems associated with gambling are a university-wide issue with student-athletes meriting additional attention because of implications for the integrity of intercollegiate sports. Improved prevention and intervention efforts for collegiate gambling are recommended.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Survey of student-athletes and students that measured both sports wagering and disordered gambling, so problem gambling among sports bettors may be reportable.

**Решение:** =

---

### 1434 · R7931

**6. HISTORY**

2007 · https://doi.org/10.1080/10948000709336519

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: Generic chapter title 'History' with no abstract; nothing points to gambling or empirical problem-gambling data among sports bettors.); Sonnet ? (нет аннотации: Title "6. HISTORY" (2007) has no abstract or venue; likely a book chapter section, and nothing shows it is a gambling study.)

**Решение:** -

---

### 1435 · R7943

**National Collegiate Athletic Association and the Issue of Sports Wagering**

2006 · New Game Plan for College Sport · other · en · https://doi.org/10.5040/9798216192565.0014

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Book chapter on NCAA and sports wagering, no abstract; likely policy-focused but may report NCAA athlete survey data on problem gambling.

**Решение:** =

---

### 1436 · R7984

**Fantasy Sports: History, Game Types, and Research**

2006 · article · en · https://doi.org/10.4324/9780203873670.ch23

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -1 (обзор, комментарий, теоретическая, правовая или регуляторная работа: The title points to a descriptive overview of fantasy sports history, game types and research, not a survey measuring problem gambling.); Sonnet ? (нет аннотации: No abstract; 2006 fantasy sports overview, likely a review/history, but may include research on players; unclear whether problem gambling was measured.)

**Решение:** ?

---

### 1437 · R7986

**Gambling on campus**

2006

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the title could be a student gambling survey covering sports betting and problem gambling, or could be commentary.

**Решение:** =

---

### 1438 · R7989

**Trauma history and severity of gambling involvement among horse-race gamblers in a South African gambling setting.**

2006 · Psychological reports · article, journal article, journalarticle · eng · https://doi.org/10.2466/pr0.99.2.472-476

The purpose of this study was to ascertain the frequency of gambling involvement and the prevalence of problem gambling among horse race gamblers and to discover whether problem gambling in this sample is associated with a history of trauma. Among a sample of 266 South African horse-race gamblers (94% men and 6% women, M age 46.8 yr., SD = 13.9, range 18–85 years), 31.2% were classified as probable pathological gamblers and 19.9% with problem gambling. Major weekly gambling activities included racetrack betting (82%), purchase of lottery tickets or scratch tickets (35%), purchase of sports lottery tickets (23%), and using casino type games (18%). Trauma history was significantly associated with gambling severity.

**ИИ:** ? · обе модели · другое · Horse-race gamblers with PG measured; 23% bought sports lottery tickets weekly. PG among sports lottery players may be reportable.

**Решение:** =

---

### 1439 · R8001

**Sports Betting as a Social Phenomenon in Macedonia**

2006 · article · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the title is about sports betting in Macedonia, and it could be a survey of bettors that measured problem gambling.

**Решение:** =

---

### 1440 · R8005

**THE IMPACT OF GAMBLING PROXIMITY ON GAMBLING ATTITUDES, SUBJECTIVE NORMS, GAMBLING INTENTIONS, AND GAMBLING BEHAVIOR OF COLLEGE ATHLETES**

2006 · Journal of contemporary athletics · review, article · en

INTRODUCTIONBecause of their desire for competition, college student athletes may be highly susceptible to the excitement of gambling. In fact, Cullen and Latessa (1996) found 25% of Division I football and basketball players indicated they had bet on college sports and Cross and Vollano (1999) found over 45% gambled on sports while attending college. Although the National Collegiate Athletic Association (NCAA) has rules strictly prohibiting athletes from participating in gambling, cases of reported gambling by athletes continues to increase.More opportunities to gamble may exasperate this problem (Kassinove, 1998). In fact, research suggests a positive link between proximity of gambling opportunities and problem gambling (Eadington, 1989; Lesieur, 1992; National Gambling Impact Study, 1999; Shaffer and Hall, 1997; Whyte, 1997). Moreover, Volberg (1994) and others (Gerstein, Volberg, Toce, and Howard, 1999: Shaffer, LaBrie, and LaPlante, 2004) have found that proximity or accessibility (Gilliland, 2003; Marshall, 2004) of gambling activities is linked to higher rates of pathological gambling. Therefore, it is very important to determine if proximity to a gambling venue affects college student athletes. Understanding the potential link between proximity and gambling among athletes is key for colleges and universities across the United States.REVIEW OF THE LITERATUREDefinition of GamblingGambling, especially problem or pathological gambling, is of major concern in the United States. Pathological gambling was formally recognized as a mental disorder in 1980 (American Psychiatric Association, 1980). In 1994, the American Psychiatric Association published a new set of criteria for evaluating excessive gambling habits in its Diagnostic Statistical Manual IV (DSM-IV). A person was diagnosed as a compulsive gambler with five yes responses to 10 items, which together indicate a persistent and recurrent maladaptive behavior. The DSM-IV also classifies gamblers as:1. Recreational gamblers or those who can gamble merely for recreational purposes and do not develop problem gambling habits,2. At-Risk gamblers or those who gamble more than once a week and use the means of gambling as a money making opportunity, and3. Pathological gamblers or those who gamble continuously with hopes of hitting the big one. They risk personal relationships, employment opportunities, and other life conditions in order to gamble.College Student Athletes and GamblingWhile student athletes are not the only students involved in gambling on college campuses, and not all are pathological or even at-risk gamblers, more attention is given when they get caught. This can have a negative impact on the players, the athletic department, and the image of the university. Over the years, there have been highly publicized incidents involving athletes at major universities, including the University of Maryland, Boston College, Northwestern University, and Arizona State University. The issue of gambling, and especially sports wagering, has been of significant importance to the NCAA membership for the entire existence of the Association (NCAA, 2004). Even an isolated incident can undermine the integrity of a sport. Thus, there remains a strong commitment by NCAA institutions to educate those associated with college sports about the dangers of gambling (NCAA, 2004). The NCAA has a no tolerance policy, whereby the athlete is removed from competition as a result of gambling involvement.In addition, to the negative impact on the athlete, the concern about gambling by college athletes also stems from the substantial economic investment of colleges and universities and associated businesses in intercollegiate athletics (Cross, Basten, Hendrick, Kristofic, and Schaffer, 1998) and the potential of a negative impact. The integrity of college sports and the continuation of the associated economic rewards depend on the assurance the games are being played straight (Cross et al. …

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Empirical survey of college athletes' gambling and sports wagering; abstract truncated, unclear whether a problem-gambling screen (e.g., DSM-IV) was administered.

**Решение:** =

---

### 1441 · R8011

**The Comparative Study on the Loyal Consumers and Ordinary Consumers in Sport Lottery**

2006 · Journal of Tianjin University Science and Technology · article · en

Used the random sampling,134 loyal consumers and 87 ordinary consumers in sport lottery were investigated.The results showed that there was a difference between these consumers in the characteristics of constitute,consume mental and consume behavior.Comparing with ordinary consumers,in the group of loyal consumers,there are fewer women,middle aged is more,has higher income,the motives to get big prize is stronger than ordinary consumers.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Survey of sports lottery consumers comparing demographics and motives; no problem-gambling instrument mentioned, though consumption behaviour may include one.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Survey of sport lottery consumers on demographics, motives and behavior; no problem-gambling instrument is mentioned.)

**Решение:** -

---

### 1442 · R8014

**Sports Gambling Participation Inclination and Relation of Feeling of Satisfaction**

2006 · Journal of Sport and Leisure Studies · article, journal-article · en · https://doi.org/10.51979/kssls.2006.08.27.461

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; a survey of sports gambling participants is plausible, and problem gambling measurement is unknown.

**Решение:** =

---

### 1443 · R8028

**Poker på Internet - en studie om studenters konsumtion av Internetbaserade pokertjänster**

2005 · article · sv

En mangd nya Internetbaserade spelbolag har under den senaste tiden vaxt fram, primart inriktade pa vadslagning men ocksa pa pokerspel. Svenskarna har sedan lange fascinerats av spel och Internets ...

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Swedish student study of online poker; the abstract is cut off and does not say whether sports betting or a problem-gambling screen was measured.

**Решение:** =

---

### 1444 · R8048

**Investigation on Consumption Behavior of Sports Lottery Consumer in Zhejiang Province**

2005

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Survey of sports lottery consumers; no abstract, so it's unclear whether a problem-gambling instrument was used.

**Решение:** =

---

### 1445 · R8064

**Gambling by Underage College Students: Preferences and Pathology**

2005 · College student journal · review, article · en

University students (N=995) residing in an environment which affords many opportunities to gamble were surveyed. For those participants over 21 years of age, 92.5% said they had gambled at least once in a casino, compared to 59.8% of the 18 year olds, 72.8% of the 19 year olds, and 86.1% of the 20 year olds. Casino gambling is legal only at 21. Preferences in favorite game showed no difference between the two groups except that those under 21 years were more than twice as likely to prefer sports betting to those over 21. The percentage of participants classified as probable pathological gamblers by the South Oaks Gambling Screen was 9.21% for those under 21 years, and 14.91% for those over 21 ********** The gaming industry shares a problem with the makers of alcoholic beverages: how to market a product to a broad set of consumers some of whom are excluded by legal statute from partaking. Just as there are underage drinkers of alcohol, there are the underage who frequent casinos and create a regulatory problem for the industry, and occasionally personal problems for themselves. The legal age for casino wagering in the United States is 21 years for all states, though some states may permit other forms of gambling at lower ages. Thus, the problem of gambling by underage persons is recognized as a matter of social concern for both the industry and for the individual. College students provide a convenient population to assess the extent of gambling by underage persons, especially when the population is centered in an environment prolific with casinos. We are acutely aware of the problem because the gambling milieu of Las Vegas offers an enormous temptation to students of the University of Nevada, Las Vegas. Gambling machines are accessible within a 100 yards of the campus, and the famed Las Vegas Strip is only a mile away. Most UNLV students come from the greater Las Vegas valley and have thus grown up in a city unmatched in opportunities for gaming. In previous studies we have examined pathological gambling (Oster & Knapp, 2001) and sports betting (Oster & Knapp, 1998; Knapp, Rasmussen, & Niaghi, 2003) by college students. Here our particular interest is in the gambling patterns of college students who are under 21 years of age, and how they compare to their over 21 years cohort. The best data to date on gambling by college students is contained in a meta-analytic review of studies which surveyed college students in both the United States and Canada (Shaffer, Hall, & Bilt (1997). The authors reported a lifetime prevalence of Level 3 gamblers, those with clinically meaningful problems of disordered for college students of 4.67% (p. iii). Against this broad background of gambling by college students is the narrower question of wagering by those who are not yet 21 years old. The survey studies available on this issue are limited (see Knapp & Crossman for a review). However, they constitute a body of literature which continues to grow as do regulations and enforcement efforts to keep away from the tables and machines of the gaming industry those under the legal age to gamble (Stitt, Giacopassi, & Vandiver, 2000). Based on samples from the University of Nevada, Las Vegas our previous studies have found that well over half of students under 21 years claim to have gambled in a casino with nearly a quarter claiming to do so weekly (Oster & Knapp, 2001). The present study assessed the frequency of gambling, game preferences. and degree of pathology reported by college students who were not yet of legal age to wager. Method Participants Students who voluntarily participated in this study were recruited from psychology classes at the University of Nevada. Las Vegas. The convenience sample of students (N = 995) was 53.8% female and 46.2% male. Their mean age was 21.05 years with a range from 17 to 73. The majority of the students (67. …

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Student survey with SOGS that measured game preferences, including sports betting, so it may report problem gambling among sports bettors.

**Решение:** =

---

### 1446 · R8069

**Wetten, fiebern, Kontrolle verlieren? – Jugendliche und kommerzielle Sportwetten**

2005 · SUCHT - Zeitschrift für Wissenschaft und Praxis / Journal of Addiction Research and Practice · article · de · https://doi.org/10.1024/2005.02.02

Ziel: Der vorliegende Beitrags ist eine vertiefte Auseinandersetzung mit der kommerziellen Oddset-Sportwette, die sich im Rahmen einer repräsentativen Untersuchung zum Glücksspielen von Kindern und Jugendlichen in Nordrhein-Westfalen als jugendrelevante Spielvariante herausgestellt hat. Ergebnisse: Dazu werden zunächst ausgewählte Ergebnisse der Pilotstudie zur Häufigkeit und Verteilung des Sportwettens in der untersuchten Bevölkerungsgruppe präsentiert. In einem zweiten Schritt wird der aufkommende Problemdiskurs um die Sportwetten-Teilnahme näher beleuchtet, wobei ein fragwürdiger Rekurs auf Befunde aus anderen Ländern, wie er im Rahmen eines neueren, umstrittenen Artikels praktiziert wird, im Zentrum der kritischen Analyse steht. Schlussfolgerungen: Die Schlussbetrachtung benennt wesentliche Aspekte, die es in Folgeuntersuchungen zum Thema verstärkt zu berücksichtigen gilt.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Representative adolescent gambling survey in NRW reporting Oddset sports betting; unclear whether a problem-gambling instrument was used.

**Решение:** =

---

### 1447 · R8071

**Sind Sportwetten Glücksspiel? Eine wissenschaftliche Untersuchung am Beispiel der Wettlandschaft in NRW im Auftrag des Interessenverbandes europäischer Buchmacher e.V. Duisburg.**

2005 · PUB – Publications at Bielefeld University (Bielefeld University) · book · de

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; industry-commissioned report on whether sports betting is gambling in NRW. It may be a legal or skill analysis, or may survey bettors.

**Решение:** =

---

### 1448 · R8073

**Hazards and causes and countermeasures against underground soccer gambling in Guangdong**

2005 · journal of physical education · article · en

The authors studies the phenomenon of underground soccer gambling in Shenzhen,Guangzhou,Zhuhai,Zhanjiang,Dongguan,Foshan,Shaoguan,Jiangmen,Shantou,Chaozhou,Meizhou and Zhaoqing,and analyzed its genesis,current situation and hazards, as well as the causes of its rampancy, so as to provide some countermeasures for relevant departments to sweep underground soccer gambling.

**ИИ:** разошлись — Opus -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: Descriptive policy analysis of underground soccer gambling in Guangdong (causes, hazards, countermeasures); no survey or problem-gambling instrument is mentioned.); Sonnet ? (неясно, измеряли ли проблемную игру: Study of underground soccer gambling in Guangdong; may be a survey, but abstract gives no method or problem-gambling measure, so full text check is warranted.)

**Решение:** -

---

### 1449 · R8078

**On the Reputation and Safety of Sports Lottery**

2005

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the title points to an essay on sports lottery reputation and safety, but empirical player data can't be ruled out.

**Решение:** =

---

### 1450 · R8097

**Internet och dobbel**

2004 · article · sv

Spelande och vadslagning har forekommit sedan tidernas begynnelse. Allt vartefter nya kommunikationsmedium uppfunnits och fatt spridning sa har spelandets natur andrats. Tillgangligheten till spel ...

**ИИ:** ? · обе модели · другое · Swedish 2004 article on internet gambling; the abstract is cut off, so the design and any problem-gambling measure are unclear.

**Решение:** =

---

### 1451 · R8098

**The Psychological Research on Consumers' Economic Behavior in Sports Lottery**

2004

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; psychological study of sports lottery consumers might include a problem-gambling measure.

**Решение:** =

---

### 1452 · R8102

**Sports betting: can gamblers beat randomness?**

2004 · Psychology of addictive behaviors : journal of the Society of Psychologists in Addictive Behaviors · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1037/0893-164x.18.2.143

Although skills are not considered relevant in chance-governed activities, only a few studies have assessed the extent to which sport expert skills in wagering are a manifestation of the illusion of control. This study examined (a) whether expert hockey bettors could make better predictions than chance, (b) whether expert hockey bettors could achieve greater monetary gains than chance, and (c) what kind of strategies hockey gamblers rely on when betting. Accordingly, 30 participants were asked to report their state lottery hockey bets on 6 occasions. We suggest that the information used by bettors, along with near-misses, reinforces their perception of expertise. The results of this experiment suggest that the so-called "skills" of the sports bettors are cognitive distortions.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Small study of hockey sports-lottery bettors. The abstract doesn't mention a problem-gambling screen, though the sample description may report SOGS scores.

**Решение:** =

---

### 1453 · R8112

**Interactive television gambling: a matter for concern?**

2004

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the title suggests a commentary on interactive TV gambling, but an empirical survey can't be ruled out.

**Решение:** =

---

### 1454 · R8132

**Gambling participation and problems among employees at a university health center.**

2004 · Journal of gambling studies · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1023/b:jogs.0000022307.09299.f5

This study evaluated the frequency and intensity of gambling behaviors among employees at an academic health center. Employees were sent an anonymous questionnaire assessing demographic characteristics, participation in gambling activities, and gambling-related problems. Of the 904 respondents, 96% reported gambling in their lifetimes, with 69% gambling in the past year, 40% in the past two months, and 21% in the past week. The most common forms of gambling were lottery and scratch tickets, slot machines, card playing, sports betting, bingo, and track. Only 1.2% of the sample reported gambling on the internet. Using scores on the South Oaks Gambling Screen, 3.0% of the respondents were classified as Level 2 (or problem) gamblers, and an additional 1.8% were Level 3 (or pathological) gamblers. Compared to Level 1 (non-problem) gamblers, Level 2 and Level 3 gamblers were more likely to be male, single, and employed full-time, and to have lower income and education. About half of the Level 2 and Level 3 gamblers reported interest in an evaluation of their gambling behaviors and treatment interventions. These data suggest the need to screen for gambling problems in health care professionals and to provide gambling-specific treatments.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Employee survey measured sports betting participation and SOGS problem gambling; it could report problem gambling among sports bettors.

**Решение:** =

---

### 1455 · R8133

**[Forms of pathological gambling: empirical research on consumers behaviour of sport betting and lottery participants].**

2004 · Wiener medizinische Wochenschrift (1946) · article, english abstract, journal article · ger · https://doi.org/10.1007/s10354-004-0084-x

Gambling is one of the favourite leisure activities. 70-90 % of the grown-up population have gambled at least once in their life. Over the last few years, however, the variety of opportunities to gamble has changed. Decreasing numbers of casino visitors can be seen against an ever-increasing number of people using slot machines, and taking part in national lotteries and sport betting. Comprehensive empirical research regarding consumer behaviour and addiction potential involved in sport betting has been non-existent and only a few studies have dealt with lottery. In the present study, 108 subjects were questioned in Austrian betting offices. 33.3 % of the sample fulfilled the diagnostic criteria for pathological sport betting. Of the sport betting subjects who additionally play lottery, 22.92 % were diagnosed as being pathological lottery gamblers. Based on the criteria of substance addiction, the data demonstrate that sport betting and lottery have addiction potential and can therefore be seen as non-substance-related addiction.

**ИИ:** + · обе модели · беттеры + инструмент · 108 sports bettors surveyed in Austrian betting offices; 33.3% met diagnostic criteria for pathological sport betting.

**Решение:** =

---

### 1456 · R8154

**The Relationship between Involvement Type and Addiction Propensity and Social Adaptation in Sports Gambling**

2004 · Korea Sport Research · article · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; Korean study of sports gamblers' addiction propensity, possibly measured with a problem-gambling screen.

**Решение:** =

---

### 1457 · R8198

**A Comparison Study of the Behavior and Practices of Casino Gamblers as Compared to Those Gamblers of Sport Book Activities**

2003 · Journal of Hospitality & Leisure Marketing · article · en · https://doi.org/10.1300/j150v10n01_12

ABSTRACT This study examines the behavior of gamblers who have a specific area of preferred gambling. Some gamblers prefer casino games such as table games and slots while others prefer sports betting or pari-mutuel wagering. The intention of this study was to identify differences in behaviors, activities, and attitudes of gamblers that indulge in different types of gambling. This information will be important to marketing professionals of the gaming industry in assisting them to develop promotional activities for their perspective target markets.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey comparing sports book and casino gamblers' behaviours from a marketing angle; the abstract doesn't say whether a problem-gambling screen was used.

**Решение:** =

---

### 1458 · R8207

**Mapping Internet Gambling: Emerging Modes of Online Participation in Wagering and Sports Betting**

2003 · International Gambling Studies · article, journalarticle/, review · en · https://doi.org/10.1080/14459790304586

Participation in gambling online has to date been largely regarded under homogenising terms such as 'interactive gambling' or 'e-gambling'. This article explores different modes of participation gambling in the online environment, seeking to begin a process of better understanding some of the factors that construct distinguishable populations of online gamblers and distinct experiences of gambling online. The article commences with a brief overview of the internet, commenting on the apparent suitability of commercial gambling products for the development of successful online business models. Social and institutional factors constraining various modes of online participation in gambling are briefly outlined in relation to online wagering and gaming in Australia. Data drawn from three online surveys are then used to provide an overview of participation in the areas of online wagering and sports betting. These results form the basis of an initial analytical distinction between modes of participation in online betting on racing and sports in Australia.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Online surveys of Australian online race and sports bettors; abstract does not say whether a problem-gambling instrument was used.

**Решение:** =

---

### 1459 · R8223

**Can gamblers beat randomness? : an experimental study on sport betting**

2002 · Corpus Université Laval (Université Laval) · master thesis, dissertation · en · https://hdl.handle.net/20.500.11794/66064

Although skills are not considered relevant in chance governed activities, only few studies have assessed to which extent sport expert skills in wagering are a manifestation of the illusion of control. Thus, the present paper examines: (1) if expert hockey bettors can make better predictions than random selection, (2) if expert hockey bettors can achieve greater monetary gains than what can be expected from chance, and (3) what kind of information and strategies hockey gamblers rely on when betting. Accordingly, 30 participants were asked to report their state lottery hockey bets on 6 occasions. They also filled in a questionnaire on sports wagering. Despite a rate accuracy greater than chance, the monetary gains of expert hockey gamblers are not significantly higher than what can be expected by chance. It is suggested that the information used by bettors, along with near-misses (level of precision), reinforce their perception of expertise and their illusion of control

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Study of 30 hockey sports-lottery bettors with a sports wagering questionnaire; not stated whether a PG screen like SOGS was given.

**Решение:** =

---

### 1460 · R8234

**Analysis and Study of Current Situation of Computer Sports Lottery Buyers in Beijing**

2002

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Survey of Beijing sports lottery buyers; no abstract, so unclear whether match-outcome games or a problem-gambling instrument were involved.

**Решение:** =

---

### 1461 · R8240

**The gambling behavior of college students at a midwestern university**

2002 · Cardinal Scholar (Ball State University) · dissertation · en

The purpose of this study was to determine who was gambling, what were the most common venues used to gamble, and how much money was being gambled on a Division I college campus located in the Midwest. Today, betting takes place on 99.9 percent of the college campuses in the country (Blaudschun, 2000). This would lead one to believe that there would be a high percentage of students gambling at this university. Participants consisted of 217 males and 319 females, ranging in rank from freshman to graduate. Participants were asked to complete a survey consisting of general questions about their gambling history. Four hundred fifty of the 536 participants reported to have gambled at some point in their life. The majority of the participants had purchased lottery tickets and some of the students bet on sports over the Internet. The majority of the participants who had gambled reported that they wagered less than $10.00 per bet on average. Based on these findings, a majority (84%) of the participants had gambled but played relatively low risk activities for small amounts of money. It is suggested that future researchers attempt to examine the attitude of the participants towards gambling.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Student survey measured internet sports betting; abstract mentions only general gambling history questions, so it's unclear whether a PG screen (e.g., SOGS) was used.

**Решение:** =

---

### 1462 · R8255

**Gambling participation in the U.S.--results from a national survey.**

2002 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1023/a:1021019915591

Demographic patterns of gambling participation in the U.S. were examined. A national telephone survey was conducted with 2,630 representative U.S. residents aged 18 or older. The sample as weighted for analysis was 48% male, 12% black, and 11% Hispanic. Respondents were questioned on 15 types of gambling: how often they played and how much they won or lost. Eighty-two percent gambled in the past year. Lottery was the most commonly played game, while casino gambling accounted for the largest extent of gambling involvement. Men and women were equally likely to gamble in the past year, but men gambled more frequently and had larger wins and losses, particularly on sports betting and games of skill. Blacks were less likely to have gambled in the past year, but blacks who gambled did so more heavily than other racial groups. Blacks and Hispanics were more likely than average to be pathological gamblers. The rate of past year gambling declined with age, but extent of gambling involvement among gamblers did not vary with age. Rates of participation in most forms of gambling increased with socioeconomic status, but higher socioeconomic status gamblers had lower rates of pathological gambling, and lower extent of gambling involvement, particularly for lottery. New Englanders gambled more heavily than other Americans. Comparison with past studies showed an increase in overall gambling participation in the U.S., and large increases in rates of participation in lottery and casino gambling.

**ИИ:** + · обе модели · опрос населения об азартных играх · US national survey measuring 15 gambling types including sports betting and pathological gambling (DIS-based); activity-level data likely.

**Решение:** =

---

### 1463 · R8258

**Against the odds : the sports gamblers attempt to overcome statistical probability**

2002 · Texas ScholarWorks (Texas Digital Library) · dissertation · en

This study has endeavored to discover the pertinent characteristics associated with sports gambling. Three variables appear to be especially prominent in the literature concerning gambling. Chasing one's losses is a gambling specific behavior that has been linked to pathological gambling (Lesieur, 1984). When gambler's chase their losses, they attempt to win back previously lost wagers with future gambles. In addition, previous research has focused on both the cognitive and decision making processes associated with gambling (Kahneman & Tversky, 1978; Langer, 1975). I have hypothesized that the manner in which cognitive processes, decision making, and chasing one's losses interact is a primary variable that contributes to pathological gambling. An additional hypothesis concerns the manner in which sports knowledge affects gambling behavior. The research described in this dissertation has attempted to examine the relevant cognitive and decision making processes associated with pathological gambling. Subjects engaged in gambling simulation over a six week period of time. This simulation replicated real-world gambling with the exception that money could not be lost. The top three winners were paid a percentage of their earnings in order to help insure internal validity. Results indicate that subjects with a high degree of sports knowledge gambled at a higher level and lost a greater amount of wagers than subjects with a low degree of sports knowledge. Implications associated with this include the possibility that individuals utilize knowledge as way to discount and distort statistical probabilities associated with gambling. In this study, cognition processes and decision making were not related to gambling outcomes.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Simulated sports gambling study focused on pathological gambling; unclear whether a screen like SOGS was given or real sports betting recorded.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Experimental gambling simulation with no real money loss; no problem-gambling screening instrument reported, so no prevalence among sports bettors.)

**Решение:** -

---

### 1464 · R8260

**The Status and Outlet of Sports Lottery**

2002

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: No abstract; the title suggests a paper on the sports lottery industry or policy, but a survey of players can't be ruled out.); Sonnet -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: 2002 title on sports lottery status and outlet (likely Chinese policy/industry discussion); no abstract, likely not an empirical problem-gambling study.)

**Решение:** ?

---

### 1465 · R8297

**A Study on the Consumption Behavior of Sports Lottery**

2001

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · There's no abstract. The title points to a study of sports lottery players, but we can't tell if it measured problem gambling.

**Решение:** =

---

### 1466 · R8346

**체육진흥투표권 잠재소비자 태도 조사**

2000

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Pre-launch survey of potential Sports Toto consumers' attitudes; title suggests attitudes/intentions only, no problem-gambling instrument.); Sonnet ? (нет аннотации: Korean survey of potential sports promotion lottery (sports toto) consumers' attitudes; no abstract, so unclear whether problem gambling was measured.)

**Решение:** -

---

### 1467 · R8358

**Gambling behavior of students in grades seven and eight in Alberta, Canada.**

1998 · The Journal of school health · article, journal article, journalarticle · eng · https://doi.org/10.1111/j.1746-1561.1998.tb03477.x

ABSTRACT: This article reports results from a survey of gambling activities of seventh and eighth grade students in northeastern Alberta, Canada. Results confirmed that gambling practices are common among young adolescents. During the 12 months preceding the survey, virtually all respondents (98%) had gambled. Playing scratch tickets was the gambling activity most often played by young adolescents, followed by bingo. Boys were more likely than girls to engage in all forms of gambling activities. Sports betting and wagering on games of skill dimension were mostly male domains, whereas games of chance were female pursuits. Survey implications for public health officials are discussed.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Adolescent gambling survey that measured sports betting; abstract doesn't say whether a problem-gambling screen such as SOGS-RA was used.

**Решение:** =

---

### 1468 · R8362

**Adolescent Gambling Behavior: A Prevalence Study and Examination of the Correlates Associated with Problem Gambling.**

1998 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1023/a:1023068925328

Eight-hundred and seventeen adolescent high school students in the Montreal region completed the DSM-IV-J gambling screen along with a questionnaire devised by the authors inquiring about their gambling behavior, including items assessing the types of activities in which they engage, frequency of involvement, reasons for gambling, and their cognitive perceptions of gambling activities. The results indicate that, in general, 80.2% of students reported having gambled during the previous year, with 35.1% gambling a minimum of once per week. Adolescents reported participating in gambling behavior more often than any other addictive behavior, including cigarette smoking, alcohol consumption, and illicit drug use. The mean age of onset of gambling behavior for the sample was 11.5 years. The rate of pathological gambling was 4.7% as measured by the DSM-IV-J. Pathological gamblers were more likely to have parents with gambling problems and to be engaging in illegal activities than non-pathological gamblers. Gender differences were evident, with males engaging in gambling activities more than females. Differences in game preferences were found, with males more attracted to sports lottery tickets and sports pool betting and females more attracted to lottery tickets and bingo. Gambling awareness and prevention issues are addressed.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Adolescent survey that used the DSM-IV-J and measured participation in sports lottery and sports pool betting.

**Решение:** =

---

### 1469 · R8364

**No . 88 Internet Gambling**

1998

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: No abstract; a numbered 1998 series item on internet gambling, probably a policy brief, but empirical content cannot be ruled out.); Sonnet -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: 1998 "No. 88 Internet Gambling" looks like a policy or legal report numbered in a series, with no abstract. Unlikely to be a quantitative sports-betting study.)

**Решение:** ?

---

### 1470 · R8396

**The phenomena of match-fixing and betting on sports in Singapore : a social and cultural perspective**

1996 · article · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: No abstract; socio-cultural analysis focused on match-fixing and sports betting in Singapore, unlikely to have used a problem-gambling instrument.); Sonnet ? (нет аннотации: No abstract; 1996 social/cultural study of sports betting and match-fixing in Singapore, likely qualitative or descriptive, but a survey with problem-gambling measures is possible.)

**Решение:** ?

---

### 1471 · R8400

**Do Motives Matter? Modeling Gambling on Sports among Athletes**

1995 · Sociology of Sport Journal · article, journal-article · en · https://doi.org/10.1123/ssj.12.1.21

The importance of competition and other motive statements in explaining gambling behavior is an important but controversial issue. This study operationalizes several types of motive statements related to sports participation, and then, in a novel methodological strategy, applies these as independent variables in a causal model of sport betting among college athletes. Based on questionnaires from 492 athletes at three colleges, findings showed that competitive and extrinsic motives for sport predict sports wagering. This is the case even in a multivariate equation that includes several control variables drawn from previous studies of gambling in the general population.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Questionnaire survey of 492 college athletes on sports wagering; the abstract doesn't say whether a problem-gambling instrument was used.

**Решение:** =

---

### 1472 · R8407

**Gambling among primary school students.**

1994 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/bf02104902

This study identifies the gambling behavior of 1,320 primary school students aged 8 to 12 of the 4th, 5th and 6th grades. Eighty-six percent admitted to having, at some time or another, bet money. Lotteries are the most popular form of gambling for this age group. Sixty-one percent of these students gamble with lotteries. In descending order of popularity, other games played by students were: bingo, card-playing for money, bets on sports, wagering on specific events, video gambling (video poker and slot machines), and finally betting on games of skill. Gambling behaviors differed according to gender. More than 40% of respondents reported gambling once a week or more for at least one game. Because of the early development of gambling behavior in children, prevention programs for pathological gambling should be implemented as early as the fourth grade.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Child gambling survey that measured sports betting; the abstract does not say whether a problem-gambling screen was used.

**Решение:** =

---

### 1473 · R8409

**Pathological Gambling**

1994 · Springer eBooks · book-chapter · en · https://doi.org/10.1007/978-1-4615-2409-0_19

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -1 (обзор, комментарий, теоретическая, правовая или регуляторная работа: 1994 book chapter with a generic clinical title and no abstract; most likely a narrative overview, not a survey of sports bettors.); Sonnet ? (нет аннотации: 1994 book chapter titled "Pathological Gambling" with no abstract; likely a review or overview chapter, but content cannot be determined.)

**Решение:** ?

---

### 1474 · R8422

**Gambling Behavior**

1992 · Springer eBooks · book-chapter · en · https://doi.org/10.1007/978-1-4757-9984-2_9

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · 1992 book chapter with a generic gambling title and no abstract; it's probably a review, but empirical content can't be ruled out.

**Решение:** =

---

### 1475 · R8452

**The social world of sports betting.**

1987 · article · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: No abstract; 1987 sociological title about sports betting, probably not using a PG screen, but can't rule it out.); Sonnet -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: 1987 article on the social world of sports betting. It is likely a sociological or ethnographic study from before problem-gambling screens were common. No abstract, so this is a judgment from the title.)

**Решение:** ?

---

### 1476 · R8453

**The social organization of sports gambling : a study in conventionality and deviance**

1986 · Medical Entomology and Zoology · article · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: No abstract; 1986 sociological study of sports gambling, probably ethnographic, but a problem-gambling measure can't be ruled out.); Sonnet -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: 1986 sociological study of sports gambling, likely ethnographic; it predates SOGS and standard problem-gambling instruments. No abstract is available.)

**Решение:** ?

---

### 1477 · R8466

**Science and luck in sports gambling.**

1983 · article · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: From the title, likely about betting skill versus luck; 1983 also predates standard PG screens. No abstract available.); Sonnet ? (нет аннотации: 1983 article on sports gambling with no abstract; could be an essay or a survey, and problem-gambling measurement can't be judged from the title.)

**Решение:** ?

---

### 1478 · R8510

**ThE PsYchoLoGY of IN-PLAY sPorTs BETTING : A**



_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Truncated title on in-play sports betting with no abstract; it could be empirical or a review, so check the full text.

**Решение:** =

---

### 1479 · R8513

**学生のギャンブル行動に関する予備的調査**

学生のギャンブル行動に関する予備的調査 · article · jpn · https://mukogawa.repo.nii.ac.jp/records/224

In Japan, soccer lottery is scheduled to start in 2001 as a new type of publicly-managed gambling. Relatively little is known about the effects of the advent of sports betting on youth gambling. The purposes of this study were to examine the prevalence of gambling and pseudgambling games among college students in Japan. 384 college students (aged 18-28) were administered questionnaire that inquires multiple domains of gambling behavior such as participation in gambling, dependency in gambling and cognition of gambling. Also was measured the desire for control to explore the possible relation between personality characteristics and gambling dependency. The majority of students gambled at least once in their life. However, most did not play any gamble or pseud-gambling game on a weekly/daily rate. The proportion of regular and problem gamblers found in this study were lower than prevalence rates reported in the US and Canada. Gender effect was found for gambling frequency and dependency. Male students gambled more often than female students. Cognitive factors seemed to be important in the explanation of gambling activity. Factors related to cognitive biases on gambling were discussed with reference to cognitive influences such as illusion of control, biased evaluations, and desire for control. College students will be the first generation of youth to be exposed to official sports betting and it will be important to continue monitoring the prevalence of youth gambling.

**ИИ:** разошлись — Opus ? (неясно, есть ли ставки на спорт: Japanese student gambling survey with dependency measure; ran before the soccer lottery launched, so whether sports betting was measured is unclear.); Sonnet + (игроки, есть ставки на спорт и инструмент: Survey of Japanese college students measuring gambling participation by game type and gambling dependency/problem gamblers; may report problem gambling by activity, including sports betting.)

**Решение:** ?

---

### 1480 · R8516

**SMU Data Science Review SMU Data Science Review**

review

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: The title is only the journal name and there is no abstract, so eligibility cannot be judged; likely data science, possibly betting prediction.); Sonnet -6 (не про азартные игры или «ставка/лотерея» в другом смысле: Record is only a journal name (SMU Data Science Review) with no abstract, year or gambling content; nothing suggests a sports betting or problem gambling study.)

**Решение:** -

---

### 1481 · R8520

**Gambling Away Education: A Community-Level Analysis of Gambling and Academic Performance among Junior High School Students in Ghana**

review

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; title suggests a quantitative study of adolescent gambling in Ghana, where sports betting is common; PG measure unknown.

**Решение:** =

---

### 1482 · R8524

**Montclair State University Digital Montclair State University Digital Commons Commons**



_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Title is only a repository header and there is no abstract, so the topic can't be judged; it may be a relevant thesis.

**Решение:** =

---

### 1483 · R8534

**The Relationship Between In-Play Betting and Gambling Problems The Relationship Between In-Play Betting and Gambling Problems in an Australian Context of Prohibited Online In-Play Betting in an Australian Context of Prohibited Online In-Play Betting**



_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** + · обе модели · беттеры + инструмент · No abstract, but the title suggests a quantitative study of Australian in-play sports bettors that relates their betting to gambling problems (likely PGSI).

**Решение:** =

---

### 1484 · R8536

**Gambling and Gaming in the United Kingdom during the COVID-19 Gambling and Gaming in the United Kingdom during the COVID-19 Lockdown Lockdown**

review

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; title suggests a UK lockdown gambling survey that may have measured PGSI and sports betting, despite the 'Review' label.

**Решение:** =

---

### 1485 · R8539

**The Price of Identity: Overoptimism and Congruence Concerns**

RePEc: Research Papers in Economics · article, research, preprint · en · https://doi.org/10.2139/ssrn.4670092

We examine how identity influences economic decision-making, using field experiments on sports betting to measure belief distortions and identity-driven preferences. We find that people overestimate the likelihood of identity-aligned outcomes by 10–18%, and allocate 20% more of their betting budget to teams for which they have an affinity than to neutral teams. Using a structural model of portfolio allocation, we show that overoptimism accounts for 30%–44% of this investment gap, while the remaining 56%–70% stems from an aversion to betting against one’s favored team, even when such bets offer higher expected returns. Our estimates suggest that this aversion is equivalent to discounting gains from identity-incongruent outcomes by 17%–27%. We also provide evidence for the “identity-threat response” theory: when individuals perceive their identity as under threat – such as after their team’s poor performance – they strengthen their commitment, reinforcing identity-driven betting. Our findings raise policy concerns, as identity-driven biases may exacerbate financial harm not only in the rapidly expanding sports betting market but also in broader consumer and financial decision-making contexts where identity affects choices.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Field experiments with sports bettors on identity-driven biases; abstract does not say whether a problem-gambling screen like the PGSI was given.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Field experiment on identity-driven sports betting allocation and belief distortion; no problem-gambling instrument mentioned.)

**Решение:** -

---

### 1486 · R8544

**Studio descrittivo sulla dipendenza da videogiochi e gioco d'azzardo nei giovani della provincia di Treviso**

bachelor thesis · und · https://hdl.handle.net/20.500.12608/58177

INTRODUZIONE: Negli ultimi anni la dipendenza da videogiochi si è allargato in maniera molto importante, spesso correlata anche al gioco d’azzardo. Si stima infatti che la dipendenza da videogiochi sia una patologia che coinvolge circa il 12%, e che sia in completa ascesa con un picco maggiore negli ultimi tre anni. Questa ricerca nasce dalla necessità di creare nuovi dati e analisi riguardo un argomento tanto giovane quanto attuale come la dipendenza da videogiochi, soprattutto se correlata ad uno sviluppo futuro in dipendenza da gioco d’azzardo. MATERIALI E METODI: È stata presa in considerazione la scuola secondaria “Duca degli Abruzzi” della Provincia di Treviso alla quale è stato somministrato un questionario online autoredatto, rivolto a tutti gli studenti e le studentesse, inerente al rapporto con i videogiochi e con le microtransazioni. I dati ricavati sono stati poi analizzati tramite vari programmi statistici, quali “R” e “Microsoft Excel”. RISULTATI E DISCUSSIONE: Sono stati raccolti un totale di 936 questionari, principalmente compilati dalle classi prime e dagli indirizzi scienze umane e scienze applicate. La media del coinvolgimento da videogiochi risulta essere 5,74 su una scala di 10, evidenziando un buon livello di autopercezione. Diversi risultati si notano nelle microtransazioni, in quanto solo 45 ragazzi hanno segnato un valore tra 5 e 10 nella scala di autopercezione, ma oltre il 15% ha dichiarato di aver speso soldi nell’ultimo mese. CONCLUSIONI: I risultati confermano la prevalenza del genere maschile sia per quanto riguarda il gioco, che l’utilizzo di soldi in microtransazioni, mentre si denota una superiorità delle prime rispetto alle quinte rispetto a questi ambiti. È presente una forte correlazione tra l’utilizzo di microtransazioni e i Battle Royale; questi ultimi inoltre sono anche in relazione con l’utilizzo di giochi d’azzardo non riconducibili ai videogiochi, quali ad esempio gratta & vinci, scommesse sportive o scommesse con le carte. Infine, si evince che la piattaforma maggiormente utilizzata dai giovani per giocare sia il telefono cellulare, confermando che la maggior parte del mercato videoludico si basa su questa tipologia di dispositivi. INTRODUCTION: In recent years, video game addiction has increased significantly, often also related to gambling. In fact, it’s estimated that video game addiction is a pathology that affects around 12%, and that it’s on the rise with a greater peak in the last three years. This research arises from the need to create new data and analysis regarding a topic as young as it is current such as video game addiction, especially if related to a future development in gambling addiction. MATERIALS AND METHODS: The "Duca degli Abruzzi" secondary school in the Province of Treviso was taken into consideration and a self-written online questionnaire was administered, aimed at all male and female students, relating to the relationship with video games and microtransactions . The data obtained were then analyzed using various statistical programs, such as "R" and "Microsoft Excel". RESULTS AND DISCUSSION: A total of 936 questionnaires were collected, mainly filled out by the first classes and the humanities and applied sciences courses. The average involvement with video games is 5.74 on a scale of 10, highlighting a good level of self-perception. Different results can be seen in the microtransactions, as only 45 kids scored a value between 5 and 10 on the self-perception scale, but over 15% declared having spent money in the last month. CONCLUSIONS: The results confirm the prevalence of the male gender both with regards to gaming and the use of money in microtransactions, while there is a superiority of the former over the latter in these areas. There is a strong correlation between the use of microtransactions and Battle Royale games; the latter are also also related to the use of gambling games not attributable to video games, such as scratch & win, sports betting or card betting. Finally, it is clear that the platform most used by young people to play is the mobile phone, confirming that the majority of the gaming market is based on this device.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Student survey (n=936) recorded sports betting, but used a self-written questionnaire; unclear whether any standard problem-gambling screen was included.

**Решение:** =

---

### 1487 · R8550

**Scholarship @ Claremont Scholarship @ Claremont**

review

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · The title is only a repository name (possibly a thesis), and there is no abstract, so content can't be judged without the full text.

**Решение:** =

---

### 1488 · R8551

**The Effects of Sports Gambling on Young Fans’ Attitudes and Behaviors in Hong Kong**

review

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; title suggests a possible survey of young sports bettors in Hong Kong despite the 'Review' label. PG measure unknown.

**Решение:** =

---

### 1489 · R8557

**Online betting services: a UK consumer perspective**

Ulster University Research Portal (Ulster University) · dissertation · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Dissertation on UK online betting consumers; no abstract, so it's unclear whether a problem-gambling instrument was used.

**Решение:** =

---

### 1490 · R8564

**Third Quarter 2024**



_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract or metadata. The title might belong to a quarterly gambling survey report, so it needs checking at full text.

**Решение:** =

---

### 1491 · R8565

**FANTASY SPORTS IN INDIA**



_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the title fits fantasy sports, but the record may be legal or policy work rather than a survey.

**Решение:** =

---

### 1492 · R8568

**Repositório ISCTE-IUL**



_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · The title is only a repository name (ISCTE-IUL) and there is no abstract, so the topic can't be judged; possibly a relevant thesis.

**Решение:** =

---

### 1493 · R8570

**Who uses custom sports**

review

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Title looks truncated, possibly a survey of sports bettors using custom betting products; no abstract to check for PGSI.

**Решение:** =

---

### 1494 · R8583

**AI-Assisted Bettors: Analyzing AI-Driven Betting Behavior through AI-Assisted Bettors: Analyzing AI-Driven Betting Behavior through Cluster Analysis Cluster Analysis**

review

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; cluster analysis of AI-assisted bettors could be a survey with a problem-gambling measure or behavioural data only.

**Решение:** =

---

### 1495 · R8594

**DOES PARETO RULE INTERNET GAMBLING? PROBLEMS AMONG THE “VITAL FEW” & “TRIVIAL MANY”**

RePEc: Research Papers in Economics · article · en · https://doi.org/10.5750/jgbe.v8i1.798

Using records of Internet gambling subscribers (n = 1, 384), this study tested the Pareto principle: about 20% of customers, “the vital few, ” are responsible for about 80% of the activity, while 80%, “the trivial many, ” are responsible for the remaining 20%. Participants completed the Brief Biosocial Gambling Screen (BBGS) and had a history of betting on sports and/or online casino games during the twelve months before completing the screen. Using various measures, the vital few Internet gamblers ranged between 4.6% and 17.8% of the subscribers – smaller than the Pareto principle would suggest. Between 38% and 67% of the vital few and between 24% and 35% of the trivial many screened positive for gambling-related problems. This research suggests that the concepts of the “vital few” and the “trivial many” apply to Internet gambling.

**ИИ:** + · обе модели · беттеры + инструмент · Internet subscribers who bet on sports and/or online casino, screened with the BBGS; the full text may give positive-screen rates for sports bettors.

**Решение:** =

---

### 1496 · R8598

**Les motivations du parieur et le regret : le cas des paris sportifs en ligne chez les 18 - 30 ans**

RePEc: Research Papers in Economics · article, preprint · fr · https://doi.org/10.34699/rido.2023.27

Ce travail aborde la question du regret chez les jeunes parieurs sportifs en ligne. Une méthodologie quantitative a été mobilisée auprès de 487 répondants âgés de 18 à 30 ans. Les résultats montrent que ce public semble avant tout à la recherche de sensations fortes, davantage que de gain d'argent ou de reconnaissance sociale. De plus, il est constaté que le jeune parieur regrette davantage le non-pari que le pari. Les raisons qui motivent les joueurs à miser ont un impact sur son niveau de regret. Il est donc primordial pour les entreprises de ce secteur de comprendre ce concept de regret ainsi que les motivations des parieurs, car cela aura un effet sur leur manière de jouer et leur fidélisation. This study explores the issue of regret among young online sports bettors. Aquantitative methodology was used with 487 respondents aged 18 to 30. The results show thatthis public seems above all to be looking for thrills, more than for money or social recognition.In addition,it was found that young gamblers regret not betting more than betting. The reasonswhy peoplebet have an impact on their level of regret. Understanding the concept of regret andthe motivations of bettors is critical for companies in this industry, and it will affect their wayof gambling and their loyalty.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of 487 young online sports bettors on motivations and regret; the abstract doesn't say whether a problem-gambling instrument was used.

**Решение:** =

---

### 1497 · R0602

**Payment preferences and related sports betting behavior: A secondary analysis of player data from an online sports operator**

2026 · OSF Preprints (OSF Preprints) · preprint

_Аннотации нет — решайте по названию или ставьте `?`._

**Ваша слепая метка (калибровка):** -3 данные оператора об игроках и платежах без опросника проблемной игры

**ИИ:** ? · обе модели · нет аннотации · Operator player data on sports bettors, probably behavioural only, but with no abstract we can't rule out a linked PGSI measure.

**Решение:** -

---

### 1498 · R0713

**Balancing harm prevention and liberty preservation when implementing financial risk assessments for gambling in the United Kingdom: Insights from open banking data**

2026 · Addiction · article · en · https://doi.org/10.1111/add.70513

BACKGROUND AND AIMS: The United Kingdom (UK) and Dutch governments have recently implemented mandatory financial risk (affordability) assessments for online gambling as a harm prevention measure. Assessments should trigger at a level of gambling expenditure that strikes a balance between harm prevention (most at-risk consumers should surpass the threshold) and liberty preservation (most no-/lower-risk consumers should gamble below it), yet little empirical research exists to guide threshold setting. We aimed to demonstrate how research can inform the harm-prevention, liberty-preservation trade-off in this context and evaluate the UK's proposed implementation of financial risk assessments. DESIGN, SETTING AND PARTICIPANTS: We reanalysed a dataset that combines self-reported Problem Gambling Severity Index (PGSI) scores and open banking data from consumers who gamble (n = 424) to (1) simulate the impact of the UK's rolling 30-day £150 net-deposit (deposits minus withdrawals) threshold for financial risk assessments, and (2) identify optimal threshold values for these assessments under different circumstances. Participants were UK residents who had gambled in the past year, recruited via Prolific in April 2024. MEASUREMENTS: Participants completed a survey containing the PGSI and agreed to provide their past 12 months' banking records. FINDINGS: Over 12 months, two-thirds of at-risk (PGSI ≥1) and nearly half of no-/lower-risk participants crossed the UK's £150 threshold [area under the curve = 0.66, 95% confidence intervals (CIs) = 0.62-0.71], demonstrating a greater emphasis on harm prevention over liberty preservation. Increasing the value to £186.9 (95% CIs = £69.5-£401.7) slightly improved this balance, although £150 remained within the range of appropriate values. Optimising for harm prevention in our sample required lowering the threshold to £39.0 (95% CIs = £29.6-£58.8), while emphasising liberty preservation increased it to £716.5 (95% CIs = £508.5-£990.9). We found that using a more conservative definition of risk (≥2 PGSI harms) resulted in higher thresholds, and lower thresholds may be appropriate for younger adults (<30 years). Finally, our findings suggest that thresholds based on spending with all operators-rather than single operators as implemented in the UK-may be better able to differentiate at-risk from no-/lower-risk consumers, although the added benefit of this approach in our sample was marginal and further research is needed to confirm its value. CONCLUSIONS: The United Kingdom's £150 net-deposit threshold for financial risk assessments for online gambling may place more emphasis on harm prevention than liberty preservation. This study provides a methodological template for guiding the implementation of financial risk assessments for online gambling. Because our sample is not representative of the broader UK gambling population, our specific threshold estimates should be treated as provisional.

**Ваша слепая метка (калибровка):** -3 банковские транзакционные данные пользователей без инструмента проблемной игры

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Survey of UK past-year gamblers using the PGSI plus open banking data; the abstract doesn't say whether sports betting participation was measured.

**Решение:** -

---

### 1499 · R1376

**Apuestas y Deportes: Influencia de los pronósticos deportivos en la sociedad ecuatoriana**

2025 · Mawil Publicaciones de Ecuador, 2025 · book · es · https://doi.org/10.26820/978-9942-654-94-6

Apuestas online: un síntoma de época Por Faro Digital Faro Digital es una organización social que busca fomentar una ciudadanía digital reflexiva y crítica desde Argentina, con una perspectiva que abarca lo local, lo regional y lo global. Nuestra labor se enfoca en la educación y la comunicación para, por un lado, crear espacios de diálogo y reflexión sobre la convivencia con las plataformas digitales; por otro lado, y a través de campañas y contenidos, buscamos concientizar sobre los riesgos y oportunidades que surgen al habitar los territorios digitales. Nos enfocamos especialmente en infancias, juventudes y sus relaciones con las tecnologias, promoviendo el desarrollo de herramientas de cuidado que permitan a las comunidades ejercer sus derechos. Lo digital atraviesa nuestras vidas de manera profunda, en tanto territorios sociales (Moyano, 2022) en donde nos informamos, comunicamos, vinculamos y construimos sentido y subjetividad respecto al mundo y la realidad. Nuestra misión es abordar esos desafíos desde la diversidad de realidades y contextos. En un territorio como Latinoamérica, cargado de historias, contradicciones y potencial transformador, el conocimiento se revela como una clave para forjar un futuro más justo e inclusivo. Este prologo propone un enfoque integral y desde lo relacional de los vinculos que sostenemos con (y entre) las tecnologías de la informacion y comunicacion (Passeron, 2023) para comprender un fenómeno social creciente: las apuestas online, particularmente entre las adolescencias y las juventudes. Desde Argentina hacia Ecuador, queremos tender un puente de reflexión para entender cómo el mundo digital afecta nuestras prácticas culturales, en el contexto de la denominada "economía de la atención" y a partir del fenómeno de la monetización de nuestros cuerpos, imaginarios y subjetividades. Las apuestas online como practica cultural Las apuestas online, disponibles (al igual que todas las plataformas) las 24 horas del día, los 7 días de la semana, se han convertido en una actividad masiva, especialmente entre las adolescencias. En los talleres que brindamos en escuelas, clubes y organizaciones sociales, observamos la preeminencia de las apuestas deportivas, un fenómeno que se presenta como una actividad naturalizada, no vergonzosa y con un marcado "valor social". Entre varones jovenes, en particular, estas prácticas refuerzan dinámicas grupales y sentidos de pertenencia vinculados al conocimiento del deporte, especialmente el fútbol: ligas, tácticas, equipos y jugadores. Sin embargo, las mujeres también apuestan, siendo un fenómeno que trasciende el género, edades y contextos socioculturales. Muchos jovenes describen la "adrenalina" como un elemento central en la experiencia de apostar, alimentada por la posibilidad de ganar o perder todo. Utilizan billeteras virtuales como método de pago y frecuentemente adoptan actitudes de riesgo que se resumen en frases como "voy allin" o "juego a fondo", convirtiendo a esta en una práctica legítima y popular. Eventos de gran magnitud, como el Mundial Qatar 2022 o la Copa América 2024, han funcionado como puertas de entrada a estas prácticas, impulsadas por una maquinaria publicitaria omnipresente (que funciona como elemento "normalizador") y que incluye a influencers, ídolos deportivos, periodistas y otros referentes juveniles. La economía de la atención El auge de las apuestas online no viene de la nada. Esta práctica social y cultural se inserta dentro de un ecosistema digital en donde predominan plataformas diseñadas para captar y retener nuestra atención. Las tecnologías no son en sí ni buenas ni malas, pero tampoco neutras (Sibilia, 2023). Traen consigo valores, estilos de vida e intenciones desde su diseno. Las digitales, mediante sus sistemas algorítmicos, procesan y dan sentido a los millones de datos que dia a dia usuarios y usuarias dejamos en dichos entornos. Las notificaciones, las gratificaciones instantaneas y las recompensas visibles (como likes, visualizaciones o comentarios) se convierten así en los principales motores (en clave de horizonte pero también en clave performativa) que guían las interacciones que la ciudadanía mantiene con dichas tecnologías. Las apuestas online emergen, entonces, como una extensión natural de estas lógicas. Son una expresión concreta del mandato de la inmediatez, donde la promesa de ganar (o perder) dinero en cuestión de segundos resulta irresistiblemente seductora para quienes estan ya habituados a estos ciclos de estimulo y respuesta. En este ecosistema, el dinero deja de ser visto como un recurso tangible y estable, transformandose en un numero abstracto en una pantalla que, como las métricas de las redes sociales, parece cobrar significado solo cuando está en movimiento. La idea de "dejarlo quieto" se percibe como una pérdida potencial, reforzando un paradigma de accion constante, donde el flujo continuo se asocia con exito y progreso. Esta logica de movimiento (Baricco, 2018) como valor se encuentra también en las plataformas de redes sociales digitales en donde cada publicacion puede alcanzar determinados likes, vistas, comentarios, etc. Estos modos de funcionamiento y las practicas que generan no solo alteran nuestra relacion con el dinero, sino tambien con el tiempo. Vivimos en un presente continuo, marcado por la urgencia de actuar y la imposibilidad de esperar. Las recompensas inmediatas reconfiguran nuestra paciencia y nuestras expectativas, llevando a muchos jóvenes a adoptar comportamientos de alto riesgo, como las apuestas, con la esperanza de obtener gratificaciones rápidas. Las apuestas online son la manifestación mas visible de esta economía de la atencion, donde no solo se comercializan productos o servicios, sino tambien nuestras emociones, nuestras decisiones y, en ultima instancia, nuestras vidas. La transformación del dinero en un simbolo dinámico, que debe moverse para "tener valor", refleja cómo este modelo económico nos empuja a internalizar una narrativa de constante productividad, consumo y riesgo. La cuantificacion y monetización de la vida cotidiana Comprender el modelo de funcionamiento de las plataformas digitales es fundamental para poder analizar las maneras en que nos afectan y reconfiguran nuestras maneras de ser, pensar y dar valor a las cosas. Decimos que las apuestas no son un problema aislado, ya que forman parte de un ecosistema que premia la inmediatez, prioriza el flujo continuo y monetiza nuestros imaginarios, cuerpos y subjetividades. Esto es, nos habituamos a interactuar con plataformas en donde cada acción que realizamos tiene que tener una recompensa o gratificación; y que, a su vez, nos dejan ante la gran paradoja contemporánea: que si queremos, podemos, pero que a su vez necesitamos de la valoración de los demás. Esto sucede por lo que advierte Sibilia (2024), quien describe la forma en que se dio un desplazamiento del suelo moral de lo social. Pasamos de una modernidad en donde primaba el "deber ser" (hipocrita en palabras de la investigadora) al cinismo del "si quiero, puedo" o "yo me lo merezco". Como muestra de esto basta reconocer los discursos que se promueven cada vez mas en las arenas digitales juveniles, en donde predomina el concepto de "plata fácil". Estos manifiestos de época, envasados en stories, shorts o tik-tok's encuentran eco en las adolescencias que ven en lo digital una plataforma para poder ganar dinero desde casa y casi sin esfuerzo, a través de practicas como el trading, la venta de imágenes o mismo las apuestas. Las apuestas no son nuevas, Internet no es nuevo, las publicidades no son nuevas, las adolescencias y las juventu des no son nuevas, la ludopatía no es nueva: ¿que nos preocupa?, ¿por que ahora? Estos fenomenos son parte de una transformación cultural más profunda, donde las nociones de valor, tiempo y esfuerzo están mediadas por dinámicas hipermonetizadas. En este escenario, la confianza se vuelve un tema central, cuestionando qué se valora y cómo se construyen las relaciones económicas y sociales en nuestros vínculos cotidianos con (y entre) las plataformas digitales. Dirá Sibilia (2024): "aunque este drama parezca causado por las tecnologias digitales, ellas integran cambios historicos en los modos de vivir que se fueron gestando a lo largo de décadas y terminaron produciendo una reconfiguración tanto espacio temporal como moral" (p. 90). En este escenario, es crucial fomentar un enfoque crítico y reflexivo que permita comprender cómo estas dinámicas afectan no solo a las juventudes, sino a la sociedad en su conjunto. Las plataformas digitales, lejos de ser neutras, están imbricadas en procesos históricos y culturales que moldean nuestras decisiones y formas de relacionarnos, Desde Faro Digital, proponemos construir colectivamente herramientas de cuidado y estrategias educativas que habiliten a las comunidades a ejercer sus derechos en los territorios digitales, promoviendo un uso consciente y transformador de la tecnología. Es un llamado a imaginar alternativas más justas e inclusivas para el presente y para el futuro.

**Ваша слепая метка (калибровка):** -1 коллективная монография / эссе о влиянии ставок в Эквадоре

**ИИ:** разошлись — Opus ? (другое: Ecuadorian book on sports betting; the abstract is only an essay-style prologue, so the book's chapters might include a survey with a PG measure.); Sonnet -1 (обзор, комментарий, теоретическая, правовая или регуляторная работа: The abstract is a prologue-style essay on online betting and the attention economy. It has no survey data and no problem-gambling measure.)

**Решение:** -

---

### 1500 · R1595

**Sports betting, alcohol problems follow similar trajectories: Study**

2025 · Alcoholism & Drug Abuse Weekly · article, journalarticle, journal-article · en · https://doi.org/10.1002/adaw.34447

Research evidence continues to suggest that sports bettors carry an elevated risk of alcohol‐related problems, with a newly published longitudinal study showing similar trajectories between gambling frequency and alcohol problems. There is even some evidence that problematic drinking levels are more prevalent among sports gamblers than among gamblers who don't wager on sports.

**Ваша слепая метка (калибровка):** -1 новостной дайджест о связи между ставками на спорт и алкоголем

**ИИ:** разошлись — Opus -1 (обзор, комментарий, теоретическая, правовая или регуляторная работа: Trade-newsletter news item reporting another study's findings on sports betting and alcohol; secondary reporting, not original data.); Sonnet ? (неясно, измеряли ли проблемную игру: News item on a longitudinal study of sports betting and alcohol problems; unclear whether problem gambling was measured, so the underlying study needs checking.)

**Решение:** -
