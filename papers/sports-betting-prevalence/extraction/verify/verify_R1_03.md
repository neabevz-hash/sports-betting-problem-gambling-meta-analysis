# Проверка выписывания — файл 3 из 6

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

## ST021 · Manu 2024 · BMC public health

Основной отчёт R2516: [текст](../../fulltext/text/R2516.txt) — «Betting high, feeling low: a cross-sectional examination of gambling severity and psychological distress among Ghanaian youth.» — [DOI](https://doi.org/10.1186/s12889-024-19550-2)
Расхождения в тексте: Sample size disagreement: the abstract says 403 participants and the target sample was 405, but Table 1 gives Frequency (578), and all its percentages match 578 (543/578 = 93.9% male; 375/578 = 64.9% aged 18-24). Following the table rule, n = 578. Case counts come from the text percentages (16.4%, 43.8%, 39.8%), which sum to 100%. Table 3 reports df2 = 912,648, which is not consistent with either n. The study population is defined as ages 18-35, but Table 1 has a '31 and above' band. The abstract rounds the PGSI results to 40%, 44% and 84%.
Заметка ИИ: There is one sample. The PGSI 0 and 1-2 bands appear only combined in the text (16.4%). A split may be in Figure 2 or the supplement, which were not available.

### ST021-1 · Youth (18-35) sports bettors at licensed betting centres, Volta Region, Ghana, 2023 (n=578 per Table 1; 403 per abstract)
Отчёты: R2516 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | PGSI · PGSI 0-2 | **below** | **95 / 578** | 16.4 | Results, Gambling severity among participants | «Approximately 16.4% of the youth participating in sports gambling exhibited no moderate to problematic gambling behavior.» |
| E2 | all | PGSI · PGSI 3-7 | **L2** | **253 / 578** | 43.8 | Results, Gambling severity among participants; Abstract | «around 43.8% exhibited a classification within the moderate range of gambling problems» |
| E3 | all | PGSI · PGSI>=8 | **L3** | **230 / 578** | 39.8 | Results, Gambling severity among participants; Abstract | «Significantly, an estimated 39.8% of the cohort fell within the category of problem gambling» |
| E4 | all | PGSI · PGSI>=3 | **L2** | **483 / 578** | 83.6 | Results, Gambling severity among participants | «the total prevalence of gambling that can lead to negative consequences (moderate and problem gambling) is estimated at 83.6%» |

- E1: cumulative: no; источник порога: standard; правило: PGSI row; combined 0-2 band, lower bound 0 = below; у авторов: «no moderate to problematic gambling behavior»; главная у авторов: no; период: past 12 months; **расчёт: 16.4% x 578 = 94.8 -> 95**; заметка: Combines PGSI 0 and 1-2. Table 4 uses these as separate bands, but the text does not report them separately (they may be in Fig. 2 or the supplement). If n = 403 (abstract): 66.
- E2: cumulative: no; источник порога: standard; правило: PGSI row; 3-7 band starts at L2; у авторов: «moderate range of gambling problems»; главная у авторов: no; период: past 12 months; **расчёт: 43.8% x 578 = 253.2 -> 253**; заметка: The abstract rounds this to 44%. If n = 403: 177.
- E3: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ = L3; у авторов: «problem gambling»; главная у авторов: yes; период: past 12 months; **расчёт: 39.8% x 578 = 230.0 -> 230**; заметка: Abstract gives 40%. The denominator is uncertain (with the abstract's 403: 160).
- E4: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 = L2; у авторов: «moderate and problem gambling»; главная у авторов: yes; период: past 12 months; **расчёт: 83.6% x 578 = 483.2 -> 483**; заметка: The study itself reports this cumulative estimate (abstract: 84%). If n = 403: 337.

**Ключевые поля выборки:**
- **n_bettors: 578** — Table 1 — «Variable | Frequency (578) | Percentage»
- **sample_type: bettor_recruited** — Study design — «The design necessitated visits to betting centers in the Volta Region of Ghana for the collection of data from young adults engaged in sports betting at a point in time.»
- **sampling: venue_intercept** — Sample size determination and sampling procedure — «participants were recruited in each selected town within a district using a convenient sampling approach. Any potential participant who was readily available and willing to participate at any sports betting center was included»
- **betting_period: current** — Study population — «youths aged 18 to 35 years who engaged in sports betting and resided in the Volta Region of Ghana»

**Остальные поля:**
- parent_population: NA — Study population — «The study was carried out among youths aged 18 to 35 years who engaged in sports betting and resided in the Volta Region of Ghana.»
- min_frequency: none — Study population — «youths aged 18 to 35 years who engaged in sports betting»
- country: GHA — Study site description — «The Volta region of Ghana was used as a case for the conduct of this study.»
- subnational: Volta Region — Study site description — «The Volta region of Ghana was used as a case for the conduct of this study.»
- data_years: 2023 — Study variables and instrument — «The data were collected from May to June 2023.»
- design: cross-sectional — Study design — «A cross-sectional design was adopted for this study.»
- gambling_disclosed: NR — Sample size determination and sampling procedure — «Any potential participant who was readily available and willing to participate at any sports betting center was included in the study»
- betting_mode: NR — Study design; Abstract — «To be considered as a betting center, the center needed to have an operational license, sell computerized betting tickets to their clients»
- pct_online: NR — Abstract — «This study aimed to investigate the effects of online sports betting on psychological distress»
- pct_inplay: NR — NA
- pct_dfs: NR — NA
- pct_esports: NR — NA
- sports_lottery: no — Study design — «sell computerized betting tickets to their clients»
- mixed_race: no — Study population — «who engaged in sports betting»
- legal_status: regulated legal market — Study design; Introduction — «the center needed to have an operational license ... the government has placed a 10% tax on bet winnings»
- n_invited: NR — NA
- n_responded: 578 — Table 1 — «Variable | Frequency (578) | Percentage»
- response_rate: NR — Sample size determination and sampling procedure — «A 5% non-response rate was added to account for possible non-response or incomplete data, resulting in a minimum total of 405 individuals to be interviewed.»
- age_mean: NR — Table 1 — «18–24 | 375 | 64.9%»
- age_sd: NR — NA
- age_min: 18 — Study population — «The study was carried out among youths aged 18 to 35 years»
- age_max: 35 — Study population — «The study was carried out among youths aged 18 to 35 years»
- age_group: adults — Study population — «individuals under 18 years old are legally prohibited from participating in betting in Ghana and were therefore excluded»
- pct_male: 93.9 — Table 1 — «Male | 543 | 93.9%»
- mode: face-to-face — Study variables and instrument — «The study made use of an interviewer-administered questionnaire.»
- weights: no — Statistical analyses — «Descriptive analysis involving participant characteristics, followed by reliability exploration and estimation of gambling prevalence»
- instruments: PGSI (9 items, past 12 months; language version not reported) — Study variables and instrument — «Gambling severity, the independent variable, was assessed using the nine-item Problem Gambling Severity Index (PGSI), which is a widely validated scale [40–42].»
- instrument_validated_in_language: NR — Study variables and instrument — «the nine-item Problem Gambling Severity Index (PGSI), which is a widely validated scale [40–42]»
- industry_funding: no — Funding — «There was no specific funding for this study.»
- funding_coi: No specific funding; authors declare no competing interests; permission obtained from betting companies/centres for data collection — Funding; Competing interests; Ethics — «There was no specific funding for this study. ... The authors declare no competing interests.»
- pub_status: journal — Header — «BMC public health; DOI: 10.1186/s12889-024-19550-2»
- language: English — Full text — «Betting high, feeling low: a cross-sectional examination of gambling severity and psychological distress among Ghanaian youth»
- notes: Sample size is inconsistent: the abstract says 403 participants and the target was 405, but Table 1 reports 578, and its percentages match 578 (e.g., 543/578 = 93.9%). n = 578 is used per the table rule. The age and sex fields describe all participants, who are all sports bettors. Table 1 has a '31 and above' band (48) although the population is defined as 18-35. The interview language is not reported (73.7% of the sample is Ewe). The online vs land-based share is not reported: participants were recruited at land-based licensed betting centres, but the title and abstract refer to online sport…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame = licensed betting centres in 5 of the 10 districts with centres. It misses youth bettors who bet only online or outside centres. — Sample size determination and sampling procedure — «Ten of the eighteen districts/municipalities in the region were identified to have designated betting centers. Secondly, five of the districts/municipalities (…»
2. способ отбора: **no** — The final stage was convenience sampling of available bettors at centres. — Sample size determination and sampling procedure — «participants were recruited in each selected town within a district using a convenient sampling approach»
3. размер выборки: **yes** — 578 bettors per Table 1 (403 per abstract); both are >= 385. — Table 1 — «Variable | Frequency (578) | Percentage»
4. описание выборки и условий: **yes** — Age, sex, setting, country and dates are reported. — Table 1; Study variables and instrument — «The data were collected from May to June 2023.»
5. охват (пропуски): **unclear** — Missing PGSI data are not reported, and n is inconsistent (403 vs 578). — Abstract; Table 1 — «Four hundred and three (403) participants were selected»
6. валидность определения случая: **unclear** — PGSI with standard thresholds, but the language version of the interviewer-administered questionnaire is not reported. — Statistical analyses — «a total score of zero was classified as non-problematic, 1 or 2 as low level, 3 to 7 as moderate level, and 8 and above as problem gambling [40]»
7. единое надёжное измерение: **yes** — The same interviewer-administered PGSI was used for everyone, and alpha is reported. — Study variables and instrument — «The scale demonstrated an overall coefficient alpha (α) of 0.80.»
8. статистика (числитель и знаменатель): **unclear** — Only percentages are reported, the denominator conflicts (403 vs 578), and there are no CIs for prevalence. — Gambling severity among participants — «an estimated 39.8% of the cohort fell within the category of problem gambling»
9. отклик: **no** — Convenience recruitment at venues, with no denominator of people approached and no response rate. — Sample size determination and sampling procedure — «Any potential participant who was readily available and willing to participate at any sports betting center was included in the study until the required sample…»

Правки:
- 

Проверено: да

---

## ST022 · Stone 2024 · Journal of gambling studies

Основной отчёт R2661: [текст](../../fulltext/text/R2661.txt) — «Gambling in Victoria: Changes in Participation, Problem Gambling and Gambling Environment Between 2008 and 2018.» — [DOI](https://doi.org/10.1007/s10899-024-10282-x)
Приложен R5777: [текст](../../fulltext/text/R5777.txt) — «Risk Factors for Gambling Problems: An Analysis by Gender.»
Связь отчётов: Victorian gambling prevalence studies 2008, 2014 and 2018 (R2661); R5777 analyses the 2008 study (A Study of Gambling in Victoria, August-October 2008, N = 15,000)
Расхождения в тексте: 2008: summing R5777 Table 3 sports-betting Ns (110+7+419+72 = 608; 79 at-risk) gives 13.0% at PGSI 3+. R2661 Table 5 reports 13.1%. These counts are weighted (R5777: 'After weighting, the number of included respondents was 8917'). The Table 2 percentages × group Ns agree with the Table 3 Ns (9.9% × 4227 ≈ 419; 25.4% × 285 ≈ 72; 2.6% × 4228 ≈ 110; 3.9% × 179 ≈ 7). R5777 has internal discrepancies: the text says 463 at-risk (284 males), but Table 2 gives 285 male AR, and the Table 2 Ns sum to 8,919 rather than 8,917. The 2008 sports question included event betting. 2014: the R2661 Methods say SGHV 2014 was not used for frequency analysis, yet Tables 1, 4 and 5 report 2014 monthly and weekly sports-betting estimates. R2661 gives no counts for sports bettors in any year, so its estimates are weighted percentages only (cases and n = NR). The 2014 and 2018 response rates are frame-specific, s…
Заметка ИИ: I extracted three samples (2008, 2014, 2018). The 2008 and 2014 surveys used the Queensland 5-point modified PGSI response scale, which R5777 calls non-validated; 2018 used the original PGSI. Only 2008 has traceable counts, and those are weighted counts from R5777 (n = 608; at-risk 79). For 2014 and 2018, the sports-bettor n can only be approximated from weighted participation (~650 and ~617). R2661 states no funding source in the text provided.

### ST022-1 · Victoria SGV 2008 – sports bettors in CATI population survey (N=15,000)
Отчёты: R2661 (main); R5777

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | PGSI · PGSI>=8 (0-27, Queensland-modified response scale) | **L3** | **NR / NR** |  | R2661, Table 4 (2008, Yearly) | «Sports betting / 2.8(1.4, 5.4)» |
| E2 | all | PGSI · PGSI>=3 (0-27, Queensland-modified response scale) | **L2** | **NR / NR** |  | R2661, Table 5 (2008, Yearly) | «Sports betting / 13.1(9.6, 17.6)» |
| E3 | all | PGSI · PGSI>=3 (0-27, Queensland-modified response scale) | **L2** | **79 / 608** | 13.0 | R5777, Table 3 | «Betting on sports or event results ... N / 110 / 7 / 419 / 72» |
| E4 | all | PGSI · PGSI 0-2 | **below** | **529 / 608** | 87.0 | R5777, Table 3 | «N / 110 / 7 / 419 / 72» |
| E5 | male | PGSI · PGSI>=3 (0-27, Queensland-modified response scale) | **L2** | **72 / 491** | 14.7 | R5777, Table 3; Table 2 | «Betting on sports or event results / 2.6 / 3.9 / 9.9 / 25.4a ... N / 110 / 7 / 419 / 72» |
| E6 | male | PGSI · PGSI 0-2 | **below** | **419 / 491** | 85.3 | R5777, Table 3 | «N / 110 / 7 / 419 / 72» |
| E7 | female | PGSI · PGSI>=3 (0-27, Queensland-modified response scale) | **L2** | **7 / 117** | 6.0 | R5777, Table 3; Table 2 | «Betting on sports or event results / 2.6 / 3.9 / 9.9 / 25.4a ... N / 110 / 7 / 419 / 72» |
| E8 | female | PGSI · PGSI 0-2 | **below** | **110 / 117** | 94.0 | R5777, Table 3 | «N / 110 / 7 / 419 / 72» |
| E9 | monthly sports bettors | PGSI · PGSI>=8 | **L3** | **NR / NR** |  | R2661, Table 4 (2008, Monthly) | «Sports betting / 2.8(1.4, 5.4) / 4.7(2.0, 10.7) / 6.5(1.8, 21.0)» |
| E10 | monthly sports bettors | PGSI · PGSI>=3 | **L2** | **NR / NR** |  | R2661, Table 5 (2008, Monthly) | «Sports betting / 13.1(9.6, 17.6) / 20.6(13.9, 29.3) / 27.1(16.0, 42.1)» |
| E11 | weekly sports bettors | PGSI · PGSI>=8 | **L3** | **NR / NR** |  | R2661, Table 4 (2008, Weekly) | «Sports betting / 2.8(1.4, 5.4) / 4.7(2.0, 10.7) / 6.5(1.8, 21.0)» |
| E12 | weekly sports bettors | PGSI · PGSI>=3 | **L2** | **NR / NR** |  | R2661, Table 5 (2008, Weekly) | «Sports betting / 13.1(9.6, 17.6) / 20.6(13.9, 29.3) / 27.1(16.0, 42.1)» |

- E1: cumulative: yes; источник порога: standard; правило: PGSI row; >=8 = L3; у авторов: «problem gambling (PG)»; главная у авторов: yes; период: past 12 months; взвешенная доля: 2.8; заметка: Weighted %, 95% CI 1.4-5.4; counts not reported. Includes event betting.
- E2: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 = L2; у авторов: «high-risk gamblers (MPG: moderate risk + problem)»; главная у авторов: yes; период: past 12 months; взвешенная доля: 13.1; заметка: Weighted %, 95% CI 9.6-17.6.
- E3: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 = L2; у авторов: «at-risk (AR) gamblers»; главная у авторов: no; период: past 12 months; **расчёт: R5777 Table 3 sports N: F AR 7 + M AR 72 = 79; n = 110+7+419+72 = 608**; заметка: Counts are weighted counts. 79/608 = 13.0%, consistent with R2661 13.1%.
- E4: cumulative: no; источник порога: study's own; правило: PGSI row; band 0-2 lower bound 0 = below; у авторов: «non-problem gambler (NP)»; главная у авторов: no; период: past 12 months; **расчёт: F NP 110 + M NP 419 = 529; n = 608**; заметка: Weighted counts; NP combines PGSI 0 and 1-2.
- E5: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 = L2; у авторов: «at-risk (AR) gamblers»; главная у авторов: no; период: past 12 months; **расчёт: n = M NP 419 + M AR 72 = 491 (Table 2: 9.9% x 4227 = 418.5; 25.4% x 285 = 72.4)**; заметка: Weighted counts; 14.7%.
- E6: cumulative: no; источник порога: study's own; правило: PGSI row; band 0-2 lower bound 0 = below; у авторов: «non-problem gambler (NP)»; главная у авторов: no; период: past 12 months; **расчёт: 419 + 72 = 491**; заметка: Weighted counts.
- E7: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 = L2; у авторов: «at-risk (AR) gamblers»; главная у авторов: no; период: past 12 months; **расчёт: n = F NP 110 + F AR 7 = 117 (Table 2: 2.6% x 4228 = 109.9; 3.9% x 179 = 7.0)**; заметка: Weighted counts; 6.0%; authors note small n for females.
- E8: cumulative: no; источник порога: study's own; правило: PGSI row; band 0-2 lower bound 0 = below; у авторов: «non-problem gambler (NP)»; главная у авторов: no; период: past 12 months; **расчёт: 110 + 7 = 117**; заметка: Weighted counts.
- E9: cumulative: yes; источник порога: standard; правило: PGSI row; >=8 = L3; у авторов: «problem gambling (PG)»; главная у авторов: no; период: past 12 months; взвешенная доля: 4.7; заметка: At least 12 days/year; 95% CI 2.0-10.7.
- E10: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 = L2; у авторов: «high-risk gamblers (MPG)»; главная у авторов: no; период: past 12 months; взвешенная доля: 20.6; заметка: 95% CI 13.9-29.3.
- E11: cumulative: yes; источник порога: standard; правило: PGSI row; >=8 = L3; у авторов: «problem gambling (PG)»; главная у авторов: no; период: past 12 months; взвешенная доля: 6.5; заметка: At least 52 days/year; 95% CI 1.8-21.0.
- E12: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 = L2; у авторов: «high-risk gamblers (MPG)»; главная у авторов: no; период: past 12 months; взвешенная доля: 27.1; заметка: 95% CI 16.0-42.1.

**Ключевые поля выборки:**
- **n_bettors: 608** — R5777, Table 3 (N row, Betting on sports or event results) — «N | 110 | 7 | 419 | 72»
- **sample_type: rep_survey_subsample** — R2661, Methods — «The SGV 2008 consisted of random digit dialling (RDD) of landline phones to conduct a CATI ... survey of 15,000 Victorians, 18 years and older»
- **sampling: probability** — R2661, Methods — «The sample was stratified by the eight state government regions and by high, medium, and low EGM expenditure ... High EGM expenditure areas were oversampled»
- **betting_period: past 12 months** — R2661, Gambling Participation — «Gambling participation or yearly gambling refers to those who gambled at least once in a year»

**Остальные поля:**
- parent_population: Adults 18+ resident in Victoria, Australia (landline households) — R2661, Methods — «random digit dialling (RDD) of landline phones to conduct a CATI ... survey of 15,000 Victorians, 18 years and older, in 2008»
- min_frequency: none — R2661, Table 4 — «Sports betting | 2.8(1.4, 5.4)»
- country: AUS — R2661, Methods — «cross-sectional population prevalence studies of gambling and health in Victoria»
- subnational: Victoria — R2661, Methods — «a CATI (Computer Assisted Telephone Interviews) survey of 15,000 Victorians, 18 years and older, in 2008»
- data_years: 2008 — R5777, Methods: Recruitment and Sampling — «Conducted between August–October 2008, 15,000 adults (18 years+) were surveyed.»
- design: prevalence survey — R2661, Methods — «three large observational, cross-sectional population prevalence studies of gambling and health in Victoria»
- gambling_disclosed: yes — R2661, Strengths and Limitations — «The large computer-assisted telephone interview (CATI) surveys were all described as gambling and health surveys»
- betting_mode: both — R2661, Gambling Mode — «Online gambling ever was identified by combining those who had endorsed "over the internet", "computer games online", and "on a mobile phone" for the SGV 2008»
- pct_online: NR — R2661, Sports Gambling Online — «More males, 7.5%, gambled on sports online than females, 1.4% and this increased from 1.5% and 0.3% respectively.»
- pct_inplay: NR — NA
- pct_dfs: NR — NA
- pct_esports: NR — NA
- sports_lottery: no — R2661, Gambling Activities — «lotto (Lotto, Powerball or the Pools)»
- mixed_race: no — R2661, Gambling Activities — «In SGV 2008, event betting was included in the sports betting question resulting in a slight overestimation of sports betting.»
- legal_status: regulated legal market — R2661, Introduction — «Tabcorp holding the exclusive wagering and betting licence in Victoria ... an exception is made for wagering in the form of race and sports betting, and lotter…»
- n_invited: NR — NA
- n_responded: 15000 — R2661, Methods — «CATI (Computer Assisted Telephone Interviews) survey of 15,000 Victorians»
- response_rate: 43.5 — R2661, Methods — «The response rate was 43.5% based on the more conservative calculation.»
- age_mean: NR — NA
- age_sd: NR — NA
- age_min: 18 — R2661, Methods — «survey of 15,000 Victorians, 18 years and older»
- age_max: NR — NA
- age_group: adults — R2661, Methods — «15,000 Victorians, 18 years and older»
- pct_male: 80.8 — R5777, Table 3 — «N | 110 | 7 | 419 | 72 (F NP, F AR, M NP, M AR)»
- mode: telephone — R2661, Methods — «CATI (Computer Assisted Telephone Interviews) survey»
- weights: yes — R2661, Analysis; R5777 Methods — «Weighted percentages with 95% confidence intervals were calculated.»
- instruments: PGSI (Queensland modification: 5-point response scale never/rarely/sometimes/most of the time/almost always, rarely+sometimes scored 1; range 0-27; language version not stated) — R2661, Problem Gambling — «the SGV 2008 and SGHV 2014 used the Queensland modification of the item response scale consisting of five points ... Responses of 'rarely' and 'sometimes' were…»
- instrument_validated_in_language: no — R5777, Measures; Discussion — «Unlike the validated version, responses were asked and scored as never = 0, rarely = 1, sometimes = 1, most of the time = 2, and always = 3. ... Use of a non-v…»
- industry_funding: NR — R5777, Acknowledgments — «The Victorian Responsible Gambling Foundation provided financial support for this project»
- funding_coi: R2661: funding not reported in the text provided. R5777 was funded by the Victorian Responsible Gambling Foundation; its authors have received funding and consultancies from governments and industry operators, and declare no COI for that manuscript. — R5777, Acknowledgments; Conflict of interest — «All authors have received funding support and provided consultancies to organisations directly and indirectly benefiting from gambling, including Australian go…»
- pub_status: journal — R2661 header — «Journal of gambling studies; DOI: 10.1007/s10899-024-10282-x»
- language: English — R2661 full text — «Gambling in Victoria: Changes in Participation, Problem Gambling and Gambling Environment Between 2008 and 2018»
- notes: The 2008 sports betting question included event betting (slight overestimate). R2661 gives only weighted % with 95% CI (no counts). n_bettors 608 and pct_male 80.8 (491/608) are WEIGHTED counts derived from R5777 Table 3. R5777's analytic sample after weighting = 8,917; its exclusion of infrequent low-risk-only gamblers does not affect sports bettors. Population sports-betting participation was 4.0% (weighted). Age not reported for bettors. The same survey is also reported in Hare 2009 and Billi et al. 2015 (not attached). High-EGM-spend areas were oversampled; landline frame only. R5777 Tabl…

**Риск смещения (JBI):**
1. рамка выборки: **unclear** — RDD of landline phones only; mobile-only households not in frame (authors list as limitation). — R2661, Methods; Strengths and Limitations — «sampling has transitioned from 100% landline or household survey to a mixed landline and mobile phone»
2. способ отбора: **yes** — Stratified random digit dialling (probability sample). — R2661, Methods — «The SGV 2008 consisted of random digit dialling (RDD) of landline phones ... The sample was stratified by the eight state government regions»
3. размер выборки: **yes** — About 608 (weighted) sports bettors >= 385. — R5777, Table 3 — «N | 110 | 7 | 419 | 72»
4. описание выборки и условий: **unclear** — Setting, country and dates reported; age/sex composition of sample/bettors not described (only prevalence by subgroup). — R5777, Methods — «Conducted between August–October 2008, 15,000 adults (18 years+) were surveyed.»
5. охват (пропуски): **unclear** — Missing PGSI data among sports bettors not reported. — R2661, Strengths and Limitations — «the PGSI was administered to all gamblers»
6. валидность определения случая: **no** — PGSI with modified 5-point response scale, described as non-validated version. — R5777, Discussion — «Use of a non-validated version of the PGSI may have affected assignment to PGSI groups.»
7. единое надёжное измерение: **yes** — Same PGSI version via CATI for all gamblers; Cronbach alpha 0.87 reported. — R5777, Measures — «The 9-item PGSI was administered to all gamblers. ... Cronbach's alpha = 0.87.»
8. статистика (числитель и знаменатель): **yes** — Weighted % with 95% CI in R2661; weighted counts by PGSI group traceable in R5777. — R2661, Analysis; R5777 Table 3 — «Weighted percentages with 95% confidence intervals were calculated.»
9. отклик: **no** — Response 43.5% (<60%); population weighting reported but not described as non-response adjustment; no responder/non-responder comparison. — R2661, Methods — «The response rate was 43.5% based on the more conservative calculation.»

Правки:
- 

Проверено: да

### ST022-2 · Victoria SGHV 2014 – sports bettors in dual-frame CATI population survey (N=13,554)
Отчёты: R2661 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | PGSI · PGSI>=8 (0-27, Queensland-modified response scale) | **L3** | **NR / NR** |  | R2661, Table 4 (2014, Yearly) | «Sports betting / 2.8(1.4, 5.4) / 4.7(2.0, 10.7) / 6.5(1.8, 21.0) / 7.5(2.8, 18.5)» |
| E2 | all | PGSI · PGSI>=3 (0-27, Queensland-modified response scale) | **L2** | **NR / NR** |  | R2661, Table 5 (2014, Yearly) | «Sports betting / 13.1(9.6, 17.6) / 20.6(13.9, 29.3) / 27.1(16.0, 42.1) / 16.5(10.3, 25.4)» |
| E3 | monthly sports bettors | PGSI · PGSI>=8 | **L3** | **NR / NR** |  | R2661, Table 4 (2014, Monthly) | «7.5(2.8, 18.5) / 10.1(4.3, 22.1) / 12.8(3.5, 37.2)» |
| E4 | monthly sports bettors | PGSI · PGSI>=3 | **L2** | **NR / NR** |  | R2661, Table 5 (2014, Monthly) | «16.5(10.3, 25.4) / 29.2(19.4, 41.5) / 31.7(17.3, 50.8)» |
| E5 | weekly sports bettors | PGSI · PGSI>=8 | **L3** | **NR / NR** |  | R2661, Table 4 (2014, Weekly) | «7.5(2.8, 18.5) / 10.1(4.3, 22.1) / 12.8(3.5, 37.2)» |
| E6 | weekly sports bettors | PGSI · PGSI>=3 | **L2** | **NR / NR** |  | R2661, Table 5 (2014, Weekly) | «16.5(10.3, 25.4) / 29.2(19.4, 41.5) / 31.7(17.3, 50.8)» |

- E1: cumulative: yes; источник порога: standard; правило: PGSI row; >=8 = L3; у авторов: «problem gambling (PG)»; главная у авторов: yes; период: past 12 months; взвешенная доля: 7.5; заметка: Weighted %, 95% CI 2.8-18.5; counts not reported.
- E2: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 = L2; у авторов: «high-risk gamblers (MPG)»; главная у авторов: yes; период: past 12 months; взвешенная доля: 16.5; заметка: Weighted %, 95% CI 10.3-25.4.
- E3: cumulative: yes; источник порога: standard; правило: PGSI row; >=8 = L3; у авторов: «problem gambling (PG)»; главная у авторов: no; период: past 12 months; взвешенная доля: 10.1; заметка: 95% CI 4.3-22.1; frequency data for 2014 described as incomplete.
- E4: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 = L2; у авторов: «high-risk gamblers (MPG)»; главная у авторов: no; период: past 12 months; взвешенная доля: 29.2; заметка: 95% CI 19.4-41.5.
- E5: cumulative: yes; источник порога: standard; правило: PGSI row; >=8 = L3; у авторов: «problem gambling (PG)»; главная у авторов: no; период: past 12 months; взвешенная доля: 12.8; заметка: 95% CI 3.5-37.2.
- E6: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 = L2; у авторов: «high-risk gamblers (MPG)»; главная у авторов: no; период: past 12 months; взвешенная доля: 31.7; заметка: 95% CI 17.3-50.8.

**Ключевые поля выборки:**
- **n_bettors: NR** — R2661, Table 1 — «Sports betting | ... | 4.8(4.0, 5.6)»
- **sample_type: rep_survey_subsample** — R2661, Methods — «The 13,554 CATI surveys conducted included 12,551 landline and 1,003 mobile surveys.»
- **sampling: probability** — R2661, Methods — «dual frame sampling using RDD methodology ... the sample was stratified by eight state government regions and by high, medium, and low EGM expenditure»
- **betting_period: past 12 months** — R2661, Gambling Participation — «Gambling participation or yearly gambling refers to those who gambled at least once in a year»

**Остальные поля:**
- parent_population: Adults 18+ resident in Victoria, Australia — R2661, Methods — «The SGHV 2014 sampled Victorians aged 18 years and older using dual frame sampling using RDD methodology.»
- min_frequency: none — R2661, Table 4 — «Sports betting ... 7.5(2.8, 18.5)»
- country: AUS — R2661, Methods — «The SGHV 2014 sampled Victorians aged 18 years and older»
- subnational: Victoria — R2661, Methods — «The SGHV 2014 sampled Victorians aged 18 years and older using dual frame sampling»
- data_years: 2014 — R2661, Methods — «Study of Gambling and Health in Victoria (SGHV) – Findings from the Victorian Prevalence Study 2014»
- design: prevalence survey — R2661, Methods — «three large observational, cross-sectional population prevalence studies of gambling and health in Victoria»
- gambling_disclosed: yes — R2661, Strengths and Limitations — «The large computer-assisted telephone interview (CATI) surveys were all described as gambling and health surveys»
- betting_mode: NR — R2661, Gambling Mode — «SGHV 2014 was not used for online gambling analysis due to limited information collected for gambling channels»
- pct_online: NR — R2661, Gambling Mode — «SGHV 2014 was not used for online gambling analysis»
- pct_inplay: NR — NA
- pct_dfs: NR — NA
- pct_esports: NR — NA
- sports_lottery: no — R2661, Gambling Activities — «lotto (Lotto, Powerball or the Pools)»
- mixed_race: no — R2661, Gambling Activities — «In SGHV 2014 and VPGHS 2018–2019 sports betting was asked as a stand-alone question.»
- legal_status: regulated legal market — R2661, Introduction — «an exception is made for wagering in the form of race and sports betting, and lotteries.»
- n_invited: NR — NA
- n_responded: 13554 — R2661, Methods — «The 13,554 CATI surveys conducted included 12,551 landline and 1,003 mobile surveys.»
- response_rate: NR — R2661, Methods — «The response rates based on the more conservative calculation were reported as 58% for landlines and 31% for mobile surveys.»
- age_mean: NR — NA
- age_sd: NR — NA
- age_min: 18 — R2661, Methods — «sampled Victorians aged 18 years and older»
- age_max: NR — NA
- age_group: adults — R2661, Methods — «Victorians aged 18 years and older»
- pct_male: NR — NA
- mode: telephone — R2661, Methods — «The 13,554 CATI surveys»
- weights: yes — R2661, Analysis — «Weighted percentages with 95% confidence intervals were calculated.»
- instruments: PGSI (Queensland modification: 5-point response scale, rarely+sometimes scored 1; range 0-27; language version not stated) — R2661, Problem Gambling — «the SGV 2008 and SGHV 2014 used the Queensland modification of the item response scale consisting of five points»
- instrument_validated_in_language: no — R2661, Problem Gambling — «The Productivity Commission found the modified PGSI underestimated the number of PG and overestimated MRG based on simulations»
- industry_funding: NR — NA
- funding_coi: Not reported in the text provided for R2661. — NA
- pub_status: journal — R2661 header — «Journal of gambling studies; DOI: 10.1007/s10899-024-10282-x»
- language: English — R2661 full text — «Gambling in Victoria: Changes in Participation, Problem Gambling and Gambling Environment Between 2008 and 2018»
- notes: Response rates are frame-specific: 58% landline, 31% mobile (no single figure). The n of sports bettors is not reported; weighted participation was 4.8% of 13,554 (~650, approximate, weighted). R2661 says SGHV 2014 was not used for frequency analysis (frequency not collected for all activities), yet Tables 1, 4 and 5 report monthly/weekly sports-betting figures for 2014. The original report (Hare 2015) is not attached. High-EGM-spend areas were oversampled.

**Риск смещения (JBI):**
1. рамка выборки: **yes** — Dual-frame (landline + mobile) RDD covering Victorian adults. — R2661, Methods — «sampled Victorians aged 18 years and older using dual frame sampling using RDD methodology»
2. способ отбора: **yes** — Stratified RDD probability sampling. — R2661, Methods — «the sample was stratified by eight state government regions and by high, medium, and low EGM expenditure»
3. размер выборки: **yes** — Approx. 4.8% of 13,554 = ~650 sports bettors (derived from weighted %; exact n not reported). — R2661, Table 1 — «Sports betting | ... | 4.8(4.0, 5.6)»
4. описание выборки и условий: **unclear** — Setting, country, year reported; sample age/sex composition not described. — R2661, Methods — «The SGHV 2014 sampled Victorians aged 18 years and older»
5. охват (пропуски): **unclear** — Missing PGSI data not reported. — R2661, Strengths and Limitations — «the PGSI was administered to all gamblers»
6. валидность определения случая: **no** — Modified (Queensland 5-point) PGSI response scale, not the validated version. — R2661, Problem Gambling — «used the Queensland modification of the item response scale consisting of five points ... rather than the original four-point scale»
7. единое надёжное измерение: **unclear** — Same instrument and CATI mode for all; reliability not reported for this survey. — R2661, Strengths and Limitations — «the PGSI was administered to all gamblers»
8. статистика (числитель и знаменатель): **no** — Weighted % with CI only; numerator and denominator of sports bettors not reported. — R2661, Table 4 — «Sports betting ... 7.5(2.8, 18.5)»
9. отклик: **no** — Response 58% landline, 31% mobile (<60%); no non-response analysis reported. — R2661, Methods — «The response rates ... were reported as 58% for landlines and 31% for mobile surveys.»

Правки:
- 

Проверено: да

### ST022-3 · Victoria VPGHS 2018-19 – sports bettors in dual-frame CATI population survey (N=10,638)
Отчёты: R2661 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | PGSI · PGSI>=8 (0-27) | **L3** | **NR / NR** |  | R2661, Table 4 (2018, Yearly) | «Sports betting / ... / 3.2(1.1,5.2) / 6.7(1.6,11.8) / 6.5(0.0,14.0)» |
| E2 | all | PGSI · PGSI>=3 (0-27) | **L2** | **NR / NR** |  | R2661, Table 5 (2018, Yearly); Table 6 | «Sports betting / ... / 13.3(9.6,17.0) / 19.6(12.0,27.2) / 20.8(8.8,32.8)» |
| E3 | monthly sports bettors | PGSI · PGSI>=8 | **L3** | **NR / NR** |  | R2661, Table 4 (2018, Monthly) | «3.2(1.1,5.2) / 6.7(1.6,11.8) / 6.5(0.0,14.0)» |
| E4 | monthly sports bettors | PGSI · PGSI>=3 | **L2** | **NR / NR** |  | R2661, Table 5 (2018, Monthly) | «13.3(9.6,17.0) / 19.6(12.0,27.2) / 20.8(8.8,32.8)» |
| E5 | weekly sports bettors | PGSI · PGSI>=8 | **L3** | **NR / NR** |  | R2661, Table 4 (2018, Weekly) | «3.2(1.1,5.2) / 6.7(1.6,11.8) / 6.5(0.0,14.0)» |
| E6 | weekly sports bettors | PGSI · PGSI>=3 | **L2** | **NR / NR** |  | R2661, Table 5 (2018, Weekly) | «13.3(9.6,17.0) / 19.6(12.0,27.2) / 20.8(8.8,32.8)» |
| E7 | online | PGSI · PGSI>=3 | **L2** | **NR / NR** |  | R2661, Table 6 (Sports, Mode: online ever, All) | «Mode: online ever All / 7.2 (5.7,8.8) / 12.6 (8.4,16.7)» |
| E8 | online, female | PGSI · PGSI>=3 | **L2** | **NR / NR** |  | R2661, Table 6 (Sports, online ever, Female) | «Female / 4.6 (2.8,6.5) / 4.2 (0.0,10.3)» |
| E9 | online, male | PGSI · PGSI>=3 | **L2** | **NR / NR** |  | R2661, Table 6 (Sports, online ever, Male) | «Male / 9.3 (6.9,11.6) / 14.2 (9.4,19.0)» |
| E10 | online, 18-24 | PGSI · PGSI>=3 | **L2** | **NR / NR** |  | R2661, Table 6 (Sports, online ever, 18-24) | «18–24 / 17.5 (11.2,23.8) / 21.7 (12.2,31.2)» |
| E11 | online, 25-44 | PGSI · PGSI>=3 | **L2** | **NR / NR** |  | R2661, Table 6 (Sports, online ever, 25-44) | «25–44 / 6.7 (4.5,8.9) / 8.1 (3.1,13.0)» |
| E12 | online, 45-64 | PGSI · PGSI>=3 | **L2** | **NR / NR** |  | R2661, Table 6 (Sports, online ever, 45-64) | «45–64 / 5.6 (3.1,8.0) / 13.4 (2.7,24.2)» |
| E13 | online, 65-74 | PGSI · PGSI>=3 | **L2** | **NR / NR** |  | R2661, Table 6 (Sports, online ever, 65-74) | «65–74 / 2.8 (0.5,5.0) / 13.1 (0.0,32.7)» |
| E14 | land-based | PGSI · PGSI>=3 | **L2** | **NR / NR** |  | R2661, Table 6 (Sports, Mode: land-based venues only, All) | «Mode: land-based venues only All / 3.5 (2.9,4.1) / 14.6 (6.4,22.9)» |
| E15 | land-based, female | PGSI · PGSI>=3 | **L2** | **NR / NR** |  | R2661, Table 6 (Sports, LBVO, Female) | «Female / 2.3 (1.6,3.0) / 22.1 (0.5,43.6)» |
| E16 | land-based, male | PGSI · PGSI>=3 | **L2** | **NR / NR** |  | R2661, Table 6 (Sports, LBVO, Male) | «Male / 4.9 (3.8,6.0) / 13.0 (4.1,21.9)» |
| E17 | land-based, 18-24 | PGSI · PGSI>=3 | **L2** | **NR / NR** |  | R2661, Table 6 (Sports, LBVO, 18-24) | «18–24 / 8.0 (4.3,11.8) / 16.3 (0.0,39.0)» |
| E18 | land-based, 25-44 | PGSI · PGSI>=3 | **L2** | **NR / NR** |  | R2661, Table 6 (Sports, LBVO, 25-44) | «25–44 / 3.5 (2.2,4.7) / 14.7 (3.9,25.4)» |
| E19 | land-based, 45-64 | PGSI · PGSI>=3 | **L2** | **NR / NR** |  | R2661, Table 6 (Sports, LBVO, 45-64) | «45–64 / 3.2 (2.2,4.2) / 15.1 (0.0,34.0)» |
| E20 | land-based, 65-74 | PGSI · PGSI>=3 | **L2** | **NR / NR** |  | R2661, Table 6 (Sports, LBVO, 65-74) | «65–74 / 2.9 (1.8,4.1) / 10.9 (0.0,27.1)» |

- E1: cumulative: yes; источник порога: standard; правило: PGSI row; >=8 = L3; у авторов: «problem gambling (PG)»; главная у авторов: yes; период: past 12 months; взвешенная доля: 3.2; заметка: Weighted %, 95% CI 1.1-5.2; counts not reported.
- E2: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 = L2; у авторов: «high-risk gamblers (MPG)»; главная у авторов: yes; период: past 12 months; взвешенная доля: 13.3; заметка: Weighted %, 95% CI 9.6-17.0.
- E3: cumulative: yes; источник порога: standard; правило: PGSI row; >=8 = L3; у авторов: «problem gambling (PG)»; главная у авторов: no; период: past 12 months; взвешенная доля: 6.7; заметка: 95% CI 1.6-11.8.
- E4: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 = L2; у авторов: «high-risk gamblers (MPG)»; главная у авторов: no; период: past 12 months; взвешенная доля: 19.6; заметка: 95% CI 12.0-27.2.
- E5: cumulative: yes; источник порога: standard; правило: PGSI row; >=8 = L3; у авторов: «problem gambling (PG)»; главная у авторов: no; период: past 12 months; взвешенная доля: 6.5; заметка: 95% CI 0.0-14.0.
- E6: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 = L2; у авторов: «high-risk gamblers (MPG)»; главная у авторов: no; период: past 12 months; взвешенная доля: 20.8; заметка: 95% CI 8.8-32.8.
- E7: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 = L2; у авторов: «high-risk gamblers (MPG)»; главная у авторов: no; период: past 12 months; взвешенная доля: 12.6; заметка: Online ever = gambled online on any activity; 95% CI 8.4-16.7.
- E8: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 = L2; у авторов: «high-risk gamblers (MPG)»; главная у авторов: no; период: past 12 months; взвешенная доля: 4.2; заметка: 95% CI 0.0-10.3.
- E9: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 = L2; у авторов: «high-risk gamblers (MPG)»; главная у авторов: no; период: past 12 months; взвешенная доля: 14.2; заметка: 95% CI 9.4-19.0.
- E10: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 = L2; у авторов: «high-risk gamblers (MPG)»; главная у авторов: no; период: past 12 months; взвешенная доля: 21.7; заметка: 95% CI 12.2-31.2.
- E11: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 = L2; у авторов: «high-risk gamblers (MPG)»; главная у авторов: no; период: past 12 months; взвешенная доля: 8.1; заметка: 95% CI 3.1-13.0.
- E12: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 = L2; у авторов: «high-risk gamblers (MPG)»; главная у авторов: no; период: past 12 months; взвешенная доля: 13.4; заметка: 95% CI 2.7-24.2.
- E13: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 = L2; у авторов: «high-risk gamblers (MPG)»; главная у авторов: no; период: past 12 months; взвешенная доля: 13.1; заметка: 95% CI 0.0-32.7; 75+ cell blank.
- E14: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 = L2; у авторов: «high-risk gamblers (MPG)»; главная у авторов: no; период: past 12 months; взвешенная доля: 14.6; заметка: LBVO = never gambled online on any activity; 95% CI 6.4-22.9.
- E15: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 = L2; у авторов: «high-risk gamblers (MPG)»; главная у авторов: no; период: past 12 months; взвешенная доля: 22.1; заметка: 95% CI 0.5-43.6; small n per authors.
- E16: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 = L2; у авторов: «high-risk gamblers (MPG)»; главная у авторов: no; период: past 12 months; взвешенная доля: 13.0; заметка: 95% CI 4.1-21.9.
- E17: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 = L2; у авторов: «high-risk gamblers (MPG)»; главная у авторов: no; период: past 12 months; взвешенная доля: 16.3; заметка: 95% CI 0.0-39.0.
- E18: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 = L2; у авторов: «high-risk gamblers (MPG)»; главная у авторов: no; период: past 12 months; взвешенная доля: 14.7; заметка: 95% CI 3.9-25.4.
- E19: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 = L2; у авторов: «high-risk gamblers (MPG)»; главная у авторов: no; период: past 12 months; взвешенная доля: 15.1; заметка: 95% CI 0.0-34.0.
- E20: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 = L2; у авторов: «high-risk gamblers (MPG)»; главная у авторов: no; период: past 12 months; взвешенная доля: 10.9; заметка: 95% CI 0.0-27.1; 75+ cell blank.

**Ключевые поля выборки:**
- **n_bettors: NR** — R2661, Table 1 — «Sports betting | ... | 5.8(5.2, 6.4)»
- **sample_type: rep_survey_subsample** — R2661, Methods — «using dual frame sampling split 50/50 between landline and mobile numbers and RDD methodology»
- **sampling: probability** — R2661, Methods — «dual frame sampling split 50/50 between landline and mobile numbers and RDD methodology ... sampling quota was set in the landline sample»
- **betting_period: past 12 months** — R2661, Gambling Participation — «Gambling participation or yearly gambling refers to those who gambled at least once in a year»

**Остальные поля:**
- parent_population: Adults 18+ resident in Victoria, Australia — R2661, Methods — «sampled 10,638 Victorians aged 18 years or above»
- min_frequency: none — R2661, Table 4 — «Sports betting ... 3.2(1.1,5.2)»
- country: AUS — R2661, Methods — «The VPGHS 2018–2019 sampled 10,638 Victorians aged 18 years or above»
- subnational: Victoria — R2661, Methods — «The VPGHS 2018–2019 sampled 10,638 Victorians aged 18 years or above»
- data_years: 2018-2019 — R2661, Methods — «the Victorian population gambling and health study (VPGHS) 2018–2019 (Rockloff et al., 2020)»
- design: prevalence survey — R2661, Methods — «three large observational, cross-sectional population prevalence studies of gambling and health in Victoria»
- gambling_disclosed: yes — R2661, Strengths and Limitations — «The large computer-assisted telephone interview (CATI) surveys were all described as gambling and health surveys»
- betting_mode: both — R2661, Sports Gambling Online — «Three-quarters of the sports gamblers have gambled online»
- pct_online: 75 — R2661, Sports Gambling Online — «Gambling online on sports has increased so that in 2018 the online mode predominates. Three-quarters of the sports gamblers have gambled online»
- pct_inplay: NR — NA
- pct_dfs: NR — R2661, Gambling Activities — «eSports (0.4%) and fantasy sports (0.3%) in VPGHS 2018-19»
- pct_esports: NR — R2661, Gambling Activities — «These activities included ... eSports (0.4%) and fantasy sports (0.3%) in VPGHS 2018-19»
- sports_lottery: no — R2661, Gambling Activities — «lotto (Lotto, Powerball or the Pools)»
- mixed_race: no — R2661, Gambling Activities — «In SGHV 2014 and VPGHS 2018–2019 sports betting was asked as a stand-alone question.»
- legal_status: regulated legal market — R2661, Introduction; Discussion — «an exception is made for wagering in the form of race and sports betting, and lotteries.»
- n_invited: NR — NA
- n_responded: 10638 — R2661, Methods — «The VPGHS 2018–2019 sampled 10,638 Victorians aged 18 years or above»
- response_rate: NR — R2661, Methods — «The response rates for the landline and mobile frames were 6.0% and 12.6%, respectively.»
- age_mean: NR — NA
- age_sd: NR — NA
- age_min: 18 — R2661, Methods — «Victorians aged 18 years or above»
- age_max: NR — NA
- age_group: adults — R2661, Methods — «Victorians aged 18 years or above»
- pct_male: NR — NA
- mode: telephone — R2661, Strengths and Limitations — «The large computer-assisted telephone interview (CATI) surveys»
- weights: yes — R2661, Analysis — «Weighted percentages with 95% confidence intervals were calculated.»
- instruments: PGSI (original 4-point response options, range 0-27; language version not stated) — R2661, Problem Gambling — «While the VPGHS 2018-19 used the original PGSI response options»
- instrument_validated_in_language: yes — R2661, Strengths and Limitations — «in 2018 there was a return to the original 4-point scale (Ferris & Wynne, 2001)»
- industry_funding: NR — NA
- funding_coi: Not reported in the text provided for R2661. — NA
- pub_status: journal — R2661 header — «Journal of gambling studies; DOI: 10.1007/s10899-024-10282-x»
- language: English — R2661 full text — «Gambling in Victoria: Changes in Participation, Problem Gambling and Gambling Environment Between 2008 and 2018»
- notes: Response rates are frame-specific: 6.0% landline, 12.6% mobile (no single figure). The n of sports bettors is not reported; weighted participation was 5.8% of 10,638 (~617, approximate). eSports (0.4%) and fantasy sports (0.3%) were asked separately and excluded from the analysis. In Table 6, 'online ever' means the respondent gambled online on any activity, not necessarily on sports. The original report (Rockloff et al. 2020) is not attached. No stratification or oversampling in 2018.

**Риск смещения (JBI):**
1. рамка выборки: **yes** — Dual-frame landline+mobile RDD of Victorian adults. — R2661, Methods — «using dual frame sampling split 50/50 between landline and mobile numbers and RDD methodology»
2. способ отбора: **yes** — RDD probability sampling (regional quota in landline frame). — R2661, Methods — «sampling quota was set in the landline sample (38% landline Greater Melbourne, 12% landline rest of Victoria, and 50% mobile)»
3. размер выборки: **yes** — Approx. 5.8% of 10,638 = ~617 sports bettors (derived from weighted %; exact n not reported). — R2661, Table 1 — «Sports betting | ... | 5.8(5.2, 6.4)»
4. описание выборки и условий: **unclear** — Setting, country, years reported; sample age/sex composition not described. — R2661, Methods — «The VPGHS 2018–2019 sampled 10,638 Victorians aged 18 years or above»
5. охват (пропуски): **unclear** — Missing PGSI data not reported. — R2661, Strengths and Limitations — «the PGSI was administered to all gamblers»
6. валидность определения случая: **yes** — Original PGSI with standard thresholds. — R2661, Problem Gambling — «the VPGHS 2018-19 used the original PGSI response options ... ≥ 8, problem gambling (PG)»
7. единое надёжное измерение: **unclear** — Same instrument and CATI mode for all; reliability not reported for this survey. — R2661, Strengths and Limitations — «the PGSI was administered to all gamblers»
8. статистика (числитель и знаменатель): **no** — Weighted % with CI only; counts of sports bettors not reported. — R2661, Table 4 — «Sports betting ... 3.2(1.1,5.2)»
9. отклик: **no** — Response 6.0% landline, 12.6% mobile; no non-response analysis reported. — R2661, Methods — «The response rates for the landline and mobile frames were 6.0% and 12.6%, respectively.»

Правки:
- 

Проверено: да

---

## ST023 · Greer 2023 · Journal of gambling studies

Основной отчёт R2909: [текст](../../fulltext/text/R2909.txt) — «Motivations for Esports Betting and Skin Gambling and Their Association with Gambling Frequency, Problems, and Harm.» — [DOI](https://doi.org/10.1007/s10899-022-10137-3)
Не выписано ИИ: Skin gambling on games of chance (n=325): betting skins on roulette, jackpots and similar is not sports betting. The Total sample column (N=736) was not extracted because it includes respondents who only gambled skins on games of chance. No treatment or self-exclusion groups.
Расхождения в тексте: 1) The text says esports cash betting n = 576 (77.0%), but the abstract and Tables 2, 4, 5, 6 and 7 give n = 567. 567/736 = 77.0%, so 576 looks like a typo; 567 was used. 2) In Table 1, frequency counts (last 6 months) for esports cash betting are 378 at least monthly + 209 less than monthly = 587 non-never, not 567. Likewise skin betting is 112 + 111 = 223 vs 180, and skin gambling is 199 + 163 = 362 vs 325. The 'less than monthly' group includes code 1 'not in the last 6 months', which probably explains the excess. Table 2 denominators were used. 3) The response rate of 25.0% matches 737 completes / 2952 starters. The authors call it 'from eligible participants', but 2952 includes people who were later found ineligible.
Заметка ИИ: One eligible sample (esports bettors). The paper reports PGSI only for two overlapping esports subgroups (cash, skins); there is no figure for all esports bettors. The 6-month entry period and PGSI time frame do not fit the form codes, so both are coded NR. Coding legal_status as 'mixed' rests on the introduction's description (skin betting via unregulated operators, cash betting via wagering operators), not on a statement about each country.

### ST023-1 · Esports bettors (cash and/or skins), MTurk + social media, USA/GBR/CAN/IRL, 2018-2019 (esports cash bettors n=567; esports skin bettors n=180, overlapping)
Отчёты: R2909 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | esports cash bettors | PGSI · PGSI 0 | **below** | **112 / 567** | 19.8 | Table 2 | «0 Non-problem, n (%) / 112 (19.8)» |
| E2 | esports cash bettors | PGSI · PGSI 1-2 | **L1** | **119 / 567** | 21.0 | Table 2 | «1–2 Low risk, n (%) / 119 (21.0)» |
| E3 | esports cash bettors | PGSI · PGSI 3-7 | **L2** | **170 / 567** | 30.0 | Table 2 | «3–7 Moderate risk, n (%) / 170 (30.0)» |
| E4 | esports cash bettors | PGSI · PGSI>=8 | **L3** | **166 / 567** | 29.3 | Table 2 | «8 + Problem, n (%) / 166 (29.3)» |
| E5 | esports skin bettors | PGSI · PGSI 0 | **below** | **32 / 180** | 17.8 | Table 2 | «0 Non-problem, n (%) / 112 (19.8) / 32 (17.8)» |
| E6 | esports skin bettors | PGSI · PGSI 1-2 | **L1** | **43 / 180** | 23.9 | Table 2 | «1–2 Low risk, n (%) / 119 (21.0) / 43 (23.9)» |
| E7 | esports skin bettors | PGSI · PGSI 3-7 | **L2** | **50 / 180** | 27.8 | Table 2 | «3–7 Moderate risk, n (%) / 170 (30.0) / 50 (27.8)» |
| E8 | esports skin bettors | PGSI · PGSI>=8 | **L3** | **55 / 180** | 30.6 | Table 2 | «8 + Problem, n (%) / 166 (29.3) / 55 (30.6)» |

- E1: cumulative: no; источник порога: standard; правило: PGSI row; score 0 is below L1; у авторов: «Non-problem»; главная у авторов: no; период: NR; заметка: PGSI time frame last 6 months. Prevalence is descriptive; not presented as a main estimate.
- E2: cumulative: no; источник порога: standard; правило: PGSI row; 1-2 band starts at L1; у авторов: «Low risk»; главная у авторов: no; период: NR; заметка: PGSI time frame last 6 months.
- E3: cumulative: no; источник порога: standard; правило: PGSI row; 3-7 band starts at L2; у авторов: «Moderate risk»; главная у авторов: no; период: NR; заметка: PGSI time frame last 6 months.
- E4: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ is L3; у авторов: «Problem»; главная у авторов: no; период: NR; заметка: PGSI time frame last 6 months.
- E5: cumulative: no; источник порога: standard; правило: PGSI row; score 0 is below L1; у авторов: «Non-problem»; главная у авторов: no; период: NR; заметка: Overlaps with the esports cash bettor subgroup. PGSI time frame last 6 months.
- E6: cumulative: no; источник порога: standard; правило: PGSI row; 1-2 band starts at L1; у авторов: «Low risk»; главная у авторов: no; период: NR; заметка: Overlaps with the esports cash bettor subgroup.
- E7: cumulative: no; источник порога: standard; правило: PGSI row; 3-7 band starts at L2; у авторов: «Moderate risk»; главная у авторов: no; период: NR; заметка: Overlaps with the esports cash bettor subgroup.
- E8: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ is L3; у авторов: «Problem»; главная у авторов: no; период: NR; заметка: Overlaps with the esports cash bettor subgroup.

**Ключевые поля выборки:**
- **n_bettors: 567** — Table 2 — «Esports cash bettor (n = 567) | Esports skin bettor (n = 180)»
- **sample_type: bettor_recruited** — Methods, Participants and Procedure — «766 were excluded because they did not meet the inclusion criteria of participating in esports cash betting, esports skin betting, or skin gambling in the last 6 months.»
- **sampling: convenience** — Methods, Participants and Procedure — «via online crowdsourcing: (1) Amazon's Mechanical Turk, and (2) social media posts (Facebook, Twitter, Reddit) targeted to online video-gaming, esports, and gambling communities»
- **betting_period: NR** — Methods, Participants and Procedure — «participating in esports cash betting, esports skin betting, or skin gambling in the last 6 months»

**Остальные поля:**
- parent_population: NA (recruited as esports cash bettors, esports skin bettors or skin gamblers aged 18+ in USA, UK, Canada, Ireland) — Methods, Participants and Procedure — «inclusion criteria of participating in esports cash betting, esports skin betting, or skin gambling in the last 6 months»
- min_frequency: none (any esports betting in the last 6 months) — Methods, Participants and Procedure — «activities they had participated in during the last 6 months: (1) esports cash betting (n = 576, 77.0%), (2) esports skin betting (n = 180, 24.5%)»
- country: MULTI: USA, GBR, CAN, IRL — Methods, Participants and Procedure; Table 1 — «did not reside in one of four selected in-scope countries (USA, UK, Canada, Ireland)»
- subnational: NA — Methods, Participants and Procedure — «four selected in-scope countries (USA, UK, Canada, Ireland)»
- data_years: 2018-2019 — Methods, Participants and Procedure — «The sample was recruited between October 2018-February 2019 via online crowdsourcing»
- design: cross-sectional — Abstract — «Data were collected via a cross-sectional online survey with 736 participants aged 18 +»
- gambling_disclosed: NR — Methods, Participants and Procedure — «social media posts (Facebook, Twitter, Reddit) targeted to online video-gaming, esports, and gambling communities»
- betting_mode: NR — Introduction — «Esports cash betting involves gambling money on video gaming competitions (esports), typically via wagering operators or dedicated esports betting providers.»
- pct_online: NR — Introduction — «esports skin betting involves using virtual video game items known as “skins” to bet on esports, most often via unregulated online operators»
- pct_inplay: NR — NA — «NR»
- pct_dfs: NR — NA — «NR»
- pct_esports: all — Methods, Participants and Procedure — «(1) esports cash betting (n = 576, 77.0%), (2) esports skin betting (n = 180, 24.5%)»
- sports_lottery: no — Introduction — «Esports cash betting involves gambling money on video gaming competitions (esports), typically via wagering operators or dedicated esports betting providers.»
- mixed_race: no — Introduction — «Three popular products are esports cash betting, esports skin betting, and skin gambling on games of chance.»
- legal_status: mixed — Introduction — «esports cash betting ... typically via wagering operators ... esports skin betting involves using virtual video game items known as “skins” to bet on esports, …»
- n_invited: NR — Methods, Participants and Procedure — «A total of 2952 respondents started the survey (Mechanical Turk = 1,949; social media posts = 1003).»
- n_responded: 2952 — Methods, Participants and Procedure — «A total of 2952 respondents started the survey (Mechanical Turk = 1,949; social media posts = 1003).»
- response_rate: 25.0 — Methods, Participants and Procedure — «A cull left a total of 737 completes, yielding a 25.0% response rate from eligible participants.»
- age_mean: 28.98 — Table 1 — «Age (scale) | Mean = 28.98 years (SD = 8.07) Range: 18–64 years»
- age_sd: 8.07 — Table 1 — «Mean = 28.98 years (SD = 8.07)»
- age_min: 18 — Table 1 — «Range: 18–64 years»
- age_max: 64 — Table 1 — «Range: 18–64 years»
- age_group: adults — Abstract — «736 participants aged 18 +»
- pct_male: 80.2 — Table 1 — «Male | 590 (80.2)»
- mode: online — Abstract — «Data were collected via a cross-sectional online survey»
- weights: no — Table 2 — «0 Non-problem, n (%) | 112 (19.8)»
- instruments: PGSI (English; adapted to a last-6-months time frame); Short Gambling Harm Screen (SGHS, harm measure, not a PG screen) — Measures, Problem Gambling and Gambling-Related Harm — «Problem gambling was measured using the Problem Gambling Severity Index (PGSI: Ferris & Wynne, 2001) for the last 6-month timeframe.»
- instrument_validated_in_language: yes — Measures, Problem Gambling and Gambling-Related Harm — «Problem Gambling Severity Index (PGSI: Ferris & Wynne, 2001)»
- industry_funding: NR — NA — «NR»
- funding_coi: NR: no funding or conflict-of-interest statement in the supplied text — NA — «NR»
- pub_status: journal — Header — «Journal of gambling studies; DOI: 10.1007/s10899-022-10137-3»
- language: English — Full text — «Motivations for Esports Betting and Skin Gambling and Their Association with Gambling Frequency, Problems, and Harm»
- notes: PGSI is reported only for two overlapping subgroups: esports cash bettors (n=567) and esports skin bettors (n=180). The number who bet on esports by either method is not reported, so no figure for all esports bettors can be given; n_bettors=567 is the larger subgroup. The Total column (N=736) includes skin-only gamblers and was not extracted. Entry period and PGSI time frame were the last 6 months; no form code fits, so both are NR. Age and sex describe the whole sample of 736, not esports bettors only. n_responded = 2952 survey starters; 737 completed; 25.0% response rate as reported. Whethe…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame was MTurk workers and social-media followers of gaming/esports/gambling communities, not a frame covering esports bettors of the four countries. — Methods, Participants and Procedure — «via online crowdsourcing: (1) Amazon's Mechanical Turk, and (2) social media posts (Facebook, Twitter, Reddit) targeted to online video-gaming, esports, and ga…»
2. способ отбора: **no** — Non-probability volunteer online crowdsourcing. — Methods, Participants and Procedure — «The sample was recruited between October 2018-February 2019 via online crowdsourcing»
3. размер выборки: **yes** — Esports cash bettors n=567 (>=385); the skin-bettor subgroup is only 180. — Table 2 — «Esports cash bettor (n = 567) | Esports skin bettor (n = 180)»
4. описание выборки и условий: **yes** — Age, sex, countries, recruitment setting and dates are reported, but age and sex are for the whole sample of 736 rather than esports bettors only. — Methods; Table 1 — «The sub-sample was mostly male (80.2%) with an average age of 28.98 years (SD = 8.07). The majority resided in the USA (73.0%)»
5. охват (пропуски): **yes** — PGSI categories sum to each subgroup n (no missing PGSI among analysed completers); non-completers were excluded before analysis. — Table 2 — «Total, n (%) | 567 (100.0) | 180 (100.0)»
6. валидность определения случая: **yes** — English PGSI with standard 8+ threshold; time frame changed to the last 6 months. — Measures — «categorising gamblers by score into: non-problem (0), low-risk (1–2), moderate-risk (3–7), and problem gambling (8–27)»
7. единое надёжное измерение: **yes** — Same online PGSI, time frame and threshold for all; source cited (Ferris & Wynne 2001). PGSI alpha was not reported in this sample. — Measures — «Problem gambling was measured using the Problem Gambling Severity Index (PGSI: Ferris & Wynne, 2001) for the last 6-month timeframe.»
8. статистика (числитель и знаменатель): **yes** — Counts and denominators are given for each esports subgroup; CI calculable; no weighting required for a convenience sample. — Table 2 — «8 + Problem, n (%) | 166 (29.3) | 55 (30.6)»
9. отклик: **no** — Open online recruitment with no invited denominator; 25% of starters completed, with no non-response handling. — Methods, Participants and Procedure — «A cull left a total of 737 completes, yielding a 25.0% response rate from eligible participants.»

Правки:
- 

Проверено: да

---

## ST024 · Hing 2023 · Journal of behavioral addictions

Основной отчёт R2934: [текст](../../fulltext/text/R2934.txt) — «Situational features of smartphone betting are linked to sports betting harm: An ecological momentary assessment study.» — [DOI](https://doi.org/10.1556/2006.2023.00065)
⚠ Возможное пересечение (держим раздельно; если видите общие данные — напишите в «Правки»): possible overlap with R2429 (ST020): Both young Australian sports bettors recruited by Qualtrics panels for Hing et al. (April 2021, N = 616; June-September 2021, NSW, N = 267): separate surveys, panel members may overlap
Расхождения в тексте: In Table A2 the PGSI categories have 30 + 49 + 36 + 103 = 218 respondents (11.2 + 18.4 + 13.5 + 38.6 = 81.7%), not the N = 267. Each percentage equals count/267. The paper does not explain the 49 respondents (18.3%) who are not in any category. Table A2 employment counts (e.g., Full time 54.7%, 55) also do not match N = 267, which suggests errors in the table. Text and table agree on the percentages for the PGSI and for sex.
Заметка ИИ: There is one sample: the baseline of an EMA study. The PGSI estimates use denominator 267 as printed. The reviewer should decide whether 218 is the right denominator.

### ST024-1 · Young adult (18-29) frequent sports/esports/DFS bettors, NSW Australia, Qualtrics panels, EMA baseline June 2021, N=267
Отчёты: R2934 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | PGSI · PGSI 0 | **below** | **30 / 267** | 11.2 | Appendix B, Table A2 | «Non-problem gambling (0) / 11.2 / 30» |
| E2 | all | PGSI · PGSI 1-2 | **L1** | **49 / 267** | 18.4 | Appendix B, Table A2 | «Low risk gambling (1–2) / 18.4 / 49» |
| E3 | all | PGSI · PGSI 3-7 | **L2** | **36 / 267** | 13.5 | Appendix B, Table A2 | «Moderate risk gambling (3–7) / 13.5 / 36» |
| E4 | all | PGSI · PGSI>=8 | **L3** | **103 / 267** | 38.6 | Appendix B, Table A2; Participants' characteristics | «the sample was skewed towards higher gambling severity: problem gambling (38.6%)» |

- E1: cumulative: no; источник порога: standard; правило: PGSI row; score 0 is below L1; у авторов: «Non-problem gambling»; главная у авторов: no; период: past 12 months; заметка: Categories sum to 218 of 267; percentages printed are of 267.
- E2: cumulative: no; источник порога: standard; правило: PGSI row; 1-2 band starts at L1; у авторов: «Low risk gambling»; главная у авторов: no; период: past 12 months; заметка: Categories sum to 218 of 267.
- E3: cumulative: no; источник порога: standard; правило: PGSI row; 3-7 band starts at L2; у авторов: «Moderate risk gambling»; главная у авторов: no; период: past 12 months; заметка: Categories sum to 218 of 267.
- E4: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ is L3; у авторов: «Problem gambling»; главная у авторов: yes; период: past 12 months; заметка: Reported as a sample characteristic, not as a prevalence aim. Categories sum to 218 of 267; if 49 are missing, 103/218 = 47.2%.

**⚠ Проверка скриптом (обратите внимание):**
- all: категории (E1+E2+E3+E4) дают 218, а n = 267

**Ключевые поля выборки:**
- **n_bettors: 267** — Appendix B, Table A2 — «Between subject measures (N = 267)»
- **sample_type: bettor_recruited** — Methods, Recruitment and survey administration — «bet on sports, esports or DFS at-least fortnightly. Qualtrics, a cloud-based software services company, recruited the respondents through several panel providers»
- **sampling: convenience** — Methods, Recruitment; Limitations — «Qualtrics ... recruited the respondents through several panel providers ... purposive sampling facilitated collecting data on a large number of betting sessions»
- **betting_period: NR** — Methods, Recruitment and survey administration — «bet on sports, esports or DFS at-least fortnightly»

**Остальные поля:**
- parent_population: NA — NA
- min_frequency: at least fortnightly (sports, esports or DFS) — Methods, Recruitment and survey administration — «bet on sports, esports or DFS at-least fortnightly»
- country: AUS — Methods, Recruitment and survey administration — «resided in New South Wales (NSW) in Australia»
- subnational: New South Wales — Methods, Recruitment and survey administration — «Respondents were aged between 18 and 29 years, resided in New South Wales (NSW) in Australia»
- data_years: 2021 — Methods, Recruitment; Appendix A, Table A1 — «The study was conducted from June to September 2021. ... 0 (Baseline) | 19th June 2021 | 29th June 2021 | 267»
- design: EMA baseline — Methods, Recruitment and survey administration — «A baseline survey (N = 267) was followed by 10 EMA surveys, each administered one week apart.»
- gambling_disclosed: NR — NA
- betting_mode: both — Participants' characteristics — «Most betting sessions were conducted using a smartphone (82.9%), 14.3% using a computer/laptop/tablet, 2.0% using a gaming console, 0.8% in a land-based venue»
- pct_online: NR — Participants' characteristics — «Most betting sessions were conducted using a smartphone (82.9%)»
- pct_inplay: NR — NA
- pct_dfs: NR — Participants' characteristics — «2,335 betting sessions: 50.9% on sports, 27.3% on esports and 21.8% on DFS»
- pct_esports: NR — Participants' characteristics — «2,335 betting sessions: 50.9% on sports, 27.3% on esports and 21.8% on DFS»
- sports_lottery: no — NA
- mixed_race: no — Methods, Recruitment — «bet on sports, esports or DFS at-least fortnightly»
- legal_status: NR — NA
- n_invited: 567 — Appendix A — «A total of 567 potential respondents were invited to the baseline survey.»
- n_responded: 267 — Appendix A — «Of the remaining 282 respondents, 15 started but did not complete the baseline survey, for a completion rate amongst eligible respondents of 94.7% (N = 267).»
- response_rate: NR — Appendix A — «it is unclear how many respondents were invited into the survey so a response rate cannot be calculated.»
- age_mean: 24.8 — Participants' characteristics — «The mean participant age was 24.8 years (Median 25, Min. 18, Max. 29).»
- age_sd: NR — NA
- age_min: 18 — Participants' characteristics — «(Median 25, Min. 18, Max. 29)»
- age_max: 29 — Participants' characteristics — «(Median 25, Min. 18, Max. 29)»
- age_group: adults — Methods, Recruitment — «Respondents were aged between 18 and 29 years»
- pct_male: 50.9 — Appendix B, Table A2 — «Male | 50.9 | 136»
- mode: online — Methods, Recruitment — «Qualtrics, a cloud-based software services company, recruited the respondents through several panel providers»
- weights: NR — NA
- instruments: PGSI (English, past 12 months); SGHS adapted (harm measure, past 7 days, not a PG instrument) — Measures — «Respondents completed the 9-item PGSI in relation to the past 12 months.»
- instrument_validated_in_language: yes — Measures — «Problem Gambling Severity Index (PGSI; Ferris & Wynne, 2001)»
- industry_funding: no — Funding sources — «Funding for this study was provided by the NSW Government's Responsible Gambling Fund, with support from the NSW Office of Responsible Gambling.»
- funding_coi: NSW Government Responsible Gambling Fund; authors declare no conflicts of interest — Funding sources; Conflicts of interest — «The authors declare no conflicts of interest in relation to this manuscript.»
- pub_status: journal — Header — «Journal of behavioral addictions; DOI: 10.1556/2006.2023.00065»
- language: English — Full text — «Situational features of smartphone betting are linked to sports betting harm: An ecological momentary assessment study»
- notes: Sample = baseline of an EMA study; 10 weekly EMA waves followed (retention 55% at wave 10) - only baseline PGSI extracted. Sample includes bettors on sports, esports or DFS (eligible if any at least fortnightly); share betting on each form not reported for persons (sessions only). Age and sex describe all 267 (all are bettors). Betting period for screening not stated; frequency questions referred to last 12 months. PGSI categories sum to 218 of 267 (81.7%); 49 unaccounted. Possible overlap with R2429 (ST020): Both young Australian sports bettors recruited by Qualtrics panels for Hing et al. (…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame = members of commercial online panels, not all young frequent bettors in NSW — Methods, Recruitment; Limitations — «The sample was not necessarily representative of young frequent sports bettors»
2. способ отбора: **no** — Non-probability online panel, purposive sampling — Limitations — «purposive sampling facilitated collecting data on a large number of betting sessions»
3. размер выборки: **no** — n = 267 < 385 — Appendix B, Table A2 — «Between subject measures (N = 267)»
4. описание выборки и условий: **yes** — Age, sex, setting (NSW panels), country and dates reported — Participants' characteristics; Table A1 — «The mean participant age was 24.8 years ... Gender was evenly split (50.9% male).»
5. охват (пропуски): **unclear** — PGSI categories sum to 218 of 267; 49 (18.4%) unaccounted, missingness not reported or explained — Appendix B, Table A2 — «Non-problem gambling (0) | 11.2 | 30 ... Low risk gambling (1–2) | 18.4 | 49 ... Moderate risk gambling (3–7) | 13.5 | 36 ... Problem gambling (8+) | 38.6 | 103»
6. валидность определения случая: **yes** — PGSI with standard 8+ threshold, original English version — Measures — «Total scores categorise respondents into non-problem (0), low risk (1–2), moderate risk (3–7) and problem gambling (8–27) groups.»
7. единое надёжное измерение: **yes** — Same online PGSI, same time frame for all; reliability reported — Measures — «Cronbach's alpha and McDonald's omega were both 0.92.»
8. статистика (числитель и знаменатель): **yes** — Counts and N given so prevalence and CI calculable, though categories do not sum to N — Appendix B, Table A2 — «Problem gambling (8+) | 38.6 | 103»
9. отклик: **no** — Online panel; response rate cannot be calculated, no non-response handling — Appendix A — «it is unclear how many respondents were invited into the survey so a response rate cannot be calculated.»

Правки:
- # Table A2 counts sum to 218; percentages published with N=267 denominator

Проверено: да

---

## ST025 · Newall 2023 · PsyArXiv

Основной отчёт R3059: [текст](../../fulltext/text/R3059.txt) · [PDF](../../fulltext/pdf/R3059.pdf) — «‘Chances are you’re about to lose’: new independent Australian safer gambling messages tested in UK and USA bettor samples» — [DOI](https://doi.org/10.31234/osf.io/ejqdf)
Расхождения в тексте: PGSI category counts add up to the analysed N: 660+490+421+294 = 1865. Percentages check out: 15.8% of 1865 is 294.7, and 35.4% of 1865 is 660.2. Table titles appear swapped: 'Table 1. Demographic characteristics' lists gambling modes, while 'Table 2. Gambling engagement' lists demographics. Sex counts add up to 1865 (1389+466+3+7). The ethnicity row 'Other 91 (1.4)' does not match 91/1865 = 4.9%. The number of US states with legal sports betting differs within the paper: 38 in the Introduction and 30 in the Discussion. Responses: 1017 + 884 = 1901; 1901 − 30 − 6 = 1865, which matches the final N.
Заметка ИИ: This is one convenience sample of Prolific online race/sports bettors from the UK and USA. PGSI prevalence is given only for the combined race-and-sports sample (mixed_race = yes). PGSI time frame and data-collection dates are not reported. The job lists the main report as a PsyArXiv preprint, but the text supplied is the published journal version.

### ST025-1 · Prolific online race/sports bettors, UK and USA, combined, n=1865
Отчёты: R3059 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | PGSI · PGSI 0 | **below** | **660 / 1865** | 35.4 | Page 4, Participants | «Within the sample, 660 participants (35.4%) were categorized as ‘non-problem gamblers’» |
| E2 | all | PGSI · PGSI 1-2 | **L1** | **490 / 1865** | 26.3 | Page 4, Participants | «490 (26.3%) as ‘low-risk gamblers’» |
| E3 | all | PGSI · PGSI 3-7 | **L2** | **421 / 1865** | 22.6 | Page 4, Participants | «421 (22.6%) as ‘moderate-risk gamblers’» |
| E4 | all | PGSI · PGSI>=8 | **L3** | **294 / 1865** | 15.8 | Page 4, Participants; Page 8, Discussion | «294 (15.8%) as ‘problem gamblers’ ... The relatively high proportion (15.8%) of participants in the highest-risk PGSI category» |

- E1: cumulative: no; источник порога: standard; правило: PGSI row; score 0 is below L1; у авторов: «non-problem gamblers»; главная у авторов: no; период: NR; заметка: Mixed race/sports bettors. Score bands not stated explicitly; the four standard categories of Ferris & Wynne 2001 are assumed.
- E2: cumulative: no; источник порога: standard; правило: PGSI row; 1-2 band starts at L1; у авторов: «low-risk gamblers»; главная у авторов: no; период: NR; заметка: Mixed race/sports bettors.
- E3: cumulative: no; источник порога: standard; правило: PGSI row; 3-7 band starts at L2; у авторов: «moderate-risk gamblers»; главная у авторов: no; период: NR; заметка: Mixed race/sports bettors.
- E4: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ is L3; у авторов: «problem gamblers»; главная у авторов: yes; период: NR; заметка: Mixed race/sports bettors. PGSI is not the study's outcome (message ratings are), but this is the prevalence figure the authors highlight.

**Ключевые поля выборки:**
- **n_bettors: 1865** — Page 4, Participants — «the final sample consisted of 1001 participants from the UK and 864 from the US (N = 1865)»
- **sample_type: bettor_recruited** — Page 3, Participants — «Participants were recruited via the online crowdsourcing platform Prolific ... had previously indicated to Prolific that they have engaged in either online race or sports betting»
- **sampling: convenience** — Page 3-4, Participants — «recruited via the online crowdsourcing platform Prolific ... We aimed to recruit 1000 participants each from both the UK and USA»
- **betting_period: NR** — Page 3, Participants — «had previously indicated to Prolific that they have engaged in either online race or sports betting»

**Остальные поля:**
- parent_population: NA — Page 3, Participants — «Participants were recruited via the online crowdsourcing platform Prolific»
- min_frequency: none — Page 3, Participants — «have engaged in either online race or sports betting»
- country: MULTI: GBR, USA — Page 3, Participants — «had previously indicated to Prolific that they have engaged in either online race or sports betting, and reside in the UK or USA were eligible»
- subnational: NA — Page 3, Participants — «reside in the UK or USA were eligible»
- data_years: NR — Page 4, Participants — «could only recruit 884 responses from eligible USA-based participants within the study timeframe»
- design: other — Page 4, Procedure — «In this within-participants online experiment, the nine messages were presented in a random order»
- gambling_disclosed: NR — Page 3, Participants — «Only Prolific users who were 18 years of age or older, had previously indicated to Prolific that they have engaged in either online race or sports betting»
- betting_mode: online only — Page 3, Participants — «have engaged in either online race or sports betting»
- pct_online: all — Page 3, Participants — «have engaged in either online race or sports betting»
- pct_inplay: NR — NA
- pct_dfs: NR — NA
- pct_esports: NR — Page 4, Table 1 — «Virtual sports betting 808 (43.3)»
- sports_lottery: no — Page 3, Participants — «have engaged in either online race or sports betting»
- mixed_race: yes — Page 4, Participants — «Overall, 80.8% of participants reported being primarily interested in sports betting, with the remainder being primarily interested in horse race betting.»
- legal_status: mixed — Page 8, Discussion (limitations) — «sports betting is legalized in the US on a state-by-state basis ... it is beyond the scope of the present study to look at whether US-based participants were e…»
- n_invited: NR — NA
- n_responded: 1901 — Page 4, Participants — «obtained 1,017 responses from UK-based participants, but could only recruit 884 responses from eligible USA-based participants»
- response_rate: NR — NA
- age_mean: 39.4 — Page 4, Table 2 — «Age: mean (SD) 39.4 (11.8)»
- age_sd: 11.8 — Page 4, Table 2 — «Age: mean (SD) 39.4 (11.8)»
- age_min: 18 — Page 3, Participants — «Only Prolific users who were 18 years of age or older»
- age_max: NR — NA
- age_group: adults — Page 3, Participants — «Only Prolific users who were 18 years of age or older»
- pct_male: 74.5 — Page 4, Table 2 — «Male 1389 (74.5) Female 466 (25)»
- mode: online — Page 4, Procedure — «In this within-participants online experiment»
- weights: no — Page 4, Participants — «Within the sample, 660 participants (35.4%) were categorized as ‘non-problem gamblers’»
- instruments: PGSI (English) — Page 4, Participants — «the Problem Gambling Severity Index (PGSI), which is a commonly-used self-report screen for disordered gambling in community samples (Ferris and Wynne 2001)»
- instrument_validated_in_language: yes — Page 4, Participants — «Problem Gambling Severity Index (PGSI) ... (Ferris and Wynne 2001). Total scores out of 27 can be produced that correspond to four clinical categories.»
- industry_funding: no — Page 9, Funding — «This research was funded internally by Central Queensland University.»
- funding_coi: Funded internally by Central Queensland University; authors declare no competing interests; authors report past funding from government gambling research bodies, GambleAware (JT PhD funding), AFSG, GREO. — Page 9, Disclosure statement; Funding — «The authors declare that they have no competing interests. ... Jamie Torrance has received; (1) PhD funding from GambleAware»
- pub_status: journal — Page 1 — «Addiction Research & Theory ... Published online: 21 Nov 2023.»
- language: English — Page 2 — «‘Chances are you’re about to lose’: new independent Australian safer gambling messages tested in UK and USA bettor samples»
- notes: Sample is online race OR sports bettors (mixed_race = yes); 80.8% primarily interested in sports betting, the rest in horse racing. PGSI is not reported separately for sports-primary bettors. UK (n=1001) and USA (n=864) were recruited with separate targets of 1000 each, but PGSI categories are reported only for the combined sample, so they are extracted as one sample. Age and sex describe the whole analysed sample (= all bettors). age_min 18 is the eligibility criterion, not an observed minimum. Gambling activity info came from Prolific prescreeners; the betting reference period is not stated…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame is Prolific users who self-reported online race/sports betting, which covers only part of UK/USA bettors. — Page 3, Participants — «Only Prolific users who ... had previously indicated to Prolific that they have engaged in either online race or sports betting»
2. способ отбора: **no** — Volunteer opt-in crowdsourcing panel, non-probability. — Page 3, Participants — «Participants were recruited via the online crowdsourcing platform Prolific and were compensated £1»
3. размер выборки: **yes** — n = 1865 bettors (>=385). — Page 4, Participants — «(N = 1865)»
4. описание выборки и условий: **unclear** — Age, sex, setting and countries reported; dates of data collection not reported. — Page 4, Table 2 — «Age: mean (SD) 39.4 (11.8) ... Male 1389 (74.5)»
5. охват (пропуски): **yes** — 36 of 1901 responses (1.9%) removed as incomplete or failing attention checks; PGSI categories cover all 1865. — Page 4, Participants — «Thirty incomplete responses were removed alongside six responses that failed attention-checks»
6. валидность определения случая: **yes** — PGSI (English original) with the standard four categories. — Page 4, Participants — «Total scores out of 27 can be produced that correspond to four clinical categories.»
7. единое надёжное измерение: **unclear** — Same online PGSI for everyone, but time frame not stated and no reliability reported. — Page 5, Procedure — «Participants then completed the PGSI.»
8. статистика (числитель и знаменатель): **yes** — Counts and denominator given (660+490+421+294=1865); CI calculable; weights not applicable. — Page 4, Participants — «660 participants (35.4%) ... 490 (26.3%) ... 421 (22.6%) ... 294 (15.8%) as ‘problem gamblers’»
9. отклик: **no** — Opt-in panel with no denominator of invited people; response rate not reported or handled. — Page 4, Participants — «obtained 1,017 responses from UK-based participants, but could only recruit 884 responses from eligible USA-based participants within the study timeframe»

Правки:
- 

Проверено: да

---

## ST026 · Rockloff 2023 · Addictive behaviors

Основной отчёт R3113: [текст](../../fulltext/text/R3113.txt) · [PDF](../../fulltext/pdf/R3113.pdf) — «Testing the effectiveness of different safer gambling messages for sports and race betting: A five-week experiment.» — [DOI](https://doi.org/10.1016/j.addbeh.2023.107893)
Расхождения в тексте: The week-5 n is reported two ways: 1,099 in 2.2 Participants and 1,116 in 4.2 Limitations. PGSI results are printed only as percentages per randomised arm (Table 2). Whole-sample counts were derived by summing rounded arm counts, and the derived categories add up exactly to 692, 691 and 691 (total 2,074). PGSI category bands and the PGSI time frame are not printed. Overall age and sex are not given. Age is a weighted mean of the arm means, and the male share is 100 minus 36.0% 'female/other'.
Заметка ИИ: This is an experiment baseline, not a prevalence study. The sample combines sports and race bettors (mixed_race = yes), and there is no estimate for sports-only bettors. PGSI percentages are descriptive (they were used for stratified randomisation), so no estimate is flagged as the authors' primary prevalence estimate.

### ST026-1 · Australian online-panel sports or race bettors (at least monthly), safer-gambling message experiment, baseline Feb 2021, n=2,074
Отчёты: R3113 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | PGSI · PGSI 0 | **below** | **370 / 2074** | 17.8 | Page 4, Table 2 | «PGSI No risk 18.5% 18.4% 16.6%» |
| E2 | all | PGSI · PGSI 1-2 | **L1** | **321 / 2074** | 15.5 | Page 4, Table 2 | «Low-risk 14.6% 15.2% 16.6%» |
| E3 | all | PGSI · PGSI 3-7 | **L2** | **463 / 2074** | 22.3 | Page 4, Table 2 | «Moderate-risk 22.7% 23.2% 21.1%» |
| E4 | all | PGSI · PGSI>=8 | **L3** | **920 / 2074** | 44.4 | Page 4, Table 2 | «Problem gambling 44.2% 43.3% 45.6%» |
| E5 | completers of all 5 waves | PGSI · PGSI>=3 | **L2** | **446 / 836** | 53.3 | Page 3, 2.2 Participants | «A total of 836 respondents provided responses for all 5 waves and of these, 446 (53.3%) reported a PGSI score in the moderate or high-risk categories (3 + )» |

- E1: cumulative: no; источник порога: standard; правило: PGSI row; score 0 = below L1; у авторов: «No risk»; главная у авторов: no; период: NR; **расчёт: 18.5% x 692 = 128.0 -> 128; 18.4% x 691 = 127.1 -> 127; 16.6% x 691 = 114.7 -> 115; 128+127+115 = 370 of 692+691+691 = 2074**; заметка: Sports or race bettors combined. Category bands not printed; standard PGSI categories assumed (No risk = 0). Authors give PGSI only descriptively per arm.
- E2: cumulative: no; источник порога: standard; правило: PGSI row; 1-2 band starts at L1; у авторов: «Low-risk»; главная у авторов: no; период: NR; **расчёт: 14.6% x 692 = 101.0 -> 101; 15.2% x 691 = 105.0 -> 105; 16.6% x 691 = 114.7 -> 115; 101+105+115 = 321**; заметка: Sports or race bettors combined.
- E3: cumulative: no; источник порога: standard; правило: PGSI row; 3-7 band starts at L2; у авторов: «Moderate-risk»; главная у авторов: no; период: NR; **расчёт: 22.7% x 692 = 157.1 -> 157; 23.2% x 691 = 160.3 -> 160; 21.1% x 691 = 145.8 -> 146; 157+160+146 = 463**; заметка: Sports or race bettors combined.
- E4: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ = L3; у авторов: «Problem gambling»; главная у авторов: no; период: NR; **расчёт: 44.2% x 692 = 305.9 -> 306; 43.3% x 691 = 299.2 -> 299; 45.6% x 691 = 315.1 -> 315; 306+299+315 = 920 (44.4%)**; заметка: Sports or race bettors combined. Derived category counts sum to 2074.
- E5: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 = L2; у авторов: «moderate or high-risk categories (3+)»; главная у авторов: no; период: NR; заметка: Subset defined by retention, not a baseline subgroup; wave of PGSI measurement not stated (presumably baseline). Not representative of baseline sample (problem gamblers more likely to drop out).

**Ключевые поля выборки:**
- **n_bettors: 2074** — Page 4, Table 2 — «Positive N = 692 Norm N = 691 Control N = 691»
- **sample_type: bettor_recruited** — Page 3, 2.2 Participants — «Participants were recruited based on having bet on sports or racing at least monthly within the last 12-months.»
- **sampling: convenience** — Page 2-3, 2.2 Participants — «Survey respondents were recruited with the assistance of Qualtrics, which aggregates online panel providers. Online panels were chosen over other methods of recruitment both for cost-efficiency»
- **betting_period: past 12 months** — Page 3, 2.2 Participants — «having bet on sports or racing at least monthly within the last 12-months»

**Остальные поля:**
- parent_population: NA — Page 2-3, 2.2 Participants — «Survey respondents were recruited with the assistance of Qualtrics, which aggregates online panel providers.»
- min_frequency: at least monthly (sports or racing) — Page 3, 2.2 Participants — «having bet on sports or racing at least monthly within the last 12-months»
- country: AUS — Page 3, 2.2 Participants — «The participants were 18 years or older, the legal age of gambling in Australia ... IPs outside Australia»
- subnational: NA — Page 3, 2.2 Participants — «IPs outside Australia, and suspicious responses»
- data_years: 2021 — Page 2, 2.1 Procedure — «The study had 5 weekly surveys, starting February 15, 2021.»
- design: experiment baseline — Page 2, 2.1 Procedure — «The surveys included a baseline survey, 3 follow-up surveys where participants viewed and commented on safer gambling messages, and a final survey»
- gambling_disclosed: NR — Page 2-3, 2.2 Participants — «Participants were recruited based on having bet on sports or racing at least monthly within the last 12-months.»
- betting_mode: NR — Page 3, 2.2 Participants — «having bet on sports or racing at least monthly within the last 12-months»
- pct_online: NR — Page 5, 3.1 — «For context, about 70% of sports betting and 67% of race betting in Australia takes place online»
- pct_inplay: NR — NR — «NR»
- pct_dfs: NR — NR — «NR»
- pct_esports: NR — Table 1 — «how much money have you bet on sports, racing, esports or novelty bets»
- sports_lottery: unclear — NR — «NR»
- mixed_race: yes — Page 3, 2.2 Participants — «Participants were recruited based on having bet on sports or racing at least monthly within the last 12-months.»
- legal_status: regulated legal market — Page 1, Introduction 1.1 — «In Australia, sports and race betting are the only high-risk products that can legally be offered online, including on smartphone apps»
- n_invited: NR — NR — «NR»
- n_responded: 2074 — Page 3, 2.2 Participants — «In total, 174 participants were removed from the study based on Week 1 responses ... A total of 2,074 participants completed the baseline survey.»
- response_rate: NR — NR — «NR»
- age_mean: 41.4 — Page 4, Table 2 — «Age M = 41.3 SD = 14.9; M = 41.4 SD = 15.0; M = 41.4 SD = 14.9»
- age_sd: NR — Page 4, Table 2 — «Age M = 41.3 SD = 14.9; M = 41.4 SD = 15.0; M = 41.4 SD = 14.9»
- age_min: 18 — Page 3, 2.2 Participants — «The participants were 18 years or older»
- age_max: NR — NR — «NR»
- age_group: adults — Page 3, 2.2 Participants — «The participants were 18 years or older, the legal age of gambling in Australia»
- pct_male: 64.0 — Page 5, 3.1 Demographic profile — «Female sport and race bettors, at 36.0% of the sample»
- mode: online — Page 2-3, 2.2 Participants — «Online panels were chosen over other methods of recruitment»
- weights: NR — NR — «NR»
- instruments: PGSI (Ferris & Wynne 2001), English — Page 3, 2.3 Assignment to conditions — «Problem Gambling Severity Index (Ferris & Wynne, 2001) score (0–2 or 3 + )»
- instrument_validated_in_language: yes — Page 3, 2.3; References — «Problem Gambling Severity Index (Ferris & Wynne, 2001)»
- industry_funding: no — Page 2, 1.1; Page 10, Funding — «Gambling Research Australia (GRA). GRA is a partnership between the Commonwealth, State and Territory Governments, independent of industry»
- funding_coi: Gambling Research Australia (government partnership, independent of industry); authors declare no competing interests — Page 10, Funding; Declaration of Competing Interest — «The authors declare that they have no known competing financial interests or personal relationships»
- pub_status: journal — Page 1 — «Addictive Behaviors 149 (2024) 107893»
- language: English — Page 1 — «Testing the effectiveness of different safer gambling messages for sports and race betting: A five-week experiment»
- notes: Sports OR race bettors combined (mixed_race=yes); no sports-only estimate. Three randomised arms (692/691/691); PGSI given only as % per arm (Table 2), whole-sample counts derived by summing arm counts. age_mean = weighted mean of arm means (41.37); arm SDs 14.9-15.0; age and sex describe whole sample. pct_male derived as 100 - 36.0% female/other. Weekly sport betting 42-44%, weekly race 51-54% by arm. Later waves: wk2 1,380, wk3 1,302, wk4 1,168, wk5 1,099 (1,116 in Limitations); 836 completed all 5 waves. Possible overlap with GRA report Rockloff et al. 2021 'Behavioural trial for consisten…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Commercial online panels aggregated by Qualtrics; frame does not cover Australian sports/race bettors. — Page 2-3, 2.2 — «Survey respondents were recruited with the assistance of Qualtrics, which aggregates online panel providers.»
2. способ отбора: **no** — Non-probability online panel recruitment. — Page 2-3, 2.2 — «Online panels were chosen over other methods of recruitment both for cost-efficiency and ease in re-contacting participants»
3. размер выборки: **yes** — n = 2,074 bettors at baseline (>=385). — Page 3, 2.2 — «A total of 2,074 participants completed the baseline survey.»
4. описание выборки и условий: **yes** — Age, sex, country, online panel setting and start date reported. — Page 2, 2.1; Page 4, Table 2 — «The study had 5 weekly surveys, starting February 15, 2021.»
5. охват (пропуски): **unclear** — Missing PGSI data at baseline not reported; Table 2 percentages sum to 100% per arm. — Page 4, Table 2 — «PGSI No risk 18.5% Low-risk 14.6% Moderate-risk 22.7% Problem gambling 44.2%»
6. валидность определения случая: **yes** — PGSI with standard categories, English original version. — Page 3, 2.3; Table 2 — «Problem Gambling Severity Index (Ferris & Wynne, 2001)»
7. единое надёжное измерение: **unclear** — Same online PGSI for all, but time frame and reliability not reported. — Page 3, 2.3 — «The analyses that follow used raw PGSI scores instead, albeit transformed (i.e., log (pgsi + 1)).»
8. статистика (числитель и знаменатель): **yes** — Percentages per arm with arm n allow numerators and CIs to be derived; denominator is sports or race bettors. — Page 4, Table 2 — «Positive N = 692 Norm N = 691 Control N = 691»
9. отклик: **no** — Online panel with no denominator of invited people; response rate not reported. — Page 3, 2.2 — «A total of 2,074 participants completed the baseline survey.»

Правки:
- 

Проверено: да

---

## ST027 · Abu 2022 · Research Square

Основной отчёт R3255: [текст](../../fulltext/text/R3255.txt) · [PDF](../../fulltext/pdf/R3255.pdf) — «Problematic Gambling and Associated Factors Among Sports Bettors in Jimma Town Betting Centers, South West Ethiopia» — [DOI](https://doi.org/10.21203/rs.3.rs-1960760/v1)
Расхождения в тексте: Sex: the text says males were 97.1% (n=402), but Table 1 gives 401 males (96.9%) and 13 females. The Table 1 value was used. Dates: the text gives data collection as August-September 2021, but Table 1 says November 2021 and Table 3 says October 2021. SOGS cut-off: '5 or more' on page 6 (operational definition) but 'greater than 5' in the tool description. Age band: '39-45' in Table 1 vs '38-45' in Table 3. Table 3 age-band cases add up to 223, matching the overall prevalence (223/414 = 53.9%). Other inconsistencies: Table 2 has peer influence Yes 130 vs 284 in the text, and substance use 49% vs 96% in the text. The Statistical Analysis section mentions 'prevalence of ADHD', which looks like a copy-paste error.
Заметка ИИ: One sample was extracted: consecutive sports bettors at all 11 betting centres in Jimma town. The single SOGS 5+ estimate (223/414) is the primary estimate. Age-band subgroups were taken from Table 3. No estimates by sex or betting mode are reported.

### ST027-1 · Sports bettors at all 11 betting centres, Jimma town, Ethiopia, 2021 (n=414)
Отчёты: R3255 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | SOGS · SOGS>=5 (range 0-20) | **L3** | **223 / 414** | 53.9 | Page 10, Prevalence of Problematic Gambling; Abstract | «The overall prevalence of Problematic gambling in this study was (53.9%, n=223) with 95% CI:(0.49-0.59).» |
| E2 | 18-24 | SOGS · SOGS>=5 (range 0-20) | **L3** | **24 / 62** | 38.7 | Table 3 | «18-24 38(61.3) 24 (38.7)» |
| E3 | 25-31 | SOGS · SOGS>=5 (range 0-20) | **L3** | **158 / 226** | 69.9 | Table 3 | «25-31 68(30.1) 158(69.9)» |
| E4 | 32-38 | SOGS · SOGS>=5 (range 0-20) | **L3** | **25 / 74** | 33.8 | Table 3 | «32-38 49(66.2) 25(33.8)» |
| E5 | 39-45 | SOGS · SOGS>=5 (range 0-20) | **L3** | **11 / 33** | 33.3 | Table 3 | «38-45 22(66.7) 11(33.3)» |
| E6 | >46 | SOGS · SOGS>=5 (range 0-20) | **L3** | **5 / 19** | 26.3 | Table 3 | «>46 14(73.7) 5(26.3)» |

- E1: cumulative: yes; источник порога: standard; правило: SOGS row; 5+ is L3; у авторов: «problematic gambling»; главная у авторов: yes; период: NR; заметка: The cut-off is also described as 'greater than 5' on page 6.
- E2: cumulative: yes; источник порога: standard; правило: SOGS row; 5+ is L3; у авторов: «problematic gambling»; главная у авторов: no; период: NR; **расчёт: n = 38 No + 24 Yes = 62 (matches Table 1)**
- E3: cumulative: yes; источник порога: standard; правило: SOGS row; 5+ is L3; у авторов: «problematic gambling»; главная у авторов: no; период: NR; **расчёт: n = 68 + 158 = 226**
- E4: cumulative: yes; источник порога: standard; правило: SOGS row; 5+ is L3; у авторов: «problematic gambling»; главная у авторов: no; период: NR; **расчёт: n = 49 + 25 = 74**
- E5: cumulative: yes; источник порога: standard; правило: SOGS row; 5+ is L3; у авторов: «problematic gambling»; главная у авторов: no; период: NR; **расчёт: n = 22 + 11 = 33**; заметка: Table 3 labels this band '38-45'; Table 1 labels it '39-45' (n=33).
- E6: cumulative: yes; источник порога: standard; правило: SOGS row; 5+ is L3; у авторов: «problematic gambling»; главная у авторов: no; период: NR; **расчёт: n = 14 + 5 = 19**; заметка: The band is labelled '>46' as printed.

**Ключевые поля выборки:**
- **n_bettors: 414** — Page 7, Result; Table 3 — «A total of 414 agreed to be enrolled in the study and completed the interview»
- **sample_type: bettor_recruited** — Page 5, Sampling technique and procedure — «422/11=38 from each site to addressed 38 individuals or participants who come to take a ticket or for payment from a sports betting center.»
- **sampling: venue_intercept** — Page 5, Sampling technique and procedure — «The consecutive sampling technique was used because there is no information (number and list) on the number of sports betting gamblers in the town.»
- **betting_period: current** — Page 4, Eligibility criteria — «All individuals visited the sports betting center at Jimma town, during the study period.»

**Остальные поля:**
- parent_population: NA — NA — «NA»
- min_frequency: none (but excluded those who had been betting for less than 12 months) — Page 4, Exclusion criteria — «Those who never fulfill 12 months after started betting»
- country: ETH — Page 4, Setting — «The study was conducted in Jimma town from located in Western Oromia regional state, Southwest Ethiopia.»
- subnational: Jimma town — Page 4, Setting — «The town has 11 betting centers and the study was conducted at all.»
- data_years: 2021 — Page 4, Study design — «A cross-sectional study design was conducted from one August 2021 to one September 2021»
- design: cross-sectional — Page 2, Abstract Methods — «A quantitative cross-sectional survey was conducted among 422 sports bettors.»
- gambling_disclosed: NR — Page 15, Ethical Approval — «Respondents were informed about the purpose, procedure, risks, and benefits of the study»
- betting_mode: NR — Page 5, Sampling technique and procedure — «participants who come to take a ticket or for payment from a sports betting center»
- pct_online: NR — NR — «NR»
- pct_inplay: NR — NR — «NR»
- pct_dfs: NR — NR — «NR»
- pct_esports: NR — NR — «NR»
- sports_lottery: no — Page 6, Operational definition — «Sports betting: - a popular form of gambling where people made predictions about sporting results and place a bet (wager) on its outcome»
- mixed_race: no — Page 6, Operational definition — «Sports bettors: - A person who bets or makes a wager, as on the outcome of a game.»
- legal_status: regulated legal market — Page 14, Discussion — «Moreover, licensed betting companies operating and betting outlets spread across our country.»
- n_invited: 422 — Page 5, Sample size — «n=422»
- n_responded: 414 — Page 7, Result — «A total of 414 agreed to be enrolled in the study and completed the interview giving a response rate of 98.1%.»
- response_rate: 98.1 — Page 7, Result — «giving a response rate of 98.1%»
- age_mean: NR — NR — «NR»
- age_sd: NR — NR — «NR»
- age_min: NR — Table 1 — «Age 18-24 62 15»
- age_max: NR — Table 1 — «>46 19 4.6»
- age_group: adults — Table 1 — «Age 18-24 62 15 25-31 226 54.6 32-38 74 17.9 39-45 33 8 >46 19 4.6»
- pct_male: 96.9 — Table 1 — «Sex Female 13 3.1 Male 401 96.9»
- mode: face-to-face — Page 7, Data collection procedure — «Face-face interviewer-administered questionnaires were used to collect data»
- weights: no — Page 7, Statistical Analysis — «Descriptive statistics were used to describe the sample characteristics»
- instruments: SOGS (20 items; language version not reported) — Page 6, Data collection tool — «South Oaks Gambling Screen (SOGS) is a self-report questionnaire consists of 20 items to identify problematic and non-problematic gambling.»
- instrument_validated_in_language: NR — Page 6, Data collection tool — «There are validations of this questionnaire that showed good psychometric properties (Cronbach's α = .97, test-retest reliability 0.98»
- industry_funding: no — Page 16, Funding — «This research work was funded by Jimma University.»
- funding_coi: Funded by Jimma University; authors declare no competing interests — Page 16, Funding; Competing interests — «This research work was funded by Jimma University. ... The authors declare that they have no competing interests.»
- pub_status: preprint — Page 1 — «Research Article ... Posted Date: August 29th, 2022 DOI: https://doi.org/10.21203/rs.3.rs-1960760/v1»
- language: English — Full text — «Problematic Gambling and Associated Factors Among Sports Bettors in Jimma Town Betting Centers, South West Ethiopia»
- notes: Age and sex fields describe the whole sample, which is all sports bettors. The lowest age band is 18-24, so the sample is coded adults, but no minimum age is stated. Participants were recruited at land-based betting centres; whether they also bet online is not reported (91% said they had accessible internet for sports betting). The interview language and the SOGS language version are not reported. Table dates (November/October 2021) conflict with the stated data collection period (Aug-Sep 2021). The SOGS cut-off is stated as '5 or more' in one place and 'greater than 5' in another. The SOGS t…

**Риск смещения (JBI):**
1. рамка выборки: **yes** — The target is sports bettors at Jimma town betting centres, and the frame covered all 11 centres in the town. — Page 4, Setting — «The town has 11 betting centers and the study was conducted at all.»
2. способ отбора: **no** — Consecutive (non-probability) sampling with an equal quota of 38 per centre. — Page 5 — «The consecutive sampling technique was used ... 422/11=38 from each site»
3. размер выборки: **yes** — 414 sports bettors, which is at least 385. — Page 7, Result — «A total of 414 agreed to be enrolled in the study and completed the interview»
4. описание выборки и условий: **yes** — Age, sex, setting, country and dates are reported (the dates are given inconsistently). — Pages 4, 7-8 — «conducted from one August 2021 to one September 2021»
5. охват (пропуски): **yes** — All 414 respondents are classified in the SOGS outcome (223 + 191 = 414). — Table 3 — «18-24 38(61.3) 24 (38.7) ... >46 14(73.7) 5(26.3)»
6. валидность определения случая: **unclear** — SOGS with the standard 5+ cut-off, but the language version and its validation are not reported, and the threshold is stated inconsistently ('5 or more' vs 'greater than 5'). — Page 6 — «for those scoring 5 or more from counted questionaries was problematic gambling ... the score greater than 5 considers problematic gambling»
7. единое надёжное измерение: **yes** — The same SOGS was given by trained interviewers face to face to everyone; reliability is cited from validation studies. — Pages 6-7 — «training was given to data collectors and supervisors ... Face-face interviewer-administered questionnaires were used»
8. статистика (числитель и знаменатель): **yes** — The numerator (223) and denominator (414) are clear and a 95% CI is given; the design needs no weights. — Page 10 — «The overall prevalence of Problematic gambling in this study was (53.9%, n=223) with 95% CI:(0.49-0.59).»
9. отклик: **yes** — Response rate of 98.1%. — Page 7 — «giving a response rate of 98.1%»

Правки:
- 

Проверено: да

---

## ST028 · Afe 2022 · Indian journal of psychological medicine

Основной отчёт R3259: [текст](../../fulltext/text/R3259.txt) — «Prevalence of and Factors Associated with Disordered Gambling Disorder, and Use of DSM-5 Based Sports Betting Questionnaire, in a Southwest Nigerian Community.» — [DOI](https://doi.org/10.1177/02537176211023809)
Расхождения в тексте: 1) The abstract's prevalence (30.5%) matches no figure in the results. The results and discussion give 34.5% (138/400, DSM-5) for the community, and Table 2 gives 122/249 (48.9%) among community players. 2) The community denominator is inconsistent. The inclusion criterion requires having played sports bets, but only 249 of 400 are players in Table 2, and the text prevalences (138/400, 152/400) use 400. 3) The DSM-5 severity percentages (9.8%, 11.18%, 12.3%) match neither 400 nor 249 as denominator. 4) Male share: Table 1 gives 323/400 (81%), while the text says 'Males constituted the majority (212, 85.1%) of the community sample'. 212 is the male bettor count in Table 2. 5) The discussion gives clinical prevalence as 4.5%, against 22/53 = 41.5% in the results. 6) In Table 2 the percentages in some cells are column shares of cases, not prevalences (e.g., 29-39: 21/33 printed as 17.2%). …
Заметка ИИ: Two samples: (1) community house-to-house sample, 249 lifetime sports bettors among 400 residents; (2) clinical outpatient sample of 53 regular bettors. For the community sample, the authors' headline (138/400) is marked primary, and the Table 2 estimate among bettors (122/249) is also given. The reviewer should decide which denominator to use. The DSM-5 questionnaire was developed by the authors and validated only in this study.

### ST028-1 · Sagamu community house-to-house survey, Nigeria, 2019-2020 (lifetime sports bettors n=249 of 400)
Отчёты: R3259 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | DSM-5-screen · DSM-5 criteria>=4 (0-9) | **L3** | **122 / 249** | 49.0 | Table 2 | «N / 249/122 (48.9%)» |
| E2 | all | DSM-5-screen · DSM-5 criteria>=4 (0-9) | **L3** | **138 / 400** | 34.5 | Results, Demographics; Discussion | «individuals with gambling disorder made up 138, 34.5% (n = 138) using DSM-5 cutoff criteria» |
| E3 | all | DSM-5-screen · DSM-5 criteria 4-5 (mild) | **L3** | **40 / 400** | 10.0 | Results, Demographics | «the severity was mild in 40, 9.8% (n = 40), moderate in 48, 11.18% (n = 48), and severe in 50, 12.3% (n = 50).» |
| E4 | all | DSM-5-screen · DSM-5 criteria 6-7 (moderate) | **L3** | **48 / 400** | 12.0 | Results, Demographics | «moderate in 48, 11.18% (n = 48)» |
| E5 | all | DSM-5-screen · DSM-5 criteria 8-9 (severe) | **L3** | **50 / 400** | 12.5 | Results, Demographics | «severe in 50, 12.3% (n = 50)» |
| E6 | all | SOGS · SOGS>=5 (0-20) | **L3** | **152 / 400** | 38.0 | Results, Demographics | «The prevalence of individuals with probable pathological gambling disorder in the community was 152, 38% (n = 152) using the SOGS criteria» |
| E7 | male | DSM-5-screen · DSM-5 criteria>=4 (0-9) | **L3** | **112 / 212** | 52.8 | Table 2 | «Male / 212 (85.1%)/112(91.8%)» |
| E8 | female | DSM-5-screen · DSM-5 criteria>=4 (0-9) | **L3** | **10 / 37** | 27.0 | Table 2 | «Female / 37 (14.9)/10(8.2%)» |
| E9 | 18-28 | DSM-5-screen · DSM-5 criteria>=4 (0-9) | **L3** | **94 / 204** | 46.1 | Table 2 | «18–28 / 204/94 (46.1%)» |
| E10 | 29-39 | DSM-5-screen · DSM-5 criteria>=4 (0-9) | **L3** | **21 / 33** | 63.6 | Table 2 | «29–39 / 33/21 (17.2%)» |
| E11 | 40-50 | DSM-5-screen · DSM-5 criteria>=4 (0-9) | **L3** | **7 / 12** | 58.3 | Table 2 | «40–50 / 12/7 (58.3%)» |

- E1: cumulative: yes; источник порога: standard; правило: DSM-5-screen row; >=4 is L3; у авторов: «Disordered Gambling Disorder»; главная у авторов: no; период: NR; заметка: Sports bettors ('players') in the community sample. Instrument assumed to be the DSM-5 questionnaire (the table does not name it). The authors' text headline is 138/400 = 34.5%.
- E2: cumulative: yes; источник порога: standard; правило: DSM-5-screen row; >=4 is L3; у авторов: «gambling disorder»; главная у авторов: yes; период: NR; заметка: Denominator unclear: 400 is the whole community sample, which per Table 2 includes 151 non-players. The abstract reports 30.5%.
- E3: cumulative: no; источник порога: standard; правило: DSM-5-screen row; band starts at 4 = L3; у авторов: «mild»; главная у авторов: no; период: NR; заметка: Denominator unclear: 40+48+50=138 (the 400-denominator estimate), but the printed percentages match neither 400 nor 249. Bands assumed to be the standard DSM-5 severity bands.
- E4: cumulative: no; источник порога: standard; правило: DSM-5-screen row; band within >=4 = L3; у авторов: «moderate»; главная у авторов: no; период: NR; заметка: Denominator unclear (see the mild band).
- E5: cumulative: yes; источник порога: standard; правило: DSM-5-screen row; band within >=4 = L3; у авторов: «severe»; главная у авторов: no; период: NR; заметка: Denominator unclear (see the mild band).
- E6: cumulative: yes; источник порога: standard; правило: SOGS row; >=5 is L3; у авторов: «probable pathological gambling disorder»; главная у авторов: no; период: NR; заметка: Denominator is the whole community sample (400), not the 249 bettors. The SOGS 1-4 band ('problem gambling') was used, but no counts are reported.
- E7: cumulative: yes; источник порога: standard; правило: DSM-5-screen row; >=4 is L3; у авторов: «Disordered Gambling Disorder»; главная у авторов: no; период: NR; заметка: 91.8% is the share of the 122 cases, not a prevalence.
- E8: cumulative: yes; источник порога: standard; правило: DSM-5-screen row; >=4 is L3; у авторов: «Disordered Gambling Disorder»; главная у авторов: no; период: NR; заметка: 8.2% is the share of the 122 cases.
- E9: cumulative: yes; источник порога: standard; правило: DSM-5-screen row; >=4 is L3; у авторов: «Disordered Gambling Disorder»; главная у авторов: no; период: NR
- E10: cumulative: yes; источник порога: standard; правило: DSM-5-screen row; >=4 is L3; у авторов: «Disordered Gambling Disorder»; главная у авторов: no; период: NR; заметка: Printed 17.2% doesn't match 21/33 (63.6%). It seems to be the share of the 122 cases.
- E11: cumulative: yes; источник порога: standard; правило: DSM-5-screen row; >=4 is L3; у авторов: «Disordered Gambling Disorder»; главная у авторов: no; период: NR

**⚠ Проверка скриптом (обратите внимание):**
- E2, E3, E4, E5, E6: n оценки не равно n_bettors выборки (249): проверьте знаменатель
- E2, E3, E5, E6: ни случаев, ни n нет в вашей строке «Где цифры» (этап полных текстов) — сверьте

**Ключевые поля выборки:**
- **n_bettors: 249** — Table 2 — «N | 249/122 (48.9%)»
- **sample_type: rep_survey_subsample** — Procedure; Results, Demographics — «Multistage random sampling method was adopted... House to house visits were done in streets that were randomly selected, to recruit residents within each ward.»
- **sampling: probability** — Procedure — «Multistage random sampling method was adopted. The more populated wards were ranked in terms of population size in descending order. A greater number of participants were recruited from the heavily populated wards.»
- **betting_period: lifetime** — Results, Demographics; Design — «More than half of the participants within the community had either played sports bets in the past or are currently active players of sports bets.»

**Остальные поля:**
- parent_population: adult (18+) residents of Sagamu community, Nigeria (400 recruited house to house) — Procedure — «House to house visits were done in streets that were randomly selected, to recruit residents within each ward.»
- min_frequency: none — Design and Participants Recruitment — «Inclusion criteria included participants who gave informed consent (verbal and written) and played or ever played sports bet.»
- country: NGA — Title — «in a Southwest Nigerian Community»
- subnational: Sagamu — Setting — «Sagamu is a major commercial center and transportation hub in Nigeria. It consists of 15 wards.»
- data_years: 2019-2020 — Design and Participants Recruitment — «The cross-sectional surveys were conducted between March 2019 and February 2020.»
- design: validation study — Abstract — «Our study aimed to evaluate psychometric properties of the Diagnostic and Statistical Manual (DSM)-5 for use as a self-report screening instrument for large-sc…»
- gambling_disclosed: NR — NA
- betting_mode: NR — NA
- pct_online: NR — NA
- pct_inplay: NR — NA
- pct_dfs: NR — NA
- pct_esports: NR — NA
- sports_lottery: no — Introduction — «The most common form of gambling among young adults in Nigeria is sports (soccer) bets.»
- mixed_race: no — Limitation — «Our study focused on sports betting as typical of gambling behavior»
- legal_status: NR — Setting — «sports-betting shops and stalls can be found on almost every street in Sagamu.»
- n_invited: 507 — Results, Demographics — «400 participants were recruited from Sagamu community (see Table 1), out of the 507 persons approached (79.0% response rate).»
- n_responded: 400 — Results, Demographics — «400 participants were recruited from Sagamu community (see Table 1), out of the 507 persons approached (79.0% response rate).»
- response_rate: 79.0 — Results, Demographics — «out of the 507 persons approached (79.0% response rate)»
- age_mean: 25.09 — Results, Demographics — «Mean ± SD ages in years were 26.05 ± 6.89 (clinical sample) and 25.09 ± 5.09, (community sample).»
- age_sd: 5.09 — Results, Demographics — «25.09 ± 5.09, (community sample)»
- age_min: 18 — Table 1; Design — «those below 18 years of age»
- age_max: 50 — Table 1 — «40–50 | 16/4.0»
- age_group: adults — Design and Participants Recruitment — «We excluded respondents with a history of mental illness or cognitive disorders and those below 18 years of age.»
- pct_male: 85.1 — Table 2; Results text — «Male | 212 (85.1%)/112(91.8%)»
- mode: face-to-face — Procedure; Instruments — «House to house visits were done... Research assistants were taught how to use the various instruments and to communicate effectively in the local language if t…»
- weights: no — Statistical Analyses — «Missing data were handled using list-wise deletion.»
- instruments: DSM-5 Betting Questionnaire (author-developed 9-item self-report, English); SOGS (English) — Instruments — «The questionnaire was developed by the authors. The questionnaire items are based on the 9-items in the DSM-5 criteria... We trained the research assistants to…»
- instrument_validated_in_language: no — Instruments — «The questionnaire was developed by the authors... We simplified the wordings in keeping with the local setting»
- industry_funding: no — Footnotes — «Funding: The authors received no financial support for the research, authorship, and/or publication of this article.»
- funding_coi: No funding; no conflicts declared — Footnotes — «The authors declared no potential conflicts of interest»
- pub_status: journal — Header — «Indian journal of psychological medicine»
- language: English — Full text — «The instruments were used in the English language.»
- notes: Age mean/SD are for the whole community sample (n=400); pct_male is of the 249 sports bettors (Table 2). Table 1 gives 323/400 (81%) male for the whole sample. The DSM-5 questionnaire is validated in this same study only; no earlier published validation. The inclusion criterion says participants had to have played sports bets, yet only 249 of 400 are 'players' in Table 2. The headline prevalences (DSM-5 138/400 = 34.5%; SOGS 152/400 = 38%) use 400 as denominator, while Table 2 gives 122/249. The clinical sample is a separate sample (extracted separately).

**Риск смещения (JBI):**
1. рамка выборки: **yes** — Frame was residents of all wards of the Sagamu community, reached through randomly selected streets — Procedure — «House to house visits were done in streets that were randomly selected, to recruit residents within each ward.»
2. способ отбора: **unclear** — Described as multistage random sampling, but allocation across wards was non-proportional and authors admit skewed sampling (heavy male over-representation) — Procedure; Limitation — «A major limitation of our study is the small sample size, especially in phase 1 clinical recruitment, and the skewed sampling.»
3. размер выборки: **no** — 249 sports bettors, below 385 — Table 2 — «N | 249/122 (48.9%)»
4. описание выборки и условий: **yes** — Age, sex, setting, country and dates reported — Results; Table 1; Design — «conducted between March 2019 and February 2020»
5. охват (пропуски): **unclear** — Listwise deletion used but amount of missing data not reported — Statistical Analyses — «Missing data were handled using list-wise deletion.»
6. валидность определения случая: **unclear** — Author-developed DSM-5 questionnaire with standard >=4 cut-off; validated only within this same study, no prior published validation — Instruments — «The questionnaire was developed by the authors... A cutoff score of ≥4 was decided.»
7. единое надёжное измерение: **unclear** — Same instrument and cut-off, alpha 0.92 reported, but research assistants interpreted items into the local language ad hoc for some participants — Procedure; Reliability — «Research assistants were taught... to communicate effectively in the local language if the wordings were not well understood.»
8. статистика (числитель и знаменатель): **no** — Denominators inconsistent: the main estimate 138/400 includes non-bettors, Table 2 gives 122/249, the abstract says 30.5%, and severity percentages do not match — Abstract; Results; Table 2 — «The prevalence rate for gambling disorder was 30.5%.»
9. отклик: **yes** — Response 79.0% — Results, Demographics — «out of the 507 persons approached (79.0% response rate)»

Правки:
- E2 удалить # whole community sample n=400, not sports bettors
- E3 удалить # whole community sample n=400, not sports bettors
- E4 удалить # whole community sample n=400, not sports bettors
- E5 удалить # whole community sample n=400, not sports bettors
- E6 удалить # whole community sample n=400, not sports bettors
- E1.primary_for_authors = yes

Проверено: да

### ST028-2 · Sagamu teaching hospital general outpatient attendees who bet on sports, Nigeria, 2019 (n=53)
Отчёты: R3259 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | interview · interview: ICD-11 gambling disorder criteria (consultant psychiatrist) | **L4** | **22 / 53** | 41.5 | Results, Demographics | «In the clinical study, those who met the ICD-11 criteria and DSM-5 criteria were the same percentage, 22, 41.5% (n = 22)» |
| E2 | all | DSM-5-screen · DSM-5 criteria>=4 (0-9) | **L3** | **22 / 53** | 41.5 | Results, Demographics; Table 2 | «53/22 (41.5%)» |
| E3 | all | SOGS · SOGS>=5 (0-20) | **L3** | **27 / 53** | 50.9 | Results, Demographics | «while for SOGS was higher, 27, 50.9% (n = 27)» |
| E4 | 18-28 | DSM-5-screen · DSM-5 criteria>=4 (0-9) | **L3** | **18 / 45** | 40.0 | Table 2 | «18–28 / 204/94 (46.1%) / 45/18 (40%)» |
| E5 | 29-39 | DSM-5-screen · DSM-5 criteria>=4 (0-9) | **L3** | **3 / 4** | 75.0 | Table 2 | «29–39 / 33/21 (17.2%) / 4/3 (75%)» |
| E6 | 40-50 | DSM-5-screen · DSM-5 criteria>=4 (0-9) | **L3** | **1 / 4** | 25.0 | Table 2 | «40–50 / 12/7 (58.3%) / 4/1 (25%)» |

- E1: cumulative: yes; источник порога: standard; правило: interview row; clinician diagnosis = L4; у авторов: «met ICD-11 criteria»; главная у авторов: yes; период: past 12 months; заметка: ICD-11 criteria based on a one-year pattern.
- E2: cumulative: yes; источник порога: standard; правило: DSM-5-screen row; >=4 is L3; у авторов: «gambling disorder»; главная у авторов: no; период: NR; заметка: The discussion says 4.5% for the clinical sample, which looks like a typo.
- E3: cumulative: yes; источник порога: standard; правило: SOGS row; >=5 is L3; у авторов: «probable pathological gambling»; главная у авторов: no; период: NR
- E4: cumulative: yes; источник порога: standard; правило: DSM-5-screen row; >=4 is L3; у авторов: «Disordered Gambling Disorder»; главная у авторов: no; период: NR; заметка: Table 2 does not name its instrument. The DSM-5 questionnaire is assumed; ICD-11 gives the same total (22).
- E5: cumulative: yes; источник порога: standard; правило: DSM-5-screen row; >=4 is L3; у авторов: «Disordered Gambling Disorder»; главная у авторов: no; период: NR
- E6: cumulative: yes; источник порога: standard; правило: DSM-5-screen row; >=4 is L3; у авторов: «Disordered Gambling Disorder»; главная у авторов: no; период: NR

**⚠ Проверка скриптом (обратите внимание):**
- E1, E2, E3: ни случаев, ни n нет в вашей строке «Где цифры» (этап полных текстов) — сверьте

**Ключевые поля выборки:**
- **n_bettors: 53** — Table 2 — «N | 249/122 (48.9%) | 53/22 (41.5%)»
- **sample_type: other** — Procedure — «A survey form was used to recruit participants who play sports bet, from clinic attendees from all clinic days and units»
- **sampling: convenience** — Procedure — «A survey form was used to recruit participants who play sports bet, from clinic attendees from all clinic days and units, for further interviews with the investigators.»
- **betting_period: current** — Procedure — «Fifty-three persons who play sports betting regularly were recruited for the clinical survey.»

**Остальные поля:**
- parent_population: general outpatient attendees of the Teaching Hospital, Sagamu — Procedure — «The first sampled population was recruited from patients presenting at the General Outpatient Unit.»
- min_frequency: regularly (not defined) — Procedure — «Fifty-three persons who play sports betting regularly»
- country: NGA — Title — «in a Southwest Nigerian Community»
- subnational: Sagamu — Procedure — «recruitment of clinic attendees from the General Outpatient Unit of the Teaching Hospital in Sagamu»
- data_years: 2019-2020 — Design and Participants Recruitment — «The cross-sectional surveys were conducted between March 2019 and February 2020.»
- design: validation study — Instruments — «The clinical sample was used to determine classification accuracy, sensitivity, specificity, hit rate, precision rate, receiver operating curve (ROC), and area…»
- gambling_disclosed: NR — NA
- betting_mode: NR — NA
- pct_online: NR — NA
- pct_inplay: NR — NA
- pct_dfs: NR — NA
- pct_esports: NR — NA
- sports_lottery: no — Introduction — «The most common form of gambling among young adults in Nigeria is sports (soccer) bets.»
- mixed_race: no — Limitation — «Our study focused on sports betting as typical of gambling behavior»
- legal_status: NR — NA
- n_invited: NR — NA
- n_responded: 53 — Results, Demographics — «Fifty-three participants were recruited for the clinical study»
- response_rate: NR — NA
- age_mean: 26.05 — Results, Demographics — «Mean ± SD ages in years were 26.05 ± 6.89 (clinical sample)»
- age_sd: 6.89 — Results, Demographics — «26.05 ± 6.89 (clinical sample)»
- age_min: 18 — Table 1 — «18–28 | 340/85.0 | 45/84.0»
- age_max: 50 — Table 1 — «40–50 | 16/4.0 | 4/7.5»
- age_group: adults — Design — «those below 18 years of age»
- pct_male: 100 — Results, Demographics — «Participants in the clinical sample were all males.»
- mode: face-to-face — Procedure — «for further interviews with the investigators. The diagnosis was made based on the ICD version 11 criteria»
- weights: no — Statistical Analyses — «Missing data were handled using list-wise deletion.»
- instruments: ICD-11 clinical diagnosis by consultant psychiatrists; DSM-5 Betting Questionnaire (author-developed, English); SOGS (English) — Procedure; Instruments — «Sensitivity and specificity were examined by comparing the diagnostic correlation with the ICD-11 diagnosis by Consultant Psychiatrists.»
- instrument_validated_in_language: NR — NA
- industry_funding: no — Footnotes — «Funding: The authors received no financial support for the research, authorship, and/or publication of this article.»
- funding_coi: No funding; no conflicts declared — Footnotes — «The authors declared no potential conflicts of interest»
- pub_status: journal — Header — «Indian journal of psychological medicine»
- language: English — Procedure — «The instruments were used in the English language.»
- notes: General outpatients recruited because they bet on sports, not because of gambling problems, so the sample is eligible. Used as the validation (criterion) sample. The discussion gives the clinical prevalence as '4.5%', which conflicts with the 41.5% (22/53) in the results and Table 2. Age and sex fields describe the 53 bettors (the whole clinical sample). instrument_validated_in_language is NR because the main estimate is a clinician ICD-11 diagnosis.

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame is attendees of one hospital outpatient unit, only part of the area's sports bettors — Procedure — «The first sampled population was recruited from patients presenting at the General Outpatient Unit.»
2. способ отбора: **unclear** — Recruitment from clinic days via a survey form; selection method not described as random or consecutive — Procedure — «A survey form was used to recruit participants who play sports bet, from clinic attendees from all clinic days and units»
3. размер выборки: **no** — n=53, below 385 — Results — «Fifty-three participants were recruited for the clinical study»
4. описание выборки и условий: **yes** — Age, sex, setting, country and dates reported — Results; Table 1 — «Participants in the clinical sample were all males.»
5. охват (пропуски): **unclear** — Missing data not reported — Statistical Analyses — «Missing data were handled using list-wise deletion.»
6. валидность определения случая: **yes** — Primary estimate is the ICD-11 diagnosis by consultant psychiatrists (L4) — Procedure — «The diagnosis was made based on the ICD version 11 criteria for pathological gambling.»
7. единое надёжное измерение: **unclear** — Same ICD-11 procedure for all, but no inter-rater reliability reported for the diagnoses — Procedure — «ICD-11 diagnosis by Consultant Psychiatrists»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator clear (22/53); CI calculable — Results — «those who met the ICD-11 criteria and DSM-5 criteria were the same percentage, 22, 41.5% (n = 22)»
9. отклик: **unclear** — Response rate for clinical sample not reported — Results — «Fifty-three participants were recruited for the clinical study»

Правки:
- # clinical sample n=53 regular sports bettors from Table 2

Проверено: да

---

## ST029 · Balem 2022 · Addiction (Abingdon, England)

Основной отчёт R3283: [текст](../../fulltext/text/R3283.txt) — «Impact of wagering inducements on the gambling behaviors of on-line gamblers: A longitudinal study based on gambling tracking data.» — [DOI](https://doi.org/10.1111/add.15665)
Не выписано ИИ: Excluded: gamblers engaged in horse race betting (n=3524) and poker players (n=4858) from the ARJEL dataset, because these are not sports-bettor samples and they overlap with the sports bettors. Also excluded: the FDJ online lottery/scratch-game sample (2019, n=5682), which contains no sports bettors.
Расхождения в тексте: The Table 1 PGSI categories for sports bettors add up to n: 1379+2581+579+624=5163. At-risk 1203 = 579+624, and 1203/5163 = 23.3%. Sex: 4795+320+48 = 5163. The text says the PGSI was scored using the original categories but then applies the revised Currie categories (1-4, 5-7, 8+). The table shows only the revised bands. The abstract's sex range (87.1-92.9% male) matches Table 1.
Заметка ИИ: There is one eligible sample: ARJEL online gamblers engaged in sports betting. The paper does not say whether 'engaged in sports betting' comes from tracking data or self-report, so betting_period is coded NR. No PGSI estimates by subgroup (sex, age) are reported.

### ST029-1 · France, ARJEL online gamblers engaged in sports betting, 2015-2016, n=5163
Отчёты: R3283 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | PGSI · PGSI 0 (range 0-27) | **below** | **1379 / 5163** | 26.7 | Table 1 | «Non‐problem gambler (score PGSI = 0) / 1379 (26.7%)» |
| E2 | all | PGSI · PGSI 1-4 (range 0-27) | **L1** | **2581 / 5163** | 50.0 | Table 1 | «Low‐risk gambler (score PGSI between 1 and 4) / 2581 (50.0%)» |
| E3 | all | PGSI · PGSI 5-7 (range 0-27) | **L2** | **579 / 5163** | 11.2 | Table 1 | «Moderate‐risk gambler (score PGSI between 5 and 7) / 579 (11.2%)» |
| E4 | all | PGSI · PGSI>=8 (range 0-27) | **L3** | **624 / 5163** | 12.1 | Table 1 | «Excessive gambler (score PGSI greater or equal to 8) / 624 (12.1%)» |
| E5 | all | PGSI · PGSI>=5 (range 0-27) | **L2** | **1203 / 5163** | 23.3 | Table 1; Methods, On-line survey | «At‐risk gambler (PGSI ≥ 5) / 1203 (23.3%)» |

- E1: cumulative: no; источник порога: standard; правило: PGSI row; score 0 is below L1; у авторов: «Non-problem gambler»; главная у авторов: no; период: past 12 months
- E2: cumulative: no; источник порога: validation paper; правило: PGSI row; 1-4 band starts at L1 (>=1); у авторов: «Low-risk gambler»; главная у авторов: no; период: past 12 months; заметка: Revised Currie et al. 2013 band; includes scores 3-4 that are moderate risk under standard scoring.
- E3: cumulative: no; источник порога: validation paper; правило: PGSI row; 5-7 band lower bound 5 lies in L2 (>=3, <8); у авторов: «Moderate-risk gambler»; главная у авторов: no; период: past 12 months; заметка: Revised Currie et al. 2013 band.
- E4: cumulative: yes; источник порога: standard; правило: PGSI row; >=8 is L3; у авторов: «Excessive gambler»; главная у авторов: no; период: past 12 months
- E5: cumulative: yes; источник порога: validation paper; правило: PGSI row; lower bound 5 lies in L2 (>=3, <8); у авторов: «At-risk gambler (moderate-risk or excessive)»; главная у авторов: yes; период: past 12 months; заметка: Cumulative category reported by the study (= 579 + 624); the authors' main status variable.

**Ключевые поля выборки:**
- **n_bettors: 5163** — Table 1 — «Gamblers engaged in sports betting, n = 5163»
- **sample_type: rep_survey_subsample** — Methods, Participants; Table 1 — «a large random panel (n = 840 797) of on‐line gamblers with an active gambling account ... used for poker, horse race betting and sports betting were contacted by e‐mail by the ARJEL»
- **sampling: probability** — Methods, Participants — «a large random panel (n = 840 797) of on‐line gamblers with an active gambling account»
- **betting_period: NR** — Table 1; Methods, Participants — «Gamblers engaged in sports betting, n = 5163»

**Остальные поля:**
- parent_population: Online gamblers in France with an active ARJEL-regulated account (poker, horse race betting, sports betting; at least one bet in past 12 months) — Methods, Participants — «on‐line gamblers with an active gambling account (i.e. with at least one bet during the past 12 months) used for poker, horse race betting and sports betting»
- min_frequency: none (active account = at least one bet in past 12 months) — Methods, Participants — «an active gambling account (i.e. with at least one bet during the past 12 months)»
- country: FRA — Methods, Participants — «on‐line gambling was regulated differently in France depending upon the type of gambling activity»
- subnational: NA — Methods, Participants — «Regulatory Authority for On‐line Gambling (Autorité de Régulation des Jeux En Ligne: ARJEL)»
- data_years: 2015-2016 — Methods, Participants — «contacted by e‐mail by the ARJEL in two successive waves (November 2015 and February 2016)»
- design: other — Methods, Design — «This longitudinal observational study is part of the second stage of the EDEIN (Screening for Excessive Gambling Behaviors on the Internet) research program»
- gambling_disclosed: NR — Methods, Participants — «The e‐mail included information on the study and a link to an on‐line survey hosted by the ARJEL.»
- betting_mode: online only — Methods, Participants — «The study participants were on‐line gamblers»
- pct_online: all — Methods, Participants — «The study participants were on‐line gamblers»
- pct_inplay: NR — NA
- pct_dfs: NR — NA
- pct_esports: NR — NA
- sports_lottery: no — Methods, Participants — «ARJEL regulated only gambling activities open to competition ... i.e. poker, horse race betting and sports betting. In parallel, the national lottery operator …»
- mixed_race: no — Table 1 — «Gamblers engaged in sports betting, n = 5163 | Gamblers engaged in horse race betting, n = 3524»
- legal_status: regulated legal market — Methods, Participants — «The Regulatory Authority for On‐line Gambling ... regulated only gambling activities open to competition in the on‐line gambling French market, i.e. poker, hor…»
- n_invited: 840797 — Methods, Participants — «a large random panel (n = 840 797) of on‐line gamblers»
- n_responded: 9306 — Methods, Participants — «A total of 9306 gamblers responded to the survey and had actionable data, which represents a response rate of 1.11%.»
- response_rate: 1.11 — Methods, Participants — «which represents a response rate of 1.11%»
- age_mean: NR — Table 1 — «Age (median, minimum–maximum) | 35 (18–94)»
- age_sd: NR — Table 1 — «Age (median, minimum–maximum) | 35 (18–94)»
- age_min: 18 — Table 1 — «Age (median, minimum–maximum) | 35 (18–94)»
- age_max: 94 — Table 1 — «Age (median, minimum–maximum) | 35 (18–94)»
- age_group: adults — Table 1 — «Age (median, minimum–maximum) | 35 (18–94)»
- pct_male: 92.9 — Table 1 — «Male | 4795 (92.9%)»
- mode: online — Methods, Participants — «a link to an on‐line survey hosted by the ARJEL»
- weights: NR — Methods, Analyses — «Analyses were performed separately for each indicator and for each type of gambling»
- instruments: PGSI (language version not stated; presumably French) — Methods, On-line survey — «The participants also responded to the Problem Gambling Severity Index (PGSI), which is a nine‐item self‐report questionnaire derived from the Canadian Problem…»
- instrument_validated_in_language: NR — Methods, On-line survey — «The participants also responded to the Problem Gambling Severity Index (PGSI)»
- industry_funding: no — Acknowledgements; Declaration of interests — «This research project received funding from the Primary Prevention Call for Proposals that was issued in 2013 by the French Institute for Public Health Researc…»
- funding_coi: Funded by IREsP (public). Four authors declare the University Hospital of Nantes received philanthropic sponsorship from FDJ and PMU (gambling industry), not assigned to this work. Data provided by ARJEL (regulator). — Declaration of interests — «the University Hospital of Nantes received funding from the gambling industry [Française des Jeux (FDJ) and Pari Mutuel Urbain (PMU)] in the form of a philanth…»
- pub_status: journal — Citation — «Addiction. 2022;117:1020–1034. 10.1111/add.15665»
- language: English — Full text — «Impact of wagering inducements on the gambling behaviors of on‐line gamblers»
- notes: Sports bettors are the subset of the ARJEL dataset (n=9306) 'engaged in sports betting'; the definition of engagement (tracking data vs self-report) is not stated, though the tracking data cover the 12 months before the survey (likely past 12 months). Sports bettors overlap with the horse-race and poker columns (same respondents can be in several). Age is median (35) and range for sports bettors; sex is for sports bettors (48 missing sex). Age and sex come from account data. PGSI categories use the revised Currie et al. 2013 thresholds (0, 1-4, 5-7, 8+); the standard 3-7 band is not reported.…

**Риск смещения (JBI):**
1. рамка выборки: **yes** — Frame was all active online gambling accounts regulated by ARJEL, covering online sports bettors in France. — Methods, Participants — «a large random panel (n = 840 797) of on‐line gamblers with an active gambling account ... used for poker, horse race betting and sports betting»
2. способ отбора: **yes** — Random sample drawn from the regulator's account frame. — Methods, Participants — «a large random panel (n = 840 797) of on‐line gamblers»
3. размер выборки: **yes** — 5163 sports bettors >= 385. — Table 1 — «Gamblers engaged in sports betting, n = 5163»
4. описание выборки и условий: **yes** — Age, sex, setting (online ARJEL accounts), country and dates reported. — Table 1; Methods, Participants — «Male | 4795 (92.9%) ... Age (median, minimum–maximum) | 35 (18–94)»
5. охват (пропуски): **yes** — PGSI categories sum to all 5163 sports bettors; no missing PGSI data among analysed bettors. — Table 1 — «1379 (26.7%) ... 2581 (50.0%) ... 579 (11.2%) ... 624 (12.1%)»
6. валидность определения случая: **unclear** — PGSI with standard 8+ threshold available, but the primary at-risk cut-off is 5+ and the language version and its validation are not stated. — Methods, On-line survey — «In the present study, a score of 5 was used as the threshold to define an at‐risk gambler»
7. единое надёжное измерение: **yes** — Same online survey, same PGSI, past-12-month time frame for all; psychometric source cited. — Methods, On-line survey — «The content of the on‐line survey was the same for gamblers in the two data sets ... the reference period for the PGSI was the past 12 months.»
8. статистика (числитель и знаменатель): **yes** — Counts and denominator of sports bettors given; CI can be calculated. — Table 1 — «At‐risk gambler (PGSI ≥ 5) | 1203 (23.3%)»
9. отклик: **no** — Response rate 1.11% with no non-response handling. — Methods, Participants — «which represents a response rate of 1.11%»

Правки:
- 

Проверено: да

---

## ST030 · Todorović 2022 · Medicinska istrazivanja

Основной отчёт R3603: [текст](../../fulltext/text/R3603.txt) · [PDF](../../fulltext/pdf/R3603.pdf) — «Social and lifestyle characteristics of sports bettors in Serbia» — [DOI](https://doi.org/10.5937/medi55-38731)
Расхождения в тексте: Sports bettor counts don't match. Text: 537 past-30-day bettors (10.0% of 5385) and 927 past-year bettors (17.2%). Table 1: the sex rows add to 538 (504+34), the residence rows to 538 (159+379), and the PGSI rows in the 'Sports betting' column to 913 (756+133+24). The PGSI percentages (82.8/14.6/2.6) are of 913. Following the rule to use the table, the PGSI estimates use n=913, with a flag that this probably matches past-year bettors (927, minus missing) rather than the 537 past-30-day bettors. The PGSI total of 3191 (3000+165+26) means only gamblers were scored on the PGSI. Text vs Table 2: the misuse OR is 1.76 in the text and 1.77 in the table. The employed CI is 1.19-4.72 in the text and 1.19-4.07 in the table. The Discussion says 'more than 43 times' for problem gambling, but the OR is 38.34.
Заметка ИИ: One sample was extracted. The PGSI time frame and language version are not reported. PGSI 1-2 and 3-7 are merged into 1-7 by the authors. The reviewer should check the sports-bettor definition behind the PGSI denominator: possibly the overlapping Terzic-Supic 2018 report clarifies it.

### ST030-1 · Serbia National Survey on Lifestyles (substance abuse and gambling) 2014, past-30-day sports bettors (n=537; PGSI denominator 913)
Отчёты: R3603 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | PGSI · PGSI 0 | **below** | **756 / 913** | 82.8 | Page 5, Table 1 (PGSI score) | «No problem gambling 3000 (94.0) 756 (82.8) 2244 (98.5)» |
| E2 | all | PGSI · PGSI 1-7 | **L1** | **133 / 913** | 14.6 | Page 5, Table 1 (PGSI score) | «Low/ moderate gambling 165 (5.2) 133 (14.6) 32 (1.4)» |
| E3 | all | PGSI · PGSI>=8 | **L3** | **24 / 913** | 2.6 | Page 5, Table 1 (PGSI score) | «Problem gambling 26(0.8) 24 (2.6) 2 (0.1)» |

- E1: cumulative: no; источник порога: standard; правило: PGSI row; 0 = below; у авторов: «No problem gambling»; главная у авторов: no; период: NR; **расчёт: n = 756 + 133 + 24 = 913 (sum of PGSI categories in the Sports betting column)**; заметка: Denominator unclear: 913 differs from the 537 past-30-day sports bettors; it may be past-year bettors (927) who answered the PGSI.
- E2: cumulative: no; источник порога: study's own; правило: PGSI row; 1-7 band starts at L1; у авторов: «Low/ moderate gambling»; главная у авторов: no; период: NR; **расчёт: n = 756 + 133 + 24 = 913**; заметка: Authors merged the low-risk and moderate-risk categories. Denominator unclear (913 vs 537).
- E3: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ = L3; у авторов: «Problem gambling»; главная у авторов: yes; период: NR; **расчёт: n = 756 + 133 + 24 = 913**; заметка: Reported as a covariate comparison, not as a headline prevalence. Denominator unclear (913 vs 537 past-30-day bettors). Unclear whether weighted.

**⚠ Проверка скриптом (обратите внимание):**
- E1, E2, E3: n оценки не равно n_bettors выборки (537): проверьте знаменатель

**Ключевые поля выборки:**
- **n_bettors: 537** — Page 4, Results — «537 participants (10.0%, 537/5385) reported sports betting in the month before the study.»
- **sample_type: rep_survey_subsample** — Page 2, Methods — «Sampling was done in accordance with Probability Proportion Sampling – PPS, with the use of multistage cluster sampling (19). The sample was representative of the general working-age population in Serbia (18-64 years).»
- **sampling: probability** — Page 2, Methods — «small territorial units were selected randomly with probability proportional to the population size. Then, each unit was selected using the National household registry as a sampling frame. The respondents in each of the selected households were selected using…»
- **betting_period: past 30 days or month** — Page 3, Measures — «Sports betting engagement was assessed with yes/ no question: ‘Have you done sports betting in the past 30 days?’ (Yes/No).»

**Остальные поля:**
- parent_population: Household-dwelling general working-age population of Serbia aged 18-64 — Page 2, Methods — «The sample was representative of the general working-age population in Serbia (18-64 years).»
- min_frequency: none — Page 3, Measures — «Participants who answered ,,Yes'' were categorized in the group of sports betting in the past 30 days»
- country: SRB — Page 2, Methods, Data source/sample — «The sample was representative of the general working-age population in Serbia (18-64 years).»
- subnational: NA — Page 2, Methods — «National Survey on lifestyles in Serbia: substance abuse and gambling, conducted during 2014»
- data_years: 2014 — Page 2, The procedure of data collection — «The data collection was conducted between January and March 2014.»
- design: cross-sectional — Page 2, Methods, Data source/sample — «The cross-sectional study included 5385 participants, aged 18-64 and was a secondary analysis of the data from the National Survey on lifestyles in Serbia: sub…»
- gambling_disclosed: yes — Page 2, Methods — «questionnaire specially developed for the National Survey on Lifestyle in Serbia: Substances Abuse and Gambling, 2014»
- betting_mode: NR — Page 7, Discussion — «Sports betting in our study refers to sports betting at betting places, as online betting was not very common in Serbia at the time the study was conducted (18…»
- pct_online: NR — Page 7, Discussion — «online betting was not very common in Serbia at the time the study was conducted»
- pct_inplay: NR — NA — «NR»
- pct_dfs: NR — NA — «NR»
- pct_esports: NR — NA — «NR»
- sports_lottery: unclear — Page 3, Measures — «‘Have you done sports betting in the past 30 days?’ (Yes/No).»
- mixed_race: no — Page 3, Measures — «‘Have you done sports betting in the past 30 days?’»
- legal_status: NR — Page 7, Discussion — «Sports betting market have grown in Serbia in the past two decades and sports betting places are now available in every quarter and every neighborhood in urban…»
- n_invited: 8079 — Page 2, Methods — «A total of 8079 households were eligible to participate (out of 11144 visited households).»
- n_responded: 5385 — Page 2, Methods; Page 4, Results — «The study included a total of 5385 participants.»
- response_rate: 66.7 — Page 2, Methods — «A total of 8079 households were eligible to participate (out of 11144 visited households).»
- age_mean: 34.45 — Page 4, Table 1 — «Age (in years) (X±SD) 42.18±13.63 34.45±11.70 43.04±13.56»
- age_sd: 11.70 — Page 4, Table 1 — «Age (in years) (X±SD) 42.18±13.63 34.45±11.70 43.04±13.56»
- age_min: 18 — Page 2, Methods — «The cross-sectional study included 5385 participants, aged 18-64»
- age_max: 64 — Page 2, Methods — «The cross-sectional study included 5385 participants, aged 18-64»
- age_group: adults — Page 2, Methods — «participants, aged 18-64»
- pct_male: 93.7 — Page 4, Table 1 — «Males 2676 (49.7) 504 (93.7) 2172 (44.8) Females 2709 (50.3) 34 (6.3) 2675 (55.2)»
- mode: face-to-face — Page 2, The procedure of data collection — «Face-to-face interviews were used for data collection»
- weights: yes — Page 2, Methods — «The sample was weighted for the sex, age, educational level, regions, and urban or rural areas.»
- instruments: PGSI (language version not stated; presumably Serbian, not reported) — Page 3, Measures — «Gambling severity was assessed with Problem Gambling Severity Index- PGSI (21)»
- instrument_validated_in_language: NR — Page 3, Measures — «PGSI is a nine-item scale used to screen individuals with high risk for pathological gambling (α=0.97).»
- industry_funding: no — Page 1, Funding information — «The authors received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors.»
- funding_coi: No specific funding; authors declare no competing interests — Page 1 — «The authors received no specific grant from any funding agency... The authors have declared that no competing interests exist»
- pub_status: journal — Page 1, header — «Medicinska istaživanja 2022; 55(2):47-55 | DOI 10.5937/medi55-38731»
- language: English (Serbian summary) — Page 1; Page 9 — «RESEARCH ARTICLE Social and lifestyle characteristics of sports bettors in Serbia»
- notes: Secondary analysis of the 2014 Serbian national lifestyles/gambling survey, also reported in Terzic-Supic et al. 2018 Int Gambl Stud (ref 18); check for overlap with that study. Response rate derived: 5385/8079 eligible households = 66.7% (5385/11144 visited = 48.3%). Age mean/SD and pct_male are for the past-30-day sports bettors (Table 1); age range is for the whole sample. Sports bettor counts don't match: text says 537 past-30-day bettors, Table 1 sex rows add to 538, and the PGSI rows in the Sports betting column add to 913 (756+133+24), close to the 927 past-year bettors. So the PGSI de…

**Риск смещения (JBI):**
1. рамка выборки: **yes** — Parent survey used the National household registry, which covers the Serbian adult household population. — Page 2, Methods — «each unit was selected using the National household registry as a sampling frame»
2. способ отбора: **yes** — Multistage PPS cluster sampling with Kish grid selection within households. — Page 2, Methods — «Sampling was done in accordance with Probability Proportion Sampling – PPS, with the use of multistage cluster sampling (19).»
3. размер выборки: **yes** — 537 past-30-day sports bettors (913 in PGSI rows), both >=385. — Page 4, Results — «537 participants (10.0%, 537/5385) reported sports betting in the month before the study.»
4. описание выборки и условий: **yes** — Age, sex, setting, country and dates of data collection are all reported. — Page 2; Page 4, Table 1 — «The data collection was conducted between January and March 2014. Face-to-face interviews were used»
5. охват (пропуски): **unclear** — Missing PGSI data among sports bettors not reported; PGSI denominator (913) does not match 537 bettors. — Page 5, Table 1 (PGSI score) — «No problem gambling 3000 (94.0) 756 (82.8) 2244 (98.5)»
6. валидность определения случая: **unclear** — PGSI with standard 8+ threshold, but the language version and its validation are not stated. — Page 3, Measures — «0 = non- problem gambler, 1-7 = low/moderate risk gambler, 8-27 = problem gambler.»
7. единое надёжное измерение: **yes** — Same instrument, same face-to-face mode and same thresholds for all participants; alpha reported. — Page 3, Measures — «PGSI is a nine-item scale used to screen individuals with high risk for pathological gambling (α=0.97).»
8. статистика (числитель и знаменатель): **no** — PGSI counts in the sports-betting column add to 913, not the 537 defined bettors; denominator cannot be traced; no CI; unclear whether weighted. — Page 4 Results; Page 5 Table 1 — «537 participants (10.0%, 537/5385) ... Problem gambling 26(0.8) 24 (2.6) 2 (0.1)»
9. отклик: **yes** — 5385 of 8079 eligible households responded (66.7%), and weights were applied. — Page 2, Methods — «A total of 8079 households were eligible to participate (out of 11144 visited households).»

Правки:
- n_bettors = 913
- betting_period = past 12 months

Проверено: да

