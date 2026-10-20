# Проверка с метками ИИ, часть 7

Записи 901–1050 из 1525, с метками обеих моделей над строкой решения. Модели согласны и вы тоже — поставьте `=`; иначе свой код (`+`, `?` или `-`, причина не нужна). Если модели разошлись, `=` не годится — нужен ваш код. Решаете вы.

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

### 901 · R4804

**Cognitions des parieurs sportifs**

2019 · Corpus Université Laval (Université Laval) · doctoral thesis, dissertation · fr · https://hdl.handle.net/20.500.11794/33999

Les paris sportifs constituent la seconde forme de jeux de hasard et d’argent (JHA), après les appareils de loteries vidéo (ALV), la plus fréquemment associée au jeu d’argent pathologique (JAP; Williams et al., 2002). Peu d’informations sont disponibles sur le profil de ces joueurs et sur les croyances qu’ils entretiennent par rapport aux paris sportifs. Jusqu’à présent les études portant sur les perceptions ont principalement été réalisées auprès de joueurs de hasard pur. De plus, lorsque les cognitions des joueurs d’habiletés sont évaluées, elles le sont avec des outils qui n’ont pas été adaptés aux caractéristiques structurelles des jeux d’habiletés. Considérant les fréquentes associations entre les cognitions erronées des joueurs et le JAP, réduire le flou qui persiste quant aux liens entre les cognitions des joueurs de paris sportifs et leurs comportements de jeu est essentiel. Cette thèse vise à étoffer les connaissances portant spécifiquement sur les parieurs sportifs afin d’identifier les facteurs de risque spécifiques à cette forme de JHA, notamment leurs cognitions. La première étude de cette thèse est une recension systématique des études publiées entre 1980 et 2014 qui comprennent un échantillon de parieurs sportifs. Cette revue documente les habitudes de jeu des parieurs, leurs cognitions, ainsi que les données des études visant à déterminer si les habiletés des parieurs sportifs augmentent leurs probabilités d’obtenir des gains au jeu. Sur les 991 études identifiées dans les bases de données, 31 satisfaisaient les critères d’inclusion de cette recension. Les données récoltées indiquent que les études portant sur les parieurs sportifs ont principalement été réalisées auprès d’hommes âgés de 30 à 50 ans, misant plusieurs fois par semaine et dépensant environ 100 à 200 $ CA hebdomadairement. Onze études rapportent des données quant aux cognitions des parieurs sportifs. Les résultats suggèrent que les parieurs sportifs entretiennent l’idée que leurs habiletés influencent leurs probabilités d’obtenir des gains financiers au jeu et qu’il est possible de devenir un meilleur parieur. Quant aux cinq études rapportant des résultats quant à l’impact de l’habileté sur la performance des parieurs sportifs, trois ont montré que les parieurs sportifs prédisent mieux les résultats sportifs que le hasard, mais ils ne gagnent pas plus d’argent qu’une sélection réalisée aléatoirement en raison de la structure du jeu. Des recommandations cliniques et de recherches futures sont formulées. Il est notamment suggéré de conceptualiser les cognitions des parieurs sportifs quant aux habiletés comme étant « à risque » plutôt qu’erronées et de réaliser de la psychoéducation auprès des parieurs quant aux connaissances actuelles portant sur l’impact de l’habileté au jeu. La seconde étude de cette thèse vise à développer et valider l’Inventaire des Cognitions à Risque — Loteries Sportives (ICR-LS) ainsi que de (1) déterminer la structure factorielle de l’ICR-LS, (2) vérifier sa validité de convergence avec le Gambling Related Cognitions Scale (GRCS; Raylu et Oei, 2004, version française : Grall-Bronnec et al., 2012), les habitudes de jeu, et la gravité des problèmes de jeu et (3) vérifier les liens entre le nombre d’heures mensuellement consacrées à la préparation des paris aux loteries sportives en saison de paris et les habitudes des joueurs. Un total de 272 parieurs sportifs, majoritairement de sexe masculin (86,5 %), dans la vingtaine (M = 26,7 ans), issus de la communauté universitaire (88,3 %) compose l’échantillon. Les analyses en composantes principales indiquent que l’instrument possède deux facteurs (superstitions et habiletés), une forte cohérence interne (alphas > , 85) ainsi qu’une bonne validité convergente au GRCS. Les associations entre le score moyen à l’ICR-LS, le montant annuel dépensé aux loteries, à la préparation des paris et à la gravité des problèmes de jeu, à la fréquence mensuelle de jeu sont toutefois négligeables. Ces résultats pourraient s’expliquer par la contribution quasi nulle de l’échelle superstitions aux associations, l’utilisation d’une échelle Likert à cinq niveaux ainsi qu’à l’absence de certains thèmes cognitifs extérieurs dans l’instrument qui auraient potentiellement bonifié celui-ci. À la lumière des résultats obtenus, il est suggéré de réaliser des entretiens focalisés auprès de parieurs sportifs afin d’identifier un maximum de thèmes cognitifs qui pourraient contribuer aux comportements de jeu des parieurs. Par la suite, il serait important de bonifier l’instrument et de procéder à une nouvelle expérimentation en vérifiant la stabilité temporelle de l’ICR-LS. Sports betting is the second most frequently form of gambling, after video lottery terminals (VLTs), associated with pathological gambling (PG; Williams et al., 2002). However, little is known about the profile of sports bettors and their cognitions. So far, gambling studies have mainly been conducted with pure chance gambler

**ИИ:** + · обе модели · беттеры + инструмент · Thesis surveying 272 sports lottery bettors; measured gambling problem severity alongside new cognition inventory validation.

**Решение:** =

---

### 902 · R4805

**Crypto-currency Trading Among Regular Gamblers: A New Risk for Problem Gambling?**

2019 · Digital Scholarship - UNLV (University of Nevada Reno) · conference-paper · en

Abstract Crypto-currency or “crypto” is digital money that can be used to fund risk-taking activities anonymously via the Internet (e.g., drugs, gambling). There is growing concern in the field of gambling studies that trading cryptos will appeal to high-risk gamblers. The present study assessed the prevalence of crypto trading among regular gamblers and its relationship to problem gambling severity. Adults (18+) who gambled at least monthly in the past year were recruited through Amazon’s Mechanical Turk (N = 876; 58.33% male) and completed the Problem Gambling Severity Index, Patient Health Questionnaire, and Generalized Anxiety Disorder scale via an online survey. More than half of the sample indicated they had traded cryptos in the past year. Crypto trading was strongly associated with higher levels of high-risk stock trading (r = .67), greater problem gambling severity (r = .53), and modestly associated with both anxiety (r = .20) and depressive symptoms (r = .20). Results from a linear regression revealed that sports betting, daily fantasy sports, high-risk stock trading, and problem gambling severity were positive predictors of crypto trading frequency, whereas gambling in land-based casinos was a negative predictor. Implications for problem gambling education, screening, and treatment will be discussed. Implications Statement The present findings represent an initial assessment of the prevalence of cryptocurrency trading among regular gamblers, and its relation to problem gambling. Future research should begin to include cryptocurrency trading in screening, assessment, and treatment protocols, particularly with regular gamblers.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Survey of regular gamblers measured sports betting, daily fantasy sports participation, and PGSI; may report problem gambling among sports bettors.

**Решение:** =

---

### 903 · R4806

**Preliminary findings on cryptocurrency trading among regular gamblers: A new risk for problem gambling?**

2019 · Addictive behaviors · article, journal article, journalarticle · eng · https://doi.org/10.1016/j.addbeh.2019.01.005

Cryptocurrencies are emerging digital currencies that allow anonymity in accessing various risk-taking activities through the Internet (e.g., drugs, gambling). However, given conceptual links to high-risk stocks, the present study sought to assess the association between trading cryptocurrencies and problem gambling. Data was collected through a cross-sectional online survey. Advertisement for the survey was posted on Amazon's Mechanical Turk. Participants were adults who had gambled at least monthly in the past year (N = 876; 58.33% male; M = 33.74 years, SD = 9.73). Participants completed the Problem Gambling Severity Index, Patient Health Questionnaire (2-item version), and Generalized Anxiety Disorder scale (2-item version). Trading cryptocurrencies is strongly associated with problem gambling severity (r = 0.53, p < .001). Results from a linear regression with backwards elimination revealed that sports betting, daily fantasy sports, high-risk stock trading, and problem gambling severity contribute to trading cryptocurrencies more frequently in the past year, whereas gambling in on-land casinos contributed to less cryptocurrency trading. Finally, trading cryptocurrencies overlapped strongly with trading high-risk stocks. Moreover, gamblers who engaged in both forms of trading reported greater problem gambling and depression and anxiety symptoms relative to those trading either cryptocurrencies or high-risk stocks, but not both. The present results suggest that trading cryptocurrencies may be appealing to gamblers that are exhibiting greater problem gambling severity. Future research should begin to include cryptocurrency trading in screening, assessment, and treatment protocols, particularly with regular gamblers.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Survey of regular gamblers that measured PGSI along with sports betting and DFS participation, so problem gambling among sports bettors may be reportable.

**Решение:** =

---

### 904 · R4810

**La epidemia de la adicción al juego online en la adolescencia: un estudio empírico del trastorno de juego**

2019 · Revista Española de Drogodependencias · article · es · https://hdl.handle.net/10550/106254

espanolLas primeras licencias de juego online (casino, bingo, tragaperras, apuestas y poquer online) se dieron en Espana en junio de 2012. Desde entonces se ha incrementado la oferta de juego, la publicidad y el gasto de los espanoles en esta actividad. En consecuencia han aparecido nuevos casos de trastorno de juego debidos al juego online, principalmente en poblacion juvenil. En este estudio se analiza el patron de juego y los problemas asociados (juego de riesgo y trastorno de juego) en 7.265 escolares de entre 15 y 19 anos, atendiendo a las diferencias en funcion de la edad y sexo. Los resultados obtenidos indican que el juego en el que los adolescentes participan con mayor regularidad son las apuestas deportivas, encontrando diferencias estadisticamente significativas tanto en frecuencia como en problemas de juego (trastorno de juego y juego de riesgo) entre mujeres y hombres, asi como entre menores de edad y adolescentes de 18 y 19 anos. En todos los casos, la prevalencia de adiccion al juego online en adolescentes entre 15 y 19 anos es superior a la de la poblacion general por trastorno de juego, que es del 0,72%. Si consideramos que una epidemia es un problema de salud que se desarrolla por un agente externo que afecta a una parte de la poblacion en un momento determinado y que se extiende mas rapidamente de lo esperado, podemos afirmar que en la actualidad existe una epidemia de adiccion al juego online en los adolescentes debido a la legalizacion del juego online. La legalizacion supuso la aparicion de estas modalidades de juego y la ausencia de una regulacion que tuviera como principal objetivo la prevencion del trastorno de juego tuvo como consecuencia la extension de este problema de salud. EnglishLicenses to operate with online gambling establishments (casino, bingo, slots, bets and online poker) started in Spain in June 2012. Since then, the gambling offerchoice, advertising and spending of among Spaniards has strongly increased heavily. Since online gambling is more addictive than traditional gambling, new cases of pathological gambling have appeared due to online gambling, mainly in the younger population. In this study, the gambling pattern and the associated problems (risk and pathological gambling) are analyzed in 7,265 schoolchildren between 15 and 19 years old, taking into account differences according to age and sex. From the results obtained it is concluded that adolescents mostly engage in sports betting, the gambling that adolescents participate with more regularity are sports betting, finding statistically significant differences both in frequency and in gambling problems (pathological gambling and risk gambling) between women and men, and between minors and adolescents between 18 and 19 years old. Differences were also obtained between women and men, as well as among minors of age and adolescents of 18 and 19 years old.In all cases, the prevelance of adition to online gambling in adolescents between 15 and 19 years old id higher than in the general population in terms of gambling disorders, standing at 0.72%. An epidemic is a health problem that affects a part of the population at a certain time in a way that is higher than expected. Therefore, we can affirm that now we are now seeing have an epidemic of addiction to online gambling in adolescents. And tThe causes of this are the legalization, promotion and the absence of any regulation that defends the right to health over the economic interests.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Survey of 7,265 adolescents measuring sports betting plus classifying risk gambling and gambling disorder; the screening instrument is presumably used but not named.

**Решение:** =

---

### 905 · R4811

**The Risk of Online Gambling: a Study of Gambling Disorder Prevalence Rates in Spain**

2019 · International Journal of Mental Health and Addiction · article · en · https://doi.org/10.1007/s11469-019-00067-4

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the title points to a Spanish gambling disorder prevalence study of online gambling, which probably includes sports betting.

**Решение:** =

---

### 906 · R4817

**Testing a gambling warning label’s effect on behavior**

2019 · PsyArXiv · article, other literature type, preprint · en · https://doi.org/10.31234/osf.io/dxfkj

Responsible gambling campaigns are one measure enacted by a number of statutory bodies and gambling operators in response to concerns about gambling marketing and the accessibility of modern gambling products. For example, since 2015 a number of the UK‘s largest gambling operators have attached the following warning label to TV and shop window adverts: "when the FUN stops, stop" (where the word "fun" is printed in noticeably larger font than any other word). Here we present an initial independent test of this warning label‘s effect on contemporaneous gambling behavior. A short incentivized survey was conducted to mimic the scenario of online gambling advertising, with warning label presence manipulated between-participants. Participants were given a sequence of nine £0.10 bonuses, and on each trial were presented with the possibility to gamble this bonus on a soccer bet, with bet details and payoffs taken from a major gambling operator‘s website. There were 506 unique participants who had all previously indicated that they were Premier League soccer fans and had experience in online sports betting. Overall, participants decided to bet on 41.3% of trials when a warning label was shown, compared to 37.8% when no warning label shown (i.e., descriptively the label increases the probability of gambling). According to the preregistered analysis plan, this difference was not significant, (χ^2 (1)=2.10, p=.15) The "when the FUN stops, stop" gambling warning label did not achieve its aim of prompting more responsible gambling behavior in the experiment.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Experiment with 506 online sports bettors; the abstract doesn't say whether PGSI or another problem-gambling screen was collected.

**Решение:** =

---

### 907 · R4818

**Who uses custom sports betting products?**

2019 · PsyArXiv · preprint, posted-content · und · https://doi.org/10.31234/osf.io/qnxcz

Background: The expansion of online gambling in the UK has been accompanied by an increase in the number of novel betting products, particularly for soccer. The present research investigates which types of sports bettors are the most likely to use novel gambling products called ‘custom sports bets’ (CSBs), which allow gamblers to create their own unique bets. Method: A large-scale, cross-sectional survey of online sports/horse racing bettors (N = 789, 32.7% female). The survey collected two measures of CSB usage and four validated gambling measures: the Problem Gambling Severity Index, the Gambling Related Cognition Illusion of Control Scale, the Short Gambling Harm Screen, and the Consumption Screen for Problem Gambling. Results: Overall, 62.0% of participants reported having used a CSB, and those who had used a CSB did so on an average of 29.4 days over the last year. Overall, 16.0% of participants who had used a CSB were current problem gamblers, compared to 6.7% among those who had not. CSB users reported an average of 2.3 out of 10 possible gambling harms, compared to 1.5 harms for those who had not used a CSB. The illusion of control scale was significantly positively correlated with whether participants had ever used a CSB before, but not with past year frequency of CSB usage. The usage of CSB products was most strongly associated with the frequency of gambling consumption. Conclusions: Overall, these findings suggest that CSB products raise distinctive concerns around consumer protection for frequent sports bettors which deserve further investigation.

**ИИ:** + · обе модели · беттеры + инструмент · Survey of online sports/race bettors using PGSI; reports problem gambling rates by custom sports bet use.

**Решение:** =

---

### 908 · R4822

**Characteristics of Sports Betters in an Epidemiological Study**

2019 · Digital Scholarship - UNLV (University of Nevada Reno) · conference-paper · en

ABSTRACT The potential impact of the recent legalization of sports wagering in the U.S. on rates of problem gambling is unknown, particularly in light of interactive media. The current study examines the self-reported behavior of 332 sports betters in a representative sample of 2,213 participants (>18 years) in a statewide study on gambling. Results of univariate analyses and multiple regression modeling indicated: More than 97% of sports betters also bet on other forms of gambling, including daily fantasy sports (58%). Compared to other gamblers, those who bet on sports were more likely to be younger, male, undereducated (less than high school) and to report a physical limitation or disability. In addition, sports betters were more likely to smoke, binge drink, use illegal drugs, report a mental health problem in the past year and to seriously have contemplated suicide. Unlike a majority of other gamblers, sports betters gambled both online and in land-based venues; preferred activities were lottery, poker, live casino tables games, daily fantasy sports, and horse track betting. Finally, sports betters in the study were significantly more likely to score as moderate or high risk problem gamblers on the PGSI than other gamblers in the study. IMPLICATIONS: States are legalizing sports wagering without investigating the potential impacts on underage youth or young adults, who may subvert regulatory age limitations on interactive platforms. Our findings suggest these effects should be a serious concern. Suggestions for harm reduction, prevention, and education strategies targeting this group will be discussed.

**ИИ:** + · обе модели · беттеры + инструмент · Statewide representative survey; 332 sports bettors compared on PGSI moderate/high risk categories.

**Решение:** =

---

### 909 · R4823

**Risky decision making and cognitive flexibility among online sports bettors in Nigeria.**

2019 · PsyArXiv · preprint, posted-content · en · https://doi.org/10.31234/osf.io/cujyp

Online sports betting is a popular recreational activity in Nigeria. Like other forms of gambling, risk of pathological progression exists for gamblers who continue betting despite severe financial and psychosocial consequences. In the present study, we examined whether this population of gamblers shows deficits in decision making and cognitive flexibility that have been documented in Western gambling populations. Thirty-six online sports bettors and 42 non-gambling participants completed a version of the Iowa gambling task (IGT) and an established set-shifting task for the assessment of cognitive flexibility. The two groups did not differ significantly in the selection of disadvantageous decks on the IGT. In contrast, sports bettors committed significantly more errors on the set-shifting task than non-gambling control participants. As this performance deficit was not specific to trials requiring a set shift, it most likely resulted from gambling-related changes in general cognitive or motivational abilities that are required to successfully complete challenging mental tasks. While our results illustrate that findings from Western populations cannot automatically be generalized to other contexts, it should be noted that we focused on only one particular type of gambling and included mostly participants with mild gambling-related problems.

**ИИ:** + · обе модели · беттеры + инструмент · Sample of 36 online sports bettors described as having mostly mild gambling problems, which suggests a PG screen was used; not recruited for problems.

**Решение:** =

---

### 910 · R4824

**Does Sports Betting Affect Investment Behaviour? Evidence from Ghanaian Sports Betting Participants**

2019 · Journal of Gambling Issues · article, review, journal-article · en · https://doi.org/10.4309/jgi.2019.43.5

The study sought to assess the impact of sports betting on the investment behaviour of Ghanaians, focusing on sports betting centers within the Accra Metropolis, Ghana. The objectives of this observational study were to determine how individuals perceive the risk of sports lotteries as opposed to investment, to determine if sports lottery was viewed as an alternative to investments and savings, and to understand how participation in sports lotteries affects individuals’ ability to save and invest. In adopting a survey approach, 99 sports betting participants across selected betting centers were examined using questionnaires and the data subsequently analyzed through cross-tabulations. The study found that sports betting behaviour had a complementary rather than a substitutionary effect on investment behaviour. The participants were both risk-aware and risk-averse, but engaged nevertheless in betting for a chance of winning a high payoff. Thus, the findings demonstrated that sports betting participants viewed betting as a means to an end, a chance to improve their financial circumstances, rather than as a substitute for investing, and exhibited understanding of a clear distinction, with regards to behaviour, towards investing and sports betting. In return for a substantive payoff, the respondents were willing to stop sports betting, thereby indicating that the financial payoffs were the main motivation for sports betting. The findings also provided evidence that individual sports betting behaviour can be moderated by influencing one’s financial circumstances.RésuméL’étude cherche à évaluer l’incidence des paris sportifs sur le comportement d’investissement des Ghanéens, en mettant l’accent sur les centres de paris sportifs au sein de la métropole d’Accra, au Ghana. Cette étude observationnelle vise à déterminer comment les personnes perçoivent le risque lié à la loterie sportive par rapport à l’investissement, à déterminer si la loterie sportive est considérée comme une solution de rechange aux investissements et à l’épargne et à comprendre comment la participation à la loterie sportive affecte la capacité des personnes à épargner et à investir. En adoptant une approche d’enquête et à l’aide de questionnaires et de données analysées dans des tableaux croisés, on a analysé 99 participants aux paris sportifs dans les centres de paris sélectionnés. L’étude a révélé que les paris sportifs avaient un effet complémentaire plutôt qu’un effet de substitution en matière de comportement d’investissement. Les participants étaient conscients du risque et démontraient une aversion au risque, mais pariaient pour avoir la chance de remporter un gain élevé. Ainsi, les résultats ont montré que les participants aux paris sportifs considéraient ces paris comme un moyen d’atteindre une fin, une chance d’améliorer leur situation financière plutôt que comme un substitut à l’investissement. Et en ce qui concerne le comportement, ils savaient clairement faire la différence entre l’investissement et les paris sportifs. Les données ont montré qu’en échange d’un gain substantiel, les répondants étaient disposés à cesser de participer à ces paris, ce qui a permis de démontrer que les gains financiers étaient la principale motivation de ces jeux. Les résultats fournissent également des preuves étayant l’idée selon laquelle le comportement individuel lié aux paris sportifs peut être modéré en influençant la situation financière de chacun.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Questionnaire survey of 99 Ghanaian sports bettors on investment behaviour; abstract doesn't say whether a problem-gambling screen was used.

**Решение:** =

---

### 911 · R4828

**Associations of Dark Triad traits and problem gambling: Moderating role of age among university students**

2019 · Current Psychology · article · en · https://doi.org/10.1007/s12144-018-0093-3

The current study examined the associations of Dark Triad personality factors (namely, Machiavellianism, narcissism, and psychopathy) with problem gambling, and whether age moderates nature of these associations. Participants were 252 Nigerian undergraduate students who were identified as sports gamblers. They completed the 27-item Short Dark Triad and the Problem Gambling Severity Index (PGSI). Results showed that psychopathy and student’s age positively predicted problem gambling, while narcissism was a negative predictor of problem gambling. Machiavellianism did not significantly predict problem gambling. It was also found that at older age, the associations of narcissism and psychopathy with problem gambling was stronger than at mean age, but non-existent at younger age. Age did not moderate of the relationship between Machiavellianism and problem gambling. Implications of the findings for problem gambling engagement, and prevention strategies in at risk university students were highlighted.

**ИИ:** + · обе модели · беттеры + инструмент · 252 Nigerian student sports gamblers completed the PGSI, so problem gambling prevalence among sports bettors could be reported.

**Решение:** =

---

### 912 · R4835

**Exploring psychological need satisfaction from gambling participation and the moderating influence of game preferences**

2019 · International Gambling Studies · article, review · en · https://doi.org/10.1080/14459795.2019.1633381

ABSTRACT Psychological needs are satisfied through leisure participation, which in turn influences subjective well-being. The present study explored the psychological needs reported to be satisfied through gambling participation and examined associations between need satisfaction, game preferences and subjective well-being. A heterogeneous, self-selected sample of 1446 participants was recruited, through the Internet gambling provider Kindred Group Plc, for an online questionnaire survey. Five psychological need dimensions of gambling were identified, using exploratory and confirmatory factor analyses on calibration and validation samples, respectively: mastery, detachment, self-affirmation, risk and excitement, and affiliation. Challenge and mastery need satisfaction was higher for poker than for sports betting, horse racing, slots or casino table games; both self-affirmation and affiliation were also higher for poker than for sports betting and slots. By comparison, detachment was higher for slots than for sports gambling. While there were no significant variations in stress levels between the different forms of gambling, happiness ratings were lower for slots compared with sports betting and poker. This study provides insight into how distinctive patterns of play may satisfy different psychological needs and provides preliminary insights into how gambling patterns may prove adaptive or maladaptive as leisure choices.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Online gambler survey with sports betting preference group; abstract doesn't say if a problem-gambling instrument such as PGSI was used.

**Решение:** =

---

### 913 · R4838

**The liberalization of sports betting in the United States of America**

2019 · article · fra/fre · https://hal.science/hal-04999895v1

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: The title points to a policy or regulatory paper on US sports betting liberalization, and there is no abstract suggesting survey data.); Sonnet ? (нет аннотации: No abstract; title suggests a policy/legal paper on US sports betting liberalization, likely not empirical, but content is unclear.)

**Решение:** ?

---

### 914 · R4839

**Obilježja kockanja mladića grada Zadra**

2019 · dissertation · hr

The aim of this study is to gain insight into gambling activites and gambling intensity among male high school students in Zadar, prevalence of gambling related problems as well as its correlation with internet addiction. Specific aims are to determine representation and frequency of participation in various games of chance and representation of problem gambling, possible differences in frequency of gambling and representation of problem gambling regarding age and type of school. Last specific aim is to explore possible differences in the intensity of internet addiction between adolescents with different levels of gambling-related problems. This research is integral part of study „Prevalention of gambling and usage of internet of adolescents iz Zadar county“ conducted by Service for mental health and prevetion of addiction of Croatian Institute of Public Health, led by dr. Marija Pupic-Bakrac, and was conducted in April of 2019th on a sample of 411 male high school students from first to final grades from different high schools in Zadar. In this study, a validated set of instruments with good metric characteristics was used: Questionnaire on basic socio-demographic characteristics, Gambling activities questionnaire, Canadian adolescents gambling inventory (CAGI), Internet addiction test, and separate questions about some gambling characteristics. The research results show that 56,8% of male students once participated in sports betting during their lifetime, and that 37,4% once played lottery tickets during lifetime. Most frequent gambling activity among male high school students is sports betting, where 22,7% of participants are betting regularly and 34,1% occasionally. The differences in frequency of gambling was found in the way that students of higher classes are gambling more often, and students from gymnasium school are gambling more often than students from vocational schools. The research showed that 9,4% of students belong to the group characterized by high severity of gambling related problems, 21,8% of students belong to the group with low to medium severity of gambling related problems, while 68,8% of students have no problems related to gambling. Students of fourth and second classes are showing highest level of problems related to gambling, while gymnasium students have higher level of problem gambling in comparison with students from vocational schools. Lastly, the results confirm that male students who have adverse psychosocial consequences related to gambling in greater measure manifest problems connected with excessive usage of internet.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Survey of 411 male adolescents that measured sports betting participation (56.8%) and problem gambling severity with the CAGI.

**Решение:** =

---

### 915 · R4840

**Obilježja kockanja mladića grada Zadra – učestalost kockanja, zastupljenost problema i povezanost s problematičnom uporabom interneta**

2019 · University of Zagreb. University of Zagreb, Faculty of Education and Rehabilitation Sciences · master thesis · hrv · https://www.bib.irb.hr/1025508

Temeljni cilj ovog rada je stjecanje uvida u aktivnosti i učestalost kockanja muških učenika zadarskih srednjih škola, zastupljenost problema povezanih s kockanjem, kao i povezanost problematičnog kockanja i problematične uporabe interneta. Specifični ciljevi ovog rada su utvrditi učestalost sudjelovanja u različitim igrama na sreću i zastupljenost problema povezanih s kockanjem, te razlike u učestalosti kockanja i zastupljenosti problema povezanih s kockanjem s obzirom na razred i vrstu škole. Uz to, specifični cilj je bio istražiti postoje li razlike u izraženosti ovisnosti o internetu s obzirom na razinu problema povezanih s kockanjem. Ovo istraživanje je sastavni dio istraživanja "Prevalencija kockanja i korištenje interneta kod mladih u Zadarskoj županiji" Službe za mentalno zdravlje i prevenciju ovisnosti Zavoda za javno zdravstvo Zadar, čija je voditeljica Marija Pupić-Bakrać, dr. med. spec. epidemiologije, a provedeno je u travnju 2019. godine na uzorku od 411 muških učenika od prvog do završnog razreda različitih srednjoškolskih usmjerenja u Zadru. U istraživanju su korišteni provjereni instrumenti dobrih metrijskih obilježja, a radi se o sljedećim instrumentima: Upitnik o osnovnim sociodemografskim obilježija, Upitnik kockarskih aktivnosti (Ricijaš i sur., 2011), Kanadski upitnik kockanja adolescenata - CAGI (Tremblay, Stinchfield, Wiebe i Wynee, 2010), Test ovisnosti o internetu (eng. Internet Addiction Test - IAT, Young, 1998), te zasebna pitanja o nekim obilježjima sudjelovanja u igrama na sreću. Rezultati istraživanja su pokazali da se 56,8% mladića barem jednom u životu kladilo, dok je njih 37,4% jednom u životu odigralo jednokratne srećke. Najučestalija kockarska aktivnost među muškim srednjoškolcima je sportsko klađenje, gdje je dobiveno da se njih 22,7% kladi redovito a 34,1% povremeno. Utvrđene su razlike u učestalosti kockanja na način da učenici viših razreda češće kockaju u od učenika nižih razreda, dok se učenici gimnazija učestalije kockaju od učenika iz strukovnih škola. Istraživanjem je utvrđeno da 9,4% učenika pripada skupini koju obilježava visoka ozbiljnost problema vezanih uz kockanje, 21,8% učenika pripada skupini s niskom do srednjom ozbiljnosti problema vezanih uz kockanje, dok 68,8% učenika pripada skupini koju obilježava nepostojanje problema vezanih uz kockanje. Učenici četvrtih i drugih razreda iskazuju najvišu razinu problema povezanih s kockanjem, dok učenici iz gimnazija iskazuju najvišu razinu zastupljenosti problema povezanih s kockanjem u odnosu na učenike strukovnih škola. Posljednje, istraživanje je pokazalo da postoje razlike u ovisnosti o internetu s obzirom na razinu problema povezanih s kockanjem na način da učenici koji imaju izraženije štetne psihosocijalne posljedice povezane s kockanjem u većoj mjeri manifestiraju i probleme povezane s prekomjernom uporabom interneta. The aim of this study is to gain insight into gambling activites and gambling intensity among male high school students in Zadar, prevalence of gambling related problems as well as its correlation with internet addiction. Specific aims are to determine representation and frequency of participation in various games of chance and representation of problem gambling, possible differences in frequency of gambling and representation of problem gambling regarding age and type of school. Last specific aim is to explore possible differences in the intensity of internet addiction between adolescents with different levels of gambling-related problems. This research is integral part of study "Prevalention of gambling and usage of internet of adolescents iz Zadar county" conducted by Service for mental health and prevetion of addiction of Croatian Institute of Public Health, led by dr. Marija Pupić-Bakrać, and was conducted in April of 2019th on a sample of 411 male high school students from first to final grades from different high schools in Zadar. In this study, a validated set of instruments with good metric characteristics was used: Questionnaire on basic socio-demographic characteristics, Gambling activities questionnaire, Canadian adolescents gambling inventory (CAGI), Internet addiction test, and separate questions about some gambling characteristics. The research results show that 56,8% of male students once participated in sports betting during their lifetime, and that 37,4% once played lottery tickets during lifetime. Most frequent gambling activity among male high school students is sports betting, where 22,7% of participants are betting regularly and 34,1% occasionally. The differences in frequency of gambling was found in the way that students of higher classes are gambling more often, and students from gymnasium school are gambling more often than students from vocational schools. The research showed that 9,4% of students belong to the group characterized by high severity of gambling related problems, 21,8% of students belong to the group with low to medium severity of gambling related pro

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Survey of 411 male high school students that measured sports betting participation (56.8%) and problem gambling with the CAGI screen.

**Решение:** =

---

### 916 · R4842

**Digital WPI Major Qualifying Projects ( All Years ) Major Qualifying Projects April 2019 Choice Effects and Classification in Online Daily Fantasy Sports**

2019

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; DFS student project probably analyses contest or behavioural data, but problem-gambling measurement cannot be ruled out.

**Решение:** =

---

### 917 · R4843

**Gambling during adolescents: the role of playing sports as a risk factor**

2019 · Universitat Jaume I · bachelor thesis · eng · http://hdl.handle.net/10234/184401

Introducción: En los últimos años ha aumentado la participación en los juegos de azar debido, en parte, a la Ley 13/2011 que regula el juego online (Caselles, Cabrera y Lloret, 2018; Chóliz y Saiz-Ruiz, 2016). El juego en los jóvenes se ha convertido cada vez más en un problema importante. Según Choliz, Marcos y Lázaro (en prensa) la prevalencia de juego patológico es del 0,72% en adolescentes. Además, hay pocos estudios que hayan analizado si practicar deportes es un factor de riesgo para apostar (Mateu Puchades, 2016). Por ello, el objetivo de esta investigación fue estudiar la prevalencia del juego en estudiantes federados y no federados. Método: Ciento ochenta estudiantes (Edad Media= 16,4 años (DT= 0,93); 35% mujeres) completaron vía online cuestiones sociodemográficas, la frecuencia de juego, y el NODS (Wickwire, Burke, Brown, Parker, & May, 2008). Para comparar la frecuencia de juego y los problemas derivados del juego entre los grupos de estudio, se realizó un análisis multivariado de covarianza controlado por edad, sexo y paga semanal. Resultados: El grupo de federados en fútbol mostró una frecuencia de uso significativamente mayor de quinielas, juegos de casino y apuestas deportivas, frente a los no federados (d =.82, .60 y .76) y federados en otros deportes (d =.79, .40 y .79), y una mayor puntuación en juego problemático que los no federados (d =.44). Discusión: De forma similar a estudios previos, encontramos que practicar deportes es un factor de riesgo para los juegos de azar (Huang, Jacobs, Derevensky, Gupta y Paskus, 2007). Además, este es el primer estudio que distingue entre estudiantes federados en fútbol y otros deportes a la hora de estudiar las prevalencias de juegos de apuestas y problemas derivados. Los resultados apuntan la necesidad de desarrollar programas de prevención selectiva para este colectivo de riesgo. Introduction: In recent years, participation in gambling has increased due to, in part, to the Law 13/2011 which regulates the online gambling (Caselles, Cabrera & Lloret, 2018; Chóliz & Saiz-Ruiz, 2016). The gambling in youths has become increasingly an important problem. According to Choliz, Marcos and Lázaro (in press), the prevalence of pathological gambling is 0.72% in adolescents. In addition, there are few studies that have analyzed if playing sports is a risk factor for gambling (Mateu Puchades, 2016). Therefore, the aim of this study was to study the prevalence of gambling in federated and non-federated students. Method: One hundred and eighty students (Average Age = 16.4 years (SD= 0,93), 35% women) completed online sociodemographic questions, frequency of gambling and the NODS (Wickwire, Burke, Brown, Parker, & May, 2008). To compare the frequency of gambling and the gambling-related problems between groups, we performed multivariate analysis of covariance controlling for age, sex and weekly pocket money. Results: The federated group in soccer showed a significantly higher frequency of use of pool, casino games and sports bets compared to the non-federated group (d = .82, .60 and .76) and federated in others sports (d = .79, .40 and .79); and a higher score in gambling-related problems than non-federated students (d = .44). Discussion: Similarly to previous studies, we found that playing sports is a risk factor for gambling (Huang, Jacobs, Derevensky, Gupta, & Paskus, 2007). In addition, this is the first study that differentiate between federated soccer players and students federated to other sports when prevalence of gambling and gambling-related problems are studied. The results highlight that soccer players are target youths to benefit of selective prevention programs. Treball Final de Grau en Psicologia. Codi: PS1048. Curs: 2018/2019.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Adolescent student survey measuring sports betting and football pools frequency plus NODS; could report problem gambling among sports bettors.

**Решение:** =

---

### 918 · R4851

**Adolescent Gambling, Gambling Expenditure and Gambling–Related Harms in Finland, 2011–2017**

2019 · Journal of Gambling Studies · article · en · https://doi.org/10.1007/s10899-019-09892-7

Abstract Existing literature on recent trends in adolescent gambling is scarce. The rapidly changing landscape of gambling, together with the generally applied legal age limits, calls for the continuous monitoring of gambling also among the adolescent population. In Finland, the legal gambling age is 18. We examined changes in adolescents’ gambling, gambling expenditure and gambling–related harms from 2011 to 2017. Comparable cross-sectional biennial survey data were collected in 2011, 2013, 2015 and 2017 among 12–18-year-olds (N = 18,857). The main measures were self-reported six-month gambling, average weekly gambling expenditure (€) and harms due to gambling. Data were analyzed using cross-tabulations, χ2-tests and linear regression analysis. A significant decline in gambling among minors (aged 12–16-year-olds) was found (β = − 0.253), while no significant changes were observed among 18-year-olds (who are not targeted by the law). The mean gambling expenditure also declined from 2011 to 2017. Adolescent gamblers experienced significantly less (p = .003) gambling–related harms in 2017 (7.4%) compared to 2011 (13.5%). Adolescent gambling and its related negative consequences have become less prevalent in Finland between 2011 and 2017. Further monitoring is necessary to ascertain whether the positive direction will continue. Also, empirical analyses providing evidence of reasons for the observed trend are warranted.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Adolescent population survey measured gambling-related harms, but unclear if a validated PG instrument was used or sports betting was measured.

**Решение:** =

---

### 919 · R4852

**Assessment of motives for sports betting among youth in Tanzania: A case study of Kinondoni District**

2019 · dissertation · en

A Dissertation Submitted in Partial/Fulfillment of the Requirements for Award of Degree of Masters of Marketing Management (MSc. Marketing) of Mzumbe University

**ИИ:** ? · обе модели · нет аннотации · Marketing dissertation on why young people bet on sports; no real abstract, so it's unclear whether problem gambling was measured.

**Решение:** =

---

### 920 · R4858

**Predictors of older adult gambler in representative sample: Implications for education, prevention and treatment**

2019 · Digital Scholarship - UNLV (University of Nevada Reno) · conference-paper · en

Abstract: Though rates of gambling among older adults appear to be increasing, few studies have examined the factors that distinguish older adult problem gamblers in a representative sample. This presentation will detail findings from a statewide, epidemiological survey using univariate and multinomial logistic regression. Among older adults (56-97; N=624), those with gambling problems were more likely to be African American or to have gambling friends and less likely to be divorced than all other older adult gamblers. Overall, older adult gamblers were more likely than young gamblers (18-35; N=714) to be white, divorced or separated, and undereducated and to report military service, owning a home, using tobacco, having a disability and less likely to play daily fantasy sports, live poker or to bet on sports. Compared to middle-aged adults (36-55; N+624), older adult gamblers were less likely to be Asian or Hispanic, to report drug usage, to play daily fantasy sports, trade high risk stocks or bet on sports, and more likely to report military service or home ownership. Across groups, older adults were underrepresented among those with the highest levels of problem gambling severity but were more likely than other gamblers to participate in multiple gambling activities. Implications: A greater understanding of older adult gamblers will assist in tailoring education, intervention, and treatment efforts to the unique needs and characteristics of this population, resulting in harm reduction and more robust prevention strategies.

**ИИ:** + · обе модели · опрос населения об азартных играх · Statewide epidemiological gambling survey that measured problem gambling severity along with sports betting and DFS participation.

**Решение:** =

---

### 921 · R4859

**La influència de la publicitat de cases d'apostes en un increment de la ludopatia**

2019 · other literature type · cat · https://ddd.uab.cat/record/213003

En un contexto con las apuestas deportivas en el punto de mira de los medios de comunicación y parte de la opinión pública, algunos sectores de la población, incluidos algunos partidos políticos, sitúan la publicidad de estas apuestas como uno de los aspectos más urgentes a erradicar para combatir el incremento de jugadores de azar, sobretodo online. ¿Cuál es, pero, la relación de esos anuncios con el incremento del juego y la ludopatía? En un context on les apostes espotives es troben al punt de mira en mitjans de comunicació i part de l'opinió pública, alguns sectors de la població, inclosos alguns partits polítics, situen la publicitat d'aquestes apostes com un dels aspectes més urgents a erradicar per combatre l'increment de jugadors d'atzar, sobretot online. Quina és, però, la relació que han tingut aquests anuncis amb l'increment del joc i amb la ludopatia? In a context where sports bets are targeted in the media and part of public opinion, some sectors of the population, including some political parties, place the advertising of these bets as one of the most urgent aspects of Eradicate to combat the increase of gamblers at random, especially online. What, however, is the relationship that these ads have had with the increase of the game and with ludopathy?

**ИИ:** разошлись — Opus ? (другое: Catalan student work on sports betting advertising and gambling addiction; unclear whether it includes a survey or a problem-gambling instrument.); Sonnet -1 (обзор, комментарий, теоретическая, правовая или регуляторная работа: Appears to be a commentary/opinion piece on sports betting advertising and gambling increase; no indication of an empirical survey with a problem-gambling instrument.)

**Решение:** -

---

### 922 · R4860

**Trends in gambling behavior among college student-athletes: A comparison of 2004, 2008, 2012 and 2016 NCAA survey data**

2019 · Journal of Gambling Issues · article, review · en · https://doi.org/10.4309/jgi.2019.41.5

Student-athletes represent a vulnerable subgroup of the college student population with regards to engagement in high-risk behaviours. Four large samples of National Collegiate Athletic Association (NCAA) student-athletes in 2004 (N = 20,587), 2008 (N = 19,942), 2012 (N = 22,935) and 2016 (N = 22,388) were surveyed about their gambling behaviours and attitudes. A cross-sectional study was conducted to gain insight into changing gambling behaviours and attitudes among college student-athletes. Findings revealed gender differences in participation rates of gambling with men consistently engaging in all gambling activities at higher rates than women (55% of men versus 38% women in 2016). Despite gender differences, the results suggest that participation rates for most gambling activities have generally decreased over the twelve-year span. The proportion of student-athletes at-risk or meeting criteria for pathological gambling between 2004 and 2016 has also decreased among men (4% in 2004 versus 2% in 2016) while remaining relatively consistent among women (&lt;1% across all years). Furthermore, attitudes towards various forms of gambling appear to have changed over time, with a greater number of student-athletes in 2016 believing that sports wagering is unacceptable and a potentially harmful activity. Taken together, the results suggest that gambling behaviours among student-athletes may be on a downward trend despite the increased accessibility and availability of gambling opportunities.RésuméEn ce qui concerne la participation à des comportements à risque élevé, les étudiants-athlètes représentent un sous-groupe vulnérable de la population des étudiants universitaires. Quatre grands échantillons d’étudiants-athlètes de la National Collegiate Athletic Association (NCAA), 2004 (N = 20 587), 2008 (N = 19 942), 2012 (N = 22 935) et 2016 (N = 22 388), ont été sondés sur leurs comportements et leurs attitudes de jeu. Une étude transversale a été menée afin de mieux comprendre l’évolution des comportements et des attitudes face au jeu chez les étudiants athlètes. Les résultats ont révélé des différences entre les sexes dans les taux de participation au jeu, les hommes pratiquant systématiquement toutes les activités de jeu à un taux plus élevé que celui des femmes (55 % d’hommes contre 38 % de femmes en 2016). Malgré les différences entre les sexes, les résultats laissent entendre que les taux de participation à la plupart des activités de jeu ont généralement diminué au cours de la période de douze ans. La proportion d’étudiants-athlètes à risque ou satisfaisant aux critères du jeu pathologique entre 2004 et 2016 a également chuté chez les hommes (4 % en 2004 contre 2 % en 2016), tout en restant relativement stable chez les femmes (&lt;1 % pour toutes les années). En outre, les attitudes vis-à-vis des différentes formes de jeu semblent avoir évolué au fil du temps. En 2016, un plus grand nombre d’étudiants-athlètes pensaient que les paris sportifs étaient inacceptables et potentiellement nocifs. Mis ensemble, les résultats suggèrent que les comportements de jeu parmi les étudiants-athlètes pourraient être à la baisse, en dépit de l’accessibilité accrue et de la disponibilité des possibilités de jeu.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · NCAA student-athlete surveys measured sports wagering and pathological/at-risk gambling (likely DSM-based); full text may report problem gambling among sports bettors.

**Решение:** =

---

### 923 · R4863

**Sports betting incentives encourage gamblers to select the long odds: An experimental investigation using monetary rewards.**

2019 · Journal of behavioral addictions · article, journal article, journalarticle · eng · https://doi.org/10.1556/2006.8.2019.30

Background and aims Incentives for wagering products can provide extra value to gamblers. However, there is no financial reason why this added value should lead people to take greater gambling risks. This study aimed to experimentally test if wagering incentives cause gamblers to choose higher-risk (long odds) bets than un-incentivized bets. Methods An online experiment was conducted with wagering customers ( N = 299, female = 12). Participants bet $4 on each of six video game simulations of a sport that they had wagered on in the past 12 months (Australian Football League, Cricket, or Soccer). Each game offered different common wagering incentives: Bonus bet, Better odds/winnings, Reduced risk, Cash rebate, Player's choice of inducement, or No-inducement. For each game, participants could bet on long, medium, or short odds, and subsequently viewed a highlight reel of the simulated game outcome and bet outcome. Results Participants selected significantly longer odds (i.e., riskier) bets on games when an incentive was offered compared to the No-inducement condition. Better odds/winnings was the most attractive incentive, followed by Bonus bet, Cash rebate, Reduced risk, and No-incentive, respectively. No significant differences were observed based on demographics or problem gambling severity. Discussion and conclusions The choice of long odds with incentivized bets increases the volatility of player returns. Increased volatility results in more gamblers in a losing position and fewer gamblers with larger wins. Moreover, if long odds bets are priced to provide poorer value to bettors compared to short odds, they would increase gamblers' losses and equivalently increase operators' profits.

**ИИ:** + · обе модели · беттеры + инструмент · Experiment with 299 sports wagering customers; problem gambling severity was measured (likely PGSI), so it could report problem-gambling prevalence.

**Решение:** =

---

### 924 · R4870

**Gambling Risk Groups are Not All the Same: Risk Factors Amongst Sports Bettors.**

2019 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-018-9765-z

Sports betting is increasing worldwide, with an associated increase in sports betting-related problems. Previous studies have examined risk factors for problem gambling amongst sports bettors and have identified demographic, behavioural, marketing, normative and impulsiveness factors. These studies have generally compared those in problem gambling, or a combination of moderate risk and problem gambling, groups to non-problem gamblers, often due to statistical power issues. However, recent evidence suggests that, at a population level, the bulk of gambling-related harm stems from low risk and moderate risk gamblers, rather than problem gamblers. Thus it is essential to understand the risk factors for each level of gambling-related problems (low risk, moderate risk, problem) separately. The present study used a large sample (N = 1813) to compare each gambling risk group to non-problem gamblers, first using bivariate and then multivariate statistical techniques. A range of demographic, behavioural, marketing, normative and impulsiveness variables were included as possible risk factors. The results indicated that some variables, such as gambling expenditure, number of accounts with different operators, number of different types of promotions used and impulsiveness were significantly higher for all risk groups, while others such as some normative factors, age, gender and particular sports betting variables only applied to those with the highest level of gambling-related problems. The results generally supported findings from previous literature for problem gamblers, and extended these findings to low risk and moderate risk groups. In the future, where statistical power allows, risk factors should be assessed separately for all levels of gambling problems.

**ИИ:** + · обе модели · беттеры + инструмент · Survey of 1813 sports bettors grouped into PGSI-style risk groups (non-problem, low, moderate, problem).

**Решение:** =

---

### 925 · R4871

**Risk Factors for Gambling Problems Specifically Associated with Sports Betting.**

2019 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-019-09848-x

Studies examining risk factors for problem gambling amongst sports bettors have used screens that assess gambling problems in general. Because people experiencing gambling-related problems tend to gamble on multiple forms, it is unclear whether problems identified amongst sports bettors are due to sports betting itself. The present study examined a range of distal and proximal demographic, behavioural and psychological risk factors using a modified version of the Problem Gambling Severity Index which respondents answered only in relation to their sports betting. In general, those at risk were younger, spoke a language other than English, were more engaged sports bettors and gamblers, and tended not to watch the event they had bet on. They particularly endorsed money-oriented motivations, and had higher erroneous cognitions, gambling urges, and were more likely to experience alcohol issues. Higher-risk sports bettors were also more likely to apportion less responsibility for their gambling to themselves, and to have lower self control. A penalised model found that key predictors were money motivations, gambling urges and erroneous cognitions, alcohol issues and lower self-control, but not sports betting behaviour. These findings suggest that one's psychological relationship to sports betting is a primary driver of gambling-related problems, rather than just betting behaviour. As sports betting expands through new products and legalisation in additional jurisdictions, understanding who is most at risk from this form of gambling is important to inform legislation as well as harm reduction and treatment measures.

**ИИ:** + · обе модели · беттеры + инструмент · Survey of sports bettors using a modified PGSI specific to sports betting; risk-category prevalence is likely reported.

**Решение:** =

---

### 926 · R4872

**Who Bets on Micro Events (Microbets) in Sports?**

2019 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-018-9810-y

Sports betting is expanding globally through introduction into new markets and growth in existing markets. Traditionally, bets were placed on the outcome of a match before match commencement, with the outcome not determined for hours or even days. The advent of in-play betting has reduced the delay between bet and outcome. A controversial form of in-play betting is betting on micro events (micro-betting), where consumers bet on outcomes such as the next ball in cricket, or the next point in tennis, with the outcome determined almost immediately. This enables rapid, impulsive and continuous betting and may heighten the risk of problem gambling. We surveyed 1813 Australian sports bettors to determine demographic, behavioural and psychological characteristics of micro event bettors, and of those who place a higher proportion of their bets on micro events. Our two hypotheses were supported: that more highly engaged bettors, including those with gambling problems, are more likely to (1) bet on micro events, and (2) place more of their bets on micro events. Of those who bet on micro events, 78% met criteria for problem gambling, and only 5% non-problem gambling (vs 29% and 28% respectively for non micro event bettors). Placing a higher proportion of bets on micro events was also related to problem gambling. Micro event bettors were likely to: be younger, well educated and single; engaged in a wider variety of gambling activities; and to have high trait impulsivity. Micro event betting appears to appeal almost exclusively to bettors with gambling problems, so a ban would represent a highly targeted intervention to reduce gambling-related harm.

**ИИ:** + · обе модели · беттеры + инструмент · Survey of 1813 Australian sports bettors reporting problem gambling prevalence among micro-event and other bettors.

**Решение:** =

---

### 927 · R4879

**Menção honrosa 2: Rastreamento do transtorno do jogo: um panorama sobre os apostadores esportivos brasileiros**

2019 · article · pt

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** + · обе модели · беттеры + инструмент · There's no abstract, but the title says it screened Brazilian sports bettors for gambling disorder, so it likely reports prevalence.

**Решение:** =

---

### 928 · R4880

**Sports Gambling among Iranians: A Test of Control and Rational Choice Theories**

2019 · Deviant Behavior · article, journal-article · en · https://doi.org/10.1080/01639625.2019.1580252

ABSTRACT Gambling on sporting events is an illegal activity in Iran, and this phenomenon is widespread. Taking its point of departure from Control and Rational Choice Theories, this study examines the effects of self-control, social bonding, and rational choice on both gambling behavior and pro-gambling orientations. From a sample of 417 gamblers from the city of Rasht (the capital city of the Guilan province, one of Iran’s largest cities) and using structural modeling analysis, we investigated how various theoretically derived parameters predict gambling behavior and gambling orientations. The results showed significant, negative associations between our latent variables (self-control, social bonding, and rational choice) and respondents’ self-reported gambling behavior and pro-gambling orientations. Moreover, self-control, social bonding, and rational choice combined to account for 54% of the variance of self-reported gambling and 49% of the variance in respondents’ pro-gambling orientations. Measures of the total standardized effects showed that self-control was more strongly associated with both gambling behavior and a pro-gambling orientation than either social bonding or rational choice.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of 417 Iranian sports gamblers; the abstract reports self-reported gambling behaviour but doesn't say whether a problem-gambling instrument was used.

**Решение:** =

---

### 929 · R4889

**Biddable Youth Sports and esports Gambling Advertising on Twitter: Appeal to Children, Young &amp; Vulnerable People**

2019 · Unpublished · text/other · en · https://doi.org/10.13140/rg.2.2.30040.24328

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: No abstract; mainly an analysis of Twitter ad content, but may include a youth survey that measured gambling behaviour.); Sonnet -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: Title suggests a content analysis of gambling advertising on Twitter, not a survey of people with a problem-gambling measure.)

**Решение:** ?

---

### 930 · R4892

**Controversial and Global Issues Fantasy Sports' Outcomes**

2019 · DigitalCommons - Kennesaw State University (Kennesaw State University) · article · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; fantasy sports topic, possibly a discussion piece, but empirical data on players cannot be ruled out.

**Решение:** =

---

### 931 · R4894

**El uso de las Nuevas Tecnologías (internet, redes sociales, videojuegos) en jóvenes: un estudio con población canaria**

2019

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -6 (не про азартные игры или «ставка/лотерея» в другом смысле: Study of internet, social media and video game use among Canary Islands youth; title doesn't mention gambling or sports betting.); Sonnet ? (нет аннотации: No abstract; survey of Canary Islands youth on technology use may include online gambling and problem gambling screens, but this is unclear.)

**Решение:** -

---

### 932 · R4901

**ปจจยทมผลตอพฤตกรรมการเลนการพนนฟตบอลของเยาวชนในสถาบนการอาชวศกษา**

2019 · Political Science and Public Administration Journal · article · th

This study was a study on factors affecting football gambling behaviors among youths in vocational education institutions in Bangkok. This study collected data from 382 youths studying in vocational institutions in Bangkok using questionnaire as a collecting tool. Multiple regression analysis was used for data analysis. The study found that social bonding has a negative effect whereas social learning has a positive effect on football gambling behavior among youths. It is suggested that we should focus on family and educational institutions to promote social bonding and to reduce the misuse of social learning regarding football gambling.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Questionnaire survey of 382 vocational students about football gambling behaviour; the abstract doesn't say whether a problem-gambling instrument was used.

**Решение:** =

---

### 933 · R4902

**Gambling among Swedish youth: Predictors and prevalence among 15- and 17-year-old students**

2019 · Nordic Studies on Alcohol and Drugs · article · en · https://doi.org/10.1177/1455072518807788

BACKGROUND: Gambling among adolescents is a growing public health concern in Sweden as in many other countries. Excessive gambling has been found to be associated with a wide range of negative consequences such as financial problems, strained relationships, criminal behaviour, depression, and an elevated risk for suicide. Research suggests a link between alcohol consumption and gambling, particularly among male gamblers. There are nevertheless gaps in the available knowledge pertaining to school-aged students in Sweden. AIM: The purpose of this study is to investigate predictors of gambling and frequent gambling among Swedish students in Grade 9 and Grade 11 (ages 15 and 17 years). DATA AND METHOD: = 3720). Poisson regression models have been applied to estimate the association between less frequent and frequent gambling with the predictors of gender, family and school satisfaction, school situation, and alcohol and drug use. RESULTS: Gambling among Swedish students is a highly gendered activity: boys gamble more and more frequently than girls. Having consumed alcohol was associated with both less frequent and more frequent gambling among Grade 9 students while controlling for other variables. In Grade 9, heavy episodic drinking was only associated with less frequent gambling, not with frequent gambling. Among Grade 11 students, both alcohol consumption and heavy episodic drinking was associated with less frequent gambling but heavy episodic drinking was only associated with frequent gambling. Moreover, drug use was associated with less frequent gambling in Grade 11. Skipping classes was the only school factor that was found to be associated with less frequent gambling (Grade 11). Such factors as family satisfaction and two measurements of economic situation were not associated with gambling at all.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Swedish school survey reporting gambling frequency only; the full text may include a problem-gambling screen and data on sports betting.

**Решение:** =

---

### 934 · R4912

**Sportwetten – Begeisterung vs Suchtgefahr**

2019 · article · de

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · German title on sports betting and addiction risk; there's no abstract, so it may be an empirical study or a commentary.

**Решение:** =

---

### 935 · R4915

**Assoziation von Glücksspielsymptomatik und kultureller Herkunftsregion: Befunde aus der MIGUEL-Studie**

2019 · Suchttherapie · conference-paper · de · https://doi.org/10.1055/s-0039-1696174

Einleitung Menschen mit Migrationshintergrund stellen eine Hochrisikogruppe zur Entwicklung einer Gambling Disorder dar. Frühere Studien weisen auf eine Assoziation bestimmter Eigenschaften einzelner Kulturkreise und glücksspielbezogenen Problemen hin. Bislang ist der Zusammenhang der kulturellen Herkunftsregion mit der Ausprägung sowie dem Verlauf der Glücksspielsymptomatik ungeklärt. Methode Bei einem proaktiven Screening in Berufsschulen in Schleswig-Holstein berichteten 488 Schüler*innen mit Migrationshintergrund ein mindestens auffälliges Glücksspielverhalten, von denen 207 an einer weiterführenden telefonischen Diagnostik teilnahmen. Nach durchschnittlich zehn Monaten konnten 73% (n = 151) zur Nachbefragung erreicht werden. Die Proband*innen wurden drei Clustern zugeteilt: Cluster Ost1 (Türkei, Länder des Mittleren und Fernen Ostens, Afrika; n = 110), Cluster Ost2 (Osteuropäische Staaten, Länder der ehemaligen Sowjetunion; n = 68) und Cluster West (West-, Süd- und Mitteleuropa, Australien, Nord-, Mittel- und Südamerika; n = 29). Glücksspielbezogene Probleme wurde mittels des Stinchfield Fragebogens erfasst. Mithilfe multinomialer logistischer Regressionsmodelle wurden die Zusammenhänge der kulturellen Herkunftsregionen und der Symptombelastung sowie des Verlaufs der Glücksspielsymptomatik betrachtet. Ergebnis Proband*innen des Clusters Ost 1 wiesen im Vergleich zum Cluster West zum Baseline-Zeitpunkt eine signifikant höhere Symptomschwere auf (OR = 1.290, 95%-KI = 1.031 – 1.613, p = .026). Bezüglich der Anzahl genutzter Glücksspielarten konnten keine bedeutsamen Unterschiede gefunden werden. Jedoch nahmen Zugehörige des Clusters Ost 1 signifikant häufiger an Sportwetten teil (= .006) und es zeigte sich eine Tendenz für Sofortlotterien im Cluster West (= .064). Die Herkunftsregion Ost 1 erwies sich in der multivariaten Analyse bei Kontrolle auf Problemschwere zum Baseline-Zeitpunkt als signifikanter Risikofaktor für eine Verschlechterung der Glücksspielsymptomatik nach durchschnittlich zehn Monaten (OR = 5.065, 95%-KI = 1.682 – 15.250, p = .004). Diskussion Die Befunde deuten darauf hin, dass die Zugehörigkeit zu Cluster Ost 1 mit einem erhöhten Risiko zur Entwicklung und Aufrechterhaltung einer Glücksspielsymptomatik assoziiert ist. Dies ist für die Weiterentwicklung von kultursensiblen Behandlungsangeboten relevant und sollte bei der Ausgestaltung von Präventions- und Therapieangeboten berücksichtigt werden.

**ИИ:** разошлись — Opus -5 (выборка набрана по проблемам с игрой: лечение, горячая линия, самоисключение, сравнение проблемных игроков с контролем: Analysed sample is only migrant students who screened positive for at least conspicuous gambling; Stinchfield was then given to this problem-selected subsample.); Sonnet ? (другое: School screening of migrant students; the analysed sample was pre-selected for at-risk gambling, but sports betting and the Stinchfield screen were measured, so the full text may report the screening data.)

**Решение:** ?

---

### 936 · R4916

**The Star Tribune/WCCO-TV Minnesota Poll: Sports and Gambling**

2019 · Roper Center for Public Opinion Research · other/study · https://doi.org/10.25940/roper-31094035

Interest in sports (4); budgeting for sports events (1); sports games attended (11); following major sporting events (9); spending on special events (1); ticket prices (5); disposable income spending (7); agreement about sports statements (5); interest in hockey (4); lottery tickets (4); gambling activities (10); gambling outside of Minnesota (4); gambling for money (4); age starting gambling (1); most recent gamble (2); Minnesota casinos (2); limiting gambling money (2); favorite casino games (4); agreement with gambling statements (6).

**ИИ:** разошлись — Opus -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Public opinion poll; the detailed question list covers gambling activities and attitudes but includes no problem-gambling screening instrument.); Sonnet ? (неясно, измеряли ли проблемную игру: Minnesota public poll on sports and gambling activities; no problem-gambling instrument listed in the abstract, but the full survey might include a screen.)

**Решение:** -

---

### 937 · R4920

**Some Neuropsychological Profiles and Personality Traits of Undergraduate Regular Online Football Gamblers (a New Online Gambling Game) in Nigeria.**

2019 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-018-9812-9

Online football (soccer) gambling is among the relatively new sports betting games in Nigeria that use internet connections. Like other gambling games, some psychological profiles either propel or sustain the behavior. We tested some neuropsychological profiles and personality traits that distinguish the regular online football gamblers from non-gamblers. Using a between group design, we tested 140 (60: online football gamblers; 80: non-gamblers) university undergraduate students between the ages of 18-26 years on specific neuropsychological domains (i.e., attention, inhibition and executive function) and personality traits. The neuropsychological tasks used were the Series Addition Task (a modified version of Paced Auditory Serial Addition Task), Stroop-Word Color Test and Trail Making Test (TMT), Parts A and B. The personality traits were assessed using the Big Five Personality Inventory. The findings showed significant differences between the online football gamblers and non-gamblers, reflecting greater agreeableness, conscientiousness, neuroticism and openness to experience for the football gamblers. However, on the attention tasks, the non-gamblers made significantly fewer errors on forward addition and backward subtraction tasks, but did take more time to complete the backward counting task as compared to gamblers. On the other hand, online football gamblers took significantly less time to complete the Stroop congruence task and made significantly fewer errors on Stroop incongruence task. Similarly, the online football gamblers took less time to complete the TMT B and made fewer errors on TMT A. University undergraduate regular online football gamblers, as compared to non-gamblers, demonstrate stronger personality traits of ambition and gregariousness, and perform better on tasks of executive function, though they had more difficulty on tasks of divided and sustained attention.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Sample of online football bettors; abstract names no problem-gambling screen, but one may have been used to classify gamblers.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Compares online football gamblers with non-gamblers on neuropsychological tasks and personality; no problem-gambling instrument is mentioned.)

**Решение:** ?

---

### 938 · R4936

**The Same or Different? Convergence of Skin Gambling and Other Gambling Among Children**

2019 · Journal of Gambling Studies · article · en · https://doi.org/10.1007/s10899-019-09840-5

There is increasing attention on the introduction of gambling-like practices within video games. Termed convergence, this has been explored from the viewpoint of the product, examining similarities in game/gambling mechanics. Understanding convergence of practice is essential to map the epidemiology of these behaviours, especially among children. This paper focuses on the betting of skins within video games to explore co-occurrence with other forms of gambling among British children aged 11-16. Analysing the British Youth Gambling Survey showed that 39% of children who bet on skins in the past month had also gambled on other activities. Betting on skins and other forms of gambling increased with age and concordance of skin gambling/betting was greatest for those who also gambled online. Among gamblers, those who bet skins had higher rates of at-risk and problem gambling than those who did not (23% vs. 8%), though they had a greater breath of gambling involvement. Skin gambling alone was not significantly associated with at-risk gambling when other forms of gambling activity were taken into account. Skin betting and gambling on other activities cluster together, especially where the medium underpinning the behaviours is the same. Children who engage in both skin gambling/betting and other forms of gambling should be considered at-risk for the experience of harms because of their heightened engagement in gambling and gambling-like activities.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · British Youth Gambling Survey measured at-risk/problem gambling and gambling activities, including skin betting (often esports) and likely sports betting.

**Решение:** =

---

### 939 · R4939

**An Exploratory Study of Relationships Among Five-Factor Personality Measures and Forms of Gambling in Adults With and Without Probable Pathological Gambling.**

2019 · Journal of gambling studies · journal article, journalarticle, article · eng · https://doi.org/10.1007/s10899-018-9809-4

The present study explored relationships between personality domains and gambling forms in individuals with and without probable pathological gambling (PPG). Associations among personality domain scores obtained from the NEO Personality Inventory-Revised, endorsements of gambling activities on the South Oaks Gambling Screen (SOGS), and PPG as determined by the SOGS were examined with bivariate and logistic regression analyses. Compared to recreational gamblers, those with PPG scored significantly higher in neuroticism and lower in agreeableness and conscientiousness. Agreeableness was inversely associated with gambling on cards, sports, bingo, stock market, dice, and skill games. Conscientiousness was inversely associated with gambling on sports and animal racing. Extraversion was positively associated with gambling on cards, dice, and stocks. Neuroticism and openness were positively associated with gambling on animal racing and stock gambling, respectively. Significant interactions indicated stronger inverse associations between agreeableness and gambling in casinos, on sports, and on skill games and stronger positive associations between openness and gambling on stocks and skill games in individuals with PPG compared to those without. The results suggest different relationships between personality domain measures and specific forms of gambling in individuals with and without PPG. Future research efforts should examine how personality factors may be used to enhance policy, prevention, and treatment efforts.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Gamblers sample with SOGS-based probable pathological gambling and sports gambling endorsement; check full text for recruitment and sports bettors' PPG rates.

**Решение:** =

---

### 940 · R4948

**Spike in Sports Betting**

2019 · DigitalCommons-Cedarville (Cedarville University) · article · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; probably a university news or opinion piece, but the title alone can't rule out an empirical survey.

**Решение:** =

---

### 941 · R4950

**Gambling-like video game practices: A cross-sectional study of links with problem gambling and disordered gaming**

2019 · PsyArXiv · article, other literature type, preprint · en · https://doi.org/10.31234/osf.io/fh3vx

A variety of practices have recently emerged which are related to both video games and gambling. Most prominent of these are loot boxes. However, a broad range of other activities have recently emerged which are also related to both gambling and video games: esports betting, real-money video gaming, token wagering, social casino play, and watching videos of both loot box opening and gambling on game streaming services like Twitch.Whilst a nascent body of research has established the robust existence of a relationship between loot box spending and both problem gambling and disordered gaming, little research exists which examines whether similar links may exist for the diverse practices outlined above. Furthermore, no research has thus far attempted to estimate the prevalence of these activities.A large-scale survey of a representative sample of UK adults (n=1081) was therefore conducted in order to investigate these issues. Engagement in all measured forms of gambling-like video game practices were significantly associated with both problem gambling and disordered gaming. An aggregate measure of engagement was associated with both these outcomes to a clinically significant degree (r=0.23 and r=0.43). Engagement in gambling-like video game practices appeared widespread, with a 95% confidence interval estimating that 16.3% – 20.9% of the population engaged in these activities at least once in the last year. Engagement in these practices was highly inter-correlated: Individuals who engaged in one practice were likely to engage in several more.Overall, these results suggest that the potential effects of the blurring of lines between video games and gambling should not primarily be understood to be due to the presence of loot boxes in video games. They suggest the existence of a convergent ecosystem of gambling-like video game practices, whose causal relationships with problem gambling and disordered gaming are currently unclear but must urgently be investigated.

**ИИ:** + · обе модели · беттеры + инструмент · Representative UK adult survey that measured esports betting and problem gambling, so it could report problem gambling among esports bettors.

**Решение:** =

---

### 942 · R4970

**Can Your Neighborhood Bookie Compete With the Internet ?**

2018

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: No abstract; the title points to the economics of competition between illegal bookies and online sportsbooks, not a problem-gambling survey.); Sonnet ? (нет аннотации: No abstract; the title suggests illegal bookmaking versus online sports betting. It could be an economic or policy piece, but a survey isn't ruled out.)

**Решение:** -

---

### 943 · R4974

**The role of structural assurance on previous satisfaction, trust and continuance intention: The case of online betting**

2018 · review

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: An information-systems study of trust, satisfaction and continuance intention among online bettors; nothing suggests a problem-gambling instrument was used.); Sonnet ? (нет аннотации: No abstract; likely a survey of online bettors on trust and continuance intention, with problem-gambling measurement unlikely but unverified.)

**Решение:** ?

---

### 944 · R4984

**Gambling Participation, Expenditure and Risk of Harm in Australia, 1997-1998 and 2010-2011.**

2018 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-017-9708-0

Gambling-related harm results primarily from financial losses. Internationally Australia continues to rank as the largest spending nation per capita on gambling products. This would suggest that Australian gamblers are at disproportionately high risk of harm despite almost two decades of industry scrutiny and regulation, and investment in research, treatment and education programs. However, declines in participation rates, per capita expenditure, household expenditure, national disposable income spent on gambling and problem gambling rates have been cited as evidence that fewer people are gambling, that gamblers are spending less, and that gambling safety in Australia has improved. The current study investigated these propositions using national population and accounts data, and statistics from Australia's two population-representative gambling surveys conducted in 1997-1998 and 2010-2011. Despite a falling participation rate the study found no real change in the number of people gambling overall, and increasing numbers consuming casino table games, race wagering and sports betting. Further found were increases rather than decreases in average gambler expenditure, overall, and across most products, particularly electronic gaming machines (EGMs). Potentially risky levels of average expenditure were observed in both periods, overall and for race wagering, casino table gaming, and EGMs. Changes in the proportion of income spent on gambling suggest risks declined overall and for race wagering and casino table gaming, but increased for EGMs. Finally, while problem gambling statistics were not comparable between periods, the study found double the number of moderate risk gamblers previously estimated for 2010-2011 amongst the 2 million Australians found to have experienced one or more gambling-related problems. The findings have implications for public health policy and resourcing, and the way in which prevalence and expenditure statistics have been interpreted by researchers, government and industry in Australia and elsewhere.

**ИИ:** разошлись — Opus ? (другое: Secondary analysis of Australian national gambling surveys covering sports betting participation and problem gambling; full text may report problem gambling by activity.); Sonnet + (опрос населения об азартных играх: Secondary analysis of two Australian national gambling surveys covering participation by activity (incl. sports betting) and problem gambling/risk; activity-level PG figures likely.)

**Решение:** ?

---

### 945 · R4985

**The nature of high risk investing: risky business or gambling?**

2018 · Adelaide Research & Scholarship (AR&S) (University of Adelaide) · dissertation · en

This thesis seeks to understand the theoretical and empirical relationship between gambling and financial market speculation. More specifically, are there fundamental conceptual differences between engaging in traditional forms of gambling, such as sports betting and electronic gambling machines, and engaging in speculative activities on the financial markets such as day trading and penny stocks? And, regardless of whether conceptual differences exist, a) To what extent do traditional gamblers engage in financial market speculation and vice versa?, and b) What individual differences, if any, predict engagement in one but not the other? In a series of four studies this thesis documents that gambling is conceptually distinct from investment, but that financial speculation is conceptually intermediate between gambling and investment. Consistent with the conceptual overlap between gambling and speculation, the studies within this thesis show there to be a strong empirical relationship at both the population level and individual level between these two activities. In general, the large majority of speculators also appear to engage in traditional forms of gambling, particularly skill-based formats. An important reason for this overlap is that skill-based gambling and speculation are very similar to each other. Because of the similarity in their nature, they tend to attract similar types of people. A central feature of both gamblers and speculators is having a propensity for taking risk, and secondarily, having an excitement-seeking orientation. Speculators and skill-based gamblers also both share cognitive biases of overconfidence, a tendency to confirm rather than disconfirm beliefs, illusion of control, gravitation toward products with low participation costs and high potential returns, and being highly loss-averse. Although the large majority of speculators are involved in gambling, only a minority of gamblers are involved in financial speculation. The likely reason for this difference is likely that most skill-based gamblers do not perceive themselves to have the level of knowledge, experience, or income needed for financial speculation. Consistent with this contention, age, educational attainment, and income are the demographic variables that most strongly discriminate between speculators and gamblers.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Thesis with population and individual surveys covering gambling, including sports betting, and speculation; whether problem gambling was measured is unclear.

**Решение:** =

---

### 946 · R4989

**Gender differences in gambling preferences and problem gambling: a network-level analysis**

2018 · International Gambling Studies · article · en · https://doi.org/10.1080/14459795.2018.1495750

ABSTRACT Most gambling studies have a gender-blind research approach, although a large body of scientific evidence suggests that gambling in females is on the rise and that males and females have different gambling behaviours and experience specific gambling-related harm. This study addressed these gender differences using a network analysis, an innovative approach considering disorders/concepts as dynamic systems of interacting symptoms/items. Data on gambling activities, problem gambling, substance use and mental health were collected in a representative sample of French adult gamblers (n = 8805). The study capitalized on the network analysis directly to compare associations of specific gambling activities with gambling disorder symptoms separately for both genders. The network analysis revealed that problem gambling was strongly associated with gambling machines among females, whereas it was related to sports betting, poker and casino games among males. The networks that included substance use and mental health showed that substance use was related to specific gambling activities. These findings confirm the links between various gender-specific gambling patterns and problem gambling and suggest a need to consider these gender differences to improve prevention efforts. More broadly, the present study further supports the importance of gender differences for gambling research and policy.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · A representative French sample of gamblers that measured both sports betting and problem gambling, and analysed problem-gambling symptoms by gambling activity.

**Решение:** =

---

### 947 · R4992

**EFFECTS OF GAMBLING ADVERTISING ON SPORTS BETTING BEHAVIOUR (UG&amp;SA)**

2018 · Unpublished · presentation, text/presentation · en · https://doi.org/10.13140/rg.2.2.18379.49447

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Presentation with no abstract about advertising and sports betting behaviour; may involve a bettor survey that includes a problem-gambling measure.

**Решение:** =

---

### 948 · R5001

**Prevalence of Pathological Gambling among Alcohol Addicts in Outpatient Treatment in the City of Zagreb: a Cross-Sectional Study.**

2018 · Psychiatria Danubina · article, journal article, journalarticle · eng · https://doi.org/10.24869/psyd.2018.348

BACKGROUND: Various types of addictions often co-occur, particularly substance and behavioral ones, which affects the clinical course of mental health disorders as well as the efficacy of therapy and rehabilitation efforts. The present study aims to explore gambling activities and possible gambling addiction among alcoholics in an outpatient treatment in the city of Zagreb. SUBJECTS AND METHODS: Gambling activities were assessed in 140 members of alcohol addiction clubs in the City of Zagreb (Croatia). Participants were undergoing treatment after being diagnosed by their psychiatrist with alcohol dependence syndrome based on ICD-10 criteria. Intensity of gambling-related problems was measured using the South Oaks Gambling Screen (SOGS), while intensity of alcohol addiction was assessed using DSM-5 diagnostic criteria for alcohol use disorder. All instruments were self-report forms and were completed using pen and paper in a group context during outpatient treatment. RESULTS: Pathological gambling was more prevalent in this clinical subsample than in general populations analysed in other studies. Alcohol addicts showing problematic or pathological gambling behaviors tended to play more highly addictive games (sports betting, slot machines, roulette). However, intensity of gambling-related problems did not correlate significantly with the intensity of alcohol addiction. CONCLUSION: These results confirm studies from other countries showing higher prevalence of problematic and pathological gambling among alcohol addicts than in the general population. Gambling behavior in our sample more often involved games with greater addictive potential. These findings suggest that alcohol addicts should be systematically screened for problematic and pathological gambling, which may improve therapeutic efficacy and rehabilitation, as well as reduce relapse in addictive behavior in general.

**ИИ:** разошлись — Opus + (игроки, есть ставки на спорт и инструмент: Alcohol-treatment sample (not recruited for gambling problems); SOGS measured alongside gambling activities including sports betting.); Sonnet ? (другое: Alcohol-treatment sample (not recruited for gambling) with SOGS and game types including sports betting; full text may give PG among sports bettors.)

**Решение:** ?

---

### 949 · R5003

**Overconfidence and the conjunction fallacy in sports betting behaviour**

2018 · Cross Connect (Southern Cross University) · dataset/dataset, dataset · en · https://doi.org/10.4226/47/5ad57a1d6dbb1

Respondents were asked whether or not they would bet on the outcomes of eight single pairs of NRL matches. Sports betting behaviour, gambling consumption, overconfidence and other demographics were also obtained.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Dataset from a survey of NRL sports betting behaviour; "gambling consumption" may include a problem-gambling screen, which is not stated.

**Решение:** =

---

### 950 · R5006

**Facing temptation: The neural correlates of gambling availability during sports picture exposure.**

2018 · Cognitive, affective & behavioral neuroscience · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.3758/s13415-018-0599-z

Nowadays, sports betting has become increasingly available and easy to engage in. Here we examined the neural responses to stimuli that represent sporting events available for betting as compared to sporting events without a gambling opportunity. We used a cue exposure task in which football (soccer) fans (N = 42) viewed cues depicting scheduled football games that would occur shortly after the scanning session. In the "betting" condition, participants were instructed to choose, at the end of each block, the game (and the team) they wanted to bet on. In the "watching" condition, participants chose the game they would prefer to watch. After the scanning session, participants completed posttask rating questionnaires assessing, for each cue, their level of confidence about the team they believed would win and how much they would enjoy watching the game. We found that stimuli representing sport events available for betting elicited higher fronto-striatal activation, as well as higher insular cortex activity and functional connectivity, than sport events without a gambling opportunity. Moreover, games rated with more confidence towards the winning team resulted in greater brain activations within regions involved in affective decision-making (ventromedial prefrontal cortex), cognitive inhibitory control (medial and superior frontal gyri) and reward processing (ventral and dorsal striatum). Altogether, these novel findings offer a sensible simulation of how the high availability of sports betting in today's environment impacts on the reward and cognitive control systems. Future studies are needed to extend the present findings to a sample of football fans that includes a samilar proportion of female and male participants.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · fMRI study of football fans who may bet; the sample description may include a problem-gambling screen, but the abstract doesn't mention one.

**Решение:** =

---

### 951 · R5014

**Irrational Beliefs and Social Adaptation of Online Sports Gamblers According to Addiction Level: A Comparative Study**

2018 · Sustainability · article, review · en · https://doi.org/10.3390/su10114314

The purpose of this study is to analyze the differences in psychological characteristics (i.e., irrational beliefs) and social adaptation according to a participant’s level of addiction to online sports gambling (i.e., non-problem, low-risk, moderate-risk, and high-risk gamblers). A survey was completed by participants of online sports gambling, aged 19 years or older; 291 completed questionnaires were obtained and analyzed using multivariate analysis of variance (MANOVA). As results of this study, according to the level of addiction to online sports gambling, there were significant differences on people’s mental state and social adaptation. Specifically, the more people are attached to a group that is exposed to high gambling addiction risk, the more they tend to become irrational while gambling, adopt an overconfident viewpoint, and overestimate their techniques. Moreover, as addiction to online sports gambling worsens, adaptation problems begin to appear in their work and family lives. This study demonstrated that people who are addicted to online sports gambling tend to find difficulties in thinking reasonably and logically and struggle to lead normal lives. By raising awareness on online sports gambling addiction, this study could suggest a way out of the difficulty.

**ИИ:** + · обе модели · беттеры + инструмент · Survey of 291 online sports gamblers, grouped as non-problem, low-, moderate- and high-risk gamblers (PGSI-like categories).

**Решение:** =

---

### 952 · R5025

**The Comorbidity of Gambling Disorder among Macao Adult Residents and the Moderating Role of Resilience and Life Purpose**

2018 · International Journal of Environmental Research and Public Health · article · en · https://doi.org/10.3390/ijerph15122774

Macao, China’s only city with legalized casinos, has maintained a high prevalence of gambling participation and gambling disorder (GD) over the past decade. The mental health risks associated with such high levels have been overlooked. In order to estimate the comorbid prevalence of GD with depression, anxiety, and Internet gaming disorder (IGD) and to explore the potential buffering effect of psychological resilience and purpose in life, this study obtained a representative adult Chinese sample (N = 1000, 44% male, aged 18–97 years) from a telephone survey conducted between October and November of 2016. As hypothesized, the highest psychiatric comorbid prevalence was observed in the GD subgroup (n = 19, 21.1% probable IGD, 26.3% probable depression, and 37.0% probable anxiety). All these mental health problems could increase one’s proclivity to GD, and vice versa. Psychological resilience was found to buffer the association between anxiety symptoms and probable GD (χ2(1) = 4.30, p = 0.04/GD symptoms, Fchange (1,162) = 6.29, p = 0.01), whereas purpose in life did not display any hypothesized moderating effect. These results indicate the usefulness of mental health screening for GD, taking into consideration its associated risks, and of fostering psychological resilience in prevention and treatment programs.

**ИИ:** разошлись — Opus ? (неясно, есть ли ставки на спорт: Representative Macao adult telephone survey measuring gambling disorder; unclear whether participation by gambling activity, including sports betting, was recorded.); Sonnet + (опрос населения об азартных играх: Representative Macao telephone survey measuring gambling disorder; likely reports gambling activity participation, so sports betting figures may appear in full text.)

**Решение:** ?

---

### 953 · R5026

**Effects of sports betting on youth economic development in Kalerwe trading center in Uganda**

2018 · dissertation · en

A Research Project Submitted to the School of Humanities and Social Science Fulfillment of the Requirement for the Award of a Bachelor’s Degree in Development Peace and Conflict Studies

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Bachelor's dissertation, probably surveying young sports bettors on economic effects; no real abstract, so whether a problem-gambling screen was used is unknown.

**Решение:** =

---

### 954 · R5029

**A national survey of online gambling behaviours.**

2018 · Irish journal of psychological medicine · article, journal article, journalarticle · eng · https://doi.org/10.1017/ipm.2017.64

OBJECTIVES: The aim of this study is to look at an Irish population in relation to the online gambling activities people are engaging with, the reasons for gambling online, their attitudes to online gambling and the financial/mental health consequences of online gambling. METHODS: The outline for this study was adapted from a study by McCormack et al. (2014) in relation to online gambling, with the aim of replicating this study in an Irish population. An online survey consisting of 11 categories related to online gambling was advertised online over a 7-month period. Participants answered on activities gambled online, devices used, duration of time gambling, as well mental health/financial consequences of their gambling. RESULTS: A total of 208 users participated in the online survey. The most popular gambling activity played was Sports Betting (26.9%) and the most commonly used device was Mobile app (68.6%). The main reason for gambling online was 'To win money' (84.6%), the main reason for ending gambling sessions - 'Had something else to do' (67.3%) and the most prominent emotion experienced - Excitement (60.6%). There were findings related to the severity of gambling addiction (75% - had to borrow or sell to fund gambling) and their attitudes towards online gambling (strongly agreed - 39.9% - The potential dangers of gambling should be advertised). CONCLUSIONS: Online gamblers in Ireland share similar behavioural profiles to online gamblers in the United Kingdom and worldwide. The majority of participants in this research have been adversely affected from both a mental and financial perspective due to their gambling behaviours.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Online gambler survey measured sports betting; severity items reported, but unclear whether a validated instrument (e.g., PGSI) was used.

**Решение:** =

---

### 955 · R5032

**Fantasy Sports: Follow up on synergies between professional sports clubs and eSport**

2018 · article · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -6 (не про азартные игры или «ставка/лотерея» в другом смысле: No abstract; title points to a sports-business paper on club–esport synergies, not a survey measuring problem gambling.); Sonnet ? (нет аннотации: No abstract; title on fantasy sports and eSport clubs is likely a business or commentary piece, but could involve a survey of players.)

**Решение:** ?

---

### 956 · R5033

**Where Lies the Harm in Lottery Gambling? A Portrait of Gambling Practices and Associated Problems**

2018 · Journal of Gambling Studies · article · en · https://doi.org/10.1007/s10899-018-9761-3

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; likely French population-survey analysis of lottery gamblers with PGSI, may report sports betting participation alongside lottery play.

**Решение:** =

---

### 957 · R5045

**Gambling problems and the impact of family in UK armed forces veterans**

2018 · Journal of Behavioral Addictions · article · en · https://doi.org/10.1556/2006.7.2018.25

Background and aims International evidence indicates elevated problem gambling rates in armed forces veterans compared with the general population. Gambling problems adversely impact one's family, and family-related variables may increase vulnerability to gambling-related harm. Little is known, however, about gambling problems in the United Kingdom (UK) veterans or to what extent family variables, such as parenting history and experience of domestic violence, influence veterans' gambling. Methods We compared veterans (n = 257) and sex- and age-matched controls (n = 514) drawn from the 2007 Adult Psychiatric Morbidity Survey on gambling, financial management, domestic violence, childhood parental presence, and experience of stressful life events. Veterans who left the military before or after 4 years of service were compared. Results Problem gambling was significantly more prevalent in veterans (1.4%) than non-veterans (0.2%), and the impact of gambling problems on the family was specific to male veterans, particularly those who had experienced a traumatic event after the age of 16, and those who were more likely to have been physically attacked by their partner. Overall, this study revealed that the UK armed forces veterans report a higher prevalence rate of problem gambling compared with non-veterans, with potential negative impact on family life.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Veterans vs matched controls from the APMS 2007 population survey, with problem gambling measured; unclear whether sports betting participation was reported.

**Решение:** =

---

### 958 · R5050

**Fantasy Millionaires: Identifying At-Risk Consumers Based on Motivation**

2018 · Journal of Sport Management · article · en · https://doi.org/10.1123/jsm.2018-0164

The daily fantasy sports (DFS) industry came under heavy criticism for marketing messages focused on the potential for financial gain despite overwhelming evidence that only a small percentage of participants were actually winning money. Under pressure, many DFS websites are shifting their focus toward the activity’s entertainment value. The purpose of the current study is to determine if participants exhibit cognitive and behavioral differences based on their reason for playing. In this study, a sample of DFS participants was segmented based on intrinsic (entertainment) and extrinsic (financial gain) motivation scores. Once separated, cognitive and behavioral contrasts were drawn. The results indicated those individuals motivated by financial gain were more similar to problem gamblers cognitively, yet those intrinsically motivated spent more time and money on the activity. Given the changing legal status of sports betting in the United States, managers and policymakers should carefully consider the risks associated with DFS participation.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of DFS participants comparing them with problem gamblers cognitively; unclear whether a problem-gambling screen was used or only cognitions.

**Решение:** =

---

### 959 · R5054

**Daily Fantasy Football and Self-Reported Problem Behavior in the United States.**

2018 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-017-9720-4

Traditional, season-long fantasy sport participation has grown considerably since the late 1990s, and in an attempt to capitalize on this growing demand, daily fantasy sports (DFS) providers have created a new game where money changes hands instantly. This change has led some legal commentators and state agencies to believe the game is a form of Internet gambling similar to online poker, blackjack, and sports wagering, and thus, it requires increased regulation or even prohibition. Little is known, however, about the gambling behavior associated with DFS participation. Thus, the purpose of the current study was to examine problem gambling severity in conjunction with DFS participant motives, perceptions, and consumption behavior. Over 500 DFS participants were surveyed, and the results suggest DFS participants behave similarly with participants in other forms of gambling activities. In addition, the findings suggest additional consumer protections may be needed to prevent further problem behavior such as chasing.

**ИИ:** + · обе модели · беттеры + инструмент · Survey of over 500 daily fantasy sports participants that examined problem gambling severity.

**Решение:** =

---

### 960 · R5055

**Daily Grind: A Comparison of Causality Orientations, Emotions, and Fantasy Sport Participation.**

2018 · Journal of gambling studies · article, comparative study, journal article · eng · https://doi.org/10.1007/s10899-017-9684-4

In 2015, daily fantasy football entered the fantasy sports market as an offshoot of the traditional, season-long form of the game. With quicker payouts and less commitment, the new activity has drawn comparisons to other forms of illegal gambling, and the determination of whether it is a primarily a game of skill or chance has become the center of the comparison. For the most part, legal commentators and society, in general, views traditional, season-long fantasy football as an innocuous, social activity governed equally by both skill and chance. Little evidence exists, however, about participant perception of skill and chance components in daily fantasy football. The current study surveyed 535 daily and traditional-only fantasy football participants in order to understand differences and similarities in the causality orientations of participation (skill or chance). In addition, enjoyment and anxiety were tested for mediating effects on causality orientations and consumption behavior. The results suggest the differences between the activities are not extreme. However, differences were found in which causality orientations influenced enjoyment and which emotion mediated the relationship between perceived skill and consumption.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of 535 daily/traditional fantasy football players; measures skill/chance perceptions and emotions; no problem-gambling instrument mentioned.

**Решение:** =

---

### 961 · R5063

**La influencia de la publicidad comercial en la conducta de riesgo en las apuestas deportivas: Recomendaciones para reguladores, operadores, instituciones y medios**

2018 · external research report · und · https://doi.org/10.13140/rg.2.2.23040.48645

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Research report on advertising and risky sports betting behaviour, no abstract; it may include a survey of bettors measuring problem gambling.

**Решение:** =

---

### 962 · R5068

**¿Entretenimiento, pasión o inversión? : comportamiento y perfil del público brasileño en las apuestas deportivas online**

2018 · Dipòsit Digital de Documents de la UAB (Universitat Autònoma de Barcelona) · dissertation · es

En la industria de apuestas en las dos últimas décadas se ha producido un enorme “boom” en términos de crecimiento no solo a nivel de actividad, sino también a nivel de presencia online y adhesión. Es, sin dudas, un mercado en ascenso, donde hay una gran inversión para desarrollo de tecnologías, marketing digital y publicidad en general. En el contexto de la evolución tecnológica en la que vivimos se crearon las condiciones necesarias para que el juego online se volviera más popular todavía y accesible a países donde no es permitida la instalación de Casas de Apuestas o Casinos.\nSi bien el mercado se muestre con un potencial de crecimiento gigante en toda Latinoamérica, en Brasil las apuestas deportivas online todavía son un tema con muchas incógnitas, como la falta de reglamentación. Por otra vertiente las empresas de apuestas buscan alternativas para convertir la práctica para el mercado online posible y “driblear” este escenario. Para eso cada vez más se desarrollan más estrategias de marketing propias para acercarse al público y retenerlos.\nEste producto, que es 100% online, se muestra cada vez más relevante enel mercado brasileño, pero todavía son escasos los estudios académicos, tanto sobre el mercado, cuanto sobre el público. Con eso, hay muchas premisas interesantes que se pueden ser abordadas acerca del sector, aprovechando que el mercado en Latinoamérica, diferentemente del europeo, está en proceso de maduración y todavía hay mucho a explorar. Considerando que el público brasileño es apasionado por los deportes y tiene características distintas por actuar muchas veces llevados por su emoción, en este estudio buscamos identificar si este factor influye en su performance en las apuestas deportivas. Queremos identificar si el público tiene un perfil orientado hacia el consumo de acuerdo con su preferencia y gusto por el deporte, o un perfil más de inversor, profesional, en el que el único objetivo es el retorno financiero. Con eso buscamos entender mejor los matices de este público tan emblemático para contribuir en el desarrollo de estrategias de marketing innovadores y eficaces.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Marketing thesis profiling Brazilian online sports bettors, probably through a survey; the abstract does not say whether problem gambling was measured.

**Решение:** =

---

### 963 · R5069

**Gambling motivation: comparisons across gender and preferred activity**

2018 · International Gambling Studies · review, article · en · https://doi.org/10.1080/14459795.2018.1505936

ABSTRACT People gamble for emotional, social and monetary reasons. However, it remains unclear whether the relationships between these distinct aspects of gambling motivation and gambling behaviour hold across gender and types of gambling. Thus, the current study compared gambling motivation across different subgroups while taking into account problem gambling severity. A total of 4945 adults were recruited as part of the Northern Territory (Australia) population gambling survey. Of the full sample, 1207 participants (52% female) completed the Gambling Outcomes Expectancies Scale to assess gambling motivation. This subsample comprised those who scored one or more on the PGSI (n = 407) and a random sample of those who gambled at least once a year with a PGSI of zero (n = 800). The findings revealed excitement, escape and monetary expectancies increased in concert with gambling risk for both men and women, although only escape differentiated the low-risk and at-risk gamblers when other expectancies were controlled. In relation to differences across types of gambling, horse races/sports bettors rated excitement but not escape more favourably than lottery players. These findings suggest problem gambling severity should be considered when examining motivation difference by gender and that gambling motivation depends, in part, on preferred activity.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · NT population gambling survey with PGSI; compares by preferred activity including horse race/sports bettors, so PGSI by activity may be reported.

**Решение:** =

---

### 964 · R5077

**Prevalence, risk factors, and psychosocial adjustment of problematic gambling in adolescents: Results from two representative German samples**

2018 · Journal of Behavioral Addictions · article · en · https://doi.org/10.1556/2006.7.2018.37

Background and aims Gambling disorder is a significant public health concern. Especially, male minors have been shown to gamble in a problematic way, despite legal prohibitions. Methods We examined representative samples of students aged from 12 to 18 years (N = 9,309) in two German federal states to provide prevalence data and clinical description of risk factors for problematic gambling. Results We found that about 40% of the adolescents reported engaging in gambling activities within the past 12 months and found prevalence rates of 1.7% and 2.2% for problematic gambling. Especially, use of online gambling and slot machines was found to be related to problematic gambling. Male adolescents with a migration background were of higher risk for problematic gambling and psychopathological symptoms were significantly elevated among that group. Discussion The results indicate that participation in gambling activities is common among underaged adolescents and that prevalence of problematic gambling exceeds rates of adults. Similarly, problematic gambling is associated with increased psychopathological strain. Conclusion Given that a high proportion of adult gamblers report having started gambling in adolescents, our data emphasize the need for prevention and early intervention strategies for problematic gambling.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Representative adolescent survey with problem-gambling prevalence that relates gambling activities to problem gambling; sports betting likely among the activities.

**Решение:** =

---

### 965 · R5093

**Vorarlberger Suchtbericht 2018**

2018 · article · de

Der Vorarlberger Suchtbericht 2018 stellt aktuelle Entwicklungen in Bezug auf substanzgebundene und nicht substanzgebundene Suchte in Vorarlberg dar und liefert eine wichtige Grundlage fur Pravention, Therapie und Behandlung. Der Bericht wurde in Zusammenarbeit mit Expertinnen und Experten erarbeitet und beinhaltet erstmals auch eine Wastewater Analysis. Das Kompetenzzentrum Sucht der GOG analysierte im Kapitel „Epidemiologie mit Zahlen, Daten und Fakten“ die Situation hinsichtlich Alkohol, Tabak, illegaler Drogen, Psychopharmaka sowie Glucksspiel und Sportwetten und stellte sie in Bezug zur Lage in Osterreich insgesamt und in der EU.

**ИИ:** ? · обе модели · другое · Regional addiction report covering gambling and sports betting epidemiology; it may compile survey data on problem gambling among sports bettors.

**Решение:** =

---

### 966 · R5104

**DraftKings and the Future of Fantasy Sports**

2018 · article · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; title suggests a business or commentary piece on daily fantasy sports, but an empirical study can't be ruled out.

**Решение:** =

---

### 967 · R5106

**Does the uptake of wagering inducements predict impulse betting on sport?**

2018 · Journal of behavioral addictions · article, journal article, journalarticle · eng · https://doi.org/10.1556/2006.7.2018.17

Background and aims Marketing inducements for addictive products, such as wagering, can prompt impulse purchasing by triggering consumption reminders, urges, and cravings. Wagering inducements incentivize betting by providing bonus bets, money-back guarantees, deposits into betting accounts, and discounts. Their promotion during sporting events, push marketing efforts directed at consumers, and ease of uptake at the point-of-sale, may trigger betting on impulse. This study examined whether the uptake of wagering inducements predicted impulse betting on sport. Methods Australian sports bettors ( N = 1,813) completed an online survey measuring their proportion of planned bets, impulse bets before match commencement, and impulse bets during play; frequency of using wagering inducements; and several psychological, behavioral, and demographic variables. Results More frequent users of wagering inducements had a greater tendency to place impulse in-play bets, which were also predicted by problem gambling, higher buying impulsiveness, higher frequency of watching sports, younger age, and higher educational status. Sports bettors with a greater tendency to place impulse bets before match commencement also tended to have higher buying impulsiveness and to be younger, but they used inducements less frequently, and tended to be female, less-educated and non-problem, moderate risk, or problem gamblers. Discussion and conclusions Uptake of wagering inducements appeared to be particularly effective in stimulating impulse in-play betting among problem gamblers and frequent sports viewers. These results suggest that a more cautious approach to the regulation of both in-play bets and wagering inducements may be required to better protect young adults from gambling problems and harm.

**ИИ:** + · обе модели · беттеры + инструмент · Survey of 1,813 Australian sports bettors that reports PGSI categories (non-problem, moderate risk, problem gamblers).

**Решение:** =

---

### 968 · R5107

**On the Spur of the Moment: Intrinsic Predictors of Impulse Sports Betting.**

2018 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-017-9719-x

Betting on impulse, without thoughtful consideration, research or informed decision-making, may cause financial and other harms and lead to the development of gambling problems. Impulse betting undermines responsible consumption of gambling because it reflects self-regulatory failure, impaired control, unreflective decision-making and betting more than planned. In this paper we define impulse gambling and report on a study that aimed to understand more about the intrinsic characteristics of sports bettors who have a greater tendency to bet on impulse. Specifically, the study aimed to identify behavioural, psychological and socio-demographic predictors of impulse sports betting. A sample of 1816 Australian sports bettors completed an online survey that measured the proportion of their bets placed on impulse both before and during sporting events, as well as bets that were researched and planned in advance. Impulse betting was common, accounting for nearly one-half of all past-year sports bets by respondents. Over three-quarters of respondents had placed one or more impulse bets in the last year and one in seven respondents had made all of their sports bets on impulse. More impulsive sports bettors were characterised as having higher trait impulsiveness, higher problem gambling severity, more frequent sports betting and a shorter history of sports betting. They favoured betting on in-match contingencies instead of overall match outcomes. While health promotion strategies are needed to discourage impulse betting, research into contextual factors that arouse urges to bet would also provide direction for harm minimisation measures that help consumers to resist impulsive betting decisions.

**ИИ:** + · обе модели · беттеры + инструмент · Survey of 1816 Australian sports bettors that measured problem gambling severity (probably PGSI) as a predictor.

**Решение:** =

---

### 969 · R5112

**Online Betting System**

2018

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: No abstract; the title points to a software/system design project rather than a survey measuring problem gambling.); Sonnet ? (нет аннотации: No abstract; the title suggests a software or system description, but a survey of online bettors can't be ruled out.)

**Решение:** ?

---

### 970 · R5113

**Association of problem gambling with psychosocial characteristics among undergraduate students in Astana, Kazakhstan**

2018 · Nazarbayev University Repository (Nazarbayev University) · dissertation · en

Background. The prevalence of probable pathological gamblers among college students worldwide doubled in 15 years. While gambling addiction causes financial and social losses, there is lack of studies on gambling involvement in Kazakhstan. Aims. The current research aims to find the prevalence of gambling, explore the link with sociodemographic and psychological variables among college and university students is Astana, Kazakhstan. The study also aims to evaluate the association between gambling and school satisfaction, which was not reported before. Methods. The analysis included questionnaires of 399 students from three universities and three colleges in Astana, using random sampling. The survey consisted of demographic questions, and scales on anxiety and depression, alcohol use, school satisfaction, family cohesion and suicide ideation. Results. From 399 questionnaires analyzed, 5.76% were classified as pathological gamblers according to the gambling scale used. The most popular gambling type was betting on sport events with bookmakers. 12.4% reported placing a bet through bookmakers at present time, and of them 91.5% were male, around half (46.8%) were categorized as some-problem gamblers, and one-third (36.1%) as pathological gamblers. Two-third of them (66%) did not reach legal age for gambling. Pathological gamblers in comparison with non-gamblers/non-problem gamblers are more likely to be male, aged older than 21, have alcohol use disorders, have lower family cohesion, more frequent suicide ideation, and their fathers have no after school education. Some-problem gamblers in comparison with non-gamblers/non-problem gamblers are more likely to be male, have lower school satisfaction, show symptoms of depression, and do not combine work and study. Conclusions. The study gives the first overview for gambling problem and associated problems among undergraduate students in Astana. Associates of problem gambling is consistent with the literature. Since every fourth male in the study places a bet with bookmakers, and majority had a gambling problem, there is need for developing interventions to increase awareness and prevent problem gambling and associated psychosocial problems.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Student survey reports problem/pathological gambling rates among current bookmaker sports bettors; gambling scale classified pathological gamblers.

**Решение:** =

---

### 971 · R5116

**I think, therefore I am… thinking? Fast and slow information processing within sports betting.**

2018 · Frontiers in Psychology · article, journal-article · en · https://doi.org/10.3389/conf.fpsyg.2018.74.00009

Frontiers Events is a rapidly growing calendar management system dedicated to the scheduling of academic events. This includes announcements and invitations, participant listings and search functionality, abstract handling and publication, related events and post-event exchanges. Whether an organizer or participant, make your event a Frontiers Event!

**ИИ:** ? · обе модели · нет аннотации · The abstract is generic Frontiers Events text. The title points to an empirical study of cognition in sports bettors that may have measured problem gambling.

**Решение:** =

---

### 972 · R5119

**[Latent Class Analysis of Gambling Activities among Korean Adolescents].**

2018 · Journal of Korean Academy of Nursing · article, journal article, journalarticle · kor · https://doi.org/10.4040/jkan.2018.48.2.232

PURPOSE: The aim of this study is to identify the types of gambling among adolescents and provide basic prevention information regarding adolescents' gambling problems. METHODS: Secondary data from representative national survey on 2015 Youth Gambling Problems of Korea Center on Gambling Problems were used. Using latent class analysis (LCA), 13 gambling types such as offline and online games of 14,011 adolescents were classified, and gambling experiences and characteristics were analyzed. RESULTS: The subgroups of adolescent gambling were identified as four latent classes: a rare group (84.5% of the sample), a risk group (1.0%), an offline group (11.9%), and an expanded group (2.6%). The types and characteristics of gambling among the latent classes differed. In the risk group, adolescents participated in online illegal sports betting and internet casino, and gambling time, gambling expenses, and the number of gambling types were higher than other groups. CONCLUSION: Gambling frequently occur among adolescent, and the subtypes of gambling did not reveal homogeneous characteristics. In order to prevent adolescent gambling problems, it is a necessary to develop tailored prevention intervention in the nursing field, which is appropriate to the characteristics of adolescent gambling group and can help with early identification.

**ИИ:** разошлись — Opus + (опрос населения об азартных играх: National Korean youth gambling problems survey (n=14,011) covering online sports betting; it likely used a problem-gambling screen such as CAGI.); Sonnet ? (неясно, измеряли ли проблемную игру: National Korean adolescent gambling survey including sports betting; abstract doesn't say whether a problem-gambling instrument was used or reported by activity, so full text is needed.)

**Решение:** ?

---

### 973 · R5122

**A Study on the Improvement of the Structure of Sports Toto's Business Model and the Improvement Plan for Illegal Sports Betting and Elimination of the Game : With IPA Matrix Analysis**

2018 · 한국체육학회지 · article, other literature type, journal-article · en · https://doi.org/10.23949/kjpe.2018.01.57.1.18

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Policy/business-model study of Sports Toto using an importance-performance (IPA) attitude survey; a problem-gambling instrument is very unlikely.); Sonnet ? (нет аннотации: No abstract; Korean Sports Toto business model and illegal betting IPA analysis, likely a survey of stakeholders, probably no problem-gambling instrument, but unclear.)

**Решение:** ?

---

### 974 · R5124

**Researching Fantasy Sports Using Mixed- and Multi-Methods**

2018 · SAGE Publications Ltd eBooks · book, reference-book, reference-entry · en · https://doi.org/10.4135/9781526446244

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: SAGE methods case on fantasy sports research with no abstract; it could describe a survey of fantasy players, but a problem-gambling measure is uncertain.); Sonnet -1 (обзор, комментарий, теоретическая, правовая или регуляторная работа: Reference-book entry on research methods for fantasy sports (SAGE); no abstract, likely a methodological overview rather than an empirical prevalence study.)

**Решение:** ?

---

### 975 · R5126

**A Study on Participation of Illegal Sport Gambling by the Korean School Elite Sports Athletes**

2018 · 한국체육학회지 · article, journal-article · en · https://doi.org/10.23949/kjpe.2018.11.57.6.2

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; survey of Korean student athletes on illegal sports betting, so problem gambling may have been measured.

**Решение:** =

---

### 976 · R5131

**Comparisons by gender and school type in the association between betting games and problem gambling among adolescents**

2018 · review · https://doi.org/10.14400/jdc.2018.16.10.523

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; title suggests an empirical adolescent survey linking betting games to problem gambling despite 'Review' record type.

**Решение:** =

---

### 977 · R5132

**Does Legalized Gambling Industry Substitute Illegal Gambling?: A Case Study on Sports Betting**

2018 · Korea International Trade Research Institute · article, journal-article · en · https://doi.org/10.16980/jitc.14.1.201802.303

This study empirically analyzes whether legalized gambling is a substitute for or a complement to illegal gambling by conducting a case study on sports betting. For this purpose, we first estimate determinants of sales of legal sports betting (e.g., Sports Toto/Proto) and illegal sports betting with a time series econometric model. In addition, from cross-sectional data obtained from 1,000 participants of sports betting, we examine the impacts of increased competitiveness of legal sports betting on illegal sports betting. Through time series analysis, we find that legal and illegal sports betting have a substitute relationship, but the relationship is weak due to the relative competitiveness of illegal sports betting in areas including accessibility, variety of products, and odds of winning. Cross-sectional data analysis reinforces the findings of the time series analysis. That is, instituting measures to deregulate restrictions on legal sports betting such as allowing purchases on mobile phones, 24-hour purchases, and higher odds of winning would significantly increase its substitution effect. The results suggest that policy effectiveness can be enhanced by steering illegal gambling to the legal domain by improving competitiveness of legal gambling, contrary to the prevailing tendency to focus on regulatory and punitive measures.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Mostly economic analysis, but includes a survey of 1,000 Korean sports bettors; unclear whether a problem-gambling instrument was used.

**Решение:** =

---

### 978 · R5139

**Do sports bettors understand probability and take risks?**

2018 · Frontiers in Psychology · article, journal-article · en · https://doi.org/10.3389/conf.fpsyg.2018.74.00033

Frontiers Events is a rapidly growing calendar management system dedicated to the scheduling of academic events. This includes announcements and invitations, participant listings and search functionality, abstract handling and publication, related events and post-event exchanges. Whether an organizer or participant, make your event a Frontiers Event!

**ИИ:** ? · обе модели · нет аннотации · The abstract is Frontiers Events boilerplate. The title points to a study of sports bettors that may have measured problem gambling.

**Решение:** =

---

### 979 · R5144

**Spanish validation of the Problem Gambling Severity Index: A confirmatory factor analysis with sports bettors.**

2018 · Journal of behavioral addictions · article, journal article, validation study · eng · https://doi.org/10.1556/2006.7.2018.84

Background and aims The Problem Gambling Severity Index (PGSI) is one of the most widely used screening tools for problem gambling (PG). However, to date, no empirically validated adaptation of the instrument to Spanish-speaking countries exists. Methods A sample of 659 sports bettors ( M age = 35.1 years, SD = 10.12, 74.2% males) were recruited through an online research panel. A confirmatory factor analysis (CFA) was performed to confirm its construct validity. The participants were administered the Spanish version of the PGSI, along with the adaptation to Spanish of the DSM-IV PG instrument for convergent validity. Results The CFA of the Spanish PGSI showed satisfactory construct validity. The internal consistency (α ordinal = .97) as well as its convergent validity with the DSM-IV scores ( r = .77, p &lt; .001) was good. Conclusion The Spanish adaptation of the PGSI offers satisfactory validity and reliability properties, and is a good psychometric instrument for exploring the social consequences of PG in Spanish-speaking contexts.

**ИИ:** + · обе модели · валидация инструмента · Validation study of the Spanish PGSI in 659 sports bettors, using the PGSI and DSM-IV screens.

**Решение:** =

---

### 980 · R5146

**Romanian National Prevalence Study – problem and pathological gambling in children and adolescents**

2018 · Medicine and Pharmacy Reports · article · en · https://doi.org/10.15386/cjmed-1001

BACKGROUND AND AIMS: The purpose of the present study was to measure the prevalence of problem and pathological gambling in children and adolescents at a national level, given that previous studies at regional level had demonstrated high rates of prevalence. METHODS: After designing the sample (2006 children and adolescents aged 11-19 years) we used two validated instruments for measuring the prevalence of problem and pathological gambling in children and adolescents - South Oaks Gambling Screen -Revised for Adolescents (SOGS-RA) and 20 Questions of Gamblers Anonymous Revised for Adolescents (20 GA-RA). RESULTS: The following data have been found: gambling at risk is 7.1% and problem and pathological gambling is 4%, when results were analyzed by SOGS-RA; prevalence of problem gambling is 10.1% and pathological gambling is 2.6% when results were analyzed by 20 GA-RA. CONCLUSIONS: High rates of prevalence are noticed in Romania, similar to other European countries. This rates are based on self-reported questionnaires, meaning that real rates may be higher than reported, being known that children and adolescents tend to give socially expected response. An important issue is that we found pathological gambling at the age of only 11 years. Our results compared to those of other studies from Romania are very similar to those from other European countries.

**ИИ:** + · обе модели · опрос населения об азартных играх · National adolescent prevalence survey using SOGS-RA; activity participation including sports betting likely reported in full text.

**Решение:** =

---

### 981 · R5147

**In-Play Betting, Sport Broadcasts, and Gambling Severity: A Survey Study of Spanish Sports Bettors on the Risks of Betting on Sport While Watching It**

2018 · Communication & Sport · article, journalarticle, review · en · https://doi.org/10.1177/2167479518816338

Fans watching live sport events, both mediated or in stadia, have witnessed an increase in sports betting products. Most of these products feature in-play betting, that is, the ability to bet on a game once it has started while watching it. In-play betting has raised many concerns among responsible gambling advocates due to its perceived relationship with problem gambling behaviour. This study explored the association between in-play betting and problem gambling. More specifically, the study examined how motives for consuming sport and how involved sports fans were in watching sport affected their gambling. Also, adjacent risk behaviours to in-play betting (such as consuming junk food and alcohol) during live sports betting were examined. Using a survey comprising 659 sports bettors from Spain, the study found that compared to participants not engaging in in-play betting, in-play bettors reported higher (i) problem gambling severity, (ii) sport watching involvement, (iii) consumption of sport to escape from everyday preoccupations, and (iv) consumption of junk food and/or alcohol while watching sport. These findings make the case that in-play betting regulators and providers should be cognizant of the interplay of sport-specific, media-related, and other risks, involved in the act of in-play betting while watching live sport.

**ИИ:** + · обе модели · беттеры + инструмент · Survey of 659 Spanish sports bettors that measured problem gambling severity, most likely with the PGSI.

**Решение:** =

---

### 982 · R5148

**Internet-Based Structural Characteristics of Sports Betting and Problem Gambling Severity: Is There a Relationship?**

2018 · International Journal of Mental Health and Addiction · article, review, journal-article · en · https://doi.org/10.1007/s11469-018-9876-x

With the adoption and popularization of internet-based platforms, sports betting has introduced new functionalities that transform the design of its products and therefore the way bettors interact with them. This study aims to explore the association between the use of new structural characteristics of online betting and gambling severity. Five characteristics are examined here: (i) live in-play betting; (ii) cash out feature use (as example of in-play betting in-built features); (iii) fantasy sports gaming; (iv) location of betting; and (v) device or platform used to make bets. A cohort (N = 659) of Spanish gamblers who had bet on sports during the previous year was recruited through an online survey. The results suggested that those bettors scoring higher on gambling problems also utilized more often such new structural characteristics, in a proportion not explained only by their higher overall gambling activity. Mobile betting was especially frequent among problem gamblers.

**ИИ:** + · обе модели · беттеры + инструмент · Online survey of 659 Spanish past-year sports bettors that assessed problem gambling severity; the screening instrument is likely in the full text.

**Решение:** =

---

### 983 · R5151

**Trends in Gambling Behaviour among NCAA College Student-Athletes: A Comparison of 2004, 2008 and 2012 NCAA Survey Data**

2018 · International Journal of Sports and Exercise Medicine · review · https://doi.org/10.23937/2469-5718/1510096

Student-athletes represent a vulnerable subgroup of the college student population with regards to engagement in high-risk behaviours, including gambling. Three large samples of National Collegiate Athletic Association (NCAA) student-athletes in 2004 (N = 20,587), 2008 (19,942), and 2012 (N = 22,935) were surveyed about their gambling behaviour and attitudes. A cross-sectional study was conducted to gain insight into how the landscape of gambling and attitudes among college student-athletes has changed within the last eight-years in relation to the ongoing expansion of gambling opportunities. Findings revealed gender differences in participation rates of gambling with males consistently engaging in all gambling activities at higher rates than females (57% of males versus 39% females in 2012). Despite gender differences, the results suggested that participation rates for all gambling activities has decreased over the eight-year span (57% of student-athletes in 2012 compared to 70.7% of student-athletes in 2004), except for past year purchasing of lottery tickets, which increased in 2012 among males. Across sports, gambling participation was notably highest among golfers of both genders. The proportion of student-athletes at-risk or meeting criteria for a gambling problem between 2004 and 2012 has also decreased among males (4% in 2004 versus 1.9% in 2012) while remaining relatively consistent among females (< 1% across all years). Taken together, the results suggest that gambling behaviour among NCAA student-athletes is on a downward trend despite the increase in available gambling opportunities.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · NCAA athlete surveys measured gambling activities (likely sports wagering) and problem gambling criteria; empirical despite 'Review' label.

**Решение:** =

---

### 984 · R5153

**eSports, skins and loot boxes: Participants, practices and problematic behaviour associated with emergent forms of gambling**

2018 · Figshare · collection/collection · https://doi.org/10.25384/sage.c.4168025

Twenty years since the Internet transformed gambling products and services, the convergence of online games and gambling has initiated a new means of consuming Internet-based media. Gambling specifically connected to eSports is a significant development, not only offering a new avenue for existing gambling products to be inserted into gaming media but also affording several novel experiences (e.g. skins and loot boxes). This study assesses participation rates and demographic characteristics of eSports spectators who gamble via an international online survey ( N = 582). The sample highlighted the prevalence of young, often under-age, males in eSports-related gambling activities. Participation in gambling, and gambling-like activities, was found to be 67%, with rates of problematic and potentially problematic gambling in the sample being 50.34%. Finally, increased gambling is associated with increased spectating of eSports. Although the results are not generalisable to the wider population, they suggest a need for increased attention, from academia and regulators, regarding newly emergent gambling behaviours in contemporary digital culture.

**ИИ:** + · обе модели · беттеры + инструмент · Survey of eSports spectators who gamble, including eSports betting, reports rates of problematic gambling; figshare deposit judged by its article.

**Решение:** =

---

### 985 · R5154

**Obilježja roditeljstva i odnos roditelja prema kockanju kao prediktori kockanja muške djece**

2018 · University of Zagreb. University of Zagreb, Faculty of Education and Rehabilitation Sciences · doctoral thesis, dissertation · hr · https://www.bib.irb.hr/910922

The research of youth gambling in Croatia and the world have mostly been approached from a child's point of view. This dissertation, beside including child's perspective, includes parents’ personal characteristics through different way of assessment and self-assessment. The impact of parenthood on a negative child outcomes has been proven through many researches (Farrington, Loeber i Ttofi, 2007; Andrews i Bonta, 2006, Feric, 2002, Ricijas, 2012), as well as on gambling as a risky behaviour (Gupta i Derevensky, 1997; Dickson, Derevensky i Gupta, 2000, Wood i Griffiths, 2002; Griffiths, 2003), although literature holdings in this field are rather moderate and recent. The aim of this research is to provide an insight into characteristics of parenthood, particularly those related to relationship with youth gambling, parents’ attitudes toward gambling, frequency of parent gambling and the differences in perception between parents and their children. Moreover, the goal was to determine how those characteristics explain the frequency of their children’s gambling and the way in which child’s perception of parents and parenthood, and child’s personal characteristics, experiences and attitudes to gambling explain the frequency of their gambling. The important attribute of this research is that both, parents (n=244) and their male children (n=244) were involved, so comparison between parents’ perception and their children self-assessment could be done. Subsample of parents consists of n=126 mothers (51.6%) and n=118 fathers (48.4%). Parents’ age ranges from 30 to 63 with the average age Mage=45.98 (SDage=5.59). Age of boys ranges from 14 to 19, with the average age Mage=16 (SDage=1.21). The research was conducted on a convenience sample in Split and Zagreb. In order to conduct this research, a wide battery of instruments was used: (1) Questionnaire about general and socio- demographic data, (2) Questionnaire of risk perception for the youth, (3) Questionnaire of communication assessment about youth risks, (4) Questionnaire of assessment of the experiences of a child with risky behaviour, (5) Questionnaire of family interaction quality – KOBI (Vulic-Prtoric, 2002), (6) Questionnaire of parent behaviour URP-29 (Kuterovac Jagodic, Kerestes I Brkovic, 2007), (7) Gambling attitudes scale (Jelic, Huic I Dinic, 2013), (8) Questionnaire of gambling activities (shorten version): parents’ self-assessment, partners’ assessment, parents’ self- assessment about gambling with their child (Ricijas et all., 2011), (9) South Oaks Gambling Screen- SOGS (Lesieur and Bloom, 1987), (10) Questionnaire of child’s gambling activities (shorten version) (Ricijas et all., 2011), (11) General Problem Severity Subscale (GPSS) as a part of Canadian Adolescent Gambling Inventory- CAGI (Wiebe, Tremblay, Wynne and Stinchfield, 2010), (12) Questionnaire of self- assessment of probability of parents’ disciplining their children for risky behaviour and (13) Questions about whether they gamble together with their child. In order to reach the aforementioned goals, the following data analyses methodology was used: (1) Descriptive statistics (means, standard deviation, frequencies), (2) Wilcox range test, (3) Hi-square test, (4) Mann-Whitney U- Test with the calculation of effect sizes, and (5) Hierarchical regression analysis. The results of the research have shown that parents do not rank gambling that high as the risks related to psychoactive substances use and that they perceive gambling as a greater risk then their children do. When compared to communication with their children, parents communicate more often about substance use (alcohol, cigarettes, drugs) and other behavioural addictions, that is technological risks such as Internet and video games, rather than gambling and they assess their communication more frequent their children do. In relation with parents’ perception of type, frequency and consequences related to gambling, the results show that parents believe sport betting to be the most frequent with the children, but also children self-assessed to gamble more frequent then their parents think so. That difference is shown also in disciplining risky behaviour in a way that parents report to be more prone to disciplining the children, whereas the children do not have the same perception. As far as psychosocial consequences connected to gambling, 88.0% of parents assess that their children do not have any of the consequences, while 64.3% of their children think so. The total of 8.4% of parents assess low and medium level of the problem, while 21.6% of their male children is self-assessed to be in this range of the problem. Finally, 2.8% of parents assessed that their male children have serious psychosocial consequences related to gambling, while 14.1% of children self-assesses to suffer the consequences, which is significant. Related to differences between mothers and fathers, the results show that the fathers have a more positive attitude towards gambling, they gamble more often and have more developed problems connected to gambling. When questioning the contribution of parents’ personal characteristics, parenthood characteristics, parenting related to youth gambling, attitudes toward gambling, frequency and intensity of the problems related to parents gambling in prediction of self- expressed gambling frequency of their male children, the results demonstrate that the frequency of male children gambling cannot be described completely by parents’ self-assessment since only 20% of the variance is explained in that way. However, the set of predictors which measures, from child’s perspective, the assessment of family and parenthood, and also includes children’s self-expression and self-assessment of their attitudes and experiences while gambling, the results show that frequency of boys gambling can be explained through inadequate parenting styles which include restrictive control and permissiveness and parents’ knowledge about their children gambling, a child’s positive attitude toward gambling, experience of winning a great amount of money which motivates the child to gamble more, which explains about 59% variance of criterion.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Survey of male adolescents that measured gambling activities, including sports betting, and problem gambling with CAGI GPSS; parents were screened with SOGS.

**Решение:** =

---

### 986 · R5157

**Factors Influencing Online Betting Behavior in Nairobi**

2018 · dissertation · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Dissertation on online betting in Nairobi (likely sports betting); there's no abstract, so it's unclear whether problem gambling was measured.

**Решение:** =

---

### 987 · R5160

**Sports Betting: Attitudes and Behaviours among Children and Adolescents: Final Report**

2018 · Figshare · report · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; report on youth sports betting attitudes and behaviours may include a problem-gambling screen in the full text.

**Решение:** =

---

### 988 · R5162

**Women's gambling behaviour, product preferences, and perceptions of product harm: differences by age and gambling risk status.**

2018 · Harm reduction journal · article, journal article, multicenter study · eng · https://doi.org/10.1186/s12954-018-0227-9

BACKGROUND: Women's participation in, and harm from gambling, is steadily increasing. There has been very limited research to investigate how gambling behaviour, product preferences, and perceptions of gambling harm may vary across subgroups of women. METHODS: This study surveyed a convenience sample of 509 women from Victoria and New South Wales, Australia. Women were asked a range of questions about their socio-demographic characteristics and gambling behaviour. Focusing on four gambling products in Australia-casino gambling, electronic gambling machines (EGMs), horse betting, and sports betting-women were asked about their frequency of participation, their product preferences, and perceptions of product harms. The sample was segmented a priori according to age and gambling risk status, and differences between groups were identified using Chi-square tests and ANOVAs. Thematic analysis was used to interpret qualitative data. RESULTS: Almost two thirds (n = 324, 63.7%) of women had engaged with one of the four products in the previous 12 months. Compared to other age groups, younger women aged 16-34 years exhibited a higher proportion of problem gambling, gambled more frequently, and across more products. While EGMs were the product gambled on most frequently by women overall, younger women were significantly more likely to bet on sports and gamble at casinos relative to older women. Qualitative data indicated that younger women engaged with gambling products as part of a "night out", "with friends", due to their "ease of access" and perceived "chance of winning big". There were significant differences in the perceptions of the harms associated with horse and sports betting according to age and gambling risk status, with younger women and gamblers perceiving these products as less harmful. CONCLUSIONS: This study highlights that there are clear differences in the gambling behaviour, product preferences, and perceptions of product harms between subgroups of women. A gendered approach will enable public health researchers and policymakers to ensure that the unique factors associated with women's gambling are taken into consideration in a comprehensive public health approach to reducing and preventing gambling harm.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Women's survey measuring sports betting participation and gambling risk status (likely PGSI); could report problem gambling among sports bettors.

**Решение:** =

---

### 989 · R5163

**Beyond the Betting Shop: Youth, Masculinity and the Growth of Online Sports Gambling**

2018 · article · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; title fits online sports betting among youth but could be qualitative or a commentary. Full text needed.

**Решение:** =

---

### 990 · R5170

**Uso y abuso de las Tecnologías de la Información y la Comunicación por adolescentes: un estudio representativo de la ciudad de Madrid**

2018 · Universidad Camilo José Cela. Cátedra para el Desarrollo Social · book · esl/spa · http://hdl.handle.net/20.500.12020/839

La Cátedra para el Desarrollo Social de la Universidad Camilo José Cela (UCJC) y el Organismo Autónomo Madrid Salud del Ayuntamiento de Madrid han presentado el estudio ‘Uso y abuso de las Tecnologías de la Información y la Comunicación por adolescentes. Un estudio representativo de la ciudad de Madrid’ que tiene como resultado la gran prevalencia de problemas asociados al abuso de las TIC en esta población de adolescentes escolarizados. El estudio ha utilizado el MULTICAGE-TIC aplicado a una muestra de 2.341 estudiantes de 4º de la ESO (15 y 16 años) de centros educativos públicos, concertados y privados de la ciudad de Madrid. Se trata del primer estudio que analiza una muestra representativa –con bajo grado de error– de adolescentes escolarizados en una gran ciudad occidental para explorar el uso y abuso de las TIC y su relación con indicadores de salud mental. Los resultados apuntan a una gran prevalencia de problemas asociados al abuso de las TIC entre los adolescentes de 15 y 16 años. Según los resultados obtenidos, solo un 32% de los adolescentes hacen un uso adecuado de Internet, mientras que el 31,5% muestran señales de riesgo, un 23,3% mantienen una conducta de uso abusiva y un 13,2% muestran una clara dependencia comportamental en el uso de la red. En definitiva, más de un tercio de la muestra desarrolla un uso problemático de Internet y casi otro tercio está en riesgo de desarrollarlo. El estudio revela que más de la mitad de los adolescentes hacen un uso inadecuado del teléfono móvil: un 28,4% muestra un uso de riesgo, un 21% hace un uso abusivo y un 8% presenta dependencia de su smartphone. En cuanto al uso de Whatsapp, un 43,5% de los adolescentes presenta una conducta problemática en su uso. Concretamente, un 21% de los adolescentes muestra un uso de riesgo, un 14,5% un abuso y un 8% una dependencia. El estudio alerta de que el hecho de que casi la mitad de la muestra de adolescentes presente en mayor o menor grado un uso problemático de estas aplicaciones puede establecer patrones que persistan a lo largo del tiempo. Estos comportamientos tienen una relación directa con indicadores de mal aprovechamiento académico. En cuanto a las redes sociales, los adolescentes madrileños mostraron en casi un 40% un uso problemático: un 19% mostró un uso de riesgo, un 13% un abuso y un 7% una dependencia. En el caso de los videojuegos, un 24% de la muestra mostró un uso de riesgo, un 12,5% un abuso y el 5,7% una dependencia. El estudio evidencia diferencias entre los chicos y las chicas, ya que las adolescentes presentan puntuaciones de abuso o dependencia mucho más frecuentemente que los varones en todas las conductas problemáticas salvo en los videojuegos. El tamaño de las diferencias es muy considerable, especialmente en el uso de aplicaciones de mensajería instantánea y de redes sociales. Más del 90% de los participantes hacen uso de Whatsapp (un 96% de las chicas y un 92% de los chicos). La segunda aplicación más utilizada por los jóvenes es Youtube, con un 90% de las muestras y sin diferencias por sexo. En tercer lugar, Instagram es utilizado por el 87% de las chicas y significativamente menos por los chicos, un 74%. Lejos queda el uso de Snapchat, al que recurren más las chicas (71%) que los chicos (41%). Más de un 40% utiliza Spotify y menos de la tercera parte de la muestra hace uso de Spotify. Facebook y Twitter no evidencian un uso significativo por los adolescentes. El estudio concluye que, a mayor grado de uso problemático de las TIC, la puntuación en riesgo de mala salud mental es mayor. El incremento de los problemas asociados al uso y abuso de las TIC contribuye a la pérdida de control superior de la conducta. La inmadurez cerebral propia de la adolescencia es un importante factor de vulnerabilidad para la pérdida de control superior de la conducta. Sin embargo, estos factores solo explican una parte pequeña del abuso de las TIC, pues debe atenderse a variables no estudiadas como la presión de grupo, factores culturales o modas. El 5% de los adolescentes declara jugar con mucha frecuencia en webs de apuestas deportivas y casi un 12% lo ha hecho en alguna ocasión. Éste es un problema mayoritariamente de los adolescentes varones. El 4% de los adolescentes afirma contar con el permiso de sus padres cuando gasta dinero en Internet y un 15% dice hacerlo sin su consentimiento. La Cátedra para el Desarrollo Social de la Universidad Camilo José Cela (UCJC) y el Organismo Autónomo Madrid Salud del Ayuntamiento de Madrid

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Representative adolescent survey measured sports betting website use; MULTICAGE-TIC targets ICT abuse, and it is unclear whether any problem-gambling screen was used.

**Решение:** =

---

### 991 · R5176

**Prevalence of youth gambling and potential influence of substance use and other risk factors throughout 33 European countries: first results from the 2015 ESPAD study**

2018 · Addiction · article · en · https://doi.org/10.1111/add.14275

BACKGROUND AND AIMS: Although generally prohibited by national regulations, underage gambling has become popular in Europe, with relevant cross-country prevalence variability. This study aimed to estimate the prevalence of underage gambling in Europe stratified by type of game and on-/off-line mode and to examine the association with individual and family characteristics and substance use. DESIGN: Our study used data from the 2015 European School Survey Project on Alcohol and Other Drugs (ESPAD) cross-sectional study, a survey using self-administered anonymous questionnaires. SETTING: Thirty-three European countries. PARTICIPANTS: Sixteen-year-old-year-old students (n = 93 875; F = 50.8%). MEASUREMENTS: The primary outcome measure was prevalence of past-year gambling activity. Key predictors comprised individual behaviours, substance use and parenting (regulation, monitoring and caring). FINDINGS: A total of 22.6% of 16-year-old students in Europe gambled in the past year: 16.2% on-line, 18.5% off-line. High prevalence variability was observed throughout countries both for mode and types of game. With the exception of cannabis, substance use shows a higher association with gambling, particularly binge drinking [odds ratio (OR) = 1.46, 95% confidence interval (CI) = 1.39-1.53), life-time use of inhalants (OR = 1.57, 95% CI = 1.47-1.68) and other substances (OR = 1.78, 95% CI = 1.65-1.92)]. Among life habits, the following showed a positive association: truancy at school (OR = 1.26, 95% CI = 1.18-1.35), going out at night (OR = 1.32, 95% CI = 1.26-1.38), participating in sports (OR = 1.30, 95% CI = 1.24-1.37). A negative association was found with reading books for leisure (OR = 0.82%, 95% CI = 0.79-0.86), parents' monitoring of Saturday night activities (OR = 0.81, 95% CI = 0.77-0.86) and restrictions on money provided by parents as a gift (OR = 0.89, 95% CI = 0.84-0.94). CONCLUSIONS: Underage gambling in Europe appears to be associated positively with alcohol, tobacco and other substance use (but not cannabis), as well as with other individual behaviours such as truancy, going out at night and active participation in sports, and is associated negatively with reading for pleasure, parental monitoring of evening activities and parental restriction of money.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · ESPAD student survey measured gambling by game type; abstract doesn't mention a PG screen, though ESPAD 2015 included Lie/Bet.

**Решение:** =

---

### 992 · R5180

**Business Ethics and Regulation of the Sports Betting Industry in Kenya**

2018 · review, dissertation · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: Regulation and business-ethics dissertation tagged as a review, with no abstract; unlikely to include a survey using a problem-gambling screen.); Sonnet ? (нет аннотации: No abstract; title suggests regulatory/ethics focus, but a dissertation could include a bettor survey with problem gambling measures.)

**Решение:** -

---

### 993 · R5184

**Digital media in international sport: engaging fans via social media and fantasy sports**

2018 · Swinburne figshare (Swinburne University of Technology) · article · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -6 (не про азартные игры или «ставка/лотерея» в другом смысле: Sports marketing paper on fan engagement through social media and fantasy sports; there's no indication of gambling or problem-gambling measurement.); Sonnet ? (нет аннотации: No abstract; the title is about fan engagement via social media and fantasy sports. It is probably a marketing paper without a problem-gambling measure, but this can't be confirmed.)

**Решение:** ?

---

### 994 · R5185

**Daily Fantasy Sports Players: Gambling, Addiction, and Mental Health Problems.**

2018 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-018-9744-4

Studies point to a relationship between fantasy sports/daily fantasy sports (DFS) play and gambling behavior. However, little is known about the nature of those relationships, particularly regarding the development of gambling problems. This study investigates the nature, frequency, and preferences of gambling behavior as well as problem gambling severity and comorbid conditions among DFS players. Data were collected from an epidemiologic survey of 3634 New Jersey residents on gambling and leisure activities. Participants were contacted by phone (land-line and cell) and online to obtain a representative, cross-sectional sample of non-institutionalized adults, aged 18 years or older. Excluding non-gamblers, the remaining 2146 participants, included in these analyses, indicated they had either played DFS (n = 299) or had gambled but not played DFS (1847) in the past year. Univariate comparisons and multiple logistic regression analyses were performed to identify the most significant characteristics and predictors of DFS players. Overall, a higher number of gambling activities, high frequency gambling, male gender, and reports of suicidal thoughts in the past year were most predictive of DFS players. Being Hispanic (vs. Caucasian) and/or single (vs. married or living with a partner) also doubled the odds of DFS play. Findings suggest that DFS players are characterized by high gambling frequency and problem severity and comorbid problems, notably suicidal ideation. Future research should examine the motivations and possible etiological sub-types of DFS players and the nature and course of DFS play, particularly in relation to gambling behavior and the development of gambling and other problems.

**ИИ:** + · обе модели · беттеры + инструмент · New Jersey population survey comparing DFS players (n=299) with other gamblers, including problem gambling severity; DFS counts as sports betting.

**Решение:** =

---

### 995 · R5192

**ZADÁNÍ DIPLOMOVÉ PRÁCE**

2018

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Generic Czech title meaning 'master's thesis assignment', with no abstract; it may be a thesis on sports betting, so the full text should be checked.

**Решение:** =

---

### 996 · R5202

**Sports betting advertising: shaping children’s gambling attitudes and consumption intentions**

2018 · Figshare · dissertation · en

This research found that sports betting advertising was influencing young people’s gambling attitudes, knowledge and behaviours. While this research contributed to a ban of gambling advertisements during live sport, further regulations and education strategies are needed to ensure young people are protected from the potential harms associated with gambling.

**ИИ:** разошлись — Opus -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Thesis on how advertising shapes children's gambling attitudes and intentions; no problem-gambling instrument indicated, likely qualitative.); Sonnet ? (неясно, измеряли ли проблемную игру: Thesis on sports betting advertising and young people's gambling attitudes and behaviours; abstract doesn't say whether a problem-gambling instrument was used.)

**Решение:** -

---

### 997 · R5205

**Sports Gambling in Select Nations**

2018

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the title suggests a descriptive or policy overview chapter, but survey data on sports bettors cannot be ruled out.

**Решение:** =

---

### 998 · R5208

**Las apuestas deportivas en el Concurso Hípico (CSIO) Gijón**

2018 · Dialnet (Universidad de la Rioja) · article · es

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Betting on an equestrian show-jumping event (not racing); no abstract, so it's unclear whether bettors were surveyed with a problem-gambling instrument.

**Решение:** =

---

### 999 · R5231

**Are direct messages (texts and emails) from wagering operators associated with betting intention and behavior? An ecological momentary assessment study.**

2018 · Journal of behavioral addictions · article, journal article, journalarticle · eng · https://doi.org/10.1556/2006.7.2018.99

BACKGROUND AND AIMS: Direct messaging via text messages (texts) and emails is a widely used method to advertise sports and race-betting offers. However, they have attracted little research, as this advertising is not in the public domain. This study aimed to determine whether betting expenditure is related to receiving direct wagering messages, and the specific inducements they promote. We hypothesized that receiving direct messages, particularly texts, would be related to betting expenditure within 24 hr. METHODS: In this ecological momentary assessment study, regular sports (n = 98) and race (n = 104) bettors from Australia completed short daily surveys over 1 week that captured exposure to direct messages, betting behavior in the previous 24 hr, and betting intention for the next 24 hr. Respondents were asked to forward any texts and emails received to the researchers, who coded them for inducement content. RESULTS: Longitudinal analyses found that receiving emails was positively associated with betting intention, whereas texts were positively associated with higher likelihood of betting and betting expenditure. These effects persisted when controlling for problem gambling status and signature betting events. Refund stake and bonus odds inducements were positively associated with likelihood of race betting (although not in multivariate models), as were bonus winnings inducements for sports betting. DISCUSSION AND CONCLUSIONS: Direct messages, particularly texts, are powerful marketing tools, encouraging a nearly immediate, and arguably impulsive, betting response, which may increase gambling-related problems. Overseeing this private form of advertising presents challenges to regulators, and to public health efforts that aim to reduce gambling harm.

**ИИ:** + · обе модели · беттеры + инструмент · EMA study of 98 regular Australian sports bettors that controlled for problem gambling status, likely measured with the PGSI.

**Решение:** =

---

### 1000 · R5234

**Gambling expenditure by game type among weekly gamblers in Finland.**

2018 · BMC public health · journal article · eng · https://doi.org/10.1186/s12889-018-5613-4

Excessive expenditure and financial harms are core features of problem gambling. There are various forms of gambling and their nature varies. The aim was to measure gambling expenditure by game type while controlling for demographics and other gambling participation factors. A further aim was to find out how each game type was associated with gambling expenditure when the number of game types played is adjusted for. Using data from the 2015 Finnish Gambling survey on adult gamblers (n = 3555), multiple log-linear regression was used to examine the effects of demographics, gambling participation, and engaging in different game types on weekly gambling expenditure (WGE) and relative gambling expenditure (RGE). Male gender, lower education level, higher gambling frequency and higher number of game types increased both WGE and RGE, while younger age decreased WGE but increased RGE. Furthermore, seven specific game types increased both WGE and RGE. Weekly horse race betting and non-monopoly gambling had the strongest increasing effect on expenditure. Betting games and online poker were associated with higher expenditure even when they were played less often than weekly. Among weekly gamblers the highest mean WGE was recorded for those who played non-monopoly games (146.84 €/week), online poker (59.61 €/week), scratch games (51.77 €/week) and horse race betting (48.67 €/week). Those who played only 1-2 game types a week had the highest mean WGE and RGE on horse race betting and other betting games. It seems that overall gambling frequency is the strongest indicator of high gambling expenditure. Our results showed that different game types had different effect sizes on gambling expenditure. Weekly gambling on horse races and non-monopoly games had the greatest increasing effect on expenditure. However, different game types also varied based on their popularity. The extent of potential harms caused by high expenditure therefore also varies on the population level. Based on our results, future prevention and harm minimization efforts should be tailored to different game types for greater effectiveness.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Secondary analysis of the 2015 Finnish Gambling population survey that covers betting games; the abstract does not mention any problem-gambling instrument.

**Решение:** =

---

### 1001 · R5256

**Gambling among Youth in Contemporary Ghana: Understanding, Initiation, and Perceived Benefits**

2018 · https://doi.org/10.2979/africatoday.64.3.03

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the title suggests a possibly qualitative study of youth gambling in Ghana. Sports betting and a PG instrument can't be confirmed or ruled out.

**Решение:** =

---

### 1002 · R5259

**National survey on lifestyles and gambling in Serbia: gambling participation and problem gambling in adult population**

2018 · International Gambling Studies · review, article · en · https://doi.org/10.1080/14459795.2018.1552713

ABSTRACT The aim was to examine the association of socio-demographic and lifestyle characteristics with gambling severity level. The study was a part of the National Survey on Lifestyles in Serbia: Substance Abuse and Gambling, in 2014. The sample consisted of 5385 individuals. Based on the Problem Gambling Severity Index (PGSI) score participants were divided into non-problem gambling, low-/moderate-risk gambling and problem gambling. Prevalence of problem gambling was 0.5%, which was associated with having poor self-perceived financial status, having moderate or high risk for psychological distress, playing sports betting, casino games and slot machines. Low/moderate gambling was associated with having poor self-perceived financial status, number of drinking days per year, using any illicit drugs in the last 30 days, playing sports betting, slot machines, and online betting. Programmes of early detection of problem gambling should be developed, and regulation of availability of slot machines and sports betting.

**ИИ:** + · обе модели · опрос населения об азартных играх · Serbian national adult survey measuring PGSI and sports betting participation; it links sports betting to problem gambling.

**Решение:** =

---

### 1003 · R5262

**Public Awareness and Practice of Responsible Gambling in Macao**

2018 · Journal of Gambling Studies · article · en · https://doi.org/10.1007/s10899-018-9750-6

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; a Macao public survey on responsible gambling might have measured gambling activities, including sports betting, and problem gambling.

**Решение:** =

---

### 1004 · R5266

**SLOTZ: A Game-Based Measure of Problem Gambling**

2018 · Griffith Research Online · other/griffith thesis, review, dissertation · en · https://doi.org/10.25904/1912/2401

The last decade has seen a marked increase in gambling availability and participation. This increase is in part due to a rapid proliferation in digital platforms of gambling delivery, including online betting and smartphone betting applications. In turn, this rise in gambling availability and participation has led to an increase in the prevalence of gambling-related issues. This is particularly concerning, as relatively few problem gamblers ever engage in treatment, despite experiencing substantial psychological and social impairment as a result of their gambling. Difficulties with engagement are likely to stem from the many barriers problem gamblers face when seeking treatment, including financial issues, stigma, embarrassment and shame. Successful utilisation of digital technologies may help overcome barriers often faced by more traditional face-to-face mental health assessments and interventions, with these novel forms of digital delivery being potentially better suited to fostering user engagement, motivation and retention in mental health assessments and interventions. To date, virtual reality technologies present as one the most efficacious forms of digital mental health assessments and interventions, providing a range of interactive systems, environments and mechanisms by which mental health assessment and intervention can be enacted. Review of the literature and meta-analysis, as reported in Chapter 3, supported the efficacy of virtual reality-based interventions, though issues regarding methodological rigour remain. Yet despite the promise of virtual reality-based assessments and interventions, their development and implementation has been sluggish. For this reason, there appears to be a need to explore the utility of alternative digital delivery platforms. Video games provide a more readily-accessible, cost-effective digital delivery platform for mental health assessment and intervention. Mental health video games aim to make the processes of change and learning more meaningful and engaging. As is reported in Chapter 4, review of the literature revealed that mental health video game assessments and interventions have successfully been investigated in the assessment and treatment of a number of populations and presentations. Moreover, it was observed that mental health video games may pose a particularly useful platform for engaging hard-to-reach populations such as problem gamblers, engaging users emotionally, capturing their attention and promoting continuing engagement. However, it was concluded that the lack of empirically supported theory, methodological rigour and psychometric validation in the literature makes it difficult to draw overall conclusions regarding the efficacy and utility of mental health video games. It was determined that there remains a need in the literature for robust examples of the development and implementation of empirically driven, well-validated mental health video games. The overall aim of this thesis was to explore the role digital technologies can play in the development and delivery of mental health assessment and intervention, with particular focus placed upon the area of problem gambling. To this end, a novel mental health video game assessment of problem gambling was developed (SLOTZ). Game play was developed in accordance with game design and gambling-related neuropsychological theory. Initial conceptualization, development, piloting and the first iteration of revision and refinement of SLOTZ game play is described over the course of Chapter 5 and Chapter 6. Levels of immersion and engagement were found to be high, with participants observed to find SLOTZ game engaging and enjoyable. Two SLOTZ sub-tests were observed to significantly correlate with established measures of gambling severity and to demonstrate an ability to significantly predict gambling severity in participants. Implications, limitations and directions for future research are discussed in Chapter 7 and Chapter 8. Overall, findings from this thesis provide evidence that problem gambling can be identified and predicted via video game play. SLOTZ presents as an economical, engaging, enjoyable, and psychometrically validated means of problem gambling assessment that is likely to be wide-in-reach and less psychological, socially and financially aversive to populations who are historically difficulty to engage. Moreover, this thesis provides a sound example of the process of empirically testing digital mental health video assessments and interventions via a multi-step iterative process of pilot testing and refinement, demonstrating the utility of video games in mental health assessment and interventions.

**ИИ:** разошлись — Opus ? (неясно, есть ли ставки на спорт: Thesis validating a slot-style game against established problem-gambling measures; participants' sports betting participation might be reported but is not mentioned.); Sonnet -7 (другое — напишите почему: Thesis developing a slot-game-based problem gambling assessment; no sports betting focus and not a prevalence survey of sports bettors.)

**Решение:** ?

---

### 1005 · R5268

**What is sport betting**

2018

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: No abstract; the title points to a descriptive explainer defining sports betting, not a quantitative study of bettors.); Sonnet ? (нет аннотации: No abstract; title "What is sport betting" suggests an explanatory or descriptive piece, but empirical content with problem-gambling data cannot be ruled out.)

**Решение:** ?

---

### 1006 · R5271

**Magnitude and extent of gambling disorder in the Mexican population**

2018 · Salud Mental · article · en · https://doi.org/10.17711/sm.0185-3325.2018.024

Introduction. Gambling disorder is characterized by an uncontrollable need to gamble, lack of control over gambling, prioritizing gambling over other activities, and continuing to gamble despite the negative consequences this entails. Worldwide, between .1% and 5% of people show signs of problem gambling and between .1% and 2.2% present a positive result in gambling disorder criteria. Objective. To determine the extent of the problem of gambling disorder in Mexico and to identify and analyze the demographic groups in which it occurs. Method. ENCODAT 2016-2017 is a probabilistic, multi-stage survey with national and state representativeness. The sample comprises 56 877 people who answered a standardized questionnaire that collects information on addictive substance use and other areas such as gambling disorder. Results. A total of 24.5% of the population aged 12 to 65 have played a betting game at lifetime. Men have higher statistically significant prevalences than women in nearly all types of gambling and in six of the nine symptoms of gambling disorder. In Mexico, .3% of the target population meet the criteria for gambling disorder, with adolescents showing the highest percentage (.4%). Discussion and conclusion. It is necessary to reinforce public policies for this issue that include the development of preventive actions targeting the adolescent and youth population in Mexico, and to ensure the adequate monitoring of authorized centers.

**ИИ:** + · обе модели · опрос населения об азартных играх · Mexican national survey (ENCODAT) asking about types of gambling and DSM-based gambling disorder criteria; activity tables likely.

**Решение:** =

---

### 1007 · R5272

**THE RELATIONSHIP BETWEEN DAILY FANTASY SPORTS (DFS) FREQUENCY AND GAMBLING PROBLEMS AMONG A SAMPLE OF COLLEGE STUDENT DFS PLAYERS**

2018 · The Scholarship East Carolina University's Institutional Repository (East Carolina University) · dissertation · en

Fantasy sports has been an increasingly popular form of entertainment over the last decade. It involves picking players from a specific sport and those players performance being compared to the performance of players on competing fantasy teams. The fantasy sport participant whose players perform the best is the winner. While some leagues are free to enter, fantasy sports leagues can be set up to have entry fees. While some may be low-stakes, such as $20 a person, there are many leagues where the stakes are much higher and can get into the thousands of dollars to enter. The premise behind the entry fees is players can win back their fee and everyone else’s as a form of prize money for winning the fantasy sports league. This form of wagering on fantasy sports is a form of gambling (Martin, Nelson, & Gallucci, 2016).

**ИИ:** + · обе модели · беттеры + инструмент · Dissertation surveying college student DFS players on how DFS frequency relates to gambling problems; a PG instrument was likely used.

**Решение:** =

---

### 1008 · R5273

**Gambling: spreading among students in Palermo**

2018 · Journal of Biological Research - Bollettino della Società Italiana di Biologia Sperimentale · article, review · en · https://doi.org/10.4081/jbr.2018.7498

Adolescents represent a particularly high-risk group and they are also vulnerable to the development of gambling related problems. Thanks to technological advances in gaming industry (slot machines, video lottery terminals, casino-types games) new form of gambling are continuously appearing. With the purpose of having an idea about the spreading of gambling among the students of Palermo, a survey has been conducted through administration of questionnaires during the period from January to May 2017: this study involved 1622 students (686 boys and 936 girls) between the age of 14 and 19. In this survey it has been demonstrated that only 15% of students have never played; 36% declare they have played cards with money at least once in their life and 19% of them play lotteries and scratchers; some others have played sport betting (14%), bingo (7%), slot machines (5%), horse betting (4%). The money spent on a single day is between 1 and 10 euros (584 students); 530 teenagers spend 1 euro or less; 132 between 1 o and 100 euros; 16 students more than 100 euros/die. Moreover, most alarming is evidence indicating that there is a considerable number of students who have gambling players parents (father 18,65%; mother 16,4%; both of them 4,52%): this is considered an important vulnerability factor. The analysis of the picked data suggests that there is a widespread diffusion of gambling among the adolescent population. So, to conclude, the present research points out the need to complete immediate interventions on both levels of information and prevention.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of 1622 Palermo students measured sports betting participation; abstract does not say whether a problem-gambling screen (e.g., SOGS-RA) was used.

**Решение:** =

---

### 1009 · R5278

**International Sports Betting**

2018 · Routledge eBooks · book · en · https://doi.org/10.4324/9781315768175

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -1 (обзор, комментарий, теоретическая, правовая или регуляторная работа: Probably the 2018 Routledge edited book on sports betting integrity, deviance, governance and policy; not a prevalence survey.); Sonnet ? (нет аннотации: Book "International Sports Betting" (2018) with no abstract; likely a policy or industry overview, but content is unclear, so a full-text check is safer.)

**Решение:** ?

---

### 1010 · R5280

**Longitudinal Links Between Gambling Participation and Academic Performance in Youth: A Test of Four Models**

2018 · Journal of Gambling Studies · article · en · https://doi.org/10.1007/s10899-017-9736-9

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Youth longitudinal gambling study; no abstract. It may have measured sports betting participation and a problem-gambling screen.

**Решение:** =

---

### 1011 · R5298

**Ηλεκτρονικά τυχερά παίγνια: το προφίλ των παικτών στο νομό Λακωνίας**

2018 · review

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Greek title: 'Online gambling: profile of players in Laconia'. Likely a thesis surveying online gamblers; no abstract, so PG measure is unknown.

**Решение:** =

---

### 1012 · R5299

**Ηλεκτρονικά τυχερά παίγνια: το προφίλ των παικτών στο νομό Λακωνίας**

2018 · Πανεπιστήμιο Πελοποννήσου · other/μεταπτυχιακή διπλωματική εργασία · el · https://doi.org/10.26263/amitos-5794

Δύο εξαιρετικά δημοφιλείς μορφές ψυχαγωγίας, το διαδίκτυο και η αρχαία τέχνη των τυχερών παιχνιδιών, έχουν συνδυαστεί για να δημιουργήσουν ένα δυναμικό κλάδο σηματοδοτώντας την απαρχή μιας νέας εποχής στις δραστηριότητες της βιομηχανίας των τυχερών παιχνιδιών και της παγκόσμιας οικονομίας. Η ραγδαία ανάπτυξη των ηλεκτρονικών τυχερών παιχνιδιών, με έντονους ρυθμούς, δίνει το έναυσμα τους ερευνητές του οικονομικού πεδίου να ασχοληθούν σοβαρά μαζί τους, αναλύοντας τόσο τους λόγους της εκρηκτικής πορεία προς την κορυφή της παγκόσμιας οικονομίας, όσο και τα κίνητρα που οδηγούν παραδοσιακούς και νέους παίκτες προς την κατεύθυνση του διαδικτυακού στοιχηματισμού. Στην παρούσα εργασία πραγματοποιείται η προσπάθεια να σκιαγραφηθεί και να αποτυπωθεί σε όσο δυνατόν καλύτερο βαθμό το προφίλ των παικτών ηλεκτρονικών τυχερών παιχνιδιών στο νομό Λακωνίας. Σε πρώτη φάση, με την ανασκόπηση της βιβλιογραφίας, στοιχειοθετείται ο ρόλος και τα χαρακτηριστικά των τυχερών παιχνιδιών στην καθημερινότητα του ανθρώπου, τόσο σήμερα όσο και διαχρονικά. Ταυτόχρονα, η σύντομη έρευνα στην αντίστοιχη βιβλιογραφία, σε ένα μικρό αριθμό διαθέσιμων ερευνητικών προσπαθειών σε διευρυμένη και παγκόσμια κλίμακα, δημιουργεί μικρά συγκρίσιμο δείγματα που μας βοηθούν κατά τη σκιαγράφηση του προφίλ των παικτών των διαδικτυακών τυχερών παιγνιδιών. Η διεξαγωγή της έρευνας πραγματοποιήθηκε με τη μέθοδο του ερωτηματολογίου σε ένα δείγμα 109 ατόμων που κατοικούν στο νομό Λακωνίας. Κατά την ανάλυση των αποτελεσμάτων εξετάζονται τα συγκριτικά δημογραφικά χαρακτηριστικά των παικτών, οι συνήθειες και οι επιλογές τους, η στοιχηματική τους συμπεριφορά και μοτίβα του παιχνιδιού τους, τα κίνητρα επιλογής μιας διαδικτυακής σελίδας τυχερών παιχνιδιών, καθώς και επίπεδο ικανοποίησης του χρήστη αυτών, οδηγώντας μας σε στιβαρά συμπεράσματα σχετικά με το προφίλ των παικτών στο νομό Λακωνίας.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Greek thesis surveying 109 online gamblers/bettors on profiles, habits, motives and satisfaction; abstract doesn't say whether a problem-gambling screen was used.

**Решение:** =

---

### 1013 · R5302

**Advertising has been frequently proposed as a motivational factor for initiating gambling, although the empirical evidence of its actual impact on gamblers’ behaviour remains elusive (Binde, 2014; Parke, Harris, Parke, Rigbye, & Blaszczynski, 2014). Early theorisations concerning the possible negati**

2017

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Title is an introduction snippet on gambling advertising (2017). No abstract, so sports betting and problem-gambling measurement can't be judged.

**Решение:** =

---

### 1014 · R5313

**An investigation of highly identified fans who bet against their favorite teams**

2017 · review · https://doi.org/10.1016/j.smr.2016.09.004

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; title points to an empirical study of fans who bet on sports, and it may have measured problem gambling.

**Решение:** =

---

### 1015 · R5323

**AZ ALACSONYNAK TŰNŐ KOCKÁZAT ELHANYAGOLÁSA A SPORTFOGADÁSOKBAN = NEGLECTING THE LOW RISK IN SPORTS BETTING**

2017 · Repository of the Academy's Library (Library of the Hungarian Academy of Sciences) · article · hu

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Hungarian article on risk perception in sports betting, no abstract; could be a market or decision study, or a survey of bettors.

**Решение:** =

---

### 1016 · R5327

**The Size of Illegal Gambling Industry and Its Components in Korea**

2017 · Korean Development Economics Association · article · en · https://doi.org/10.20464/kdea.2017.23.4.2

선행 연구들은 운영자와 단속자의 진술이나 사법적 판결 및 연구자의 가정에 의거하여 불법사행산업(불법도박)의 규모와 구성을 추정하여 왔다. 그 반면에 이 연구는 일반국민 및 불법도박 참여자를 대상으로 한 설문조사 결과를 활용하여 도박 참여자의 지출을 기준으로 불법사행산업의 규모와 구성을 추정하고 그 결과를 기존의 운영자 기준 추정방법을 이용한 결과와 비교한다. 설문조사 결과를 활용하여 참여자 기준으로 2015년의 불법사행산업의 규모를 추정한 결과, 그 규모는 순매출액 기준으로 당해 명목 GDP의 0.54-0.56%에 달하는 것으로 분석되었다. 이 비중은 내국인의 합법사행산업 순매출액 비중 0.49%보다 약간 높은 수준이다. 불법도박의 유형별 구성비율을 추정한 결과, 불법 스포츠도박, 불법 온라인도박, 불법 카지노, 불법 경주류도박 순으로 높은 것으로 분석되었다. 참여자 기준의 추정방법에 의한 규모는 도박 운영자나 단속자의 진술에 의존하는 추정방법에 의한 규모보다 작은 것으로 나타났 으나 유형별 비중의 순위는 큰 차이를 보이지 않았다. 이와 같이 운영자와 참여자 두 가지 접근방법을 함께 사용하여 불법사행산업의 규모를 추정하면 불법사행산업의 규모나 구성에 대한 추정의 신빙성을 높일 수 있다(JEL 분류: L83, K42).The preceding studies on illegal gambling have estimated the size of illegal gambling industry and its components by some arbitrary assumptions of researchers and the statements of regulator and illegal gambling manager or judicial executions. But this study estimates the size of illegal gambling industry and its components by the statements of gamblers who participate in legal or illegal gambling without any arbitrary assumptions of researchers. The data of this study is collected by the random sample of 1,700 people and targeted sample of 300 illegal gamblers in 2015. This study suggests the following results. First, the size of illegal gambling industry in term of the net sales is 0.54-0.56% of nominal GDP in 2015. Second, the gross sales of illegal gambling industry estimated by the statements of regulator and illegal gambling manager is 18% larger than that estimated by the expenditure of gamblers. Third, the share of illegal sport gambling is estimated 26-29%, that of illegal online gambling is 28-30%, that of illegal racing gambling 15-18% by two approaches.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Korean survey of the general population and illegal gamblers that covers illegal sports betting; estimates market size; no problem-gambling instrument mentioned.

**Решение:** =

---

### 1017 · R5349

**SOGS-RA gambling scores and substance use in adolescents**

2017 · Journal of Behavioral Addictions · article · en · https://doi.org/10.1556/2006.6.2017.043

Background and aims There is a well-established association between pathological gambling and substance use disorders in adolescents. The aim of this study was to shed light on the association between adolescents' different levels of involvement in gambling activities and substance use (smoking tobacco and cannabis and drinking alcoholic beverages), based on a large sample. Methods A survey was conducted in 2013 on 34,746 students attending 619 secondary schools, who formed a representative sample of the Italian 15- to 19-year-old population. The prevalence of different categories of gamblers was estimated by age group and gender. A multiple correspondence analysis (CA) was conducted to explain the multivariate associations between substance use and gambling. Results The prevalence of problem gambling was 2.7% among the 15- to 17-year-olds, and rose to 3.6% among the 18- and 19-year-olds. Multiple CA revealed that, even when it does not reach risk-related or problem levels, gambling is associated with the use of alcohol and tobacco. In particular, the analysis showed that non-problem gambling levels were associated with alcohol and tobacco use at least once in the previous month, and that higher-risk gambling levels related to the use of cannabis and episodes of drunkenness at least once in the previous month. Conclusion This study found that any gambling behavior, even below risk-related or problem levels, was associated with some degree of substance use by youths, and that adolescents' levels of gambling lay along a continuum of the categories of substance use.

**ИИ:** + · обе модели · опрос населения об азартных играх · Representative Italian adolescent school survey (ESPAD-type) using SOGS-RA; gambling activities, likely including sports betting, probably measured.

**Решение:** =

---

### 1018 · R5352

**Gamification through Fantasy Sports**

2017

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; fantasy sports may involve money, but 'gamification' suggests a non-gambling engagement topic. Full text needed to check.

**Решение:** =

---

### 1019 · R5353

**Gamification Through Fantasy Sports : Empirical Findings In The Context Of Professional Sport Leagues**

2017 · article · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; fantasy sports study likely about sport-marketing gamification, but a problem-gambling measure can't be ruled out.

**Решение:** =

---

### 1020 · R5354

**Glücksspielprobleme bei türkeistämmigen Migranten**

2017 · Suchttherapie · conference-paper · de · https://doi.org/10.1055/s-0037-1604557

Einleitung: Aus Repräsentativbefragungen ist bekannt, dass die Gruppe der türkeistämmigen Migranten einen überdurchschnittlich hohen Anteil von Personen mit einem pathologischen Spielverhalten aufweist. Gleichzeitig verweisen die Ergebnisse empirischer Studien darauf, dass die Raten der Inanspruchnahme von Hilfeangeboten sowie die Erfolgsquoten begonnener therapeutischer Maßnahmen reduziert sind. Welche Faktoren hierfür verantwortlich sind, ist bisher nur unzureichend wissenschaftlich untersucht worden. Ziele dieser Studie sind, (1) Ursachen eines vermehrten Auftretens von Glücksspielproblemen bei türkeistämmigen Migranten zu untersuchen, (2) Barrieren der Inanspruchnahme von Hilfe zu identifizieren und (3) Unterstützungsbedarfe zu ermitteln, um empirisch fundierte Empfehlungen für die Praxis abzuleiten zu können. Methodik: Diese vom Bundesministerium für Gesundheit geförderte Studie ist in Form von drei aufeinander folgenden Teilprojekten (TP) durchgeführt worden. TP1 beinhaltete Gespräche mit 10 Experten aus den Bereichen der Migrations-, Familien- und Suchtberatung. In TP2 wurden mittels Einzelinterviews acht aktuelle oder remittierte türkeistämmige pathologische Glücksspieler befragt. Das TP3 bestand aus einer quantitativen Befragung von insgesamt 160 türkeistämmigen Personen (Rekrutierung aus dem Hilfesystem sowie Selbstmelder), die dazu beitragen soll, die qualitativen Befunde zu validieren und gegebenenfalls zu ergänzen. Abschließend wurden die Ergebnisse der drei Teilprojekte im Rahmen eines halbtägigen Workshops hinsichtlich ihrer Relevanz für zukünftige Präventions- und Beratungs-/Behandlungsmaßnahmen diskutiert und bewertet. Ergebnisse: Erste Auswertungen machen deutlich, dass türkeistämmige Spieler dem klassischen Suchtkonzept – Spielsucht als eine psychische Erkrankung – häufig skeptisch bis ablehnend gegenüberstehen. Insbesondere das Suchtpotential der Sportwetten wird unterschätzt. Es bestehen eine Reihe von problematischen Fehlannahmen in Bezug auf das Versorgungs- und Hilfesystem. Als bedeutsames Motiv für die Glücksspielteilnahme und sich entwickelnde Spielprobleme erweisen sich insbesondere innerfamiliäre Konflikte im Kontext der Migrationskultur. Es lassen sich drei größere Spielergruppen darstellen: „Importbräutigame“, junge Sportwetter und ältere Automatenspieler. Schlussfolgerung: Die vorliegenden Befunde verweisen auf die Notwendigkeit der Entwicklung neuer bzw. Intensivierung bestehender Maßnahmen zur Aufklärung der türkeistämmigen Bevölkerung hinsichtlich der Risiken des Glücksspiels (mit besonderer Berücksichtigung von Sportwetten), der Vermittlung von Problemlösekompetenzen sowie der Bekanntmachung von Möglichkeiten der Inanspruchnahme von Hilfe. Die besondere Bedeutung der Familie ist bei der Entwicklung von Präventions- und Spielerschutzmaßnahmen für diese Bevölkerungsgruppe zu berücksichtigen.

**ИИ:** разошлись — Opus ? (другое: Mixed-methods study: 160 Turkish-origin people surveyed, partly recruited via help services; sports betting noted, PG instrument unclear.); Sonnet -5 (выборка набрана по проблемам с игрой: лечение, горячая линия, самоисключение, сравнение проблемных игроков с контролем: Mixed-methods study of Turkish-origin migrants recruited from the help system and self-referrers, mainly pathological gamblers; expert and gambler interviews, no sports bettor prevalence of problem gambling.)

**Решение:** -

---

### 1021 · R5357

**Responsible Gambling Strategies for Internet Gambling: An Empirical Investigation into the Italian Gambling Market**

2017 · International Journal of Business and Management · article, journal-article · en · https://doi.org/10.5539/ijbm.v12n7p17

The aim of this study is to analyse, in the Italian sports betting sector, the impact of Internet gambling on the level of consumption of gambling products and the responsible gambling strategies adopted by the on line gambling operators. From the methodological viewpoint the research work has been organised into two phases. In the first phase, an empirical investigation has been carried out on a sample of Italian consumers directed towards measuring the impact that the use of the Internet has on the volume of bets made on sports events. In the second phase, an analytical work has been performed on the on line gambling websites of the main operators of the Italian sports betting market, directed towards examining the measures adopted for promoting responsible gambling. The results of the empirical research indicate, on the one hand, that in the Italian market, as has happened in other national gambling markets, the legalization of on line sports betting may determine an increase in the level of consumption of gambling products and, thus, in the potential risks of excessive gambling; and, on the other hand, that the normative approach adopted in the Italian gambling market, based on a ‘concession model’ which provides for a strong public control of the gambling operators, has favoured a widespread adoption by the on line betting companies of an articulated series of measures aimed towards harm minimisation in Internet gambling. Thus, the findings of this study contribute towards the economic-managerial literature on the theme of firms’ social responsibility by providing important insights for gambling firms and public policy makers regarding the responsible gambling strategies for Internet gambling adoptable in the markets, such as the Italian one, in which on line gambling is fully regulated.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of Italian sports bettors on how Internet use affects betting volume; the abstract does not say whether a problem-gambling screen was used.

**Решение:** =

---

### 1022 · R5360

**Gambling, geographical variations and deprivation: findings from the adult psychiatric morbidity survey**

2017 · International Gambling Studies · article · en · https://doi.org/10.1080/14459795.2017.1355405

Gambling problems are prevalent in the UK, especially in the most deprived boroughs of the country. Individual-level characteristics may exist alongside a social and geographical gradient. The study aimed to establish whether living in specific geographic areas increases problem gambling likelihood. It used data from the 2007 Adult Psychiatric Morbidity Survey. It adopted a twofold categorization distinguishing recreational from problem/pathological gambling. It used the 2004 Overall Index of Multiple Deprivation to measure deprivation of the district of residence, and primary sampling units, based on postcode sectors, to take into account area characteristics in multi-level mixed-effects regression models. The determinants of recreational gambling operated solely at the individual level. These included male sex, stable relationship and employment, though a number of clinical variables were also important: impulsivity, hazardous use or dependency on alcohol, and current smoking. In contrast, an appreciable proportion of the variance in problem/pathological gambling was explained by area-level clustering. Unlike recreational gamblers, problem/pathological gamblers appear to cluster in specific areas. Thus, there are grounds for restricting the location and density of gambling opportunities and for providing selective prevention programmes targeting geographic areas characterized by contextual determinants.

**ИИ:** разошлись — Opus ? (неясно, есть ли ставки на спорт: Secondary analysis of the 2007 English Adult Psychiatric Morbidity Survey with a problem-gambling measure; unclear whether sports betting participation is reported.); Sonnet + (опрос населения об азартных играх: National UK Adult Psychiatric Morbidity Survey 2007 measured gambling and problem gambling; activity-level data may include sports betting in full text.)

**Решение:** ?

---

### 1023 · R5361

**The Effect of Peer Participation on Risk Attitudes in Fantasy Sportsi**

2017

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: No abstract; the title points to a behavioural-economics study of risk attitudes in fantasy sports, probably without a problem-gambling instrument.); Sonnet ? (нет аннотации: No abstract; fantasy sports risk attitudes study may be a survey or experiment, and it is unclear whether problem gambling was measured or money was wagered.)

**Решение:** -

---

### 1024 · R5369

**Dueling for Trust in the Online Fantasy Sports Industry: Fame, Fortune, and Pride for the Winners**

2017 · Lecture notes in computer science · article, conference object, part of book or chapter of book · en · https://doi.org/10.1007/978-3-319-58484-3_16

Trust is a necessary condition for many industries. However, trust may not be the most important factor driving participation in online fantasy sports gambling. In this research we examine how different classifications of gamblers (i.e., passive gamblers, problem gamblers, and pathological gamblers) perceive their participation in fantasy sports. We argue that trust is not commonly a primary consideration and that trust does not need to be present in these types of online transactions. To prove this relationship, a trust model is proposed to be tested in the context of online fantasy sports with a focus on the market leader in the industry: fanduel.com.

**ИИ:** ? · обе модели · другое · Fantasy sports players classified as problem/pathological gamblers, but the model is only proposed; unclear whether data or an instrument were used.

**Решение:** =

---

### 1025 · R5400

**Lephon ELEWISCN Nirm**

2017

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: Title looks garbled, with no abstract or venue, so relevance can't be judged; flagged for manual retrieval.); Sonnet -6 (не про азартные игры или «ставка/лотерея» в другом смысле: Title is unintelligible, with no abstract, venue or record type. Nothing links it to gambling or sports betting.)

**Решение:** -

---

### 1026 · R5403

**GAME ON: COMPARISON OF DEMOGRAPHIC PROFILES, CONSUMPTION BEHAVIORS, AND GAMBLING SITE SELECTION CRITERIA OF ESPORTS AND SPORTS BETTORS**

2017 · Gaming Law Review · article, journalarticle, journal-article · en · https://doi.org/10.1089/glr2.2017.21813

The esports betting market remains predominantly unregulated, although regulated sites have begun offering options to wager on these types of events. Previously, esports has been considered a niche market sector with participants differing from traditional sports and race bettors. However, as esports increasingly becomes absorbed into mainstream markets, it is important to understand the comparative similarities and differences in characteristics and behaviours between esport and traditional sports bettors. In particular, with regulators increasingly attempting to reduce use of offshore gambling sites, it is important to determine the extent to which those who bet on esports are more likely to access and engage in unregulated sites and activities. This paper classified and compared the characteristics of 501 Australians reporting participation in both sports and esports (n=160), or only in sports (n=341) bets online in the past month. Measures assessed use of online onshore and offshore sites, factors used to select gambling sites, and perceived advantages/disadvantages of using onshore compared to offshore sites. Findings suggested that the two groups were distinct in several ways; esports bettors were younger, more highly educated, had higher incomes and were represented by a greater proportion of females and individuals from Asian ethnic backgrounds. This group additionally reported starting gambling more recently and frequently overall, and expressed a preference to gamble on illegal offshore sites as opposed to domestically-licensed sites. Sports bettors were more likely to select domestic sites seeking more reliable and safe experiences, in contrast to esports bettors, who were motivated by the gambling experience, regardless of where a site was regulated. Results suggested that sports bettors perceived greater disadvantages of using offshore sites, and that this acted to deter access. In contrast, esports bettors sought a specific experience and were willing to use offshore sites. It is concluded that domestic operators need to provide a competitive online gambling environment and meet customer demands if online gamblers are to be deterred from using offshore sites.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of 501 Australian online sports and esports bettors; abstract doesn't say whether PGSI or another problem-gambling screen was used.

**Решение:** =

---

### 1027 · R5404

**INTENSITY AND GAMBLING HARMS: EXPLORING BREADTH OF GAMBLING INVOLVEMENT AMONG ESPORTS BETTORS**

2017 · Gaming Law Review · article, journal-article · en · https://doi.org/10.1089/glr2.2017.21812

The esports betting market remains predominantly unregulated, although regulated sites have begun offering options to wager on these types of events. Previously, esports has been considered a niche market sector with participants differing from traditional sports and race bettors. However, as esports increasingly becomes absorbed into mainstream markets, it is important to understand the comparative similarities and differences in characteristics and behaviours between esport and traditional sports bettors. In particular, with regulators increasingly attempting to reduce use of offshore gambling sites, it is important to determine the extent to which those who bet on esports are more likely to access and engage in unregulated sites and activities. This paper classified and compared the characteristics of 501 Australians reporting participation in both sports and esports (n=160), or only in sports (n=341) bets online in the past month. Measures assessed use of online onshore and offshore sites, factors used to select gambling sites, and perceived advantages/disadvantages of using onshore compared to offshore sites. Findings suggested that the two groups were distinct in several ways; esports bettors were younger, more highly educated, had higher incomes and were represented by a greater proportion of females and individuals from Asian ethnic backgrounds. This group additionally reported starting gambling more recently and frequently overall, and expressed a preference to gamble on illegal offshore sites as opposed to domestically-licensed sites. Sports bettors were more likely to select domestic sites seeking more reliable and safe experiences, in contrast to esports bettors, who were motivated by the gambling experience, regardless of where a site was regulated. Results suggested that sports bettors perceived greater disadvantages of using offshore sites, and that this acted to deter access. In contrast, esports bettors sought a specific experience and were willing to use offshore sites. It is concluded that domestic operators need to provide a competitive online gambling environment and meet customer demands if online gamblers are to be deterred from using offshore sites.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of 501 Australian online sports/esports bettors; title mentions gambling harms, but abstract names no problem-gambling instrument.

**Решение:** =

---

### 1028 · R5409

**The psychosocial impact of daily fantasy sports games**

2017 · Nottingham Trent University's Institutional Repository (Nottingham Trent Repository) · article · en · https://irep.ntu.ac.uk/id/eprint/31705/1/PubSub9146_Griffiths.pdf

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the title fits daily fantasy sports, but this NTU repository item may be a non-empirical commentary. Needs a check.

**Решение:** =

---

### 1029 · R5418

**Three Applied Economic Studies on Issues Facing African Youth**

2017 · eScholarship (California Digital Library) · dissertation · en

This manuscript is comprised of three independent essays in applied microeconomics. Each essay examines a distinct challenge or trend impacting African youth. First, I look at the sports betting industry which has exploded across many African countries over the past decade, targeting young men as its primary consumers. In Kampala, Uganda, the site of my study, nearly one in three young men age 18 to 40 participate in sports betting, spending 8-12% of their weekly income on these activities. The second chapter presents results from an impact evaluation of a sports and youth group program in Monrovia, Liberia. The use of sports and youth programs has become extremely popular for many multilateral and international non-profit organizations' efforts to engage and improve the conditions of marginalized or at-risk youth in developing countries. The final chapter looks at the impact of rainfall shocks on marriage decisions among youth from Burkina Faso, a setting where marriages are determined by households and influenced by financial constraints and economic shocks.In the first essay, "Betting, Saving, and Lumpy Expenditures: Sports Betting in Uganda'', I present evidence from my field study on one of the causes of high betting demand among young Ugandan men. In my paper, I show that financial constraints push many men towards betting in the hopes of payouts desired for unmet liquidity needs. I use a range of experimental and quasi-experimental methods and present four pieces of evidence in support of this claim. Winnings from betting increase the size and likelihood of making large, lumpy purchases, with strongest effects among those with limited ability to save. I then use a randomized intervention to improve an alternative strategy of liquidity generation to betting by distributing a basic commitment savings technology and find that it lowers recipients' demand for betting. Next, I use an experimental prime or nudge, increasing the salience of a desired large expenditure, and find that it increases demand for betting tickets, particularly among those with low ability to save. And finally, I use a randomized budgeting exercise and find that it lowers demand for betting among those who learn that their ability to save is better than previously believed. For people whose ability to save and borrow is inhibited or costly, betting provides an enticing alternative way to generate meaningful sums of liquidity despite imposing considerable losses.My second essay, "Do Sports Change Lives? Evidence from a Randomized Control Trial'', is the product of a joint project with Lori Beaman, Niall Keleher, and Jeremy Magruder. In this project we assess the impact of a popular form of international development program that uses sports both as a direct intervention and also as a point of entry to facilitate engagement with vulnerable youth. The stated ambitions of sports for development programs are typically both admirable and lofty, but we find only limited evidence that the impacts of these programs match their promises. We find evidence of some modest impacts on psychosocial behaviors for young men with moderate improvements in measures of self-esteem and aggressive behavior. We also see an increase in labor force participation for both men and women, although earnings among those working remain unchanged. We also explore whether the research structure required by randomization may have hindered program efficacy. However, it appears that program effects were likely stronger among late registrants who are more likely to have been excluded in the absence of the study. And finally, permitting endogenously formed sports groups may have increased pre-existing social network connections on sports teams. We find that presence of friends does impact program attendance but does not significantly impact program outcomes.\tIn my third essay, "Marriage Markets and Rainfall Shocks: Evidence from Burkina Faso'', I analyze the impact of rainfall shocks on marriage outcomes for young men and women in Burkina Faso. In particular, I use quasi-random variation in rainfall to provide evidence that low rainfall from two years ago causes an increase in the likelihood of marriage for young women by 15%. These effects are strongest among women aged 13-16. In addition, I present evidence that closed marriage markets, where womens' partners are most likely to come from the same local geographic area, respond less to rainfall shocks than areas where marriage markets are likely to be more geographically integrated. This finding is consistent with basic trade theory on market structure and response to simultaneous shifts of supply and demand in opposite directions.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Field survey/experiment with Ugandan sports bettors; the abstract doesn't say whether a problem-gambling screen like the PGSI was used.

**Решение:** =

---

### 1030 · R5422

**Bet Anywhere, Anytime: An Analysis of Internet Sports Bettors' Responses to Gambling Promotions During Sports Broadcasts by Problem Gambling Severity.**

2017 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-017-9671-9

Promotions for online sports betting during televised sports broadcasts are regularly viewed by millions of Australians, raising concerns about their impacts on vulnerable groups including at-risk and problem gamblers. This study examined whether responses to these promotions varied with problem gambling severity amongst 455 Australian Internet sports bettors participating in an online survey. Results indicated that young male Internet sports bettors are especially vulnerable to gambling problems, particularly if they hold positive attitudes to gambling sponsors who embed promotions into sports broadcasts and to the promotional techniques they use and this heightens the risk that alluring messages contribute to excessive gambling. As problem gambling severity increased, so too did recognition that these promotions have impacted negatively on their sports betting behaviour. Because a plethora of sports betting brands and promotions are now heavily integrated into sports coverage, social marketing efforts are needed to offset their persuasive appeal and counter the positive attitudes towards them that appear linked to excessive gambling amongst Internet sports bettors.

**ИИ:** + · обе модели · беттеры + инструмент · Survey of 455 Australian internet sports bettors analysed by problem gambling severity (likely PGSI).

**Решение:** =

---

### 1031 · R5423

**Risk Factors for Gambling Problems on Online Electronic Gaming Machines, Race Betting and Sports Betting.**

2017 · Frontiers in psychology · article, journal article, journalarticle · eng · https://doi.org/10.3389/fpsyg.2017.00779

Growth of Internet gambling has fuelled concerns about its contribution to gambling problems. However, most online gamblers also gamble on land-based forms, which may be the source of problems for some. Studies therefore need to identify the problematic mode of gambling (online or offline) to identify those with an online gambling problem. Identifying most problematic form of online gambling (e.g., EGMs, race betting, sports betting) would also enable a more accurate examination of gambling problems attributable to a specific online gambling form. This study pursued this approach, aiming to: (1) determine demographic, behavioral and psychological risk factors for gambling problems on online EGMs, online sports betting and online race betting; (2) compare the characteristics of problematic online gamblers on each of these online forms. An online survey of 4,594 Australian gamblers measured gambling behavior, most problematic mode and form of gambling, gambling attitudes, psychological distress, substance use, help-seeking, demographics and problem gambling status. Problem/moderate risk gamblers nominating an online mode of gambling as their most problematic, and identifying EGMs ( n = 98), race betting ( n = 291) or sports betting ( n = 181) as their most problematic gambling form, were compared to non-problem/low risk gamblers who had gambled online on these forms in the previous 12 months ( n = 64, 1145 and 1213 respectively), using bivariate analyses and then logistic regressions. Problem/moderate risk gamblers on each of these online forms were then compared. Risk factors for online EGM gambling were: more frequent play on online EGMs, substance use when gambling, and higher psychological distress. Risk factors for online sports betting were being male, younger, lower income, born outside of Australia, speaking a language other than English, more frequent sports betting, higher psychological distress, and more negative attitudes toward gambling. Risk factors for online race betting comprised being male, younger, speaking a language other than English, more frequent race betting, engaging in more gambling forms, self-reporting as semi-professional/professional gambler, illicit drug use whilst gambling, and more negative attitude toward gambling. These findings can inform improved interventions tailored to the specific characteristics of high risk gamblers on each of these online activities.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Online survey of 4,594 Australian gamblers measuring problem gambling status (likely PGSI), with problem/moderate-risk vs non-problem counts among online sports bettors.

**Решение:** =

---

### 1032 · R5425

**Understanding persuasive attributes of sports betting advertisements: A conjoint analysis of selected elements.**

2017 · Journal of behavioral addictions · article, journal article, journalarticle · eng · https://doi.org/10.1556/2006.6.2017.062

Background and aims Despite recent growth in sports betting advertising, minimal research has examined the influence of different advertising message attributes on betting attitudes and behaviors. This study aimed to identify which attributes of sports betting advertisements most engage attention, interest, desire and likelihood of betting among non-problem, low-risk, moderate-risk, and problem gamblers. Methods A novel approach utilizing an experimental design incorporating conjoint analysis examined the effects of: three message formats (commentary, on-screen display, and studio crossover); four appeals (neutral, jovial, ease of placing the bet, and sense of urgency); three types of presenters (match presenter, sports betting operator, and attractive non-expert female presenter); and four bet types (traditional, exotic key event, risk-free, and micro-bet). A professional film company using paid actors produced 20 mock television advertisements simulating typical gambling messages based on the conjoint approach. These were embedded into an online survey of 611 Australian adults. Results The most attention-grabbing attributes were type of presenter and type of bet. The attractive non-expert female presenter gained more attention from all gambler groups than other presenters. The type of bet was most persuasive in converting attention into likely betting among all gambler groups, with the risk-free bet being much more persuasive than other bet types. Problem gamblers were distinct by their greater attraction to in-play micro-bets. Discussion and conclusion Given the potential for incentivized bets offering financial inducements and for in-play micro-bets to undermine harm minimization and consumer protection, regulators and wagering operators should reconsider whether these bet types are consistent with their responsible gambling objectives.

**ИИ:** + · обе модели · беттеры + инструмент · Online survey of 611 Australian adults, probably sports bettors, grouped by PGSI risk category; the full text likely gives counts per group.

**Решение:** =

---

### 1033 · R5433

**Is lottery playing always harmful? Development of the Lottery Playing Health Scale**

2017 · Social Behavior and Personality An International Journal · article, journal-article · en · https://doi.org/10.2224/sbp.6596

We developed a multidimensional measure of lottery playing health, simultaneously considering the positive and negative perspectives of playing the lottery. Participants were 4,521 sports lottery players. The final version of the Lottery Playing Health Scale (LPHS) comprised 17 items divided across 5 factors: enjoyable experience, favorable socialization, rational control, negative mood, and social harm. The LPHS showed good psychometric properties, including level of fit to the data, discriminant validity, and reliability. Several lottery player characteristics (i.e., age, perceived risk, and urge to play) were found to be significant predictors of players' LPHS scores. This study represents an initial effort to understand the multidimensional effects of lottery playing on health.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of 4,521 sports lottery players developing a new scale; the full text may report validity checks against an established problem-gambling instrument.

**Решение:** =

---

### 1034 · R5435

**Problem Gambling among Adolescent Girls in Croatia-The Role of Different Psychosocial Predictors.**

2017 · Frontiers in psychology · article, journal article, journalarticle · eng · https://doi.org/10.3389/fpsyg.2017.00792

Although, compared to boys, adolescent girls gamble less often and less problematically, prevalence studies still show significant numbers of at risk/problem gamblers among girls. However, girl gambling has been on the sidelines of adolescent gambling research. The available studies usually focus only on a narrow set of correlates often ignoring that adolescent gambling is a complex phenomenon determined by various factors. Also, they often measure gambling related consequences with instruments that are not specifically developed for use on adolescents. In order to contribute to a better understanding of adolescent gambling this study focuses on problem gambling among girls. We consider different social, cognitive, motivational and behavioral factors as predictors of girl problem gambling. A total of 1,372 high-school girls from 7 Croatian cities participated in the study. They provided data on their gambling activities, peer gambling, cognitive distortions related to gambling, motivation for gambling, and levels of general risky behavior. As the only instrument developed specifically for use on adolescents, the Canadian Adolescent Gambling Inventory was used to examine adverse gambling consequences. Results show 7.4% of girls can be considered regular gamblers, and out of those who gambled at least once in their lifetime ( n = 862), 11.2% already experience mild adverse consequences because of their gambling (at risk gamblers), with 3.2% experiencing serious consequences (problem gamblers). In general, girls seem to prefer lotto and scratch cards, but sports betting seems to be the preferred game of choice among regular girl gamblers. A hierarchical regression model confirmed the importance of much the same factors identified as risky for the development of problem gambling among adolescent boys-cognitive distortions, motives to earn money, to be better at gambling and to relax, the experiences of winning large and the drive to continue gambling, together with social factors such as having friends who also gamble, being involved in other risky and delinquent behavior and higher gambling frequency. Results call into question the importance of the motive to feel better for adolescent girls problem gambling. We discuss implications of our findings for both universal and indicated youth gambling prevention programs.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Survey of adolescent girls that measured sports betting participation and problem gambling with the CAGI screening instrument.

**Решение:** =

---

### 1035 · R5446

**A psychometric and behavioural analysis of mobile gambling**

2017 · Nottingham ePrints (University of Nottingham) · doctoral thesis, dissertation · en · https://uon-repo.eks.prod.4science.cloud/handle/123456789/64022

The British population are increasingly using mobile devices (e.g. smartphones, tablets) to gamble. The empirical work in this thesis looks at how the interaction of gambling’s schedule of reinforcement and mobile device behaviours accelerate the acquisition of learned maladaptive behaviours. The first four chapters report psychometric modelling of gambling prevalence data to understand problem gambling further and identify key indicators relevant to associative processes in gambling behaviour. Chapter 2 reports a taxometric analysis of problem gambling assessment data to test whether these screens measure a dimensional or latent class model, finding stronger support for the latter. However, this only identified a small taxon consisting of around 5% of gamblers endorsing more than one problem gambling symptom. Chapter 3 reports the use of latent class analysis to examine distinct subtypes of responding to different screens, findings a common three-class model that showed signs of a mixed latent structure: the same taxon as Chapter 2 was observed, but the three classes showed little overlap in symptom count. Chapter 4 reports further work modelling the sociodemographic characteristics of these different subgroups. Together the data from these chapters were used help to identify indicators of those most likely to a) be most susceptible to gambling harm and b) common to all problem gamblers. In Chapter 5 a Monte Carlo analysis was conducted to understand the efficacy of taxometric procedures on binary variables, before replicating the taxometric analysis reported in Chapter 2 using dichotomous variables and extending the work to the South Oaks Gambling Screen. The indicators derived from these chapters were then used in laboratory and field studies to study mobile gambling behaviour. The laboratory study in Chapter 6 manipulated two behavioural processes, trial spacing and partial reinforcement, that are relevant to mobile gambling behaviour, showing how a mobile-like schedule is related to increased perseverance and loss-chasing. The same paradigm was used to deliver an experiment on participants’ mobile phones in a field environment in Chapter 7. They further demonstrate that a mobile style schedule of reinforcement is associated with considerable persistence in the face of mounting losses, as participants continued to persevere in the face of losses despite a free choice to cease playing. Finally in the discussion I apply the key themes of the thesis to in-play betting, a form of play that has been heavily promoted alongside mobile gambling, and to an understanding of behavioural addictions.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Thesis reanalyses British gambling prevalence data with PG screens (PGSI/DSM-IV/SOGS); unclear whether sports betting participation is reported.

**Решение:** =

---

### 1036 · R5455

**Effects of expertise on football betting KHAZAAL , Yasser**

2017

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the title suggests a quantitative study of football bettors, and a problem-gambling measure may have been used.

**Решение:** =

---

### 1037 · R5456

**A Survey on the Illegal Sport Gambling of Male Middle and High School Students**

2017 · Korean Journal of Sports Science · review, article, journal-article · en · https://doi.org/10.35159/kjss.2017.06.26.3.23

The purpose of the study was to investigate the status quo of the illegal sport gambling of male middle and high school students. To collect data, a survey with 719 middle and high school students was conducted in Seoul, Kyeonggi province, and Chungnam province. The survey was to investigate subjects

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of 719 adolescent males on illegal sports gambling; abstract truncated, unclear whether a problem-gambling instrument was used.

**Решение:** =

---

### 1038 · R5458

**The Difference of Awareness Level on Positive and Negative Effects of Permitting Online Gambling's Expansion: Focused on Gambling Users, Gambling Addicts, and General Population**

2017 · The Journal of the Korea Contents Association · article · en · https://doi.org/10.5392/jkca.2017.17.01.426

온라인베팅은 누구나 언제 어디서나 접속이 가능하며 ICT기술의 발전에 따라 베팅의 편리성과 다양한 기회로 국내 불법 도박규모는 합법 사행산업의 4배 이상에 달하며, 불법 온라인베팅 시장 또한 가파르게 커지고 있다. 이에, 국내에서 운영되고 있는 체육진흥투표권과 전자복권 외에 다른 유형의 온라인베팅도 확대허용하고 관리해야 할 필요성이 제기되고 있다. 본 연구는 온라인베팅 확대허용에 대한 인식, 온라인베팅 확대허용 시 운영방안과 불법 온라인베팅 축소방안에 대한 인식을 온라인베팅 이용자, 중독자 및 일반인 대상으로 파악하였다. 분석결과, 온라인베팅 확대허용에 대한 긍정적 부정적 인식에 집단별 유의한 차이가 있는 것으로 검증되었으며, 합법 온라인베팅 종목으로 경주류 베팅 확대허용 시 운영방안에 대한 인식 차이도 의미 있는 차이를 보였다. 이를 통해 온라인베팅 확대허용으로 양성화하게 되면 불법 온라인베팅 이용자가 합법 온라인베팅 이용자로 전환하게 될 가능성과 건전하게 이용할 수 있는 가능성이 있다는 것이 확인된 만큼 온라인베팅 확대허용의 긍정적 효과를 기대할 수 있을 것이다. Since online betting occurs on online where anybody can access through internet, thus, the online gambling market has been expanding. Domestic illegal gambling market size is 4 times bigger than that of legal gambling market, and illegal online betting market is rapidly growing as well. Currently online gambling does exist domestically in form of Sports promotion voting rights, also known as, Toto and Proto and internet lottery. However, the need for other types of online gambling to be permitted, expanded and managed has been suggested. This research has analyzed online gambling users, online gambling addicts and general population's awareness on expansion and operation of online gambling, contraction measures of illegal online gambling and operation measures in case of permitted expansion of online gambling. The result of this research's analysis showed that each group has significantly different awareness level on positive and negative effects of permitting online gambling's expansion. Also, it showed that each group has significantly different awareness on permitting expansion of racing betting as a legal gambling item. Since it is the proven fact that illegal online gambling users could turn into legal users and that users could use the service more positively if online gambling is legalized through allowance and expansion process; one could expect the positive effects from permitting expansion of online gambling.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Attitude survey of Korean online bettors (Toto/Proto), addicts and general public; unclear whether a problem-gambling instrument was used.); Sonnet -5 (выборка набрана по проблемам с игрой: лечение, горячая линия, самоисключение, сравнение проблемных игроков с контролем: Korean survey comparing attitudes toward expanding legal online betting among users, addicts (likely clinical sample) and general public; no problem-gambling prevalence among sports bettors.)

**Решение:** -

---

### 1039 · R5459

**The Effects of Being around Gambling and Gambling Advertising on Sports Gambling Addiction**

2017 · The Korean Journal of Health Service Management · article, other literature type, journal-article · en · https://doi.org/10.12811/kshsm.2017.11.3.105

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; title suggests a Korean survey of sports gamblers that measured sports gambling addiction, possibly with a screening instrument.

**Решение:** =

---

### 1040 · R5460

**주위도박과 도박광고가 스포츠도박중독에 미치는 영향**

2017 · article · ko

Objectives : The purpose of this study was to investigate the effects of gambling environment factors (being around gambling, gambling ad access) and irrational gambling belief on the gambling behaviors of college students who experienced sports gambling. Methods : Study participants were 240 college students with sports gambling experience. Data were collected through self-report questionnaires and analyzed with SPSS 18.0. Results : Being around gambling and sports gambling ad access have a statistically significant effect on irrational gambling beliefs, which have statistically significant statistical effects on gambling addiction. Self-regulation did not show statistically significant regulatory effects between irrational gambling beliefs and gambling addiction. Conclusions : It is necessary to take a proactive approach to minimize the negative effects of sports betting and to be aware of the rapidly changing sports gambling environment factors.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Survey of 240 college sports gamblers with gambling addiction as an outcome; the abstract doesn't name the instrument, though it is probably CPGI.); Sonnet + (беттеры + инструмент: Survey of 240 college students with sports gambling experience measuring gambling addiction, likely with a screening instrument; the full text may report problem-gambling prevalence.)

**Решение:** ?

---

### 1041 · R5471

**A coordinated health communication campaign addressing casino and sports gambling among undergraduate students**

2017 · Journal of Gambling Issues · article · en · https://doi.org/10.4309/jgi.v0i37.3992

Research has outlined many negative effects of disordered gambling. While gambling disorder exists among all US sociodemographic groups, college students are particularly vulnerable. This study describes a health communication approach commonly studied in the intervention of college behaviors such as risky alcohol/substance use and sexual activity. Specifically, two health communication messages targeting casino and sports betting disordered gambling were distributed at a Midwestern US public research university, and central intercept techniques were utilized to collect quantitative and qualitative data assessing student reception. Results revealed females preferred the casino message more than males (U = 4696.50, p < .05) and stated more often that the advertisement would appeal to friends (U = 4745.50, p < .05). Individuals who lost more money than they intended to lose 1–2 times understood the message more than those persons who never gambled (U = 946.50, p < .05) and those persons who never lost more than planned (U = 249.50, p < .05). Students who first gambled at ages 16–18 liked the casino message less than those students who first gambled at 13–15 (U = 208.00, p < .05) and the students who had never gambled (U = 1656.00, p < .05). For the sports betting message, the only significant association was between students’ understanding of the advertisement and race/ethnicity (c2(5) = 14.095, p < .05). Based on our findings, we suggest a health communication approach might be effective to raise awareness about gambling disorder among college students. We recommend researchers develop targeted materials with support of college administrators to deter disordered gambling.RésuméLa recherche a mis en relief de nombreux effets négatifs du jeu pathologique. Bien qu’on retrouve des problèmes de jeu dans tous les groupes sociodémographiques américains, les étudiants constituent une classe particulièrement vulnérable. Cette étude décrit une approche de communication sur la santé qui est couramment étudiée pour effectuer des interventions sur les comportements à risque observés dans les collèges et universités, tels que la consommation d’alcool ou de drogues et l’activité sexuelle. Plus précisément, on a distribué deux messages sur la santé ciblant les jeux de hasard et les jeux de paris sportifs dans une université de recherche publique du Midwest américain, et on a eu recours à des techniques centrales d’interview pour recueillir des données quantitatives et qualitatives évaluant la réception des messages par les étudiants. Les résultats ont révélé que les femmes ont préféré les messages du casino davantage que les hommes (U = 4696,50, p <0,05) et ont plus souvent dit que l’annonce intéresserait les amis (U = 4745,50, p <0,05). Les personnes qui ont perdu au jeu une à deux fois de plus que prévu ont davantage saisi le message que ceux qui n’ont jamais joué (U = 946,50, p <0,05) et que ceux qui n’ont jamais perdu plus que prévu (U = 249,50, p <0,05). Les étudiants qui ont joué pour la première fois entre 16 et 18 ans ont moins aimé le message du casino que les étudiants qui ont joué la première fois entre 13 et 15 ans (U = 208, p <0,05) et que les étudiants qui n’avaient jamais joué (U = 1656, p <0,05). Pour le message sur les paris sportifs, la seule association significative était celle entre la compréhension de l’annonce par les étudiants et la race/l’origine ethnique, c2 (5) = 14,095, p < 0,05. Selon nos constatations, nous sommes d’avis qu’une approche de communication sur la santé pourrait être efficace pour sensibiliser les étudiants aux problèmes du jeu. Nous recommandons donc aux chercheurs de concevoir du matériel ciblé, avec le soutien des administrateurs de collèges et d’universités, pour dissuader les comportements de jeu pathologique.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Student intercept survey on reception of a casino/sports-betting campaign; gambling items asked, but unclear whether a full PG screen or sports betting participation was measured.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Message-reception intercept survey of students; no problem-gambling screening instrument, only gambling history items such as losing more than intended.)

**Решение:** ?

---

### 1042 · R5472

**Empirical Study on Information Seeking and Betting Behavior in Taiwan Sports Lottery**

2017

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Empirical study of Taiwan Sports Lottery bettors; no abstract, so unclear whether a problem-gambling instrument was used.

**Решение:** =

---

### 1043 · R5475

**Can Daily Fantasy Sports Overcome the Odds**

2017

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; title about daily fantasy sports, likely a legal commentary, but an empirical study can't be ruled out.

**Решение:** =

---

### 1044 · R5485

**Patterns of Gambling Activities and Gambling Problems Among Italian High School Students: Results from a Latent Class Analysis**

2017 · Journal of Gambling Studies · article · en · https://doi.org/10.1007/s10899-017-9694-2

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · No abstract, but the title points to a student survey linking gambling activities (sports betting likely) to gambling problems.

**Решение:** =

---

### 1045 · R5493

**Understanding the Relationship Between Sports-Relevant Gambling and Being At-Risk for a Gambling Problem Among American Adolescents.**

2017 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-016-9653-3

Fantasy sports is a growing industry with a reported 56.8 million individuals participating in the United States and Canada alone in 2015. Whereas this activity has attracted considerable public attention, little research has examined its impact on adolescents in spite of their high rates of gambling. The current study examined the relationship between regular participation (more than once a month) in sport-relevant gambling activities among adolescents and those identified as being at-risk for a gambling problem. Questionnaire responses were collected from high school students (N = 6818; 49 % male) in Wood County, Ohio, United States. Statistical analyses revealed that regular involvement in sports betting, fantasy sports betting, and daily fantasy sports betting among adolescents was associated with a higher risk of gambling problems. Further, although males participate more frequently in these activities, females who participate have a stronger likelihood of being at-risk. Students aged 16-19 years old are at a higher risk for developing a gambling problem compared to younger adolescents when regularly engaging in sports-related gambling. Moreover, regularly participating in daily fantasy sports is the strongest predictor of at-risk gambling behavior in 13-15 year old students. A hierarchical logistic regression supports that controlling for gender and age, all forms of sport-relevant gambling activities are significant predictors of at-risk gambling. This study contributes to a more comprehensive understanding of the impact of sports betting and fantasy sports on adolescents and establishes an initial step for future studies to further investigate these relationships.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Adolescent survey measuring sports betting, fantasy sports and at-risk gambling, likely via a screening instrument (probably DSM-based).

**Решение:** =

---

### 1046 · R5496

**Daily and season-long fantasy sports participation and gambling-related problems among a sample of college students at three universities**

2017 · International Gambling Studies · article, journal-article · en · https://doi.org/10.1080/14459795.2017.1409248

Traditionally, fantasy sports have been played in season-long leagues, but recently daily fantasy sports (DFS) have emerged, allowing participants to play fantasy contests over shorter periods of time. Although participating in fantasy sports contests with entry fees or deposits could be considered a form of gambling, very few studies have examined associations between fantasy sport participation and gambling-related problems. Using a 2016 sample of college students (N = 941) at three institutions, this study examined associations between fantasy sports participation (season-long and DFS) and (1) gambling, (2) gambling frequency, and (3) endorsing DSM-5 gambling disorder (GD) criteria. The study found that engagement with fantasy sports and paying to play increased the likelihood of gambling and more frequent gambling. Respondents who paid an entry fee/deposit to play fantasy sports gambled more frequently than those who did not, and respondents who participated in DFS endorsed more DSM-5 GD criteria than those who did not. Because of the association found between DFS play and gambling-related problems in some participants, the study suggests that mental health professionals who treat clients with gambling problems be cognizant of DFS and that some clients might be experiencing problems with DFS.

**ИИ:** + · обе модели · беттеры + инструмент · College student survey measuring paid DFS and season-long fantasy participation with DSM-5 gambling disorder criteria.

**Решение:** =

---

### 1047 · R5505

**“¡Hagan juego, menores!”: frecuencia de juego en menores de edad y su relación con indicadores de adicción al juego**

2017 · Revista Española de Drogodependencias · review, article · es

espanolEl presente trabajo tiene como objetivo analizar la implicacion de los menores de edad con el juego de azar, especialmente la relacion entre algunos juegos con la presencia de indicadores de adiccion al juego. Tambien se atiende a las diferencias de genero. Se administro el programa de prevencion de la adiccion al juego Ludens a 807 estudiantes de bachiller y ciclos formativos de colegios privados e institutos publicos de Valencia y provincia. Dicho programa contiene una encuesta en la que se evalua la frecuencia de juego, asi como el juego patologico a traves del NODS. Los principales resultados demuestran que el 62,1% de los menores de 18 anos relata haber jugado a algun juego de azar durante los ultimos meses, de entre los cuales, las apuestas deportivas y las quinielas son las mas frecuentes. De entre los que juegan, el 22,6% manifiestan entre uno y tres criterios de juego patologico del DSM-5, mientras que el 2,8% muestran cuatro o mas criterios, que es la cifra utilizada para el diagnostico de juego patologico. Se encontraron diferencias estadisticamente significativas en genero, tanto en frecuencia de juego como en incidencia y vulnerabilidad al juego patologico. Los resultados obtenidos ponen de relevancia que, a pesar de que el juego es una actividad que esta prohibida a menores de edad, esta no es infrecuente en ellos. Algunos tipos de juego presentan una mayor correlacion con indicadores de juego problematico que son, ademas, juegos en los que existe un control laxo sobre el acceso a ellos por parte de los menores. Esta situacion podria remediarse –y la adiccion al juego podria prevenirse- con adecuadas medidas de regulacion, como la identificacion fehaciente del jugador. EnglishThis paper aims to analyze minors’ involvement with gambling, especially the relationship between certain games and the incidence of gambling addiction indicators. It also addresses gender differences. A gambling addiction prevention program named Ludens was implemented with 807 students in public and private schools of Valencia. This prevention program contains a survey that evaluates the frequency of gambling as well as pathological gambling through NODS. The main results show that 62.1% of minors reported having played a game of chance over the past year. The most common ones were sports betting and football pools. Among those who play, 22.6% have from one to three DSM-5 criteria for pathological gambling, while 2.8% show four or more criteria, which is the figure used for the diagnosis of pathological gambling. Significant gender differences in frequency of play and incidence and vulnerability to pathological gambling were found. The results obtained reveal that, although gambling is forbidden for minors, this activity is not uncommon among them. Some types of gambling have a greater correlation with problematic gambling indicators, which are also the games for which there is lax control over access to these by minors. This situation could be remedied - and addiction to gambling could be prevented - with appropriate regulatory measures, such as the gambler’s reliable identification

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Survey of 807 adolescents measuring sports betting and football pools plus NODS; relates game types to problem gambling indicators.

**Решение:** =

---

### 1048 · R5515

**Mladi i kockanje: sociološko istraživanje iskustava splitskih studenata i studentica**

2017 · University of Split. University of Split, Faculty of Humanities and Social Sciences. Department of Sociology · bachelor thesis, dissertation · hr · https://urn.nsk.hr/urn:nbn:hr:172:823608

Dostupnost i rasprostranjenost kockanja i igara na sreću postavlja pitanje kako je ova aktivnost, kroz povijest češće karakterizirana kao negativna, opstala do danas? Dokolica u suvremenom društvu postaje sinonim za slobodu i bijeg od ograničenja koje pojedincu nameće društvena sfera. Kockanje nudi mogućnost bijega i ponovog stvaranja vlastita identiteta u kontekstu igre na sreću, zajedno s fantazijom o osvajanju velikog bogatstva bez ikakva truda. Analiza kockanja polazi i od uvjetovanosti individualnih akcija širim društvenim okvirom, pri čemu se ističe interdisciplinarni pristup fenomenu. U središtu interesa su posljedice koje kockanje ima za pojedinca na različitim razinama (njegove) društvene stvarnosti. Osobito ranjiva skupina su upravo mladi, a među njima studenti i studentice stoga se ovim radom pokušalo odgovoriti na pitanje kakva iskustva splitska studentska populacija ima s kockanjem u oblicima danas dostupnim. U istraživanju je korištena metoda ankete s upitnikom kao mjernim instrumentom. Uzorak je bio prigodni, a činili su ga studenti i studentice Sveučilišta u Splitu sa sljedećih sastavnica: Filozofskog fakulteta u Splitu; Fakulteta elektrotehnike, strojarstva i brodogradnje; Fakulteta građevinarstva, arhitekture i geodezije u Splitu; Medicinskog fakulteta u Splitu i Kineziološkog fakulteta u Splitu. Istraživanje je provedeno 2017. godine. Dobiveni rezultati pokazali su da među splitskom studentskom populacijom studenti češće sudjeluju u igram na sreću i to u casino igrama. Kad je riječ o sportskom klađenju, nešto manje od petine ispitanika učestalo se kladi (jednom tjedno ili više), riječ je isključivo o studentima, dok manje od petine ispitanih studentica sudjeluje u aktivnosti sportskog klađenja i to otprilike jednom mjesečno. S druge strane, prema podacima studentice učestalije igraju eurojackpot. The availability and prevalence of gambling and games of chance asks a question how is this activity, often criticized trough history as negative survived till now? Leisure time become synonymous for freedom and escape from the limitations that are imposed on the individual by the social sphere. Gambling offers the oportunity of escape and reinvention of one's own identity in the context of the game of chance, combined with the fantasy of winning a great fortune without any effort. Analysis of gambling derive as well from the idea that individual actions are based on a social frameworks while interdisciplinary approache to the phenomenon is noticable. The main focus are consequences that gambling has for an individual on different levels of (his/hers) social reality. The youth are an especially vulnereble group, among them students so this research tried to answer a question what are the student populations expiriences with forms of gambling available today. The method used in this research was the polling method. Convinience sample was used, the sample consisted of students from the University of Split, from the following facultys: Faculty of philosophy in Split, Faculty of electrotechnics, engeneering and shipbuilding, Faculty of construction, architecture and geodesy in Split. Medical faculty in Split and the faculty of kinesiology. The research was conducted in 2017. The results show that within the student population in Split male students participate in games of chance more often, especialy casino games. Regarding sports betting, less then a fifth of the students bet frequently (once a week or more), all of wich are male students, less then a fifth of female students participate in sports betting on an averege once a month. On the other hand, results show female students more frequently play eurojackpot.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of Split university students measured sports betting frequency; the abstract doesn't say whether a problem-gambling instrument was used.

**Решение:** =

---

### 1049 · R5518

**Zwischen spekulativen Strategien und strategischen Spekulationen. Zur reflexiven Mediatisierung riskanter Geldverausgabung**

2017 · Springer eBooks · book-chapter · de · https://doi.org/10.1007/978-3-658-16084-5_10

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: German media-studies chapter on how risky money spending and speculation are mediatized; it reads as theoretical, with no sign of sports betting or a screening instrument.); Sonnet ? (нет аннотации: German book chapter on mediatization of risky spending (possibly betting/speculation); no abstract, likely theoretical or qualitative, but content cannot be confirmed.)

**Решение:** -

---

### 1050 · R5529

**Stavovi očeva prema kockanju i iskustvo u igrama na sreću**

2017 · University of Zagreb. University of Zagreb, Faculty of Education and Rehabilitation Sciences · master thesis, dissertation · sr · https://www.bib.irb.hr/885010

The main aim of this study was to examine fathers' attitudes towards gambling, frequency of their gambling and the prevalence of psychosocial problems related to gambling. Specific goals were to explore differences in attitudes towards gambling, gambling frequency and gambling related problems between younger and older fathers. Also, the goal was to investigate differences in attitudes towards gambling and gambling frequency considering gambling related problems. The research has been a part of study "Parental Perception of Youth Gambling", whose activities are being carried out by the Faculty of Education and Rehabilitation Sciences, within the wider project "Youth gambling in Croatia". Leader of this project is Neven Ricijaš, PhD. Participation in the study was completely anonymous and voluntary. The research was conducted on a sample of 283 males, high scool students' fathers from Zagreb and Split. The age range of participants ranges from 30 to 67 years, with an average age of Mage=47,50 (SDage=5,736). The attitude was measured with Attitudes Towards Gambling Scale (Jelić, Huić and Dinić, 2013), gambling activities with modified version of Gambling Activities Questionnaire (Ricijaš et al., 2011), while the gambling related problems were measured with South Oaks Gambling Screen (SOGS) (Lesieur and Blume, 1987). The results showed that fathers generaly have negative attitudes towards gambling as an activity and there was no significant differences in attitudes towars gambling considering fathers' age. Further, fathers have certain experience in games of chance and, as expected, they mostly engage in sports betting. Significant differences considering age exists in a way that younger fathers played sports betting and slot machines more games than older ones did. SOGS instrument examined fathers' gambling related problems and results showed that fathers generally don't have gambling related problems. Results showed that 16,7% fathers have moderate gambling related problems, while 1,6% are probable pathological gamblers. Also, between fathers that have some gambling related problems and the ones that haven't, there was no significant difference in attitudes towards gambling but fathers that have some gambling related problems played sports betting and slot machines more. Also, between fathers with problems and fathers without gambling related problems there was no significant differences considering age. Temeljni cilj ovog diplomskog rada jest dobiti uvid u stavove očeva prema kockanju, istražiti učestalost njihovog kockanja kao i prevalenciju psihosocijalnih problema povezanih s kockanjem. Specifični su ciljevi istražiti razlike u stavovima, učestalosti kockanja i problemima povezanim s kockanjem između mlađih i starijih očeva te razlike u navedenim obilježjima s obzirom na probleme povezane s kockanjem. Ovaj rad je sastavni dio šireg podprojekta pod nazivom "Roditeljska percepcija kockanja mladih", a koji se provodi na Edukacijsko-rehabilitacijskom fakultetu u okviru višegodišnjeg znanstveno-istraživačkog projekta "Kockanje mladih u Hrvatskoj" pod voditeljstvom izv.prof.dr.sc. Nevena Ricijaša. Sudjelovanje u istraživanju bilo je dobrovoljno i anonimno, a provedeno je na uzorku od ukupno 283 osobe muškog spola, odnosno na očevima srednjoškolaca s područja gradova Zagreb i Split. Raspon dobi sudionika kreće se od 30 do 67 godina, s prosječnom dobi od Mdob=47,50 godina (SDdob=5,736). Stav je mjeren Skalom stavova prema kockanju (Jelić, Huić i Dinić, 2013), aktivnosti kockanja modificiranom verzijom Upitnika aktivnosti kockanja (Ricijaš i sur., 2011), dok su problemi povezani s kockanjem mjereni Upitnikom South Oaks Gambling Screen (SOGS) (Lesieur i Blume, 1987). Rezultati su pokazali kako kod očeva prevladavaju uglavnom negativni stavovi prema kockanju kao aktivnosti te nisu utvrđene značajne razlike u stavovima prema kockanju s obzirom na dob očeva. Nadalje, očevi imaju određeno iskustvo u igranju igara na sreću, a sukladno očekivanjima, najviše sudjeluju u klađenju na sportske rezultate. Postoje značajne razlike u učestalosti igranja određenih igara s obzirom na dob, na način da se mlađi očevi češće klade. SOGS instrumentom kod očeva su ispitani problemi povezani s kockanjem, a rezultati su pokazali da većina očeva nema probleme povezane s kockanjem. Odnosno, 16,7% očeva ima umjerene probleme povezane s kockanjem, a kod 1,6% njih se radi o vjerojatnom patološkom kockanju. Također, između očeva koji imaju i koji nemaju problema povezanih s kockanjem nema značajne razlike u stavovima prema kockanju, ali se očevi koji imaju neke probleme povezane s kockanjem češće klade i češće igraju igre na automatima. Jednako tako, između očeva s problemima i očeva bez problema povezanih s kockanjem nisu pronađene značajne razlike s obzirom na dob.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Survey of 283 fathers measuring sports betting participation and SOGS; links problem gambling to sports betting frequency.

**Решение:** =
