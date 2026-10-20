# Проверка с метками ИИ, часть 2

Записи 151–300 из 1525, с метками обеих моделей над строкой решения. Модели согласны и вы тоже — поставьте `=`; иначе свой код (`+`, `?` или `-`, причина не нужна). Если модели разошлись, `=` не годится — нужен ваш код. Решаете вы.

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

### 151 · R0988

**Comparative Analysis of Video Gamers, Esports Spectators, and Esports Athletes on Gambling, Gaming, and Psychological Characteristics.**

2026 · Journal of gambling studies · journal article, comparative study · eng · https://doi.org/10.1007/s10899-025-10454-3

Collegiate athletes in traditional sports are a vulnerable population for problem gambling. Little is known about whether collegiate esports (competitive video gaming) athletes share the same vulnerability. Additionally, existing research combines esports groups into a larger sample of involvement, which does not capture potential distinct behaviors. This cross-sectional comparative study aimed to address this gap by comparing gambling behaviors, gaming behaviors, and psychological characteristics of video gamers (n = 234), esports spectators (n = 137), and collegiate esports athletes (n = 116) from North America. An online survey was distributed to universities and collegiate esports communities through convenience sampling. All participants completed self-report measures assessing gambling behaviors, gaming behaviors, emotional regulation, and impulsivity. Kruskal-Wallis H-tests and post-hoc comparisons were used to assess group differences. Results show esports athletes significantly having the highest proportion of problem gambling (19%) relative to spectators (16.9%) and gamers (5.3%). Esports spectators significantly spent the most median money per day gambling (Median = 0.65), followed by gamers then esport athletes (Median = 0.00). Spectators had the highest problem gaming proportion (16.1%) than esports athletes (6.9%) and video gamers (3.4%). Video gamers scored the lowest on all subscales of gaming motives, whereas spectators reported highest motivations in escapism, coping and fantasy. Esports athletes' motivation was highest in social, competition, and skill development. Esports spectators reported the most difficulties in emotional regulation, followed by esports athletes then video gamers. Findings suggest that the normalization of gambling in esports could be associated with increased gambling engagement. Future research should explore prevention strategies and long-term esports involvement effects on gambling. Word Count: 250.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Survey of gamers/esports athletes reports problem gambling rates; unclear whether esports or sports betting participation was measured by activity.

**Решение:** =

---

### 152 · R0989

**Betting on More Than the Game: Elevated Cannabis Use Disorder Risk Among U.S. Sports Gamblers**

2026 · Digital Scholarship - UNLV (University of Nevada Reno) · conference-paper

Problem gambling and cannabis use disorder (CUD) are two increasing mental health concerns in the United States (U.S.). These concerns often co-occur and this co-occurrence is associated with more severe outcomes. Emerging research shows that U.S. adults who wager on sports experience significantly elevated difficulties with problem gambling and binge-drinking, yet less is known about problematic cannabis use among these communities. The purpose of the current study was to examine CUD in the context of sports betting in the U.S. Participants (N = 4363) included both a census-matched sample of U.S. adults (n = 2806) and an oversample of sports gamblers (n = 1557). Symptoms of CUD were measured through a total cannabis involvement index score (i.e., risk marker for CUD). Results indicated that risk for CUD is significantly higher among sports gamblers (M = 7.25, SD = 11.06) relative to other types of gamblers (M = 2.39, SD = 5.51; MD = 4.87 [4.21, 5.52], SE = 0.28, p < .001) as well as non-gamblers (M = 1.37, SD = 3.81; MD = 5.89 [5.10, 6.68], SE = 0.34, p < .001). Additionally, a moderation analysis (adjusted for age) indicated that the relationship between problem gambling severity and risk for CUD was significantly higher in sports gamblers relative to other types of gamblers (R2 = .345, F(4, 4061) = 534.48, p < .001, b = -5.18 [-6.48, -3.87]).

**ИИ:** + · обе модели · беттеры + инструмент · US survey with an oversample of sports gamblers; problem gambling severity was measured and used as a moderator.

**Решение:** =

---

### 153 · R0992

**Reasons for Gambling Amongst Men in Matasia Location, Ngong Sub-County Kajiado County, Kenya.**

2026 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-025-10464-1

Gambling has become a significant social issue in Kenya, particularly among men in peri-urban areas, driven by economic hardships and the proliferation of digital betting platforms. This study aims to explore the reasons for gambling among men in Matasia Location, Ngong Sub-County, Kajiado County, a semi-arid region with notable socio-economic challenges. A descriptive mixed-methods approach was used, surveying 150 men aged 18-65 identified at gambling hotspots (betting shops, bars, and eateries), with 145 completing questionnaires (96.7% response rate). Data were collected in July 2025 and analysed using SPSS 25 for descriptive statistics and chi-square tests, complemented by thematic analysis of interviews. Key motivations, frequency, types, and spending habits of gambling were assessed to identify driving factors. The primary reason for gambling was the desire for wealth, as participants indicated 48.3% were motivated by this factor, followed by financial pressures, with survey data revealing 25.5% cited this reason. Daily gambling was reported, with individuals reporting 54.5% engaged in it regularly, and 57.2% spent KES 1,000-5,000 monthly. Sports betting and casino games were the most common types, with interviewees noted 58.6% preferred sports betting and 51.7% chose casino games. The Key Informant Interview (Member of County Assembly) for Matasia Location, highlighted idleness and unemployment as key drivers. Economic desperation and digital accessibility fuel gambling in Matasia, and interventions such as vocational training, financial literacy programs, and policy restrictions on online platforms are recommended, aligning with Kenya's National Substance Abuse Prevention Strategy (2021) and Sustainable Development Goal 3.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Survey of male gamblers in Kenya that measured sports betting; abstract reports only motives, frequency and spending, with no problem-gambling instrument mentioned.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Survey of men at gambling hotspots on motives, frequency and spending; no problem-gambling instrument mentioned, and the sample was recruited at gambling venues.)

**Решение:** ?

---

### 154 · R0996

**Prevalence and Associated Factors of Gambling Among High School Students in a Portuguese City.**

2026 · Journal of gambling studies · journal article, journalarticle, article · eng · https://doi.org/10.1007/s10899-026-10517-z

Adolescent gambling has become increasingly prevalent with the rise of online platforms and the normalization of gambling behaviors. This study aimed to estimate the past-year prevalence of gambling among high school students in Viana do Castelo, Portugal, to investigate sex-related differences in gambling behavior, and to identify factors associated with gambling. A cross-sectional study was conducted in 2024 with 1064 students from the three existing high schools. Participants completed an anonymous online questionnaire covering sociodemographic data, gambling in the past 12 months and its characterization, substance use, and environmental influences. The primary dependent variable was past-year gambling, coded dichotomously as yes/no. Chi-square tests and logistic regression were used to assess associations between past-year gambling and the other variables. The weighted past-year prevalence of gambling was 35.0%, higher among males. Statistically significant sex differences emerged in gambling type, companions, expenditure, frequency, and mode of access. Compared with females, males were more likely to engage in sports betting and poker, gamble alone or with friends, spend more money, gamble more frequently, and gamble online only or both online and land-based. Multivariable analysis showed that being male, attending public schools, early tobacco initiation, frequent consumption of spirit drinks, and knowing others who gamble were independently associated with gambling in the past 12 months. Gambling is widespread among adolescents in this sample, with distinct sex-related patterns and strong social influences. Early prevention strategies should address both individual behaviors and broader social contexts. Longitudinal studies are needed to understand causal pathways and inform targeted interventions.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Adolescent survey measuring sports betting participation; abstract does not mention any problem-gambling screening instrument.

**Решение:** =

---

### 155 · R0997

**The Surprising Effects of Bet Size on Enjoyment of Sports Wagering**

2026 · Digital Scholarship - UNLV (University of Nevada Reno) · conference-paper

Many people engage in sports gambling for the fun of it. In a series of studies, we find that people tend to overestimate the impact of bet size on the fun they have. They believe that betting on the winner of a sports event is more enjoyable than simply predicting the winner, and that higher-stakes bets make the experience more enjoyable than smaller bets. This belief leads them to prefer larger bets over smaller bets. In reality, the enjoyment derived from gambling is relatively stakes-independent: at least within a certain range, lower-stakes gamblers derive as much enjoyment from watching a sports event as their higher-stakes counterparts. Simply predicting the outcome improves the watching experience to a similar extent as placing relatively large bets.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Experiments with sports bettors on enjoyment and bet size; abstract doesn't say whether a problem-gambling screen like PGSI was used.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Behavioural experiments on bet size and enjoyment of sports wagering; no problem-gambling instrument mentioned in the abstract.)

**Решение:** -

---

### 156 · R0998

**Women-Led Crypto and Sports Betting Groups: New Gender Roles in Digital Hustle Culture**

2026 · AKSU Journal of Social Sciences · article, journalarticle, review · und · https://doi.org/10.61090/aksujoss.7.1.123-139

This study investigates the evolving roles of women within cryptocurrency trading and sports betting communities in Nigeria’s expanding digital hustle culture. The research examines how women led groups in these high-risk digital economies redefine gender roles, build alternative support networks, and negotiate financial autonomy. Guided by feminist theory, Bourdieu’s concept of capital, and digital labor perspectives, the study addresses three core questions: how women led crypto and betting groups operate, what new gender roles are emerging within digital hustle spaces, and what social and economic implications arise from these developments. A mixed methods design was employed, combining surveys, participant observation, and content analysis across major urban centers including Lagos, Abuja, Port Harcourt, and Delta State. Out of 1,532 questionnaires distributed, 1,486 were completed and returned, enabling a robust quantitative analysis supported by thematic insights. The findings indicate that digital literacy, mentorship access, and leadership participation significantly enhance women’s empowerment within digital financial ecosystems. Women led groups function as collective learning hubs, risk sharing communities, and alternative economic networks that challenge traditional gendered exclusions. The study concludes that women are reconfiguring the digital financial landscape by mobilizing cultural, social, and economic capital to assert agency and negotiate new identities within speculative markets. These findings have implications for digital finance policy, gender equity interventions, and future research on intersectional participation in emerging digital economies.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Survey of 1,486 women in Nigerian crypto and sports betting groups; the abstract focuses on empowerment and does not say whether problem gambling was measured.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Mixed-methods survey of women in Nigerian crypto and betting groups about empowerment and gender roles; no problem-gambling instrument is mentioned.)

**Решение:** ?

---

### 157 · R1004

**The Impact of Sports Betting on University Undergraduates: A Case Study**

2026 · Indonesian Journal of Social Research (IJSR) · journalarticle, review, article · https://doi.org/10.30997/ijsr.v8i2.870

This article investigated the impact of sports betting on university undergraduates with University of Nigeria, Nsukka (UNN) as the case study. The primary aim is to examine the involvement of students in sports betting, the frequency, motivations behind it, and its impact on both their academic and social activities. Guided by a set of research objectives, the study employed a cross-sectional survey design, with a sample of 200 respondents drawn from the study population. The study employed a quantitative approach and data were collected through a semi-structured questionnaire. Statistical tools and techniques, such as SPSS, descriptive statistics, and chi-square were adopted to analyze the generated quantitative data. The findings showed that the level of participation in sports betting is high, with varying frequency of participation, reflective of a pattern of habitual engagement. Peer influence was identified as the most common entry point, while social media and advertisements also accounted for involvement in sports betting. Financial motivation was also a key factor for most of the respondents as they see betting as a means of surviving financially during school. Given these insights, the study recommends that universities intensify awareness campaigns on the academic risks associated with betting, as well as introduce counseling and peer mentorship programs, to mitigate the habit and adverse effect of sports betting on university students. Policy interventions such as banning betting apps on campus can also curb the growing normalization of gambling behavior among undergraduates and preserve academic integrity.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of undergraduate sports bettors that measured frequency, motivations and impacts; the abstract doesn't say whether a problem-gambling instrument was used.

**Решение:** =

---

### 158 · R1008

**Determinants of sports betting addiction among Turkish university students: The mediating role of family resilience in the relationship between religious coping and sports betting addiction**

2026 · Addicta The Turkish Journal on Addictions · article, journalarticle, journal-article · und · https://doi.org/10.15805/addicta.2026.509

This study investigated the relationships between sociodemographic factors, family resilience, and religious coping among Turkish university students, a population vulnerable to sports betting addiction. The research, conducted with 587 students (ages 17–27), found that 30.5% of the participants had engaged in sports betting. Analyses showed that sports betting addiction differed significantly by gender, with men scoring higher than women. Other significant factors included having betting acquaintances, the importance of religion, betting frequency, and motivations. Both family resilience (r=−.136, p&lt;.001) and positive religious coping (r=−0.154, p&lt;.001) were negatively associated with addiction. Mediation analysis was a key finding, revealing that positive religious coping indirectly reduces addiction by increasing family resilience. Furthermore, multiple regression analysis identified betting frequency and motivations like making money and seeking excitement as the strongest predictors. These findings emphasize the importance of strong family bonds and positive religious beliefs as crucial protective factors against addiction. The results have important implications for prevention strategies that focus on strengthening family resilience and promoting religious coping methods among young people.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Student survey of sports bettors measuring 'sports betting addiction'; unclear whether a recognised problem-gambling instrument was used or a case definition applied.

**Решение:** =

---

### 159 · R1009

**Gambling and its associated factors among students of the University of Ilorin, Nigeria.**

2026 · The South African journal of psychiatry : SAJP : the journal of the Society of Psychiatrists of South Africa · article, journal article, journalarticle · eng · https://doi.org/10.4102/sajpsychiatry.v32i0.2481

Background: Studies have revealed a global surge in gambling and gambling disorders, particularly among young adults, including university students. This disturbing trend poses significant risks not only to individual’s mental well-being but also to the wider community. Aim: The objectives of the study were to determine the prevalence of gambling, gambling disorder and the associated socio-demographic factors among undergraduate students of University of Ilorin. Setting: The study was conducted at the University of Ilorin, a federal government owned tertiary educational institution located in Kwara State, North-Central Nigeria. Methods: A pro forma questionnaire was used to obtain socio-demographic information about the students. Respondents who had gambled in their lifetime proceeded to complete the self-administered South Oaks Gambling Screen (SOGS). Score of at least 1 out of 20 on the SOGS indicated gambling disorder, having met the criteria for either problem gambling (score 1-4) or pathological gambling (score ≥ 5). Results: Responses of 2044 of the respondents were analysed. Their mean age was 21.74 ± 2.64 years, and male respondents accounted for 54.5%. A total of 409 (20%) of respondents had ever gambled in their lifetime, with sports betting been the most gambled activity. About 14.9% of the respondents had gambling disorders (10.5% problem gambling; 4.4% pathological gambling). Male gender, positive family history of mental illness, a lack of adequate financial support and staying off-campus were significantly associated with presence of gambling disorders. Logistic regression revealed that only positive family history of mental illness was predictive of gambling disorder (OR = 6.987, 95% CI [2.119–23.038], p = 0.001). Conclusion: This study revealed that three-quarters of respondents with a lifetime history of gambling developed gambling disorder. Contribution: This implies that a significant proportion of individuals who initially engage in social gambling may have a propensity to develop gambling disorder overtime.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Nigerian university student survey using SOGS; measured sports betting participation (the most common activity) and gambling disorder.

**Решение:** =

---

### 160 · R1010

**FINANCIAL LITERACY, VOCATIONAL EDUCATION AND YOUTH GAMBLING BEHAVIOUR AMONG UNDERGRADUATE STUDENTS**

2026 · AKOKA JOURNAL OF VOCATIONAL EDUCATION · article · en

The rising prevalence of gambling among Nigerian youths has become a major socio-economic concern, with adverse consequences for financial wellbeing, productivity, and sustainable development. This study examined the roles of vocational skills development and financial literacy education in mitigating gambling tendencies among students of the Federal College of Education (Technical), Akoka, Lagos State, Nigeria. Specifically, the study investigated the prevalence and patterns of gambling behaviour, assessed the influenceof financial literacy on gambling tendencies, determined the effect of vocational skills development on gambling behaviour, and examined the implications of gambling on students' financial freedom. A descriptive survey research design was adopted. A sample of 120 students was selected through simple random sampling, while data were collected using a structured questionnaire. Descriptive statistics were used to answer the research questions, whereas Pearson Product Moment Correlation and multiple regression analysis tested the hypotheses at the 0.05 level of significance. The findings revealed a high prevalence of gambling, with football betting, online betting, and Premier Lotto being the most common forms. Financial literacy showed a significant negative relationship with gambling behaviour (r = -0.621, p < 0.05), while vocational skills development significantly reduced gambling tendencies. The joint prediction model showed that both interventions explained a significant proportion of variance in youth gambling tendencies (R2 = 0.548, p < 0.05). Gambling behaviour was also found to undermine students' financial freedom through poor savings, financial stress, and increased financial vulnerability (r = -0.684, p < 0.05). The study concludes that strengthening financial literacy and vocational skills acquisition can effectively reduce gambling tendencies and promote financial independence among Nigerian youths. It recommends integrating financial literacy and vocational skills development into youth empowerment programmes and tertiary education curricula.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Student survey measured football/online betting; a structured questionnaire was used, but it is unclear whether it included a validated problem-gambling instrument.

**Решение:** =

---

### 161 · R1013

**Investigating the Relationship between Financial Motivation and Risk-Taking Behaviour in Sports Betting among Different Demographics in Nigeria**

2026 · WORLD JOURNAL OF FINANCE AND INVESTMENT RESEARCH · article, journal-article · https://doi.org/10.56201/wjfir.v9.no7.2025.pg67.87

In investigating the relationship between financial motivation and risk-taking behavior in sports betting behavior. This study aims to investigate the relationship between financial motivation and risk-taking behavior in sports betting among different demographics and identify the factors influencing risk-taking behavior in sports betting. The use of questionnaires to collect data and analysis of responses using SPSS computer package was actualized using regression model. There was only one dependent model which was the risk-taking behavior in sports betting. Financial motivation, demographics (age, income, education level) constituted the independent variables. The control variables included betting experience and frequency of betting. Overall, these results suggest that there are significantly strong arguments that suggest a very strong nexus between financial motivation and risk-taking behavior. The results prove demographics play a significant role in explaining the variation in financial motivation and risk-taking behavior. Apparently, the results show age, income and betting experience as significant predicators of risk-taking behavior. The three hypotheses in the study were all accepted. In conclusion, the results show a significant relationship between financial motivation and risk-taking behavior. The model fitting information suggests that demographics collectively contribute to the model, indicating that financial motivation and risk-taking behavior differ across various demographics. The model fitting information suggests that age, income, and betting experience are significant predictors of risktaking behavior. The recommendations included targeting responsible gambling initiatives that consider demographic differences, age, income, and betting experience. Offer financial education resources to help bettors manage their finances effectively and make informed decisions. Provide risk management tools, such as betting limits and reality checks, to help bettors control their risktaking behavior. Consider demographic differences when designing regulations and guidelines for sports betting. Enforce age restrictions and ensure that betting operators have adequate measures in place to prevent underage betting. Promote financial inclusion and education to help individuals manage their finances effectively and make informed decisions. Conduct longitudinal studies to examine the long-term effects of financial motivation and risk-taking behavior in sports betting. Conduct qualitative research to gain a deeper understanding of the factors influencing financial motivation and risk-taking behavior. Conduct cross-cultural comparisons to examine the generalizability of the findings to other contexts.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Questionnaire survey of Nigerian sports bettors on risk-taking; the abstract doesn't say whether a problem-gambling instrument was used.

**Решение:** =

---

### 162 · R1014

**Sport Betting and Mental Health Among Undergraduates of Rev. Fr. Moses Orshio Adasu University Makurdi Nigeria: The Mediating Role of Frustration**

2026 · INTERNATIONAL JOURNAL OF SOCIAL SCIENCES AND MANAGEMENT RESEARCH · journalarticle, review, article · https://doi.org/10.56201/ijssmr.vol.12no1.2026.pg391.408

Mental health is important for maximal functioning especially for students as it necessary for high academic performance. To this end, this study investigated the mediating role of frustration in sport betting and mental health among undergraduates of Rev. Fr. Moses Orshio Adasu University Makurdi Nigeria. Cross-sectional survey design was used and a sample of 394 students were sampled using multi-stage sampling technique, which was determined using Taro Yamane formula for sample size determination. Among the sampled students, 296 (74.9%) were male while 99 (25.1%) were female, and their age ranged from 18 – 33 years (with average age of 24.47; SD = 4.11). Sports Betting Scale, General Health Questionnaire (GHQ-12) and Frustration Scale were used for data collection. Four hypotheses were formulated and tested and result from the first hypothesis showed that there was a significant influence of sports betting on mental health among undergraduates of Rev. Fr. Moses Orshio Adasu University, Makurdi. From the second hypothesis, it was found that there was a significant influence of frustration on mental health among undergraduates of Rev. Fr. Moses Orshio Adasu University, Makurdi. Finding from hypothesis three showed that frustration significantly mediated the relationship between sports betting and mental health among undergraduates of Rev. Fr. Moses Orshio Adasu University, Makurdi. From the fourth hypothesis, it was found that all the independent variables (sports betting and frustration) significantly and jointly influenced mental health among undergraduates of Rev. Fr. Moses Orshio Adasu University, Makurdi. The findings were discussed in relation to other findings and conclusions were drawn. It was recommended among others that there should be campus wide awareness programs on the psychological risks associated with sports betting, emphasizing its impact on mental health and promoting healthier recreational activities.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Student survey used an unspecified 'Sports Betting Scale'; unclear whether it is a recognised problem-gambling screen.

**Решение:** =

---

### 163 · R1023

**Gambling behaviors associated with problem gambling among patients in treatment for substance use disorder**

2026 · American Journal on Addictions · article · en · https://doi.org/10.1111/ajad.70203

BACKGROUND AND OBJECTIVES: Problem gambling impacts substance use disorder (SUD) treatment outcomes. To support early intervention, this study investigated gambling behaviors associated with problem gambling among SUD patients. METHODS: Patients (N = 593) from 19 residential SUD treatment facilities in California were surveyed about gambling behaviors and services. Patients identified as "problem gamblers" screened positive for gambling disorder or reported gambling behaviors at high risk for progression to gambling disorder. Multivariate regression analyses compared problem gamblers to nonproblem gamblers on specific gambling behaviors and receipt of gambling services. RESULTS: Of the total sample, 223 (37.6%) gambled in the past year. Among past-year gamblers, those meeting problem gambling criteria (n = 106) were more likely than nonproblem gamblers to endorse betting on "games of skill" including cards (adjusted odds ratio [AOR] = 2.35, 95% confidence interval [CI] = 1.46, 3.78) and participating in online/electronic gambling (AOR = 5.61, 95% CI = 2.27, 13.88) and casino games (AOR = 2.30, 95% CI = 1.42, 3.72). Patients with problem gambling reported more gambling activity types than nonproblem gamblers (mean difference = 1.82, 95% CI = 1.59, 2.05). Only 35% of patients with problem gambling received gambling services from the SUD treatment program. DISCUSSION AND CONCLUSIONS: Specific gambling behaviors increase risk of problem gambling for SUD patients. SUD treatment programs should screen for and address problem gambling. SCIENTIFIC SIGNIFICANCE: SUD patients may have lower risk thresholds for gambling disorder. This study provides new data on specific behaviors associated with problem gambling among SUD patients.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · SUD patients screened for gambling disorder and compared by gambling activity; sports betting likely among activities but not mentioned in abstract.

**Решение:** =

---

### 164 · R1024

**Gambling, Discrimination, and Stressful Life Events among Substance Use Disorder Treatment Patients**

2026 · Journal of Gambling Studies · article · en · https://doi.org/10.1007/s10899-026-10567-3

People with addictive disorders are vulnerable to stigma and discrimination, which can impact addiction treatment outcomes through increased psychological distress and reduced self-efficacy. We investigated relationships between problem gambling, psychological distress, self-efficacy, and stressful life experiences related to identity among patients in SUD treatment. Patients (N = 590) from 19 residential treatment facilities across California completed a survey on substance use, problem gambling, psychological distress (Kessler Psychological Distress Scale - K6), self-efficacy, and intersectional discrimination [Intersectional Discrimination Index - Major (InDI-M)]. Multivariable regression analyses compared three groups on these measures: problem gambling (PG, n = 70), non-problem gambling (NPG, n = 154), and no gambling (NG, n = 366). About 38% of the sample reported past-year gambling. Compared to NG, PG had higher lifetime (mean difference [MD] = 2.61, 95% CI = 0.80, 4.42) and past-year (MD = 1.82, 95% CI = 1.37, 2.27) InDI-M scores; and higher K6 scores (MD = 2.09, 95% CI = 1.14, 3.04). PG also had increased risk of lifetime eviction (adjusted odds ratio [AOR] = 2.49, 95% CI = 1.66, 3.75) and property damage/theft (AOR = 2.99, 95% CI = 1.43, 6.26); and past-year relationship loss (AOR = 4.95, 95% CI = 1.77, 13.83) and physical attack (AOR = 2.57, 95% CI = 1.40, 4.72) compared to NG. In this sample, PG reported more psychological distress and identity-based stressful experiences. Clinical interventions for SUD patients with comorbid PG should prioritize trauma-informed approaches, self-stigma reduction, and case navigation for social determinants of health such as housing insecurity.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · SUD treatment patients (not selected for gambling) surveyed on problem gambling; unclear whether sports betting participation was recorded.

**Решение:** =

---

### 165 · R1025

**Trends and Gender Differences in Gambling with Money between 2018 and 2021: A Population-Based Study among 60,331 Spanish Adolescents**

2026 · Journal of Gambling Studies · article · en · https://doi.org/10.1007/s10899-026-10545-9

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; large Spanish adolescent survey (likely ESTUDES) may include sports betting and a problem-gambling screen such as Lie/Bet.

**Решение:** =

---

### 166 · R1037

**Internet Gaming Disorder, Problem Gambling Symptoms and Mental Health in Spanish Adolescents: A Cross-Sectional Study on the Role of Microtransactions and Loot Boxes**

2026 · Healthcare · article · en · https://doi.org/10.3390/healthcare14131846

Background/Objectives: Adolescent mental health problems have increased in recent years, with growing concern about the impact of digital behaviors such as problematic video game use and gambling. Internet Gaming Disorder (IGD) and Problem Gambling Symptoms may share psychological risk markers, but evidence in Spanish adolescents is limited. This study aimed to examine the relationship between IGD, problem gambling symptoms, and mental health, and to identify sociodemographic, psychological, and behavioral factors associated, including microtransactions and loot boxes. Methods: A cross-sectional study was conducted with secondary education students from Extremadura (Spain). The final sample included 343 participants. Measures included an ad hoc questionnaire on video game use, the IGDS9-SF, SOGS-RA, and the Strengths and Difficulties Questionnaire (SDQ). Descriptive analyses, Spearman correlations, and multivariable regression (Poisson and negative binomial) were performed. Results: IGD and gambling were positively correlated (Spearman’s ρ = 0.386, p < 0.001) and associated with higher mental health difficulty scores (IGD: ρ = 0.299, p < 0.001; gambling: ρ = 0.214, p < 0.001). Male gender was associated with both outcomes (IGD: incidence rate ratio [IRR] = 1.21 [95% Confidence Interval: 1.13–1.30]; gambling: IRR = 2.90 [1.85–4.60]). Microtransactions were associated with both behaviors (IGD: IRR = 1.17 [1.09–1.25]; gambling: IRR = 1.74 [1.19–2.54]), while loot box use was related only to IGD (IRR = 1.13 [1.05–1.21]). Total SDQ score was positively associated with both IGD (IRR = 1.02 [1.02–1.03]) and gambling (IRR = 1.10 [1.06–1.13]). Younger age was associated with higher IGD scores (IRR = 0.97 [0.96–0.99]). Conclusions: There are similarities in the associations among the examined factors and increased scores of IGD and gambling in adolescents, particularly male gender, higher mental health difficulties scores, and involvement in monetized gaming systems. School-based, family, and public health prevention strategies may benefit from addressing the importance of psychological well-being and increase awareness of the potential risks associated with digital gaming practices.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Adolescent survey using SOGS-RA; unclear whether sports betting participation was measured, though SOGS-RA activity items may include it.

**Решение:** =

---

### 167 · R1044

**Supplementary Material "The Illusion of Control in Sports Betting: Belief, Skill, and Losses in a Latin American Market""**

2026 · OSF · other literature type, text/project, preprint · und · https://doi.org/10.17605/osf.io/7e3ga

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Supplement to a study of illusion of control among sports bettors with no abstract; it may or may not have used a problem-gambling instrument.

**Решение:** =

---

### 168 · R1047

**Η ψυχοκοινωνική διάσταση του διαδικτυακού τζόγου στους νέους: Ο ρόλος της οικογένειας, των συναισθηματικών δυσκολίων και της ψυχικής ανθεκτικότητας**

2026 · master thesis · gre/ell · https://pergamos.lib.uoa.gr/uoa/dl/object/5401211

Εισαγωγή: Ο διαδικτυακός τζόγος στους νέους αποτελεί μια από τις πιο συχνά εμφανιζόμενες μορφές εξάρτησης, η οποία χαρακτηρίζεται από την επίμονη ενασχόληση με τα τυχερά παιχνίδια μέσω διαδικτύου, πάρα τις δυσμενείς συνέπειες. Σκοπός: Σκοπός τις έρευνας ήταν η διερεύνηση ψυχολογικών και κοινωνικών παραγόντων που σχετίζονται με την εμφάνιση διαταραχής τζόγου. Συγκριμένα, να εξεταστεί αν οι συναισθηματικές δυσκολίες (κατάθλιψη, άγχος και στρες), η οικογενειακή δυσλειτουργία και το φύλο συσχετίζονται με την διαταραχή διαδικτυακού τζόγου. Διερευνήθηκε, επίσης, κατά πόσο η ψυχική ανθεκτικότητα μπορεί να λειτουργήσει ως προστατευτικός παράγοντας σχετικά με τη διαταραχή αυτή. Μεθοδολογία: Η μελέτη διεξήχθη στο διάστημα Οκτώβριος 2025 – Μάρτιος 2026. Οι συμμετέχοντες ήταν 239 άτομα εκ των οποίων οι 127 (53,1%) ήταν άνδρες και 112 (46,9%) ήταν γυναίκες. Οι συμμετέχοντες ήταν ηλικίας 18-30 ετών, με μέση ηλικία τα 24,65 έτη. Για τη συλλογή δεδομένων χρησιμοποιήθηκαν τα ερωτηματολόγια: Ερωτηματολόγιο δημογραφικών στοιχείων, Ερωτηματολόγιο Διαταραχής από τη Συμμετοχή στα Τυχερά Παίγνια (Vasios &amp; Roussos, 2017) που ανιχνεύει το βαθμό κινδύνου για παθολογικό τζόγο, η Κλίμακα Ανθεκτικότητας – Connor-Davidson Resilience Scale (CD-RISC-25) που μετράει τις υποκλίμακες που σχετίζονται με τη ψυχική ανθεκτικότητα, η Κλίμακα Εκτίμησης της Οικογένειας (Family Assessment Device - General Functioning Scale), η οποία μετράει την λειτουργικότητα της οικογένειας και η κλίμακα Κατάθλιψη – Άγχους – Στρες (DASS-21) που μετράει τους παράγοντες άγχος, κατάθλιψη και στρες. Η έρευνα κοινοποιήθηκε μέσω ερωτηματολογίων με τη χρήση του Google Forms. Αποτελέσματα: Τα αποτελέσματα έδειξαν ότι η κατάθλιψη, το άγχος και το στρες σχετίζονται θετικά με την διαταραχή τζόγου (p &lt; .001). Από τη γραμμική παλινδρόμηση, το στρες εμφανίστηκε ως ισχυρός προβλεπτικός παράγοντας (p &lt; .001), ενώ το άγχος, αν και εμφανίστηκε επίσης στατιστικά σημαντικός παράγοντας (p = .007), παρουσίασε αρνητική συσχέτιση, κάτι που υποδηλώνει ότι υψηλά επίπεδα άγχους σχετίζονται με χαμηλότερο επίπεδο διαταραχής διαδικτυακού τζόγου. Η κατάθλιψη δεν αποδείχτηκε στατιστικά σημαντική (p = .172). Επίσης, η οικογενειακή δυσλειτουργία συσχετίστηκε θετικά με την εμπλοκή με τον τζόγο (p &lt; .001) και η ψυχική ανθεκτικότητα εμφάνισε αρνητική συσχέτιση τονίζοντας τον προστατευτικό της ρόλο (p &lt; .001). Όσο αφορά τις επιμέρους πτυχές της ψυχικής ανθεκτικότητας, ο έλεγχος και η προσωπική απόδοση παρουσίασαν στατιστικά σημαντική αρνητική σχέση (p = .001, p = .049), σε αντίθεση με την ανεκτικότητα που βρέθηκε να συσχετίζεται θετικά με τον διαδικτυακό τζόγο (p = .007). Η πτυχή αλλαγή και σχέσεις, καθώς και η πτυχή πνευματικές επιδράσεις δεν αποτελούν στατιστικά σημαντικούς αποτρεπτικούς/προγνωστικούς παράγοντες (p = .274, p = .678). Τέλος, όπως φάνηκε, οι άνδρες παρουσίασαν υψηλότερα επίπεδα διαταραχής τζόγου σε σύγκριση με τις γυναίκες (p &lt; .001). Συγκεκριμένα, το ποσοστό προβληματικής ενασχόλησης στους άνδρες ανήλθε σε 40.2% σε σύγκριση με 8.0% στις γυναίκες. Συμπεράσματα: Συμπερασματικά, τα ευρήματα της μελέτης υπογραμμίζουν τη σημασία των ψυχολογικών και κοινωνικών παραγόντων στην κατανόηση του διαδικτυακού τζόγου στους νέους. Η ενίσχυση της ψυχικής ανθεκτικότητας και η διαχείριση του στρες, όπως επίσης και η οικογενειακή λειτουργικότητα αναδεικνύονται ως βασικοί στόχοι για την πρόληψη και την αντιμετώπιση της προβληματικής συμπεριφοράς. Introduction: Online gambling is one of the most common addictions among young people, involving persistent engagement in online betting activities despite negative consequences. Purpose: The study was aimed at investigating psychological and social factors associated with the development of gambling disorder. Specifically, it examined whether emotional difficulties (depression, anxiety, and stress), family dysfunction, as well as gender, are associated with online gambling disorder. Additionally, the study examined whether psychological resilience can be a protective factor against this disorder. Methodology: The study was conducted between October 2025 and March 2026. The sample consisted of 239 participants of whom 127 (53.1%) were men and 112 (46.9%) were women. Participants were aged between 18 and 30 years with a mean age of 24.65 years. Data were collected using the following questionnaires: a demographic questionnaire, the Gambling Disorder Questionnaire (Vasios &amp; Roussos, 2017), which assesses the level of risk for pathological gambling, the Connor–Davidson Resilience Scale (CD-RISC-25), which measures the dimensions of psychological resilience, the Family Assessment Device – General Functioning Scale, which evaluates family functionality, and the DASS-21 (Depression, Anxiety, Stress Scale), which measures levels of depression, anxiety, and stress. The survey was distributed online via Google Forms. Results: The findings indicated that depression, anxiety, and stress were positively associated with gambling disorder (p &lt; .001)

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Greek thesis on young adults' online gambling using a gambling disorder questionnaire; unclear whether sports betting participation was measured.

**Решение:** =

---

### 169 · R1060

**Responsible Sports Betting in Canada: Applied Evidence for Positive Play and Harm Prevention**

2026 · Digital Scholarship - UNLV (University of Nevada Reno) · conference-paper

The 2021 legalization of single‑event wagering and the introduction of regulated iGaming have reshaped gambling in Canada, with mobile access, in‑play betting, and microbetting increasing engagement while introducing new risks. To examine these changes, a national online survey of ~5,000 Canadian adults who gambled in the past year was conducted as part of a five‑year longitudinal study; this presentation reports first‑year results. Sports bettors were compared with other online gamblers, with sub‑analyses by betting format. Measures included gambling harm (PGSI), anxiety (GAD‑7), cognitive distortions (GABS‑15), motives (GMQ‑SF), and protective behaviors (Positive Play Scale [PPS]). Sports bettors showed significantly higher harm, anxiety, and cognitive distortions, and lower PPS scores, than non‑sports gamblers. Risk increased with wager speed: exclusive in‑play bettors and frequent microbettors showed the highest harm profiles. Young adult males (19–29) were particularly vulnerable. In contrast, high PPS scores were associated with markedly lower harm and coping‑motivated gambling, highlighting positive play as a key protective factor.

**ИИ:** + · обе модели · беттеры + инструмент · National survey of Canadian past-year gamblers comparing sports bettors with other gamblers using the PGSI.

**Решение:** =

---

### 170 · R1063

**Les paris sportifs**

2026 · Open Repository and Bibliography (University of Liège) · book-chapter · fr

editorial reviewed

**ИИ:** ? · обе модели · нет аннотации · Book chapter on sports betting with no real abstract; probably a narrative overview, but empirical content can't be ruled out.

**Решение:** =

---

### 171 · R1064

**Individual and Neighborhood Risk and Protective Factors of At-Risk and Problem Gambling: a Spatial Analysis Using Geographic Information Systems**

2026 · Journal of Gambling Studies · article · en · https://doi.org/10.1007/s10899-026-10475-6

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; likely a population survey with at-risk/problem gambling measured, but unclear whether sports betting participation was recorded.

**Решение:** =

---

### 172 · R1065

**Sports Betting Among Active Athletes: A Sociological Study of Risk Behavior in a Gendered Environment**

2026 · Digital Repository (National Repository of Grey Literature) · dissertation · cs

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Thesis on sports betting among athletes with no abstract; it may be a survey that measured problem gambling, so the full text is needed.

**Решение:** =

---

### 173 · R1074

**Sport participation and gambling-related problems in adolescents: findings from a large school-based study**

2026 · Frontiers in Public Health · journalarticle, article · en · https://doi.org/10.3389/fpubh.2026.1931143

Background Adolescent gambling is increasingly shaped by digital access, sports betting, and gambling-like mechanisms embedded in everyday youth culture. This study examined gambling-related problems among high school students and their associations with sociodemographic, family, mental health-related, and behavioral characteristics, with particular attention to sport participation. Methods A school-based cross-sectional study was conducted among 2,379 high school students in Novi Sad, Serbia, between 2024 and 2026. Participants completed a structured sociodemographic and behavioral questionnaire and the Serbian version of the Gambling Disorder Identification Test. Students were classified as non-gambling, recreational gambling, or having gambling-related problems. Associations between gambling categories and selected characteristics were examined using omnibus chi-square tests, Cramér's V, and post-hoc pairwise comparisons. Results Overall, 1,969 students (82.8%) were classified as non-gambling, 314 (13.2%) as recreational gambling, and 96 (4.0%) as having gambling-related problems. Gambling category was significantly associated with male sex, lower school achievement, living arrangement, parental marital status, sport participation, previous psychiatric treatment, family psychiatric history, smoking, alcohol use, and psychoactive substance use. In the univariate analyses, sport participation increased from 64.0% among non-gambling students to 75.2% among recreational gamblers and 78.1% among students with gambling-related problems. Post-hoc comparisons showed that sport participation differentiated non-gambling students from both gambling-involved groups, but not recreational gambling from gambling-related problems. However, after adjustment for sex and other relevant behavioral and mental health-related characteristics, sport participation was no longer independently associated with gambling-related problems. Male sex, previous psychiatric treatment, smoking, alcohol use, and psychoactive substance use remained the strongest independent correlates. Conclusion Gambling-related problems in adolescents were associated with a broader pattern of behavioral and mental health-related factors. Although sport participation was associated with gambling involvement in unadjusted analyses, this association did not remain significant after adjustment for sex and other relevant characteristics. These findings support understanding adolescent gambling within a broader risk-behavior and public health framework, with sport representing a relevant context for prevention rather than an independent risk factor.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · School survey of adolescents using the GDIT problem-gambling screen; the abstract does not say whether sports betting participation was measured.

**Решение:** =

---

### 174 · R1082

**Translation and Adaptation of the Online Gambling Disorder Questionnaire (OGD-Q) into Brazilian Portuguese**

2026 · Journal of Gambling Studies · article · en · https://doi.org/10.1007/s10899-026-10480-9

Online gambling has grown increasingly popular over the past decade, especially since the COVID-19 pandemic. Online gamblers tend to face more issues than those who gamble in traditional settings, leading to a higher risk of developing pathological gambling. In Brazil, gambling activities are culturally accepted and normalized, which encourages widespread participation among the population. Therefore, screening and assessing online gambling is now a public necessity. The Online Gambling Disorder Questionnaire (OGD-Q), developed by González-Cabrera et al. (2020), aims to evaluate symptoms of gambling disorder primarily online. Given the significance of this issue in Brazil, this study sought to adapt the scale for cross-cultural use and examine its psychometric properties. The sample included 298 participants who completed an online survey. Nomothetic validity was tested through Spearman’s Rho correlations between measures of depression, anxiety, stress, and online gaming behavior. Internal consistency was assessed using Cronbach’s alpha and Omega Coefficient, along with confirmatory factor analysis. Results showed strong reliability, with a Cronbach’s alpha of 0.92 and an Omega Coefficient of 0.93. The confirmatory factor analysis supported the proposed one-factor structure, demonstrating good fit indices and factor loadings. Significant correlations were found in the total sample between OGD-Q scores and measures of online gaming, depression, anxiety, and stress. In summary, the findings demonstrate that the Brazilian version of OGD-Q is an effective tool for assessing online gambling disorder in the Brazilian population.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Validation of a DSM-5-based online gambling disorder questionnaire among Brazilian online gamblers; sports betting ("bets") is likely included but isn't reported.

**Решение:** =

---

### 175 · R1085

**High Stakes, Low Mood: Gambling Behavior and Mental Health Across Age Groups in Indiana**

2026 · Digital Scholarship - UNLV (University of Nevada Reno) · conference-paper

Gambling behavior is recognized as part of broader mental health outcomes across the lifespan. Prior research indicates that gambling problems are associated with psychological distress, including depression, anxiety, and suicidal ideation. Despite growing evidence of these links, few studies have examined gambling behavior and mental health patterns across multiple age groups within a single state population. This study examines gambling participation, problem-gambling severity, and self-reported mental health indicators among youth, college students, and adults in Indiana. Data were drawn from three statewide surveys conducted between 2023 and 2025. Measures included gambling frequency and type, validated problem-gambling indices, awareness and help-seeking behaviors, and self-reported mental health indicators such as stress, depression, and mentally unhealthy days. Across all age groups, gambling participation was common but varied by form. Youth and college students reported higher engagement in online and sports gambling, whereas adults more frequently reported lottery and casino play. Greater gambling severity was associated with elevated psychological distress and substance use across age groups, yet awareness of and engagement with treatment services remained low. These findings underscore the need for prevention and intervention strategies that address gambling and mental health through early intervention, education, and improved awareness of available support.

**ИИ:** + · обе модели · опрос населения об азартных играх · Statewide Indiana surveys measured gambling type, including sports gambling, and used validated problem-gambling indices.

**Решение:** =

---

### 176 · R1088

**The State of Gambling Behaviors Among NCAA Student-Athletes: Findings from Five Waves of the National Study on Collegiate Wagering (2004-2024).**

2026 · Journal of gambling studies · journal article, journalarticle, review · eng · https://doi.org/10.1007/s10899-026-10515-1

Technological advances and regulatory changes have substantially expanded access to sports wagering in the United States, raising concerns about gambling behaviors among collegiate athletes. Since 2004, the National Collegiate Athletic Association (NCAA) has conducted a large-scale survey every four years to monitor gambling behaviors among student-athletes. The present study examined trends in gambling among NCAA student-athletes over a twenty-year period. Data were drawn from five waves of the NCAA National Study on Collegiate Wagering conducted in 2004, 2008, 2012, 2016, and 2024. Across these cohorts, more than 100,000 student-athletes completed anonymous surveys assessing gambling participation, sports wagering behaviors, attitudes toward gambling, and problem gambling severity. Gambling activities were measured using the Gambling Activities Questionnaire, and gambling severity was assessed using DSM-IV-TR criteria for pathological gambling. Descriptive analyses were used to examine trends across survey years. Overall gambling participation declined over time, with increasing proportions of non-gamblers and decreasing rates of social gambling among both men and women. Rates of at-risk and probable pathological gambling remained low and relatively stable. Male student-athletes consistently reported higher gambling participation and sports wagering than females. Notable shifts included increases in fantasy sports betting, parlay bets, live in-game betting, and prop bets, often conducted through mobile platforms. Although overall gambling participation has declined, evolving forms of sports wagering and greater accessibility through online platforms present new challenges. Continued prevention, education, and responsible gambling policies are needed to protect student-athletes and preserve the integrity of college sports.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · NCAA student-athlete surveys measured sports wagering and DSM-IV-TR problem gambling; could report PG among sports bettors.

**Решение:** =

---

### 177 · R1090

**Prevalence of gambling behavior and risk for gambling disorder in Austria**

2026 · Neuropsychiatrie · article · en · https://doi.org/10.1007/s40211-026-00586-2

BACKGROUND: After gambling disorder (GD) was included as the first behavioral addiction in the Diagnostic and Statistical Manual of Mental Disorders, fifth edition (DSM-5), many studies focused on epidemiology and the impact of different risk factors. In this context, online gambling seems to show especially high addictive potential and, additionally, lacks government control and restrictions. METHODS: In this study, we aimed to evaluate the prevalence of GD, as well as various aspects of gambling behavior in a representative Austrian sample (N = 3658). An adapted version of a standardized questionnaire was applied, which covered all nine DSM-5 criteria for GD. RESULTS: Results indicate a lifetime prevalence for gambling of 34.9%, with 4.5% of the whole population at high risk for GD. Males engaged in online gambling three times more often than female participants, and prevalence for online gambling was highest in the youngest cohort (16-29 years). CONCLUSION: Our findings suggest a general increase in gambling behavior, with clear indications for a higher vulnerability of younger participants as well as for males compared to females. Results are discussed in light of clinical relevance, and the need for further restrictions, especially for online gambling, is argued.

**ИИ:** + · обе модели · опрос населения об азартных играх · Representative Austrian prevalence survey using a DSM-5 based GD screen and gambling activities; sports betting likely shown in activity tables.

**Решение:** =

---

### 178 · R1093

**Betting on Boys: Understanding Gambling Among Adolescent Boys**

2026 · Common Sense Media · casereport, report · https://doi.org/10.65077/zsnc9706

Anyone raising a son is all too familiar with the rhythms of digital life. Between the nonstop notifications, ceaseless social media scrolling, and late-night gaming sessions, boys are figuring out who they are online. Parents love to see their sons connect, but they're uneasy, too. And the data backs up their concern. Our newest research reveals that gambling has become common among adolescent boys, with more than a third of boys gambling before they turn 18. In "Betting on Boys: Understanding Gambling Among Adolescent Boys," our second report about boys' online lives, we discovered that for boys today, gambling largely doesn't happen at casinos or card tables. It lives in sports betting and inside boys' favorite video games—in loot boxes, skin cases, and other reward systems that blur the line between playing and paying—and it's showing up in their social media feeds through algorithmic recommendations. Nearly half of boys who gamble see online material that promotes gambling, mostly through algorithmic exposure. Our research makes clear that we're at a pivotal moment for boys' well-being. We can either let gambling become normalized during a critical period of their development, or we can act now—with education, safeguards, and real accountability.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of adolescent boys covering sports betting; abstract doesn't say whether a problem-gambling screen was used.

**Решение:** =

---

### 179 · R1094

**Direct gambling marketing, direct harm: A randomised experiment.**

2026 · Addiction (Abingdon, England) · journal article, randomized controlled trial · eng · https://doi.org/10.1111/add.70369

Whether gambling marketing has a causal effect on harm is of regulatory interest. Direct marketing offers (emails, push notifications and text messages) are frequently received by people with active gambling accounts, but they can opt out. This study aimed to test whether opting out of direct marketing reduces betting and short-term gambling harms in a real-world gambling environment. Stratified randomised field experiment with a between-participants design, embedded in a 14-day ecological momentary assessment (EMA). Nationwide, Australia (July-August 2023). Participants (n = 227; 61.7% men; mean age = 45), 52.0% of whom scored in the moderate-risk or problem range on the Problem Gambling Severity Index (PGSI), were regular Australian sports and race bettors recruited from online panels who agreed in principle to opt out of receiving direct marketing from all wagering operators with whom they held accounts. Participants were stratified by PGSI risk category, age group and gender and then randomly allocated either to an opt-out condition (n = 96), in which they opted out of direct marketing from their wagering operators and provided proof, or to a control condition (n = 131) that continued to receive direct marketing as usual. Seven EMA surveys were administered every 48 hours over a 14-day period during a high-volume betting season. Outcomes were self-reported number of bets placed, gambling expenditure (in Australian dollars, AUD) and short-term gambling harms in the previous 48 hours, assessed with a 10-item adapted Short Gambling Harm Screen (SGHS). The opt-out group placed 23% fewer bets [B = -0.11, 95% confidence interval (CI) = -0.20, -0.03, P = 0.011], spent 39% less money (B = -0.53, 95% CI = -0.84, -0.21, P = 0.001) and reported 67% fewer short-term gambling harms (B = -0.22, 95% CI = -0.36, -0.07, P = 0.004) compared with the controls. Opting out of receiving direct marketing from wagering operators appears to be associated with statistically significantly fewer bets made, amount spent gambling and short-term gambling harms.

**ИИ:** + · обе модели · беттеры + инструмент · Regular Australian sports and race bettors from online panels; the PGSI was used, and 52.0% scored moderate-risk or problem.

**Решение:** =

---

### 180 · R1095

**Persuasive Design in Esports Gambling: A Behavioral Analysis Through Cialdini’s Principles and the PSD Model**

2026 · Lecture notes in computer science · journalarticle, part of book or chapter of book, conference-paper · en · https://doi.org/10.1007/978-3-032-29593-4_35

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: No abstract; likely a design analysis of esports gambling platforms, but a 'behavioral analysis' could include a survey of bettors.); Sonnet -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: Design analysis of esports gambling persuasive features using Cialdini and PSD model; likely a content/design analysis, not a survey of people with a problem-gambling measure.)

**Решение:** ?

---

### 181 · R1102

**Changes in gambling behaviors among young adults in Rhode Island, 2022-2024.**

2026 · Addictive behaviors · journal article, journalarticle, review · eng · https://doi.org/10.1016/j.addbeh.2026.108804

Background The rapid expansion of legalized sports betting and mobile gambling in the U.S. has transformed how gambling is accessed and experienced. Young adults are particularly vulnerable to these changes; however, limited research has examined how gambling behaviors are shifting across multiple modalities during periods of expanding gambling availability. Methods We analyzed repeated cross-sectional data from the Rhode Island Young Adult Survey (RIYAS) collected in 2022 (n = 1,022) and 2024 (n = 1,008) among individuals aged 18-25 years. Outcomes included past-year participation in specific gambling behaviors, positive BBGS (Brief Biosocial Gambling Screen) screens, and overall gambling involvement measured as the number of gambling types endorsed. Multivariable logistic regression models estimated adjusted odds ratios for differences in individual gambling behaviors between survey waves, and Poisson/zero-inflated Poisson models estimated differences in gambling involvement. Results Gambling participation did not differ significantly between 2022 and 2024. However, among individuals reporting gambling, participation increased in several activities, including lottery tickets (AOR = 1.36, 95 % CI: 1.01-1.83), raffle gambling (AOR = 1.40, 95 % CI: 1.05-1.88), sports betting (AOR = 1.65, 95 % CI: 1.07-2.56), casino slot machines (AOR = 2.99, 95 % CI: 2.10-4.27), other slot machines (AOR = 2.30, 95 % CI: 1.23-4.33), and app-based gambling (AOR = 2.14, 95 % CI: 1.38-3.32). The number of gambling types endorsed increased (IRR = 1.28, 95 % CI: 1.16-1.41). Positive BBGS screens were more common in 2024 but not statistically significant after adjustment. Conclusions Findings suggest while overall gambling participation remained stable, engagement across multiple and mobile-based gambling activities increased between survey waves, potentially signaling emerging risk. Increasing diversification and digitalization of gambling behaviors requires continued surveillance and public health strategies addressing emerging gambling environments.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Young adult survey measuring sports betting participation and BBGS screens; could report problem gambling among sports bettors.

**Решение:** =

---

### 182 · R1103

**ESTRATEGIAS DE MARKETING EN LAS APUESTAS DEPORTIVAS: ANÁLISIS DE SU INFLUENCIA EN EL COMPORTAMIENTO Y FIDELIZACIÓN DE LOS JÓVENES**

2026 · BURJC Digital (King Juan Carlos University) · dissertation · es

Trabajo Fin de Grado leído en la Universidad Rey Juan Carlos en el curso académico 2025/2026. Directores/as: Jesús Anguita Grajales

**ИИ:** ? · обе модели · нет аннотации · Bachelor's thesis on sports betting marketing and youth behaviour; no abstract, so a survey with a problem-gambling screen cannot be ruled out.

**Решение:** =

---

### 183 · R1110

**A Study on Gambling Effect on Youths and Their Lifestyle In Tumkuru District**

2026 · Zenodo (CERN European Organization for Nuclear Research) · article, journalarticle/ · https://doi.org/10.5281/zenodo.22283600

Abstract The rapid growth of online and offline gambling activities has become a major social concern among young people in recent years. This study focuses on analyzing the effects of gambling on the lifestyle, behavior, financial condition, and social relationships of youths in Tumakuru. The research aims to understand the reasons behind the increasing involvement of youths in gambling activities and to examine how such habits influence their daily lives and future well-being. The study is based on both primary and secondary data. Primary data were collected through questionnaires and direct interaction with selected respondents from different areas of Tumakuru. Secondary information was gathered from journals, articles, reports, and online sources related to gambling behavior among youths. The findings indicate that factors such as peer influence, easy access to online betting platforms, stress, unemployment, and the desire for quick money are major reasons for youth participation in gambling activities. The research further reveals that excessive gambling negatively affects academic performance, mental health, family relationships, financial stability, and social behavior. Many respondents reported experiencing anxiety, loss of concentration, debt, and reduced productivity due to gambling habits. The study also highlights that continuous exposure to gambling can lead to addiction and unhealthy lifestyle patterns among youths. The paper concludes that awareness programs, parental guidance, educational support, and stricter regulation of gambling platforms are necessary to reduce the harmful effects of gambling on young individuals. Creating employment opportunities and promoting healthy recreational activities can also help youths avoid gambling-related risks and develop a more balanced lifestyle .

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Questionnaire survey of youths mentioning online betting platforms; abstract names no problem-gambling instrument and no sports betting measure.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Questionnaire study of youth gambling effects in Tumakuru; no problem-gambling instrument or sports betting measure evident, only reported impacts and motives.)

**Решение:** -

---

### 184 · R1112

**Sports betting as a social phenomenon: Public attitudes and motivation for participation**

2026 · Вестник Тюменского государственного университета. Социально-экономические и правовые исследования · journalarticle, review, article · https://doi.org/10.21684/2411-7897-2026-12-2-58-77

This article examines bookmaking and sports betting as a social phenomenon emerging at the intersection of economic, cultural, and institutional processes. It analyzes the contradictory nature of public attitudes toward bookmaking. The theoretical basis of the study is formed by classical and modern sociological approaches to the analysis of gambling, deviant behavior, social inequality, and the rationalization of economic practices. The main focus is on the motivation for participation in sports betting, the role of the social environment, media, and digital communications in the process of involvement. Financial and non-financial incentives for participation, emotional involvement, as well as the characteristics of trust in advertising and informal sources of information are considered. The study is based on data from a sociological survey conducted in Tyumen and examines the relationships between the social context of involvement, motivation for participation, and subjective assessment of the consequences of betting. The range of social and economic consequences of participation in bookmaking practices, as well as strategies for limiting or terminating participation, are analyzed. In conclusion, the place of bookmaking in the structure of modern leisure and economic practices, its role in the reproduction of social differences and the formation of ambivalent public attitudes towards gambling are determined.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Tyumen survey on sports betting attitudes and motivation; abstract does not say whether a problem-gambling instrument was used.

**Решение:** =

---

### 185 · R1115

**Mediterranean Diet Adherence and Screening Indicators of Gambling-Related Problems in a Sample of Young Adults: An Exploratory Cross-Sectional Analysis of the EVA-Adic Study**

2026 · Nutrients · article · en · https://doi.org/10.3390/nu18172919

Background/Objectives: Gambling disorder is recognized as a behavioral addiction, and gambling-related problems represent an important public health concern among young adults. However, evidence regarding their association with overall diet quality, particularly adherence to the Mediterranean diet (MedDiet), remains scarce. This exploratory secondary analysis examined whether screening indicators of gambling-related problems were associated with MedDiet adherence in young adults. Methods: We conducted a cross-sectional analysis of 496 participants aged 18–34 years from the EVA-Adic study. MedDiet adherence was assessed using the 14-item Mediterranean Diet Adherence Screener (MEDAS-14). Gambling-related indicators were assessed using the Short Pathological Gambling Questionnaire (CBJP), the Lie/Bet Questionnaire, and their six individual items. Independent multiple linear regression models were fitted for each indicator. The fully adjusted Model 2 included age, sex, alcohol consumption, sleep quality, sitting time, marital status, and educational level. Given the secondary nature of the analysis, the absence of an a priori sample-size calculation for the present research question, and the limited number of participants with positive gambling-related indicators, the analyses were considered exploratory and hypothesis-generating rather than confirmatory. Results: The mean age was 26.60 ± 4.41 years; 276 participants (55.6%) were women, and 157 (31.7%) had high MedDiet adherence. In the fully adjusted Model 2, feeling guilty about gambling (Q2) was nominally associated with a lower MEDAS-14 score (B = −1.10; 95% CI, −1.97 to −0.22; p = 0.015). However, this association did not remain statistically significant after Benjamini–Hochberg correction (q = 0.116), and none of the eight primary Model 2 associations met the FDR-adjusted significance threshold. Conclusions: Several gambling-related screening indicators showed nominal inverse associations with MedDiet adherence, with gambling-related guilt showing the most consistent estimate across sensitivity analyses. However, no association remained statistically significant in the fully adjusted model after correction for multiple testing, and formal interaction analyses provided no robust evidence of effect modification by sex. Given the small number of positive screens and the cross-sectional design, these findings should be considered exploratory and hypothesis-generating.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Young-adult sample screened with Lie/Bet and CBJP; the abstract doesn't say whether sports betting participation was measured.

**Решение:** =

---

### 186 · R1117

**PERSUASÃO DIGITAL E APOSTA ONLINE: UM EXPERIMENTO DE CAMPO SOBRE APELOS CENTRAIS E PERIFÉRICOS EM ANÚNCIOS DE APOSTAS ESPORTIVAS**

2026 · Anais do VII Congresso Internacional de Sustentabilidade · conference-paper, proceedings-article · https://doi.org/10.51189/vii-coninters/83390

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Field experiment on sports betting ad appeals with no abstract; unclear whether participants' problem gambling was measured.

**Решение:** =

---

### 187 · R1123

**Perceived parental attitudes and gambling behavior in adults: the moderating role of resilience**

2026 · Frontiers in Psychology · article · en · https://doi.org/10.3389/fpsyg.2026.1913942

Introduction Although multiple risk factors for problematic gambling have been identified, evidence regarding perceived parental attitudes and resilience remains limited, particularly among adults in Türkiye. This study investigated the associations between perceived parental attitudes and gambling behavior and the moderating role of resilience. Methods A cross-sectional online correlational study was conducted in İstanbul, Türkiye, between October 2024 and May 2025 with 389 participants recruited via convenience sampling. Data were collected using the Abbreviated Perceived Parental Attitudes–Child Form, the Brief Psychological Resilience Scale, and the South Oaks Gambling Screen–Turkish Version. Moderator analyses with bias-corrected bootstrap confidence intervals were performed. Results Maternal rejection was positively associated with gambling severity (B = 0.106, 95% CI [0.053, 0.160], p < 0.001), as was paternal rejection (B = 0.123, 95% CI [0.073, 0.174], p < 0.001). Resilience significantly moderated both associations (maternal rejection × resilience: B = −0.017, 95% CI [−0.028, −0.005], p = 0.005; paternal rejection × resilience: B = −0.016, 95% CI [−0.028, −0.003], p = 0.012). Simple slope analyses showed that the associations between parental rejection and gambling severity were significant at low (maternal: B = 0.176, p < 0.001; paternal: B = 0.189, p < 0.001) and average (maternal: B = 0.106, p < 0.001; paternal: B = 0.123, p < 0.001) levels of resilience but were not significant at high resilience (maternal: B = 0.037, p = 0.265; paternal: B = 0.058, p = 0.092). Exploratory correlation analyses additionally showed that parental emotional warmth was positively associated with resilience. Discussion These findings suggest that resilience may buffer the association between perceived parental rejection and gambling severity.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Adult survey (n=389) used SOGS-Turkish; sports betting participation not mentioned but may be captured by SOGS activity items.

**Решение:** =

---

### 188 · R1127

**AI-Assisted Bettors: Analyzing AI-Driven Betting Behavior through Cluster Analysis**

2026 · Journal of the Association for Information Systems · article · https://doi.org/10.17705/3jmwa.000097

The use of artificial intelligence (AI) systems in consumer-facing decision-support systems (DSS) such as predictive analytics and automated recommendation platforms is growing in popularity in numerous domains, including sports betting. The degree to which users interact with the output of automated systems, calibrate trust, and exhibit automation bias–consistent behavior is largely unknown. In this study, we investigate the behavioral segments formed by bettors using AI-powered predictive sports betting DSS based on their shifts in confidence, risk-taking behavior, and bankroll management practices. We use survey data from a sample of 200 U.S.-based bettors and SPSS TwoStep Clustering to identify three distinct behavioral profiles: Traditional Bettors, AI-Influenced Confident Bettors, and AI-Adopting Risk-Takers, each with their own unique set of interactions with and through predictive DSS. The findings show that bettors can engage in responsible adoption through strategic bankroll management practices and a tempering of AI trust, while overreliance behaviors can be mitigated or amplified, respectively, by counter or co-aligning with individual differences. Framing betting platforms as real-time, in-the-wild, and consumer-deployed DSS contributes to IS research on algorithmic decision environments, user trust, and human–computer interaction. The results advance IS theory by contributing to the discussion of how cognitive biases, human decision behaviors, and confidence amplification in and through automated systems manifest in such domains. We conclude the paper with implications for responsible DSS design and deployment as well as practical guidelines for user segmentation in predictive analytics DSS environments.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of 200 US sports bettors using AI tools; the abstract doesn't say whether a problem-gambling instrument was used.

**Решение:** =

---

### 189 · R1128

**Predicting and Understanding Mobile Sports Gambling with the Reasoned Action Approach.**

2026 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-025-10456-1

Mobile sports betting is an increasingly popular way to wager in the United States, but few studies have examined the social cognitive predictors of engaging in this specific form of gambling. The present studies were designed to do so with the application of the Reasoned Action Approach (RAA; Fishbein & Ajzen, 2010). Study 1 was a belief elicitation study that identified the most common behavioral, normative, and control beliefs regarding mobile sports betting. Study 1 also reported an initial test of the degree to which attitude, perceived normative pressure, and perceived behavioral control predict intentions to place mobile sports bets. Study 2 examined the predictive validity of the identified beliefs and tested whether future betting behavior can be predicted from the model. The RAA significantly predicted mobile sports gambling intentions and future behavior. The most important beliefs contributing to the prediction of mobile sports gambling were the degree that participants endorsed gambling is fun and easy, leads to addiction, and results in winning money. Implications for future research and interventions are discussed.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Reasoned Action Approach survey of mobile sports betting; abstract doesn't say whether a problem-gambling screen was used as a covariate.

**Решение:** =

---

### 190 · R1130

**Football World Cup 2026 Gambling Study**

2026 · OSF Registries · studyregistration/pre-registration, preprint · https://doi.org/10.17605/osf.io/fwq67

The present study includes online research into betting behaviour within the real-life context of the 2026 World Cup. Variables aside from descriptives that will be investigated are sports betting consumption, gambling problems, bet amount, preferred odds, bet choice motivation, subjective probability of the real-life bets, and subjective probability of an urn-and-ball task. The manipulation will be in the verbal framing of the bet (aggregated vs. disaggregated), and the verbal and visual framing of the urn-and-ball task (aggregated vs. disaggregated). The present research will investigate whether aggregated vs. disaggregated framing of the bets will change sports betting behaviour (bet amount). Additionally, the sports betting behaviour will be investigated as a function of subjective probabilities. The overall aim is to discover whether framing can be applied as a way to increase subjective probability, to subsequently lessen the amounts bet by sports bettors. Furthermore, the present study will add to the literature on determinants of betting behaviour, to eventually be used to inform policy on how (sports) bettors can be better protected. We hypothesize that bet amounts will differ between aggregated and disaggregated bet framing conditions. Since the preparation timeline of the study is very short and dependent on the FIFA World Cup 2026, we did not have sufficient time to preregister all analyses, but we will add amendments to this pre-registration to further specify additional analyses before inspection of the data (aside from quality checks).

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Pre-registered online survey/experiment of World Cup sports bettors measuring 'gambling problems'; instrument not named, and no results yet.

**Решение:** =

---

### 191 · R1131

**Associations Between Gambling Motives and More Severe Gambling Disorder – Does Gender Matter?**

2026 · Journal of Gambling Studies · article · en · https://doi.org/10.1007/s10899-025-10470-3

Gambling Disorder (GD) is a behavioural addiction with complex, detrimental psychological, economic, and social consequences. Previous research has examined gender differences in the prevalence of distinct gambling motives and has linked gambling motives to at-risk behaviour. Whether motives affect probabilities of transition to higher GD severity levels differently in males and females remains unclear. Using an online self-test, we assessed the prevalence distinct GD severity levels according to the DSM-5 criteria and gambling motives with items addressing domains of the "Gambling Motives Questionnaire - Financial" (GFQ-F). Associations between motives and GD severity at three transition points (no GD to mild, mild to moderate, moderate to severe GD) were analysed using age-adjusted logistic adjacent category regression models. Interaction terms (motive*gender) were examined to detect gender-specific "effects". Furthermore gender-stratified models were run. No significant gender*motive interactions emerged. In the total sample, a transition to a higher GD severity level was predicted by: "(to) Forget worries", "When depressed," and "(to) Earn money" at each transition point; "Thrill" and "Stress" at the first two points, and "Boredom" at the first point. In males, the results were nearly identical. In females only "Thrill", "Boredom", and "(to) Earn money" were predictive at the first transition point. Given the prevalence of coping motives in females and the consistent detrimental "effect" of coping and financial motives in males, these motives should be prioritized in treatment and support offers for both genders. For prevention, strategies targeting enhancement motives may be particularly effective.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Online self-test sample of gamblers using DSM-5 GD criteria; unclear whether gambling activities such as sports betting were recorded.

**Решение:** =

---

### 192 · R1135

**The Effects of Game-Related Experiences on Delinquent Behavior among Adolescents: The Mediating Roles of Gambling Problem Perception and Gambling Experience.**

2026 · The Korean Society of Private Security · article, journalarticle, review · und · https://doi.org/10.56603/jksps.2026.25.1.191

This study aims to examine the effect of adolescents’ game-related experiences on deviant behavior and to analyze whether problem gambling perception and gambling experience serve as mediating variables in this relationship. In recent years, digital gaming environments have become a primary leisure space for adolescents. However, concerns have been raised as these environments increasingly incorporate gambling-like features, such as loot boxes, virtual item trading, and sports betting-related elements, which may lead to gambling behaviors and subsequent deviant activities. This study goes beyond examining direct effects by structurally testing a parallel mediation model in which problem gambling perception and gambling experience function as key mediators between game-related experiences and deviant behavior. The analysis utilized data from the “2022 National Survey on Youth Gambling Problems” conducted by the Korea Center on Gambling Problems, with a total sample of 18,944 adolescents, including both in-school and out-of-school youth. The results indicate that game-related experiences have a significant positive effect on deviant behavior. In addition, game-related experiences were found to negatively influence problem gambling perception while positively affecting gambling experience. The mediation analysis revealed that game-related experiences influence deviant behavior through both a cognitive pathway, which weakens problem gambling perception, and a behavioral pathway, which increases gambling experience. These findings suggest that adolescents’ gaming experiences extend beyond mere leisure activities and may contribute to deviant behavior through gambling-related perceptions and behaviors. This study highlights the need for preventive policy approaches that move beyond reactive control strategies. Specifically, it emphasizes the importance of proactively managing gambling-like elements within gaming environments and enhancing adolescents’ awareness of gambling risks as part of comprehensive prevention efforts.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Secondary analysis of Korean national youth gambling survey; abstract names perception and experience variables, not a problem-gambling screen; full text might.

**Решение:** =

---

### 193 · R1140

**Beyond cognitive distortions: the mediating role of passion between erroneous cognitions and gambling severity**

2026 · Australian Journal of Psychology · article · en · https://doi.org/10.1080/00049530.2026.2726226

Objective: While erroneous gambling cognitions and gambling passion (harmonious and obsessive) are recognised as key factors underpinning an individual's gambling, limited research has examined whether passion explains how cognitive distortions relate to gambling severity. Method: = 11.52). . Results: Controlling for gambling preference, frequency, and social desirability, predictive control exhibited a significant negative indirect path to gambling severity via harmonious passion, whereas obsessive passion positively mediated the relationship between illusion of control, interpretive bias, and gambling severity. Furthermore, obsessive passion significantly (negatively) moderated the relationship between interpretive bias and gambling severity. Conclusion: Findings suggest that when individuals overestimate predictive control, they may cognitively minimise risks associated with their gambling. Additionally, internal pressure from obsessive passion could inflate perceived control over random outcomes and heighten the tendency to attribute outcomes to skill. Moderation results indicated obsessive passion may exert a stronger influence on gambling severity than interpretive bias. Overall, findings highlight the need to target both gambling cognitions and passion when addressing an individual's gambling severity.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Survey of gamblers measuring gambling severity, controlling for gambling preference; method truncated, unclear whether sports bettors are identifiable.

**Решение:** =

---

### 194 · R1141

**Harmonious and obsessive gambling passion: a comparative analysis of non-problem to problem gamblers**

2026 · Addiction Research & Theory · article · en · https://doi.org/10.1080/16066359.2026.2638744

While researchers have investigated the link between gambling and passion, there is currently a paucity of literature detailing the precise relationship between harmonious and obsessive passion across the full spectrum of this behavior. The current study aimed to investigate the association between these passion constructs and empirically established levels of gambling severity: non-problem, low-risk, moderately at-risk, and problem gamblers. A total of (n = 630) gamblers aged between 18 and 73 (Mage = 38.56, SDage = 11.52) recruited via the general community and through Prolific.co, completed an online survey consisting of the Gambling Passion Scale (GPS), Problem Gambling Severity Index (PGSI) and the Short-Marlowe-Crowne Social Desirability Scale (S-MCSDS). Partial correlations revealed a significant weak negative correlation between harmonious passion and PGSI scores, and a strong positive partial correlation between obsessive passion and PGSI scores. Results from one-way ANOVAs showed that problem gamblers scored significantly higher on both harmonious and obsessive passion compared to the non-problem, low-risk and moderately at-risk gamblers. Findings from the current study provide insights into the role of passion in problem gambling and suggest that both may be salient toward an individual’s gambling behavior. Given these results, clinicians should consider focusing on the construct of passion when assessing and classifying a gambler’s risk profile. Focusing on passion may also elucidate a more holistic understanding of individuals’ perception of their own gambling behavior, which, in turn, could facilitate the development of more refined, personalized intervention strategies.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Community survey of gamblers using the PGSI; the abstract doesn't say whether participation in sports betting was measured.

**Решение:** =

---

### 195 · R1143

**NORMATIVE INFLUENCE ON SPORTS BETTING AMONG YOUNG MEN IN GHANA**

2026 · UKnowledge (University of Kentucky) · dissertation/, article · https://doi.org/10.13023/etd.2026.408

Sports betting has become an increasingly visible feature of everyday sport culture in Ghana, yet theory-driven communication research explaining how betting becomes socially normalized among young men remains limited. Drawing on the theory of normative social behavior and its communication-centered reconceptualization, this dissertation used an exploratory sequential mixed-methods design to examine how interpersonal communication, observation, and media exposure shape perceived norms, and how those norms relate to sports betting and its associated harms. Study One used semi-structured interviews with ten young Ghanaian men who bet on sports. Participants described a filtered communication environment in which wins circulate widely, losses are minimized or withheld, and audiences are carefully selected. Betting appeared ordinary because young men encountered it through friends, betting shops, phones, advertisements, sports media, and public debate. At the same time, participants described avoiding the people most likely to object, including parents, partners, religious figures, and non-betting peers. The qualitative findings showed that betting was widely normalized as participation, but not uniformly approved, and that help-seeking was constrained because admitting a desire to stop also meant admitting that betting was no longer working. Study Two tested the proposed communication-centered normative pathway in a survey of 314 young Ghanaian men who bet on sports. The results showed a consistent distinction between descriptive and injunctive norms. Perceived descriptive norms were predicted by observation of referent others, media exposure, and communication frequency, and were associated with betting frequency. Perceived injunctive norms were predicted only by positive and excitatory betting talk and were associated with PGSI-SB severity. Indirect-association models showed that descriptive norms accounted for pathways from communication frequency, observation, and media exposure to betting frequency, while injunctive norms accounted for the pathway from positive betting talk to PGSI-SB severity. Outcome expectations and pro-betting attitudes strengthened the association between injunctive norms and PGSI-SB severity. Together, the findings show that communication does more than accompany sports betting. It helps make betting visible, frames what is worth sharing, signals what appears common or approved, and shapes the conditions under which young men can disclose harm or seek support. Findings distinguish the normative processes associated with how often young men bet from those associated with how much harm they experience. The findings clarify communication mechanisms relevant to harm reduction, including the potential value of correcting one-directional information environments and of addressing the disclosure barriers that discourage help-seeking.

**ИИ:** + · обе модели · беттеры + инструмент · Mixed-methods dissertation; its quantitative part surveyed 314 young Ghanaian men who bet on sports and used a sports-betting version of the PGSI (PGSI-SB).

**Решение:** =

---

### 196 · R1144

**Neurobehavioral Heterogeneity in Problem Gambling Severity and Nicotine Use Risk: Divergent Profiles of Cognitive and Emotional Control**

2026 · Journal of Gambling Studies · article · en · https://doi.org/10.1007/s10899-026-10519-x

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; a quantitative study of problem gambling severity in gamblers that might record gambling activities, including sports betting.

**Решение:** =

---

### 197 · R1151

**ANALYZING THE DETERMINANTS, PSYCHOLOGICAL CORRELATES, AND INTERVENTION STRATEGIES FOR ONLINE GAMING ADDICTION AMONG AVIATOR BET USERS IN NAIROBI COUNTY, KENYA**

2026 · International Journal of Social Sciences and Management Review · article, journalarticle, review · und · https://doi.org/10.37602/ijssmr.2026.9320

The rapid proliferation of digital gaming and betting platforms has fundamentally transformed patterns of leisure, economic participation, and behavioral health across the globe, with particularly acute implications for emerging digital economies in sub-Saharan Africa. The small but growing niche occupied by hybridal types of gaming-gambling games, like the Aviator Bet service, has combined real-time wagering systems with the high frequency nature of gaming in ways that increase the susceptibility to compulsive and addictive behavior. The overlap of efforts to provide a mobile financial infrastructure, most prominently M-Pesa, and a greater Sony number of more advanced online betting technologies has provided a space in which younger adult online gambling addicts are uniquely predisposed to form behavioral addiction patterns. The paper explores the predictors, mental factors, and treatment consequences of online gaming addiction between the users of Aviator Bet in the Nairobi County, Kenya with the two-fold aim of defining the extent of the issue, and analyzing evidence-based interventions.To obtain convergent qualitative and quantitative data, a parallel mixed-methods approach was used that combined quantitative survey data that was gathered on 248 participants who are adults and qualitative information obtained via the in-depth interview. The study sample was selected using stratified sampling in the different sub-counties in Nairobi, which is a diverse city and peri-urban area. The high prevalence of moderate to severe online gaming addiction was found as quantitative results, where 62.5% of the participants fit the criteria of engaging in a way that was considered to be clinically significant. Regression analysis proved the severity of addiction as a significant predictor of psychological distress (0.48, p &lt;.001) and significant positive correlation was identified between addiction severity and anxiety (r =.52), depression (r =.49) and perceived stress (r =.46). Social outcomes were also evident with high addiction levels showing the existence of financial strain ( 0.41, p &lt;.01), interpersonal conflict ( ${-0.37, p &lt;.01).It is the qualitative data that complemented these quantitative trends by pointing to cognitive distortions such as illusions of control and gamblertype fallacy thinking, maladaptive coping styles, vulnerability of socioeconomic status and peer normalization as primary psychosocial influences in perpetuating and maintaining compulsive involvement.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Survey of Kenyan users of Aviator, a crash game. Sports betting participation and the addiction instrument are unclear; these users may also bet on sports.

**Решение:** =

---

### 198 · R1153

**Understanding the Socio-Demographic Profiles and Motivations behind Youth Participation in Sports Betting: A case study of Dar es Salaam City, Tanzania**

2026 · Tanzania Journal of Community Development · article, journalarticle, journal-article · und · https://doi.org/10.4314/tajocode.v5i1.6

This study examines the socio-demographic profiles and motivations of youth sports bettors in Dar es Salaam city, Tanzania. The study employed a cross-sectional design; data were collected from 205 participants across five wards through mixed-methods analysis. Both primary and secondary data were used in this study, while the data analysis involved SPSS. The study is anchored in Rational Choice Theory, Social Learning Theory and Sustainable Livelihood Frameworks; challenging the "idleness" myth, and suggesting that sports betting is a rational, albeit high-risk, adaptive strategy to structural economic constraints and urban income instability. Findings reveal that betting participation is not limited only to marginalized youth. While economic gain serves as the primary driver; social environments play a critical role in sustaining betting practices. The study concludes that social learning in urban hubs (vijiwe) sustains participation beyond initial entry. Recommendations include implementing stricter zoning regulations for betting outlets near residential areas and developing community-based programs that offer more stable financial growth than speculative gambling. This research emphasizes shifting policy from moralistic discouragement toward evidence-based structural interventions beyond Dar es Salaam context.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Cross-sectional survey of 205 youth sports bettors focused on demographics and motivations; abstract does not say whether problem gambling was screened.

**Решение:** =

---

### 199 · R1176

**Decisions at Play: Influence of Gambling Advertisements and Influencer Content during FIFA World Cup 2026 on Attitudes, Cognitions, and Gambling Initiation**

2026 · OSF Registries · studyregistration/pre-registration, preprint · https://doi.org/10.17605/osf.io/s3jud

This project investigates how exposure to gambling advertisements, including sports betting, and influencer gambling-related content during the 2026 FIFA World Cup is associated with gambling-related attitudes, cognitions, and behaviour among adults in Germany. Major sporting events are characterised by heightened visibility of gambling promotions across television and digital media, which may contribute to the normalisation of gambling, to the initiation or intensification of gambling behaviour as well as the reinforcement of gambling-related cognitive distortions. Data will be collected at three timepoints: before the tournament, during the tournament, and after the tournament. Participants will self-report their exposure to gambling-related content, gambling attitudes and expectancies, gambling-related cognitive distortions, motivation to gamble, gambling behaviour (including initiation, frequency, and spending), and gambling-related problems. The study further examines whether these associations are stronger among individuals with known vulnerability factors for gambling-related harm. The study aims to improve understanding of the associations between gambling-related media exposure during major sporting events and changes in gambling-related cognition and behaviour over time, with potential implications for responsible gambling and advertising policies.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Pre-registered German adult panel survey covering sports betting and gambling-related problems; instrument unspecified, and no data yet.

**Решение:** =

---

### 200 · R1180

**PATTERNS AND PREVALENCE OF SPORTS BETTING AMONGST UNDERGRADUATE SPORTS ENTHUSIAST**

2026 · Journal of the Nigeria Association of Sports Science and Medicine · article, journalarticle, journal-article · und · https://doi.org/10.66986/jnassm.2026.1901.33-j

Sports betting has transformed from an ancient pastime into a multi-billion-dollar global industry, influencing economies, sports culture, and individual behaviours. This article critically examines the evolution of sports betting, its global and national trends, and its growing prevalence among Nigerian youth, particularly among university students and sports enthusiasts. While the industry generates substantial revenue, supports employment, and enhances sports engagement, it also raises concerns about addiction, financial distress, and regulatory loopholes. The accessibility of online betting platforms, coupled with aggressive marketing and celebrity endorsements, has fuelled increased participation, often at the expense of financial stability and academic performance. Additionally, this paper explores the socioeconomic impact of betting, highlighting how economic hardship and peer influence contribute to widespread gambling behaviours. With Nigeria emerging as a major betting hub in Africa, a strategic balance between economic benefits and social responsibility is crucial. Strengthening regulatory frameworks, promoting financial literacy, and implementing responsible gambling measures are imperative to mitigate associated risks. This article advocates for a holistic approach that safeguards vulnerable populations while ensuring the sustainability of the industry within ethical boundaries.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · The title suggests a prevalence survey of student sports bettors, but the abstract reads like a narrative review and names no problem-gambling instrument.

**Решение:** =

---

### 201 · R1188

**Gambling behavior and problem risk by coaching status in individuals with athletic backgrounds from an epidemiological sample**

2026 · International Gambling Studies · article · en · https://doi.org/10.1080/14459795.2026.2697456

The popularity and expansion of sports wagering has highlighted the betting behavior of athletes, particularly at college and professional levels. Far less attention, however, has been paid to the gambling behavior of coaches, despite their immersion in sports environments saturated with gambling opportunities and their potential influence on athletes’ attitudes and behaviors. The present study utilized a subsample of individuals with athletic backgrounds from an epidemiological study (N = 1,778), including current coaches (n = 161), former coaches (n = 595), and individuals who never coached (n = 1,022). Bivariate comparisons by coaching status found that current coaches gambled at the highest frequency, in more venues, across more activities, including sports and fantasy sports betting, and reported the highest rates of problem gambling. In a multivariate linear regression, current coach status was associated with a 2.33-point higher Problem Gambling Severity Index score (p < .001) compared to non-coaches; former coaches did not significantly differ from non-coaches. Among current coaches, problem gambling was associated with being an NCAA athlete, current sports participation, perceiving family and friend participation in sports betting, depression, drug and alcohol problems, risky sex, and excessive video/internet gaming. These findings suggest coaches require their own education and intervention, and should be included in prevention programs targeting athletes.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Epidemiological subsample of athletes; measured sports and fantasy sports betting and PGSI, so the full text may report problem gambling among sports bettors.

**Решение:** =

---

### 202 · R1195

**An Exploratory Investigation of College Student Betting Behaviors: How Pervasive is Sports Betting in the Age of Legalized Gambling?**

2026 · DigitalCommons - Kennesaw State University (Kennesaw State University) · article

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the title points to a survey of college students' sports betting, and it is unclear whether problem gambling was measured.

**Решение:** =

---

### 203 · R1197

**Personality Traits, Self Esteem and Perceived Controllability as Predictors of Psychological Health among Gamblers in Ado Ekiti, Ekiti State**

2026 · Nigerian Journal of Social Psychology · article · en

Sports betting and other forms of gambling have increased rapidly across many African cities, including those in Nigeria, largely driven by the growth of commercial betting outlets and mobile betting platforms. Although research from high-income countries links gambling with adverse psychological outcomes, empirical evidence on the psychological determinants of gamblers’ well-being in low- and middle-income countries (LMICs) remains limited. Understanding how personality characteristics and perceived control relate to psychological health among gamblers in African settings is therefore important for informing prevention and intervention strategies. A cross-sectional survey design was employed among 300 active gamblers recruited through purposive sampling from major sports betting centres in Ado Ekiti, Nigeria. Participants completed standardized measures assessing Big Five personality traits, self-esteem, perceived controllability, and psychological health. Data were analysed using Pearson correlation, multiple regression analysis, and independent-samples t tests. Perceived controllability showed a significant positive association with psychological health (r = .12, p .05. However, extraversion (β = −.15, t = −1.69, p .05. Personality factors and perceived controllability appear to have modest but meaningful associations with gamblers’ psychological health. Interventions targeting gamblers in Nigeria may benefit from incorporating personality-informed counselling and cognitive-behavioural approaches aimed at strengthening perceived control.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Survey of 300 gamblers recruited at Nigerian sports betting centres; the listed measures include no problem-gambling instrument, though one may appear in the full text.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Survey of gamblers at sports betting centres, but measures only personality, self-esteem, controllability and psychological health; no problem-gambling instrument mentioned.)

**Решение:** ?

---

### 204 · R1200

**The impact of cash out availability on online betting behavior**

2026 · PsyArXiv · article, preprint, studyregistration/pre-registration · und · https://doi.org/10.31234/osf.io/rkb7a_v1

The rise of online sports betting, facilitated by technological innovations such as the cash-out feature, has transformed the gambling landscape. While cash-outs (a facility provided by betting operators which allows gamblers to close a bet early before the final outcome of a sports event is known) have been suggested to intensify problematic gambling behaviors, empirical studies to date have been correlational, leaving a gap in determining causal evidence. The present Registered Report investigated the direct impact of the perceived availability of the cash-out feature on various facets of gambling behavior in an online experiment. Hungarian residents with an online gambling history (N=595) were informed that they would have the chance to gamble with real money on sports events. Following random allocation, half of the participants were told that they would have the option to cash out their bets before the outcome of the sports event is known, while the other half did not have this option. Overall, the findings provided evidence that cash-out availability did not influence bet placement, wager size, or bet risk among our sample. However, the low variance in the outcomes may have limited the ability to detect subtle differences. Consequently, the null results should not be taken as conclusive evidence of no behavioral effect.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Online experiment with 595 online gamblers betting on sports; a PGSI covariate is likely but the abstract doesn't mention one.

**Решение:** =

---

### 205 · R1214

**Correction to: Patterns of Gambling Behavior Influenced By Materialism, Financial Well-Being, and Monetary Motivation Among Sports Bettors: A Latent Profile Analysis.**

2026 · Journal of gambling studies · article, journalarticle, published erratum · eng · https://doi.org/10.1007/s10899-026-10488-1

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Erratum to a survey of sports bettors with latent profiles of gambling behaviour; a problem-gambling instrument is likely but not confirmed.); Sonnet -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: Published erratum with no abstract or data; the original sports bettor latent profile article would be screened separately.)

**Решение:** ?

---

### 206 · R1215

**(Mis)Comprehension and (Mistaken) Attractiveness of Financial Gambling Inducements among UK Bettors.**

2026 · Journal of gambling studies · journal article · eng · https://doi.org/10.1007/s10899-026-10491-6

Financial gambling inducements such as ‘free’ bets and welcome bonuses involve complex wagering requirements that many consumers miscomprehend. UK regulations cap these wagering requirements at x10 (i.e., users must wager x10 the bonus before withdrawal) but don’t require worked examples to aid comprehension. This study assessed UK bettors’ comprehension of inducement wagering requirements, whether comprehension varied by gambling severity, whether perceived attractiveness differed when worked examples were displayed, and bettors’ broader perceptions of inducements. A between-subjects, mixed-methods online experiment randomised UK bettors (n = 585) to view a welcome bonus inducement either with or without (control) a worked example detailing its wagering requirement. Participants completed measures of comprehension, perceived attractiveness, gambling severity, and qualitative questioning. Participants in the control condition significantly underestimated the inducement’s wagering requirements (p<.001, r=.94), with a median estimate of £500 versus the correct value of £750. Underestimation did not differ by gambling severity. The inducement was rated significantly less attractive (p<.001, η²=.18) when the worked example was displayed (M = 2.39, SD = 1.46) compared to the control (M = 3.75, SD = 1.48). However, this effect was moderated by gambling severity (B=-0.112, p=.005), with the reduction in perceived attractiveness associated with the worked example becoming smaller as gambling severity scores increased. Qualitative analysis identified three overarching perceptions of inducements: as manipulative, economically worthless, and requiring better regulation. UK bettors significantly underestimate inducements’ wagering requirements, while worked examples significantly reduce their mistaken attractiveness. These findings demonstrate how informed choice can be enhanced via worked examples.

**ИИ:** разошлись — Opus + (беттеры + инструмент: Online experiment with 585 UK bettors that measured gambling severity scores (probably PGSI) as a moderator; the full text may give problem-gambling rates.); Sonnet ? (неясно, есть ли ставки на спорт: Online experiment with 585 UK bettors measuring gambling severity (likely PGSI); unclear whether they are sports bettors or whether problem-gambling rates are reported by sample.)

**Решение:** ?

---

### 207 · R1217

**PERSONALITY TRAITS AND THEIR INFLUENCE ON FANTASY SPORTS GAMBLING**

2026 · Zenodo (CERN European Organization for Nuclear Research) · dissertation/, doctoral thesis, thesis · en · https://doi.org/10.5281/zenodo.21084664

Online fantasy sports gambling is a rapidly growing field of entertainment, in which players bet on athletes across various sports to win cash prizes. Online fantasy sports gambling’s rapid development raises concerns regarding the underlying factors that may drive problematic sports betting behavior (e.g. risky betting behavior). This study focuses on the association between the two personality domains of Neuroticism and Extraversion on fantasy sports gambling severity. A quantitative study was conducted utilizing college student fantasy sports betters. Participants (N = 98) reported engaging in fantasy sports in the past year and were assessed for as personality traits, income, engagement rate, number of bets placed on average, size of bets placed, motivational orientation, and impulsivity rate. Pearson’s correlations were used to assess associations between neuroticism, extraversion, and fantasy sport gambling severity. Multiple regressions utilizing variables were used to derive the best set of predictors for gambling severity. Findings indicated no statistically significant relationship between neuroticism and gambling severity (r [96] = -.10, p = .34). No significant linear associations were found between extraversion and gambling severity (r [96] = .10, p = .34). Neuroticism and extraversion were nonsignificant predictors of gambling severity, F(2,95) = 1.05, p = .35, R² = .02. The best predictors of fantasy sport gambling severity were external regulation motivational orientation, bet size, personal income, impulsivity, and engagement, F(5,92) = 13.43, p <.001, R² = .42. Findings suggest that behavioral factors may be more accurate predictors of problematic gambling rather than personality traits.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of college fantasy sports bettors measuring gambling severity; the instrument is not named in the abstract.

**Решение:** =

---

### 208 · R1219

**Understanding Gambling Behavior Among Hispanic College Students: The Role of Attitudes, Norms, Self-Efficacy, and Acculturation**

2026 · DigitalCommons@UTEP (The University of Texas at El Paso) · article · en

Gambling has become increasingly accessible and socially normalized among young adults, particularly through mobile platforms and the expansion of legalized sports betting. Hispanic college students may be at heightened risk for gambling-related harms, given evidence of elevated rates of problem gambling, comorbid mental health concerns, and underrepresentation in empirical research. Cultural factors, such as acculturation, may further influence engagement in gambling behaviors and susceptibility to negative outcomes. Guided by the Theory of Planned Behavior, the present study investigated the relationships between gambling injunctive norms, gambling attitudes, and gambling self-efficacy across three outcomes: gambling frequency, problem gambling severity, and gambling intention. Additionally, this study examined whether acculturation and enculturation moderated these relationships. Participants included 318 Hispanic college students recruited from a U.S.-Mexico border university. Participants completed self-report measures assessing sociodemographic characteristics, gambling attitudes and norms, gambling intentions, gambling self-efficacy, gambling behaviors, problem gambling severity, and acculturation/enculturation. Two linear regression analyses were conducted to test main and interaction effects, controlling for age and sex, and negative binomial regression analysis was utilized to assess gambling frequency after it was observed to have a non-normal distribution to be zero inflated. Results indicated that gambling attitudes were positively associated with gambling frequency, problem gambling severity, and gambling intention. Gambling self-efficacy was negatively associated with gambling intention, problem gambling severity, gambling intention, suggesting a protective effect. Neither acculturation nor enculturation significantly moderated any of the examined relationships. These findings highlight the importance of cognitive and perceived control factors in understanding gambling behaviors among Hispanic college students. By integrating culturally relevant constructs within an established theoretical framework, this study contributes to the growing literature on gambling in underrepresented populations. Implications include the development of culturally responsive prevention and intervention strategies that target maladaptive attitudes and enhance self-efficacy to reduce gambling-related harm.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Student survey measured problem gambling severity and gambling behaviours; the abstract doesn't say whether sports betting participation was recorded.

**Решение:** =

---

### 209 · R1228

**Sanctified Bets? Religiosity, Gender, and Sports Gambling in the United States**

2026 · Sociology of Sport Journal · article, journalarticle, review · und · https://doi.org/10.1123/ssj.2025-0136

Over the past decade, the gambling landscape in the United States has shifted dramatically, with sports betting becoming more accessible and widespread than ever. Sports gambling is linked to sanctified constructs and rituals involving masculinity, leisure, sport, nation, and religiosity, complicating traditional moral deterrents related to it. To investigate connections between religiosity and sports gambling, we drew on the National Sports and Society Survey data ( N = 3,701) on U.S. adults. Findings challenge assumptions that religiosity uniformly suppresses gambling behavior. Those who attended religious services infrequently (e.g., once or twice a year) were more likely to gamble and wager more money than both weekly attenders and nonattenders. Catholics were especially likely to engage in sports gambling. Yet, gender moderated these relationships, with religious women significantly less likely to gamble on sports or wager large sums. Still, religiosity did not appear to determine sports gambling outcomes (i.e., wins/losses), among those who gambled. Overall, our findings reveal a complex, contingent relationship between religion and sports gambling.

**ИИ:** разошлись — Opus -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: US adult survey reporting sports gambling participation, amounts wagered and wins/losses only; no problem-gambling instrument indicated.); Sonnet ? (неясно, измеряли ли проблемную игру: National survey of US adults on sports gambling and religiosity; the abstract doesn't say whether a problem-gambling instrument was used, so the full text is worth checking.)

**Решение:** ?

---

### 210 · R1232

**Gambling Advertising and Problem Gambling in the United States: Multi‐Level Evidence Beyond Sports‐Betting Legal Status**

2026 · Policy & Internet · article · en · https://doi.org/10.1002/poi3.70060

ABSTRACT US gambling debates often center on the legal status of sports‐betting, but advertising can also be used as a distinct policy lever. This paper presents the findings of two related studies. Study 1 links quarterly state‐level gambling advertising outlays across paid media (2014–2023) to Google Trends indices for 116 problem‐gambling help‐seeking queries across 41 states (1640 state‐quarters). Study 2 combines surveys with passive digital traces from 419 exposure‐eligible mobile‐platform users. Higher state‐level ad spend, but not sports‐betting legal status, was associated with greater help‐seeking search interest, and this association strengthened over time. Platform‐specific gambling‐ad exposure on Facebook, TikTok, and X was associated with gambler status, gambling frequency, and the probability of any observed gambling‐site visit. Clean gambling ads were also associated with higher 24‐h odds of subsequent gambling touchpoints, especially web visits; among gamblers, ad‐triggered touchpoints were associated with problem‐gambling scores more consistently than raw clean ad volume. Convergent state‐level and individual‐level evidence links gambling advertising with engagement and harm‐related indicators, while the observational designs do not identify causal effects. The findings support stronger restrictions on advertising volume, placement, inducements, and targeting.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Survey of 419 US users measured problem-gambling scores; unclear whether sports betting participation was recorded per respondent.

**Решение:** =

---

### 211 · R1238

**Gambling disorder symptom severity and mental health: an item-response-theory analysis of DSM-5 criteria for gambling disorder**

2026 · medRxiv · preprint · https://doi.org/10.64898/2026.08.12.26360267

Abstract The present study examined the relationship between the DSM-5 diagnostic criteria for gambling disorder (GD) and gambling severity via an item response theory (IRT) analysis in two large German population survey data sets (Buth et al. (2022, 2024)). IRT-based person fit analyses may reveal atypical response patterns (e.g. endorsing criteria linked to higher levels of disorder severity, but not criteria linked to lower levels). We examined the link of such atypical response patterns and mental health as measured by the MHI-5, employing a 2-parameter-logistic (2PL) IRT model and a linear mixed model with random intercepts. Results largely replicated previously reported item severity rankings across both samples: GD criteria such as loss chasing and a preoccupation with gambling were generally linked to lower severity levels, whereas criteria such as withdrawal symptoms or job/family problems where generally linked to higher severity levels. Modelling revealed a reduced assessment sensitivity in lower gambling severity ranges. Furthermore, person fit analyses suggest that atypical symptom patterns may be linked to poorer mental health (MHI-5). Implications for the interpretability of total scores of endorsed criteria and the validity of diagnostic practices determining eligibility for treatment and financial compensation are discussed.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · IRT secondary analysis of German population surveys using DSM-5 criteria; unclear whether sports betting participation is reported by PG status.

**Решение:** =

---

### 212 · R1239

**The Social and Economic Impacts of Casinos in Massachusetts and Implications for Other Jurisdictions**

2026 · Digital Scholarship - UNLV (University of Nevada Reno) · conference-paper

After casino gambling was legalized in Massachusetts in 2011, the Social and Economic Impacts of Gambling in Massachusetts (SEIGMA) study was launched to investigate the impacts of casinos in the state. Extensive social and economic data was collected prior to and after the opening of the new casinos to identify the impacts of their introduction. The study also allowed for consideration of the impacts of COVID-19 and the legalization of sports betting in Massachusetts on gambling behavior and gambling problems in the Commonwealth. The presentation will focus on the impacts identified through 2024 in three areas, including overall impacts, social and health impacts, and economic and fiscal impacts. Particular attention will be paid to notable differences in the impacts of the casinos in three distinct markets in urban and suburban areas of the state. The findings have particular relevance for the pending introduction of casino gambling at three locations in New York City, anticipated between 2026 and 2030.

**ИИ:** ? · обе модели · опрос населения об азартных играх · Conference presentation of SEIGMA findings; population surveys likely measured sports betting and problem gambling, but the data reported here are unclear.

**Решение:** =

---

### 213 · R1240

**Gambling Prevalence, Determinants and Association with Anti-Retroviral Therapy Adherence Among Adolescents Living with HIV in Abuja**

2026 · AIJR Abstracts · article · eng · https://abstracts.aijr.org/index.php/index/article/view/665

Background: Gambling, classified as a behavioural addiction in DSM-5, poses a public health challenge among adolescents, particularly those living with HIV (ALHIV), where it intersects with mental health disorders, substance use, and barriers to antiretroviral therapy (ART) adherence. In sub-Saharan Africa, where adolescent HIV prevalence remains high (approximately 1.01 million aged 15-19 years globally per UNICEF 2023), limited data exist on gambling’s prevalence, determinants, and impact on ART outcomes in urban ALHIV cohorts. This study addresses this gap by examining gambling patterns and their association with ART adherence in Abuja, Nigeria. Methods: A cross-sectional study was conducted from August to September 2025 among 140 ALHIV (aged 10-19 years) accessing care at purposively selected secondary and tertiary facilities in the Federal Capital Territory. Multistage sampling (purposive area council selection, random facility balloting, consecutive enrolment) yielded a sample adjusted for 10% non-response. Data were collected via interviewer-administered semi-structured questionnaires incorporating the Problem Gambling Severity Index (PGSI), Patient Health Questionnaire-9 (PHQ-9)/Generalized Anxiety Disorder-7 (GAD-7), AUDIT-C, and self-reported adherence (≥95% doses in past 30 days). Bivariate (χ²/Fisher’s exact) and multivariate logistic regression analyses were performed using SPSS v27, with p&lt;0.05 denoting significance. Results: Gambling prevalence was 32.1%, with 48.8% at moderate-to-high PGSI risk; sports betting (15.7%) and online gambling (12.9%) predominated. Bivariate analyses linked gambling to alcohol use (χ²=10.607, p=0.003) and smoking (χ²=5.232, p=0.037); multivariate regression confirmed alcohol as a determinant (adjusted OR=0.275, 95% CI: 0.071-1.056, p=0.034 for non-use vs. hazardous). Sociodemographic showed no associations. ART adherence was suboptimal (40.7% good), but no significant link emerged with gambling status (χ²=0.731, p=0.463) or PGSI category (χ²=3.690, p=0.282). Conclusion: Elevated gambling prevalence among urban ALHIV underscores modifiable risks like substance use, yet without direct ART adherence disruption. Integrated screening (PGSI/AUDIT-C) in HIV clinics is recommended to achieve UNAIDS 95-95-95 targets and SDG 3, with longitudinal studies needed for causality. &nbsp;

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Survey of adolescents with HIV that measured sports betting participation and PGSI; problem gambling among sports bettors may be reported.

**Решение:** =

---

### 214 · R1241

**The Silent Epidemic: Early-Onset Ludopathy in Children and the Invisible Digital Threat**

2026 · The Journal of Pediatrics · article · en · https://doi.org/10.1016/j.jpeds.2026.114987

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -1 (обзор, комментарий, теоретическая, правовая или регуляторная работа: No abstract; the rhetorical title in a pediatrics journal suggests a commentary or letter, with no sign of survey data or sports betting.); Sonnet ? (нет аннотации: No abstract; title on child gambling in a pediatrics journal looks like a commentary but could be a data-bearing study.)

**Решение:** -

---

### 215 · R1244

**More Than a Bad Bet: Problem Gambling, Emotional Reactivity, and Athlete Cyberbullying Among Sports Bettors**

2026 · Research Square · preprint, posted-content · https://doi.org/10.21203/rs.3.rs-10733136/v1

Abstract Background The rapid expansion of legal sports betting in the United States since Murphy v. National Collegiate Athletic Association has coincided with a documented rise in online harassment of athletes, yet research has focused almost exclusively on athletes as victims rather than on bettors as perpetrators. Objective This study examined individual-level predictors of athlete cyberbullying (ACB) among sports bettors. Methods A survey of 1,013 U.S. sports bettors using a survey. Participants reported mood reactivity to betting outcomes, gambling-related harm, typical wager amount, age, and the frequency of seven cyberbullying behaviors directed at athletes and coaches. Logistic regression models predict any ACB and high-frequency ACB (several times weekly or more). Results More than half of respondents (57.0%) endorsed at least one cyberbullying behavior, and 35.7% reported at least one at high frequency. Supporting the hypothesis that mood reactivity independently predicted ACB. Odds increased steadily for the high frequency of ACB outcome with increased mood reactivity. Self-reported problem gambling more than tripled the adjusted odds of any ACB and showed a stronger association with high-frequency ACB. Larger wagers and younger age also predicted ACB. Mood reactivity did not moderate the problem-gambling association, indicating that the two operate as parallel rather than interacting pathways. Conclusions Gambling related harm extends beyond bettors and families to athletes and sport communities. Because the two risk pathways are additive rather than interacting, either can be addressed independently. Social work assessment of problem gambling should incorporate items on emotional reactivity to losses and post-loss online behavior.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of 1,013 US sports bettors measuring 'self-reported problem gambling' and gambling harm; unclear whether a validated instrument such as the PGSI was used.

**Решение:** =

---

### 216 · R1246

**Suicidal ideation among people with different gambling behaviour profiles: analysis of a longitudinal survey of people who gamble regularly in the UK.**

2026 · BJPsych open · journal article, journalarticle, review · eng · https://doi.org/10.1192/bjo.2025.10935

BACKGROUND: People who gamble experience elevated rates of suicidal thoughts and behaviours. Longitudinal studies have been scarce, and none has focused on those who regularly gamble in the UK. AIMS: To examine the relationship between specific products and locations of gambling activity (and their combinations) and risk of subsequent suicidal thoughts. METHOD: We analysed a UK longitudinal survey of 3927 adults (18 years old or over) who regularly bet on sports. Data were collected online between June and November 2020. Latent class analysis was used to identify groups of people with similar gambling profiles on the basis of 13 types of gambling activity. Weighted group characteristics are presented. Regression modelling was used to test associations between gambling groups and suicidal thoughts, adjusting for baseline characteristics. RESULTS: Five distinct groups were identified. One group (5.6% of the sample) reported multiple types of both in-person and online gambling. This group was the most likely to use electronic gambling machines. After adjustment for baseline suicidal thoughts, this group had significantly higher odds of subsequent suicidal thoughts (adjusted odds ratio 3.42; 95% CI: 1.18-9.89) than other groups. CONCLUSIONS: Although many profiles of gambling activity present suicide risk, some types present greater risk. National Institute for Health and Care Excellence guidelines recommend enquiry in primary care settings about gambling behaviours. Our findings suggest that clinicians should consider asking questions on mode (online or in-person) and product (especially electronic gambling machines) to identify those at heightened risk of suicidal ideation. Gambling should also be considered routinely in psychosocial assessments across clinical settings and incorporated into suicide prevention campaigns.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · UK longitudinal survey of 3927 regular sports bettors; the abstract doesn't name a PG instrument, but this cohort likely collected PGSI.

**Решение:** =

---

### 217 · R1258

**Objective Performance, Subjective Appraisal, and Mood Across a Fantasy Premier League Season: A 38-Wave Longitudinal Study**

2026 · SSRN Electronic Journal · preprint · https://doi.org/10.2139/ssrn.7532302

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: No abstract; FPL longitudinal mood study, likely free-to-play and no PG instrument, but cannot confirm without full text.); Sonnet -6 (не про азартные игры или «ставка/лотерея» в другом смысле: Free-to-play Fantasy Premier League study of performance, appraisal and mood; no indication of gambling or problem-gambling measurement, and no abstract.)

**Решение:** -

---

### 218 · R1259

**Canadian provincial channelization of online gambling in 2025: a cross-provincial analysis of player and revenue channelization**

2026 · International Gambling Studies · article · en · https://doi.org/10.1080/14459795.2026.2708668

There are widespread claims that most online gambling in Canada occurs on unsanctioned out-of-country sites rather than on provincial government platforms. However, these claims rely on black-box proprietary modeling and surveys with important sampling and measurement limitations. This study provides the first academic investigation of this issue and the first cross-provincial assessment of online gambling channelization in Canada. Player channelization was estimated in two ways: by comparing active registered players on provincial platforms in fiscal year 2024/25 with the number of past-year online gamblers in each province from the 2025 Rapid Response Gambling Module of the Canadian Community Health Survey (CCHS), and through a weighted national online panel survey of 12,970 adults that assessed patronization by gambling format. Expenditure channelization was also estimated from weighted self-reported spending in the panel survey. Results showed strong rank-order agreement across methods, with relatively high channelization in Quebec, Ontario, British Columbia, and the Atlantic Provinces, and lower channelization in Alberta and Saskatchewan. Channelization was highest for lotteries, instant lotteries, and bingo, and lowest for casino table games, sports betting, and other niche online gambling formats. Overall, channelization varied by province and gambling format and was higher in some provinces than prior estimates have suggested.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · National panel survey (n=12,970) measured online sports betting by format; abstract doesn't say if a problem-gambling instrument was used.

**Решение:** =

---

### 219 · R1263

**The relationship between executive functions, decision-making, and changes in symptoms of gambling disorder in online sports bettors.**

2026 · Scientific reports · article, journal article, journalarticle · eng · https://doi.org/10.1038/s41598-026-48449-8

Deficits in executive functions (EFs) and impulsive decision-making are well-established cognitive mechanisms underlying gambling disorder (GD), though there are some inconsistent findings. This study investigated the relationship between changes in GD symptoms in online sports bettors and specific EFs as well as decision-making processes over time. A subsample of online sports bettors (n = 54, mean age = 33, 96% male) from a larger study underwent an in-person assessment. Initial GD symptom severity was measured online according to DSM-5 criteria and was low to mild in most participants. All other assessments took place an average of 443 days later, during the in-person assessment. We analyzed cross-sectional and longitudinal associations between three facets of EFs (response inhibition, cognitive flexibility, and working memory) and four decision-making facets (delay discounting, probability discounting for gains and losses, and loss aversion) and GD symptom severity and changes over time. Cross-sectional results showed that higher GD symptom severity was associated with poorer working memory and reduced loss aversion. Reduced loss aversion was also associated with greater symptom increase over time. However, these associations were not statistically significant after correction for multiple testing, so they should be interpreted with caution. No other significant relationships were found. These findings provide preliminary evidence that reduced loss aversion is one cognitive factor in disordered gambling among online sports bettors, a population with heterogeneous profiles of EFs and decision-making. Further longitudinal studies are needed to clarify the role of specific cognitive processes in the development and progression of GD to better inform treatment strategies. Supplementary Information The online version contains supplementary material available at 10.1038/s41598-026-48449-8.

**ИИ:** + · обе модели · беттеры + инструмент · Sample of online sports bettors with DSM-5 gambling disorder symptoms measured; could report how many met the GD case definition.

**Решение:** =

---

### 220 · R1269

**Classification-Behavior Discordance and Problem Gambling: Differential Patterns for Fantasy Sports and Loot Boxes Among College Students.**

2026 · Journal of gambling studies · journal article, journalarticle, review · eng · https://doi.org/10.1007/s10899-026-10549-5

Fantasy sports and loot boxes share similarities with gambling yet remain largely unregulated as such, creating ambiguity in how individuals perceive and engage with these activities. While participation in both activities has been linked to problem gambling, whether individuals' classification of these activities as gambling is associated with differential risk has not been examined. This study introduces the concept of classification-behavior discordance, defined as the misalignment between how an individual classifies an activity and whether they participate in it. Using data from an online survey of 4,016 college students enrolled at public colleges and universities in Nevada, United States, we constructed four discordance groups for each activity based on the intersection of classification and participation: non-participants, aware participants, unaware participants, and non-participating classifiers. We conducted separate binary logistic regression models for fantasy sports and loot boxes to examine associations between discordance group membership and problem gambling. Results revealed divergent patterns across activities. For loot boxes, classifying the activity as gambling was associated with significantly elevated problem gambling risk among participants, whereas for fantasy sports, participating without classifying the activity as gambling was associated with significantly lower risk. These findings highlight the importance of considering individuals' subjective classification of gambling-like activities in problem gambling screening, prevention, and regulatory efforts.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Survey of 4,016 college students measuring fantasy sports participation and problem gambling; could report problem gambling among fantasy sports participants.

**Решение:** =

---

### 221 · R1270

**Religiosity and Online Gambling Addiction: A Serial Mediation Model of Perceived Social Support and Life Satisfaction within the Framework of Conservation of Resources Theory**

2026 · Journal of Gambling Studies · article · en · https://doi.org/10.1007/s10899-026-10531-1

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; likely a survey of online gamblers measuring addiction, possibly including sports bettors.

**Решение:** =

---

### 222 · R1275

**Scale development: betting in sport**

2026 · Edward Elgar Publishing eBooks · book-chapter · https://doi.org/10.4337/9781035317226.00023

Scale development is widely used for systematically measuring individuals’ attitudes and behaviors. Scale development focuses on constructing psychometric instruments that ensure valid and reliable measurement of specific constructs. This chapter details the scale development procedure, followed by a case study demonstrating its application in identifying the motivations behind sports betting. Sports betting is considered a motivated behavior, and understanding the underlying drivers behind this behavior is crucial for sports management. The case study focuses on developing a valid and reliable measurement tool to assess how sports betting motivations influence consumer engagement and industry practices. As a result of the survey, seven core motivational dimensions emerged from the data analysis: Make Money, Fun, Socialization, Recreation-Escape, Knowledge of the Game, Interest in Sports, and Being in the Game. These findings provide valuable insights into the broader implications of sports betting motivations for stakeholders in sports management. The developed scale offers practical applications for industry professionals, regulatory bodies, and researchers, supporting the design of responsible gambling policies and effective consumer engagement strategies. The chapter concludes with recommendations for future research, emphasizing the potential for extending the scale's application to diverse populations and settings and further examining its impact on sports-related consumer behavior.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Survey of sports bettors developing a motivation scale; the abstract doesn't say whether a problem-gambling screen like the PGSI was used for validation.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Chapter develops a sports betting motivation scale from a survey; no problem-gambling instrument is mentioned, only motives.)

**Решение:** ?

---

### 223 · R1276

**Stressful Life Events, Masculinity and Gambling Participation: An Age-Stratified Analysis of Australian Men**

2026 · Journal of Gambling Studies · article · en · https://doi.org/10.1007/s10899-026-10506-2

Gambling participation varies across genders and throughout the life course, yet little research has examined how stressful life events and masculinity-related factors influence gambling behaviour across different stages of adulthood among men. Using Wave 4 data from Ten to Men: The Australian Longitudinal Study on Male Health (n = 5,434), this study investigates age-stratified associations between stressful life events, self-perceived masculinity, masculinity strain and gambling frequency among Australian men. Negative binomial regression analysis reveals that masculinity and masculinity strain predict higher gambling frequency only among young men, highlighting the salience of masculine identity during early adulthood. Stressful life events also showed age-specific effects: job loss is associated with lower frequency of gambling among young men, while bereavement of loved ones is linked to higher gambling among middle-aged men. No stressful life events correlated with gambling among older men. Across all age groups, higher income was associated with more frequent gambling, while possessing a university degree was associated with less frequent gambling among those aged 30 and above only. These findings accentuate the importance of a life course perspective for understanding gambling participation and informing age-tailored interventions.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Population cohort of Australian men; abstract reports only gambling frequency. The full text may include PGSI and gambling-activity data, including sports betting.

**Решение:** =

---

### 224 · R1286

**GAMBLING INVOLVEMENT, HOPELESSNESS, AND SUICIDE-RELATED INDICATORS IN TURKİYE: A CROSS-SECTIONAL ONLINE SURVEY**

2026 · Kocaeli Üniversitesi Sağlık Bilimleri Dergisi · article · en · https://doi.org/10.30934/kusbed.2013046

ABSTRACT Objective: We aimed to estimate gambling participation and positive screening for probable gambling disorder and to examine their associations with hopelessness and suicide-related outcomes in a Turkish online sample. Methods: In this cross-sectional web-based survey, 1,057 adults completed the South Oaks Gambling Screen (SOGS), Beck Hopelessness Scale (BHS), and Suicide Probability Scale (SPS). Group differences were examined using non-parametric tests, followed by multivariable regression analyses. Results: Gambling participation was reported by 30.7% (95% CI 28.0–33.6) of participants; 4.9% (95% CI 3.8–6.4) screened positive for probable gambling disorder using the Turkish SOGS cut-off of ≥8. Participants reporting gambling had higher BHS and SPS scores, and differences were more pronounced among those screening positive for probable gambling disorder. The between-group difference in SPS scores among participants reporting gambling corresponded to a moderate-to-large effect (r=0.497, 95% CI 0.343–0.653). After covariate adjustment, gambling participation was associated with a 1.46-point higher BHS (95% CI 0.79–2.13) and 5.26-point higher SPS scores (95% CI 3.15–7.36). Among participants reporting gambling, positive screening was associated with 2.60-point higher BHS (95% CI 0.88–4.32) and 12.59-point higher SPS scores (95% CI 7.21–17.96). Gambling participation was also associated with histories of suicidal ideation (OR=1.71, 95% CI 1.17–2.50) and suicide attempt (OR=2.54, 95% CI 1.32–4.88). Conclusions: Gambling involvement, particularly positive SOGS screening, was associated with greater hopelessness and suicide-related symptom burden. The cross-sectional design and non-probability sampling preclude causal interpretation and population-level prevalence estimates.

**ИИ:** разошлись — Opus ? (неясно, есть ли ставки на спорт: Turkish adult online survey using SOGS; sports betting (e.g., Iddaa) is likely but the abstract doesn't report gambling activities.); Sonnet + (опрос населения об азартных играх: Online survey of 1,057 Turkish adults using SOGS; gambling participation measured, so activity-level (possibly sports betting) problem gambling data may appear in the full text.)

**Решение:** ?

---

### 225 · R1287

**Gambling in Sports: Validity and Reliability Study of the Gambling Passion Scale**

2026 · DergiPark (Istanbul University) · article · en

Bu araştırmanın amacı, Rousseau ve arkadaşları (2002) tarafından geliştirilen “Bahis Tutkusu Ölçeği”nin Türk kültürüne uyarlanması, geçerlik ve güvenirlik analizlerinin gerçekleştirilmesidir. Araştırma, nicel araştırma desenlerinden tarama modeliyle yürütülmüştür. Uyarlama süreci literatürde önerilen beş aşamalı çeviri modeline göre gerçekleştirilmiştir: hedef dile çeviri, geri çeviri, uzman görüşü alınması, pilot uygulama ve geçerlik–güvenirlik analizleri. Araştırma grubu, 18–35 yaş aralığında yer alan ve aktif olarak spor bahsi oynayan toplam 344 katılımcıdan oluşmuştur (AFA=166; DFA=178). Elde edilen verilere ilişkin Açımlayıcı Faktör Analizi (AFA) sonucunda ölçeğin iki faktörlü (Obsesif Tutku ve Uyumlu Tutku) bir yapıya sahip olduğu ve toplam varyansın %63.9’unu açıkladığı belirlenmiştir (KMO=0.92; Bartlett χ²=801.495; p<0.001). Faktör yükleri 0.53 ile 0.92 arasında, Cronbach Alfa katsayıları 0.85–0.90, Omega güvenirlik katsayısı ise 0.90 olarak tespit edilmiştir. Doğrulayıcı Faktör Analizi (DFA) sonuçlarına göre uyum iyiliği indeksleri kabul edilebilir düzeydedir (χ²/sd=1.76; RMSEA=0.066; CFI=0.981; SRMR=0.292). Ayrıca yapı geçerliğini destekleyen CR (0.87–0.93) ve AVE (0.58–0.73) değerleri, ölçeğin birleşim ve ayrışım geçerliğini doğrulamaktadır. Bulgular, Türkçe Bahis Tutkusu Ölçeği’nin, bireylerin bahis tutkusu düzeylerini değerlendirmede geçerli ve güvenilir bir ölçme aracı olduğunu göstermektedir.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Turkish validation of a gambling passion scale in 344 active sports bettors; a PG screen may have been used for criterion validity, but the abstract doesn't say.

**Решение:** =

---

### 226 · R1288

**Gambling Involvement and Problem Gambling: Finding from a General Population Survey**

2026 · Digital Scholarship - UNLV (University of Nevada Reno) · conference-paper

Certain gambling formats, such as slot machines, have consistently been related to problem gambling. Extensive involvement in multiple gambling activities may also represent an important risk factor. This study explored the relationship between gambling involvement, gambling formats, and problem gambling in a subsample of 817 participants who reported engaging in gambling in the past month, drawn from a representative sample of Croatian residents aged 15-64 (N=4,988), Gambling involvement was assessed by the number of gambling formats and frequency of gambling in the past month, while problem gambling was assessed using the Problem Gambling Severity Index. Most participants (37.3%) engaged in one, 26.8% in two, 21.4% in three, and 14.5% in four or more gambling formats. Overall, 67.4% of participants were classified as non-problem, 10.1% as low-risk, 14.0% as moderate-risk, and 8.5% as participants with problem gambling. High gambling involvement was related to problem gambling, and frequent sports betting, casino games, and slot machines use. Participants with problem gambling most commonly engaged in four or more gambling formats. Findings suggest problem gambling is related not only to specific gambling formats but also to patterns of extensive and frequent involvement in multiple gambling activities, highlighting the importance of monitoring overall gambling behavior rather than focusing on specific games to identify high-risk individuals and inform prevention efforts.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Croatian population survey subsample of gamblers; PGSI measured and linked to frequent sports betting among other formats.

**Решение:** =

---

### 227 · R1295

**경륜(競輪) 고객의 심리 요인이 베팅 행동에 미치는 영향: 행동경제학 관점에서**

2026 · 한국체육학회지 · article · en · https://doi.org/10.23949/kjpe.2026.3.65.2.43

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Survey of keirin (cycle-race) bettors on psychological factors; no abstract, so unclear whether a problem-gambling instrument was used.

**Решение:** =

---

### 228 · R1296

**An Analysis of the Importance and Priority of Match Reference Factors in Football Sports Toto Decision-Making**

2026 · The Korea Journal of Sport · article · https://doi.org/10.46669/kss.2026.24.2.005

본 연구는 축구 스포츠토토 의사결정에서 경기 참고요인의 중요도와 우선순위를 분석하고, 참여자 특성에 따라 이러한 인식 구조가 어떻게 달라지는지를 확인하는 데 목적이 있다. 연구대상은 최근 1년 이내 축구 스포츠토토 구매 경험이 있는 성인 400명이었으며, 자료는 설문조사를 통해 수집하였다. 설문 문항은 축구 경기 결과 판단과 스포츠토토 의사 결정 과정에서 반복적으로 활용되는 경기 참고요인을 중심으로 구성하였다. 구체적으로 팀 시장가치, 팀 명성·인지도, 시즌 순위·승점, 최근 5경기 성적, 홈/원정 조건, 주전 선수의 부상 및 결장 정보, 일정 혼잡도·휴식일 차이, 최근 상대전적, 아시안핸디캡 개장정보, 유럽배당 개장정보 등 10개 요인의 중요도를 평정하도록 하였고, 실제 의사결정에서 우선적으로 고려하는 요인을 1~3순위로 선택하도록 하였다. 수집된 자료는 SPSS 통계프로그램을 활용하여 빈도분석, 기술통계 분석, Friedman 검정, 우선순위 분석 및 주요 하위집단 비교분석을 실시하였다. 분석 결과, 중요도 평균은 주전 선수 부상·결장 정보가 가장 높았고, 최근 5경기 성적, 일정 혼잡도·휴식일 차이, 아시안핸디캡 개장정보, 유럽배당 개장정보순으로 나타났다. 우선순위 분석에서는 최근 5경기 성적, 주전 선수 부상·결장 정보, 일정 혼잡도·휴식일 차이가 핵심 판단요인으로 확인되었다. 또한 구매경력과 배당 이해도가 높은 고경험·고배당이해 집단은 최근 경기 성적, 일정 관련 정보 및 배당정보를 상대적으로 더 중시하는 경향이 나타난 반면, 저경험·저배당이해 집단은 팀 시장가치와 팀 명성·인지도를 상대적으로 더 중요하게 평가하는 경향이 나타났다. 이러한 결과는 축구 스포츠토토 참여자의 경기 참고요인 인식이 단일한 구조가 아니라 참여 경험과 시장정보 이해 수준에 따라 달라질 수 있음을 시사한다.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Survey of 400 football Sports Toto bettors on decision factors; abstract doesn't mention a problem-gambling instrument, but the sample table might include one.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Survey of 400 football sports toto buyers on importance of match reference factors; no problem-gambling instrument mentioned.)

**Решение:** -

---

### 229 · R1297

**한국 스포츠토토 시장의 종목별 비교를 중심으로**

2026 · Seoul National University Open Repository (Seoul National University) · dissertation · ko

학위논문(석사) -- 서울대학교 대학원 : 사범대학 체육교육과(글로벌스포츠매니지먼트전공), 2026. 2. 김기한.

**ИИ:** ? · обе модели · нет аннотации · Korean Sports Toto master's thesis comparing sports within the market; no abstract. Probably a market analysis, but a bettor survey can't be ruled out.

**Решение:** =

---

### 230 · R1301

**Factors Associated with Gambling Behaviors After Legalization of Online Sports Wagering and Fantasy Sports**

2025 · Journal of Gambling Issues · article, journalarticle, journal-article · und · https://doi.org/10.4309/dtnz3060

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; title suggests a survey of gambling behaviour after online sports wagering and DFS were legalized, which may have used a PG instrument.

**Решение:** =

---

### 231 · R1307

**The Hidden Harms of Convenience: The Impact of Credit Card-Funded Online Sports Betting Through Hard Rock Bet in Florida**

2025 · Journal of Gambling Issues · article, journalarticle, journal-article · und · https://doi.org/10.4309/ambl9794

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; online sports betting harms in Florida could be a bettor survey or a policy paper.

**Решение:** =

---

### 232 · R1365

**Sports Betting Behaviour among Flemish Youth: A Dual Perspective of the Reasoned Action Approach and the Self-Determination Theory**

2025 · Lirias · article

status: Published

**ИИ:** ? · обе модели · нет аннотации · No abstract; youth sports betting survey framed by behavioural theories. A problem-gambling instrument may have been included.

**Решение:** =

---

### 233 · R1369

**Online Gambling and Its Prevalence Among Nigerian Medical and Dental Students.**

2025 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-025-10393-z

With a global rise in online gambling platforms, medical undergraduates are increasingly engaging themselves in gambling as a means of surviving and escaping challenges peculiar to their course of study. The objective of this research was to determine online gambling prevalence among Nigerian medical (MBBS) and dental (BDS) students to gain knowledge and understanding of the factors influencing this behavior. A cross-sectional study design was employed using the South Oaks Gambling Screen (SOGS), which recruited medical and dental students from selected medical and dental schools involving all geo-political zones in Nigeria. Descriptive analysis was carried out on the socio-demographic factors, Binary Logistic Regression analysis was done between the various factors affecting online gambling. A total of 403 students from 12 universities completed the study. All analyses were done with statistical significance set at p 2 = 57.79, p 2 = 20.77, p 2 = 40.49, p z = 0.05, 0.226, 0.004, in respect to reference age 16-20), males (p > z = 0), source of income, Parents/Family, Loans, Scholarships, Government, or third party organizations (p > z = 0.107, 0.164, 0.208), course of study MBBS (p > z = 0.031) respectively. This study found that online gambling is present among Nigerian medical and dental students, with associations observed between gambling behavior and factors such as age, gender, financial dependency, and family history of gambling. Sports betting was the most common form of gambling reported. While most students gambled with relatively small amounts, about 10% of respondents exhibited behaviors consistent with a possible gambling disorder. Awareness of the ills of this habit needs to be heightened and more research is needed on the psychological and physical effects in our population.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Student survey using the SOGS; sports betting was the most common form of gambling, so full text may give problem-gambling rates among bettors.

**Решение:** =

---

### 234 · R1370

**Empirical Analysis of the Socio-Economic Influence of Sports Betting on Academic Performance of Students in Nigerian Tertiary Institutions**

2025 · Faculty of Natural and Applied Sciences Journal of Scientific Innovations · article, journalarticle, review · en · https://doi.org/10.63561/fnas-jsi.v6i3.958

The study investigated the socio economic and psychological drivers behind the effect of sport betting on academic performance in tertiary institution using descriptive analysis and multinomial logistic regression model. Descriptive survey design was adopted utilizing simple random sampling method in choosing students from the targeted population. The study's findings revealed that academic performance was affected significantly by demographic statistics (age and sex), influence of loss of dignity, peer influence, hobby, immoral act and unnecessary additions. Additionally, there was no significant effect of religious belief and entertainment towards sport betting influencing academic performance among tertiary institutions student. Consequently, suggestions on how to mitigate identified significant predictors that influence academic performance of students via sport betting and strategies for interventions to reduce the mayhems in educational institutions were given.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of Nigerian students about sports betting and academic performance; no problem-gambling instrument mentioned, but one may have been used.

**Решение:** =

---

### 235 · R1373

**Ipsos Sports Betting Poll**

2025 · Roper Center for Public Opinion Research iPOLL · other/study, other · https://doi.org/10.25940/roper-31123249

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Opinion poll on sports betting with no abstract; unclear whether a problem-gambling instrument was used.

**Решение:** =

---

### 236 · R1375

**A influência do marketing das casas de apostas no comportamento dos estudantes da UEMG Carangola**

2025 · Contribuciones a las Ciencias Sociales · article, journal-article · pt · https://doi.org/10.55905/revconv.18n.1-219

O presente estudo teve como objetivo explorar como as estratégias de marketing de empresas de apostas esportivas exercem influência direta ou indireta no comportamento dos estudantes da UEMG Carangola. Buscou-se analisar a crescente influência das plataformas de apostas esportivas, com foco nas estratégias de patrocínio e publicidade direcionadas às instituições de ensino superior, visando compreender os benefícios financeiros, como o financiamento de programas esportivos, bem como os riscos associados, incluindo o aumento do comportamento problemático de jogo entre os estudantes, com potenciais impactos negativos em seu desempenho acadêmico e bem-estar. A base teórica incluiu uma revisão sobre estratégias de marketing, marketing esportivo e a evolução e impacto das apostas esportivas. Com uma abordagem quantitativa, através de métodos estatísticos, foi possível analisar a percepção e o comportamento de 111 estudantes em relação às campanhas de marketing das casas de apostas. Após a apuração dos dados, a pesquisa forneceu insights relevantes e aplicáveis como proposta de elaboração de políticas públicas e estratégias de marketing mais responsáveis e eficazes, considerando tanto os interesses financeiros das atléticas universitárias, quanto a saúde e bem-estar dos estudantes. Em síntese, o estudo proporcionou uma análise aprofundada das complexas interações entre o marketing das apostas esportivas e o ambiente universitário, destacando a importância de equilibrar os benefícios econômicos com estratégias eficazes para mitigar os riscos envolvidos.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Quantitative survey of 111 students on sports betting marketing; mentions problem gambling risk but no screening instrument is stated.

**Решение:** =

---

### 237 · R1379

**Socio-Economic Determinants of Higher Learning Institution (HLIs) Students’ Betting Behavior in Tanzania**

2025 · Tanzania Journal of Community Development · article, journalarticle · und · https://doi.org/10.4314/tajocode.v4i2.12

Sports betting is increasingly common among (HLIs) students, driven by personal traits, access to technology, and unemployment pressures. However, little is known about the socioeconomic determinants of this behavior in Tanzanian Higher Learning Institutions (HLIs). This study examined such factors using a cross-sectional design, collecting quantitative data from 2,857 students across six Tanzania Institute of Accountancy (TIA) campuses through simple random sampling. The qualitative phase of data collection involved 8 Key Informant Interviews (KIIs) and 6 Focus Group Discussions (FGDs), with six to eight participants considered knowledgeable about sports betting. Quantitative data were analyzed descriptively, with logistic regression for quantitative variables, while qualitative data were analyzed using thematic analysis. Results showed that out of 10 variables, 5, namely age, sex, personal factors, unemployment, and technological factors, were statistically significant (p&lt;0.05). FGDs and KIIs results revealed that peer pressure, easy access to online betting platforms, and financial incentives are the strongest motivators for sports betting. The study recommends that HLIs integrate financial literacy modules into their curricula to help students manage their finances responsibly and understand the risks of gambling. Also, the Ministry of Youth Development should implement and enforce regulations, such as age restrictions and spending limits on mobile money and betting platforms. HLI's counseling units should provide readily available counselling services for students experiencing gambling-related problems.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Large student survey on sports betting determinants; abstract doesn't say whether a problem-gambling instrument was used.

**Решение:** =

---

### 238 · R1382

**Sports Gambling and the Battle with Mental Health**

2025 · Murray State's Digital Commons (Murray State University) · article

This research paper is about how sports gambling can lead to other serious mental health issues.

**ИИ:** ? · обе модели · другое · A minimal abstract of a student paper on sports gambling and mental health; it's unclear whether it's empirical or used a problem-gambling instrument.

**Решение:** =

---

### 239 · R1398

**Exploratory Study on How Substance Use Affects Gambling and Spending Among Students**

2025 · Preprints.org · article, preprint · en · https://doi.org/10.20944/preprints202506.2133.v1

This research examines the connection between gambling behavior and substance use among youths, with special interest regarding gender difference and the cost of gambling. With a representative sample of 700 high school students aged between ages of 14 and 18 years, the research utilized structured questionnaires to collect information. Respondents indicated their participation on gambling, ranging from slot and scratch cards to internet gambling and sports betting, and their use of psychoactive drugs. Analysis identifies a strong, statistically significant connection between gambling and use of substances, particularly among respondents who use slot gambling or sport betting. For the entire sample, 19.7% gambled and 24% took substances. Use of substances, particularly psychoactive drugs and tobacco use, were much more prevalent among gamblers compared with non-gamblers, and an associated pattern, particularly among males, unveiled much more salient features. Log odds ratio and Fisher’s exact test analysis uncovered much elevated probabilities of use of substances among gamblers, particularly among slot machine users, with odds ratios higher than 2.0 among some female subgroups. Nevertheless, internet gambling could not demonstrate strong associations with use of substances, but there revealed an evident modest positive connection among men users. Data on expenditure unveiled the majority of young persons pay less than €10 monthly on gambling, but there exists a small group with much elevated expenditure. These respondents accounted for the size of the right-skewed distribution and may demonstrate burgeoning signs of harmful gambling. Prevention and detection are highlighted with special interest regarding gender-specific behavior. Recommendations are combined, integrated prevention among young persons within schools and communities, especially regarding gambling and use of substances during youth.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Student survey measured sports betting participation; no problem-gambling instrument is named, only expenditure, so needs full-text check.

**Решение:** =

---

### 240 · R1403

**AVERSÃO À PERDA E COMPORTAMENTO FINANCEIRO NAS APOSTAS ONLINE: UM ESTUDO COM A POPULAÇÃO DE CUIABÁ-MT LOSS AVERSION AND FINANCIAL BEHAVIOR IN ONLINE BETTING: A STUDY WITH THE POPULATION OF CUIABÁ, MT**

2025 · Caderno de Administração · journal-article · https://doi.org/10.23925/2595-4865.2025v1n19.72992

O objetivo geral desta pesquisa é analisar o perfil dos apostadores do município de Cuiabá-MT e sua aversão à perda. A coleta de dados foi realizada por meio da aplicação de questionários estruturados, na qual obteve-se 135 respostas. Os resultados evidenciam que a maioria dos participantes realiza apostas com alta frequência, muitas vezes motivada pela expectativa de ganhos rápidos, em contraste com os investimentos tradicionais. Além disso, identificou-se a presença de vieses como a aversão à perda, em que os indivíduos demonstram maior sensibilidade às perdas, o que pode indicar um comportamento impulsivo do ponto de vista financeiro.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Questionnaire survey of 135 online bettors in Cuiabá on loss aversion; the abstract doesn't say whether a problem-gambling instrument was used.

**Решение:** =

---

### 241 · R1405

**Modeling the Impact of Sports Betting on Mathematics Performance Among Pre-Service Teachers in a Ghanaian College of Education**

2025 · International Journal of Research and Innovation in Social Science · article, journalarticle, journal-article · en · https://doi.org/10.47772/ijriss.2025.906000441

Male college students are increasingly engaging in sports betting, which has led to serious worries about how it can affect their academic performance, especially in mathematics. A mixed-method research design was used in this study to examine how sports betting affected Mampong College of Education students' mathematical competency. The study included 200 male students as a purposive sample. Focus groups and semi-structured interviews were used to acquire qualitative insights, while structured questionnaires and academic records were used to collect quantitative data. Additionally, a differential equation model that included variables like betting frequency, financial stress, and cognitive overload was created to depict the pace of change in students' mathematics performance. Sports betting and math proficiency were found to be significantly correlated negatively, according to quantitative data. This conclusion was corroborated by qualitative data, which revealed important issues such as diminished study time, peer pressure, academic distraction, and emotional suffering. The model's simulation output showed that higher betting activity was linked to a decline in performance. In order to lessen the negative academic effects of sports betting, the study suggests focused awareness efforts, institutional policy enforcement, and the creation of student support services.

**ИИ:** разошлись — Opus -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Mixed-methods student survey on sports betting and maths performance; measures are betting frequency, financial stress and cognitive load, with no problem-gambling instrument.); Sonnet ? (неясно, измеряли ли проблемную игру: Questionnaire survey of male students on sports betting and maths performance; abstract doesn't say whether a problem-gambling instrument was used, so full text is needed.)

**Решение:** ?

---

### 242 · R1408

**Measurement invariance of the Problem Gambling Severity Index across sociodemographics and gambling modalities**

2025 · International Gambling Studies · journalarticle, review, article · en · https://doi.org/10.1080/14459795.2025.2529177

ABSTRACT The Problem Gambling Severity Index (PGSI) has been extensively used to identify the severity of problematic gambling behaviors in the general population; however, presently there is a lack of research that ensures that the PGSI measures the same latent construct in a consistent way across different socio-demographic groups (age, gender, income, education, and race) and gambling modalities (online, sports, and casino gamblers). This concept, known as measurement invariance (MI), is important as it reinforces the validity of the scale as well as survey research conclusions in the field of problem gambling. A sample of nationally representative respondents in the United States was used to test the measurement invariance of the PGSI (n = 2,972). Measurement invariance was tested using multiple group confirmatory factor analysis across the various comparison groups. Analysis supported the measurement invariance of the PGSI across demographic groups (sex, age, race, income, and education) as well as gambling modalities (online gambling, sports wagering, and casino gambling). Differences in latent means demonstrated that younger adults, sports wagerers, and online gamblers reported higher problem gambling severity. As the global gambling industry continues to grow and expand into new jurisdictions, this study has implications for both scientific and clinical use of the PGSI as an instrument to diagnose gambling disorder.

**ИИ:** + · обе модели · валидация инструмента · Tests PGSI invariance in a nationally representative US sample across groups including sports wagerers; may report PGSI among sports bettors.

**Решение:** =

---

### 243 · R1412

**Navigating a Gambling Loss: Examining the Impact of Cognitive Appraisal and Sport Gambling Identity**

2025 · Journal of Sport Management · article · en · https://doi.org/10.1123/jsm.2024-0082

Sport gambling, a complementary sport-related activity, has significant impacts on the spectator sport industry. However, although losses are the most common gambling outcomes and often lead to negative consequences, an examination of consumer response after gambling losses has been neglected. Guided by the transactional theory of stress and social identity theory, a cross-sectional survey design was applied to examine: (a) the direct effect of perceived controllability on future gambling intention and the indirect effect through challenge/threat appraisal, and (b) the moderating effects of sport gambling identity. Our results showed challenge appraisal partially mediated the relationship between perceived controllability and future gambling intention. Additionally, the indirect effect through challenge appraisal was conditional depending on the level of sport gambling identity. This research contributes to academia and the practical field by offering intertwined effects of cognitive appraisal and sport gambling identity as underlying mechanisms that determine behavioral responses after a gambling loss.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Cross-sectional survey of sport gamblers on loss appraisal; abstract doesn't say whether a problem-gambling instrument was used, e.g. as a covariate.

**Решение:** =

---

### 244 · R1413

**Overcoming a Bad Beat: An Examination of Sport Gambling Consumer Motives, Dehumanization, and Athlete Blame**

2025 · Sport Marketing Quarterly · article, journalarticle · en · https://doi.org/10.1177/10616934251391622

The integration of gambling into the sports industry presents both opportunities and challenges that warrant careful examination. Guided by frustration–aggression, self-determination, and dehumanization theories, this study investigates how distinct gambling motivations (excitement, escape, and money) are combined to shape sports gamblers’ negative attitudes and behaviors toward athletes following a gambling loss. Structural equation modeling results confirmed the mediating role of dehumanization in the relationship between both excitement and athlete blame, as well as escape and athlete blame. Specifically, excitement followed an indirect-only mediation pattern. Additional exploratory analysis revealed that escape demonstrated a complementary mediation pattern, with both direct and indirect effects on blame, while money exhibited a direct-only effect on blame. These findings underscore the potential adverse impacts of sports gambling on athletes, an area that has received limited attention. This study also offers practical implications for sports professionals to develop tailored marketing strategies while creating policies to protect athletes.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of sports gamblers on motives and athlete blame; abstract doesn't say whether a problem-gambling instrument was used, e.g. as a covariate.

**Решение:** =

---

### 245 · R1414

**Gambling Risk Potential of Fantasy Sports: Observations from an Exploratory Study Among Treatment-seeking Patients with Substance Use Disorders with Engagement in Gambling.**

2025 · Indian journal of psychological medicine · article, lettersandcomments, journalarticle · eng · https://doi.org/10.1177/02537176241252362

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Research letter with data on fantasy sports gambling among SUD patients (not recruited for gambling problems); no abstract, so PG instrument unknown.

**Решение:** =

---

### 246 · R1417

**Multimodal Analytics for Mitigating the Harms of Sports Gambling Advertising**

2025 · Journal of the Association for Information Systems · article

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; likely computational analysis of sports betting ads, but a user study with a problem-gambling measure cannot be ruled out.

**Решение:** =

---

### 247 · R1420

**Apuestas deportivas y especulación con activos financieros en estudiantes de educación superior**

2025 · Economía Sociedad y Territorio · article, journal-article · pt · https://doi.org/10.22136/est20252239

La participación de estudiantes de educación superior en actividades especulativas en línea ha aumentado significativamente, junto con los problemas derivados de decisiones precipitadas o desinformadas. Este estudio analiza percepciones, actitudes, comportamientos y contexto socioeconómico asociados a dichas actividades, con el fin de identificar factores de riesgo. Se observa que 38.5% de quienes apuestan y 28.6% de quienes especulan financieramente presentan conductas problemáticas. La evidencia sugiere la existencia de una relación negativa entre educación financiera y conductas disfuncionales, pero una relación positiva entre estas y una autopercepción de educación financiera. Preparar a los jóvenes para decidir bajo riesgo es esencial.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Student survey on sports betting reports 38.5% of bettors with problematic behaviour, but the abstract does not name the instrument.); Sonnet + (беттеры + инструмент: Student survey reporting 38.5% of sports bettors with problematic behaviours; likely a gambling screening instrument was used, so full text is worth reading.)

**Решение:** ?

---

### 248 · R1421

**Evaluation of the gambling habits of Spanish adolescents and young adults post-COVID-19 and implementation of a digital escape room intervention for preventing gambling: study protocol of a cluster-randomized controlled trial (GAMBL-OUT project).**

2025 · BMC psychology · article, clinical trial protocol, research-article · eng · https://doi.org/10.1186/s40359-025-03035-x

BACKGROUND: Gambling behaviors among adolescents and young adults have been experiencing an upward trend in the last years, possibly because of new habits developed during the COVID-19 lockdown restrictions. Different preventive strategies have been proposed: universal classroom-based interventions have shown promising evidence as preventive tools, but challenges exist in engaging the target audience effectively. Serious games, i.e., those designed with the specific intent to educate, broaden knowledge, and change behaviors, have been tested with positive outcomes. Digital escape rooms constitute a modality of serious game that has shown potential for a variety of educational purposes, but their efficacy for preventing addictive behaviors, as well as their long-term impact, has not been widely studied. METHODS: The present protocol includes two studies: Study 1 aims to examine changes in gambling habits among a large sample (N = 420) of adolescents and young adults (aged 16-25) in Aragon, Spain, comparing pre-COVID-19 data to current trends. It will assess various gambling types, including online betting, and estimate the prevalence of problem gambling. Study 2 will be a cluster-randomized controlled trial focused on testing the effectiveness of the GAMBL-OUT digital escape-room in preventing gambling among a sample of 240 youngsters. It will evaluate knowledge, intentions, and attitudes pre- and post-intervention, as well as in a 3-month follow-up assessment. Implementation outcomes will also be assessed using qualitative methods, considering acceptability, adoption, appropriateness, feasibility, fidelity, penetration, and sustainability. DISCUSSION: The present project aims at assessing the gambling habits of a sample of 16-25-year-olds in the region of Aragon, Spain, that could be compared to the data gathered before the pandemic started, so not only the prevalence rates can be updated but also potential differences in habits (e.g., preferred gambling alternatives) can be detected. This will undoubtedly help the design of effective preventive measures, such as the GAMBL-OUT digital escape room, a serious game to be implemented in high schools with the aim of increasing knowledge, reducing intentions to gamble, and changing attitudes towards gambling. TRIAL REGISTRATION: This study was registered in ClinicalTrials.gov on 25/03/2025; registration number: NCT06904794.

**ИИ:** разошлись — Opus ? (другое: Protocol for a youth survey of gambling types (including online betting) and problem-gambling prevalence; no results yet. Look for the linked results paper.); Sonnet -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: Study protocol for a survey and cluster-RCT with no results, so it cannot report problem gambling among sports bettors.)

**Решение:** ?

---

### 249 · R1422

**Post-COVID gambling habits of adolescents and young adults in Aragon, Spain: a cross-sectional study.**

2025 · BMC public health · article, journal article, journalarticle · eng · https://doi.org/10.1186/s12889-025-23591-6

BACKGROUND: Gambling has become increasingly normalized in Spain, with 49.3% of the population participating and high engagement among youth, particularly online. Despite legal restrictions, some studies have reported that over 20% of adolescents aged 14-19 reported gambling in 2022. These findings raise concerns about gambling disorder, which affects 4.7% of Spanish youth and is linked to other mental health problems. Factors such as advertising and the COVID-19 pandemic may have contributed to this trend. This study, part of the GAMBL-OUT project, examines gambling behaviors among young people in Aragon, Spain, focusing on prevalence, advertising exposure, post-COVID vs. pre-pandemic comparisons, and factors associated with problem gambling, while comparing high school and university students. METHODS: A cross-sectional study was conducted between November 2023 and March 2024 with 617 participants aged 16-25 from high schools, vocational centers, and universities. Measures included sociodemographic variables, gambling behaviors, advertising exposure, and psychological constructs. Standardized tools included the Problem Gambling Severity Index, Gambling Related Cognitions Scale, Gambling Motives Questionnaire, and UPPS-P Impulsive Behavior Scale. RESULTS: Nearly 60% of participants had gambled, 78.4% of whom had done so in the past 12 months. The overall prevalence of problem gambling in our sample was 3.5%. Among university students, 64.6% had gambled and 3.4% showed signs of problem gambling, which does not represent a significant increase compared to 2019 data. University students post-COVID reported significantly lower exposure to gambling advertisements and less knowledge of betting venues and websites, despite stable levels of preventive information. Although lifetime gambling increased (65.3% vs. 58.1%), riskier behaviors such as sports betting, online gambling, and microtransactions decreased. University students showed greater gambling participation and online awareness, while high school students showed higher impulsivity and stronger gambling intentions. Regression analyses identified enhancement motives, predictive control, negative urgency, and peer influence as factors associated with problem gambling. CONCLUSIONS: Gambling remains a prevalent issue among youth in Aragon, with problem gambling rates stable over time. Despite reduced advertising exposure, the normalization of gambling persists. Findings support the need for age-specific, psychologically informed interventions addressing both individual vulnerabilities and social contexts.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Youth survey measured sports betting participation and problem gambling with the PGSI; could report problem gambling among sports bettors.

**Решение:** =

---

### 250 · R1424

**The relationship between Problem Gambling Severity Index scores and suicidality: Results of a 9‐year cohort study of young United Kingdom adults**

2025 · Addiction · article · en · https://doi.org/10.1111/add.70156

BACKGROUND AND AIMS: Previous studies report cross-sectional associations between harmful gambling and suicidality. Longitudinal evidence is less common, but among young adults in the United Kingdom (UK), current longitudinal evidence highlights the specific association between increases in harmful gambling and subsequent suicidality. In a young UK adult cohort, we aimed to investigate whether harmful gambling, as measured by the Problem Gambling Severity Index (PGSI), would be associated with concurrent and future suicide attempts (at intervals of one, four and five years). Furthermore, the four-year window was used to observe whether PGSI increases were a unique risk factor for suicidality, as has been observed before. In all instances, hierarchical logistic regression models explored whether associations were robust to controls for adolescent suicidality and relevant confounders. DESIGN: A birth cohort study of the UK general population. SETTING: Avon, UK. PARTICIPANTS: n = 2801 (62.4% female) participants with data for suicidality at 24 years from the Avon Longitudinal Study of Parents and Children (ALSPAC). MEASUREMENTS: Past-year non-fatal suicide attempt prevalence was self-reported at 24 and 25 years (in 2017-2018). PGSI was measured at 20 and 24 years. Measured confounders were sex, maternal education, economic activity (employment/education status), hyperactivity, alcohol disorder likelihood and adolescent suicidality. FINDINGS: Past-year suicide attempt prevalence was 2.57% at 24 years, and 1.86% at 25 years. Confounder-adjusted models found that PGSI predicted suicide attempts at 24 years [odds ratio (OR) = 1.13, 95% confidence interval (CI) = 1.05-1.21, P = 0.001], and predicted future suicide attempts over one-year (OR = 1.15, 95% CI = 1.06-1.25, P = 0.001) and four-year timespans (OR = 1.20, 95% CI = 1.08-1.34, P < 0.001), but there was inconclusive evidence of this association over five years (OR = 1.14, 95% CI = 0.995-1.31, P = 0.058). There was inconclusive evidence that increases in PGSI scores between 20 and 24 years predict suicide attempts at 24 years (OR = 1.69, 95% CI = 0.72-3.99, P = 0.230). CONCLUSIONS: Among young adults in the United Kingdom, harmful gambling appears to be associated with suicide attempts; however, this association may be more complex long-term, and increases in harmful gambling during adulthood may not be an important factor.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · General-population ALSPAC cohort using PGSI; the abstract doesn't say whether sports betting participation was reported, though ALSPAC collects activity data.

**Решение:** =

---

### 251 · R1442

**An Odd Game? Understanding Esports Betting Access, Drivers and Consumption**

2025 · doctoral thesis · eng · https://lirias.kuleuven.be/handle/20.500.12942/765919

Over the past years, the options to place a wager on a bookmaker platform have broadened substantially, from being merely focused on traditional forms of sports to almost any type of competitive event related or unrelated to sports (Hing, Thorne, Russell, et al., 2024). While many of these new 'bettable' events remain marginally present and seem only requested by some heavy bettors (Newall, Walasek, Kiesel, et al., 2021), one notable exception are competitive video gaming tournaments, also known as cyber sports (Tang, Kim-wau Sum, Li, et al., 2023) or esports, short for electronic sports (Rogers, 2019). A unique, distinguishing feature of the esports betting phenomenon is that it is a form of third-order gameplay (cf. Kido Lopez, 2023); it is a game (i.e., betting) based on a game (i.e., competition) of games (i.e. video games). Put differently, inherent to esports betting is that it brings together three type of games - video games, sports and gambling (image 2). In line with Lopez-Gonzalez & Griffiths (2016:3), one could see this as a clear example of convergence: "a horizontal integration and collision of adjacent industry sectors". In this case, it is about the [RDC1] convergence[BZ2] of the video games, sports and gambling industries into something new. Surprisingly, however, the empirical and theoretical knowledge gained so far has been rather limited, This is in sharp contrast with research into other gaming-gambling convergence dynamics, such as the emergence of loot boxes or simulated gambling games (Mattinen, Macey & Hamari, 2023). In addition, when considering the scarcely available insights at hand, it becomes clear that the focus of most esports betting research is skewed towards particular (recurring) research questions, approaches, samples and settings (Lawn et al., 2020). It is particularly striking to see that, exceptions put aside (e.g., Yüce, Gökce Yüce, Katirci, et al., 2023), most studies are very traditionally designed around surveys, individualize the phenomenon as a merely psychological construct, and, while doing so, are often focused on Anglo-Saxon consumers and research settings. While these insights are all valuable in their own right and have provided a first insight in, among others, the demographic profile of the esports bettor (e.g., Gainsbury et al., 2017a-b), its motivations or the associated harms (e.g., Greer, Hing, Browne, et al., 2023), betting strategies (e.g., Sweeney, Tuttle, & Berg, 2021), or media use of these consumers (e.g., Macey & Hamari, 2018a-b), they also come with some issues. First, by merely having focused on Anglo-Saxon esports betting consumers, we currently only get a very limited picture of what esports betting entails in other nations or cultures. Despite their potential theoretical relevance, one cannot assume that many of the insights from a USA- and/or UK-context can just be translated into policies of other national jurisdictions, which have other gambling histories (Breuil, 2018), gambling rules (Hoekx, 2011) and/or values at stake (e.g., Hofstede, 2011). Second, the current state of the art has left many questions unanswered beyond the level of the individual. As research has shown, gambling, like other risky product consumption, is more than just an individual matter and also needs a thorough investigation from other levels of investigation, in particular from the level of the environment and product / technology (cf. Zinberg, 1984; Geeraerts, Wijgaerts, Claessens, et al., 2018). Third, and related to the former, two not many of the obtained insights seem to have been thoroughly replicated or triangulated with the methodological apparatus at our disposal, making us question whether some of the conclusions currently made about esports betting are reliable and valid (Wohl, Tabri, & Zelenski, 2019). The purpose of this doctoral dissertation, therefore, is to offer a complementary take towards the study of esports betting by: &bull; Location-wise, changing 'where' and 'who' to focus on, shifting our attention to a geographically understudied, non-Anglo-Saxon research setting - Belgium (Lawn et al., 2020); &bull; Topic-wise, expanding 'what' to investigate, by widening the scope towards both the environment, the product and the individual consumer, paying attention to structural and agentic properties of the Belgian gambling landscape (Giddens, 1984). &bull; Method-wise, proposing new avenues on 'how' to do research, producing both novel and replicated insights into the Belgian esports betting landscape (Wohl, Tabri and Zelenski (2019). This endeavor will be reported and showcased throughout four empirical standalone chapters, all based on published (peer-reviewed) or ongoing research conducted between 2019 and 2025 (i.e., 'when').

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Doctoral thesis with empirical chapters on Belgian esports bettors; may include a consumer survey, but the abstract doesn't say whether problem gambling was measured.

**Решение:** =

---

### 252 · R1455

**Celebrity Endorsements And Inducements In Sports Betting Advertising: A Mixed-Methods Analysis Of NFL Marketing Practices And Its Impact On Consumer Trust And Risk Perception**

2025 · The University of North Carolina at Chapel Hill University Libraries · master thesis, text/masters thesis · en · https://doi.org/10.17615/ezfa-vd63

This study investigates sports betting advertising strategies and their impact on college students following the 2018 legalization wave. Content analysis of NFL broadcasts revealed ubiquitous celebrity endorsements and promotional inducements, with minimal visibility of responsible gambling information. Survey results from 224 college students demonstrated that celebrity appearances significantly enhanced betting operators' perceived trustworthiness and reduced risk perception, outperforming monetary inducements in effectiveness. Athletes and sports personalities generated particularly strong trust effects. Responsible gambling messages went largely unnoticed, creating a concerning asymmetry between promotional and protective elements. These findings suggest that parasocial relationships with celebrities may be more influential than financial incentives in shaping how young adults evaluate betting operators and gambling risks, with important implications for regulatory approaches and consumer protection strategies.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Thesis surveying 224 college students about sports betting advertising; abstract doesn't say whether a problem-gambling instrument like PGSI was used.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Content analysis of NFL ads plus a student survey on trust and risk perception; no problem-gambling instrument is mentioned.)

**Решение:** ?

---

### 253 · R1467

**Do Sports Bettors Need Consumer Protection? Evidence from a Field Experiment Link to Latest Version**

2025 · SSRN Electronic Journal · article, posted-content, preprint · en · https://doi.org/10.2139/ssrn.5191510

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Field experiment with sports bettors; no abstract, so unclear whether a problem-gambling instrument was used.

**Решение:** =

---

### 254 · R1469

**South Australian attitudes, beliefs, and behaviours regarding sports betting 2023**

2025 · CQUniversity · report, report/report · und · https://doi.org/10.25946/30081145

This report presents findings from a 2023 survey of 1,994 South Australian adults regarding their attitudes, beliefs, and behaviours related to sports betting. It compares results to an earlier 2021 baseline survey to identify any changes over the two-year period. The study also evaluates community recall and sentiment towards the 'Here for the Game' public health campaign, which aims to counter the normalisation of sports betting and reduce harmful sports betting in South Australia.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Population survey of South Australian adults on sports betting behaviours; the abstract does not say whether a problem-gambling screen like the PGSI was used.

**Решение:** =

---

### 255 · R1476

**Matched Betting: A Safe Bet or a Risky Gamble?**

2025 · OSF Preprints (OSF Preprints) · preprint

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; matched betting involves sports bookmakers, and the preprint could survey matched bettors on problem gambling.

**Решение:** =

---

### 256 · R1482

**The rise of online gambling addiction: A mental health challenge**

2025 · European Psychiatry · article, journalarticle · en · https://doi.org/10.1192/j.eurpsy.2025.308

Introduction Gambling disorder is a rising concern among young adults, highlighting the need for effective screening to offer appropriate support and intervention. Objectives This study aims to characterize gambling disorder among young adults (ages 18-25) in Portugal. Methods A quantitative cross-sectional study was conducted using a self-administered online questionnaire completed by young adults. Results This study included a population of 554 participants, 166 of whom were gamblers. Among the gamblers, the prevalence was as follows: 63% did not show signs of pathological gambling, while the remaining participants exhibited gambling addiction at varying levels: 25% mild, 9% moderate, and 3% severe. The typical profile of a gambler was identified as a male university student with an average age of 23.5 years, of a middle economic status and residing in an urban area. The preferred types of gambling were sports betting and online casino games. Most online gamblers had previously engaged in offline gambling at the age of M=19.25. The primary attractions of online gambling for these individuals were accessibility, the variety of games, and the potential for economic gains. The main encouragements to gamble online were friend´s influence and online advertising. No significant differences were observed in depression (PHQ-9) and anxiety scores (GAD-7) between gamblers and non-gamblers (p &gt; 0.05). However, among gamblers, a strong positive correlation was found between higher levels of addiction (assessed by DSM-V gambling disorder criteria) and both depression and anxiety scores (r = 0.732, r = 0.681; p &lt; 0.01). Furthermore, severe gambling cases were associated with a higher prevalence of prior formal diagnoses of psychiatric disorders, such as ADHD, anxiety, and depression, although this association was not statistically significant (p &gt; 0.05). All gamblers showed a higher prevalence of substance abuse (p &lt; 0.01). However, this trend did not extend to alcohol consumption (p &gt; 0.05). The Jacobs Dissociative Experiences Scale was used to assess the presence of dissociative symptoms in relation to the severity of gambling addiction, revealing a strong positive correlation (r = 0.721; p &lt; 0.01). Gamblers reported negative impacts on their family and romantical relationships. In contrast, they did not perceive their gambling behavior as having an adverse effect on their friendships or work performance. The majority (71.4%) of high-severity gamblers did not seek professional help and were not receiving any psychopharmacological therapy. Conclusions This study features the critical need for effective screening and intervention strategies for gambling disorder among young adults, given its correlation with mental health disorders and substance abuse. Addressing these challenges is essential for enhancing support and improving outcomes for individuals with gambling disorder. Disclosure of Interest None Declared

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Survey of Portuguese young adults that measured gambling disorder with DSM-5 criteria; sports betting was the most preferred gambling type.

**Решение:** =

---

### 257 · R1483

**El impacto social de las apuestas deportivas en Cataluña**

2025 · RIUVic (UVic-UCC) · bachelor thesis, dissertation · es · http://hdl.handle.net/10854/180336

Las apuestas deportivas han adquirido una gran relevancia en la sociedad actual. Las facilidades para poder realizarlas y las posibles ganancias económicas son los principales motivos por los que muchas personas deciden interesarse en este fenómeno. Se mostrará la evolución de las apuestas deportivas, cuál es la relación que establecen estas con el fútbol, y comprenderá cómo esta conducta influye en la sociedad. Las apuestas deportivas son una modalidad de juego interactivo que combina conocimiento deportivo con la posibilidad de obtener ganancias mediante pronósticos concretos (Plaza, 2024). Por lo general, estas apuestas han estado tradicionalmente administradas de forma estatal. A pesar de que las apuestas deportivas han existido a lo largo de la historia, el advenimiento del siglo XXI y, sobre todo, el tránsito en los sistemas de comunicación, han favorecido la convivencia de las diferentes modalidades de apuesta, generando un mercado fácil e inmediato sobre todo tipo y escalas de eventos. info:eu-repo/semantics/publishedVersion Curs 2024-2025

**ИИ:** ? · обе модели · другое · Bachelor thesis on sports betting in Catalonia; abstract doesn't say whether it includes a survey or a problem-gambling instrument.

**Решение:** =

---

### 258 · R1492

**Estudio epidemiológico sobre las adicciones sin sustancia en el Campus Universitario de Lugo: usos y abusos de las TIC por estudiantes universitarios**

2025 · Hispana · book · es · https://hdl.handle.net/10347/42570

Introducción: No cabe duda de que Internet y los teléfonos inteligentes (smartphones) se han convertido en tecnologías imprescindibles en nuestras vidas debido, en buena medida, a las potencialidades comunicativas y de conectividad que nos ofrecen. No obstante, la intensiva utilización de dispositivos con conexión a Internet está propiciando paulatinamente un desplazamiento hacia entornos virtuales en detrimento de los tradicionales espacios de socialización, lo que está repercutiendo de forma negativa en aspectos de carácter social, personal, emocional, comunicacional (Polo et al., 2017), así como en aquellos otros vinculados al rendimiento académico (Yang et al., 2019; Han y Yi, 2019; Mendoza et al., 2018; Duke y Montag, 2017) y que afectan especialmente a los más jóvenes. En este sentido, en los últimos años existe una especial preocupación desde el ámbito socioeducativo respecto a las consecuencias negativas que puede entrañar un uso inadecuado de la tecnología. Diversos estudios internacionales (Laurence et al., 2020; Sha et al., 2019; García-Umaña y Tirado-Morueta, 2018; Elhai et al., 2017) alertan de los riesgos a los que la población se enfrenta al realizar un uso abusivo y poco responsable de Internet y de los smartphones, como por ejemplo: ansiedad, exposiciones a casos de acoso, alteraciones en la convivencia, trastornos del sueño, fomento de las expresiones agresivas y violentas, acceso a contenidos que pueden llegar a originar dependencias (como es el caso del juego en línea), suplantación de identidad, grooming, nomofobia, phubbing, FoMo, alteraciones en la comunicación, etc. Conscientes de esta situación, así como de las exiguas investigaciones existentes en el contexto universitario gallego sobre los riesgos, abusos y usos problemáticos con las TIC, se ha elaborado un estudio que pretende arrojar luz sobre el comportamiento manifestado por parte de los estudiantes del campus de Lugo, pertenecientes a la Universidad de Santiago de Compostela. Objetivos: 1) Determinar la prevalencia de uso problemático de Internet en el alumnado universitario del campus de Lugo; 2) Identificar las variables sociodemográficas asociadas al uso problemático de Internet y del móvil. 3) Conocer los niveles de nomofobia y phubbing de los estudiantes universitarios lucenses. Método: Estudio transversal o de prevalencia entre estudiantes universitarios del campus de Lugo de la Universidad de Santiago de Compostela. La población objeto de estudio está constituida por todos aquellos estudiantes matriculados en titulaciones de Grado, Doble Grado y Máster (n=774). El instrumento de recogida de información fue un cuestionario autoadministrado y aplicado en línea en el que se incluyeron diversas escalas validadas en otras investigaciones, con preguntas relacionadas con los siguientes aspectos: 1) variables sociodemográficas; 2) uso problemático de Internet; 3) frecuencia de uso de Internet; 4) juego on-line; 5) uso problemático del móvil (nomofobia); 4) nivel de phubbing. Resultados: Los datos revelan, en líneas generales, que en conjunto no existe un uso problemático de Internet. No obstante, se han identificado algunos aspectos relevantes a considerar y que merecen atención. Así, una de cada cuatro personas encuestadas afirma que Internet es un mecanismo de evasión ante los problemas. De hecho, casi la mitad de los estudiantes (48.2%) han abandonado “Algunas veces” las cosas que estaban haciendo para estar más tiempo conectados a la Red. Asimismo, el 43.2% de los estudiantes universitarios piensan que “Algunas veces” su rendimiento académico o laboral se ha visto afectado negativamente por el uso de la Red. Un nada desdeñable 16.5% del alumnado ha manifestado que “Casi siempre” se siente agitado o preocupado cuando no están conectados a Internet, mientras que un 1.9% indica que esta situación la experimenta “siempre”. Por otra parte, se ha podido identificar la existencia de una tendencia decreciente en el uso problemático de Internet conforme aumenta el rendimiento académico del alumnado. En lo que respecta al uso de Internet, cerca de 3 de cada 10 estudiantes confirman que tienen dificultades para cesar una conexión. Esta misma proporción es aplicable a las advertencias recibidas por parte de la familia, amistades o pareja para dejar de usar Internet. Se ha podido constatar que el uso de las redes sociales es muy habitual entre los usuarios (sobre todo de primer curso) en el siguiente orden: ver contenidos de otras personas, crear y difundir y compartir contenidos ajenos. La Red también se ha convertido en un espacio habitual para la realización de compras, ya que 7 de cada 10 estudiantes usan Internet para este tipo de acciones. En esta misma línea, cabe señalar que el consumo de aplicaciones y plataformas de descarga de música y vídeo es algo habitual en 9 de cada 10 individuos. Igualmente, los hombres y los estudiantes de bajo rendimiento informan de un mayor consumo de contenido para adultos que sus compañeros de rendimiento medio (aunque las medias son realmente bajas). En lo que atañe al juego on-line, un 11% del alumnado universitario del campus de Lugo afirma haber jugado alguna vez dinero en páginas web, aplicaciones de juegos de azar o apuestas on-line con el objetivo de obtener un beneficio económico. Por género, resulta significativo que un 33% de los hombres en algún momento hayan jugado dinero a través de medios telemáticos y que un 18,9% lo haya hecho en los últimos doce meses. Así pues, los varones desarrollan hábitos de juego on-line en mayor medida que las mujeres, existiendo una proporción significativamente más alta de hombres que de mujeres que han jugado dinero. También se ha podido constatar que el alumnado con calificaciones más bajas (rendimiento bajo) son los que tienen un mayor nivel en el desarrollo de comportamientos de juego en línea. Cabe señalar que la mayoría de los estudiantes lucenses nunca han jugado dinero (n=643). No obstante, los alumnos que sí han manifestado jugar o gastar dinero, lo han hecho principalmente en videojuegos y apuestas deportivas, siendo los hombres los que gastan más dinero que las mujeres. Asimismo, entre los factores que influyen en el desarrollo de conductas de juego on-line existe una mayor probabilidad de que los hombres desarrollen este tipo de conductas, en concreto, 12.82 veces más frente a las mujeres. Por otra parte, si bien los resultados no han sido estadísticamente significativos en relación con la edad, se ha observado que los estudiantes de menos de 20 años tienen menos probabilidades de desarrollar comportamientos de juego on-line con fines de lucro, en comparación con aquellos alumnos de 30 o más años. En cuanto al uso problemático del móvil, se pudo identificar que un 94% (n=73) de los estudiantes universitarios están en una posición de riesgo y un 5% (n=39) obtuvieron puntuaciones que indicaron la existencia de un Grado de nomofobia de carácter problemático. Las mujeres han obtenido puntuaciones medias más altas frente a los hombres, siendo las diferencias entre ambos estadísticamente significativas, pudiendo evidenciarse además que a medida que aumenta la edad disminuye el comportamiento nomofóbico. La “pérdida de conexión” es un aspecto que preocupa especialmente a los más jóvenes (< 20 años) frente a otros grupos de edad. Otro de los aspectos analizados fueron las conductas consistentes en ignorar a otras personas durante una interacción social por el uso del teléfono móvil (phubbing). Entre los principales resultados, cabe destacar que, a mayor número de horas conectado, mayor nivel de comportamientos relacionados con el phubbing en: “alteraciones en la comunicación”, “apego al móvil” y “obsesión por el móvil”. Las mayores diferencias de medias se han producido en el factor “obsesión por el smartphone” entre aquellos estudiantes que dedican 4 horas o más a conectarse de forma diaria a Internet, respecto a los que se conectan menos de una hora. También han emergido algunos aspectos que pueden resultar relevantes, como el hecho de que: • Un tercio de los estudiantes está pendiente del móvil cuando está con otras personas. • 7 de cada 10 estudiantes tienen siempre a su alcance el teléfono móvil. • La consulta del móvil es una rutina común al levantarse para más de la mitad de los estudiantes. • Un número preocupante de universitarias y universitarios afirma sentirse vacío casi siempre (16%) o siempre (6.9%), sin su móvil.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Student survey covering online gambling including sports betting; unclear whether a problem-gambling screen was used.

**Решение:** =

---

### 259 · R1493

**How Does Problem Gambling Impact the Relationship Between Gambling Attitudes and Frequency?**

2025 · Journal of Gambling Studies · article · en · https://doi.org/10.1007/s10899-025-10379-x

Individuals' beliefs and perceptions about gambling are known to influence gambling behaviours. However, the associations between gambling attitudes, gambling frequency, and problem gambling are unclear within the existing literature. The study aimed to elucidate the relationship between gambling attitudes, gambling behaviour, and problem gambling, using responses to the 2018 Northern Territory Gambling Prevalence and Wellbeing Survey. Data from 1629 participants (Mage = 49.87 years; SD = 14.58 years; 51.63% female) who completed the Attitudes Towards Gambling Survey (ATGS), Problem Gambling Severity Index (PGSI), and reported their gambling frequency were analysed. Prior to testing for moderation of the attitude-frequency path by PGSI risk category, the measurement model of the ATGS was assessed for invariance and one item was removed to improve its psychometric properties. Problem gambling severity moderated the relationship between attitudes towards gambling and gambling frequency. The relationship between attitudes towards gambling and gambling behaviour strengthened at higher levels of problem gambling. Results indicate that the higher the risk of problem gambling, the stronger the influence of gambling attitudes on gambling frequency. These findings are discussed in relation to cognitive dissonance, rationalisation, gambling motivation, and the potential implications for problem gambling prevention strategies.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Secondary analysis of the 2018 NT prevalence survey with PGSI; unclear whether sports betting participation is reported.

**Решение:** =

---

### 260 · R1499

**One in Six Southern New England & NH Residents Bet on Sports at Least Sometimes 10/1/2025**

2025 · University of New Hampshire Scholars Repository (University of New Hampshire at Manchester) · article

Fifteen percent of southern New England and New Hampshire residents legally bet on sports at least occasionally: 2% bet a few times a week or more often, 1% bet a few times a month, less than 1% bet once a month, 5% bet a few times a year, and 6% bet less often than that. Massachusetts and Connecticut residents are most likely to bet legally on sports, while New Hampshire residents are least likely to do so.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Regional poll of sports betting frequency; abstract doesn't say whether any problem-gambling screen was used, though one seems unlikely.

**Решение:** =

---

### 261 · R1509

**The Magic of the Game: Experimental Evidence on Sports Betting Behavior**

2025 · Journal of Economic Behavior &amp; Organization · article, journalarticle, review · eng · https://doi.org/10.1016/j.jebo.2025.107301

As sports betting is surging worldwide, so are concerns about excessive gambling. To explore the drivers of this phenomenon, we conduct an experiment investigating how regular sports bettors in urban Tanzania value sports bets and form expectations about winning probabilities. We find that subjects assign higher certainty equivalents and winning probabilities to sports bets than to urn-and-balls lotteries with identical odds, even though, in fact, they are not more likely to win. We complement the experimental evidence with original survey data on sports betting frequency and motives. Overall, our results suggest that systematic misperceptions of the risks and returns associated with sports betting may contribute to its booming popularity.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Experiment and survey of regular sports bettors in Tanzania; the abstract doesn't say whether a problem-gambling screen like PGSI was used.

**Решение:** =

---

### 262 · R1511

**Decision Revise: Impulsivity and online sports betting behavior: Untangling the causal relationship. Round#1**

2025 · Peer Community In Registered Reports · journalarticle, review, article · en · https://doi.org/10.24072/pci.rr.100996.d1

A recommendation of: Anne Jacob, Mohsen Joshanloo, Robert Czernecka, Anja Kräplin Impulsivity and online sports betting behavior: Untangling the causal relationship https://pada.psycharchives.org/bitstream/ed85321f-28e5-42dd-8f97-cf1cfce9e5d8

**ИИ:** разошлись — Opus -1 (обзор, комментарий, теоретическая, правовая или регуляторная работа: Editorial peer-review decision letter for a registered report, not a study report; the underlying article should be screened separately.); Sonnet ? (неясно, измеряли ли проблемную игру: Registered-report review of an online sports betting impulsivity study; abstract gives no detail, so whether a problem-gambling instrument was used is unclear.)

**Решение:** -

---

### 263 · R1512

**Decision Revise: Impulsivity and online sports betting behavior: Untangling the causal relationship. Round#2**

2025 · Peer Community In Registered Reports · journalarticle, review, article · en · https://doi.org/10.24072/pci.rr.100996.d2

A recommendation of: Anne Jacob, Mohsen Joshanloo, Robert Czernecka, Anja Kräplin Impulsivity and online sports betting behavior: Untangling the causal relationship https://pada.psycharchives.org/bitstream/ed85321f-28e5-42dd-8f97-cf1cfce9e5d8

**ИИ:** разошлись — Opus -1 (обзор, комментарий, теоретическая, правовая или регуляторная работа: Editorial decision letter on a registered report about impulsivity and online sports betting; has no data of its own, so the underlying study should be screened separately.); Sonnet ? (неясно, измеряли ли проблемную игру: Registered-report decision letter on impulsivity and online sports betting; no abstract, and it's unclear whether problem gambling was measured with an instrument in the underlying study.)

**Решение:** -

---

### 264 · R1513

**Recommendation of: Impulsivity and online sports betting behavior: Untangling the causal relationship. Round#3**

2025 · Peer Community In Registered Reports · journalarticle, review, article · en · https://doi.org/10.24072/pci.rr.100996

A recommendation of: Anne Jacob, Mohsen Joshanloo, Robert Czernecka, Anja Kräplin Impulsivity and online sports betting behavior: Untangling the causal relationship https://pada.psycharchives.org/bitstream/ed85321f-28e5-42dd-8f97-cf1cfce9e5d8

**ИИ:** разошлись — Opus -1 (обзор, комментарий, теоретическая, правовая или регуляторная работа: PCI Registered Reports recommendation (editorial commentary) on a study; not itself a primary data report. The underlying article should be screened separately.); Sonnet ? (неясно, измеряли ли проблемную игру: Recommendation of a registered report on impulsivity and online sports bettors; the abstract doesn't say whether a problem-gambling instrument was used, and the study may report PG data.)

**Решение:** -

---

### 265 · R1525

**“Searching for excitement”: exploring the gambling experiences of adult Australian sports fans**

2025 · Managing Sport and Leisure · article · en · https://doi.org/10.1080/23750472.2025.2477500

This study addresses the gambling experiences of 777 adult (aged 18+) sports fans in Australia, collected via an online survey from July 2024 to September 2024. Although 86% were aware of gambling advertising in Australian sports, just under one third (31%) gamble on sports, with a majority gambling low amounts of money on an infrequent basis. Focusing on the reasons behind those who gamble, we apply Bourdieu’s concepts of field, habitus, and social and cultural capital to explain how they sought a quest for excitement to accrue social and cultural capital in matches they watched, rather than trying to acquire economic capital. Although they primarily gamble via apps on their mobile phone, gambling discussions with family and friends on apps like Snapchat and WhatsApp maintain social and cultural capital as part of their broader experience of being a sports fan.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of 777 sports fans that identifies sports bettors; the abstract doesn't say whether a problem-gambling screen such as the PGSI was used.

**Решение:** =

---

### 266 · R1527

**Who Makes In-Play Bets? Investigating the Demographics, Psychological Characteristics, and Gambling-Related Harms of In-Play Sports Bettors**

2025 · OSF · other literature type, text/project · und · https://doi.org/10.17605/osf.io/85whc

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: No abstract; title suggests survey of in-play sports bettors measuring gambling harms, possibly with PGSI; needs full text.); Sonnet + (беттеры + инструмент: No abstract, but title indicates a survey of in-play sports bettors with gambling-related harms and psychological characteristics, likely including a problem gambling measure such as the PGSI; full text needed.)

**Решение:** ?

---

### 267 · R1530

**Engagement in New Gambling Practices and its Association with Gambling Disorder, Impulsivity, and Cognitive Distortions: Findings from a Nationally Representative Sample of Spanish Gamblers.**

2025 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-024-10361-z

Most epidemiological surveys focus on adult gambling behaviors related to traditional gambling forms, while studies on novel forms often focus on loot boxes and cryptocurrency trading individually. This study examines the co-ocurrence of emergent gambling and gambling-like practices, analyzing the demographic and psychological characteristics of involved gamblers. A cross-sectional study surveyed 1429 Spanish individuals aged 18-65, using a web-based questionnaire. The survey assessed participation in 19 gambling (e.g., lotteries, sports betting) and gambling-like activities (e.g., trading of cryptocurrencies and other assets, buying loot-boxes), along with sociodemographic and substance use. Problem gambling (PGSI), Impulsivity (UPPS-P), and cognitive distortions (Labrador's cognitive distortions scale) were also assessed. Participants who gambled over the past year (n = 921) were classified into four groups: traditional gambling (TG) only (64.5%, n = 594), TG with trading activities (27.5%, n = 253), TG with gambling withing video games or streaming platforms (2.5%, n = 23), and TG with both trading and video gambling (5.5%, n = 51). Most gamblers engaged exclusively in traditional formats, but 35.5% also participated in novel gambling forms. Those involved in both trading and video gambling were generally younger, male, with higher levels of impulsivity and gambling-related cognitive distortions compared to TG-only gamblers (p < 0.001). This group also exhibited higher rates of problem gambling and substance use (p < 0.001). This study emphasize the importance of including emerging gambling activities, which are particularly prevalent among high-risk gamblers, in epidemiological surveys. Identifying new gambling patterns and associated risk factors could help optimize public policies and develop more effective regulatory and prevention strategies.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Spanish national survey of gamblers that measured sports betting participation and PGSI; it may report problem gambling by activity.

**Решение:** =

---

### 268 · R1533

**Exploring the Differences in Positive Play among Various Sports Wagering Behaviors.**

2025 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-024-10304-8

Recent technological advances and legislative changes have led to an increase of sports wagering across the United States, raising concerns about possible increases in problem gambling behaviors. This, in turn, points to an increased need to understand responsible gambling and how it relates to sports gambling behaviors. The present work utilizes the Positive Play Scale (PPS), a recent scale designed to measure the increasingly popular responsible gambling concept of Positive Play, to assess how various aspects of sports gambling relate to responsible gambling. Participants were recruited by YouGov Opinion polling and taken from two U.S. samples, and the present analyses look only at those who self-identified as sports gamblers (n = 561, M age = 50.7). Gamblers' location of gambling, types of bets wagered on, timing of gambling, and website used to gamble were assessed. Those who bet online in any capacity, as well as participating in in-game wagering, were found to be significantly less positive in their gambling behaviors. In addition, certain types of sports wagers such as moneylines appeared to be associated with higher positive play, while other types such as parlays were associated with less positive play. Finally, certain websites, particularly offshore websites, were associated with lower positive play behavior. Collectively, these results suggest that there are various aspects of sports wagering behaviors that are associated with positive play variations in gambling.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of US sports gamblers using the Positive Play Scale; the abstract doesn't say whether a problem-gambling instrument like PGSI was also used.

**Решение:** =

---

### 269 · R1536

**APOSTAS ESPORTIVAS E SEU IMPACTO NO ENDIVIDAMENTO E NO CONSUMO DA POPULAÇÃO BRASILEIRA**

2025 · Faculdades Catolicas · doctoral thesis, dissertation · und · https://doi.org/10.17771/pucrio.acad.73919

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Brazilian thesis on sports betting, debt and consumption; no abstract, so a bettor survey with a PG screen is possible.

**Решение:** =

---

### 270 · R1537

**Drivers of adolescent chasing behavior: The role of craving, decision-making, alcohol use, and gambling severity**

2025 · Addictive Behaviors · article · en · https://doi.org/10.1016/j.addbeh.2025.108414

Craving and impaired decision-making are hallmark features of addiction, playing a prominent role in gambling disorder. These factors are central to loss-chasing behavior, a core diagnostic criterion of gambling dependence characterized by persistent attempts to recover prior losses. This study examines the interplay of craving, affective decision-making, decision-making styles, alcohol use, and gambling severity in chasing behavior among 272 Italian adolescents aged 14-19. Participants completed validated measures, including the South Oaks Gambling Screen-Revised for Adolescents (SOGS-RA), Iowa Gambling Task (IGT), General Decision-Making Style (GDMS), Gambling Craving Scale (GACS), and Alcohol Use Disorders Identification Test (AUDIT). Chasing behavior was assessed using a computerized task, with participants randomly assigned to either a Control or Loss condition. Regression and path analyses indicated that craving was the strongest predictor of both chasing initiation and persistence, while alcohol consumption was uniquely associated with greater chasing persistence. Conversely, a dependent decision-making style emerged as a protective factor, being associated with reduced engagement in chasing behavior. Notably, neither gambling severity (measured by the SOGS-RA) nor affective decision-making capacity (assessed via the IGT) predicted chasing outcomes. These findings suggest that chasing operates as an independent behavioral mechanism within gambling disorder, distinct from generalized gambling severity or neurocognitive decision-making deficits.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Italian adolescents screened with SOGS-RA in an experimental chasing study; unclear whether sports betting participation was recorded.

**Решение:** =

---

### 271 · R1539

**Impact of Sports Gambling on Physical Activity**

2025 · SSRN Electronic Journal · article, posted-content, preprint · und · https://doi.org/10.2139/ssrn.5703524

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; SSRN preprint on sports gambling and physical activity, possibly economics/legalization study; unclear if a problem-gambling instrument was used.

**Решение:** =

---

### 272 · R1545

**Consumer behavior of promotions: Do free bets and bonuses encourage riskier behavior in sports gamblers?**

2025 · SHAREOK (University of Oklahoma; Oklahoma State University; Central Oklahoma University) · dissertation · en

The number of people who sports bet and gamble has steadily increased over the past few decades, but with the rise of promotions and other types of “free bets,” that number has spiked (delasport.com). The launch of marketing campaigns and promotions focused on sports betting could have contributed to this spike. Today, it has become common for people to use numerous sportsbooks and websites to place bets and wager money. I propose that these advertisements and the game-like style of sportsbook apps have led to a potential shift in consumers’ attitudes and behaviors towards sports gambling. This study focuses on identifying students’ perceptions of sports betting and whether or not utilizing these “free bet” promotions leads to a behavior shift in gamblers' minds to perceive risk less and engage in riskier betting behavior. The data was collected by conducting an extensive literature search on sports betting and the consumer behavior behind it, and by conducting an online survey using Qualtrics. The data from the survey found that 61.5% of respondents said they would use their promotions and free-bets on higher risk bets.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Online student survey on sports betting promotions and risk perception; the abstract doesn't say whether a problem-gambling instrument was used.

**Решение:** =

---

### 273 · R1548

**Prevalence, patterns, correlates, and academic implications of sports betting and problem gambling among Nigerian undergraduates.**

2025 · Discover mental health · article, journal article, journalarticle · eng · https://doi.org/10.1007/s44192-025-00214-5

BACKGROUND: Sports betting has become increasingly popular among Nigerian undergraduates, particularly males. Once a recreational activity, sports betting has now become an economic pursuit for many young students to augment income. This trend raises concerns about its potential impact on academic performance and mental health. This study examined the patterns, correlates, academic implications, and predictors of sports betting and problem gambling among University of Calabar undergraduate students. METHODS: A cross-sectional analytical study was conducted among undergraduate students at the University of Calabar using a self-administered questionnaire. Data on gambling behaviour, problem gambling severity, reasons for gambling, and demographic information were collected using the Reasons for Gambling Questionnaire (RGQ) and the Problem Gambling Severity Index (PGSI). The impact of sports betting on participants' academic performance was also assessed. Data was analysed using SPSS Statistics v25, employing descriptive statistics, bivariate analysis, and logistic regression. RESULTS: Among 406 respondents, 36.7% had engaged in sports betting, with 30.3% participating in the past year. One underage bettor was identified. Males (83.2%) were more likely to bet. Two-thirds of respondents preferred online sports betting. The primary motivation behind sports betting was monetary gain (87.8%), followed by recreational purposes (47.1%) and thrill-seeking (45.1%). Problem gambling prevalence was 14.3%, increasing to 47.2% among those who had gambled in the previous year. Negative academic impacts were reported by 64.2% of respondents who gambled in the year prior. Strong evidence of an association between male gender and higher income with sports betting and problem gambling was identified (p < 0.05). Gambling frequency had strong evidence of association with adverse academic effects (p < 0.01). Problem gambling was associated with spending study time on sports betting (60.7%) or following sports betting games (75%) (p < 0.001). Logistic regression showed strong evidence of an association between advertisement influence and problem gambling, with those influenced by exposure to gambling adverts being four times more likely to have problem gambling (OR 4.36, 95% CI 1.93-9.86). CONCLUSION: The study revealed a high prevalence of sports betting and problem gambling among Nigerian undergraduates. Academic impacts were also evident, highlighting the need for targeted interventions. We recommend developing and implementing educational campaigns, financial literacy programs, and support services for at-risk individuals. Additionally, regulatory measures to restrict the advertising and marketing of sports betting to minors and vulnerable populations should be considered.

**ИИ:** + · обе модели · беттеры + инструмент · Student survey measuring sports betting and PGSI; reports problem gambling prevalence among past-year sports bettors (47.2%).

**Решение:** =

---

### 274 · R1560

**Youth and Gambling: Determinants and Impact on Psychological Resilience in Senegal**

2025 · Research Square · preprint · en · https://doi.org/10.21203/rs.3.rs-7437944/v1

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; a survey of youth gambling in Senegal could have measured sports betting and problem gambling.

**Решение:** =

---

### 275 · R1566

**Anxiety and Distress Tolerance as Mediators between Complex Posttraumatic Stress Disorder Symptoms and Gambling Severity in Veterans**

2025 · Journal of Gambling Studies · article · en · https://doi.org/10.1007/s10899-025-10449-0

Experiences of gambling-related harm are significant concerns among military veterans, particularly those with posttraumatic stress disorder (PTSD) and complex PTSD (CPTSD). CPTSD, as outlined in the ICD-11, includes disturbances in self-organisation (DSO), encompassing affective dysregulation, negative self-concept, and interpersonal difficulties. While anxiety and distress tolerance (DT) have been implicated in PTSD-related maladaptive behaviours, their roles in the relationship between CPTSD and gambling risk severity remain unclear. This study examines whether anxiety and DT mediate the association between CPTSD symptom clusters (PTSD and DSO) and gambling severity in UK Armed Forces veterans. A cross-sectional study was conducted with UK ex-service personnel (n = 346) who completed the International Trauma Questionnaire for CPTSD, the Generalised Anxiety Disorder scale, the Distress Tolerance Scale, and the Problem Gambling Severity Index. Mediation analyses were conducted using bootstrapped regression models. Anxiety was found to be a significant indirect pathway between CPTSD symptoms and gambling risk severity, with a stronger indirect effect observed for DSO symptoms than PTSD-specific symptoms. In contrast, DT did not show a significant indirect pathway, indicating that deficits in DT may not be central to gambling behaviours in veterans with CPTSD. These findings highlight the critical role of anxiety in gambling-related harm among veterans with symptoms of CPTSD, suggesting that interventions targeting anxiety regulation may be beneficial than those targeting distress tolerance in reducing gambling risk severity. Future research should explore additional potential pathways, such as impulsivity and trauma-related dissociation to further clarify associations between CPTSD and gambling severity.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Veteran survey used PGSI; the abstract doesn't say whether participation in sports betting was measured.

**Решение:** =

---

### 276 · R1576

**Striving Towards National Lower-Risk Gambling Guidelines: An Empirical Investigation Among a Sample of Swedish Gamblers.**

2025 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-024-10372-w

Abstract Several countries, including Canada and Australia, have developed public health-based lower-risk gambling limits to differentiate lower-risk from higher-risk gambling. This study aimed to identify a preliminary set of lower-risk gambling limits (gambling frequency, duration, expenditure, expenditure as a proportion of personal net income, and diversity), and investigate if gambling types are linked to additional harms, in a Swedish context. The study involved secondary analyses of two online survey studies using the Gambling Disorder Identification Test (GDIT). Receiver operating curve analyses were conducted in relation to both + 1 and + 2 gambling-related harms in a sample of 705 past-year gamblers. Potential lower-risk limits ranges identified were: gambling frequency of “2–3 times a week” to “4 or more times a week” (8–16 times monthly); gambling duration of 6 to 15 h per month; gambling expenditure of 2,000 SEK (approximately $USD190) per month; gambling expenditure as a proportion of personal net income of 5%; and gambling diversity of only one problematic gambling type. Gambling on slots and sports betting were associated with gambling-related harms. The lower-risk limits in the current study were higher than in previous studies, which may be explained by the large proportion of support- or treatment-seeking gamblers with high rates of problem gambling and problematic online gambling in the study sample. An international consensus-based framework on gambling consumption is warranted, with lower-risk limits validated in future empirical studies using larger datasets collected from the Swedish general population.

**ИИ:** ? · обе модели · другое · Gamblers surveyed with GDIT and sports betting measured, but many were support- or treatment-seeking; full text needed to check sample eligibility.

**Решение:** =

---

### 277 · R1579

**Cognitive Bias and the Impact of Age on Sports Betting**

2025 · Sport Marketing Quarterly · article, journalarticle, review · en · https://doi.org/10.1177/10616934251391619

Popularized and heavily promoted sports betting is new to the North American sports landscape. It is a highly competitive market and as a result, providers aggressively advertise and incentivize. Several vulnerable segments exist, but young adults are most susceptible to irrational decision-making yet receive the most attention from advertisers. Given this, it is important to understand the impact of age as it relates to betting and decision-making. The current study surveyed 514 sports bettors to learn the moderating impact of age between the theoretical relationships of self-efficacy, confirmation bias, and illusion of control. The results indicate cognitive bias varies by age. Younger sports bettors tend to be more impulsive and overconfident in their wagering decisions. Older sports bettors tend to be more rigid. Based on the findings, marketers must look solely beyond revenue when formulating strategy and consider responsible marketing tactics to ensure ethical practices.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Survey of 514 sports bettors on cognitive biases; abstract doesn't say whether a problem-gambling instrument was used.

**Решение:** =

---

### 278 · R1581

**Childhood trauma, complex PTSD, and severity of online sports betting in French bettors**

2025 · European Journal of Trauma & Dissociation · article, journalarticle, journal-article · en · https://doi.org/10.1016/j.ejtd.2025.100602

BackgroundOnline sports betting has surged in France, creating significant public health and clinical issues. Although childhood trauma and PTSD are known risk factors for gambling disorder, their role in the context of addiction—especially with regard to online sports betting—has not been well-examinedObjectiveDetermine how five Childhood Trauma Questionnaire (CTQ) subscales and International Trauma Questionnaire (ITQ) symptom severity are associated with gambling severity (GMQ-F) among French sports bettors and derive actionable insights for addiction interventionsMethodsWe conducted a cross-sectional survey of 135 adult French online sports bettors. Participants completed the CTQ, ITQ, GMQ-F, and the MIH5 impulsivity scale. Two hierarchical regressions modeled gambling severity: Step 1 included CTQ subscales, and Step 2 included the ITQ total score and CTQ × ITQ interactions. Covariates were age, gender, and impulsivity. Prevalence was as follows (valid n = 134 for CTQ): emotional abuse 44.03 % (59/134), sexual abuse 98.51 % (132/134), physical neglect 88.81 % (119/134), and physical abuse 39.55 % (53/134). All participants met the 'problematic' threshold (100 %, n = 135) on the French CPGIResultsPhysical abuse and overall PTSD symptoms independently were associated with higher betting severity. Unexpectedly, sexual abuse showed a negative association, warranting further exploration. No significant trauma × PTSD interactions were foundConclusionsPTSD symptoms and childhood physical abuse are robust predictors of the severity of online sports betting. Incorporating trauma-informed modules into standard gambling interventions, particularly those targeting arousal regulation and coping, may enhance treatment efficacy. Future addiction research should integrate detailed trauma profiling to refine risk stratification and prevention strategies.

**ИИ:** + · обе модели · беттеры + инструмент · Survey of 135 French online sports bettors using the CPGI; all 100% met the problem threshold, so check the full text for recruitment based on gambling problems.

**Решение:** =

---

### 279 · R1586

**Multidimensional Loss Chasing among Online Sports Gamblers: Assessing the Efficacy of Optimized Thresholds for the Prediction of Gambling Harm**

2025 · OSF Preprints (OSF Preprints) · studyregistration/pre-registration, preprint · https://doi.org/10.17605/osf.io/rf2pb

Open-ended registration is attached as a pdf

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Pre-registration on online sports gamblers predicting gambling harm; the abstract is missing, so it's unclear whether a problem-gambling instrument was used.

**Решение:** =

---

### 280 · R1588

**A Network Analysis of Addictive Behaviors: Risk and Protective Factors Among Israeli Youth in a Cross-Sectional Study**

2025 · International Journal of Mental Health and Addiction · article · en · https://doi.org/10.1007/s11469-025-01569-0

Abstract Although many youths engage in potentially addictive behaviors without lasting harm, some develop substance use disorders (SUD), behavioral addictions, or both, which pose significant psychological and social risks. This study employed network-analysis to investigate the interrelations among risk and protective factors in three groups of Israeli youths (12–18 years): those with behavioral addictions ( n = 4209), those with both behavioral and substance use addictions ( n = 1004), and those without any addiction ( n = 779), drawn from a community sample of 6849 participants. Youths without addictions reported the highest levels of protective characteristics and the lowest risk profiles, whereas those with both forms of addiction exhibited the most severe risk patterns. The network structures differed substantially between groups, with dual-addiction youth displaying the most fragmented and dysregulated configurations. These results reveal distinct psychological and social dynamics across addiction profiles and underscore the importance of targeted, group-specific interventions addressing impulsivity and relational vulnerabilities.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Community youth survey of behavioral addictions, possibly including gambling; unclear whether problem gambling and sports betting were measured.

**Решение:** =

---

### 281 · R1589

**The landscape of youth addiction in Israel: Identifying high-risk behaviors**

2025 · Addictive Behaviors · article · en · https://doi.org/10.1016/j.addbeh.2025.108396

While significant progress has been made in understanding the prevalence of use and severity of addictive behaviors, there remains a lack of research adopting a lay epidemiological approach to examine a broad spectrum of addictive behaviors among a large youth population. The objective of this study is to investigate the frequencies of use and severity of various addictive-like behaviors across different demographic variables including gender, religion, country of birth, religiosity, socio-economic status, and age. The sample comprised 6,849 Jewish and Arabic Israeli youth from the general community, consisting of 2,776 males (41 %) and 4,074 females (59 %), 12-18 years of age (M = 15.92, SD = 1.27) who completed the survey anonymously and with parental consent. Results indicated that higher severity in one addictive behavior correlates with increased severity in others. Substance-related behaviors such as alcohol, tobacco, cannabis, and cocaine showed stronger correlations within their group than with behavioral addictions like gambling, shopping, gaming, eating disorders, sexual activity and social networking. Similarly, behavioral addictions also display stronger correlations within their own cluster. In addition, significant prevalence of use and severity differences were observed in addictive behaviors based on gender, religion, country of birth, religiosity, socio-economic status, and age. The research underscores the critical role of providing support and resources to youth, which is essential for preventing addictive behaviors and reducing the risks associated with their development.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Large youth community survey measuring gambling severity; unclear whether sports betting participation was measured.

**Решение:** =

---

### 282 · R1592

**Sports Betting, the gateway drug to a gambling addiction: A study of the implications of sports gambling on societal well-being and its effects on the younger generation**

2025 · Journal of the Arkansas Academy of Science · article

Introduction It is everywhere you turn. In recent years we have seen unprecedented growth in the advertising, activities, and addiction of gambling. To put it into perspective “the AGA reported that total revenue from land-based casino games, sports betting and iGaming reached $66.52 billion for the calendar year, a 10% gain from the previous record set in 2022.” Of that, $10.92 billion came from sports betting specifically which was a 44.5% increase from the prior year (Reynolds, 2024). Factors contributing to the rise include the increase in gambling advertisements, the legalization of sports betting, and the removal of environmental barriers to gambling. Presently, gambling addictions may start at a younger age than in previous years. Many college students engage in gambling, whether through sports betting, going to the casino, or playing blackjack on their phones. Without proper restriction and awareness of gambling addiction disorders, the negative consequences will continue to affect people worldwide. In today’s world, gambling, particularly sports betting, is heavily promoted. Super Bowl advertisements, halftime shows, and television commercials frequently feature gambling ads. In fact, the NHL, NFL, MBA, and MLB all have deals with sportsbook operators (Bumbaca, 2023). It may not have been noticed until now how often these ads occur. There is evidence that gambling advertisements most heavily affect children, young people, and those already suffering from gambling addictions (McGrane et al. 2023). They serve as a subliminal reminder that a bet is only a few clicks away, making gambling seem fun and risk-free. People are developing gambling behaviors at a young age. With the increasing popularity of sports betting and fantasy sports, gambling has become a hobby for many college students. Professional sports leagues exploit gambling addictions to make millions, similar to how cigarette manufacturers exploit nicotine addictions for profit. Advancements in technology allow sports gambling to happen anytime and anywhere from a cell phone. People addicted to gambling are aware of the potential financial losses, but they may not consider the other adverse impacts it can have on their lives. “From a clinical perspective, gambling disorder is characterized as a behavioral addiction involving persistent and repetitive behaviors leading to significant harm or distress” (Kardefelt-Winther et al. 2017). Gambling can affect personal well-being, family relationships, impulse control, and morality. These and other factors will be further discussed in this project. This research project has the potential to positively affect our community, this educational institution, and society as a whole. It is important to spread awareness of problem gambling and to educate others so that they may understand the scope of this issue. A broader knowledge of addiction, gambling behavior, and psychological well-being can contribute to improving the outcomes for individuals affected by gambling. These findings may provide data to implement gambling regulations that support prevention and treatment. My goal is to increase awareness, reduce the number of individuals who engage in problem gambling, and to increase the practice of responsible gambling, as encouraged by this research. Sports betting is heading in a scary direction. With studies like this, its path can be changed. With this research I am seeking to answer: What are the main influences of sports betting? What are the consequences and long-lasting effects of sports betting? Are individuals aware of the negative consequences of sports betting? How is sports gambling marketed and integrated into professional sports, and what is the effect of this integration?

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Student project on sports betting among young people; only the introduction is shown, so it's unclear whether it surveyed people or used a problem-gambling instrument.

**Решение:** =

---

### 283 · R1601

**Unraveling the Impact of Early Adversity and Perpetration on Problematic Gambling in Young Adults: Insights from the Add Health Study**

2025 · Journal of Gambling Studies · article · en · https://doi.org/10.1007/s10899-025-10439-2

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; Add Health population cohort measured problem gambling, but whether sports betting participation was recorded is unclear.

**Решение:** =

---

### 284 · R1604

**Research of sports betting habits among amateur and professional athletes and physical education teachers**

2025 · Gradus · article, journalarticle, journal-article · en · https://doi.org/10.47833/2025.1.art.007

Gambling in different forms is present in the life of many people, thanks to the fact that it is an oppurtunity for consumers to improve their financial situation as well as the joy of the game. Sports betting involves some kind of excitement, which encourages people to play in the hope of luck. Based on this, our research analysed the sports betting habits of athletes at different levels and PE teachers and also their opinions about sports betting. During the research, we conducted a questionnaire study among hobby athletes, PE teachers, coaches, and licensed athletes (n=65). The results of the study indicated that most of the respondents (95%) had tried gambling at least once. Furthermore, we also found that lower-level athletes spend proportionally more on gambling than higher-level athletes. Our results highlighted that amateur or hobby athletes spend more time, energy, and also money to gambling. An interesting result is that 46% of sports bettors have felt that they have gone too far with their bets, so it is not surprising that almost half of the sports bettors experienced a problem that had negative consequences This proved that it is very easy to become addicted to sports betting and it is also significantly dangerous due to the development of addiction. Based on the answers received during the research, it can also be concluded that, according to the significant majority of the respondents, gambling has a negative effect on the individuals rather than a positive one.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Questionnaire of athletes' sports betting; items like 'gone too far' suggest possible screen items, but no named problem-gambling instrument.

**Решение:** =

---

### 285 · R1611

**Concerned significant others of persons with problem gambling and problem gaming: Prevalence and characteristics in the Norwegian population**

2025 · Journal of Behavioral Addictions · article · en · https://doi.org/10.1556/2006.2025.00083

Background: Problem gambling (PG) and problem gaming (GAM) generate concern for close ones often denoted as concerned significant others (CSO). There is a dearth of evidence on the characteristics associated with being a CSO of PG and GAM, which is explored in the present study. Methods: A total of 2,000 persons (aged 16-74 years), randomly drawn from the Norwegian population registry, were invited to respond to a questionnaire assessing current or past concerns about gambling and gaming of significant others, as well as questions about their own gambling, gaming, alcohol and illegal drug use, personality traits, and demographic characteristics. Multiple regression analyses were conducted to identify correlates of being a CSO of PG and GAM, split by close (i.e., first degree relatives and partners) and remote relationships. Results: In all, 575 persons (46% men, age M = 44.05, SD = 17.31 years) completed the questionnaire (response rate = 30.4%). The prevalence of ever being a CSO was 23.2% for PG (6.8% for close, specifically) and 27.1% for GAM (17.4% for close, specifically). Close/PG was associated with higher Neuroticism. Remote/PG was associated with lower education and own PG. Close/GAM were younger. Remote/GAM correlates were lower income, own PG, and higher Extraversion scores. Conclusions: PG and GAM have high CSO prevalence rates. In line with the problem behavior theory, the correlates of being a CSO suggest the presence of environments with problems and fewer resources connected to PG and GAM.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Norwegian population survey measured respondents' own gambling and problem gambling; unclear whether sports betting participation was recorded.

**Решение:** =

---

### 286 · R1613

**"Who Do Tipsters Work For? Tipster Exposure and Adolescent Gambling"**

2025 · Zenodo (CERN European Organization for Nuclear Research) · article, journal article, review · eng · https://doi.org/10.5281/zenodo.17778668

El manuscrito aborda un problema de salud pública emergente: la influencia de los tipsters —una nueva forma de influenciador digital en el mundo de las apuestas— en la vulnerabilidad de los adolescentes al juego. Si bien los tipsters se han convertido en actores destacados en los ecosistemas de apuestas deportivas en línea, la investigación empírica sobre su impacto en los adolescentes es prácticamente inexistente. Nuestros hallazgos demuestran un claro gradiente de riesgo, mostrando que seguir a los tipsters —en lugar de simplemente conocerlos— está fuertemente asociado con una mayor intención de juego, implicación conductual, gravedad y factores de riesgo cognitivo-motivacionales. Al documentar estas asociaciones mediante instrumentos psicométricos bien validados y realizar análisis estadísticos rigurosos (incluidas estimaciones del tamaño del efecto), el estudio proporciona uno de los primeros análisis cuantitativos de este fenómeno en la adolescencia. Entre sus fortalezas metodológicas se incluyen: 1) Una muestra amplia y diversa (N = 782) procedente de nueve centros educativos. 2) El uso de medidas internacionales validadas (CSPG, Lie/Bet, GMQ-F, EDGAR-A). 3) Una operacionalización clara de los grupos de exposición que permita la identificación de un gradiente de riesgo de desarrollo consistente. 4) Procedimientos estadísticos transparentes y reproducibles alineados con las mejores prácticas en investigación psicológica y de salud pública.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Adolescent survey (N=782) on sports-betting tipster exposure using Lie/Bet; unclear whether sports betting participation itself was measured.

**Решение:** =

---

### 287 · R1618

**Online Sports Betting in Greece: An Empirical Investigation**

2025 · Elsevier BV · article, journalarticle, posted-content · eng · https://doi.org/10.2139/ssrn.5651292

Although international interest on e-gambling commerce is steadily increasing, studies about the online sports betting sector in Greece are very rare. Based on a web survey the present study, attempts to address this gap, by shedding light on the active sports bettors characteristics, preferences and patterns in Greece. A thorough analysis of 325 internet sport bettors reveals contingent relations between significant variables, while conclusions are drawn about the size of stakes placed and the punters motivations.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Web survey of 325 Greek online sports bettors; abstract mentions stakes and motivations but doesn't say whether problem gambling was measured.

**Решение:** =

---

### 288 · R1637

**The Detrimental Effects of Technology on the Academic Performance of University Student Athletes: The Implications of Online Sports Betting in Kenya**

2025 · International Journal of Physical Education Recreation and Sports · article, journalarticle, journal-article · en · https://doi.org/10.47604/ijpers.3476

Purpose: This study explores the impact of technology, particularly online sports betting, on the academic performance of university student-athletes in Kenya. While technology offers opportunities, it also creates challenges, such as distractions, poor time management, sleep disruption, and financial or psychological distress. Methodology: This study employed a descriptive research design targeting 24,639 student-athletes and university sports officers across Kenyan universities. Using simple random sampling, a representative sample of 423 participants was selected, including 385 athletes and 38 sports officers. Data collection involved self-report questionnaires, observation score sheets, and key informant protocols, with gambling behaviors carefully recorded during observations. Findings: The regression analysis showed that gambling severity explains 5% of the variance in students’ academic performance (R² = 0.05), with the model being statistically significant (F = 12.907, p &lt; 0.001). The regression coefficient (β = 0.346, p &lt; 0.001) indicates a positive and significant relationship, meaning that an increase in gambling severity predicts poorer academic performance. Additionally, demographic factors significantly moderated this relationship, increasing the explained variance to 56.6% (R² = 0.566, F = 3.07, p &lt; 0.001). This suggests that demographic characteristics strongly influence how gambling severity affects academic outcomes, aligning with findings that socioeconomic background relates to gambling addiction and its effects. Unique Contribution to Theory, Practice and Policy: Based on the study findings, it was recommended that the Online sports betting companies should engage scholars in formulating policies that advocate for responsible gambling practices while mitigating the risks associated with academic detrimental online betting behaviours. Secondly, prior to granting licenses, betting companies should implement technological solutions that empower users to establish personal gambling limits, particularly for student-athletes representing Kenyan universities, to prevent excessive spending and potential addiction. Third, both public and private higher education institutions should create betting policies that foster mental wellbeing, which may include regular mental health workshops and screenings.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Survey of Kenyan student-athletes on online sports betting measuring 'gambling severity'; instrument not named, may be PGSI or similar.); Sonnet + (беттеры + инструмент: Survey of Kenyan student-athletes on online sports betting measuring gambling severity; likely uses a problem-gambling instrument and could report prevalence.)

**Решение:** ?

---

### 289 · R1639

**Gambling behaviors in Israeli adults: findings from a nationally representative sample.**

2025 · Israel journal of health policy research · article, journal article, journalarticle · eng · https://doi.org/10.1186/s13584-025-00733-0

Abstract Globally, 46.2% of all adults report having gambled in the previous 12 months. While most experience no negative repercussions from gambling, individuals who are highly engaged in gambling are at greater risk of problem gambling (PG). Studies point to the psycho-social, environmental, and socio-demographic risk factors associated with gambling and PG, and the associated harm to individuals, families, and society, making it a public health concern worldwide. Israel has a relatively regulated conservative gambling market where casinos and electronic gambling machines are banned, and online gambling is only permitted for sports betting. Nevertheless, Israel has a relatively high percentage of PG. This study was designed to characterize involvement in gambling behavior during the previous year in non-gamblers, low-frequency, and high-frequency gamblers as a function of socio-demographic, health, and psycho-social risk and protective factors, and differentiate between problem and non-problem high-frequency gamblers. A representative sample of 3224 Israeli Jews and Arabs filled in an online questionnaire in 2022. The findings showed that 50.7% were non-gamblers, 33.8% were low-frequency gamblers, and 15.5% were high-frequency gamblers. Compared to non-gamblers, low-frequency and high-frequency gamblers were associated with Jewish ethnicity, low levels of financial self-efficacy and neighborhood cohesion, a greater likelihood to smoke and drink, and having a significant other (family/social network member) with perceived excessive gambling. Male gender and traditional self-perceived religiosity were associated with both low-frequency and high-frequency gamblers as well, but to a greater extent with high-frequency than low-frequency gamblers. Online gambling, stress, low financial self-efficacy, using social welfare allowances for gambling, having a significant other who engages in perceived excessive gambling, and identifying as an Israeli Arab were all associated with PG in high-frequency gamblers. These findings suggest that despite its conservative regulated market, gambling in Israel exceeds international averages. The similarities between low-frequency and high-frequency gamblers in terms of risk factors may hint at a type of gambling normalization. Regulatory reforms informed by public health policies are recommended to decrease access to gambling, including banning online gambling and curbing special gambling offers timed to coincide with welfare payments. Awareness campaigns, culturally sensitive prevention programs are recommended, as well as studies to monitor gambling harm.

**ИИ:** + · обе модели · опрос населения об азартных играх · Nationally representative Israeli gambling survey measuring problem gambling; sports betting is the main legal online form, so activity data is likely.

**Решение:** =

---

### 290 · R1648

**El marketing deportivo, su utilización por parte de las casas de apuestas y el impacto en la salud mental**

2025 · bachelor thesis · esl/spa · https://hdl.handle.net/10612/25632

[ES] El marketing ha ido evolucionando en los últimos años, llegando a convertirse en una de las principales herramientas en el ámbito empresarial. Este hecho ha promovido la extensión del marketing a diferentes ramas, propagándose al mundo del deporte, un sector que con el paso de los años ha ido abarcando un gran volumen de aficionados, convirtiéndolo en un gran escaparate para muchas empresas como las casas de apuestas. En el presente trabajo se persigue como principal finalidad analizar la evolución del marketing deportivo, cómo se ha implementado las estrategias en el ámbito de las apuestas deportivas y cuáles son las consecuencias negativas que estas pueden tener en la salud mental de las personas. Para ello, se desarrolla un marco teórico, en el que se recopila y analiza información relevante acerca de estos temas, que servirá de base para el estudio empírico posterior. Este estudio recoge datos sobre hábitos de consumo deportivo, percepción de las estrategias de marketing y experiencias vinculadas a la ludopatía. [EN] Marketing has been evolving in recent years, becoming one of the main tools in the business world. This fact has promoted the extension of marketing to different branches, spreading to the world of sport, a sector that over the years has been covering a large volume of fans, making it a great showcase for many companies such as bookmakers. The main aim of this paper is to analyse the evolution of sports marketing, how strategies have been implemented in the field of sports betting and the negative consequences that these can have on people's mental health. To this end, a theoretical framework is developed, in which relevant information on these issues is collected and analysed, which will serve as the basis for the subsequent empirical study. This study collects data on sports consumption habits, perceptions of marketing strategies and related experiences of pathological gambling.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Bachelor thesis with a survey on sports betting marketing and pathological gambling experiences; unclear whether a validated PG instrument was used.

**Решение:** =

---

### 291 · R1649

**Gambling and Gaming: A Comparative Study of Professional Footballers Versus the General Population.**

2025 · Sports (Basel, Switzerland) · journal article · eng · https://doi.org/10.3390/sports13020034

(1) Background: Elite sport can increase vulnerability to developing mental health pathologies. The purpose of the study is to determine the frequency at which these behavioural disorders appear in elite footballers and evaluate their relationship with other addictions. (2) Methods: A cross-sectional study was conducted between November 2020 and January 2022 on 306 participants. The variables of gambling and gaming were studied. The different groups were compared using Chi-squared tests. Probabilities exceeding 95% (p-values < 0.05) and residuals results greater than 2 or less than -2 were considered significant. (3) Results: There were significant differences between the two groups in terms of alcohol (p < 0.001), tobacco (p < 0.001), and cannabis (p = 0.016) consumption. We also found differences between those who had a history of a nervous disease (p = 0.015). 6.6% of the of football players had a probable diagnosis of a gambling disorder compared to 1% in the general population (p = 0.011). Among the pathological and non-pathological cases of gambling in the football population, significant differences were found between those with a salary of EUR 900-1500/month (p = 0.027) or a history of a nervous pathology (p = 0.021). (4) Conclusions: This study showed that professional football players were vulnerable to mental health pathologies related to gambling.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Survey of footballers and general population reporting probable gambling disorder; the abstract doesn't say whether sports betting participation was measured.

**Решение:** =

---

### 292 · R1650

**Assessing harm severity: a Rasch analysis of the gambling harm measure**

2025 · International Gambling Studies · article · en · https://doi.org/10.1080/14459795.2025.2486122

The Gambling Harm Measure (GHM) is a 16-item self-report instrument used to measures gambling-related harm (GRH) across its six principal domains. Unlike other GRH measures, the GHM uses multiple items to assess harm along a gradient of within each of its principle domain (excluding illegal acts). The objective of this study was to evaluate this severity gradient using Rasch analysis. Data from 2,941 respondents were obtained from three independent surveys, two conducted in the American state of Massachusetts and one conducted nationally across Canada. Item thresholds varied within each domain, providing evidence that the GHM can capture harm across a gradient of severity. There was evidence of differential item functioning (DIF), with younger adults and those participating in more harmful gambling formats (e.g. electronic gambling machines, casino table games) being more likely to endorse several items on the GHM. Finally, we identified three discrete categories of GHM scores: mild harm included individuals endorsing 1–6 items; high harm included individuals endorsing 7–13 items; and severe harm included individuals endorsing 14 or more items. This study provides support for the GHM as a valid measure of GRH that can capture both the range and severity of harm experienced by individuals who gamble.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Gambler surveys with gambling formats measured; the harm measure is not a PG screen, so it's unclear whether PGSI or a similar screen and sports betting were captured.

**Решение:** =

---

### 293 · R1651

**Correlates of Problem Gambling in Canada: The Moderating Effect of Sex.**

2025 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-025-10404-z

Numerous studies report sex differences in the prevalence of problem gambling (PG), but the etiological basis of these differences across recognized risk factors is unclear. Data from a large, nationally-stratified Canadian survey (n = 10,044) were used to explore whether sex moderates relationships between PG and its risk factors, including (1) gambling participation, (2) gambling motivations, (3) mental health, and (4) substance use. The sample was 53.6% female, had a mean age of 52.4 years (SD = 15.4), and 61.8% had Northern/Western European heritage. The magnitude of the relationship between sixteen (44%) study variables and PG varied between sexes, though these effects were generally small. These variables include: (1) past month participation in lotteries, electronic gambling machines, sports betting, bingo, and financial speculation; (2) all measures of gambling intensity (breadth, frequency, expenditure); (3) enhancement and coping motivations for gambling; and (4) five additional substance use and mental health variables. With the exception of past month bingo participation, posttraumatic stress disorder, history of substance-related problems, negative life events, and impulsivity, these effects were larger for females relative to males. Finally, multivariate analyses revealed notable differences in the risk factors for PG, with variation in male PG being uniquely explained by gambling to develop skill, substance use disorder, negative life events, and age, and variation in female PG being uniquely explained by online gambling, breadth of gambling involvement, and coping motives. These findings highlight potential sex-specific pathways to PG that should be the subject of future research.

**ИИ:** + · обе модели · игроки, есть ставки на спорт и инструмент · Large Canadian national survey measuring PG and past-month sports betting participation; it could report PG among sports bettors.

**Решение:** =

---

### 294 · R1662

**Alcohol use frequency relates to elevated sports betting engagement, risk-taking, and negative consequences in a year-long biweekly study of young adults.**

2025 · Addictive behaviors · article, journal article, journalarticle · eng · https://doi.org/10.1016/j.addbeh.2025.108359

Background: Sports betting is a rapidly growing addictive behavior that has been cross-sectionally linked to other risky behaviors including alcohol use. To better understand how alcohol use contributes to sports betting engagement, risk-taking, and negative consequences, the present study examined within-person associations using 26 repeated biweekly assessments. Method: A sample of 210 U.S. young adult sports bettors (aged 18–29) reported alcohol use frequency and sports betting behaviors every other week for a full year. Generalized linear mixed models disentangled between- and within-person associations. Results: Within-person fluctuations in alcohol use frequency were significantly related to sports betting engagement (i.e., frequency Rate Ratio = 1.08, total bets RR = 1.09), high-risk betting behavior (i.e., total amount wagered RR = 1.09, chasing losses RR = 1.08), and negative sports betting consequences (RR = 1.11). Across each outcome, the between-person effects of alcohol use frequency were non-significant, suggesting that alcohol use and gambling behavior may not simply be a trait- or person-level clustering as previously theorized. Alternatively, alcohol use may more directly impact young adults’ sports betting behavior through fluctuating and dynamic processes, potentially driven by the dysregulating effects of alcohol. Conclusions: The evolving sports betting landscape increasingly emphasizes high-risk and impulsive behaviors such as live/in-game betting, which presents unique opportunities for alcohol to adversely impact one’s sports betting behavior. Findings highlight the need for policy and prevention strategies that effectively decouple alcohol use from sports betting, as the combination of these behaviors can amplify risks and consequences.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Longitudinal sample of young adult sports bettors; negative consequences measured, but the abstract doesn't say whether a standard PG screen (e.g., PGSI) was used.

**Решение:** =

---

### 295 · R1663

**Sports Gambling and Drinking Behaviors Over Time.**

2025 · JAMA psychiatry · article, journal article, journalarticle · eng · https://doi.org/10.1001/jamapsychiatry.2025.0024

Importance: Sports gambling has become one of the most accessible forms of gambling in the United States, and recent research suggests that sports gambling coupled with frequent alcohol use may have deleterious health consequences. Objective: To examine the trajectories of sports gambling frequency and alcohol-related problems over time and the associations between these trajectories. Design, Setting, and Participants: This survey study was a 2-year longitudinal study conducted in the United States. Participants were recruited from a nonprobability internet panel from 2 sources: a large cross-section of adults matched and weighted to US Census norms and a specific oversample of sports-gambling adults. Recruitment began in spring 2022, and the last surveys concluded in spring 2024. To identify trajectories within sports gambling frequency and alcohol use problems, latent growth curve modeling was used. Main Outcomes: At each time point, the National Institute on Drug Abuse-modified Alcohol, Smoking, and Substance Involvement Screening Test 2 was used to assess alcohol-related problems and sports gambling frequency was assessed by a single item. Results: The cross-section of US adults (n = 2806) and oversample of sports-gambling adults (n = 1557) resulted in a total baseline sample of 4363 (mean [SD] age, 49.6 [16.2] years; 2243 men [51.4%] and 2120 women or nonbinary gender reported [48.6%]). Latent growth curve modeling revealed that alcohol problems decreased over time (slope = -0.059; 95% CI, -0.090 to -0.028). Sports gambling frequency did not show a significant trend over time (slope = -0.003; 95% CI, -0.053 to 0.047), though there was significant variance in this slope (variance = 0.024; 95% CI, 0.013 to 0.034). The trajectories of alcohol-related problems and sports gambling did not move independently, instead being highly positively correlated, suggesting that increases in one would correspond to increases in the other. Conclusions and Relevance: This study found that over time, the trajectory of sports gambling frequency was associated with the trajectory of alcohol-related problems. Screening and treatment interventions are recommended for sport gamblers who also drink concurrently, especially because this group appears to be at an elevated risk for developing greater alcohol-related problems over time.

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Longitudinal US survey with a sports-gambler oversample; the abstract names only alcohol screening, but the panel may also have measured problem gambling.

**Решение:** =

---

### 296 · R1665

**Health risk behaviours, obesity, and gambling severity: findings from a nationwide population study**

2025 · European Journal of Public Health · article · en · https://doi.org/10.1093/eurpub/ckaf216

Prior research on the relationship between health risk behaviours (HRBs), obesity, and gambling has primarily focused on problem gambling, while studies focusing on lower severity levels are scarce. Moreover, this relationship has rarely been analysed separately for women and men. This study aimed to investigate the association between HRBs, obesity, and the full spectrum of gambling severity in women and men. Cross-sectional population-based data from Healthy Finland Survey 2022-23 was exploited, including adults aged 20+ years (n = 28 154, response rate 46%, mean age 52 years). The Problem Gambling Severity Index (PGSI) was used as the dependent variable, both in continuous (score 0-27) and categorical (non-problem, low-risk, moderate-risk, and problem gambling) form. Independent variables included HRBs (daily smoking, excessive drinking, low fruit and vegetable (F & V) consumption, low physical activity, and insufficient sleep) and obesity. Sociodemographic factors, suboptimal self-rated health, and psychological distress were adjusted for. Daily smoking, excessive drinking, low F & V consumption, and insufficient sleep were less prevalent in the non-problem gambling category (PGSI score = 0) compared to the low-risk (score 1-2), moderate-risk (score 3-7), and problem gambling (score ≥8) categories. After adjusting for potential confounding variables, all HRBs and obesity, except for physical inactivity, were significantly associated with higher PGSI scores. These findings highlight the need for public health strategies that address gambling across the entire risk spectrum. Moreover, a holistic approach that considers the individual's broader life context could strengthen both research and prevention efforts.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Finnish nationwide population survey using PGSI; unclear whether participation in gambling activities such as sports betting was measured.

**Решение:** =

---

### 297 · R1673

**Social media advertising of gamified problem gambling: a mixed-method analysis of the advertising nexus and financial motivation of Gen Zs**

2025 · Journal of Social Media Research · article, journalarticle · en · https://doi.org/10.29329/jsomer.53

Gamified Problem Gambling (GPG) is an increasingly popular trend in Africa, with many young individuals using numerous gambling apps. Numerous studies have identified Social Media Advertising (SMA) as the primary channel for raising awareness and driving participation in GPG. The desire to become rich overnight has been a strong motivator for Gen Zs to engage in GPG, as other studies have found. Consequently, this research aimed to investigate how SMA of GPG influences the financial motivation of Gen Zs and the extent to which Trust, Affect, and Loyalty mediate the nexus. The Cognitive Theory of Gambling, the Relative Deprivation Theory, and the Weak Theory all contribute to the theoretical underpinning for this study. This study adopted the Explanatory Sequential Mixed-Method and Quota sampling techniques to collect data from 617 Ghanaian university students. The results were analyzed using PLS-SEM and NVivo (v. 14). The findings revealed that SMA of GPG has a significant impact on FM. Loyalty, Affect, and Trust of Gen Zs strongly mediate the nexus between SMA of GPG and FM to patronize sports betting. The study contributes to the literature on SMA and GPG and recommends that, to ensure sports betting companies remain in business, they must address the concerns of Gen Z bettors as revealed in this study and respond accordingly, since they are their major clients.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Survey of 617 Ghanaian student sports bettors on advertising and motivation; 'problem gambling' in title but no standard screening instrument mentioned.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Survey of Ghanaian students on social media advertising and financial motivation for sports betting; no problem-gambling instrument evident, only PLS-SEM of attitudes and motives.)

**Решение:** ?

---

### 298 · R1677

**Lonely gamble – A longitudinal study of loneliness, gambling to escape and problem gambling**

2025 · Journal of Behavioral Addictions · article · en · https://doi.org/10.1556/2006.2025.00025

Background and Aims: The evidence concerning the relationships between loneliness, gambling to escape, and problem gambling is mixed. This study aimed to investigate how loneliness relates to gambling to escape and gambling problems using a longitudinal approach. Method: This population-based, longitudinal study included five time points, with data having been collected between April 2021 (T1) and April-May 2023 (T5). Participants were 18-75-year-old Finnish residents. Only those who had taken part in the study at each time point (T1-T5) and had gambled at least once a month at some point in the follow-up period were included in the study (n = 612; 54.58% male; Mage = 51.85 years). Loneliness was measured with the UCLA 3-Item Loneliness Scale, and gambling to escape was measured with three questions concerning negative escapism taken from the Motivations to Play Inventory. Problem gambling was measured using the Problem Gambling Severity Index (PGSI). Random intercept cross-lagged panel modeling was used to analyze the relationships. Results: Gambling problems predicted future loneliness on a within-person level, but loneliness did not predict future gambling problems. Also, gambling to escape predicted future gambling problems on a within-person level. On a between-person level, loneliness, gambling to escape and gambling problems were positively correlated. Discussion and Conclusion: Gambling problems may predispose individuals to future loneliness. However, the relatively small effects observed indicate that individual differences play a significant role in this regard.

**ИИ:** ? · обе модели · неясно, есть ли ставки на спорт · Population-based Finnish longitudinal gambler sample with PGSI; unclear whether sports betting participation was measured or reported.

**Решение:** =

---

### 299 · R1682

**Bet More - But Only with Me: Role of Celebrity Endorsers in Sports Betting Advertising.**

2025 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-025-10399-7

Abstract Since the federal ban on sports betting was lifted in 2018, the industry has grown rapidly in the United States, raising concerns about the risk of problem gambling. Building on existing research that suggests the limited effectiveness of traditional responsible gambling campaigns, the current study examines whether the use of celebrity endorsers in advertising can enhance responsible gambling intentions. Using a scenario-based experiment with 383 U.S. sports bettors, regression analyses reveal that an endorser whose image aligns with the target audience increases consumer awareness of responsible gambling messages, thereby enhancing intentions to gamble responsibly. In addition, an image-congruent endorser boosts consumers’ betting intentions and word-of-mouth advocacy for the sportsbook. Although image congruence in advertising is often operationalized through racial similarity, the findings suggest that same-race endorsers are effective in enhancing image congruence only when sports betting is perceived as socially acceptable. This study is the first to examine the effect of endorser-consumer image congruence on consumer intentions toward both sports betting brands and responsible gambling. The findings provide important insights to sportsbooks aiming to balance branding and social responsibility in marketing campaigns.

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Experiment with 383 US sports bettors on advertising and intentions; the full text might use PGSI as a covariate or to describe the sample.); Sonnet -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Experiment on celebrity endorsers and responsible gambling intentions among sports bettors; no problem-gambling instrument is mentioned, only intentions and advertising effects.)

**Решение:** -

---

### 300 · R1689

**Impact of cash-out availability in a naturalistic betting task: A randomized experimental study**

2025 · PsyArXiv · article, preprint, posted-content · en · https://doi.org/10.31234/osf.io/2z3eu_v2

Background and Aims: People place larger bets on outcomes of risky events when they can settle their bet earlier – i.e., they are allowed to cash-out before the bet concludes. Using a naturalistic gambling task, the present study aims to determine how the opportunity to cash-out impacts the decision to bet and to assess the underlying association between cash-out availability and risk of gambling harm.Design and setting: We conducted an incentivised between-participants online experiment, where participants could place fixed-odds bets on the outcomes of pre-recorded horse races via an interface resembling a commercial bookmaker’s website. Participants were randomly assigned to conditions in which the cash-out was either available or not available to them and were given the option to gamble an endowment that they had previously earned in a real-effort task.Cases: 377 participants with experience in online sports betting were recruited from online research participation platform Prolific. Measurements: The decision to engage with the gambling task was recorded at 3 points during the experimental session. Stake sizes and implied win probabilities of placed bets were recorded. Risk of gambling harms was measured by administering the PGSI.Results: People in the cash-out-available group were more likely to choose the gambling task over a distractor (non-gambling) game (χ²(1, N=377)=4.59, p=0.032) and made larger bets when wagering than those in the no-cash-out group (W=19761.5, p=0.021). There was no effect of the manipulation on the average odds of bets placed (W=10635.5, p=0.67). No significant interactions with PGSI were observed for either stake size (β=-0.02, SE=0.02, p=0.15) nor the implied win probability of placed bets (β&amp;lt;0.01, SE&amp;lt;0.01, p=0.44). Participants in the cash-out-available group engaged with the gambling task for longer than participants in the no-cash-out group (β=0.65, SE=0.23, p=0.0047). Conclusions: The provision of cash-out options in horse race betting results in significant changes in betting behaviour. These behaviours can lead to gambling harms, pointing towards the potential risks of the cash-out option.

**ИИ:** + · обе модели · беттеры + инструмент · Online experiment with 377 people who had online sports betting experience; PGSI given, so the distribution of PGSI categories is probably reported.

**Решение:** =
