# Проверка с метками ИИ, часть 1

Записи 1–150 из 1525, с метками обеих моделей над строкой решения. Модели согласны и вы тоже — поставьте `=`; иначе свой код (`+`, `?` или `-`, причина не нужна). Если модели разошлись, `=` не годится — нужен ваш код. Решаете вы.

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

### 1 · R0002

**ผลกระทบจากอาชญากรรมคอมพิวเตอร์: ศึกษาเฉพาะกรณีการพนันทายผลฟุตบอลออนไลน์**

2559 · วารสารดุษฎีบัณฑิตทางสังคมศาสตร์ · text/article · https://doi.org/10.14456/phdssj.2016.17

วารสารดุษฎีบัณฑิตทางสังคมศาสตร์, 6, 1

**ИИ:** ? · обе модели · нет аннотации · Thai study on impacts of online football betting as computer crime; no abstract, design and problem-gambling measure unknown.

**Решение:** =

---

### 2 · R0007

**Do Sports Bettors Remember Their Bets? The Role of Problem Gambling in Bet Recall**

2026 · Journal of Gambling Issues · journalarticle, article, journal-article · https://doi.org/10.4309/ikva7818

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus + (беттеры + инструмент: No abstract, but the title points to a study of sports bettors that looks at problem gambling, so a screening instrument was likely used.); Sonnet ? (нет аннотации: No abstract; title suggests a study of sports bettors that uses problem gambling as a variable, probably with an instrument. Full text needed.)

**Решение:** ?

---

### 3 · R0008

**Evaluating the Psychometric Properties of the Sports Betting Motivations Scale – Revised (SBMS-R) in Canadian Sports Bettors**

2026 · Journal of Gambling Issues · article, journalarticle, journal-article · und · https://doi.org/10.4309/wkwq5305

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Psychometric study of sports bettors with no abstract; a PGSI may have been used to test convergent validity.

**Решение:** =

---

### 4 · R0016

**Understanding Gambling Culture and the Normalisation of Sports Betting in Elite Female Sports Clubs**

2026 · Journal of Gambling Issues · article, journalarticle, journal-article · und · https://doi.org/10.4309/lmne7799

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract available. The title could fit a qualitative study or a survey of female athletes that measured sports betting and problem gambling.

**Решение:** =

---

### 5 · R0032

**Psychometric analysis of brief adolescent gambling screen, problem gambling severity index, and gambling motives questionnaire-financial among Ghanaian adolescents**

2026 · Discover Mental Health · article · en · https://doi.org/10.1007/s44192-026-00568-4

The purpose of this study was to evaluate the psychometric properties of the Brief Adolescent Sport Betting Screen (BASBS), Problem Sport Betting Severity Index (PSBSI), and Sport Betting Motives Questionnaire–Financial (SBMQF) among Ghanaian adolescents. A cross-sectional survey was conducted among 514 adolescents (352 males and 162 females) recruited from six public senior high schools in Accra, Ghana. Confirmatory factor analysis and multigroup confirmatory factor analysis were performed to examine the factorial validity, internal consistency, measurement invariance across sex, and convergent validity of the three instruments. The PSBSI demonstrated a one-factor structure, whereas the SBMQF supported the hypothesised four-factor structure. Both instruments exhibited satisfactory internal consistency, measurement invariance across sex, and expected convergent validity, supporting their suitability for assessing sports betting severity and betting motives among Ghanaian adolescents. Although the BASBS demonstrated an acceptable one-factor structure, it showed lower internal consistency, lack of full measurement invariance, and unexpected convergent validity, indicating that further cultural adaptation and validation are required. These findings provide initial psychometric evidence supporting the use of the PSBSI and SBMQF in adolescent sports betting research, school-based screening, and prevention programmes in Ghana.

**ИИ:** + · обе модели · валидация инструмента · Validation study of sports-betting-adapted PGSI and BAGS among Ghanaian adolescent bettors; it may report prevalence of problem sports betting.

**Решение:** =

---

### 6 · R0035

**The gamblification of digital leisure: The introduction of gambling among new publics**

2026 · Journal of Consumer Culture · article, journalarticle, review · en · https://doi.org/10.1177/14695405261440730

In recent years, the internet and digitalization have propelled a phenomenon of ‘gamblification’ across various sectors. This event extends beyond traditional areas like sports betting, introducing gambling elements into new domains such as video games and streaming platforms. The rise of loot boxes in online games exemplifies this trend, merging gambling mechanics with gaming. Not only does this process spread activities that may lead to problematic behaviors, but also normalizes gambling in contexts not typically associated with it, exposing individuals to a broader range of potential harms. Our study explores the ‘gamblification’ and normalization of gambling in digital leisure by examining the correlation between online and land-based gambling, electronic device-based leisure activities, and online sports betting with other kinds of online gambling. Utilizing data from a 2022 survey of the Spanish population (n = 1429), we identify a segmentation and introduction of gambling to new audiences who do not engage in traditional gambling ways. These findings, which address the evolving landscape of gambling in the digital age, have significant implications for the development of public prevention and intervention policies.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Spanish population survey (n=1429) measuring online sports betting; the abstract doesn't say whether a problem-gambling instrument was used.

**Решение:** =

---

### 7 · R0036

**Social Acceptance of Sportsbooks and their Influence on the Ecuadorian Market**

2026 · Lecture notes in networks and systems · conference-paper · en · https://doi.org/10.1007/978-3-032-09077-5_21

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; sportsbook social-acceptance study may be an attitudes or market survey, and it is unclear whether problem gambling was measured.

**Решение:** =

---

### 8 · R0040

**Matraquage médiatique, addiction et risques sanitaires liés aux paris sportifs en ligne à Abidjan (Côte d’Ivoire): Media masking, addiction and health risks linked to online sports betting in Abidjan (Ivory Coast)**

2026 · AKIRI (Revue des sciences humaines et sociales lettres langues et civilisations) · article · en · https://www.ajol.info/index.php/akiri/article/view/318100

Étrange en apparence qu’une étude scientifique de se pencher sur la question des paris sportifs en ligne et de l’engouement qui s’est développement autour ces dernières années. Certainement, le contexte, les réformes et le déploiement du numérique y ont contribué. Nul besoin de se déplacer désormais pour être acteurs majeurs d’une compétition. Entre campagnes de communication et la présence des réseaux sociaux numériques, l’habitude de se frotter à ces jeux a fini par s’installer dans le quotidien des populations. Selon une étude le nombre de parieurs est déjà à plus de 54% en Afrique subsaharienne1 , il est important de se poser les questions suivantes à savoir : comment les médias impactent-ils la pratique des paris sportif numériques ? Quels est le niveau de pratique de ces jeux ? Les populations connaissent-elles les risques sanitaires liés à l’addiction aux paris sportif ? Il ressort de notre étude menée au travers d’entretiens semi-directifs et de questionnaires que les campagnes de communication accrues autour des paris sportifs développent une addiction chez les populations ; la fréquence de paris est très élevée eu égard aux messages diffusés excessivement sur les médias, les populations dans leur majorité ignorent qu’ils existent des risques sanitaires liés à l’addiction aux paris sportifs en ligne. It may seem strange that a scientific study would examine the issue of online sports betting and the craze that has developed around it in recent years. Certainly, the context, reforms, and the rollout of digital technology have contributed to this. Nowadays, there is no need to travel to be a major player in a competition. Between advertising campaigns and the presence of digital social networks, the habit of engaging in these games has become part of everyday life for many people. According to a study, the number of bettors is already over 54% in sub-Saharan Africa, so it is important to ask the following questions: How do media impact the practice of digital sports betting? How widespread is the practice of these games? Are people aware of the health risks associated with sports betting addiction? Our study, conducted through semi-structured interviews and questionnaires, shows that increased advertising campaigns for sports betting are creating addiction among the population. The frequency of betting is very high due to excessive advertising in the media, and the majority of the population is unaware of the health risks associated with online sports betting addiction.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Mixed-methods questionnaire study of online sports bettors in Abidjan reports addiction; unclear whether a validated problem-gambling instrument was used.

**Решение:** =

---

### 9 · R0041

**Sports Betting and Christian Youth in Nigeria: Emerging Trends, Ethical Tensions and Ecclesial Responses**

2026 · Zenodo (CERN European Organization for Nuclear Research) · bookchapter/, part of book or chapter of book, book-chapter · https://doi.org/10.5281/zenodo.21990761

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Book chapter on sports betting among Nigerian Christian youth, no abstract; probably theological, but it could include a survey.

**Решение:** =

---

### 10 · R0043

**Gendered motivations and behaviour in online sports betting: perspectives from university students in Kumasi, Ghana**

2026 · SN Social Sciences · article, journalarticle, journal-article · en · https://doi.org/10.1007/s43545-026-01348-1

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; sports bettor student sample, but "perspectives" may mean a qualitative study, and no problem-gambling measure is mentioned.

**Решение:** =

---

### 11 · R0046

**Finnish Sports Betting Study 2025 - Vedonlyontiyhtiot.com**

2026 · Figshare · other · https://doi.org/10.6084/m9.figshare.31932309

The "Suomalainen vedonlyöntitutkimus 2025" by Vedonlyontiyhtiot.com (the Finnish sports betting study 2025) collected responses from 1,007 Finnish bettors to examine how they bet, where they bet, and what types of licences dominate the market. The results provide one of the clearest snapshots to date of the behaviour of active sports bettors in Finland.One of the clearest findings in the Suomalainen Vedonlyöntitutkimus 2025 is the overwhelming preference for tax-free betting sites.According to the survey, 98.50% of respondents primarily use a platform that offers tax-free winnings through an EU or ETA licence, such as Malta or Estonia. This result is strikingly consistent and leaves very little ambiguity about what Finnish bettors value when choosing where to play.The dominance of Malta and Estonia in the licensing breakdown explains much of this preference. Together, these two EU jurisdictions account for more than 75% of all primary sites selected by respondents.Åland’s PAF licence adds another sizeable share, while non-EU licences remain extremely marginal. Taken as a whole, the numbers show that Finnish bettors overwhelmingly choose environments where winnings are tax-free by default, and where the regulatory structure is familiar and stable.It’s important to note that the study does not measure whether tax-free status is the reason players chose these sites, but the end result is clear: almost every respondent ends up on a tax-free platform regardless of their initial motivation. This makes tax-free play one of the strongest behavioural trends in the dataset.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Industry survey of 1,007 Finnish sports bettors about licences; the abstract doesn't say whether problem gambling was measured.

**Решение:** =

---

### 12 · R0058

**A behavioral economic investigation of the effect of sports wagering on alcohol demand and relations to gambling motives.**

2026 · Experimental and clinical psychopharmacology · article, journal article, journalarticle · eng · https://doi.org/10.1037/pha0000871

Sports wagering is associated with alcohol use and alcohol-related harm, and gambling can increase alcohol consumption and drinking urges. However, the effect of sports wagering on alcohol reward value remains unclear. The present study explored the interactive effect of placing a single-event sports wager and social context on alcohol demand (a behavioral economic measure of alcohol reward value) using context-adapted alcohol purchase tasks in a sample of individuals reporting past-month alcohol use and sports wagering ( n = 425; M age = 31.28; 71.29% male). Contrary to hypotheses, there were no differences in alcohol demand between context-adapted alcohol purchase tasks as a function of concurrent sports wagering ( p adj = .876-.924) or social context ( p adj = .170-.667). Exploratory analyses investigated relations between gambling motives and alcohol demand and the relations between various behavioral economic constructs and problem gambling. O max was associated with an increased likelihood of problem gambling ( OR = 1.02, p adj = .03). O max and elasticity were associated with financial gambling motives, but less so during concurrent gambling events, with concurrent sports wagering attenuating the relation between elasticity and financial motives ( b = 0.34, p adj = .003). Financial motives for gambling were positively associated with alcohol use broadly, but not with simultaneous drinking while gambling. These findings suggest relations between sports wagering and alcohol demand are complex-highlighting the need for future research into the sports wagering experience, specific sports wagering forms, and alcohol's role in sports culture to better understand the relation between alcohol use and sports wagering. (PsycInfo Database Record (c) 2026 APA, all rights reserved).

**ИИ:** + · обе модели · беттеры + инструмент · Survey of 425 sports bettors who drink. Problem gambling was analysed as an outcome, which suggests a screening instrument was used.

**Решение:** =

---

### 13 · R0059

**Drink in Hand, Limit in Mind: Simultaneous Alcohol Use Does Not Attenuate the Relation Between Monetary Limit Setting and Gambling Harm**

2026 · Digital Scholarship - UNLV (University of Nevada Reno) · conference-paper

Responsible gambling strategies include a range of behavioral strategies to minimize gambling harm. One such strategy is setting monetary limits before gambling, which has been associated with reduced gambling expenditure. The simultaneous use of alcohol while gambling is associated with greater gambling-related harm severity, reduced receptivity to warning messages during play, and may affect gambling behavior when intoxicated. The present study explored the relation between monetary limit setting and gambling- and alcohol-related harm, and the extent to which these relations are moderated by the simultaneous alcohol use while gambling, in a sample of 495 individuals reporting sports betting and using alcohol during the past month. Limit setting was negatively associated with both gambling- and alcohol-related harm and drinking while gambling was positively associated with gambling- and alcohol-related harm. The proportion of gambling time spent drinking potentiated the strength of the relation between limit setting and harm, such that the negative association between limit setting and gambling harm was greater for those with relatively higher proportions of gambling time spent drinking. These findings suggest that setting monetary limits is associated with reduced gambling harm, irrespective of the extent to which individuals report simultaneous alcohol use while gambling.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of 495 sports bettors measuring gambling harm; unclear whether a problem-gambling instrument (e.g., PGSI) or only a harm scale was used.

**Решение:** =

---

### 14 · R0061

**Mobile Gambling Addiction and Its Effects on the Academic Performance and Mental Health of Criminology Students at CICOSAT Colleges**

2026 · International Journal For Multidisciplinary Research · article, journalarticle, review · und · https://doi.org/10.36948/ijfmr.2026.v08i03.78483

This study investigated the prevalence and effects of mobile gambling addiction among criminology students at CICOSAT Colleges. Specifically, it examined the level of addiction to online betting and gambling activities, the factors influencing gambling behavior, and the effects of mobile gambling addiction on students’ academic performance and mental health. The study utilized an Explanatory Sequential mixed-methods research design, combining quantitative and qualitative approaches to gain a comprehensive understanding of the phenomenon. Quantitative data were gathered from 330 criminology students through structured survey questionnaires, while qualitative data were obtained through interviews with 20 purposively selected students involved in online gambling activities. Weighted mean and thematic analysis were used to analyze the collected data. The findings revealed that criminology students were moderately addicted to online gambling activities, showing early signs of gambling dependency such as increased engagement, cognitive preoccupation, and tolerance. Social, environmental, financial, and technological factors were found to be influential contributors to gambling behavior. Peer influence, easy access to gambling applications, availability of e-wallet services such as GCash, and continuous exposure to gambling advertisements significantly encouraged students to participate in mobile gambling. Moreover, the study found that mobile gambling addiction negatively affected students’ academic performance by reducing concentration, causing absenteeism, poor time management, and declining academic motivation. In terms of mental health, students experienced stress, anxiety, emotional instability, sleep deprivation, and compulsive behavior associated with gambling activities. The study concluded that although mobile gambling has not yet become a dominant routine among most respondents, its increasing prevalence poses serious risks to students’ academic achievement and psychological well-being. The researchers recommended the implementation of stricter anti-gambling policies within educational institutions, the establishment of counseling and mental health support programs, integration of financial literacy education into the curriculum, and restrictions on gambling access within campus internet networks. These measures may help reduce gambling-related harm and promote healthier academic and personal development among criminology students.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Student survey of online betting addiction scored by weighted mean; a standard PG instrument and sports betting participation are unclear.

**Решение:** =

---

### 15 · R0065

**Sports betting and college students’ subjective well-being: The role of peers and family norms**

2026 · Iowa State University Digital Repository (Iowa State University) · dissertation · en

August2026

**ИИ:** ? · обе модели · нет аннотации · Dissertation surveying college students about sports betting; there's no abstract, so it's unclear whether problem gambling was measured.

**Решение:** =

---

### 16 · R0067

**ปจจยสวนบคคล สงคม และสอทมผลตอการเลนพนนฟตบอล ความเสยงตดพนน และผลกระทบตอประชาชน จงหวดเชยงใหม**

2026 · Journal of Social Innovation and Lifelong Learning · article · th

Chiang Mai Province faces ongoing football gambling problems and consistent arrest statistics, reflecting those residents are at risk of gambling addiction. This research aimed to study the general characteristics, football gambling behaviors, risk of gambling addiction, influencing factors, and impacts under the framework of Football Gambling, Social Learning Theory, Uses and Gratifications Theory, and Technological Determinism. Data were collected from 400 respondents who had engaged in football gambling using convenience sampling. A questionnaire and the Problem Gambling Severity Index (PGSI) were used as research instruments, considering research ethics. Data were analyzed using descriptive statistics, Pearson correlation, and multiple regression. The results showed that most football gamblers were male and initiated gambling due to peer influence. More than half were at risk of football gambling addiction. Personal, social, and media factors strongly influenced football gambling behaviors, including enjoyment, peer influence, and betting odds. Moderate impacts were reported, such as stress and insomnia. Hypothesis testing indicated that individuals who had won or lost large amounts of money had a higher risk of gambling addiction than other groups. All three factors were positively associated with gambling risk. Multiple regression analysis showed that these factors significantly predicted the risk of football gambling addiction (Adjusted R² = .257, F = 20.751, p < .001). This study proposes the G-SHIELD (Gambling Shield) Model as a theoretical framework and policy measures to prevent and address football gambling problems, aiming to reduce risks at the individual, family, social, and media levels.

**ИИ:** + · обе модели · беттеры + инструмент · Survey of 400 football gamblers in Chiang Mai that used the PGSI and reports risk of gambling addiction.

**Решение:** =

---

### 17 · R0068

**Incentivos de marketing en la percepción de riesgo y comportamiento de apuestas deportivas**

2026 · Ciencia Latina Revista Científica Multidisciplinar · article · https://doi.org/10.37811/cl_rcm.v10i4.25080

El presente estudio tuvo como objetivo analizar los incentivos de marketing en la percepción de riesgo y comportamiento de las apuestas deportivas en las decisiones de los usuarios. La metodología siguió un enfoque cuantitativo, con un diseño no experimental de alcance descriptivo, mediante una encuesta aplicada a 625 personas de la ciudad de Machala que realizan apuestas deportivas, seleccionadas a través de un muestreo por conveniencia. Los resultados evidenciaron que los bonos de bienvenida y las apuestas gratuitas son los incentivos más frecuentes que se encuentran los apostadores, mientras que las redes sociales son el principal medio de difusión de estas promociones. Más de la mitad de los participantes percibe un menor riesgo de perder dinero al recibir estos beneficios y reconoce que apuesta con mayor frecuencia y montos más altos cuando recibe una promoción. Se concluye que los incentivos de marketing funcionan como un mecanismo psicológico en la manera en que los usuarios evalúan el riesgo al apostar y en el comportamiento que adoptan después de apostar, lo que refuerza la necesidad de promover estrategias publicitarias más responsables.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of 625 sports bettors on marketing incentives and risk perception; the abstract doesn't say whether any problem-gambling instrument was used.

**Решение:** =

---

### 18 · R0078

**Behavioral addiction tendencies and associated psychosocial factors in faculty members**

2026 · Journal of Dependence · article · en · https://doi.org/10.51982/bagimli.623

Objective: Behavioral addictions may be associated with psychological symptoms and work-related factors. However, studies evaluating multiple behavioral addiction domains among faculty members remain limited. This study aimed to investigate behavioral addiction tendencies and associated psychosocial factors among faculty members. Methods: This cross-sectional online study included 202 faculty members. Participants completed an online survey consisting of a sociodemographic questionnaire, the Depression Anxiety Stress Scale-21 (DASS-21), Pittsburgh Sleep Quality Index (PSQI), Bergen Work Addiction Scale (BWAS), Smartphone Addiction Scale–Short Version (SAS-SV), Bergen Social Media Addiction Scale (BSMAS), Internet Gaming Disorder Scale–Short Form (IGDS9-SF), Modified Yale Food Addiction Scale (mYFAS 2.0), and Online Gambling Addiction Scale (OGAS). Group comparisons and correlation analyses were performed. Results: Behavioral addiction tendencies were observed at varying levels among faculty members, with work addiction, smartphone addiction, and social media addiction showing the highest scores. Depression, anxiety, and stress were positively associated with work addiction, smartphone addiction, social media addiction, and internet gaming disorder scores. Faculty members working more than 40 hours per week had significantly higher work addiction scores. Smartphone use, social media use, and gaming-related behaviors were positively associated with one another, whereas online gambling/betting tendencies demonstrated a distinct pattern. Conclusion: Behavioral addiction tendencies in faculty members appear to be associated with psychological symptoms and selected work-related characteristics. These findings contribute to the limited literature examining multiple behavioral addiction domains among faculty members and highlight the importance of considering behavioral addictions within a broader psychosocial context.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Faculty survey using Online Gambling Addiction Scale; unclear whether sports betting participation was measured or OGAS defines problem-gambling cases.

**Решение:** =

---

### 19 · R0081

**Using Machine-Learning Algorithms to Predict Self-Reported Problem Gambling Among a Sample of Online Gamblers**

2026 · International Journal of Mental Health and Addiction · article, journalarticle · en · https://doi.org/10.1007/s11469-025-01602-2

Abstract Studies suggest that algorithms can effectively be used to predict self-reported problem gambling using player tracking data. The present study analyzed a sample of real-world online gamblers ( N = 1,611) who engaged in lottery playing, casino gambling, bingo playing, and sports betting. The data also comprised each player’s actual gambling activity, as well as age and gender, in the 30 days prior to answering the Problem Gambling Severity Index (PGSI). Players who engaged in at least one lottery game 30 days prior to answering the PGSI were less likely to be problem gamblers compared to players who did not play lottery games. For all other game-categories the relationship was reversed. The results also indicated that specific behavioral tracking features—such as the average number of monetary deposits per session, total amount of money bet per day, session length, and casino gambling involvement—were among the most significant predictors of self-reported problem gambling. When evaluating different machine algorithms, logistic regression and random forest emerged as the most effective in predicting self-reported problem gambling. The present study is among the few which predicts self-reported problem gambling using a sample of online lottery players, casino gamblers, bingo players and sports bettors, and provides further empirical evidence supporting the use of machine learning models to identify self-reported problem gamblers based on player tracking data. These findings can inform responsible gambling strategies by enabling operators to identify and intervene before gambling-related problems escalate.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Online gamblers, sports betting among them, given the PGSI; the paper links problem gambling to game categories, so sports bettors' rates may be reported.

**Решение:** =

---

### 20 · R0089

**Risk Factors and Prevalence of Gambling Among University Students During Academic Disruptions: A Case of Lecturer’s Strike in Kenya 2025**

2026 · Journal of the Kenya National Commission for UNESCO · article, journalarticle, review · und · https://doi.org/10.62049/jkncu.v6i2.604

This study investigated risk factors and prevalence of gambling among university students during academic disruptions brought about by such a case of lecturers' strikes, more so in public universities. A survey was used to collect data with a quantitative approach; a sample size of 620 students continuing with their academic work was randomly selected from 4 public universities in the Nairobi metropolitan area. The study established that several factors, such as socioeconomic factors like financial constraints, academic disruptions like lecturer strikes, environmental factors like exposure to betting platforms, and psychological factors like idleness and stress levels, contribute to gambling behaviours among students. The findings show that students from low socioeconomic backgrounds participate in risk gambling behaviour, which in the long run affects their academic progress and causes psychological distress. The most common form of gambling was sports betting, with the motivation of making quick money from betting. From the study, it was established that there’s a significant relationship between socioeconomic factors and gambling risk behaviours among students. The regulatory framework directly contributes to the growth of gambling in Kenya. Hence, in control measures, betting companies can adopt some technology that will only allow users to bet with limitations to ensure there is no overspending, thus preventing addictions of any kind. Institutions ought to invest in centers of counseling with the establishment of academic programmes geared towards creating awareness to promote responsible gambling even during times of academic disruptions in Kenyan public universities.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Student survey with sports betting as the most common form; "gambling risk behaviours" mentioned, but no named problem-gambling instrument.

**Решение:** =

---

### 21 · R0094

**Network structure of gambling-related cognitions and risk behaviors among sports bettors in the Democratic Republic of the Congo: a cross-sectional EBICglasso network analysis (N = 2261).**

2026 · Addictive behaviors reports · journal article, journalarticle, article · eng · https://doi.org/10.1016/j.abrep.2026.100746

Background and aims: Sports betting is expanding rapidly in sub-Saharan Africa, yet the network structure of gambling-related cognitions and risk indicators remains understudied. This study analyzed these cognitions and their financial risk, psychological, and social correlates among DRC sports bettors. Methods: A cross-sectional sample of 2261 sports bettors (85.9% male; mean age = 25.59 years, SD = 5.79) was recruited at Kinshasa betting venues (March-May 2026). The Gambling-Related Cognitions Scale (GRCS; α = 0.924) was administered alongside financial, psychological, and social measures. Network structure was estimated using thresholded EBICglasso (γ = 0.5). Bridge centrality and sex-based invariance were assessed via NetworkComparisonTest (100,000 permutations). Results: The thresholded network retained 150 edges (density = 0.302). Guilt and G1 were the most central nodes. Bridge analysis identified guilt and social pressure as bridge nodes. Seven items showed zero bridge strength. Item-level network structure showed no global sex difference (M = 0.195, p = .121), whereas a 14-node sensitivity analysis detected an omnibus structural difference (M = 0.217, p = .022) not localized to any edge. After Bonferroni and FDR corrections, applied separately to 496 edge-level and 90 centrality-level tests, one edge (G1-G15), but no centrality index, differed by sex. Conclusions: This is among the first network analyses of gambling-related cognitions in sub-Saharan Africa, with Gambling Expectancies as the most connected cognitive domain, G1 as a central hub, and guilt and social pressure as bridge nodes. These findings extend the Interaction of Person-Affect-Cognition-Execution (I-PACE) model and inform intervention research.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of 2261 DRC sports bettors using the GRCS and risk measures; the abstract does not name a problem-gambling screen like the PGSI.

**Решение:** =

---

### 22 · R0100

**Financial Determinants and Beliefs About Gambling Control: A Cross-National Structural Model of Problem Gambling Severity**

2026 · Journal of Gambling Studies · article · en · https://doi.org/10.1007/s10899-026-10553-9

Gambling-related harm is increasingly recognized as a public health concern, yet the role of financial factors in problem gambling remains insufficiently understood. This study examined the associations of financial knowledge, risk-oriented financial behaviour, prudent financial attitudes, and financial anxiety with problem gambling severity. A focused Health Belief Model-informed framework was used to investigate whether perceived benefits of reducing gambling, perceived barriers to gambling reduction, and gambling-related self-efficacy statistically accounted for indirect associations between financial variables and Problem Gambling Severity Index scores. Data were collected from 2,000 adults who had gambled during the previous 12 months in Italy and the United Kingdom. The measurement structure was evaluated through exploratory and confirmatory factor analyses and cross-country measurement invariance testing. Direct, indirect, and total associations were subsequently examined using multi-group structural equation modelling. Financial anxiety was positively associated with problem gambling severity in both countries, whereas financial knowledge and prudent financial attitudes showed inverse associations. Risk-oriented financial behaviour showed a positive direct association with gambling severity in Italy but not in the United Kingdom. Perceived barriers emerged as the strongest HBM-related correlate of gambling severity and accounted for the principal supported indirect associations involving financial anxiety, financial knowledge, and prudent financial attitudes. Perceived benefits and self-efficacy were not independently associated with gambling severity. These findings suggest that gambling-related harm is associated not only with financial competence and vulnerability, but also with the perceived difficulty of reducing gambling. Prevention may therefore benefit from combining financial education with measures that reduce practical, cognitive, and emotional barriers to gambling control.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Survey of 2,000 past-year gamblers in Italy and UK using PGSI; unclear whether sports betting participation was measured.

**Решение:** =

---

### 23 · R0107

**PSYTURK**

2026 · OSF Preprints (OSF Preprints) · preprint

# PSY-TURK Study 1: Substance-Related and Behavioral Addiction-Risk Indicators Among University Students in Türkiye ## Project Overview This repository contains the materials associated with PSY-TURK Study 1, a cross-sectional investigation of substance-related and behavioral addiction-risk indicators among university students in Türkiye. The study examined alcohol- and drug-related risk using the CAGE-AID and assessed addiction-related burden across ten behavioral domains, including compulsive shopping, problematic social media use, food-related addictive behavior, gaming, sex/pornography, gambling, sports betting, exercise, cryptocurrency investment, and internet broadcasting/live streaming. The project aimed to estimate prevalence, examine demographic correlates, evaluate overlap between substance-related and behavioral risk indicators, and assess the robustness of findings across alternative behavioral-threshold systems. ## Repository Contents This repository includes: * Analysis scripts used to prepare, score, and analyze the data. * Variable definitions and scoring procedures. * Behavioral-threshold specifications. * Supplementary analysis materials and documentation. * Reproducibility files necessary to recreate the reported analyses. ## Data Availability The original dataset contains sensitive information regarding mental health, substance use, addictive behaviors, and related personal experiences. To protect participant confidentiality and comply with ethical obligations, the raw dataset is not publicly available. A de-identified analytic dataset may be made available upon reasonable request, subject to applicable ethical, legal, and institutional requirements. Shared datasets will exclude direct identifiers and may include additional recoding or aggregation of potentially identifying variables. ## Code Availability All analysis scripts required to reproduce the primary and supplementary analyses are available in this repository. The code is provided for transparency, reproducibility, and secondary methodological evaluation. ## Citation If you use materials from this repository, please cite the corresponding publication: Batmaz, S., et al. (in preparation). Substance-related and behavioral addiction-risk indicators among university students in Türkiye: Overlap, correlates, and threshold sensitivity. ## Contact For questions regarding the project, data access, or reproducibility materials, please contact the corresponding author.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Student survey covering gambling and sports betting addiction risk; unclear whether a recognised problem-gambling instrument was used.

**Решение:** =

---

### 24 · R0109

**Title Evolution, Market Structure, and Behavioral Dynamics of the Online Sports Betting Industry Author: Minal Dutta Next Move Strategy Consulting**

2026 · Unpublished · preprint, text/preprint, article · und · https://doi.org/10.13140/rg.2.2.15494.95045

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: Market-research consultancy piece on how the betting industry and its market structure developed; no sign of a survey of bettors with a problem-gambling screen.); Sonnet ? (нет аннотации: No abstract; title suggests an industry/market-structure overview with behavioral dynamics, likely a non-empirical or consulting piece, but problem gambling data can't be ruled out.)

**Решение:** ?

---

### 25 · R0114

**Socioeconomic Impact of Sports Betting and Youth Perspectives on Regulatory Solutions in Mwanza City, Tanzania**

2026 · NG Journal of Social Development · article, journalarticle, review · und · https://doi.org/10.4314/ngjsd.v19i1.4

Sports betting has expanded rapidly across Tanzanian cities, raising concerns about its financial and social effects on youth. This study examined betting behavior and its socioeconomic consequences among youth in Mwanza City, Tanzania. A cross-sectional survey was conducted with 200 respondents aged 18 years and above who had previously engaged in sports betting. Participants were recruited from betting shops, mobile money outlets, and public gathering points across six wards. Data were analyzed using descriptive statistics, chi-square tests, and binary logistic regression. The findings revealed that betting was common, with 36.5% of respondents betting occasionally, 31.0% weekly, and 22.0% daily. Financial difficulties were widespread: 62.0% reported financial challenges, 55.5% experienced reduced savings, and 52.0% had borrowed money to continue betting. The most common economic consequence was difficulty meeting basic needs such as food and transport (34.0%). Social impacts were also evident, including family conflicts (54.0%) and social isolation (53.5%). These findings indicate that sports betting contributes to significant financial and social vulnerabilities among urban youth, highlighting the need for stronger regulation, public awareness campaigns, and accessible support services.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of 200 Tanzanian sports bettors reporting harms; the abstract names no problem-gambling instrument, though one may appear in the full text.

**Решение:** =

---

### 26 · R0129

**Troubles liés à l’usage des jeux de hasard et d’argent chez les adolescents et jeunes adultes en Afrique subsaharienne : analyse exploratoire de la prévalence et des facteurs associés en milieu universitaire au Bénin, 2025**

2026 · Santé Publique · article · fr · https://doi.org/10.3917/spub.263.0279

INTRODUCTION: Gambling is growing at an alarming rate in Benin, particularly among students. This population, seeking independence and success, is especially vulnerable to the risks of disorders associated with these practices. AIM OF THE STUDY: to determine the prevalence of, and identify factors associated with disorders related to gambling in universities in Benin. METHODS: This is a cross-sectional analytical study involving 1,360 Beninese students. Gambling-related disorders were assessed using the diagnostic criteria of the fifth edition of the Diagnostic and Statistical Manual of Mental Disorders (DSM-V). Associated factors were explored using multiple logistic regression. RESULTS: Of the 1,360 students, 455 (33.5%) were gamblers, 89 of whom were classified as having gambling-related disorders, representing a prevalence of 6.5% among all students and 19.6% [95% CI: 15.9%–23.2%] among gamblers. The distribution of disorders was as follows: 12.1% mild, 6.8% moderate, and 0.7% severe. After adjustment, factors associated with these disorders were age (p=0.007), having a gambling app on one’s phone (p<0.001), friends’ influence on decision-making (p=0.014), frequency of gambling (p=0.012), betting with money belonging to others (p=0.006), duration of engagement in online gambling (p=0.032), and anxiety (p<0.001). CONCLUSION: This study highlights the extent of gambling-related disorders in Beninese universities. It emphasizes the need for stricter regulation and targeted preventive measures to address this still insufficiently recognized public health problem.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Survey of Beninese students using DSM-5 gambling disorder criteria; full text likely lists gambling activities, but the abstract does not mention sports betting.

**Решение:** =

---

### 27 · R0131

**When Sports Betting Addiction Takes Hold: Creation and Validation of the Sports Betting Addiction Index**

2026 · Digital Scholarship - UNLV (University of Nevada Reno) · conference-paper

The mainstreaming and legalization of sports betting in over three quarters of the country has given rise to significant increases in sport betting addiction (Yeola et al., 2025). One problem in determining the overall addiction levels is that most mainstream gambling addiction measures are (a) not sport-specific and (b) several decades old. Given the role mobile media plays in easing the placement of bets and consumption of sports media in general, there is substantial need to establish a robust, valid measure that reflects contemporary sports fan betting behaviors. This presentation would present the pilot results for the establishment of a Sports Betting Addiction Index (SBAI). Using Netemeyer et. al’s (2003) index development framework as guidance, the pilot will unfold via the following structure: (a) identification of key literature to build an expert list, (b) solicitation of input from the expert panel, (c) generation of proposed measurement items, and (d) pilot testing. Findings would include the advancement of multiple subfactors of sports betting addiction along with relevant demographic correlates that could help crystallize when interventions are warranted. Implications for sports management, media, marketing, and psychology will all be imbued within the creation and advancement of this pilot data.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Pilot validation of a new sports betting addiction index in bettors; unclear whether an established PG screen was used for comparison.

**Решение:** =

---

### 28 · R0139

**Pay to Play: Behavioral and Demographic Patterns in Problematic Gambling, Sports Betting, and Within-Title Video Game Spending**

2026 · Digital Scholarship - UNLV (University of Nevada Reno) · conference-paper

Since a federal ruling in 2018, legalized online sports betting in the US generated $26 billion of revenue in 2025. A parallel digital market is in video gaming, where in-game transactions comprised $30 billion in the US in 2025. Some in-game purchasing mechanics have risk-reward pathways identical to gambling, where real money is spent for outcomes that are not guaranteed, such as loot boxes and gachas. Research has established parallels to gambling for these types of purchases, including connections to problematic behaviors. To better understand the links between sports betting, in-game transactions, and problematic gambling, this study examined the overlap of these activities across individuals from diverse demographics. Over 500 online participants were selected for either video game play or sports betting. They reported frequency of sports betting, in-game purchasing, and completed the PGSI, a measure of gambling harm. Higher PGSI scores were associated with greater sports betting and in-game spending (rhos>.5). Behaviors varied by demographics, with higher scores for men (all measures), those identifying as Black compared to White (all measures) and Asian (sports betting), and older individuals (sports betting). This suggests that underlying mechanisms shared by sports betting and video game transactions are associated with problematic behaviors. We posit that demographic differences may be due to beliefs and norms associated within subcultures of these groups.

**ИИ:** + · обе модели · беттеры + инструмент · Online sample including people recruited as sports bettors, all completed the PGSI; could report problem gambling among sports bettors.

**Решение:** =

---

### 29 · R0463

**Matched Betting and Gambling Harm: Reassessing the "Risk-Free" Claim**

2026 · Digital Scholarship - UNLV (University of Nevada Reno) · conference-paper

Matched betting—often promoted as “risk-free —uses mathematical strategies to profit from free bets and promotions offered by online gambling platforms. By placing back bets with bookmakers and lay bets via exchanges, individuals aim to reduce chance and secure profit. Despite growing visibility, particularly among university students and those seeking supplementary income, its relationship to gambling-related harm remains unknown. This study uses a mixed-methods approach to examine the prevalence, motivations, and lived experiences of matched betting, and its associations with harm. Quantitative data were collected through a screening survey of UK online gamblers (n=7,041) and a follow-up survey with matched bettors (n=2,112). This follow-up assessed gambling behaviour, gambling severity, and harm indices. We collected 2,954 open-text responses exploring perceptions and experiences, which were analysed thematically. Additionally, in-depth qualitative interviews (n=30) offered insight into motivations and practices. Across datasets, matched betting was commonly framed as skill-based and distinct from gambling, with fewer than half of participants classifying it as gambling. However, reported experiences revealed notable harm, including financial losses and elevated gambling risk. Students emerged as a particularly vulnerable group, reporting higher gambling severity, a broader range of financial, emotional, and academic harms, and riskier engagement patterns.

**ИИ:** разошлись — Opus + (беттеры + инструмент: Survey of UK matched bettors (bookmaker and exchange betting) measuring gambling severity, likely with PGSI; mixed methods, but includes quantitative survey data.); Sonnet ? (неясно, измеряли ли проблемную игру: Survey of UK matched bettors (bookmaker/exchange, effectively sports betting) measured gambling severity, probably PGSI, but the instrument isn't named in the abstract.)

**Решение:** ?

---

### 30 · R0464

**“ There is no risk, so long as you follow the rules” : perceptions of risk and illusion of control in matched betting**

2026 · International Gambling Studies · journalarticle, article · en · https://doi.org/10.1080/14459795.2026.2708667

Matched betting, growing in popularity, is widely advertised as a risk-free, skill-based strategy exploiting bookmaker incentives to accumulate guaranteed profits. Limited research has investigated experiences of matched betting or understanding of its risks and relationship to gambling. An online survey with UK-based adults (n = 2,112) reporting engagement with matched betting generated 2,954 open-text responses to questions around whether matched betting is gambling, difficulties experienced, and losses incurred, to explore perceptions of risk, control, and potential harm in matched betting. Reflexive Thematic Analysis, supported by large language model-assisted classification to enable systematic exploration while retaining research-led interpretation, identified five themes: risk-free, skill-based and controllable; external barriers and bookmaker-imposed restrictions; mistakes, errors, and a steep learning curve; emotional impulses and vulnerability; and addiction risk and gambling harms. Participants frequently framed matched betting as not gambling, emphasizing mathematical certainty, discipline, and personal control, but also revealed financial losses, cognitive strain, emotional lapses, and shifts in responsibility from individual error and structural constraints. While many highlighted self-control to distance from harm, others acknowledged matched betting’s potential to lead to gambling harms, particularly for vulnerable individuals. This psychological ambiguity suggests claims of risk-free profit warrant closer scrutiny, with implications for harm prevention and consumer protection.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Large online survey of UK matched bettors; this paper analyses the open-text answers, but the survey may have included the PGSI.

**Решение:** =

---

### 31 · R0467

**Identifying Key Correlates of Problem Sports Betting in Young Adults: A Machine Learning Approach.**

2026 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-026-10478-3

Problem sports betting is an increasing public health concern, especially among young adults who are developmentally vulnerable to gambling-related harm. Although past studies have identified correlates of sports betting harm, most have not accounted for the potential influence of wide ranges of other variables in multivariable models. This study applied machine learning to identify the most influential predictors of problem sports betting in a sample of 221 young adults (ages 18–29; 77% male) from 35 U.S. states who reported recent engagement in sports betting. Two machine learning algorithms, regularized regression and random forest, were used to predict scores on the Problem Gambling Severity Index–Sports Betting (PGSI-SB) from a broad set of 80 candidate predictors. Nested cross-validation was used to tune model parameters and obtain unbiased out-of-sample performance estimates in this modest sample. The regularized regression model reduced out-of-sample prediction error by 39% relative to a naïve baseline model, whereas the random forest reduced error by 34%. Across both models, sports betting motives, social functioning, amount wagered, and perceived harm from sports betting emerged as the most influential predictors. Given that both models left considerable prediction error unexplained, it is likely that important determinants of problem sports betting were not captured in the available feature set. Findings demonstrate the utility of machine learning in identifying key risk factors across multiple domains and highlight the importance of focusing on sports betting motives and social functioning in prevention efforts. This study contributes to a growing evidence base by identifying factors that are uniquely predictive of problem sports betting among young adults.

**ИИ:** + · обе модели · беттеры + инструмент · Survey of 221 young adult US sports bettors using PGSI-Sports Betting; machine learning used on survey data, not on match outcomes.

**Решение:** =

---

### 32 · R0470

**The gambling environment and gambling problems in Western Australia**

2026 · Addiction Research & Theory · article · en · https://doi.org/10.1080/16066359.2026.2733842

Background Gambling-related harm is a widely recognized global public health challenge, yet comparatively little work has examined how differences in gambling environments relate to patterns of gambling behavior and harm. In Australia, Western Australia (WA) provides a distinctive regulatory setting in which electronic gaming machines (EGMs) are restricted to a single casino, while lotteries operate under public monopoly.Method Using nationally representative self-report data from the Household Income and Labour Dynamics in Australia (HILDA) survey (2015–2018; 29,517 respondents), we compared gambling participation, expenditure and problems (PGSI scores) in WA with the rest of Australia.Results WA residents were 76% less likely to gamble on EGMs (OR 0.24, 95% CI 0.18–0.32) and more than twice as likely to use lotteries (OR 2.07, 95% CI 1.86–2.30). Overall gambling participation was higher in WA, but total expenditure recorded in HILDA was similar across jurisdictions. However, average PGSI scores were lower in WA (–0.26, p < 0.01), consistent with differences in overall environmental product mix, rather than within-product differences in gambling problems. PGSI scores among people using EGMs and lotteries did not differ by jurisdiction.Conclusions These findings indicate that WA’s regulatory settings are associated with a distinctive gambling environment characterized by lower engagement with high-risk EGMs, and greater engagement with lower-risk lotteries. By drawing on a nationally representative dataset distinct from that used in previous work on WA, this study extends prior evidence on product-mix differences across jurisdictions and highlights how variation in environmental product availability influences population patterns of gambling problems.

**ИИ:** + · обе модели · опрос населения об азартных играх · Nationally representative HILDA survey measured participation by gambling activity (which includes sports betting in HILDA) and PGSI; activity breakdowns are likely.

**Решение:** =

---

### 33 · R0475

**Longitudinal Trajectories of Problem Gambling Symptoms and Alcohol Related Problems in a U.S. National Sample**

2026 · Digital Scholarship - UNLV (University of Nevada Reno) · conference-paper

The rapidly expanding access to gambling in the U.S. has been linked with increased gambling participation, gambling-related problems, and symptoms of gambling disorder. Individuals who gamble also report higher alcohol consumption, greater alcohol-related harm, and more frequent binge drinking. Sports gambling legalization has also been linked to reductions in retirement savings and increases in bankruptcy filings and payday lending, highlighting potential economic risks of expanded gambling access. The present study examined longitudinal associations among gambling disorder symptoms, alcohol use frequency, and family income over a three-year period in a census-matched sample of U.S. adults (N = 4,363). Gambling disorder symptoms were assessed using the Problem Gambling Severity Index (PGSI), and alcohol use frequency was measured with the NIDA-ASSIST-2. Data were analyzed using parallel process growth curve models. Results showed small but significant declines over time in PGSI scores (slope = -0.135, p < .001) and alcohol use frequency (slope = -0.035, p < .001). However, the slopes of PGSI and alcohol use frequency were strongly positively correlated (r = .806, p < .001), suggesting closely linked trajectories. Higher income was linked with greater alcohol use (estimate = 0.102, p < .001), more frequent gambling (estimate = 0.044, p < .001), and predicted lower PGSI scores (estimate = -0.012, p < .001), indicating that financial security may serve as a protective factor.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Census-matched US adult panel using PGSI; sports gambling is mentioned only as background, so it's unclear whether sports betting participation was measured.

**Решение:** =

---

### 34 · R0486

**Acceptability and Perceived Usefulness of a Digital Gambling Harm Minimisation Tool: A Cross-Sectional Study (Preprint)**

2026 · preprint · https://doi.org/10.2196/preprints.101430

BACKGROUND Gambling consumers show low uptake and engagement with tools designed to support safer gambling practices and reduce the risk of experiencing gambling-related harms. We used co-design principles to design and develop a digital tool for safer gambling (‘BetWell’) to overcome known barriers to tool uptake, including a focus on gambling problems. BetWell aims to increase awareness of personal gambling expenditure and knowledge of how gambling products function to support informed decision-making about gambling. It was designed based on behavioural change theories and presents a personalised amalgamation of gambling expenditure relative to alternative spend options, and psychoeducational information via a quiz. OBJECTIVE This exploratory study assessed the perceived acceptability and usefulness of the newly designed digital tool ‘BetWell’ and gathered end-user feedback to improve future prototypes. The study explored whether usability, gambling severity, financial wellbeing, gambling frequency, spend tracking, activity statement use, and the number of accounts held impacted acceptability and perceived usefulness, and the extent to which these factors independently predicted acceptability and perceived usefulness when controlling for life satisfaction, gambling satisfaction, and demographic variables. METHODS This cross-sectional study recruited 140 gambling consumers (M=41.3, SD=10.9 years) via the market research panel CRNRSTONE. Participants accessed and engaged with BetWell and completed an online survey to share their perceptions towards the tool. RESULTS The overall acceptability (M=32/40, SD=5.2) and perceived usefulness (M=20/25, SD=3.9) of the tool were considered ‘good’ and ‘useful’, respectively by participants. Individuals with higher gambling severity scores were more likely to perceive the tool as useful than those of the lower risk categories. Individuals with higher financial wellbeing were more likely to perceive the tool as useful and acceptable compared to those in lower financial wellbeing categories. Higher usability scores corresponded with higher tool acceptability. Previous efforts to monitor and track gambling spend was associated with both acceptability and perceived usefulness. Gambling frequency and the number of gambling accounts were not related to acceptability and perceived usefulness. Qualitative feedback included participant identified suggestions for improvements such as a need for interactive elements, a more detailed view of gambling expenditure, automation of activity statement upload functionality, more challenging and positively framed quiz content, and an emphasis on data security. CONCLUSIONS The study provides preliminary support for the acceptability and perceived usefulness of a newly developed tool to increase awareness of gambling expenditure and knowledge on how gambling products function, providing directions for future improvements to the tool.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Survey of gambling consumers that measured gambling severity; online accounts suggest wagering, but sports betting participation is not stated.

**Решение:** =

---

### 35 · R0487

**Acceptability and Perceived Usefulness of a Digital Gambling Harm Minimization Tool: Cross-Sectional Study**

2026 · JMIR Formative Research · article · en · https://doi.org/10.2196/101430

BACKGROUND: Gambling consumers show low uptake and engagement with tools designed to support safer gambling practices and reduce the risk of experiencing gambling-related harms. We used co-design principles to design and develop a digital tool for safer gambling ('BetWell') to overcome known barriers to tool uptake, including a focus on gambling problems. BetWell aims to increase awareness of personal gambling expenditure and knowledge of how gambling products function to support informed decision-making about gambling. It was designed based on behavioural change theories and presents a personalised amalgamation of gambling expenditure relative to alternative spend options, and psychoeducational information via a quiz. OBJECTIVE: This exploratory study assessed the perceived acceptability and usefulness of the newly designed digital tool and gathered end-user feedback to improve future prototypes. The study explored whether usability, gambling severity, financial wellbeing, gambling frequency, spend tracking, activity statement use, and the number of accounts held impacted acceptability and perceived usefulness, and the extent to which these factors independently predicted acceptability and perceived usefulness when controlling for life satisfaction, gambling satisfaction, and demographic variables. METHODS: This cross-sectional study recruited 140 gambling consumers (M=41.3, SD=10.9 years) via the market research panel CRNRSTONE. Participants accessed and engaged with BetWell and completed an online survey to share their perceptions towards the tool. RESULTS: The overall acceptability (M=32/40, SD=5.2) and perceived usefulness (M=20/25, SD=3.9) of the tool were considered 'good' and 'useful', respectively by participants. Individuals with higher gambling severity scores were more likely to perceive the tool as useful than those of the lower risk categories. Individuals with higher financial wellbeing were more likely to perceive the tool as useful and acceptable compared to those in lower financial wellbeing categories. Higher usability scores corresponded with higher tool acceptability. Previous efforts to monitor and track gambling spend was associated with acceptability and perceived usefulness. Gambling frequency and the number of gambling accounts held were not related to acceptability and perceived usefulness. Qualitative feedback included participant identified suggestions for improvements such as a need for interactive elements, a more detailed view of gambling expenditure, automation of activity statement upload functionality, more challenging and positively framed quiz content, and an emphasis on data security. CONCLUSIONS: The study provides preliminary support for the acceptability and perceived usefulness of a newly developed tool to increase awareness of gambling expenditure and knowledge on how gambling products function, providing directions for future improvements to the tool.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Survey of gambling consumers that measured gambling severity (likely PGSI); the mentions of wagering accounts and activity statements suggest betting, but sports betting isn't stated.

**Решение:** =

---

### 36 · R0493

**Gambling participation and risk over time associated with type of gambling activity: Trends in Australian general population 2015-2022.**

2026 · Addictive behaviors · article, journal article, journalarticle · eng · https://doi.org/10.1016/j.addbeh.2026.108618

• Gambling participation in Australia fell from 37% in 2015 to 33% in 2022. • Higher-risk gambling increased from 3.7% to 4.7% over the same period. • Young people under 35 saw larger increases in higher-risk gambling over this time. • Slot machines, race betting, and sports betting were linked to higher-risk gambling. • Clear need for public health approaches targeting higher-risk young adults. There is limited longitudinal data examining national gambling trends in Australia. This study examines longitudinal trends in gambling participation and higher-risk gambling in Australia from 2015 to 2022 using data from the nationally representative Household Income and Labour Dynamics in Australia (HILDA) panel study. Study participants were HILDA respondents aged 15 and older in 2015, 2018, or 2022 who completed the Problem Gambling Severity Index (PGSI; N = 44,836 observations). Gambling participation was based on self-reported typical monthly expenditure on 10 gambling activities. Gambling risk was assessed using the 9-item PGSI and categorised as low-risk (0–2) or higher-risk (3+) gambling. Age and sex were included as socio-demographic variables. The results indicated that monthly gambling participation declined from 37.1% in 2015 to 32.9% in 2022 but levels of higher-risk gambling did not reduce at the same rate. Higher-risk gambling was independently associated with participation in electronic gaming machines (EGMs; OR = 8.0, p < 0.001), race betting (OR = 2.3, p < 0.001) and sports betting (OR = 1.5, p = 0.01). These were the most popular forms of gambling among those aged under 25. Although overall gambling participation in Australia has declined to 2022, this did not result in a reduction to higher-risk gambling. Young adults were the least likely to gamble, but show disproportionate participation in EGMs, race, and sports betting, and an increasing rate of higher-risk gambling.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · National HILDA survey measured sports betting participation and PGSI; it links higher-risk gambling to type of activity, including sports betting.

**Решение:** =

---

### 37 · R0501

**Financial Wellbeing and Gambling Risk in Australia**

2026 · University of Sydney Library · report/, report · https://doi.org/10.25910/rgj8-3p52

This report examines gambling risk through a financial wellbeing lens. Rather than focusing only on individual indicators of problem gambling, it considers how gambling activity relates to household income, expenditure burden, financial stress, and economic vulnerability. Using wave 22 of the Household, Income and Labour Dynamics (HILDA) Survey, the analysis compares five major gambling activities: electronic gaming machines (EGMs), lotteries, sports betting, race betting, and casino table games. EGM participants had the lowest average household disposable income, the highest activity-specific expenditure burden, and the highest prevalence of financial stress among the gambling activity groups examined. After adjusting for expenditure and participant characteristics, EGM participation was associated with higher odds of both household financial stress and problem gambling. The results show that gambling-related harm is not evenly distributed across gambling activities. Lotteries was the most common activity, but problem gambling risk was more concentrated among EGM and casino table game participants. This pattern indicates that participation rates alone provide an incomplete picture of gambling risk. The report also draws on behavioural decision-making research and safer gambling intervention evidence. Gambling products differ in speed of play, frequency of outcomes, and opportunities for repeated spending. These features matter because financial risk may build through repeated decisions before individuals reassess their behaviour. Safer gambling policy should therefore consider who is financially vulnerable, how much is spent relative to income, and whether interventions reduce behaviour that may contribute to financial harm. Interventions should be evaluated using observable behavioural and financial wellbeing outcomes, including expenditure, betting intensity, limit-setting behaviour, and persistence after losses.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · HILDA wave 22 analysis compares problem gambling risk across activities, including sports betting; HILDA includes the PGSI.

**Решение:** =

---

### 38 · R0534

**Traditional gambling, betting in video games, and financial trading: Associations with gambling severity and associated harm in young adults.**

2026 · Adicciones · article, journal article, observational study · eng;spa · https://doi.org/10.20882/adicciones.2512

La digitalización del juego ha favorecido la expansión de productos análogos al juego de azar en espacios como los videojuegos y las plataformas de inversión financiera. Aunque estas prácticas comparten mecanismos estructurales y perfiles de riesgo con el juego de azar, la evidencia sobre su relación con el daño asociado y su papel conjunto en la predicción de la gravedad del juego sigue siendo limitada. Este estudio analizó si la participación reciente (últimos 60 días) en estas actividades, junto con las formas tradicionales de juego, se asocia con la gravedad del juego (PGSI) y el daño relacionado (SGHS). La muestra procede de un ensayo controlado aleatorizado (ClinicalTrials.gov ID: NCT06681103), del que se emplearon únicamente los datos de la evaluación inicial previos a la intervención. Se reclutaron 1.889 jóvenes de 18–34 años residentes en España, de los cuales el 53,9 % (n=1.018) había participado recientemente en actividades de juego o análogas, conformando la muestra analizada. Ambos indicadores se modelaron mediante regresión ordinal jerárquica ajustada por implicación global (frecuencia y número de actividades) y sociodemográficas. Las asociaciones con la gravedad se mantuvieron tras todos los ajustes, con OR ajustadas (ORa) entre 1,9 y 3,6 (p&lt;0,01), destacando las apuestas en videojuegos y el trading de materias primas, con magnitudes similares a las observadas para máquinas tragaperras, casino y apuestas deportivas. En el SGHS, solo las apuestas en eSports y el trading de materias primas (ORa=2,23, p&lt;0,05) conservaron su asociación con un mayor número de daños tras el ajuste sociodemográfico, mientras que las loterías mostraron asociaciones inversas con ambos indicadores (ORa=0,58 en PGSI, y ORa=0,56 en SGHS, p&lt;0,05). Los resultados subrayan la necesidad de incorporar estas nuevas formas de gasto digital en la detección y prevención del daño asociado al juego entre jóvenes adultos.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Baseline data on Spanish young adults: measured sports and esports betting participation and PGSI severity, analysed by activity.

**Решение:** =

---

### 39 · R0535

**Online Personalized Normative Feedback to Foster Intention to Change and Help Seeking in Young Adults With Disordered Gambling and Trading Behaviors: Protocol for a Randomized Controlled Trial**

2026 · JMIR Research Protocols · article · en · https://doi.org/10.2196/73155

Background: Despite the availability of treatment options, help-seeking rates among individuals with gambling problems remain low. To reach a broader population of those affected by disordered gambling, online and self-guided interventions have been developed. Personalized normative feedback (PNF) is one of the most widely used strategies for preventing gambling issues among young adults. However, most studies on PNF efficacy focus solely on its impact on the intensity and severity of gambling behavior, without exploring its potential to increase intention to change and help-seeking behaviors. Furthermore, there is a lack of studies assessing the efficacy of PNF in addressing emerging online gambling-like behaviors, such as betting within video games or excessive financial trading of high-risk assets (eg, cryptocurrencies), which have been linked to gambling disorder. Objective: This study aims to (1) quantify intention to change and the prevalence of help-seeking behaviors in young adults in Spain with disordered gambling or trading behaviors and (2) assess the efficacy of online PNF in increasing these behaviors. Methods: A randomized controlled trial using a Solomon 3-group design was conducted with a sample of emerging adults aged 18 to 34 years. The study included 3 assessments: a pretest, an immediate posttest, and a 12-week follow-up assessment. Participants were randomized into 1 of 3 conditions, with the intervention group receiving online PNF. The primary outcomes were intention to change and help-seeking behaviors. Secondary outcomes included gambling and trading behaviors (intensity, frequency, and severity) and their longitudinal trajectories. Individual, interpersonal, and contextual factors will be assessed to identify the profile of individuals most likely to benefit from this intervention. Results: The study was funded in December 2023 by the Spanish Ministry of Social Rights, Consumer Affairs and 2030 Agenda (SUBV23/00004) and approved by the Ethics Committee of the Miguel Hernández University. The first study assessment was conducted between December 2024 and January 2025. A total of 1889 people completed the eligibility assessment, of whom 1112 (58.9%) met the inclusion criteria (gambling or trading within the past 60 days) and were enrolled in the trial. The 12-week follow-up was finalized in March 2025, with 666 completing the final assessment (59.9% retention). Data collection has been completed, statistical analyses are ongoing, and primary results are expected to be published in March 2026. Conclusions: By examining motivational outcomes rather than behavioral change alone, this trial addresses a key gap in the literature on digital interventions for gambling-related harm. Findings are expected to inform the development of scalable prevention and early intervention strategies targeting gambling and gambling-like behaviors in young adults.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · RCT protocol enrolling young gamblers/traders and measuring gambling severity; unclear whether sports betting participation by problem-gambling status will be reported.

**Решение:** =

---

### 40 · R0538

**Exploring the relationship between Positive Play and perceived knowledge in traditional sports gambling**

2026 · International Gambling Studies · article, journalarticle, journal-article · en · https://doi.org/10.1080/14459795.2026.2697457

The growing accessibility of gambling in the United States, fueled by legalization and online platforms, has increased the need to examine both problem and responsible gambling, particularly among sports gamblers. Sports betting is often viewed as a skill-based activity, in which knowledge and skill are perceived to influence betting outcomes. The present research examines how perceived sports gambling knowledge relates to Positive Play behaviors and beliefs, as measured by the Positive Play Scale (PPS), which assesses responsible gambling from the gambler’s perspective. Participants (n = 396; Mage = 51.3, SD = 14.4, 69.9% men) were sports gamblers drawn from the fourth wave of a longitudinal sample recruited via YouGov Opinion in the United States. They rated their perceived knowledge of sports they had bet on in the past 6 months, reporting high confidence in their knowledge of the sport they identified as their preferred choice. Greater perceived knowledge was associated with lower Positive Play, particularly with poorer Gambling Literacy. These findings suggest that heightened confidence in one’s sports gambling knowledge may reflect overconfidence rather than accurate understanding, which may undermine responsible gambling practices. These results highlight the importance of addressing overconfidence in interventions aimed at promoting safer sports gambling behaviors.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of US sports gamblers using the Positive Play Scale; the longitudinal YouGov panel may also have used PGSI, but the abstract doesn't say.

**Решение:** =

---

### 41 · R0539

**From Prevalence to Prevention: Assessing Gambling Behaviors and Implementing a Harm-Reduction Program Among University Students.**

2026 · Digital Scholarship - UNLV (University of Nevada Reno) · conference-paper

The rapid growth of legal and online gambling in the United States has increased exposure among young adults, raising concerns about gambling-related harm on college campuses. This presentation describes a two-phase project conducted at the University of New Mexico aimed at assessing student gambling behaviors and piloting a targeted prevention response. Phase one involved a campus-wide survey of students (N = 2,129) assessing gambling participation, modalities, and risk indicators. Results suggest that slightly under a third of students reported past-six month gambling behavior (29.4%), and sports betting being endorsed by 19.0% of gamblers. A subset of students reported patterns associated with elevated risk, underscoring the need for proactive intervention. Building on these findings, phase two focuses on the development and implementation of a group-based harm-reduction-program adapted from the Alcohol Skills Training Program (ASTP), referred to as the Gambling Skills Training Program (GSTP). GSTP is designed to increase gambling literacy, promote safer gambling practices, and reduce gambling-related harm without requiring abstinence. The presentation will outline the rationale for the program, components of the intervention, and early feasibility outcomes (e.g., engagement, acceptability, preliminary change indicators). Together, these phases illustrate a data-driven pathway from assessment to intervention for addressing gambling-related risk among college students.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Campus survey (N=2,129) measured sports betting; "risk indicators" may or may not come from a validated problem-gambling instrument.

**Решение:** =

---

### 42 · R0540

**Generational differences in the initiation of gambling: impacts from the legalization of sports gambling and the rise of online gambling**

2026 · Journal of Public Health · journalarticle, article, journal-article · en · https://doi.org/10.1007/s10389-026-02879-w

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the title points to a survey of how gambling started, including sports gambling, and problem gambling may have been measured.

**Решение:** =

---

### 43 · R0541

**The differences in alcohol frequency while gambling among sports versus non-sports gamblers.**

2026 · Journal of psychiatric research · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1016/j.jpsychires.2025.11.041

With the drastic increase of sports wagering availability in the United States, there has been a growing body of research investigating the relationship between sports betting and alcohol use behaviors. Of note, there appears to be a link between sports wagering and alcohol consumption. The majority of research has focused on how these two behaviors occur distinct from each other, but there has been limited efforts to examine how these behaviors co-occur. As such, the present work examines frequency of drinking while gambling among individuals who gamble on sports as opposed to those who gamble not on sports. Participants were recruited by YouGov Opinion polling as part of a larger longitudinal study and the present analyses make use of data from the second follow up in spring of 2022. Gambling participants were asked what types of gambling they had participated in the past six months, and were asked about their alcohol use while gambling, as well as the percentage of time gambling that they also drink. Sports gamblers were found to report higher drinking frequency while gambling than non-sports gamblers, as well as at a higher percentage of time. As such, these results suggest a concerning trend among sports gamblers as opposed to non-sports gamblers in drinking behaviors, and may suggest that the recent legislative changes in the United States regarding sports gambling could have larger impacts outside of just gambling frequency.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · YouGov longitudinal survey comparing sports and non-sports gamblers; abstract doesn't mention a problem-gambling instrument, though the larger study likely used one.

**Решение:** =

---

### 44 · R0542

**Youth sports betting: exploring associations with addictive behaviors and sport participation**

2026 · Addiction Research & Theory · article, journalarticle, journal-article · en · https://doi.org/10.1080/16066359.2026.2653599

Abstract Background Youth sports betting is a growing public health concern. This exploratory study scrutinizes the profile of young people who bet on sports, examining associations with addictive behaviors and sport participation. Method Through a school-based collaboration across Belgium, 11,103 young people between 12 and 24 years completed an anonymous questionnaire. Results Binary logistic regression analyses indicated that 33% of the variance in whether young people had bet on sports during the past year could be explained by the model (Nagelkerke R2 = 0.33). In the past year, sports betting was significantly (p < 0.01) associated with age, being male, use of lotteries, alcohol, psychedelics, and tobacco, and being involved in football, cycling, and combat sports. Conclusions Broadening our understanding to the link with lotteries, substance use, and sport participation, this study contributes a novel perspective to the scientific literature on youth sports betting and its underlying mechanisms. This study also suggests that sports clubs may serve as valuable settings for educating young people about the risks of sports betting, drawing on their distinctive social and pedagogical potential.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Large Belgian youth survey measuring past-year sports betting; abstract doesn't say whether a problem-gambling screen was used.

**Решение:** =

---

### 45 · R0547

**Chasing the Present: Cognitive Distortions, Time Perspective, and Alcohol use in Adolescent Gambling**

2026 · Journal of Gambling Studies · article · en · https://doi.org/10.1007/s10899-026-10516-0

Adolescence represents a critical developmental period for the emergence of maladaptive gambling behaviors, including loss chasing, a key marker of gambling-related harm. The present study provides the first behavioral examination of the interplay among gambling severity, gambling-related cognitive distortions, temporal perspective, alcohol use, and chasing behavior in a sample of Italian adolescents. Participants completed the South Oaks Gambling Screen for Adolescents (SOGS-RA), the Gambling Related Cognitions Scale (GRCS), the Consideration of Future Consequences Scale (CFC-14), and the Alcohol Use Disorders Identification Test (AUDIT), and performed a computerized task assessing chasing behavior. Participants were randomly assigned to either a control or a loss condition. Logistic regression analyses indicated that illusion of control and present-oriented time perspective predicted chasing initiation, independent of gambling severity. The loss condition did not significantly influence initiation but did predict chasing persistence. Hierarchical linear regression further showed that chasing persistence was predicted by the loss condition, higher illusion of control and predictive control, stronger present orientation, and greater alcohol use, over and above gambling severity. Path analysis identified cognitive distortions as the primary mechanism underlying chasing persistence, exerting both direct effects and indirect effects through increased temporal myopia. Notably, gambling severity did not independently predict chasing once cognitive and temporal factors were considered. These findings suggest that loss chasing in adolescence may reflect a distinct behavioral vulnerability driven by distorted beliefs and present-focused orientation rather than overall gambling severity. Targeting predictive control beliefs and strengthening future-oriented thinking may enhance prevention and early intervention strategies for youth gambling.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Italian adolescents assessed with SOGS-RA in an experimental chasing study; unclear whether sports betting participation was recorded.

**Решение:** =

---

### 46 · R0549

**Deu green? Estudo exploratório sobre o envolvimento de estudantes da rede pública de educação básica com apostas Online no RS**

2026 · Zenodo (CERN European Organization for Nuclear Research) · journal, other · pt · https://doi.org/10.5281/zenodo.23018539

O presente artigo analisa o envolvimento de estudantes da rede p&uacute;blica de ensino do Rio Grande do Sul com plataformas de apostas esportivas online (bets) e aplicativos de cassinos (&ldquo;Jogo do Tigrinho&rdquo;), buscando compreender como essas pr&aacute;ticas t&ecirc;m se disseminado entre adolescentes. A partir de uma pesquisa explorat&oacute;ria, foram aplicados question&aacute;rios em tr&ecirc;s escolas de ensino m&eacute;dio e uma de ensino fundamental, com o objetivo de identificar perfis, motiva&ccedil;&otilde;es e impactos sociais e escolares relacionadas &agrave;s apostas online. Ao todo, responderam o question&aacute;rio 286 estudantes entre 13 e 19 anos. O estudo dialoga com autores que se debru&ccedil;aram sobre o tema e situam as apostas online no contexto mais amplo da cultura digital e das novas formas de entretenimento. Os resultados apontam que as apostas pela internet est&atilde;o muito pr&oacute;ximas dos jovens, o que pode levar a uma naturaliza&ccedil;&atilde;o dessa pr&aacute;tica pelos adolescentes. Conclui-se que o fen&ocirc;meno transcende a esfera do entretenimento de econ&ocirc;mico, exigindo uma abordagem sociol&oacute;gica mais ampla

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Questionnaire survey of 286 Brazilian students on online sports betting; abstract does not say whether a problem-gambling instrument was used.

**Решение:** =

---

### 47 · R0554

**Online Gambling: The Odds are Stacked Against Us**

2026 · The Canadian Journal of Addiction · article · en · https://doi.org/10.1097/cxa.0000000000000279

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: No abstract; title sounds like an editorial on online gambling, but it could report survey data on online or sports bettors.); Sonnet -1 (обзор, комментарий, теоретическая, правовая или регуляторная работа: Title and venue suggest a commentary/editorial in Canadian Journal of Addiction on online gambling; no abstract, likely no prevalence data.)

**Решение:** ?

---

### 48 · R0559

**A Bettor's Paradox: AI, Predictive Analytics, and the Information Systems of Legalized Sports Wagering**

2026 · Iowa State University Digital Repository (Iowa State University) · dissertation · en

August2026

**ИИ:** ? · обе модели · нет аннотации · No real abstract; this dissertation on AI/predictive analytics in sports wagering may be about markets or systems, but might survey bettors.

**Решение:** =

---

### 49 · R0562

**Drink more, bet more, spend more: Examining who engages in simultaneous drinking while sports betting and impact on betting behaviour.**

2026 · Journal of behavioral addictions · journal article, journalarticle, article · eng · https://doi.org/10.1556/2006.2025.00577

Abstract Background and aims There is a shared culture between sports betting and drinking alcohol, yet there is a lack of studies investigating predictors of simultaneous alcohol use, and whether drinking carries increased risk of gambling-related harms among sports bettors. Methods We examined four groups of Canadian sports bettors: (1) no alcohol use ( n = 70), concurrent use ( n = 429), (3) sometimes-simultaneous alcohol use ( n = 211), and (4) always/almost always simultaneous alcohol use ( n = 198). Participants completed measures of demographic characteristics, sports gambling-related variables, alcohol problems, gambling problems, and emotion dysregulation. Results Any simultaneous alcohol use was associated with younger age and gender diversity compared to concurrent and no alcohol use. Bisexuality was specifically linked to always simultaneous alcohol use. Always simultaneous alcohol use was also associated with higher alcohol and gambling problems compared to sometimes simultaneously drinking alcohol, despite the sometimes-simultaneous drinking group reporting higher sports betting frequency. Simultaneous alcohol use was also associated with a greater number of bets made and more money spent. Discussion and conclusions Findings suggest that simultaneously drinking alcohol while sports betting is linked to making more bets and spending more money on bets. Demographic and psychological determinants of simultaneous drinking were generally consistent with the rest of the literature except that the group which always simultaneously drank alcohol reported lower sports gambling frequency, but greater alcohol and gambling problems. This highlights the harms associated with always simultaneously drinking while betting and also warrants future research to better understand these behaviours.

**ИИ:** + · обе модели · беттеры + инструмент · Survey of 908 Canadian sports bettors that measured gambling problems; the instrument is likely the PGSI.

**Решение:** =

---

### 50 · R0564

**Understanding the links between anxiety, depression, and sports betting: The mediating role of sports betting motivations.**

2026 · Addictive behaviors · article, journal article, journalarticle · eng · https://doi.org/10.1016/j.addbeh.2025.108482

Sports betting has grown in popularity in recent years in the US and Canada, and is now a major form of gambling. In the present research, we examined which motivations for sports betting mediated the association between emotional vulnerabilities (i.e., anxiety and depression) and sports betting and gambling problems. We recruited sports bettors in Ontario, Canada (final N = 915; 77.2 % men) and categorized them as in-play bettors (n = 221), single-event bettors (n = 531), and traditional bettors (n = 163). Participants completed an online battery of questionnaires measuring depression, anxiety, sports betting behaviour, problem gambling, and sports betting motives. Analyses showed that depression and anxiety were highly correlated in this sample of sports bettors. Both depression and anxiety were associated with greater gambling problems, and these associations were mediated primarily through coping motives. On the other hand, mediation analyses showed that depression and anxiety were associated with greater sports betting frequency primarily through enhancement motives. We also found that the associations did not differ significantly for type of sports betting, nor did they differ between men and women. These results demonstrate that depression and anxiety may be more likely to be comorbid in those who partake in sports betting, and that coping motives are related to gambling problems in sports bettors. Thus, our findings support the pathways model of problem gambling, suggesting that interventions for those who primarily engage in sports betting should focus on comorbid depression and anxiety, and should bolster coping styles.

**ИИ:** + · обе модели · беттеры + инструмент · Survey of 915 Ontario sports bettors that measured problem gambling; the instrument isn't named but is likely the PGSI.

**Решение:** =

---

### 51 · R0565

**Predictors of Fantasy Sports Gambling Severity**

2026 · Elsevier BV · posted-content, preprint · https://doi.org/10.2139/ssrn.7177138

&lt;p&gt;Online fantasy sports gambling is a rapidly growing field of entertainment, in which players bet on athletes across various sports to win cash prizes. Online fantasy sports gambling’s rapid development raises concerns regarding the underlying factors that may drive problematic sports betting behavior (e.g. risky betting behavior). A quantitative study was conducted in December 2025 and February 2026 utilizing college student fantasy sports betters. Participants (&lt;i&gt;N&lt;/i&gt; = 98) reported engaging in fantasy sports in the past year and were assessed for as personality traits, income, engagement rate, number of bets placed on average, size of bets placed, motivational orientation, and impulsivity rate. Pearson correlations and multiple regression were used to assess associations between study variables and fantasy sport gambling severity. Regarding personality traits, multiple regression analyses showed no statistically significant association between neuroticism/extraversion and gambling severity, &lt;i&gt;Model F&lt;/i&gt;(2,95) = 1.05, &lt;i&gt;p&lt;/i&gt; = .35, &lt;i&gt;R&lt;/i&gt;² = .02. However, multiple regression did reveal that external regulation motivational orientation, bet size, personal income, impulsivity, and engagement were all significant predictors of gambling severity, &lt;i&gt;F&lt;/i&gt;(5, 92) = 13.43, &lt;i&gt;p&lt;/i&gt; &amp;lt; .001, &lt;i&gt;R&lt;/i&gt;² = .42. &lt;i&gt;Together, these five variables accounted for 42% of the variance in gambling severity, with higher fantasy sports gambling severity associated with greater external motivation, higher impulsivity, higher personal income, larger bet sizes, and more frequent daily engagement with fantasy sports&lt;/i&gt;&lt;i&gt;&lt;span&gt;.&lt;/span&gt;&lt;/i&gt;&lt;span&gt; &lt;/span&gt;Findings suggest that behavioral factors may be more accurate predictors of problematic gambling rather than personality traits.&lt;/p&gt;

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Survey of college fantasy sports bettors measuring 'gambling severity'; the abstract doesn't name the instrument, so it may or may not be PGSI.); Sonnet + (беттеры + инструмент: Survey of college fantasy sports bettors (N=98) measuring gambling severity, likely with an instrument such as the PGSI. Cutoff-based prevalence may be reported.)

**Решение:** ?

---

### 52 · R0566

**Communication Scholars Should Help Uncover the Causes and Consequences of Mobile Sports Gambling: A Call for Research and Theory Development**

2026 · Communication & Sport · article, journalarticle, review · en · https://doi.org/10.1177/21674795261453880

Advances in communication technology have led to sharp increases in sports betting via smartphones and other mobile devices around the world. At the same time, legal changes in places such as the United States have drastically altered the media ecosystem surrounding sports. As a result, sports betting now permeates many facets of sports media coverage and the broader culture of sports. Despite these developments, mobile sports gambling has received relatively little attention from communication scholars. In this agenda-setting commentary, we argue that communication researchers are uniquely positioned to elucidate the causes and consequences of mobile sports betting and build and test theory related to this issue. In doing so, we illustrate research opportunities for studying mobile sports gambling across the field. We begin by documenting the rapid increase in mobile sports betting and gambling-related media content in society. We then explain why features of mobile sports betting and the contemporary media ecosystem combine to create complexities that require the attention of communication scholars. Finally, we bolster our arguments with survey data from a sample of 1,075 American adults who reported using a mobile device to gamble on sports in the past year.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Commentary, but it includes survey data from 1,075 US mobile sports bettors; the abstract doesn't say whether a problem-gambling instrument was used.

**Решение:** =

---

### 53 · R0575

**Perception of gambling marketing among Spanish adolescents: an analysis based on gambling severity risk**

2026 · International Gambling Studies · article · en · https://doi.org/10.1080/14459795.2026.2681975

Marketing is one of the most extensively studied contextual factors influencing gambling behavior. However, its association with adolescent gambling behavior remains underexplored. This study adopts a mixed-methods approach to: 1) analyze gambling behavior among Spanish adolescents, and 2) examine their exposure to gambling advertising based on gambling risk. A total of 1,189 students (M = 15.64, SD = 1.08; 52.5% girls) participated in the study. Gambling severity was assessed using the adolescent-adapted version of the South Oaks Gambling Screen. Additionally, exposure and perceptions to gambling marketing were evaluated through an ad hoc questionnaire. Problematic gambling was found in 3.03% of the sample, with higher rates among males. Exposure to gambling marketing was reported by 64.3%, and 60.7% specifically via social media. Individuals with at-risk and problematic gambling were more likely to report exposure to gambling marketing. Finally, 53% of participants considered that gambling marketing influences gambling behavior, and 72% indicated that advertising should be regulated. These findings suggest that gambling marketing may play a significant role in adolescent gambling behavior. The high levels of exposure, combined with the increased vulnerability observed among those adolescents with at-risk and problematic gambling, highlight the need for regulating advertising targets or accessibility to adolescents.

**ИИ:** разошлись — Opus ? (неясно, есть ли ставки на спорт: Survey of Spanish adolescents using SOGS-RA that analyses gambling behaviour; abstract doesn't say whether sports betting participation was measured.); Sonnet + (игроки, есть ставки на спорт и инструмент: Adolescent school survey using SOGS-RA; likely reports gambling by activity including sports betting, so problem gambling among sports bettors may be extractable.)

**Решение:** ?

---

### 54 · R0577

**Development and psychometric validation of the Sports Betting Risk Index (SBRI-17): a novel screening instrument for pathological gambling risk in sports bettors**

2026 · PsyArXiv · article, preprint, posted-content · und · https://doi.org/10.31234/osf.io/yc4eb_v1

Background. Sports betting is the fastest-growing gambling modality globally, yet no validated screening instrument exists that is specifically calibrated for sports betting populations. Existing tools were developed for general gambling contexts and may not adequately capture the cognitive distortions and behavioural patterns distinctive to sports betting.Aims. To develop and psychometrically validate the Sports Betting Risk Index (SBRI-17), a brief screening instrument grounded in DSM-5 and ICD-11 diagnostic frameworks, designed to identify pathological gambling risk among sports bettors.Method. Items were derived from an integrated DSM-5/ICD-11 construct framework adapted for sports betting. An international online sample of active sports bettors (N = 954) completed the 24-item pool alongside the Short UPPS-P Impulsive Behaviour Scale. Analyses followed a split-half design: exploratory factor analysis (n = 477) identified a two-factor, 17-item structure; confirmatory factor analysis (n = 477, weighted least squares mean- and variance-adjusted estimation) cross-validated fit. Reliability, convergent and discriminant validity, measurement invariance, latent profile analysis, and item response theory analyses were conducted.Results. The two-factor model (Factor 1: Behavioural Pathology, 12 items; Factor 2: Cognitive Distortion, 5 items) demonstrated good fit (comparative fit index = 0.955, root mean square error of approximation = 0.043, 90% CI 0.034–0.052). Total scale reliability was strong (ω = .923). Behavioural Pathology correlated substantially with urgency facets of impulsivity (r = .50–.51). Cognitive Distortion was positively associated with self-reported win rate (ρ = .34), suggesting distorted cognition extends to self-report of betting outcomes. A cut-off of ≥13 identified 23.0% as at-risk (Cohen's d = 1.72). Item response theory indicated peak measurement precision at the recreational-to-problematic transition zone (θ = 0.17). Measurement invariance was supported across geographical regions.Conclusions. SBRI-17 is a brief, reliable, and valid screening instrument specifically calibrated for sports betting populations, with measurement precision optimised for early identification of pathological gambling risk.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Survey of 954 sports bettors using a new DSM-5-based scale; the abstract doesn't say whether an established instrument such as the PGSI was used.); Sonnet + (валидация инструмента: Validation of a new sports-betting risk screen in 954 active sports bettors; reports 23.0% at-risk using a cut-off, though the instrument is novel rather than established.)

**Решение:** +

---

### 55 · R0579

**Du territoire physique au territoire numérique : une approche socio-spatiale de l’addiction au pari sportif en ligne en Côte d’Ivoire**

2026 · European Scientific Journal ESJ · article · und · https://doi.org/10.19044/esj.2026.v22n11p121

L’avènement des technologies numériques a profondément redéfini les modalités des jeux d’argent, propulsant le pari sportif dans une ère de démocratisation et d’accessibilité sans précédent. En Côte d'Ivoire, cette transformation se manifeste par l’essor fulgurant des plate-formes de paris en ligne, générant des implications socio-spatiales complexes, notamment à Yamoussoukro, la capitale politique. Cet article propose une analyse de l’ancrage territorial de la vulnérabilité face au jeu, en explorant comment l’espace numérique (sites web, applications mobiles) interagit avec le territoire physique (quartiers, lieux de vie) pour produire de nouvelles formes d’addiction chez les jeunes parieurs. La méthodologie, basée sur une enquête qualitative et quantitative (entretiens semi-dirigés, questionnaires auprès de 150 parieurs obtenus par un échantillonnage non-probabiliste par convenance complété par une approche boule de neige, observations participantes), démontre une forte tendance addictive chez les jeunes Ivoiriens. L’étude a révélé que la dépendance au jeu pari sportif n'est pas uniforme dans la ville de Yamoussoukro. Elle présentait des disparités significatives selon le lieu d’habitation et le statut socio-économique des parieurs. Ces résultats mettent en lumière une véritable lecture territoriale du phénomène, où la précarité et l’accès différencié aux infrastructures (numériques et urbaines) modulent le risque addictif. L’article conclut sur la nécessité de politiques publiques adaptées à la prévention et la gestion de l’addiction au jeu en ligne. The advent of digital technologies has profoundly redefined the nature of gambling, propelling sports betting into an era of unprecedented democratization and accessibility. In the Ivory Coast, this transformation is manifested by the rapid rise of online betting platforms, generating complex socio-spatial implications, particularly in Yamoussoukro, the political capital. This article offers an analysis of the territorial roots of gambling vulnerability, exploring how the digital space (websites, mobile apps) interacts with the physical territory (neighborhoods, living spaces) to produce new forms of addiction among young bettors. The methodology, based on a qualitative and quantitative survey (semi-structured interviews, questionnaires administered to 150 bettors obtained through non-probabilistic convenience sampling supplemented by a snowball sampling approach, and participant observation), reveals a strong tendency toward addiction among young Ivorians. The study revealed that addiction to sports betting is not uniform across the city of Yamoussoukro. It showed significant disparities depending on the bettors’ place of residence and socioeconomic status. These findings highlight a genuine regional perspective on the phenomenon, in which precarious living conditions and unequal access to infrastructure (both digital and urban) influence the risk of addiction. The article concludes by emphasising the need for public policies tailored to the prevention and management of online gambling addiction.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Questionnaire survey of 150 online sports bettors that assesses addiction levels; the abstract does not say whether a standard instrument such as the PGSI was used.

**Решение:** =

---

### 56 · R0580

**Du Territoire Physique au Territoire Numérique: Une Lecture Socio-Spatiale et Technologique du Pari Sportif à Yamoussoukro**

2026 · European Scientific Journal ESJ · article, journalarticle, review · und · https://doi.org/10.19044/esipreprint.3.2026.p324

The advent of digital technologies has profoundly redefined the way gambling works, propelling sports betting into an era of unprecedented democratization and accessibility. In Côte d'Ivoire, this transformation is reflected in the rapid rise of online betting platforms, generating complex socio-spatial implications, particularly in Yamoussoukro, the political capital. This article offers an analysis of the territorial roots of vulnerability to gambling, exploring how the digital space interacts with the physical territory to produce new forms of addiction among young bettors. The methodology is based on documentary research and a field survey of 150 bettors. Above all, the study reveals that this addiction is not uniform; there are significant disparities depending on where bettors live and their socioeconomic status. These results highlight a truly territorial interpretation of the phenomenon, where precariousness and differentiated access to infrastructure modulate the risk of addiction. The article concludes with the need for public policies tailored to the prevention and management of online gambling addiction.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Field survey of 150 sports bettors in Yamoussoukro measuring addiction risk; the abstract doesn't say whether a validated instrument was used.

**Решение:** =

---

### 57 · R0585

**Gambling Problems in a Sample of UK University Students: Associations with Mental Health, Other Addictive Behaviours, and Transdiagnostic Factors**

2026 · Journal of Gambling Studies · article · en · https://doi.org/10.1007/s10899-026-10534-y

University students may be particularly vulnerable to experiencing gambling-related problems. This study investigated the rate of screening positive for gambling problems in a UK university and associated factors, including demographic, mental health, and trans-diagnostic variables. We analysed cross-sectional data from the Nurture-U student mental health and wellbeing survey (2022-2024 data; N = 2302). The 3 item NORC DSM-IV Screen (NODS-CLiP) was used to identify positive screen for gambling problems. Variables of interest were anxiety, depression, eating symptoms, self-reported ADHD, problematic use of the internet (PUI), hazardous alcohol use, drug use, compulsivity and suicide attempts. Logistic regression was conducted to examine associations between gambling problems and these measures. Overall, 8.1% of students screened positive for potential gambling problems. When considering associations with comorbid mental disorders and problematic behaviours, positive associations of moderate strength were observed between a positive screen for gambling problems and any drug use (OR 3.00 [95% Confidence Interval 2.09, 4.33]), restrictive eating (OR 2.74 [1.89, 3.99]), PUI (OR 1.04 [1.02, 1.07]) and hazardous drinking (OR 1.5 [1.03, 2.26]), but not for anxiety, depression, binge eating or ADHD. When considering transdiagnostic factors, suicide attempts (OR 2.61 [1.69, 4.04]) and standardised reward drive (OR 1.41 [1.16, 1.72]) were associated with screening positive for gambling problems, while standardised perfectionism had a protective effect (OR 0.59 [0.49, 0.71]). The findings of this study suggest that gambling problems may be common in university students and linked to impairments in reward-driven compulsive behavioural patterns that can extend beyond gambling.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Student survey used NODS-CLiP; abstract does not say whether sports betting participation was measured.

**Решение:** =

---

### 58 · R0587

**Exploring the Role of Masculinity in Gambling Behaviors and Responsible Gambling Among Emerging Adult Men**

2026 · Digital Scholarship - UNLV (University of Nevada Reno) · conference-paper

Emerging adulthood is a developmental period marked by increased autonomy and heightened vulnerability to risk-taking behaviors, including gambling. Young men experience disproportionately higher gambling involvement and harm, particularly in socially embedded contexts such as sports betting. Masculine socialization—emphasizing risk-taking, competitiveness, and emotional control—may play an important role in shaping gambling behavior and engagement with responsible gambling (RG) strategies, yet remains understudied. This study examined associations between conformity to traditional masculine norms, RG strategy use, and problem gambling severity among emerging adult men. Participants were 593 men who gambled in the past month and were primarily white, heterosexual, unmarried, and college-educated, with an average age of 24.84. A survey assessment assessing masculinity, gambling involvement, RG strategy use, and gambling-related harm was used. As predicted, greater conformity to traditional masculine norms was positively associated with problem gambling severity and negatively associated with engagement in RG strategies. These findings suggest that masculinity may function as a psychological risk factor for gambling-related harm while also acting as a barrier to protective behaviors. This presentation also explores whether gambling engagement and problems moderate the association between masculine norm conformity and RG strategy use.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Survey of 593 past-month gambling men measuring problem gambling severity; sports betting is mentioned, but it's unclear whether participation was measured by activity.

**Решение:** =

---

### 59 · R0588

**Trustworthiness of responsible gambling ads: How sponsor type and message framing affect emerging adults who sports bet.**

2026 · Psychology of addictive behaviors : journal of the Society of Psychologists in Addictive Behaviors · journal article, randomized controlled trial, journalarticle · eng · https://doi.org/10.1037/adb0001177

Objective Sports betting is a common activity for emerging adults (ages 18-29) and is associated with financial harm, academic decline, and psychological distress. Responsible gambling (RG) messages aim to mitigate such harms, but generic slogans like "gamble responsibly" often lack actionable guidance and credibility, particularly when sponsored by gambling operators. Drawing from Cialdini's theoretical framework of persuasion, this study experimentally examined how RG advertisement message framing (generic vs. self-appraisal) and sponsor type (sportsbook vs. State Department of Health) influenced perceived trust in the advertisement, behavioral intentions, and gambling desire among emerging adult sports bettors. Method A total of 255 crowdsourced participants ( M age = 24.77; 47.8% men, 48.2% women) were randomly assigned to view one of four 20-s RG video advertisements varying by sponsor type and framing. Measures included perceived trustworthiness, personal responsibility toward RG, intentions to sports bet and engage in RG, and gambling desire. Results Sponsor type significantly influenced the perceived trustworthiness of the advertisement, with Department of Health-sponsored ads rated as more trustworthy than sportsbook-sponsored ads. There was no significant interaction between sponsor type and message framing, and message framing did not significantly influence trust. Additionally, neither sponsor type nor framing significantly affected personal responsibility toward RG, intentions to sports bet or engage in RG, or gambling desire. Conclusions Findings indicate that while Department of Health advertisements enhance perceived trustworthiness, these effects did not translate into changes in behavioral intentions or gambling desire. Results highlight the importance of message source within RG communications. (PsycInfo Database Record (c) 2026 APA, all rights reserved).

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Experiment with emerging adult sports bettors; the abstract doesn't mention PGSI, though it may appear in the sample description.

**Решение:** =

---

### 60 · R0597

**Problem gambling among working youth in Southeast Türkiye: predictors and psychological consequences.**

2026 · BMC public health · article, journal article, journalarticle · eng · https://doi.org/10.1186/s12889-026-26878-4

Abstract Background In low-socioeconomic contexts like South-eastern Türkiye, where child labor rates exceed national averages due to economic pressures, working youth face amplified risks of gambling as a maladaptive coping mechanism. The present study was conducted to identify gambling addiction, predictors and psychological consequences among working youth in the South-eastern Anatolia Region of Türkiye. Methods This cross-sectional and descriptive study, which was planned in accordance with STROBE guidelines, was conducted between 01.04.2024 and 31.12.2024 with youth working on the streets of Şanlıurfa and Diyarbakır for more than two years. Ethical approval was obtained from the university and institutional permission was obtained from the governor's office in the province where the study was conducted. After explaining the study to each adolescent and parent, informed consent was obtained from all adolescents and parents. The study was conducted with 671 working youth who met the specified inclusion criteria. Regression analysis and mediation models were used in the analyses. Results It was found that 18% (122) of the adolescents working on the street played rummikub, 25% (171) played billiards or bowling for money once a week, 32% (217) played iddaa (official football betting game), 17% (112) betted on horse racing, 11% (72) bought numerical lotto tickets, 33% (223) played scratch card games and 23% (152) played online games every week in the last 12 months. Strengths and Difficulties Questionnaire score had a negative statistical effect on multidimensional perceived social support scale (β1 = -0.973), and a positive statistical effect on depressive symptoms (β1 = 0.690) and anxiety symptoms (β1 = 0.726). The change of 60.2% of the scores in the gambling screening test was explained by depressive symptoms, anxiety symptoms and multidimensional perceived social support scores (R 2 = 0.602). More than half of the gambling screening test was explained by these three variables. Conclusions Current evidence indicates that culturally sensitive, enhanced social support could alleviate symptoms of depression and anxiety associated with gambling behaviour. However, randomised controlled trials (RCTs) are needed to establish causality and the clinical efficacy of this relationship definitively. Therefore, future policy frameworks must balance methodological rigour and robust evidence generation with advocacy for the potential role of such interventions.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Survey of working youth measured iddaa football betting participation and used a gambling screening test; it could report problem gambling among bettors.

**Решение:** =

---

### 61 · R0604

**Trajectories of unemployment and sport betting on antisocial behaviour among youth in Nigeria: demystifying the myth**

2026 · Alvan Journal of Social Sciences · journalarticle · https://doi.org/10.67638/ajss-2026-v3-i2-005

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; title suggests possible survey of Nigerian youth sports bettors, unclear whether a problem-gambling instrument was used.

**Решение:** =

---

### 62 · R0605

**APOSTAS ESPORTIVAS: UMA ANÁLISE DA AVERSÃO À PERDA EM DISCENTES DE GRADUAÇÃO EM UMA UNIVERSIDADE DO OESTE DE SANTA CATARINA**

2026 · Anuário Pesquisa e Extensão Unoesc Joaçaba · article · pt

O presente estudo teve como objetivo analisar de que forma a aversão à perda influencia o comportamento dos estudantes de graduação em Ciências Contábeis de uma Universidade do Oeste de Santa Catarina em relação às apostas esportivas. Para tal, realizou-se uma pesquisa descritiva, de abordagem quantitativa, utilizando-se de um questionário estruturado aplicado aos acadêmicos do curso (survey). A população da pesquisa compreendeu os acadêmicos do curso de Ciências Contábeis da Universidade do Oeste de Santa Catarina (UNOESC), campus de Joaçaba-SC, totalizando 153 alunos. A amostra da pesquisa foi composta por 108 respondentes, representando 70,53% da população total. Os dados utilizados no estudo foram coletados a partir de uma entrevista estruturada, com perguntas fechadas. Esse roteiro foi dividido em cinco partes, sendo elas: Bloco I - Perfil do respondente; Bloco 2 - Frequência de participação; Bloco 3 - Motivações e comportamentos; Bloco 4 - Gastos e resultados em apostas e Bloco 5 - Avaliação de aversão à perda. O questionário foi aplicado aos acadêmicos no mês de agosto de 2025. Os dados foram tabulados e analisados por meio de estatística descritiva, com uso do software IBM SPSS Statistics. Os resultados demonstram uma a baixa adesão dos participantes às apostas esportivas, uma vez que 73,15% declararam nunca ter apostado e, ainda 87,96% dos estudantes nunca destinaram recursos a apostas esportivas. Também foi constatada a ausência de comportamentos viciosos ou problemáticos relacionados a essa prática, posto que esses percentuais ficaram em torno de 0,93%.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Student survey on sports betting reports problematic behaviour (~0.93%), but unclear whether a validated problem-gambling instrument was used.

**Решение:** =

---

### 63 · R0610

**Gambling behavior among adolescent and young recreational athletes: the role of gender, gambling modality, and sport characteristics.**

2026 · Psychology, health & medicine · journal article, journalarticle, article · eng · https://doi.org/10.1080/13548506.2026.2659696

Adolescence and youth are periods of increased vulnerability to risk behaviors, including gambling, particularly among athletes. The present study aimed to examine 1) the prevalence and severity of gambling, 2) gender differences in gambling-related behaviors, and 3) associations between sport modality, betting on one's own sport, and engagement in specific gambling activities with gambling severity and motives among recreational athletes. The sample consisted of 244 athletes aged 15 to 35 years ( M = 20.58, SD = 4.58), of whom 68% were male. Gambling severity and motives were assessed, along with sport type, involvement in different modalities of gambling activities, and betting on the sport they practiced. Results indicated that 73% of the participants had gambled in their lifetime, and 16.3% presented at-risk or problem gambling behaviors. Males showed higher involvement in strategic and online gambling, higher gambling severity, and stronger gambling motives than females. Regression analyses indicated that online gambling, card games, and sports betting were associated with higher gambling severity. Furthermore, betting on own's sport and participation in specific gambling types (particularly slot machines) were related to higher enhancement, social, coping, and financial motives. Early identification of at-risk athletes, with attention to gender differences in gambling behaviors and motives, may help in developing tailored educational and preventive strategies within recreational sports environments.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Survey of athletes that measured gambling severity (at-risk/problem gambling) and participation in sports betting, including betting on their own sport.

**Решение:** =

---

### 64 · R0617

**Effect of Sports Betting and its Potential Risk on Emotional Control and Entertainment of Players**

2026 · Advance Social Science Archive Journal · article, journalarticle/ · en · https://doi.org/10.5281/zenodo.20315560

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; title suggests a possible survey of sports bettors on risk and emotional control, problem-gambling measure unknown.

**Решение:** =

---

### 65 · R0622

**Sports Betting Behaviour in Portugal: A Descriptive and Bivariate Statistical Analysis of Betting Patterns, Profiles and Associated Factors Using SPSS**

2026 · Unpublished · other literature type, text/research proposal, article · pt · https://doi.org/10.13140/rg.2.2.33025.42089

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the title points to a quantitative survey of Portuguese sports bettors, and it's unknown whether problem gambling was measured.

**Решение:** =

---

### 66 · R0627

**Prevalence, Patterns, and Sociodemographic Determinants of Gambling Participation Among Community Adults in Urban Nigeria: A Cross-Sectional Study from Obio-Akpor, Rivers State**

2026 · Research Square · article, preprint · und · https://doi.org/10.21203/rs.3.rs-9800243/v1

Abstract Background Nigeria has experienced rapid expansion of mobile sports betting, yet community-level data on gambling prevalence, patterns, and sociodemographic determinants in the South-South geopolitical zone are entirely absent. This study examined gambling participation, primary gambling type, frequency, expenditure, and their sociodemographic correlates among adults in Obio-Akpor Local Government Area (LGA), Rivers State. Methods A quantitative cross-sectional survey was conducted in six wards of Obio-Akpor LGA using multistage sampling. A total of 468 adults participated (response rate 93.2%). Gambling prevalence, type, frequency, and weekly expenditure were assessed via structured questionnaire. Chi-square tests examined sociodemographic associations; binary logistic regression identified independent predictors of gambling participation. Ethics approval: UPH/CEREMAD/REC/MM118/087. Results Twelve-month gambling prevalence was 31.2% (n = 144/461). Sports betting predominated (49.6%), followed by online applications (34.8%). Daily gambling was reported by 40.3% of gamblers; 29.4% spent ₦10,000–19,999 weekly, representing 57–114% of weekly income for the lowest earners. Gender (χ²=36.815, p &lt; 0.001), educational attainment (χ²=7.369, p = 0.025), and monthly income (χ²=10.019, p = 0.018) were significantly associated with gambling participation. After adjustment, male gender was the sole independent predictor (AOR = 3.76; 95% CI: 2.36–6.01; p &lt; 0.001). Conclusion Gambling is prevalent and financially intensive in Obio-Akpor, disproportionately affecting educated young men. Findings support urgent regulatory reform, targeted digital prevention, and integration of gambling screening into primary care in Rivers State.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Community adult survey in which sports betting predominates; the abstract lists only prevalence, frequency and expenditure, so a problem-gambling instrument is uncertain.

**Решение:** =

---

### 67 · R0642

**1XBET addiction at general Lansana conte university of Sonfonia-Conakry: Scope of analysis of university results**

2026 · World Journal of Advanced Research and Reviews · article, journalarticle, review · und · https://doi.org/10.30574/wjarr.2026.30.3.1707

This study aims to identify the factors explaining 1xbet addiction among students at the General Lansana Conté University of Sonfonia, Conakry, and to analyze the effects of 1xbet addiction on their academic performance. To this end, a quantitative survey was conducted with 325 student gamblers at the General Lansana Conté University of Sonfonia, Conakry. To better define the scope of this study, we used the Sharpe and Tarrier model (1993). We were thus able to show that the hope of quick profits, the pursuit of easy money, social influence, aggressive advertising from betting platforms, bonus offers, and financial incentives are the factors that explain 1xbet addiction among students at the General Lansana Conté University of Sonfonia, Conakry. Furthermore, this game has enormous consequences for these students on a social level (social isolation, sleep disorders, delinquency, theft, etc.); a financial level (financial ruin, debt, even over-indebtedness, etc.); and an academic level, as they devote most of their time to placing bets at the expense of their studies; this is the root cause of the failures observed in university settings. To better guide them regarding the risks associated with online sports betting addiction, several suggestions have been made, the most essential of which are: organizing awareness sessions on the risks associated with sports betting; integrating financial education programs into students' curricula; encouraging the practice of sports, cultural, or artistic activities to entertain students and offer them healthy alternatives to sports betting; and controlling access to online betting platforms.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Quantitative survey of 325 student 1xbet sports bettors about "addiction"; the abstract doesn't say whether a problem-gambling instrument was used.

**Решение:** =

---

### 68 · R0644

**Online sports gambling and financial wellbeing in the United States**

2026 · Journal of Financial Literacy and Wellbeing · journalarticle, review, article · en · https://doi.org/10.1017/flw.2026.10009

Abstract Online sports gambling expanded rapidly in the United States since 2018. This article uses a nationally representative sample survey in early 2025 to measure who is gambling, how much, and online sports gambling’s association with financial wellbeing and decision-making. Gambling in a casino was still more common than online sports gambling in early 2025, but the populations appear distinct, suggesting that sports gambling rapidly expanded the gambling population. Three-quarters of online sports gamblers were male. They were typically younger and had higher incomes than either non-gamblers or casino gamblers. Sports gambling was not statistically associated with lower financial wellbeing or a higher likelihood of difficulty paying bills but was associated with higher rates of revolving credit card debt and did cause some financial distress. One-third of sports gamblers engaged in high-intensity gambling which could indicate problems. Sports gamblers rated their ability to make complex financial decisions higher than non-gamblers, yet they were more impatient and more likely to be overconfident.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Nationally representative US survey of online sports gamblers; 'high-intensity gambling' may not come from a validated problem-gambling instrument.

**Решение:** =

---

### 69 · R0648

**What Bettors Don't Know About Their Own Betting: A Programme of Research Using Matched Behavioural and Self-Report Data to Examine the Limits of Informed Decision-Making in Online Sports Wagering**

2026 · Digital Scholarship - UNLV (University of Nevada Reno) · conference-paper

Informed decision-making is a foundational assumption of consumer protection frameworks for online gambling, yet the conditions required to support it are rarely examined empirically. This talk presents a programme of research investigating the cognitive, behavioural, and socioeconomic factors that systematically undermine awareness and decision-making in online sports wagering. Drawing on a series of studies that uniquely combine transaction-level behavioural account data with matched self-report measures, we examine how bettors estimate their own expenditure, respond to wins, losses, and liquidity shocks, and differ in self-control awareness across problem gambling severity levels and socioeconomic groups. Findings demonstrate systematic and predictable failures of financial self-awareness that are most pronounced among those at greatest risk of harm. We also present an evaluation of government-mandated strategies designed to enhance spending awareness, assessing their impact on both self-reported and objectively measured behaviour. Implications for the design of harm minimisation frameworks are discussed, with attention to the structural conditions under which informed decision-making can be meaningfully supported rather than assumed.

**ИИ:** + · обе модели · беттеры + инструмент · Conference talk on online sports bettors with matched self-report data that compares them by problem gambling severity level, so a screening instrument was likely used.

**Решение:** =

---

### 70 · R0656

**Effects of Lottery Games on Students' University Education in Arusha Region, Tanzania**

2026 · Journal of Research Innovation and Implications in Education · article · eng · https://doi.org/10.59765/prd2t5

This study investigated the effects of lottery games on students' university education in Arusha region. Objectives were to: examine the extent to which lottery games affect university students’ education and find out possible measures to minimize the effects of lottery games on University Students' education. Entertainment Utility Theory and convergent mixed method design guided the study. The target population included 5 deans of students and 1002 students from 5 universities in Arusha region. The sample size of 205 comprised of 200 students and 5 deans of students. Questionnaires and interview guide were used to collect data. Simple random sampling was employed to sample students while the deans of students were selected purposively. Validity was established through expert review while reliability was determined using Cronbach’s Alpha and the coefficient value was r=0.67. While the trustworthiness of instrument for collecting qualitative data was done through peer debriefing. The data from quantitative data were analyzed using descriptive statistics in SPSS version 23 and presented in tables. Qualitative data was presented in themes alongside research questions. The results show that participating in lottery games such as aviator, sports betting and casino games negatively affects students’ university education. In conclusion, students who are addicted to lottery games participation are likely to be distracted from their educational goals. The study recommends that self-awareness, provision of education on effects of lottery games, regulations and limits of purchasing lottery tickets by the gaming boards is useful to reduce the risks associated with lottery games.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Student survey covering sports betting and mentioning addiction, but the questionnaire looks self-developed; no standard problem-gambling instrument is named.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Mixed-method student survey on effects of lottery/betting on education; no problem-gambling instrument or prevalence among sports bettors is mentioned.)

**Решение:** ?

---

### 71 · R0658

**APUESTAS DEPORTIVAS ONLINE Y JÓVENES**

2026 · BURJC Digital (King Juan Carlos University) · dissertation · es

Trabajo Fin de Grado leído en la Universidad Rey Juan Carlos en el curso académico 2025/2026. Directores/as: Yolanda Ortiz De Guinea Ayala

**ИИ:** ? · обе модели · нет аннотации · Undergraduate thesis on online sports betting and young people; no abstract, so design and any problem-gambling measure are unknown.

**Решение:** =

---

### 72 · R0660

**Identifying the Socio-Emotional and Mental Health Correlates of Online Sports Betting Among Late Adolescent Boys.**

2026 · Journal of adolescence · article, journal article, journalarticle · eng · https://doi.org/10.1002/jad.70215

ABSTRACT Introduction Online sports betting is emerging as a novel form of gambling, particularly popular among late adolescent boys, ages 18–25. While the socioemotional determinants of traditional forms of gambling are generally understood, less is known about how these correlate with online sports betting behavior and whether online sports betting recency relate to mental health outcomes. Methods Online questionnaires were used to assess late adolescent boys' social lives, emotional functioning, mental health, and online sports betting behavior. Results Path analysis reveal that college enrollment, participation in social gaming, and higher life satisfaction were related to more recent online sports betting. Online sports betting recency was not related but depression or anxiety symptoms. Conclusions With nearly half (47%) having participated, online sports betting was highly prevalent. Several key social and emotion factors are related to online sports betting recency among late adolescent boys. Contrary to expectations, there were no links with depression or anxiety.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of young men on online sports betting and mental health; the abstract doesn't say whether a problem-gambling instrument was used.

**Решение:** =

---

### 73 · R0664

**Assessment of gambling perspectives amongst elite Irish athletes; A qualitative analysis.**

2026 · Irish journal of medical science · journal article · eng · https://doi.org/10.1007/s11845-025-04179-w

Problem gambling levels amongst elite athletes are above the populational baseline. These elevated rates may lead to increased financial and emotional strain. The aims of this study were to provide a qualitative analysis of elite GAA players on the impact of gambling in the GAA. An anonymous web-based questionnaire was distributed amongst elite Irish sports players. In a previous paper, we showed high problem gambling rates (5%) in this cohort (n = 608) compared to the general Irish population (1%). Problem gamblers were more likely to be male, smokers and less likely to have completed university. In this study, we qualitatively assess the impact of gambling on this cohort by analysing the free text comments of players. 68 comments were included for analysis. A majority (n = 43, 63%) of respondents shared opinions regarding harms related to gambling. Other prevalent themes included gambling as an issue amongst elite Irish athletes (n = 32, 47%), gambling sponsorship of sports (n = 20, 29%), individual responsibility (n = 5, 7%), need for education on the topic (n = 5, 7%), dangers of online gambling (n = 4, 6%) and role of players representative body in combatting gambling issues (n = 4, 6%). These responses corroborate what is the concerning role of gambling in elite sports and suggest potential interventions to address the issue.

**ИИ:** ? · обе модели · другое · Qualitative analysis of free-text comments, but from an athlete survey (n=608) that measured problem gambling; sample tables may report sports betting.

**Решение:** =

---

### 74 · R0670

**Αξιοποίηση Τεχνητής Νοημοσύνης για υποστήριξη αποφάσεων στο αθλητικό στοίχημα: Μια προσέγγιση από την οπτική του παίκτη**

2026 · National Technological University of Athens · other/other · https://doi.org/10.26240/heal.ntua.32523

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: Engineering thesis on AI decision support for sports betting; looks like a prediction or strategy tool, not a problem-gambling survey.); Sonnet ? (нет аннотации: Greek thesis on AI decision support in sports betting from the player's perspective; no abstract, so it's unclear whether bettors were surveyed with a problem-gambling measure.)

**Решение:** -

---

### 75 · R0673

**Gambling Involvement and Problem Gambling: Findings from a General Population Survey**

2026 · conference object · und

Certain gambling formats, such as slot machines, have consistently been related to problem gambling. Extensive involvement in multiple gambling activities may also represent an important risk factor. This study explored the relationship between gambling involvement, gambling formats, and problem gambling in a subsample of 817 participants who reported engaging in gambling in the past month, drawn from a representative sample of Croatian residents aged 15-64 (N=4,988), Gambling involvement was assessed by the number of gambling formats and frequency of gambling in the past month, while problem gambling was assessed using the Problem Gambling Severity Index. Most participants (37.3%) engaged in one, 26.8% in two, 21.4% in three, and 14.5% in four or more gambling formats. Overall, 67.4% of participants were classified as non-problem, 10.1% as low-risk, 14.0% as moderate-risk, and 8.5% as participants with problem gambling. High gambling involvement was related to problem gambling, and frequent sports betting, casino games, and slot machines use. Participants with problem gambling most commonly engaged in four or more gambling formats. Findings suggest problem gambling is related not only to specific gambling formats but also to patterns of extensive and frequent involvement in multiple gambling activities, highlighting the importance of monitoring overall gambling behavior rather than focusing on specific games to identify high-risk individuals and inform prevention efforts.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Croatian general population survey; PGSI measured and sports betting frequency analysed among past-month gamblers.

**Решение:** =

---

### 76 · R0678

**“I’m probably not a bookie’s dream”: A Think-Aloud Study of Dark Patterns and Self-Control Strategies in Online Sports Betting**

2026 · OSF Preprints (OSF Preprints) · preprint

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: Think-aloud study of dark patterns and self-control in online sports betting; qualitative design, not a quantitative survey.); Sonnet ? (нет аннотации: No abstract; think-aloud study of sports bettors is mainly qualitative, but participant description might include PGSI scores, so full text check is worthwhile.)

**Решение:** ?

---

### 77 · R0687

**The relationship of gambling disorder to obsessive-compulsive disorder.**

2026 · CNS spectrums · journal article, journalarticle, review · eng · https://doi.org/10.1017/s109285292610114x

Abstract Objective Gambling disorder frequently co-occurs with other psychiatric conditions, yet its relationship with obsessive-compulsive disorder (OCD) remains unclear. Emerging evidence suggests impulsivity and compulsivity may be inter-related rather than diametrically opposed constructs, warranting investigation of their clinical overlap. The aim of this study is to examine the rate of gambling disorder in adults with OCD and to explore associated clinical, behavioral, and treatment-related characteristics. Methods Adults with probable OCD were recruited via online Reddit groups for OCD, OCD clinics, and support groups and completed a cross-sectional survey. OCD symptom types were assessed using the Obsessive-Compulsive Inventory-Revised, and gambling disorder was identified using the Minnesota Impulsive Disorders Interview. Additional measures included gambling severity, impulsivity, and problematic internet use. Group comparisons were conducted between participants with and without gambling disorder. Results Among 186 adults with OCD, 34 (18.8%) met criteria for gambling disorder. Individuals with comorbid gambling disorder demonstrated significantly greater OCD severity, particularly in ordering, checking, and neutralizing symptoms, and reported later onset of OCD. The comorbid group showed higher impulsivity, greater problematic internet use, and distinct gambling behaviors, including higher rates of online gambling, esports betting, and use of artificial intelligence tools for gambling. They were also less likely to have received pharmacological treatment for OCD. Conclusions Gambling disorder in adults with OCD is associated with distinct clinical characteristics, greater impulsivity, problematic internet use, and concerning treatment gaps. These findings highlight the importance of screening for gambling in OCD, and vice versa, and suggest a need for integrated treatment approaches.

**ИИ:** разошлись — Opus + (игроки, есть ставки на спорт и инструмент: OCD sample survey; gambling disorder assessed via MIDI interview, with esports betting compared between groups with and without gambling disorder.); Sonnet ? (неясно, есть ли ставки на спорт: Survey of adults with OCD using a gambling disorder interview; esports betting reported by group, but unclear if gambling disorder rates among sports bettors can be extracted.)

**Решение:** ?

---

### 78 · R0689

**Betting on risk: applying perceived risk theory to online sport betting across bettor and non-bettor segments**

2026 · Sport Management Review · journalarticle, article, journal-article · en · https://doi.org/10.1080/14413523.2026.2728223

The explosive growth of online sport betting has created a novel consumption context that challenges the direct application of established consumer behavior frameworks. This study applies perceived risk theory to online sport betting by examining the relationship among consumer confusion, perceived risk, and behavioral intentions across two distinct consumer groups: active sport bettors (n = 250) and non-betting sport fans (n = 249). Data were collected via an online panel of U.S. residents from states with legalized sport wagering in November of 2023. Structural equation modeling and MANOVA results revealed perceived risk theory’s core risk-deterrence assumption held for non-bettors: consumer confusion increased perceived risk, which strongly deterred behavioral intentions. However, among experienced sport bettors, while confusion increased perceived risk, perceived risk had no significant association with intentions. Betting frequency also moderated this association, although the modest effect should be interpreted cautiously. These findings indicate heterogeneity in the association between perceived risk and behavioral intentions across and within the study’s betting segments. Practically, risk-based responsible gambling communications may not align equally well with the intention formation of active sport bettors and non-betting sport fans.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · US survey of 250 active sports bettors on perceived risk; abstract doesn't say if a problem-gambling screen (e.g., PGSI) was used.

**Решение:** =

---

### 79 · R0696

**Gambling Purchase Demand and Drift-Diffusion Modelling of Value-Based Decisions**

2026 · OSF Registries · studyregistration/pre-registration, preprint · https://doi.org/10.17605/osf.io/7gyd2

Gambling is highly prevalent in the UK and is associated with substantial harms at population level. According to the Gambling Survey for Great Britain (GSGB) Year 2 (2024), nearly half of adults (48%) gambled in the past four weeks, including lottery participation. Online gambling is particularly widespread, with 38% of adults reporting online gambling activity in the past four weeks, including sports betting, online slots, and instant win games. Gambling-related harm affects a large proportion of the population. Based on the Problem Gambling Severity Index (PGSI), 8.8% of adults scored 1–2 (low risk), 3.1% scored 3–7 (moderate risk), and 2.7% scored 8 or above, indicating severe gambling problems (GSGB Year 2, 2024). These harms extend beyond financial losses, to relationship difficulties, psychological distress, and suicidality (Trezza &amp; Popp, 2000). In order to understand why individuals continue to gamble despite escalating costs and harms, research in addiction has used two behavioural paradigms. First, purchase tasks quantify the value of a commodity from hypothetical consumption across increasing prices (Murphy &amp; MacKillop, 2006). Second, value-based decision-making (VBDM) tasks measure how people make repeated choices between alternatives that differ in subjective value (Berkman et al., 2017). By employing computational models (e.g. drift-diffusion modelling), the task demonstrates how value affects decision making processes. In previous alcohol and tobacco research, both purchase tasks and VBDM tasks were used to measure the demand across increasing cost and trial-level decision-making dynamics (Copeland et al., 2022, 2023). However, gambling studies have not integrated behavioural economic measures with VBDM tasks within the same participants. The present study addresses this gap by combining a Gambling Purchase Task (GPT) with a VBDM task in a gambling context. Participants will complete a GPT assessing gambling demand with increasing costs, and a repeated choice task measuring value-based preferences and reaction times. Additionally, individual difference measures such as PGSI scores and gambling motive scores will be collected.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Pre-registered experimental study of gamblers that collects PGSI; unclear whether participation in sports betting is recorded.

**Решение:** =

---

### 80 · R0697

**Gambling-Related Individual Differences and Decision-Making During the 2026 FIFA World Cup**

2026 · OSF Registries · studyregistration/pre-registration, preprint · https://doi.org/10.17605/osf.io/pafsg

Sports betting is one of the most common and rapidly growing forms of gambling, and is associated with gambling-related harm. Compared to other forms of gambling, sports betting is particularly strongly linked to problem gambling severity, an effect thought to be driven by the breadth of betting engagement and the structural characteristics of sports betting products (e.g. frequent betting opportunities and real-time odds fluctuations), which increase addictive potential (Newall et al., 2021; Grubbs &amp; Kraus, 2023). Major international football tournaments such as the FIFA World Cup are associated with marked increases in sports betting participation and gambling-related harm (Sharman et al., 2023), making them an ecologically relevant context in which to study gambling-related cognition. Problem gambling has been linked to a range of cognitive vulnerabilities, including impulsivity and disrupted valuation of gambling-related outcomes (Zhang &amp; Clark, 2020). Within a value-based decision-making (VBDM) framework, choices reflect the evidence accumulation process in which options are evaluated according to their expected value, with decision speed and accuracy indexing the relative value attributed to available options (Ratcliff et al., 2016). The present study examines whether gambling-related individual differences (e.g. gambling severity, sports betting frequency, and intention to bet on the World Cup) are associated with decision accuracy and reaction time, and other VBDM parameters (i.e. drift rate, boundary separation, non-decision time) when choosing between FIFA World Cup teams that differ in objective ranking, and whether any such associations are specific to football-related relative to neutral stimuli.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Pre-registration measuring gambling severity and sports betting frequency; instrument not named and no data yet; linked article could report PG among bettors.

**Решение:** =

---

### 81 · R0710

**The Rise of Online Gambling and Its Impact on College Students**

2026 · SUNY Digital Repository Support (State University of New York System) · other · en

Sports gambling has grown in popularity since it was legalized in numerous states following the 2018 Supreme rule in Murphy v. NCAA , generating serious concerns among college students. This paper contends this rapid growth and associated risks, such as financial stress, mental health issues and behavioral differences among students and athletes.

**ИИ:** разошлись — Opus -1 (обзор, комментарий, теоретическая, правовая или регуляторная работа: Argumentative repository paper on sports gambling risks for college students; nothing suggests a survey or a problem-gambling instrument.); Sonnet ? (другое: Student thesis/paper on sports gambling in college students; abstract is vague and may be a narrative review, so empirical data and problem-gambling measures are unclear.)

**Решение:** ?

---

### 82 · R0712

**A Cross-Sectional Examination of the Relationships Between Sports and Race Betting Motives, Expenditure, Problem Severity, and Harm in Young Australian Adults.**

2026 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-026-10533-z

Abstract Sports and race betting are high-risk gambling activities used by young adults, yet limited research has examined how motives relate to outcomes assessed separately for each betting activity. This online survey examined associations between sports- and race-specific betting motives (enhancement, financial, social, coping) and betting expenditure, problem severity, and harm among young Australian adults. The sample comprised 188 participants aged 18-30 years (84.6% male; M age = 24.11), including 185 sports betting participants and 127 race betting participants (defined as ≥2 bets in the past month and in a typical month over the past year). Separate linear regressions showed that financial motives were positively associated with sports betting expenditure (β = .16, p = .006), with no associations for race betting expenditure. Financial and coping motives were independently, positively associated with sports and race betting problem severity (sports: financial β = .34; coping β = .39; race: financial β = .19; coping β = .46) and harm (sports: financial β = .23; coping β = .47; race: financial β =.22; coping β = .49) in multivariable models (all p ≤ .004), demonstrating small-to-moderate associations for financial motives and moderate associations for coping motives. At the univariable level, social motives were positively associated with sports betting problem severity (β = .19, p = .007), and enhancement motives were positively associated with race betting problem severity (β = .32, p = .001). Findings highlight financial and coping motives as potential targets for early identification and prevention of harmful betting among young adults.

**ИИ:** + · обе модели · беттеры + инструмент · Survey of 185 young Australian sports bettors that assessed sports betting problem severity, probably with a PGSI-type instrument.

**Решение:** =

---

### 83 · R0714

**Development of lower-risk guidelines for online sports and race betting in Australia using objective behavioural data.**

2026 · Harm reduction journal · journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1186/s12954-026-01402-4

Lower risk gambling guidelines provide clear, actionable advice for reducing the risk associated with gambling by specifying behaviour associated with non-harmful use. Here we aimed to develop lower-risk guidelines specific to online sports and race betting in Australia that Currie (Addiction 112:2011-20, 2017) captured behaviours unique to this activity associated with high risk of experiencing gambling harms (e.g., depositing frequency, number of sports & races bet on) and Currie (Health Promot 34:1207-17, 2019) were based on objective behavioural data from a gambling operator not subject to self-report inaccuracies. Customers from two large online wagering sites in Australia owned by the same parent company were invited to take part in a survey including the Problem Gambling Severity Index (PGSI) and the Gambling Harm Measure (GHM). Survey responses were matched to customer's account data provided by the operator, including all bets and transactions placed six months before and after the survey. The final sample consisted of 1,647 participants (84.6% male; mean age = 44.1). Receiver Operating Characteristic curve analyses were used to identify optimal threshold values for PGSI and GHM harm separately across eight behavioural indicators: frequency, spend, percentage of household income spent, number of different sports/races bet on, deposit frequency, deposit amount, percentage of household income deposited, and number of active wagering accounts (self-reported). All indicators had acceptable Area Under the Curve values (AUC; ≥ 0.6) except gambling frequency. Optimal threshold values were higher for GHM than PGSI harm, and higher than those established in studies using self-report data (e.g., ≤ 6% vs. ≤ 1% of monthly income spent) irrespective of the measure of harm. A dose-response relationship was observed, whereby surpassing more limits was generally associated with greater odds of reporting harm. Our findings provide preliminary support for the following Lower-Risk Guidelines for Online Sports and Race Betting in Australia: Currie (Addiction 112:2011-20, 2017) make no more than four deposits per month, Currie (Health Promot 34:1207-17, 2019) deposit no more than 2% of your pre-tax household income per month, Rockloff (J Gambl Stud 28: 207-16, 2012) bet with no more than two different sites or apps, and as reported by National Health and Medical Research Council (Australian guidelines to reduce health risks from drinking alcohol, Commonwealth of Australia Canberra, 2020) stick to betting on four or fewer different types of sports or races. We strongly encourage further evaluation and testing of these guidelines to confirm their value across samples and over time.

**ИИ:** + · обе модели · беттеры + инструмент · Survey of 1,647 online sports and race betting customers in Australia that used the PGSI alongside matched account data.

**Решение:** =

---

### 84 · R0715

**Predicting problem gambling among online sports and race bettors: Assessing the value of machine learning using behavioural and self-reported data.**

2026 · Journal of behavioral addictions · journal article · eng · https://doi.org/10.1556/2006.2025.00525

Online gambling operators collect detailed behavioural data that can identify customers at risk of harmful gambling. However, there is limited clarity on how to optimally achieve this in practice, including which variables are most useful and whether short-term data windows are sufficient for risk detection. These details are increasingly important as regulatory frameworks emphasise timely intervention. We examined the value of machine learning in this context by comparing models trained on 30 days versus six months of behavioural data and exploring whether incorporating survey responses enhanced performance. Customers from two Australian sports and race betting sites (N = 1,470) completed a survey including the Problem Gambling Severity Index (PGSI) and measures of employment, income, gambling satisfaction, and number of gambling accounts. We built machine learning models to classify participants into risk groups (PGSI 1-7 [no-to-moderate-risk] vs. PGSI≥8 [high-risk]), comparing performance across data windows (30 days vs. six months), and with or without survey variables. Models using only behavioural data achieved adequate classification accuracy (AUROC = 0.74-0.75), with similar performance across 30-day and six-month windows. The most predictive account-based variables were age, deposits per active day, average stake, and days since betting. Combining behavioural data with self-reported variables enhanced performance (AUROC = 0.76-0.85). Two self-reported variables-number of gambling accounts held and gambling satisfaction-were primarily responsible for these improvements. Machine learning models can detect at-risk customers on online sports and race betting sites using only 30 days of behavioural data. Performance can be improved by adding minimal, non-intrusive self-report measures.

**ИИ:** + · обе модели · беттеры + инструмент · Customers of Australian sports and race betting sites (N=1,470) were surveyed with the PGSI, and PGSI≥8 high-risk groups were reported.

**Решение:** =

---

### 85 · R0719

**Sports Betting Participation, Perceived Consequences, and Mental Health Among U.S. College Students: A Multilevel Analysis**

2026 · Research Square · preprint, posted-content · https://doi.org/10.21203/rs.3.rs-10909275/v1

Abstract Legal sports betting has expanded rapidly across the United States since 2018, and college students are widely regarded as an at-risk population. Existing evidence, however, derives largely from single-campus convenience samples that cannot separate the effects of betting from the characteristics of students who bet. Using the 2024–2025 Healthy Minds Study, we analyzed a randomly assigned sports betting module completed by 37,121 students at 135 U.S. institutions. Two-level models with random institutional intercepts examined correlates of participation and associations with depression, anxiety, flourishing, suicidal ideation, and binge drinking. Lifetime participation was reported by 9.0% of students and was strongly patterned by sex assigned at birth (20.3% vs. 4.7%). Unadjusted, bettors reported better mental health than non-bettors; after adjustment, associations with depression, anxiety, and suicidal ideation were null, while higher flourishing and nearly twice the odds of binge drinking persisted. Among bettors, the frequency of sportsbook application use showed no gradient. However, the 4.5% endorsing a betting consequences item reported substantially worse mental health (adjusted difference of 2.15 points on the PHQ-9) and lower treatment utilization than other bettors despite greater perceived need. Race and ethnicity moderated the betting–depression association, which reversed direction between White and Hispanic/Latino students. Findings indicate that gambling involvement is a poor proxy for gambling harm among college students and that campus responses should target perceived consequences and access to care rather than participation.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Large student survey measuring sports betting; harm measured by a single consequences item, but a validated screen in the module is unclear.

**Решение:** =

---

### 86 · R0724

**Smartphone betting on sports, esports and daily fantasy sports amongst young adults**

2026 · Bristol Research (University of Bristol) · report, report/report · en · https://doi.org/10.25946/31697380

Key findings Portability is the main feature that distinguishes smartphone betting from betting using computers and land-based venues. Portability allows betting anywhere at any time, increasing the ease, speed and convenience of betting, and access to betting opportunities, betting information, and wagering inducements.While bettors value this convenience, the platform characteristics and situational features of smartphone betting interact in ways that can elevate harmful behaviours.These harmful behaviours include more frequent betting, impulsive betting, placing less well researched and a wider variety of bets, and betting more than usual when smartphone betting is done in social situations.Three situational features of betting sessions were significantly associated with consequent betting-related harm: 1) privacy while betting, 2) ability to bet anywhere anytime, and 3) greater access to inducements and betting options. In combination, these features can only be accommodated when betting on a smartphone and were found to elevate the likelihood of betting harm.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Report surveying young adult sports, esports and DFS bettors on betting harm; the abstract doesn't say whether a PG instrument such as PGSI was used.

**Решение:** =

---

### 87 · R0728

**SPORTS GAMBLING, TECHNOLOGY, AND BEHAVIORAL INTENTION AMONG COLLEGE STUDENTS**

2026 · Michigan State University Libraries · doctoral thesis, text/dissertation, dissertation · und · https://doi.org/10.25335/p8mn-nr41

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Thesis on sports gambling among college students with no abstract; it's unclear whether problem gambling was measured.

**Решение:** =

---

### 88 · R0732

**Psychometric Properties of the Online Gambling Disorder Questionnaire, Online Gambling Symptom Assessment Scale, and Gambling Urge Scale among Young Adults with the Experience of Online Gambling in Taiwan: A Preliminary Validation Study**

2026 · Journal of Gambling Studies · article · en · https://doi.org/10.1007/s10899-026-10530-2

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract. Validation of gambling disorder measures in online gamblers; may include sports bettors and a DSM-based criterion.

**Решение:** =

---

### 89 · R0736

**PEER RELATIONS AND PSYCHOLOGICAL ABUSE AS PREDICTORS OF CYBER-DELINQUENT BEHAVIOUR: THE MEDIATING ROLE OF SPORTS BETTING ADDICTION AMONG UNDERGRADUATES IN SOUTH-EASTERN NIGERIA.**

2026 · The Living Cell · article · en

Cyber delinquency is one of the growing concern particularly among the teaming population of young adults, most of whom are undergraduates. Their relation with peers and psychological experience has been linked to this delinquent behaviour, where sports betting seem to be an enabling factor. This study therefore investigate peer relations and psychological abuse as predictors of cyber-delinquent behaviour among undergraduates in South-Eastern Nigeria: The Mediating Role of Sports Betting Addiction. Cross-sectional survey design was used and a total of 768 university students were selected using online survey (google forms), comprising of 440 (57.3%) male and 328 (42.7%) female aged between 17 - 30 years. Peer relations scale developed by Kelvin et al. (1999), psychological abuse scale developed by Momta et al. (2020), sports betting addictive behaviour scale developed by Igo and Ehigie (2021) and cyber-delinquent scale developed by Arıcak et al. (2012) were used as instruments for data collection. Two hypotheses were formulated and tested and the result showed that peer relations, psychological abuse and sports betting significantly, independently and jointly predicted cyber-delinquent behaviour among undergraduates in South-Eastern Nigeria. The result further showed that sports betting significantly mediate the predictive power of peer relations and psychological abuse on cyber-delinquent behaviour among undergraduates in South Eastern Nigeria. Findings were discussed in relation to other studies, conclusions were drawn and implications enumerated. Key Words: Peer Relations, Psychological Abuse, Cyber-Delinquent Behaviour, Sports Betting Addiction, Undergraduates

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Student survey measured sports betting addiction with a non-standard local scale (Igo & Ehigie); unclear whether it is an accepted problem-gambling instrument or gives a case definition.

**Решение:** =

---

### 90 · R0743

**Efficacy of the School Gambling Prevention Program “What’s at stake?”: A Cluster Randomized Controlled Trial**

2026 · Journal of Gambling Studies · article · en · https://doi.org/10.1007/s10899-026-10486-3

Adolescent gambling has become a growing public health concern. Despite international evidence supporting preventive interventions, few programs have been rigorously evaluated in Spanish-speaking populations. This study examined the effectiveness of the school-based gambling prevention program What’s at stake? ( WAS? ). A randomized controlled trial was conducted with secondary school students ( N = 6,308; 50.6% female; mean age = 15.3 years). Participants were assigned to an experimental group ( n = 5,022) or control group ( n = 1,286). Assessments were carried out at baseline (T 1 ) and one week post-intervention (T 2 ). Primary outcomes included gambling intention and gambling severity. Secondary outcomes included gambling motives, cognitive bias, normative perception, and risk perception. Validated self-report measures were employed. Population-averaged pre-post effects were estimated using generalized estimating equations. The pre-post analyses showed significant population-average differential changes with small standardized magnitudes (RESI) in motivational dimensions, normative perception, risk perception, and gambling intention. Regarding intention, subgroup analyses by gender showed similar patterns. Descriptively, the proportion of at-risk and problem gamblers decreased in the experimental group at post-intervention, whereas minimal change was observed in the control group. The WAS? program produced significant short-term population-level preventive effects on key cognitive, motivational and intentional risk factors for gambling. Our findings contribute to strengthening the evidence base for culturally and linguistically adapted gambling prevention and extend program benefits in Hispanic adolescent populations. Future studies should include follow-up assessments and booster sessions to evaluate the maintenance of these effects.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · School prevention RCT measured adolescent gambling severity; baseline data might report sports betting participation, but abstract doesn't say so.

**Решение:** =

---

### 91 · R0745

**Sports betting, online gambling, and suicidal behavior: a relationship to consider in emergency departments.**

2026 · Emergencias : revista de la Sociedad Espanola de Medicina de Emergencias · article, journal article, journalarticle · spa;eng · https://doi.org/10.55633/s3me/036.2026

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; may be a commentary or letter, but could report emergency department data on sports bettors with problem gambling.

**Решение:** =

---

### 92 · R0747

**Gambling and its association with psychological distress among different population groups: a cross-sectional study in Great Britain, 2022**

2026 · BMC Public Health · article · en · https://doi.org/10.1186/s12889-026-27630-8

Abstract Objectives To estimate associations between past-year gambling and risk of harm from gambling with psychological distress, and explore whether these associations differ across population subgroups. Methods Data were collected from 1,987 adults (≥ 18y) in Great Britain in October 2022 through a nationally-representative household survey. Participants reported past-year gambling activity. Those who had gambled completed the Problem Gambling Severity Index; scores ≥ 1 indicated the person was at risk of harm from gambling. Past-30-day psychological distress was assessed with the K6 and categorised as low/no (scores < 5) vs. moderate/severe distress (≥ 5). Covariates included sociodemographics, mental health history, smoking status, and alcohol consumption. Results Past-year gambling was not associated with increased odds of experiencing psychological distress relative to not gambling (29.7% vs. 32.6%; OR = 0.87 [0.70–1.09]; OR adj =0.81 [0.62–1.06]), and there was no clear evidence of moderation by age, gender, social grade, children in the household, mental health history, smoking, or alcohol consumption. Among past-year gamblers, those at risk of harm from gambling were more likely to report distress than those not at risk (46.9% vs. 28.2%; OR = 2.25 [1.23–4.10]). This association was attenuated after adjustment for sociodemographics (OR adj =1.67 [0.84–3.35]) and additionally for mental health history, smoking status, and alcohol consumption (OR adj =1.16 [0.57–2.35]). Conclusions Psychological distress appears similar between those who had and had not gambled in the past year in Great Britain in 2022. Those at risk of harm from gambling were more likely to experience psychological distress but it does not appear independent of their sociodemographic characteristics, mental health history, and smoking and alcohol consumption. These findings underscore the need for integrated policies and intervention strategies that address not only gambling behaviour but also consider associated sociodemographic and health-related factors to effectively mitigate distress among individuals at risk.

**ИИ:** + · обе модели · опрос населения об азартных играх · Nationally representative GB survey; participants reported past-year gambling activities and PGSI was used, so sports bettors could be identified.

**Решение:** =

---

### 93 · R0752

**Motivational Concordance Between Alcohol Use and Gambling as a Moderator of Gambling Severity**

2026 · Digital Scholarship - UNLV (University of Nevada Reno) · conference-paper

Alcohol use and gambling frequently co-occur, yet the mechanisms underlying this association remain unclear. Prior research suggests overlapping motives for drinking and gambling. Less is known about whether individual-level alignment in these motives shapes problem severity across behaviors. The present study examined whether motivational concordance between alcohol use and gambling moderates the association between alcohol-related and gambling-related problems. Participants (N = 495) aged 21–40 reported past-month alcohol use and sports betting. Participants completed measures of alcohol-related problems (BYAACQ), gambling-related problems (PGSI), and motives for alcohol use and gambling. Motivational concordance was operationalized as the inverse of the summed distance between standardized alcohol and gambling motive scores across shared motivational domains. A moderation model was estimated using structural equation modeling in R (lavaan). Results indicated a significant interaction between alcohol-related problems and motivational concordance in predicting gambling-related problems (b = .094, p = .007). The association between alcohol-related and gambling-related problems was stronger among individuals with higher motivational concordance. These findings suggest that alignment in motivational profiles across alcohol use and gambling represents an important risk context for greater cross-behavioral problem severity.

**ИИ:** + · обе модели · беттеры + инструмент · Sample of past-month sports bettors (N=495) who completed the PGSI; the full text may report problem-gambling prevalence.

**Решение:** =

---

### 94 · R0754

**COMPROMETIMENTO DA RENDA COM APOSTAS ONLINE E A SITUAÇÃO FINANCEIRA DOS INDIVÍDUOS EM UMA REGIÃO DE FRONTEIRA: UM ESTUDO EM FOZ DO IGUAÇU-PR COMMITMENT OF INCOME TO ONLINE BETTING AND THE FINANCIAL SITUATION OF INDIVIDUALS IN A BORDER REGION: A STUDY IN FOZ DO IGUAÇU-PR COMPROMISO DE INGRESOS CON LAS APUESTAS EN LÍNEA Y LA SITUACIÓN FINANCIERA DE LAS PERSONAS EN UNA REGIÓN FRONTERIZA: UN ESTUDIO EN FOZ DO IGUAÇU-PR**

2026 · Revista de Geopolítica · journal-article · https://doi.org/10.56238/revgeov17n6-043

O avanço das apostas online no Brasil tem chamado atenção pelos possíveis impactos na forma como as pessoas organizam suas finanças, especialmente em um contexto de maior acesso a plataformas digitais e instabilidade econômica. Este estudo buscou analisar como a renda destinada a essa prática se relaciona com a situação financeira de indivíduos da cidade de Foz do Iguaçu. A pesquisa adotou abordagem quantitativa, com metodologias exploratória e descritiva, recorte temporal entre janeiro e fevereiro de 2026, recorte espacial no município de Foz do Iguaçu e utilização do método Survey, por meio de questionário estruturado. Os resultados mostram que a maior parte dos participantes destina uma parcela reduzida da renda às apostas, indicando que essa prática, isoladamente, não se apresentou como o principal fator de comprometimento do orçamento. Ainda assim, ao analisar o conjunto das respostas, apareceram diferenças entre aquilo que os indivíduos acreditam controlar e o que ocorre na prática, especialmente quanto ao registro de gastos, à organização financeira e à formação de reserva de emergência. Também foram observadas situações de inadimplência e dificuldades no cumprimento de despesas essenciais, mesmo entre aqueles que afirmaram manter controle sobre suas finanças. Embora muitos não percebam interferência direta das apostas em sua capacidade de pagamento, surgiram indícios de efeitos indiretos, como uso de crédito, necessidade de recorrer a terceiros e limitação da poupança. Assim, a relação entre renda destinada às apostas e situação financeira mostrou-se mais associada à forma como os indivíduos organizam e administram seus recursos ao longo do tempo.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Survey of Brazilian online bettors on how betting affects their finances; the abstract doesn't say whether a problem-gambling instrument was used.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Survey on online betting income share and personal finances in Foz do Iguaçu; no problem-gambling instrument mentioned, and sports betting is not specified.)

**Решение:** -

---

### 95 · R0774

**Impact des paris sportifs sur la situation économique des jeunes dans la ville de Bukavu**

2026 · International Journal of Strategic Management and Economic Studies (IJSMES) · article · fr · https://doi.org/10.5281/zenodo.21375854

Cette étude examine l'impact des paris sportifs sur la situation économique des jeunes dans la ville de Bukavu, en République Démocratique du Congo. Face au chômage croissant, de nombreux jeunes considèrent les paris sportifs comme une source potentielle de revenus. L'objectif de la recherche était d'évaluer l'influence de cette pratique sur leurs conditions économiques. Une approche mixte (quantitative et qualitative) a été adoptée auprès d'un échantillon de 250 jeunes composés d'étudiants, de chômeurs, d'élèves, de conducteurs de taxi-moto et de manutentionnaires. Les données ont été analysées à l'aide de statistiques descriptives, d'une analyse de régression et d'une analyse de contenu. Les résultats révèlent que 53,2 % des enquêtés pratiquent les paris sportifs depuis un à trois ans et que 77,6 % estiment que cette activité a détérioré leur situation financière. En outre, 81,6 % considèrent que les gains obtenus ne permettent pas d'améliorer durablement leurs conditions de vie. L'étude conclut que les paris sportifs constituent davantage un facteur de vulnérabilité économique qu'un moyen efficace d'améliorer le niveau de vie des jeunes. Elle recommande au gouvernement congolais de renforcer l'éducation financière, la sensibilisation aux risques des jeux d'argent et les politiques de promotion de l'emploi et de l'entrepreneuriat des jeunes.Mots-clés : Impact, paris sportifs, situation économique, jeunes et Bukavu

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Survey of 250 young sports bettors in Bukavu focused on economic impact; abstract does not say whether a problem-gambling instrument was used.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Survey of youth sports bettors in Bukavu on economic impact; no problem-gambling instrument mentioned, only perceived financial effects.)

**Решение:** -

---

### 96 · R0778

**Sports Betting Attitudes**

2026 · OSF Preprints (OSF Preprints) · preprint

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; an attitudes survey of sports bettors might also have measured problem gambling, so the full text should be checked.

**Решение:** =

---

### 97 · R0779

**Sports Betting Probability Estimates**

2026 · OSF Preprints (OSF Preprints) · preprint

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; title could mean market odds modelling or a study of bettors' probability judgements, which might include a PGSI measure.

**Решение:** =

---

### 98 · R0781

**&lt;p&gt;Profiling Bettors In “The Land Of Football”: A Cluster Analysis&lt;/p&gt;**

2026 · Elsevier BV · posted-content, preprint · https://doi.org/10.2139/ssrn.5958439

Using a sample of 491 Brazilian university students who bet on sports, this study profiles sports bettors according to demographic characteristics through principal component and cluster analyses. Based on four components-instrumental financial education, risk related to sports betting, ethics and responsibility, and entrepreneurship-we identify four clusters. These clusters differ demographically both within and across groups. The dreamers are mostly female, with low financial education, and moderate interest in sports betting, while the sports betting affectionate are mostly male and differ from the first group in terms of financial education. The risk-averse and the financially imprudent lack an ethical and responsible mindset as well as financial education, and differ in their intention to engage in sports betting, with the former group not being interested in the activity, whereas the latter is. This study contributes to policymakers, practitioners, and academics by offering new insights into an increasingly concerning gambling activity.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of 491 Brazilian student sports bettors; the 'risk related to sports betting' component may or may not use a PG instrument.

**Решение:** =

---

### 99 · R0782

**Playing Sports, Placing Sports Bets? Sports Club Membership, Gambling Norms and Sports Gambling Behavior among Flemish Youth.**

2026 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-025-10428-5

In recent years, gambling has become increasingly embedded in sports culture, a phenomenon known as "gamblification", raising concerns about youth exposure to sports betting. This study explores the role of descriptive norms (perceived peer gambling behavior) and injunctive norms (perceived peer approval) within Flemish sports clubs, assessing their impact on youths' (18-25 year old) online sports betting frequency. Using a quantitative cross-sectional survey (N = 1,290), results indicated that sports club membership is significantly positively correlated with online sports betting frequency, a relation mediated specifically by descriptive norms. However, injunctive norms did not mediate this relationship. The results of this study suggest a need for targeted prevention strategies within sports clubs.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of Flemish youth on online sports betting frequency; abstract doesn't mention a problem-gambling instrument, though one may have been used.

**Решение:** =

---

### 100 · R0783

**Predicting Sports Betting Intentions Among Adolescents: Gender-Specific Pathways in the Reasoned Action Approach.**

2026 · Journal of gambling studies · journal article, journalarticle, article · eng · https://doi.org/10.1007/s10899-026-10548-6

Abstract Sports betting among adolescents is a growing public health concern, yet the social-cognitive mechanisms driving sports betting intentions in legally underage populations remain largely underexplored. This study applied the Reasoned Action Approach (RAA) to sports betting intentions in a large sample of secondary school students ( N = 1,215; age range 13–19). Structural equation modeling was used to examine the extent to which sports betting-specific attitudes (instrumental and affective), perceived norms (injunctive and descriptive), and perceived behavioral control (capacity and autonomy) predicted sports betting intention, and whether these relationships were invariant across gender. The model explained 38.0% of variance in sports betting intention. Instrumental attitude and descriptive norms emerged as significant predictors. Multi-group analysis confirmed metric invariance across gender. The pattern of RAA predictors was consistent across groups, although structural paths were not fully invariant, with household income emerging as a gender-specific predictor of sports betting intention among female adolescents. Because both instrumental attitude and descriptive norms are strongly shaped by the commercial and media-driven normalization of sports betting, findings suggest that prevention efforts should target cognitive outcome evaluations and perceived peer betting norms, and that these pathways are relevant for both male and female adolescents.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Adolescent school survey on sports betting intentions; no PG instrument mentioned, but sample description might include past betting and PG.

**Решение:** =

---

### 101 · R0792

**Examining potential behavioral and psychological consequences of unjustified confidence in knowledge and in forecasting**

2026 · Judgment and Decision Making · article, journalarticle · en · https://doi.org/10.1017/jdm.2026.10040

Abstract Understanding confidence in one’s knowledge has been a longstanding goal in judgment and decision-making research. This study takes an initial step toward identifying the psychological and behavioral consequences of unjustified confidence—confidence not supported by actual knowledge—by examining its associations with multiple psychological and behavioral variables within the domain of sports betting. A sample of 997 participants completed either a knowledge-confidence or forecasting-confidence assessment, followed by measures of empowerment, decisiveness, openness to information, risk taking, information search, and information use. Psychologically, unjustified confidence was related to greater feelings of empowerment and decisiveness, but unrelated to openness to information. Behaviorally, unjustified confidence was related to greater risk taking and information search, but showed little consistent relationship with information use. These patterns were largely consistent across knowledge and forecasting tasks, with only minor variations. Multiple regression analyses revealed distinct predictor patterns for different behavioral outcomes, suggesting that confidence’s role varies across decision-making behaviors. These findings provide an extensive examination of multiple theorized consequences of confidence within a single domain, identifying which relationships warrant experimental investigation and suggesting that understanding confidence’s causal effects will require nuanced, behavior-specific models.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Survey of 997 people about confidence in sports betting; no problem-gambling instrument listed, but one might appear in the full-text sample description.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Study of confidence and decision behaviours in a sports betting context; no problem-gambling instrument mentioned in the abstract.)

**Решение:** ?

---

### 102 · R0796

**Financial Hardship and Problem Gambling Severity Among Young South Koreans: A Conditional Strain Model**

2026 · Journal of Gambling Studies · article · en · https://doi.org/10.1007/s10899-026-10556-6

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract. Survey of young South Koreans measuring problem gambling severity; may report sports betting (e.g., Sports Toto) participation.

**Решение:** =

---

### 103 · R0797

**Loot box purchases are associated with problem gambling severity and harms beyond traditional gambling activities.**

2026 · Addictive behaviors · journal article, journalarticle, article · eng · https://doi.org/10.1016/j.addbeh.2026.108783

Loot boxes are virtual chests containing randomized in-game items. Given their structural similarities, loot boxes have been argued to be a form of gambling. Indeed, previous meta-analytic studies suggest that loot boxes are associated with problem gambling severity and act as a "gateway" to gambling. Yet, little is known about loot box purchasing among individuals who already gamble. In the present study, we assessed the demographic characteristics and addictions and mental health comorbidities of adult loot box purchasers, through a nationally stratified sample of regular gamblers who also regularly play video games (N = 3709). We also investigated whether loot box engagement is associated with problem gambling severity and gambling harms when controlling for traditional gambling activities. Of the total sample, 1,922 reported having purchased loot boxes (Mage = 38.72, 61.3% male). Loot box purchasers were more likely to be younger, single, employed, have a college degree or higher, and report upper-middle income. Loot box purchasers were significantly more likely to endorse addictions and mental health comorbidities (e.g., substance use, depression). When controlling for other forms of gambling (e.g., electronic gambling machines, sports betting), both the frequency of loot box purchasing and money spent were associated with problem gambling severity and gambling-related harms. The results from the present study provide further support that loot boxes when purchased with money may be conceptualized as a form of gambling and contribute to problem gambling risk and harms. Given the popularity of loot boxes and relative lack of age restrictions, jurisdictions may wish to regulate the purchase of loot boxes similarly to traditional forms of gambling.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Survey of regular gamblers measuring sports betting participation and problem gambling severity; could report PG among sports bettors.

**Решение:** =

---

### 104 · R0806

**Gambling, smoking and alcohol use in Great Britain: insights from the 2023 Gambling Survey of Great Britain**

2026 · Addictive Behaviors · article · en · https://doi.org/10.1016/j.addbeh.2026.108641

Gambling often co-occurs with tobacco smoking and alcohol use, which likely exacerbates the physical, psychological, and financial harm that each of them cause. Using 2023 Gambling Survey for Great Britain (GSGB; n = 9742) data, we ran generalized linear models (adjusted for sex, age, income, housing tenure and ethnicity) to assess associations between i) risk or severity of gambling problems (Problem Gambling severity Index [PGSI], and reported overspend or ignoring spend limits), and ii) attempts to reduce gambling, with alcohol consumption (Alcohol Use Dependence Test for Consumption [AUDIT-C]) and current smoking. A multinomial model explored the association between the same gambling harm predictors and a composite measure of smoking and high-risk drinking. Compared with non-gamblers, AUDIT-C was significantly (all p < 0.001) higher across all PGSI response categories in a dose dependent fashion (PGSI 0 β=0.30; PGSI 1–2 β=0.64; PGSI 3–7 β=0.75; PGSI ≥ 8 β=1.40). The odds of current smoking also increased with higher PGSI scores but was only statistically significant for PGSI scores ≥ 8 (OR adj = 2.81, 95%CI 1.85, 4.28). Similar associations were apparent for overspending or ignoring limits. Those who attempted to reduce or stop gambling in the past year were more likely to smoke. Disordered gamblers (PGSI ≥ 8) compared with those who do not gamble had greatly increased odds of both smoking and having an AUDIT-C ≥ 8 (high-risk drinking) vs. not smoking and having an AUDIT-C score < 8 (OR adj = 9.37; 95%CI = 4.15–21.14; p < 0.001). Increased risk or severity of gambling problems is associated with risky drinking and odds of smoking in a dose dependent fashion. These findings underscore the need for integrated policy and intervention approaches to address gambling-related and substance-related harms together.

**ИИ:** + · обе модели · опрос населения об азартных играх · Secondary analysis of the national GSGB 2023 survey using the PGSI; the survey records gambling activities, possibly including sports betting.

**Решение:** =

---

### 105 · R0812

**An evolving threat: Problem gambling and sports wagering in the United States military.**

2026 · Journal of behavioral addictions · article, journal article, journalarticle · eng · https://doi.org/10.1556/2006.2025.00527

Abstract Background This study examined the stability and interplay of gambling depth, breadth, and problems in the United States (US) public, with a particular attention to military-affiliated individuals (i.e., veterans, active duty service members, reservists). Methods Longitudinal survey study using YouGov Opinion Polling's sample-matching methodology. A sample of 4,363 participants were collected as part of a large sport wagering project. Participants completed measuring assessing problem gambling symptoms, sports wagering status, gambling breadth and depth, and questions assessing military status and demographics. Analyses of Variance (ANOVAs) were conducted for group comparisons, and longitudinal models were specified using Random Intercept Cross Lagged Panel modeling. Results Results indicated that these domains were largely stable over time, with low within-person variability and effects driven primarily by between-person differences. US veterans and active duty reported greater gambling breadth and problems, with active duty and reserve service members showing elevated risk across all domains. Sports wagers exhibited higher involvement and greater problems, while younger age was associated with more problems and breadth, and male gender with greater breadth and depth. Residual covariances suggested that changes in breadth, depth, and problems tended to co-occur. Within individuals, greater gambling frequency often preceded narrower breadth, indicating increased focus on specific activities. Conclusions Study limitations include reliance on self-report, long assessment intervals, and use of frequency rather than spending as the measure of depth. Findings highlight the need for targeted public health initiatives for problem gambling symptoms among US military personnel.

**ИИ:** + · обе модели · беттеры + инструмент · Longitudinal US survey (n=4,363) measuring sports wagering status and problem gambling symptoms; sports bettors compared on problems.

**Решение:** =

---

### 106 · R0818

**Understanding sports betting among youth in Oforikrom Municipality, Ghana: An integrated psychosocial perspective**

2026 · Geopsychiatry · article, journalarticle, journal-article · en · https://doi.org/10.1016/j.geopsy.2026.100103

Sports betting has become a major public health concern, where many young people view it as an economic opportunity to supplement their income. However, limited research has examined this phenomenon using an integrated framework that considers the psychological, social, and environmental factors influencing youth participation in sports betting. This study examined the prevalence and the factors influencing sports betting among the youth in Oforikrom Municipality. We analyzed data from 744 youth (mean age = 21.95, SD = 3.05, 74.2% Male) from a cross-sectional survey. Results show a high prevalence of sports betting among youth in Oforikrom Municipality, with 84.4% reporting lifetime participation, 62.4% reporting betting within the past 12 months, and 33.6% within the past 30 days. Again, higher odds/trends of sports betting were largely driven by being traditionalist, fear of missing out, easy accessibility of online platforms, and peer pressure, while social acceptance, promotions and bonuses, family gambling history, and aggressive advertising were associated with lower odds/trends of sports betting. These findings indicate that sports betting is growing, though at a decreasing rate, among the youth; targeted interventions and public health policies and strategies are needed to reduce the growing prevalence among the youth in Oforikrom Municipality, Ghana.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Youth survey on sports betting prevalence and its predictors; the abstract does not say whether a problem-gambling instrument was used.

**Решение:** =

---

### 107 · R0824

**Social harms of sport betting among urban youth: evidence from Mwanza city, Tanzania.**

2026 · African Journal of Social Issues · article, journalarticle, journal-article · und · https://doi.org/10.4314/ajosi.v9i1.51

Sports betting has expanded rapidly among urban youth in sub-Saharan Africa, yet evidence on its social harms in Tanzanian community settings remains limited. This cross-sectional study examined the prevalence, types, sociodemographic predictors, and awareness dimensions of social harms associated with sports betting among 200 urban youth in Mwanza City, Tanzania. Data were collected using structured questionnaires administered at betting centres and analysed through descriptive statistics, Pearson chi square tests, and binary logistic regression. Results showed that all measured social harms exceeded 50% prevalence: concentration problems (66.5%), financial challenges (62.0%), missed obligations (56.0%), affected savings (55.5%), family conflict (54.0%), and borrowing for betting (52.0%). Reduced interaction with family (53.5%) and frequent conflicts (54.0%) were the dominant types of social and family impact, respectively. Binary logistic regression identified divergent predictor profiles across harms: male sex independently predicted family conflict (AOR = 4.72, p &lt; .001) and concentration problems (AOR = 7.40, p &lt; .001), whereas single marital status (AOR = 18.65, p &lt; .001) and primary education (AOR = 8.04, p &lt; .001) were the strongest predictors of missed obligations. Betting frequency independently predicted concentration problems (AOR = 1.47, p = .011) and missed obligations (AOR = 1.56, p = .008) but not family conflict. Although harm prevalence was high, only 50.5% of respondents were aware of betting risks and 34.5% had accessed counselling services, while 74.5% supported youth awareness programmes. These findings highlight the need for targeted, gender sensitive, and frequency aware interventions that address the social harms of sports betting among Tanzanian urban youth.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Survey of youth sports bettors measuring social harms with structured questionnaires; no standard problem-gambling instrument mentioned, but one may have been used.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Survey of sports bettors in Mwanza measuring social harms (concentration, finances, family conflict); no problem-gambling screening instrument is mentioned.)

**Решение:** ?

---

### 108 · R0828

**Driven to Win, Destined to Lose? A Process Model of How Sports Betting Escalates Into Gambling Harm and Shapes Help‐Seeking**

2026 · Psychology and Marketing · journalarticle, article, journal-article · en · https://doi.org/10.1002/mar.70271

ABSTRACT Sports betting has become a routine part of watching sport. Online and mobile platforms let consumers bet continuously, receive instant feedback, and respond to new odds throughout a match. Frequent betting is known to raise the risk of gambling‐related harm, but far less is known about the psychological mechanisms through which that harm develops and about the conditions under which gamblers decide to seek help. This research develops and tests a process model of the sports betting harm spiral across five studies. Studies 1a, 1b, and 1c show that higher betting intensity increases problem gambling severity through two mechanisms, where competitive intensification strengthens the drive to outperform other bettors while overconfidence bias inflates belief in predictive skill, which yields evidence consistent with the proposed ordering in which competitive motivation precedes distorted judgment. Studies 2a and 2b show that severe losses increase intentions to seek help, especially among highly engaged bettors, yet this response depends on attribution style, as gamblers who attribute losses to external causes report stronger help‐seeking intentions than gamblers who blame themselves. Theoretically, the findings integrate consumer culture theory, cognitive bias theory, and attribution theory into a single process model that explains how gambling harm escalates and when recovery‐oriented behavior emerges. Practically, the findings offer guidance for consumer protection, gambling policy, and responsible platform design.

**ИИ:** + · обе модели · беттеры + инструмент · Several quantitative studies of sports bettors measuring problem gambling severity, probably with an instrument such as the PGSI.

**Решение:** =

---

### 109 · R0831

**All My Friends Are Doing It: Perceived Social Norms Predict Heavier Sports Betting Behavior Among Young Adults.**

2026 · Health education & behavior : the official publication of the Society for Public Health Education · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1177/10901981251350877

Sports betting is the fastest growing gambling behavior in the United States, particularly among young adults. Despite burgeoning evidence of the public health concerns associated with sports betting, antecedents of this addictive behavior are largely understudied. Informed by seminal psychological theories of conformity and existing norms-based prevention paradigms for high-risk behavior, the current study aimed to quantitatively examine perceived social norms as a potential explanatory factor for sports betting behavior. The sample was comprised of 221 young adults from 36 different U.S. states ( M age = 24.4; 77.7% male; 64.6% White). Eligibility criteria included betting on sports at least twice in the past month. At baseline, participants reported perceptions of friends' sports betting approval and engagement for the next 2 weeks and then 2 weeks later reported indices of their own sports betting behavior. Generally, young adults perceived their peers to wager much more on sports betting than they themselves reported wagering, suggesting potential normative misperceptions in line with social norms theory. Those who perceived their friends to be more accepting of, and more engaged in sports betting, reported engaging in more sports betting behaviors in the subsequent 2-week period. Injunctive norms more strongly predicted young adults' total number of bets, whereas descriptive norms more strongly predicted total amount wagered and negative consequences. Findings provide foundational evidence for peer influence processes on sports betting behaviors among young adults. These key early-stage findings inform how social norms may be leveraged within forthcoming prevention/intervention approaches aimed at stymieing the rapidly growing harms associated with sports betting.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of young adult sports bettors measuring negative consequences; a problem-gambling instrument such as PGSI may be reported in the full text.

**Решение:** =

---

### 110 · R0833

**Sports Betting and Psychosocial Well-Being of Boda-Boda Riders: Perspectives from Kajiado County, Kenya**

2026 · INTERNATIONAL JOURNAL OF MULTIDISCIPLINARY RESEARCH AND ANALYSIS · article, journalarticle/ · ang · https://doi.org/10.5281/zenodo.20678539

Psychosocial well-being is an important component of overall health and quality of life, as it encompasses both psychological and social factors that influence how individuals cope with stress, form relationships, and function within their communities. However, the convenience of mobile betting platforms has led to a surge in sports betting activities, particularly among low-income groups such as boda-boda riders. The purpose of this study was to examine the effect of sports betting on the psychosocial well-being of boda-boda riders in Kajiado County, Kenya. The specific objectives were to examine the effect of sports betting on the psychological well-being of boda-boda riders and establish its effect on their social well-being. The study was guided by Cognitive Behavioural Theory and Social Learning Theory. A mixed-method research design was adopted, targeting 21,568 registered boda-boda riders in Kajiado County. The sample size of 379 riders was determined using the Krejcie and Morgan Table. Additionally, five boda-boda SACCO leaders participated in in-depth interviews. The study covered all five sub-counties of Kajiado County: Kajiado North, Kajiado South, Kajiado Central, Kajiado West, and Kajiado East. Data were collected using the Canadian Problem Gambling Index (CPGI), the Mental Health Continuum Short Form Scale (MHC-SF), questionnaires, focus group discussions, and interview schedules, capturing both quantitative and qualitative data. Quantitative data was analyzed using the Statistical Package for Social Sciences (SPSS) version 28, employing both descriptive and inferential statistics, including linear regression analysis. Qualitative data was analyzed thematically using content analysis. The findings revealed that sports betting explained 68.2% of the variation in psychosocial well-being (R² = 0.682), indicating a significant negative effect. Specifically, a unit increase in sports betting was associated with a 0.396 unit decrease in psychosocial well-being (β = -0.396, p &lt; .001). The ANOVA results further confirmed the model’s significance (F = 66.86, p &lt; .001). These findings indicate that increased engagement in sports betting is associated with emotional distress, financial instability, and weakened social relationships among boda-boda riders. The study concludes that sports betting has a significant negative effect on the psychosocial well-being of boda-boda riders in Kajiado County. The study recommends the implementation of structured interventions, including financial literacy programs, accessible counseling services, and policy measures to regulate gambling participation.

**ИИ:** + · обе модели · беттеры + инструмент · Mixed-method survey of 379 boda-boda riders who bet on sports, with the CPGI used to measure problem gambling.

**Решение:** =

---

### 111 · R0834

**Sports Betting and Psychosocial Well-Being of Boda-Boda Riders: Perspectives from Kajiado County, Kenya**

2026 · INTERNATIONAL JOURNAL OF MULTIDISCIPLINARY RESEARCH AND ANALYSIS · journalarticle, article, journal-article · https://doi.org/10.47191/ijmra/v9-i6-43

Psychosocial well-being is an important component of overall health and quality of life, as it encompasses both psychological and social factors that influence how individuals cope with stress, form relationships, and function within their communities. However, the convenience of mobile betting platforms has led to a surge in sports betting activities, particularly among low-income groups such as boda-boda riders. The purpose of this study was to examine the effect of sports betting on the psychosocial well-being of boda-boda riders in Kajiado County, Kenya. The specific objectives were to examine the effect of sports betting on the psychological well-being of boda-boda riders and establish its effect on their social well-being. The study was guided by Cognitive Behavioural Theory and Social Learning Theory. A mixed-method research design was adopted, targeting 21,568 registered boda-boda riders in Kajiado County. The sample size of 379 riders was determined using the Krejcie and Morgan Table. Additionally, five boda-boda SACCO leaders participated in in-depth interviews. The study covered all five sub-counties of Kajiado County: Kajiado North, Kajiado South, Kajiado Central, Kajiado West, and Kajiado East. Data were collected using the Canadian Problem Gambling Index (CPGI), the Mental Health Continuum Short Form Scale (MHC-SF), questionnaires, focus group discussions, and interview schedules, capturing both quantitative and qualitative data. Quantitative data was analyzed using the Statistical Package for Social Sciences (SPSS) version 28, employing both descriptive and inferential statistics, including linear regression analysis. Qualitative data was analyzed thematically using content analysis. The findings revealed that sports betting explained 68.2% of the variation in psychosocial well-being (R² = 0.682), indicating a significant negative effect. Specifically, a unit increase in sports betting was associated with a 0.396 unit decrease in psychosocial well-being (β = -0.396, p &lt; .001). The ANOVA results further confirmed the model’s significance (F = 66.86, p &lt; .001). These findings indicate that increased engagement in sports betting is associated with emotional distress, financial instability, and weakened social relationships among boda-boda riders. The study concludes that sports betting has a significant negative effect on the psychosocial well-being of boda-boda riders in Kajiado County. The study recommends the implementation of structured interventions, including financial literacy programs, accessible counseling services, and policy measures to regulate gambling participation.

**ИИ:** + · обе модели · беттеры + инструмент · Mixed-methods survey of 379 boda-boda riders in Kenya on sports betting, using the CPGI; it may report problem-gambling prevalence among bettors.

**Решение:** =

---

### 112 · R0838

**Ludopatía y prevención ausente: Evaluación crítica de las estrategias estatales frente a una adicción silenciosa**

2026 · Institutional Repository of the Santo Tomás University · dissertation · es

Este artículo se realiza para examinar el creciente problema de la adicción al juego en Colombia, una adicción que, aunque definida por la Organización Mundial de la Salud como un trastorno mental, sigue siendo marginada en comparación con otros comportamientos adictivos. Desde el crecimiento del juego en línea, el fenómeno se ha generalizado, causando deudas, problemas familiares, colapso de la salud mental, vulnerabilidad social y altas tasas de juego entre los jóvenes. Su impacto, sin embargo, ha tenido una respuesta institucional limitada influenciada por, pero no limitada a, la insuficiente capacitación de los profesionales de la salud mental, la falta de datos oficiales sobre su prevalencia y un conflicto de intereses con el negocio del juego, que genera importantes ingresos para el estado. La legalización de las apuestas deportivas se inició con un juego de azar regulado establecido a través de la Ley 643 de 2001 en Colombia. Luego, también siguiendo esto, la Ley 1753 de 2015, junto con el establecimiento de Coljuegos, estableció aspectos legales a través de la regulación de las plataformas digitales, así como la concesión de licencias a los operadores, llevando a Colombia como pionera hacia este mercado en América Latina. El juego ha sido comercializado como una forma de diversión desde entonces, integrado incluso en la cultura deportiva, donde las apuestas ahora son parte de la tradición futbolística y un rito de paso. Esta socialización y accesibilidad digital ha puesto a los adolescentes y estudiantes universitarios en un riesgo elevado de desarrollar un comportamiento adictivo. En realidad, los datos de encuestas de este estudio sugieren que alrededor del 19% de todos los estudiantes encuestados tenían adicción al juego y algunos están en riesgo. En consecuencia, esto permite expandir la idea de manera periodística que, en sí misma, permite identificar los determinantes que vinculan la adicción al juego y la práctica social de las apuestas deportivas en Colombia. Para ello, también propusimos el podcast "Apuesta Perdida", para visibilizar el problema, debatirlo abiertamente en público y pedir una respuesta más ética, humana y responsable de las instituciones. Esta es la única manera de abordar la adicción silenciosa y generalizada que, a menos que se enfrente, continuará floreciendo e impactando a los sectores más marginados de la sociedad.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Journalistic thesis on Colombian sports betting; student survey reports 19% gambling addiction, but the instrument and sports-betting breakdown are unclear.

**Решение:** =

---

### 113 · R0839

**THE NCAA'S GAMBLING PROBLEM**

2026 · SSRN Electronic Journal · preprint · https://doi.org/10.2139/ssrn.6077426

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; SSRN title suggests a legal/policy paper on NCAA and sports betting, but it could contain student-athlete survey data.

**Решение:** =

---

### 114 · R0841

**Game related over-spending across age groups and its association with gaming disorder.**

2026 · Addictive behaviors · article, journal article, journalarticle · eng · https://doi.org/10.1016/j.addbeh.2025.108490

BACKGROUND: Gaming disorder is a new addictive disorder under the ICD-11. Most of recent research focuses on young people and its impact on mental and physical health. However, it can also have negative financial impacts as in-game microtransaction and esport betting becoming more common, and this impact could be particularly problematic for older people. This study estimates the association between gaming disorder and game-related overspending. METHOD: Data were from the 2022 International Gaming Study (IGS22), a multi-country cross sectional survey of 955 individuals aged 18-94 (M = 46; SD = 16; 45 % Male). We estimated the proportion of participants who reported game-related overspending and modelled its association with ICD-11 Gaming Disorder using logistic regression. RESULT: In general, a much smaller but non-negligible proportion of older people (66 years old + ) reported various type of game-related overspending (4 - 9 %) compared to younger age groups. Individuals who are at risk of gaming disorder were at six to nine times higher odds of reporting various type of gaming-related overspending. CONCLUSION: This study reveals a novel association between gaming disorder and overspending on purchasing games, in-game purchases, and esports betting across various age groups. While young individuals were more likely to report overspending, some older adults were also affected. As the measure reflects self-reported overspending, further research is needed to assess whether this translates into actual financial hardship.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Gaming-disorder survey covering esports betting overspending; unclear whether a problem-gambling instrument was also given.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Survey measures ICD-11 gaming disorder and self-reported overspending, including esports betting; no problem-gambling instrument used.)

**Решение:** ?

---

### 115 · R0843

**An investigation of esports betting: Involvement, risk and gambling-related harms**

2026 · Digital Scholarship - UNLV (University of Nevada Reno) · conference-paper

Esports betting is an emerging form of gambling that intersects with video gaming and may pose a unique risk for younger populations. This presentation reports findings from a mixed-methods study examining the scope, correlates, and potential harms of esports betting. Quantitative analyses of a population-based sample of U.S. adults (N=3,512) showed that 7% engaged in esports betting in the past year, with one-third betting at least weekly. Compared to individuals who gamble on non-esports activities, esports bettors were significantly younger, more likely to be male and single, and more frequently engaged in other gambling activities and video gaming. Importantly, esports betting was independently associated with elevated risk of problem gambling after controlling for engagement in 14 other gambling activities. A latent profile analysis of esports bettors (n=274) identified four distinct risk profiles. The high-risk subgroup was characterized by high engagement in loot box purchasing and skin betting, and more severe video gaming problems. Qualitative focus groups with 46 college students who play and/or bet on esports further contextualized young esports consumers’ experiences and perceptions. Many participants reported betting on offshore sites, including some using cryptocurrency, believed that esports knowledge improved betting accuracy, and had limited awareness of esports betting legality and the presence of responsible gambling safeguards on the platforms they used.

**ИИ:** + · обе модели · беттеры + инструмент · Population survey of US adults with esports bettors (n=274) and a problem gambling risk measure; full text could give prevalence.

**Решение:** =

---

### 116 · R0847

**Beneficial or harmful? Finns’ perceptions of the consequences of their gambling on relationships, health, and finances**

2026 · International Gambling Studies · article · en · https://doi.org/10.1080/14459795.2026.2683624

Gambling can result in benefits and harm, yet their relationship and underlying predictors remain inadequately understood. Using data from the Finnish Gambling 2023 population survey (N = 5,977), this study examines to what extent Finnish gamblers self-report gambling as beneficial or harmful. We examined associations between sociodemographic and gambling behavior-related variables and harms and benefits across three domains: relationships, health, and finance. Binary logistic regression models were used. The majority of respondents evaluated their gambling as having neither benefits nor harms for health (93.1%), finances (85.2%), and relationships (90.8%), respectively. While examining the extremes of the rating scale, 10.2% rated their gambling financially harmful while 4.6% perceived it as beneficial. Conversely, from the perspective of health and, particularly, relationships, gambling was rated more beneficial than harmful. Deviations from neutrality, positive and negative, were most common among those with frequent and at-risk gambling based on Problem Gambling Severity Index (PGSI) scores. Findings suggest that experiencing benefits from gambling is associated with experiencing harms and having higher PGSI scores. Although these findings describe co-occurring self-reported evaluations rather than directional or causal relationships, our results support the view that gambling is an atypical consumer product, inherently risky even when perceived as beneficial to the individual.

**ИИ:** + · обе модели · опрос населения об азартных играх · Finnish Gambling 2023 population survey with PGSI; the full text may include activity-level data covering sports betting.

**Решение:** =

---

### 117 · R0854

**The Immediate Effects of Sports Gambling, Surprise, and Suspense on Attention and Memory**

2026 · JoCN Forum · article, journalarticle, journal-article · en · https://doi.org/10.21428/8e6ba8ef.b3f55f26

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; experimental study of sports gambling effects on cognition, so participants may have been screened with a problem-gambling instrument.

**Решение:** =

---

### 118 · R0855

**The Emerging Public Health Challenge of Online Sports Gambling Among Adolescents in the United States.**

2026 · The Journal of adolescent health : official publication of the Society for Adolescent Medicine · journal article, journalarticle, article · eng · https://doi.org/10.1016/j.jadohealth.2026.07.012

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the title sounds like a commentary or editorial, but it could be an empirical study of adolescent online sports betting.

**Решение:** =

---

### 119 · R0856

**Cutting the odds: Understanding non-suicidal self-injury patterns among people gambling online**

2026 · Comprehensive Psychiatry · article · en · https://doi.org/10.1016/j.comppsych.2026.152686

Non-suicidal self-injury (NSSI) and gambling are considered notable public health challenges, each linked to emotion dysregulation, impulsivity, and heightened mental health risks. Although examined separately, their co-occurrence may reflect overlapping vulnerabilities. This study examined the prevalence, correlates, and predictors of NSSI among people who gamble online and identified distinct behavioral subgroups using latent class analysis. A cross-sectional study was conducted among people with past-year online gambling ( N = 1047; 50% males; mean age = 39.60 years [SD = 12.46]). Measures included problem-gambling severity, NSSI, impulsivity, sleep difficulties, and psychological distress. Multinomial logistic regressions tested associations between gambling severity and NSSI, latent class analysis (LCA) identified NSSI subgroups. Hierarchical multinomial regressions assessed demographic, gambling-related, and psychological predictors of class membership. Lifetime NSSI was reported by 64% of participants, with higher odds among those with scores reflecting problem gambling. LCA identified three subgroups: low/no self-harming (61.6%), moderate/occasional self-harming (23.2%), and high/multi-method self-harming (15.2%), reflecting stepwise increases in frequency and method diversity. NSSI class membership was significantly associated with problem-gambling severity (χ 2 [3] = 45.0, p < .001). Younger age, insomnia, impulsivity, and psychological distress predicted higher NSSI class membership, insomnia and distress emerging as the strongest independent predictors. NSSI is a prevalent and clinically significant correlate of online gambling, emerging even at lower levels of problem-gambling severity, underscoring the importance of integrating emotion regulation and distress-focused support into interventions targeting problem gambling. The study's findings deepen the understanding of psychological pathways linking gambling and self-injury among adults. • NSSI is common among people who gamble online and increases with gambling problem severity. • Latent class analysis revealed three NSSI subgroups with different risk levels. • Insomnia and distress independently predict NSSI beyond gambling and impulsivity. • Younger adults with gambling problems show greater NSSI engagement levels. • Screening for NSSI is advised at all gambling severity levels.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Survey of online gamblers that measured problem-gambling severity; the gambling-related predictors may include sports betting, but the abstract doesn't say.

**Решение:** =

---

### 120 · R0857

**Does Sports Betting Satisfy the Conventional Investment Criteria? Evidence from Administrative and Socio-economic Data from Tanzania**

2026 · Journal of Economics and Business · journalarticle, journal-article · https://doi.org/10.31014/aior.1992.09.03.730

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; economic framing of sports betting as investment, but socio-economic data on Tanzanian bettors might include a problem-gambling measure.

**Решение:** =

---

### 121 · R0859

**Sports Betting Ads are Everywhere. That Could be a Public Health Problem.**

2026 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-026-10497-0

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: No abstract; title sounds like a commentary on advertising, but it could be an exposure survey that also measured problem gambling.); Sonnet -1 (обзор, комментарий, теоретическая, правовая или регуляторная работа: Headline-style title about sports betting advertising as a public health problem; no abstract, likely a commentary without prevalence data.)

**Решение:** ?

---

### 122 · R0867

**Changes in Gambling Behaviors Among Young Adults**

2026 · ScholarsArchive at Johnson & Wales University (Johnson & Wales University) · conference-paper

Background: Following the repeal of PASPA in 2018, sports betting and mobile gambling have expanded rapidly across the United States. Young adults are particularly vulnerable to gambling-related harms, yet state-level post-legalization surveillance data remain limited. Methods: Cross-sectional data from the 2022 (n=1,022) and 2024 (n=1,008) Rhode Island Young Adult Surveys were analyzed. Gambling behaviors and problem gambling (Brief Biosocial Gambling Screen) were compared across years. Multivariable logistic and Poisson regression models adjusted for age, race/ethnicity, sexual/gender status, and subjective social status. Results: Overall gambling participation remained stable (40.6% in 2022 vs. 38.6% in 2024). However, among gamblers (n=803), participation increased significantly in sports betting (AOR=1.65, 95% CI: 1.07‚Äì2.56), casino slot machines (AOR=2.99, 95% CI: 2.10‚Äì4.27), internet gambling (AOR=1.69, 95% CI: 1.00‚Äì2.88), and app-based gambling (AOR=2.14, 95% CI: 1.38‚Äì3.32). The number of gambling types engaged in increased by 28% (IRR=1.28, 95% CI: 1.16‚Äì1.41). Problem gambling rose from 2.5% to 4.3% but was not statistically significant after adjustment. Conclusions: Although overall participation did not increase, gambling behaviors became more diversified and mobile-oriented. These findings underscore the importance of continued surveillance and targeted public health prevention among young adults in the post-legalization era.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Young adult survey measured sports betting participation and problem gambling (BBGS); could report PG among sports bettors.

**Решение:** =

---

### 123 · R0869

**36. The Sports Bettor: Gambling**

2026 · New York University Press eBooks · book-chapter · https://doi.org/10.18574/nyu/9781479830282.003.0043

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Book chapter on sports bettors with no abstract; probably an essay, but an empirical problem-gambling measure can't be ruled out.

**Решение:** =

---

### 124 · R0877

**Risk gambling in Brazil: National Prevalence and Structural Correlates from the Third Brazilian National Alcohol and Drugs Survey (LENAD III).**

2026 · Revista brasileira de psiquiatria (Sao Paulo, Brazil : 1999) · journal article, journalarticle, review · eng · https://doi.org/10.47626/1516-4446-2026-4920

The rapid expansion of online gambling in Brazil has outpaced the consolidation of regulatory safeguards, raising concerns about gambling-related harm at the population level. The Third Brazilian National Alcohol and Drugs Survey (BNADS/LENAD III) investigated gambling participation and risk gambling, providing nationally representative estimates of the magnitude of the problem and identifying vulnerable groups to inform public policy. LENAD III is a survey conducted in Brazil in 2022-2023 with 16,608 individuals aged 14 years and older. Gambling participation and risk were assessed using the Problem Gambling Severity Index (PGSI). Weighted prevalence estimates and multivariable logistic regression models were used to examine associations between structural, sociodemographic, behavioural factors, and risk gambling. Past-year gambling was reported by 17.6% of the population. Overall, 6.6% fell within the PGSI risk spectrum, while 2.8% were classified as moderate- or high-risk. Risk gambling was substantially more frequent among online gamblers. In multivariable models, online gambling remained the strongest correlate of gambling-related harm. Risk gambling in Brazil is substantial and disproportionately concentrated in online betting. Regulatory responses should prioritize structural measures that address product design, advertising exposure, and access control. Strengthening enforcement and aligning regulation with public health principles are urgent priorities.

**ИИ:** + · обе модели · опрос населения об азартных играх · National Brazilian survey using the PGSI that measured gambling participation, including online betting; it likely reports activity-level data.

**Решение:** =

---

### 125 · R0880

**Who Bets Online? A Multidimensional Analysis of Demographic, Financial, and Psychosocial Predictors in Brazil's Emerging Gambling Market.**

2026 · Journal of gambling studies · journal article, journalarticle, review · eng · https://doi.org/10.1007/s10899-026-10550-y

Brazil has rapidly become one of the world's largest online betting markets, raising public health and consumer-protection concerns in a newly regulated environment. Using data from a nationally representative Brazilian survey, the 2023-2024 X-Ray of the Brazilian Investor (N = 10,305), this study examined demographic, digital, financial, and psychosocial correlates of fixed-odds online betting participation. Logistic regressions showed that participation was most strongly associated with younger age, male sex, and constant internet use. Compared with adults aged 60+, respondents aged 18-34 had substantially higher odds of betting (OR = 7.30, 95% CI [5.38, 10.08]); men also had higher odds than women (OR = 2.32, 95% CI [2.04, 2.63]), as did constant internet users compared with non-users (OR = 4.62, 95% CI [2.53, 9.48]). High-risk/high-complexity investment profiles were also positively associated with betting (OR = 1.86, 95% CI [1.28, 2.68]), whereas saving was negatively associated (OR = 0.76, 95% CI [0.66, 0.88]). Findings suggest that regulatory strategies in emerging betting markets should prioritize youth exposure, digital accessibility, and intersections between gambling and speculative financial behavior.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: National Brazilian survey of fixed-odds online betting participation; psychosocial measures may include a problem-gambling screen, but the abstract doesn't say.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Survey of online fixed-odds betting participation correlates in Brazil; no problem-gambling instrument mentioned, only demographic, financial and psychosocial predictors.)

**Решение:** -

---

### 126 · R0884

**Esports bettors versus traditional sports bettors: Differences in demographics, impulsivity, psychopathological symptoms, and gaming and gambling behavior.**

2026 · Comprehensive psychiatry · article, comparative study, journal article · eng · https://doi.org/10.1016/j.comppsych.2026.152667

BACKGROUND AND AIMS: Esports betting (i.e., betting on the outcome of professional competitive videogaming matches) has become a regular feature of most online gambling websites in recent years. The present study compared differences between esports bettors and traditional sports bettors, in addition to exploring factors that predict participation in esports betting. METHODS: Data regarding demographics, impulsivity, psychopathological symptoms, gaming, and gambling among 359 esports bettors (mean age = 37.98 years [SD = 13.64]; 86.9% male) and 326 sports bettors (mean age = 43.79 years [SD = 13.75]; 91.7% male) from the United Kingdom, Hungary, and Canada were collected through surveys via two gambling service providers (Betway and Midnite) and a gaming magazine. RESULTS: Compared to sports bettors, esports bettors were significantly younger, scored higher on gambling risk severity, and had more gaming disorder symptoms. Esports bettors were also more likely than sports bettors to report higher levels of stress, anxiety, and depression symptoms, and impulsivity, as well as be driven by coping, social, and financial motives to engage in betting. In an unadjusted binary regression model, being younger, being driven by coping, social, and financial motives, and reporting elevated levels of impulsivity, depression, anxiety, and stress symptoms were predictors of esports betting. Higher rates of problem gambling severity and gaming disorder symptoms were also predictors of esports betting. CONCLUSIONS: The findings suggest that esports bettors are a distinct betting group, and vulnerable to multiple gaming/gambling-related harms and psychopathological harms.

**ИИ:** + · обе модели · беттеры + инструмент · Survey of esports and sports bettors that measured problem gambling severity (probably PGSI); prevalence by group is likely reported.

**Решение:** =

---

### 127 · R0885

**Determinants of Sports Betting Among Urban Youth in Tanzania: Evidence from Mwanza City**

2026 · Journal of Policy and Development Studies · article, journalarticle, review · und · https://doi.org/10.4314/jpds.v20i1.10

Sports betting has expanded rapidly across sub-Saharan Africa, raising concerns about its social, economic, and public health implications, particularly among youth. This study examined the determinants of sports betting among urban youth in Mwanza City, Tanzania. A cross-sectional survey was conducted among 200 respondents aged 18 years and above who had previously engaged in sports betting. Data were collected using a structured questionnaire and analyzed using descriptive statistics, chi-square tests, Spearman correlation, and logistic regression models. Results showed high betting prevalence, with 53% reporting daily or weekly participation. Betting was associated with several adverse outcomes, including concentration difficulties (66.5%), financial challenges (62.0%), and missed school or work responsibilities (56.0%). Frequent betting was significantly associated with education level, risk awareness, age group, and marital status (p &lt; 0.001). Logistic regression indicated that tertiary education (OR = 0.123) and risk awareness (OR = 0.175) significantly reduced the likelihood of frequent betting, while females had higher odds (OR = 2.893). The study highlights education and risk awareness as key protective factors and recommends strengthening gambling education, counselling services, and regulatory enforcement to reduce youth betting risks in Tanzania.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of youth sports bettors reporting harms; abstract does not say whether a standardized problem-gambling instrument was used.

**Решение:** =

---

### 128 · R0893

**Illusion of Control in Gambling Behavior in a Non-Clinical Sample of Adults Aged 40-75.**

2026 · Journal of gambling studies · journal article, article · eng · https://doi.org/10.1007/s10899-025-10452-5

The illusion of control (IoC) is a cognitive distortion implicated in risky and problem gambling. This study aimed to validate a comprehensive IoC measure, the Multi-Dimensional Rating Scale for Illusion of Control in Gambling (EEMDIC), in a large non-clinical sample of adult and aging gamblers, and to clarify how IoC relates to gambling severity, game type, and age. A total of 1,311 participants aged 40-75 completed the EEMDIC, the Problem Gambling Severity Index (PGSI), and questions on gambling habits and sociodemographics. Exploratory (n = 649) and confirmatory (n = 662) factor analyses assessed scale structure. ANOVAs, linear regressions, Mann-Whitney U tests, and Spearman correlations examined associations with game category, PGSI scores, education, occupation, and age. Factor analyses supported a reduced 14-item EEMDIC with four coherent factors: Luck, Skill, Strategy, and Rituals/Superstitious Behaviors. Higher EEMDIC scores, especially on primary-control dimensions (Skill, Strategy), were associated with greater gambling severity and engagement in strategic betting (sports, horse racing). Education correlated negatively with IoC, and occupational differences emerged. Age was modestly but significantly associated with lower IoC: it explained ≈ 2.8% of total variance and 0.9-4.1% across factors. Framing on gains or losses showed no age effect after controlling for PGSI. The EEMDIC is a reliable, multidimensional tool distinguishing primary and secondary control beliefs. Findings link primary-control beliefs to gambling harm and show modest age-related declines in IoC. The scale can inform targeted prevention and tailored interventions across game types and sociodemographic groups.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Non-clinical survey of gamblers aged 40-75 that used the PGSI and looked at game type, including sports betting.

**Решение:** =

---

### 129 · R0897

**Assessing the Effectiveness of a Responsible Sports Betting Public Service Announcement (PSA): The Role of Message Processing and Audience Characteristics**

2026 · Sport Marketing Quarterly · article, journalarticle, journal-article · en · https://doi.org/10.1177/10616934261432734

With the expansion of legalized sports betting in North America, sport organizations increasingly rely on public service announcements (PSAs) to promote responsible gambling. Guided by the elaboration likelihood model, this study examines how central and peripheral message processing relate to perceived PSA effectiveness and positive play outcomes, and whether these relationships vary by sports fandom and betting experience. Using a between-subjects experiment with 734 National Football League fans, multivariate multiple regression analyses indicate that central route processing is the dominant driver of perceived PSA effectiveness across informational, emotional, and behavioral dimensions, while peripheral processing plays a more limited role. Moderation analyses show that sports fandom and betting experience exert small, selective amplifying effects on the relationship between central processing and responsible gambling intentions, but do not broadly alter PSA effectiveness. These results offer practical guidance for operators and regulators, emphasizing the value of informative, direct messaging over celebrity-driven or emotionally evocative appeals in fostering responsible, positive play.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: PSA experiment with 734 NFL fans, including people with betting experience; the abstract doesn't say whether a problem-gambling screen like PGSI was used.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Experiment on responsible-gambling PSA effectiveness among NFL fans; outcomes are perceived effectiveness and intentions, with no problem-gambling instrument evident.)

**Решение:** -

---

### 130 · R0899

**Segmenting College Student Sports Bettors: Who Bets, Why They Bet, and How to Tailor Interventions**

2026 · Digital Scholarship - UNLV (University of Nevada Reno) · conference-paper

Sports betting is rapidly expanding on U.S. college campuses, yet little evidence exists to guide higher education leaders, regulators, and industry partners in managing related risks. This study aims to segment college student sports bettors so that prevention and intervention efforts can be tailored to their specific motivations and behaviors. Survey data from 482 college students were analyzed using Uses and Gratifications (U&G) theory for segmentation and Self-Determination Theory (SDT) for interpretation. Four motivational clusters emerged: Highly Motivated Generalists, Social Entertainment Seekers, Boredom Relief Bettors, and Low Engagement Bettors. While groups differed in behaviors, demographics did not predict cluster membership. Findings show that betting motivations are shaped by both psychological needs and technological affordances, highlighting the need for tailored approaches. This study provides actionable insights for colleges, regulators, and operators to design targeted education, prevention campaigns, and responsible marketing strategies that balance consumer engagement with harm reduction.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of college student sports bettors on motivations; the abstract doesn't say whether a problem-gambling instrument was used.

**Решение:** =

---

### 131 · R0900

**Who Bets, Why They Bet, and How They Bet: Segmenting College Students for Targeted Sports Betting Interventions**

2026 · Journal of Sport Management · article, journalarticle, journal-article · und · https://doi.org/10.1123/jsm.2025-0214

Online sports betting is rapidly expanding on U.S. college campuses, yet little evidence exists to guide higher education leaders, regulators, and industry partners in managing related risks. This study segmented college student sports bettors, so that prevention and intervention efforts can be tailored to their specific motivations and behaviors for engaging with online sports betting platforms. Data from 482 college students were analyzed using Uses and Gratifications (U&amp;G) theory for segmentation and Self-Determination Theory for interpretation. Four clusters emerged: Highly Motivated Generalists, Social Seekers, Boredom Relief Bettors, and Low Engagement Bettors. While groups differed in behaviors, demographics did not predict cluster membership. Findings show that betting motivations are shaped by both psychological needs and technological affordances, highlighting the need for tailored approaches. This study provides actionable insights for colleges, regulators, and operators to design targeted education, prevention campaigns, and responsible marketing strategies that balance consumer engagement with harm reduction.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of 482 college student sports bettors segmented by motives and behaviors; the abstract doesn't say whether a problem-gambling instrument was used.

**Решение:** =

---

### 132 · R0902

**Are Gambling Motives all the Same? The Psychometric Properties of the GMQ-F Amongst Sports Bettors.**

2026 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-025-10450-7

The Gambling Motives Questionnaire - Financial (GMQ-F) is the most widely used scale for assessing gambling motives. Although previous research supports the reliability and validity of GMQ-F scores, no study has examined its psychometric properties among sports bettors, which present distinct demographics and clinical characteristics. To this end, this study evaluated the psychometric properties and measurement invariance of the GMQ-F among 920 sports bettors. We hypothesized that the GMQ-F would exhibit a four-factor structure and conducted a confirmatory factor analysis (CFA) and exploratory structural equation modelling (ESEM) to test model fit. Participants completed measures assessing their demographic characteristics, sports betting behaviours (frequency, time spent, bet type), and problem gambling. Results indicated that the ESEM model provided an excellent fit, outperforming the CFA model, with a clear four-factor structure (social, enhancement, coping, financial) that better captured the relationship between gambling motives while allowing for minimal cross-loadings. Measurement invariance testing revealed that the GMQ-F was consistent across different types of sports bettors (in-play, single-event, and traditional), gender (man vs. woman), and ethnicity (White vs. Racialized). Regression analyses showed that social, coping, and financial motives were positively associated with problem gambling severity, while enhancement motives were negatively related to problem gambling severity among sports bettors. These findings provide evidence supporting the validity and reliability of GMQ-F scores for assessing gambling motives, and suggest its utility across a range of demographic and sports betting subgroups.

**ИИ:** + · обе модели · беттеры + инструмент · Survey of 920 sports bettors that measured problem gambling severity (likely PGSI) as an outcome.

**Решение:** =

---

### 133 · R0903

**Are Increased Gambling Problems Associated with Intentions to Reduce College Enrollment? A Population Study Across a State University System during the COVID-19 Pandemic**

2026 · International Journal of Mental Health and Addiction · article · en · https://doi.org/10.1007/s11469-026-01694-4

Abstract Prior college student research has demonstrated that risky gambling is associated with mental health concerns, but there is limited research on how gambling behavior may be associated with enrollment. This study examined data from 1831 students to determine the prevalence of gambling behaviors and problems, their relationship with mental health symptoms, and whether they were associated with students’ intentions to reduce their enrollment in college. The overall rate of gambling was 24.17% in the past year, and 6.89% of students experienced gambling problems. Gambling problems were associated with greater mood, worry, and substance use symptoms. Gambling problems were associated with intentions to reduce coursework, but not after mental health symptoms were accounted for. The high correlation between mood and worry ( r = .79) may explain why this association did not persist. These results indicate the complex relationship between gambling problems, mental health symptoms, and college enrollment.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Population survey of college students that measured gambling problems; the abstract doesn't say whether sports betting participation was measured.

**Решение:** =

---

### 134 · R0904

**Problem sports betting/gambling in U.S. undergraduate students at a large public university.**

2026 · Journal of American college health : J of ACH · journal article, journalarticle, review · eng · https://doi.org/10.1080/07448481.2026.2744233

Objective: To estimate the prevalence of potential problem gambling among college students at a large U.S. public university who reported having participated in sports betting/gambling. Participants: A customized Healthy Minds Study (HMS) Student Survey was administered to undergraduate students (n = 1,489) at a large U.S. public university in 2025. Methods: The survey assessed lifetime participation in sports betting/gambling excluding one-time events like March Madness, and the prevalence of potential problem gambling based on the 3-question NODS-CLiP, a validated screening tool. Results: Of weighted responses, 10% (152/1,471) had engaged in sports betting/gambling in their lifetime. Of students endorsing lifetime participation in sports betting/gambling, 38% (58/152) screened positive for potential problem gambling on the NODS-CLiP. Conclusions: Of college students who had engaged in sports betting/gambling, more than one third screened positive for potential problem gambling based on a validated screening tool.

**ИИ:** + · обе модели · беттеры + инструмент · Student survey reports NODS-CLiP positive screens among lifetime sports bettors (58/152); the "Review" record-type tag looks wrong.

**Решение:** =

---

### 135 · R0905

**Consent banners, dark patterns, and GDPR infringements in online gambling: Evidence from a systematic audit and online experiment**

2026 · Computers in Human Behavior Reports · article · en · https://doi.org/10.1016/j.chbr.2026.101270

Online gambling operators collect vast amounts of consumer data to track behaviour and personalise inducements. Under General Data Protection Regulation (GDPR), access to these data requires user consent, obtained via pop-up consent banners. However, such banners tend to exhibit “dark patterns” or designs which nudge users towards accepting data sharing. To date, little is known about the extent of such dark patterns in online gambling. Here, we investigated the format of consent banners used on UK gambling websites and assessed how they may influence behaviour. Study 1 reports an audit of all UK-licensed gambling sites (n = 624). We found that 86% of banners exhibited at least one dark pattern, while GDPR infringements were also identified such as 24% of sites offering no option to reject tracking and over two-thirds (67%) processing personally identifiable data prior to obtaining consent. Only 1 in 7 (14%) sites were GDPR compliant. In Study 2, an online experiment was conducted, whereby participants (n = 615) were randomly assigned to different consent banners within a simulated gambling platform. The most common banner identified in Study 1 significantly increased acceptance of tracking and produced significantly lower alignment between user choices and preferences. No association between banner decisions and self-reported gambling harm severity was detected. Overall, our findings reveal widespread dark patterns and non-compliance of GDPR requirements on UK online gambling sites, influencing users towards unintended data sharing. These findings highlight the need for stronger regulatory enforcement and stricter consent banner design standards to protect consumers.

**ИИ:** разошлись — Opus ? (неясно, есть ли ставки на спорт: Experiment with 615 participants measured gambling harm severity; unclear whether sports betting participation was recorded in the sample description.); Sonnet -6 (не про азартные игры или «ставка/лотерея» в другом смысле: Audit of consent banners and an experiment on data tracking in online gambling; no sports bettor focus or prevalence of problem gambling among sports bettors.)

**Решение:** -

---

### 136 · R0907

**The effect of television advertising on gambling behaviour: a quasi-experimental study during the 2022 Qatar FIFA World Cup.**

2026 · Addictive behaviors reports · journal article, article · eng · https://doi.org/10.1016/j.abrep.2026.100666

• This study provides evidence that − despite current restrictions on advertising around live sport in the UK − television gambling advertising increases both the frequency and probability of betting during a live televised football game in a sample of men in England. • It does so using a novel pseudo-randomised quasi-experiment. • Supported by the precautionary principle, this suggests that restrictions on television advertising around live sport may be a useful policy tool to reduce gambling behaviour and potentially subsequent gambling harm. Gambling is a recognised public health problem, and population-level advertising restrictions may be an effective way to reduce gambling-related harm. This study fills an important evidence gap by employing a quasi-experiment to estimate the impact of television gambling advertising on gambling behaviour during the 2022 Qatar World Cup. It exploits the variation in gambling advertising between two broadcasters to evaluate its impact on gambling behaviour in a real-world setting. Poisson and Logistic panel data regression models using the broadcaster in place of gambling advertising are employed with individual fixed effects and match-level controls. Betting data is from a purposive sample of 365 men aged 18 to 45 who bet on football in England. Frequency of betting on football was 16 % to 24 % higher during games televised on a channel with gambling advertising compared to one without [IRR: 1.16 – 1.24,p < 0.01]. Furthermore, participants were 22 % to 33 % more likely to place a football bet during games that contained television gambling advertising [OR: 1.22 – 1.33, p < 0.01]. Using a pseudo-randomised quasi-experiment, this study found that television advertising significantly increased both the likelihood and frequency of betting during live football games in the sample studied. This raises concerns about the adequacy of current advertising restrictions in the UK and suggests that a policy which restricts television gambling advertising around live football might be an effective part of a wider public health strategy to tackle gambling-related harms. Future studies should replicate this design, using larger, more representative samples, to inform policy.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Sample of men who bet on football; the abstract doesn't mention a problem-gambling instrument, though one such as the PGSI may have been used to describe the sample.

**Решение:** =

---

### 137 · R0917

**Sports Betting : Complex Systems**

2026 · Unpublished · presentation, text/presentation, article · und · https://doi.org/10.13140/rg.2.2.21344.44806

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Unpublished presentation with no abstract; 'complex systems' suggests modelling or theory, but a survey of bettors can't be ruled out.

**Решение:** =

---

### 138 · R0920

**Gambling and Problem Gambling in Germany: Data from the Gambling Survey 2025 and the OASIS Player Exclusion System**

2026 · Digital Scholarship - UNLV (University of Nevada Reno) · conference-paper

With the enactment of the new State Treaty on Gambling on July 1, 2021, the availability of legal gambling in Germany has increased significantly. In addition to the existing licenses for land-based casinos, gambling halls with German-style slot machines, and lotteries, a comprehensive legalization of sports betting was implemented, together with the granting of licenses to operators of virtual slot machines, online poker, and casinos. At the same time, the State Treaty introduced a central exclusion system (OASIS) for all forms of gambling, which includes both self-exclusion and third-party exclusion by relatives and gambling operators. Gambling operators are legally obliged to exclude players who may be at risk of gambling addiction. The presentation will include data from the Gambling Survey 2025 on gambling participation among the population and proportion of problem gamblers, and data on self- and third-party exclusions by type of gambling from the OASIS exclusion system.

**ИИ:** + · обе модели · опрос населения об азартных играх · A national German gambling survey that reports gambling participation and problem gambling prevalence, and sports betting is legal there, so activity-level data is likely.

**Решение:** =

---

### 139 · R0926

**Preliminary data regarding gambling activities among adolescents within a study sample in Galati, Romania**

2026 · Dezvoltarea continuă și ciclică a curriculumului educațional · article, conference-paper · und · https://doi.org/10.59295/dccce2025.23

In recent years, there has been a noticeable increase in adolescent participation in gambling activities, particularly within the virtual environment, where accessibility is facilitated by mobile devices, and game design is inspired by video games. Although gambling is illegal for minors, the prevalence of this activity remains high. Risk factors for problematic gambling include individual behaviors (alcohol consumption, depression, impulsivity), relational factors (antisocial behaviors), and community-level influences (reduced academic performance). In Romania, sports betting and lottery games are the most frequently practiced forms, which contribute to the development of illusions of control and subsequently foster problematic gambling behaviors. This study, employing an analytical cross-sectional methodology, aims to obtain preliminary data regarding gambling behavior among adolescents aged 14 to 18 years in Galați city, Romania. It identified a prevalence rate of 33.64% for gambling within the past 12 months, with the highest occurrence in the 17-18 age group. These findings highlight the urgent need to implement preventive interventions and to conduct a comprehensive national epidemiological study to inform effective public health strategies.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Adolescent gambling survey in Romania that mentions sports betting; the abstract doesn't say whether a problem-gambling instrument was used.

**Решение:** =

---

### 140 · R0929

**“Show me the money!”: Esports betting behaviour of Gen Z: antecedents, motivations and marketing exposure**

2026 · Marketing & Menedzsment · article, journalarticle, review · en · https://doi.org/10.15170/mm.2026.60.02.06

THE AIM OF THE PAPERThis study investigates the esports betting behaviour of Gen Z, focusing on psychological, social, and commercial factors associated with betting habits. It explores the relationship between early gambling socialisation, motivational factors (such as financial gain, fandom, and entertainment) and the role of different marketing exposure formats in betting propensity. METHODOLOGYThe research utilized a quantitative survey of 119 Hungarian university students with verifiable esports betting experience. Data collection occurred between March and April 2025 using convenience sampling at the Budapest University of Technology and Economics. Statistical analyses, including factor analysis, Spearman’s rank-order correlation, and binary logistic regression, were performed using IBM SPSS to test five hypotheses regarding expertise, motivations, social influence, and marketing effectiveness. MOST IMPORTANT RESULTSThe findings show that financial gain and entertainment/excitement are the strongest motivations, while fandom is less central. Early childhood exposure to gambling, particularly within family and school contexts, was positively associated with later betting habits. Regarding marketing exposure, social media advertising was positively associated with frequent betting, while affiliate marketing was not supported as the strongest format. Perceived expertise/control was not generally strong, but it was linked to more active and more optimistic betting behaviour. RECOMMENDATIONSMarketing and regulation should avoid messages that overstate skill, control, or easy financial gain. Legislative efforts should be reinforced to regulate children's exposure to gaming communications and offline betting premises. Finally, social media advertising deserves special regulatory attention because it was positively associated with frequent betting.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of esports bettors (n=119) on motivations and marketing; the abstract doesn't say whether a problem-gambling instrument was used.

**Решение:** =

---

### 141 · R0931

**Quantifying the negative impact of gambling: psychometric evaluation of the Spanish version of the Short Gambling Harm Scale (S-SGHS) among individuals engaged in gambling activities**

2026 · International Gambling Studies · article · en · https://doi.org/10.1080/14459795.2026.2670993

Gambling-related harm (GRH) extends beyond addiction, affecting multiple life domains, yet validated tools for its assessment are currently lacking for the Spanish population. This study adapted and validated a Spanish version of the Gambling Related Harm (GRH) Checklist and developed a short form (S-SGHS) to quantify GRH and facilitate population-level metrics. A Spanish survey of 800 individuals, with gambling experience in the past year, assessed their gambling behaviors, GRH (via the 72-item GRH-CL), the Problem Gambling Severity Index (PGSI), and quality of life (SF-6D, TECVASP). Confirmatory Factor Analysis (CFA) supported a unidimensional structure for the 72-item. Using a genetic algorithm and manual Item Response Theory (IRT) selection, a 12-item short form (S-SGHS-12) was derived, showing strong internal consistency and gender invariance. The S-SGHS demonstrated good predictive validity over the PGSI for quality of life (SF-6D, TECVASP), highlighting its sensitivity to subtle harms. Results underscore the need for culturally tailored instruments. The S-SGHS enables nuanced public health evaluations, informing preventive strategies beyond clinical addiction frameworks. This study provides the first validated Spanish tool for GRH assessment, advancing insights into gambling’s multifaceted impacts.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Survey of 800 Spanish past-year gamblers using the PGSI and asking about gambling behaviours; unclear whether sports betting participation was reported.

**Решение:** =

---

### 142 · R0937

**College student sports betting experiences and behaviors at a U.S. public university.**

2026 · Journal of American college health : J of ACH · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1080/07448481.2025.2503840

Abstract Objective: The primary goal was to evaluate college student sports gambling experiences and behaviors. Participants: A college student convenience sample (n = 575) was recruited at an on-campus health service during the fall 2024 semester. Methods: Clinical, public health, and health promotion staff collaborated to create a 16-item survey derived from validated screening tools, a recent national poll, and novel questions of interest informed by staff experience. Descriptive statistics summarize key data, chi-square analysis evaluates demographic differences, and an exploratory thematic analysis categorizes qualitative feedback. Results: There were significant differences (p < 0.05) in sports gambling experiences and behaviors for enrollment level and gender. Students reported knowing people with sports betting problems, experiencing pressure to sports gamble, and expressed concern about the online sports betting industry. Bettors endorsed several at risk behaviors. Conclusion: These findings identify opportunities for greater research, prevention, and support of college students around this rapidly evolving issue.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Student sports betting survey with items drawn from validated screening tools; unclear whether a full problem-gambling instrument was scored.

**Решение:** =

---

### 143 · R0964

**Social Exposure to Gambling and Gambling Involvement Among 4176 Italian Adolescents: A Cross-Sectional Study**

2026 · International Journal of Mental Health and Addiction · article · en · https://doi.org/10.1007/s11469-026-01734-z

Abstract Gambling behaviors can be viewed as the product of individual characteristics and the social environment. We analyzed cross-sectional data from 4176 Italian students aged 14–17 years using modified Poisson GEE models accounting for school-level clustering to investigate associations of sociodemographic factors and reported exposure to habitual (daily/almost daily) gambling across different social circles with gambling involvement. Overall, 53.7% of participants reported lifetime gambling experience; among them, 20.1% reported regular (≥ 1 time/month) gambling. Lifetime and regular gambling showed distinct sociodemographic patterns across age, sex, nationality, and school type. Among those with lifetime gambling experience, after mutual adjustment across social circles, knowing habitual gamblers among close relatives, friends, or acquaintances was independently associated with regular gambling, with the strongest association observed for friends (Adjusted Prevalence Ratio: 1.90, 95% CI 1.47–2.45). Regular gambling also increased with the number of social circles in which participants knew someone who gambled habitually ( p for trend < 0.001), although estimates plateaued between three and four circles. These findings suggest that adolescent gambling tends to cluster within interpersonal networks and support prevention strategies that consider both sociodemographic characteristics and the broader relational context.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of Italian adolescents' gambling; outcome is gambling frequency. Unclear if SOGS-RA or similar and sports betting were measured.

**Решение:** =

---

### 144 · R0967

**Gambling, the Zero- Sum Game among KMTC Students: A Descriptive Cross-Sectional Case Study of KMTC Mombasa Campus**

2026 · Global Journal of Health Sciences · article, journalarticle · en · https://doi.org/10.47604/gjhs.3805

Purpose: This study aimed to examine the prevalence, trend and effects of gambling on the students at the Kenya Medical Training College (KMTC) Mombasa Campus. As gambling is becoming more accepted via mobile and advertising, the research sought to evaluate the effects of gambling on student psychological health, academic achievement, and financial stability. Methodology: The study was descriptive cross-sectional study conducted on 518 students in KMTC Mombasa Campus years 1-3. Structured questionnaires were used to gather data on demographics, gambling prevalence, types, frequency, and impacts. Chi-square tests and descriptive statistics were used to analyse associations between gambling behaviour and awareness of counselling services. Findings: The prevalence rate was high (67.2%), and men (77.3%) were more involved in gambling than women (55.2%). Most popular types included sports betting (38.6%) and Aviator (16.6%). The most common consequences were psychological distress (79.1%), financial instability (75.4%), and academic disruption (33.1%). While 86.9% agreed that gambling was an addictive activity, only 31.7% of the gamblers knew about the KMTC counselling services. Gambling is a major public health and educational problem among the KMTC students at Mombasa campus, and there is some clear evidence of there being psychological, financial and academic cost. If no measures are taken, the situation will worsen, with detrimental effects on the well-being and professional growth of the students. Unique Contribution to Theory, Practice and Policy: Counselling centres to be set up at Mombasa campus, peer education and awareness campaigns to mitigate these harms. Financial literacy and responsible money management programs should be implemented, which are to be accompanied by the improvement and training of staff's competencies and gender responsive outreach programs to respond to different gambling profiles.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Student survey measured sports betting participation, but the abstract does not say whether a problem-gambling screening instrument was used.

**Решение:** =

---

### 145 · R0970

**Repetitive responsible gambling slogans and imagery may not be better than AI-generated content**

2026 · International Gambling Studies · article · en · https://doi.org/10.1080/14459795.2026.2712374

Responsible Gambling (RG) messaging is a common element in online gambling harm reduction, but current practices may be suboptimal. Artificial Intelligence (AI) technologies enable rapid development of ‘always new’ RG content, but it is unclear whether such materials could be effective. Online gamblers from Australia, Canada, the UK, and the USA (N = 657, Mage = 38.93, cisgender male = 59.97%) played a simulated electronic gambling machine with (or without) in-play RG popup messages. Popups were comprised of either real (but unfamiliar) RG content or fully AI-generated content. Some participants saw ten different popups, while others saw the same popup repeated ten times. Popup exposure was associated with lower gambling cravings (t(652) = −3.10, p = .01, η2 = .02) and intentions (t(652) = −2.18, p = .03, η2 = .02). Participants exposed to changing popups reported lower gambling intentions (F(1,498.54) = 5.24, p = .02, η2p = .01) and higher message credibility (F(1,515) = 10.55, p = .007, η2p = .02). AI-generated messages were more recognizable (F(1,279.36) = 29.54, p < .001, η2p = .07) and less discouraging of gambling in general (F(1,515) = 12.40, p = .002, η2p = .02), but otherwise did not significantly differ from real RG content. These initial results suggest non-repetition may be important for RG content efficacy, while origin (human- or AI-generated) may be less important. Pending replication, operators and regulators could consider scaling ongoing efforts to deploy more varied RG content using AI-generated materials.

**ИИ:** разошлись — Opus ? (неясно, есть ли ставки на спорт: Experiment on RG messaging with online gamblers; the full text may include PGSI and activity participation, but sports betting isn't mentioned.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Experiment on responsible gambling popups in simulated slot play; no sports betting focus and no problem-gambling prevalence measure reported in abstract.)

**Решение:** -

---

### 146 · R0974

**Qu'est-ce qui fait gagner ? Une étude des déterminants du succès chez les parieurs sportifs à Mbujimayi**

2026 · Revue Internationale de la Recherche Scientifique (Revue-IRS) · article · fr · https://doi.org/10.5281/zenodo.18195630

Cette étude vise à identifier les principaux déterminants du succès au pari foot, un jeu de hasard dont les mécanismes restent largement influencés par l’incertitude. En s’appuyant sur la littérature existante et sur une analyse en composantes principales (ACP), la recherche regroupe un large ensemble de variables cognitives, situationnelles et personnelles en quatre facteurs majeurs : la stratégie et la préparation analytique, la compétence technique face au hasard, la motivation et les caractéristiques individuelles, ainsi que la maîtrise des outils technologiques. Les résultats montrent que, si certaines stratégies et compétences semblent améliorer les performances des parieurs, le hasard demeure une composante essentielle, limitant la prédictibilité des résultats sportifs. Le succès repose donc sur une combinaison de connaissance, d’analyse, de motivation et d’outils numériques, tout en restant fortement conditionné par l’aléa. L’étude insiste sur l’importance d’une pratique responsable du pari sportif et met en garde contre les biais cognitifs, notamment l’illusion de contrôle. Elle ouvre enfin des pistes de recherche portant sur d’autres dimensions psychologiques ou contextuelles, ainsi que sur le rôle des dispositifs de régulation et de prévention.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of football bettors in Mbujimayi on what predicts betting success; the abstract names no problem-gambling instrument, though one may have been used.

**Решение:** =

---

### 147 · R0976

**Brand loyalty and tribalism motivational factors in sports betting in the post-pandemic era**

2026 · International Journal of Business and Systems Research · journalarticle, article, journal-article · en · https://doi.org/10.1504/ijbsr.2027.10081655

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; likely a survey of sports bettors' motives, and it is unclear whether a problem-gambling instrument was used.

**Решение:** =

---

### 148 · R0977

**The Effect of Message Framing Type on Gambling Passion among Sport Bettors : The Moderating Role of Sport Betting Involvement**

2026 · 한국스포츠산업경영학회지 · article, journalarticle, journal-article · en · https://doi.org/10.31308/kssm.31.3.98

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Quantitative study of sport bettors on message framing and gambling passion; no abstract, so unclear whether a problem-gambling instrument was used.

**Решение:** =

---

### 149 · R0981

**Gambling refusal self-efficacy and protective behavioral strategies mediate and moderate the relationships between impulsivity and gambling outcomes**

2026 · Scientific Reports · article · en · https://doi.org/10.1038/s41598-026-46112-w

Studies suggest that refusal self-efficacy and protective behavioral strategies may influence how impulsivity relates to addictive behaviors. However, their mediating and moderating roles have not yet been examined in the context of gambling. This study investigated whether gambling refusal self-efficacy (GRSE) and gambling protective behavioral strategies (GPBS) mediate or moderate the associations between impulsivity and gambling outcomes, including problem gambling (PG) and gambling involvement. A cross-sectional online survey was conducted among 926 gamblers from the general population (females: 53.2%; age: M = 41.85, SD = 13.49). Standardized self-report measures were used, including the Problem Gambling Severity Index, the Consumption Screen for Problem Gambling, the Barratt Impulsiveness Scale, the Gambling Self-Efficacy Questionnaire, and the Gambling Protective Behavior Scale. Linear regression-based mediation and moderation models were tested. Significant indirect associations between impulsivity and both PG and gambling involvement were observed via GRSE and GPBS. In addition, a significant interaction between impulsivity and GPBS indicated that associations between impulsivity and gambling outcomes were evident primarily at lower GPBS levels, whereas they were non-significant at higher levels. These findings extend prior evidence from other addictive behaviors to gambling, highlighting potential similarities across addictive processes. Longitudinal studies using representative or clinical samples are warranted.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · General-population gambler survey using PGSI; gambling involvement may include sports betting participation, but the abstract doesn't say.

**Решение:** =

---

### 150 · R0987

**Greater impulsivity is associated with a reduced propensity to cash out of bets.**

2026 · Addictive behaviors reports · article, journal article, research-article · eng · https://doi.org/10.1016/j.abrep.2025.100645

A common feature of contemporary sports-betting apps is 'instant cash-out', which allows users to settle a bet early in exchange for a discounted immediate payout. Despite high prevalence and links with gambling-related harm, relatively little is known about how personality traits associated with gambling, such as impulsivity, predict instant cash-out usage. To address this question, we recruited 145 general-population adult participants (69 men, 66 women, 10 non-binary or undisclosed; M age = 36.3, SD = 10.7; participants resided in Australia, Canada, Ireland, New Zealand, the UK, or the USA) to complete five self-report questionnaires related to impulsivity, as well as the Problem Gambling Severity Index (PGSI), and a validated cognitive task measuring individual differences in cash-out frequency. We then assessed how cash-out frequency in the behavioral task was associated with both self-reported impulsivity and PGSI. We found that cash-out frequency was negatively correlated both with PGSI scores and with a number of impulsivity-related traits including Dysfunctional Impulsivity, Lack of Premeditation, Positive Urgency, Sensation Seeking, and Fun Seeking. An exploratory factor analysis revealed that higher scores on a latent 'Dysfunctional Impulsivity' factor were negatively associated with cash-out frequency overall, whereas higher scores on an 'Inhibition and Inflexibility' factor predicted higher cash-out frequency specifically for bets with a low win probability. Taken together, results suggest that instant cash-out may primarily appeal to less impulsive people and those with lower PGSI scores. This raises the possibility that instant cash-out may specifically facilitate increased gambling behaviors among people with less prior experience of gambling.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · General-population sample given PGSI and a cash-out task; unclear whether real sports betting participation was recorded.

**Решение:** =
