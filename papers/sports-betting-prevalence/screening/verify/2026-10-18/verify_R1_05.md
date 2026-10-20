# Проверка с метками ИИ, часть 5

Записи 601–750 из 1525, с метками обеих моделей над строкой решения. Модели согласны и вы тоже — поставьте `=`; иначе свой код (`+`, `?` или `-`, причина не нужна). Если модели разошлись, `=` не годится — нужен ваш код. Решаете вы.

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

### 601 · R3167

**A health inequality examination of problem gambling, substance abuse, mental health, and poverty in the United Kingdom; A secondary analysis and stakeholder interviews**

2023 · Greo Evidence Insights · casereport, review, report · en · https://doi.org/10.33684/2024.003

Purpose: This project is focused on the social determinants of health associated with problem gambling and examined gambling-related disparities and the determinants of negative health outcomes. Social determinants include social class education, ethnic group, age, and sex (Elton-Marshall, et al., 2017). The main aims of the study were as follows: Aim 1: In this study, we used the large data set to determine subpopulations who are experiencing social inequity (e.g., youth, older adults, women, Black people and other minority ethnic groups, and people with low income; see Elton-Marshall, et al., 2017) to determine how much they are impacted by gambling. Aim 2: We tested the data as an interaction model to see if there are disparities in the impact of gambling by sociodemographic variables. The analysis included tests of the factorial structure of the Problem Gambling Severity Index (PGSI) across subpopulations (e.g., young vs. old, low-income vs. higher income, and Scotland vs England). Aim 3: In addition, we conducted interviews with a small number of key stakeholders who were treatment providers or administrators of problem gambling services to discuss the research findings and to help us understand the data and develop a dissemination plan. Methodology: This project consisted of a secondary analysis of the “Gambling in England and Scotland, 2016: Combined Data from the Health Survey for England and the Scottish Health Survey.” We concatenated the data from 2012, 2014, and 2016. This study is a secondary analysis of a large data set. The project incorporated a series of statistical analysis including logistic regression, multinominal regression, cluster analysis and confirmatory factor analysis and to explore the relationship between gambling and social and demographic variables. Results: Based on our analysis combining the DSM and PGSI, about half a percent of the adults in England and Scotland met the threshold for a severe gambling problem. In terms of gambling behaviors, the most common games were national lottery tickets, scratch cards, and other lotteries. As expected, social and demographic variables were both significantly associated with problem gambling. Significant social and demographic risk factors for problem gambling include sex (male), age (being younger, 25 to 34), marital status (being single or never married), social class (manual and routine labour), ethnic /racial group (Black or other), and education (lower levels of education). In addition, being a heavy drinker, a current smoker and having a lower level of Wellbeing were also related to problem gambling. Although the results suggest that people in Scotland gamble somewhat more often especially on lotteries, Country (England vs. Scotland) was not associated with gambling problems. In terms of games played, according to the logistic regression, the largest association was for electronic gambling machines (EGMs), followed by Sports gambling and then online gambling. The interaction of games with sex is interesting suggesting that the male vs. female differences is smaller for EGMs and online gambling, but larger for sports gambling. As Part of Aim 2, we tested the psychometric properties of the PGSI gambling inventory and found that the PGSI was a valid construct for measuring problem gambling in the United Kingdom (UK). Moreover, we found that the PGSI scale operated similarly for respondents from both England and Scotland, suggesting generalisability across the UK. In terms of Aim 3, the key stakeholder interviews, most of the stakeholders felt that the reported frequencies were lower than they expected and questioned the accuracy of the prevalence estimates. Several stakeholders noted that some ethnic communities (Chinese, Muslims) were not adequately represented in the survey, and speculated that this was due to under reporting. Several stakeholders also suggested that the prevalence of gambling problems among women who gamble may be higher than males who gamble, however analysis did not support this view. In terms of directions for future research, the stakeholders suggested the need to better understand the impact of trauma on gambling, the potential side effects of medication(s), and a more comprehensive examination of environmental factors during childhood that increase the risk of problem gambling during adulthood. Overall, the stakeholders felt that the results provide useful information but note that more research is needed to better understand gambling problems. Finally, several stakeholders believed that both government and industry should do more to help reduce problem gambling; however, one stakeholder cautioned that over regulation could backfire and push gamblers to non-regulated gambling sites. Conclusions: The results of this research provide a detailed examination of the association between problem gambling and the social determinants of health in the UK. In summary, the key findings are that social and demographic risk factors for problem gambling include sex (male), age (being younger, 25 to 34), marital status (being single or never married), social class (manual and routine labour), ethnic /racial group (Black or other), education (lower levels of education), are significant factors in determining problem gambling. In addition, being a heavy drinker, a current smoker and having a lower level of Wellbeing, more psychological distress, and a greater rate of mental health problems, were also related to problem gambling. This knowledge will help to inform public health strategies in the UK related to the prevention and treatment of gambling disorders, as well as the prevention of gambling-related harm at the population level and for different groups (e.g., age groups, income groups, ethnic groups). Implications: 1. Problem gamblers are more likely to have lower levels of education, were less likely to be in managerial work, and in terms of ethnic group were Black or other. 2. Problem gamblers are physically healthy, but have an elevated risk of mental health problems, have a poorer sense of well-being and are more likely to smoke or engage in heavy drinking. 3. The results found that country (England vs. Scotland) was not associated with differences in gambling problems, however, people in Scotland gamble somewhat more often especially on Lotteries. 4. In terms of Aim 2, the results suggest that the PGSI is a valid measure of gambling in the Great Britain and that it is equally valid for both England and Scotland. 5. Non-problem gamblers appear to be a relatively healthy population and had the best scores in terms of mental health and well-being, though the contrasts with non-gamblers were trivial. 6. Non-problem gamblers had a somewhat greater rate of smoking, heavy drinking and obesity compared to non-gamblers suggesting they may have more health problems eventually. Effort should be made to encourage more physical activity amongst recreational gamblers.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Secondary analysis of England/Scotland health surveys with PGSI/DSM; sports gambling's association with problem gambling is analysed.

**Решение:** =

---

### 602 · R3173

**Predicting Risky Decision Making (Odds Selection) in Regular Soccer Gamblers from Nigeria using Cognitive Tasks Combined with Non-Cognitive Measures.**

2023 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-022-10159-x

As real time soccer gambling is becoming a game of choice for many Nigerian youths, there is need to examine some predictive factors that could account for risky decision making in the population. We combined some cognitive tasks (memory, concentration, executive function and problem solving) and non-cognitive measures (time taken to complete a bet, years of gambling and addiction tendency measures) to derive a more parsimonious model of predicting risky decision making in this population. Twenty-eight undergraduate students that endorsed regular involvement (at least once a week) in soccer betting and were willing to come to the psychology lab for testing were recruited. Four neuropsychological measures (Craft Story 21: Immediate and delayed, Number Span Test: Forward and backward, Trail Making Test: A&B, Tower of Hannoi and a gambling questionnaire (Gamblers Anonymous Questionnaire) were used for the study. Study design was correlational and linear regression (step wise method) was used for data analysis. Step wise regression statistics yielded nine possible model combinations with high predictive strengths. Overall, model 9 (with adjusted R 2 = 0.57) that has 6 measures including one from non-cognitive and 5 from cognitive measures was adjudged to be most parsimonious putting into consideration its predictive strength and number of tasks required. The tasks in our most parsimonious model were: time taken to complete a bet (non-cognitive), Craft Story 21: immediate (cognitive: memory), Number Span Forward: Total correct and longest correct (cognitive: concentration), Trail Making Test: B (cognitive: executive function) and Tower of Hannoi: Time taken to complete (cognitive: problem solving). Pearson product moment correlation between the predictor variables and the dependent variable (number of odds selected) showed inverse correlation of Craft Story Immediate, Number Span total correct and Number span longest correct suggesting strong divergence of these variables to odd selection. Time taken to complete bet, Trail Making Test: B and time taken to complete Tower of Hannoi respectively had positive correlations with number of odds selected. Our results suggest that multiple domains of cognitive abilities and time taken to complete a bet are important for predicting gamblers at risk for poor decision making. It further suggests that use of single task for a particular cognitive domain could be sufficient in predicting persons at risk for decision making. Overall, our study suggests that risky decision making in real time sports betting could be predicted using fewer neuropsychological tasks measuring wider domains of brain behaviour and a non-cognitive measure.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · 28 regular soccer bettors assessed with the Gamblers Anonymous 20 Questions; unclear whether a problem-gambling cutoff or case count is reported.

**Решение:** =

---

### 603 · R3186

**This time with feeling: In-play sports betting as a vehicle for emotion regulation.**

2023 · Psychology of addictive behaviors : journal of the Society of Psychologists in Addictive Behaviors · article, journal article, journalarticle · eng · https://doi.org/10.1037/adb0000966

OBJECTIVE The purpose of this research was to assess factors (i.e., emotion regulation, impulsivity) that motivate in-play sports betting. Specifically, we examined whether individuals report increased excitement after placing an in-play bet and whether trait negative and positive urgency moderate the effect of emotion regulation motives on in-play betting frequency. METHOD Three cross-sectional studies were conducted, each following a major sporting event: Superbowl LVI (56) (Study 1), March Madness Final (Study 2), and Union of European Football Associations Champions League Final (Study 3). Participants were U.S. (NStudy 1 = 111; NStudy 2 = 121) and U.K. (NStudy 3 = 239) residents who reported placing at least one in-play bet during the respective sporting events. Participants completed self-report measures of excitement, emotion regulation motives, in-play betting frequency, problem gambling, and trait affective impulsivity. Data from the three studies were pooled to conduct an integrative data analysis (IDA). RESULTS Participants reported increased excitement after placing an in-play bet (p < .001). In bivariate analyses, greater emotion regulation motives were associated with greater in-play betting frequency (p < .05). In moderation analyses, emotion regulation motives interacted with trait negative (p < .001) and positive urgency (p < .001) to predict in-play betting frequency, such that the bivariate effects were amplified among those higher (relative to lower) in trait affective impulsivity. CONCLUSIONS In-play sports betting is an exciting activity that people who gamble may engage in to regulate their emotions. These effects are amplified in those with high trait affective impulsivity. Responsible gambling tools such as mandatory play breaks may discourage the continuation of impulsive betting episodes. (PsycInfo Database Record (c) 2023 APA, all rights reserved).

**ИИ:** + · обе модели · беттеры + инструмент · Three surveys of in-play sports bettors (US, UK) that measured problem gambling; the specific instrument isn't named in the abstract.

**Решение:** =

---

### 604 · R3187

**Who makes in-play bets? Investigating the demographics, psychological characteristics, and gambling-related harms of in-play sports bettors.**

2023 · Journal of behavioral addictions · article, journal article, journalarticle · eng · https://doi.org/10.1556/2006.2023.00030

Abstract Background and aims Sports betting has increased markedly in recent years, in part due to legislative changes and the introduction of novel forms of sports betting (e.g., in-play betting). Some evidence suggests that in-play betting is more harmful than other types of sports betting (i.e., traditional and single-event). However, existing research on in-play sports betting has been limited in scope. To address this gap, the present study examined the extent to which demographic, psychological, and gambling-related constructs (e.g., harms) are endorsed by in-play sports bettors relative to single-event and traditional sports bettors. Methods Sports bettors ( N = 920) aged 18+ from Ontario, Canada completed an online survey containing self-report measures of demographic, psychological, and gambling-related variables. Participants were classified as either in-play ( n = 223), single-event ( n = 533), or traditional bettors ( n = 164) based on their sports betting engagement. Results In-play sports bettors reported higher problem gambling severity, endorsed greater gambling-related harms across several domains, and reported greater mental health and substance use difficulties compared to single-event and traditional sports bettors. There were generally no differences between single-event and traditional sports bettors. Discussion Results provide empirical support for the potential harms associated with in-play sports betting and inform our understanding of who may be at risk for increased harms associated with in-play betting. Conclusions Findings may be important for the development of public health and responsible gambling initiatives to reduce the potential harms of in-play betting, particularly as many jurisdictions globally move towards legalization of sports betting.

**ИИ:** + · обе модели · беттеры + инструмент · Survey of 920 Ontario sports bettors that measured problem gambling severity (probably PGSI) by bettor type.

**Решение:** =

---

### 605 · R3189

**Young male athletes at risk for problem gambling: Findings from a cross-sectional study in Sweden.**

2023 · Scandinavian journal of psychology · journal article · eng · https://doi.org/10.1111/sjop.12934

Previous research has shown that male athletes at the elite level in Sweden have a higher proportion of gambling problems than the average male population in the country. However, there is a knowledge gap in the prevalence of gambling problems among young athletes. To address this gap, this study aimed to explore gambling behavior among young athletes and to examine the associations between individual and environmental factors and problem gambling. The cross-sectional survey comprised questions from the Problem Gambling Severity Index and the Alcohol Use Disorders Identification Test, in addition to self-constructed items on individual and environmental factors. The data were derived from a sample of 1,636 students from the National Sports Education Program (NIU) and 816 grassroots athletes of the same age (16-20 years old). The results showed that male athletes had a higher prevalence of problem gambling compared to female athletes, and that a large proportion of male athletes had gambled during school hours. The prevalence of problem gambling was almost zero for women. The prevalence of problem gambling among male athletes over 18 years of age was 9% in NIU athletes and 3.6% in grassroots athletes, while for men under 18 years of age, the prevalence was 4.9% in NIU athletes and 1.3% in grassroots athletes. The study highlights the importance of considering contextual factors such as the school and team environment in preventing problem gambling among young male athletes.

**ИИ:** разошлись — Opus ? (неясно, есть ли ставки на спорт: Survey of young Swedish athletes using PGSI; sports betting participation is likely measured but the abstract doesn't say so.); Sonnet + (игроки, есть ставки на спорт и инструмент: Survey of young athletes using PGSI and gambling behaviour; likely reports sports betting and problem gambling by activity in full text.)

**Решение:** ?

---

### 606 · R3197

**The relationship between problematic gambling severity and engagement with gambling products: Longitudinal analysis of the Emerging Adults Gambling Survey.**

2023 · Addiction (Abingdon, England) · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1111/add.16125

Abstract Aims To measure the association between problem gambling severity and 19 different gambling activities among emerging adults (aged 16–26). Design An online non‐probability longitudinal survey collecting data in two waves: wave 1, July/August 2019; wave 2, July/October 2020. Setting Great Britain Participants A total of 2080 young adults participating in both waves. Measurements Problem gambling scores were collected using the Problem Gambling Severity Index (PGSI). Binary variables recorded past year participation in 19 different gambling forms, ranging from lotteries to online casino and gambling‐like practices within digital games (e.g. loot box purchase, skin betting). Controls included socio‐demographic/economic characteristics, the Eysenck Impulsivity Scale and the number of gambling activities undertaken. Findings Zero inflated negative binomial model lacked evidence of an effect between past year participation in any individual activities and subsequent PGSI scores. However, negative binomial random effects models for current gamblers ( n = 497) showed that skin betting (incidence‐rate ratio [IRR] = 2.32; 95% CI = 1.69–3.19), fixed odd betting terminals (IRR = 2.21, 95% CI = 1.61–3.05), slot/fruit machines (IRR = 1.43, 95% CI = 1.07–1.91), online betting on horse/dog races (IRR = 1.53, 95% CI = 1.17–2.00) and online betting on non‐sports events (IRR = 1.44, 95% CI = 1.11–1.89) were associated with increased PGSI scores. Online casino gambling had a significant interaction by wave; the impact of online casino betting in wave 2 on PGSI scores increased by a factor of 1.61. Conclusions Past year participation of young adults (aged 16–26) in certain forms of gambling does not appear to be associated with future Problem Gambling Severity Index scores. Among young adults who are current gamblers, past year participation in certain land‐based (e.g. electronic gaming machines) and online forms (e.g. skin betting) of gambling appears to be strongly associated with elevated Problem Gambling Severity Index scores.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Emerging adults survey with PGSI and 19 gambling activities, including sports betting forms; PGSI may be reported by activity.

**Решение:** =

---

### 607 · R3204

**Bet On It: The New Arena of Sports Fandom**

2023 · SSRN Electronic Journal · preprint · en · https://doi.org/10.2139/ssrn.4422756

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; SSRN preprint on sports betting and fandom could be a fan survey, but it may be economic or legal analysis.

**Решение:** =

---

### 608 · R3215

**Football Betting Among University Students in Ghana**

2023 · Emerald Group Publishing Limited eBooks · part of book or chapter of book, book-chapter · en · https://doi.org/10.1108/s1476-285420230000018007

Abstract Football is a popular sport among young people across Africa, incited by the heavy presence of European football that has become central to youth cultures, everyday social routines, forms of consumption and opportunities for establishing social status. A growing body of evidence suggests increasing trends in harmful gambling behaviours in African youth, while the proliferation of football betting particularly remains a critical potential risk for negative mental health outcomes among young people in Sub-Saharan Africa. This chapter draws on original empirical data from a web-based cross-sectional survey to examine the prevalence estimates and associations of socio-demographic and behavioural factors with football betting among young adults attending university in Ghana. It draws on a multivariable logistic regression model to assess the associations with football betting. Our findings point not only to the growing salience of football betting among male demographics, but also the role of peer culture, alcohol and media as predominant sources of participants' initiation of football betting. Moreover, participants indicated the motive ‘to make money’ as their single major motivation, which raises the prospect that football betting is used as a means to mitigate the adverse effects of unemployment. Overall, the study points to a need for harm prevention strategies that align more closely with public health approaches focused on students, their families, their communities and their universities/schools.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of Ghanaian students on football betting; mentions harmful gambling, but the abstract doesn't say whether a PG instrument was used.

**Решение:** =

---

### 609 · R3220

**Prediktori učestalosti klađenja na sportske događaje**

2023 · Sveučilište u Zagrebu. Filozofski fakultet. Odsjek za psihologiju. · master thesis · hrv · https://www.bib.irb.hr/1274447

Sports betting is a type of gambling that is becoming ever more prevalent in the Croatian society. The alarming data shows that a large percentage of Croats place bets on monthly basis (17,4% of men population). Unfortunately, this trend is visible with high school students as well, 72,9% of whom report to have placed a sport bet at least once in their life. A worrisome 12,9% of high school students show severe gambling problems. The aim of this research was to determine how some predictors (locus of control, cognitive distortions, coping mechanisms and cognitive styles) might affect the frequency of one's sports betting and whether the frequency of betting is related to gender and problem gambling severity. The research was conducted online, with a convenience sample of 433 participants, aged 16-71 years. The results of the hierarchical regression analysis on male sample confirm previously found positive correlations between the sports betting and the illusion of control, as well as the negative relation of sports betting and coping mechanisms directed towards problem-solving. On top of these results, a positive moderate correlation has been confirmed between the betting frequency and addiction to sports betting. These results could help in early identification of individuals susceptible to risky behaviors, as well as with the addiction-prevention interventions aimed at adolescents and adults. Klađenje na sportske događaje vrsta je kockanja koja je sve zastupljenija u hrvatskom društvu. Alarmantni podaci u Republici Hrvatskoj ukazuju na velik broj građana koji sudjeluju u ovoj aktivnosti na mjesečnoj osnovi (17,4% muškaraca). Nažalost, trend je vidljiv i kod srednjoškolaca, od kojih se 72,9% barem jednom upustilo u neki oblik kockanja, a čak 12,9% ih pokazuje visoku razinu problematičnog kockanja. Svrha ovog istraživanja bila je ispitati kako neki prediktori (lokus kontrole, kognitivne distorzije, mehanizmi suočavanja i kognitivni stilovi) mogu predvidjeti učestalost klađenja na sportske događaje te je li učestalost klađenja na sportske događaje povezana s rodom i problematičnošću kockanja. Istraživanje je provedeno online, na prigodnom uzorku od 433 sudionika, u dobi od 16 do 71 godine. Rezultati multiple regresijske analize na muškom uzorku potvrđuju prethodna istraživanja o pozitivnoj povezanosti klađenja na sportske događaje i iluzije kontrole te negativnoj povezanosti klađenja na sportske događaje i suočavanja usmjerenog na problem. Povrh toga, potvrđena je i umjereno visoka pozitivna povezanost učestalosti klađenja i razine problematičnog kockanja. Rezultati ovog istraživanja mogu pomoći u ranoj identifikaciji pojedinaca podložnih rizičnom ponašanju te edukaciji i intervenciji kod adolescenata i odraslih u svrhu prevencije pojave ovisničkog ponašanja.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Online survey of 433 people that measured sports betting frequency and problem gambling severity, but the abstract does not name the instrument.); Sonnet + (беттеры + инструмент: Online survey of 433 Croatian participants on sports betting frequency, with problem gambling severity/addiction to sports betting measured; likely reports PG among bettors.)

**Решение:** ?

---

### 610 · R3221

**GAMBLING HABITS AMONG VIDEO GAME PLAYERS**

2023 · Zdravstveni glasnik · article, journalarticle · en · https://doi.org/10.47960/2303-8616.2023.2.9.10

Introduction: Gambling is a legal and socially accepted recreational activity that can progress into a serious public health problem. The prevalence of gambling is higher among men of younger age and lower economic status, and older divorced men. There are many similarities between playing video games and gambling that the industry encourages by implementing the elements gambling into video games, and the elements of video games in gambling, but despite the similarities, in problem use we recognize two separate behavioral disorders. Methods and participants: The research was conducted on an intentional and judgmental sample of adolescents and young adults who play video games. A questionnaire containing questions on sociodemographic characteristics, video game playing and gambling habits, and the SOGS-RA was used to assess the gambling risk. Results: Most of the participants gamble very rarely or not at all, but 5.1% of the participants gamble every day. Almost all of the participants play several types of games of chance, with lottery games, sports betting and games on electronic devices leading the way. Pronounced problems with gambling were recognized in 28.3% of the research participants. Discussion: The lifetime prevalence of gambling in this research is similar to the results of other research conducted among video game players, although the results of all research in this area are not homogeneous. When comparing the results of gambling among video game players and the general population, the prevalence of gambling among video game players is significantly higher than in the general population. Conclusion: Adolescent and young adult video game players play more games of chance, and prefer gambling games that have a higher addictive potential. Considering the age, easy accessibility and the difficult recognition of the development of problem gambling, it is important to focus preventive activities on the youngest age group. Key words: games of chance, video game players, problem gambling

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Survey of young video game players measured sports betting participation and SOGS-RA problem gambling.

**Решение:** =

---

### 611 · R3222

**Navike kockanja među igračima videoigara**

2023 · Zdravstveni glasnik = Health bulletin · article · und · https://hrcak.srce.hr/311267

Introduction: Gambling is a legal and socially accepted recreational activity that can progress into a serious public health problem. The prevalence of gambling is higher among men of younger age and lower economic status, and older divorced men. There are many similarities between playing video games and gambling that the industry encourages by implementing the elements gambling into video games, and the elements of video games in gambling, but despite the similarities, in problem use we recognize two separate behavioral disorders. Methods and participants: The research was conducted on an intentional and judgmental sample of adolescents and young adults who play video games. A questionnaire containing questions on sociodemographic characteristics, video game playing and gambling habits, and the SOGS-RA was used to assess the gambling risk. Results: Most of the participants gamble very rarely or not at all, but 5.1% of the participants gamble every day. Almost all of the participants play several types of games of chance, with lottery games, sports betting and games on electronic devices leading the way. Pronounced problems with gambling were recognized in 28.3% of the research participants. Discussion: The lifetime prevalence of gambling in this research is similar to the results of other research conducted among video game players, although the results of all research in this area are not homogeneous. When comparing the results of gambling among video game players and the general population, the prevalence of gambling among video game players is significantly higher than in the general population. Conclusion: Adolescent and young adult video game players play more games of chance, and prefer gambling games that have a higher addictive potential. Considering the age, easy accessibility and the difficult recognition of the development of problem gambling, it is important to focus preventive activities on the youngest age group. Uvod: Kockanje je legalna i društveno prihvaćena zabavna aktivnost koja se može progredirati u ozbiljan javnozdravstveni problem. Prevalencija kockanja je veća kod muškaraca mlađe životne dobi i nižeg ekonomskog statusa i starijih razvedenih muškaraca. Postoji velik broj sličnosti između igranja videoigara i kockanja koje industrija potiče uvodeći elemente kockanja u videoigre i elemente videoigara u kockanje, no unatoč sličnostima, kod problematične upotrebe govorimo o dva zasebna bihevioralna poremećaja. Metode i sudionici: Istraživanje je provedeno na namjernom prosudbenom uzorku adolescenta i mlađih odraslih osobama koji igraju videoigre. Korišten je upitnik s pitanjima sociodemografskih obilježja, navika igranja videoigara i kockanja i SOGS-RA za procjenu rizičnosti kockanja. Rezultati: Većina sudionika kocka vrlo rijetko ili uopće ne kocka, no 5,1% sudionika kocka svaki dan. Gotovi svi igraju više vrsta igara na sreću, a prednjače lutrijske igre, sportska kladionica i igre na elektronskim aparatima. Izraženi problemi s kockanjem su prepoznati kod 28,3% sudionika istraživanja. Rasprava: Životna prevalencija kockanja u ovom istraživanju je slična rezultatima drugih istraživanja među igračima videoigara iako nisu rezultati svih istraživanja na tom području homogeni. Uspoređujući rezultate kockanja među igračima videoigara i u općoj populaciji, prevalencija kockanja među igračima je znatno viša nego u općoj populaciji. Zaključak: Adolescenti i mlađi odrasli igrači videoigara igraju više igara na sreću, preferirajući kockarske igre koje imaju veći adiktivni potencijal. S obzirom na dob, laku dostupnost i teško prepoznavanje razvoja problematičnog kockanja, važno je usmjeriti preventivne aktivnosti na što mlađu dobnu skupinu.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Survey of young video game players that measured sports betting participation and used SOGS-RA; may report problem gambling among sports bettors.

**Решение:** =

---

### 612 · R3233

**2.8 Play-in-Play**

2022 · Unbridled · book-chapter · https://doi.org/10.7208/chicago/9780226816890.003.0019

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: Book subsection on in-play betting with no abstract; probably descriptive, but whether it reports problem-gambling data can't be ruled out.); Sonnet -6 (не про азартные игры или «ставка/лотерея» в другом смысле: Book chapter "Play-in-Play" in "Unbridled", no abstract; title suggests a play/theatre concept, not sports betting or problem gambling measurement.)

**Решение:** -

---

### 613 · R3234

**Based on UTAUT Model: Multi-factor Analysis of Internet Sports Lottery Consumption Behavior**

2022 · Health Science and Management · article, journalarticle, journal-article · en · https://doi.org/10.62091/hsm2022002

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; a UTAUT survey of internet sports lottery consumers probably didn't measure problem gambling, but the full text should be checked.

**Решение:** =

---

### 614 · R3235

**DAILY FANTASY SPORTS**

2022 · Princeton University Press eBooks · part of book or chapter of book, book-chapter · en · https://doi.org/10.2307/j.ctv1t8q8wq.65

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Book chapter on daily fantasy sports with no abstract; probably not empirical, but the title alone can't rule it out.

**Решение:** =

---

### 615 · R3236

**E-Sports, Gambling, Match-Fixing, and Performance Enhancement**

2022 · other · en · https://doi.org/10.5040/9781666990331.ch-8

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -1 (обзор, комментарий, теоретическая, правовая или регуляторная работа: No abstract; the title points to an overview chapter on esports integrity (gambling, match-fixing, doping), not a survey of bettors.); Sonnet ? (нет аннотации: No abstract; title suggests esports, gambling, match-fixing overview, possibly a commentary or chapter, but could include survey data on esports betting.)

**Решение:** ?

---

### 616 · R3238

**O-005 - ANÁLISIS DE LAS CONDUCTAS ASOCIADAS A JUEGO DE APUESTAS EN UNIVERSITARIOS**

2022 · ABSTRACT BOOK 2022 · article, conference-paper · es · https://doi.org/10.17579/abstractbooksepd2022.o005

El juego se ha convertido en una forma habitual de entretenimiento para muchos jóvenes. El objetivo de este estudio fue describir el comportamiento de juego que están desarrollando los estudiantes universitarios en Aragón, España. Se aplicó un diseño transversal, recogiendo datos sobre exposición publicitaria, hábitos y experiencias de juego y opiniones sobre el impacto y regulación del juego de 516 estudiantes universitarios de la Universidad de Zaragoza. La encuesta online incluyó preguntas ad-hoc y el "Cuestionario breve de juego patológico". Casi la mitad de la muestra había apostado dinero al menos una vez en la vida (48,1%) y el 2,4% presentaba un posible diagnóstico de juego patológico. Las apuestas deportivas (38,8%) y las tiendas de apuestas (31%) fueron las opciones más utilizadas para el juego, y los que estudiaron ciencias del deporte presentaron una mayor prevalencia de juego patológico y tenían más probabilidades de apostar. El juego es percibido como una actividad de ocio normal por muchos estudiantes universitarios. Es necesario desarrollar estrategias transversales para concienciar sobre los peligros potenciales del juego.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Survey of university students that measured sports betting (38.8%) and pathological gambling with the Brief Pathological Gambling Questionnaire (CBJP).

**Решение:** =

---

### 617 · R3239

**SPORTS BETTING:**

2022 · Rutgers University Press eBooks · part of book or chapter of book, book-chapter · en · https://doi.org/10.2307/j.ctv2v55k3g.15

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Book chapter on sports betting with no abstract; probably not empirical, but the title alone can't rule out survey data.

**Решение:** =

---

### 618 · R3243

**WHAT'S THE LINE? THE INFLUENCE OF NUMERICAL LITERACY ON THE PERCEPTIONS AND EVALUATIONS OF SPORT ODDS**

2022 · Temple University. Libraries · collection/text, other literature type · en · https://doi.org/10.34944/dspace/7693

In 2018, the United States Supreme Court overturned PASPA, a law which had previously deemed sports betting illegal. Following this ruling, states have already or have begun passing legislation which legalizes sport betting. As legalization continues to sweep the nation, an untapped domain of research has emerged. From a sport management perspective, there is a new, highly lucrative sport industry with which there is minimal research. The main purpose of this research project is to examine how bet presentation influences consumer behavior related to sports gambling. Specifically, the role that bet format presentation has on consumers’ willingness to bet and the amount they are willing to bet. Additionally, the potentially mediating effects of numeracy and team identification were examined. Participants (N=703) were recruited from the United States, United Kingdom, and Australia, as these locations natively use different forms of bet presentation (American, fractional, and decimal). This study utilized a Latin square experimental design that examined whether participants were willing to bet more money when shown American odds first compared to fractional odds first. Further, evidence was provided demonstrating the positive mediating influence of team identification, and the influence of subjective numeracy. Practically, the results from this study can inform sports betting organizations, sports betting consumers, as well as government and industry regulators. Theoretically, knowledge is contributed to the domains of sport management, behavioral pricing, and appraisal theory literature.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Experimental thesis on sports odds presentation (N=703); the abstract mentions no problem-gambling instrument, but a thesis might include one.

**Решение:** =

---

### 619 · R3244

**WHO’S BETTING ON SPORTS? THREE ESSAYS ON UNDERSTANDING SPORTS BETTING MOTIVATION AND ITS INFLUENCE ON BETTING INTENTION AND BEHAVIOR**

2022 · Temple University. Libraries · collection/text, other literature type · en · https://doi.org/10.34944/dspace/7702

Since the U.S. Supreme Court lifted the federal ban on sports gambling, the popularity of sports gambling continues to increase. This has left the sport industry, including academics, interested in examining the drivers of sports gambling participation and their influence on consumers’ betting behavior. This dissertation includes three essays considering motivations to engage in sports gambling. While all focus on sports gambling, each of these three standalone essays embrace a different focus to explore sports gambling motivations and betting behavior. First, Essay One explores the differences in motivation and perception of skill versus luck between daily fantasy sports (DFS) and sports betting participants. Next, Essay Two investigates the interplay between motivations and game characteristics on betting intentions. Finally, Essay Three explores the effects of different marketing promotions and their fit with consumers’ regulatory focus on consumers’ betting behavior. Collectively, this research will provide insights and understandings of different drivers of sports gambling and their influence on consumer behavior regarding sports gambling.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Dissertation surveying sports bettors and DFS players on motivations and intentions; unclear whether a problem-gambling instrument was used.

**Решение:** =

---

### 620 · R3251

**Gamers Who Gamble**

2022 · Journal of Emerging Sport Studies · article, review, journal-article · en · https://doi.org/10.26522/jess.v3i.3710

During recent years, while electronic sports (esports) has increasingly become a positive mainstream cultural phenomenon, it also may have several socio-economic implications, such as the growth of esports betting. Much like betting in sport, betting on esports has become a prominent form of gambling. However, there is still a paucity of knowledge on the demographic characteristics of this gambling cohort, particularly in regard to its relationship to video game play and spectatorship. In the present study, past-year video gamers (N = 1368) completed an online survey. Survey questions inquired about their esports event spectating, video game play, and esports betting behaviours, as well as general demographic questions. Video gamers who bet on esports were a distinct cohort from their counterparts: younger, more likely to be male, lower frequency of video game play, higher frequency of esports spectatorship, and more likely to watch esports in a social setting (e.g., with others). By providing a background on gamers’ behaviours this work contributes to the growing body of research into the dynamic profile of esports play, spectatorship, and gambling. Findings are reflective of the growing interrelation of gambling and gaming behaviours, a subject garnering increasing attention from governments, regulatory agencies, public health specialists and clinicians, and the related industries themselves.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of video gamers including esports bettors; abstract does not say whether a problem-gambling instrument was used.

**Решение:** =

---

### 621 · R3255

**Problematic Gambling and Associated Factors Among Sports Bettors in Jimma Town Betting Centers, South West Ethiopia**

2022 · Research Square · article, other literature type, preprint · en · https://doi.org/10.21203/rs.3.rs-1960760/v1

Abstract Background: problematic gambling is a silent epidemic that is ruining the mental health of many individuals with far-reaching consequences on mental health, economical and overall wellbeing. It is now an issue of growing concern in developing countries. Over the last three years, sports betting has expanded rapidly in Ethiopia. However, there is a scarcity of studies conducted on problematic gambling among sports bettors in Ethiopia. So, the aim of this study was to assess problematic gambling and its associated factors among sports bettors in Jimma town betting center, Ethiopia,2021 Methods: A quantitative cross-sectional survey was conducted among 422 sports bettors. A consecutive sampling technique was employed to select study participants. Problematic gambling was assessed by South Oaks Gambling Screening tool. Data were collected using pre-tested interviewer-administered structured questionnaires. The collected data were coded and entered into EPI data Version 4.6 and exported to SPSS Version 26.0 for analysis. Descriptive statistics, bivariate and multivariate logistic regression analyses were done. Statistical significance of association was declared at P-values less than 0.05 with 95%CI in the final model. Result: A total of 414 participants were involved in the study with a response rate of 98.1%. The overall prevalence of problematic gambling among the study participants was 53.9%.Age between (25-31) years (AOR=4.89(1.42-16.87)),unemployed(AOR=3.56(1.99-6.41)),current alcohol use (AOR =3.89,95%CI (2.25-6.72)), positive attitude towards sports betting(AOR =2.57,95%CI (1.49-4.44)), easily availability of betting center (AOR= 2.23,95%CI (1.23-4.00)), accessibility of internet service (AOR=4.51,95%CI (1.84-11.06)), media advertising such as DSTV (AOR= 3.15,95%CI (1.78-5.56)) and Facebook/telegram use (AOR= 3.59,95%CI (1.46-8.83)) were significantly associated with problematic gambling. Conclusion: The finding of this study showed that the prevalence of problematic gambling among sports bettors was high. Age between (25-31) years old, unemployment, current alcohol use, positive attitude towards sports betting, easily availability of betting center, accessibility of internet service, media advertising such as Dstv and social media like Facebook/telegram were associated with problematic gambling. Problematic gambling is a public health issue that requires great emphasis. Concerted actions from governmental and non-governmental organization are needed to mitigate the problem.

**ИИ:** + · обе модели · беттеры + инструмент · Cross-sectional survey of 414 sports bettors in Ethiopia using SOGS; reports problem gambling prevalence of 53.9%.

**Решение:** =

---

### 622 · R3259

**Prevalence of and Factors Associated with Disordered Gambling Disorder, and Use of DSM-5 Based Sports Betting Questionnaire, in a Southwest Nigerian Community.**

2022 · Indian journal of psychological medicine · article, journal article, journalarticle · eng · https://doi.org/10.1177/02537176211023809

Background: Gambling disorder is rarely diagnosed in Nigeria. The prevalence and factors associated with gambling disorder in many parts of Nigeria are not known. Our study aimed to evaluate psychometric properties of the Diagnostic and Statistical Manual (DSM)-5 for use as a self-report screening instrument for large-scale studies in Nigeria. Methods: Cross-sectional surveys were done involving two independent sampled populations from a hospital setting and the surrounding community. Instruments administered included a semistructured sociodemographic questionnaire, South Oaks Gambling Screen (SOGS), International Classification of Diseases (ICD) 11 criteria, and a screening questionnaire based on Diagnostic Statistical Manual (DSM-5), which was designed as a self-report measure (Sports betting). Results: The prevalence rate for gambling disorder was 30.5%. The diagnostic accuracy of DSM-5 and ICD-11, and SOGS were comparably similar. Factors associated with gambling disorder (sports betting) were low educational level and poor employment status. Conclusion: The DSM-5-based screening questionnaire showed good psychometric properties, with sensitivity and specificity comparable to that of ICD-11 criteria and SOGS. The study also found a high prevalence of gambling disorder. There is a need to address educational and employment opportunities.

**ИИ:** + · обе модели · валидация инструмента · Nigerian community and hospital survey validating a DSM-5 sports betting screen against SOGS and ICD-11; reports gambling disorder prevalence among sports bettors.

**Решение:** =

---

### 623 · R3273

**Gaming, substance use and distress within a cohort of online gamblers.**

2022 · Journal of public health research · article, journal article, journalarticle · eng · https://doi.org/10.4081/jphr.2021.3434

Background: The fifth edition of the Diagnostic and Statistical Manual of Mental Disorders (DSM-5) included Internet Gaming Disorder (IGD) as a tentative diagnosis and inquires for additional research. The research on gaming is inconsistent regarding measurement approach and diagnostic cut-offs. Some scholars suggest the core approach, accentuating some of the diagnostic criteria to avoid pathologizing harmless behaviour. Also, the co-occurrence of gaming and other addictions, gambling in specifically, is frequently reported but poorly understood. The present study aimed to explore gaming within a population of online gamblers in order to evaluate the core approach but also to investigate the possible co-occurrence of different addictions. Design and methods: The present study is derived from material collected for a study on online gambling. The study addressed 1007 adult individuals from the general population who had gambled for money on an online casino site or an online betting site, on at least 10 occasions during the past 12 months. Results: Both the level of distress and problem gambling increased as the severity of gaming increased. The co-occurrence of problems with alcohol, illicit drug use/prescription sedatives/strong painkillers and gambling was roughly 50% among the addictive gamers. Conclusion: The present study suggests that the core approach manages to distinguish in severity of gaming in regards to interference and comorbidity. We also brought light to the occurrence of gaming within a population of gamblers and our results indicate that this specific group of addicted gamers are particularly burdened by co-occurrent addictive behaviours and severe distress. Significance for public health Internet gaming is a highly common recreational behaviour, mainly without negative consequences. However, most research agree on a pathological potential in gaming and the fifth edition of the DSM-5 included Internet Gaming Disorder as a tentative diagnosis and inquires for additional research. The research on gaming is inconsistent regarding measurement approach and diagnostic cut-offs. Some scholars suggest the “core approach”, which accentuates some of the diagnostic criteria in order to capture and differentiate truly pathological from harmless gaming behaviour. This study evaluates the core approach and explore gaming within a population of gamblers. The attention and interest of problems related to gaming and gambling in media, institutions such as schools, social services and other health institutions are huge. Despite this little is known about the co-occurrence of gaming and other addictions, gambling in specifically. Our findings are clinically relevant in screening and treatment of both problem gamers and problem gamblers.

**ИИ:** разошлись — Opus + (игроки, есть ставки на спорт и инструмент: Survey of 1007 online casino/betting-site gamblers that measured problem gambling; could report problem gambling among online sports bettors.); Sonnet ? (неясно, есть ли ставки на спорт: Survey of 1007 online casino/betting gamblers from the general population, with problem gambling measured. The abstract doesn't say whether sports betting was separated out.)

**Решение:** ?

---

### 624 · R3279

**Moderating Effect of Impulsivity on the Association Between Entrapment and Problem Gambling.**

2022 · Journal of gambling studies · journal article, journalarticle, article · eng · https://doi.org/10.1007/s10899-021-10047-w

Impulsivity as measure by delay discounting and entrapment have been known to influence gambling, but their individual and joint influence on problem gambling among Soccer gamblers are not yet understood. We examine the direct and moderation influences of entrapment and delay discounting on problem gambling among 174 Soccer gamblers in Nigeria. Data were obtained by means of self-report questionnaires of entrapment, delay discounting and problem gambling. Results from Hayes PROCESS moderated regression showed that delay discounting moderated the association between entrapment and problem gambling such that the association between entrapment and problem gambling was strong when delay discounting was high and diminished when delay discounting was low. Our findings provide insight into the conditional effect of delay discounting on the entrapment-problem gambling association.

**ИИ:** + · обе модели · беттеры + инструмент · Survey of 174 soccer bettors in Nigeria with a self-report problem-gambling questionnaire; full text should name the instrument.

**Решение:** =

---

### 625 · R3290

**Stimulation of the dorsolateral prefrontal cortex modulates brain cue reactivity to reward (un)availability**

2022 · PsyArXiv · preprint · und · https://doi.org/10.31234/osf.io/tb2dj

Brain imaging studies have shown that stimulation of the left dorsolateral prefrontal cortex (dlPFC), which plays a pivotal role in high-order cognitive control processes, modulates brain reactivity to reward-related cues. Nevertheless, the impact of contextual factors such as reward availability (the reward that is depicted in the cue exposure task) on such modulation effect remains unclear. Here we tested whether a single session of high-frequency repetitive transcranial magnetic stimulation (HF-rTMS) over the left dlPFC differently impacts brain reactivity to cues signalling either availability or unavailability of a sports betting opportunity. Employing a within-subject design (verum versus sham HF-rTMS) among thirty-two frequent sports bettors, we first observed that, as compared to the sham condition, verum HF-rTMS modulated brain reactivity to game cues prior to being made (un)available for betting, through simultaneous increases (posterior insula and caudate nucleus) and decreases (occipital pole) in brain activation. Second, verum HF-rTMS led to increased ventral striatal activity towards cues available for betting but did not modulate brain response to cues unavailable for betting. Third, exploratory functional connectivity analyses revealed increased negative coupling in the verum condition between the left dlPFC and the right and left superior frontal gyrus toward available and non-available betting cues, respectively. Taken together, these findings demonstrate that transient stimulation of the left dlPFC led to a general modulation in brain activity and functional connectivity in responses to cues, and that this effect is only partly dependent on cues signalling for reward (un)availability.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · rTMS/fMRI study of 32 frequent sports bettors, not chosen for gambling problems; the sample description may report PGSI but the abstract doesn't say.

**Решение:** =

---

### 626 · R3293

**Benchmarking gambling screens to health-state utility: the PGSI and the SGHS estimate similar levels of population gambling-harm**

2022 · BMC Public Health · article · en · https://doi.org/10.1186/s12889-022-13243-4

BACKGROUND: Both the Problem Gambling Severity Index (PGSI) and the Short Gambling Harms Screen (SGHS) purport to identify individuals harmed by gambling. However, there is dispute as to how much individuals are harmed, conditional on their scores from these instruments. We used an experienced utility framework to estimate the magnitude of implied impacts on health and wellbeing. METHODS: We measured health utility using the Short Form Six-Dimension (SF-6D), and used this as a benchmark. All 2603 cases were propensity score weighted, to balance the affected group (i.e., SGHS 1+ or PGSI 1+ vs 0) with a reference group of gamblers with respect to risk factors for gambling harm. Weighted regression models estimated decrements to health utility scores attributable to gambling, whilst controlling for key comorbidities. RESULTS: We found significant attributable decrements to health utility for all non-zero SGHS scores, as well as moderate-risk and problem gamblers, but not for PGSI low-risk gamblers. Applying these coefficients to population data, we find a similar total burden for both instruments, although the SGHS more specifically identified the subpopulation of harmed individuals. For both screens, outcomes on the SF-6D implies that about two-thirds of the 'burden of harm' is attributable to gamblers outside of the most severe categories. CONCLUSIONS: Gambling screens have hitherto provided nominal category membership, it has been unclear whether moderate or 'at-risk' scores imply meaningful impact, and accordingly, population surveys have typically focused on problem gambling prevalence. These results quantify the health utility decrement for each category, allowing for tracking of the aggregate population impact based on all affected gamblers.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Survey of 2603 gamblers using PGSI; abstract doesn't say if sports betting participation was measured, though gambling activities likely were.

**Решение:** =

---

### 627 · R3294

**Adolescent gambling behavior: a gender oriented prevention strategy is required?**

2022 · The Italian Journal of Pediatrics/Italian journal of pediatrics · article · en · https://doi.org/10.1186/s13052-022-01309-3

BACKGROUND: Studies published on gender-related differences in the gambling behavior of adolescents have focused mainly on psychological and social factors. The aim of this study was to develop separate risk factor models for male and female adolescents, considering the environmental, psychological, behavioral and socio-economic factors related to their gambling. METHODS: A survey was conducted through a questionnaire developed on a dedicated web site in 2014 on a representative sample of the Italian 15-19-years-old population, including 34,922 students attending 438 secondary schools. The SOGS-RA questionnaire was used to measure gambling behavior. To verify the risk factors associated with gambling a logistic regression stratified by gender was performed. RESULTS: In our representative sample of Italian adolescents nationwide, the prevalence of each level of gambling was higher in males than in females. The logistic regression stratified by gender found that for both genders, gambling was positively associated with internet surfing, playing sports, getting into a fight, having unprotected sex, pulling stunts, drinking alcohol at least once in the previous month, having not a satisfactory relationship with teachers, receiving pocket money from parents, spending each week much money and having someone in the family (father, sister/brother, other relatives) who gambles. On the other hand, having poor or average school marks, going to ED in the previous year, smoking at least once in the previous month, having dissatisfied with relationships with father and having a lower family income than their friends was only associated with gambling in boys. Having an accident or injury in the previous year and having a mother who gambled was associated only in girls with higher odd of at risk or problem gambling behavior. A low psychological distress is protective only in girls for risk of gambling. CONCLUSIONS: Understanding the gender-related differences, and how they emerge in younger people at the start of their gambling careers, can suggest how best to educate individuals, families and the community on the topic of gambling. Programs to prevent substance use and abuse should be multifaceted, and include efforts to prevent gambling with a gender perspective approach.

**ИИ:** + · обе модели · опрос населения об азартных играх · Nationally representative Italian adolescent survey (n=34,922) using SOGS-RA; activity data, likely including sports betting, probably in full text.

**Решение:** =

---

### 628 · R3297

**Glücksspiel-Survey Deutschland: Teilnahme- und Problemprävalenzen**

2022 · Suchttherapie · article · de · https://doi.org/10.1055/s-0042-1755995

Einleitung Glücksspiele sind für die meisten Menschen ein harmloses Freizeitvergnügen. Bei manchen Personen entwickeln sich jedoch mit der Zeit glücksspielbezogene Probleme, bis hin zur Sucht. Gleichzeitig handelt es sich bei dem Spielen um Geld um ein milliardenschweres Business. Entsprechend kontrovers wird in der Fachöffentlichkeit über die Wirksamkeit und Angemessenheit von Maßnahmen des Jugend- und Spielerschutzes diskutiert. Für diese Diskussion eine empirische Grundlage zu schaffen, ist ein wesentliches Ziel des Glücksspielsurveys 2021. Material und Methodik Die Datenerhebung erfolgte in Form eines Mixed-Mode-Design (CATI: Festnetz- und Mobiltelefonnutzer*innen & CAWI: Online-Access-Panelist*innen). Zwischen dem 03.08.2021 und dem 16.10.2021 sind insgesamt 12.303 Personen zwischen 16 und 70 Jahren befragt worden (CATI: 7.501; CAWI: 4.802). Die Gewichtung erfolgte nach soziodemografischen Merkmalen (Alter, Geschlecht, Schulabschluss) sowie der Erhebungsart (2/3 telefonisch; 1/3 online). Glücksspielbezogene Probleme der erwachsenen Bevölkerung (18-70 Jahre) wurden auf Basis des DSM-5 erhoben. Ergebnisse 29,7% der Bevölkerung haben in den letzten 12 Monaten mindestens ein Glücksspiel um Geld gespielt (Männer: 34,7%; Frauen: 24,5%). Jede fünfte Person nahm in den letzten 12 Monaten zumindest einmal am Zahlenlotto teil (19,3%; Eurojackpot: 10,7%). Insgesamt 6,8% spielten riskante Glücksspielformen (Automatenspiel, Kasinospiele, Sportwetten). 2,3% der 18- bis 70-Jährigen sind – bezogen auf die zurückliegenden 12 Monate – von einer „Störung durch Glücksspielen“ (DSM-5) betroffen (leichte Störung 1,1%, mittelschwere Störung: 0,7% schwere Störung: 0,5%). Bei 5,7% der Befragten ist zudem von einem riskanten Spielverhalten (1-3 erfüllte DSM-5-Kriterien) auszugehen. Die höchsten Anteilswerte einer glücksspielbezogenen Störung finden sich unter den Spieler*innen an Geldspielautomaten (33,4%), gefolgt von Spieler*innen an Glücksspielautomaten in Spielbanken (31,5%) und den Live-Sportwetter*innen (29,7%). Deutlich geringer sind die zugehörigen Prävalenzwerte bei den klassischen Lotterien. Zusammenfassung Die Ergebnisse des Glücksspielsurveys 2021 verweisen auf das unterschiedliche Gefährdungspotential der einzelnen Glücksspielformen. Bei der Gestaltung und Etablierung von Spieler- und Jugendschutzmaßnahmen sollte dies dahingehend Berücksichtigung finden, dass Präventionskonzepte für die riskanten Glücksspiele eher restriktiv gestaltet und verhältnispräventiv ausgerichtet werden. Publication History Article published online: 30 August 2022 © 2022. Thieme. All rights reserved. Georg Thieme Verlag Rüdigerstraße 14, 70469 Stuttgart, Germany

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · German national survey using DSM-5; reports gambling disorder prevalence by activity, including live sports bettors (29.7%).

**Решение:** =

---

### 629 · R3301

**O preço do jogo : o papel de variáveis individuais e contextuais no envolvimento em apostas desportivas em adolescentes portugueses**

2022 · master thesis · por · https://hdl.handle.net/10400.14/38407

As apostas desportivas demonstraram ser uma das modalidades de jogo mais praticada por adolescentes, verificando-se cada vez mais uma maior incidência e subsequente risco para o desenvolvimento de Perturbação de Jogo Patológico. O presente estudo teve como objetivo geral caracterizar o envolvimento nas apostas desportivas em adolescentes portugueses e analisar o papel de diferentes variáveis individuais (género, crenças erróneas e impulsividade) e contextuais (família e grupo de pares) neste comportamento. A amostra integrou adolescentes do décimo ano de escolaridade (N = 224), de onze escolas na área metropolitana do Porto (Maia, Gondomar e Porto). Os resultados apontam para um maior envolvimento dos participantes do género masculino em apostas desportivas. O envolvimento em apostas desportivas da família e dos pares também tem implicações no comportamento em apostas desportivas nos adolescentes. Foi encontrado que quando os participantes se envolvem em apostas desportivas, tendem a envolverem-se também em outras modalidades de jogo a dinheiro e, que, quando os participantes se encontram envolvidos em apostas desportivas apresentam maiores níveis de crenças erróneas, ao contrário de impulsividade. Estes resultados salientam a necessidade de investimento em futuras investigações, e de integrar programas de promoção de literacia, junto das famílias, e programas de prevenção junto dos adolescentes. Sports betting has proved to be one of the most practiced ways of gambling by adolescents, with an increasing incidence and subsequent risk for the development of Pathological Gambling Disorder. The broad objective was to characterize the involvement in sports betting in Portuguese adolescents and to analyze the role of different individual variables (gender, erroneous beliefs and impulsivity) and contextual variables (family and peer group). The sample included adolescents from the tenth year of schooling (n = 224), from eleven schools in the metropolitan area of Porto (Maia, Gondomar and Porto). The results point to a greater involvement of male participants in sports betting. The results indicate a greater involvement of male participants in sports betting. Family and peer involvement in sports betting also has implications for sports betting behavior in adolescents. It was found that when participants are involved in sports betting, they tend to also be involved in other types of gambling and, that when participants are involved in sports betting they have higher levels of erroneous beliefs, as opposed to impulsiveness. These results highlight the need to invest in future research, and to integrate literacy promotion programs, with families, and prevention programs with adolescents.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of Portuguese adolescents on sports betting; abstract mentions erroneous beliefs and impulsivity but not whether a problem-gambling screen was used.

**Решение:** =

---

### 630 · R3314

**Gambling and Gaming in the United Kingdom during the COVID-19 Lockdown**

2022 · COVID · article, review · en · https://doi.org/10.3390/covid2020007

During the first UK national COVID-19 lockdown, there were fears that increased online gaming and gambling could negatively impact wellbeing. Using a cross-sectional retrospective change survey of 631 UK adult gamers and/or gamblers during the week the UK lockdown was partially lifted (June 2020), we investigated participation in gaming/gambling and relationships with problem gaming, problem gambling and wellbeing (using the following previously validated scales: the Internet Gaming Disorder Short Form; a short-form version of the Problem Gambling Severity Index; a short-form of the Warwick–Edinburgh Mental Well-Being Scale). Results indicated a near-doubling in gaming activity during lockdown and significant increases in problem gaming scores, but not in numbers of disordered gamers. Aggregate changes to gambling participation and problem gambling were negligible: decreases in offline and sports gambling were balanced by increases in online gambling. Wellbeing scores decreased during lockdown across the sample, particularly amongst women, and path analysis revealed moderate correlations between increases in problem gaming and gambling scores and reductions in wellbeing. We conclude that for some, maladaptive gaming/gambling coping strategies during the lockdown may have exacerbated its negative effects.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Survey of UK gamers/gamblers measured sports gambling participation and PGSI short form; could report problem gambling among sports bettors.

**Решение:** =

---

### 631 · R3319

**Part of the Game? Exploring the Prevalence and Normalization of Gambling in Belgian Sports Clubs.**

2022 · International journal of environmental research and public health · article, journal article, journalarticle · eng · https://doi.org/10.3390/ijerph19116527

Gambling and sports are entangled in a close relationship. However, little remains known about gambling behaviors and perceptions in sports. Drawing on normalization theory, this study explores the prevalence and predictors of problem gambling as well as the normalization of gambling (including its availability and accessibility, prevalence, and socio-cultural accommodation) in sports clubs. A cross-sectional study design was implemented, based on an online survey completed by 817 Belgian sports club actors. This survey consisted of the Problem Gambling Severity Index (PGSI) and questions about personal and socio-cultural factors regarding gambling. Data were analyzed with SPSS 26 software, using descriptive statistics and an ordinal logistic regression analysis. These analyses exposed being male, being aged 26-35 years old, and being involved in football (soccer) as factors that might be linked with higher levels of problem gambling in sports. Furthermore, sports betting is especially shown to be normalized in sports clubs given its prevalence, and its frequently organized and discussed character. Moreover, respondents disclosed a lack of formal rules (96%) and education initiatives (98.7%) on gambling in their sports club. Given the indicated support for gambling regulations and educational measures, this study may inform sports organizations about how to help denormalize gambling.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Survey of 817 people involved in Belgian sports clubs; it used the PGSI and measured how common sports betting is.

**Решение:** =

---

### 632 · R3321

**Predictors of Problem Gambling for Sports and Non-sports Gamblers: A Stochastic Search Variable Selection Analysis.**

2022 · Journal of gambling studies · article, other literature type, journal article · eng · https://doi.org/10.1007/s10899-021-10025-2

Differences in the psychological characteristics and gambling behaviors of sports bettors and non-sports bettors were examined with a view to identifying predictors of problem gambling severity. A survey was completed by 1,280 participants, 596 of whom had placed bets on a sporting event in the last year. We found that sports bettors are at greater risk of problem gambling due to differences in attitudes towards gambling, personality traits, thinking styles, erroneous cognitions, and gambling motivations. Moreover, our findings suggest that the difference between individuals who bet on sports and those who do not is more quantitative than qualitative. A stratified stochastic search variable selection analysis by type of bettor revealed similar important predictors of problem gambling for both sports bettors and non-sports bettors; however, the association between the predictors and problem gambling was stronger for sports bettors. Overall, the findings of this study suggest that preventative methods and interventions for problem gambling should be targeted as a function of whether individuals bet on sports.

**ИИ:** + · обе модели · беттеры + инструмент · Survey of 1,280 gamblers, 596 of them sports bettors, that measured problem gambling severity; prevalence among sports bettors can likely be reported.

**Решение:** =

---

### 633 · R3332

**Online Gambling in Iranian Social Media Users: Prevalence, Related Variables and Psychiatric Correlations.**

2022 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-021-10020-7

The exponential increase in Internet use has been associated with dangers and harms. Recently, the prevalence of online gambling is increasing in various countries. Online gambling can be a prelude to gambling disorder. No study has been conducted in this field in Iran yet. The aim of this study was to investigate the prevalence of online gambling (without disorder and pathological), and its relationship with demographic variables and psychiatric symptoms. 3252 people participated in this study online. Research tools included gambling disorder screening questionnaire-Persian (GDSQ-P), brief symptom inventory (BSI), Young's addiction questionnaire, and Demographic questionnaire. The prevalence of online gambling was 8.9%. 26.6% of online gamblers experience moderate to severe degrees of pathological gambling. 74.7% of online gamblers were male. Online gamblers have a lower mean age than non-online gamblers (p 0.05). In BSI-assessed psychiatric symptoms, online gamblers showed higher scores on anxiety and obsession, and lower scores on paranoid ideation, compared to the control group (p < 0.05). Also, Internet addiction and daily use of the Internet as entertainment were significantly higher in online gamblers than non-online gamblers (p < 0.05). Also, a positive and significant correlation was found between the severity of gambling and the severity of Internet addiction, severity of depression, severity of anxiety, and severity of obsession in online gamblers (p < 0.05). Overall, online gambling is common in Iran and is associated with psychiatric problems. Health professionals and the government should pay special attention to online gambling and its related problems.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Survey of online gamblers using a gambling disorder screen (GDSQ-P); the full text may report sports betting as an online activity.

**Решение:** =

---

### 634 · R3335

**Relating Compulsivity and Impulsivity With Severity of Behavioral Addictions: A Dynamic Interpretation of Large-Scale Cross-Sectional Findings**

2022 · Frontiers in Psychiatry · article · en · https://doi.org/10.3389/fpsyt.2022.831992

Background and Aim Impulsivity and compulsivity are two key temperament traits involved in behavior regulation. The aim of this study was to test several existing theories in explaining the role of impulsivity and compulsivity in symptom severity in various behavioral addictions. Methods Data were collected from a (representative) general population sample (N = 2,710, mean age:39.8 years (SD:13.6), 51% woman), and from people who are at increased risk of having a behavioral addiction (N = 9,528 in total, mean age: 28.11 (SD:8.3), 34.3% woman), including people with problematic gaming and internet use, pathological gambling, exercise dependence, compulsive buying and work addiction. Symptom severity, reward driven impulsivity and relief driven compulsivity were assessed. Results For non-problematic groups, impulsivity is present to about the same extent as compulsivity, whereas for problematic groups, compulsivity dominates over impulsivity in all groups (except for gambling). The strength of the correlation between impulsivity and compulsivity is higher in more severe forms of the disorders (from r = 0.18 to r = 0.59 in the representative population). Discussion Based on these data, it appears that relief-driven behavior (negative reinforcement) dominates over reward-driven behavior (positive reinforcement) in more severe cases of a behavioral addiction. Conclusion This is the first large-scale study to find empirical support for the neuroscientific theory on the dominance of compulsivity (“needing”) over impulsivity (“wanting”) in more severe cases of a behavioral addiction. Although longitudinal research is needed, a possible shift from impulsivity to compulsivity takes place, similar to substance use addictions, which maintains the circle of addiction.

**ИИ:** разошлись — Opus ? (неясно, есть ли ставки на спорт: General population and at-risk samples with gambling symptom severity measured; unclear whether sports betting participation was recorded.); Sonnet -7 (другое — напишите почему: Impulsivity/compulsivity correlations across behavioral addictions; no sign of sports betting measurement, and the at-risk samples were recruited for addiction problems.)

**Решение:** ?

---

### 635 · R3349

**Influence of Online Sports Events on Betting among Nigerian Youth**

2022 · review

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; title suggests possible survey of Nigerian youth sports betting, though it is tagged as a review and PG measurement is unknown.

**Решение:** =

---

### 636 · R3352

**The Identification of Low-risk Gambling Limits for Specific Gambling Activities.**

2022 · Journal of gambling studies · journal article · eng · https://doi.org/10.1007/s10899-021-10036-z

An emerging literature has identified optimal low-risk gambling limits in an effort to reduce gambling-related harm. Concerns have, however, been raised about the construction of aggregate low-risk limits that are applied to all gambling activities and there is support from gambling experts and the general public in Australia for the identification of low-risk limits for specific gambling activities. The study's aim was to identify and evaluate a set of empirically-based activity-specific limits (gambling frequency, gambling expenditure, gambling expenditure as a proportion of gross personal income, session expenditure, session duration) in a secondary analysis of Social and Economic Impact Studies of Gambling in Tasmania and the 2014 Survey on Gambling, Health and Wellbeing in the ACT. Balancing sensitivity and specificity, limits were identified for all gambling activities: EGMs (10 times per year, AUD$300/year, 0.63-1.04% of personal income, AUD$35 per session, 40 min/session), horse/dog racing (0.55% of personal income), instant scratch tickets (AUD$45/year), lotteries (0.45% of personal income), keno (4-13 times/year, AUD$45-$160/year), casino table games (AUD$345/year, 0.36-0.76% of personal income), bingo (AUD$150/year, 0.49% of personal income, AUD$17/session, 90 min/session), and sports/other event betting (14 times/year, AUD$400/year, 0.55-0.86% of personal income). These limits were exceeded by one-quarter to one-half of gamblers on these specific activities and were generally good predictors of gambling-related harm in subgroups of gamblers participating in these gambling activities and in the overall gambling sample. The limits provide gamblers, regulators, prevention workers, and researchers with simple rules of thumb in prevention efforts to reduce gambling-related harm in specific contexts.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Secondary analysis of Tasmania and ACT population surveys with a sports/event betting subgroup; gambling harm probably measured with PGSI.

**Решение:** =

---

### 637 · R3358

**Con cabeza fría y con toda la esperanza: construcción de subjetividades en el capitalismo contemporáneo en las apuestas deportivas en línea**

2022 · other literature type · und · https://doi.org/10.57784/1992/58663

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: No abstract; sociological study of online sports betting subjectivities, probably qualitative, but the methods can't be confirmed from the title alone.); Sonnet -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: Title indicates a sociological or qualitative study of subjectivities in online sports betting. No abstract, and no sign of a problem-gambling instrument or survey.)

**Решение:** ?

---

### 638 · R3365

**Intraindividual Variability in Internet Sports Gambling**

2022 · OSF Preprints (OSF Preprints) · preprint

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; internet sports gambling study, possibly operator account data, unclear whether a problem-gambling instrument was used.

**Решение:** =

---

### 639 · R3368

**Gambling disorder risk factors in a population of online sports betting players in Sfax**

2022 · European psychiatry : the journal of the Association of European Psychiatrists · abstract, article, journal-article · eng · https://doi.org/10.1192/j.eurpsy.2022.2127

Introduction Online sports betting (OSB) is frequently associated with gambling disorder (GD). In Tunisia, no study on this has been done so far. Objectives To detect GD in a population of Tunisian OSB players, and to identify its risk factors. Methods This was a cross-sectional study of 58 male OSB players in the city of Sfax. The GD was assessed by a questionnaire relating to the DSM-V criteria. Depression, anxiety and stress were assessed using the DASS scale, gambling motivations using the GMQ-F scale, and impulsivity using the UPPS-P scale. Results The mean age was 37.4 ± 8.29 years. The prevalence of JAP was 53.4%. On univariate analysis, the factors associated with GD were university level of education, the practice of other gambling, daily gambling, gambling spending &gt; 300 Dinars / month , gambling duration &gt; 3 years, the frequency of winning &gt;1 win /6months , the occurrence of a Big Win, total GMQ-F score, coping motivation , and financial motivation. In the multivariate study, GD risk factors were gambling spending &gt; 300 Dinars / month (p = 0.011; ORa = 223.16), financial motivation (p = 0.022; ORa = 3.967), pathological stress (p = 0.036; ORa = 224.388) and inversely associated with the age at onset of gambling (p = 0.026; ORa = 0.751) and the UPPS score (p = 0.011; ORa = 0.6). Conclusions Our results push us to deepen our knowledge and our studies concerning this problem in our country and to reflect on the management and prevention measures. Disclosure No significant relationships.

**ИИ:** + · обе модели · беттеры + инструмент · Cross-sectional survey of 58 online sports bettors in Tunisia; GD assessed with a DSM-5 criteria questionnaire; prevalence of 53.4% reported.

**Решение:** =

---

### 640 · R3369

**Problem Gambling in Early Adulthood: a Population-Based Study.**

2022 · International journal of mental health and addiction · article, journal article, journalarticle · eng · https://doi.org/10.1007/s11469-020-00401-1

Abstract The aims of this study were to investigate stability of problem gambling between 20 and 24 years of age, and the antecedents and consequences of problem gambling at age 20 years. Young adult participants in the Avon Longitudinal Study of Parents and Children (ALSPAC) completed computer-administered gambling surveys on paper, or online. Responses to the Problem Gambling Severity Index (PGSI) were complete for 2624 participants at 20 years, and 1921 participants at 24 years. Responses were categorized into ‘non-problem’ (71–78%), ‘low-risk gambling’ (16–21%), ‘moderate-risk gambling’ (4–5.5%), and ‘problem gambling’ (1–1.5%). The overall frequency of moderate-risk/problem gambling varied little between age 20 and 24 years, and scratch cards, online betting and gambling were the most frequent activities. Problem gamblers at age 20 years had a history of hyperactivity and conduct problems in adolescence, high sensation seeking, and an external locus of control. They were more likely to have mothers who had problems with gambling, reported less parental supervision, and higher social media usage. Moderate-risk/problem gambling at age 20 years was associated with regular cigarette smoking, high levels of illicit drug use, and problematic use of alcohol at age 24 years. A significant minority of young adults (mainly males) showed problem gambling behaviours which appeared to be established by the age of 20 years and were associated with other potentially addictive behaviours.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · ALSPAC cohort population survey: PGSI plus gambling activities, including online betting; full text may break problem gambling down by activity.

**Решение:** =

---

### 641 · R3383

**Measuring loot box consumption and negative consequences: Psychometric investigation of a Swedish version of the Risky Loot Box Index.**

2022 · Addictive behaviors reports · journal article, article, research-article · eng · https://doi.org/10.1016/j.abrep.2022.100453

Loot boxes are products in videogames that is earned by playing a video game or by buying them. Loot boxes has similar mechanisms as a lottery and there is an ongoing debate if loot boxes are gambling. However, to understand the potential harm of loot boxes valid instruments are needed. An English study psychometrically evaluated an instrument focused on risky loot box use called the Risky Loot Box Index. The study evaluated 12 item scale and based on a factor analysis it was reduced to a five-item scale. The aim of our study is to evaluate a Swedish version of the 12-item instrument from a psychometric perspective. Two samples recruited via an online survey were used. The first sample was recruited from the gambling site Unibet. A mail with an invitation to participate was sent to esports bettors and sport bettors at the gambling site. The second sample was recruited from a Facebook forum focused on e-sports. An invitation was posted on the forum to partake in the study. A total of 195 of respondents (96% men and 4% women) with a mean age of 33.76 (SD = 12.34) answered the Unibet survey and 169 respondents (96% men and 4% women and non-binary) with a mean age of 23.89 (SD = 5.52) answered the Facebook survey. An exploratory factor analysis yielded a two-factor seven item solution. The factors were overconsumption regarding time spent on loot boxes and the other factor was focused on overconsumption of loot boxes in terms of spending money. The confirmatory factor analysis conducted in the Facebook sample validated the result from the exploratory factor analysis. The conclusion of the study is that the Swedish version of the Risky Loot Index has good psychometric properties and can used to measure risky loot box consumption.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Sample includes Unibet sports and esports bettors; problem gambling screen (e.g., PGSI for validity) possible but not stated.

**Решение:** =

---

### 642 · R3385

**The Prevalence and Correlates of Gambling in Australian Secondary School Students.**

2022 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-021-10098-z

Abstract Youth gambling is associated with a range of harms. This study aimed to examine, among Australian adolescents, the prevalence of gambling (ever, in the last month, at-risk and problem), the most frequent gambling types and modalities, and to explore the student characteristics associated with gambling in the last month and with at-risk or problem gambling. Students aged 12–17 years from Victoria and Queensland answered gambling questions as part of the Australian Secondary School Alcohol and Drug (ASSAD) Survey in 2017. The ASSAD also included a series of questions about smoking, alcohol and other drug use, and mental health. A total of 6377 students from 93 schools were included in analysis. The prevalence of ever gambling and gambling in the last month was 31% and 6% respectively. Of students who had gambled in the last month, 34% were classified as at-risk and 15% were classified as problem gamblers. The most frequent types of gambling in the last month were horse or dog race and sports betting. Students who gambled in the last month did so most frequently via a parent or guardian purchasing or playing for them, at home or at a friends’ house, and online or using an app. Regression analysis indicated that male gender, having money available to spend on self, alcohol consumption in the last seven days, the number of types of advertisements seen in the last month, and the number of peer or family members who gambled in the last month, were significantly associated with the likelihood of students gambling in the last month. Male gender, some age categories, and exposure to more types of gambling advertising were also significant predictors of being classified as an at-risk or problem gambler. This large study of youth gambling provides data on gambling behaviours and related variables from a large sample of Australian secondary school students. Student characteristics, including male gender and exposure to more types of gambling advertising, were associated with an increased likelihood of gambling in the last month and of being classified as an at-risk or problem gambler. Further implications of the study findings are discussed.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Adolescent survey measured sports betting participation and at-risk/problem gambling; it may report problem gambling by activity.

**Решение:** =

---

### 643 · R3392

**Participation in Sports Betting and Youth Welfare Nexus**

2022 · Society & Sustainability · article, journal-article · en · https://doi.org/10.38157/ss.v4i2.516

This paper seeks to establish the nexus between sports betting participation and youth welfare in Kenya. The focus of the study is the youth based in the Kajiado North constituency which has the highest youth population within the Nairobi metropolitan statistical area. There are 9 universities around the region. The study sample size is 341. Endogenous switching regression estimation is adopted to determine the association between sports betting participation and youth welfare. From the regression analysis, this study obtains a significant and negative coefficient of -1.4971 relating to sports betting and youth welfare. This suggests that sports betting negatively affects youths' overall welfare in a 1.49 percent greater manner than those who abstain from it. It is important to address the factors that lead the youth to participate in sports betting, particularly control of commercials by making it mandatory that they issue disclaimers that doing so may worsen one's welfare. It is also essential to properly educate young people on financial management in order that they may channel their money toward worthwhile endeavors rather than sports betting.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of Kenyan youth (n=341) on sports betting and welfare; abstract doesn't say whether a problem-gambling instrument was used.

**Решение:** =

---

### 644 · R3404

**Moral incongruence and addiction: A registered report.**

2022 · Psychology of addictive behaviors : journal of the Society of Psychologists in Addictive Behaviors · article, journal article, journalarticle · eng · https://doi.org/10.1037/adb0000876

Objective Diagnostic guidelines for compulsive sexual behavior disorder note that moral distress related to sexual behavior is not sufficient to receive the diagnosis. Recent work has questioned the uniqueness of moral distress in predicting self-reported feelings of sexual addiction, demonstrating that other so-called addictive behaviors (e.g., gaming and internet use) are well-predicted by moral disapproval of those behaviors. The present work tested if moral incongruence (the interaction of behavioral frequency and moral disapproval of a behavior) is uniquely related to sexual behavior, or if it generalizes to other addictions as well. Method This work used a large sample ( N = 4,363) involving a representative sample of the U.S. population ( n = 2,806) and a sample of sports-wagering individuals in the U.S. ( n = 1,557). Interactions between moral disapproval and behavioral frequency were tested for several behaviors (i.e., pornography use, gambling, and several substances). Results The interaction of behavioral frequency and behavioral disapproval (i.e., moral incongruence) predicted self-reported feelings of addiction to pornography and gambling. Moral incongruence was consistently unrelated to self-reported feelings of addiction to tobacco, illicit substances, and prescription drugs. Results regarding alcohol and marijuana were inconclusive. Conclusions Moral incongruence is clearly a salient factor in understanding compulsive sexual behavior, and it appears to also be salient to gambling disorder. Though moral incongruence does not seem relevant to some substances (i.e., nicotine, prescription drug misuse, or illicit drug use), further research is needed regarding the effect of moral incongruence on self-reported feelings of addiction to alcohol and marijuana. (PsycInfo Database Record (c) 2022 APA, all rights reserved).

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Includes a sample of 1,557 US sports bettors; the abstract mentions only perceived addiction, and it is unclear whether a problem-gambling screen was used.

**Решение:** =

---

### 645 · R3405

**Symptoms of Problem Gambling Among US Adults Who Wager on Sports**

2022 · JAMA Network Open · journal article, research support, non-u.s. gov't, journalarticle · eng · https://doi.org/10.1001/jamanetworkopen.2022.39670

This survey study assesses levels of problem-gambling risk across 4 categories of sports-related wagering among US adults.

**ИИ:** + · обе модели · беттеры + инструмент · Survey study of US adults who wager on sports that assesses problem-gambling risk across sports-wagering categories.

**Решение:** =

---

### 646 · R3414

**Perceptions of Gambling and Gaming Among Digital Native Millennials**

2022 · Academia Letters · article · en · https://doi.org/10.20935/al4889

Most regular gamblers will be well aware that technology is revolutionizing the way they can gamble and access gambling. One of the most notable innova- tions has been the proliferation of various gambling applica- tions (‘apps’) for smartphones and computer tablets. A majority of the British bookmakers have launched sports betting apps in- cluding Betfred Mobile Sportsbook, William Hill iPhone, Ladbrokes Mobile, Betfair iPhone Client, and Paddy Power Mobile. Most of the apps allow sports bettors to gam- ble via their mobile phones and/ or tablets (e.g., iPad) with all the same options that gamblers can get offline, and additionally keep track of the bets made. Combined with this, many operators have introduced iPhone compatible websites. Bookmakers have also launched similar apps and ser- vices for Android (i.e., non-Apple) products (e.g., Unibet’s mobile sports betting app). In short, mo- bile sports betting has gone main- stream.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Short letter that may be a perception survey of millennials; abstract is only background, so the design and any PG measure are unclear.); Sonnet -1 (обзор, комментарий, теоретическая, правовая или регуляторная работа: Short Academia Letters essay on mobile gambling apps; the abstract is a narrative introduction with no sign of a survey or problem-gambling measure.)

**Решение:** -

---

### 647 · R3415

**Online sports betting; the gateway to a betting addiction? : and the influence the government should have**

2022 · bachelor thesis · eng · https://tilburguniversity.on.worldcat.org/search?queryString=scr.uvt.nl:10256862

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Bachelor thesis on online sports betting and addiction, with no abstract; it may include a bettor survey using a problem-gambling screen.

**Решение:** =

---

### 648 · R3416

**Accuracy of self-reported gambling frequency and outcomes: Comparisons with account data.**

2022 · Psychology of addictive behaviors : journal of the Society of Psychologists in Addictive Behaviors · journal article, text/project · eng · https://doi.org/10.1037/adb0000792

Objectives: The ability to accurately recall past gambling behavior and outcomes is essential for making informed decisions about future gambling. We aimed to determine whether online gambling customers can accurately recall their recent gambling outcomes and betting frequency. Method: An online survey was distributed to 40,000 customers of an Australian sports and race wagering website which asked participants to recall their past 30-day net outcome (i.e., total amount won or lost) and number of bets. We compared responses to these questions with participants' actual outcomes as provided by the online site. Results: Among the 514 participants who reported their net outcome, only 21 (4.09%) were accurate within a 10% margin of their actual outcome. Participants were most likely to underestimate their losses (N = 333, 64.79%). Lower actual net losses were associated with greater underestimation and overestimation of losses. Of the 652 participants who reported their gambling frequency, 48 (7.36%) were accurate within a 10% margin of their actual frequency. Most participants underestimated their number of bets (N = 454, 69.63%). Higher actual betting frequencies were associated with underestimating betting and lower actual frequencies with overestimating betting. Conclusions: The poor recall accuracy we observed suggests public health approaches to gambling harm minimization that assume people make informed decisions about their future bets based on past outcomes and available funds should be reconsidered. Findings also question the reliability of research outcomes predicated on self-reported gambling behavior. Research is needed to determine the best methods of increasing people's awareness of their actual expenditure and outcomes. (PsycInfo Database Record (c) 2022 APA, all rights reserved).

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of sports and race wagering customers; abstract does not say whether PGSI or another problem-gambling instrument was used.

**Решение:** =

---

### 649 · R3419

**Adolescent betting on esports using cash and skins: Links with gaming, monetary gambling, and problematic gambling.**

2022 · PloS one · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1371/journal.pone.0266571

Adolescents can easily access esports betting sites and place bets using cash or skins. This descriptive cross-sectional study examined the characteristics of adolescent esports bettors and relationships between their esports betting, video gaming activities, monetary gambling participation, and at-risk/problem gambling. Two survey samples of Australians aged 12–17 years were recruited through advertisements ( n = 841) and online panel providers ( n = 826). In both samples, gender and parents’ living situation did not differ by past-month esports cash and skin betting, but recent esports betting was associated with engaging in esports gaming activities such as playing and watching esports, and in monetary gambling activities. Past-month esports betting using cash and skins was significantly associated with at-risk/problem gambling. After controlling for recent monetary gambling, recent esports skin bettors were over 3 times more likely to meet criteria for at-risk/problem gambling. Esports betting using skins appears to pose risks for young people and is easily accessible through unlicensed operators.

**ИИ:** + · обе модели · беттеры + инструмент · Adolescent survey of esports cash/skin bettors that measured at-risk/problem gambling, likely with the DSM-IV-MR-J or a similar screen.

**Решение:** =

---

### 650 · R3421

**Legalized Sports Wagering in America**

2022 · SSRN Electronic Journal · article, journal-article, preprint · en · https://doi.org/10.2139/ssrn.4216904

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the title points to a legal, policy or economic paper on SSRN, but an empirical survey can't be ruled out.

**Решение:** =

---

### 651 · R3436

**Gambling in India: Industry, Social Issues, and Future Directions**

2022 · Glücksspielforschung · book-chapter · en · https://doi.org/10.1007/978-3-658-35635-4_16

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -1 (обзор, комментарий, теоретическая, правовая или регуляторная работа: Book chapter giving an overview of the Indian gambling industry, social issues and future directions; it looks like a narrative overview, not primary survey data.); Sonnet ? (нет аннотации: No abstract; chapter on gambling in India may be a review, but could report survey data on problem gambling and sports betting.)

**Решение:** ?

---

### 652 · R3441

**Parameters for Change in Offline Gambling Behavior After the First COVID-19 Lockdown in Germany.**

2022 · Frontiers in psychology · article, journal article, journalarticle · eng · https://doi.org/10.3389/fpsyg.2022.857234

Introduction: In spring 2020, the first nationwide lockdown in response to the spreading COVID-19 pandemic came into effect in Germany. From March to May, gambling venues, casinos, and betting offices were forced to close. This study explores how land-based gamblers respond to short-term closures of higher-risk forms of gambling. Which gamblers are particularly susceptible to switching to online gambling? Which are more likely to use the lockdown as an opportunity to quit or pause gambling? Potential parameters for these switching or cessation processes are identified using multivariate multinomial logistic regression analysis. Methods: The research questions are analyzed on the basis of quantitative data. For this purpose, a survey was conducted among members of a comparatively large German online access panel ("PAYBACK panel"). The sample of analysis consisted of 612 gamblers who had participated in at least one higher-risk form of gambling and had done so exclusively offline before the first lockdown (January and February 2020). Results: A total of 37.1% of sports bettors ceased participation in higher-risk forms of gambling, compared to 64.1% of casino gamblers. Switching to online gambling, on the other hand, was a rather rare event, regardless of the form of gambling: the proportions differ between 7.7% (slot machines) and 10.9% (sports betting). In the multivariate model female gender, younger age, and a lower frequency of gambling before the first lockdown were found to be significant factors for quitting (instead of continuing) higher-risk offline gambling forms. Secondly, the analysis revealed that individuals with more pronounced cognitive distortions had an increased risk of switching to online gambling rather than staying offline. Discussion: A key finding of this study is that the temporary closure of offline venues does not result in a significant shift towards the online market. Instead, the results of this study show that these short, temporary closures of gambling venues were an appropriate opportunity to give individual groups of gamblers the opportunity to reflect, reduce or quit gambling. It is worth considering implementing such temporary closures as a preventive measure in the future - this should be investigated in advance in further evaluation studies.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Panel survey of offline gamblers including sports bettors; the abstract mentions cognitive distortions but does not name a problem-gambling screen.

**Решение:** =

---

### 653 · R3443

**EXAMINING THE REASONS OF BOXING TRAINERS AND REFEREES WHO PLACE SPORTS BETTING**

2022 · SOCIAL SCIENCE DEVELOPMENT JOURNAL · article, journal-article · en · https://doi.org/10.31567/ssd.785

Purpose: Sports Betting Games; It includes the reasons that are effective in people's desire to earn a lot of money, sometimes their leisure hobby, and sometimes their big dreams. So that; These reasons also become habits in people over time and affect the frequency and habits of playing sports bets. Therefore, the purpose of this research is to examine the reasons for the boxing referees and trainers, who are involved in sports, to play sports bets. Material Method: The universe of the research; The referees and trainers who participated in the Turkish Individual Boxing Championship held in Elazig on September 3-9, affiliated with the Turkish Boxing Federation. The sample of the research is; 62 volunteers from these referees and coaches, 50 male and 12 female, who play sports bets. Data obtained at the end of the research SPSS. Data obtained at the end of the research SPSS. It was defined in 22 package programs and the statistical significance level was accepted as p&lt;0.05. In this research, the 7-question socio-demographic variable created by Yüce (2020) and the Sports Betting Addiction Index (SBBI), which consists of 7 dimensions and 37 items related to betting, were used, and the frequency and percentage values and tables were explained. Results: While the rate of those who bet every day is 43.5%, it is seen that 82.3% of them are from the betting dealers. It has been seen that the amount allocated for betting is 40.3%, 50 TL and below. When the findings, which indicate the degree of risk assessment status of the participants, are examined, it is seen that the motivation levels for playing sports bets are generally indicated by the lower levels of "Less" and "A little". Conclusion: It can be said that sports betting games are not at the addiction level of boxing referees and trainers, the amounts they allocate to bets are low and they do not have any expectations from betting.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of sports-betting boxing referees/trainers using a Turkish 'Sports Betting Addiction Index', not a standard PG screen; needs full-text check.

**Решение:** =

---

### 654 · R3449

**The acquisition, development and maintenance of online sports betting**

2022 · thesis · eng

Sports betting is now the most popular online gambling activity in Europe. The growth of this industry has been attributed to technological advancements and innovations, such as betting via a smartphone and in-play betting. These new advancements have given sports bettors the facility to bet anywhere, anytime, and on hundreds, if not thousands of discrete events. Moreover, the UK has seen a significant increase in the volume of advertising for sports betting products. The growth of sports betting marketing, together with developments in technology, has resulted in concerns about the potentially negative effects of this gambling activity. Therefore, the overall aim of the research presented in this thesis was to contribute to the understanding of online sports betting, particularly in terms of the impact of newer features of online sports betting and sports betting advertising. \ud \ud The aims of this thesis were addressed through four stages of research employing a mixed methods approach including a scoping study, a content analysis study (of 3,375 tweets on social media), in-depth interviews with sports bettors (n=19), and a comprehensive online survey of sports bettors (n=643). Data across the studies were analysed using thematic analysis, principal component analysis, latent class analysis, and multiple regression.\ud \ud The first empirical study within this thesis was a scoping study that systematically reviewed the existing literature on in-play sports betting and quantified the prevalence of these features by examining online sports betting websites. The findings of the review indicated that in-play sports betting has the potential to be more harmful than other forms of gambling (e.g., gambling on fixed odds) because of the inherent structural characteristics. \ud \ud Study 2 was a content analysis that examined how gambling operators marketed their products on Twitter. The results highlighted that Twitter serves as a platform where gambling operators market their products in a normalised and positive way. The findings also highlight that over 90% of the tweets contained no responsible gambling information. \ud \ud Studies 3 and 4 were qualitative explorations of online sports betting. Study 3 explored the perceived impact of sports betting marketing. The study identified the sports betting inducements perceived to be most influential on sports betting behaviour, and highlighted the pervasive nature of sports betting advertising across multiple marketing platforms. Study 4 examined opinions and attitudes towards in-play betting and the ‘cash out’ feature. Overall, in-play sports betting was viewed favourably and easily accessible. However, the findings demonstrated that this is a way of gambling that can be played without interruption and which may lead to repetitive (i.e., continuous) gambling and/or unwarranted feelings of control. \ud \ud Study 5 used latent class analysis to identify five classes of modes used to access sports betting. The results from this study suggest that participating exclusively in online sports betting is not inherently associated with problem gambling. In addition, salient motivations for online sports betting were identified using items from an adapted version of the British Gambling Prevalence Survey (BGPS; Wardle et al., 2011), \ud \ud Drawing together the findings from the previous chapters, the final empirical chapter (study 6), examined which factors might predict problem gambling among sports bettors. Predictors of problem gambling were identified and included higher motor impulsivity, motivations for sports betting, using a laptop to bet, betting at work, mixed mode betting, in-play and ‘cash out’ feature use, and sports betting advertising involvement. This thesis contributes to a greater understanding of online sports betting, and supports the contention that gambling is a multifaceted phenomenon, in which individual factors, as well as structural and situational characteristics should be considered.

**ИИ:** + · обе модели · беттеры + инструмент · The thesis includes an online survey of 643 sports bettors that looked at predictors of problem gambling, so a screening instrument was probably used.

**Решение:** =

---

### 655 · R3457

**Prevalence and Trends in Problem Gambling in Denmark with Special Focus on Country of Origin: Results from the Danish Health and Morbidity Surveys**

2022 · Journal of Gambling Studies · article · en · https://doi.org/10.1007/s10899-021-10093-4

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: National Danish health survey of problem gambling prevalence; no abstract, so unclear whether participation by activity (sports betting) was measured.); Sonnet + (опрос населения об азартных играх: Danish national health survey measuring problem gambling prevalence; likely reports gambling activities (possibly sports betting) by problem gambling status. No abstract, but full text worth reading.)

**Решение:** ?

---

### 656 · R3460

**Problem Gambling Severity of Students Sports Bettors and Its Relationship among the Dimensions of Study Habits: Implications for Counselling**

2022 · Journal of Education Society and Behavioural Science · article, review, journal-article · en · https://doi.org/10.9734/jesbs/2022/v35i111184

Gambling is a well-known activity in most nations. Problem gambling as an index of gambling refers to the adverse effects on the gambler, on other individuals, his/her social life or even on the community as a result of the individual’s excessive gambling behaviour. Hence, problem gambling refers to all the harmful behaviours resulting from constant gambling. The purpose of this study was to investigate problem gambling severity and its relationship with the dimensions of study habits of students’ sport bettors in the University of Cape Coast. Descriptive survey design was adopted for the study. A population of 4,172 of level 400 students from four colleges of the university of Cape Coast were used for the study. Using the Krejcie and Morgan table, a fair representation of a population of 4,172 is 351. The researchers further used disproportionate stratified sampling technique to draw from each college the number required for the study. The PGSI items and Essuman Study Habit Inventory recorded Cronbach alpha of .76 and .97 respectively. The ordinal logistic regression was used to determine whether problem gambling severity had any relationship with any of the dimensions of study habits. The findings showed that the dimensions of study habit has a predictive relationship on gambler sub-type. It was recommended among other things that a proposed ‘Gaming Research Unit’ under the auspices of the Department of Education and Psychology should ensure the screening of students who are low risk, moderate-risk or problem gambler and with difficulties in their study habit should be referred for guidance and counselling.

**ИИ:** + · обе модели · беттеры + инструмент · Survey of student sports bettors at University of Cape Coast that used the PGSI to group them by gambler subtype.

**Решение:** =

---

### 657 · R3471

**Análisis de los perfiles y prácticas potencialmente adictivas de los usuarios de plataformas de trading**

2022 · bachelor thesis · esl/spa · https://academica-e.unavarra.es/handle/2454/44632

El trading online ha experimentado un gran crecimiento en los últimos años y ha cambiado radicalmente el universo de la inversión. El impacto del COVID-19 fue excepcional e hizo que el número de inversores primerizos se multiplicara durante los meses de movilidad más restringida. Operar en los mercados financieros siempre ha implicado altos niveles de estrés y adrenalina relacionados con la pérdida o ganancia de dinero. Algunas formas de negociación especulativa comparten similitudes con los juegos de azar y las apuestas deportivas. Las decisiones se suelen basar en información limitada, motivos de ganancia a corto plazo y resultados altamente volátiles e inciertos. El presente estudio investiga la relación entre el trading “según frecuencia de operación” y las formas tradicionales de juego en España, así como el perfil de los individuos que lo practican. Los resultados muestran diferencias en el comportamiento de los inversores y en sus datos demográficos. Son necesarias investigaciones futuras con una muestra de mayor tamaño para llegar a resultados más concluyentes. Online trading has experienced tremendous growth in recent years and has radically changed the investment universe. The impact of COVID-19 was exceptional and caused the number of first-time investors to multiply during the months of more restricted mobility. Trading in financial markets has always involved high levels of stress and adrenaline related to making or losing money. Some forms of speculative trading share similarities with gambling and sports betting. Decisions are often based on limited information, short-term profit motives and highly volatile and uncertain outcomes. This study investigates the relationship between trading “by trading frequency” and traditional forms of gambling in Spain, as well as the profile of the individuals who trade. The results show differences in investor behaviour and demographics. Future research with a larger sample size is needed to reach more conclusive results. Graduado o Graduada en Administración y Dirección de Empresas por la Universidad Pública de Navarra Enpresen Administrazio eta Zuzendaritzan Graduatua Nafarroako Unibertsitate Publikoan

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of trading users about traditional gambling forms (possibly including sports betting); unclear if a problem-gambling instrument was used.

**Решение:** =

---

### 658 · R3475

**Differences between Gamblers and Non-Gamblers on Sports Betting Websites.**

2022 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-021-10065-8

Online sports gambling is a popular recreational activity. Using the Theory of Planned Behaviour as the theoretical foundation, the aim of this study was to examine for differences between gamblers and non-gamblers in terms of their attitudes, subjective norms and perceived behavioral control towards online sports gambling. 173 male students from a tertiary educational institution were recruited for this study of which 56 respondents (32%) were gamblers. A series of regression analysis revealed differences between gamblers and non-gamblers. While subjective norms and perceived behavioural control were significant predictors of gambling intentions for the gamblers group, only attitude was a significant predictor for the non-gamblers group. Further analysis showed that subjective norms had a larger effect on the gamblers group in comparison to the non-gamblers group. Physiological data from an eye tracker provided further empirical evidence that there were differences between gamblers and non-gamblers. Gamblers, perhaps because they are more familiar with gambling websites, take less time to process information. The findings from this study suggests that there are differences between gamblers and non-gamblers. To prevent problem gambling, there is a need to develop different communication messages for gamblers and non-gamblers.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Student survey on online sports gambling (TPB, eye-tracking); the abstract doesn't say whether a problem-gambling screen was used.

**Решение:** =

---

### 659 · R3477

**Chapter 8 : E-Sports, Gambling, Match-Fixing, and Performance Enhancement**

2022 · Lexington Books · part of book or chapter of book, book-chapter · en · https://doi.org/10.5771/9781793613387-115

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: Book chapter covering esports integrity issues (gambling, match-fixing, doping); likely conceptual or legal discussion, not a survey of bettors.); Sonnet ? (нет аннотации: Book chapter on esports, gambling, match-fixing without abstract; likely a review/discussion, but could report survey data on esports betting and problem gambling.)

**Решение:** ?

---

### 660 · R3498

**Effects of Sport Betting Practices on Income and Livelihood Among Youths in the Dodoma City, Tanzania**

2022 · Springer eBooks · part of book or chapter of book, book-chapter, conference-paper · en · https://doi.org/10.1007/978-3-030-90973-4_50

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · There is no abstract. The title suggests a study of young sports bettors in Tanzania, but it doesn't say whether problem gambling was measured.

**Решение:** =

---

### 661 · R3509

**Sports Betting Has Gone Virtual: A Sociological Analysis of a New Form of Sports Betting Among Youths in Northern Nigeria**

2022 · Indonesian Journal of Sociology Education and Development · article, other literature type, text/ · en · https://doi.org/10.52483/ijsed.v4i1.59

The paper examined the rise of virtual sports betting among football bettors in Northern Nigeria. The study aims to examine the level of penetration of virtual betting and identify the reasons for the development. The researcher adopted Instant Gratification Model to explain the shift from betting on real-time sports betting to virtual betting in the areas selected for the study. The study has adopted a cross-sectional study design, and data were elicited through mixed methods (qualitative and quantitative). Thirteen interviews were conducted: Six Key Informant Interviews (KII) and seven In-Depth Interviews (IDI) with the sports bettors &amp; operators of sports betting outlets. For the quantitative data, 927 structured questionnaires were administered, while 685 were retrieved from the respondents, indicating a 74% response rate. Qualitative data are presented in a prose style, while quantitative data are presented in a tabular form, of frequency tables and cross-tabulation based on the study's objectives. The study found that most virtual sports bettors were youth and educated. It also found that the availability of virtual sports betting 24 hours, unlike actual sporting events, has been identified as one factor that motivates football bettors or gamblers to shift their attention to virtual betting. Furthermore, it found that there are other virtual sporting events like Dog Race and Basketball that attract the bettors' attention to virtual betting. Additionally, the time to finish a virtual football match of fewer than three minutes is also one of the reasons that sports bettors patronize virtual betting because they do not need to wait for 90 minutes to know their fate as in an accurate football match.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Questionnaire survey of 685 Nigerian sports bettors on virtual betting; no problem-gambling instrument mentioned, though one is not ruled out.

**Решение:** =

---

### 662 · R3517

**Markers of Harm in Internet Sports Gambling**

2022 · OSF Preprints (OSF Preprints) · preprint · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; sports gambling harm markers may be behavioural-only or may be validated against a PGSI-type instrument.

**Решение:** =

---

### 663 · R3520

**Impact of the "when the fun stops, stop" gambling message on online gambling behaviour: a randomised, online experimental study.**

2022 · The Lancet. Public health · journal article, research support, non-u.s. gov't, journalarticle · eng · https://doi.org/10.1016/s2468-2667(21)00279-6

BACKGROUND: Safer gambling messages are a common freedom-preserving method of protecting individuals from gambling-related harm. Yet, there is little independent and rigorous evidence assessing the effectiveness of safer gambling messages. In our study, we aimed to test the effect of the historically most commonly-used UK safer gambling message on concurrent gambling behaviour of people who gamble in the UK. METHODS: In this study, three preregistered, incentivised, and randomised online experiments, testing the UK's "when the fun stops, stop" message, were carried out via the crowdsourcing platform Prolific. Adults based in the UK who had previously participated in the gambling activities relevant to each experiment were eligible to participate. Experiments 1 and 3 involved bets on real soccer events, and experiment 2 used a commercially available online roulette game. Safer gambling message presence was varied between participants in each experiment. In experiment 2, exposed participants could be shown either a yellow or a black-and-white version of the safer gambling message. Participants were provided with a monetary endowment with which they were allowed to bet. Any of this money not bet was afterwards paid to participants as a bonus, in addition to the payouts from any winning bets. In experiment 2 participants had the opportunity to re-wager any winnings from the roulette game. The primary outcome in experiment 1 was participants' decisions to accept (or reject) a series of football bets, which varied in their specificity (and payoffs), and the primary outcomes of experiments 2 and 3 were the proportion of available funds bet, which were defined as the total amount of money bet by a participant out of the total that could have been bet. FINDINGS: Participants for all three experiments were recruited between May 17, 2019, and Oct 17, 2020. Of the 506 participants in experiment 1, 41·3% of available bets were made by the 254 participants in the gambling message condition, which was not significantly different (p=0·15, odds ratio 1·22 [95% CI 0·93 to 1·61]) to the 37·8% of available bets made by the 252 participants in the control condition. In experiment 2, the only credible difference between conditions was that the 501 participants in the condition with the yellow version of the gambling message bet 3·64% (95% Bayesian credibility interval 0·00% to 7·27%) more of available funds left over than the 499 participants in the control condition. There were no credible differences between the bets made by the 500 participants in the black-and-white gambling message condition and the other conditions. In experiment 3, there were no credible differences between the 502 participants in the gambling message condition and the 501 participants in the control condition, with the largest effect being a 5·87% (95% Bayesian credibility interval -1·44% to 13·20%) increase in the probability of betting everything in the gambling message condition. INTERPRETATION: In our study, no evidence was found for a protective effect of the most common UK safer gambling message. Alternative interventions should be considered as part of an evidence-based public health approach to reducing gambling-related harm. FUNDING: University of Warwick, British Academy and Leverhume, Swiss National Science Foundation.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Experiments with UK football bettors; the abstract doesn't say whether PGSI or another problem-gambling screen was given to describe the sample.

**Решение:** =

---

### 664 · R3524

**Sports Betting in Denmark: An Explorative Study on Male Adolescents Aged 15-17**

2022 · Copenhagen Business School · master thesis · eng · https://research.cbs.dk/en/studentProjects/e35c8ec3-5289-4ee9-b991-d27a9d5790ba

Since the partial liberalization of the gambling market in Denmark, the industry has expanded considerably. Modern sports betting has intensified which has created a situation in which sports betting is no longer confined to adult-dominated leisure spheres but is becoming an increasingly popular leisure activity for adolescents (defined here as individuals aged 15-17). The current literature has not examined the phenomenon of sports betting among male adolescents and the impact it can have on their lives. This thesis proposes an indication of the current extent of sports betting among male adolescents aged 15-17 in Denmark. Furthermore, the thesis study analyzes adolescents’ motivations to engage in sports betting, as well as the role of identity and socialization agents. Finally, adolescents’ perception and understanding of sports betting advertising is examined. This was accomplished by using mixed methods (review of literature), a questionnaire (n = 204), focus groups (n = 12), and semi-structured interviews (n = 7). The findings based on the quantitative data indicated the current scope of sports betting amongst Danish male adolescents aged 15-17. The analysis found that all Danish male adolescents aged 15-17 are aware of sports betting and that 59% have tried betting on sports at least once. Furthermore, the analysis showed that Danish male adolescents mostly bet once a week, and that they on average spend between DKK 1 - 50 per session. The findings of the qualitative data found that the primary driver for engaging in sports betting is sport. Subsequently, secondary drivers for male adolescents’ engagement in sports betting was identified as excitement, use of knowledge and competencies to gain a financial profit, and social motivation. Furthermore, it is concluded that male adolescents do not consider sports betting as a part of their identity. However, multiple facets of sports betting were found to contribute to adolescents’ identity development, and adolescents’ peers were found to be a main factor for their sports betting behavior. Finally, it was determined that male adolescents are highly aware of sports betting advertisements and advertising techniques, and that they are able to recognize and recall specific sports betting brands and advertisements. It was concluded that adolescents’ have varying perceptions and understanding of sports betting advertising as some perceive it with critical and skeptical attitudes whereas others have positive or indifferent attitudes towards them. Finally, recommendations to improve the circumstances of sports betting among male adolescents in Denmark are proposed to sports betting operators, policy makers, and authorities.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Questionnaire of adolescent sports bettors (n=204); abstract reports frequency and spending but doesn't say whether a problem-gambling screen was used.

**Решение:** =

---

### 665 · R3533

**Changes in sports gambling behavior during the COVID-19 pandemic in Canada.**

2022 · Frontiers in psychiatry · article, journal article, journalarticle · eng · https://doi.org/10.3389/fpsyt.2022.1018234

Sports betting is one of the most popular forms of gambling in Canada; recent prevalence estimates indicate that 7.9% of Canadian adults endorsed gambling on sports in the past year. The ongoing COVID-19 pandemic led to the temporary closure of most major sports leagues worldwide beginning in March of 2020. These sudden closures created a dramatic decrease in the availability of sports betting opportunities in the early stages of the pandemic, followed by a subsequent increase in availability as most sport leagues returned during the summer of 2020. Using a retrospective self-report measure of gambling participation, the present study investigated how the gambling behaviors of N = 85 past-year sports gamblers changed over the course of the pandemic. It was hypothesized that sports gamblers would report an initial decrease in gambling behaviors from pre-pandemic baseline levels to the early stages of the pandemic in May of 2020 when the availability of sports gambling was heavily restricted, followed by an increase in gambling behaviors from May to August, in accordance with the re-emergence of live sporting events. The general pattern of results supported the hypotheses, though gambling behaviors did not completely return to baseline levels. Beyond quantifying the changes in gambling behaviors over the early stages of the pandemic in Canada, results may have implications regarding the utility of voluntary gambling exclusion programs as well as legislation concerning gambling access.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of 85 past-year sports gamblers in Canada; the abstract doesn't say whether a problem-gambling instrument like the PGSI was used.

**Решение:** =

---

### 666 · R3534

**심리적 도박 중독성 지수 및 행동적 도박 심각도 지수를 통한 국내 스포츠베팅 이용자의 중독 영향요인에 대한 연구**

2022 · Korean Journal of Sport Science · article, review · ko · https://doi.org/10.24985/kjss.2022.33.4.687

PURPOSEThis study aimed to a) develop suitable screening tools for identifying gambling severity in Korea and b) explore factors that affect the gambling severity index in order to prevent Korean sports betting users from easily falling into gambling addiction, thus providing practical and useful guidelines in this regard.METHODS This study examined Korean sports fans who had experiences of participating in sports betting (Sports Toto), a legal sports betting system in Korea.Toward this end, an online survey was conducted from May 10 to June 25, 2022.A total of 214 questionnaire results, excluding 23 who gave insincere and/or incomplete answers, were analyzed for normal distribution through skewness and kurtosis, and subscale scores were calculated after performing exploratory factor analysis and reliability analysis using Cronbach's α. RESULTS A psychological gambling severity index and behavioral gambling severity index were developed based on a stepwise regression analysis, which was conducted using the demographic characteristics of domestic sports betting participants and their lifestyle habits (e.g., smoking and drinking, problem gambling severity index, selfcontrol scale, and gambling expectation scale).CONCLUSIONS First, factors affecting the psychological gambling severity index were identified (having a job, job stability, and security) along with lifestyle habits (smoking and drinking).Second, gender, occupational characteristics, full-time employment, confidence in self-control, and desire for self-improvement were indicated as significant factors that influenced the behavioral gambling severity index. 서론 서론연구의 필요성 1. 체육진흥투표권 확대 논의 2001년 10월 국내에서 발매를 시작한 체육진흥투표권은 2020년 까지 총 12조원의 수익금을 조성하였다.이러한 수익금은 프로스포 츠 활성화, 유소년 아마추어 스포츠 활성화, 스포츠클럽육성 지원, 스포츠 인프라 구축, 스포츠 모태펀드 사업, 저소득가정을 위한 스포 츠 바우처 프로그램,

**ИИ:** + · обе модели · беттеры + инструмент · Survey of 214 Korean Sports Toto bettors that used the problem gambling severity index (PGSI); prevalence may be reported.

**Решение:** =

---

### 667 · R3538

**Development and validation of a prediction model for online gambling problems based on players' account data.**

2022 · Journal of behavioral addictions · article, journal article, journalarticle · eng · https://doi.org/10.1556/2006.2022.00063

Abstract Background and aims Gambling disorder is characterized by problematic gambling behavior that causes significant problems and distress. This study aimed to develop and validate a predictive model for screening online problem gamblers based on players' account data. Methods Two random samples of French online gamblers in skill-based (poker, horse race betting and sports betting, n = 8,172) and pure chance games (scratch games and lotteries, n = 5,404) answered an online survey and gambling tracking data were retrospectively collected for the participants. The survey included age and gender, gambling habits, and the Problem Gambling Severity Index (PGSI). We used machine learning algorithms to predict the PGSI categories with gambling tracking data. We internally validated the prediction models in a leave-out sample. Results When predicting gambling problems binary based on each PGSI threshold (1 for low-risk gambling, 5 for moderate-risk gambling and 8 for problem gambling), the predictive performances were good for the model for skill-based games (AUROCs from 0.72 to 0.82), but moderate for the model for pure chance games (AUROCs from 0.63 to 0.76, with wide confidence intervals) due to the lower frequency of problem gambling in this sample. When predicting the four PGSI categories altogether, performances were good for identifying extreme categories (non-problem and problem gamblers) but poorer for intermediate categories (low-risk and moderate-risk gamblers), whatever the type of game. Conclusions We developed an algorithm for screening online problem gamblers, excluding online casino gamblers, that could enable the setting of prevention measures for the most vulnerable gamblers.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · French online gamblers, including sports bettors, surveyed with the PGSI alongside account data; PGSI results by game type may be reported.

**Решение:** =

---

### 668 · R3540

**Análisis de las campañas de publicidad de las casas de apuestas Betfair y Bet365, y su influencia en los estudiantes del Campus María Zambrano**

2022 · bachelor thesis · esl/spa · https://uvadoc.uva.es/handle/10324/54659

Durante el año 2020 el consumo de las casas de apuestas deportivas online creció considerablemente, incrementándose un 58% durante los últimos meses. La finalidad de esta investigación es dar cuenta de la influencia de las campañas de publicidad de las casas de apuestas entre los jóvenes universitarios del Campus María Zambrano, en concreto, analizaremos las campañas de Betfair y Bet365, ya que son las casas de apuestas a las que más recurre el target investigado. Para llevar a cabo la investigación, hemos analizado las campañas de Bet365 y Betfair, asimismo, hemos realizado una encuesta y una serie de entrevistas semiestructuradas al objeto de dar respuesta a la pregunta principal: ¿La publicidad de las casas de apuestas Bet365 y Betfair influye en los estudiantes del Campus de María Zambrano de la Universidad de Valladolid en su decisión de apostar? Grado en Publicidad y Relaciones Públicas

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Bachelor thesis surveying students about betting-ad influence; a problem-gambling instrument seems unlikely but the abstract doesn't say.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Thesis on betting advertising influence in university students via survey and interviews; no problem-gambling instrument mentioned.)

**Решение:** -

---

### 669 · R3541

**Cognitive Distortions and Problem Gambling in Sports Betting**

2022 · Journal of Gambling Issues · article, journal-article · en · https://doi.org/10.4309/mxdf4708

The open access publication is available at: https://doi.org/10.4309/mxdf4708 ; Sports betting is an activity that has seen tremendous growth over the past decade. The integrative nature of sports betting in marketing mediums and the advent of modern technology makes it a particularly dangerous form of gambling. This study aimed to compare the cognitions of sports bettors and non-sports gamblers. A total of 713 participants were recruited, of which 80 were sports bettors, 270 were non-sports gamblers, and 363 were non- gamblers. Cognitive distortions were measured using the Gamblers Belief’s Questionnaire, which comprises two factors: Luck/Perseverance, and Illusion of Control. The results of a between-groups MANOVA showed that sports bettors recorded higher scores for Luck/Perseverance (M = 35.27, SD = 13.63) than non-gamblers (M = 17.60, SD = 8.20, p < .001) and non-sports gamblers (M = 27.19, SD = 11.81, p < .001). Sports gamblers also recorded higher Illusion of Control scores (M = 25.48, SD = 8.81) than both non-gamblers (M = 13.46, SD = 6.50, p < .001) and non-sports gamblers (M = 19.76, SD = 7.91, p < .001). Problem gambling was measured using the South Oaks Gambling Screen. One-way analysis of variance between the three groups showed sports bettors scores (M = 3.45, SD = 3.29) were higher than those of nonsports gamblers (M = 1.62, SD = 2.30), and non- gamblers (M = 0.29, SD = 0.96, p < .001). These findings suggest that gamblers should not be treated as a homogenous group, and that greater attention should be placed on sports bettors in prevention and treatment efforts.

**ИИ:** + · обе модели · беттеры + инструмент · Survey of 80 sports bettors and other gamblers that used the SOGS; the problem-gambling prevalence among sports bettors may be reportable.

**Решение:** =

---

### 670 · R3543

**Bored Boys Bet: Predictors of Sports Gambling Behavior by University Students during the COVID-19 Lockdown**

2022 · Addiction & Addictive Disorders · article, journal-article · en · https://doi.org/10.24966/aad-7276/100092

A state of emergency was declared on March 27, 2020 in the province of Manitoba due to the COVID-19 pandemic. For three months, the population of Manitoba was confined to their homes; social contact was restricted to grocery shopping, medical appointments and medical prescription purchases.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of university students' sports gambling during COVID lockdown; abstract truncated, unclear if problem-gambling instrument used.

**Решение:** =

---

### 671 · R3545

**Glücksspiel- und Wettverhalten in Österreich – aktuelle Ergebnisse einer Repräsentativerhebung**

2022 · Suchttherapie · article · de · https://doi.org/10.1055/s-0042-1755994

Einleitung Nach zwei Erhebungen zum Glücksspiel- bzw. Wettverhalten der österreichischen Wohnbevölkerung 2009 bzw. 2015 bestand Bedarf an rezenteren Daten, um aktuelle Entwicklungen – nicht zuletzt vor dem Hintergrund der Corona-Pandemie – abzubilden. Material und Methodik Repräsentativerhebung zu Substanzkonsum- und Verhaltensweisen mit Suchtpotenzial. Panel mit drei Erhebungswellen im Frühjahr 2022 (N= 5.963), Herbst 2020 (N= 3.289) und Frühjahr 2022 (laufend). Ergebnisse Im Zeitraum vom Beginn der Pandemie bis zur zweiten Erhebungswelle kam es zu einer Abnahme der Glücksspieltätigkeit. Knapp die Hälfte der Befragten (47 %) gibt an, in den letzten zwölf Monaten an Glücksspiel oder Sportwetten teilgenommen zu haben, und ein Viertel (25 %) berichtet dies für die letzten 30 Tage. Tägliche Teilnahme an Glücksspiel oder Sportwetten wird in der Stichprobe nur sehr selten berichtet (0,3 %). Bei 1,8 % der Befragten legen die Ergebnisse problematisches oder pathologisches Spielverhalten nahe. Zusammenfassung Pandemiebedingt kam es zu Veränderungen im Glücksspiel- und Wettverhalten der österreichischen Wohnbevölkerung. Ob diese Veränderungen nachhaltig sind, können anhand der vorläufigen Ergebnisse der dritten Erhebungswelle, die bei dem Vortrag erstmals vorgestellt werden, diskutiert werden. Publication History Article published online: 30 August 2022 © 2022. Thieme. All rights reserved. Georg Thieme Verlag Rüdigerstraße 14, 70469 Stuttgart, Germany

**ИИ:** + · обе модели · опрос населения об азартных играх · Austrian representative population survey measuring gambling and sports betting participation plus problem/pathological gambling (1.8%).

**Решение:** =

---

### 672 · R3546

**Juego en Euskadi: las mujeres prefieren las loterías y los hombres las apuestas deportivas**

2022 · The Conversation · article, other · es · https://doi.org/10.64628/aao.x5u7wsgrr

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Popular article apparently reporting Basque gambling survey data by activity and gender; no abstract, unclear whether problem gambling measured.

**Решение:** =

---

### 673 · R3562

**Study of the factors affecting the changes in people&#039;&#039;s tendency to online betting in sports during corona pandemy**

2022 · 13th International Congress on Sport Sciences · article · eng · https://doi.org/10.22089/ssrc-13th.2022.3529

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Conference paper on online sports betting during COVID; no abstract, so unclear whether a problem-gambling instrument was used.

**Решение:** =

---

### 674 · R3566

**Prevalence and Possible Predictors of Gambling Disorder in a Sample of Students in the Healthcare Professions.**

2022 · International journal of environmental research and public health · journal article, journalarticle, article · eng · https://doi.org/10.3390/ijerph20010452

The Italian version of the South Oaks Gambling Screen questionnaire (SOGS) and a socio-demographic questionnaire were administered to a sample of 275 healthcare professions students aged 19 to 58 years (mean age = 22.17; females = 81.1%) to address the research objectives: to examine the prevalence and correlates of problem gambling in a population of university healthcare professions students in Italy. Among the sample, 8.7% ( n = 24) of participants showed problem gambling and 1.5% ( n = 4) pathologic gambling. Lottery and scratch cards were the most frequent type of gambling in the sample, followed by cards and bingo. Compared to females, males tend to be more involved in problem gambling and pathological gambling. Males tend to be more involved than females in different types of gambling (such as cards, sports bets, gambling at the casino). Pathological gambling is positively associated with gender, being students lagging behind the regular schedule of exams and parents' level of education. These findings have important implications in terms of prevention and intervention on gambling and pathological gambling. Universities should make available educational programs and counselling services to address this issue.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Student survey using SOGS that also measured sports betting participation; it could report problem gambling among sports bettors.

**Решение:** =

---

### 675 · R3568

**The Gambling Behaviour and Attitudes to Sports Betting of Sports Fans.**

2022 · Journal of gambling studies · article, journal article, journalarticle/journal contribution · eng · https://doi.org/10.1007/s10899-021-10101-7

Abstract Survey responses from a sample of nearly 15,000 Australian sports fans were used to study the determinants of: (i) gambling behaviour, including if a person does gamble and the type of gambling engaged with; (ii) the number of sports and non-sports bets made over a 12-month period; and (iii) attitudes towards betting on sports. The probability of betting on sports decreased with increasing age and was lower for women and people with a university education. This gender difference varied with age, with the greatest difference found among the young. Similar effects were observed for the number of sports bets made, which declined with age. The gender difference in the number of sports bets also varied with age with the greatest difference found among the young arising from the high propensity of young men to bet on sports. Attitudes to sports betting were also analysed, with a key finding that, within friendship circles, the views that sports betting is perceived as harmless, common and very much a part of enjoying sports were stronger among young men. These permissive attitudes were stronger among people who bet on sports and those who bet on sports more frequently. The analysis of sports fans provides insights into the characteristics of the target market most likely to bet on sports, which can be used to inform public health initiatives and harm reduction campaigns.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Large survey of sports fans that measured sports betting; abstract doesn't say whether a problem-gambling instrument like PGSI was used.

**Решение:** =

---

### 676 · R3588

**HABITS AND FREQUENCY OF (ONLINE) GAMBLING AMONG YOUNG PEOPLE IN BOSNIA AND HERZEGOVINA**

2022 · Socijalna politika · article · en · https://doi.org/10.22182/sp.32021.6

Gambling of young people as a risky behavior is an increasingly current social problem, but also the subject of numerous researches. The gambling industry is one of the fastest-growing industries in the world, and a significant increase in availability has taken place in the Bosnian and Herzegovinan society. Young people in BiH are entering the world of gambling more often and easier. Bad economic situation, social unrest, high poverty and unemployment rates contribute to this situation. World statistics show that the increase in gambling was significantly affected by the COVID-19 pandemic. Omnipresent digitalization during the pandemic, movement restrictions, but also existential uncertainty have opened a new path to online gambling. Therefore, an research was conducted in which the habits of young people (N=174) and their frequency of (online) gambling were examined. The questionnaire results showed that 70.5% of respondents had played games of chance at least once in their lives. Young people usually play one-time tickets and sports betting. Of particular concern is the fact that individuals play online games of chance on a daily basis. They usually invest a smaller amount of money and more than half of the respondents have lost money on betting at least once. The data show that gambling is most often out of boredom, fun and socializing, and they do not consider such behavior to be problematic. According to self-assessment, only 5.9% of respondents believe that their gambling is somewhat or completely problematic, while 3.7% state that the degree of gambling addiction is so high that they need professional help. On the other hand, Bosnia and Herzegovina lacks prevention programs aimed at problematic youth gambling, which is why they remain deprived of professional support. All of this suggests that serious investment in public health and social policies is needed to offer quality prevention and psychoeducational programs.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Youth survey measured sports betting; problem gambling reported only by self-assessment, so it is unclear whether a validated screening instrument was used.

**Решение:** =

---

### 677 · R3592

**Gambling among 16-year-olds and associated covariates: A Nordic comparison.**

2022 · Scandinavian journal of public health · journal article · eng · https://doi.org/10.1177/1403494820923814

Aims: This study aimed to compare the prevalence in different gambling types as well as problem gambling in the Nordic countries, examining gambling, leisure activities, school truancy, parental relations and consumption of alcohol and other substances as covariates for problem gambling. Methods: Cross-country data were provided by the European Survey Project on Alcohol and Other Drugs (ESPAD) 2015. Prevalence of gambling and potential covariates were analysed for Denmark, Finland, Iceland Norway and Sweden (N=13,172 respondents aged 16 years), while analyses regarding problem gambling only included countries that participated in the optional questions on gambling problems (Denmark, Finland and Sweden; N=8108). We tested variables for problem gambling by bivariate logistic regression and multivariate logistic regression. Results: Cross-country differences were found in gambling and problem gambling, as well as differences in covariates for problem gambling. Sweden had the lowest rate of problem gambling. No significant difference was found between Denmark and Finland. Reports of too much gaming, inhalants, slots, betting and online gambling were positively associated with problem gambling, while parental monitoring and parental caring had a negative association. The relevance of the covariates varied across countries. Conclusions: Results indicate that although gambling regulation and its implementation have an important impact on gambling behaviour, we need more research on social, economic and cultural factors and how youth understand and interact with them. Contexts and regulations in other related fields should inform gambling research, policies and interventions.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · ESPAD adolescent survey measured gambling types including betting and problem gambling (likely Lie/Bet); association with betting reported.

**Решение:** =

---

### 678 · R3603

**Social and lifestyle characteristics of sports bettors in Serbia**

2022 · Medicinska istrazivanja · article, review, journal-article · en · https://doi.org/10.5937/medi55-38731

Aim: The aim of our study was to examine the prevalence of sports betting in the previous month in Serbia and its association with social and lifestyle characteristics. Methods: The analysis of the data from the cross-sectional survey National Survey on lifestyles in Serbia: substance abuse and gambling conducted in 2014 was performed. 10% of participants reported sports betting in the past 30 days. Results: Sports betting was associated with male gender, living in urban areas compared to living in rural areas, having secondary education compared to having primary education, being employed compared to being retired. Sports betting in the previous month was also associated with binge-drinking compared to abstaining from alcohol, non-prescription use of anti-anxiety medications compared to no use of anti-anxiety medications and low/ moderate problem gambling compared to no problem gambling as measured by PGSI. However, it was not associated with a higher risk of tobacco smoking and illicit drug use. Conclusions: The association of sports betting with risk behaviors among young males should be a concern for public health authorities.

**ИИ:** + · обе модели · беттеры + инструмент · National survey in Serbia; sports bettors from the past month were compared with others on problem gambling measured by the PGSI.

**Решение:** =

---

### 679 · R3607

**Conceptualising emotional and cognitive dysregulation amongst sports bettors; an exploratory study of 'tilting' in a new context.**

2022 · PloS one · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1371/journal.pone.0264000

Tilting is a poker-related phenomenon that involves cognitive and emotional dysregulation in response to unfavourable gambling outcomes. Tilting is characterised by an increase in irrational, impulsive and strategically weak betting decisions. This study aimed to adapt and investigate the concept of tilting amongst sport bettors in order to provide preliminary insight regarding previously unexplored instances of maladaptive sports betting. The sample consisted of 225 sports bettors who completed an online questionnaire that investigated their reported tilting episodes, awareness of tilting, impulsivity, perceived skill, gambling severity, gambling frequency, and product preferences. Cluster analyses revealed three distinct groups of sports bettors based on their reported tilting episodes and their awareness of this phenomenon. The first group were labelled 'Conscious tilters' due to being cognizant of their own tilting occurrence which was significantly higher than the other two groups. These 'Conscious tilters' had the highest mean problem gambling severity that was indicative of the 'problem gambler' categorisation. The second group were labelled 'Unconscious tilters' due to their underestimation of their own tilting occurrence and were categorised as 'moderate risk gamblers'. The third group were labelled 'Non-tilters' due to a relatively accurate perception of their low to non-existent tilting occurrence and were categorised as 'low-risk gamblers'. Additionally, there were significant differences between these groups in relation to reported gambling frequency, impulsivity, and product preferences. There is evidence of various classifications of 'tilters' within sports betting. Specific sports betting product features may also facilitate tilting and therefore require further research in this context. It is important for this research area to develop in order to mitigate harms associated with the rapidly changing sport betting environment.

**ИИ:** + · обе модели · беттеры + инструмент · Survey of 225 sports bettors that measured gambling severity using PGSI-type risk categories (problem gambler, moderate risk, low risk).

**Решение:** =

---

### 680 · R3613

**Gender and Age in Gambling Participation, Gambling Onset, and Problematic Gambling in a General Population Sample: Empirical Findings from Germany**

2022 · International Journal of Mental Health and Addiction · article · en · https://doi.org/10.1007/s11469-021-00746-1

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** + · обе модели · опрос населения об азартных играх · German general population survey of gambling participation and problem gambling; activity-level data (including sports betting) probably in the full text.

**Решение:** =

---

### 681 · R3631

**Gambling Harm and the Prevention Paradox in Massachusetts**

2022 · Addicta The Turkish Journal on Addictions · article · en · https://doi.org/10.5152/addicta.2021.21114

The term “prevention paradox” focuses on the notion that more aggregate harm is experienced by low-risk individuals even though high-risk individuals experience the greatest amount of harm per individual. This paper examines whether the prevention paradox in relation to gambling harms exists in Massachusetts. The analysis is drawn from two population surveys and the distribution of harms across four gambling severity groups is examined. The results show that because of the larger size of the three lower severity groups, even the much smaller average number of harms endorsed by members of these groups accounts for nearly three-quarters (72.9%) of the aggregate number of harms across all groups. While almost all individuals in the highest severity group report one or more harms, any individual reporting one or more harms is more likely to be in a lower severity group. Financial, health, and emotional/psychological harms are more common and more broadly distributed across the gambling severity groups compared to relationship, work/school, and illegal harms. In contrast to a similar study in Finland, which found that the most severe group accounted for over 50% of the harms in the health, relationship, and illegal harm domains, the prevention paradox is supported across all harm domains in Massachusetts.

**ИИ:** разошлись — Opus + (опрос населения об азартных играх: Analysis of two Massachusetts population gambling surveys using gambling severity groups (likely PGSI); the full text may give activity-level data.); Sonnet ? (неясно, есть ли ставки на спорт: Massachusetts population surveys with PGSI severity groups; the abstract doesn't say whether sports betting participation was measured or reported, so full text is needed.)

**Решение:** ?

---

### 682 · R3632

**Basic psychological needs in gambling and gaming problems**

2022 · Addictive Behaviors Reports · article · en · https://doi.org/10.1016/j.abrep.2022.100445

Background and Aims: Studies on self-determination theory (SDT) have placed satisfaction of basic psychological needs (autonomy, relatedness, and competence) at the core of well-being, whereas frustration of these needs results in multiple potentially unhealthy mental and behavioral patterns. This study analyzed how need satisfaction and frustration relate to the severity of gambling and gaming problems. Methods: = 1530; 50.33% male) was conducted in April 2021. Basic psychological needs were measured with the Basic Psychological Need Satisfaction and Frustration Scale, mental health issues with the five-item Mental Health Inventory, gambling problems with the Problem Gambling Severity Index, and gaming problems with the Internet Gaming Disorder Test. Zero-inflated negative binomial analyses were conducted to examine how satisfaction and frustration of basic psychological needs, together with mental health issues, are associated with gaming and gambling problems. Results: Mental health issues were associated with gambling and gaming problems, but this association became nonsignificant when basic psychological needs were added to the model. However, better mental health still was associated with the absence of gaming problems. While need satisfaction had no association with the absence of gaming or gambling problems, need frustration was associated with increases in the severity of both gaming and gambling problems. Discussion: Frustration of basic psychological needs for autonomy, relatedness, and competence is associated with both gambling and gaming problems and should be considered when developing treatment and support for those who experience such problems.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Population sample (N=1530) using PGSI; abstract doesn't say whether sports betting participation was measured.

**Решение:** =

---

### 683 · R3634

**Is the economic model of gambling dependent on problem gambling? Evidence from an online survey of regular sports bettors in Britain**

2022 · International Gambling Studies · article, review, journal-article · en · https://doi.org/10.1080/14459795.2022.2088823

ABSTRACT Understanding how the gambling industry generates revenue is of paramount importance. Questions about whether higher volumes of expenditure are concentrated among a small proportion of gamblers, and how this varies by problematic gambling status, underpin policy debate about consumer protection. Analyzing data from two timepoints (T0; T2) from a British longitudinal study of regular sports bettors, we explored both for total (gross) spend and gross spend on individual activities: (a) the concentration of self-reported spend on gambling among individuals; and (b) the extent to which spending was disproportionately generated by those with elevated Problem Gambling Severity Index (PGSI) scores. Results showed that gross gambling expenditure was unequal (GINI-coefficient >0.70 for most activities). At both timepoints, those with a PGSI score of 3+ had an elevated share of spending: at T2, 14.1% of PGSI 3+ gamblers accounted for 43.5% of gross gambling spend. There were differences by activity: lotteries displayed less reliance on those with a PGSI score of 3+ whereas this group contributed over 80% of gross spend on online casinos. Policy attention should focus on reframing the underlying economic model on which some gambling activities are predicated, creating more equal patterns of consumption and less reliance on those harmed.

**ИИ:** + · обе модели · беттеры + инструмент · Survey of regular sports bettors in Britain that used the PGSI and reports PGSI 3+ proportions.

**Решение:** =

---

### 684 · R3635

**The association between gambling marketing and unplanned gambling spend: Synthesised findings from two online cross-sectional surveys.**

2022 · Addictive behaviors · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1016/j.addbeh.2022.107440

Background In 2020, the British Government initiated a review about whether to introduce stricter controls on gambling marketing. We examine: (i) what proportion of regular sports bettors and emergent adult gamblers report that marketing has prompted unplanned spend; and (ii) what factors are associated with reporting that marketing had prompted unplanned spend. Methods Data are from two British non-probability online surveys with: (i) emerging adults (16-24 years; n = 3,549; July/August 2019) and (ii) regular sports bettors (18+; n = 3,195; November 2020). Among current gamblers, logistic regressions examined whether reporting that gambling marketing had prompted unplanned spend (vs never) was associated with past-month marketing awareness, past-month receipt of direct marketing (e.g., e-mails), following gambling brands on social media, and problem gambling classification. Results Almost a third of current gamblers reported that marketing had prompted unplanned gambling spend (sports bettors: 31.2 %; emerging adults: 29.5 %). Escalated severity of problem gambling was associated with reporting that marketing had prompted unplanned spend in both samples, in particular those experiencing gambling problems compared to those experiencing no problems (sports bettors: OR Adj = 17.01, 95 % CI: 10.61-27.27; emerging adults: OR Adj = 11.67, 95 % CI: 6.43-21.12). Receipt of least one form of direct marketing in the past month and following a gambling brand on at least one social media platform was also associated unplanned spend among sports bettors and emerging adults. Conclusion Among emerging adults and regular sports bettors, increased severity of gambling problems, receiving direct marketing, and following gambling brands on social media are associated with reporting that marketing has prompted unplanned spend.

**ИИ:** + · обе модели · беттеры + инструмент · Survey of regular sports bettors (n=3,195) with problem gambling classification (likely PGSI); full text should show PG prevalence.

**Решение:** =

---

### 685 · R3642

**Indigenous Gambling and Problem Gambling in Canada.**

2022 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-021-10022-5

The present study provides a profile of Canadian Indigenous gambling and problem gambling using the 2018 Canadian Community Health Survey (CCHS) (n = 23,952 adults; 1,324 Indigenous) and an online panel survey of 10,199 gamblers (n = 589 Indigenous). The relative popularity of different types of gambling was similar between Indigenous and non-Indigenous samples. However, there was higher Indigenous participation in electronic gambling machines (EGMs), bingo, instant lotteries, overall gambling and a higher rate of problem gambling (2.0% versus 0.5%). Variables predictive of Indigenous problem gambling were EGM participation, gambling fallacies, having a mental or substance use disorder, sports betting, and male gender. Compared to non-Indigenous problem gamblers, Indigenous problem gamblers had higher substance use and lower impulsivity. In general, variables predictive of Indigenous problem gambling were the same ones predictive of problem gambling in all populations, with elevated Indigenous problem gambling rates primarily being due to elevated rates of these generic risk factors. Many of these risk factors are modifiable. Particular consideration should be given to reducing the disproportionate concentration of EGMs in geographic areas having the highest concentration of Indigenous people and ameliorating the disadvantageous social conditions in this population that are conducive to mental health and substance use problems.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Population and gambler surveys measured gambling types (including sports betting) and problem gambling (PGSI), and sports betting predicted problem gambling.

**Решение:** =

---

### 686 · R3643

**Associations between playing free-to-play sports gambling predictor games and online sports betting frequency for men in the United Kingdom**

2022 · Journal of Public Health · article, review, journal-article · en · https://doi.org/10.1007/s10389-022-01774-4

Abstract Aim This study aimed to describe associations between playing predictor games and online sports betting behaviours, and problem gambling. Methods An online survey using a convenience sample was completed by males aged 18 + years, living in the United Kingdom, and having participated in any gambling activity in the past year (n = 384). The survey asked questions about sociodemographics, gambling behaviours and predictor game playing behaviours. The Problem Gambling Severity Index (PGSI) tool was used to determine existence of at-risk and problem gambling. Bivariate analyses using X 2 , and multivariate analyses using binary logistic regressions were carried out. Results Predictor games were played by 45.8% of all participants. In bivariate analyses, there was an association between predictor game playing and age ( p = 0.019), with predictor game playing most prevalent in the age group 18–24 years 51.8%. In bivariate analysis, there was a significant graded relationship between playing predictor games and PGSI group ( p &lt; 0.001), with predictor game playing most prevalent among those with problem gambling 76.9%. In multivariate analysis, after controlling for sociodemographics and PGSI group, those who played predictor games were 2.80 (1.65–4.74 p &lt; 0.001) times more likely to engage in high frequency online sports gambling than those who did not play predictor games. Conclusions This study suggests there may be links between playing predictor games and gambling harms through increased frequency of online sports gambling, particularly amongst already vulnerable groups. Policy options placing restrictions on the most harmful inducements – one of which being predictor games – must be considered to protect against gambling harms.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Survey of UK male gamblers measured online sports betting frequency and PGSI; problem gambling among sports bettors could likely be extracted.

**Решение:** =

---

### 687 · R3655

**Sports betting and COVID-19**

2022 · Edward Elgar Publishing eBooks · part of book or chapter of book, book-chapter · en · https://doi.org/10.4337/9781802207576.00043

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Book chapter with no abstract; could be an empirical survey of sports bettors or an economic/review chapter.

**Решение:** =

---

### 688 · R3660

**Factores socioeconómicos y administrativos en la actividad de las casas de apuestas deportivas en el distrito del Callao 2021**

2022 · Universidad César Vallejo · master thesis · spa · https://hdl.handle.net/20.500.12692/81815

El presente trabajo de investigación tiene como objetivo determinar los factores socioeconómicos y su influencia en la actividad de las casas de apuestas deportivas que están muy de moda en este último quinquenio a lo largo y ancho del territorio nacional. Actualmente en Perú no existe un marco normativo que regule la actividad de los juegos y apuestas deportivas sean estas a distancia utilizando el internet o en casas de apuestas o locales de juego (retail). La característica principal de este tipo de negocio son las apuestas y cómo estas son percibidas desde tres puntos de vista distintos: a) el empresario (económico), b) el apostador (social) y c) el estado (socioeconómico). A diferencia de los dos primeros, empresario y apostador, el estado es un mero espectador, al no tener un marco legal como lo tienen países como Colombia, Argentina y Chile en América Latina o España, Inglaterra y Croacia en Europa entre otros, donde la regulación de esta actividad genera bastantes ingresos en impuestos a sus respectivos fiscos. Es por ello que para analizar esta problemática se necesita conocer un poco de la historia del juego a nivel mundial y cómo, con el transcurrir de los años, se ha ido desarrollando en los países que hoy en día han logrado direccionar esta actividad para el beneficio económico de su territorio sin perjudicar a los sectores vulnerables de su sociedad. Estos mismos factores diferenciadores de la realidad de los juegos de azar en el Perú, generó un inicial interés en conocer las implicancias que el juego puede llegar a tener en una sociedad tan diversa como la nuestra, y nos impele a saber cómo llegar a velar por la seguridad de las personas más vulnerables, realizando para ello, una investigación de campo, mediante entrevistas y encuestas a los asistentes a estas casas de apuestas (apostadores) y a los operadores de las mismas (empresarios). Promoción de la salud, nutrición y salud alimentaria Biodiversidad, cambio climático y calidad ambiental Reforma y Modernización del Estado Maestría en Gestión Pública Fin de la pobreza Callao

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Thesis surveying sports betting shop customers in Callao, Peru; the abstract doesn't say whether a problem-gambling instrument was used.

**Решение:** =

---

### 689 · R3668

**SPORTS BETTING IN MODERN SOCIO-CULTURAL SPACE**

2022 · THE KAZAN SOCIALLY-HUMANITARIAN BULLETIN · article, journal-article · en · https://doi.org/10.26907/2079-5912.2022.6.86-91

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; sociocultural sports betting title is probably theoretical, but it may report survey data.

**Решение:** =

---

### 690 · R3671

**Factores de riesgo en juego patológico en la población joven del Gran Bilbao**

2021 · bachelor thesis · spa · https://hdl.handle.net/10810/74738

En el presente informe, se analizan los factores de riesgo en torno al juego patológico de la población joven, en concreto de una muestra de jóvenes de entre 18 y 24 años de habitantes en el Gran Bilbao. Los juegos de azar están volviéndose una actividad cada vez más integrada en el ocio de las personas jóvenes en general, ayudada por un aumento de locales en los que se ofertan diferentes modalidades de juego, que han pasado a ser puntos de encuentro fomentando el consumo de juegos de azar y/o apuestas deportivas. La importancia de la prevención y del desarrollo de la investigación en esta área va a ser determinante para el futuro de nuestra población joven. La información basada en la evidencia les va a aportar herramientas para hacerles frente y reaccionar a tiempo. [73] p. -- Bibliogr.: p. 56-60

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Bachelor thesis studying a sample of young adults in Bilbao and mentioning sports betting; unclear whether a problem-gambling instrument was used.

**Решение:** =

---

### 691 · R3673

**Gambling in Uganda: Are Large Expenses and Financial Constraints Driving the Popularity of Sports Betting?**

2021

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the title suggests a study of sports betting in Uganda that might have measured problem gambling.

**Решение:** =

---

### 692 · R3693

**Propuesta Del Plan De Acción Tutorial Para Contrarrestar Los Factores De Riesgo Asociado A La Participación De Los Adolescentes En Las Apuestas Deportivas**

2021 · master thesis · und · http://hdl.handle.net/10553/102064

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Master thesis on adolescent sports betting risk factors with no abstract; it may include a diagnostic survey using a problem-gambling screen.

**Решение:** =

---

### 693 · R3694

**Current addiction in youth: online sports betting**

2021 · Hispana · article · en · https://doi.org/10.3389/fpsyt.2020.590554/full

The authors thank Dr. Carlos Garcia Forero, from the Faculty of Medicine and Health Sciences, Universitat Internacional de Catalunya, Barcelona, Spain, for his advice in the Statistical Analysis.

**ИИ:** ? · обе модели · нет аннотации · Abstract is only an acknowledgment; the title suggests an empirical study of young online sports bettors, possibly measuring addiction.

**Решение:** =

---

### 694 · R3716

**Public Perceptions of Harm for Nine Popular Gambling Products.**

2021 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-021-10014-5

Gambling causes significant levels of harm globally and is recognised as a serious public health issue. To reduce gambling-related harm, various strategies and policies have been recommended, including decreasing the availability of gambling products, restricting gambling advertising, and implementing public education campaigns. Government willingness to implement such strategies will be influenced by levels of public support, which in turn will be dependent on public perceptions of the harm caused by gambling products. The aim of the present study was to assess public perceptions of the harm associated with individual gambling products to inform future gambling reform. A sample of 2112 Australian adults provided perceived harm ratings for nine popular gambling products that are known to be associated with gambling-related harm: electronic gambling machines, casino table games, sports betting, bingo, scratch tickets, private betting, horse/dog races, keno, and the lottery. Binary logistic regressions were used to identify factors associated with harm perceptions. Only electronic gambling machines (70%), casino table games (64%), betting on horse/dog races (59%), and sports betting (53%) were perceived by a majority of respondents as being harmful. Less frequent gambling and experiencing greater levels of gambling-related harm were associated with higher harm perceptions. Many potentially harmful gambling products may not be recognised as such by the public, which is likely to reduce support for recommended harm-reduction strategies and policies. Efforts are needed to ensure Australians in general and gamblers in particular understand the levels of harm associated with popular gambling products.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Australian adult survey that measured gambling harm and likely product participation; unclear whether PGSI or another instrument was used for sports bettors.

**Решение:** =

---

### 695 · R3728

**The Gambling Consumption Mediation Model (GCMM): A Multiple Mediation Approach to Estimate the Association of Particular Game Types with Problem Gambling.**

2021 · Journal of gambling studies · journal article, journalarticle, review · eng · https://doi.org/10.1007/s10899-020-09928-3

Abstract Bivariate associations of problem gambling with participation in particular game types often decrease when adjusting for demographics or consumption behavior (e.g., number of game types played). A summary of 14 peer-reviewed studies showed inconsistencies as well as conceptual and methodological challenges. The aim of this study was to expand previous research by a combination of (1) sophisticated feature-engineering, which disaggregates gambling intensity into facets within and beyond a game type of interest, and (2) the application of mediation models. Data comprised last year gamblers of three merged cross sectional Icelandic gambling surveys of 2007, 2011, and 2017 (N = 4422). For each of 15 game types (12-month time frame), a parallel multiple mediation model was applied to disaggregate bivariate associations of last year game type participation and problem gambling (Problem Gambling Severity Index) by six mediating mechanisms: (1) demographic problem gambling propensity, (2) number of game types played, (3) gambling frequency within the type, (4) maximum gambling frequency across all types beyond, (5) usual spending within the type, (6) maximum usual spending across all types beyond. Games showed two distinct profiles via which mediator they mostly impacted problem gambling: Electronic gaming machines offline, scratch cards offline, live betting online, and poker offline as well as online impacted problem gambling mostly via gambling frequency within , whereas all other types mostly impacted via the number of game types played . The applied mediation models answer the question by which mechanism game types impact problem gambling in a more exhaustive way than previous research.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Icelandic gambling surveys with PGSI measured across 15 game types, including online live betting, so sports bettors' problem gambling may be reported.

**Решение:** =

---

### 696 · R3736

**CONSUMER BEHAVIOUR ANALYSIS IN THE SPORTS BETTING MARKET**

2021 · Bulletin of the Transilvania University of Brasov Series V Economic Sciences · article, journal-article · en · https://doi.org/10.31926/but.es.2021.14.63.1.1

This paper aims to evaluate the sociological and economic implications that the sports betting industry has over the consumers financial resources and on the psyche of the consumers. The aim of the research is to gather information about the sports bettor’s behaviour, motivations, expectations, his decision-making process, the factors that influence his choices, their perspective about skill and chance and the overall management of the betting activity.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Likely a survey of sports bettors on behaviour and psychological effects; the abstract does not say whether a problem-gambling instrument was used.

**Решение:** =

---

### 697 · R3738

**Risk and protective factors for the development of gambling-related harms and problems among Australian sexual minority men.**

2021 · BMC psychology · article, other literature type, collection/collection · eng · https://doi.org/10.1186/s40359-021-00597-4

Abstract Background Sexual minority men (SMM) often experience stressful social environments dominated by stigma and discrimination. SMM are typically more likely than heterosexual men to engage in certain risky behaviours such as problem gambling. This study aimed to compare gambling behaviour among SMM and examine potential risk factors (erroneous gambling cognitions, gambling outcome expectancies, hazardous alcohol use, impulsivity, and psychological distress; as well as perceived stigma and discrimination for the SMM participants) and potential protective factors (resilience, social support, and community connectedness) for problem gambling severity and gambling-related harms among SMM living in Australia. Methods An online survey, with an over-representation of SMM participants and problem, moderate-risk, and low-risk gamblers, was completed by 101 SMM (mean age = 28.5) and 207 heterosexual men (mean age = 26.4). Results SMM were found to have significantly lower levels of problem gambling severity compared with heterosexual men, and report significantly lower gambling participation, frequencies and expenditure on any gambling activity, casino table games, horse racing/greyhound betting, sports betting, and keno. However, in the SMM group, 38.3% were classified in the problem gambling category of the Problem Gambling Severity Index and 27.6% were classified in the moderate-risk gambling category. There were no significant differences between groups in gambling-related harms. Multiple regression analyses revealed that problem gambling severity and related harms were independently predicted by higher levels of impulsivity and erroneous gambling cognitions for both groups. Conclusions Lower frequency of gambling behaviours among SMM and similar risk factors predicting problem gambling severity/harms for both groups suggests that problem gambling is not pronounced among SMM. This study adds new evidence to the gambling literature which can be used as comparative benchmarks for future research.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Online survey of men measuring sports betting participation and PGSI; problem gamblers were oversampled, which should be checked at full text.

**Решение:** =

---

### 698 · R3741

**Impact of Warning Pop-Up Messages on the Gambling Behavior, Craving, and Cognitions of Online Gamblers: A Randomized Controlled Trial.**

2021 · Frontiers in psychiatry · article, journal article, journalarticle · eng · https://doi.org/10.3389/fpsyt.2021.711431

Background: Many features of Internet gambling may impact problem severity, particularly for vulnerable populations (availability, anonymity, a convenience and ease of play, digital forms of payment, and a higher level of immersion). To prevent the risks associated with excessive gambling and to inform gamblers, we need responsible gambling strategies. Gambling-related warning messages are one possible strategy that can help minimizing gambling-related harm. Methods: Our experimental study aimed to evaluate the effectiveness of self-appraisal and informative pop-up messages compared to a control condition (blank pop-up messages), for both at-risk (ARG) and low risk/non-problem Internet gamblers (LR/NPG) according to their favorite type of game, in a semi naturalistic setting and with a 15-day follow-up. During the experimental session, participants were invited to gamble on their favorite website with their own money in the laboratory. Effectiveness was investigated through the impact of pop-ups on gambling behavior (money wagered and time spent), craving, cognitive distortions, and gambling experience, taking into account message recall. We analyzed data from 58 participants, playing preferentially either to skill and chance bank games (sports betting, horse race betting) and skill and chance social games (poker). Results: We observed a significant decrease in the illusion of control for ARG in the informative pop-up condition at the 15-day follow-up. A significant effect of self-appraisal pop-ups compared to blank pop-up messages was also demonstrated only for sport and horse bettors, with a decrease on time spent gambling and an increase of gambling-related expectancies at the follow-up. Finally, we also observed that a majority of the participants were disturbed and irritated by pop-ups during their gambling session. Conclusions: The results of our study demonstrated the limited impact of pop-up warning messages on gambling behavior and cognition in Internet gamblers according to the type of game and the status of gamblers. The limited impact of warning messages on gambling behavior and the inconvenience of the pop-ups for Internet gamblers lead us to only consider warning messages as one piece of a larger responsible gambling strategy. Trial Registration Number: NCT01789580 on February 12, 2013.

**ИИ:** разошлись — Opus + (игроки, есть ставки на спорт и инструмент: Online gamblers sorted into at-risk vs low-risk groups (probably by a screening tool) and by favourite game, including sports/horse bettors; at-risk counts per group likely available.); Sonnet ? (неясно, измеряли ли проблемную игру: RCT of online gamblers incl. sports bettors, split into at-risk vs low-risk by a screen; counts by game type might be reported, but the sample was selected by risk status.)

**Решение:** ?

---

### 699 · R3742

**Essays on Self-Employment, Income Taxation, Non-Compete Agreements, and Sports Betting**

2021 · dissertation · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Economics dissertation with a sports betting essay and no abstract; it is unclear whether bettors were surveyed with a problem-gambling instrument.

**Решение:** =

---

### 700 · R3755

**Changes in Self-Reported Web-Based Gambling Activity During the COVID-19 Pandemic: Cross-sectional Study.**

2021 · JMIR serious games · journal article, journalarticle, review · eng · https://doi.org/10.2196/30747

BACKGROUND: The COVID‑19 pandemic has affected not only somatic health with over 3.7 million deaths worldwide, but also has had a huge impact on psychological health, creating what amounts to a mental health crisis. The negative effect of the pandemic on traditional addictions is well described and concerning, and the same has been seen for gambling. OBJECTIVE: This study explores self-reported web-based gambling behavior during the COVID‑19 pandemic in Sweden. We investigated overall changes, but also changes in specific web-based gambling types, and whether they are associated with certain risk factors or lifestyle changes. METHODS: Our study is based on an anonymous web-based survey of web panel participants in Sweden (N=1501) designed to study a range of behavioral changes during the COVID‑19 pandemic. Increases in gambling were analyzed using logistic regression models against sociodemographic data and psychological distress. RESULTS: The majority of the respondents who gambled reported no changes in their gambling habits during the COVID‑19 pandemic. We found significant associations with the problem gambling severity index (PGSI), the Kessler score (indicating psychological distress), employment status, changes in alcohol habits, and self-exclusion when looking at overall changes in gambling activity in the pandemic. In the subgroup that reported an increase in gambling activity, we found an association with both the PGSI and Kessler scores. The PGSI score was also an independent predictor for all specific web-based gambling (horses, sports, poker, and casino) whereas the Kessler score only had a significant impact on changes in casino gambling. In addition, male gender was an independent predictor for gambling on sports and casino gambling. CONCLUSIONS: The majority of respondents who gambled reported no changes in their gambling activity during the COVID‑19 pandemic. The group that reported an increase in overall gambling activity during the COVID-19 pandemic represent a group with gambling problems and psychological distress. The group that reported increased sports and casino gambling were often male, and this group seemed to experience more psychological distress.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Swedish web-panel survey that measured PGSI and web-based sports gambling; it could report problem gambling among sports bettors.

**Решение:** =

---

### 701 · R3770

**Gambler’s expectations and regret :Online sports betting in the case of the 18 -30 year olds**

2021 · conference object · eng · https://hal.science/hal-05077778v1

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Conference paper on online sports bettors aged 18-30 with no abstract; it may have used a problem-gambling measure.

**Решение:** =

---

### 702 · R3771

**Cryptocurrency trading, gambling and problem gambling.**

2021 · Addictive behaviors · article, journal article, journalarticle · eng · https://doi.org/10.1016/j.addbeh.2021.107021

Some forms of speculative trading share similarities with gambling. Decisions are often based on limited information, short-term motives for gain, and highly volatile and uncertain outcomes. Given these similarities, there is evidence to show that people who are attracted to gambling are also statistically more likely to engage in higher risk speculation such as day-trading of stocks and crypto-currency trading. In this study, involving 543 people (M = 388, F = 155, 85% aged 18-40 years) who reported at least monthly sports-betting, crypto-currency trading or both, we examined whether gambling and problem gambling were reliable predictors of the reported intensity of crypto-currency trading. The results showed that gambling and problem gambling rates were highest among those who reported both activities and that problem gambling scores (PGSI) and engaging in stock trading was significantly related to measures of crypto-currency trading intensity as based on the time spent per day, number of trades and level of expenditure. Future research should examine whether gambling history and involvement influences how people manage their investments in crypto-currencies, including their propensity for making riskier decisions and experiencing more negative outcomes.

**ИИ:** + · обе модели · беттеры + инструмент · This is a survey of monthly sports bettors and crypto traders that used the PGSI, and it reports problem gambling rates by group.

**Решение:** =

---

### 703 · R3775

**Sports Bets and Instant Regrets**

2021 · figshare · audiovisual/presentation, presentation, presentation/presentation · und · https://doi.org/10.6084/m9.figshare.16867210

Sports Bets and Instant Regrets, the effects of sports betting.

**ИИ:** ? · обе модели · нет аннотации · Figshare presentation on the effects of sports betting; the minimal abstract doesn't say whether it's empirical or whether problem gambling was measured.

**Решение:** =

---

### 704 · R3776

**Proyecto de intervención. Prevención de la ludopatía (apuestas deportivas) en el barrio de Tamaraceite**

2021 · bachelor thesis · und · http://hdl.handle.net/10553/86868

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: Bachelor thesis on sports-betting addiction prevention; likely a proposal, but could include a local needs-assessment survey.); Sonnet -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: Bachelor thesis designing a prevention intervention project for sports-betting gambling in a neighborhood; no abstract, likely a program proposal without prevalence data.)

**Решение:** ?

---

### 705 · R3777

**Short-Term Effectiveness of the Youth Gambling Prevention Program "Who Really Wins?"-Results from the First National Implementation.**

2021 · International journal of environmental research and public health · article, journal article, journalarticle · eng · https://doi.org/10.3390/ijerph181910100

As a response to significant adolescent gambling involvement, a Croatian team of researchers and practitioners developed a universal, comprehensive, evidence-based youth gambling prevention program called "Who Really Wins?". This study presents the results on its short-term effectiveness following the first national implementation in 18 Croatian cities, with a total of 629 high school students (66.5% male) who completed the program. A design with two measurement sessions (pre-test and post-test) was used to explore the short-term effects of the program on gambling-related knowledge and cognition, frequency of gambling, and various socio-emotional skills. The results showed significant effects when it comes to knowledge, cognitive distortions, and the frequency of sports betting and playing lottery games. Furthermore, the program had no harmful effects on any of the measured variables. The results are interpreted in terms of methodological challenges in measuring effects, possible improvements of the program, and implications for future evaluation research.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Adolescent prevention evaluation measured sports betting frequency; unclear whether a problem-gambling screen (e.g., SOGS-RA/CAGI) was administered.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Prevention program evaluation in students; measured knowledge, cognitive distortions, gambling frequency and skills, with no problem-gambling instrument mentioned.)

**Решение:** ?

---

### 706 · R3779

**The identification of Australian low-risk gambling limits: A comparison of gambling-related harm measures.**

2021 · Journal of behavioral addictions · comparative study, journal article · eng · https://doi.org/10.1556/2006.2021.00012

Problem gambling severity and gambling-related harm are closely coupled, but conceptually distinct, constructs. The primary aim was to compare low-risk gambling limits when gambling-related harm was defined using the negative consequence items of the Problem Gambling Severity Index (PGSI-Harm) and the Short Gambling Harms Scale items (SGHS-Harm). A secondary aim was compare low-risk limits derived using a definition of harm in which at least two harms across different domains (e.g. financial and relationship) were endorsed with a definition of harm in which at least two harms from any domain were endorsed. Data were collected from dual-frame computer-assisted telephone interviews of 5,000 respondents in the fourth Social and Economic Impact Study (SEIS) of Gambling in Tasmania. Receiver operating characteristic (ROC) curve analyse were conducted to identify low-risk gambling limits. PGSI-Harm and SGHS-Harm definitions produced similar overall limits: 30-37 times per year; AUD$510-$544 per year; expenditure comprising no more than 10.2-10.3% of gross personal income; 400-454 minutes per year; and 2 types of gambling activities per year. Acceptable limits (AUC ≥0.70) were identified for horse/dog racing, keno, and sports/other betting using the PGSI definition; and electronic gaming machines, keno, and bingo using the SGHS definition. The requirement that gamblers endorse two or more harms across different domains had a relatively negligible effect. Although replications using alternative measures of harm are required, previous PGSI-based limits appear to be robust thresholds that have considerable potential utility in the prevention of gambling-related harm.

**ИИ:** + · обе модели · опрос населения об азартных играх · Tasmanian population survey (n=5,000) using PGSI with activity-specific analyses including sports/other betting.

**Решение:** =

---

### 707 · R3782

**A comparative analysis of sports gambling in the United States**

2021 · International Journal of Sports Marketing and Sponsorship · article, journal-article · en · https://doi.org/10.1108/ijsms-03-2021-0074

Purpose The purpose of the study was to explore differences in demographic, self-concept and fan behavior factors that predict sports fans who bet and those who do not in legal and illegal gambling jurisdictions in the United States (US). Design/methodology/approach Seven hundred and eighty-nine sports fans and bettors from 47 states were surveyed through a partnership with a major media provider in the US. A number of demographic items, theoretically defined factors and fan behaviors were measured, and several two-way MANOVAs with interaction effects were conducted to determine differences between those who gamble and those who do not in legal and illegal jurisdictions. Findings Statistically significant differences between those who bet and those who do not were found. Bettors look different and come from different backgrounds and locations. Psychographically, they were clearly more narcissistic. They also indicated a higher social identity and self-worth, yet perceived themselves as less worthy members of important social institutions. In general, sports bettors out consumed non-bettors as it relates sports spectatorship. In terms of differences between the groups across legal and illegal states, only a few factors were impacted. Self-worth and personal identity were factors that were found to be different between groups and jurisdictions as well as DFS participation. Originality/value The US sports gambling market is expected to grow US$6.5 billion in the next five years, yet very little is known, psychographically, about the US sports bettor. Sports gambling research, especially from a marketing perspective, has primarily been limited to Australia and the United Kingdom. This paper contributes to what we know about sports gambling and the emerging US market. In particular, the results uncovered fundamental trait, demographic and behavioral differences between US sports fans and sports bettors. The findings also provide similar foundational differences and similarities between those who bet in states with legal and illegal gambling.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of US sports bettors vs non-bettors (marketing focus); abstract doesn't say whether a problem-gambling instrument was used.

**Решение:** =

---

### 708 · R3792

**What drives sports betting?**

2021 · AEA Randomized Controlled Trials · dataset · en · https://doi.org/10.1257/rct.8447-1.0

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · AEA RCT registry entry on sports betting with no abstract; possibly an experiment with bettors, unclear whether problem gambling was measured.

**Решение:** =

---

### 709 · R3800

**Ocio y juego online: Las apuestas deportivas**

2021 · Dialnet (Universidad de la Rioja) · article · es

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; Spanish article on online leisure and sports betting could be an empirical survey or a commentary.

**Решение:** =

---

### 710 · R3803

**Impacts of the COVID-19 Shutdown on Gambling Patterns in Australia: Consideration of Problem Gambling and Psychological Distress.**

2021 · Journal of addiction medicine · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1097/adm.0000000000000793

Supplemental Digital Content is available in the text Objectives: The COVID-19 pandemic reduced access to gambling and contributed to widespread psychological distress. Psychological distress is a known risk factor for problem gambling as it can motivate excessive gambling as a coping response. The availability of gambling is considered a factor in maintaining problems. This paper aimed to investigate the impact of the shutdown of gambling venues on Australians, particularly among those vulnerable to mental health problems and gambling disorder. Methods: Australian adults who had gambled at least once in the past 12 months (N = 764, 85.2% male) completed an online cross-sectional survey. Self-report measures retrospectively assessed typical monthly gambling frequency and expenditure before and after the COVID-19 venue shutdown, problem gambling, and psychological distress. Results: Significant median decreases in gambling frequency were observed, both online and overall. No relationship was found between psychological distress and baseline or increases in gambling. Greater problem gambling severity was related to higher baseline gambling, but not to increases in gambling. Exploratory analysis showed that individuals engaged in moderate-risk gambling, but not problem gambling, were more likely to report increased gambling frequency compared to nonproblem and low-risk gamblers combined. Conclusions: Findings provide important insights into how changes in availability influence gambling participation, and for understanding the effectiveness of forced restrictions and venue exclusion strategies. Most people moderated their gambling when venue-based gambling was unavailable and opportunities for sports betting were limited. However, harms experienced by individuals with some gambling problems may have been exacerbated during the period of limited access. Policies to enhance prevention and treatment of gambling problems are necessary even when availability is reduced.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Survey of Australian gamblers (85% male) that measured PGSI-type problem gambling; sports betting is mentioned, so activity breakdown is likely.

**Решение:** =

---

### 711 · R3806

**Las casas de apuestas deportivas on line: los motivos de uso y perfil del usuario grancanario en el año 2020.**

2021 · bachelor thesis · und · http://hdl.handle.net/10553/103207

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Bachelor thesis on Gran Canaria online sports bettors' motives and profile; no abstract, so problem-gambling measurement unknown.

**Решение:** =

---

### 712 · R3807

**Examining the effects of online sports betting on the perceived economic wellbeing of student-athletes**

2021 · International Journal of Research in Business and Social Science (2147-4478) · article, journal-article · en · https://doi.org/10.20525/ijrbs.v10i7.1435

The aim of the study was to investigate the effects of online sports betting on the perceived economic wellbeing of student-athletes using the regression analysis with an interaction effect used to test the effect of demographic variables on the relationship between dependent and independent variables. Correlation analysis was used to test the relationship between independent variables. The findings reveal that there was a positive and significant association3 between gambling severity and economic wellbeing. The study revealed that students’ sports bet online with large amounts of money to get the feeling of excitement. Sports betting leads to overspending which can disrupt home life to such an extent that it has some social effects such as the break-up of families. Sometimes due to sports betting the only deceptive course of action that seems to remain too often may lead the bettor to commit suicide.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Quantitative survey of student-athletes who bet on sports online; 'gambling severity' was measured, but the abstract doesn't name the instrument.

**Решение:** =

---

### 713 · R3808

**Investigating the effects of online sports betting on the perceived social wellbeing of student athletes**

2021 · International Journal of Business Ecosystem and Strategy (2687-2293) · article, other literature type, review · en · https://doi.org/10.36096/ijbes.v3i2.259

This study investigates the effects of online sports betting on the perceived social wellbeing of student-athletes using a cross-sectional survey methodology with a sample of 38 universities. Findings of the study demonstrate that (i) there was a positive and significant association between gambling severity and social wellbeing, (ii) gambling severity and social wellbeing of students are positively and significantly related, (iii) demographic factors have a significant interaction effect on gambling severity and social wellbeing relationship. This paper also exhibited that gamblers were disappointed after online sports betting efforts and that fatigue and sleep disturbances were common after a loss or victory on online sports betting. Problem gamblers should be introduced to treatment or rehabilitation programmes that will help them to overcome their addiction to online sports betting.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Survey of student-athletes who bet on sports online; it measures 'gambling severity', but the abstract doesn't name the screening instrument.); Sonnet + (беттеры + инструмент: Cross-sectional survey of student athletes on online sports betting measuring gambling severity; likely reports problem gambling levels among bettors.)

**Решение:** ?

---

### 714 · R3809

**Sports Betting Participation and its Effects on Youths’ Welfare in Kenya**

2021 · dissertation · en

A Research Project Submitted to the Department of Economic Theory in the School of Economics in Partial Fulfilment of the Requirements for the Award of the Degree of Master of Economics (Policy And Management) of Kenyatta University, June 2021

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Economics thesis on youth sports betting in Kenya; abstract gives no methods, so it's unclear whether a problem-gambling instrument was used.

**Решение:** =

---

### 715 · R3814

**Tipsters and Addiction in Spain. Young People's Perception of Influencers on Online Sports Gambling.**

2021 · International journal of environmental research and public health · article, journal article, journalarticle · eng · https://doi.org/10.3390/ijerph18116152

This research analyzes young people's perception of the presence of tipsters as influencers on online sports gambling and whether their presence can promote addiction to this activity. To achieve this goal, we designed a questionnaire that was administered to young people in public universities in Madrid, being answered by 1032 individuals, out of whom 613 claimed to be regular bettors. We proceeded to the factor analysis of the variables with a high or very high correlation, and results showed that young people perceive a clear relationship between gambling and addiction. An even more enlightening aspect is the result that links tipsters with addiction to online sports gambling; young people's perception correlates both concepts with extraordinary strength. This study's main conclusion makes it clear that there is a huge amount of influence of tipsters on the world of online sports betting, as well as the risk of marrying these two concepts, since young people perceive that either they or others could be initiated into the world of problem gambling.

**ИИ:** разошлись — Opus -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Student survey using a purpose-built perception questionnaire about tipsters and addiction; no problem-gambling screening instrument is evident.); Sonnet ? (неясно, измеряли ли проблемную игру: Survey of 613 regular online sports bettors in Madrid focused on perceptions of tipsters and addiction; the abstract doesn't say whether a problem-gambling instrument was used.)

**Решение:** ?

---

### 716 · R3824

**Winners and Losers: Factors Affecting Daily Fantasy Sports Addiction.**

2021 · Journal of the Association for Information Systems · conference object, journalarticle, article · en · https://aisel.aisnet.org/amcis2021/adopt_diffusion/adopt_diffusion/2

The growing popularity of daily fantasy sports (DFS) services such as DraftKings and FanDuel has created a new medium for sports gambling. With the emergent DFS industry, a growing number of consumers could be classified as being addicted to DFS. Thus, this paper examines the factors leading to DFS addiction. We propose that several factors influence consumer perceived hedonic benefits and utilitarian benefits of DFS that affect their addictive behavior. These features include competition, emotion, escapism, ease of use, cost, financial impact, and social interaction. Based on our proposed research framework, a series of hypotheses are presented. This research is one of the first to examine the factors leading to DFS addiction and could provide early insights for practitioners and academics interested in exploring DFS.

**ИИ:** разошлись — Opus -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: Conference paper proposing a research framework and hypotheses on DFS addiction; no data collection or problem-gambling instrument reported.); Sonnet ? (неясно, измеряли ли проблемную игру: DFS addiction framework with hypotheses; unclear whether a survey with a problem-gambling instrument was run or if the paper is only conceptual.)

**Решение:** -

---

### 717 · R3836

**Comparing football bettors' response to social media marketing differing in bet complexity and account type - An experimental study.**

2021 · Journal of behavioral addictions · article, journal article, journalarticle · eng · https://doi.org/10.1556/2006.2020.00056

Abstract Background and aims The current study aimed to assess how sports bettors respond to advertised bets on social media and whether this differs dependent upon bet complexity and social media account type. Methods Employing a 3 × 2 repeated measures design, 145 regular football bettors were recruited to take part in an online study requiring them to rate bets advertised upon social media, providing indications of their likelihood to bet, confidence in the bet and how much they would stake on the bet. Advertised bets differed in terms of complexity (low, medium and high) and each bet was presented separately on both an operator account and an affiliate account. Results Data analysis highlighted a significant interaction between bet complexity and account type, with bettors rating themselves as being more likely to bet and more confident in bets which were presented on an affiliate account for medium complexity bets but not for low or high complexity bets. Discussion and conclusions This study provides initial evidence that affiliate marketing of sports betting increases bettor's confidence in certain types of bets. This heightens previously addressed concerns around affiliate marketing, given that affiliates are financially incentivised to attract custom toward gambling operators. Future research should explore risk factors for increased uptake of affiliate marketing, and the impact on gambling behaviour.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Online experiment with 145 regular football bettors; such studies often record PGSI as a covariate, but the abstract doesn't mention it.

**Решение:** =

---

### 718 · R3840

**The Effect of Recreational Gambling on Health and Well-Being**

2021 · Eastern Economic Journal · article · en · https://doi.org/10.1057/s41302-020-00181-5

The relationship between gambling and health has important economic and public policy implications. We develop causal evidence on this relationship exploiting regional variation in access to legal gambling. Empirical models treat gambling as an endogenous regressor in explaining variation in health outcomes. Results from instrumental variable and bivariate probit models show recreational gambling has no or a negative impact on the probability of having certain chronic health conditions and a positive impact on life satisfaction. Past research generally found a positive association between problem gambling and adverse health outcomes. The generation of some positive health benefits provides important context for the expansion of legal sports betting in the USA following the repeal of the Professional and Amateur Sports Protection Act in 2018.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Econometric survey analysis of gambling and health; may use population health survey data with CPGI and activity measures, but this is unclear.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Econometric study of recreational gambling and health using regional access as an instrument. It reports no problem-gambling instrument or sports-bettor subgroup, and mentions sports betting only as policy context.)

**Решение:** -

---

### 719 · R3845

**Development and Validation of Sports Betting Addictive Behaviour Scale**

2021 · Global Journal of Human-Social Science · review, article · en

Abstract not found

**ИИ:** ? · обе модели · нет аннотации · New scale developed in sports bettors; no abstract. A full text may show convergent validation against an established problem-gambling instrument.

**Решение:** =

---

### 720 · R3849

**Revenue Associated With Gambling-Related Harm as a Putative Indicator for Social Responsibility: Results From the Swiss Health Survey**

2021 · Journal of Gambling Issues · article, review · en · https://doi.org/10.4309/jgi.2021.48.6

Gambling behaviours represent a significant social and economic cost and an important public health problem. A putative index for monitoring gambling-related harm is a concentration of spending indicator that reports the proportion of gambling revenue derived from problem gambling. Using this indicator, we aimed to provide a first estimate of the proportion of gambling revenue associated with gambling-related harm in Switzerland according to the Swiss Health Survey. Data were obtained from the Swiss Health Survey 2017. The National Opinion Research Centre Diagnostic and Statistical Manual of Mental Disorders – Loss of Control, Lying and Preoccupation (NODS-CLiP) screening tool was used as part of the questionnaire, and the study findings were evaluated to determine the prevalence of gambling-related harm. Self-reported spending on terrestrial and online gambling (including gaming tables, electronic gaming machines, lotteries, sports betting) during the past 12 months was then used to calculate the portion of gambling revenue derived from players experiencing harm. A total of 12,191 respondents were included. Gambling-related harm was reported by 3.10% of our sample, according to NODS-CLiP criteria. The findings showed that although 52% of people experiencing harm spend less than 100 francs per month on gambling, 31.3% of total spending is attributable to gambling-related harm. In addition to pre-existing national prevalence studies, data on spending should be made readily available by gambling operators and regulators, in keeping with their regulatory obligations. The revenue structure, according to gambling type, should also be provided, including data from third-party gambling operators. In an interdisciplinary effort to improve public health and consumer protection, organized national structural prevention measures should be developed and evaluated.

**ИИ:** + · обе модели · опрос населения об азартных играх · Swiss national health survey with NODS-CLiP and spending by gambling type, sports betting included; could report problem gambling among sports bettors.

**Решение:** =

---

### 721 · R3850

**Adolescenti i igre na sreću**

2021 · Paediatria Croatica · article · hrv · https://doi.org/10.13112/pc.2021.13

Sudjelovanje u igrama na sreću (kockanje) zabavna je društvena aktivnost, koja je sve zastupljenija među mladima. Baš povećana popularnost, uz laku dostupnost igrama na sreću, povećava mogućnost pojave problema vezanih za kockanje. Istraživanje je imalo za cilj ispitati učestalost kockanja među učenicima završnih razreda srednjih škola u Slavonskom Brodu, vrste igara na sreću kojima su skloni te njihove stavove o kockanju. U istraživanju je sudjelovalo 163-je učenika završnih razreda srednjih škola na području grada Slavonskog Broda, tijekom travnja i svibnja 2019. godine. Primijenjen je standardizirani upitnik o navikama i procjeni postojanja problema vezanih za kockanje. Bilo kakav oblik kockanja tijekom života navelo je 114-ero (69,9%) učenika. Mladići su češće zastupljeni, dok druga sociodemografska obilježja nemaju utjecaj. Najučestalija igra na sreću su športske kladionice 61 (41,9%), potom Loto listići 46-ero (30,1%) te jednokratne srećke 45-ero (29,8%). Najčešći razlog kockanja je zabava/uzbuđenje 80-ero (58,8%) te zarada 69-ero (50,7%). Uočeno je kako 20-ero (12,2%) učenika ima nisku i srednju razvijenost problema, dok se u njih 17-ero (10,4%) na temelju procjene rizičnog ponašanja uočava visoki stupanj razvijenosti problema vezanih za igre na sreću. Mladići su zastupljeniji u skupini problematičnog kockanja u odnosu na djevojke. Adolescenti u Slavonskom Brodu često sudjeluju u igrama na sreću. Mladići su skloniji kockanju, s većom učestalošću negativnih posljedica kockanja. Problematičnom kockanju ishodiše je u adolescenciji. Nužno je provođenje preventivnih mjera u općoj populaciji te u skupinama adolescenata s naznakom problema vezanih za kockanje radi uklanjanja i ublažavanja negativnih posljedica problematičnog kockanja. Gambling is a fun social activity that is very popular among adolescents. The experience in gambling as entertainment and the increased availability of legalized gambling increase the risk of gambling-related problems. The aim of the study was to investigate the frequency of gambling and types of gambling among secondary school students in Slavonski Brod. The risk-based sociodemographic factors for adolescent gambling were analysed. We recruited 163 final grade students from Slavonski Brod in April and May 2019. A standardized questionnaire on habits and assessment of the existence of gambling problems was used. Any form of gambling was reported by 114 (69.9%) students. Male adolescents predominated, whereas other sociodemographic features had no effect. The most commonly played games were sports betting 61 (41.9%), then lottery tickets 46 (30.1%) and one-offs 45 (29.8%). The most common reason for gambling was fun/excitement 80 (58.8%) and earnings 69 (50.7%). It was observed that 20 (12.2%) students had low or medium problem development, while 17 (10.4%) had high development of gambling problems. Male adolescents had significantly greater severity of gambling-related problems as compared with girls. In conclusion, adolescents from Slavonski Brod often participated in games of chance. Young men were found to be more inclined to gambling, with more frequent adverse consequences of gambling. Problematic gambling has emerged in adolescence. It is necessary to implement preventive measures in the general population and in the groups of adolescents with an indication of gambling problems in order to reduce and mitigate the negative consequences of problem gambling

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Adolescent survey measured sports betting participation and problem gambling severity with a standardized screen (likely CPGI-type categories).

**Решение:** =

---

### 722 · R3853

**Skin in the game - Erroneous beliefs and emotional involvement as correlates of athletes' sports betting behavior and problems.**

2021 · Journal of behavioral addictions · article, journal article, journalarticle · eng · https://doi.org/10.1556/2006.2021.00034

Abstract Background and aims The sports betting market has been growing rapidly over the last years, as have reports of problematic gambling behavior associated with betting. Due to the well-documented gambling problems of famous athletes and the betting supportive nature of many sports-related environments, athletes have been highlighted as a potential group at-risk for problematic sports betting. However, there currently remains a lack of research on individual-level athlete-specific risk-factors or mechanisms that might contribute to the development and perpetuation of betting-related problems. Here, we examine the influence of two potential risk-factors on sports betting behavior and problems: erroneous beliefs and athletes' emotional involvement. Methods 201 athletes with different levels of expertise completed a newly developed scale to assess both factors. Participants were sampled from the general German population, predominantly male (83.08%) and on average 29.52 (SD = 11.05) years old. We use principal components analysis to detect patterns of covariation, potentially due to the proposed underlying latent factors, and regression analyses to test associations of these factors with betting behavior and problems. Results We find that athletes' emotional involvement was strongly associated with betting problems whereas erroneous beliefs were not. However, distorted cognitions/beliefs were associated with higher volumes and more frequent betting activities. Discussion and Conclusions This might contribute to betting problems in the long run. These results highlight athletes' emotional involvement and erroneous beliefs as potential targets for future intervention and prevention efforts.

**ИИ:** + · обе модели · беттеры + инструмент · Survey of 201 German athletes who bet on sports; betting problems were the outcome. The instrument isn't named but is likely a standard screen.

**Решение:** =

---

### 723 · R3868

**Point-of-care testing for HIV and sexually transmitted infections reveals risky behavior among men at gambling centers in Uganda".**

2021 · International journal of STD & AIDS · article, journal article, research support, n.i.h., extramural · eng · https://doi.org/10.1177/09564624211000973

In sub-Saharan Africa (SSA), men are generally difficult to engage in healthcare programs. However, sports gambling centers in SSA can be used as avenues for male engagement in health programs. We offered point-of-care HIV and syphilis testing for men located at five gambling centers in Uganda and assessed HIV risky sexual behavior. Among 507 men, 0.8% were HIV-positive and 3.8% had syphilis. Risky sexual behavior included condomless sex with partner(s) of unknown HIV status (64.9%), having multiple sexual partners (47.8%), engaging in transactional sex (15.5%), and using illicit drugs (9.3%). The majority at 64.5% were nonalcohol consumers, 22.9% were moderate users, and 12.6% had hazardous consumption patterns. In 12 months of follow-up, the incidence rate of syphilis was 0.95 (95% CI: 0.82-1.06) among 178 men. Thus, men in SSA have a high prevalence of syphilis and risky sexual behavior which should be more effectively addressed to reduce the risk of HIV acquisition.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Men recruited at sports betting centres in Uganda; HIV/STI focus, no problem-gambling instrument mentioned in abstract.

**Решение:** =

---

### 724 · R3875

**Postoje a motivace mladých lidí ke kurzovému sázení na sport**

2021 · master thesis · ces/cze · http://www.nusl.cz/ntk/nusl-455074

Title: Attitudes and motivations of young people towards sport betting Objectives: To find out which factors significantly influence sport betting in young Czechs between the age of 18 and 30. Methods: Due to the quantitative nature of the research, the only used method was electronic survey. The survey was based on the theory of planned behaviour. It primarily sought information on independent variables (predictors) within this theory, which are attitudes, subjective norm and perceived control (in connection with sport betting). This part was adopted from a similar previous research. The intention and behaviour of the respondents as response variables were also surveyed in order to describe the relationships between independent and response variables. The sample consisted of 122 respondents, mostly active betters. Statistical methods such as correlation and regression analysis were used, followed by a final path analysis, which provided a model visualizing the relationships between the crucial variables. Results: All of the examined predictors within the theory of planned behaviour influence the intention to bet - the values are 0,241 for attitudes, 0,335 for subjective norm and -0,410 for perceived control. The negative value means that those with higher perceived control have lower intention to...

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Theory-of-planned-behaviour survey of young sports bettors; no problem-gambling instrument mentioned, but the abstract is truncated.

**Решение:** =

---

### 725 · R3876

**Attitudes and motivation towards sport betting in young people**

2021 · Digital Repository (National Repository of Grey Literature) · dissertation · cs

Title: Attitudes and motivations of young people towards sport betting Objectives: To find out which factors significantly influence sport betting in young Czechs between the age of 18 and 30. Methods: Due to the quantitative nature of the research, the only used method was electronic survey. The survey was based on the theory of planned behaviour. It primarily sought information on independent variables (predictors) within this theory, which are attitudes, subjective norm and perceived control (in connection with sport betting). This part was adopted from a similar previous research. The intention and behaviour of the respondents as response variables were also surveyed in order to describe the relationships between independent and response variables. The sample consisted of 122 respondents, mostly active betters. Statistical methods such as correlation and regression analysis were used, followed by a final path analysis, which provided a model visualizing the relationships between the crucial variables. Results: All of the examined predictors within the theory of planned behaviour influence the intention to bet - the values are 0,241 for attitudes, 0,335 for subjective norm and -0,410 for perceived control. The negative value means that those with higher perceived control have lower intention to...

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of young Czech sports bettors built on planned-behaviour constructs; the truncated abstract doesn't say whether a problem-gambling instrument was used.

**Решение:** =

---

### 726 · R3886

**Social disadvantage and gambling severity: a population-based study with register-linkage**

2021 · European Journal of Public Health · article · en · https://doi.org/10.1093/eurpub/ckab162

BACKGROUND: Studies have found an association between problem gambling and poverty. However, there is relatively little research on social inequalities and problem gambling using population representative data. METHODS: A population-representative self-report web-based and postal survey with register-based linkage was conducted in the three geographical areas of Finland. Participants (n = 7186, aged 18 or older) were randomly selected from the population register. Sociodemographic factors and social welfare benefits were studied among gambling groups and their statistical difference were examined by χ2 test. Seven logistic regression models were calculated, where unemployment, social security benefits and low income were treated as dependent variables and where sex, age, family structure and education were controlled as covariates. The results were presented as odds ratios (OR) with 95% confidence intervals (CIs). RESULTS: Problem and at-risk gambling (ARG) was more common among people who were unemployed [PG: χ2=6.4 (1), P < 0.01, ARG: χ2=12.4 (1), P < 0.001] or had received social security benefits [PG: χ2=41.6 (1), P < 0.001, ARG: χ2=22.9 (1), P < 0.001]. The OR for problem gambling was high as 5.6 (CI: 3.22-9.61) among respondents who had received social assistance even when covariates were taking into count. Almost a third of those experiencing problem or at-risk gambling received at least one form of social security benefit. CONCLUSIONS: The most important task of gambling policy should be reducing gambling-related harms and diminishing social inequality. However, even in government organized system where gambling profits are used for common good, profits come from the most socially disadvantaged people thereby exacerbating inequality.

**ИИ:** + · обе модели · опрос населения об азартных играх · Regional Finnish population gambling survey (n=7186) measuring problem gambling; full text may report gambling activities including sports betting.

**Решение:** =

---

### 727 · R3889

**Online Gambling Activity, Pay-to-Win Payments, Motivation to Gamble and Coping Strategies as Predictors of Gambling Disorder Among e-sports Bettors.**

2021 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-021-10015-4

Abstract Research on esports activity usually captures it from the perspective of involvement in gaming. This study presents the results of the first research in Poland ( N = 438) on esports betting (ESB). ESB is compared to other forms of e-gambling and involvement in pay-to-win games. The aim was to build a predictive model of gambling disorder among people betting on esports. A predictive model of gambling disorder based on ordinal regression was built, including sociodemographic variables, involvement in esports betting, involvement in other Internet activities connected to ESB, as well as psychological variables—motivation to gamble and coping strategies. The results showed that gambling disorder among esports bettors is associated with time spent on one game session, placing other forms of online gambling bets once a week or more often, and paying in pay-to-win games. Gambling disorder was also predicted by escape coping strategies and lower engaged strategies as well as financial and coping motivation to bet on esports results. The results show the crucial role of psychological factors (motivation, coping) in the development of esports betting addiction. Esports betting is an activity associated with both gambling and gaming—involvement in both activities explains the development of ESB addiction. There is a need for further research focused on the specificity of esports betting behavior to discover the direction of links among gaming, gambling, and esports gambling.

**ИИ:** + · обе модели · беттеры + инструмент · Survey of 438 Polish esports bettors with gambling disorder as the ordinal outcome, which implies a screening instrument was used.

**Решение:** =

---

### 728 · R3890

**Gambling fallacies: Predicting problem gambling in a national sample.**

2021 · Psychology of Addictive Behaviors · article · en · https://doi.org/10.1037/adb0000673

Collectively, these results show that gambling fallacies have some etiological relationship to problem gambling but are not the main cause of problem gambling and should not be the exclusive focus of problem gambling treatment. (PsycInfo Database Record (c) 2021 APA, all rights reserved).

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · National sample predicting problem gambling (likely PGSI/PPGM); abstract truncated, unclear whether sports betting participation was measured.

**Решение:** =

---

### 729 · R3900

**The impact of COVID-19 lockdown on gambling habit: A cross-sectional study from Italy**

2021 · Journal of Behavioral Addictions · article · en · https://doi.org/10.1556/2006.2021.00033

BACKGROUND AND AIMS: Few preliminary studies have shown an impact of COVID-19 confinement on gambling habits. We aim to evaluate short-term effects of lockdown restrictions on gambling behaviors in Italy. METHODS: Within the project Lost in Italy, a web-based cross-sectional study was conducted on a representative sample of 6,003 Italians aged 18-74 years, enrolled during April 27-May 3 2020, and were asked to report gambling activity before the lockdown and at the time of interview. RESULTS: The prevalence of participants reporting any gambling decreased from 16.3% before lockdown to 9.7% during lockdown. Traditional gambling decreased from 9.9 to 2.4% and online gambling from 9.9 to 8.0%. Among gamblers, median time of gambling grew from 4.5 to 5.1 h/month. Among non-players before lockdown, 1.1% started playing. Among players before lockdown, 19.7% increased gambling activity. Multivariate analysis showed an increase in gambling activity in younger generations (p for trend = 0.001), current smokers (odds ratio, OR 1.48), users of electronic cigarettes (OR 1.63), heated tobacco products (OR 1.82), cannabis (OR 5.16), psychotropic drugs (OR 3.93), and subjects having hazardous alcohol drinking (OR 1.93). Self-reported low quality of life (OR 1.97), low sleep quantity (OR 2.00), depressive symptoms (OR 3.06) and anxiety symptoms (OR 2.93) were significantly related to an increase in total gambling activity during lockdown. DISCUSSION AND CONCLUSIONS: Although gambling substantially decreased during lockdown, time spent in gambling slightly increased. The strong relationship found between compromised mental health and addictive behaviors calls for urgent policies to prevent vulnerable populations from increasing and developing severe gambling addiction.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Representative Italian web survey on gambling activities during lockdown; the abstract doesn't say whether a problem-gambling instrument was used.

**Решение:** =

---

### 730 · R3905

**A Whole New Ball Game: The growing prevalence of video game-related gambling**

2021 · Tampere University · doctoral thesis, other literature type · eng · https://trepo.tuni.fi/handle/10024/135299

Viime vuosikymmenten aikana esiin on noussut kaksi rinnakkaista suuntausta, rahapelikäytäntöjen lisääntynyt vapauttaminen sekä pelien kasvanut merkitys viihdemedioina ja kulttuurisina kiinnekohtina. Näistä suuntauksista johtuen video- ja rahapelien välillä tapahtunut nopea lähentyminen ei siis ole yllättävää. Prosessin aikana perinteiset erot ovat yhä enemmän hämärtyneet, luoneet uusia toimintoja sekä vaikuttaneet uudenlaisten sosiaalisten suhteiden ja kulutuskäytäntöjen kehittymiseen. Digitaaliteknologian mahdollistama pelaamisen ja rahapelien lähentyminen on saanut viime vuosina yhä enemmän huomiota myös akateemisessa yhteisössä, näiden digitaalisten mediatuotteiden nopeasti kasvavien sosiaalisten ja taloudellisten vaikutusten vuoksi. Pelien sisäisiin kohteisiin, yllätyslaatikoihin (eng. loot boxes), on kiinnitetty paljon huomiota, mutta esimerkkejä rahapelien kaltaisesta mekaniikasta pelaajien sitouttamiseksi ja siten taloudellisen kannattavuuden edistämiseksi on olemassa paljon enemmän. Tämän kaltainen kehitys on herättänyt huolta ja nostanut esiin väitteitä ilmiön hyväksikäyttävästä luonteesta, rahapelien ja rahapelimäisten piirteiden normalisoinnista sekä ongelmalliseen kulutukseen kannustamisesta. Tätä tutkimusta tehtäessä esiin nousi huomattava, video- ja rahapelejä käsittelevän empiirisen tutkimuksen puute. Aiheesta aiemmin julkaistu tutkimus on keskittynyt pääasiassa pelaamisen oikeudellisiin näkökulmiin ja säännöstelyyn liittyviin kysymyksiin. Tämän väitöskirjatyön tavoitteena onkin siis tutkia videopeleihin liittyvää rahapelaamista (kuten e-urheiluvedonlyöntiä, virtuaalisia arpajaisia ja yllätyslaatikoita) ja sen yhteyttä videopelien pelaamistottumuksiin, virheellisiin uskomuksiin sekä motiiveihin verkkopalveluiden kuluttamisesta. Tämä väitöskirjatyö on jaettu sarjaksi toisiaan täydentäviä näkökulmia, jotka yhdessä tuovat tutkimukseen syvyyttä ja laajuutta. Tämä väitöskirja muodostaa ensimmäisen empiirisen tutkimuksen, joka keskittyy erillisenä aiheenaan nimenomaan videopeleihin liittyvän rahapelaamisen tarkasteluun. Aiemmin tällä kentällä tehdyt tutkimukset ovat tarkastelleet yksittäisiä käytäntöjä, esimerkiksi sosiaalisessa mediassa pelattavia kasinopelejä (eng. social casino games, SCG) tai e-urheiluvedonlyöntiä. Erityisesti mainittakoon, että tähän työhön sisällytetyt artikkelit käsittelivät ensimmäisten joukossa yllätyslaatikoiden ja muiden virtuaalisten tuotteiden roolia videopeleihin liittyvän rahapelaamisen mahdollistajina. Aihe on sittemmin saanut merkittävää huomiota paitsi akateemisen yhteisön sisällä, myös sen ulkopuolella. Lisäksi tämä työ muodostaa kuvan videopeleihin liittyvän rahapelaamisen kehityksen avainaikakaudesta, sen aikana tapahtuneista merkittävistä muutoksista sekä aiheen saamasta, lisääntyneestä huomiosta niin videopeliekosysteemin sisä- kuin ulkopuolellakin. Aikaisempien töiden keskittyessä tutkimaan videopelien pelaajia, e-urheilun seuraajia tai rahapelaajia, tämä työ tunnistaa ensimmäistä kertaa näiden ryhmien leikkauspisteissä olevat henkilöt: ne, jotka erityisesti osallistuvat videopeleihin liittyvään rahapelaamiseen. Erityishuomio tässä työssä on ollut tuoda esiin alaikäisten henkilöiden läsnäolo videopelien ja rahapelien ekosysteemissä. Tämä ryhmä on usein poissa vastaavanlaisista tutkimuksista, vaikka varhaiseen rahapelaamiselle altistumiseen tiedetäänkin liittyvän lisääntyneitä riskejä. Edellä kuvattuihin aihealueisiin pohjautuen tämä väitöskirjatyö pitää sisällään yhden ensimmäisistä tutkimuksista, joka käsittelee rahapelaamiseen liittyviä uskomuksia rahapelejä harrastavien videopelaajien keskuudessa. Tutkimuksen tulosten perusteella kehitettiin myös ensimmäinen mittari tunnistamaan kyseisiä uskomuksia kyseisessä pelaajien joukossa. Samaan aikaan tutkimuksen tulokset tarjoavat tietoa, jonka avulla voidaan parantaa jo vakiintuneita, rahapelaamiseen liittyviä uskomuksia perinteisissä rahapelaajaryhmissä tarkastelevia mittareita. Tämän väitöskirjatyön tuottama teoreettinen ja käytännön tieto on auttanut suuresti videopelien pelaamisen ja rahapelikäyttäytymisen välisten suhteiden ymmärtämistä. Se liittyy osaksi tutkimusten sarjaa, jotka osaltaan kyseenalaistavat polkuteorian näkemyksen videopelien pelaamisen suorasta myötävaikutuksesta ongelmallisen rahapelaamisen kehittymiseen. Sen sijaan tämä työ korostaa asiayhteyden, esimerkiksi pelaajayhteisöjen ja mediamuotojen vaikutuksen tärkeyttä. Näiden yhteyksien merkitys rahapelikäyttäytymisen kehittymiselle on pelkkää pelaamista suurempi. Kaikissa neljässä tähän väitöskirjatyöhön sisältyvässä artikkelissa käytetään kvantitatiivisia menetelmiä ilmiön tarkastelemiseksi ja korkeatasoisen näkemyksen saavuttamiseksi. Kaikki artikkelit ovat ensimmäisten empiiristen tutkimusten joukossa tarkastelemassa videopeleihin liittyvää rahapelaamista ja sen erilaisia ilmenemismuotoja. Tutkimukset luovat perustan, jonka varaan kyseisiä ilmiöitä tarkasteleva jatkotutkimus voi rakentua, ja ne toimivat myös tallenteena toiminnoista ja kä

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Quantitative thesis on video game-related gambling, including esports betting; the abstract does not name a problem-gambling instrument, though the articles likely used PGSI.

**Решение:** =

---

### 731 · R3909

**Between two worlds: Exploring esports betting in relation to problem gambling, gaming, and mental health problems.**

2021 · Journal of behavioral addictions · article, journal article, journalarticle · eng · https://doi.org/10.1556/2006.2021.00045

Abstract Background and aims Esports betting is an emerging gambling activity where individuals place bets on an organized video gaming competition. It represents only one of several gambling activities commonly endorsed by adolescents. To date, limited research has explored the relationship between esports betting and mental health among adolescents and its convergence with both problem gambling (PG) and problem video gaming (PVG). The present study examined the relation between esports betting, PG and PVG, and both externalizing and internalizing problems among adolescents while accounting for adolescents' video gaming intensity (i.e., how often they play 2 h or more in a day) and engagement in other gambling activities. Methods Data was collected from 6,810 adolescents in Wood County, Ohio schools. A subset of 1,348 adolescents ( M age = 14.67 years, SD = 1.73, 64% male) who had gambled and played video games during the past year were included in the analyses. Results Approximately 20% ( n = 263) of the included sample had bet on esports during the past year. Esports betting was positively correlated with other forms of gambling, both PG and PVG, and externalizing behaviors. Mediation analyses revealed esports betting was associated to both internalizing and externalizing problems through PVG and not PG. Conclusions Esports betting may be particularly appealing to adolescents who are enthusiastic video gamers. As such, regulators must be vigilant to ensure codes of best practices are applied to esports betting operators specifically for underaged individuals.

**ИИ:** + · обе модели · беттеры + инструмент · Adolescent survey with past-year esports bettors (n=263) and a problem gambling measure; could report PG prevalence among esports bettors.

**Решение:** =

---

### 732 · R3910

**How are the causes of gambling harm conceptualised by people who gamble?**

2021 · European Journal of Public Health · article · en · https://doi.org/10.1093/eurpub/ckab164.595

Abstract Background Messages to prevent gambling harm traditionally focused on individualised responsibility which stigmatise those who experience harm. Shifts have occurred among researchers, advocates, and some governments towards public health approaches which recognise broader determinants of harm. This includes the social practices of gambling and the tactics used by the industry to increase profits. This exploratory study aimed to identify how people who gamble conceptualise the causes of gambling harm. Methods A qualitatively led online panel survey was conducted via Qualtrics. A sample of 427 adults in two Australian states who gamble using electronic gambling machines or sports betting in a typical month provided text responses to the question “What do you think causes gambling harm?”. A reflexive thematic analysis was conducted. Results The vast majority of participants viewed gambling harm as being an issue of personal responsibility or addiction, with some making moral judgements about those who experience harm. Only a small portion of participants recognised the broader determinants beyond the individual that produce harm. Conclusions Gambling is still viewed by people who gamble as an issue of individual behaviour and addiction among a stigmatised sub-group of gamblers. The broader determinants of harm were generally not identified as causes of harm. This suggests the shift towards public health understandings of harm has not extended to the public. There are discrepancies between how the general public understands gambling harm and how it has been conceptualised by experts. Public health messages need to be reconsidered so they are relevant to and understood by the general community. Strategies to shift public understandings of harm also need to be identified. Key messages People who gamble understand gambling harm differently to how it has been conceptualised by experts. This has implications for how harm should be communicated in public health strategies. This study demonstrates the benefits of collecting qualitative data through online surveys.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Online survey of 427 EGM/sports bettors analysed qualitatively; PGSI not mentioned but often collected for sample description in this research group's work.); Sonnet -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: Qualitatively led open-text survey of EGM/sports bettors on perceived causes of harm; thematic analysis, no problem-gambling instrument evident.)

**Решение:** ?

---

### 733 · R3911

**Dichotomous and Weighted Scoring of the Problem Gambling Severity Index Converge on Predictors of Problem Gambling**

2021 · International Journal of Mental Health and Addiction · review, article · en · https://doi.org/10.1007/s11469-021-00715-8

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; title suggests an empirical PGSI study of predictors of problem gambling, possibly including gambling activities such as sports betting.

**Решение:** =

---

### 734 · R3913

**Instant Gratification Behavior Among Gambling Individuals in Uganda.**

2021 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-020-09973-y

Gambling has had mixed reactions over the years as a positive economic activity and as a negative action that leads to addiction. The purpose of the study is to examine whether the level of income and nature of employment explain the actual instant gratification behavior among bettors in Uganda. This study adopted a cross-sectional quantitative research design. Data was collected from 257 bettors in 26 betting firms, and a census survey was found appropriate to achieve a response rate of 98%. The research findings indicate that low-income earners are more likely to engage in sports betting. Secondly, individuals with jobs where they have too much free time and inadequate supervision are most likely to participate in sports betting. We, therefore, recommend that both private and public organizations should be concerned about the impact of sports betting on their performance and employees. Most entities don't have gambling policies, and sports betting has a negative impact, for example, in terms of labor productivity and well-being of the employees; hence organizations need to develop clear anti-gambling policies at the workplace. Our study finds that the youth are the most gambling group in the country; specific gambling pieces of training and support services should be developed and organized for the child to increase the awareness of the impact of sports betting on their lives. Finally, there is a need to improve on the saving culture of Ugandans in addition to the revision of the minimum wage level for the workers in the country, and also introducing a weekly payment system would help to manage the betting behavior. In this study, Betting firms from one of the divisions Kampala Central Business District were studied, i.e., Nakawa. Yet, it would be better to cover all the divisions of Kampala; hence future studies should focus on all the divisions and may even study all the betting firms in the entire country. A self-administered questionnaire with close-ended questions was used to collect data from the field. However, this might have limited the amount of information collected from the respondents. Therefore, future studies should employ other methods, such as an interview guide.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of 257 sports bettors in Uganda; the abstract mentions no problem-gambling instrument, so it is unclear whether one was used.

**Решение:** =

---

### 735 · R3919

**Estratégias de persuasão em apps de apostas desportivas: estudo de caso Placard**

2021 · Instituto Politécnico de Lisboa, Escola Superior de Comunicação Social · master thesis · por · https://hdl.handle.net/10400.21/14176

Atualmente, qualquer indivíduo está exposto a uma panóplia de agentes persuasores que podem assumir as mais variadas formas, entre as quais, sob a forma de aplicação móvel. O conceito de tecnologia persuasiva continua a gerar discórdias e diversas opiniões, tanto do lado do emissor, ao configurar um sistema persuasivo, como do lado do recetor, responsável por aceitar e incutir as iniciativas persuasivas. Tendo como estudo de caso a aplicação de apostas desportivas Placard, a presente dissertação recorre a um método misto através de recolha de dados com entrevistas semiestruturadas a responsáveis pela gestão da app e inquérito por questionário aos utilizadores da app Placard, compondo uma amostra de 70 inquiridos. Os principais resultados permitiram concluir que, por mais que uma tecnologia persuasiva seja idealizada, programada e desenhada para alterar um determinado comportamento, atitude ou crença, esta estará sempre dependente do recetor da mesma, bem como dos diferentes fatores que influenciam a sua decisão em aceitar, ou não, as intenções persuasivas. A própria plataforma persuasiva também necessita de proporcionar uma boa user experience, de forma a não ser resistida e, por sua vez, refutada. ABSTRACT: Nowadays, every individual is exposed to a multitude of persuasive agents, which can take many different forms, including that of a mobile app. The concept of persuasive technology still generates disagreements and different opinions, both on the sender’s side, by setting up a persuasive system, and on the receiver’s side, who is responsible for accepting and instilling the persuasive initiatives. Having as a case study the sports betting app Placard, this investigation uses mixed methods through data collection using semi-structured interviews with those responsible for the app’s management and a survey to Placard’s app users, composing a sample of 70 respondents. The main results allowed us to conclude that, no matter how much persuasive technology is idealized, programmed, and designed to change a certain behaviour, attitude or belief, it will always depend on the receiver, as well as on the different factors that influence their decision on whether or not to accept the persuasive intentions. The persuasive platform itself also needs to provide a good user experience in order to not be resisted and, consequently, refuted.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Survey of 70 Placard sports-betting app users about persuasive design; the abstract doesn't say whether a problem-gambling screen was used, though that seems unlikely.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Master thesis on persuasive design in Placard sports betting app; survey of 70 users on persuasion, no indication of a problem-gambling instrument.)

**Решение:** ?

---

### 736 · R3920

**Inventaire des cognitions à risque — Loteries sportives (ICR-LS) : un premier pas dans l’élaboration de mesures spécifiques au type de jeu/The Inventaire des cognitions à risque Loteries Sportives: A First Step in Developing Game-Specific Measures**

2021 · Journal of Gambling Issues · article · fr · https://doi.org/10.4309/jgi.2021.47.12

A travers le monde, les paris sportifs representent la deuxieme forme de jeux de hasard et d’argent (JHA) la plus associee aux problemes de jeu. Les cognitions des parieurs sportifs pourraient contribuer a cette association. Cependant, aucun outil ne semble adapte aux parieurs de loteries sportives, principalement a cause de la composante d’habilete. Cette etude vise (a) a developper l’Inventaire des cognitions a risque — Loteries sportives (ICR-LS) et en determiner la structure factorielle, (b) a evaluer la validite de convergence de l’ICR-LS avec Gambling Related Cognitions Scale (GRCS), les habitudes de jeu, et la gravite des problemes de jeu; et (c) a evaluer les liens entre le nombre d’heures mensuelles consacrees a la preparation des paris aux loteries sportives et les habitudes de jeu. Les parieurs sportifs recrutes ( N = 272) etaient principalement de sexe masculin (86,5 %), dans la vingtaine ( M = 26,7 ans) et issus de la communaute universitaire (88,3 %). Les analyses en composantes principales indiquent que l’instrument possede deux dimensions (Superstitions et Habiletes), une forte coherence interne (les coefficients alpha > ,85) et une bonne validite convergente. Des associations negligeables, mais statistiquement significatives, ressortent entre l’ICR-LS et le montant annuel depense aux loteries, les heures consacrees a la preparation des paris et la gravite des problemes de jeu. En outre, le temps consacre a la preparation des paris sportifs est moderement correle avec le montant depense, la frequence de jeu et la gravite des problemes de jeu, ce qui incite a y voir, peut-etre, un facteur de risque lie aux loteries sportives. Le temps consacre a la preparation des paris sportifs et ses effets sur les differentes spheres de vie meriteraient d’etre etudies davantage, notamment aupres de joueurs problematiques. Abstract Around the world, sports betting is the second type of gambling activity most associated with gambling problems. Thus, sports bettors’ cognitions play an essential role in this association. However, no instrument is specifically designed to assess sports bettors’ cognitions. This study aims (a) to develop the Inventaire des cognitions a risque — Loteries sportives (ICR-LS) and to determine its factor structure, (b) to assess the convergent validity of the ICR-LS with the Gambling Related Cognitions Scale (GRCS), gambling habits, and the severity of gambling problems; and (c) to assess the links between the number of monthly hours spent preparing for sports lottery bets and gambling habits. Participants are sport lottery bettors ( N = 272) that are mainly men (86.5%) in their twenties ( M = 26.7 years old), and from a university community (88.3%). Principal component analysis results indicate that the instrument is composed of two factors (Superstitions and Abilities), and shows strong internal consistency (coefficients alpha > .85) and good convergent validity. The scale shows statistically significant but negligible associations with the annual amount spent on lotteries, hours spent on the preparation of bets, and gambling problem severity. In addition, time dedicated to bet preparation is moderately associated with the amount spent, gambling frequency, and gambling problem severity, suggesting that sports bettors bet preparation time could be a risk factor in sports betting. Studies should explore further the amount of time dedicated to bet preparation and its effects on different spheres of life, especially for problem gamblers.

**ИИ:** + · обе модели · беттеры + инструмент · Survey of 272 sports lottery bettors that measured gambling problem severity, probably with the PGSI/CPGI, though the abstract doesn't name the instrument.

**Решение:** =

---

### 737 · R3923

**Mitglieder von Sportvereinen: Empirische Befunde zum Wettverhalten und Ausmaß glücksspielbezogener Probleme**

2021 · Suchttherapie · article · de · https://doi.org/10.1055/a-1327-0867

Zusammenfassung Internationale Forschungsergebnisse deuten an, dass sportinteressierte Personen bzw. Mitglieder von Sportvereinen besonders gefährdet sind, glücksspielbezogene Probleme zu entwickeln. Vor diesem Hintergrund verfolgt der vorliegende Beitrag das Ziel, die Ergebnisse einer hierzulande durchgeführten Pilotstudie zu diesem Themenfeld aus dem Jahr 2012 zu replizieren und zu ergänzen. Im Rahmen einer standardisierten Erhebung im Querschnitt wurden in 2019 insgesamt N=317 Mitglieder (87,4% männlich; M=28,1 Jahre) aus Bremer Fußballvereinen in differenzierter Weise zu ihrem Glücksspielverhalten mit dem Schwerpunkt „Sportwetten“ befragt. Während knapp 70% der Stichprobe im letzten Jahr Geld für Glücksspiele (außer Sportwetten) ausgegeben hatten, belief sich die 12-Monats-Prävalenz für eine Teilnahme an Sportwetten auf 54,6%. Am häufigsten wurden dabei Sportwetten im Internet nachgefragt. Soziale Bezüge, wie der Freundeskreis (außerhalb des Vereins) und z. T. auch die eigenen Teammitglieder, spielen sowohl beim Erstkontakt zu Sportwetten als auch bei den Wettaktivitäten an sich eine wichtige Rolle. Schließlich zeigen etwa 10% der Stichprobe Anzeichen einer Glücksspielproblematik, hierunter befinden sich insbesondere Personen mit einem Migrationshintergrund. Damit bestätigt diese Studie nicht nur, dass aktive FußballerInnen im Breitensport eine ausgeprägte Glücksspiel- bzw. Sportwetten-Affinität aufweisen, sondern darüber hinaus auch vermehrt zur Gruppe der ProblemspielerInnen zählen. Zukünftige Präventionsansätze zur Bekämpfung der mit Glücksspielen einhergehenden Suchtgefahren sollten sich daher verstärkt auf das Setting „Sportvereine“ und die dort vorherrschenden Besonderheiten fokussieren.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Survey of 317 football club members; 54.6% bet on sports; about 10% showed signs of problem gambling, which implies a screening instrument was used.

**Решение:** =

---

### 738 · R3939

**Alcohol consumption and sports-betting among young male motorcycle taxi boda boda riders in urban southwestern Uganda.**

2021 · BMC public health · article, collection/collection, journal article · eng · https://doi.org/10.1186/s12889-021-10406-7

Abstract Introduction: The popularity of sports-betting is growing globally and may be associated with alcohol consumption among young adults. In this study, we examine the relationship between alcohol consumption plus other substances with sports-betting in a group of young adult males in Uganda. Methods: We conducted a cross-sectional study and interviewed male motorcycle taxi bodaboda riders in the southwestern Uganda town of Mbarara. We asked questions about alcohol consumption, smoking and history and frequency of sports-betting. Results: We enrolled 401 riders. The median age was 29.0 years, interquartile range 25-32. Seventy four (18.5%) had engaged in sports-betting in the past 30 days. Among those that reported sports-betting, 16(21.6%) engaged daily or almost daily. Alcohol use was significantly associated with gambling with an adjusted risk ratio (aRR) of 2.08(95% CI 1.36, 3.18) among moderate drinkers compared to low or non-drinkers but not among heavy drinkers. Cigarette smoking was significantly associated with sports-betting with an aRR 1.85(95% CI 1.13, 3.01). Conclusion: Our data show sports-betting is common among these relatively young male motorcycle riders, and is associated with alcohol consumption and cigarette smoking. Interventions to regulate sports-betting should be co-packaged with those to reduce alcohol consumption and cigarette smoking among young adult males.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey measured sports betting; abstract lists only history and frequency, so a problem-gambling screen seems unlikely but isn't ruled out.

**Решение:** =

---

### 739 · R3942

**Assessing the effects of sports gambling among the youths in Blantyre City of Southern Malawi**

2021 · International Journal of Sociology and Anthropology · article, journal-article · en · https://doi.org/10.5897/ijsa2021.0921

The study aimed at assessing the effects of sports gambling among the youths of Blantyre City in Southern Malawi. In this study, the sample size was made up of 30 youths compromising 19 males and 11 females. They were randomly selected by the researcher through probability sampling. Questionnaires were used to collect data for the study. The study achieved a 100% response rate. The study revealed that 84.2% of the youths involved in sports betting are not aware of any of the rules or regulations protecting them as bettors, 68% of them do not invest in the money they get. Asked how this activity has affected them either negatively or positively, it is discovered it has brought more harm than good. A total of 9 of the respondents were affected by addiction, 5 of the respondents had financial constraints caused by betting, 3 of the respondents agreed that it wasted their time and 8 of them said that it affected them positively as it helps them spend their leisure time. The study established that sports betting is an activity that can jeopardize the social and moral welfare of the youths; hence, more research on sports betting addiction is needed about the youths to examine more the effects associated with this activity in Blantyre; and that more protection must be devised for the youths through the main stakeholders to safeguard their moral, social and academic welfare. The government policy should be more strengthened and tightened by increasing the eligible age for bettors and that more awareness about pathological betting is needed among the youths of Blantyre. Key words: Gambling, betting, youths, effect, sports.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Questionnaire survey of 30 youth sports bettors reporting self-reported addiction; abstract names no problem-gambling instrument.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Small questionnaire of 30 youths on effects of sports betting; no problem-gambling instrument, only self-reported effects like addiction.)

**Решение:** ?

---

### 740 · R3945

**Population Screening of Gambling Behavior: Playing to Escape From Problems May Be a Key Characteristic of At-Risk Players**

2021 · Frontiers in Psychiatry · article · en · https://doi.org/10.3389/fpsyt.2021.690210

The increase in gambling availability and the inclusion of gambling disorder as an addiction in DSM-5 highlight the importance of brief screening measures aiming to identify at-risk gamblers. The current study, using a brief telephone survey, assessed demographic characteristics and gambling behaviors in 2,118 adults. Questions were developed based on DSM-5 criteria for Gambling Disorder and common assessment tools. A 7% prevalence of as at-risk gamblers was identified. Male gender, low monthly income, high frequency of gambling behavior, large amounts of money spent, and gambling to escape from everyday problems or for amusement, specifically for men, were found to be the characteristics that can help in the early identification of at-risk gamblers. Gambling for financial gain and as a way to socialize, age, and employment status were not significant predictors of gambling severity. This study shows that the above characteristics can be assessed easily through phone screening of large populations, aiding in prevention practices to reduce the problematic use of gambling activities.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Telephone population survey with DSM-5-based at-risk screen; unclear whether gambling activities including sports betting were reported.

**Решение:** =

---

### 741 · R3947

**No credible evidence that UK safer gambling messages reduce gambling**

2021 · PsyArXiv · article, preprint, posted-content · en · https://doi.org/10.31234/osf.io/hv6w9

Safer gambling messages are a common freedom-preserving method of protecting individuals from gambling-related harm. Yet, there is a striking lack of independent and rigorous evidence to attest to the effectiveness of safer gambling messages. This study presents results from three large (N ≈ 3,000), preregistered, and incentivized experimental tests of the UK’s commonly used “When the fun stops, stop” gambling message. Variants of this message were tested on gamblers’ propensity to accept bets on soccer events (Experiment 1), behavior on a realistic online roulette table (Experiment 2), and betting patterns on an online soccer betting platform (Experiment 3). All three experiments find either no beneficial effect or a small backfire effect on gamblers’ behaviour. We conclude that independent evaluations should inform policy-makers’ decisions on how to best implement improved safer gambling messages.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Large experiments with gamblers betting on soccer; the abstract does not say whether a problem-gambling instrument such as the PGSI was used.

**Решение:** =

---

### 742 · R3948

**Request-a-bet sports betting products indicate patterns of bettor preference and bookmaker profits.**

2021 · Journal of behavioral addictions · article, journal article, journalarticle · eng · https://doi.org/10.1556/2006.2020.00054

Abstract Background and aims Request-a-bet services are a modern gambling product delivered via the social network Twitter, which allow sports bettors to design custom bets. The public nature of Twitter data provided a unique opportunity to investigate patterns of bettor preference and the bookmaker profit margin in soccer, the UK’s favorite sport. Methods Two multi-method studies. Twitter users’ engagement with request-a-bet services was monitored unobtrusively ( n = 1,406), meaning that potential patterns across users’ requests could be observed, and the bookmaker profit margin could be estimated. Twitter users were also surveyed directly ( n = 55), providing self-report measures of request-a-bet usage. Results Twitter users requested bets with an average potential payoff of £56.5 per £1 risked (median = £9). Overall, 9.7% of requested bets paid-off, but these were mostly bets at short odds. This meant that requests yielded a high bookmaker profit margin of 43.7% (roughly eight times higher than current margins in conventional soccer bets), which increased to 74.6% for bets at longer odds. Requested bets also tended to involve star players from the best teams. Finally, 92.7% of surveyed Twitter users reported placing at least one bet via request-a-bet services (mean = 44.4 bets). Discussion and conclusions Researchers can use request-a-bet products to increase their understanding of sports betting behavior. Sports bettors should be given information about how much higher the bookmaker profit margin can be in modern sports bets compared to the conventional sports bets that they may be more familiar with.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Includes a small survey of sports bettors (n=55); the abstract doesn't say whether a problem-gambling screen such as the PGSI was used.

**Решение:** =

---

### 743 · R3954

**How did regular sports bettors behave during covid-19 lockdown? Evidence from Poland**

2021 · European Sport Management Quarterly · article, review, journal-article · en · https://doi.org/10.1080/16184742.2021.1909092

ABSTRACT Research question The coronavirus pandemic (covid-19) has significantly altered everyday life in numerous aspects. One of them is sports betting and the uncertainty regarding the effects of lockdown on bettors’ behaviour. This paper explores four key questions about sports bettors during covid-19: (1) have they ceased their sports betting? (2) Have they substituted betting for other online gambling activities (or esports)? (3) Have they saved more time or money?, and (4) How do they feel about their betting? Research methods The study reports findings from an online survey. Data was collected during the pandemic outbreak and before any major sport competition resumed its activity (5–7 May 2020). The survey was conducted in Poland. A purposive sampling method was used to reach regular sport bettors – where ‘regular’ means those who had bet at least once a month before covid-19. In total, 240 regular sports bettors completed the questionnaire in full. A binominal logistic regression model was used to analyse the behavioural changes of bettors during the pandemic. Results and findings The findings showed that most bettors ceased or seriously reduced their betting. In general, they did not substitute it with other forms of gambling. The majority of respondents saved time and money. Many of them also declared not missing betting. Implications The results did not depict sports bettors as desperate to resume betting, and willing to substitute it for any other gambling form in order to maintain their gambling habit. The betting industry’s efforts to mitigate the impact of sport events cancellations by promoting virtual sports, esports, or other casino games do not seem to be especially attractive for regular sports bettors.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Online survey of 240 regular Polish sports bettors during COVID-19; abstract doesn't say whether a problem-gambling instrument was used.

**Решение:** =

---

### 744 · R3963

**¿Cómo hemos llegado hasta aquí? La dimensión socio-cultural de las apuestas deportivas**

2021 · presentation · und · https://doi.org/10.13140/rg.2.2.12563.40483

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Presentation on the socio-cultural side of sports betting with no abstract; probably conceptual, but survey data can't be ruled out.

**Решение:** =

---

### 745 · R3964

**The Role of Narcissism, Hyper-competitiveness and Maladaptive Coping Strategies on Male Adolescent Regular Gamblers: Two Mediation Models.**

2021 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-020-09980-z

The present study aimed to explore the unique and common role that some cognitive, personality and relational characteristics play in male adolescents' regular gambling behavior. Participants were 273 male adolescents and young adults aged 15-19 recruited in sports betting centers. They completed the South Oaks Gambling Screen, the Narcissistic Admiration and Rivalry Questionnaire, the Hypercompetitive Attitude scale, and The Coping Strategy Indicator. The relationship between narcissistic rivalry and gambling was mediated by hyper-competitiveness and avoidant coping strategy. These findings suggest that narcissistic features and maladaptive coping strategies might be involved in the development of disordered gambling in youth, supporting a compensatory model of this addictive behavior and claiming for preventative actions that take into account the psychological vulnerabilities of adolescents and young adults.

**ИИ:** + · обе модели · беттеры + инструмент · The study surveyed 273 adolescents recruited in sports betting centres using the SOGS, so it could report problem-gambling prevalence among sports bettors.

**Решение:** =

---

### 746 · R3965

**Gambling in adolescents during the financial crisis in Greece**

2021 · Psychiatriki · article · en · https://doi.org/10.22365/jpsych.2021.006

Problem gambling emerges as a serious and ever growing problem of modern societies, largely affecting adolescents as well. The etiology of gambling disorder is complex and multifaceted as it is governed by multiple and interrelated factors. In this context and in light of the pervasive financial crisis in Greece, we conducted a study in order to explore adolescents' gambling involvement in Athens region and also to identify the socio-economic characteristics of adolescents who have engaged into gambling activities. Students were recruited from a sample of schools in Athens area. For the assessment of gambling involvement in adolescents, the Diagnostic and Statistical Manual of Mental Disorders-IV Multiple Response Adapted for Juveniles Questionnaire (DSM-IV-MR-J) was administered. Additional self-constructed questions enquired about students' socio-demographic and economic characteristics. Our results indicate that adolescents that had problem with gambling or had at least one pathological item on DSM were more likely to be boys and to have been born in a country other than Greece. Additionally, the proportion of those having at least one pathological item on DSM was greater in those with low school grades. Τhe lack of food in the household due to inability of providing food during the last month was significantly associated with both having problem with gambling and having at least one pathological item on DSM. Furthermore, having been worried that there would not be enough food during the last month and having been fed with a restrained variety of food due to lack of recourses were associated with at least one pathological item on DSM. These findings are congruent with the literature suggesting that youth living under poverty often resort to gambling. In conclusion, our results point out the adverse effects of the financial crisis on the development of problem gambling in adolescents within the Greek society. Problem gambling may have developed in response to the ubiquitous insecurity characterizing the Greek society during this rough time period. Interventions should prioritize endowing adolescents with the necessary coping skills for dealing with daily obstacles or life adversities productively and without losing their self-control.

**ИИ:** разошлись — Opus ? (неясно, есть ли ставки на спорт: Adolescent school survey using DSM-IV-MR-J; the abstract doesn't say whether sports betting participation was measured.); Sonnet + (игроки, есть ставки на спорт и инструмент: Adolescent school survey using DSM-IV-MR-J; likely reports gambling by activity, so sports betting may be reported with problem gambling.)

**Решение:** ?

---

### 747 · R3966

**Changes Over Time and Predictors of Online Gambling in Three Norwegian Population Studies 2013–2019**

2021 · Frontiers in Psychiatry · article · en · https://doi.org/10.3389/fpsyt.2021.597615

Objectives: To investigate changes over time and identify predictors of online gambling among gamblers by using three Norwegian representative samples covering a 6-year (2013–2019) period. We also aimed to identify different characteristics (including video game participation and video gaming problems) of online compared to offline gamblers. Methods: Data from gamblers (N = 15,096) participating in three cross-sectional surveys (2013, 2015, and 2019) based on random sampling from the Norwegian Population Registry were analyzed. Participants were asked how frequently they engaged in online gambling on different platforms (e.g., mobile phone). Data on sociodemographics, games gambled, gambling problems, gaming, and problem gaming were collected and analyzed by logistic regression analyses. Results: Overall, an increase in online gambling from 2013 to 2015 was found (a larger percentage of gamblers reported having gambled online at least once during the last year), and an increase in online gambling from 2015 to 2019 was found (more gamblers reported having gambled online at least once last year and at least once per week). The increase was largest for gambling on mobile phone. Consistent predictors of online gambling (at least once last year and at least once per week) were male gender, high income, being unemployed, being on disability pension, having work assessment allowance, being a homemaker or retiree, number of games gambled, and gambling problems. Conclusions: Online gambling, especially on mobile phones, has increased significantly during the last 6 years in Norway. Hence, gambling availability seems to have grown, which may pose a risk for development of gambling problems. Compared to offline gamblers, online gamblers were more likely to be men, young, not working or studying, gambling on several games, and having gambling problems. Responsible gambling efforts aiming at preventing or minimizing harm related to online gambling should thus target these groups.

**ИИ:** + · обе модели · опрос населения об азартных играх · Norwegian representative population surveys that measured the games people gambled and gambling problems; tables by activity, including sports betting, are likely.

**Решение:** =

---

### 748 · R3972

**Développement d’un modèle de repérage des joueurs problématiques sur Internet à l’aide de méthodes d’intelligence artificielle**

2021 · Revue d Épidémiologie et de Santé Publique · article · fr · https://doi.org/10.1016/j.respe.2021.04.016

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; AI detection of online problem gamblers may use account data, possibly validated with PGSI, and may include sports bettors.

**Решение:** =

---

### 749 · R3982

**Gambling in Spanish Adolescents: Prevalence and Association with Mental Health Indicators**

2021 · International Journal of Environmental Research and Public Health · article · en · https://doi.org/10.3390/ijerph19010129

Concern about the development of behavioral addictions in adolescence, including gambling, has increased in recent years. Evidence shows that problem gambling can lead to personal, social, or health problems. However, even though gambling is an illegal activity, studies on this problem are quite limited in Spain. The main objective of this study was to analyze the prevalence of gambling in adolescents in Spain. Moreover, gambling behaviors were examined according to gender and age, and their possible relationship with several mental health indicators was analyzed. The results showed that 20.6% of the adolescents who participated in the study had gambled money in the past year. The highest gambling prevalence was found in boys and in adolescents from the age of 16 years old. Moreover, the results showed that gambling behavior was related to different mental health indicators.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Spanish adolescent gambling survey; the abstract doesn't say whether a problem-gambling instrument or sports betting participation was measured.

**Решение:** =

---

### 750 · R3989

**Towards an Understanding of Esports Gambling: Demographic and Clinical Characteristics of Youth Esports Bettors**

2021 · Gaming Law Review · article, journalarticle, journal-article · en · https://doi.org/10.1089/glr2.2021.0013

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: No abstract; title describes clinical characteristics of youth esports bettors, which likely includes a problem-gambling measure.); Sonnet + (беттеры + инструмент: No abstract, but the title points to a survey of youth esports bettors with clinical characteristics, likely including problem gambling screens. Full text should be read.)

**Решение:** ?
