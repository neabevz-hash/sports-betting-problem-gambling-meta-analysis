# Проверка с метками ИИ, часть 11

Записи 1501–1525 из 1525, с метками обеих моделей над строкой решения. Модели согласны и вы тоже — поставьте `=`; иначе свой код (`+`, `?` или `-`, причина не нужна). Если модели разошлись, `=` не годится — нужен ваш код. Решаете вы. Последние 25 — калибровочные записи, где ваша слепая метка разошлась с правилом ИИ: она показана над метками.

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

### 1501 · R1597

**The Mediating Role of Mental Health in the Relationship Between Gambling Severity and Suicidal Ideation: A Study with Clinical and General Population**

2025 · International Journal of Mental Health and Addiction · article · en · https://doi.org/10.1007/s11469-025-01503-4

Abstract Gambling is a public health problem that affects many people in many ways. One of the most serious effects is on people's mental health and suicidal ideation. This study has two main aims: 1) To analyse the differences between the clinical population (i.e., individuals with gambling disorder) and the general population in terms of gambling severity, suicidal ideation, and mental health; and 2) to test the mediating role of mental health in the relationship between gambling severity and suicidal ideation in people with gambling disorder and the general population. A total of 318 participants were included in the study: 153 gamblers undergoing treatment for gambling disorder ( M age = 44.38, SD = 12.48, 81% males) and 165 individuals from the general population ( M age = 47.57, SD = 13.52, 26.67% males). Two structural equation models were conducted to test the mediating role of mental health issues (i.e., depression, anxiety, hostility, somatisation, and obsessive–compulsive) in the relationship between gambling severity and suicidal ideation. The results show no significant differences in mental health between the population with gambling disorder and the general population. However, the relationship between gambling severity and suicidal ideation appears to be mediated by mental health, both in the clinical and general populations. Findings show the importance of addressing mental health to prevent suicidal ideation. Given the high prevalence of suicidal ideation in individuals with gambling disorder, the assessment and treatment of gambling problems and mental health is strongly recommended. Results also highlight the importance of transdiagnostic protocols that address mental health, with a particular focus on suicidal ideation.

**Ваша слепая метка (калибровка):** ? опрос с инструментом PG в общей и клинической выборках, проверить выделение ставок на спорт в полном тексте

**ИИ:** -5 · обе модели · выборка набрана по проблемам с игрой: лечение, горячая линия, самоисключение, сравнение проблемных игроков с контролем · Compares treatment-seeking gambling disorder patients with general population controls; no mention of sports betting participation.

**Решение:** ?

---

### 1502 · R1603

**More frequent use of live sports-betting features is associated with increased risk of gambling harm: evidence from a case- control design**

2025 · PsyArXiv · preprint, posted-content · en · https://doi.org/10.31234/osf.io/je38f_v1

BackgroundMany theories of gambling harm propose that interactive design features of sports-betting platforms confer risk of harm by enabling cyclical patterns of repeated gambling engagement. This exploratory study investigated whether such features were used more frequently by people at higher risk of gambling harm relative to a demographically matched lower-risk control group.MethodsThis study used a case-control design to compare a group of 85 people at higher risk of gambling harm (PGSI 5+) with an age- and gender-matched control group at lower risk of harm (n = 84, PGSI 0-4). We compared the frequency with which groups self-reported using in-play betting, instant cash-out, multi and micro bets, social betting, and viewing live-streamed events within a betting app.ResultsThe higher-risk group reported more frequent use of in-play betting and instant cash-out and were more likely to report streaming live sporting events within a betting app. Higher-risk participants were also more likely to make an immediate deposit to qualify for a marketing offer, and both groups reported being more likely to make risky bets when using bonus funds. We observed no group differences in the frequency of use of multis, micro-bets, or social betting.ConclusionsOur findings were broadly consistent with the theory that design features of modern betting platforms contribute to gambling harm by facilitating continuous engagement. A notable finding was that in-app streaming of live events was more common among people at higher risk of gambling harm, consistent with a novel prediction made by the motivating theory.

**Ваша слепая метка (калибровка):** -5 исследование дизайна случай-контроль по степени риска гемблинга

**ИИ:** разошлись — Opus ? (другое: Sports bettors were sampled into matched groups by PGSI score, so prevalence in this sample is artificial. The PGSI distribution of the full screened pool might be reported.); Sonnet -5 (выборка набрана по проблемам с игрой: лечение, горячая линия, самоисключение, сравнение проблемных игроков с контролем: Case-control design recruiting matched groups by PGSI (5+ vs 0-4) among sports bettors; sampling by problem status means prevalence cannot be estimated.)

**Решение:** -

---

### 1503 · R1712

**Author response of: Impulsivity and online sports betting behavior: Untangling the causal relationship. Round#1**

2025 · Peer Community In Registered Reports · journalarticle, review, journal-article · en · https://doi.org/10.24072/pci.rr.100996.ar1

A recommendation of: Anne Jacob, Mohsen Joshanloo, Robert Czernecka, Anja Kräplin Impulsivity and online sports betting behavior: Untangling the causal relationship https://pada.psycharchives.org/bitstream/ed85321f-28e5-42dd-8f97-cf1cfce9e5d8

**Ваша слепая метка (калибровка):** -1 рецензия / ответ авторов на зарегистрированный отчет

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Peer-review author response for a registered report on online sports bettors' impulsivity; unclear whether the underlying study used a problem-gambling instrument.

**Решение:** -

---

### 1504 · R1940

**Relationship between Socio-Demographic Factors and Sports Betting among Football Fans in Satellite Television Football Viewing Centres in Osogbo, Osun State, Nigeria**

2025 · International Journal of Innovative Research and Development · article, journalarticle, review · und · https://doi.org/10.24940/ijird/2025/v14/i7/jul25012

Sports betting makes an incursion into the nooks and crannies of society and propagates capitalism in some ways. As such, it has shown far-reaching negative implications on the individual, family, community and society. The habitual betting problem affects a quantifiable extent of youth players and may show in both mental and physical conditions. Despite this, there is a dearth of studies on sports betting; specifically, a Descriptive survey research design was adopted. A simple random sampling technique was used to select the respondents, while a self-developed questionnaire was used for data collection. Descriptive statistics, including frequency counts and percentages, and the inferential Pearson product-moment correlation coefficient, were used to test the hypotheses. This study, therefore, examined the relationship between socio-demographic factors and betting in sports among football fans in satellite television football viewing centres in Osogbo, Osun State. The results revealed a significant positive relationship between peer influence and sports betting among football fans in satellite television football viewing centres in Osogbo, Osun State. The results also revealed that age relations did not have a significant positive relationship with sports betting among football fans in satellite television football viewing centres in Osogbo, Osun State (r = 0.028, p &gt; 0.05). Furthermore, educational level had a significant positive relationship with sports betting among football fans in satellite television football viewing centres (r = 0.368, p &lt; 0.05). Occupation did not have a significant positive relationship with sports betting among football fans in satellite television football viewing centres (r = 0.192, p &gt; 0.05). Gender had a significant positive relationship with sports betting among football fans in satellite television football viewing centres (r = 0.468, p &lt; 0.05). The findings of this study revealed that educational level and gender had a significant positive relationship with sports betting among football fans in satellite television football viewing centres in Osogbo, while age relations and occupation did not. The government and other relevant stakeholders should therefore ensure that fans in satellite television football viewing centres in Osogbo are enlightened on the negative consequences of sports betting.

**Ваша слепая метка (калибровка):** ? опрос футбольных болельщиков о ставках на спорт, проверить наличие инструмента PG в полном тексте

**ИИ:** -3 · обе модели · нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора · Survey of football fans using a self-developed questionnaire on socio-demographic correlates of sports betting; no problem-gambling instrument reported.

**Решение:** ?

---

### 1505 · R2077

**Fear of missing out’s mediating role in sensation-seeking and online betting intentions: impact of sales promotions**

2025 · Sport Business and Management An International Journal · article, journalarticle, review · en · https://doi.org/10.1108/sbm-05-2024-0054

Purpose This research investigates the complex relationships between individual psychological traits, the fear of missing out (FOMO) and sales promotions in the online sports betting industry. Specifically, it aims to comprehend how sensation-seeking, as a personality trait and FOMO influence the intention to engage in instant online sports betting under various sales promotions like win-bet boosting and lose-bet protecting. Design/methodology/approach An online survey was conducted with USA adults familiar with major online betting platforms. Participants were assigned to different promotional scenarios, and their responses were analyzed using partial least squares structural equation modeling (PLS-SEM). Findings The findings show that sensation-seeking positively affects betting intentions, with FOMO playing a partially mediating role. Sales promotions were found to negatively moderate the relationship between sensation-seeking and betting intention. Notably, the impact of FOMO on betting intention was stronger in the lose-bet protecting scenario than in the win-bet boosting scenario. Originality/value This research enriches existing literature by elucidating the nuanced interactions between sensation-seeking, FOMO and sales promotions in the context of online sports betting. The study offers practical insights for developing targeted marketing strategies, particularly for users inclined towards sensation-seeking.

**Ваша слепая метка (калибровка):** ? опрос о факторах намерения делать ставки, проверить наличие инструмента PG в полном тексте

**ИИ:** -3 · обе модели · нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора · Marketing survey of betting intentions, sensation-seeking and FOMO under promotional scenarios; no problem-gambling instrument mentioned.

**Решение:** ?

---

### 1506 · R2319

**Examining the causal pathways from impulsivity to disordered gambling in online sports betting**

2024 · Peer Community In Registered Reports · journalarticle, review, article · en · https://doi.org/10.24072/pci.rr.100574

A recommendation of: Anne Jacob, Mohsen Joshanloo, Robert Czernecka, Anja Kräplin, Impulsivity and online sports betting behaviour: Untangling the causal relationship (ISPO study) http://dx.doi.org/10.23668/psycharchives.14372

**Ваша слепая метка (калибровка):** -1 рецензия / рекомендация на зарегистрированный отчет по импульсивности и ставкам

**ИИ:** ? · обе модели · другое · PCI RR recommendation (commentary) on the ISPO study of online sports bettors' disordered gambling; check linked study for PG data.

**Решение:** -

---

### 1507 · R2665

**Seniors and Gambling**

2024 · Elsevier BV · posted-content, preprint · en · https://doi.org/10.2139/ssrn.4770475

Online sports gambling is increasing at a rapid pace. This is due to changes in the law allowing online betting, the prolific increase of online platforms, and aggressive marketing campaigns. Sports betting is legal in 38 states and Washington, D.C. as of March 2024. The elderly population is especially at risk for this platform as they do not need to leave their homes.

**Ваша слепая метка (калибровка):** -1 аналитический комментарий об уязвимости пожилых людей перед ставками

**ИИ:** ? · обе модели · другое · Preprint on seniors and online sports betting; the abstract reads like a commentary but doesn't rule out a survey with a problem-gambling measure.

**Решение:** -

---

### 1508 · R3865

**Why Do Individuals Engage in In-Play Sports Betting? A Qualitative Interview Study.**

2021 · Journal of gambling studies · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10899-020-09968-9

Abstract Increasing technological advancements and changing consumer behavior has resulted in individuals having access to a wider range of online gambling markets and sporting events than ever before. Sports betting in real time has been aided by the accessibility of smartphone devices. Consequently, the popularity of live sports betting (i.e., ‘in-play’ betting) has spread across Europe and around the rest of world. The aim of the present exploratory study was to examine attitudes and opinions towards online sports betting. Qualitative interviews were conducted with 17 males and 2 females aged between 21 and 32 years. Participants were asked a range of semi-structured interview questions based on pre-determined topic areas. Socio-demographic data were collected and the Problem Gambling Severity Index (PGSI) was used to assess problem gambling. The data were analyzed using thematic analysis in order to identify themes. Analysis of the transcripts identified several notable areas including the ease of engaging in in-play sports betting, motivations for engaging in in-play sports betting (including increased excitement, demonstrating knowledge/skill and response to live odds), and different reasons for using the ‘cash-out’ feature. The findings will contribute to the design of future research investigating in-play sports betting behaviours.

**Ваша слепая метка (калибровка):** -2 качественное феноменологическое исследование лайв-ставок без опроса

**ИИ:** ? · обе модели · другое · Qualitative interviews with 19 in-play sports bettors, but the PGSI was given, so the full text may report problem-gambling counts.

**Решение:** -

---

### 1509 · R4134

**Fiche 26. Les paris sportifs**

2020 · Cairn.info · book-chapter · fr

_Аннотации нет — решайте по названию или ставьте `?`._

**Ваша слепая метка (калибровка):** -1 справочная карточка по спортивным ставкам

**ИИ:** разошлись — Opus -1 (обзор, комментарий, теоретическая, правовая или регуляторная работа: A numbered summary sheet ('fiche') in a textbook is likely a teaching overview, not primary empirical research.); Sonnet ? (нет аннотации: French book chapter "Sports betting" fact sheet with no abstract; likely a descriptive overview, but empirical problem-gambling data cannot be ruled out.)

**Решение:** -

---

### 1510 · R4921

**Gambling in Greenlandic adolescents.**

2019 · International journal of circumpolar health · journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1080/22423982.2019.1577094

Gambling has never been investigated in Greenlandic adolescents. High prevalence of gambling problems and a relation to other addictive behaviours has been found in adult Greenlanders. Greenlandic adolescents are daily exposed to gambling, for example, by selling lottery tickets, through advertises and electronic devices. The aim of this study is to investigate how Greenlandic adolescents perceive gambling, and to pilot test the Lie/Bet screening-instrument.Ten semi-structured focus group interviews were conducted for 31 adolescents, aged 12-16, from 3 schools in Nuuk, Greenland.The 31 adolescents have experiences with gambling. Whether they define a game as gambling depends on: 1) Whether the game is about playing with or about money, 2) whether the game is about earning items, 3) the gain/loss, 4) who they lose money to, and 5) the purpose. If the purpose is to have fun, it is not necessarily seen as gambling. None mentioned bingo as gambling, arguing that bingo is about having fun. Two recent trends were found to have reached Greenland: The close link between sports and gambling, and skin-betting. Additionally, the Lie/Bet screen was, with slight modifications, found to be useful as a screening-instrument among Greenlandic adolescents and it is proposed to be used in future studies.

**Ваша слепая метка (калибровка):** ? качественное исследование и пилотный тест скрининга Lie/Bet, проверить полный текст

**ИИ:** -2 · обе модели · качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи · Focus group study of 31 adolescents. Lie/Bet was only pilot-tested qualitatively, with no prevalence survey.

**Решение:** ?

---

### 1511 · R4951

**Is real-money mobile gaming a form of gambling or video gaming?**

2019 · PsyArXiv · article, other literature type, preprint · en · https://doi.org/10.31234/osf.io/9wp5h

Several new mobile video games have recently hit the market which allow players to wager real-world money on their in-game performance. For example, players of Strike! eSports Bowling can bet up to $60 before playing each game of ten-pin bowling, in the hopes of winning up to $100 in cash should they beat their opponent. Similarly, players of Block Blitz can place real money wagers on the outcomes of the Tetris-style puzzle games that they play. In the same vein, players of Pro Pool can stake real money on the chance of beating their opponent in a simulated game of 8 ball pool, in the hopes of winning a large cash prize. Real money stakes on this game range from $0.60 to $30.A significant amount of recent research has dealt with the emergence of links between gambling and video games. This attention has focused on topics as diverse as loot boxes, skin gambling, and esports betting. However, real-money mobile gaming has received little scrutiny.

**Ваша слепая метка (калибровка):** ? препринт о ставках в мобильных играх и киберспорте, проверить полный текст

**ИИ:** -1 · обе модели · обзор, комментарий, теоретическая, правовая или регуляторная работа · Commentary on real-money mobile skill-based gaming; no survey of people, no sports betting or problem-gambling data.

**Решение:** ?

---

### 1512 · R5376

**The influence of marketing on the sports betting attitudes and consumption behaviours of young men: implications for harm reduction and prevention strategies.**

2017 · Harm reduction journal · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1186/s12954-017-0131-8

BACKGROUND: Gambling can cause significant health and social harms for individuals, their families, and communities. While many studies have explored the individual factors that may lead to and minimise harmful gambling, there is still limited knowledge about the broader range of factors that may contribute to gambling harm. There are significant regulations to prevent the marketing of some forms of gambling but comparatively limited regulations relating to the marketing of newer forms of online gambling such as sports betting. There is a need for better information about how marketing strategies may be shaping betting attitudes and behaviours and the range of policy and regulatory responses that may help to prevent the risky or harmful consumption of these products. METHODS: We conducted qualitative, semi-structured interviews with 50 Australian men (aged 20-37 years) who gambled on sports. We explored their attitudes and opinions regarding sports betting marketing, the embedding of marketing within sports and other non-gambling community environments, and the implications this had for the normalisation of betting. RESULTS: Our findings indicate that most of the environments in which participants reported seeing or hearing betting advertisements were not in environments specifically designed for betting. Participants described that the saturation of marketing for betting products, including through sports-based commentary and sports programming, normalised betting. Participants described that the inducements offered by the industry were effective marketing strategies in getting themselves and other young men to bet on sports. Inducements were also linked with feelings of greater control over betting outcomes and stimulated some individuals to sign up with more than one betting provider. CONCLUSIONS: This research suggests that marketing plays a strong role in the normalisation of gambling in sports. This has the potential to increase the risks and subsequent harms associated with these products. Legislators must begin to consider the cultural lag between an evolving gambling landscape, which supports sophisticated marketing strategies, and effective policies and practices which aim to reduce and prevent gambling harm.

**Ваша слепая метка (калибровка):** -2 качественное исследование влияния маркетинга на ставки среди молодежи

**ИИ:** разошлись — Opus ? (неясно, измеряли ли проблемную игру: Qualitative interviews with 50 male sports bettors; studies in this series may have used PGSI to describe the sample, so check the full text.); Sonnet -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: Qualitative semi-structured interviews with 50 young Australian male sports bettors about marketing; no problem-gambling instrument or prevalence data.)

**Решение:** -

---

### 1513 · R5441

**To i?nvesti?gate the relati?onshi?p between the moti?vati?on to watch sport and the moti?vati?on to bet i?n those who parti?ci?pate i?n sport betti?ng**

2017 · Niğde Üniversitesi Açık Erişim Sistemi · dissertation · tr

Bu araştırmada spor bahisi oynayan seyircilerin seyretme güdüleri ile bahis oynama motivasyonları arasındaki ilişkilerin incelenmesi amaçlanmıştır. Betimsel yöntem ve ilişkisel tarama modelinin kullanıldığı bu çalışma, toplanılan veriler anket yöntemiyle elde edilmiştir. Araştırmanın örneklem grubunu Niğde ilinde yaşayan spor bahis oyunlarına katılan spor müsabakaları izleyen seyircilerden oluşmuştur. Bahis oynayan spor müsabaka seyircileri hakkında kayıtlı bir veri bulunmadığından anket dağıtımı sırasında katılımcıların bahis oyunlarına katılıp katılmadıkları sorularak örneklem grubu oluşturulmuştur. 345 adet anket dağıtılmıştır ve doğru doldurulan 327 anket değerlendirilmeye alınmıştır. Araştırmada, veri toplama aracı olarak 4 ana bölümden oluşan bir anket kullanılmıştır. Birinci bölümünde Polat ve Yalçın (2017) tarafından geliştirilen, 7'li likelt şeklinde ve 25 maddeden oluşan Spor Seyircileri için Dışsal Güdü Ölçeği, ikinci bölümünde yine (Polat ve Yalçın, 2017) tarafından geliştirilen, 7'li likelt şeklinde ve 21 maddeden oluşan Spor Seyircileri İçin İçsel Güdü Ölçeği, üçüncü bölümde (Chantal, Vallerand ve Vallieres, 1994) tarafından geliştirilen ve (Karlı, 2008) tarafından Türkçe'ye uyarlanan, 5'lilikelt şeklinde ve 28 maddeden oluşan Bahis Güdülenme Ölçeği, dördüncü bölümde ise kişisel bilgi formu yer almaktadır. Verilerin analizinde SPSS paket programı kullanılmıştır. Öncelikle değişkenlere ait Kolmogov-Smirno ve Shapiro-Wilk normallik dağılım istatistiği yapılmıştır (Tablo 3.1). Elde edilen sonuçlara dayanak tüm hipotez testleri için nonparametrik test kararı alınmıştır. Sonrasında bazı tanımlayıcı istatistiklere ilişkin yüzde frekans dağılımları, ortalama ve yaygınlık sonuçları verilmiştir. Gruplar arası ikili kategorik karşılaştırmalar için Mann Whitney U testi, çoklu kategorik karşılaştırmalar için ise Kruskall Wallis H testi yapılmıştır. Ayrıca sürekli veri niteliğindeki bağımsız değişkenler ve ölçüm araçları alt boyutları arası ilişkiler için Spearman Kolerasyon Analizinden yararlanılmıştır. Elde edilen bulgular sonucunda bağımsız değişkenlerin (cinsiyet, yaş, aylık ortalama gelir, spor müsabakası için aylık ortalama harcama, bahis oynanan branş, bahis oynama süresi, bahis oynamak için aylık ortalama harcama, aktif spor yapma durumu, bir branş takımı tutma, taraftarlık düzeyi) bahis motivasyonu, spor müsabakalarını dışsal seyretme sebepleri ve spor müsabakalarını içsel seyretme sebeplerinden bazılarını etkilediği söylenebilir. Ayrıca bahis oynama motivasyonu arttıkça seyretme güdülerinin de arttığı söylenebilir.

**Ваша слепая метка (калибровка):** ? опрос спортивных беттеров о мотивах, проверить наличие опросника PG в полном тексте

**ИИ:** -3 · обе модели · нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора · Survey of sports bettors whose four questionnaire sections were watching-motive scales, a betting motivation scale and demographics; no problem-gambling instrument.

**Решение:** ?

---

### 1514 · R5685

**The Fantasy Sport Industry: Games Within the Games**

2016 · International Journal of Sport Communication · article · en · https://doi.org/10.1123/ijsc.2016-0056

_Аннотации нет — решайте по названию или ставьте `?`._

**Ваша слепая метка (калибровка):** -1 рецензия / обзор индустрии фэнтези-спорта

**ИИ:** разошлись — Opus -1 (обзор, комментарий, теоретическая, правовая или регуляторная работа: Title matches the Billings & Ruihley book; a journal record with no abstract is most likely a book review, not empirical data.); Sonnet ? (нет аннотации: No abstract; fantasy sport industry paper in a sport communication journal, likely a review or commentary, but could include a survey of players with a problem-gambling measure.)

**Решение:** -

---

### 1515 · R5800

**Parents’ Perception of Youth Gambling and Other Risk Behaviors**

2016 · Digital Scholarship - UNLV (University of Nevada Reno) · article, conference object, conference-paper · en · http://www.library.unlv.edu/system/files/webform/ir/files/ppt_kranzelic_et_al_las_vegas_2016.pdf

Recently conducted national prevalence study of youth gambling in Croatia indicated high prevalence of adolescent gambling (especially sports betting), as well as perceived parental acceptance of such behavior (Ricijas et al, 2011). As international research suggest positive correlations between parental perception of gambling and other risk behaviors with the intensity of their childrens' participation in these behaviors (Meerkamper, Derevensky, Cutajar, 2008; Farrington, Loeber, Ttofi, 2011; Cambell et al, 2011), a new study on parental perception of gambling is currently being conducted, using two comparable perspectives - parents and their adolescent children.\nResearch is being conducted in two largest Croatian cities (Zagreb and Split) from October to December 2015 with expected sample of approximately N=400 parents and their adolescent children. The following instruments are being used: (1) Questionnaire on basic socio-demographic characteristics, (2) Parents as Partners Gambling Research Study (Derevensky, 2008) and (3) Gambling Activities Questionnaire.\nThe analysis will be based on matched pairs (parents and their children) in order to examine the hypothesis that parental and children’s perception of gambling and other risk behaviors, as well as perception of gambling accessibility in Croatia, significantly differs. Furthermore, this paper will also examine differences in parental knowledge about their children’s gambling activities compared to children’s self-report, with special emphasis on controlling the effects of child’s gender.\nResearch results will be considered in direction of providing guidelines for development and implementation of preventive and treatment interventions that engage both children and parents.

**Ваша слепая метка (калибровка):** -3 опрос родителей о восприятии гемблинга подростков без инструмента проблемной игры

**ИИ:** ? · обе модели · неясно, измеряли ли проблемную игру · Croatian survey of parents and adolescents measuring gambling activities (sports betting likely); no problem-gambling screen is clearly listed among the instruments.

**Решение:** -

---

### 1516 · R5810

**A Markovian Approach**

2016

_Аннотации нет — решайте по названию или ставьте `?`._

**Ваша слепая метка (калибровка):** -2 марковские модели в спортивной аналитике без опроса людей

**ИИ:** разошлись — Opus -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: There's no abstract, and the title points to a mathematical Markov model, probably of match outcomes, not a survey of people.); Sonnet ? (нет аннотации: Title "A Markovian Approach" has no abstract or venue; it is likely a modelling paper, but nothing shows it is about gambling, so it is uncertain.)

**Решение:** -

---

### 1517 · R5884

**The Mainstreaming of Fantasy Sport**

2016 · other · en · https://doi.org/10.5040/9781666993677.ch-012

_Аннотации нет — решайте по названию или ставьте `?`._

**Ваша слепая метка (калибровка):** -1 аналитическая глава книги о мейнстримизации фэнтези-спорта

**ИИ:** ? · обе модели · нет аннотации · No abstract; title on fantasy sport may be commentary, but an empirical survey of players cannot be ruled out.

**Решение:** -

---

### 1518 · R5935

**Fantasy sports across the pond**

2016 · Lexington Books · part of book or chapter of book · eng · https://pub.uni-bielefeld.de/record/2943266

_Аннотации нет — решайте по названию или ставьте `?`._

**Ваша слепая метка (калибровка):** -1 глава книги о сравнительном анализе фэнтези-спорта в США и Великобритании

**ИИ:** ? · обе модели · нет аннотации · Book chapter on fantasy sports (likely UK vs US), no abstract; problem-gambling measurement unlikely but cannot be ruled out.

**Решение:** -

---

### 1519 · R6381

**A neurocognitive examination of impulsivity, inhibitory control and decision making in problem gambling**

2014

_Аннотации нет — решайте по названию или ставьте `?`._

**Ваша слепая метка (калибровка):** ? нейрокогнитивное исследование проблемных игроков, нет аннотации, проверить полный текст

**ИИ:** -5 · обе модели · выборка набрана по проблемам с игрой: лечение, горячая линия, самоисключение, сравнение проблемных игроков с контролем · There is no abstract. The title points to a neurocognitive study comparing problem gamblers with controls, and sports betting is not mentioned.

**Решение:** ?

---

### 1520 · R6815

**運動彩券交易之資料採礦分析; Data Mining on Sport Lottery Transactions**

2013 · dissertation · zh

_Аннотации нет — решайте по названию или ставьте `?`._

**Ваша слепая метка (калибровка):** -3 интеллектуальный анализ транзакционных данных спортивной лотереи

**ИИ:** разошлись — Opus -3 (нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора: Data mining of sport lottery transaction records; title gives no sign of a survey of people or a problem-gambling instrument.); Sonnet ? (нет аннотации: Taiwan sport lottery transactions data mining thesis; no abstract. Likely behavioural transaction data, but a problem-gambling measure can't be ruled out.)

**Решение:** -

---

### 1521 · R6864

**Pathways to problem gambling: A summary of research from 2010-2012**

2012 · article · en

This study is a meta-analysis on the results of eight projects undertaken by the first author and his research team in Hong Kong and Macau. The purpose of the present meta-analysis was to understand the pathways development of recreational and problem gambling. These eight research projects were all qualitative studies on different groups of active gamblers, which included day-traders (N=16), elderly gamblers in public housing estates (N=25), working class women (N=15), young gamblers primarily interested in soccer-betting (N= 18), a group of gamblers with criminal background (N=11), female sex workers (N=20), male sex workers and taxi drivers (N=20) and working adults (N=20). All the participants were clinically interviewed by the first author, who is an experienced clinical psychologist or his assistants. The interviews were structured on the Diagnostic and Statistical Manual 4th edition, text revision (American Psychiatric Association, 2000). The questions covered the participant? developmental history, his/her recollections on the acquisition and maintenance of the gambling habits, his career and family development and the current state of gambling. In addition, personality tests and the Problem Gambling Severity Index ((Ferris & Wayne, 2001) will be given to the participants in order to assess their personality and gambling involvement. Results indicated that 25% of the participants can be classified as pathological gamblers. Most of the pathological gamblers came from the groups of sex workers and gamblers with criminal background. Further analysis on the participants? Background and history and their trajectory of gambling development demonstrate that the pathways development of problem gambling does not follow a linear model, whereby problem gambling is always preceded by recreational gambling. The current study clearly indicates that the basic differences between recreational and problem gambling are more qualitative than quantitative. When compared to recreational gamblers, pathological gamblers were found to have significant deficits in impulse control, which resulted in frequent chasing of losses, the preoccupation of gambling and the failure to pursue a law-abiding lifestyle. Further, most of the pathological gamblers show a general lack of adequate moral development. While the current study supports the claims of Volberg (2002) and Blaszczynski and Nower (2002) model, it proposes a new model that focuses the subjective experiences of gambling and the influences of one? work and social environment.

**Ваша слепая метка (калибровка):** -1 обзор исследований путей развития проблемного гемблинга 2010-2015

**ИИ:** ? · обе модели · другое · Pools eight mainly qualitative studies but used DSM interviews and PGSI; one subgroup was soccer bettors (N=18), so per-group PG rates may exist.

**Решение:** -

---

### 1522 · R7321

**Sports betting – International sports betting services**

2011

_Аннотации нет — решайте по названию или ставьте `?`._

**Ваша слепая метка (калибровка):** -1 глава серии по международному спортивному праву

**ИИ:** разошлись — Opus -2 (качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи: No abstract; title suggests an industry/market or regulatory piece on betting services, not a survey of people measuring problem gambling.); Sonnet ? (нет аннотации: No abstract; title is about sports betting services, likely a trade or market piece, but empirical content and problem-gambling measurement cannot be ruled out.)

**Решение:** -

---

### 1523 · R7484

**The Fantasy Sport Experience: Motivations, Satisfaction, and Future Intentions.**

2010 · article · en

_Аннотации нет — решайте по названию или ставьте `?`._

**Ваша слепая метка (калибровка):** ? исследование пользователей фэнтези-спорта, нет аннотации, проверить полный текст

**ИИ:** -3 · обе модели · нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора · Fantasy sport study of motives, satisfaction and intentions; no sign of a problem-gambling instrument or betting for money.

**Решение:** ?

---

### 1524 · R8025

**대학생들의 스포츠토토에 대한 인식 및 구매행동에 관한 연구**

2006 · 한국스포츠산업경영학회지 · article · ko

이 연구는 스포츠토토 활성화를 위해 대학생들의 복권에 대한 인식과 스포츠토토 구매행동을 살펴보아 스포츠토토 마케팅의 기초자료를 제시하는데 목적을 가지고 설문조사를 통해 다음과 같은 결론을 도출하였다. 복권에 대한 사행성과 도박성에 대하여 참여경험이 있는 조사자가 미 경험자보다 낮게 나타났으며, 즐거움, 공익성 취미에 대하여 긍정적으로 인지하는 것으로 나타나 참여하는 사람이 그렇지 않은 사람보다 긍정적인 이미지를 가지고 있어 이미지 제고를 위해선 경험의 제공이 필요하다. 참여 유형별로 문항간의 상관관계 결과에서 즐거움과 중독성의 상반된 이미지 요인에 대하여 둘 다 높은 수준에서 상관관계를 개별적으로 인식하고 있는 것으로 나타나 부정적 이미지 제거를 위한 방안과 긍정적 이미지의 강화를 위한 방안이 이원적으로 따로 진행되어야 함을 시사한다. 스포츠토토의 참여이유는 스포츠에 대한 관심과 높은 당첨확률에 대한 기대가 가장 많은 것으로 나타나 현재와 같이 스포츠토토를 기존의 스포츠와 연계 내지 동일시하는 홍보 전략이 유효한 것으로 판단되고 당첨 확률의 가능성을 부각시켜 대학생들로 하여금 사행성보다는 스포츠여가로서의 가능성 있는 건전한 배팅게임으로의 이미지를 강화시켜야 할 것으로 판단된다. 본 결과에서는 판매량중 축구가 가장 높게 나타났으나 수시로 구매자의 종목과 방식에 대한 요구를 조사하여 그 결괴에 따라 종목과 방식을 적용하는 구조적인 조사 경로를 확보하여야 할 것으로 사료된다. 긍정적인 이미지제고는 서비스 요인에서도 고려되어야 하기 때문에 광고는 가장 선호하는 홍보수단인 스포츠신문에 집중하여야 할 것이며 마감시간 변경등의 불편사항을 감소시키고 인터넷 이용과정을 공시하여 이용횟수를 늘려나가는 것이 이미지 제고에 영향을 주는 것으로 판단된다. 결론적으로 참여유도가 이미지 제고에 직접적인 상관이 있으므로 서비스요인을 고려하여 참여를 유도하면서 이미지 요인에 대하여 이원적인 이미지 제고전략을 시행하여야 한다.

**Ваша слепая метка (калибровка):** ? опрос студентов о покупке Sports Toto, проверить опросник PG в полном тексте

**ИИ:** -3 · обе модели · нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора · Marketing survey of university students on Sports Toto perceptions and purchasing; only image/attitude items, no problem-gambling instrument.

**Решение:** ?

---

### 1525 · R8448

**Sports gambling and the media.**

1987

_Аннотации нет — решайте по названию или ставьте `?`._

**Ваша слепая метка (калибровка):** -1 исторический комментарий о ставках и медиа 1987 года

**ИИ:** разошлись — Opus ? (нет аннотации: No abstract; 1987 title about sports gambling and the media is probably commentary, but a survey can't be ruled out.); Sonnet -1 (обзор, комментарий, теоретическая, правовая или регуляторная работа: 1987 title on sports gambling and media, no abstract; likely a commentary or media discussion, unlikely to measure problem gambling.)

**Решение:** -
