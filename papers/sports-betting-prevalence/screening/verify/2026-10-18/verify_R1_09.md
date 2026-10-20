# Проверка с метками ИИ, часть 9

Записи 1201–1350 из 1525, с метками обеих моделей над строкой решения. Модели согласны и вы тоже — поставьте `=`; иначе свой код (`+`, `?` или `-`, причина не нужна). Если модели разошлись, `=` не годится — нужен ваш код. Решаете вы.

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

### 1201 · R6302

**Gambling Participation and Problem Gambling Severity in a Stratified Random Survey: Findings from the Second Social and Economic Impact Study of Gambling in Tasmania**

2014 · Journal of Gambling Studies · article · en · https://doi.org/10.1007/s10899-014-9495-9

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** + · обе модели · опрос населения об азартных играх · Regional population survey from Tasmania that measured participation in gambling activities and problem-gambling severity; it probably has activity tables.

**Решение:** =

---

### 1202 · R6304

**Jeu problématique en France : une première enquête nationale**

2014 · Drogues santé et société · article · fr · https://doi.org/10.7202/1026875ar

Avant l’enquête nationale sur les jeux de hasard et d’argent (JHA) de 2010, la France ne disposait pas de mesure de la prévalence du jeu et du jeu problématique dans la population. Objectif : Cette étude présente un premier portrait des JHA en France, décrivant le profil sociodémographique des joueurs courants, les pratiques de jeu des joueurs dits assidus, c’est-à-dire de joueurs qui jouent fréquemment et qui dépensent beaucoup, ainsi que les associations entre les problèmes de jeu et l’usage de substances psychoactives. Méthodologie : Un module sur les pratiques de JHA fut introduit dans l’enquête nationale Baromètre santé. Lors d’une entrevue téléphonique, les participants répondaient à des questions au sujet de la fréquence à laquelle ils jouent et au sujet de la quantité d’argent qu’ils dépensent au jeu. On a mesuré la gravité des problèmes de jeu en utilisant l’indice canadien de jeu excessif (ICJE) et des mesures sur la consommation de substances psychoactives. Participants : L’enquête générale a été menée en 2010 auprès d’un échantillon représentatif de 25 034 répondants âgés de 18 à 75 ans. Résultats : Les résultats révèlent que près de 12 % de la population générale est constituée de joueurs assidus qui ont joué 52 fois ou plus ou qui ont misé 500 euros ou plus au cours des 12 derniers mois. La proportion de joueurs excessifs parmi les joueurs assidus est estimée à 3,7 % et celle des joueurs à risque modéré à 7,1 %. Ces joueurs problématiques sont plus souvent des hommes issus de milieux socioéconomiques modestes. L’enquête met en évidence une relation significative entre les pratiques de jeu les plus à risque et la consommation problématique d’alcool, de tabac ou de cannabis. Conclusion : L’inclusion d’un ensemble élargi de conduites de jeux de hasard et d’argent à d’autres pratiques de santé assurera une meilleure compréhension des facteurs de risques et de vulnérabilité au jeu problématique.

**ИИ:** + · обе модели · опрос населения об азартных играх · French national prevalence survey (Baromètre santé 2010) using CPGI/ICJE; gambling practices measured, sports betting likely in activity tables.

**Решение:** =

---

### 1203 · R6312

**SPORTSKO KLAĐENJE STUDENATA U ZAGREBU − DOPRINOS UVJERENJA O KOCKANJU, MOTIVACIJE I ISKUSTVA U IGRAMA NA SREĆU**

2014 · Ljetopis socijalnog rada · article · und · https://doi.org/10.3935/ljsr.v21i2.19

In Croatia, we are witnessing an increasing availability of games of chance, and especially the great popularity of sports betting. It is known that adolescents and young adults have the highest risk of developing gambling-related problems. Therefore, the aim of this paper is to explore characteristics of sports betting by students in relation to frequency, gender differences and other gambling activities, as well as to explore the specific contribution that irrational beliefs, motivation and experience in games of chance have in explaining the frequency of sports betting. The study was conducted on a sample of 254 students at the University of Zagreb (M=147, F=107). The age of participants ranged from 19 to 27 years (Mage=21.42; SD=1.37). The results show that almost half of the students (49.8%) have experience in sports betting, and the group largely consists of young men for whom sports betting is the most frequently played game of chance. Girls are significantly less likely to bet on sports results, but they play lottery games more often. Frequent sports betting is correlated with more frequent participation in slot machine games, roulette and virtual race betting. To determine the contribution that different characteristics and constructs have in explaining the frequency of sports betting, a hierarchical regression analysis was conducted. The main determinants of intensive sports betting are behavioural and experiential variables – more frequent gambling (participating in other games of chance) and subjective experience in winning large amounts of money. The results underline the importance of experience, availability and accessibility of gambling activities in the specific Croatian market, and are interpreted in the context of possible psychosocial and broader social interventions. U Republici Hrvatskoj svjedočimo sve većoj dostupnosti igara na sreću, te posebno velikoj popularnosti sportskog klađenja. Poznato je da su za razvoj problema povezanih s kockanjem posebno ranjivi mladi, pri čemu dostupnost i pristupačnost igara te učestalost uključivanja u aktivnosti kockanja značajno doprinose razvoju štetnih posljedica. Stoga su ciljevi ovog rada istražiti obilježja sportskog klađenja studenata u Zagrebu iz perspektive učestalosti, rodnih razlika kao i sudjelovanja u drugim igrama na sreću, te istražiti specifičan doprinos uvjerenja o kockanju, motivacije za kockanjem i iskustva u igrama na sreću u objašnjavanju učestalosti sportskog klađenja. U istraživanju je sudjelovalo 254 studenta Sveučilišta u Zagrebu (M=147, Ž=107), čiji se raspon dobi kreće od 19 do 27 godina (Mdob=21,42; SDdob=1,37). Rezultati pokazuju kako gotovo polovica studenata (49,8%) ima iskustvo sportskog klađenja, a tu skupinu u većoj mjeri čine mladići kojima je to i vrsta igre na sreću koju najučestalije igraju. Djevojke se značajnije rjeđe klade na sportske rezultate, dok lutrijske igre igraju nešto češće. Učestalije sportsko klađenje povezano je kod studenata i s učestalijim sudjelovanjem u igrama na automatima, ruletu te klađenjem na virtualne utrke. Regresijskom analizom su kao glavne odrednice intenzivnijeg sportskog klađenja identificirane ponašajne i iskustvene varijable − učestalije kockanje, odnosno igranje drugih igara na sreću te iskustvo dobitka (subjektivno) velikog iznosa novca. Rezultati dodatno naglašavaju značaj iskustva, dostupnosti i pristupačnosti aktivnosti kockanja na specifičnom hrvatskom tržištu, te su interpretirani u kontekstu mogućih psihosocijalnih i širih društvenih intervencija.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Student survey of sports betting with beliefs and motivation measures; the abstract doesn't mention a problem-gambling screen, though the full text may include one.

**Решение:** =

---

### 1204 · R6333

**Brand community and sports betting in Australia**

2014 · QUT ePrints (Queensland University of Technology) · report · en

This study aimed to examine the impact of different approaches to wagering marketing, including inducements, on vulnerable adults (adults at-risk of, or experiencing, gambling problems).It involved five empirical stages: Ecological momentary assessment (EMA) study.This study captured longitudinal data over 15 surveys from regular bettors on races (n = 402) and sports (n = 320).It assessed: 1) exposure to different types of wagering advertisements and inducements; 2) their reported influence on the size, frequency, and riskiness of subsequent bets placed; and 3) longitudinal associations between exposure to wagering advertisements and inducements and betting expenditure. Experimental study.This study tested the effects of four types of wagering inducements (bonus bet, better odds, reduced risk, cash rebate) on propensity to choose riskier bets (with greater theoretical loss).Using video game simulation, 299 sports bettors watched and bet on AFL, cricket or soccer matches.Participants were provided with a $4 stake for each trial, and winnings accrued to their take-home compensation.This study assessed: 1) the effects of different types of wagering inducements on the riskiness of bets placed; 2) their relative appeal to bettors; and 3) any differential effects for vulnerable adults. Study of play-through conditions on bonus bets.The 299 participants rated the attractiveness of three variations of an inducement offer.Promo1 simply noted 'terms and conditions apply;' promo2 included the terms and conditions; promo3 revealed the offer's true cost.Respondents were asked to calculate the true cost before it was revealed.This study assessed: 1) whether the attractiveness of bonus bet inducements varied with information provided about their play-through conditions; 2) bettors' comprehension of their true cost; and 3) whether this varied by gambler risk group. Psychophysiological study.This study measured electrodermal, cardiac and eye movement responses of 60 participants to 12 advertisements.Participants also rated how stimulating each advertisement was and their likelihood of taking up each inducement.This study assessed: 1) the appeal of wagering vs non-wagering inducements; 2) attention, excitement and desire to gamble elicited by four types of wagering inducements (bonus bet, better odds, reduced risk, cash rebate); and 3) variations by gambler risk group. Interview study.Interviews with 31 regular race and sports bettors explored causal mechanisms driving betting-related responses to wagering advertisements and inducements.Constructivist grounded theory methods were used to develop a model of influences from wagering advertisements and inducements, including environmental, situational, structural, and individual factors.Key findings from the study include that wagering advertisements and inducements: are prolific; encourage riskier betting; increase betting expenditure; elicit attention, excitement, and desire to bet amongst vulnerable gamblers; and have negative effects on all gambler risk groups.While aggregate exposure across all types of advertisements and inducements increased betting expenditure, those with most influence were: direct messages from wagering operators; advertisements on betting websites and apps; betting brands promoted during live and televised race/sports events; commentary promoting betting or betting odds during events; stake-back offers; multi-bet offers; and inducements for rewards program points.Most bettors underestimated the cost of bonus bets with Table of contents Acknowledgements ..

**ИИ:** разошлись — Opus + (беттеры + инструмент: Surveys of regular sports bettors (n=320, n=299) classified by gambler risk group, likely using PGSI; the title and abstract may not match.); Sonnet ? (неясно, измеряли ли проблемную игру: Surveys of regular sports bettors with results by "gambler risk group", probably PGSI-based. The abstract doesn't name the instrument, so this needs a full-text check.)

**Решение:** ?

---

### 1205 · R6334

**Lifestyle consumption communities : exploring the concept in relation to sports betting**

2014 · article · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; consumer-research study of sports betting communities, possibly qualitative or conceptual, but a survey with a PG measure can't be ruled out.

**Решение:** =

---

### 1206 · R6335

**Relationship Between Gambling Severity and Attitudes in Adolescents: Findings from a Population-Based Study**

2014 · Journal of Gambling Studies · article · en · https://doi.org/10.1007/s10899-014-9481-2

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract. A population-based adolescent survey of gambling severity probably used a PG screen; whether it measured sports betting is unclear.

**Решение:** =

---

### 1207 · R6337

**« Ces français qui jouent, du plaisir à l’excès »**

2014 · European Psychiatry · article · fr · https://doi.org/10.1016/j.eurpsy.2014.09.402

En France, la loi du 12 mai 2010 a encadré l’ouverture à la concurrence et à la régulation du marché des jeux de hasard et d’argent (JHA) sur Internet. Seuls trois types de jeux ont été autorisés : les paris sportifs, les paris hippiques et le poker. Une récente enquête épidémiologique nationale a indiqué que 3,7 % de la population générale adulte déclaraient avoir joué à un JHA en ligne au cours de l’année écoulée, soit environ deux millions d’individus [1]. Se basant sur l’Indice canadien du Jeu Excessif [2] pour l’évaluation des pratiques de jeu, cette même enquête identifiait 17 % de joueurs « problématiques » parmi les joueurs dans l’année. Ces chiffres sont nettement supérieurs à ceux retrouvés avec l’offre de jeu traditionnelle hors ligne, confirmant que jouer sur Internet est un facteur de risque considérable de perdre le contrôle. Le poker est sans aucun doute le JHA qui a le plus « bénéficié » de la légalisation des jeux en ligne en France, représentant à lui seul plus de 80 % des mises sur l’ensemble des jeux en ligne. Au troisième trimestre 2013, le nombre moyen de comptes joueurs actifs en poker était ainsi de 244 000 comptes/semaine [3]. Il existe encore peu de données épidémiologiques disponibles sur la prévalence du jeu excessif dans le cadre précis du poker, ni sur les caractéristiques des joueurs de poker en ligne, problématiques ou non. Pourtant, il apparaît aux cliniciens qui reçoivent les joueurs de poker en ligne problématiques qu’ils présentent des caractéristiques bien particulières, qu’il convient d’étudier à grande échelle. Mieux connaître les spécificités de ces joueurs permet de mieux adapter l’offre de soins, mais aussi de mener des politiques de prévention plus efficaces, car mieux ciblées. L’une des pistes en ce sens serait d’imposer aux opérateurs de jeu l’installation de modérateurs de jeu dont l’efficacité a été scientifiquement démontrée.

**ИИ:** разошлись — Opus -1 (обзор, комментарий, теоретическая, правовая или регуляторная работа: Narrative congress abstract on online gambling in France, mainly poker; it cites an existing survey and reports no original data.); Sonnet ? (неясно, есть ли ставки на спорт: French online gambling context with CPGI; focus appears to be online poker, and it's unclear whether sports bettors' problem gambling is reported.)

**Решение:** -

---

### 1208 · R6342

**Prevalence and Correlates of Problem Gambling in a Representative Sample of Norwegian 17-Year-Olds**

2014 · Journal of Gambling Studies · article · en · https://doi.org/10.1007/s10899-014-9455-4

We report data collected in a representative sample of 17-year-old Norwegians to investigate prevalence rates of non-problem, risk, and problem gambling, as measured by the Problem Gambling Severity Index (PGSI). In addition, we explored the importance of demographic, personality, motivational, social, and health variables explaining variance in adolescent gambling. Prevalence rates of risk and problem gambling were low but similar to those found in previous studies outside of Norway using the PGSI in adolescent samples. With regard to the relative importance of the various covariates, we found that motivational variables (future gambling intentions, attitudes toward gambling, and gambling-related knowledge) distinguished best between those who did not gamble, non-problem gamblers, and risk and problem gamblers. Furthermore, social variables were important covariates of adolescent gambling; significant associations were found for family and friends' approval of gambling, parental monitoring, father's level of education, and having relatives or friends with a history of a gambling disorder. We discuss possible reasons for differences between the covariates with regard to their importance for explaining adolescent gambling and address implications for future research.

**ИИ:** + · обе модели · опрос населения об азартных играх · Representative adolescent survey using PGSI; the full text may report gambling activities, including sports betting.

**Решение:** =

---

### 1209 · R6348

**Sports betting and advertising**

2014 · article · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the title could mean a commentary or a survey of bettors that may have measured problem gambling.

**Решение:** =

---

### 1210 · R6349

**The gambling behavior of indigenous Australians.**

2014 · Journal of gambling studies · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1007/s10899-013-9358-9

Abstract The gambling activities of minority groups such as Indigenous peoples are usually culturally complex and poorly understood. To redress the scarcity of information and contribute to a better understanding of gambling by Indigenous people, this paper presents quantitative evidence gathered at three Australian Indigenous festivals, online and in several Indigenous communities. With support from Indigenous communities, the study collected and analyzed surveys from 1,259 self-selected Indigenous adults. Approximately 33 % of respondents gambled on card games while 80 % gambled on commercial gambling forms in the previous year. Gambling participation and involvement are high, particularly on electronic gaming machines (EGMs), the favorite and most regular form of gambling. Men are significantly more likely to participate in gambling and to gamble more frequently on EGMs, horse/dog races, sports betting and instant scratch tickets. This elevated participation and frequency of gambling on continuous forms would appear to heighten gambling risks for Indigenous men. This is particularly the case for younger Indigenous men, who are more likely than their older counterparts to gamble on EGMs, table games and poker. While distinct differences between the gambling behaviors of our Indigenous sample and non-Indigenous Australians are apparent, Australian Indigenous behavior appears similar to that of some Indigenous and First Nations populations in other countries. Although this study represents the largest survey of Indigenous Australian gambling ever conducted in New South Wales and Queensland, further research is needed to extend our knowledge of Indigenous gambling and to limit the risks from gambling for Indigenous peoples.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of 1,259 Indigenous adults that measured sports betting participation; the abstract doesn't say whether a problem-gambling instrument such as the PGSI was used.

**Решение:** =

---

### 1211 · R6364

**The Effects of College Students" Sport Value on Sport Gambling Perception and Addiction**

2014 · Journal of Sport and Leisure Studies · article · en · https://doi.org/10.51979/kssls.2014.08.57.651

The purpose of this study was to investigate the relationship ebtween sport value and sport gambling pe-rception, cognition of college students. To fulfill this purpos,e a total of 240 college students were selected a sresearch participants, using the convenience sampling method. iFnally, 215 surveys were used for this study . Subjects were analyzed with t-test, exploratory factor analysi,s Cronbach``s α, multiple regression analysis andChi-square. The findings of this study were as follows; First, characteristic, recreational, economic values outof sub-factors of college students`` sport value had an impact on sport gambling perception. Second, collegestudents`` sport value partially effected on sport gambling addiction. Precisely, the level of characteristic, recreationalvalues had an impact on sport gambling addiction. Thir,d college students`` sport gambling perceptionaffected sport gambling addiction. The results of this study wll iprovide policy implications for the preventionof sport gambling addiction for college students.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Korean college student survey measuring sport gambling addiction; abstract doesn't say which instrument was used or whether it is validated.

**Решение:** =

---

### 1212 · R6365

**Media Interactivity and Fantasy Sport**

2014 · Media peripheries : · article · en · https://doi.org/10.11157/medianz-vol11iss1id57

Media Interactivity and Fantasy Sport

**ИИ:** разошлись — Opus ? (нет аннотации: No abstract; likely a media-studies chapter on fantasy sport, but a survey with a problem-gambling measure can't be ruled out.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Media-studies paper on fantasy sport and interactivity from a media journal; the abstract is only the title, and nothing suggests a gambling or problem-gambling survey.)

**Решение:** ?

---

### 1213 · R6373

**Breadth and depth involvement: Understanding Internet gambling involvement and its relationship to gambling problems.**

2014 · Psychology of addictive behaviors : journal of the Society of Psychologists in Addictive Behaviors · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1037/a0033810

The "involvement effect" refers to the finding that controlling for gambling involvement often reduces or eliminates frequently observed game-specific associations with problem gambling. In other words, broader patterns of gambling behavior, particularly the number of types of games played over a defined period, contribute more to problem gambling than playing specific games (e.g., lottery, casino, Internet gambling). This study extends this burgeoning area of inquiry in three primary ways. First, it tests independently and simultaneously the predictive power of two gambling patterns: breadth involvement (i.e., the number of games an individual plays) and depth involvement (i.e., the number of days an individual plays). Second, it includes the first involvement analyses of actual betting activity records that are associated with clinical screening information. Third, it evaluates and compares the linearity of breadth and depth effects. We conducted analyses of the actual gambling activity of 1,440 subscribers to the bwin.party gambling service who completed an online gambling disorder screen. In all, 11 of the 16 games we examined had a significant univariate association with a positive screen for gambling disorder. However, after controlling for breadth involvement, only Live Action Internet sports betting retained a significant relationship with potential gambling-related problems. Depth involvement, though significantly related to potential problems, did not impact game-based gambling disorder associations as much as breadth involvement. Finally, breadth effects appeared steeply linear, with a slight quadratic component manifesting beyond four games played, but depth effects appeared to have a strong linear component and a slight cubic component.

**ИИ:** + · обе модели · беттеры + инструмент · bwin subscribers screened for gambling disorder; game-specific associations including live-action sports betting reported.

**Решение:** =

---

### 1214 · R6374

**Does the Living Room Become the Fantasy Front Office ? A Cognitive Evaluation of the Consumption Habits of Fantasy Sport Users**

2014

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; fantasy sport consumption study, probably sport marketing without a problem-gambling measure, but this can't be confirmed from the title.

**Решение:** =

---

### 1215 · R6375

**Examining the structural relationships among gambling motivation, passion, and consequences of internet sports betting.**

2014 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-013-9400-y

The rise in popularity of Internet gambling has led to new gambling controversies among researchers and policymakers alike. Opponents frequently point to the negative impacts of problem gambling, while advocates tend to view this form of gambling as relatively harmless and convenient entertainment for the vast majority of participants. Interestingly, in making their points, both sides cite empirical arguments about passion for the gambling act-with opponents arguing that Internet gambling enables unhealthy obsessions, and advocates pointing to the apparent intensive interest of large numbers of Internet players. As it turns out, both sides may have a point. In this paper, we examine whether types of passion were related to types of motivation and consequences. The data were collected through a sample from an online gambling website in South Korea. We rely upon Rousseau et al.'s (J Gambl Stud 18(1):45-66, 2002) seminal work on positive and negative aspects of passion, and in the process we develop a framework for understanding positive and negative consequences of this form of gambling. The results reveal that intrinsic gambling motivations (e.g., gambling for excitement) is related to harmonious passion, which in turn results in positive consequences. Meanwhile, extrinsic gambling motivations (e.g., money) is related to obsessive passion, which in turn results in negative consequences.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of Korean internet sports bettors; the abstract doesn't say whether negative consequences were measured with a problem-gambling instrument.

**Решение:** =

---

### 1216 · R6376

**Positive and Negative Effects of Sport Betting Industry**

2014 · Kookmin Social Science Reviews · article · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; title suggests an industry or policy discussion, but a survey measuring problem gambling can't be ruled out.

**Решение:** =

---

### 1217 · R6377

**The role of responsible gambling strategy and gambling passion in the online gamblers' decision-making process: revising the theory of planned behavior.**

2014 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-013-9359-8

This study revised the theory of planned behavior (TPB) by incorporating the new concepts of gambling passion and responsible gambling strategy (RGS) to predict gamblers' intention to gamble in online sports betting. The data were collected at the end of March in 2012 through an online gambling website. The findings indicated that the inclusion of two types of gambling passion and two types of RGS explains online gambling intention well. Specifically, out of the original antecedent predictors of TPB, attitude toward online gambling was positively related to harmonious passion. Subjective norm had a positive relationship with both harmonious and obsessive passion. The results also showed that perceived behavioral control does not have a significant effect on the two gambling passions but has a direct and significant influence on behavioral intention. Additionally, the compulsory RGS had a negative effect on obsessive passion, whereas supplementary RGS had concurrent positive impacts on harmonious and obsessive passion. Lastly, the two gambling passions were notable predictors of behavioral intention toward online sports betting.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of online sports bettors on TPB constructs and passion; abstract doesn't say whether a problem-gambling instrument was used.

**Решение:** =

---

### 1218 · R6391

**Fantasy sports, real money: exploration of the relationship between fantasy sports participation and gambling-related problems.**

2014 · Addictive behaviors · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1016/j.addbeh.2014.05.017

Participation in fantasy sports increases annually. Wagering on fantasy sports is a form of gambling and researchers have found that fantasy sports participants are more likely to engage in other forms of sports betting than non-fantasy players; however, no published studies have examined whether there is a relationship between fantasy sports participation and gambling-related problems. Our study examined whether fantasy sports participation is associated with gambling-related problems among college students. We assessed fantasy sports participation and endorsement of DSM-5 gambling disorder (GD) criteria among a large convenience sample (N=1556) of college students via an online health survey. We found that 11.5% of respondents participated in fantasy sports in the past year, the majority of which were males. Logistic regression analyses indicated that males who play fantasy sports for money and females who play fantasy sports (for money or not) were more likely to experience gambling-related problems.

**ИИ:** + · обе модели · беттеры + инструмент · College survey of fantasy sports participation for money, with DSM-5 gambling disorder criteria measured.

**Решение:** =

---

### 1219 · R6394

**Extending Sports Wagering Studies Outside of the Student-Athlete Population: NCAA Division I Athletic Trainers' Gambling Behaviors**

2014 · Scholar Commons (University of South Carolina) · article · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Survey of athletic trainers' sports wagering with no abstract; unclear if a problem-gambling instrument was used.

**Решение:** =

---

### 1220 · R6406

**Perceived Social Impacts of Legalized Betting: The Case of Famagusta, TRNC**

2014 · Eastern Mediterranean University (EMU) - Doğu Akdeniz Üniversitesi (DAÜ) · master thesis, thesis · eng · https://hdl.handle.net/11129/1656

ABSTRACT: Over time, the features of gaming in TRNC has been altering, influenced mostly by the establishment of the gaming, but in addition to the growing accessibility of other types of gaming like widespread sport-betting and online betting. Even as there is mounting attention on the perceived social impacts of these new types of gaming on TRNC residents. The scale of betting have been on the rise after betting in Turkey was banned in 1997 and Turkish betting operators moved their activities over to northern Cyprus, which, as a result have made TRNC ‘oversea betting reserve for Turkey and the Middle Easterners, from 2003, for Greek Cypriot bettors, recently allowed to go over to the north. Betting-related issues can be perceived to have both social cost and benefit to bettors, the family and the entire society. Betting problems can result from detrimental effects of individuals betting habit. This researched was carried out using quantitative research procedure facilitated with the help of structure questionnaires given to respondent in different betting offices. It was observed that legalized betting is of benefit to both the bettors and the city. This study used the term problem betting extensively as a means to describe the variety of problems caused by pathological betting. The investigation covered several areas relating to betting expansion, cost and benefit of betting, emerging trends, the scale of betting and the motivation for betting. Sport betting in the city is a male dominated activity performed mostly by youths. Despites the low scale of pathological betting, this study reveals that other forms of betting problem persists. The involvement of all stakeholders in the betting process will ensure problem free betting. Keyword: Gaming, betting, perceived social impacts, accessibility, betting-related, social cost and benefits, betting problems, pathological betting, stakeholders. ………………………………………………………………………………………………………………………… ÖZ: Zamanla kumar kuruluşlarının ortaya çıkmasıyla ve yaygınlaşmış spor bahisleri ile internet üzerinden oynanan bahisler gibi giderek erişimine kolayca ulaşılan diğer kumar türleri KKTC’deki kumar özelliklerini değiştirmeye başlamıştır. Bu tür kumar oyunlarının sosyal etkileri bilinmesine rağmen KKTC sakinleri bunları edinmiştir. Kumar oyunları 1997’de Türkiye’de yasaklandığı için 2003’ten itibaren Türk kumar operatörleri aktivitelerini Kuzey Kıbrıs’a taşıyarak kumar oranlarını arttırmış ve son zamanlarda Türk tarafına geçişi olan Kıbrıslı Rum kumarcılar ile Türkiye ve Orta Doğululara KKTC’den denizaşırı kumar oyunları tahsis etmektedir. Kumar içerikli konular ailelere ve tüm topluma hem sosyal maliyet hemde bahiscilere kazanç olarak sonuçlanabilir. Bu çalışma, yapılandırılmış anket desteğiyle nicel yordam izlenerek değişik bahis ofislerinde bahiscilere uygulanmıştır. Yasallaştırılmış kumar hem kumar isletmeciliği yapan kişilere hem de şehire yaralı olduğu gözlemlenmiştir. Bu çalışma bahis problemleri terimi anlamsız/patolojik bahislerin neden olduğu çeşitli problemleri tanımlamak amacıyla kapsaplı olarak kullanmiştır. Söz konusu araştırma kumarın yaygınlaşması, zararları ve yararları, yeni trendleri, bahis boyutunu ve kumar oynama kaynaklarını kapsayan çesitli alanlarını ele almıştır. Spor oyunları (bahisleri) erkek cinsin baskın olduğu ve gençlerin oynadığı bir kumar çeşididir. Düşük oranda saptanan anlamsız/patolojik kumar oynama dışında, bu çalışmada kumar oynama alışkanlığının sürüp gideceğini açığa çıkarmıştır. Kumar oynayan insanların varlığı kumarın serbest olarak sürreceğini garanti etmektedir. Anahtar Kelimeler: kumar, bahis, sosyal etki algısı, erişebilirlik, kumar-kaynaklı, sosyal kayıp ve kazançlar, kumar problemleri, patolojik kumar, katılımcı.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Questionnaire survey of sports bettors in betting offices reports a low level of pathological betting; unclear whether a validated instrument was used.

**Решение:** =

---

### 1221 · R6413

**Senior gambling in Hong Kong: through the lenses of Chinese senior gamblers – an exploratory study**

2014 · Asian Journal of Gambling Issues and Public Health · article · en · https://doi.org/10.1186/s40405-014-0004-y

The meanings of gambling among senior gamblers in Hong Kong were investigated using semi-structured interviews based on an ethnographic approach. 18 senior gamblers (10 men; 8 women) over the age of 55 years were asked to describe their childhood, adolescent and early adult experience and developmental history of gambling and gambling trajectories. They also completed the Problem Gambling Severity Index (PGSI) of the Canadian Problem Gambling Index. Most senior gamblers ( n = 15) were non-problem gamblers, except 3 participants who were classified as pathological gamblers. The majority of the senior gamblers began their lifelong gambling career when they were young. Their family members often introduced the participants to gambling. Some participants reported that an early big win was a focal memorable experience in their early gambling history. Women played mahjong most frequently, whereas men gambled on horse races and sports betting such as football lotteries. The main motivation of gambling for older adult women was socialisation with friends, whereas older adult men were motivated to gamble because of potential financial gain. To senior women, games of mahjong with friends have provided an oasis and a comfort zone, within which they can find peace and comfort away from hustles of daily life. Cultural conditions in Hong Kong and their link to senior gambling have been also discussed.

**ИИ:** ? · обе модели · другое · Mainly qualitative interviews with 18 seniors, but the PGSI was given and some bet on football lotteries; a participant table could cross these.

**Решение:** =

---

### 1222 · R6419

**Gambling and the Onset of Comorbid Mental Disorders**

2014 · Journal of Psychiatric Practice · article · en · https://doi.org/10.1097/01.pra.0000450320.98988.7c

While the association between gambling disorders and comorbid mental disorders has been extensively studied, only a few studies have used longitudinal data or evaluated the association across different levels of gambling behavior and specific gambling-related symptoms. In this study, longitudinal data from waves 1 and 2 of the National Epidemiological Survey on Alcohol and Related Conditions (NESARC) were used to determine whether different levels of gambling behavior and gambling-related symptoms were associated with the onset of psychiatric disorders. Although NESARC used DSM-IV diagnoses, for this study, the recently published DSM-5 diagnostic criteria for gambling disorder were used to group the NESARC respondents (N=34,653) into three levels of gambling (gambling disorder, sub-threshold gambling disorder, and recreational gambling) and one non-gambling comparison group. Three years after the initial intake interview, compared to the non-gamblers, those reporting any gambling behavior at baseline were at increased risk to have any mood, anxiety, or substance use disorders (recreational gambling: adjusted odds ratio [AOR]=1.16, 95% confidence interval [CI]=1.10-1.23; sub-threshold gambling disorder: AOR 1.77, 95% CI 1.63-1.92; gambling disorder: AOR 2.51, 95% CI 1.83-3.46). Similar graded relationships were found for a number of specific disorders. In addition, multiple specific gambling-related symptoms were associated with comorbid disorders, possibly suggesting the interaction of different mechanisms linking gambling disorder and the onset of comorbid psychopathology. In conclusion, a graded or dose-response relationship exists between different levels of gambling and the onset of comorbid psychopathology. Among gambling groups, those with a gambling disorder were at the highest risk for the new onset of comorbid conditions and those with recreational gambling were at the lowest risk, while the risk among participants with sub-threshold gambling disorder fell between these two groups.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · National NESARC survey using DSM-based gambling disorder criteria; unclear whether sports betting participation was measured or reported.

**Решение:** =

---

### 1223 · R6433

**Identifying indicators of harmful and problem gambling in a Canadian sample through receiver operating characteristic analysis.**

2014 · Psychology of addictive behaviors : journal of the Society of Psychologists in Addictive Behaviors · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1037/a0032801

Many gamblers would prefer to reduce gambling on their own rather than to adopt an abstinence approach within the context of a gambling treatment program. Yet responsible gambling guidelines lack quantifiable markers to guide gamblers in wagering safely. To address these issues, the current investigation implemented receiver operating characteristic (ROC) analysis to identify behavioral indicators of harmful and problem gambling. Gambling involvement was assessed in 503 participants (275 psychiatric outpatients and 228 community gamblers) with the Canadian Problem Gambling Index. Overall gambling frequency, duration, and expenditure were able to distinguish harmful and problematic gambling at a moderate level. Indicators of harmful gambling were generated for engagement in specific gambling activities: frequency of tickets and casino; duration of bingo, casino, and investments; and expenditures on bingo, casino, sports betting, games of skill, and investments. Indicators of problem gambling were similarly produced for frequency of tickets and casino, and expenditures on bingo, casino, games of skill, and investments. Logistic regression analyses revealed that overall gambling frequency uniquely predicted the presence of harmful and problem gambling. Furthermore, frequency indicators for tickets and casino uniquely predicted the presence of both harmful and problem gambling. Together, these findings contribute to the development of an empirically based method enabling the minimization of harmful or problem gambling through self-control rather than abstinence.

**ИИ:** разошлись — Opus + (игроки, есть ставки на спорт и инструмент: Community gamblers and psychiatric outpatients were assessed with the CPGI, including sports betting involvement, so sports bettors could be cross-tabulated with problem gambling.); Sonnet ? (другое: CPGI measured with sports betting activity in a mixed sample of psychiatric outpatients and community gamblers. Unclear whether PG among sports bettors is reported; full text needed.)

**Решение:** ?

---

### 1224 · R6436

**The extent and distribution of gambling harm in Finland as assessed by the Problem Gambling Severity Index**

2014 · European Journal of Public Health · article · en · https://doi.org/10.1093/eurpub/cku210

BACKGROUND: Preventing gambling harm has become a policy priority in many European countries. Adverse consequences related to problem gambling are well known, but few studies have analyzed gambling-related harm in detail in general population samples. We determined the extent and distribution of gambling harm in Finland, as assessed by the Problem Gambling Severity Index (PGSI), and analyzed gambling involvement, demographics and their association with various types of harm. METHODS: A nationwide telephone survey was conducted among 4484 Finns aged 15-74 years in 2011-12. Gambling-related harms were based on the nine-item PGSI. Gambling involvement was measured by gambling frequency and weekly average gambling expenditure. Associations among harms, demographics and gambling involvement were examined in logistic regression. RESULTS: During the previous year, 13% of respondents experienced at least one gambling-related harm (males 18.1%, females 7.2%). The four commonest harms were 'chasing losses' (8.6%), 'escalating gambling to maintain excitement' (3.1%), 'betting more than could afford to lose' (2.8%), and 'feeling guilty' (2.6%). The harm profile in descending order was the same for both genders but differed in prevalence. Young age (<25 years) was associated with increased likelihood of reporting harms. Both monthly and weekly gambling and spending over €21 per week on gambling were related to the harms. CONCLUSIONS: Our results provide support for the public health approach to gambling: harms were reported even at low gambling frequency-expenditure levels. In addition to the high-risk approach, adopting a population-level approach to preventing gambling harm could shift the population distribution of harm in a lower direction.

**ИИ:** + · обе модели · опрос населения об азартных играх · Finnish national gambling survey using PGSI; the full text may include problem-gambling figures broken down by gambling activity, including sports betting.

**Решение:** =

---

### 1225 · R6437

**Problem Gambling among Athletes in the United Kingdom**

2014 · Palgrave Macmillan UK eBooks · other literature type, part of book or chapter of book, book-chapter · en · https://doi.org/10.1057/9781137272423_6

Gambling among athletes has increasingly attracted the interest of policymakers and key stakeholders over recent years. This has been fuelled by high-profile cases of elite sports people disclosing extreme gambling behaviour. For example, John Daly, a leading American golfer, claims to have lost over $50m in his autobiography (Daly & Waggoner, 2006). More recently, allegations regarding the fixing of horse races by owners and jockeys (Lees, 2009) and of the bowling of deliberate no-balls (spot-fixing bets) by Pakistani cricketers in a match against England (Mahmood & Evans, 2010) have served to highlight the issue of corruption related to sports gambling. Despite this, only a limited body of empirical work has explored the extent of problem gambling among athletes (e.g. Ellenbogen et al., 2008; Engwall et al., 2004), and there is no empirical research in UK athletes. These keywords were added by machine and not by the authors. This process is experimental and the keywords may be updated as the learning algorithm improves.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Probably an empirical study of problem gambling in UK athletes, with sports gambling as context; sports betting and the instrument should be checked in the full text.

**Решение:** =

---

### 1226 · R6439

**Prevention of gambling and sports betting among youth - synthesis of science, theory and practice**

2014 · conference object, article · en

Od 2010. godine na Edukacijsko-rehabilitacijskom fakultetu provodi se znanstveno-istraživacki projekt pod nazivom „Kockanje mladih u Hrvatskoj“. U okviru projekta proveden je znacajan broj znanstveno-istraživackih i strucnih aktivnosti, a prevalencijska studija provedena je s N=2.702 srednjoskolaca u sedam hrvatski gradova (Zagreb, Split, Rijeka, Osijek, Koprivnica, Slavonski Brod i Vinkovci). Ova studija je, uz ucestalost kockanja i klađenja utvrdila i zastupljenost stetnih psihosocijalnih posljedica, kao i korelate koji doprinose njihovom razvoju. Dobiveni rezultati ukazuju na potrebu sveobuhvatnog, multidisciplinarnog i međuresornog pristupa ovom fenomenu, kao i potrebu za kreiranjem sirokog spektra intervencija s ciljem prevencije i tretmana ovog rizicnog ponasanja. Kao odgovor na jedan segment potreba, u okviru projekta osmisljen je i kreiran preventivni program kockanja mladih pod nazivom „Tko zapravo pobjeđuje?“. Radi se o programu univerzalne prevencije kockanja mladih, sto znaci da je svojim sadržajem i nacinom implementacije namijenjen opcoj populaciji adolescenata u dobi od 14-16 godina, dakle mladima koji se angažiraju u aktivnostima povezanim s kockanjem, ali jos nisu razvili probleme povezane s kockanjem do mjere da bi im bile potrebne intenzivnije intervencije, odnosno tretman. Program je vremenski usklađen s potrebama korisnika na nacin da je usmjeren na rizicne cimbenike prije nego se problem pojavi, ali i na nacin da sadržajem obuhvaca rizicne i zastitne cimbenike koji su relevantni u odnosu na razvojno razdoblje adolescencije u kojem se korisnici programa nalaze. Program je osmisljen i implementiran tako da se temelji na znanstveno dokazanim i međunarodno priznatim principima uspjesnih preventivnih programa kockanja mladih. Karakteriziraju ga sljedeca obilježja: (1) sveobuhvatnost u pristupu, (2) utemeljenost na teoriji i empirijskim rezultatima istraživanja, (3) koristenje raznolikih metoda ucenja, (4) dostatno trajanje, (5) promicanje pozitivnih odnosa, (6) razvojna usklađenost s korisnicima, (7) socijalno-kulturalna prikladnost, (8) educirani provoditelji programa, te (9) evaluacija ucinka i procesa. U pilot verziji preventivni program kockanja mladih „Tko zapravo pobjeđuje?“ sastoji se od 6 tematskih cjelina koje se provode unutar 90 minuta (2 skolska sata), dok je nakon prve primjene modificiran u 8 radionica u trajanju od 45 minuta (1 skolski sat). Opci cilj programa je prevencija kockanja i klađenja maloljetnika, te razvoj ispravnog odnosa prema igrama na srecu, kao i osobno odgovornog ponasanja u ovom podrucju. Program kombinira razvijanje specificnih znanja, sa specificnim vjestinama važnim za razvoj otpornosti prema razvoju stetnih psihosocijalnih posljedica kockanja. U izlaganju ce biti prikazana znanstveno i teorijsko utemeljenje programa, kao i rezultati prve evaluacije ucinka koji su pokazali da je program ostvario svoje temeljne ciljeve. Također je pozitivno da evaluacija pokazuje i da su primarni korisnici (srednjoskolci) zadovoljni programom i vide korist od sudjelovanja, te bi vecina njih ovaj program preporucila i svojim prijateljima. Isto vrijedi i za roditelje i njihovo zadovoljstvo predavanjem i predavacem. Procjene subjektivne koristi jos su vece od samog zadovoljstva programom, sto je dodatni pokazatelj da je program postigao sve postavljene ciljeve.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Conference talk mainly on a youth prevention program; it summarises a survey of 2,702 students covering betting and gambling harms, but the instrument used is unclear.

**Решение:** =

---

### 1227 · R6440

**Youth Sports Betting - The Croatian Perspective**

2014 · other literature type · eng · https://www.bib.irb.hr/750986

This text consists of the following chapters: 1. The Social Context of Gambling 2. Youth Sports Betting Research Study

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Croatian youth sports betting research study; abstract doesn't say whether a problem-gambling instrument was used.

**Решение:** =

---

### 1228 · R6445

**Betting on Sports Betting**

2014 · Gaming Law Review and Economics · article, journalarticle, journal-article · en · https://doi.org/10.1089/glre.2014.18102

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: No abstract. The gaming-law venue suggests legal or policy commentary, but empirical content can't be ruled out from the title alone.); Sonnet -1 (обзор, комментарий, теоретическая, правовая или регуляторная работа: No abstract; the title and venue (Gaming Law Review and Economics, 2014) suggest a legal or policy commentary, likely with no prevalence data.)

**Решение:** ?

---

### 1229 · R6457

**First Evidence of Comorbidity of Problem Gambling and Other Psychiatric Problems in a Representative Urban Sample of South Africa**

2014 · Journal of Gambling Studies · article · en · https://doi.org/10.1007/s10899-014-9469-y

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; representative urban South African survey measuring problem gambling; unclear whether sports betting participation was recorded.

**Решение:** =

---

### 1230 · R6458

**Trends in Gambling Behavior among College Student-Athletes: A Comparison of 2004 and 2008 NCAA Survey Data**

2014 · Journal of Gambling Issues · article, review · en · https://doi.org/10.4309/jgi.2014.29.18

Two large samples of National Collegiate Athletic Association (NCAA) student-athletes in 2004 (N = 18,916) and 2008 (N = 17,675) were surveyed about their gambling behavior. A cross-comparison highlighted gambling trends among college-student athletes across the four-year span. Overall, past-year and weekly gambling rates were lower in 2008 compared to 2004. There were no within-gender differences in the proportion of individuals at-risk or meeting criteria for a gambling problem between 2004 (4.0% males, 0.3% females) and 2008 (3.8% males, 0.4% females). Participation rates were higher in 2004 for all gambling activities, except for past-year Internet gambling and sports wagering, which increased in 2008 among males. Across sports, gambling participation was notably highest among golfers of both genders. Collectively, the results suggest that gambling activity among student-athletes is on a downward trend in spite of ongoing expansion of gambling opportunities.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · NCAA student-athlete surveys measured sports wagering participation and at-risk or problem gambling, likely with a DSM-based screen.

**Решение:** =

---

### 1231 · R6465

**Freizeit- und Glücksspielverhalten Jugendlicher und junger Erwachsener**

2014 · article · de

Risiken von Glücksspielen um Geld, insbesondere auch für Jugendliche, sind seit geraumer Zeit Gegenstand der politischen und gesellschaftlichen Diskussion. Das vorliegende Buch diskutiert die Forschungslage zum Glücksspielen in Deutschland und stellt die Ergebnisse einer Studie vor, die dazu beitragen soll, die empirische Grundlage für die Ableitung wirksamer Präventionsansätze im Bereich Glücksspielen zu verbessern. Im Rahmen einer breit angelegten Online-Befragung von fast 7.000 Jugendlichen und jungen Erwachsenen in Deutschland wurden über das Spielverhalten hinaus – von Lotto, Sportwetten, Internet-Glücksspiel, bis hin zu Geldgewinnspielgeräten – eine Vielzahl von Daten zum Freizeitverhalten und zur Lebenswelt der Jugendlichen und jungen Erwachsenen erfasst. Dabei zeigte sich u. a., dass Glücksspielen an sich noch kein Hinweis auf eine Problemlage ist, sondern dass bei problematischen Spielern das missbräuchliche Glücksspiel offensichtlich nur ein Symptom vielfältiger dahinterliegender Problematiken ist.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · German online survey of ~7,000 young people that measured sports betting and identified problem gamblers; the instrument used still needs checking in the full text.

**Решение:** =

---

### 1232 · R6472

**¿Qué apostamos? El boom de las casas de apuestas deportivas reafirma el binomio ancestral entre vascos y juego**

2014 · article · es

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; Spanish article on the sports-betting boom in the Basque Country, possibly journalistic, but survey data can't be ruled out.

**Решение:** =

---

### 1233 · R6483

**Sociocultural Influences on Gambling and Alcohol Use Among Native Americans in the United States**

2014 · Journal of Gambling Studies · article · en · https://doi.org/10.1007/s10899-014-9512-z

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; may draw on a US national gambling survey that measured activities and problem gambling. Needs full text.

**Решение:** =

---

### 1234 · R6484

**Gambling disorder: Estimated prevalence rates and risk factors in Macao.**

2014 · Psychology of Addictive Behaviors · article · en · https://doi.org/10.1037/a0037603

An excessive, problematic gambling pattern has been regarded as a mental disorder in the Diagnostic and Statistical Manual for Mental Disorders (DSM) for more than 3 decades (American Psychiatric Association [APA], 1980). In this study, its latest prevalence in Macao (one of very few cities with legalized gambling in China and the Far East) was estimated with 2 major changes in the diagnostic criteria, suggested by the 5th edition of DSM (APA, 2013): (a) removing the "Illegal Act" criterion, and (b) lowering the threshold for diagnosis. A random, representative sample of 1,018 Macao residents was surveyed with a phone poll design in January 2013. After the 2 changes were adopted, the present study showed that the estimated prevalence rate of gambling disorder was 2.1% of the Macao adult population. Moreover, the present findings also provided empirical support to the application of these 2 recommended changes when assessing symptoms of gambling disorder among Chinese community adults. Personal risk factors of gambling disorder, namely being male, having low education, a preference for casino gambling, as well as high materialism, were identified.

**ИИ:** + · обе модели · опрос населения об азартных играх · Representative Macao population survey using DSM-based gambling disorder criteria and gambling preferences; full text may include sports betting by activity.

**Решение:** =

---

### 1235 · R6485

**Internet Gambling Among Community Adults and University Students in Macao**

2014 · Journal of Gambling Studies · article · en · https://doi.org/10.1007/s10899-014-9451-8

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; survey of Macao adults/students on internet gambling likely measured sports betting and problem gambling.

**Решение:** =

---

### 1236 · R6489

**Gambling and Mobile Money Payments: A Case Study of Sports Betting in Uganda (Final Report)**

2014 · eScholarship, University of California · article · und · https://escholarship.org/content/qt06x163x8/qt06x163x8.pdf

The usage of mobile money payment systems has become a popular means of transmitting money across different regions in Uganda because of its low transfer charges, quick and easy process, and availability among the unbanked and rural communities of the population. Around 400,000 customers are currently using mobile payment facilities processing around UGX 1.3 billion (US$ 0.5 million) per day. In spite of Uganda’s rising youth unemployment, which would seem to indicate that the youth do not have spare cash, the reality is that the country’s youth--especially those in urban areas--increasingly participate in sports betting using cash as well as mobile money payments.Nevertheless, there is a knowledge gap with regard to the drivers of sports betting (especially the mobile money payments system) and the socioeconomic implications of this phenomenon. Whereas some betters strike it rich, others continuously lose cash but are not about to stop participating, thereby keeping them in a vicious circle of poverty. This study examines the role of mobile money payments in the practice of gambling in general. Specifically, the study sought to examine the role of mobile money payments (making bets and receipt of payments) in the execution of sports betting in Uganda. An exploratory mixed- methods (qualitative and quantitative) research design was employed. We administered a questionnaire and collected more data using qualitative approaches.The reasons for gambling among youth are not different from those for adult gambling. Young people who gamble report that fun, the opportunity to win money, and the excitement of gambling on games are the top reasons that they participate. Approximately 5.7% of shops offer online betting facilities. 55% of respondents use both cash and mobile money payments to place bets and to receive payments. Approximately only 25% (37) out of 104 sports betting shops in the country are licensed. This finding is corroborated by Okoth (2013) who reported that sports betting is a booming business in the country although most of the companies are operating illegally, which has significant policy implications for the regulatory environment within which sports betting takes place.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Mixed-methods questionnaire survey of Ugandan sports bettors; the abstract does not say whether a problem-gambling instrument was used.

**Решение:** =

---

### 1237 · R6498

**Behavior of watching sports media and playing betting games for high School and college students**

2014 · Hitit University Institutional Repository · article · tr

research

**ИИ:** ? · обе модели · нет аннотации · No usable abstract; this is a student survey on watching sports media and betting games, and it's unclear if problem gambling was measured.

**Решение:** =

---

### 1238 · R6513

**불법 스포츠토토 참여자들의 도박중독수준에 따른 이용행태 및 합법 스포츠토토 전환의사 차이분석**

2014 · 한국체육학회지-인문사회과학 · article · ko

본 연구는 불법 스포츠토토 참여자들의 도박중독수준을 진단하고 이용행태와 합법 스포츠토토 전환의사의 관계를 분석하기 위해 불법 스포츠토토에 참여하는 257명을 대상으로 교차분석, x2 검증, 일원변량분석을 실시하였다. 그 결과는 첫째, 모든 집단에서 ‘20~30대’,‘미혼’,‘대졸이하’의 비율이 높게 나타났다. 둘째, 참여빈도는 문제성 위험군에서 ‘주 3회이상’의 비중이, 1회 평균베팅액은 모든 집단에서 ‘3만원이하’의 비율이 높았고, 참여이유로는 비문제성군, 문제성위험군은 ‘높은 배당률’이, 저위험군, 중위험군은 ‘간편한 구매방법’이, 참여경로는 모든 집단에서 ‘주변인 소개’가 가장 높게 나타났다. 단속에 있어 비문제성군을 제외한 집단들에서 큰 두려움이 없는 경향을 보였고, 단속경험은 문제성위험군에서 비교적 높은 분포로 나타났다. 셋째, 전환의사에 있어 ‘방식의 간편성제고’는 저위험성군과 중위험군이 문제성 위험군보다,‘상품 다양성 제고’는 저위험군이 문제성위험군보다,‘마감시간 제고’는 저위험군이 비문제성군과 문제성위험군보다 높게 나타났다. ‘단속강화’는 비문제성군이 중위험군, 문제성위험군보다,‘처벌강화’는 비문제성군이 나머지 모든 집단보다 낮게 나타났다.

**ИИ:** + · обе модели · беттеры + инструмент · Survey of 257 illegal sports toto bettors grouped as non-problem, low, moderate and problem risk, which suggests the PGSI/CPGI was used.

**Решение:** =

---

### 1239 · R6514

**대학생들의 스포츠가치관이 스포츠도박 인식 및 중독에 미치는 영향**

2014 · review

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Korean survey of university students' sports values and sports gambling addiction; no abstract, so the addiction instrument is unclear.

**Решение:** =

---

### 1240 · R6515

**성인체육 편 : 대학생들의 스포츠가치관이 스포츠도박 인식 및 중독에 미치는 영향**

2014 · review

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Korean survey of university students on sports values, sports gambling perception and addiction; no abstract, and the instrument is unclear.

**Решение:** =

---

### 1241 · R6516

**대학생의 스포츠토토 경험유형에 따른 도박중독 심각성에 대한 차이연구**

2014 · 한국심리학회 학술대회 자료집 · article · ko

연구목적 본 연구는 사설 스포츠를 통한 도박 사이트 전체 가입자 중 20대 대학생이34%의 가장 높은 비율을 차지한다는 연구결과를 토대로 대학생의 사설 스포츠도박을 감소시키기 위한 방법을 모색하기 위하여, 대학생의 스포츠토토 경험유형에 따른 도박중독 심각성을 분석하였다. 특히 스마트폰의 발달을 통하여 불법 스포츠토토에 대한 접근성이 높아져 문제성도박자로 전략하는 사람들이 늘어나고 있으나 이에 연구가 부족한 실정에 있다. 이를 위해서 대학생들의 스포츠토토 경험유형에 따른 도박중독 심각성 및 그에 따른 자아존중감, 내외통제성의차이를 살펴보도록 하였다. 연구방법 서울 및 경기 지역의 대학교를 중심으로 재학 혹은 휴학하는 학생 193명(남=91, 여=102)을 대상으로 설문지를 통해 분석을 하였다. 설문지는 인구통계학적 질문, 사설 스포츠도박경험에 대한 질문, CPGI(Canadian Problem Gambling Index), 자아존중감척도(이영자,1996), 내외통제성 척도(윤유경, 1996)가 포함된 총 59문항으로 이루어져있다. 연구결과 대학생들의 스포츠토토의 구매에 대한 경험을 묻는 질문에서는 총 설문대상자 193명중 33명(17.1%)이 참여 경험이 있는 것으로 나타났다. 또한 스포츠토토 경험 유무에 따른 도박중독 수준을 알아보기 위하여 교차분석을 실시하였다. 경험자 33명 중 28명(84.8%)이 CPGI 중위험 도박 이상으로 나타났다. 반면 스포츠토토를 경험하지 않은 대학생의 경우 19명(11.9%)으로 나타나 통계적으로 유의한 수준(X2=79.081, p<.001)으로 나타났다. 반면 불법스포츠 도박 경험에 따른 도박중독 수준에 따른 교차분석에서는 통계적으로 유의한 수준의 차이는 타나나지 않았다. 가설에서 제시한 스포츠토토경험 유무에 따른 자아존중감, 내외통제성에 대한 차이를 있을 것으로 예상되었으나 t검정을 실시한 결과 통계적으로 유의한 차이를 나타내지 않았다. 기타 스포츠토토 경험에 대한 실태를 조사하였다.

**ИИ:** + · обе модели · беттеры + инструмент · Korean student survey using the CPGI; 28 of 33 Sports Toto bettors (84.8%) scored moderate risk or higher.

**Решение:** =

---

### 1242 · R6517

**포스터 발표 : 대학생 ; 대학생의 스포츠토토 경험유형에 따른 도박중독 심각성에 대한 차이연구**

2014 · article · ko

연구목적 본 연구는 사설 스포츠를 통한 도박 사이트 전체 가입자 중 20대 대학생이34%의 가장 높은 비율을 차지한다는 연구결과를 토대로 대학생의 사설 스포츠도박을 감소시키기 위한 방법을 모색하기 위하여, 대학생의 스포츠토토 경험유형에 따른 도박중독 심각성을 분석하였다. 특히 스마트폰의 발달을 통하여 불법 스포츠토토에 대한 접근성이 높아져 문제성도박자로 전략하는 사람들이 늘어나고 있으나 이에 연구가 부족한 실정에 있다. 이를 위해서 대학생들의 스포츠토토 경험유형에 따른 도박중독 심각성 및 그에 따른 자아존중감, 내외통제성의차이를 살펴보도록 하였다. 연구방법 서울 및 경기 지역의 대학교를 중심으로 재학 혹은 휴학하는 학생 193명(남=91, 여=102)을 대상으로 설문지를 통해 분석을 하였다. 설문지는 인구통계학적 질문, 사설 스포츠도박경험에 대한 질문, CPGI(Canadian Problem Gambling Index), 자아존중감척도(이영자,1996), 내외통제성 척도(윤유경, 1996)가 포함된 총 59문항으로 이루어져있다. 연구결과 대학생들의 스포츠토토의 구매에 대한 경험을 묻는 질문에서는 총 설문대상자 193명중 33명(17.1%)이 참여 경험이 있는 것으로 나타났다. 또한 스포츠토토 경험 유무에 따른 도박중독 수준을 알아보기 위하여 교차분석을 실시하였다. 경험자 33명 중 28명(84.8%)이 CPGI 중위험 도박 이상으로 나타났다. 반면 스포츠토토를 경험하지 않은 대학생의 경우 19명(11.9%)으로 나타나 통계적으로 유의한 수준(X2=79.081, p<.001)으로 나타났다. 반면 불법스포츠 도박 경험에 따른 도박중독 수준에 따른 교차분석에서는 통계적으로 유의한 수준의 차이는 타나나지 않았다. 가설에서 제시한 스포츠토토경험 유무에 따른 자아존중감, 내외통제성에 대한 차이를 있을 것으로 예상되었으나 t검정을 실시한 결과 통계적으로 유의한 차이를 나타내지 않았다. 기타 스포츠토토 경험에 대한 실태를 조사하였다.

**ИИ:** + · обе модели · беттеры + инструмент · Korean student survey; 33 Sports Toto bettors, 84.8% moderate-risk or higher on CPGI.

**Решение:** =

---

### 1243 · R6518

**대학생들의 스포츠가치관이 스포츠도박 인식 및 중독에 미치는 영향**

2014 · article · ko

The purpose of this study was to investigate the relationship ebtween sport value and sport gambling pe-rception, cognition of college students. To fulfill this purpos,e a total of 240 college students were selected a sresearch participants, using the convenience sampling method. iFnally, 215 surveys were used for this study . Subjects were analyzed with t-test, exploratory factor analysi,s Cronbach``s α, multiple regression analysis andChi-square. The findings of this study were as follows; First, characteristic, recreational, economic values outof sub-factors of college students`` sport value had an impact on sport gambling perception. Second, collegestudents`` sport value partially effected on sport gambling addiction. Precisely, the level of characteristic, recreationalvalues had an impact on sport gambling addiction. Thir,d college students`` sport gambling perceptionaffected sport gambling addiction. The results of this study wll iprovide policy implications for the preventionof sport gambling addiction for college students.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Korean college student survey that measured sports gambling addiction; the instrument and the sports betting participation figures aren't stated.

**Решение:** =

---

### 1244 · R6519

**성인체육 편 : 대학생들의 스포츠가치관이 스포츠도박 인식 및 중독에 미치는 영향**

2014 · article · ko

The purpose of this study was to investigate the relationship ebtween sport value and sport gambling pe-rception, cognition of college students. To fulfill this purpos,e a total of 240 college students were selected a sresearch participants, using the convenience sampling method. iFnally, 215 surveys were used for this study . Subjects were analyzed with t-test, exploratory factor analysi,s Cronbach``s α, multiple regression analysis andChi-square. The findings of this study were as follows; First, characteristic, recreational, economic values outof sub-factors of college students`` sport value had an impact on sport gambling perception. Second, collegestudents`` sport value partially effected on sport gambling addiction. Precisely, the level of characteristic, recreationalvalues had an impact on sport gambling addiction. Thir,d college students`` sport gambling perceptionaffected sport gambling addiction. The results of this study wll iprovide policy implications for the preventionof sport gambling addiction for college students.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Korean college student survey measuring sport gambling addiction; the abstract does not name the instrument or say whether a validated screen was used.

**Решение:** =

---

### 1245 · R6520

**Different sports, different identities: player’s heterogeneity and fantasy sport play**

2013 · Routledge eBooks · book-chapter · en · https://doi.org/10.4324/9780203119945-10

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Book chapter on fantasy sport players with no abstract; unclear whether play was for money or whether problem gambling was measured.

**Решение:** =

---

### 1246 · R6521

**Enough is enough: exiting and burnout of fantasy sport participants**

2013 · Routledge eBooks · book-chapter · en · https://doi.org/10.4324/9780203119945-13

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Book chapter on burnout and exiting among fantasy sport participants; no abstract, so it is unclear whether play was for money or problem gambling was measured.

**Решение:** =

---

### 1247 · R6523

**Fantasy sport: the game changer**

2013 · Routledge eBooks · book-chapter · en · https://doi.org/10.4324/9780203119945-8

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Book chapter on fantasy sport with no abstract; probably conceptual or media-focused, but problem-gambling data can't be ruled out.

**Решение:** =

---

### 1248 · R6532

**Gambling and Problem Gambling in Sweden: Changes Between 1998 and 2009**

2013 · Journal of Gambling Studies · article · en · https://doi.org/10.1007/s10899-013-9396-3

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** + · обе модели · опрос населения об азартных играх · Swedish national gambling prevalence surveys (1998, 2009); these likely measured activity participation and problem gambling with SOGS/PGSI.

**Решение:** =

---

### 1249 · R6534

**Gambling Involvement: Considering Frequency of Play and the Moderating Effects of Gender and Age**

2013 · International Journal of Mental Health and Addiction · review, article · en · https://doi.org/10.1007/s11469-013-9452-3

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract. The title suggests a population-survey analysis of how often people play different gambling activities, possibly with a problem-gambling measure such as the PGSI.

**Решение:** =

---

### 1250 · R6545

**Estimating the prevalence of adult problem gambling in Italy with SOGS and PGSI**

2013 · Journal of Gambling Issues · article · en · https://doi.org/10.4309/jgi.2013.28.3

Two assessment measures, the South Oaks Gambling Screen (SOGS), and the Problem Gambling Severity Index (PGSI), were administered to 1,979 participants (53% males, mean age 44.81 years). Results from exploratory and confirmatory factor analyses showed the presence of one single dimension underlying the SOGS and PGSI items. The 2 scales showed high levels of reliability. SOGS and PGSI results were highly correlated and showed positive and significant correlations with measures of gambling behaviour. Probable pathological gamblers identified by SOGS represented 2.05% (95% confidence interval 'CI' '1.17, 2.93') of the adult Italian population, and problem gamblers identified by PGSI represented 2.17% (95% CI '1.26, 3.07') of the population. A more conservative estimate of the prevalence of problem gambling in Italy, corresponding to 1.01% (95% CI '0.39, 1.63') of the adult population, was identified by considering only those participants for whom SOGS and PGSI were in perfect agreement concerning risk categories.

**ИИ:** + · обе модели · опрос населения об азартных играх · National adult prevalence survey in Italy using SOGS and PGSI with gambling behaviour measures; may report problem gambling by activity, including sports betting.

**Решение:** =

---

### 1251 · R6558

**The Influential Factors and Mechanism of Purchasing Lottery Addiction of Sports Lottery Players**

2013 · Sport Science and Technology · review, article · en

To explore the influential factors and mechanism of purchasing lottery addiction of sports lottery player,2426sports lottery players from 10provinces have been surveyed by means of questionnaire and mathematical statistics.Based on correlation analysis and structure equation models,the results showed that firstly,the purchasing lottery addiction has significantly positive correlation with sensation seeking,economic utility and unhealthy information dissemination,but negative with family economics.Secondly,sensation seeking,economic utility,family economics and unhealthy information dissemination are influential factors for purchasing lottery addiction.Thirdly,economic utility is a partial mediator between family economics,unhealthy information dissemination and purchasing lottery addiction.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of 2426 China sports lottery players measuring lottery addiction; abstract doesn't say whether a validated problem-gambling instrument was used.

**Решение:** =

---

### 1252 · R6559

**More than just an excuse to watch sports all day: why people participate in fantasy sport**

2013 · Routledge eBooks · book-chapter · en · https://doi.org/10.4324/9780203119945-9

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Book chapter on motives for fantasy sport participation; no abstract, and the title points to motives with no problem-gambling instrument.); Sonnet ? (нет аннотации: No abstract; chapter on motives for fantasy sport participation, likely motives only, but unclear whether money was wagered or problem gambling was measured.)

**Решение:** ?

---

### 1253 · R6580

**An analysis of problem gambling among the Finnish working-age population: a population survey**

2013 · BMC Public Health · article · en · https://doi.org/10.1186/1471-2458-13-519

BACKGROUND: Gambling problems currently affect approximately 100,000 Finns. In order to prevent and reduce gambling-related harms it is crucial for the Finnish public health authorities to gain a stronger understanding of the association between gambling problems and related socio-demographic factors, other commonly co-occurring dependencies (e.g. alcohol and nicotine) and the type of games gambled. In this article the prevalence of problem gambling in Finland and the socio-demographic profiles of problem gamblers are studied. METHOD: An annual postal survey entitled Health Behaviour and Health among the Finnish Adult Population AVTK was sent to a random sample of Finnish adults (N=5000) aged between 15 and 64. The sample was derived from the Finnish Population Register. The survey was mailed to the participants in April 2010. Gender differences in socio-demographic variables and Problem Gambling Severity Index PGSI were assessed. A multinomial regression model was created in order to explore the association between socio-demographic factors and the severity of gambling. RESULTS: A total of 2826 individuals (1243 males and 1583 females) replied to the survey. Of the respondents, 1.1% (2.1% of males, 0.3% of females) were identified as problem gamblers. Those who were of younger age, gender, had less than twelve years of education, consumed alcohol at risk level and smoked had higher odds of having low or moderate levels of gambling problems. Whereas, unemployment and smoking predicted significantly for problem gambling. Females gambled Lotto and slot machines less frequently than males and had more low level gambling problems. Males gambled more with a higher frequency and had a more severe level of gambling problems. Females were more attracted to scratch card gambling and daily Keno lotteries compared to males. In comparison, males gambled more on internet poker sites than females. Overall, a high frequency of gambling in Lotto, daily lotteries, slot machines, horse race betting and internet gambling was significantly associated with a more severe level of problem gambling. CONCLUSION: Gambling problems affect tens of thousands of individuals annually, therefore certain vulnerabilities should be noted. Comorbid dependencies, smoking in particular, ought to be screened for and recognised in the public health sector. Regulating the availability of slot machine gambling and enforcement of the age limit should be acknowledged. In establishing new gambling venues, prevalence rates in those particular areas should be actively monitored.

**ИИ:** + · обе модели · опрос населения об азартных играх · Finnish population survey with PGSI and gambling by game type; sports betting is likely among the activities measured.

**Решение:** =

---

### 1254 · R6584

**Social Strain, Self-Control, and Juvenile Gambling Pathology**

2013 · Youth & Society · article · en · https://doi.org/10.1177/0044118x13477869

Despite recent concerns over youthful problem gambling, few gambling studies have looked into Asian adolescent populations. This study of a stratified, random sample of high school students in Hong Kong is designed to estimate the prevalence of gambling pathology among Chinese adolescents and to examine the relationships between social strain, self-control and gambling pathology. Based on the DSM-IV-J gambling screen, the rates of probable pathological gambling and at-risk gambling in this sample are 1.1% and 2.4%, respectively. Social strain and low self-control are predictive of gambling pathology, and a higher level of self-control can dilute the adverse effect of social strain on gambling pathology. These findings suggest that besides the social control, support and learning mechanisms often emphasized in juvenile gambling research, a greater understanding of the role that social strain plays and how it interacts with personality traits such as self-control may be informative in the management of gambling-related addictions in adolescents.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Hong Kong adolescent prevalence survey using DSM-IV-J; football betting participation likely but not stated in the abstract.

**Решение:** =

---

### 1255 · R6610

**Session 2-3-C: Sports betting of adolescents in Croatia: from favorable environment to psychosocial consequences**

2013 · Digital Scholarship - UNLV (University of Nevada Reno) · conference-paper · en

Social context Expansion of places registered for gambling, especially sports betting Croatian Law on Games of Chance (2009.) Sports betting is illegal for minors (<18) Minimum 200 meters from schools

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Conference paper on adolescent sports betting and its psychosocial consequences in Croatia; likely a survey, but the abstract doesn't say whether a problem-gambling instrument was used.

**Решение:** =

---

### 1256 · R6611

**Sports betting of adolescents in Croatia: from favorable environment to psychosocial consequences**

2013 · conference object, article · en

All forms of gambling are prohibited for minors (persons under the age of 18) by Croatian Law on Games of Chance. Current and contemporary research in Croatia confirms that minors have access to different types of games of chance - mostly to sports betting which is a widespread activity especially among the younger population of boys (around 34% of high-school boys regularly bet on sport events). This presentation is a part of the scientific project “Habits and characteristics of adolescent gambling in Croatian urban areas” conducted on a representative sample of high-school students (N=1.952) from 4 major urban centers in Croatia. Since 42.67% of all participants reported betting on sports at least once in their lifetime, results in this presentation are based on a total of 833 adolescents - 77.1% boys and 22.9% girls. Mean age is M=16.73 (SD=1.15). Our aim was to explore how many high-school students report that their parents and friends play games of chance, how often they gamble and do they gamble together. We also explored the intensity of different psychological, social, financial and behavioral consequences that have negative impact on their psychosocial development and are a result of their gambling activities. The Canadian adolescent gambling inventory (Wiebe et. al., 2010) was used to assess the severity of gambling related problems. We also asked adolescents about parents’, siblings’ and peers’ frequency of engaging in gambling activities. Adolescents who bet on sports regularly are more likely to have fathers, siblings and friends that also bet on sports. Furthermore, it is more probable that their parents know about their gambling activities and that sometimes they bet on sports together with their fathers. It is interesting how adolescents, who don’t bet on sports regularly, play lottery games and scratch tickets more often with their parents. More intensive adolescent sports betting is positively correlated with more severe psychological, social and financial consequences, as well as with preoccupation with gambling/betting and impaired control. These results not only confirm the accessibility of sports betting to minors in Croatia, but also show that parents have relatively accepting attitudes about these activities. Therefore, future preventive strategies and interventions should not only include adolescents, but also parents and other important stakeholders in order to sensitize them to possible negative outcomes of gambling on healthy psychosocial development of young people.

**ИИ:** + · обе модели · беттеры + инструмент · 833 adolescent sports bettors from a representative student survey; problem severity measured with the Canadian Adolescent Gambling Inventory.

**Решение:** =

---

### 1257 · R6613

**Examining the impact of league entry fees on online fantasy sport participation and league consumption**

2013 · European Sport Management Quarterly · article, review · en · https://doi.org/10.1080/16184742.2013.783605

After American legislators explicitly exempted fantasy sports from online gambling laws, legal theorists have debated whether or not playing fantasy sports for money warranted such an exemption. However, there is currently no survey-based research which has examined the relationship between gambling and the attitudes and behaviours of fantasy players. The current study surveyed 253 fantasy participants and separated respondents into groups based on whether or not they play fantasy baseball for money. Results indicate that those who play for money are increasingly motivated by the social benefits associated with participation and are not motivated by the opportunity to win money. This finding runs counter to research on traditional forms of gambling, which often reports strong anti-social tendencies associated with increased gambling along with a strong motivation for financial gain. Further, from the league and team perspective, those who play fantasy baseball for money actually exhibited higher levels of team-related consumption.

**ИИ:** разошлись — Opus -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Survey of fantasy baseball players measuring motives and team consumption by money-play status; no problem-gambling instrument indicated.); Sonnet ? (неясно, измеряли ли проблемную игру: Survey of 253 fantasy baseball players, some playing for money; abstract reports motives and consumption, and doesn't say whether a problem-gambling instrument was used.)

**Решение:** ?

---

### 1258 · R6618

**Explaining the performance of online sports bettors**

2013 · International Gambling Studies · article, review, journal-article · en · https://doi.org/10.1080/14459795.2013.826709

This article reports the results of an online survey conducted among a sample of 161 online sports bettors in which their return-on-investment (ROI) performance as computed on the basis of their last 20 bets was used as the main dependent variable. A regression analysis showed that the online gamblers’ ROI performance is positively associated with their experience in sports betting, the degree of information search and analysis performed prior to betting, and their propensity to consider that events that happen in their life are the results of chance forces. These research results are discussed in the context of a general theoretical model where gambling performance is seen as depending on four types of determinants: the gambler's experience, personality, motivation and cognitive abilities.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of 161 online sports bettors on their ROI performance; the abstract doesn't say whether a problem-gambling instrument was used.

**Решение:** =

---

### 1259 · R6629

**The impact of internet gambling on gambling problems: a comparison of moderate-risk and problem Internet and non-Internet gamblers.**

2013 · Psychology of addictive behaviors : journal of the Society of Psychologists in Addictive Behaviors · comparative study, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1037/a0031475

Numerous studies have reported higher rates of gambling problems among Internet compared with non-Internet gamblers. However, little research has examined those at risk of developing gambling problems or overall gambling involvement. This study aimed to examine differences between problem and moderate-risk gamblers among Internet and non-Internet gamblers to determine the mechanisms for how Internet gambling may contribute to gambling problems. Australian gamblers (N = 6,682) completed an online survey that included measures of gambling participation, problem gambling severity, and help seeking. Compared with non-Internet gamblers, Internet gamblers were younger, engaged in a greater number of gambling activities, and were more likely to bet on sports. These differences were significantly greater for problem than moderate-risk gamblers. Non-Internet gamblers were more likely to gamble on electronic gaming machines, and a significantly higher proportion of problem gamblers participated in this gambling activity. Non-Internet gamblers were more likely to report health and psychological impacts of problem gambling and having sought help for gambling problems. Internet gamblers who experience gambling-related harms appear to represent a somewhat different group from non-Internet problem and moderate-risk gamblers. This has implications for the development of treatment and prevention programs, which are often based on research that does not cater for differences between subgroups of gamblers.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Online survey of 6,682 Australian gamblers that measured problem gambling severity and sports betting participation, so it may report PG among sports bettors.

**Решение:** =

---

### 1260 · R6639

**Expanding the Study of Internet Gambling Behavior: Trends Within the Icelandic Lottery and Sportsbetting Platform**

2013 · Journal of Gambling Studies · journal-article · https://doi.org/10.1007/s10899-013-9427-0

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: No abstract; recalled as an analysis of Icelandic operator betting records (Division on Addiction) with no problem-gambling instrument.); Sonnet ? (нет аннотации: No abstract; Icelandic lottery and sportsbetting platform study may be operator account data only, but a problem-gambling measure can't be ruled out.)

**Решение:** ?

---

### 1261 · R6642

**Development of Judgment Criterion for Problem Gamblers in Sports Lottery**

2013 · Beijing Tiyu Daxue xuebao · article · en

To screen items and define boundary value for problem gamblers’judgment criterion,by Delphi Method,the feedback data of 23 experts were statistically analyzed in terms of authority,concentricity and coordination.A total sample of 2 426 lottery consumers was assessed.The conclusions show that by Delphi Method and item discrimination method,the problem gamblers’judgment criterion consists of 12 items and 5 factors(continued and repeated purchasing behavior,cognitive bias,loss of control,abstinence,actus reus).2) By sensitivity,specificity and Youden index analysis on morbid group and control group,it shows that 6 point is the best boundary value to define problem gambler.It means the cutoff point of the problem gamblers scale was 6.3) With the standard of psychological status as the criterion,the chi-square test indicates there exists significant difference(P 0.01) among problem gamblers and non-problem gamblers.4) The problem gamblers’judgment criterion has a relatively reliability and validity,which can be regarded as a research tool.

**ИИ:** разошлись — Opus ? (другое: New problem-gambling scale developed in 2,426 Chinese sports lottery consumers; unclear if quiz-type betting or established instruments involved.); Sonnet + (валидация инструмента: Develops and validates a problem gambler scale with cutoff among 2,426 sports lottery consumers; a new instrument, so full text needed to check prevalence figures.)

**Решение:** ?

---

### 1262 · R6662

**How is gambling related to perceived parenting style and/or family environment for college students?**

2013 · Journal of behavioral addictions · article, journal article, journalarticle · eng · https://doi.org/10.1556/jba.1.2012.014

Background and aims The relationship between college student gambling, parenting styles, and family environments is a neglected area of gambling research. Do parenting styles indirectly influence problem gambling behaviors via family environments? Do poor family environments, characterized by high levels of conflict and low levels of cohesion, increase the likelihood of problem gambling among youth? This study explored the interrelationships among college students' current gambling behaviors and a) having an emotionally close and supportive family environment, b) having nagging and critical parents, c) having an authoritative mother, and d) frequency of alcohol consumption. Methods and results Survey data were collected from 450 undergraduate students enrolled in introductory psychology classes at two state universities in a southern state. Feeling that one has nagging and critical parents was associated with gambling in more venues, while the opposite was true for having emotionally close and supportive families. However, perceptions of having authoritative mothers were not related to gambling. The results also showed that more frequent alcohol consumption was associated with higher odds of gambling in casinos, playing cards for money, betting on sports, gambling on the Internet, higher gambling losses, and a larger number of gambling venues. Conclusions As with any exploratory research, there are several unique lines of inquiry that can, and should, follow from these findings, including more research on how college students' attitudes toward gambling activities may have begun prior to college and been influenced by their feelings about their homes and parents.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · College student survey measured sports betting; the outcomes were gambling venues and losses, and no problem-gambling instrument is stated.

**Решение:** =

---

### 1263 · R6668

**Prevalence and correlates of problematic gambling among D anish adolescents**

2013 · International Journal of Social Welfare · article · en · https://doi.org/10.1111/ijsw.12021

This study reports the findings from a national survey on gambling behaviour among Danish primary school children. A questionnaire was administered to 2,223 primary school students ranging in age from 11 to 17 years. The questionnaire contained a gambling screen (SOGS‐RA) and items that measure gambling behaviour, social network and cognitive perceptions. The prevalence of problem gambling was 1.29 per cent, while 4.5 per cent were categorised as at‐risk gamblers. The three most frequently reported reasons for gambling were to win money, to have fun and to socialise with family and friends. It is suggested that gambling may be linked to a masculine universe and that at‐risk gambling behaviour patterns may be part of a normal adolescent life in which gambling serves recreational or leisure purposes. Implications for further research and preventive measures are discussed.

**ИИ:** + · обе модели · опрос населения об азартных играх · National survey of Danish adolescents using SOGS-RA and gambling behaviour items; sports betting participation likely reported in the full text.

**Решение:** =

---

### 1264 · R6684

**Updates of the prevalence of problem gambling in Romanian teenagers.**

2013 · Journal of gambling studies · journal article, journalarticle, article · eng · https://doi.org/10.1007/s10899-012-9296-y

The aim of this study was to find out what is the prevalence of pathological in Romanian teenagers. We questioned one thousand thirty-two teenagers in Cluj-Napoca and Harghita counties. Participants completed a questionnaire with 40 items including gamblers anonymous twenty questions. The sample included teenagers aged 11-19 years; 65.57% were male and 34.43% were female. The subjects were divided into three groups: non-gambling/recreational gambling or occasional gambling (0-1 positive answers -Level 1)-753 subjects (72.96%) [316 females and 437 males]; problem gambling (2-6 points-Level 2)-243 subjects (23.54%) [43 females and 200 males]; pathological gambling (above 7 points-Level 3)-36 subjects (3.48%) [3 females and 33 males]. The mean age of pathological gamblers was 16.48 years. Gender differences were as expected, males engaging in pathological gambling (91.66% from pathological gamblers) more than females did (8.33% from pathological gamblers). Data revealed that the most encountered games practiced weekly were sport bets and slot machines in the case of 36.11% of the pathological gamblers; lotto, internet casino and pool bets each with 25%, followed by roulette and black-jack with 22.22%.From those who reported practicing gambling at a pathological level 66.66% engaged in alcohol consumption, 13.88% illicit drug use and 19.44% licit drugs. Just 16.66% smoke cigarettes. Data revealed higher rates of prevalence in Romanian teenagers than in other Central and Eastern European countries. A prevalence study at a national level should be designed.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Adolescent survey using GA20 problem-gambling screen; reports sport and pool betting by gambling level.

**Решение:** =

---

### 1265 · R6690

**Exploration of the relationship between fantasy sports participation and disordered gambling**

2013 · PsycEXTRA Dataset · dataset · en · https://doi.org/10.1037/e575632013-019

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; title suggests empirical study of fantasy sports participation and disordered gambling, likely using a PG measure.

**Решение:** =

---

### 1266 · R6693

**NCAA Division I Athletic Trainers: Examining Sport-Wagering Behavior**

2013 · Journal of contemporary athletics · article · en

IntroductionSports betting threatens the integrity of and public confidence in professional and amateur team sports, converting sports from wholesome entertainment into a vehicle for gambling * * * sports gambling raises people's suspicions about point-shaving and game-fixing * * * All of this puts undue pressure on players, coaches, and officials. (The National Gambling Impact Study, 2001, p. 3).Gamblers were present at the earliest stages of the American sporting world and have been a part of sports for over a century (Thornton, Champion, & Ruddell, 2011). The Merriam-Webster Dictionary (2011a) defines gambling as: La.: playing a game for money or property, l.b.: betting on an uncertain outcome, or 2: taking something on a contingency: taking a chance. Gambling can also be defined by the various types of activities that constitute gambling such as: pari-mutuel betting, lotteries, casino gambling and charitable gaming. It should be noted that sports betting or wagering, which is defined as making a bet or venturing on a final outcome (Merriam-Webster, 2011b), is considered as one form of pari- mutuel betting (Eadington & Cornelius, 1991). For the purpose of this research, sports wagering is betting on sporting contests while gambling refers to other forms of betting.According to Holtgraves (2009), wagering on sports is among the most popular gambling activities. With this, it comes as no revelation that amid a group of self-identified problem gamblers, sports emerged as one of the most problematic forms of wagering and gambling (Petiy, 2003).Therefore, sports wagering is seemingly a highly consumed activity (Holtgraves, 2009) with evidence pointing towards an increase in disordered gambling behaviors (Eadington, 1989; Whyte, 1997; Shaffer, Hall & Vanderbilt, 1999). Such behavior may likely be the result of a combination of numerous, legal gaming options regarding sports wagering as well as the desire for individuals to be associated with select players and/or teams. As such gambling and wagering on college and professional sporting events has been a popular target for those who wager on sports (Rockey & King, 2006). College athletics administrators have been concerned about the integrity of college sports due in part to the popularity of wagering on college games by college students (2006). Over the past 25 years, this concern has expanded to the gambling and sports wagering behaviors of student-athletes (Thrasher, Andrew & Mahoney, 2007; Ellenbogen, Jacobs, Derevensky, Gupta & Paskus, 2008), yet little thought has been given to other susceptible athletic populations. As noted, a scant amount of literature exists regarding sport related populations outside of the student-athlete group (such as athletics administrators, coaches and athletic trainers). Holtgraves (2009) suggested that researchers should focus on understanding the differences in people and their gambling activities as this could foster developments in awareness, education, and rehabilitation programs. For sport researchers and practitioners alike, this includes extending studies outside of the student-athlete population and looking at other groups that might be distinct, yet have some of the same characteristics as the student-athletes.Recently, Mathner, Martin and Allen (2011) provided the first, evidenced-based rationale to further explore designated sport populations such as athletic trainers, coaches, equipment managers, and academic advisors. Specifically, the researchers examined NCAA Division I certified athletic trainers (ATCs); a group of medical professionals who abide by both a professional and educational code of ethics, and noted that 61.6% had made friendly wagers on sports and 37.8% had made monetary wagers on sports at some point in time in their life. Though the researchers noted that a majority of these wagers were not categorized as problematic gambling, there was still cause for further scrutiny due to the potential corruption of collegiate athletics. …

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of athletic trainers' sports wagering; the abstract hints at categorising problem gambling but no instrument is named.

**Решение:** =

---

### 1267 · R6694

**Apostas desportivas online comportamento e perfil do apostador português**

2013 · master thesis · por · http://hdl.handle.net/10071/6840

The market of online sports betting has had a huge growth in recent years and is estimated to continue to grow in a sustainable way in the next ones. In spite of this big growth, academic studies on the subject are still scarce. The main objective of this study consists in the development of the empirical knowledge that concerns the market of online sports betting. It was sought to identify and comprehend the behavior and profile of the portuguese better. In other words, the final aim of this research is to understand if the typical portuguese better has a fan type profile directed to consumption or an investor type profile closer to that of the investor, which means, professional and with the sole purpose of financial return. To achieve this outcome, in the context of this research, it was made a survey. The first part of the survey addresses the subject identification, where as the second part regards the participation in sport betting online and consumer type behavior. Through this research it is intended to apprehend if subjects with higher identification indexes with their team are more willing to perform sports bets online. Furthermore, it is wanted to understand if betters that wager more money are also the ones that waste more money on their team, namely in buying game tickets, merchandizing and television subscriptions. O mercado das apostas desportivas online tem tido um enorme crescimento nestes últimos anos, e estima-se que continue a crescer de forma sustentada nos próximos. Apesar deste grande crescimento ainda são escassos os estudos académicos neste mercado. O principal objectivo deste estudo consistiu no desenvolvimento do conhecimento empírico no que concerne ao mercado das apostas desportivas online. Procurou-se identificar e compreender o comportamento e perfil do apostador português. Ou seja, o intuito final desta investigação é entender se o apostador português tem um perfil de fã virado para o consumo, ou um perfil mais de investidor, profissional em que único objectivo é o retorno financeiro. Para tal, nesta pesquisa foi realizado um questionário em que a primeira parte aborda a identificação do indivíduo com a sua equipa, e a segunda parte aborda a participação em apostas desportivas online e o comportamento do consumo. Através desta pesquisa procura-se perceber se os indivíduos com maiores índices de identificação com a sua equipa são mais propensos a realizar apostas desportivas online, bem como entender se os apostadores que apostam mais dinheiro são também os que mais gastam com a equipa em bilhetes, merchandising e subscrições televisivas. Projecto

**ИИ:** разошлись — Opus -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Marketing thesis surveying Portuguese online sports bettors; the questionnaire covered only team identification, betting participation and spending, with no problem-gambling screen.); Sonnet ? (неясно, измеряли ли проблемную игру: Survey of Portuguese online sports bettors; abstract mentions identification, spending and behavior but doesn't say whether a problem-gambling instrument was used.)

**Решение:** ?

---

### 1268 · R6695

**An examination of participation in online gambling activities and the relationship with problem gambling.**

2013 · Journal of behavioral addictions · article, journal article, journalarticle · eng · https://doi.org/10.1556/jba.2.2013.1.5

Background and aims Online gambling participation is increasing rapidly, with relatively little research about the possible effects of different gambling activities on problem gambling behaviour. The aim of this exploratory study was to examine the participation in online gambling activities and the relationship with problem gambling among an international sample of online gamblers. Methods An online gambling survey was posted on 32 international gambling websites and resulted in 1,119 respondents over a four-month period. Results Poker was the most popular gambling activity online. A number of online activities were associated with problem gambling, including: roulette, poker, horse race betting, sports betting, spread betting and fruit (slot) machines. Not surprisingly, those that gambled on these activities regularly (except poker) were more likely to be a problem gambler, however, what is interesting is that the reverse is true for poker players; those that gambled regularly on poker were less likely to be a problem gambler compared to the non-regular poker players. The majority of the players also gambled offline, but there was no relationship between problem gambling and whether or not a person also gambled offline. Discussion Problem gambling is associated more with certain online gambling activities than others, and those gambling on two or more activities online were more likely to be a problem gambler. Conclusion This paper can help explain the impact different online gambling activities may have on gambling behaviour. Consideration needs to be given to the gambling activity when developing and implementing treatment programmes.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Online gambler survey linking problem gambling to activities including sports betting; likely used a PG screen (PGSI).

**Решение:** =

---

### 1269 · R6708

**Falsches Spiel mit dem Sport. Zur Mediatisierung von Sportwetten und ihren nicht-intendierten Nebenfolgen**

2013 · Springer eBooks · book-chapter · de · https://doi.org/10.1007/978-3-658-03664-5_8

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · German book chapter on the mediatization of sports betting and its side effects; no abstract, probably conceptual, but empirical data can't be ruled out.

**Решение:** =

---

### 1270 · R6710

**Promotion of gambling and live betting odds during televised sport: Influences on gambling participation and problem gambling**

2013 · Unpublished · text/book · en · https://doi.org/10.13140/2.1.1643.8087

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; title suggests a survey report on sports betting promotion and problem gambling, possibly with PGSI data on bettors.

**Решение:** =

---

### 1271 · R6713

**Associations between problem gambling, socio-demographics, mental health factors and gambling type: sex differences among Finnish gamblers**

2013 · International Gambling Studies · article · en · https://doi.org/10.1080/14459795.2013.840328

This study examined associations between problem gambling and type of gambling engagement (online, land-based or both), psychological distress, alcohol-related problems and demographics among male (n = 1438) and female (n = 1546) past-year gamblers in Western Finland. In this sample, 7.6% of men and 3.1% of women were screened as problem gamblers. Logistic regression analyses were used to study the associations for men and women separately. Among men, engaging in both land-based and online gambling or engaging in online gambling only and psychological distress increased the risk of problem gambling. Among women, engaging in both land-based and online gambling and alcohol-related problems were significantly associated with problem gambling. The findings further highlight the need to consider sex differences in preventive and treatment initiatives and policies targeting problem gambling. Online gambling seems to have stronger links with problem gambling, which motivates further research in the eventual harmfulness of this gambling form.

**ИИ:** разошлись — Opus + (опрос населения об азартных играх: Regional population survey of past-year gamblers in Western Finland screened for problem gambling; activity-level data, including sports betting, is likely in the full text.); Sonnet ? (неясно, есть ли ставки на спорт: Population survey of Finnish past-year gamblers with problem gambling screen; sports betting not mentioned in abstract but activity-level data may appear in full text.)

**Решение:** ?

---

### 1272 · R6723

**educación física educacion fisica deportes deporte sport futbol fútbol entrenamiento deportivo discapacidad aventura poker jackpot bet apuesta dados dice casino naturaleza lesión lesion deportiva psicologia sociologia estudios sociales culturales physical juegos game gambling education sports scienc**

2013

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: The title is just a list of website keywords (physical education, sports, poker, casino), with no abstract and no sign of a study.); Sonnet ? (нет аннотации: Title is a keyword list (sports, betting, gambling, casino) with no abstract; study type and problem gambling measurement cannot be determined.)

**Решение:** ?

---

### 1273 · R6728

**Gambling involvement and increased risk of gambling problems.**

2013 · Journal of gambling studies · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1007/s10899-012-9325-x

The opportunity to gamble has undergone rapid expansion with technology allowing for access to gambling products 24 h a day. This increased online availability challenges governments' abilities to restrict access to gambling. Indeed, the ready access to multiple forms of gambling may potentially contribute to impaired control over urges for problem gamblers. The present study considered whether problem gamblers manifested a tendency to engage in multiple forms of gambling and identified forms of gambling which were more strongly related to problem gambling. In reanalyses of two surveys (Sample 1, N = 464, Sample 2, N = 1141), significant relationships accounting for between 11.3 and 13.5% of the variance were found between the numbers of forms of gambling accessed and degree of problem. Participation in online poker, playing cards and sports wagering were linked to problem gambling. Access to multiple forms of gambling may pose difficulties for the tracking and control of gambling.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Reanalysis of two surveys measuring degree of gambling problems and participation by form, including sports wagering, linked to problem gambling.

**Решение:** =

---

### 1274 · R6755

**Evaluación de riesgos y toma de decisiones en entorno de incertidumbre. El caso de las apuestas deportivas**

2013 · Universitat Politècnica de València · bachelor thesis · esl/spa · https://riunet.upv.es/handle/10251/31024

Consulta en la Biblioteca ETSI Industriales (8519)

**ИИ:** разошлись — Opus -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: Engineering bachelor thesis on risk evaluation and decision-making under uncertainty in sports betting; likely betting strategy modelling, not a problem-gambling survey.); Sonnet ? (нет аннотации: Bachelor thesis on risk assessment and decision-making in sports betting; no abstract, likely an industrial engineering/modelling work, but problem gambling measurement is unknown.)

**Решение:** -

---

### 1275 · R6771

**STUDY OF CAUSES OF PATHOLOGICAL GAMBLERS IN INTERNET SPORTS GAMBLING**

2013 · Zhongguo yaowu yilaixing zazhi · review, article · en

Objective:Through the data analysis of psychological and behavioral characteristics of pathological gamblers(PGs) in Internet sports gambling(ISG) in Chinese Mainland,we explored the causes of PGs to provide reference data for better treatment and prevention.Methods:In this study,155 self-selecting Internet sports gamblers were surveyed using online questionnaires posted on the most famous sports forum in China.The questionnaire includes DSV-IV criteria for pathological gambling,Chen Internet Addiction Scale,Chinese Version of the Gambling Motivation and Cognitions Scale,general information and related questions.Results:Male,above 28,employed,university degree and monthly income 1000-3000 yuan were the significant features of the 88 PGs.The multivariate Logistic regression analysis showed that among the independent factors which significantly associated with PGs,the most significant included Internet addiction(AOR=3.15;95% CI:1.43-6.96),Don't have the ability to stop gambling(AOR=1.67;95% CI:1.24-2.25),and Parents smoking(AOR=1.42;95% CI:1.02-1.98).Conclusion:The gamblers with Internet addiction in ISG had more risk to be PGs.In addiction,the misconception of Don't have the ability to stop gambling and Parents smoking,were two very important reasons for gamblers developing into PGs.

**ИИ:** + · обе модели · беттеры + инструмент · Online survey of 155 internet sports gamblers using DSM-IV criteria; 88 classified as pathological gamblers, so prevalence can be extracted.

**Решение:** =

---

### 1276 · R6775

**Estimating the prevalence of problem gambling among older adults in Singapore**

2013 · Psychiatry Research · article · en · https://doi.org/10.1016/j.psychres.2013.06.017

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: Population prevalence study of older adults; no abstract, so unclear whether sports betting participation was measured alongside problem gambling.); Sonnet + (опрос населения об азартных играх: Population survey of problem gambling in older Singaporeans; the full text may report prevalence by gambling activity, including sports betting. No abstract available.)

**Решение:** ?

---

### 1277 · R6779

**College Students and Gambling: Do Student Athletes Really Gamble More?**

2013 · Journal for the Study of Sports and Athletes in Education · article, review · en · https://doi.org/10.1179/1935739713z.0000000008

A large amount of scholarship has focused on the historical prevalence of gambling, in general, and within the world of sport. In the early part of the 21st century, sport gambling behaviors on college campuses came under scrutiny. The NCAA now has gambling programs designed to educate student athletes on the dangers and illegality of sports gambling, but prevailing concerns regarding sport-related gambling are still evident. The purpose of this research was to identify the differences in gambling behaviors of student athletes and non-athletes in an urban university setting. A survey was developed and distributed to a sample of college students and student athletes regarding their gambling-related behaviors. Survey sample consisted of college students present in a priori identified classes on the day of data collection. Data were collected at a public, state university in the high plains region of the US with an urban-serving mission. Contrary to the previous literature, statistical analyses indicate college students engage in more gambling activities as compared to student athletes but there are no significant differences between gambling behaviors and these two groups. Limitations and avenues for future research are discussed.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of student athletes and other students about gambling, sports gambling likely included; unclear whether a problem-gambling instrument was used.

**Решение:** =

---

### 1278 · R6784

**A utilização deste artigo é exclusiva para fins educacionais**

2013

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Title is a Portuguese copyright notice, not a real title, and there is no abstract; the topic can't be judged without the full text.

**Решение:** =

---

### 1279 · R6788

**EXAMINING PARTICIPATION IN SPORTS BETTING IN GERMANY**

2013 · The Journal of Gambling Business and Economics · article, review, journal-article · en · https://doi.org/10.5750/jgbe.v6i3.610

Previous research has examined participation in betting in general, while sports bets have not been investigated specifically. The purpose of this study is to investigate the participation in sports betting and the mechanisms to place bets in Germany. Based on the economic household theory, it is assumed that participation in sports betting can be explained by a set of economic, socio-demographic, and lifestyle factors. A convenience sample of German citizens is drawn using an online survey (n=464). The results show that the typical online bettor is a male with high income, low education, and non-German nationality, who plays cards and poker during his leisure time, but does not regularly participate in sport. On the contrary, people betting via automats are predominantly female with low income and high education, who do not play poker, but practice sport in their leisure time. The findings have implications for policy makers.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Online survey of German sports betting participation (n=464); the abstract doesn't say whether a problem-gambling instrument was used.

**Решение:** =

---

### 1280 · R6789

**The classification accuracy of four problem gambling assessment instruments in population research**

2013 · International Gambling Studies · article · en · https://doi.org/10.1080/14459795.2013.839731

Improved methodology was used to re-examine the weak correspondence between problem and pathological gamblers identified in population surveys and subsequent classification of these individuals in clinical interviews. The SOGS-R, the CPGI, the NODS and the Problem and Pathological Gambling Measure (PPGM), as well as questions about gambling participation and expenditures, were administered to a total of 7272 adults. Two clinicians then assessed each person's status, based on comprehensive written profiles derived from these questionnaire responses. Instrument classification was then compared to clinical classification. All four instruments correctly classified most non-problem gamblers (i.e. had good to excellent sensitivity, specificity and negative predictive power). However, the PPGM was the only instrument with good classification of problem gamblers (i.e. excellent sensitivity and positive predictive power). The CPGI and SOGS-R had weak positive predictive power and the NODS had only adequate sensitivity and positive predictive power. Improvement in the classification accuracy of the CPGI occurred when a 5+ cut-off was used and when a 4+ cut-off was used with the SOGS. In general, the classification accuracy of the NODS, SOGS and CPGI is better than prior research suggested but overall accuracy is still modest. With adjusted cut-offs, all three instruments are reasonably congruent with clinical ratings.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Population sample of 7272 adults given several PG instruments and gambling participation questions; unclear if sports betting is reported separately.

**Решение:** =

---

### 1281 · R6791

**The prevalence and nature of gambling and problem gambling in South Korea.**

2013 · Social psychiatry and psychiatric epidemiology · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1007/s00127-012-0580-z

Purpose To establish the current prevalence of gambling and problem gambling in South Korea and to determine the associated demographic and game play patterns. Methods Administration of a gambling survey over the phone to 4,000 randomly selected South Korean adults (19+), supplemented by an online survey of 4,330 members of a South Korean online panel. Results The past year prevalence of gambling among South Korean adults was 41.8 %. The past year engagement in individual forms of gambling was 36.2 % for lotteries and instant lotteries; 12.0 % for social gambling; 2.3 % for sports betting; 1.5 % for casino gambling; 1.5 % for internet gambling; and 1.1 % for horse, bicycle, or motor boat betting. The past year prevalence of problem gambling was 0.5 %. Logistic regression identified the best predictors of problem gambling to be: having a greater number of gambling fallacies; gambling on the internet; betting on horses, bicycling, or motor boat racing; social gambling; male gender; mental health problems; sports betting; motivation for gambling (gambling to escape); casino gambling; and lower income. Conclusions The past year prevalence of gambling (41.8 %) and problem gambling (0.5 %) in South Korea is low compared to other countries, especially relative to other Asian jurisdictions. This relatively low prevalence of gambling is likely related to the very strong negative attitudes toward it, the low participation by females, and restricted access. The low prevalence of problem gambling is likely related to the relatively low prevalence of gambling and restricted access to continuous forms of gambling. The variables that are predictive of problem gambling in South Korea are quite similar to those found in other countries with a couple of important differences.

**ИИ:** + · обе модели · опрос населения об азартных играх · National South Korean prevalence survey measuring sports betting participation and problem gambling; sports betting predicted problem gambling.

**Решение:** =

---

### 1282 · R6806

**Wagers' ideas on İDDAA who accommodate betting game.**

2013

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; title suggests a study of Turkish İDDAA sports bettors' opinions, so whether problem gambling was measured is unknown.

**Решение:** =

---

### 1283 · R6820

**부산지역 대학생의 도박행동유형과 건강위험행동이 도박문제에 미치는 영향**

2013

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Korean student survey of gambling types and gambling problems; may cover sports betting (e.g., Sports Toto) and a PG screen. No abstract.

**Решение:** =

---

### 1284 · R6821

**A Study on the Advancement of the China Sports Lottery and Sports Industry**

2013 · article · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: Title points to a sports-economics or industry-development paper on the China Sports Lottery, not a survey measuring problem gambling.); Sonnet ? (нет аннотации: No abstract; title suggests a sports lottery/industry policy paper, likely not empirical on problem gambling, but can't be confirmed.)

**Решение:** ?

---

### 1285 · R6822

**부산지역 대학생의 도박행동유형과 건강위험행동이 도박문제에 미치는 영향**

2013 · Journal of Health Informatics and Statistics · article · ko

Objectives: This study aims to examine college students` gambling behavior and investigates the effect of factors on problem gambling, such as personal characteristics, gambling history, and health risk behaviors. Methods: The subjects of the study were students selected from six colleges in Busan, Korea. A total of 431 questionnaires were used in the final analysis. Results: First, the results showed that more than 60% of respondents had gambled in the past year. The most popular forms of gambling were the lottery, followed by card betting, sports betting, and online gambling, betting on horse-racing, cycle-racing, and motorboat-racing games, and casino games. Second, frequent smoking and drinking increased the incidence of the problem gambling. Third, it was revealed that gender and age were negatively correlated with gambling, while the frequency of gambling activities and the number of previous gambling experiences were positively correlated with problem gambling behavior. Conclusions: Ongoing preventive screening and early intervention must be made a priority to prevent college students` gambling behavior from reaching serious levels.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Survey of Busan college students measured sports betting participation and problem gambling; the abstract doesn't name the instrument, but a screen is likely.

**Решение:** =

---

### 1286 · R6825

**레저,스포츠 : 스포츠토토의 중독성향과 합리화 기제; Sykes와 Matza의 중화이론 관점으로**

2013

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Korean study of addiction tendency among Sports Toto bettors; no abstract, so it is unclear whether a problem-gambling instrument was used.

**Решение:** =

---

### 1287 · R6826

**스포츠토토의 중독성향과 합리화 기제**

2013

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Korean study on addictive tendency of Sports Toto (sports betting) players; no abstract, may have used a problem-gambling screen.

**Решение:** =

---

### 1288 · R6829

**스포츠토토 참여자의 계획된 행동과 갬블링 열정의 관계**

2013 · article · ko

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Survey of Korean Sports Toto bettors on planned behaviour and gambling passion; no abstract, so it's unclear whether a PG instrument was used.

**Решение:** =

---

### 1289 · R6833

**Taking the Points: The Socialization Process of a Sports Book â•œRegularâ•š**

2012

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: No abstract; sports book regulars' socialization is probably qualitative/ethnographic, but a survey with a problem-gambling screen can't be ruled out.); Sonnet -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: Title suggests an ethnographic/qualitative study of socialization of a sports book regular; no abstract, and a problem-gambling prevalence measure is unlikely.)

**Решение:** -

---

### 1290 · R6839

**Consequences and associated factors of youth gambling.**

2012 · Journal of the Medical Association of Thailand = Chotmaihet thangphaet · article, journal article, research support, non-u.s. gov't · eng · https://pubmed.ncbi.nlm.nih.gov/23130485/

OBJECTIVE: To examine gambling behaviors, consequences and its associated factors among Thai youths. MATERIAL AND METHOD: A cross-sectional survey of 1,694 students from Matthayom 1 (grade 7) to university undergraduate level was conducted using a self-administered questionnaire. Questionnaire items consisted of socio-economic characteristics, health behaviors, attitudes towards gambling and consequences of gambling. Factors associated with gambling experience were identified by multivariate logistic regression. RESULTS: Approximately 20% of youth gambling was reported. Gamblers had higher proportion of males, studying in vocational schools and lower GPA and history of smoking and alcohol consumption. Card games were the most common type of gambling, followed by football-betting. Approximately 10% of the gamblers potentially had pathological gambling. Factors positively associated with gambling included having friends (adjusted OR = 4.82) and relatives (adjusted OR = 2.48) who gambled. Having a GPA > or = 3.0 was negatively associated with gambling (adjusted OR = 0.58). The present study reported negative consequences of gambling including feeling of guilt, perception of poorer health and depression or insomnia after losing. CONCLUSION: Gambling prevention program should be developed and focused on student with poor study performance and wrecked relationships in family. Also, a surveillance system for health risk behaviors among youth in school and community should be established by the participation of multiple organizations.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Thai student survey measured football betting and reported potential pathological gambling, but the screening instrument is not named.); Sonnet + (игроки, есть ставки на спорт и инструмент: Thai youth survey covering football betting and probable pathological gambling among gamblers; the instrument is unstated, but full text may give problem gambling by activity.)

**Решение:** ?

---

### 1291 · R6874

**Patologické hráčství: sázky a hazardní hry v životě sportovních redaktorů**

2012 · master thesis · ces/cze · http://www.nusl.cz/ntk/nusl-538470

This thesis deals with the definition of the concept of pathological gambling, diagnosis, prevalence and a description of vulnerable groups. It also discusses the creation, development and various stages of pathological gambling. Theoretical knowledge is enhanced by our own research, carried out a questionnaire, which has pointed out that the profession can be a risk factor for developing an illness / addiction. The research objective is to describe the rate and quality of risk-taking behavior in gambling on sports editor, and identify any related pathological gambling with their selected characteristics. The paper looks at what it looks like gambling and betting on sports editors in terms of rates, forms and circumstances. Whether the people in this group of pathological gambling occurs and, if so, to what extent and with what consequences. They try to answer it then also, what is the relationship between work characteristics and playing sports editor of gambling or betting. How this relationship sports editors perceive themselves and how to understand. Keywords: Pathological gambling, pathological player, gambling, gambling

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Questionnaire survey of sports editors on sports betting and pathological gambling; abstract does not name a screening instrument.); Sonnet + (игроки, есть ставки на спорт и инструмент: Questionnaire survey of sports editors on gambling and sports betting, assessing pathological gambling; likely uses a screening instrument and could report PG among bettors.)

**Решение:** ?

---

### 1292 · R6890

**Sports betting of adolescents: Gambling intensity, experience of winning and cognitive distortions**

2012 · conference object, article · en

RIZICNI CIMBENICI ZA RAZVOJ PROBLEMA VEZANIH UZ KOCKANJE SU BROJNI. SUVREMENA ISTRAŽIVANJA I TEORIJSKI MODELI NAGLASAVAJU VAŽNOST SVEOBUHVATNOG PRISTUPA KOJI U OBZIR UZIMA INDIVIDUALNA OBILJEŽJA POJEDINCA, TE OBILJEŽJA UŽE I SIRE OKOLINE. U OVOJ CE PREZENTACIJI BITI PREDSTAVLJEN DIO REZULTATA ISTRAŽIVANJA “NAVIKE I OBILJEŽJA KOCKANJA ADOLESCENATA IZ URBANIH SREDINA REPUBLIKE HRVATSKE” KOJIM JE OBUHVACEN UZORAK SREDNJOSKOLACA IZ CETIRI HRVATSKA REGIONALNA SREDISTA (N=1.952). CILJ OVOG RADA JE STJECANJE UVIDA U NEKA OBILJEŽJA ADOLESCENATA KOJI SU SE BAREM JEDNOM U ŽIVOTU KLADILI U SPORTSKOJ KLADIONICI S NAGLASKOM NA UCESTALOST KLAĐENJA, ISKUSTVO DOBITKA I KOGNITIVNE DISTORZIJE VEZANE UZ KOCKANJE. UZORAK CINI UKUPNO N=833 SREDNJOSKOLACA (M=77, 1% ; Ž=22, 9%), A RASPON DOBI KRECE SE OD 14 DO 20 GODINA (M=16, 73 ; SD=1, 15). UZORAK JE PODIJELJEN U DVIJE SKUPINE: 1. ONI KOJI SE REDOVITO KLADE, TE 2. ONI KOJI SE POVREMENO KLADE. ZA PROCJENU OZBILJNOSTI PSIHOSOCIJALNIH POSLJEDICA KOCKANJA/KLAĐENJA KORISTEN JE KANADSKI UPITNIK KOCKANJA ADOLESCENATA – CAGI (WIEBE I SUR., 2010), A ZA PROCJENU KOGNITIVNIH DISTORZIJA „SKALA UVJERENJA O KOCKANJU“ (KONSTRUIRANA ZA POTREBE OVOG ISTRAŽIVANJA). SUDIONIKE SMO TAKOĐER PITALI O NJIHOVOM UKLJUCIVANJU U DRUGE IGRE NA SRECU, O ISKUSTVU DOBITKA NOVCA KOCKANJEM, TE O PROCJENI VLASTITOG PONASANJA PRILIKOM DOBITKA I GUBITKA NOVCA KOCKANJEM/KLAĐENJEM. REZULTATI POKAZUJU DA ADOLESCENTI KOJI SE REDOVITO KLADE IMAJU OZBILJNIJE PSIHOSOCIJALNE PROBLEME VEZANE UZ KOCKANJE/KLAĐENJE, U VECOJ MJERI SUDJELUJU I U DRUGIM KOCKARSKIM AKTIVNOSTIMA, CESCE IZVJESTAVAJU O ISKUSTVU VELIKOG DOBITKA KOCKANJEM, SKLONIJI SU NASTAVITI KOCKATI/KLADITI SE CAK I KADA IZGUBE NOVAC, TE IMAJU VISE KOGNITIVNIH DISTROZIJA VEZANIH UZ KOCKANJE/KLAĐENJE. DOBIVENI REZULTATI POTVRĐUJU DA JE SPORTSKO KLAĐENJE NAJZASTUPLJENIJA IGRA NA SRECU MEĐU ADOLESCENTIMA. TAKOĐER, POTVRĐENO JE DA UCESTALOST KLAĐENJA, ISKUSTVO DOBITKA I KOGNITIVNE DISTORZIJE IMAJU VAŽNU ULOGU U RAZUMIJEVANJU PROBLEMA VEZANIH UZ KOCKANJE. STOGA INTERVENCIJE KOJE NAGLASAK STAVLJAJU UPRAVO NA RAZUMIJEVANJE VJEROJATNOSTI DOBITKA PRILIKOM KOCKANJA I NA KOGNITIVNE DISTORZIJE MOGU DOPRINIJETI INTERVENCIJAMA U OVOM PODRUCJU.

**ИИ:** + · обе модели · беттеры + инструмент · Croatian adolescents who had bet on sports (n=833), with problem severity measured by CAGI. Its severity scale can classify problem gambling.

**Решение:** =

---

### 1293 · R6896

**The Prevalence of Problem Gambling in Denmark in 2005 and 2010: A Sociodemographic and Socioeconomic Characterization**

2012 · Journal of Gambling Studies · article · en · https://doi.org/10.1007/s10899-012-9347-4

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** + · обе модели · опрос населения об азартных играх · Danish national problem gambling prevalence surveys (2005, 2010); the full text likely includes tables of gambling activities.

**Решение:** =

---

### 1294 · R6900

**Gambling Participation and Prevalence Estimates of Pathological Gambling in a Far-East Gambling City: Macao**

2012 · UNLV Gaming Research & Review Journal · journalarticle, article, journal-article · en · https://doi.org/10.9741/2327-8455.1158

Davis Ka-Chio Fong Bernadete Ozorio This research is the first scientific study of gambling participation and pathological gambling in Macao. In 2003, a computer-assisted random digit dialing method was used to conduct 1,121 telephone interviews. Two-thirds of respondents expressed that they have participated in at least one of the fourteen forms of gambling in the past year. The three most popular forms of gambling include social gambling, Mark Six lottery, and soccer/basketball betting. As for the prevalence of pathological gambling, the Chinese DSM-IV Gambling Behavior Index was used as the screening tool and results indicate that 1.78% of respondents are classified as probable pathological gamblers and 2.5% are classified as probable problem gamblers. Logistic Regression test indicates that male respondents with a monthly personal income of less than MOP 8,000 (Macau currency is the Pataca) tend to be more vulnerable to problem and pathological gambling when they participate in casino gambling, soccer matches betting and mahjong house gambling.

**ИИ:** + · обе модели · опрос населения об азартных играх · Macao population telephone survey that measured soccer/basketball betting participation and screened with a DSM-IV-based instrument, with analyses by activity.

**Решение:** =

---

### 1295 · R6904

**Future Trends**

2012 · SpringerBriefs in behavioral medicine · book-chapter · en · https://doi.org/10.1007/978-1-4614-3390-3_8

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -1 (обзор, комментарий, теоретическая, правовая или регуляторная работа: A 'Future Trends' chapter in a SpringerBriefs book reads as a forward-looking discussion, not a quantitative survey of bettors.); Sonnet ? (нет аннотации: Generic title "Future Trends" in a SpringerBrief on behavioral medicine, no abstract; likely a review chapter, but the topic can't be determined.)

**Решение:** -

---

### 1296 · R6909

**Prévalence des habitudes de jeu en Gaspésie et aux Îles-de-la-Madeleine en 2009**

2012 · The Canadian Journal of Psychiatry · article · fr · https://doi.org/10.1177/070674371205700309

UNLABELLED: OBJECTIF : Estimer la prévalence des habitudes aux jeux de hasard et d'argent (JHA), du jeu à risque (JAR) et du jeu pathologique probable (JPP) dans la région de la Gaspésie et des Îles-de-la-Madeleine (GIM) (Québec). MÉTHODE : Un sondage téléphonique portant sur les habitudes de jeu a été réalisé auprès de 1014 adultes résidents de la région de la GIM. Les participants ont été sélectionnés aléatoirement. L'échelle Problem Gambling Severity Index de l'Indice canadien du jeu excessif a servi à l'évaluation du jeu pathologique. RÉSULTATS : Quatre-vingt-cinq pour cent des répondants rapportent avoir joué à un JHA au cours de l'année précédente. Les activités les plus populaires sont l'achat de billets de loterie, la participation à des tirages et collectes de fonds, le bingo, les cartes ou jeux de société en famille ou avec des amis pour de l'argent, la loterie vidéo et les jeux de casino. Les taux de prévalence du JAR et du JPP s'élèvent à 1,5 % et 0,8 % respectivement. La loterie vidéo s'avère le jeu le plus souvent identifié comme étant problématique, suivi des loteries instantanées et ordinaires (par exemple, Lotto 6/49). CONCLUSION: Les habitudes de jeu des Gaspésiens et des Madelinots sont similaires à celles observées chez l'ensemble des Québécois. La discussion soulève entre autres la question de la validité de l'évaluation de la présence d'un problème de jeu parmi les membres de l'entourage, et certaines perceptions à risque, dont celle qu'il est impossible de développer un problème aux loteries instantanées et au bingo.

**ИИ:** + · обе модели · опрос населения об азартных играх · Regional random-sample adult gambling prevalence survey in Quebec using PGSI with gambling activity participation; sports betting (Mise-o-jeu) likely in tables.

**Решение:** =

---

### 1297 · R6925

**Zusammenhang zwischen verschiedenen Glücksspielformen und glücksspielassoziierten Problemen**

2012 · SUCHT - Zeitschrift für Wissenschaft und Praxis / Journal of Addiction Research and Practice · article · de · https://doi.org/10.1024/0939-5911.a000207

Fragestellung: Anhand der Daten aus drei in den Jahren 2007, 2009 und 2011 durchgeführten Repräsentativbefragungen zum Glücksspielverhalten der 16- bis 65-jährigen Bevölkerung in Deutschland werden Zusammenhänge zwischen der Nutzung einzelner Glücksspiele, der Glücksspielgesamtaktivität und dem Auftreten von glücksspielassoziierten Problemen untersucht. Methodik: Erhebung der Teilnahme an den verbreitetsten Glücksspielformen in Deutschland in den zurückliegenden 12 Monaten per Telefonbefragung (CATI), standardisierte Instrumente: South Oaks Gambling Screen (SOGS) zum Screening auf Glücksspielsucht, bi- und multivariate logistische Regressionsanalysen, abhängige Variable: Problemspielverhalten (problematische oder pathologische Ausprägung nach SOGS). Ergebnisse: Problemspieler geben im Vergleich zu problemfreien Glücksspielern bei den meisten Glücksspielen (außer Lotterien) erheblich häufiger an, diese in den zurückliegenden 12 Monaten gespielt zu haben. Zudem weisen sie eine höhere Glücksspielanzahl (GSA) auf, haben also mehr verschiedene Glücksspiele genutzt. Die höchsten Problemspieleranteile finden sich unter Befragten, die Casinospiele im Internet, das kleine Spiel in der Spielbank, Geldspielautomaten in Spielhallen, Gaststätten etc., Sportwetten privater Anbieter, das große Spiel oder Keno angegeben haben (Anteile in abnehmender Reihenfolge: 11,7 % bis 6,5 %). Entsprechend ergeben sich bei diesen Glücksspielen in bivariaten Regressionsanalysen in annähernd gleicher Reihenfolge auch die höchsten Risiken für Problemspielverhalten. Wird zusätzlich die GSA statistisch kontrolliert, reduzieren sich die Risiken zwar deutlich, bleiben aber bei den genannten Glücksspielen (Ausnahme: großes Spiel) signifikant. Auch bei simultaner Betrachtung aller Glücksspiele im multivariaten Modell, womit zusätzlich die individuelle Spieleauswahl berücksichtigt wird, ergeben sich die höchsten Risiken für Geldspielautomaten, gefolgt von Casinospielen im Internet (Odds Ratios 4,77 bzw. 3,75). Vergleichsweise niedrige Risiken finden sich dagegen, modellunabhängig, für die Lotterien. Schlussfolgerungen: Aufgrund des häufig multiplen Spielverhaltens von Problemspielern sollte bei der Analyse von Zusammenhängen zwischen dem Auftreten problematischen Spielverhaltens und der Nutzung einzelner Glücksspielformen die Glücksspielgesamtaktivität einbezogen werden. Regulierungs- und Präventionsmaßnahmen erscheinen den Analysen zufolge insbesondere in Hinsicht auf Geldspielautomaten und Casinospiele im Internet indiziert.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · German representative surveys (SOGS) report problem gambler proportions by game type, including private-operator sports betting.

**Решение:** =

---

### 1298 · R6931

**Investigation on Consuming Behavior of Sports Lottery Player in Wuhan**

2012 · Hubei Sports Science · article · en

The paper takes the consumers of sports lottery as the object of study,which are selected from the 20 sports lottery marketing point of Jiang'an District,Jianghan District,Qiaokou District,Wuchang district and Hongshan District in Wuhan,and sums up their present situation through analyzing their the basic situation and consuming behavior,and then proposes some corresponding countermeasure and suggestions in order to provide practical reference for Wuhan's sports administrative departments on widening the sports lottery consuming market.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of sports lottery players about consumption, with a marketing focus; the abstract doesn't say whether problem gambling was measured.

**Решение:** =

---

### 1299 · R6938

**Who Bets on Sports? Characteristics of Sports Bettors and the Consequences of Expanding Sports Betting Opportunities/¿Quién apuesta? Características de los apostantes deportivos y consecuencias de la expansión de las oportunidades de apostar**

2012 · Estudios de Economia Aplicada · article · es

Currently, several proposed changes in sports betting laws are being debated in the United States and the European Union. This article examines the characteristics of sports bettors in three countries, Canada, Spain, and the United Kingdom, to determine who bets on sports in environments where this activity is both legal and popular. Uncondi¬tional and conditional analyses find that annual participation rates in sport betting are low, and that sport bettors tend to be young males with relatively high incomes. Sports bettors stand to gain the most from an expansion of legal sports betting opportunities, while the negative impacts of increased access to sports betting are expected to be mini¬mal in the United States and difficult to assess in the European Union. Actualmente, un importante numero de cambios en la legislacion del mercado de apuestas deportivas estan siendo debatidos tanto en Estados Unidos como en la Union Europea. En este articulo se examinan las caracteristicas socio-economicas de los apostantes deportivos en Canada, Espana y el Reino Unido con el objeto de determinar el perfil de estos jugadores en contextos donde esta actividad es legal y muy popular. El analisis empirico muestra que la fre¬cuencia de participacion en este mercado es baja y que el perfil de los apostantes tiende a ser el de un hombre joven con ingresos relativamente altos. Se concluye que los propios apostantes serian los potenciales beneficiarios de una expansion de las oportunidades de apostar, mientras que el impacto negativo de esta liberalizacion se espera sea minimo en Estados Unidos y dificil de calcular en la Union Europea.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Analyses sports bettors in Canadian, Spanish and UK survey data, which may include PGSI/DSM-IV; the abstract doesn't say whether problem gambling was reported.

**Решение:** =

---

### 1300 · R6946

**A whole new ball game? An international comparison of fantasy sport usage and outcomes**

2012 · Swinburne figshare (Swinburne University of Technology) · conference-paper · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; fantasy sport usage study might involve paid fantasy play, but it's unclear whether problem gambling was measured.

**Решение:** =

---

### 1301 · R6955

**Gambling Behavior and Problem Gambling Reflecting Social Transition and Traumatic Childhood Events Among Greenland Inuit: A Cross-Sectional Study in a Large Indigenous Population Undergoing Rapid Change**

2012 · Journal of Gambling Studies · article · en · https://doi.org/10.1007/s10899-012-9337-6

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** + · обе модели · опрос населения об азартных играх · Large population survey of Greenland Inuit covering gambling behaviour and problem gambling; activity-level data are likely in the full text.

**Решение:** =

---

### 1302 · R6959

**[Psychological and social impact of online gambling].**

2012 · Bulletin de l'Academie nationale de medecine · article, english abstract, journal article · fre · https://doi.org/10.1016/s0001-4079(19)31872-2

The arrival of online betting has important implications for pathological gambling New gamblers are easily recruited online, especially among young people who are highly involved in web-mediated activities. In addition, gamblers used to betting in "real life" settings can now play their favorite games at any time of the day or night. Negative economic, social and psychological consequences of this new phenomenon are beginning to appear. We present original data from a study conducted in a French University, showing a 7% prevalence of online gambling This activity was associated with male gender, alcohol consumption and smoking. New prevention messages and new means of early diagnosis are needed.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · French university student survey of online gambling (likely includes sports betting); unclear whether a problem-gambling instrument was used.

**Решение:** =

---

### 1303 · R6960

**Testing NLCLiP: Validation of Estimates of Rates of Non-problematic and Problematic Gambling in a Sample of British Schoolchildren**

2012 · Journal of Gambling Studies · article · en · https://doi.org/10.1007/s10899-012-9294-0

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Validation of an adolescent problem-gambling screen (NLCLiP) in a British school survey; may report sports betting participation. No abstract.

**Решение:** =

---

### 1304 · R6966

**Contrast Study on Consuming Condition of New and Old Sports Lottery Players in Suzhou**

2012 · Mianyang Shifan Xueyuan xuebao · article · en

New lottery players are the main force of the sport lottery consumption,and it is quite important to enlarge the scale of sports lottery players and its healthy development by understanding this new group and guiding them to correctly buy sports lottery,and help them become long-term players.This paper introduces that there exist significant differences between new and old players from consumption patterns,as the new players are somewhat blind and arbitrary by comparing their consuming behaviors.

**ИИ:** разошлись — Opus -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Compares consumption patterns of new and old sports lottery players from a marketing angle; no problem-gambling instrument indicated.); Sonnet ? (неясно, измеряли ли проблемную игру: Survey of sports lottery players in Suzhou on consumption patterns; abstract doesn't say whether problem gambling was measured, likely not.)

**Решение:** -

---

### 1305 · R6973

**Gambling and Fantasy: An Examination of the Influence of Money on Fan Attitudes and Behaviors**

2012 · Sport Marketing Quarterly · article, journalarticle, review · en · https://doi.org/10.1177/106169341202100305

The sports gambling industry represents a multi-billion dollar enterprise composed of a variety of activities, the composition of which is under constant debate. Among the topics of importance is the effect of sports gambling (both legal and illegal) on the attitudes and behaviors of sport fans. In particular, investigation into the nature and extent of involvement in activities such as betting on sport events and fantasy sport participation— along with any resultant effects on attitudes and more ‘traditional’ forms of sport fan behavior—could be of interest to sport marketing scholars and practitioners alike. To that end, the current study used an online questionnaire to survey self-identified sports fans on participation in fantasy sports, sports betting, as well as spending habits related to sports. Results suggested that fantasy sports and sports betting appear to serve as complementary investments by fans. The implications for both scholars and practitioners are also discussed.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Online survey of sports fans on sports betting and fantasy participation; the abstract does not say whether problem gambling was measured.

**Решение:** =

---

### 1306 · R6989

**Can bettors convert odds into probabilities? Three studies of how oddsin sports betting is perceived as probabilistic information.**

2012 · article · en

Can bettors convert odds into probabilities? Three studies of how oddsin sports betting is perceived as probabilistic information.

**ИИ:** ? · обе модели · нет аннотации · Empirical studies of sports bettors' perception of odds; no real abstract, so whether a problem-gambling screen was used is unknown.

**Решение:** =

---

### 1307 · R7008

**An empirical evaluation of proposed changes for gambling diagnosis in the DSM ‐5**

2012 · Addiction · article · en · https://doi.org/10.1111/j.1360-0443.2012.04087.x

AIMS: Recommendations related to pathological gambling for the fifth edition of the Diagnostic and statistic manual for mental disorders (DSM) are to eliminate the criterion related to committing illegal acts and reduce the threshold for diagnosis from five to four criteria. This study evaluated the impact of these changes on prevalence rates and classification accuracy. DESIGN: Data were analyzed from five samples, varying in severity of gambling problems. SETTINGS AND PARTICIPANTS: Surveys of randomly selected household residents in the United States (US) (n = 2417), gambling patrons (n = 450), individuals in brief intervention studies (n = 375), patients in community-based gambling treatment programs (n = 149) and participants in randomized intervention studies (n = 319). MEASUREMENTS: The national opinion research center DSM-IV screen for gambling problems (NODS) was administered to all participants. Internal consistency and factor structure were evaluated using both 10 and nine criteria. Base rates, hit rates, sensitivity, specificity and overall agreement were compared across classification systems, using DSM-IV classification as the standard. FINDINGS: Eliminating the illegal acts criterion did not impact internal consistency and modestly improved variance accounted for in the factor structure. In comparing a classification system using four of 10 criteria versus one using four of nine, the four of nine system yielded equal or slightly better classification accuracy in all comparisons and across all samples. CONCLUSIONS: The inclusion of the illegal acts criterion in the proposed DSM-V pathological gambling diagnosis does not appear necessary for diagnosis of pathological gambling and, if it is eliminated, reducing the cut-point to four results in more consistent diagnoses relative to the current classification system.

**ИИ:** разошлись — Opus ? (неясно, есть ли ставки на спорт: NODS diagnostic-criteria analysis that includes a US household survey sample; unclear whether sports betting participation is reported.); Sonnet -7 (другое — напишите почему: NODS psychometric evaluation of DSM-5 criteria across mixed samples, including treatment samples. No sign sports betting was measured or reported.)

**Решение:** ?

---

### 1308 · R7013

**Exploring Youth Gambling in Croatia - Guidelines for Creating Evidence Based Prevention Program**

2012 · conference object, article · en

The aim of this paper is to present key elements of the first evidence-based prevention of youth gambling in Croatia that is developing based on a large research study about youths’ gambling activities, prevalence of risk and problem gambling and correlates of problem gambling among high-school students. A sample of N=1.952 high-school students (47% of boys and 53% of girls) participated in the research from 4 biggest Croatian cities (Zagreb, Split, Osijek & Rijeka). This probability sample included students from different types of school programs and generations, and is representative for adolescents in urban areas. Age range is from 14 to 20 years of age (M=16.56, SD=1, 17). Results show that 83% of high-schools students gambled at least once in their lifetime, 19.0% play sport betting regularly and 6.2% play slot machines regularly. Male students more often play gambling games that are more risky for the development of problem gambling (e.g. sport betting, slot machines, casino, cards, virtual races etc.). Psychosocial consequences of gambling were measured with Canadian Problem Gambling Inventory (CAGI), developed by Wiebe, Tremblay, Wynne & Stinchfield (2010). This instruments measures global severity score on three levels as follows: (1) no problem, (2) low-to-moderate severity and (3) high severity. Our results reveal that 12% of high-school students show serious, high severity consequences due to their gambling activities, and 17% low-to-moderate severity. Boys are in greater risk of developing harmful psychosocial consequences of gambling as they also gamble more often. Our results also indicate that students who have more serious consequences due to their gambling activities have more friends that gamble, manifest other risky behavior with some elements of delinquent behavior, are more motivated by earning money and believe more often that they can predict and control the outcome of the game. They are also less responsible and worry less for other people, show more tendency for hedonism with less orientation for the future and achievement, and have generally less sense of control in their life. Even though in Croatia gambling is prohibited for minors (children under the age of 18), results clearly indicate their involvement in these activities and provide strong arguments for the development and implementation of preventive interventions. In this paper, with our major results, we shall also present developing activities of the first Croatian evidence-based prevention program of youth gambling in school setting that focuses on the most predictive factors for developing problem gambling syndromes.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · High-school student survey measuring sports betting participation and problem gambling with CAGI; could report PG among sports bettors.

**Решение:** =

---

### 1309 · R7031

**Prevalence of gambling and problem gambling in New South Wales**

2012 · Acquire (CQUniversity) · report · en · https://doi.org/10.13140/2.1.1905.9526

This report contains the results from the 2011 survey (N=10,000 adults) of the prevalence of gambling and problem gambling in New South Wales (NSW). The research was undertaken by Ogilvy Illumination on behalf of the NSW Government. The survey found that 65% of the NSW population had participated in at least one gambling activity in the last 12 months. The most popular gambling activity was lotteries (41%) followed by instant scratch tickets (28%), gaming machines (27%), horse-greyhound races (24%), Keno (14%), sports betting (8%), table games in a casino (7%) and casino or pokies-style games on the Internet (2%). Problem gambling was measured using the Problem Gambling Severity Index. The survey classified 0.8% of adults as problem gamblers, 2.9% as moderate risk gamblers and 8.4% as low risk gamblers. Problem gamblers were significantly more likely to be male, younger (18-24 years and 35-54 years), be single, be divorced/separated/widowed, unemployed,\nhave low educational attainment and be a regular gambler on gaming machines, on horse or greyhound races and on sports or non-sports events.

**ИИ:** + · обе модели · опрос населения об азартных играх · 2011 NSW population prevalence survey (N=10,000) that measured sports betting participation and PGSI; reports problem gambling by activity.

**Решение:** =

---

### 1310 · R7033

**Beyond description: Understanding gender differences in problem gambling**

2012 · Journal of Behavioral Addictions · article · en · https://doi.org/10.1556/jba.1.2012.3.5

Background and aims Though women make up roughly one third of all problem gamblers, research has typically focused on male problem gamblers. Recent research has started to shift its attention toward the importance of gender. However, studies rarely attempt to understand gender differences in problem gambling or subject these differences to thorough multivariate analyses. To address some of the gaps in our knowledge of gender differences, we examine whether patterns of gambling behavior and psychological factors mediate the relationship between gender and problem gambling. Methods We use logistic multiple regression to analyze two large Canadian datasets - the 2005 Ontario Prevalence Survey and the 2007 Canadian Community Health Survey. Results Variables found to mediate the relationship between gender and problem gambling are the type(s) of game(s) played (in the 2005 Ontario Prevalence Survey) and the number of games played (in the 2007 Canadian Community Health Survey). Conclusions Men are more likely to be problem gamblers than women, and this gender difference is understandable in terms of differences in patterns of gambling behavior. We conclude that men experience problems because they play riskier games and women experience problems because they prefer chance-based games, which are associated with significantly higher odds of problem gambling. We specify the three main ways that women's reasons for gambling - to escape or for empowerment - translate into chance-based games.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Analysis of Canadian population surveys (CPGI) by game type; sports betting may be among the game types analysed.

**Решение:** =

---

### 1311 · R7041

**Dangerous Games: The Psychological Case for Regulating Gambling**

2012 · SSRN Electronic Journal · article, other literature type, preprint · en · https://doi.org/10.2139/ssrn.2103619

The gambling market is growing rapidly, as is the number of gambling addicts. This is fueling the call for changes in regulation. Some regulators intend to enable the entertainment industry to fully harvest a market potential magnitudes larger than today’s gaming market by minimizing regulation. Others aim at further limiting games to reduce pathological gambling and to enhance consumer protection. Current legal doctrine subjects a game to restrictions if chance, rather than skill, is its predominant trait. This rests on the assumption that only games of chance are harmful. As our experimental study shows, this is wrong: if a notion of skill seems relevant for a game, players fall prey to psychological biases that are breeding grounds for addiction and economic exploitation. We therefore suggest to abandon the distinction between skill and chance, and to condition regulation instead on the psychological biases a game induces, i.e. on the danger it actually poses.The empirical part of the argument focuses on sports bets which are among the set of particularly controversial games, as there is contention whether skill or chance dominates the performance of bettors. Recent academic papers and court decisions argue that such games are properly categorized as games of skill, and as such should not fall afoul of current gambling laws. We show that, empirically, skill does have an — albeit extremely limited — impact on performance. However, the participants’ general assumption that skill does matter for performance makes them suffer an illusion of control and overconfidence, that as has been established in clinical research makes them highly vulnerable for excessive betting and pathological gaming behavior. We therefore suggest to subject sports betting to regulation.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Experimental study of sports bettors (illusion of control, overconfidence) in a regulatory paper; the abstract doesn't say whether a problem-gambling screen was used.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Experimental study on skill vs chance and biases in sports betting for regulation; no problem-gambling instrument evident, regulatory argument.)

**Решение:** ?

---

### 1312 · R7046

**Advances in sports and athletics**

2012 · Medical Entomology and Zoology · article · en

Preface Risk Management Strategies at Division I Intercollegiate Football Stadiums: Do Spectators Perceive They Are Protected Against Terrorism? Negligent Marketing: What All Sport Marketers Should Know Investigating Fantasy Sport Participation among College Students A Look at Academic Reform, Student Athlete Compensation & the Case for a New Classification of Student-Athlete Motivational Profiles of Sports Fans Attending Different Levels of Baseball Games Characteristics of Success in Men's Football & Men's Basketball at the Division I Level Alternative Dispute Resolution in Sport: A Conceptual Approach Just Not on My Turf: Student-Athletes' Perceptions of Homosexuality New Technology Holds Promise for the Future Application of Psychophysiological Methods for the Enhancement of Performance During Sport & Exercise Identification with Multiple Sporting Teams: How Many Teams Do Sport Fans Follow? Motivations of International Student-Athletes to Participate in Intercollegiate Athletics Athletic Administrators Perceptions of Work-Life Balance Policies: A Divisional Comparison The Impact of Playing Position on Perceptions of Horizontal Interpersonal Power in Sport Index.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Edited book, mostly off-topic; one chapter surveys college students on fantasy sport participation. Unclear whether it was for money or used a PG measure.); Sonnet -6 (не про азартные игры или «ставка/лотерея» в другом смысле: Table of contents of a sports journal volume; fantasy sport participation among students is listed but no sign of gambling or problem-gambling measurement.)

**Решение:** ?

---

### 1313 · R7047

**Knowledge, views and experiences of gambling and gambling‐related harms in different ethnic and socio‐economic groups in New Zealand**

2012 · Australian and New Zealand Journal of Public Health · article · en · https://doi.org/10.1111/j.1753-6405.2012.00847.x

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; could be a NZ population survey with a problem-gambling screen, or a qualitative/attitudes study. Needs the full text.

**Решение:** =

---

### 1314 · R7050

**Analysis of Reliability and Validity on Satisfaction Scale for Sports Lottery Buyers**

2012 · Advanced Science Letters · article, journal-article · en · https://doi.org/10.1166/asl.2012.1933

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Validation of a consumer satisfaction scale for sports lottery buyers; no indication a problem-gambling instrument was used.); Sonnet ? (нет аннотации: Sports lottery buyers survey, but it is a satisfaction scale validation with no abstract. Unclear whether problem gambling was measured.)

**Решение:** ?

---

### 1315 · R7053

**Psychological and Behavioral Characteristics of Elderly Sports Lottery Buyers**

2012 · Wuhan Ti-Yuan xuebao · article · en

The psychological and behavioral characteristics of 173 elderly sports lottery buyers in ten provinces or cities were compared with those of 2359 younger buyers.It could be seen that the elderly buyers spent more on sports lottery than the younger buyers.They preferred to buy lotto-type,high-frequency lottery.They bought lottery for more communication with others and to kill time.Their family usually supported their lottery buying.They did not like to buy lottery for investment.Instead,they bought for entertainment and public welfare.They were generally more satisfied with the lottery issuing than the younger buyers.However,they were not much satisfied with the de sign,lottery selling stores and managing departments.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of China sports lottery buyers; abstract covers spending and motives, and the full text might include a problem-gambling screen.

**Решение:** =

---

### 1316 · R7055

**Gambling Behaviors of Former Athletes: The Delayed Competitive Effect**

2012 · UNLV Gaming Research & Review Journal · article, journalarticle · en · https://doi.org/10.9741/2327-8455.1124

Stephen M. Weiss* Sherri L. Loubier Gambling behaviors in current athletes, former athletes and non-athletes were examined. Gambling tendencies were determined from participants' responses on the South Oaks Gambling Screen (SOGS). A delayed competitive effect among athletes that might surface in the form of pathological gambling was investigated. To test this novel theory, participants were divided into three groups: athletes who are currently playing sports, former athletes who used to play competitive sports and non-athletes who have never participated in competitive sporting events. A 2 x 3 independent groups AN OVA was utilized comparing SOGS scores across gender and athletic status. The mean score for former athletes on the SOGS was significantly higher than for both current athletes and non-athletes as was the frequency of those classified as "probable pathological" gamblers suggesting the possibility that a delayed competitive effect might exist among former athletes. Additionally, a higher percentage of former athletes were involved in sports gambling.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Survey of athletes and non-athletes using SOGS that also measured sports gambling participation.

**Решение:** =

---

### 1317 · R7060

**Development of an Internet Questionnaire System for Sports Lottery Buyers**

2012 · Sport Science Research · review, article · en

Due to the deficiencies of paper questionnaire,such as insufficient samples,unreal data,long survey period,high cost,low efficiency of statistics analysis,etc,the author,based on the merits of the traditional questionnaire design and web design,shifts the paper questionnaire for identifying the purchasing behavior of problem lottery buyers to web questionnaire.A system for internet questionnaire and statistics analysis has been designed and developed.The article introduces the design concept,structure,function module and application of the system.

**ИИ:** ? · обе модели · другое · Paper mainly on building a web questionnaire system for problem sports lottery buyers; its application may include survey data.

**Решение:** =

---

### 1318 · R7068

**Las apuestas deportivas en España**

2012 · Investigación y marketing · article · es

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; title on sports betting in Spain in a marketing journal could describe a bettor survey, possibly with a problem-gambling measure.

**Решение:** =

---

### 1319 · R7077

**Belief in luck or in skill: which locks people into gambling?**

2012 · Journal of gambling studies · journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1007/s10899-011-9263-z

According to the social axioms framework, people's beliefs about how the world functions (i.e., internal or external locus of control) are related to their social behaviors. Previous researchers have attempted to relate locus of control to gambling behavior, but the results have not been clear-cut. The present study speculated that the effects of perceived control (i.e., belief in luck and belief in skill) on gambling behavior are domain-specific and vary with the type of gambling. A total of 306 adult Macau residents ranging in age from 18 to 65 with casino gambling experience were recruited by going door to door. Empirical data on gambling frequency and perceived control relating to 13 types of gambling were collected. Our results demonstrated that the effects of belief in luck or skill on gambling behavior varied across different gambling categories. Specifically, for football lottery, Chinese lottery, and baccarat, it was not belief in skill but rather belief in luck that was a positive significant predictor of gambling frequency. Only for slot machines and stud poker did belief in skill significantly predict gambling frequency. For the remaining eight gambling categories, neither belief in luck nor belief in skill could predict gambling frequency. Our findings indicate that neither internal nor external locus of control can consistently explain people's gambling behaviors. Instead, which factor plays a greater role in a person's gambling behavior is dependent on the gambling type. Therefore, the finding that not all gambles are created equal might be a promising avenue for further research and treatment approaches.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Macau gambler survey covering football lottery; abstract mentions only gambling frequency and perceived control, so a problem-gambling screen is uncertain.

**Решение:** =

---

### 1320 · R7080

**Pathological gambling: betting and gambling in the life of sport journalists**

2012 · Digital Repository (National Repository of Grey Literature) · dissertation · cs

This thesis deals with the definition of the concept of pathological gambling, diagnosis, prevalence and a description of vulnerable groups. It also discusses the creation, development and various stages of pathological gambling. Theoretical knowledge is enhanced by our own research, carried out a questionnaire, which has pointed out that the profession can be a risk factor for developing an illness / addiction. The research objective is to describe the rate and quality of risk-taking behavior in gambling on sports editor, and identify any related pathological gambling with their selected characteristics. The paper looks at what it looks like gambling and betting on sports editors in terms of rates, forms and circumstances. Whether the people in this group of pathological gambling occurs and, if so, to what extent and with what consequences. They try to answer it then also, what is the relationship between work characteristics and playing sports editor of gambling or betting. How this relationship sports editors perceive themselves and how to understand. Keywords: Pathological gambling, pathological player, gambling, gambling

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Questionnaire thesis on sports betting among sports journalists assessing pathological gambling; the abstract does not say which instrument was used.); Sonnet + (игроки, есть ставки на спорт и инструмент: Questionnaire survey of sports journalists on gambling and betting, identifying pathological gambling; likely uses a screening instrument and could report PG among sports bettors.)

**Решение:** ?

---

### 1321 · R7096

**Part 5: Fans and Fantasy Sports**

2011 · Lexington Books · part of book or chapter of book, book-chapter · en · https://doi.org/10.5771/9780739146224-253

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Book section header on fantasy sports fans with no abstract; a problem-gambling measure is unlikely but can't be ruled out.

**Решение:** =

---

### 1322 · R7106

**Gambling on Sports**

2011 · Edward Elgar Publishing eBooks · book-chapter · en · https://doi.org/10.4337/9780857936301.00016

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -1 (обзор, комментарий, теоретическая, правовая или регуляторная работа: 2011 Edward Elgar handbook chapter with no abstract; probably an economics overview of sports betting, not a survey of bettors.); Sonnet ? (нет аннотации: Book chapter "Gambling on Sports" (2011, Edward Elgar) with no abstract; likely economics or review, but content cannot be determined from the title.)

**Решение:** ?

---

### 1323 · R7114

**Essays in economics : evidence from online sports gambling**

2011 · Medical Entomology and Zoology · article · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: Economics essays using online sports gambling data; most likely betting-market or behavioural analysis with no problem-gambling instrument.); Sonnet ? (нет аннотации: Economics thesis on online sports gambling with no abstract; likely behavioural or market data, but a problem-gambling measure can't be ruled out.)

**Решение:** ?

---

### 1324 · R7124

**Complex Factors and Behaviors in the Gambling Population of Italy**

2011 · Journal of Gambling Studies · article · en · https://doi.org/10.1007/s10899-011-9283-8

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; title suggests an Italian general-population gambling survey (likely IPSAD with CPGI), possibly with activity data.

**Решение:** =

---

### 1325 · R7127

**What are the most harmful forms of gambling? Analyzing problem gambling prevalence surveys**

2011 · Gothenburg University Publications Electronic Archive (Gothenburg University) · other literature type, review, article · en · http://hdl.handle.net/2077/26165

Eighteen national prevalence surveys of problem gambling (PG), most of them from Europe, were analyzed to assess the relative harmfulness of various forms of gambling. It was found that interactive Internet gambling, casino gambling, electronic gaming machines, and high-stakes unregulated/illegal gambling are often relatively closely associated with PG, while lotteries and instant lotteries appear relatively harmless. Other forms of gambling—sports pools, bingo, horse betting, and sports betting—are typically relatively moderately associated with PG. This paper discusses the possibilities and limitations of assessing the harmfulness of various forms of gambling by analyzing prevalence survey data. It is concluded that although such analyses yield valuable insights, they should be complemented by other sources of information, such as statistics on the gambling activities of those seeking help for PG and qualitative studies of problem gambling.

**ИИ:** разошлись — Opus -1 (обзор, комментарий, теоретическая, правовая или регуляторная работа: Secondary review of 18 published national prevalence surveys comparing how harmful different gambling forms are; no new primary data.); Sonnet ? (другое: Secondary analysis of 18 national PG surveys by gambling form including sports betting; review-like, but may report PG among sports bettors or point to primary surveys.)

**Решение:** ?

---

### 1326 · R7151

**Prevalence and Correlates of 12-Month Prescription Drug Misuse in Alberta**

2011 · The Canadian Journal of Psychiatry · article · en · https://doi.org/10.1177/070674371105600106

OBJECTIVE: We examined the prevalence and correlates of prescription drug misuse (PDM) in a population-based sample of adults from Alberta. METHODS: Data were collected from 3511 adults in Alberta aged 18 years and older in 2002 using a computer-aided telephone survey; the survey response rate was 57.4%. RESULTS: The prevalence of 12-month PDM in Alberta was 8.2% in 2002. Opiates were the most frequently misused drug class, followed by sedatives, stimulants, and tranquilizers. Current disability was particularly associated with PDM. Odds of PDM were also elevated among adult students and adults with a high school diploma relative to adults with a post-secondary degree. Past-year problem gambling, illicit drug use, and alcohol use and dependence were each associated with PDM, while past-year binge drinking and daily smoking were not. CONCLUSIONS: Findings suggest PDM was an important public health concern in Alberta in 2002. Estimates suggest prescription use and misuse have increased substantially in Canada since that time. There is an urgent need for an ongoing assessment of this evolving problem so that effective prevention and therapeutic strategies can be developed.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Population survey that measured past-year problem gambling as a correlate of drug misuse; unclear whether participation in sports betting was recorded.

**Решение:** =

---

### 1327 · R7156

**Poker, Sports Betting, and Less Popular Alternatives**

2011 · Youth & Society · article, journalarticle, review · en · https://doi.org/10.1177/0044118x10396641

The authors argue that the recent increase in poker play among adolescent males in the United States was primarily attributable to high-status male youth who are more able to organize informal gambling games (e.g., poker and sports betting) than are low-status male youth who are left to gamble on formal games (e.g., lotteries and slot machines). Using participation in sports as a proxy for status, the authors test the prediction that male athletes were more likely to engage in informal gambling and were largely responsible for the recent and much-discussed poker craze among adolescents. These and related predictions are supported using data from consecutive cross-sectional surveys of American youth from 2002 to 2008. Despite their social status, however, male youth engaging in informal gambling are more at risk for gambling problems than are those engaging in formal gambling. The authors discuss the dilemmas that their findings present for the prevention of problem gambling in young people.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · US youth surveys (2002–2008) measured sports betting and gambling-problem risk; the full text needs checking for the instrument used, likely DSM-based.

**Решение:** =

---

### 1328 · R7171

**Investigation on the Status Quo of Shanghai Problem Sports Lottery Buyers**

2011 · Sport Science Research · article · en

By the ways of document consultation,field inspection and questionnaire,elaborates on the concept of problem gambling,negative social influence and evaluation criteria,analyzes the status of problem gambling in Shanghai sports lottery and discusses the cause for problem gambling.Suggestions are put forward from the viewpoint of forming a social salvation mechanism for problem lottery buyers.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Questionnaire survey of Shanghai sports lottery buyers about problem gambling; the abstract doesn't say whether a screening instrument was used or which lottery games were covered.); Sonnet + (беттеры + инструмент: Questionnaire survey of Shanghai sports lottery buyers analysing problem gambling status using evaluation criteria; likely reports problem gambling prevalence among sports lottery players.)

**Решение:** ?

---

### 1329 · R7172

**Online and sports betting: new responsible gambling environments**

2011 · Cross Connect (Southern Cross University) · article · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; university magazine piece on online and sports betting, possibly summarising a research project, so the full text needs checking.

**Решение:** =

---

### 1330 · R7185

**[Problematic and pathologic gambling in Hungary: the Hungarian version and use of the South Oaks Gambling Screen (SOGS-HU)].**

2011 · PubMed · other · en · https://pubmed.ncbi.nlm.nih.gov/22058255/

BACKGROUND AND AIM: Gambling is a form of entertainment with a history of thousand years that has a significant potential for development and has become a widely spread global industry recently. Excessive gambling can take the form of problem, or even pathological gambling. The South Oaks Gambling Screen (SOGS) is the most common measure used for the assessment of problem and pathological gambling. The aim of our study was the development and psychometric analysis of the Hungarian version of the instrument, and its verification on a representative population sample. METHOD: The administration of the instrument was conducted within the frame of the National Household Survey on Addiction Problems, where 2710 persons were interviewed from Hungarian population between 18 and 64 years. RESULTS: The psychometric properties of SOGS-HU are adequate. 65.3% of the respondents had ever gambled. The most popular games are lottery and other number draw games. According to the data obtained by SOGS 1.9 % of the sample was considered to be problem gambler, and 1.4 % of the sample was considered to be pathological gambler. In both groups the proportion of man was higher, while additional risk factors were lower income, lower expected level of education and legal / illegal substance use. CONCLUSION: Based on these results Hungary can be found in the middle-rank of Europe regarding the prevalence of problem and pathological gambling.

**ИИ:** + · обе модели · опрос населения об азартных играх · Hungarian national representative survey; it measured participation in gambling games and used SOGS, so activity tables are likely in the full text.

**Решение:** =

---

### 1331 · R7186

**Relationship between compulsive addiction to sport-gambling and the quality of life of participants in recreational**

2011 · Korean Journal of Sports Science · article · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; Korean study on compulsive sport-gambling addiction and quality of life — it may have used a problem-gambling screen.

**Решение:** =

---

### 1332 · R7187

**Overseas Internet Poker and Problem Gambling in Finland 2007: A Secondary Data Analysis of a Finnish Population Survey**

2011 · Nordic Studies on Alcohol and Drugs · article · en · https://doi.org/10.2478/v10199-011-0005-4

AIMS Internet gambling has been associated with Increased risk of problem gambling. In this study different clusters of gambling activities and behavioral measures of gambling were used In analyses, which aimed at Investigating prevalence of problem gambling in Internet poker gamblers and In other gamblers. DATA AND METHODS The study consisted of secondary analyses of a Finnish population data set collected in 2007 (telephone survey, reaching 5,008 Finns aged 15 years and over). Bivariate statistics and logistic regression models were used in the analyses. Results When only age and sex were added to logistic regressions, overseas Internet poker (IP) gamblers were almost three times more likely to be problem gamblers than other gamblers. However, when also behavioral measures of gambling were added to equations, no difference in problem gambling between IP and other gambling was found. In the slot machine (SM) cluster an opposite phenomena occurred: when behavioral variables were added to analyses, subjects in SM cluster were more likely to be problem gamblers than other gamblers. When IP and SM were compared in the same multivariate analysis, subjects in both of these gambling clusters were more likely to be problem gamblers than other gamblers. Conclusions The present study shows the importance of behavioral measures in gambling research. The level of involvement in gambling should be one of the primary interests in studies and interventions.

**ИИ:** + · обе модели · опрос населения об азартных играх · Secondary analysis of a 2007 Finnish population gambling survey that grouped gambling activities into clusters and measured problem gambling; sports betting clusters are likely.

**Решение:** =

---

### 1333 · R7192

**Pay Attention to the Soccer Gambling Problem**

2011 · ICCC International Digital Design Invitation Exhibition · article · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: Entry in a digital design exhibition, likely an awareness artwork or poster rather than an empirical survey.); Sonnet ? (нет аннотации: No abstract; title suggests soccer gambling problem, possibly a commentary or a survey; empirical design and problem-gambling measure cannot be determined.)

**Решение:** ?

---

### 1334 · R7216

**Predictors of Gambling Behaviors in Filipino Americans Living in Honolulu or San Francisco**

2011 · Journal of Gambling Studies · article · en · https://doi.org/10.1007/s10899-011-9248-y

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Community gambling survey of Filipino Americans; no abstract, may have measured problem gambling and gambling activities including sports betting.

**Решение:** =

---

### 1335 · R7222

**EFFECTS OF ENTRy FEES AND ExTRINSIC REWARDS ON FANTASy SPORT USERS’ WINNING CONFIDENCE AND ANTICIPATED EMOTION**

2011 · review

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; looks like a fantasy sports experiment on confidence and emotion, and it is unclear whether a problem-gambling instrument was used.

**Решение:** =

---

### 1336 · R7227

**Quantitative Research on Consumers' Cognitive Bias in Consumption of Sports Lottery**

2011 · Shanghai Tiyu Xueyuan xuebao · article · en

Using the method of questionnaire investigation,the present paper discussed the consumers' bias in sports lottery consumption and its influence over gambling behavior.It concluded that most of sports lottery consumers are young people of middle and low income with better education and short period of lottery consumption;the general cognition of the consumers is good and the consumers on the whole are rational in lottery buying but there are still some problem consumers;nearly sixty percent of consumers have preference to cold or hot numbers and there exist vast differences in superstition;cognitive bias has significant influence over lottery buying,which in turn results in the internal psychological mechanism of problem gambling behavior.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Questionnaire survey of Chinese sports lottery consumers mentions problem consumers; unclear whether a PG instrument or quiz-type games were used.

**Решение:** =

---

### 1337 · R7238

**A REAL LOOK AT FANTASy : DOES MONEy MATTER ?**

2011 · review

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the title is about fantasy sports for money, which could fit, and the 'Review' label may just be a database tag.

**Решение:** =

---

### 1338 · R7269

**Gambling and the NFL**

2011 · Springer eBooks · book-chapter · en · https://doi.org/10.1007/978-1-4419-6290-4_13

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: Likely a chapter in a Springer NFL economics book on betting market efficiency, not a problem-gambling survey of people.); Sonnet ? (нет аннотации: Book chapter on NFL gambling with no abstract; likely economics or commentary but could report survey data, so full text check is warranted.)

**Решение:** ?

---

### 1339 · R7287

**Football Betting Trends**

2011

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the title could mean betting-market trends or trends in betting participation, so it can't be judged.

**Решение:** =

---

### 1340 · R7310

**Analysis of Actual Internet Sports Gambling Behavior**

2011

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; title suggests bwin account data (behavioural only), but a problem-gambling measure can't be ruled out.

**Решение:** =

---

### 1341 · R7317

**Game Over: Empirical Support for Soccer Bets Regulation**

2011 · Psychology, Public Policy, and Law · article, other literature type, research · eng · https://doi.org/10.2139/ssrn.1724602

In many countries, betting in sports is highly regulated. In Germany, however, there are current debates whether regulation should be loosened. A crucial part of the argument is that sport bets could be qualified as ‘games of skill’ that are considered to be less dangerous by German Law than ‘games of chance’, and are thus assumed to need less regulation. We explore this hypothesis in three incentivized online studies on soccer betting (N=214) and provide evidence against two crucial parts of this argument. First, we show that there are no overall effects of skill on accuracy in soccer bets and monetary earnings do not increase with skill. Hence, soccer betting cannot be considered a game of skill. Second, we show that soccer betting induces strong overconfidence and illusion of control, particularly for people who assume they have high skill, and that these biases lead to increased betting. Cognitive biases that might cause financial harm for bettors or even lead to problematic or pathological gambling behavior are even stronger for soccer bets compared to bets on the outcome of lotteries. Concerning the main aims of legal regulation for gambling in German law, our results strongly speak for regulation of soccer bets.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Incentivized online soccer-betting experiments (N=214) on skill and overconfidence; abstract doesn't say whether a problem-gambling screen was used.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Incentivized online experiments on soccer betting skill and cognitive biases; no problem-gambling instrument reported, only betting accuracy, overconfidence and earnings.)

**Решение:** -

---

### 1342 · R7330

**Analysis of Consumer Behavior on Guangxi Sports Lottery**

2011 · Journal of Liuzhou Vocational & Technical College · review, article · en

By using the methods of interview,literature consultation,mathematical statistics,questionnaire survey,this paper deals with consumer behavior on Guangxi Sports Lottery,in order to grasp the full range of consumers′ characteristics and the basic status and provide business strategies and theoretic reference for promoting Guangxi sports lottery market.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Questionnaire survey of Guangxi sports lottery consumers, market-focused; abstract doesn't say whether problem gambling was measured.

**Решение:** =

---

### 1343 · R7346

**The Impact of Televising World Cup Football on Productivity Loss and Volume of Gambling in Bangkok and Vicinity**

2011 · review

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; probably a Bangkok survey of World Cup football betting, but unclear whether problem gambling was measured.

**Решение:** =

---

### 1344 · R7353

**한국 대학생의 도박참여 실태와 도박중독 유병률 조사**

2011 · 정신보건과 사회사업 · article · ko

본 연구는 대학생의 도박참여 실태와 도박중독 유병률을 파악하고자, 국내에서 처음으로 전국의 4년제 대학교 재학생을 모집단으로 한 2,026명을 표본으로 조사연구 하였다. 연구결과 CPG I 척도상의 대학생 문제도박 심각도는 비문제도박 68.7%, 저위험도박 20.3%, 중위험도박 9.5%, 문제도박 1.5% 순으로 나타났다. 이 중 중위험도박자와 문제도박자를 합한 도박중독 유병률이 11%에 달하며, 이는 우리나라 성인의 도박중독 유병률 6.1%보다 더 높은 수치이다. 스포츠토토 구매경험이 있는 대학생의 도박중독 유병률은 21.4%이고, 인터넷도박 경험이 있는 대학생의 도박중독 유병률은 19.3%로, 이 유형들은 대학생 전체 유병률보다 2배가량 높은 것으로 나타났다. 초등학교 이하시기에 도박을 처음 경험하는 집단에서 도박중독 문제가 유의미한 수준으로 더 높게 나타났으며, 여학생보다는 남학생이, 군필 집단보다는 군미필/면제 집단에서 도박중독 문제가 더 심각하게 나타났다. 이러한 결과에 기초하여 대학생 대상의 도박중독 예방정책이 시급히 마련될 필요가 있고, 도박중독예방교육이 초등학교부터 대학까지 정규교육과정에 반영될 필요가 있음을 논의하였다.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · National survey of Korean university students using CPGI; reports 21.4% problem/moderate-risk prevalence among Sports Toto purchasers.

**Решение:** =

---

### 1345 · R7354

**대학생의 도박중독 실태**

2011 · 대한보건협회 보건종합학술대회 · article · ko

[연구배경] 한국에서 전체 연령대 중 20대의 도박참여율이 가장 높다. 심각한 성인 도박중독자들은 대부분 10대부터 게임과 내기를 좋아했다. 대학생의 도박문제가 일반인과 비교해 더 심각할 수 있다. 그럼에도 불구하고, 우리나라의 경우 대학생 도박문제에 대한 연구가 매우 부족한 상황이다. [연구목적] 본 연구의 목적은 대학생을 대상으로 한 전국 규모의 도박문제 실태조사를 통해 한국 대학생의 도박중독 유병률과 도박관련 문제를 파악하기 위함이다. [연구방법] 본 연구에서는 구조화된 설문지를 이용하여 연구 참여에 동의한 대상자에게 자기기입식 조사를 실시하였으며 연구표본은 전국의 4년제 대학교 재학생 2,026명이었다. [연구결과] 연구결과 CPGI(Canadian Problem Gambling Index) 척도 상의 대학생 문제도박 심각도는 비문제도박 68.7%(1,391명), 저위험도박 20.3%(411명), 중위험도박 9.5%(193명), 문제도박 1.5%(31명) 순으로 나타났다. 이중 중위험도박자와 문제도박자를 합한 도박중독 유병률이 11%에 달하는 것으로 나타났는데, 이는 우리나라 성인의 도박중독 유병률 6.1% 보다 더 높은 수치이다. 응답자 중 스포츠토토 구매경험이 있는 대학생의 도박중독 유병률은 21.4%, 인터넷도박 경험이 있는 대학생의 도박중독 유병률은 19.3%로 대학생 전체 유병률에 비해 2배가량 높은 것으로 나타났다. 대학생의 도박중독 문제는 초등학교 이하 시기에 도박을 처음 경험하는 집단에서 도박중독 문제가 유의미하게 더 높게 나타났으며, 여학생 보다는 남학생이, 남학생 중에서는 군필 집단 보다는 군미필/면제 집단에서 도박중독 문제가 더 심각하게 나타났다.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · This is a national survey of Korean university students using the CPGI. It reports a 21.4% problem-gambling rate among students who bought Sports Toto.

**Решение:** =

---

### 1346 · R7357

**생활체육 참가자의 운동내기 중독과 삶의 질의 관계**

2011

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; Korean study on 'exercise betting' addiction among recreational sports participants; instrument and type of betting unclear.

**Решение:** =

---

### 1347 · R7358

**생활체육 참가자의 운동내기 중독과 삶의 질의 관계**

2011 · article · ko

The purpose of this study was to identify the relationship between compulsive addiction to sport-gambling and exercise and the quality of life of participants in recreational sports. For this study, 818 subjects engaging in recreational sports in three major provinces, Seoul, Kyounggi-do, and Chungcheongbuk-do, were recruited and factor analysis, reliability analysis, crosstabulation, one-way analysis of variance (ANOVA), and Simple regression analysis were used as statistical methods to broaden the understanding of various findings. Those findings obtained throughout these statistical methods were as follows. First finding was that 741 (90.6%)of 818 subjects had experienced the sport-gambling addiction in the past years and male subjects (93.6%) were exposed to sport-gambling experiences more than female subjects (80.6%). Second finding was that there were significant differences in the responses of previous sport-gambling experience by the degree of addiction to sport-gambling. For the frequency of sport-gambling, a normal group experiences sport-gambling 1 to 2 times a month, 1 to 2 times a year, a severe gambling addiction group experiences 1 to 2 times a month, a normal group experiences 1 time a week, and a problematic gambling addition group experiences 1 to 2 times a month. For all groups, paying for meals was considered the most popular type of sport-gambling. The average amount of money spent per event was 5,000 to 10,000 won and 10,000 to 30,000won for a normal group, 10,000 to 30,000 won for a severe gambling addiction group, and 5,000 to 10,000 won for a problematic gambling addiction group. Third finding was that there were significances in the responses of the quality of life by sport-gambling. The quality of life was influenced by the frequency of sport-gambling (physical, living environmental), the type of sport-gambling (physical, living environmental, and mental), the amount of money spent per event (physical, social, and living environmental). Fourth finding was that there were significant differences in the responses of the quality of life by the degree of addiction to sport-gambling. A normal group showed higher scores in the mental items than a severe gambling addiction group. This finding can be explained by that sport-gambling addiction influences the mental quality of life negatively.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Recreational athletes betting informally on their own games; addiction groups reported, but the instrument used and whether this counts as sports betting are unclear.); Sonnet + (беттеры + инструмент: Survey of 818 Korean recreational sport participants with sport-gambling experience, classified into normal, problematic and severe gambling groups; instrument unnamed but prevalence by group is likely reported.)

**Решение:** ?

---

### 1348 · R7363

**Abstracts of Student Talks**

2010

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Generic conference abstract collection with no abstract; it may contain a relevant gambling talk, so check the full text.

**Решение:** =

---

### 1349 · R7367

**Demographic and social variables associated with problem gambling among men and women in Canada**

2010 · Psychiatry Research · article · en · https://doi.org/10.1016/j.psychres.2009.10.003

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; likely a Canadian population survey (probably CCHS 1.2, CPGI) that may report gambling activities, including sports lotteries.

**Решение:** =

---

### 1350 · R7376

**Gambling on the Lottery: Sociodemographic Correlates Across the Lifespan**

2010 · Journal of Gambling Studies · article · en · https://doi.org/10.1007/s10899-010-9228-7

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract. Probably uses US national youth and adult gambling surveys that measured several gambling activities and problem gambling; needs full-text check.

**Решение:** =
