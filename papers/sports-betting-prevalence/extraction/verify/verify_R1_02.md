# Проверка выписывания — файл 2 из 6

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

## ST011 · Krotter 2025 · Journal of prevention (2022)

Основной отчёт R1768: [текст](../../fulltext/text/R1768.txt) — «Risk Factors of At-Risk/Problem Gambling Among Young Adult Spanish Students.» — [DOI](https://doi.org/10.1007/s10935-024-00814-x)
Расхождения в тексте: Text and Table 1 agree. 281+170 = 451 past-year gamblers. Sports bettors 105+103 = 208; 208/451 = 46.12%, which matches the text ("sports betting (46.12%)"). The PGSI bands match the totals: 281+97+59+14 = 451. Table 1 percentages check out: 105/281 = 37.37% and 103/170 = 60.59%.
Заметка ИИ: There is one eligible sample: past-year sports bettors among Spanish students aged 18-25. Its estimate is derived from the reverse table in Table 1, so only the PGSI 0 vs PGSI>=1 split is available; there is no problem-gambling (L3) estimate for sports bettors. Age and sex fields describe the whole sample.

### ST011-1 · Spanish university and vocational students aged 18-25, past-year sports bettors, Aragon/Asturias/Balearic Islands, 2021 (n=208)
Отчёты: R1768 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | PGSI · PGSI>=1 (range 0-27) | **L1** | **103 / 208** | 49.5 | Table 1 | «Non-problem gamblers (n = 281) / At-risk/problem gamblers (n = 170) ... Sports betting / 105 (37.37) / 103 (60.59)» |
| E2 | all | PGSI · PGSI 0 | **below** | **105 / 208** | 50.5 | Table 1 | «Sports betting / 105 (37.37) / 103 (60.59)» |

- E1: cumulative: yes; источник порога: standard; правило: PGSI row; >=1 starts at L1; у авторов: «at-risk/problem gamblers»; главная у авторов: no; период: past 12 months; **расчёт: Reverse table: 103 at-risk/problem gamblers bet on sports + 105 non-problem gamblers bet on sports = 208 sports bettors; cases = 103 (49.5%)**; заметка: The authors' main prevalence estimates are for all past-year gamblers; PGSI>=1 is their analysis outcome. The groups 281+170 = 451 cover all past-year gamblers with no overlap. PGSI time frame assumed to be past 12 months (standard PGSI; not stated explicitly).
- E2: cumulative: no; источник порога: standard; правило: PGSI row; score 0 = below; у авторов: «non-problem gamblers»; главная у авторов: no; период: past 12 months; **расчёт: 105 non-problem sports bettors of 105 + 103 = 208 sports bettors**; заметка: Finer PGSI bands (1-2, 3-7, 8+) are not reported for sports bettors.

**Ключевые поля выборки:**
- **n_bettors: 208** — Table 1 — «Sports betting | 105 (37.37) | 103 (60.59)»
- **sample_type: students** — Method, Participants — «The participants were young adult undergraduates studying at university or vocational schools»
- **sampling: convenience** — Method, Participants — «were recruited by non-probability sampling via print (flyers and posters) and mass media advertising (radio, TV, Instagram, and Twitter)»
- **betting_period: past 12 months** — Table 1 — «Gambling activities offline or online (12-months, n/%) ... Sports betting | 105 (37.37) | 103 (60.59)»

**Остальные поля:**
- parent_population: Young adults aged 18-25 studying at universities and vocational schools in Aragon, Asturias and the Balearic Islands (Spain) — Method, Participants — «young adult undergraduates studying at university or vocational schools from three autonomous communities in Spain»
- min_frequency: none — Method, Measures — «Past-year gambling activities were assessed ... and included: bingo, poker, casino games, sports betting»
- country: ESP — Method, Participants — «from three autonomous communities in Spain (Aragon, Principality of Asturias, and The Balearic Islands)»
- subnational: Aragon; Principality of Asturias; Balearic Islands — Method, Participants — «three autonomous communities in Spain (Aragon, Principality of Asturias, and The Balearic Islands)»
- data_years: 2021 — Method, Participants — «The recruitment was conducted during September–November 2021»
- design: cohort baseline — Method, Participants; Discussion — «willingness to participate in future assessments (specifically, 3 times in total every six months)... The initial assessment was completed by 2980 individuals.»
- gambling_disclosed: yes — Method, Participants — «a study aimed at evaluating addictive behaviors among young people, including alcohol, tobacco, cannabis, gaming and gambling»
- betting_mode: both — Table 1 — «Gambling activities offline or online (12-months, n/%)»
- pct_online: NR — Results — «Most participants gambled exclusively offline during the previous year (55.48%), followed by mixed modality (40.49%), and a minority exclusively online (4.03%).»
- pct_inplay: NR — NA
- pct_dfs: NR — NA
- pct_esports: NR — NA
- sports_lottery: unclear — Method, Measures — «included: bingo, poker, casino games, sports betting, lotteries, scratch-cards»
- mixed_race: no — Method, Measures — «sports betting»
- legal_status: NR — Method, Participants — «there were no specific restrictions on gambling»
- n_invited: NR — NA
- n_responded: 2980 — Method, Participants — «The initial assessment was completed by 2980 individuals.»
- response_rate: NR — NA
- age_mean: 19.47 — Method, Participants — «The final sample comprised 2762 participants with a mean age of 19.47 (SD = 1.64) years»
- age_sd: 1.64 — Method, Participants — «mean age of 19.47 (SD = 1.64) years»
- age_min: 18 — Method, Participants — «The eligibility criteria were: (1) being aged 18–25»
- age_max: 25 — Method, Participants — «The eligibility criteria were: (1) being aged 18–25»
- age_group: adults — Method, Participants — «being aged 18–25»
- pct_male: 35.84 — Method, Participants — «who were mostly women (64.16%)»
- mode: mixed — Method, Procedure — «completed an assessment (https://www.metajovenes.es) ... either using their own devices or tablets from the research project ... Participation was online or in…»
- weights: NR — Statistical Analyses — «we conducted a set of univariate descriptive statistics (i.e., means and frequencies)»
- instruments: PGSI, Spanish version (López-González et al., 2018) — Method, Measures — «Gambling severity was assessed through the Problem Gambling Severity Index (PGSI) (López-González et al., 2018).»
- instrument_validated_in_language: yes — Method, Measures — «This scale showed excellent psychometric properties in a sample of Spanish adults, with an internal consistency of 0.97 (López-González et al., 2018).»
- industry_funding: NR — Method, Procedure — «approved by the ethics committee from the university that received the funding»
- funding_coi: Funding source not named in the text provided; university-based project. COI NR. — Method, Procedure — «the ethics committee from the university that received the funding»
- pub_status: journal — Header — «Journal of prevention (2022); DOI: 10.1007/s10935-024-00814-x»
- language: English — Full text — «Risk Factors of At-Risk/Problem Gambling Among Young Adult Spanish Students»
- notes: Sports bettors were not analysed as a separate group; n and cases come from the reverse table (Table 1: sports betting among non-problem vs at-risk/problem gamblers, which together are all 451 past-year gamblers). Age and sex fields refer to the whole sample (n=2762); past-year gamblers: 269/451 male (59.6%), mean age 19.39 in both groups. pct_male 35.84 = 100 - 64.16. n_responded 2980 = completed the initial assessment; 2762 were left after exclusions (121 over age 25, 75 duplicates, 22 failed attention checks). Baseline of a longitudinal study (3 assessments 6 months apart); the authors cal…

**Риск смещения (JBI):**
1. рамка выборки: **no** — The frame is students reached by flyers, media ads and some courses in 3 regions; it does not cover young Spanish adults or students who bet. — Method, Participants — «recruited by non-probability sampling via print (flyers and posters) and mass media advertising»
2. способ отбора: **no** — Non-probability, volunteer sampling. — Method, Participants — «were recruited by non-probability sampling»
3. размер выборки: **no** — 208 sports bettors, below 385. — Table 1 — «Sports betting | 105 (37.37) | 103 (60.59)»
4. описание выборки и условий: **yes** — Age, sex, setting, country and dates reported (for the whole sample and gamblers, not for sports bettors). — Method, Participants — «2762 participants with a mean age of 19.47 (SD = 1.64) years, who were mostly women (64.16%)... September–November 2021»
5. охват (пропуски): **unclear** — Missing PGSI data are not reported; missing data are reported only for access modality (4) and gambler type (10). — Table 1 note — «b n = 4 missing data; cn = 10 missing data»
6. валидность определения случая: **yes** — Validated Spanish PGSI with standard categories. For sports bettors only the PGSI>=1 split is available; there is no L3 estimate. — Method, Measures — «Four groups were identified based on the PGSI total score: non-problem gamblers (PGSI = 0), low-risk gamblers (PGSI = 1–2), moderate-risk gamblers (PGSI = 3–7)…»
7. единое надёжное измерение: **yes** — Same e-assessment and PGSI for everyone; reliability reported in this sample (online vs in-person completion not compared). — Method, Measures — «The PGSI also showed a good internal consistency in the present study (α = 0.818).»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator can be derived from Table 1 counts, so a CI can be calculated; sports-bettor prevalence is not reported directly. — Table 1 — «Non-problem gamblers (n = 281) | At-risk/problem gamblers (n = 170) ... Sports betting | 105 (37.37) | 103 (60.59)»
9. отклик: **no** — Open advertising recruitment with no denominator of invited people; no handling of non-response. — Method, Participants — «mass media advertising (radio, TV, Instagram, and Twitter)»

Правки:
- 

Проверено: да

---

## ST012 · Mosconi 2025 · International Journal of Mental Health and Addiction

Основной отчёт R1879: [текст](../../fulltext/text/R1879.txt) · [PDF](../../fulltext/pdf/R1879.pdf) — «When Do the Stakes Get Higher? Examining Factors Associated with At-Risk or Problem Gambling in a Large Sample of Italian Adult Recent Gamblers» — [DOI](https://doi.org/10.1007/s11469-025-01472-8)
Расхождения в тексте: The sports-betting row in Table 2 is internally consistent (83 + 27 = 110). Other inconsistencies in the report: (1) Text p.5 describes moderate-risk as "PGSI score 1 to 7"; it should be 3-7. (2) Table 2, 'Both' modality: 24 + 27 = 51, not 65, and 24 is shown as 58.5%. (3) Table 2, scratch cards 'Yes': 656 + 136 = 792, not 798. (4) Table 2, '19–52 times/year': 188 + 38 = 226, not 251. (5) Table 2, virtual betting: 5/11 is printed as 45.6% (it is 45.5%). (6) Table 1, education levels sum to 753 of 1060; missing values are not explained. Two annual surveys (2022 and 2023) are pooled. Sports-betting results are not split by year, so they are extracted as one sample even though the rules treat separate years as separate samples.
Заметка ИИ: There is one sample: past-year fixed-odds sports bettors (n=110) within pooled Italian probability surveys (2022-2023). Only PGSI 0 and PGSI>=1 are available for this subsample.

### ST012-1 · Italy, DOXA population surveys 2022 and 2023 (pooled), adult past-year sports bettors among recent gamblers, n=110
Отчёты: R1879 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | PGSI · PGSI 0 (PGSI<1) | **below** | **83 / 110** | 75.5 | Page 8, Table 2, Sport betting = Yes | «Sport betting ... Yes 110 (10.4) 83 (75.5) 27 (24.5) 1.89 (1.12–3.19)» |
| E2 | all | PGSI · PGSI>=1 | **L1** | **27 / 110** | 24.5 | Page 8, Table 2, Sport betting = Yes | «Sport betting ... Yes 110 (10.4) 83 (75.5) 27 (24.5) 1.89 (1.12–3.19)» |

- E1: cumulative: no; источник порога: standard; правило: PGSI row; score 0 = below L1; у авторов: «No problem gambling»; главная у авторов: no; период: past 12 months; заметка: Row percentage 75.5%.
- E2: cumulative: yes; источник порога: standard; правило: PGSI row; >=1 starts at L1; у авторов: «At-risk or problem gambling (ARoP)»; главная у авторов: yes; период: past 12 months; заметка: Cumulative category reported by the study (24.5%). ARoP is the authors' main outcome. No PGSI 1-2, 3-7 or 8+ breakdown is given for sports bettors.

**Ключевые поля выборки:**
- **n_bettors: 110** — Page 8, Table 2, Sport betting row — «Sport betting ... Yes 110 (10.4) 83 (75.5) 27 (24.5) 1.89 (1.12–3.19)»
- **sample_type: rep_survey_subsample** — Page 3, Methods, Participants; Page 8, Table 2 — «The samples for the two surveys were selected using probabilistic sampling. ... A total of 1060 Italian adults (i.e., aged 18 years or over) who reported gambling in the past 12 months were selected from the two surveys»
- **sampling: probability** — Page 3, Methods, Participants — «The samples for the two surveys were selected using probabilistic sampling.»
- **betting_period: past 12 months** — Page 3-4, Instruments and Procedure; Page 8, Table 2 — «The interview assessed the frequency of use of each gambling format in the previous 12 months»

**Остальные поля:**
- parent_population: Italian population aged 15+ (two DOXA representative surveys, 2022 and 2023); analysis restricted to adults 18+ who gambled in the past 12 months (n=1060) — Page 3, Methods, Participants — «The exclusion criteria were an age below 15 years and a lack of Italian language comprehension. A total of 1060 Italian adults (i.e., aged 18 years or over) wh…»
- min_frequency: none — Page 3-4, Instruments and Procedure — «choosing from the following options: “never,” “once or twice a year,” “3–4 times a year,”»
- country: ITA — Page 3, Methods, Participants — «on representative samples of the Italian population»
- subnational: NA — Page 3, Methods, Participants — «representative samples of the Italian population»
- data_years: 2022-2023 — Page 3, Methods, Participants — «data collected from two surveys conducted in 2022 and 2023, respectively, by DOXA»
- design: cross-sectional — Page 11, Discussion (limitations) — «the cross-sectional design prevents the establishment of causal relationships»
- gambling_disclosed: NR — Page 3, Instruments and Procedure — «The questionnaire collected data on demographic factors, ... smoking status ... Furthermore, the questionnaire included a specific section on gambling.»
- betting_mode: both — Page 4, Data Analysis — «“sports betting” (i.e., land-based and online fixed odds sports betting)»
- pct_online: NR — Page 8, Table 2 — «Gambling Land-based 957 (90.3) Online 38 (3.6) Both 65 (6.1)»
- pct_inplay: NR — NR — «NR»
- pct_dfs: NR — NR — «NR»
- pct_esports: NR — NR — «NR»
- sports_lottery: no — Page 4, Data Analysis — «“lotteries” (i.e., ... totalizer number games), ... “sports betting” (i.e., land-based and online fixed odds sports betting)»
- mixed_race: no — Page 4, Data Analysis — «“sports betting” (i.e., land-based and online fixed odds sports betting)»
- legal_status: regulated legal market — Page 3, Introduction; Page 10, Discussion — «the Italian gambling market has undergone significant transformations, becoming one of the largest in the world ... In Italy, gambling advertising is officiall…»
- n_invited: NR — Page 3, Methods — «Details on the methodology used, including the sampling procedure, are available elsewhere»
- n_responded: NR — Page 3, Methods — «A total of 1060 Italian adults ... who reported gambling in the past 12 months were selected from the two surveys»
- response_rate: NR — NR — «NR»
- age_mean: NR — Page 7, Table 1 — «Age group 18–24 years 60 (5.7) ... 65 + years 259 (24.4)»
- age_sd: NR — NR — «NR»
- age_min: 18 — Page 3, Methods, Participants — «1060 Italian adults (i.e., aged 18 years or over)»
- age_max: NR — Page 7, Table 1 — «65 + years 259 (24.4)»
- age_group: adults — Page 3, Methods, Participants — «Italian adults (i.e., aged 18 years or over)»
- pct_male: 58.8 — Page 7, Table 1 — «Sex Male 623 (58.8) ... Female 437 (41.2)»
- mode: face-to-face — Page 3, Instruments and Procedure — «administered by ad hoc trained interviewers in the context of a computer-assisted personal in-house (CAPI) interview»
- weights: NR — Page 5, Data Analysis — «we calculated adjusted odds ratios (OR) and 95% confidence intervals (CI) using unconditional logistic regression models»
- instruments: PGSI (Italian version, Colasante et al. 2012) — Page 4, Instruments and Procedure — «assessed using the Italian version of the Problem Gambling Severity Index (PGSI) (Colasante et al., 2012; Ferris & Wynne, 2001)»
- instrument_validated_in_language: yes — Page 4; References p.13 (Colasante 2012) — «Colasante, E., ... (2012). An assessment of the psychometric properties of Italian version of CPGI»
- industry_funding: no — Page 12, Funding — «This work was supported by the Italian National Institute of Health.»
- funding_coi: Italian National Institute of Health; open access via Università di Pavia (CRUI-CARE); authors declare no competing interests — Page 12, Funding; Competing Interests — «This work was supported by the Italian National Institute of Health. ... The authors declare no competing interests.»
- pub_status: journal — Page 1, header — «International Journal of Mental Health and Addiction (2026) 24:1645–1659 ... ORIGINAL ARTICLE»
- language: English — Full text — «When Do the Stakes Get Higher? Examining Factors Associated with At-Risk or Problem Gambling in a Large Sample of Italian Adult Recent Gamblers»
- notes: Pooled sports bettors from two separate annual DOXA surveys (2022: 543 gamblers; 2023: 517 gamblers). The coding rules treat surveys in different years as separate samples, but sports-betting results are given only for the pooled data, so one pooled sample is extracted. Sports betting = fixed-odds sports betting only; virtual betting is a separate category (11 gamblers) and is not included. Age and sex describe all 1060 past-year gamblers, not the sports bettors; age is given only in bands (no mean). Total survey sizes and response rates are not reported (the authors cite Liu 2020 and Lugo 20…

**Риск смещения (JBI):**
1. рамка выборки: **yes** — The parent surveys are representative population surveys of Italy, which suits Italian adult sports bettors. The frame itself is only described in cited papers. — Page 3, Methods, Participants — «on representative samples of the Italian population ... Details on the methodology used, including the sampling procedure, are available elsewhere»
2. способ отбора: **yes** — The parent surveys used probability sampling. — Page 3, Methods, Participants — «The samples for the two surveys were selected using probabilistic sampling.»
3. размер выборки: **no** — There are 110 sports bettors, below 385. — Page 8, Table 2 — «Yes 110 (10.4) 83 (75.5) 27 (24.5)»
4. описание выборки и условий: **yes** — Age bands, sex, the face-to-face CAPI setting, the country (Italy) and the years (2022-2023) are reported, but for all gamblers rather than for sports bettors. — Page 3; Page 7, Table 1 — «computer-assisted personal in-house (CAPI) interview ... Italy, 2022–2023»
5. охват (пропуски): **yes** — All 110 sports bettors are classified by PGSI (83 + 27 = 110), so no PGSI data are missing for them. — Page 8, Table 2 — «Yes 110 (10.4) 83 (75.5) 27 (24.5)»
6. валидность определения случая: **yes** — The study uses the Italian PGSI, which has a published validation (Colasante 2012), with the standard Ferris & Wynne categories. The only estimate for sports bettors is PGSI>=1; no L3 estimate is given. — Page 4, Instruments and Procedure — «Italian version of the Problem Gambling Severity Index (PGSI) (Colasante et al., 2012; Ferris & Wynne, 2001)»
7. единое надёжное измерение: **yes** — Every participant had the same PGSI, the same past-year time frame and the same face-to-face CAPI mode. Reliability is cited from the literature, not computed in this sample. — Page 2-4 — «Psychometric evaluations have demonstrated the PGSI’s strong internal validity and reliability»
8. статистика (числитель и знаменатель): **yes** — The numerator (27) and denominator (110) are explicit, so a CI can be calculated. Weighting is not reported. — Page 8, Table 2 — «Sport betting ... Yes 110 (10.4) 83 (75.5) 27 (24.5)»
9. отклик: **unclear** — The response rate of the parent surveys is not reported. — Page 3, Methods — «Details on the methodology used, including the sampling procedure, are available elsewhere»

Правки:
- 

Проверено: да

---

## ST013 · Tomei 2025 · Journal of Gambling Studies

Основной отчёт R2108: [текст](../../fulltext/text/R2108.txt) — «Gambling Progression in Young Adults Following Online Casino-Gambling Legalization in Switzerland» — [DOI](https://doi.org/10.1007/s10899-025-10435-6)
Расхождения в тексте: 1) Past-year gamblers: 1,177 in the text, but Table 2 PGSI n = 1,130. The text says 'all participants (N = 2,302)', not 2,349. 2) Table 1 type-of-game n = 1,085 offline and 482 online, but Table 4 has 830+209 = 1,039 and Table 5 has 323+142 = 465 (missing PGSI). 3) The Table 3 group sizes vary (896/228, 896/230, 898/231). 4) The Discussion says educational attainment was a significant factor, but Results report no association with education. 5) The text says 'participants with at-risk/problem gambling were less likely to engage in offline gambling'. The figures match the 'offline only' row (36.5% vs 63.6%). 6) All percentages are weighted, so counts derived from them are approximate. 7) The land-based and online sports-bettor groups overlap, so no whole-sample sports-bettor estimate can be built.
Заметка ИИ: I extracted one sample, sports bettors among conscripts, with subgroup estimates by betting mode. The estimates come from reverse tables (Tables 4-5) and use the authors' dichotomized PGSI (0-2 vs 3+). The 3-7 and 8+ bands are not available for sports bettors. Legal status of sports betting is not described in the text. The French PGSI adaptation has no cited validation.

### ST013-1 · Swiss Army conscripts, French-speaking Switzerland, 2023-2024, past-year sports bettors (land-based n≈348; online n≈240, derived)
Отчёты: R2108 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | land-based | PGSI · PGSI>=3 | **L2** | **126 / 348** | 36.2 | Table 4 | «Type of land-based game played / (n = 830) / (n = 209) ... Sports betting / 26.8 / 60.5 / ***» |
| E2 | land-based | PGSI · PGSI 0-2 | **below** | **222 / 348** | 63.8 | Table 4; Weighting and Analyses | «the PGSI scores were dichotomized into two categories: Non-problem gambling (No problem and Low risk), At-risk/Problem gambling (Moderate risk and Problem gambling)» |
| E3 | online | PGSI · PGSI>=3 | **L2** | **83 / 240** | 34.6 | Table 5 | «Type of online game played / (n = 323) / (n = 142) ... Sports betting / 48.5 / 58.4 / ns» |
| E4 | online | PGSI · PGSI 0-2 | **below** | **157 / 240** | 65.4 | Table 5 | «Sports betting / 48.5 / 58.4 / ns» |

- E1: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 (moderate risk + problem) starts at L2; у авторов: «At-risk/Problem gambling»; главная у авторов: no; период: past 12 months; **расчёт: Reverse table: at-risk/problem 60.5% x 209 = 126.4 -> 126; non-problem 26.8% x 830 = 222.4 -> 222; n = 126 + 222 = 348**; заметка: Past-year land-based sports bettors (may also bet online). Percentages are weighted; derived counts approximate. Table 1 gives 34.1% of 1,085 land-based gamblers (≈370) bet on sports; difference due to missing PGSI.
- E2: cumulative: no; источник порога: study's own; правило: PGSI row; 0-2 band lower bound 0 = below; у авторов: «Non-problem gambling (No problem and Low risk)»; главная у авторов: no; период: past 12 months; **расчёт: 26.8% x 830 = 222.4 -> 222; n = 222 + 126 = 348**; заметка: Combined PGSI 0 and 1-2 category as dichotomized by the authors.
- E3: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 (moderate risk + problem) starts at L2; у авторов: «At-risk/Problem gambling»; главная у авторов: no; период: past 12 months; **расчёт: Reverse table: at-risk/problem 58.4% x 142 = 82.9 -> 83; non-problem 48.5% x 323 = 156.7 -> 157; n = 83 + 157 = 240**; заметка: Past-year online sports bettors (may also bet land-based). Weighted percentages; derived counts approximate. Table 1: 51.2% of 482 online gamblers (≈247) bet on sports.
- E4: cumulative: no; источник порога: study's own; правило: PGSI row; 0-2 band lower bound 0 = below; у авторов: «Non-problem gambling (No problem and Low risk)»; главная у авторов: no; период: past 12 months; **расчёт: 48.5% x 323 = 156.7 -> 157; n = 157 + 83 = 240**; заметка: Combined PGSI 0 and 1-2 category as dichotomized by the authors.

**Ключевые поля выборки:**
- **n_bettors: NR** — Tables 4-5 (derived) — «Sports betting | 26.8 | 60.5 ... Sports betting | 48.5 | 58.4»
- **sample_type: rep_survey_subsample** — Methods, Sample — «In Switzerland, all men who have reached the age of majority are required to participate in a mandatory two-day recruitment program before their 25th birthday.»
- **sampling: census** — Methods, Sample — «Paper-and-pencil questionnaires were administered to 2,618 conscripts of the Swiss Army. ... A total of 2,571 participants completed the questionnaire, yielding a response rate of 98.2%.»
- **betting_period: past 12 months** — Table 1; Weighting and Analyses — «All analyses related to gambling behaviors were based on past-year gambling.»

**Остальные поля:**
- parent_population: Male Swiss conscripts aged 18-24 residing in the French-speaking region of Switzerland, attending the Payerne Army recruitment centre Aug 2023-Jan 2024 — Methods, Sample; Acknowledgements — «Paper-and-pencil questionnaires were administered to 2,618 conscripts of the Swiss Army.»
- min_frequency: none — Methods, Questionnaire — «Those who reported past-year gambling proceeded to section two»
- country: CHE — Methods, Sample — «These conscripts were all Swiss nationals residing in the French-speaking region of Switzerland.»
- subnational: French-speaking region of Switzerland (Romandie) — Methods, Sample — «residing in the French-speaking region of Switzerland»
- data_years: 2023-2024 — Methods, Procedure — «The data collection took place between August 2023 and January 2024.»
- design: cross-sectional — Introduction — «the present study was a direct replication of the 2019 survey on the same population (Tomei et al., 2022)»
- gambling_disclosed: NR — Methods, Procedure; Questionnaire — «The questionnaires were administered prior to a problem gambling prevention class ... The cover page of the questionnaire provided information about the study'…»
- betting_mode: both — Table 1 — «Sports betting | 34.1 | 51.2»
- pct_online: NR — Table 1 — «Sports betting | 34.1 | 51.2»
- pct_inplay: NR — NA
- pct_dfs: NR — NA
- pct_esports: NR — NA
- sports_lottery: unclear — Table 1 — «Sports betting | 34.1 | 51.2 ... Lottery | 18.1 | 12.5»
- mixed_race: no — Table 1 — «Horse race betting | 3.1 | 2.5»
- legal_status: NR — Introduction — «the 2019 Federal Act on Gambling ... legalized online casino gaming for the first time. This reform allowed Swiss land-based casinos to operate online while bl…»
- n_invited: 2618 — Methods, Sample — «Paper-and-pencil questionnaires were administered to 2,618 conscripts of the Swiss Army.»
- n_responded: 2571 — Methods, Sample — «A total of 2,571 participants completed the questionnaire, yielding a response rate of 98.2%.»
- response_rate: 98.2 — Methods, Sample — «yielding a response rate of 98.2%»
- age_mean: 20.6 — Methods, Sample — «all male, aged 18–24 years (M = 20.6 years; Md = 20 years)»
- age_sd: NR — NA
- age_min: 18 — Methods, Sample — «all male, aged 18–24 years»
- age_max: 24 — Methods, Sample — «all male, aged 18–24 years»
- age_group: adults — Methods, Sample — «all male, aged 18–24 years»
- pct_male: 100 — Methods, Sample — «the final sample consisted of 2,349 participants, all male»
- mode: paper — Methods, Sample — «Paper-and-pencil questionnaires were administered»
- weights: yes — Weighting and Analyses — «data were weighted based on the Swiss population statistics (Swiss Federal Statistical Office, 2025)»
- instruments: PGSI (9 items, French adaptation, 0-3 scoring) — Methods, Questionnaire — «the 9-item Problem Gambling Severity Index (PGSI; Ferris & Wynne, 2001). The PGSI items were adapted into French and used a 4-point response scale ranging from…»
- instrument_validated_in_language: NR — Methods, Questionnaire — «The PGSI items were adapted into French»
- industry_funding: no — Acknowledgements — «The financial support for this study was generously provided by the "Programme intercantonal de lutte contre la dépendance au jeu" [Intercantonal Program again…»
- funding_coi: Intercantonal Program against Gaming Addiction (public, cantonal); open access by University of Lausanne; no conflicts declared — Acknowledgements; Funding; Conflict interest — «The authors declare that they have no conflict of interest.»
- pub_status: journal — Header — «Journal of Gambling Studies; DOI: 10.1007/s10899-025-10435-6»
- language: English — Full text — «Gambling Progression in Young Adults Following Online Casino-Gambling Legalization in Switzerland»
- notes: No PGSI estimate for all sports bettors is reported. There are only reverse tables of land-based (Table 4) and online (Table 5) game types by PGSI group (non-problem 0-2 vs at-risk/problem 3+). Counts are derived from weighted percentages x unweighted group n, so they are approximate. Land-based and online sports bettors overlap by an unknown amount, so they cannot be summed into a whole-sample n; n_bettors is therefore NR. Age and sex describe the whole sample (2,349). The earlier 2019 wave (ages 18-22, Tomei et al. 2022) is a separate survey and is not extracted here. Sampling is coded cens…

**Риск смещения (JBI):**
1. рамка выборки: **yes** — Conscription recruitment is mandatory for Swiss men before age 25, so the frame covers young men of the region (only a 6-month window at one centre). — Methods, Sample — «In Switzerland, all men who have reached the age of majority are required to participate in a mandatory two-day recruitment program before their 25th birthday.»
2. способ отбора: **yes** — Census of all conscripts attending in the data collection period. — Methods, Sample — «Paper-and-pencil questionnaires were administered to 2,618 conscripts of the Swiss Army.»
3. размер выборки: **no** — Derived sports-bettor subgroups are 348 (land-based) and 240 (online), both below 385; total not reported. — Tables 4-5 (derived) — «Type of land-based game played | (n = 830) | (n = 209) ... Sports betting | 26.8 | 60.5»
4. описание выборки и условий: **yes** — Age, sex, setting, country and dates reported. — Methods, Sample; Procedure — «all male, aged 18–24 years (M = 20.6 years ... The data collection took place between August 2023 and January 2024.»
5. охват (пропуски): **yes** — PGSI available for 1,130 of 1,177 past-year gamblers (~4% missing); 1,039 of 1,085 land-based gamblers in Table 4. — Results; Table 2 — «Degree of problem gambling severity | (n = 1,130)»
6. валидность определения случая: **unclear** — PGSI with standard thresholds, but French adaptation without cited validation. — Methods, Questionnaire — «The PGSI items were adapted into French and used a 4-point response scale ranging from 0 (Never) to 3 (Always).»
7. единое надёжное измерение: **unclear** — Same instrument, paper mode and threshold for all, but reliability not reported. — Methods, Questionnaire — «Scores were interpreted as follows: 0 = Non-problem gambling; 1–2 = Low-risk gambling; 3–7 = Moderate-risk gambling; 8 or more = Problem gambling.»
8. статистика (числитель и знаменатель): **no** — No numerator/denominator of sports bettors reported; only weighted column percentages in reverse tables; counts must be derived. — Tables 4-5 — «Sports betting | 48.5 | 58.4 | ns»
9. отклик: **yes** — Response rate 98.2%. — Methods, Sample — «yielding a response rate of 98.2%»

Правки:
- 

Проверено: да

---

## ST014 · Westerberg 2025 · BMC Psychology

Основной отчёт R2161: [текст](../../fulltext/text/R2161.txt) — «The role of craving in gambling behavior: examining its relevance and links to psychological distress, personality, and demographics» — [DOI](https://doi.org/10.1186/s40359-025-03816-4)
Расхождения в тексте: Table 2 sports-betting row: the at-risk column counts (49+28+22+21) sum to 120, but group n = 119. The 40.8% figure fits 49/120. The gambling-disorder column sums to 41, but group n = 42; 19.5% = 8/41. The same 41 total appears in the online/offline row for GD. Some percentages in Table 2 are missing (printed as only "(n)"). The abstract gives "median age 48.4", but the Participants section gives M = 48.42 (mean). Table 1 male counts (446+79+28+28 = 581, 55.2%) differ from the 54.9% in the text; this is probably because 3 'other/prefer not to say' cases were assigned to male. In the text the gender chi-square is p < 0.001, but Table 1 prints p = 0.05.
Заметка ИИ: There is one eligible sample: the past-12-month sports bettors within an Ipsos web-panel survey of Swedish adult gamblers. It was derived with the reverse-table rule from Table 2 (NODS groups cover all gamblers without overlap). Whether the printed counts are age/sex-weighted is not stated. The text gives no funding information.

### ST014-1 · Sweden, Ipsos citizen panel of past-year gamblers, 2023 – past-12-month sports bettors (n=416 derived)
Отчёты: R2161 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | NODS · NODS 0 (range 0-10) | **below** | **282 / 416** | 67.8 | Table 2, Sports betting rows | «Last year / 16.9 (144) ... Last month / 9.4 (80) ... Last week or more / 6.8 (58)» |
| E2 | all | NODS · NODS 1-2 (range 0-10) | **L1** | **71 / 416** | 17.1 | Table 2, Sports betting rows | «Last year / ... / (28) ... Last month / ... / (22) ... Last week or more / ... / 17.5 (21)» |
| E3 | all | NODS · NODS 3-4 (range 0-10) | **L2** | **30 / 416** | 7.2 | Table 2, Sports betting rows | «Last year / ... / 14.3 (6) ... Last month / ... / 26.2 (11) ... Last week or more / ... / 31.0 (13)» |
| E4 | all | NODS · NODS>=5 (range 0-10) | **L3** | **33 / 416** | 7.9 | Table 2, Sports betting rows | «Last year / ... / 31.7 (13) ... Last month / ... / 17.1 (7) ... Last week or more / ... / 31.7 (13)» |

- E1: cumulative: no; источник порога: standard; правило: NODS row; score 0 is below L1; у авторов: «non-problem gambling»; главная у авторов: no; период: past 12 months; **расчёт: Non-problem column, sports betting: 144 last year + 80 last month + 58 last week or more = 282; n = 282 + 71 + 30 + 33 = 416**; заметка: Reverse table; the groups cover all 1053 gamblers. Unclear whether counts are weighted.
- E2: cumulative: no; источник порога: standard; правило: NODS row; 1-2 band starts at L1; у авторов: «at-risk gambling»; главная у авторов: no; период: past 12 months; **расчёт: At-risk column, sports betting: 28 + 22 + 21 = 71**; заметка: At-risk column sums to 120 (49 non-bettors + 71) although group n = 119; 119 - 49 would give 70.
- E3: cumulative: no; источник порога: standard; правило: NODS row; 3-4 band starts at L2; у авторов: «problem gambling»; главная у авторов: no; период: past 12 months; **расчёт: Problem gambling column, sports betting: 6 + 11 + 13 = 30**
- E4: cumulative: yes; источник порога: standard; правило: NODS row; >=5 is L3; у авторов: «probable gambling disorder / pathological gambling»; главная у авторов: no; период: past 12 months; **расчёт: Gambling disorder column, sports betting: 13 + 7 + 13 = 33**; заметка: GD column sums to 41 (8 non-bettors + 33) although group n = 42; one respondent is missing on the sports-betting item.

**Ключевые поля выборки:**
- **n_bettors: 416** — Table 2, Sports betting rows — «Not gambled | 66.8 (568) | 40.8 (49) | 28.6 (12) | 19.5 (8) ... Last year | 16.9 (144) | (28) | 14.3 (6) | 31.7 (13) Last month | 9.4 (80) | (22) | 26.2 (11) | 17.1 (7) Last week or more | 6.8 (58) | 17.5 (21) | 31.0 (13) | 31.7 (13)»
- **sample_type: gamblers_survey_subsample** — Materials and methods, Participants — «Participants in this study (aged 18 years and older) had responded to a screening question, indicating that they had gambled for money within the past 12 months.»
- **sampling: quota** — Materials and methods, Participants — «The company recruited individuals until representative distribution was obtained.»
- **betting_period: past 12 months** — Table 2 note — «Frequency of engagement in this gambling activity: never, in the last year, in the last month, or in the last week or more recently»

**Остальные поля:**
- parent_population: Swedish adults (18+) who gambled for money in the past 12 months, members of the Ipsos citizen panel — Materials and methods, Participants — «Participants in the citizen panel had previously enrolled with their personal information in the Ipsos system, agreeing to receive surveys by e-mail. The compa…»
- min_frequency: none — Table 2 — «Sports bettingc Not gambled ... Last year ... Last month ... Last week or more»
- country: SWE — Materials and methods, Participants — «The data were collected from a web survey distributed to a citizen panel of the Swedish market research company Ipsos»
- subnational: NA — Materials and methods, Participants — «The participants comprised 1053 Swedish adult gamblers (54.9% male) aged 18–84 years»
- data_years: 2023 — Materials and methods, Participants — «The current data collection was conducted between May and August 2023»
- design: cross-sectional — Limitations — «its cross-sectional design does not allow for causal inferences regarding the observed relationships»
- gambling_disclosed: NR — Materials and methods, Procedure — «Individuals from this panel were invited to participate in the present study. Eligibility for inclusion required that participants had engaged in gambling acti…»
- betting_mode: both — Table 2 — «Form and frequency of gambling activitiesc Online 60.1 (511) ... Offline 30.4 (258)»
- pct_online: NR — Table 2 — «Online | 60.1 (511) | 84.9 (101) | 97.6 (41) | 87.8 (36)»
- pct_inplay: NR — NA
- pct_dfs: NR — NA
- pct_esports: NR — NA
- sports_lottery: unclear — Table 2 — «Sports bettingc Not gambled 66.8 (568)»
- mixed_race: no — Table 2 — «Horse bettingc Not gambled 60.6 (515)»
- legal_status: NR — NA
- n_invited: NR — Materials and methods, Procedure — «Individuals from this panel were invited to participate in the present study.»
- n_responded: 1053 — Materials and methods, Participants — «The participants comprised 1053 Swedish adult gamblers (54.9% male) aged 18–84 years (M = 48.42, SD = 17.29).»
- response_rate: NR — NA
- age_mean: 48.42 — Materials and methods, Participants — «aged 18–84 years (M = 48.42, SD = 17.29)»
- age_sd: 17.29 — Materials and methods, Participants — «aged 18–84 years (M = 48.42, SD = 17.29)»
- age_min: 18 — Materials and methods, Participants — «aged 18–84 years»
- age_max: 84 — Materials and methods, Participants — «aged 18–84 years»
- age_group: adults — Materials and methods, Participants — «Participants in this study (aged 18 years and older)»
- pct_male: 54.9 — Materials and methods, Participants — «1053 Swedish adult gamblers (54.9% male)»
- mode: online — Materials and methods, Participants — «The data were collected from a web survey»
- weights: yes — Materials and methods, Participants — «Before the data were obtained from Ipsos, all cases were weighted by gender and age to enhance representativeness»
- instruments: NODS-SA past-year version (Swedish translation) — Measures — «The Swedish version of the NORC Diagnostic Screen for Gambling Problems – Past Year version (NODS-SA; [43], translated into Swedish by [83]) was used»
- instrument_validated_in_language: NR — Measures — «translated into Swedish by [83] ... Gerstein et al. [43] reported excellent test–retest reliability for the NODS»
- industry_funding: NR — NA
- funding_coi: No funding or competing-interest statement in the supplied text — NA
- pub_status: journal — Header — «Year: 2025; venue: BMC Psychology; DOI: 10.1186/s40359-025-03816-4»
- language: English — Full text — «The role of craving in gambling behavior: examining its relevance and links to psychological distress, personality, and demographics»
- notes: The authors do not analyse sports bettors separately. The sample is derived from the reverse table (Table 2: sports-betting frequency by NODS group). Past-12-month sports bettors = respondents not reporting 'Not gambled'. Age, sex and mode describe the whole sample of 1,053 gamblers, not the sports bettors. Data were weighted by gender and age before delivery from Ipsos; it is unclear whether the table counts are weighted. Table 2 also has a separate unspecified 'Betting' row and a 'Horse betting' row; only the 'Sports betting' row was used. Three cases with gender 'other/prefer not to say' w…

**Риск смещения (JBI):**
1. рамка выборки: **no** — The frame is the members of a commercial Ipsos web panel, not all Swedish sports bettors — Materials and methods, Participants — «web survey distributed to a citizen panel of the Swedish market research company Ipsos»
2. способ отбора: **no** — Voluntary opt-in online panel recruited to a representative distribution (non-probability) — Limitations — «the use of a online survey for data collection administered to members of a voluntary web panel, may pose risks of both recall bias and selection bias»
3. размер выборки: **yes** — 416 sports bettors (derived), which is at least 385 — Table 2 — «Sports bettingc Not gambled 66.8 (568) 40.8 (49) 28.6 (12) 19.5 (8)»
4. описание выборки и условий: **yes** — Age, sex, setting, country and dates are reported (for the whole sample) — Materials and methods, Participants — «between May and August 2023 ... 1053 Swedish adult gamblers (54.9% male) aged 18–84 years (M = 48.42, SD = 17.29)»
5. охват (пропуски): **yes** — NODS classified for all 1053; the sports-betting item appears to be missing for only about one respondent — Data preparation; Table 2 — «individuals with non-problem gambling (n = 850 [81%]), at-risk gambling (n = 119 [11%]), problem gambling (n = 42 [4%]), and probable gambling disorder (n = 42…»
6. валидность определения случая: **unclear** — Standard NODS thresholds were used, but no validation of the Swedish translation is cited — Measures — «translated into Swedish by [83] ... a score of 1 or 2 indicating at-risk gambling, of 3 or 4 problem gambling, and of 5 or more pathological gambling»
7. единое надёжное измерение: **yes** — Same online NODS-SA past-year instrument for all; alpha reported in this sample — Measures — «NODS-SA as used here was found to have excellent internal consistency (Cronbach’s α = 0.92, 95% CI [0.91–0.92])»
8. статистика (числитель и знаменатель): **unclear** — Prevalence among sports bettors is not reported; it is derivable from the reverse table, but column sums are inconsistent (120 vs 119; 41 vs 42) and it is unclear whether counts are weighted — Table 2 — «Not gambled | 66.8 (568) | 40.8 (49) | 28.6 (12) | 19.5 (8)»
9. отклик: **no** — Online panel with no number of invited people or response rate; no non-response handling beyond age/sex weighting — Materials and methods, Procedure — «Individuals from this panel were invited to participate in the present study.»

Правки:
- 

Проверено: да

---

## ST015 · Adenigba 2024 · International Journal of Research Publication and Reviews

Основной отчёт R2226: [текст](../../fulltext/text/R2226.txt) · [PDF](../../fulltext/pdf/R2226.pdf) — «Sports Betting among the Catholic Youths of Ota deanery in Abeokuta Diocese» — [DOI](https://doi.org/10.55248/gengpi.5.0424.1015)
Не выписано ИИ: Qualitative interview sample (4 youths, 3 priests, 2 parents): not a prevalence sample and has no problem-gambling measurement. No treatment or help-seeking samples were included.
Расхождения в тексте: The target population is given as 1,918 youths in the abstract but 1,910 in the methods. The abstract describes a sample of 331 but does not say that only 171 completed the questionnaire (results and limitations). Table 1 counts match their percentages (53/171 = 31.0, 12/171 = 7.0, 79/171 = 46.2, 27/171 = 15.8). The 69% betting prevalence equals PGSI>=1 (118/171), so betting is inferred from the PGSI score instead of a separate participation question. In Table 2, item 2 is printed as 63.5% but 108/171 = 63.2%. The discussion's item percentages are consistent with Table 2 (chasing losses 29.8 + 14.0 + 4.7 = 48.5%). The conclusion's 'moderate level of sports betting activity' conflicts with the headline 69%. 'Priest 5' is quoted, but only 3 priests are listed.
Заметка ИИ: Eligibility is doubtful. No separate sports-betting participation question is reported, so the denominator of sports bettors is unknown. The estimates use n = 171, as printed. The notes give the alternative of 118 implied bettors (PGSI>=1). The reviewer should decide whether to include the sample and which denominator to use.

### ST015-1 · Catholic youths (CYON), Ota Deanery, Abeokuta Diocese, Nigeria, ~2023-2024, n=171 PGSI respondents
Отчёты: R2226 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all respondents (bettors and non-bettors not separated) | PGSI · PGSI 0 | **below** | **53 / 171** | 31.0 | Page 4, Table 1 | «Non 53 31.0» |
| E2 | all respondents (bettors and non-bettors not separated) | PGSI · PGSI 1-2 | **L1** | **12 / 171** | 7.0 | Page 4, Table 1 | «Low Level 12 7.0» |
| E3 | all respondents (bettors and non-bettors not separated) | PGSI · PGSI 3-7 | **L2** | **79 / 171** | 46.2 | Page 4, Table 1 | «Moderate Level 79 46.2» |
| E4 | all respondents (bettors and non-bettors not separated) | PGSI · PGSI>=8 | **L3** | **27 / 171** | 15.8 | Page 4, Table 1 and text | «Problem Gambling 27 15.8 ... a small minority (15.8%) have problem gambling» |
| E5 | all respondents (bettors and non-bettors not separated) | PGSI · PGSI>=1 | **L1** | **118 / 171** | 69.0 | Page 4, text under Table 1 | «(69.0%) show low to problematic gambling» |

- E1: cumulative: no; источник порога: standard; правило: PGSI row; score 0 = below; у авторов: «Non»; главная у авторов: no; период: past 12 months; заметка: The authors treat PGSI 0 as not betting (100 - 31 = 69% betting), so this category probably mixes non-bettors with non-problem bettors.
- E2: cumulative: no; источник порога: standard; правило: PGSI row; 1-2 band starts at L1; у авторов: «Low Level»; главная у авторов: no; период: past 12 months; заметка: Denominator is all 171 respondents. On the alternative denominator of 118 implied bettors: 12/118.
- E3: cumulative: no; источник порога: standard; правило: PGSI row; 3-7 band starts at L2; у авторов: «Moderate Level / moderate risk bettors»; главная у авторов: no; период: past 12 months; заметка: Denominator is all 171 respondents. On the alternative denominator of 118 implied bettors: 79/118.
- E4: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ = L3; у авторов: «Problem Gambling»; главная у авторов: yes; период: past 12 months; заметка: This is the authors' headline estimate ('around 15% ... problem betting'), with all respondents as the denominator. On the alternative denominator of 118 implied bettors: 27/118 = 22.9%.
- E5: cumulative: yes; источник порога: standard; правило: PGSI row; >=1 = L1; у авторов: «low to problematic gambling (interpreted by authors as engaging in sports betti…»; главная у авторов: no; период: past 12 months; **расчёт: Study reports 69.0%; 69.0% x 171 = 118.0 -> 118 (= 12 + 79 + 27 in Table 1)**; заметка: The authors use this cumulative figure as the prevalence of sports betting, not as a problem-gambling estimate.

**Ключевые поля выборки:**
- **n_bettors: NR** — Page 4, Table 1 — «Total 171 100.0»
- **sample_type: rep_survey_subsample** — Page 1, Abstract — «a simple random sample of 331 participants was drawn from a broader target demographic of 1,918 youths for the quantitative strand»
- **sampling: probability** — Page 1, Abstract — «a simple random sample of 331 participants was drawn from a broader target demographic of 1,918 youths»
- **betting_period: NR** — Page 3, Results — «The information was gotten through Section B of the questionnaire, which is the Problem Gambling Severity Index (PGSI)»

**Остальные поля:**
- parent_population: Catholic youths (CYON members) aged 15-35 of Ota Deanery, Abeokuta Diocese, Nigeria (target population 1,910/1,918) — Page 3, Methodology — «The population targeted comprised 1,910 individuals, as confirmed by the Dean of Ota Deanery, encompassing a demographically diverse group of youths aged 15-35…»
- min_frequency: NR — Page 3, Results — «The first objective of the research was to assess the prevalence of sports betting among the respondents.»
- country: NGA — Page 1, Abstract — «Catholic youths within Ota deanery of Abeokuta Diocese, Nigeria»
- subnational: Ota Deanery, Abeokuta Diocese — Page 1, Abstract — «Catholic youths within Ota deanery of Abeokuta Diocese, Nigeria»
- data_years: NR — Page 5, Results (qualitative) — «(Interview, February 16, 2024)»
- design: cross-sectional — Page 3, Methodology — «an initial quantitative phase using surveys to determine sports betting prevalence, followed by a qualitative phase involving semi-guided interviews»
- gambling_disclosed: NR — Page 3, Methodology — «an initial quantitative phase using surveys to determine sports betting prevalence»
- betting_mode: NR — NA
- pct_online: NR — NA
- pct_inplay: NR — NA
- pct_dfs: NR — NA
- pct_esports: NR — NA
- sports_lottery: unclear — Page 1, Introduction — «Once limited to pool betting, the country has seen a shift towards a more diverse sports betting scene with the advent of sports lotteries in the 1990s»
- mixed_race: no — Page 4, Table 2 — «Descriptive statistics of Youths' responses to Sports Betting Scale»
- legal_status: NR — Page 1, Introduction — «Nigeria presents an intriguing case of historical and contemporary betting culture.»
- n_invited: 331 — Page 1, Abstract; Page 7, Limitations — «Given the sample participants of 171 from the sample size of 331»
- n_responded: 171 — Page 3, Results — «Among the 171 youth participants who completed the questionnaire, a majority were male (65.5%).»
- response_rate: 51.7 — Page 7, Limitations (calculated) — «Given the sample participants of 171 from the sample size of 331»
- age_mean: NR — Page 3, Results — «grouping the ages into four age brackets: 15 – 20, 21 – 25, 26 – 30 and 31 – 35»
- age_sd: NR — NA
- age_min: 15 — Page 3, Methodology — «youths aged 15-35 years»
- age_max: 35 — Page 3, Methodology — «youths aged 15-35 years»
- age_group: mixed — Page 3, Methodology — «youths aged 15-35 years»
- pct_male: 65.5 — Page 3, Results — «Among the 171 youth participants who completed the questionnaire, a majority were male (65.5%).»
- mode: NR — Page 3, Results — «As of January 2023, the most active WhatsApp users are men.»
- weights: no — Page 3, Methodology — «Data from the surveys were analyzed descriptively with tables»
- instruments: PGSI (9 items, 0-3 scoring; language version not stated, items printed in English) — Page 3, Results — «Problem Gambling Severity Index (PGSI), comprising nine questions with a self-reporting four-point Likert scale format (0: "never", 1: "sometimes", 2: "most of…»
- instrument_validated_in_language: yes — Page 3, Validity and reliability of Instrument — «The PGSI's reliability and validity were established through confirmatory factor analysis... Cronbach's alpha confirmed the scale's reliability at 0.79»
- industry_funding: NR — NA
- funding_coi: NR (no funding or conflict-of-interest statement) — NA
- pub_status: journal — Page 1, header — «International Journal of Research Publication and Reviews, Vol 5, no 4, pp 3337-3345 April 2024»
- language: English — Full text — «Sports Betting among the Catholic Youths of Ota deanery in Abeokuta Diocese»
- notes: Sports bettors are not identified separately. The PGSI was given to all 171 respondents, and the authors' 69% 'sports betting prevalence' equals PGSI>=1 (12 + 79 + 27 = 118). The estimates use all 171 respondents as n, as printed in Table 1. On the alternative denominator of 118 implied bettors: PGSI 1-2 = 12/118, 3-7 = 79/118, 8+ = 27/118 (22.9%). Age and sex describe all 171 respondents; age range 15-35 is from the target population. Mode is not stated; a WhatsApp remark suggests online distribution. Survey dates are not stated (interviews February 2024). Instrument validation in Nigeria/En…

**Риск смещения (JBI):**
1. рамка выборки: **unclear** — Target population size was confirmed by the Dean, but the paper does not say whether a membership list was used as the frame. — Page 3, Methodology — «The population targeted comprised 1,910 individuals, as confirmed by the Dean of Ota Deanery»
2. способ отбора: **yes** — The authors state simple random sampling but do not describe the procedure; a WhatsApp remark suggests online distribution. — Page 1, Abstract — «a simple random sample of 331 participants was drawn from a broader target demographic of 1,918 youths»
3. размер выборки: **no** — 171 respondents in total (118 if bettors are taken as PGSI>=1), below 385. — Page 4, Table 1 — «Total 171 100.0»
4. описание выборки и условий: **unclear** — Sex, setting, country and age brackets are reported; dates of the survey are not. — Page 3, Results — «Among the 171 youth participants who completed the questionnaire, a majority were male (65.5%).»
5. охват (пропуски): **yes** — All 171 respondents are classified on the PGSI in Table 1; no missing data are apparent. — Page 4, Table 1 — «Total 171 100.0»
6. валидность определения случая: **yes** — PGSI with standard 0-3 scoring and categories, primary threshold 8+; the language version is not stated (items printed in English). — Page 3, Results — «8 or more suggests Problem gambling with negative consequences and a possible loss of control»
7. единое надёжное измерение: **yes** — Same PGSI for all respondents; alpha 0.79 reported; administration mode not described. — Page 3, Validity and reliability — «Cronbach's alpha confirmed the scale's reliability at 0.79»
8. статистика (числитель и знаменатель): **no** — Sports bettors are never identified separately. The denominator is all 171 youths, and betting prevalence is inferred from PGSI>=1, which is circular. — Page 4, text under Table 1 — «(69.0%) show low to problematic gambling»
9. отклик: **no** — 171/331 = 51.7% response; non-response not handled. — Page 7, Limitations — «Given the sample participants of 171 from the sample size of 331»

Правки:
- 

Проверено: да

---

## ST016 · Adu-Akoh 2024 · Psychology

Основной отчёт R2227: [текст](../../fulltext/text/R2227.txt) · [PDF](../../fulltext/pdf/R2227.pdf) — «Sports Betting: Problem Gambling Correlates among Problem Gambling Severity Index Sub-Types of University Students» — [DOI](https://doi.org/10.4236/psych.2024.156057)
Расхождения в тексте: Sex: the text says males n=247, 74.5% and females 104, 29.6%, but Table 2 gives 70.4% males; the table value (70.4) is used. Betting frequency in Table 4 section 1 sums to 166 (14+27+12+52+44+17), and with the 186 non-responses that makes 352, not 351. Sections 2 (37+49+79) and 3 (1+6+23+26+44+65) each sum to 165, which equals 351-186; 165 is used as n. The text gives 7.5% for 27/351 (should be 7.7%). Table 3 percentages use 351 as denominator, although the paper describes all 351 as 'students' sports bettors' (e.g., Table 5 n=351). The authors claim population weights but report unweighted counts.
Заметка ИИ: The main uncertainty is the denominator. The PGSI categories are printed for all 351 respondents, but 186 said they do not bet. Estimates are derived for the 165 bettors, on the assumption that all non-bettors fall in the PGSI-0 group. The printed values are given in each estimate's note.

### ST016-1 · University of Cape Coast level-400 students who bet on sports, Ghana, 2020 (n=351 surveyed; ~165 past-year sports bettors)
Отчёты: R2227 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | PGSI · PGSI 0 | **below** | **3 / 165** | 1.8 | Page 13, Tables 3 and 4 | «Non-Problem Gambler 189 53.8 ... No response 186 53.0» |
| E2 | all | PGSI · PGSI 1-2 | **L1** | **10 / 165** | 6.1 | Page 13, Table 3 | «Low-risk Gambler 10 2.8» |
| E3 | all | PGSI · PGSI 3-7 | **L2** | **51 / 165** | 30.9 | Page 13, Table 3 | «Moderate risk Gambler 51 14.5» |
| E4 | all | PGSI · PGSI>=8 | **L3** | **101 / 165** | 61.2 | Page 12, 5.1; Page 13, Table 3 | «More than one-fourth of the participants were problem gamblers (n = 101, 28.8%).» |

- E1: cumulative: no; источник порога: standard; правило: PGSI row; 0 = below; у авторов: «Non-Problem Gambler»; главная у авторов: no; период: past 12 months; **расчёт: 189 non-problem (Table 3) - 186 non-bettors (Table 4 no response) = 3; n = 351 - 186 = 165**; заметка: Printed: 189/351 (53.8%), which includes non-bettors. Assumes all 186 non-bettors scored 0.
- E2: cumulative: no; источник порога: standard; правило: PGSI row; 1-2 band starts at L1; у авторов: «Low-risk Gambler»; главная у авторов: no; период: past 12 months; **расчёт: n = 351 respondents - 186 non-bettors = 165**; заметка: Printed denominator 351 (2.8%).
- E3: cumulative: no; источник порога: standard; правило: PGSI row; 3-7 band starts at L2; у авторов: «Moderate risk Gambler»; главная у авторов: no; период: past 12 months; **расчёт: n = 351 respondents - 186 non-bettors = 165**; заметка: Printed denominator 351 (14.5%).
- E4: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ = L3; у авторов: «Problem Gambler»; главная у авторов: yes; период: past 12 months; **расчёт: n = 351 respondents - 186 non-bettors = 165**; заметка: The authors give 28.8% of all 351 respondents. With the 165 bettors as denominator it is 61.2%. Reviewer should confirm the denominator.

**Ключевые поля выборки:**
- **n_bettors: 165** — Page 13, Table 4 — «No response 186 53.0 ... 53.0% of the participant did not respond to the question because they do not bet.»
- **sample_type: students** — Page 8, 4.2 Participants — «The accessible participants were all undergraduate students of level 400 of four Colleges of the University of Cape Coast (UCC), Ghana. There were 4172 level 400 students enrolled.»
- **sampling: probability** — Page 10, 4.4 Data Collection Technique — «The researchers further used a disproportionate stratified sampling technique to draw from each college the number required ... Lastly, individual participants from the sample were randomly selected to attend the questionnaires.»
- **betting_period: past 12 months** — Page 12, Results 5.1 — «Table 4 shows students' involvement in sports betting in the past 12 months.»

**Остальные поля:**
- parent_population: Level-400 (final-year) undergraduate students of four colleges of the University of Cape Coast, Ghana (4172 enrolled) — Page 8, 4.2 Participants — «There were 4172 level 400 students enrolled.»
- min_frequency: none — Page 13, Table 4 — «"5 - 10 times/year" 14 4.0»
- country: GHA — Page 8, 4.2 Participants — «all undergraduate students of level 400 of four Colleges of the University of Cape Coast (UCC), Ghana»
- subnational: Cape Coast (University of Cape Coast) — Page 8, 4.2 Participants — «four Colleges of the University of Cape Coast (UCC), Ghana»
- data_years: 2020 — Page 11, Table 1 source; Page 12, Table 2 source — «Source: Student Record Section of UCC (2019); Field survey (2020).»
- design: cross-sectional — Page 8, 4.1 Research Design — «The descriptive survey design was used in this study.»
- gambling_disclosed: NR — Page 8, 4.2 — «The participants were informed of the study so that they knew exactly what they would be asked to do. This was done by providing the consent information on the…»
- betting_mode: NR — Page 3 — «several licenced operators throughout the country began offering online sports betting, as well as their brick-and-mortar corner shops.»
- pct_online: NR — Full text — «NR»
- pct_inplay: NR — Full text — «NR»
- pct_dfs: NR — Full text — «NR»
- pct_esports: NR — Full text — «NR»
- sports_lottery: no — Page 2 — «For this study, as stated earlier, gambling was exclusive to sports betting.»
- mixed_race: no — Page 2 — «problem gamblers and non-gamblers were exclusively captured in the context of sports betting, and no other forms of gambling were considered.»
- legal_status: regulated legal market — Page 3, 2. Empirical Review — «In Ghana, the Ghana Gaming Commission (GGC) is fully legal and regulated. The GGC is responsible for the registration of casinos and operators for sports betti…»
- n_invited: 351 — Page 11, Table 1 — «Expected no. of samples from each college ... Total 351»
- n_responded: 351 — Page 12, Table 2 — «Source: Field survey (2020), N = 351.»
- response_rate: NR — Page 10, 4.4 — «To get a high rate of returns, participants were given ample time to attend to the questionnaire.»
- age_mean: NR — Page 12, Table 2 — «20 - 25 years 289 82.3; 26 years and above 62 17.7»
- age_sd: NR — Page 12, Table 2 — «NR»
- age_min: 20 — Page 1, Abstract — «The sample was made up of both males and females who were at least 20 years old.»
- age_max: NR — Page 12, Table 2 — «26 years and above 62 17.7»
- age_group: adults — Page 1, Abstract — «who were at least 20 years old»
- pct_male: 70.4 — Page 12, Table 2 — «Males 247 70.4»
- mode: NR — Page 8-10 — «providing the consent information on the first page of the questionnaire ... participants were given ample time to attend to the questionnaire.»
- weights: no — Page 10, 4.4; Page 13, Table 3 — «the population composition was used as weights to compensate for the disproportionality in the sample»
- instruments: Canadian Problem Gambling Index (CPGI) incl. PGSI, English (unaltered) — Page 9, 4.3 Instrument — «The Canadian Problem Gambling Index (CPGI) questionnaire was adopted for data collection. Thus, no part of the instrument or its scoring format was altered.»
- instrument_validated_in_language: yes — Page 9, 4.3 — «As part of the development of the CPGI, Ferris and Wynne (2001) carried out pilot testing in a population sample (n = 143). These tests revealed good internal …»
- industry_funding: NR — Page 24 — «Conflicts of Interest The authors declare no conflicts of interest.»
- funding_coi: Funding not reported; authors declare no conflicts of interest — Page 24 — «The authors declare no conflicts of interest.»
- pub_status: journal — Page 1 — «Psychology, 2024, 15, 947-973 ... DOI: 10.4236/psych.2024.156057»
- language: English — Full text — «Sports Betting: Problem Gambling Correlates among Problem Gambling Severity Index Sub-Types of University Students»
- notes: Sex and age describe all 351 respondents (not just bettors). Table 3 PGSI categories are printed for all 351 respondents, but Table 4 shows 186 (53.0%) did not answer the betting items 'because they do not bet'. Non-gamblers skip most of the CPGI (p.2-3), so they would score PGSI 0 and fall into the non-problem group (189). Sports bettors are therefore taken as 351-186=165, matching Table 4 sections 2 and 3 (sum 165). The authors say population weights were used, but Table 3 counts are unweighted (raw/351). Probable data overlap with Adu-Akoh & Kwarteng-Nantwi (2023, J Educ Pract) and Kwarten…

**Риск смещения (JBI):**
1. рамка выборки: **no** — The frame covers only final-year (level 400) students in four colleges, not all UCC students who bet. — Page 8, 4.2 — «The accessible participants were all undergraduate students of level 400 of four Colleges»
2. способ отбора: **yes** — Disproportionate stratified sampling by college with random selection of individuals (one college undersampled because of fieldwork). — Page 10, 4.4 — «individual participants from the sample were randomly selected to attend the questionnaires»
3. размер выборки: **no** — About 165 sports bettors (351 respondents in total), below 385. — Page 13, Table 4 — «No response 186 53.0»
4. описание выборки и условий: **yes** — Age bands, sex, setting, country and year (2020) are reported. — Page 12, Table 2 — «Females 104 29.6 Males 247 70.4 ... Source: Field survey (2020), N = 351.»
5. охват (пропуски): **unclear** — Missing PGSI data among bettors not reported; the 186 non-responses are attributed to not betting. — Page 12 — «53.0% of the participant did not respond to the question because they do not bet.»
6. валидность определения случая: **yes** — Unaltered English PGSI with standard 8+ threshold. — Page 9, 4.3.1 — «0 = non-problem gambler, 1 - 2 = low-risk gambler, 3 - 7 = moderate-risk gambler 8+ = problem gambler»
7. единое надёжное измерение: **yes** — Same questionnaire for everyone; reliability reported (alpha .81 / .84). — Page 9, 4.3 — «The Canadian Problem Gambling Index on a whole recorded a Cronbach alpha value of .81.»
8. статистика (числитель и знаменатель): **no** — Prevalence is printed with all 351 respondents (incl. non-bettors) as denominator; no CI; the claimed weights are not applied to the prevalence. — Page 13, Table 3 — «Problem Gambler 101 28.8 Total 351 100.0»
9. отклик: **unclear** — Response rate not reported. — Page 10, 4.4 — «To get a high rate of returns, participants were given ample time to attend to the questionnaire.»

Правки:
- 

Проверено: да

---

## ST017 · Bibert 2024 · Journal of Emerging Sport Studies

Основной отчёт R2271: [текст](../../fulltext/text/R2271.txt) · [PDF](../../fulltext/pdf/R2271.pdf) — «Profiling the Esports Bettor» — [DOI](https://doi.org/10.26522/jess.v10i.4544)
Не выписано ИИ: Real-life sports bettors (past 4 months; Table 10: 97 non-esports bettors + 64 esports bettors = 161) were not extracted as a separate sample. PGSI results are not reported by sports betting status, so no prevalence can be derived, and 64 of them overlap with the esports bettor sample. Non-esports bettors (n=639) are not eligible. No treatment or help-seeking samples.
Расхождения в тексте: The header of Table 11 says 'PGSI Status (N = 718)', but its columns sum to 604 + 71 = 675. Esports bettors number 79 in the Sample section and Tables 2 and 10, but 88 in Table 7 (video game frequency), 62 (spectatorship), 61 (gender) and 69 in Tables 8 and 12. The PGSI moderate-risk band is '3-8' in the text (p.10) and '3-7' in Table 5; problem gambling is '8 or more' in the text and '> 8' in Table 5. The text gives gender χ2(1)=1.977, p=.16; Table 7 gives χ2(1)=2.574, p=.11. The text gives video game frequency χ2(7)=14.342, p<.05; Table 7 gives χ2(5)=4.530, p<.48. The value χ2=14.342 is repeated for every gambling activity in the RQ2 text, whereas Table 10 gives different values (e.g., 175.17 for sports betting). The t-test is t(668)=3.14 in the text and t(645)=2.62 in Table 8. The esports bettor reference period is given as '15 months prior' in the Sample section and as 'past year (2…
Заметка ИИ: One eligible sample: esports bettors (esports betting counts as sports betting) within an online convenience survey of video game consumers. The PGSI time frame, the country and funding are not reported.

### ST017-1 · Esports bettors among Dutch-speaking European adult video game consumers, online convenience survey, 2020 (n=79; PGSI n=71)
Отчёты: R2271 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | PGSI · PGSI 0 | **below** | **27 / 71** | 38.0 | Page 16, Table 11 | «PGSI Status (N = 718) ... Esports bettors N (71) % ... Non-problematic 510 84.44 27 38.03» |
| E2 | all | PGSI · PGSI 1-2 | **L1** | **19 / 71** | 26.8 | Page 16, Table 11 | «Low-risk 58 9.60 19 26.76» |
| E3 | all | PGSI · PGSI 3-7 | **L2** | **17 / 71** | 23.9 | Page 16, Table 11; Page 11, Table 5 D7 | «Moderate-risk 27 4.47 17 23.94» |
| E4 | all | PGSI · PGSI>=8 | **L3** | **8 / 71** | 11.3 | Page 16, Table 11; Pages 9-10, Measures | «Problem gambler 9 1.49 8 11.27» |

- E1: cumulative: no; источник порога: standard; правило: PGSI row; score 0 is below L1; у авторов: «non-problematic gambler»; главная у авторов: no; период: NR; заметка: PGSI missing for 8 of 79 esports bettors.
- E2: cumulative: no; источник порога: standard; правило: PGSI row; 1-2 band starts at L1; у авторов: «low-risk gambler»; главная у авторов: no; период: NR
- E3: cumulative: no; источник порога: standard; правило: PGSI row; 3-7 band starts at L2; у авторов: «moderate-risk gambler»; главная у авторов: no; период: NR; заметка: Text on p.10 gives moderate risk as 'score = 3-8'; Table 5 gives '3-7 (moderate-risk)'. Coded as the standard 3-7.
- E4: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ is L3; у авторов: «high-risk/problem gambler»; главная у авторов: yes; период: NR; заметка: Table 5 writes '> 8 (problem gambler)'; the Measures text says '8 or more'. Coded as >=8. PGSI is used as a covariate; this is the only problem-gambling estimate for esports bettors.

**Ключевые поля выборки:**
- **n_bettors: 71** — Page 16, Table 11 — «PGSI Status (N = 718) ... Esports bettors N (71)»
- **sample_type: gamblers_survey_subsample** — Page 6, Sample — «had played and/or spectated at least one esports game, and who had ever (n = 79) or never (n = 639) bet on esports within a timeframe of 15 months prior to the survey.»
- **sampling: convenience** — Page 20, Limitations — «The survey was conducted using a convenience sample of Dutch-speaking adults, who were recruited after repeatedly contacting several video gaming and gambling communities online.»
- **betting_period: NR** — Page 6, Sample; Page 8, Measures — «Possible answers were 'in the past year' (2020) (allocated to group 1), 'before 2020' (allocated to group 1 if after 2017), 'never' (allocated to group 2)»

**Остальные поля:**
- parent_population: Dutch-speaking European adults (18+) who play and/or spectate esports video games, recruited via online video game and gambling communities — Page 6, Research design and Sample — «Specific video game and gambling communities within these platforms were targeted several times with the consent of their respective administrators»
- min_frequency: none — Page 8, Measures — «participants could indicate whether and, if so, when they had bet on esports»
- country: NR — Page 1, Abstract; Page 6, footnote 3 — «we therefore investigated the esports betting profile and motivations of Dutch-speaking, European adults playing or watching video games.»
- subnational: NR — Page 7, Sample — «they are proportionally similar and representative for the region in which the study was conducted»
- data_years: 2020 — Page 6, Research design — «the final survey was sent out between 11 March, 2020 and 10 April, 2020 via the following online media channels: Facebook, Twitter, Reddit, and Discord.»
- design: cross-sectional — Page 1, Abstract — «In this cross-sectional online survey study»
- gambling_disclosed: yes — Page 6, Research design — «An online Dutch survey about the consumption of esports and legalized gambling products among video game consumers ... the first part of the survey contained a…»
- betting_mode: NR — Page 7, Sample — «a majority reported to bet with real money (N = 57), often using one of three international bookmakers as their single betting venue (i.e., Unibet, Betway, Bwi…»
- pct_online: NR — NA — «NR»
- pct_inplay: NR — NA — «NR»
- pct_dfs: NR — NA — «NR»
- pct_esports: all — Page 6, Sample — «who had ever (n = 79) or never (n = 639) bet on esports»
- sports_lottery: no — Page 8, Measures — «one fixed-choice question in which participants could indicate whether and, if so, when they had bet on esports»
- mixed_race: no — Page 8, Measures — «we created a dichotomous variable resulting in one group of esports bettors and one group of non-esports bettors»
- legal_status: NR — NA — «NR»
- n_invited: NR — Page 6, Sample — «Initially, our sample contained 1,013 entries.»
- n_responded: 1013 — Page 6, Sample — «Initially, our sample contained 1,013 entries. We filtered valid from non-valid entries, retaining 718 participants for inclusion in the final sample.»
- response_rate: NR — NA — «NR»
- age_mean: 25.26 — Page 14, Table 8 — «Esports bettors (69) ... 27.44 6.20 25.26 5.89»
- age_sd: 5.89 — Page 14, Table 8 — «Esports bettors (69) ... 27.44 6.20 25.26 5.89»
- age_min: 18 — Page 7, Sample — «Our sample reported to be between 18 and 60 years old (Mage = 27.54; SD = 6.73; N = 661)»
- age_max: 60 — Page 7, Sample — «Our sample reported to be between 18 and 60 years old (Mage = 27.54; SD = 6.73; N = 661)»
- age_group: adults — Page 6, Research design — «Respondents were only directed to the second and third part of the questionnaire if they were over 18 years old»
- pct_male: 96.72 — Page 14, Table 7 (Gender) — «Gender (N = 742) ... Esports bettors N (61) ... Male 59 96.72 ... Non-male 2 3.28»
- mode: online — Page 6, Research design — «An online Dutch survey ... was developed using the survey platform, Qualtrics.»
- weights: no — Page 12, Data analysis; Page 20, Limitations — «The survey was conducted using a convenience sample of Dutch-speaking adults»
- instruments: PGSI (Dutch translation by the authors, translation-back translation) — Page 9, Measures — «We translated the original Problem Gambling Severity Index (PGSI) (Ferris & Wyne, 2001) to Dutch, following a rigorous translation-back translation procedure .…»
- instrument_validated_in_language: no — Page 9, Measures — «We translated the original Problem Gambling Severity Index (PGSI) (Ferris & Wyne, 2001) to Dutch, following a rigorous translation-back translation procedure (…»
- industry_funding: NR — NA — «NR»
- funding_coi: NR: no funding or conflict-of-interest statement in the text — NA — «NR»
- pub_status: journal — Page 1 — «Research Article, Sport Gambling Studies Journal of Emerging Sport Studies Volume 10»
- language: English (survey administered in Dutch) — Page 6, Research design — «An online Dutch survey about the consumption of esports and legalized gambling products among video game consumers was developed»
- notes: Esports betting counted as sports betting (includes betting with skins: 14/79 used skins, 57 real money, 8 crypto; Table 2). Esports bettor definition is inconsistent: '15 months prior' (Sample) vs 'past year (2020)' or 'before 2020 if after 2017' (Measures), so betting_period coded NR. PGSI time frame not stated. Age mean/SD are for esports bettors (n=69, after removal of age outliers); age min/max are for the whole sample (N=661). pct_male is for esports bettors with gender data (59/61). 8 of 79 esports bettors lack PGSI data. Country not stated: 'Dutch-speaking, European'. Belgian help ser…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame is followers of selected video game and gambling communities on social media, not all esports bettors of a population. — Page 6, Research design — «Specific video game and gambling communities within these platforms were targeted several times with the consent of their respective administrators»
2. способ отбора: **no** — Convenience, volunteer opt-in online survey. — Page 20, Limitations — «The survey was conducted using a convenience sample of Dutch-speaking adults»
3. размер выборки: **no** — 71 esports bettors with PGSI data, below 385. — Page 16, Table 11 — «Esports bettors N (71)»
4. описание выборки и условий: **unclear** — Age, sex, setting and dates reported; country not stated explicitly (only 'Dutch-speaking, European'). — Page 1, Abstract; Page 6 — «Dutch-speaking, European adults playing or watching video games»
5. охват (пропуски): **no** — PGSI missing for 8 of 79 esports bettors (10.1%), not handled. — Page 6, Sample; Page 16, Table 11 — «who had ever (n = 79) ... Esports bettors N (71)»
6. валидность определения случая: **no** — PGSI with standard 8+ threshold, but the authors' own Dutch translation has no published validation. — Page 9, Measures — «We translated the original Problem Gambling Severity Index (PGSI) (Ferris & Wyne, 2001) to Dutch, following a rigorous translation-back translation procedure»
7. единое надёжное измерение: **yes** — Same online PGSI for all participants; reliability given (alpha 0.857). PGSI time frame not stated. — Page 9, Measures — «For each respondent, the obtained scale (α = 0.857) resulted in a score ranging from 0 – 27.»
8. статистика (числитель и знаменатель): **yes** — Counts and denominator of esports bettors given (8/71), so a CI can be calculated; unweighted convenience sample. — Page 16, Table 11 — «Problem gambler 9 1.49 8 11.27»
9. отклик: **no** — Open online survey with no denominator of invited people; 1,013 entries, 718 valid. — Page 6, Sample — «Initially, our sample contained 1,013 entries. We filtered valid from non-valid entries, retaining 718 participants»

Правки:
- 

Проверено: да

---

## ST018 · Di Censo 2024 · Journal of gambling studies

Основной отчёт R2361: [текст](../../fulltext/text/R2361.txt) — «Examining the Role of Sports Betting Marketing in Youth Problem Gambling.» — [DOI](https://doi.org/10.1007/s10899-024-10347-x)
Расхождения в тексте: Exclusions: the Participants section says 58 did not meet the criteria and were excluded. The Analytic Strategy says 82 were excluded. 649 - 82 = 567, which matches the analysed sample, so 82 is consistent. The PGSI categories in Table 1 sum to 567 (170+200+129+68). The text says problem gamblers had normative beliefs M = 28.81, but Table 2 gives 26.81; Table 2 is assumed correct. The regression df (F(10,456)) implies about 467 cases with complete data for the regression, but PGSI categories are given for all 567. Eligibility: the abstract says participants 'regularly bet on sports', but the Method criterion is at least one sports bet in the past 12 months.
Заметка ИИ: Single sample. Country is not stated: UK is inferred from 88.4% being born in the UK and spend reported in £, and the reviewer should confirm it. pct_inplay of 61.0 is derived from Table 1: Rarely + Sometimes + Often = 346/567, i.e. 100 - 39.0% Never. Funding comes from the NSW Government's Responsible Gambling Fund, a government fund, so it is coded as not industry funding. Age and sex fields describe the whole analysed sample, which is the same group as the sports bettors.

### ST018-1 · Prolific online panel, young sports bettors aged 18-24 (probably UK), n=567
Отчёты: R2361 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | PGSI · PGSI 0 | **below** | **170 / 567** | 30.0 | Table 1 | «Non-problem / 170 / 30.0» |
| E2 | all | PGSI · PGSI 1-2 | **L1** | **200 / 567** | 35.3 | Table 1 | «Low-risk / 200 / 35.3» |
| E3 | all | PGSI · PGSI 3-7 | **L2** | **129 / 567** | 22.8 | Table 1 | «Moderate-risk / 129 / 22.8» |
| E4 | all | PGSI · PGSI>=8 | **L3** | **68 / 567** | 12.0 | Table 1; Results, Descriptive Statistics | «Problem gambler / 68 / 12.0» |

- E1: cumulative: no; источник порога: standard; правило: PGSI row; score 0 is below L1; у авторов: «Non-problem»; главная у авторов: no; период: NR; заметка: PGSI time frame not stated (standard PGSI is past 12 months)
- E2: cumulative: no; источник порога: standard; правило: PGSI row; 1-2 band starts at L1; у авторов: «Low-risk»; главная у авторов: no; период: NR; заметка: PGSI time frame not stated
- E3: cumulative: no; источник порога: standard; правило: PGSI row; 3-7 band starts at L2; у авторов: «Moderate-risk»; главная у авторов: no; период: NR; заметка: PGSI time frame not stated
- E4: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ = L3; у авторов: «Problem gambler»; главная у авторов: yes; период: NR; заметка: PGSI time frame not stated. The study's aim was regression, not prevalence; this is the descriptive problem-gambler category

**Ключевые поля выборки:**
- **n_bettors: 567** — Table 1; Results — «The study comprised 567 participants aged 18 to 24.»
- **sample_type: bettor_recruited** — Method, Participants — «The eligibility criteria required that individuals be aged between 18 and 24, have participated in sports betting within the past 12 months, and possess an active betting account.»
- **sampling: convenience** — Method, Participants — «Participants were recruited from the online research panel, Prolific.»
- **betting_period: past 12 months** — Method, Participants — «have participated in sports betting within the past 12 months»

**Остальные поля:**
- parent_population: NA — Method, Participants — «The study was exclusively promoted to individuals between 18 and 24 on the Prolific platform.»
- min_frequency: none (at least once in past 12 months; abstract says 'regularly bet on sports') — Analytic Strategy; Abstract — «Participants had to confirm that they had bet on sports at least once in the past year»
- country: NR (probably GBR: 88.4% born in UK, spend reported in £; recruitment country not stated) — Table 1; Results, Descriptive Statistics — «Most participants were born in the UK (88.4%) and reported English as their primary language spoken at home (95.8%).»
- subnational: NA — Method, Participants — «Participants were recruited from the online research panel, Prolific.»
- data_years: NR — Procedure — «approved by the Human Research Ethics Subcommittee of the University of Adelaide's School of Psychology; project number: H-2023/88.»
- design: cross-sectional — Limitations — «Since the current study was cross-sectional in nature, we cannot infer directionality»
- gambling_disclosed: yes — Method, Participants — «We allowed participants to self-select whether they met the remaining inclusion criteria (i.e., bet on sports in the past 12 months and hold an active betting …»
- betting_mode: NR — Method, Participants — «possess an active betting account»
- pct_online: NR — Method — «possess an active betting account»
- pct_inplay: 61.0 — Table 1 — «Participate in live or in-play betting ... Never | 221 | 39.0 ... Rarely | 183 | 32.3 Sometimes | 121 | 21.3 Often | 42 | 7.4»
- pct_dfs: NR — Full text — «NR»
- pct_esports: NR — Full text — «NR»
- sports_lottery: unclear — Full text — «have participated in sports betting within the past 12 months»
- mixed_race: no — Method, Participants — «have participated in sports betting within the past 12 months»
- legal_status: NR — Full text — «NR»
- n_invited: NR — Method, Participants — «A total of 649 participants agreed to take part in the study.»
- n_responded: 649 — Method, Participants — «A total of 649 participants agreed to take part in the study.»
- response_rate: NR — Method — «A total of 649 participants agreed to take part in the study.»
- age_mean: NR — Results — «The study comprised 567 participants aged 18 to 24.»
- age_sd: NR — Results — «The study comprised 567 participants aged 18 to 24.»
- age_min: 18 — Results — «The study comprised 567 participants aged 18 to 24.»
- age_max: 24 — Results — «The study comprised 567 participants aged 18 to 24.»
- age_group: adults — Abstract — «We recruited 567 participants (53.1% male) aged 18–24 years from an online research panel.»
- pct_male: 53.1 — Table 1 — «Male | 301 | 53.1»
- mode: online — Procedure — «The survey was hosted on Qualtrics.»
- weights: no — Analytic Strategy — «We addressed the non-normal distribution of the dependent variable, the PGSI, by employing a logarithmic (+ 1) transformation»
- instruments: PGSI (English) — Measures, Problem Gambling Score — «We used the Problem Gambling Severity Index (PGSI) to determine participants' problem gambling scores (Ferris & Wynne, 2001).»
- instrument_validated_in_language: yes — Measures, Problem Gambling Score — «We used the Problem Gambling Severity Index (PGSI) to determine participants' problem gambling scores (Ferris & Wynne, 2001).»
- industry_funding: no — Funding — «funded by the NSW Government's Responsible Gambling Fund, and supported by the NSW Office of Responsible Gambling.»
- funding_coi: PhD scholarship funded by NSW Government's Responsible Gambling Fund, supported by NSW Office of Responsible Gambling; authors declare no competing interests — Funding; Conflict of interest — «This research was conducted as part of a PhD scholarship, awarded to Gianluca Di Censo, funded by the NSW Government's Responsible Gambling Fund ... The author…»
- pub_status: journal — Header — «Journal of gambling studies; DOI: 10.1007/s10899-024-10347-x»
- language: English — Full text — «Examining the Role of Sports Betting Marketing in Youth Problem Gambling»
- notes: Age and sex fields describe the whole analysed sample (n=567), and all of them are sports bettors. Country is not stated: UK is inferred from 88.4% being born in the UK and spend reported in £, with an Australian university as sponsor. Data collection years are not reported; ethics approval number is H-2023/88. 649 were recruited and 82 excluded as ineligible (the text also gives 58). pct_inplay of 61.0 is derived from Table 1 as 100 - 39.0% who never bet in-play (346/567). The PGSI time frame is not stated.

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame is volunteers on the Prolific panel, which covers only part of young sports bettors — Method, Participants — «Participants were recruited from the online research panel, Prolific.»
2. способ отбора: **no** — Non-probability, self-selected online panel — Method, Participants — «We allowed participants to self-select whether they met the remaining inclusion criteria»
3. размер выборки: **yes** — 567 sports bettors (>=385) — Table 1 — «Total | 567 | 100»
4. описание выборки и условий: **no** — Age, sex and setting reported; recruitment country and dates of data collection not stated — Results; Table 1 — «The study comprised 567 participants aged 18 to 24. The sample consisted of slightly more males (53.1%) than females.»
5. охват (пропуски): **yes** — PGSI categories account for all 567 analysed bettors (170+200+129+68=567) — Table 1 — «Non-problem | 170 | 30.0 Low-risk | 200 | 35.3 Moderate-risk | 129 | 22.8 Problem gambler | 68 | 12.0»
6. валидность определения случая: **yes** — PGSI, original English version, with standard thresholds — Measures, Problem Gambling Score — «non-problem gamblers (score of 0), low-risk gamblers (score of 1–2), moderate-risk gamblers (score of 3–7), and problem gamblers (score of 8 or higher)»
7. единое надёжное измерение: **yes** — Same online PGSI for all participants; reliability reported in the sample — Measures, Problem Gambling Score — «In our sample, the measure showed a high level of internal consistency, with a Cronbach's alpha of 0.89.»
8. статистика (числитель и знаменатель): **yes** — Counts and denominator are clear, so a CI can be calculated; weights not needed for this design — Table 1 — «Problem gambler | 68 | 12.0 ... Total | 567 | 100»
9. отклик: **no** — Online panel with no denominator of invited people and no handling of non-response — Method, Participants — «A total of 649 participants agreed to take part in the study.»

Правки:
- 

Проверено: да

---

## ST019 · Doblignon 2024 · European Journal of Social Sciences Studies

Основной отчёт R2366: [текст](../../fulltext/text/R2366.txt) · [PDF](../../fulltext/pdf/R2366.pdf) — «TAILLE DE LA FAMILLE, STATUT DE SCOLARISATION ET NIVEAU D’ADDICTION AUX PARIS SPORTIFS CHEZ DES ABIDJANAIS, CÔTE D’IVOIRE / FAMILY SIZE, EDUCATIONAL STATUS AND…» — [DOI](https://doi.org/10.46827/ejsss.v10i4.1838)
Расхождения в тексте: The 'excessive' (ICJE 8+) total out of 170 differs by table. Table 2 gives 76 excessive and 94 at risk. Table 3 gives 90 and 80. Table 4 gives 86 (19+12+07+48) and 84 (33+15+17+19). The schooling margins also disagree: Table 1 has scolarisés 76 and déscolarisés 94, against 74 and 96 in Table 3. Family-size subtotals implied by Table 4 do not match Table 2: small families 31 vs 23 excessive, large families 55 vs 53. The Table 4 row totals match Table 1. Table 2 was used for the whole-sample estimate, and the alternatives are given in the estimate notes. The Discussion mentions adolescents, but the Methods say 18-35.
Заметка ИИ: There is one sample, recruited at venues and by snowball, using the ICJE (French CPGI), coded as PGSI. Results are given only as counts, and those counts are internally inconsistent. Breakdowns by family size and schooling status (Tables 2-4) were not extracted because they are not sex, age or betting-mode subgroups.

### ST019-1 · Sportcash bettors at LONACI points of sale, Yopougon (Abidjan), Côte d'Ivoire, 2018, n=170 men
Отчёты: R2366 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | PGSI · PGSI>=8 (ICJE 8-27) | **L3** | **76 / 170** | 44.7 | Page 6, Tableau 2 | «Pratique à risque / Pratique excessive / Total ... Total 94 76 170» |
| E2 | all | PGSI · PGSI 1-7 (ICJE 1-7) | **L1** | **94 / 170** | 55.3 | Page 6, 2.2 and Tableau 2 | «nous combinons les deux catégories en une seule (à risque) ... de 1 à 7 pour les joueurs à risque ... Total 94 76 170» |

- E1: cumulative: yes; источник порога: standard; правило: PGSI row; ICJE = French CPGI with 0-3 item scoring; 8+ starts at L3; у авторов: «pratique excessive / joueurs excessifs»; главная у авторов: yes; период: NR; заметка: Tables disagree: Table 3 gives 90/170 and Table 4 gives 86/170 (19+12+7+48). Table 2 was used as the first reported table; it matches the Table 1 family-size margins. The authors give no percentage, and the ICJE time frame is not stated.
- E2: cumulative: no; источник порога: study's own; правило: PGSI row; band 1-7 (authors merged 1-2 and 3-7) starts at L1; у авторов: «pratique à risque / joueurs à risque»; главная у авторов: no; период: NR; заметка: Table 3 gives 80 and Table 4 gives 84. Scores of 0 are not reported; it is unclear whether anyone scored 0 or whether such respondents were placed in this group.

**Ключевые поля выборки:**
- **n_bettors: 170** — Page 6, Tableau 2 — «Total 94 76 170»
- **sample_type: bettor_recruited** — Page 6, 2.3 — «Pour avoir accès aux parieurs, nous nous rendons dans les points de vente agréés par la LONACI dans les quartiers de Selmer, Niangon Sud, Siporex, Lubrafrique et Jean Paul II. [To reach bettors, we went to LONACI-licensed points of sale in five neighbourhoods…»
- **sampling: snowball** — Page 6, 2.3 — «Etant donné qu'il est souvent difficile d'avoir l'adhésion des joueurs, nous avons adopté la méthode boule de neige. [Because it is often hard to get players to take part, we used the snowball method.]»
- **betting_period: current** — Page 5, 2.1 Participants — «avec une participation aux paris sportifs estimée à au moins un (1) an [with sports-betting participation estimated at at least one (1) year]»

**Остальные поля:**
- parent_population: NA — NA — «NA»
- min_frequency: none stated; entry required at least 1 year of Sportcash sports-betting practice — Page 1, Résumé; Page 5, 2.1 — «comptabilisent au moins un (1) an de pratique du jeu de pari Sportcash [have at least one (1) year of practice of the Sportcash betting game]»
- country: CIV — Page 6, 2.3 Procédure de collecte des données — «La collecte des données a été effectuée dans la commune de Yopougon (Abidjan-Côte d'Ivoire).»
- subnational: Abidjan (commune of Yopougon) — Page 6, 2.3 — «La collecte des données a été effectuée dans la commune de Yopougon (Abidjan-Côte d'Ivoire). [Data were collected in the commune of Yopougon (Abidjan, Côte d'I…»
- data_years: 2018 — Page 5, Tableau 1 source; Page 6, 2.3 — «Source : Données de notre enquête 2018. [Source: our survey data 2018.] ... La passation s'est déroulée sur une période de cinq (5) semaines. [Data collection …»
- design: cross-sectional — Page 10, Discussion — «La présente recherche est une étude corrélationnelle réalisée avec deux variables explicatives. [This research is a correlational study with two explanatory va…»
- gambling_disclosed: NR — Page 6, 2.3 — «nous procédons à une administration individuelle des questionnaires avec les parieurs qui acceptent de participer à l'étude [we administered the questionnaires…»
- betting_mode: NR — Page 6, 2.3 — «nous nous rendons dans les points de vente agréés par la LONACI [we went to LONACI-licensed points of sale]»
- pct_online: NR — NA — «NA»
- pct_inplay: NR — NA — «NA»
- pct_dfs: NR — NA — «NA»
- pct_esports: NR — NA — «NA»
- sports_lottery: unclear — Page 2, Introduction — «la Loterie Nationale de Côte d'Ivoire (LONACI) propose des paris sportifs via l'offre Sportcash depuis 2012 [LONACI has offered sports betting through its Spor…»
- mixed_race: no — Page 5, 2.1 — «L'échantillon de la présente étude est composé de cent-soixante-dix (170) joueurs de paris sportifs [The sample consists of 170 sports bettors]»
- legal_status: NR — Page 2, Introduction — «la Loterie Nationale de Côte d'Ivoire (LONACI) propose des paris sportifs via l'offre Sportcash depuis 2012 [LONACI has offered sports betting through Sportcas…»
- n_invited: NR — NA — «NA»
- n_responded: 170 — Page 5, 2.1; Tableau 1 — «L'échantillon de la présente étude est composé de cent-soixante-dix (170) joueurs de paris sportifs de la commune de Yopougon.»
- response_rate: NR — Page 6, 2.3 — «Etant donné qu'il est souvent difficile d'avoir l'adhésion des joueurs, nous avons adopté la méthode boule de neige.»
- age_mean: NR — NA — «NA»
- age_sd: NR — NA — «NA»
- age_min: 18 — Page 5, 2.1 — «âgés de dix-huit (18) à trente et cinq (35) ans [aged 18 to 35 years]»
- age_max: 35 — Page 5, 2.1 — «âgés de dix-huit (18) à trente et cinq (35) ans [aged 18 to 35 years]»
- age_group: adults — Page 5, 2.1 — «Ils sont tous de sexe masculin et âgés de dix-huit (18) à trente et cinq (35) ans [All are male and aged 18 to 35]»
- pct_male: 100 — Page 5, 2.1 — «Ils sont tous de sexe masculin [They are all male]»
- mode: face-to-face — Page 6, 2.3 — «Sur les lieux, nous procédons à une administration individuelle des questionnaires [On site, we administered the questionnaires individually]»
- weights: no — Page 6, 2.3 — «Ces données sont donc analysées à l'aide du test statistique du khi-carré [The data were analysed with the chi-square test]»
- instruments: ICJE (Indice canadien du jeu excessif = French CPGI/PGSI, 9-item short version, items scored 0-3, total 0-27), French — Page 5-6, 2.2 Instruments de mesure — «l'Indice Canadien du Jeu Excessif (Ferris & Wynne, 2001) a été utilisé ... La version courte que nous utilisons pour cette étude compte neuf (9) items.»
- instrument_validated_in_language: yes — Page 13-14, Bibliographie — «Ferris, J. & Wynne, J. (2001). L'indice canadien du jeu excessif. Ottawa ... Mccready, J. & Adlaf, E. (2006). Rendement et bonification de l'indice canadien du…»
- industry_funding: NR — Page 11, Déclaration de conflit d'intérêts — «Les auteurs ne déclarent aucun conflit d'intérêts [The authors declare no conflicts of interest]»
- funding_coi: Funding not reported; authors declare no conflicts of interest — Page 11 — «The authors declare no conflicts of interest.»
- pub_status: journal — Page 1, header — «European Journal of Social Sciences Studies ... DOI: 10.46827/ejsss.v10i4.1838 ... Volume 10 │ Issue 4 │ 2024»
- language: French — Page 1-15, full text — «TAILLE DE LA FAMILLE, STATUT DE SCOLARISATION ET NIVEAU D'ADDICTION AUX PARIS SPORTIFS CHEZ DES ABIDJANAIS, CÔTE D'IVOIRE»
- notes: Age and sex are for the whole sample (all are bettors): 170 men aged 18-35 with at least 1 year of Sportcash (LONACI) betting, recruited at LONACI points of sale in Yopougon plus snowball referral. The Discussion mentions adolescents, but the Methods say 18-35. Betting mode (online/land) is not reported. The ICJE was split into 1-7 'at risk' and 8-27 'excessive'; scores of 0 are not mentioned. The 'excessive' count differs by table: 76, 90 or 86 of 170 (see consistency_notes). instrument_validated_in_language = yes rests on the cited French ICJE manual and the McCready & Adlaf 2006 French eva…

**Риск смещения (JBI):**
1. рамка выборки: **no** — The frame is LONACI points of sale in 5 neighbourhoods of one commune, which covers only part of Abidjan's sports bettors. — Page 11, Conclusion — «ne concerne que les parieurs d'une contrée de la ville d'Abidjan (Yopougon) [covers only bettors from one area of Abidjan (Yopougon)]»
2. способ отбора: **no** — Volunteers were approached at venues, followed by snowball sampling. — Page 6, 2.3 — «nous avons adopté la méthode boule de neige [we adopted the snowball method]»
3. размер выборки: **no** — n=170 sports bettors, which is below 385. — Page 5, 2.1 — «cent-soixante-dix (170) joueurs de paris sportifs»
4. описание выборки и условий: **yes** — Age range, sex, setting, country and year (2018, over 5 weeks) are reported. — Page 5-6, 2.1, 2.3, Tableau 1 — «Ils sont tous de sexe masculin et âgés de dix-huit (18) à trente et cinq (35) ans ... Source : Données de notre enquête 2018.»
5. охват (пропуски): **unclear** — Missing data are not reported, and the table totals contradict each other (76/90/86 excessive of 170). — Page 6-8, Tableaux 2-4 — «Total 94 76 170 ... Total 80 90 170 ... Total 84 86 170»
6. валидность определения случая: **yes** — French ICJE (CPGI/PGSI) with the standard 8+ threshold; the French developer manual is cited. There is no local validation. — Page 6, 2.2 — «un score à partir de 8 est caractéristique d'une pratique excessive [a score of 8 or more indicates excessive gambling]»
7. единое надёжное измерение: **unclear** — The same instrument and the same individual administration were used for all, but reliability was not reported. — Page 6, 2.3 — «Sur les lieux, nous procédons à une administration individuelle des questionnaires»
8. статистика (числитель и знаменатель): **no** — The numerator of excessive gamblers differs across tables (76, 90, 86 of 170); no prevalence or CI is given. — Page 6-8, Tableaux 2-4 — «Total 94 76 170 ... Total 80 90 170 ... Total 84 86 170»
9. отклик: **no** — Snowball recruitment with no denominator of people approached; the authors note that participation was difficult to obtain. — Page 6, 2.3 — «Etant donné qu'il est souvent difficile d'avoir l'adhésion des joueurs, nous avons adopté la méthode boule de neige.»

Правки:
- 

Проверено: да

---

## ST020 · Hing 2024 · Journal of behavioral addictions

Основной отчёт R2429: [текст](../../fulltext/text/R2429.txt) — «Feature preferences of sports betting platforms: A discrete choice experiment shows why young bettors prefer smartphones.» — [DOI](https://doi.org/10.1556/2006.2023.00073)
⚠ Возможное пересечение (держим раздельно; если видите общие данные — напишите в «Правки»): possible overlap with R2934 (ST024): Both young Australian sports bettors recruited by Qualtrics panels for Hing et al. (April 2021, N = 616; June-September 2021, NSW, N = 267): separate surveys, panel members may overlap
Расхождения в тексте: The PGSI percentages (15.1 + 18.2 + 23.7 + 43.0 = 100.0) agree with N = 616, and the derived counts (93 + 112 + 146 + 265) sum to 616. No table gives PGSI counts, so all counts come from percentages. The supplementary tables (S1 to S4) were not available, so the number of recruits/invited and the screening exclusions could not be checked. The platform figures (72.9% smartphone, etc.) appear to be shares of betting expenditure, not shares of bettors, so pct_online is NR.
Заметка ИИ: Legal status is coded from the mention of Australian-licensed operators versus illegal offshore in-play betting. Sampling is coded convenience because the authors describe purposive Qualtrics panel recruitment without quotas.

### ST020-1 · Young Australian sports/esports/DFS bettors aged 18-29, Qualtrics online panels, April 2021, N=616
Отчёты: R2429 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | PGSI · PGSI 0 | **below** | **93 / 616** | 15.1 | Participant characteristics | «Most respondents were at some risk of gambling problems: 15.1% were non-problem gamblers» |
| E2 | all | PGSI · PGSI 1-2 | **L1** | **112 / 616** | 18.2 | Participant characteristics | «18.2% low risk gamblers» |
| E3 | all | PGSI · PGSI 3-7 | **L2** | **146 / 616** | 23.7 | Participant characteristics | «23.7% moderate risk gamblers» |
| E4 | all | PGSI · PGSI>=8 (8-27) | **L3** | **265 / 616** | 43.0 | Participant characteristics | «43.0% scored in the problem gambling category (mean = 7.3, SD = 6.3, median = 6)» |

- E1: cumulative: no; источник порога: standard; правило: PGSI row; score 0 is below L1; у авторов: «non-problem gamblers»; главная у авторов: no; период: past 12 months; **расчёт: 15.1% x 616 = 93.0 -> 93**; заметка: Sample includes esports-only and DFS-only bettors (85.1% bet on sports at least monthly).
- E2: cumulative: no; источник порога: standard; правило: PGSI row; 1-2 band starts at L1; у авторов: «low risk gamblers»; главная у авторов: no; период: past 12 months; **расчёт: 18.2% x 616 = 112.1 -> 112**
- E3: cumulative: no; источник порога: standard; правило: PGSI row; 3-7 band starts at L2; у авторов: «moderate risk gamblers»; главная у авторов: no; период: past 12 months; **расчёт: 23.7% x 616 = 146.0 -> 146**
- E4: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ starts at L3; у авторов: «problem gambling»; главная у авторов: no; период: past 12 months; **расчёт: 43.0% x 616 = 264.9 -> 265**; заметка: The authors state that the study did not seek to estimate prevalence; the PGSI distribution describes the sample. The derived counts sum to 616.

**Ключевые поля выборки:**
- **n_bettors: 616** — Participant characteristics — «Amongst the 616 respondents, 85.1% bet on sports, 50.5% on esports, and 49.0% on DFS at-least monthly.»
- **sample_type: bettor_recruited** — Methods, Sampling and recruitment — «the study required participants to have bet on sports, esports or DFS at-least monthly in the past year»
- **sampling: convenience** — Methods, Sampling and recruitment — «The study used purposive sampling because obtaining a probability sample was infeasible due to the relatively low prevalence of sports, esports and DFS bettors in the population.»
- **betting_period: past 12 months** — Methods, Sampling and recruitment — «the study required participants to have bet on sports, esports or DFS at-least monthly in the past year»

**Остальные поля:**
- parent_population: NA — NA — «NA»
- min_frequency: at least monthly — Methods, Sampling and recruitment — «required participants to have bet on sports, esports or DFS at-least monthly in the past year»
- country: AUS — Methods, Sampling and recruitment — «Participants were also required to live in Australia, where the funding agency is based.»
- subnational: NA — Methods, Sampling and recruitment — «Qualtrics, an online panel aggregator, recruited survey participants from several panels across Australia»
- data_years: 2021 — Methods, Sampling and recruitment — «recruited survey participants from several panels across Australia during the 15th to 29th of April 2021»
- design: cross-sectional — Methods, Measures — «The survey included a discrete choice experiment (or conjoint study) where participants indicated their preferences amongst different groups of features»
- gambling_disclosed: NR — Methods — «Screening questions: Age in years; residential postcode; and frequency of betting on sports, esports and DFS for money.»
- betting_mode: both — Results, Betting platforms used — «Smartphones were the most used platform for sports betting (72.9%), followed by a computer (12.5%) and land-based venues (7.3%).»
- pct_online: NR — Results, Betting platforms used — «Smartphones were the most used platform for sports betting (72.9%), followed by a computer (12.5%) and land-based venues (7.3%).»
- pct_inplay: NR — NA — «NA»
- pct_dfs: 49.0 — Participant characteristics — «Amongst the 616 respondents, 85.1% bet on sports, 50.5% on esports, and 49.0% on DFS at-least monthly.»
- pct_esports: 50.5 — Participant characteristics — «Amongst the 616 respondents, 85.1% bet on sports, 50.5% on esports, and 49.0% on DFS at-least monthly.»
- sports_lottery: no — Aims — «In this study, sports betting refers to betting on sports, esports and daily fantasy sports (DFS).»
- mixed_race: no — Aims — «In this study, sports betting refers to betting on sports, esports and daily fantasy sports (DFS).»
- legal_status: regulated legal market — Discussion, gambling severity — «can only place in-play bets online with illegal offshore operators as these bets cannot be provided by Australian-licensed operators»
- n_invited: NR — Methods, Sampling and recruitment — «Table S1 in the supplementary materials shows the number of recruits, the screening, eligibility and quality exclusions»
- n_responded: 616 — Methods, Sampling and recruitment — «the completion rate (72.8%) to attain the final sample of N = 616»
- response_rate: 72.8 — Methods, Sampling and recruitment — «the completion rate (72.8%) to attain the final sample of N = 616»
- age_mean: 23.8 — Participant characteristics — «Age ranged from 18 to 29 years with a mean age of 23.8 years (SD = 3.4, median = 24).»
- age_sd: 3.4 — Participant characteristics — «mean age of 23.8 years (SD = 3.4, median = 24)»
- age_min: 18 — Participant characteristics — «Age ranged from 18 to 29 years»
- age_max: 29 — Participant characteristics — «Age ranged from 18 to 29 years»
- age_group: adults — Methods, Sampling and recruitment — «inclusion criteria included being aged 18–29 years»
- pct_male: 33.0 — Participant characteristics — «Of the 616 respondents, 33.0% were men and 67.0% were women.»
- mode: online — Methods, Sampling and recruitment — «Qualtrics, an online panel aggregator, recruited survey participants from several panels across Australia»
- weights: NR — Limitations — «The respondents comprised a non-probability sample.»
- instruments: PGSI (English, past 12 months) — Methods, Measures — «Problem Gambling Severity Index (PGSI; Ferris & Wynne, 2001). The PGSI was administered in relation to the last 12 months.»
- instrument_validated_in_language: yes — Methods, Measures — «The analysis used the validated scoring of 'never' = 0, 'sometimes' = 1, 'most of the time' = 2, and 'almost always' = 3, and the validated cut-off scores»
- industry_funding: no — Funding sources — «Funding for this study was provided by the NSW Government's Responsible Gambling Fund, with support from the NSW Office of Responsible Gambling.»
- funding_coi: NSW Government's Responsible Gambling Fund (NSW Office of Responsible Gambling); authors declare no conflicts of interest — Funding sources; Conflicts of interest — «The authors declare no conflicts of interest in relation to this manuscript.»
- pub_status: journal — Header — «Journal of behavioral addictions; DOI: 10.1556/2006.2023.00073»
- language: English — Full text — «Feature preferences of sports betting platforms: A discrete choice experiment shows why young bettors prefer smartphones»
- notes: The sample is defined as bettors on sports, esports and/or DFS at least monthly in the past 12 months. Only 85.1% bet on sports at least monthly, so the PGSI estimates include esports-only and DFS-only bettors. No PGSI estimate is given for sports bettors only, by sex, or by esports/DFS. Age and sex describe the whole sample of 616 bettors (67% women). Possible overlap with R2934 (ST024): both are samples of young Australian sports bettors recruited through Qualtrics panels for Hing et al. (April 2021, N = 616; June-September 2021, NSW, N = 267). They are separate surveys, but panel members m…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame is members of Qualtrics online panels, which cover only part of young Australian sports bettors. — Methods, Sampling and recruitment — «Qualtrics, an online panel aggregator, recruited survey participants from several panels across Australia»
2. способ отбора: **no** — Purposive non-probability online panel sample. — Methods, Sampling and recruitment — «The study used purposive sampling because obtaining a probability sample was infeasible»
3. размер выборки: **yes** — n = 616 bettors, which is at least 385. — Participant characteristics — «Of the 616 respondents, 33.0% were men and 67.0% were women.»
4. описание выборки и условий: **yes** — Age, sex, setting (online panels), country and dates are all reported. — Participant characteristics; Sampling and recruitment — «Age ranged from 18 to 29 years with a mean age of 23.8 years ... during the 15th to 29th of April 2021»
5. охват (пропуски): **yes** — PGSI category percentages sum to 100% of the 616 analysed; no missing PGSI data reported. Quality exclusions are only in supplementary Table S1. — Participant characteristics — «15.1% were non-problem gamblers, 18.2% low risk gamblers, 23.7% moderate risk gamblers and 43.0% scored in the problem gambling category»
6. валидность определения случая: **yes** — English PGSI with standard scoring and cut-offs (8+ problem gambling). — Methods, Measures — «the validated cut-off scores of non-problem gambling = 0, low risk gambling = 1–2, moderate risk gambling = 3–7, and problem gambling = 8–27»
7. единое надёжное измерение: **unclear** — Same online PGSI and time frame for everyone, but no reliability reported. — Methods, Measures — «The PGSI was administered in relation to the last 12 months.»
8. статистика (числитель и знаменатель): **yes** — Denominator (616) and percentages are clear, so counts and CIs can be calculated; non-probability design, so weights are not expected. — Participant characteristics — «Most respondents were at some risk of gambling problems: 15.1% were non-problem gamblers»
9. отклик: **no** — Online panel with no denominator of invited people in the main text; 72.8% is a completion rate among recruits. — Methods, Sampling and recruitment — «Table S1 ... shows the number of recruits, the screening, eligibility and quality exclusions, and the completion rate (72.8%)»

Правки:
- 

Проверено: да

