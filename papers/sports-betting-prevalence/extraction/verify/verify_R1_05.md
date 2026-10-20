# Проверка выписывания — файл 5 из 6

Черновик заполнил ИИ (Claude Opus 5.5) по полному тексту; у каждого значения указано место и цитата. Проверяете вы, один проход.

**Как проверять выборку:**
1. Откройте полный текст по ссылке у исследования.
2. **Ключевые числа** — сверить с таблицей или текстом статьи всегда: в таблице оценок шкала, порог, уровень, случаи и n; под таблицей n_bettors, sample_type, sampling, betting_period.
3. Остальные поля и пункты JBI: проверить, что значение есть в цитате и место указано верно.
4. Неверное — исправьте строкой в блоке «Правки» этой выборки (по одной правке на строку):
   - `n_bettors = 1400`, `sampling = convenience` — поле выборки;
   - `E2.cases = 103`, `E2.level = L2` — поле оценки E2 (subgroup, instrument, threshold, cumulative, level, cases, n, time_frame, primary_for_authors и др.);
   - `E2 удалить` — убрать оценку;
   - `+ оценка: subgroup=all; instrument=PGSI; threshold=PGSI>=8; cumulative=yes; level=L3; cases=50; n=300; location=Table 2` — добавить оценку;
   - `jbi_6 = no` — пункт JBI;
   - `выборка удалить: причина` — если это не отдельная выборка или её нельзя брать;
   - после `#` — комментарий для Claude.
5. Когда выборка проверена, напишите `да` после «Проверено:».

**Как выписаны оценки.** Категории шкалы — как в статье (для PGSI обычно 0, 1–2, 3–7, 8+); суммы «3 и выше» строит анализ, не вы. **cumulative** = yes, если категория открыта вверх («8+», «≥3»), no — закрытая полоса («3–7»). **Уровень** — по нижней границе категории: PGSI 0 → below; 1–2 → L1; 3–7 → L2; 8+ → L3; BBGS и другие короткие скрининги → L3-screen; интервью → L4; самодельные вопросы и нестандартный подсчёт → not_levelled; порог по распределению выборки → E3.

**Подсказки в файле:** «⚠ Проверка скриптом» — где скрипт нашёл повод присмотреться (уровень не совпадает с таблицей порогов, категории не складываются в n, n оценки не равно n_bettors, числа не встречаются в вашей строке «Где цифры» с этапа полных текстов). «Расхождения в тексте» — ошибки самих авторов, которые нашёл ИИ. Посчитанные ИИ значения (% × n, обратные таблицы) выделены строкой **расчёт**.

**sample_type:** rep_survey_subsample (беттеры внутри вероятностного опроса населения или школ), gamblers_survey_subsample (беттеры внутри невероятностного опроса игроков), bettor_recruited (набраны как беттеры), students, school_pupils, athletes, other. **sampling:** probability, census, quota, operator_customers, venue_intercept, convenience, snowball, NR.

---

## ST041 · Newall 2020 · PsyArXiv

Основной отчёт R4427: [текст](../../fulltext/text/R4427.txt) · [PDF](../../fulltext/pdf/R4427.pdf) — «Who uses custom sports betting products?» — [DOI](https://doi.org/10.31234/osf.io/2hdbj)
Расхождения в тексте: Abstract and Results agree: 16.0% PGSI 8+ among CSB users vs 6.7% among non-users, and 62.0% used a CSB. 62.0% x 789 = 489, which matches Table 1. The study does not report a whole-sample PGSI 8+ prevalence or any other PGSI bands (0, 1-2, 3-7). The whole-sample figure was derived by adding the two subgroup counts, which were computed from rounded percentages. The main text has 'OR = 1.48, z = -2.34' for gender while Table 3 shows OR 1.483: the z sign is inconsistent with OR > 1. This does not affect the extraction.
Заметка ИИ: There is one sample and it is mixed sports/horse-racing. The PGSI time frame is not stated (the authors say 'current problem gamblers'), so it is coded NR. The response rate is coded NR because the 1,319 people are described as an eligible pool, not as invited.

### ST041-1 · UK online sports/horse-racing bettors, Prolific crowdsourcing panel, N=789
Отчёты: R4427 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | PGSI · PGSI>=8 (range 0-27) | **L3** | **98 / 789** | 12.4 | Page 12, Results; Table 1 | «Overall, 16.0% of custom sports bettors were current problem gamblers (PGSI score 8+), compared to 6.7% among those who did not use CSB products.» |
| E2 | CSB users (ever used a custom sports bet) | PGSI · PGSI>=8 (range 0-27) | **L3** | **78 / 489** | 16.0 | Page 12, Results; Table 1 | «Overall, 16.0% of custom sports bettors were current problem gamblers (PGSI score 8+)» |
| E3 | non-CSB users | PGSI · PGSI>=8 (range 0-27) | **L3** | **20 / 300** | 6.7 | Page 12, Results; Table 1 | «compared to 6.7% among those who did not use CSB products» |

- E1: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ starts at L3; у авторов: «current problem gamblers»; главная у авторов: no; период: NR; **расчёт: CSB users 16.0% x 489 = 78.2 -> 78; non-users 6.7% x 300 = 20.1 -> 20; 78 + 20 = 98 of 489 + 300 = 789**; заметка: Whole-sample prevalence not reported by the authors; derived from two rounded subgroup percentages (about 12.4%). Sample may include race-only bettors (mixed_race).
- E2: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ starts at L3; у авторов: «current problem gamblers»; главная у авторов: yes; период: NR; **расчёт: 16.0% x 489 = 78.2 -> 78**; заметка: n=489 CSB bettors from Table 1.
- E3: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ starts at L3; у авторов: «current problem gamblers»; главная у авторов: yes; период: NR; **расчёт: 6.7% x 300 = 20.1 -> 20**; заметка: n=300 non-CSB bettors from Table 1.

**Ключевые поля выборки:**
- **n_bettors: 789** — Page 8, Participants; Table 1 — «In total N = 789 (32.7% female) unique participants were recruited»
- **sample_type: bettor_recruited** — Page 9, Participants — «participants must have previously indicated (on the Prolific platform) that they are a UK resident, that they have made either a sports bet or a horse racing bet online before»
- **sampling: convenience** — Page 8, Participants — «unique participants were recruited via the crowdsourcing platform Prolific Academic»
- **betting_period: lifetime** — Page 9, Participants — «that they have made either a sports bet or a horse racing bet online before»

**Остальные поля:**
- parent_population: NA — NA — «NA»
- min_frequency: none — Page 9, Participants — «that they have made either a sports bet or a horse racing bet online before»
- country: GBR — Page 8, Method — «a large-scale, cross-sectional survey (N = 789) of UK residents who had all previously gambled online»
- subnational: NA — Page 8, Method — «UK residents who had all previously gambled online»
- data_years: NR — NR — «NR»
- design: cross-sectional — Page 3, Abstract — «A large-scale, cross-sectional survey of online sports/horse racing bettors (N = 789, 32.7% female).»
- gambling_disclosed: NR — NR — «NR»
- betting_mode: online only — Page 9, Participants — «'What types of online gambling / casino games have you played?' Answer: ― Race & sports book»
- pct_online: all — Page 8, Method — «UK residents who had all previously gambled online»
- pct_inplay: NR — NR — «NR»
- pct_dfs: NR — NR — «NR»
- pct_esports: NR — NR — «NR»
- sports_lottery: no — Page 9, Participants — «Answer: ― Race & sports book»
- mixed_race: yes — Page 9, Participants — «made either a sports bet or a horse racing bet online before ... although we cannot rule out that some pure horse racing bettors may have participated»
- legal_status: regulated legal market — Page 4, Introduction — «The UK now has the world's largest regulated online gambling market (McArthur, 2018)»
- n_invited: NR — Page 8, Participants — «Participants were recruited from a total pool of 1,319 eligible potential participants who met the study pre-screening criteria»
- n_responded: 803 — Page 8, Participants — «This number of complete and unique responses was derived from a total of 803 people who started the survey.»
- response_rate: NR — Page 8, Participants — «derived from a total of 803 people who started the survey. Participants were recruited from a total pool of 1,319 eligible potential participants»
- age_mean: 35.40 — Page 9, Table 1 — «Age 35.40 (SD = 10.86)»
- age_sd: 10.86 — Page 9, Table 1 — «Age 35.40 (SD = 10.86)»
- age_min: NR — NR — «NR»
- age_max: NR — NR — «NR»
- age_group: NR — NR — «NR»
- pct_male: 67.3 — Page 9, Table 1 — «Gender 32.7% female, 67.3% male»
- mode: online — Page 8, Participants — «recruited via the crowdsourcing platform Prolific Academic»
- weights: NR — NR — «NR»
- instruments: PGSI (English); also Short Gambling Harm Screen, Consumption Screen for Problem Gambling, GRCS Illusion of Control subscale (not problem-gambling case measures) — Page 11, Measures and Procedure — «Problem Gambling Severity Index (Ferris & Wynne, 2001), the Gambling Related Cognition Illusion of Control Scale (Raylu & Oei, 2004), the Short Gambling Harm S…»
- instrument_validated_in_language: yes — Page 11, Measures and Procedure — «completed a range of validated gambling screens in random order: Problem Gambling Severity Index (Ferris & Wynne, 2001)»
- industry_funding: no — Page 1 — «Funds for this study were obtained through the Goldsmiths Anthropology Department Impact Fund.»
- funding_coi: Goldsmiths Anthropology Department Impact Fund; authors declare grants from GambleAware, GRA, NSW RGF, VRGF, AGRI, GREO; Cassidy attended industry-supported events for fieldwork — Pages 1-2 — «Funds for this study were obtained through the Goldsmiths Anthropology Department Impact Fund.»
- pub_status: preprint — Page 1 — «Newall, P. W. S., Cassidy, R., Walasek, L., Ludvig, E. A., Meyer, C. (2020). Who uses custom sports betting products? Addiction Research & Theory. doi: 10.1080…»
- language: English — Full text — «Who uses custom sports betting products?»
- notes: Sample is online sports OR horse-racing bettors (pre-screen 'Race & sports book' plus Premier League fan); pure race bettors may be included, so mixed_race = yes. The main report is the PsyArXiv preprint of the paper published in Addiction Research & Theory (2020). Age and sex describe the whole sample (= the analysed bettors). 98.5% had gambled in the past 12 months. Prolific eligible pool 1,319; 803 started; 789 complete (803/1,319 = 60.9% if all were invited, but the invitation is not described). PGSI prevalence is reported only by CSB use (ever used a custom sports bet: n=489; not: n=300)…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame is Prolific users pre-screened as online race/sports bettors and Premier League fans; covers only part of UK sports bettors. — Page 9, Participants — «participants must have previously indicated (on the Prolific platform) that they are a UK resident... and that they are a Premier League soccer fan»
2. способ отбора: **no** — Volunteer opt-in crowdsourcing panel, non-probability. — Page 18, Discussion — «The present study was based on a crowdsourced sample who were willing to complete the survey for a relatively small amount of money.»
3. размер выборки: **yes** — 789 bettors >= 385. — Page 8, Participants — «In total N = 789 (32.7% female) unique participants»
4. описание выборки и условий: **unclear** — Age, sex, setting and country reported; dates of data collection missing. — Page 9, Table 1 — «Age 35.40 (SD = 10.86) Gender 32.7% female, 67.3% male»
5. охват (пропуски): **yes** — 789 complete of 803 started (1.7% incomplete); analyses on complete responses. — Page 8, Participants — «This number of complete and unique responses was derived from a total of 803 people who started the survey.»
6. валидность определения случая: **yes** — PGSI, standard 8+ threshold, original English version. — Page 10, Table 1 note — «Problem gamblers are those scoring 8 or higher on this measure.»
7. единое надёжное измерение: **yes** — Same online PGSI and threshold for all participants; validated source cited (no sample reliability reported). — Page 11, Measures and Procedure — «participants then completed a range of validated gambling screens in random order: Problem Gambling Severity Index (Ferris & Wynne, 2001)»
8. статистика (числитель и знаменатель): **unclear** — Only subgroup percentages (by CSB use) given with subgroup n; whole-sample prevalence and counts not reported; denominator mixes sports and race bettors. — Page 12, Results — «Overall, 16.0% of custom sports bettors were current problem gamblers (PGSI score 8+), compared to 6.7% among those who did not use CSB products.»
9. отклик: **no** — Opt-in panel; no invited denominator described, non-response not handled. — Page 8, Participants — «Participants were recruited from a total pool of 1,319 eligible potential participants who met the study pre-screening criteria»

Правки:
- 

Проверено: да

---

## ST042 · Wardle 2020 · Taylor & Francis

Основной отчёт R4528: [текст](../../fulltext/text/R4528.txt) · [PDF](../../fulltext/pdf/R4528.pdf) — «Defining the esports bettor: evidence from an online panel survey of Emerging Adults Gambling Survey»
Не выписано ИИ: Other gamblers (n=829) and non-gamblers (n=2033) in Table 1 are not sports bettors and were not extracted. No groups recruited for treatment or help-seeking.
Расхождения в тексте: Esports bettor base: Table 1 gives n = 104, but the Statistical analysis text says 'sparse number of esports bettors (n = 103)'. The table value (104) is used. Data collection dates: Methods say 'between June and August 2019', the Discussion says 'July/August 2019'. Table 1 percentages are weighted with unweighted bases, so all cases are derived (weighted % x unweighted n). The derived PGSI categories add up to the bases (21+17+11+55 = 104; 298+169+64+53 = 584). Text and table agree on PGSI 8+ (53% esports, 9% other sports).
Заметка ИИ: One sample (esports + other sports/event bettors, mutually exclusive groups by the authors' definition). The whole-sample estimates are sums of the subgroup derived cases. The paper does not state the PGSI time frame, so time_frame = NR. Overlaps with R3635 (wave one of the same survey).

### ST042-1 · Emerging Adults Gambling Survey (YouGov panel), Great Britain, 2019, past-year esports and other sports/event bettors aged 16-24, n=688
Отчёты: R4528 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | PGSI · PGSI 0 | **below** | **319 / 688** | 46.4 | Page 8, Table 1; Page 5, Measures | «the following mutually exclusive groups were derived ... 0: non gambler/non-problem gambling 20 51» |
| E2 | all | PGSI · PGSI 1-2 | **L1** | **186 / 688** | 27.0 | Page 8, Table 1 | «1–2: low risk gambling 16 29» |
| E3 | all | PGSI · PGSI 3-7 | **L2** | **75 / 688** | 10.9 | Page 8, Table 1 | «3–7: moderate risk gambling 11 11» |
| E4 | all | PGSI · PGSI>=8 | **L3** | **108 / 688** | 15.7 | Page 8, Table 1 | «8 or more: problem gambling (a: p<0.01; b: p<0.01) 53 9» |
| E5 | esports | PGSI · PGSI 0 | **below** | **21 / 104** | 20.2 | Page 8, Table 1 | «Esports bettors (n = 104) ... 0: non gambler/non-problem gambling 20» |
| E6 | esports | PGSI · PGSI 1-2 | **L1** | **17 / 104** | 16.3 | Page 8, Table 1 | «1–2: low risk gambling 16» |
| E7 | esports | PGSI · PGSI 3-7 | **L2** | **11 / 104** | 10.6 | Page 8, Table 1 | «3–7: moderate risk gambling 11» |
| E8 | esports | PGSI · PGSI>=8 | **L3** | **55 / 104** | 52.9 | Page 8, Table 1; Page 9 | «esports bettors were also highly engaged in gambling generally: 39% gambled more than once a week; 50% gambled on five or more different activities in the past year whilst 53% had a PGSI score of 8 or more» |
| E9 | other sports | PGSI · PGSI 0 | **below** | **298 / 584** | 51.0 | Page 8, Table 1 | «Bettors on other sports/events (n = 584) ... 0: non gambler/non-problem gambling 20 51» |
| E10 | other sports | PGSI · PGSI 1-2 | **L1** | **169 / 584** | 28.9 | Page 8, Table 1 | «1–2: low risk gambling 16 29» |
| E11 | other sports | PGSI · PGSI 3-7 | **L2** | **64 / 584** | 11.0 | Page 8, Table 1 | «3–7: moderate risk gambling 11 11» |
| E12 | other sports | PGSI · PGSI>=8 | **L3** | **53 / 584** | 9.1 | Page 8, Table 1; Page 9 | «Among other sports bettors, equivalent estimates were 10%; 24% and 9%» |

- E1: cumulative: no; источник порога: standard; правило: PGSI row; score 0 = below; у авторов: «non gambler/non-problem gambling»; главная у авторов: no; период: NR; **расчёт: esports 21 + other sports 298 = 319; n = 104 + 584 = 688 (mutually exclusive groups)**; заметка: Built from subgroup cases that were themselves derived from weighted percentages x unweighted bases; there is no weighted pct for the combined sample.
- E2: cumulative: no; источник порога: standard; правило: PGSI row; 1-2 band starts at L1; у авторов: «low risk gambling»; главная у авторов: no; период: NR; **расчёт: esports 17 + other sports 169 = 186; n = 104 + 584 = 688**; заметка: Built from cases derived from weighted percentages.
- E3: cumulative: no; источник порога: standard; правило: PGSI row; 3-7 band starts at L2; у авторов: «moderate risk gambling»; главная у авторов: no; период: NR; **расчёт: esports 11 + other sports 64 = 75; n = 104 + 584 = 688**; заметка: Built from cases derived from weighted percentages.
- E4: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ = L3; у авторов: «problem gambling»; главная у авторов: no; период: NR; **расчёт: esports 55 + other sports 53 = 108; n = 104 + 584 = 688**; заметка: Built from cases derived from weighted percentages.
- E5: cumulative: no; источник порога: standard; правило: PGSI row; score 0 = below; у авторов: «non gambler/non-problem gambling»; главная у авторов: no; период: NR; **расчёт: 20% x 104 = 20.8 -> 21**; взвешенная доля: 20; заметка: Cases derived from the weighted % and the unweighted base.
- E6: cumulative: no; источник порога: standard; правило: PGSI row; 1-2 band starts at L1; у авторов: «low risk gambling»; главная у авторов: no; период: NR; **расчёт: 16% x 104 = 16.6 -> 17**; взвешенная доля: 16; заметка: Cases derived from the weighted %.
- E7: cumulative: no; источник порога: standard; правило: PGSI row; 3-7 band starts at L2; у авторов: «moderate risk gambling»; главная у авторов: no; период: NR; **расчёт: 11% x 104 = 11.4 -> 11**; взвешенная доля: 11; заметка: Cases derived from the weighted %.
- E8: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ = L3; у авторов: «problem gambling»; главная у авторов: yes; период: NR; **расчёт: 53% x 104 = 55.1 -> 55**; взвешенная доля: 53; заметка: Cases derived from the weighted %. The text gives esports n = 103 elsewhere.
- E9: cumulative: no; источник порога: standard; правило: PGSI row; score 0 = below; у авторов: «non gambler/non-problem gambling»; главная у авторов: no; период: NR; **расчёт: 51% x 584 = 297.8 -> 298**; взвешенная доля: 51; заметка: Group is 'other sports/events', excluding esports bettors. Cases derived from the weighted %.
- E10: cumulative: no; источник порога: standard; правило: PGSI row; 1-2 band starts at L1; у авторов: «low risk gambling»; главная у авторов: no; период: NR; **расчёт: 29% x 584 = 169.4 -> 169**; взвешенная доля: 29; заметка: Cases derived from the weighted %.
- E11: cumulative: no; источник порога: standard; правило: PGSI row; 3-7 band starts at L2; у авторов: «moderate risk gambling»; главная у авторов: no; период: NR; **расчёт: 11% x 584 = 64.2 -> 64**; взвешенная доля: 11; заметка: Cases derived from the weighted %.
- E12: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ = L3; у авторов: «problem gambling»; главная у авторов: no; период: NR; **расчёт: 9% x 584 = 52.6 -> 53**; взвешенная доля: 9; заметка: Cases derived from the weighted %.

**Ключевые поля выборки:**
- **n_bettors: 688** — Page 7, Table 1 header — «Esports bettors (n = 104) Bettors on other sports/events (n = 584)»
- **sample_type: gamblers_survey_subsample** — Page 2, Abstract — «Using data from the Emerging Adults Gambling Study, a non- probability survey of 3549 people aged 16–24 living in Great Britain»
- **sampling: quota** — Page 5, Methods — «E-Mail invites to participate were sent by YouGov to a random selection of their panel members, stratified by region.»
- **betting_period: past 12 months** — Page 5, Measures — «whether they had bet on esports in the past year (irrespective of whether they had bet/gambled on other things); whether they had bet on other sports (excluding those who reported betting on esports) in the past year»

**Остальные поля:**
- parent_population: people aged 16-24 living in Great Britain (YouGov online panel members) — Page 4-5, Methods — «The Emerging Adult's Gambling Survey collected data from 3549 16–24 year olds. Participants were drawn from YouGov's online panel of over one million people li…»
- min_frequency: none — Page 5, Measures — «Esports bettors were defined as anyone who reported betting on esports in the past year.»
- country: GBR — Page 4-5, Methods — «Participants were drawn from YouGov's online panel of over one million people living in Britain and were eligible if they were aged between 16 and 24, living i…»
- subnational: NA — Page 2, Abstract — «a non- probability survey of 3549 people aged 16–24 living in Great Britain»
- data_years: 2019 — Page 5, Methods — «Data were collected between June and August 2019.»
- design: cross-sectional — Page 4, Aims and objectives — «The aims of this study were to conduct exploratory data analyses to examine the profile of esports bettors aged 16–24 recruited as part of a larger online surv…»
- gambling_disclosed: no — Page 5, Methods — «This e-mail asked them to take part in a survey, without advertising its content, and asked participants to click through to the bespoke study. The first page …»
- betting_mode: NR — Page 5, Measures — «how often they gambled, on a range of 18 different gambling activities legally available in Great Britain»
- pct_online: NR — NR — «NR»
- pct_inplay: NR — NR — «NR»
- pct_dfs: NR — NR — «NR»
- pct_esports: 15.1 — Page 7, Table 1 header — «Esports bettors (n = 104) Bettors on other sports/events (n = 584)»
- sports_lottery: unclear — Page 5, Measures — «a range of 18 different gambling activities legally available in Great Britain. This included whether they had bet on esports.»
- mixed_race: no — Page 7, Table 1 header — «Bettors on other sports/events (n = 584)»
- legal_status: regulated legal market — Page 5, Measures — «a range of 18 different gambling activities legally available in Great Britain»
- n_invited: NR — Page 5, Methods — «E-Mail invites to participate were sent by YouGov to a random selection of their panel members»
- n_responded: 3549 — Page 4, Methods — «The Emerging Adult's Gambling Survey collected data from 3549 16–24 year olds.»
- response_rate: NR — Page 5, Methods — «93% of people who accessed this page went on to complete the survey»
- age_mean: NR — NR — «NR»
- age_sd: NR — NR — «NR»
- age_min: 16 — Page 4-5, Methods — «were eligible if they were aged between 16 and 24»
- age_max: 24 — Page 4-5, Methods — «were eligible if they were aged between 16 and 24»
- age_group: mixed — Page 7, Table 1 — «Age group 16–18 ... 22 19 ... 19–21 40 34 ... 22–24 38 47»
- pct_male: 51 — Page 7, Table 1, Total column — «Sex Male (a: p<0.01; b: p<0.05) 74 62 48 49 51»
- mode: online — Page 5, Methods — «E-Mail invites to participate were sent by YouGov ... asked participants to click through to the bespoke study.»
- weights: yes — Page 6, Statistical analysis — «All estimates were weighted to match the age, sex, and regional profile of 16 to 24 year olds living in Great Britain. True (unweighted) bases are presented.»
- instruments: PGSI (English) — Page 5, Measures — «Problem gambling was measured using the Problem Gambling Severity Index (PGSI), a validated tool for the identification of gambling problems (Ferris & Wynne, 2…»
- instrument_validated_in_language: yes — Page 5, Measures — «the Problem Gambling Severity Index (PGSI), a validated tool for the identification of gambling problems (Ferris & Wynne, 2001)»
- industry_funding: no — Page 12, Funding — «The project is funded by Wellcome Trust through a Humanities and Social Sciences Fellowship to HW [grant no: 200306].»
- funding_coi: Wellcome Trust fellowship; authors report no conflict. HW previously worked on GambleAware-funded projects and was Deputy Chair of the Advisory Board for Safer Gambling (to March 2020). — Page 12, Funding; Competing interests — «HW has previously worked on projects funded by GambleAware. Until March 2020, she was the Deputy Chair of the Advisory Board for Safer Gambling, funded by the …»
- pub_status: journal — Page 1 — «International Gambling Studies, 20:3, 487-499, DOI: 10.1080/14459795.2020.1826559»
- language: English — Page 1 — «Defining the esports bettor: evidence from an online panel survey of emerging adults»
- notes: R3635 (attached to the job of R4056) also analyses wave one of this Emerging Adults survey (n = 3,549), so the samples overlap. Esports bettors (anyone who bet on esports in the past year) and bettors on other sports/events (excluding esports bettors) are mutually exclusive groups, so the whole sample = 104 + 584 = 688. 'Other sports/events' may include non-sport events; whether horse or dog race betting is in this group is not stated. Sex (pct_male = 51) is the weighted figure for the whole survey; for the bettors it was 74% male among esports bettors and 62% among other sports bettors (weig…

**Риск смещения (JBI):**
1. рамка выборки: **no** — The YouGov online panel covers only panel members, not all young sports bettors in Great Britain. — Page 11, Discussion — «As an online panel, YouGov also has issues of generalizability»
2. способ отбора: **no** — Non-probability online panel, with a random selection stratified by region within the panel. — Page 2, Abstract — «a non- probability survey of 3549 people aged 16–24 living in Great Britain»
3. размер выборки: **yes** — 688 sports or esports bettors (>=385); the esports subgroup alone is 104. — Page 7, Table 1 — «Esports bettors (n = 104) Bettors on other sports/events (n = 584)»
4. описание выборки и условий: **yes** — Age, sex, setting, country and dates are reported for the bettor groups. — Page 5, Methods; Page 7, Table 1 — «Data were collected between June and August 2019.»
5. охват (пропуски): **unclear** — Missing PGSI data among bettors is not reported. — Page 6, Statistical analysis — «True (unweighted) bases are presented.»
6. валидность определения случая: **yes** — English PGSI with the standard 8+ threshold. — Page 5, Measures — «a score of 8 or more is indicative of problem gambling»
7. единое надёжное измерение: **yes** — Same online PGSI and thresholds for everyone; reliability is in the cited source (Ferris & Wynne), not this sample. — Page 5, Measures — «The PGSI score ranges from 0 to 27; a score of 0 indicated non-problem gambling or non-gambling; 1–2 is low- risk gambling; 3–7 is moderate risk gambling»
8. статистика (числитель и знаменатель): **unclear** — Weighted percentages with unweighted bases. No numerators or CIs are given, and the esports base is inconsistent (103 vs 104). — Page 6; Page 8, Table 1 — «Because of the relatively sparse number of esports bettors (n = 103)»
9. отклик: **no** — Panel survey with no denominator of invited people; only a completion rate among those who opened the survey (93%). Weights are for age, sex and region, not non-response. — Page 5, Methods — «93% of people who accessed this page went on to complete the survey»

Правки:
- 

Проверено: да

---

## ST043 · Browne 2019 · Journal of behavioral addictions

Основной отчёт R4617: [текст](../../fulltext/text/R4617.txt) — «The impact of exposure to wagering advertisements and inducements on intended and actual betting expenditure: An ecological momentary assessment study.» — [DOI](https://doi.org/10.1556/2006.8.2019.10)
⚠ Возможное пересечение (держим раздельно; если видите общие данные — напишите в «Правки»): possible overlap with R5231 (ST049): Both EMA studies of regular Australian sports and race bettors by the same group (98 and 279 sports bettors): separate studies, recruitment may overlap
Не выписано ИИ: Regular horse/greyhound race bettors (baseline N=402; 318 analysed: 94 RG, 80 LR, 93 MR, 51 PG) were recruited as a separate sample. They are excluded because race betting alone is not sports betting.
Расхождения в тексте: The PGSI counts for sports bettors add up: 70+82+88+39 = 279, and 88+39 = 127 = 45.5% of 279, matching the text. The race bettor counts also add up (94+80+93+51 = 318; 144/318 printed as 45.2%; the exact figure is 45.28%). Tables 6/7 confirm 279 sports-bettor participants. The baseline n (320) and the analysed n (279) differ. PGSI categories are reported only for the analysed 279.
Заметка ИИ: One eligible sample was extracted: regular sports bettors. The PGSI time frame is not stated in the paper. Gambling disclosure in the invitation is NR, because the wording of the e-mail invitation is not described.

### ST043-1 · Regular (at least fortnightly) Australian sports bettors, EMA study baseline, 2017, n=279 analysed
Отчёты: R4617 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | PGSI · PGSI 0 | **below** | **70 / 279** | 25.1 | Methods, Participants | «The sports bettor sample comprised 70 RGs, 82 LR, 88 MR, and 39 PGs.» |
| E2 | all | PGSI · PGSI 1-2 | **L1** | **82 / 279** | 29.4 | Methods, Participants | «The sports bettor sample comprised 70 RGs, 82 LR, 88 MR, and 39 PGs.» |
| E3 | all | PGSI · PGSI 3-7 | **L2** | **88 / 279** | 31.5 | Methods, Participants | «The sports bettor sample comprised 70 RGs, 82 LR, 88 MR, and 39 PGs.» |
| E4 | all | PGSI · PGSI>=8 | **L3** | **39 / 279** | 14.0 | Methods, Participants; Introduction | «The sports bettor sample comprised 70 RGs, 82 LR, 88 MR, and 39 PGs.» |
| E5 | all | PGSI · PGSI>=3 | **L2** | **127 / 279** | 45.5 | Methods, Participants | «PGSI scores were treated as a binary contrast: MR/PG status (PGSI 3+) versus not (PGSI 0–2). Thus, there were ... 127/279 (45.5%) PG/MR sports bettors» |

- E1: cumulative: no; источник порога: standard; правило: PGSI row; score 0 is below L1; у авторов: «recreational gamblers (RG)»; главная у авторов: no; период: past 12 months; заметка: The PGSI time frame is not stated in the text; past 12 months is the standard PGSI frame.
- E2: cumulative: no; источник порога: standard; правило: PGSI row; 1-2 band starts at L1; у авторов: «low-risk gamblers (LR)»; главная у авторов: no; период: past 12 months; заметка: The PGSI time frame is not stated; the standard frame is assumed.
- E3: cumulative: no; источник порога: standard; правило: PGSI row; 3-7 band starts at L2; у авторов: «moderate-risk gamblers (MR)»; главная у авторов: no; период: past 12 months; заметка: The PGSI time frame is not stated; the standard frame is assumed.
- E4: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ is L3; у авторов: «problem gamblers (PGs)»; главная у авторов: no; период: past 12 months; заметка: The Introduction defines PG as PGSI 8+. The PGSI time frame is not stated.
- E5: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 is L2; у авторов: «PG/MR (PGSI 3+)»; главная у авторов: yes; период: past 12 months; заметка: Cumulative category reported by the authors and used as their binary analysis variable; it equals 88 MR + 39 PG.

**Ключевые поля выборки:**
- **n_bettors: 279** — Methods, Participants — «Of these, 597 (318 race and 279 sports) bettors completed at least one follow-up EMA survey and were available for analysis.»
- **sample_type: bettor_recruited** — Methods, Participants — «regular sports bettors (N = 320). ... Regular bettors were those who bet at least fortnightly on the targeted gambling activity.»
- **sampling: operator_customers** — Methods, Participants — «Eligible customers from a major sports-betting company operating in Australia, and respondents to a previous survey by the authors, were e-mailed an invitation to complete the survey»
- **betting_period: current** — Methods, Participants — «Regular bettors were those who bet at least fortnightly on the targeted gambling activity.»

**Остальные поля:**
- parent_population: NA — Methods, Participants — «Eligible customers from a major sports-betting company operating in Australia, and respondents to a previous survey by the authors, were e-mailed an invitation»
- min_frequency: at least fortnightly — Methods, Participants — «Regular bettors were those who bet at least fortnightly on the targeted gambling activity.»
- country: AUS — Methods, Participants — «targeted two separate samples of Australian adults: regular horse/greyhound race bettors (N = 402) and regular sports bettors (N = 320)»
- subnational: NA — Methods, Participants — «Eligible customers from a major sports-betting company operating in Australia»
- data_years: 2017 — Procedure, Baseline survey — «All respondents were surveyed during 2017. The relevant dates for each week for all sports bettors were February 20–26, March 13–19, and April 3–9.»
- design: EMA baseline — Methods — «We followed an ecological momentary assessment (EMA) design. ... After completing a baseline survey, participants completed up to 15 short EMA surveys»
- gambling_disclosed: NR — Methods, Participants — «were e-mailed an invitation to complete the survey»
- betting_mode: NR — Methods, Participants — «Regular bettors were those who bet at least fortnightly on the targeted gambling activity.»
- pct_online: NR — NR
- pct_inplay: NR — NR
- pct_dfs: NR — NR
- pct_esports: NR — NR
- sports_lottery: unclear — NR
- mixed_race: no — Methods, Participants — «two separate samples of Australian adults: regular horse/greyhound race bettors (N = 402) and regular sports bettors (N = 320)»
- legal_status: regulated legal market — Introduction — «Wagering on racing and sporting events in Australia has grown substantially in recent years, where the legal age for gambling is 18 years or older.»
- n_invited: NR — Methods, Participants — «were e-mailed an invitation to complete the survey»
- n_responded: 722 — Methods, Participants — «A total of 722 eligible respondents completed an initial online survey»
- response_rate: NR — NR
- age_mean: 40.7 — Methods, Participants — «mean ages of 41.3 (SD = 13.7) years and 40.7 (SD = 14.1) years for race bettors and sports bettors, respectively»
- age_sd: 14.1 — Methods, Participants — «40.7 (SD = 14.1) years for race bettors and sports bettors, respectively»
- age_min: 18 — Methods, Participants — «Ages ranged between 18 and 84 years»
- age_max: 84 — Methods, Participants — «Ages ranged between 18 and 84 years»
- age_group: adults — Procedure, Baseline survey — «Respondents who were aged 18 years and over bet at least fortnightly on horse/greyhound races or sports»
- pct_male: 92.5 — Methods, Participants — «The majority of respondents reported being Australian born, English-speaking male (88.1% of race bettors and 92.5% of sports bettors)»
- mode: online — Procedure, Baseline survey — «Surveys were completed online via computer or smartphone through the Qualtrics platform»
- weights: no — Methods, Participants — «The sports bettor sample comprised 70 RGs, 82 LR, 88 MR, and 39 PGs.»
- instruments: PGSI (English) — Measures, Baseline survey — «The survey captured demographic information and problem gambling risk status via the PGSI (Ferris & Wynne, 2001).»
- instrument_validated_in_language: yes — Measures, Baseline survey — «problem gambling risk status via the PGSI (Ferris & Wynne, 2001)»
- industry_funding: no — Funding Statement — «This study was funded by the Victorian Responsible Gambling Foundation.»
- funding_coi: Victorian Responsible Gambling Foundation. A major sports-betting company helped recruit by e-mailing customers (no control over design/data). NH reported unpublished consultancy for Echo Entertainment, Singapore Pools and Sportsbet; AMTR for Echo/Star Entertainment; all declare no conflict. — Funding Statement; Conflict of interest; Methods, Participa… — «She has conducted unpublished consultancy work for Echo Entertainment, Singapore Pools, and Sportsbet aimed at improving their responsible gambling practices.»
- pub_status: journal — Header — «Journal of behavioral addictions; DOI: 10.1556/2006.8.2019.10»
- language: English — Full text — «The impact of exposure to wagering advertisements and inducements on intended and actual betting expenditure»
- notes: Possible overlap with R5231 (ST049): both are EMA studies of regular Australian sports and race bettors by the same group (98 and 279 sports bettors). They are separate studies, but recruitment may overlap. 320 sports bettors completed the baseline survey; PGSI counts are given only for the 279 who completed at least one EMA survey, so the denominator is 279. It is unclear whether the age and sex figures describe the 320 or the 279 sports bettors. Mean age, SD and % male are for sports bettors; the 18-84 age range is for both samples combined. The % male sits in an ambiguous sentence. Recruit…

**Риск смещения (JBI):**
1. рамка выборки: **no** — The frame (customers of one operator plus earlier respondents to the authors' survey) covers only part of Australia's regular sports bettors. — Methods, Participants — «Eligible customers from a major sports-betting company operating in Australia, and respondents to a previous survey by the authors, were e-mailed an invitation»
2. способ отбора: **no** — Volunteers opted in after an e-mail invitation; there was no probability sampling. — Limitations — «those who opted into the study, and who completed most or all EMA surveys may differ from the population of regular sports and race bettors»
3. размер выборки: **no** — Only 279 sports bettors were analysed, below 385. — Methods, Participants — «597 (318 race and 279 sports) bettors completed at least one follow-up EMA survey»
4. описание выборки и условий: **yes** — Age, sex, setting, country and data-collection dates are all reported. — Methods, Participants; Procedure — «mean ages of ... 40.7 (SD = 14.1) years ... All respondents were surveyed during 2017.»
5. охват (пропуски): **no** — 41 of the 320 baseline sports bettors (12.8%) were dropped from the analysed sample. Attrition was checked only by age and sex, not for PGSI. — Methods, Participants; Limitations — «Substantial attrition occurred before and during the EMA survey periods.»
6. валидность определения случая: **yes** — The PGSI was used in its original English version with standard categories (8+ PG; 3+ MR/PG). — Measures; Methods, Participants — «The sports bettor sample comprised 70 RGs, 82 LR, 88 MR, and 39 PGs.»
7. единое надёжное измерение: **yes** — Everyone took the same PGSI online at baseline. Reliability is not reported in the sample but is in the cited source (Ferris & Wynne 2001). — Procedure; Measures — «Surveys were completed online via computer or smartphone through the Qualtrics platform»
8. статистика (числитель и знаменатель): **yes** — Counts and the denominator of 279 are given, so CIs can be calculated; no weights are needed. — Methods, Participants — «127/279 (45.5%) PG/MR sports bettors in the sample available for analysis»
9. отклик: **unclear** — The number of people invited by e-mail is not reported, so the response rate cannot be calculated. — Methods, Participants — «were e-mailed an invitation to complete the survey»

Правки:
- 

Проверено: да

---

## ST044 · Rockloff 2019 · Journal of behavioral addictions

Основной отчёт R4863: [текст](../../fulltext/text/R4863.txt) — «Sports betting incentives encourage gamblers to select the long odds: An experimental investigation using monetary rewards.» — [DOI](https://doi.org/10.1556/2006.8.2019.30)
Расхождения в тексте: The PGSI counts 47+82+114+56 add up to 299 and match the stated percentages. 'Aged 18–39 years' describes most respondents, not the full range, yet the mean is 36.0 with SD 13.7, so the true maximum is probably well above 39. age_max is coded NR. Table 3 uses n=271 (hard launch only, Game 6).
Заметка ИИ: One sample of 299 operator customers from an online experiment. The soft and hard launches were recruited the same way, so they are treated as one sample. PGSI categories are reported only for the whole sample, with no subgroups.

### ST044-1 · Customers of two Australian sports betting operators, Victoria, 2017, online experiment (n=299)
Отчёты: R4863 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | PGSI · PGSI 0 | **below** | **47 / 299** | 15.7 | Methods, Participants | «Non-problem gambler (NPG) accounted for 15.7% (n = 47)» |
| E2 | all | PGSI · PGSI 1-2 | **L1** | **82 / 299** | 27.4 | Methods, Participants | «low risk (LR) 27.4% (n = 82)» |
| E3 | all | PGSI · PGSI 3-7 | **L2** | **114 / 299** | 38.1 | Methods, Participants | «moderate risk (MR) 38.1% (n = 114)» |
| E4 | all | PGSI · PGSI>=8 | **L3** | **56 / 299** | 18.7 | Methods, Participants | «problem gambler (PG) 18.7% (n = 56)» |

- E1: cumulative: no; источник порога: standard; правило: PGSI row; score 0 is below L1; у авторов: «non-problem gambler»; главная у авторов: no; период: NR
- E2: cumulative: no; источник порога: standard; правило: PGSI row; 1-2 band starts at L1; у авторов: «low risk»; главная у авторов: no; период: NR
- E3: cumulative: no; источник порога: standard; правило: PGSI row; 3-7 band starts at L2; у авторов: «moderate risk»; главная у авторов: no; период: NR
- E4: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ starts at L3; у авторов: «problem gambler»; главная у авторов: yes; период: NR; заметка: The study does not aim to estimate prevalence; PGSI is used as a moderator. The 8+ category is coded primary because it is the problem-gambling category.

**Ключевые поля выборки:**
- **n_bettors: 299** — Methods, Recruitment and sampling; Participants — «The final data set contained 299 responses.»
- **sample_type: bettor_recruited** — Methods, Recruitment and sampling — «Two major sports betting companies operating in Australia assisted recruitment by e-mailing their customers an invitation to complete the survey»
- **sampling: operator_customers** — Methods, Recruitment and sampling — «e-mailing their customers an invitation to complete the survey, preferentially e-mailing their most frequent sports bettors first»
- **betting_period: past 12 months** — Methods, Recruitment and sampling — «betting on Australian Football League (AFL), cricket, or soccer at least twice within the past 12 months»

**Остальные поля:**
- parent_population: NA — NA — «NA»
- min_frequency: at least twice in the past 12 months on AFL, cricket or soccer — Methods, Recruitment and sampling — «betting on Australian Football League (AFL), cricket, or soccer at least twice within the past 12 months»
- country: AUS — Methods, Recruitment and sampling — «Inclusion criteria were residing in the state of Victoria, Australia»
- subnational: Victoria — Methods, Recruitment and sampling — «Inclusion criteria were residing in the state of Victoria, Australia»
- data_years: 2017 — Methods, Recruitment and sampling — «The soft launch (May 9–16, 2017)... The hard launch (June 1–18, 2017) yielded 386 responses»
- design: experiment baseline — Abstract, Methods — «An online experiment was conducted with wagering customers (N = 299, female = 12).»
- gambling_disclosed: NR — Methods, Recruitment and sampling — «The invitation contained a weblink to the information sheet, consent form, and online survey.»
- betting_mode: NR — Methods, Recruitment and sampling — «Two major sports betting companies operating in Australia assisted recruitment by e-mailing their customers»
- pct_online: NR — NA — «NR»
- pct_inplay: NR — NA — «NR»
- pct_dfs: NR — NA — «NR»
- pct_esports: NR — NA — «NR»
- sports_lottery: no — Methods, Recruitment and sampling — «betting on Australian Football League (AFL), cricket, or soccer»
- mixed_race: no — Methods, Recruitment and sampling — «betting on Australian Football League (AFL), cricket, or soccer at least twice within the past 12 months»
- legal_status: NR — Methods, Recruitment and sampling — «Two major sports betting companies operating in Australia assisted recruitment»
- n_invited: NR — NA — «NR»
- n_responded: 420 — Methods, Recruitment and sampling — «The soft launch ... yielded 34 responses ... The hard launch (June 1–18, 2017) yielded 386 responses»
- response_rate: NR — NA — «NR»
- age_mean: 36.0 — Methods, Participants — «aged 18–39 years (M = 36.0, SD = 13.7)»
- age_sd: 13.7 — Methods, Participants — «aged 18–39 years (M = 36.0, SD = 13.7)»
- age_min: 18 — Methods, Recruitment and sampling — «aged 18 years or older»
- age_max: NR — Methods, Participants — «Most of the 299 respondents were English-speaking males (male = 287), aged 18–39 years»
- age_group: adults — Methods, Recruitment and sampling — «aged 18 years or older»
- pct_male: 96.0 — Methods, Participants — «Most of the 299 respondents were English-speaking males (male = 287)»
- mode: online — Abstract; Methods — «An online experiment was conducted with wagering customers»
- weights: NR — NA — «NR»
- instruments: PGSI (English) — Methods, Problem gambling severity — «This was assessed using the PGSI (Ferris & Wynne, 2001), which contains nine items with four response options»
- instrument_validated_in_language: yes — Methods, Problem gambling severity — «This was assessed using the PGSI (Ferris & Wynne, 2001)»
- industry_funding: no — Funding Statement — «This study was funded by the Victorian Responsible Gambling Foundation»
- funding_coi: Funded by the Victorian Responsible Gambling Foundation. Two operators helped recruit but had no control or data access. One author received industry funding (Echo/Star Entertainment) and another got consultancy funds from Echo Entertainment and Sportsbet. The authors declare no conflict for this m… — Funding Statement; Conflict of interest; Recruitment and sa… — «She has also received consultancy funds from Echo Entertainment and Sportsbet... All authors declare no conflict of interest in relation to this manuscript.»
- pub_status: journal — Header — «Journal of behavioral addictions; DOI: 10.1556/2006.8.2019.30»
- language: English — Full text — «Sports betting incentives encourage gamblers to select the long odds»
- notes: Combines the soft launch (Operator 1 only, 28 complete of 34) and the hard launch (271 of 386). The hard launch excluded 115 responses: 4 lived outside Victoria, 1 had no sports bet and 110 were incomplete. The most frequent bettors were invited first: 186 (62%) bet at least fortnightly. Age and sex describe the 299 analysed. pct_male derived as 287/299 = 96.0%. The PGSI time frame is not stated. Game 6 analyses use n=271.

**Риск смещения (JBI):**
1. рамка выборки: **no** — The frame was the customers of two operators, with the most frequent bettors contacted first. It covers only part of the sports bettors in Victoria. — Methods, Recruitment and sampling — «Two major sports betting companies operating in Australia assisted recruitment by e-mailing their customers an invitation to complete the survey, preferentiall…»
2. способ отбора: **no** — Volunteer opt-in from an email invitation, with the most frequent bettors targeted first. Not probability sampling. — Methods, Recruitment and sampling — «preferentially e-mailing their most frequent sports bettors first»
3. размер выборки: **no** — n=299, which is below 385. — Methods, Recruitment and sampling — «The final data set contained 299 responses.»
4. описание выборки и условий: **yes** — Age, sex, setting, country/state and dates are all reported. — Methods, Participants; Recruitment and sampling — «male = 287), aged 18–39 years (M = 36.0, SD = 13.7)»
5. охват (пропуски): **no** — 116 of 420 responses (about 28%) were incomplete and dropped. The analysis used complete cases only, with no handling. — Methods, Recruitment and sampling — «34 responses of which 28 had complete data... 110 provided incomplete responses»
6. валидность определения случая: **yes** — English PGSI with the standard 8+ threshold. — Methods, Problem gambling severity — «0 = non-problem gambling, 1–2 = low risk, 3–7 = moderate risk, and 8–27 = problem gambling»
7. единое надёжное измерение: **unclear** — Everyone completed the same online PGSI, but reliability is not reported. — Methods, Problem gambling severity — «This was assessed using the PGSI (Ferris & Wynne, 2001)»
8. статистика (числитель и знаменатель): **yes** — Counts and the denominator (299) are given, so CIs can be calculated. The design does not need weights. — Methods, Participants — «Non-problem gambler (NPG) accounted for 15.7% (n = 47)... problem gambler (PG) 18.7% (n = 56)»
9. отклик: **no** — The number of customers invited is not given, so there is no response rate and no handling of non-response. — Methods, Recruitment and sampling — «e-mailing their customers an invitation to complete the survey»

Правки:
- 

Проверено: да

---

## ST045 · Giralt 2018 · Journal of Behavioral Addictions

Основной отчёт R5077: [текст](../../fulltext/text/R5077.txt) — «Prevalence, risk factors, and psychosocial adjustment of problematic gambling in adolescents: Results from two representative German samples» — [DOI](https://doi.org/10.1556/2006.7.2018.37)
Не выписано ИИ: Not extracted: the whole-sample prevalence estimates in Table 2 (sample 1 n=3,795; sample 2 n=5,514, by sex), because they cover all pupils, not sports bettors. Also not extracted: offline sports bettors (and online and offline combined), because they appear only as regression predictors in Table 3 (merged active gamblers, N=3,663) with no prevalence. The paper has no treatment, helpline or self-exclusion samples.
Расхождения в тексте: 1) Discussion gives 2.2% (sample 1) and 1.7% (sample 2) for problematic gambling among all pupils. This matches Table 2: (68+14)/3,795 = 2.16% and (77+14)/5,514 = 1.65%. 2) Discussion says that among past-year gamblers the rate is 4.9% in sample 1 and 3.8% in sample 2. Table 1 gives sample 1 active gamblers as 997+562 = 1,559, and 82/1,559 = 5.3%, not 4.9%. Sample 2: 91/(1,495+866) = 3.85%, which matches. 3) Table 1 for sample 2 has apparent typos: '196 (127)' (probably 19.6) and '630 (28.6)' (values swapped). 4) pct_male is computed from Table 2 for the whole school sample (sample 1: 1,843/3,795 = 48.6%; sample 2: 2,757/5,514 = 50.0%). It does not describe the sports bettors. 5) Age range 12-18 is for the whole school sample; mean age is reported only by gambling-status group (Table 1), not for the sample overall or for sports bettors. Age group is coded mixed because 18-year-olds are …
Заметка ИИ: Two separately recruited state school surveys, so two samples. The only sports-betting estimate is the percentage with problematic gambling among past-year online sports bettors (DSM-IV-MR-J >=4): 20.2% in sample 1 and 19.8% in sample 2. No counts or denominators are given, so cases and n are NR. Mode of administration (paper vs electronic) is not stated; it is probably a paper questionnaire in class. Legal status is coded NR: the text only says gambling is prohibited for minors in Germany and that Internet gambling is 'almost completely unregulated'. instrument_validated_in_language = yes re…

### ST045-1 · Pupils who bet on sports online, Rhineland-Palatinate school survey (sample 1), Germany, 2011-2012 (school sample n=3,795; n of sports bettors NR)
Отчёты: R5077 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | online | DSM-IV-MR-J · DSM-IV-MR-J>=4 (range 0-9) | **L3** | **NR / NR** |  | Results, Problematic gambling behavior and preferred gambli… | «online sports betting [sample 1: 20.2% with problematic gambling; χ2(2) = 110.26, p = .001, CV = 0.269]» |

- E1: cumulative: yes; источник порога: standard; правило: DSM-IV-MR-J row; >=4 = L3; у авторов: «problematic gambling»; главная у авторов: no; период: past 12 months; заметка: Only a percentage is reported: 20.2% problematic gambling among past-year online sports bettors. The number of online sports bettors is not reported, so cases and n are NR. The wording is ambiguous: it most likely means the share of online sports bettors with problematic gambling, but could mean th…

**Ключевые поля выборки:**
- **n_bettors: NR** — Results, Problematic gambling behavior and preferred gambling activity — «online sports betting [sample 1: 20.2% with problematic gambling; χ2(2) = 110.26, p = .001, CV = 0.269»
- **sample_type: school_pupils** — Methods, Sampling procedure and participants — «Questionnaires were provided to all the students attending class at the point of the data acquisition.»
- **sampling: probability** — Methods, Sampling procedure and participants — «random probability sample selection with a stratification regarding school type and regional population density. A second selection criterion regarded the specific school classes in the schools that were drawn.»
- **betting_period: past 12 months** — Results, Problematic gambling behavior and preferred gambling activity — «last year's engagement in online casino gaming [...], online sports betting [sample 1: 20.2% with problematic gambling»

**Остальные поля:**
- parent_population: school pupils aged 12-18 years in Rhineland-Palatinate (all school types, including vocational schools) — Methods, Sampling procedure and participants — «two representative samples of adolescents aged 12–18 years were drawn»
- min_frequency: none — Methods, General Questionnaire — «12-month prevalence (0 = no to 6 = almost daily) of 12 different gambling activities»
- country: DEU — Methods, Sampling procedure and participants — «Two independent representative samples of adolescents from two federal states of Germany (sample 1: Rhineland-Palatinate; sample 2: North Rhine-Westphalia) wer…»
- subnational: Rhineland-Palatinate — Methods, Sampling procedure and participants — «sample 1: Rhineland-Palatinate»
- data_years: 2011-2012 — Methods, Sampling procedure and participants — «Over a period of 8 months (between 2011 and 2012), two representative samples of adolescents aged 12–18 years were drawn.»
- design: prevalence survey — Methods, Sampling procedure and participants — «The procedure was based on a random probability sample selection with a stratification regarding school type and regional population density.»
- gambling_disclosed: NR — Methods — «All subjects were informed about the study and all provided informed consent.»
- betting_mode: both — Table 3 — «Sport betting (offline) | 0.13 | 0.02 | 0.126*** ... Sport betting (online) | 0.06 | 0.03 | 0.042*»
- pct_online: NR — NR — «NR»
- pct_inplay: NR — NR — «NR»
- pct_dfs: NR — NR — «NR»
- pct_esports: NR — NR — «NR»
- sports_lottery: unclear — Methods, General Questionnaire — «12 different gambling activities (slot machines, lotteries, poker, different types of Internet gambling offers, etc.) were assessed.»
- mixed_race: no — Table 3 — «Sport betting (online)»
- legal_status: NR — Introduction; Discussion — «This rate is especially alarming since gambling is strictly prohibited for minors in Germany.»
- n_invited: NR — Methods, Sampling procedure and participants — «A total of 139 schools were representatively selected (sample 1: 62; sample 2: 77).»
- n_responded: 4047 — Methods, Sampling procedure and participants — «Data were collected from a total of 4,047 (sample 1) and 6,081 (sample 2) respondents.»
- response_rate: 66.1 — Methods, Sampling procedure and participants — «The response rate of the stratified schools amounted to 66.1% (sample 1) and 54.3% (sample 2).»
- age_mean: NR — Table 1 — «M (SD) | 15.3 (1.71) | 15.6 (1.66) | 15.8 (1.60)»
- age_sd: NR — Table 1 — «M (SD) | 15.3 (1.71) | 15.6 (1.66) | 15.8 (1.60)»
- age_min: 12 — Methods, Sampling procedure and participants — «two representative samples of adolescents aged 12–18 years were drawn»
- age_max: 18 — Methods, Sampling procedure and participants — «two representative samples of adolescents aged 12–18 years were drawn»
- age_group: mixed — Table 1 — «18 years (%) | 26.1 (125) | 24.0 (115) | 49.9 (239)»
- pct_male: 48.6 — Table 2 — «Sample 1 (n = 3,795) ... Male (n = 1,843) | Female (n = 1,952)»
- mode: NR — Methods, Sampling procedure and participants — «Questionnaires were provided to all the students attending class at the point of the data acquisition.»
- weights: NR — Methods, Statistical analysis — «SPSS 21.0 was used for statistical analysis.»
- instruments: DSM-IV-MR-J (German version, as used by Hurrelmann et al., 2003), past 12 months — Methods, DSM-IV-MR-J — «Prevalence of problematic gambling was assessed using the DSM-IV-MR-J (Fisher, 2000; Hurrelmann et al., 2003). Gambling behavior is classified by nine items re…»
- instrument_validated_in_language: yes — Discussion (limitations) — «Although a validated self-report measure has been applied for classifying problematic gambling, this cannot replace a diagnosis derived from a clinical intervi…»
- industry_funding: no — Funding Statement — «This work was supported by Ministry of Social Affairs, Labour, Health and Demography of the state Rhineland Palatinate and Ministry of Health, Equalities, Care…»
- funding_coi: State ministries (Rhineland-Palatinate; North Rhine-Westphalia); authors declare no conflict of interest — Funding Statement; Conflict of interest — «The authors declare no conflict of interest.»
- pub_status: journal — Header — «venue: Journal of Behavioral Addictions; DOI: 10.1556/2006.7.2018.37»
- language: English — Full text — «Prevalence, risk factors, and psychosocial adjustment of problematic gambling in adolescents: Results from two representative German samples»
- notes: Sports bettors are a subsample of a stratified random school survey; their number is not reported. The only sports-betting estimate is for past-year online sports bettors. pct_male (1,843/3,795 = 48.6%) and the age range 12-18 describe the whole school sample, not the sports bettors. Mean age is reported only by gambling-status group (Table 1). The response rate is at school level (66.1%); n_responded 4,047 is before 252 cases were removed for missing data (final n = 3,795). Mode of administration is not stated: 'questionnaires' were given in class, probably on paper. The text says only that …

**Риск смещения (JBI):**
1. рамка выборки: **yes** — Frame was schools/classes of the federal state, covering pupils of the state (parent survey). — Methods, Sampling procedure and participants — «random probability sample selection with a stratification regarding school type and regional population density»
2. способ отбора: **yes** — Stratified random probability sample of schools and classes; all pupils present in class surveyed. — Methods, Sampling procedure and participants — «Questionnaires were provided to all the students attending class at the point of the data acquisition.»
3. размер выборки: **unclear** — Number of (online) sports bettors not reported. — Results, Problematic gambling behavior and preferred gambli… — «online sports betting [sample 1: 20.2% with problematic gambling»
4. описание выборки и условий: **yes** — Age, sex, school setting, state and data-collection period reported (for the whole sample, not for the sports bettors). — Methods; Table 1 — «Over a period of 8 months (between 2011 and 2012)»
5. охват (пропуски): **yes** — 6.2% of cases removed for missing data (whole sample); missingness among sports bettors not reported. — Methods, Sampling procedure and participants — «About 252 (6.2%; sample 1) and 382 (6.3%; sample 2) cases had to be removed from the data set because of missing data.»
6. валидность определения случая: **yes** — DSM-IV-MR-J with standard cut-off >=4, described as validated. — Methods, DSM-IV-MR-J — «Problematic gambling is indicated if at least four criteria have been met.»
7. единое надёжное измерение: **yes** — Same questionnaire for all pupils; reliability reported in the sample. — Methods, DSM-IV-MR-J — «In this survey, DSM-IV-MR-J showed high reliability (sample 1: α = .85; sample 2: α = .84).»
8. статистика (числитель и знаменатель): **no** — Sports-bettor estimate is a bare percentage with no numerator or denominator; no CI; unclear direction of the percentage. — Results, Problematic gambling behavior and preferred gambli… — «online sports betting [sample 1: 20.2% with problematic gambling; χ2(2) = 110.26, p = .001, CV = 0.269»
9. отклик: **yes** — School response 66.1%; participating vs non-participating schools compared; pupil-level response not reported. — Methods, Sampling procedure and participants — «The response rate of the stratified schools amounted to 66.1% (sample 1) and 54.3% (sample 2). Participating and non-participating schools did not differ syste…»

Правки:
- 

Проверено: да

### ST045-2 · Pupils who bet on sports online, North Rhine-Westphalia school survey (sample 2), Germany, 2011-2012 (school sample n=5,514; n of sports bettors NR)
Отчёты: R5077 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | online | DSM-IV-MR-J · DSM-IV-MR-J>=4 (range 0-9) | **L3** | **NR / NR** |  | Results, Problematic gambling behavior and preferred gambli… | «online sports betting [...] sample 2: 19.8% with problematic gambling; χ2(2) = 222.68, p = .001, CV = 0.311]» |

- E1: cumulative: yes; источник порога: standard; правило: DSM-IV-MR-J row; >=4 = L3; у авторов: «problematic gambling»; главная у авторов: no; период: past 12 months; заметка: Only a percentage is reported: 19.8% problematic gambling among past-year online sports bettors. The number of online sports bettors is not reported, so cases and n are NR. The wording is ambiguous: it most likely means the share of online sports bettors with problematic gambling, but could mean th…

**Ключевые поля выборки:**
- **n_bettors: NR** — Results, Problematic gambling behavior and preferred gambling activity — «sample 2: 19.8% with problematic gambling; χ2(2) = 222.68, p = .001, CV = 0.311»
- **sample_type: school_pupils** — Methods, Sampling procedure and participants — «Questionnaires were provided to all the students attending class at the point of the data acquisition.»
- **sampling: probability** — Methods, Sampling procedure and participants — «random probability sample selection with a stratification regarding school type and regional population density. A second selection criterion regarded the specific school classes in the schools that were drawn.»
- **betting_period: past 12 months** — Results, Problematic gambling behavior and preferred gambling activity — «last year's engagement in [...] online sports betting [...] sample 2: 19.8% with problematic gambling»

**Остальные поля:**
- parent_population: school pupils aged 12-18 years in North Rhine-Westphalia (all school types, including vocational schools) — Methods, Sampling procedure and participants — «two representative samples of adolescents aged 12–18 years were drawn»
- min_frequency: none — Methods, General Questionnaire — «12-month prevalence (0 = no to 6 = almost daily) of 12 different gambling activities»
- country: DEU — Methods, Sampling procedure and participants — «Two independent representative samples of adolescents from two federal states of Germany (sample 1: Rhineland-Palatinate; sample 2: North Rhine-Westphalia) wer…»
- subnational: North Rhine-Westphalia — Methods, Sampling procedure and participants — «sample 2: North Rhine-Westphalia»
- data_years: 2011-2012 — Methods, Sampling procedure and participants — «Over a period of 8 months (between 2011 and 2012), two representative samples of adolescents aged 12–18 years were drawn.»
- design: prevalence survey — Methods, Sampling procedure and participants — «The procedure was based on a random probability sample selection with a stratification regarding school type and regional population density.»
- gambling_disclosed: NR — Methods — «All subjects were informed about the study and all provided informed consent.»
- betting_mode: both — Table 3 — «Sport betting (offline) | 0.13 | 0.02 | 0.126*** ... Sport betting (online) | 0.06 | 0.03 | 0.042*»
- pct_online: NR — NR — «NR»
- pct_inplay: NR — NR — «NR»
- pct_dfs: NR — NR — «NR»
- pct_esports: NR — NR — «NR»
- sports_lottery: unclear — Methods, General Questionnaire — «12 different gambling activities (slot machines, lotteries, poker, different types of Internet gambling offers, etc.) were assessed.»
- mixed_race: no — Table 3 — «Sport betting (online)»
- legal_status: NR — Introduction; Discussion — «This rate is especially alarming since gambling is strictly prohibited for minors in Germany.»
- n_invited: NR — Methods, Sampling procedure and participants — «A total of 139 schools were representatively selected (sample 1: 62; sample 2: 77).»
- n_responded: 6081 — Methods, Sampling procedure and participants — «Data were collected from a total of 4,047 (sample 1) and 6,081 (sample 2) respondents.»
- response_rate: 54.3 — Methods, Sampling procedure and participants — «The response rate of the stratified schools amounted to 66.1% (sample 1) and 54.3% (sample 2).»
- age_mean: NR — Table 1 — «M (SD) | ... | 15.1 (1.56) | 15.2 (1.62) | 15.6 (1.63)»
- age_sd: NR — Table 1 — «M (SD) | ... | 15.1 (1.56) | 15.2 (1.62) | 15.6 (1.63)»
- age_min: 12 — Methods, Sampling procedure and participants — «two representative samples of adolescents aged 12–18 years were drawn»
- age_max: 18 — Methods, Sampling procedure and participants — «From sample 2, n = 185 students aged 19 years were excluded from the final data set.»
- age_group: mixed — Table 1 — «18 years (%) | ... | 196 (127) | 24.0 (156) | 56.4 (366)»
- pct_male: 50.0 — Table 2 — «Sample 2 (n = 5,514) ... Male (n = 2,757) | Female (n = 2,757)»
- mode: NR — Methods, Sampling procedure and participants — «Questionnaires were provided to all the students attending class at the point of the data acquisition.»
- weights: NR — Methods, Statistical analysis — «SPSS 21.0 was used for statistical analysis.»
- instruments: DSM-IV-MR-J (German version, as used by Hurrelmann et al., 2003), past 12 months — Methods, DSM-IV-MR-J — «Prevalence of problematic gambling was assessed using the DSM-IV-MR-J (Fisher, 2000; Hurrelmann et al., 2003). Gambling behavior is classified by nine items re…»
- instrument_validated_in_language: yes — Discussion (limitations) — «Although a validated self-report measure has been applied for classifying problematic gambling, this cannot replace a diagnosis derived from a clinical intervi…»
- industry_funding: no — Funding Statement — «This work was supported by Ministry of Social Affairs, Labour, Health and Demography of the state Rhineland Palatinate and Ministry of Health, Equalities, Care…»
- funding_coi: State ministries (Rhineland-Palatinate; North Rhine-Westphalia); authors declare no conflict of interest — Funding Statement; Conflict of interest — «The authors declare no conflict of interest.»
- pub_status: journal — Header — «venue: Journal of Behavioral Addictions; DOI: 10.1556/2006.7.2018.37»
- language: English — Full text — «Prevalence, risk factors, and psychosocial adjustment of problematic gambling in adolescents: Results from two representative German samples»
- notes: Sports bettors are a subsample of a stratified random school survey; their number is not reported. The only sports-betting estimate is for past-year online sports bettors. pct_male (2,757/5,514 = 50.0%) and the age range 12-18 describe the whole school sample (185 pupils aged 19 were excluded), not the sports bettors. Mean age is reported only by gambling-status group (Table 1). The response rate is at school level (54.3%); n_responded 6,081 is before 382 cases were removed for missing data and the 19-year-olds were excluded (final n = 5,514). Mode of administration is not stated. Parallel sa…

**Риск смещения (JBI):**
1. рамка выборки: **yes** — Frame was schools/classes of the federal state, covering pupils of the state (parent survey). — Methods, Sampling procedure and participants — «random probability sample selection with a stratification regarding school type and regional population density»
2. способ отбора: **yes** — Stratified random probability sample of schools and classes; all pupils present in class surveyed. — Methods, Sampling procedure and participants — «Questionnaires were provided to all the students attending class at the point of the data acquisition.»
3. размер выборки: **unclear** — Number of (online) sports bettors not reported. — Results, Problematic gambling behavior and preferred gambli… — «sample 2: 19.8% with problematic gambling»
4. описание выборки и условий: **yes** — Age, sex, school setting, state and data-collection period reported (for the whole sample, not for the sports bettors). — Methods; Table 1 — «Over a period of 8 months (between 2011 and 2012)»
5. охват (пропуски): **yes** — 6.3% of cases removed for missing data (whole sample); missingness among sports bettors not reported. — Methods, Sampling procedure and participants — «About 252 (6.2%; sample 1) and 382 (6.3%; sample 2) cases had to be removed from the data set because of missing data.»
6. валидность определения случая: **yes** — DSM-IV-MR-J with standard cut-off >=4, described as validated. — Methods, DSM-IV-MR-J — «Problematic gambling is indicated if at least four criteria have been met.»
7. единое надёжное измерение: **yes** — Same questionnaire for all pupils; reliability reported in the sample. — Methods, DSM-IV-MR-J — «In this survey, DSM-IV-MR-J showed high reliability (sample 1: α = .85; sample 2: α = .84).»
8. статистика (числитель и знаменатель): **no** — Sports-bettor estimate is a bare percentage with no numerator or denominator; no CI; unclear direction of the percentage. — Results, Problematic gambling behavior and preferred gambli… — «sample 2: 19.8% with problematic gambling; χ2(2) = 222.68, p = .001, CV = 0.311»
9. отклик: **yes** — School response 54.3% (<60%), but participating and non-participating schools were compared; pupil-level response not reported. — Methods, Sampling procedure and participants — «The response rate of the stratified schools amounted to 66.1% (sample 1) and 54.3% (sample 2). Participating and non-participating schools did not differ syste…»

Правки:
- 

Проверено: да

---

## ST046 · Hing 2018 · Journal of behavioral addictions

Основной отчёт R5106: [текст](../../fulltext/text/R5106.txt) — «Does the uptake of wagering inducements predict impulse betting on sport?» — [DOI](https://doi.org/10.1556/2006.7.2018.17)
Расхождения в тексте: The text and Table 1 give the same PGSI percentages (19.5/16.2/17.6/46.8). These sum to 100.1%, so the derived counts total 1,815 rather than 1,813. Table 1 ANOVA df for the PGSI groups are F(3, 1807), which implies about 1,811 respondents with PGSI and outcome data. Counts are derived from the full N of 1,813.
Заметка ИИ: Only percentages are reported, so all counts are derived. The paper reports no PGSI estimates by sex, age or betting mode. The supplied text has no funding statement.

### ST046-1 · Australian sports bettors, Qualtrics online panel, 2016, n=1,813
Отчёты: R5106 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | PGSI · PGSI 0 | **below** | **354 / 1813** | 19.5 | Table 1, PGSI rows | «Non-problem / 59.47 (40.84)b / 37.24 (40.31)a / 3.56 (11.40)a / 19.5» |
| E2 | all | PGSI · PGSI 1-2 | **L1** | **294 / 1813** | 16.2 | Table 1, PGSI rows | «Low risk / 67.13 (36.92)a / 27.98 (33.58)b / 4.89 (13.17)a,b / 16.2» |
| E3 | all | PGSI · PGSI 3-7 | **L2** | **319 / 1813** | 17.6 | Table 1, PGSI rows | «Moderate risk / 58.36 (35.51)b / 34.62 (33.69)a / 7.26 (14.57)b / 17.6» |
| E4 | all | PGSI · PGSI>=8 | **L3** | **848 / 1813** | 46.8 | Table 1, PGSI rows; Methods, Recruitment | «This sampling strategy yielded surprisingly large numbers of problem gamblers (46.8%), with 17.6% being moderate-risk gamblers, 16.2% low-risk gamblers, and 19.5% non-problem gamblers» |

- E1: cumulative: no; источник порога: standard; правило: PGSI row; score 0 is below L1; у авторов: «non-problem gambler»; главная у авторов: no; период: NR; **расчёт: 19.5% x 1813 = 353.5 -> 354**; заметка: The four derived counts sum to 1,815 (the percentages sum to 100.1). The PGSI time frame is not stated.
- E2: cumulative: no; источник порога: standard; правило: PGSI row; 1-2 band starts at L1; у авторов: «low-risk gambler»; главная у авторов: no; период: NR; **расчёт: 16.2% x 1813 = 293.7 -> 294**
- E3: cumulative: no; источник порога: standard; правило: PGSI row; 3-7 band starts at L2; у авторов: «moderate-risk gambler»; главная у авторов: no; период: NR; **расчёт: 17.6% x 1813 = 319.1 -> 319**
- E4: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ is L3; у авторов: «problem gambler»; главная у авторов: yes; период: NR; **расчёт: 46.8% x 1813 = 848.5 -> 848**; заметка: The quota sampling over-represents problem gamblers, as the authors acknowledge.

**⚠ Проверка скриптом (обратите внимание):**
- all: категории (E1+E2+E3+E4) дают 1815, а n = 1813

**Ключевые поля выборки:**
- **n_bettors: 1813** — Abstract — «Australian sports bettors (N = 1,813) completed an online survey»
- **sample_type: bettor_recruited** — Methods, Recruitment, participants, and procedure — «Inclusion criteria were aged at least 18 years, living in Australia, and having bet on sports in the previous 12 months.»
- **sampling: quota** — Methods, Recruitment, participants, and procedure — «We therefore aimed to reasonably recruit equal proportions who bet on sports more than once a week (21.0%), weekly (19.7%), 2–3 times a month (17.0%), monthly (18.5%), and less than once a month (23.9%)»
- **betting_period: past 12 months** — Methods, Recruitment, participants, and procedure — «having bet on sports in the previous 12 months»

**Остальные поля:**
- parent_population: NA — NA
- min_frequency: none — Methods, Recruitment, participants, and procedure — «having bet on sports in the previous 12 months»
- country: AUS — Methods, Recruitment, participants, and procedure — «Inclusion criteria were aged at least 18 years, living in Australia, and having bet on sports in the previous 12 months.»
- subnational: NA — Methods, Recruitment, participants, and procedure — «living in Australia»
- data_years: 2016 — Methods, Recruitment, participants, and procedure — «recruited to an online survey through a panel provider (Qualtrics, Sydney office) between July and September 2016»
- design: cross-sectional — Discussion — «These cross-sectional results cannot isolate causal pathways»
- gambling_disclosed: NR — Methods
- betting_mode: NR — Methods
- pct_online: NR — Methods
- pct_inplay: NR — Results, Bivariate results — «respondents reported that 12.29% (SD = 18.83%) of their bets were placed on impulse during the match»
- pct_dfs: NR — NA
- pct_esports: NR — NA
- sports_lottery: unclear — Methods
- mixed_race: no — Methods, Recruitment, participants, and procedure — «having bet on sports in the previous 12 months»
- legal_status: NR — NA
- n_invited: NR — NA
- n_responded: 1813 — Methods, Recruitment, participants, and procedure — «A total of 1,813 respondents were recruited to an online survey»
- response_rate: NR — NA
- age_mean: 35.3 — Methods, text below Table 1 — «with a mean age of 35.3 years (SD = 12.7 years)»
- age_sd: 12.7 — Methods, text below Table 1 — «with a mean age of 35.3 years (SD = 12.7 years)»
- age_min: 18 — Methods, Recruitment, participants, and procedure — «Inclusion criteria were aged at least 18 years»
- age_max: NR — NA
- age_group: adults — Methods, Recruitment, participants, and procedure — «Inclusion criteria were aged at least 18 years»
- pct_male: 68.9 — Table 1; text below Table 1 — «the sample was mostly male (68.9%)»
- mode: online — Methods, Recruitment, participants, and procedure — «recruited to an online survey through a panel provider (Qualtrics, Sydney office)»
- weights: NR — Methods, Statistical analysis
- instruments: PGSI (English) — Methods, Problem Gambling Severity Index — «The nine questions in the PGSI were asked, with response options ranging from “never” (0) to “almost always” (3).»
- instrument_validated_in_language: yes — Methods, Problem Gambling Severity Index — «Problem Gambling Severity Index (PGSI; Ferris & Wynne, 2001)»
- industry_funding: NR — NA
- funding_coi: NR (no funding or conflict-of-interest statement in the supplied text) — NA
- pub_status: journal — Header — «Journal of behavioral addictions; DOI: 10.1556/2006.7.2018.17»
- language: English — Full text — «Does the uptake of wagering inducements predict impulse betting on sport?»
- notes: Same data set as Hing, Li, Vitartas & Russell (2017) on impulse sports betting (overlap: do not count twice). Quota sampling by betting frequency deliberately aimed to include varied problem-gambling severity; the authors say problem gamblers are over-represented (46.8% problem gamblers). Age and sex are for the whole sample, which is all sports bettors. Whether race betting counted as sports betting is not stated.

**Риск смещения (JBI):**
1. рамка выборки: **no** — The frame is members of one online panel provider, not all Australian sports bettors. — Methods, Recruitment, participants, and procedure — «Gaining a random sample of Australian sports bettors was not possible due to cost considerations»
2. способ отбора: **no** — Non-probability online panel with quotas by betting frequency; the authors call it a convenience sample. — Discussion, limitations — «Other limitations include the convenience sample, which was overrepresentative of problem gamblers»
3. размер выборки: **yes** — n = 1,813 sports bettors (at least 385). — Abstract — «Australian sports bettors (N = 1,813)»
4. описание выборки и условий: **yes** — Age, sex, setting (online panel), country and dates are reported. — Methods; text below Table 1 — «the sample was mostly male (68.9%), with a mean age of 35.3 years»
5. охват (пропуски): **yes** — Missing data were minimal (2–4 respondents per variable); the PGSI ANOVA df imply 1,811 analysed. — Methods, Statistical analysis; Table 1 — «Each dependent variable had a small amount of missing data (2–4 respondents per variable)»
6. валидность определения случая: **yes** — English PGSI with the standard Ferris & Wynne 8+ threshold. — Methods, Problem Gambling Severity Index — «classified into non-problem gambler (0), low-risk gambler (1–2), moderate-risk gambler (3–7), and problem gambler (8–27)»
7. единое надёжное измерение: **yes** — Same instrument, mode and threshold for all respondents; alpha reported. — Methods, Problem Gambling Severity Index — «Cronbach’s α for the PGSI in this sample was .94.»
8. статистика (числитель и знаменатель): **yes** — Percentages are given with a known denominator (1,813), so counts and CIs can be calculated. — Table 1 — «Problem gambler | 44.39 (30.47)c | 35.36 (27.99)a | 20.37 (20.97)c | 46.8»
9. отклик: **no** — Online panel with no denominator of invited people and no response rate. — Methods, Recruitment, participants, and procedure — «respondents were compensated for participation according to the panel provider’s internal protocols»

Правки:
- # counts sum to 1815 due to published rounded percentages summing to 100.1%

Проверено: да

---

## ST047 · Lopez-Gonzalez 2018 · Journal of behavioral addictions

Основной отчёт R5144: [текст](../../fulltext/text/R5144.txt) — «Spanish validation of the Problem Gambling Severity Index: A confirmatory factor analysis with sports bettors.» — [DOI](https://doi.org/10.1556/2006.7.2018.84)
Расхождения в тексте: The four PGSI category counts add up to the analysed n (256 + 175 + 102 + 126 = 659), and the percentages match (38.8 / 26.6 / 15.5 / 19.1). The Methods describe the top PGSI category as ">8", while the Results use "score ≥ 8"; ≥8 was coded. Sex: 489/659 = 74.2%, which matches the reported figure. The convergent-validity correlation is given as r = .77 in the Abstract but as Spearman's ρ = .745 in the Results; this does not affect the prevalence extraction.
Заметка ИИ: This is a single-sample validation study, and the PGSI prevalence counts are given in the Results text; there is no table. No funding or COI statement was in the supplied text. The time frame of the PGSI items is not reported.

### ST047-1 · Spain, online research panel of sports bettors, March 2017, n=659
Отчёты: R5144 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | PGSI · PGSI 0 | **below** | **256 / 659** | 38.8 | Results, Within sample incidence of PG | «(a) the non-PG group (i.e., scores of 0) comprised 256 participants (38.8% of the sample)» |
| E2 | all | PGSI · PGSI 1-2 | **L1** | **175 / 659** | 26.6 | Results, Within sample incidence of PG | «(b) the low-risk gambling group (i.e., scores 1–2) comprised 175 participants (26.6%)» |
| E3 | all | PGSI · PGSI 3-7 | **L2** | **102 / 659** | 15.5 | Results, Within sample incidence of PG | «(c) the moderate-risk gambling group (i.e., scores 3–7) comprised 102 participants (15.5%)» |
| E4 | all | PGSI · PGSI>=8 | **L3** | **126 / 659** | 19.1 | Results, Within sample incidence of PG | «(d) the PG group (score ≥ 8) comprised 126 participants (19.1%)» |

- E1: cumulative: no; источник порога: standard; правило: PGSI row; score 0 is below L1; у авторов: «non-PG group / non-problem gamblers»; главная у авторов: no; период: NR; заметка: The PGSI reference period is not stated in the text.
- E2: cumulative: no; источник порога: standard; правило: PGSI row; 1-2 band starts at L1; у авторов: «low-risk gambling group»; главная у авторов: no; период: NR
- E3: cumulative: no; источник порога: standard; правило: PGSI row; 3-7 band starts at L2; у авторов: «moderate-risk gambling group»; главная у авторов: no; период: NR
- E4: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ is L3; у авторов: «PG group / problem gamblers»; главная у авторов: yes; период: NR; заметка: The Methods give the category as ">8", but the Results say "≥ 8" and the Discussion says "cut-off point of 8", so the threshold is coded as >=8.

**Ключевые поля выборки:**
- **n_bettors: 659** — Methods, Participants and procedure — «Some participants did not complete the questionnaire leaving 659 fully completed questionnaires for analysis.»
- **sample_type: bettor_recruited** — Methods, Participants and procedure — «They offered their online research panel (containing approximately 1,200 adults) who had claimed in past studies to have bet on sports.»
- **sampling: convenience** — Discussion — «A convenience sample of 659 Spanish sports bettors was recruited to explore the internal consistency and validity of the new instrument.»
- **betting_period: past 12 months** — Methods, Participants and procedure — «“Have you placed at least one bet on sports in the past 12 months?” Only those who answered “yes” continued (n = 709).»

**Остальные поля:**
- parent_population: NA — Methods, Participants and procedure — «Only those who answered “yes” continued (n = 709).»
- min_frequency: none (at least one sports bet in the past 12 months) — Methods, Participants and procedure — «“Have you placed at least one bet on sports in the past 12 months?”»
- country: ESP — Methods, Participants and procedure — «The target population was Spanish adult gamblers and a Barcelona market research company collected the data.»
- subnational: NA — Methods, Participants and procedure — «The target population was Spanish adult gamblers»
- data_years: 2017 — Methods, Participants and procedure — «In March 2017, 848 participants from the research panel accessed a Qualtrics online survey»
- design: validation study — Abstract — «A confirmatory factor analysis (CFA) was performed to confirm its construct validity.»
- gambling_disclosed: NR — Ethics — «were informed about the (a) topic of the study, (b) right to stop participating at any time»
- betting_mode: NR — Discussion — «The use of an online research panel could have overestimated the proportion of Internet bettors while underestimating those bettors who primarily bet offline.»
- pct_online: NR — Discussion — «could have overestimated the proportion of Internet bettors»
- pct_inplay: NR — NR
- pct_dfs: NR — NR
- pct_esports: NR — NR
- sports_lottery: unclear — Methods, Participants and procedure — «Have you placed at least one bet on sports in the past 12 months?»
- mixed_race: no — Methods, Participants and procedure — «Have you placed at least one bet on sports in the past 12 months?»
- legal_status: NR — NR
- n_invited: NR — Methods, Participants and procedure — «They offered their online research panel (containing approximately 1,200 adults)»
- n_responded: 848 — Methods, Participants and procedure — «In March 2017, 848 participants from the research panel accessed a Qualtrics online survey, and accepted the study’s terms and conditions.»
- response_rate: NR — Methods, Participants and procedure — «online research panel (containing approximately 1,200 adults) ... 848 participants from the research panel accessed»
- age_mean: 35.1 — Methods, Participants and procedure — «Participants’ mean age was 35.1 years (SD = 10.12) ranging from 18 to 66 years»
- age_sd: 10.12 — Methods, Participants and procedure — «Participants’ mean age was 35.1 years (SD = 10.12)»
- age_min: 18 — Methods, Participants and procedure — «ranging from 18 to 66 years»
- age_max: 66 — Methods, Participants and procedure — «ranging from 18 to 66 years»
- age_group: adults — Ethics — «The market research company who collected the sample only invited adults to participate (18+ years).»
- pct_male: 74.2 — Methods, Participants and procedure — «with significantly more males (74.2%; n = 489)»
- mode: online — Methods, Participants and procedure — «accessed a Qualtrics online survey»
- weights: NR — Analytical approach — «The remaining descriptive and inferential statistical analyses were conducted using IBM SPSS 21.»
- instruments: PGSI (Spanish version, translated and validated in this study); Stinchfield's DSM-IV measure (Spanish version, Jiménez-Murcia et al. 2009) — Measures — «Standardized procedures were followed (Brislin, 1970) to adapt the PGSI to Spanish language. ... This study used the validated Spanish version (Jiménez-Murcia …»
- instrument_validated_in_language: yes — Abstract; Conclusions — «The Spanish adaptation of the PGSI offers satisfactory validity and reliability properties»
- industry_funding: NR — NR
- funding_coi: Funding and conflicts of interest not reported in the supplied text — NR
- pub_status: journal — Header — «Journal of behavioral addictions; DOI: 10.1556/2006.7.2018.84»
- language: English — Full text — «Spanish validation of the Problem Gambling Severity Index: A confirmatory factor analysis with sports bettors»
- notes: Age and sex describe the 659 analysed sports bettors. The panel had about 1,200 adults who had said in earlier studies that they bet on sports. It is not stated whether all of them were invited, so n_invited and response_rate are NR; 848/1,200 would be about 70.7%. Flow: 848 accessed the survey, 709 passed the filter, 659 completed it (50 incomplete = 7.1%). The validation of the Spanish PGSI is this study itself. The Stinchfield DSM-IV measure was used for convergent validity only: no category counts are reported, only sensitivity/specificity and kappa. The authors state that the results do …

**Риск смещения (JBI):**
1. рамка выборки: **no** — The frame was one market-research company's online panel (~1,200 adults), while the target population was Spanish adult gamblers or sports bettors — Methods, Participants and procedure — «a Barcelona market research company collected the data. They offered their online research panel (containing approximately 1,200 adults) who had claimed in pas…»
2. способ отбора: **no** — Non-probability, self-selected online panel; the authors call it a convenience sample — Discussion — «A convenience sample of 659 Spanish sports bettors was recruited ... the self-selection method of the online panel could have prompted that participants with a…»
3. размер выборки: **yes** — 659 sports bettors, at least 385 — Methods, Participants and procedure — «leaving 659 fully completed questionnaires for analysis»
4. описание выборки и условий: **yes** — Age, sex, setting (online panel), country and dates are all reported — Methods, Participants and procedure — «In March 2017 ... Participants’ mean age was 35.1 years (SD = 10.12) ranging from 18 to 66 years with significantly more males (74.2%; n = 489).»
5. охват (пропуски): **yes** — 50 of the 709 eligible bettors (7.1%) did not complete the survey, which is within 10% — Methods, Participants and procedure — «Only those who answered “yes” continued (n = 709). Some participants did not complete the questionnaire leaving 659 fully completed questionnaires for analysis.»
6. валидность определения случая: **yes** — PGSI with the standard 8+ threshold, in a Spanish version validated in this paper — Within sample incidence of PG — «the PG group (score ≥ 8) comprised 126 participants (19.1%)»
7. единое надёжное измерение: **yes** — Same online PGSI for all participants; reliability reported in this sample — Item analysis and reliability — «This resulted in an αordinal of .97.»
8. статистика (числитель и знаменатель): **yes** — Counts for each category are given with a clear denominator of 659, so CIs can be calculated; weights are not applicable to this panel — Within sample incidence of PG — «the non-PG group (i.e., scores of 0) comprised 256 participants (38.8% of the sample)»
9. отклик: **unclear** — It is not stated how many panel members were invited; 848 of ~1,200 panel members accessed the survey, and non-responders were not compared — Methods, Participants and procedure — «online research panel (containing approximately 1,200 adults) ... 848 participants from the research panel accessed a Qualtrics online survey»

Правки:
- 

Проверено: да

---

## ST048 · McCarthy 2018 · Harm reduction journal

Основной отчёт R5162: [текст](../../fulltext/text/R5162.txt) — «Women's gambling behaviour, product preferences, and perceptions of product harm: differences by age and gambling risk status.» — [DOI](https://doi.org/10.1186/s12954-018-0227-9)
Расхождения в тексте: Table 4 sports-betting PGSI rows (30+26+18+48=122) match the column n=122 and the text (92 at PGSI>=1, 48 problem = 39.3%). Across all participants, Table 1 gives 62 problem gamblers and 235 non-problem gamblers, but among the 324 users of the four products Tables 3 and 5 give 59 problem and 167 non-problem gamblers. The rest must have gambled only on other products. Table 3's age rows (109/116/99) and the Gambling frequency text disagree on younger women's low frequency: Table 3 shows 22.0% (n=24), while the text says 22.2% (n=22). This does not affect the sports-betting estimates.
Заметка ИИ: There is one sample: 122 women who bet on sports in the past 12 months, drawn from 509 women in an online panel survey in NSW and Victoria in 2017. The estimates come straight from the counts in Table 4, so nothing was derived.

### ST048-1 · Women past-year sports bettors in an online panel survey, NSW and Victoria, Australia, 2017 (n=122)
Отчёты: R5162 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | PGSI · PGSI 0 | **below** | **30 / 122** | 24.6 | Table 4 | «Sports betting n = 122, 37.7% ... Non-problem / 117 / 46.8 / 100 / 48.5 / 63 / 38.0 / 30 / 24.6» |
| E2 | all | PGSI · PGSI 1-2 | **L1** | **26 / 122** | 21.3 | Table 4 | «Low risk / 44 / 17.6 / 34 / 16.5 / 25 / 15.1 / 26 / 21.3» |
| E3 | all | PGSI · PGSI 3-7 | **L2** | **18 / 122** | 14.8 | Table 4 | «Moderate risk / 36 / 14.4 / 24 / 11.7 / 25 / 15.1 / 18 / 14.8» |
| E4 | all | PGSI · PGSI>=8 | **L3** | **48 / 122** | 39.3 | Table 4; Gambling product use text | «which included over a third (n = 48, 39.3%) of sports betters classified as problem gamblers» |
| E5 | all | PGSI · PGSI>=1 | **L1** | **92 / 122** | 75.4 | Gambling product use text | «Over 75% (n = 92) of women who participated in sports betting were classified as either low-risk, moderate-risk, or problem gamblers» |

- E1: cumulative: no; источник порога: standard; правило: PGSI row; score 0 is below L1; у авторов: «non-problem»; главная у авторов: no; период: past 12 months; заметка: Column percentages within sports bettors.
- E2: cumulative: no; источник порога: standard; правило: PGSI row; 1-2 band starts at L1; у авторов: «low risk»; главная у авторов: no; период: past 12 months
- E3: cumulative: no; источник порога: standard; правило: PGSI row; 3-7 band starts at L2; у авторов: «moderate risk»; главная у авторов: no; период: past 12 months
- E4: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ is L3; у авторов: «problem gamblers»; главная у авторов: yes; период: past 12 months
- E5: cumulative: yes; источник порога: standard; правило: PGSI row; >=1 starts at L1; у авторов: «low-risk, moderate-risk, or problem gamblers»; главная у авторов: no; период: past 12 months; заметка: Cumulative figure reported by the authors; equals 26+18+48.

**Ключевые поля выборки:**
- **n_bettors: 122** — Table 4 — «Sports betting n = 122, 37.7%»
- **sample_type: gamblers_survey_subsample** — Recruitment and sample — «Participants were recruited through an online research panel company, which invited panel members to participate according to the age and sex quotas specified by the research team.»
- **sampling: quota** — Recruitment and sample — «which invited panel members to participate according to the age and sex quotas specified by the research team. Details of the study were sent to eligible panel members who voluntarily opted into the study.»
- **betting_period: past 12 months** — Gambling product use — «women were given binary scores to indicate whether they had used each product in the past 12 months or not»

**Остальные поля:**
- parent_population: Women aged 16+ living in NSW and Victoria, Australia (online research panel; parent study of 1000 men and women) — Recruitment and sample — «Convenience sampling techniques were used to recruit a sample that was representative (by age and state) of women aged 16 years and over living in NSW and Vict…»
- min_frequency: none — Frequency of gambling and product use — «Answers were indicated on a 5-point scale labelled 'Never' = 0, 'Less than once a month' = 1»
- country: AUS — Abstract, Methods — «This study surveyed a convenience sample of 509 women from Victoria and New South Wales, Australia.»
- subnational: New South Wales and Victoria — Data collection — «a convenience sample of 1000 Australians aged 16 years and older who lived in NSW and Victoria»
- data_years: 2017 — Data collection — «Data were collected between March and May 2017»
- design: cross-sectional — Data collection — «The data presented in this paper was collected as part of a broader online panel study of men and women, which aimed to understand community attitudes towards …»
- gambling_disclosed: NR — Recruitment and sample — «Details of the study were sent to eligible panel members who voluntarily opted into the study.»
- betting_mode: NR — Frequency of gambling and product use — «casino gambling, EGMs, horse betting, and sports betting»
- pct_online: NR — NR — «NR»
- pct_inplay: NR — NR — «NR»
- pct_dfs: NR — NR — «NR»
- pct_esports: NR — NR — «NR»
- sports_lottery: unclear — Frequency of gambling and product use — «four types of harmful gambling activities in the past 12 months—casino gambling, EGMs, horse betting, and sports betting»
- mixed_race: no — Table 4 — «EGMs | Horse betting | Casino | Sports betting»
- legal_status: NR — Recruitment and sample — «Although they are unable to legally gamble, 16- and 17-year-olds were included in the sample»
- n_invited: NR — Data collection — «A total of 2750 women accessed the survey.»
- n_responded: 509 — Data collection — «This paper focuses specifically on the data provided by female participants (n = 509).»
- response_rate: NR — Data collection — «Most women were screened out of the survey due to age quotas being filled, not consenting to participate in the study, or they did not complete each question i…»
- age_mean: NR — NR — «NR»
- age_sd: NR — NR — «NR»
- age_min: 16 — Data collection — «1000 Australians aged 16 years and older»
- age_max: NR — Table 1 — «55+ (older) | 172 | 33.8»
- age_group: mixed — Recruitment and sample — «Although they are unable to legally gamble, 16- and 17-year-olds were included in the sample»
- pct_male: 0 — Data collection — «This paper focuses specifically on the data provided by female participants (n = 509).»
- mode: online — Data collection — «The questionnaire was programmed and administered using Qualtrics survey software.»
- weights: no — Data analysis; Table 4 — «descriptive statistics used to describe the total sample ... Problem | 48 | 39.3 (n = actual number of participants)»
- instruments: PGSI (English) — Problem gambling — «The Problem Gambling Severity Index (PGSI) was used to measure problem gambling severity [56] and was administered to all participants.»
- instrument_validated_in_language: yes — Problem gambling — «non-problem gambling (score 0), low-risk gambling (1–2), moderate-risk gambling (3–7), or problem gambling (8–27) [56]»
- industry_funding: no — Funding — «funded by the Victorian Responsible Gambling Foundation Competitive Grants Scheme (Round 7). The Victorian Responsible Gambling Foundation is funded via hypoth…»
- funding_coi: Victorian Responsible Gambling Foundation (funded via hypothecated gambling taxes); authors report research funding from ARC, VRGF and other government-funded agencies — Funding; Competing interests — «ST, HP, and MD received funding for gambling research from the Australian Research Council and the Victorian Responsible Gambling Foundation.»
- pub_status: journal — Header — «Harm reduction journal; DOI: 10.1186/s12954-018-0227-9»
- language: English — Full text — «Women's gambling behaviour, product preferences, and perceptions of product harm: differences by age and gambling risk status»
- notes: Women only. Data are from a broader online panel study of 1000 men and women (ref 46); men's data not reported here. 2750 women accessed the survey; 46 excluded and replaced for missing/unreliable data. n_responded = 509 women (whole parent survey 1000). Ages of sports bettors: 62 aged 16-34, 44 aged 35-54, 16 aged 55+ (Table 4); age is given only in bands, no mean, and the number of 16-17-year-olds among bettors is not reported. Of 509 women, 324 had used any of the four products in the past 12 months. PGSI past 12 months; 'non-problem' among sports bettors = PGSI 0 gamblers. Authors note th…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame was members of a commercial online research panel, not the population of women sports bettors in NSW/Victoria. — Recruitment and sample — «Participants were recruited through an online research panel company»
2. способ отбора: **no** — Quota-based, non-probability online panel with voluntary opt-in. — Recruitment and sample — «Convenience sampling techniques were used ... Details of the study were sent to eligible panel members who voluntarily opted into the study.»
3. размер выборки: **no** — 122 sports bettors (<385). — Table 4 — «Sports betting n = 122, 37.7%»
4. описание выборки и условий: **yes** — Sex (all women), age bands, setting (online panel, NSW/Vic), country and dates are reported. — Data collection; Table 1 — «Data were collected between March and May 2017 from a convenience sample of 1000 Australians aged 16 years and older who lived in NSW and Victoria.»
5. охват (пропуски): **yes** — PGSI was given to all participants and incomplete or unreliable responses were excluded and replaced, so PGSI categories account for all 122 sports bettors. — Data collection; Table 4 — «46 women were excluded and replaced because of missing or unreliable data»
6. валидность определения случая: **yes** — PGSI with standard thresholds (8+ problem gambling), English version. — Problem gambling — «non-problem gambling (score 0), low-risk gambling (1–2), moderate-risk gambling (3–7), or problem gambling (8–27) [56]»
7. единое надёжное измерение: **yes** — Same PGSI, time frame and online mode for all; the cited source (Ferris & Wynne) reports reliability, but no reliability is given for this sample. — Problem gambling; Data collection — «The Problem Gambling Severity Index (PGSI) was used to measure problem gambling severity [56] and was administered to all participants.»
8. статистика (числитель и знаменатель): **yes** — Counts and denominator for sports bettors are given in Table 4, so a CI can be calculated. — Table 4 — «Problem | 53 | 21.2 | 48 | 23.3 | 53 | 31.9 | 48 | 39.3»
9. отклик: **no** — Online panel with no denominator of invited people; no handling of non-response. — Data collection — «A total of 2750 women accessed the survey.»

Правки:
- 

Проверено: да

---

## ST049 · Russell 2018 · Journal of behavioral addictions

Основной отчёт R5231: [текст](../../fulltext/text/R5231.txt) — «Are direct messages (texts and emails) from wagering operators associated with betting intention and behavior? An ecological momentary assessment study.» — [DOI](https://doi.org/10.1556/2006.7.2018.99)
⚠ Возможное пересечение (держим раздельно; если видите общие данные — напишите в «Правки»): possible overlap with R4617 (ST043): Both EMA studies of regular Australian sports and race bettors by the same group (98 and 279 sports bettors): separate studies, recruitment may overlap
Не выписано ИИ: Race bettors (n=104, surveyed November 3-9, 2017, Melbourne Cup week): they bet only on horse racing (99.0%) and greyhound racing (67.3%), so they are not sports bettors and were not extracted.
Расхождения в тексте: Table 1 gives PGSI categories only as percentages. It does not state the denominator. The percentages match n=98 (20/98=20.4%, 29/98=29.6%, 36/98=36.7%, 13/98=13.3%; sum 98), so 98 was used rather than the 102 who met the inclusion criteria. The text gives no PGSI time frame.
Заметка ИИ: There is one eligible sample: the 98 regular sports bettors. The PGSI distribution comes from a purposive re-invitation that deliberately included every PGSI 8+ scorer from the earlier study. It therefore overstates prevalence, and the reviewer should consider it for sensitivity analysis or exclusion. The derived counts come from the Table 1 percentages.

### ST049-1 · Regular Australian sports bettors, EMA study (AFL/NRL grand finals week), 2017, n=98
Отчёты: R5231 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | PGSI · PGSI 0 | **below** | **20 / 98** | 20.4 | Table 1 | «PGSI: non-problem (%) / 20.4 / 21.2» |
| E2 | all | PGSI · PGSI 1-2 | **L1** | **29 / 98** | 29.6 | Table 1 | «PGSI: low risk (%) / 29.6 / 25.0» |
| E3 | all | PGSI · PGSI 3-7 | **L2** | **36 / 98** | 36.7 | Table 1 | «PGSI: moderate risk (%) / 36.7 / 33.7» |
| E4 | all | PGSI · PGSI>=8 | **L3** | **13 / 98** | 13.3 | Table 1 | «PGSI: problem gambler (%) / 13.3 / 20.2» |

- E1: cumulative: no; источник порога: standard; правило: PGSI row; score 0 is below L1; у авторов: «non-problem»; главная у авторов: no; период: NR; **расчёт: 20.4% x 98 = 19.99 -> 20**; заметка: Denominator inferred as the 98 sports bettors (percentages consistent with 98). Sample oversampled PGSI 8+.
- E2: cumulative: no; источник порога: standard; правило: PGSI row; 1-2 band starts at L1; у авторов: «low risk»; главная у авторов: no; период: NR; **расчёт: 29.6% x 98 = 29.0 -> 29**; заметка: Denominator inferred as 98.
- E3: cumulative: no; источник порога: standard; правило: PGSI row; 3-7 band starts at L2; у авторов: «moderate risk»; главная у авторов: no; период: NR; **расчёт: 36.7% x 98 = 35.97 -> 36**; заметка: Denominator inferred as 98.
- E4: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ is L3; у авторов: «problem gambler»; главная у авторов: yes; период: NR; **расчёт: 13.3% x 98 = 13.03 -> 13**; заметка: PGSI 8+ is the authors' problem gambling status used as a control variable; not presented as a prevalence estimate. Inflated by deliberate invitation of all PGSI 8+ scorers. Denominator inferred as 98.

**Ключевые поля выборки:**
- **n_bettors: 98** — Table 1 — «Responded to at least one EMA | 98 | 104»
- **sample_type: bettor_recruited** — Methods, Respondents — «Respondents were recruited to the original study as regular (at least fortnightly) sports or race bettors, from two sources: account holders with a major Australian-licensed online wagering company, and a database of participants who had participated in previ…»
- **sampling: convenience** — Methods, Respondents — «We invited those who had completed at least 12 of those 15 EMAs, to maximize response rates. We also specifically invited all those scoring 8+ on the Problem Gambling Severity Index»
- **betting_period: past 12 months** — Methods, Respondents — «Inclusion criteria were providing informed consent, aged 18+, gambling at least fortnightly on sports or races in the past 12 months»

**Остальные поля:**
- parent_population: NA — Methods, Respondents — «All participants had taken part in a previous wagering study conducted by the researchers and had agreed to participate in future research»
- min_frequency: at least fortnightly; also must have bet on AFL or NRL — Methods, Respondents — «gambling at least fortnightly on sports or races in the past 12 months ... Sports bettors were also required to have bet on Australian Football League (AFL) or…»
- country: AUS — Methods, Respondents — «The sample for this study consists of 98 sports bettors and 104 race bettors from Australia.»
- subnational: NA — Methods, Respondents — «98 sports bettors and 104 race bettors from Australia»
- data_years: 2017 — Methods, EMA procedure — «Sports bettors were surveyed from September 26 to October 2, 2017 (the week leading up to the NRL and AFL grand finals).»
- design: EMA baseline — Methods, Measures — «Respondents initially completed a baseline survey that determined eligibility ... and the PGSI.»
- gambling_disclosed: yes — Methods, Respondents — «All participants had taken part in a previous wagering study conducted by the researchers and had agreed to participate in future research»
- betting_mode: NR — Methods, Respondents — «account holders with a major Australian-licensed online wagering company, and a database of participants who had participated in previous research»
- pct_online: NR — Methods — «NR»
- pct_inplay: NR — Methods — «NR»
- pct_dfs: NR — Methods — «NR»
- pct_esports: NR — Methods — «NR»
- sports_lottery: no — Methods, Respondents — «96.9% of sports bettors bet on AFL in the past 12 months, and 78.6% on NRL.»
- mixed_race: no — Methods, Respondents — «The sample for this study consists of 98 sports bettors and 104 race bettors»
- legal_status: regulated legal market — Introduction — «Sports and race betting can legally be provided by Australian-licensed operators at the sports ground or race track, at land-based venues (hotels, clubs, and c…»
- n_invited: 194 — Table 1 — «Invited from original study | 194 | 218»
- n_responded: 111 — Table 1 — «Responded to invitation | 111 | 113 57.2% of those invited»
- response_rate: 57.2 — Table 1 — «Responded to invitation | 111 | 113 57.2% of those invited»
- age_mean: 41.8 — Table 1 — «Age [mean (SD)] | 41.8 (13.1) | 44.7 (12.4)»
- age_sd: 13.1 — Table 1 — «Age [mean (SD)] | 41.8 (13.1) | 44.7 (12.4)»
- age_min: 20 — Table 1 — «Age range (years) | 20–74 | 24–72»
- age_max: 74 — Table 1 — «Age range (years) | 20–74 | 24–72»
- age_group: adults — Methods, Respondents — «Inclusion criteria were providing informed consent, aged 18+»
- pct_male: 92.9 — Table 1 — «Gender (% male) | 92.9 | 94.2»
- mode: online — Methods, EMA procedure — «Respondents were sent a link to an online survey through text message each day for seven consecutive days»
- weights: no — Methods, Statistical analysis — «No weighting described; PGSI percentages reported unweighted in Table 1»
- instruments: PGSI (English) — Methods, Measures — «how often they bet with each operator within the past 12 months, and the PGSI.»
- instrument_validated_in_language: yes — Methods, Respondents — «Problem Gambling Severity Index (PGSI; Ferris & Wynne, 2001)»
- industry_funding: no — Funding Statement — «This study was funded by the Victorian Responsible Gambling Foundation, as an extension of another project entitled “Effects of wagering marketing on vulnerabl…»
- funding_coi: Victorian Responsible Gambling Foundation; authors declare no COI, but NH received consultancy funds from Echo Entertainment and Sportsbet and AMTR industry funding from Echo/Star Entertainment — Conflict of interest — «She has also received consultancy funds from Echo Entertainment and Sportsbet and an honorarium from Singapore Pools ... She declares that she has no conflict …»
- pub_status: journal — Title page — «Journal of behavioral addictions; DOI: 10.1556/2006.7.2018.99»
- language: English — Full text — «Are direct messages (texts and emails) from wagering operators associated with betting intention and behavior?»
- notes: Sports-bettor sample of an EMA follow-on study; participants re-invited from an earlier EMA study (Hing, Russell, Rockloff et al., 2018), originally recruited from one major online wagering operator's account holders plus a research database. Invitation was purposive: only those completing >=12 of 15 earlier EMAs, plus ALL PGSI 8+ scorers deliberately invited -> PGSI distribution is biased upward (oversampling of problem gamblers) and not a prevalence estimate. Also required opt-in to direct wagering messages and AFL/NRL betting. Age, sex and PGSI describe the 98 sports bettors who responded …

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame is participants of a previous study (one operator's customers plus a research database), not all regular sports bettors in Australia. — Methods, Respondents — «account holders with a major Australian-licensed online wagering company, and a database of participants who had participated in previous research conducted by…»
2. способ отбора: **no** — Purposive re-invitation of high EMA completers and all PGSI 8+ scorers; not probability sampling. — Methods, Respondents — «We also specifically invited all those scoring 8+ on the Problem Gambling Severity Index (PGSI; Ferris & Wynne, 2001), to ensure they were adequately represent…»
3. размер выборки: **no** — 98 sports bettors, below 385. — Table 1 — «Responded to at least one EMA | 98 | 104»
4. описание выборки и условий: **yes** — Age, sex, country, recruitment setting and dates reported. — Table 1; EMA procedure — «Gender (% male) | 92.9 ... Age [mean (SD)] | 41.8 (13.1) ... Sports bettors were surveyed from September 26 to October 2, 2017»
5. охват (пропуски): **yes** — 98 of 102 eligible (96%) analysed; PGSI distribution reported for the analysed sample. — Table 1 — «Met inclusion criteria | 102 ... Responded to at least one EMA | 98 | 104 88.3% of those who responded»
6. валидность определения случая: **yes** — PGSI with standard categories (English original). — Table 1 — «PGSI: problem gambler (%) | 13.3 | 20.2»
7. единое надёжное измерение: **unclear** — Same online baseline PGSI for all, but no reliability reported and time frame not stated. — Methods, Measures — «Respondents initially completed a baseline survey that determined eligibility and captured ... and the PGSI.»
8. статистика (числитель и знаменатель): **no** — Only percentages given (denominator inferred as 98); deliberate oversampling of PGSI 8+ without weighting, so percentages do not estimate prevalence. — Table 1; Methods, Respondents — «We also specifically invited all those scoring 8+ on the Problem Gambling Severity Index ... to ensure they were adequately represented in the sample.»
9. отклик: **no** — Response to invitation 57.2%, no comparison of responders and non-responders, no weighting. — Table 1 — «Responded to invitation | 111 | 113 57.2% of those invited»

Правки:
- 

Проверено: да

---

## ST050 · Hing 2017 · Frontiers in psychology

Основной отчёт R5423: [текст](../../fulltext/text/R5423.txt) — «Risk Factors for Gambling Problems on Online Electronic Gaming Machines, Race Betting and Sports Betting.» — [DOI](https://doi.org/10.3389/fpsyg.2017.00779)
Не выписано ИИ: Problematic and non-problematic online EGM gamblers (98 + 64) and online race bettors (291 + 1145): not sports betting. No treatment or help-seeking samples. The full survey of 4,594 gamblers gives no problem-gambling estimate for all sports bettors (including land-based bettors and MR/PG sports bettors who attributed problems to other forms).
Расхождения в тексте: Abstract and Table 3 agree: 1213 non-problematic and 181 problematic online sports bettors (N = 1394). Mean income of problematic sports bettors differs between Table 3 (82.3, SD 49.4) and Table 7 (81.7, SD 49.6). Attitude means are positive in Table 3 (1.1) and negative in Table 7 (-0.90). In Table 3 the gambler-status chi-square (χ2 = 44.75, Φ = 0.18) repeats the language row exactly, which suggests a copy error. Female count: the text says three problematic sports bettors were female, which matches 1.7% of 181 = 3.1.
Заметка ИИ: I extracted this sample with caution. The study is a risk-factor comparison, not a prevalence study. The denominator and numerator are selection-biased, because MR/PG online sports bettors who attributed their problems to another form or mode were excluded. The reviewer should decide whether the sample is eligible. Data collection years and the funding source are not reported.

### ST050-1 · Australian online gamblers survey: online sports bettors (non-problem/low-risk + MR/PG attributing problems to online sports betting), n=1394
Отчёты: R5423 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | PGSI · PGSI>=3 (0-27) | **L2** | **181 / 1394** | 13.0 | Table 3; Abstract | «Non-problematic online sports gamblers (n = 1213) / Problematic online sports gamblers (n = 181) / ... χ2(1, N = 1394)» |
| E2 | all | PGSI · PGSI 0-2 (0-27) | **below** | **1213 / 1394** | 87.0 | Table 3; Abstract | «non-problem/low risk gamblers who had gambled online on these forms in the previous 12 months (n = 64, 1145 and 1213 respectively)» |
| E3 | male | PGSI · PGSI>=3 (0-27) | **L2** | **178 / 1275** | 14.0 | Table 3 | «Gender (% male) / 90.4 / 98.3∗ / χ2(1, N = 1394) = 12.61» |
| E4 | female | PGSI · PGSI>=3 (0-27) | **L2** | **3 / 119** | 2.5 | Multivariate Analyses (EGM vs sports); Table 3 | «only three problematic online sports bettors were female» |

- E1: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 starts at L2; у авторов: «moderate risk/problem gamblers (problematic online sports bettors)»; главная у авторов: yes; период: NR; **расчёт: n = 1213 non-problematic + 181 problematic online sports bettors = 1394 (also N = 1394 in Table 3 chi-square tests)**; заметка: Cases are PGSI>=3 who also named online mode and sports betting as their most problematic form. MR/PG online sports bettors who blamed other forms or modes are excluded from numerator and denominator, so this is not a true prevalence. Authors do not present it as a prevalence. 181/1394 = 13.0%.
- E2: cumulative: no; источник порога: standard; правило: PGSI row; band 0-2 has lower bound 0 = below; у авторов: «non-problem/low risk gamblers (non-problematic online sports bettors)»; главная у авторов: no; период: NR; **расчёт: n = 1213 + 181 = 1394**; заметка: Combined 0 and 1-2 bands. Separate PGSI 0 and 1-2 counts are not reported.
- E3: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 starts at L2; у авторов: «problematic online sports bettors (moderate risk/problem)»; главная у авторов: no; период: NR; **расчёт: cases 98.3% x 181 = 177.9 -> 178; non-problematic males 90.4% x 1213 = 1096.6 -> 1097; n = 1097 + 178 = 1275**; заметка: Derived from percentages. The same selection caveat as the whole-sample estimate applies.
- E4: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 starts at L2; у авторов: «problematic online sports bettors (moderate risk/problem)»; главная у авторов: no; период: NR; **расчёт: cases = 3 (text); non-problematic females 1213 - 1097 = 116 (9.6% x 1213 = 116.4); n = 116 + 3 = 119**; заметка: Derived. The same selection caveat as the whole-sample estimate applies.

**Ключевые поля выборки:**
- **n_bettors: 1394** — Table 3 — «Non-problematic online sports gamblers (n = 1213) | Problematic online sports gamblers (n = 181) ... χ2(1, N = 1394)»
- **sample_type: gamblers_survey_subsample** — Participants and Recruitment; Inclusion Criteria — «Participants were recruited via advertisements on Internet gambling sites (n = 2,475) and on gambling-related sites (n = 535), such as help services. Participants were also recruited through advertisements on Facebook (n = 810) and via Google AdWords (n = 288…»
- **sampling: convenience** — Participants and Recruitment; Discussion — «The non-random sample attained means that results may not generalize to the broader population of problematic online gamblers»
- **betting_period: past 12 months** — Abstract — «non-problem/low risk gamblers who had gambled online on these forms in the previous 12 months (n = 64, 1145 and 1213 respectively)»

**Остальные поля:**
- parent_population: Australian adults who gambled in the past 12 months (open online survey, oversampling online gamblers) — Participants and Recruitment — «an online survey which targeted Australian adults who had gambled in the past 12 months... These recruitment methods were employed to specifically oversample o…»
- min_frequency: none — Inclusion Criteria — «non-problem or low-risk gamblers ... who reported gambling online on EGMs, sports betting or race betting»
- country: AUS — Participants and Recruitment — «A total of 4,594 eligible respondents completed an online survey which targeted Australian adults who had gambled in the past 12 months.»
- subnational: NA — Participants and Recruitment — «targeted Australian adults who had gambled in the past 12 months»
- data_years: NR — Materials and Methods — «NR»
- design: cross-sectional — Discussion (limitations) — «Further, the study was cross-sectional.»
- gambling_disclosed: NR — Participants and Recruitment — «recruited via advertisements on Internet gambling sites (n = 2,475) and on gambling-related sites (n = 535)»
- betting_mode: online only — Inclusion Criteria — «moderate-risk or problem gamblers ... who specifically attributed their gambling problem to online gambling on EGMs, sports betting or race betting»
- pct_online: all — Table 3 — «Percentage of sports gambling online in last 12 months (median) | 100∗ | 98.0»
- pct_inplay: NR — Discussion — «NR»
- pct_dfs: NR — Full text — «NR»
- pct_esports: NR — Full text — «NR»
- sports_lottery: unclear — Inclusion Criteria — «Ten forms were surveyed (such as instant scratchies, bingo, keno, lotteries).»
- mixed_race: no — Inclusion Criteria — «online race betting (n = 291), online sports betting (n = 181) and online EGM gambling (n = 98)... the MR/PG groups are mutually exclusive.»
- legal_status: regulated legal market — Discussion — «in-play betting, which is illegal via the Internet in Australia, although it is legal via telephone and in land-based venues.»
- n_invited: NR — Participants and Recruitment — «NR»
- n_responded: 4594 — Participants and Recruitment — «A total of 4,594 eligible respondents completed an online survey»
- response_rate: NR — Participants and Recruitment — «NR»
- age_mean: 42.1 — Participants and Recruitment — «The overall sample was mostly male (77.8%) with a mean age of 42.1 years (SD = 14.7).»
- age_sd: 14.7 — Participants and Recruitment — «mean age of 42.1 years (SD = 14.7)»
- age_min: NR — Participants and Recruitment — «targeted Australian adults»
- age_max: NR — Participants and Recruitment — «NR»
- age_group: adults — Participants and Recruitment — «targeted Australian adults who had gambled in the past 12 months»
- pct_male: 77.8 — Participants and Recruitment — «The overall sample was mostly male (77.8%)»
- mode: online — Participants and Recruitment — «completed an online survey»
- weights: NR — Data Analysis — «NR»
- instruments: PGSI (English) — Measures: Problem Gambling — «All respondents completed the 9-item PGSI (Ferris and Wynne, 2001)»
- instrument_validated_in_language: yes — Measures: Problem Gambling — «the 9-item PGSI (Ferris and Wynne, 2001), which is the most widely used and recommended measure of problem gambling severity in Australia»
- industry_funding: NR — Conflict of Interest Statement — «NR»
- funding_coi: Funding source not reported; authors declare no conflict of interest — Conflict of Interest Statement — «The authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict…»
- pub_status: journal — Header — «Frontiers in psychology; DOI: 10.3389/fpsyg.2017.00779»
- language: English — Full text — «Risk Factors for Gambling Problems on Online Electronic Gaming Machines, Race Betting and Sports Betting»
- notes: Age and pct_male describe the whole survey (N = 4,594). Group values for sports bettors: non-problematic bettors were 41.3 (SD 14.0) years old and 90.4% male; problematic bettors were 31.1 (SD 9.8) and 98.3% male. Pooled, this gives about 40.0 years and 91.5% male (derived). The sample was constructed as follows: all non-problem/low-risk (PGSI 0-2) online sports bettors in the past 12 months, plus only those MR/PG (PGSI 3+) gamblers who named the online mode AND sports betting as their most problematic form. MR/PG online sports bettors who attributed their problems to other forms or modes are…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame was ads on gambling sites, help-service sites, Facebook and Google AdWords. This does not cover Australian sports bettors. — Participants and Recruitment — «Participants were recruited via advertisements on Internet gambling sites (n = 2,475) and on gambling-related sites (n = 535), such as help services.»
2. способ отбора: **no** — Non-random, self-selected online sample — Discussion — «The non-random sample attained means that results may not generalize»
3. размер выборки: **yes** — 1394 online sports bettors >= 385 — Table 3 — «χ2(1, N = 1394)»
4. описание выборки и условий: **unclear** — Age, sex, setting and country are reported; dates of data collection are not — Table 3 — «Gender (% male) | 90.4 | 98.3∗ ... Age (Mean/SD) | 41.3∗ (14.0) | 31.1 (9.8)»
5. охват (пропуски): **no** — Online sports bettors with MR/PG who blamed another form or mode were excluded by design. The number excluded is not reported, and this selection depends on the outcome. — Inclusion Criteria — «we excluded anyone who stated that their problems were due to land-based or telephone gambling»
6. валидность определения случая: **yes** — English PGSI with standard thresholds (3-7, 8+). Case membership also needs self-attribution of problems to online sports betting. — Measures: Problem Gambling — «non-problem gambler (0), low risk gambler (1–2), moderate risk gambler (3–7) and problem gambler (8–27)»
7. единое надёжное измерение: **yes** — Same online PGSI for all respondents; reliability reported (alpha 0.93) — Measures: Problem Gambling — «Cronbach’s alpha for the PGSI in this sample was 0.93.»
8. статистика (числитель и знаменатель): **no** — No prevalence reported. The ratio 181/1394 rests on a constructed denominator that leaves out MR/PG online sports bettors who attributed problems elsewhere, so it is not a prevalence among sports bettors. — Inclusion Criteria — «moderate-risk or problem gamblers ... who specifically attributed their gambling problem to online gambling on EGMs, sports betting or race betting»
9. отклик: **no** — Open online survey with no denominator of invited people; non-response not handled — Participants and Recruitment — «A total of 4,594 eligible respondents completed an online survey»

Правки:
- 

Проверено: да

