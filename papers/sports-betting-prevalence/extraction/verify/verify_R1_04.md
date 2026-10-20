# Проверка выписывания — файл 4 из 6

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

## ST031 · Wilson 2022 · Journal of Public Health

Основной отчёт R3643: [текст](../../fulltext/text/R3643.txt) · [PDF](../../fulltext/pdf/R3643.pdf) — «Associations between playing free-to-play sports gambling predictor games and online sports betting frequency for men in the United Kingdom» — [DOI](https://doi.org/10.1007/s10389-022-01774-4)
Расхождения в тексте: Table 1: online sports gambling frequency low 177 + high 129 = 306. This matches the text: 79.7% of 384 = 306. The PGSI groups sum to 384 (157+121+80+26). Income rows sum to 383 and education rows to 378, so a few values are missing for those variables. Text percentages for PGSI (40.9/31.5/20.8/6.8) match Table 1.
Заметка ИИ: Whether this sample is eligible needs a reviewer decision. The only PGSI prevalence is for all 384 past-year male gamblers. The sports-bettor subsample (306 online sports or horse race bettors, mixed with race betting) has no PGSI breakdown, and none can be derived. The extracted estimates are for the whole sample and are labelled that way.

### ST031-1 · UK men 18+ past-year gamblers, online convenience survey (predictor games), n=384 (306 online sports/horse race bettors)
Отчёты: R3643 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all past-year gamblers (not sports-bettor specific) | PGSI · PGSI 0 | **below** | **157 / 384** | 40.9 | Page 4, Table 1 | «Non-problem gambling 40.9 (157)» |
| E2 | all past-year gamblers (not sports-bettor specific) | PGSI · PGSI 1-2 | **L1** | **121 / 384** | 31.5 | Page 4, Table 1 | «Low-risk gambling 31.5 (121)» |
| E3 | all past-year gamblers (not sports-bettor specific) | PGSI · PGSI 3-7 | **L2** | **80 / 384** | 20.8 | Page 4, Table 1 | «Moderate-risk gambling 20.8 (80)» |
| E4 | all past-year gamblers (not sports-bettor specific) | PGSI · PGSI>=8 | **L3** | **26 / 384** | 6.8 | Page 4, Table 1 | «Problem gambling 6.8 (26)» |

- E1: cumulative: no; источник порога: standard; правило: PGSI row; 0 = below; у авторов: «non-problem gambling»; главная у авторов: yes; период: NR; заметка: Denominator = all 384 past-year gamblers, of whom 306 bet online on sports or horse racing; not a sports-bettor estimate. PGSI time frame not stated.
- E2: cumulative: no; источник порога: standard; правило: PGSI row; 1-2 band starts at L1; у авторов: «low-risk gambling»; главная у авторов: yes; период: NR; заметка: Denominator = all 384 past-year gamblers; not a sports-bettor estimate.
- E3: cumulative: no; источник порога: standard; правило: PGSI row; 3-7 band starts at L2; у авторов: «moderate-risk gambling»; главная у авторов: yes; период: NR; заметка: Denominator = all 384 past-year gamblers; not a sports-bettor estimate.
- E4: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ = L3; у авторов: «problem gambling»; главная у авторов: yes; период: NR; заметка: Denominator = all 384 past-year gamblers; not a sports-bettor estimate.

**Ключевые поля выборки:**
- **n_bettors: 306** — Page 4, Table 1 (Online sports gambling frequency) — «Online sports gambling frequency Low 57.8 (177) High 42.2 (129)»
- **sample_type: gamblers_survey_subsample** — Page 3; Page 7, Limitations — «the proportion of individuals who in the past 12-months ever engaged in both online sports gambling (79.7%)»
- **sampling: convenience** — Page 3, Study design and participants — «The survey was promoted through social media, and gambling forums, charities and support-groups were approached to promote the survey.»
- **betting_period: past 12 months** — Page 3, Online sports gambling frequency — «Participants were asked about their online sports and horse racing gambling frequency over the past 12-months»

**Остальные поля:**
- parent_population: Men aged 18+ living in the UK who gambled on any activity in the past 12 months (online convenience survey) — Page 1, Abstract — «An online survey using a convenience sample was completed by males aged 18 + years, living in the United Kingdom, and having participated in any gambling activ…»
- min_frequency: none — Page 3, Online sports gambling frequency — «Frequency of online sports gambling was categorised as low: 1 time per year – 2–3 days per month; and high: once per week – every day.»
- country: GBR — Page 3, Study design and participants — «male, living in the UK, aged 18 years or over, and having gambled within the past 12-months»
- subnational: NA — Page 3, Study design and participants — «living in the UK»
- data_years: NR — Page 1; Page 4, Ethics approval — «Received: 9 March 2022 / Accepted: 25 October 2022»
- design: cross-sectional — Page 3, Study design and participants — «A cross-sectional online survey using convenience sampling was conducted.»
- gambling_disclosed: yes — Page 3, Study design and participants — «The topics of online sports gambling and predictor games were pointed out in the survey title and adverts.»
- betting_mode: online only — Page 3, Online sports gambling frequency — «their online sports and horse racing gambling frequency over the past 12-months»
- pct_online: all — Page 3, Online sports gambling frequency — «online sports and horse racing gambling frequency»
- pct_inplay: NR — NA
- pct_dfs: NR — NA
- pct_esports: NR — NA
- sports_lottery: no — Page 3, Online sports gambling frequency — «online sports and horse racing gambling frequency»
- mixed_race: yes — Page 5 — «Of those who engaged in online sports or horse race gambling, the proportion of those doing so 1–5 times a year was 23.2%»
- legal_status: regulated legal market — Page 2, Background; Page 7, Policy implications — «gross gambling yield... increasing by 33.6% to £2.33 billion from 2015 to 2020 in the UK (The Gambling Commission 2020)... The current Gambling Act is outdated»
- n_invited: NR — Page 3 — «The survey was promoted through social media»
- n_responded: 473 — Page 3, Study design and participants — «In total 473 individuals completed the survey; however, 89 were removed due to not meeting the eligibility criteria. Therefore, the overall sample size was n =…»
- response_rate: NR — NA
- age_mean: NR — Page 4, Table 1 — «Age group (years) 18–24 36.7 (141) 25–34 45.0 (173) 35 + 18.2 (70)»
- age_sd: NR — NA
- age_min: 18 — Page 3, Study design and participants — «aged 18 years or over»
- age_max: NR — Page 4, Table 1 — «35 + 18.2 (70)»
- age_group: adults — Page 3 — «aged 18 years or over»
- pct_male: 100 — Page 3, Study design and participants — «Participants were eligible to take part in the study if they met the following inclusion criteria: male»
- mode: online — Page 3 — «A cross-sectional online survey»
- weights: no — Page 3, Statistical analysis — «All analysis was performed using SPSS v.27. Bivariate analyses were used»
- instruments: PGSI (English) — Page 3, Problem Gambling Severity Index (PGSI) — «The PGSI is a self-report, validated instrument designed for measuring the presence and severity of gambling problems in general populations (Ferris and Wynne …»
- instrument_validated_in_language: yes — Page 3, PGSI — «The PGSI is a self-report, validated instrument ... (Ferris and Wynne 2001; Holtgraves 2008)»
- industry_funding: NR — Page 8, Declarations — «Conflicts of interest The authors have no conflicts of interest to declare that are relevant to the content of this article.»
- funding_coi: No funding statement; authors declare no conflicts of interest — Page 8, Declarations — «The authors have no conflicts of interest to declare that are relevant to the content of this article.»
- pub_status: journal — Page 1, header — «Journal of Public Health (2023) 31:1989–1998»
- language: English — Full text — «Associations between playing free-to-play sports gambling predictor games and online sports betting frequency for men in the United Kingdom»
- notes: IMPORTANT: The PGSI is reported only for all 384 past-year gamblers (any gambling activity), not for the sports bettors. The sports-betting subsample is past-year online sports OR horse race bettors (mixed_race), n=306 (Table 1: low 177 + high 129; text: 79.7% of 384). No PGSI breakdown by online sports/race betting is reported, and there is no reverse table, so a sports-bettor estimate cannot be derived. The estimates are for the whole sample (all gamblers, including 78 who did not bet online on sports/races) and are given only so a reviewer can decide. Age and sex fields describe the whole …

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame was social media users and gambling forums/charities/support groups; it does not cover UK sports bettors. — Page 3, Study design and participants — «The survey was promoted through social media, and gambling forums, charities and support-groups were approached to promote the survey.»
2. способ отбора: **no** — Convenience, volunteer opt-in sampling. — Page 3 — «A cross-sectional online survey using convenience sampling was conducted.»
3. размер выборки: **no** — 306 online sports/race bettors (384 overall), below 385. — Page 4, Table 1 — «Low 57.8 (177) High 42.2 (129)»
4. описание выборки и условий: **unclear** — Age bands, sex, setting and country reported; dates of data collection not reported. — Page 3; Page 4, Table 1 — «male, living in the UK, aged 18 years or over»
5. охват (пропуски): **yes** — PGSI groups sum to all 384 respondents (157+121+80+26). — Page 4, Table 1 — «Non-problem gambling 40.9 (157) Low-risk gambling 31.5 (121) Moderate-risk gambling 20.8 (80) Problem gambling 6.8 (26)»
6. валидность определения случая: **yes** — English PGSI with standard 8+ threshold. — Page 3, PGSI — «0 = non-problem gambling; 1–2 = low-risk gambling; 3–7 = moderate risk gambling; 8 + = problem gambling»
7. единое надёжное измерение: **yes** — Same online self-report PGSI for everyone; validation sources cited, though reliability in this sample is not reported. — Page 3, PGSI — «The PGSI is a self-report, validated instrument ... (Ferris and Wynne 2001; Holtgraves 2008).»
8. статистика (числитель и знаменатель): **no** — PGSI numerators are reported only for all gamblers; there is no numerator for sports bettors. — Page 4, Table 1 — «PGSI group Non-problem gambling 40.9 (157)»
9. отклик: **no** — Open online survey with no denominator of invited people; non-response not handled. — Page 3 — «In total 473 individuals completed the survey»

Правки:
- 

Проверено: да

---

## ST032 · Greer 2021 · Journal of behavioral addictions

Основной отчёт R3816: [текст](../../fulltext/text/R3816.txt) — «Are esports bettors a new generation of harmed gamblers? A comparison with sports bettors on gambling involvement, problems, and harm.» — [DOI](https://doi.org/10.1556/2006.2021.00039)
Расхождения в тексте: Table 4 PGSI counts add up to the full groups (298 and 300), but the chi-square is reported as χ2(3, 595), which points to 3 missing cases. The table counts were used. The abstract writes '64.8.%' (a typo for 64.8%). In Table 1 the income percentages for esports bettors do not match n/298 (e.g., 52 (18.0)), which suggests missing income data. The PGSI time frame is not stated.
Заметка ИИ: Two samples recruited separately in one Qualtrics panel survey: regular esports bettors (including skin bettors) and regular sports bettors who do not bet on esports. Both were extracted. PGSI scores cover all gambling, not only sports or esports betting.

### ST032-1 · Esports bettors, Australia, Qualtrics online panel, 2019, n=298
Отчёты: R3816 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | PGSI · PGSI 0 | **below** | **25 / 298** | 8.4 | Table 4 | «Non problem gambler (0) / 25 (8.4) / 100 (33.3)» |
| E2 | all | PGSI · PGSI 1-2 | **L1** | **32 / 298** | 10.7 | Table 4 | «Low-risk gambler (1–2) / 32 (10.7) / 71 (23.7)» |
| E3 | all | PGSI · PGSI 3-7 | **L2** | **48 / 298** | 16.1 | Table 4 | «Moderate-risk gambler (3–7) / 48 (16.1) / 77 (25.7)» |
| E4 | all | PGSI · PGSI>=8 | **L3** | **193 / 298** | 64.8 | Table 4; Abstract | «Problem gambler (8+) / 193 (64.8) / 52 (17.3)» |

- E1: cumulative: no; источник порога: standard; правило: PGSI row; 0 = below; у авторов: «Non problem gambler»; главная у авторов: no; период: NR; заметка: PGSI time frame not stated (standard past 12 months)
- E2: cumulative: no; источник порога: standard; правило: PGSI row; 1-2 band starts at L1; у авторов: «Low-risk gambler»; главная у авторов: no; период: NR
- E3: cumulative: no; источник порога: standard; правило: PGSI row; 3-7 band starts at L2; у авторов: «Moderate-risk gambler»; главная у авторов: no; период: NR
- E4: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ = L3; у авторов: «Problem gambler»; главная у авторов: yes; период: NR

**Ключевые поля выборки:**
- **n_bettors: 298** — Table 4 — «Esports bettor (N = 298)»
- **sample_type: bettor_recruited** — Methods, Participants and procedures — «Esports bettors met inclusion criteria if they bet on esports regularly ('at least fortnightly') in the last 12 months, with either money ... or with skins or skin deposits»
- **sampling: quota** — Methods, Participants and procedures; Limitations — «Participants were recruited via Qualtrics and compensated via panel points.»
- **betting_period: past 12 months** — Methods, Participants and procedures — «bet on esports regularly ('at least fortnightly') in the last 12 months»

**Остальные поля:**
- parent_population: NA — Methods — «Two sub-groups were sampled: esports bettors (n = 298) and sports bettors (n = 300).»
- min_frequency: at least fortnightly (esports betting) — Methods, Participants and procedures — «bet on esports regularly ('at least fortnightly') in the last 12 months»
- country: AUS — Methods, Participants and procedures — «online survey conducted May-July 2019 with Australian residents aged 18 years or over»
- subnational: NA — Table 1 — «New South Wales | 102 (34.2) ... Victoria | 86 (28.9) ... Queensland | 46 (15.4)»
- data_years: 2019 — Methods, Participants and procedures — «Data were obtained from an online survey conducted May-July 2019»
- design: cross-sectional — Limitations — «data were collected cross-sectionally»
- gambling_disclosed: NR — Methods — «Participants were recruited via Qualtrics and compensated via panel points.»
- betting_mode: NR — Methods — «with either money (including debit, credit, or cryptocurrency), or with skins or skin deposits»
- pct_online: NR — NA
- pct_inplay: NR — NA
- pct_dfs: NR — Fig. 1 (values not given in text) — «higher proportions of esports bettors gambled on casino table games, bet privately for money, played bingo, and bet on fantasy sports»
- pct_esports: all — Methods — «Esports bettors met inclusion criteria if they bet on esports regularly»
- sports_lottery: no — Methods — «esports cash betting ... esports skin betting ... skin gambling»
- mixed_race: no — Methods — «Esports bettors met inclusion criteria if they bet on esports regularly»
- legal_status: mixed — Introduction — «available via regulated domestic (as well as illegal, offshore) gambling operators ... in-game items can also be used to bet on esports, mainly via unregulated…»
- n_invited: NR — NA
- n_responded: 598 — Methods; Table 2 — «esports bettors (n = 298) and sports bettors (n = 300)»
- response_rate: NR — NA
- age_mean: 33.28 — Table 1 — «Mean (SD) | 33.28 (10.44) | 44.53 (10.83)»
- age_sd: 10.44 — Table 1 — «Mean (SD) | 33.28 (10.44)»
- age_min: 18 — Methods — «ages ranged between 18 and 77 years»
- age_max: 77 — Methods — «ages ranged between 18 and 77 years»
- age_group: adults — Methods — «Australian residents aged 18 years or over»
- pct_male: 57.7 — Table 1 — «Male | 172 (57.7) | 254 (84.7)»
- mode: online — Methods — «Data were obtained from an online survey»
- weights: NR — Statistical analyses — «Independent groups t-tests and chi-square tests were used»
- instruments: PGSI (English); SGHS (harm, not a problem-gambling instrument) — Measures, Problem gambling — «Problem gambling was measured using the Problem Gambling Severity Index (PGSI; Ferris & Wynne, 2001).»
- instrument_validated_in_language: yes — Measures, Problem gambling — «Problem Gambling Severity Index (PGSI; Ferris & Wynne, 2001)»
- industry_funding: no — Funding sources — «This study was funded by the Victorian Responsible Gambling Foundation.»
- funding_coi: Victorian Responsible Gambling Foundation; authors declare no conflict of interest — Funding sources; Conflict of interest — «This study was funded by the Victorian Responsible Gambling Foundation. ... The authors declare no conflict of interest»
- pub_status: journal — Header — «Journal of behavioral addictions; DOI: 10.1556/2006.2021.00039»
- language: English — Full text — «Are esports bettors a new generation of harmed gamblers?»
- notes: Esports bettors include skin bettors: 53.7% money and skins, 30.9% cash only, 15.4% skins only. Not excluded for other gambling: 95.3% also bet on traditional sports in past 12 months, 72.8% regularly. Age mean/SD and % male are for esports bettors; age min/max (18-77) are for the whole sample of 598. PGSI covers all gambling, not esports only. Recruited separately from the sports-bettor sample of the same survey. Sampling coded quota (Qualtrics non-probability panel); quotas not described explicitly. Legal status coded mixed because cash esports betting goes through regulated operators but s…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Online panel (Qualtrics) members only; does not cover all Australian esports bettors — Methods; Limitations — «the sample was recruited via online panels, introducing a potentially biased sample»
2. способ отбора: **no** — Non-probability online panel — Methods — «Participants were recruited via Qualtrics and compensated via panel points.»
3. размер выборки: **no** — n=298 < 385 — Table 4 — «Esports bettor (N = 298)»
4. описание выборки и условий: **yes** — Age, sex, setting, country and dates all reported — Methods; Table 1 — «online survey conducted May-July 2019 with Australian residents aged 18 years or over»
5. охват (пропуски): **yes** — PGSI categories sum to the full 298 (although the chi-square has N=595) — Table 4 — «25 (8.4) ... 32 (10.7) ... 48 (16.1) ... 193 (64.8)»
6. валидность определения случая: **yes** — PGSI, English original, with the standard 8+ threshold — Measures — «0 = no problems, 1–2 = low risk, 3–7 = moderate risk, 8+ problem»
7. единое надёжное измерение: **yes** — Same online PGSI for everyone; source instrument cited (Ferris & Wynne 2001); no reliability reported in this sample — Measures — «Problem gambling was measured using the Problem Gambling Severity Index (PGSI; Ferris & Wynne, 2001).»
8. статистика (числитель и знаменатель): **yes** — Counts and denominator given; CI can be calculated — Table 4 — «Problem gambler (8+) | 193 (64.8)»
9. отклик: **no** — Online panel, no denominator of people invited and no response rate — Methods — «Participants were recruited via Qualtrics and compensated via panel points.»

Правки:
- 

Проверено: да

### ST032-2 · Regular sports bettors (no esports), Australia, Qualtrics online panel, 2019, n=300
Отчёты: R3816 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | PGSI · PGSI 0 | **below** | **100 / 300** | 33.3 | Table 4 | «Non problem gambler (0) / 25 (8.4) / 100 (33.3)» |
| E2 | all | PGSI · PGSI 1-2 | **L1** | **71 / 300** | 23.7 | Table 4 | «Low-risk gambler (1–2) / 32 (10.7) / 71 (23.7)» |
| E3 | all | PGSI · PGSI 3-7 | **L2** | **77 / 300** | 25.7 | Table 4 | «Moderate-risk gambler (3–7) / 48 (16.1) / 77 (25.7)» |
| E4 | all | PGSI · PGSI>=8 | **L3** | **52 / 300** | 17.3 | Table 4; Abstract | «Problem gambler (8+) / 193 (64.8) / 52 (17.3)» |

- E1: cumulative: no; источник порога: standard; правило: PGSI row; 0 = below; у авторов: «Non problem gambler»; главная у авторов: no; период: NR; заметка: PGSI time frame not stated
- E2: cumulative: no; источник порога: standard; правило: PGSI row; 1-2 band starts at L1; у авторов: «Low-risk gambler»; главная у авторов: no; период: NR
- E3: cumulative: no; источник порога: standard; правило: PGSI row; 3-7 band starts at L2; у авторов: «Moderate-risk gambler»; главная у авторов: no; период: NR
- E4: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ = L3; у авторов: «Problem gambler»; главная у авторов: yes; период: NR

**Ключевые поля выборки:**
- **n_bettors: 300** — Table 4 — «Sports bettor (N = 300)»
- **sample_type: bettor_recruited** — Methods, Participants and procedures — «Sports bettors met inclusion criteria if they: 1) bet regularly ('at least fortnightly') in the last 12 months on sports, excluding esports or fantasy sports»
- **sampling: quota** — Methods — «Participants were recruited via Qualtrics and compensated via panel points.»
- **betting_period: past 12 months** — Methods — «bet regularly ('at least fortnightly') in the last 12 months on sports»

**Остальные поля:**
- parent_population: NA — Methods — «Two sub-groups were sampled»
- min_frequency: at least fortnightly — Methods — «bet regularly ('at least fortnightly') in the last 12 months on sports, excluding esports or fantasy sports»
- country: AUS — Methods, Participants and procedures — «online survey conducted May-July 2019 with Australian residents aged 18 years or over»
- subnational: NA — Table 1 — «New South Wales | 102 (34.2) | 91 (30.3)»
- data_years: 2019 — Methods — «online survey conducted May-July 2019»
- design: cross-sectional — Limitations — «data were collected cross-sectionally»
- gambling_disclosed: NR — Methods — «Participants were recruited via Qualtrics and compensated via panel points.»
- betting_mode: NR — NA
- pct_online: NR — NA
- pct_inplay: NR — NA
- pct_dfs: NR — Fig. 1 (values not given in text) — «higher proportions of esports bettors gambled on ... fantasy sports»
- pct_esports: 0 — Methods — «2) did not bet on esports in the last 12 months with money or skins; and 3) did not watch esports in the last 12 months»
- sports_lottery: no — Methods — «bet regularly ... on sports, excluding esports or fantasy sports»
- mixed_race: no — Methods — «bet regularly ('at least fortnightly') in the last 12 months on sports»
- legal_status: regulated legal market — Introduction — «it is available via regulated domestic (as well as illegal, offshore) gambling operators»
- n_invited: NR — NA
- n_responded: 598 — Methods — «esports bettors (n = 298) and sports bettors (n = 300)»
- response_rate: NR — NA
- age_mean: 44.53 — Table 1 — «Mean (SD) | 33.28 (10.44) | 44.53 (10.83)»
- age_sd: 10.83 — Table 1 — «44.53 (10.83)»
- age_min: 18 — Methods — «ages ranged between 18 and 77 years»
- age_max: 77 — Methods — «ages ranged between 18 and 77 years»
- age_group: adults — Methods — «Australian residents aged 18 years or over»
- pct_male: 84.7 — Table 1 — «Male | 172 (57.7) | 254 (84.7)»
- mode: online — Methods — «Data were obtained from an online survey»
- weights: NR — Statistical analyses — «Independent groups t-tests and chi-square tests were used»
- instruments: PGSI (English); SGHS (harm, not a problem-gambling instrument) — Measures — «Problem gambling was measured using the Problem Gambling Severity Index (PGSI; Ferris & Wynne, 2001).»
- instrument_validated_in_language: yes — Measures — «Problem Gambling Severity Index (PGSI; Ferris & Wynne, 2001)»
- industry_funding: no — Funding sources — «This study was funded by the Victorian Responsible Gambling Foundation.»
- funding_coi: Victorian Responsible Gambling Foundation; authors declare no conflict of interest — Funding sources; Conflict of interest — «The authors declare no conflict of interest in relation to this manuscript.»
- pub_status: journal — Header — «Journal of behavioral addictions; DOI: 10.1556/2006.2021.00039»
- language: English — Full text — «A comparison with sports bettors on gambling involvement, problems, and harm»
- notes: Regular (at least fortnightly) sports bettors who did not bet on or watch esports; fantasy sports did not count toward qualifying. Age mean/SD and % male are for sports bettors; age min/max (18-77) are for the whole sample of 598. PGSI covers all gambling. Recruited separately from the esports-bettor sample of the same survey. Sampling coded quota (Qualtrics non-probability panel).

**Риск смещения (JBI):**
1. рамка выборки: **no** — Online panel members only; does not cover all Australian regular sports bettors — Limitations — «the sample was recruited via online panels, introducing a potentially biased sample»
2. способ отбора: **no** — Non-probability online panel — Methods — «Participants were recruited via Qualtrics and compensated via panel points.»
3. размер выборки: **no** — n=300 < 385 — Table 4 — «Sports bettor (N = 300)»
4. описание выборки и условий: **yes** — Age, sex, setting, country and dates all reported — Methods; Table 1 — «online survey conducted May-July 2019 with Australian residents aged 18 years or over»
5. охват (пропуски): **yes** — PGSI categories sum to the full 300 — Table 4 — «100 (33.3) ... 71 (23.7) ... 77 (25.7) ... 52 (17.3)»
6. валидность определения случая: **yes** — PGSI, English original, with the standard 8+ threshold — Measures — «0 = no problems, 1–2 = low risk, 3–7 = moderate risk, 8+ problem»
7. единое надёжное измерение: **yes** — Same online PGSI for everyone; source instrument cited; no reliability reported in this sample — Measures — «Problem Gambling Severity Index (PGSI; Ferris & Wynne, 2001)»
8. статистика (числитель и знаменатель): **yes** — Counts and denominator given — Table 4 — «Problem gambler (8+) | 193 (64.8) | 52 (17.3)»
9. отклик: **no** — Online panel, no invited denominator and no response rate — Methods — «Participants were recruited via Qualtrics and compensated via panel points.»

Правки:
- 

Проверено: да

---

## ST033 · Houghton 2021 · Journal of behavioral addictions

Основной отчёт R3836: [текст](../../fulltext/text/R3836.txt) — «Comparing football bettors' response to social media marketing differing in bet complexity and account type - An experimental study.» — [DOI](https://doi.org/10.1556/2006.2020.00056)
Расхождения в тексте: The text says the PGSI range was 1 to 26 ('Median PGSI score was 6 (range = 1 to 26)'), but Table 1 puts 10% in the Non-problem category, which would mean scores of 0. Table 1 is used as the rule requires; the reviewer should check this. Table 1 percentages add to 100 with N=100, so counts equal percentages. Missing data for 21 of the 100 participants were median-imputed; it is unclear whether this touched PGSI items and so the PGSI categories.
Заметка ИИ: One eligible sample: 100 regular (at least monthly) football bettors in GB recruited by convenience for an online experiment. PGSI categories come from Table 1 percentages (n=100). The authors name no primary prevalence estimate, so primary_for_authors = no for all; PGSI>=8 (41%) is the L3 estimate.

### ST033-1 · Regular football bettors, Great Britain, online experiment (Twitter, football forums, SurveyCircle), n=100 analysed
Отчёты: R3836 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | PGSI · PGSI 0 | **below** | **10 / 100** | 10.0 | Table 1 | «PGSI category Non-problem / 10» |
| E2 | all | PGSI · PGSI 1-2 | **L1** | **23 / 100** | 23.0 | Table 1 | «Low risk / 23» |
| E3 | all | PGSI · PGSI 3-7 | **L2** | **26 / 100** | 26.0 | Table 1 | «Moderate risk / 26» |
| E4 | all | PGSI · PGSI>=8 | **L3** | **41 / 100** | 41.0 | Table 1 | «Problem / 41» |

- E1: cumulative: no; источник порога: standard; правило: PGSI row; score 0 is below L1; у авторов: «Non-problem»; главная у авторов: no; период: NR; **расчёт: 10% x 100 = 10**; заметка: Only the percentage is printed; n = 100. The text gives a PGSI range of 1 to 26, which conflicts with 10% scoring 0 (see consistency_notes).
- E2: cumulative: no; источник порога: standard; правило: PGSI row; 1-2 band starts at L1; у авторов: «Low risk»; главная у авторов: no; период: NR; **расчёт: 23% x 100 = 23**
- E3: cumulative: no; источник порога: standard; правило: PGSI row; 3-7 band starts at L2; у авторов: «Moderate risk»; главная у авторов: no; период: NR; **расчёт: 26% x 100 = 26**
- E4: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ = L3; у авторов: «Problem»; главная у авторов: no; период: NR; **расчёт: 41% x 100 = 41**; заметка: The authors report PGSI categories only to describe participants; prevalence is not a stated aim. Median PGSI = 6.

**Ключевые поля выборки:**
- **n_bettors: 100** — Method, Participants — «Of the remaining 100 participants (mean age = 27.84, SD = 9.01, range = 18 to 64) which were included in the analysis»
- **sample_type: bettor_recruited** — Method, Participants — «regular football bettors ... were recruited to take part in the study via opportunity sampling through the researcher's Twitter account, football supporter forums and a survey-sharing website (SurveyCircle)»
- **sampling: convenience** — Method, Participants — «recruited to take part in the study via opportunity sampling through the researcher's Twitter account, football supporter forums and a survey-sharing website (SurveyCircle)»
- **betting_period: current** — Method, Participants — «Regular football betting was defined as betting once a month or more on football.»

**Остальные поля:**
- parent_population: NA — Method, Participants — «regular football bettors in Great Britain aged 18 and over»
- min_frequency: at least monthly on football — Method, Participants — «Regular football betting was defined as betting once a month or more on football.»
- country: GBR — Method, Participants — «One hundred and forty-five regular football bettors in Great Britain aged 18 and over were recruited»
- subnational: NA — Method, Participants — «regular football bettors in Great Britain»
- data_years: NR — Materials, Tweets — «The chosen bets and odds were taken from an online sports betting website and covered 2 game weeks of the 2018/2019 English Premier League season.»
- design: experiment baseline — Method, Design — «A 3 × 2 repeated measures design was employed.»
- gambling_disclosed: yes — Method, Participants — «One hundred and forty-five regular football bettors in Great Britain aged 18 and over were recruited to take part in the study»
- betting_mode: NR — Method — «NR»
- pct_online: NR — Method — «NR»
- pct_inplay: NR — Method — «NR»
- pct_dfs: NR — Method — «NR»
- pct_esports: NR — Method — «NR»
- sports_lottery: no — Method, Participants — «Regular football betting was defined as betting once a month or more on football.»
- mixed_race: no — Method, Participants — «Regular football betting was defined as betting once a month or more on football.»
- legal_status: NR — Introduction — «NR»
- n_invited: NR — Method, Participants — «NR»
- n_responded: 145 — Method, Participants — «One hundred and forty-five regular football bettors in Great Britain aged 18 and over were recruited»
- response_rate: NR — Method, Participants — «NR»
- age_mean: 27.84 — Method, Participants — «Of the remaining 100 participants (mean age = 27.84, SD = 9.01, range = 18 to 64)»
- age_sd: 9.01 — Method, Participants — «mean age = 27.84, SD = 9.01, range = 18 to 64»
- age_min: 18 — Method, Participants — «range = 18 to 64»
- age_max: 64 — Method, Participants — «range = 18 to 64»
- age_group: adults — Method, Participants — «regular football bettors in Great Britain aged 18 and over»
- pct_male: 83 — Method, Participants — «Of the remaining 100 participants ... there were 83 males and 17 females.»
- mode: online — Procedure — «Participants accessed the Qualtrics survey via a social media site or an online survey-sharing website.»
- weights: no — Results, Statistical analyses — «Data was downloaded from Qualtrics into SPSS version25 for analysis.»
- instruments: PGSI (English) — Materials, Problem Gambling Severity Index — «The Problem Gambling Severity Index (PGSI) is a nine-item questionnaire (Ferris & Wynne, 2001) validated to assess levels of problematic gambling in the genera…»
- instrument_validated_in_language: yes — Materials, Problem Gambling Severity Index — «nine-item questionnaire (Ferris & Wynne, 2001) validated to assess levels of problematic gambling in the general population (Holtgraves, 2009)»
- industry_funding: yes — Funding sources; Conflict of interests — «I receive funding from GambleAware to carry out my PhD studies, a British grant-making charity who receives donations from the Gambling Industry.»
- funding_coi: Lead author's PhD funded by GambleAware (charity funded by gambling-industry donations); GambleAware stated to have no involvement in design, conduct, analysis or write-up. — Funding sources; Conflict of interests — «The PhD is funded by GambleAware. GambleAware approved the overall focus of the PhD, however had no involvement in the research design, methodology, conduct, a…»
- pub_status: journal — Header — «Journal of behavioral addictions; DOI: 10.1556/2006.2020.00056»
- language: English — Full text — «Comparing football bettors' response to social media marketing differing in bet complexity and account type»
- notes: Age and sex are for the 100 analysed participants. 145 recruited; 38 excluded for completing <50% of the survey and 7 for not rating enough bets. Missing data points for 21 of the 100 were replaced by median imputation; the text does not say whether PGSI items were imputed. Data collection dates not reported (stimuli from the 2018/2019 EPL season). gambling_disclosed = yes is inferred from recruitment of 'regular football bettors'; the invitation wording is not quoted. Industry funding coded yes because GambleAware gets its money from industry donations; the reviewer should check this against…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame was the researcher's Twitter followers, football forums and SurveyCircle, which covers only part of GB football bettors. — Method, Participants — «via opportunity sampling through the researcher's Twitter account, football supporter forums and a survey-sharing website (SurveyCircle)»
2. способ отбора: **no** — Opportunity (convenience) sampling with volunteer opt-in and a prize-draw incentive. — Method, Participants — «recruited to take part in the study via opportunity sampling»
3. размер выборки: **no** — Only 100 sports bettors analysed (<385). — Method, Participants — «Of the remaining 100 participants ... which were included in the analysis»
4. описание выборки и условий: **unclear** — Age, sex, setting and country are reported; dates of data collection are not. — Method, Participants; Table 1 — «mean age = 27.84, SD = 9.01, range = 18 to 64 ... there were 83 males and 17 females»
5. охват (пропуски): **no** — 45 of 145 recruited (31%) were excluded for incomplete data, and this was not handled. — Method, Participants — «Thirty-eight participants were removed from analysis for completing less than 50% of the survey and a further 7 participants were removed»
6. валидность определения случая: **yes** — English PGSI with the standard 8+ problem category; a validation paper is cited. — Materials, PGSI; Table 1 — «The Problem Gambling Severity Index (PGSI) is a nine-item questionnaire (Ferris & Wynne, 2001) validated to assess levels of problematic gambling»
7. единое надёжное измерение: **unclear** — Everyone completed the same online PGSI, but no reliability is reported for this sample, and the time frame and median imputation of missing items are unclear. — Procedure — «Participants were asked to fill out the demographics questionnaire, the gambling activities questionnaire and the PGSI in that order.»
8. статистика (числитель и знаменатель): **yes** — PGSI category percentages are given for N=100, so counts and CIs can be calculated; no weighting is needed for a convenience sample. — Table 1 — «PGSI category Non-problem | 10 Low risk | 23 Moderate risk | 26 Problem | 41»
9. отклик: **no** — Open online recruitment with no denominator of invited people; response rate cannot be calculated. — Method, Participants — «recruited ... through the researcher's Twitter account, football supporter forums and a survey-sharing website»

Правки:
- 

Проверено: да

---

## ST034 · Lelonek-Kuleta 2021 · Journal of gambling studies

Основной отчёт R3889: [текст](../../fulltext/text/R3889.txt) — «Online Gambling Activity, Pay-to-Win Payments, Motivation to Gamble and Coping Strategies as Predictors of Gambling Disorder Among e-sports Bettors.» — [DOI](https://doi.org/10.1007/s10899-021-10015-4)
Расхождения в тексте: The PGSI counts 78+86+121+153 add up to 438 = N, and the percentages match the counts (e.g., 153/438 = 34.9%). The Results label the top category 'above 8 points' while the Measures section gives '8 and more'. The response scale is printed as '0 = Never, 1 = Sometimes, 3 = Most of the time, 4 = Almost always', which is probably a typo for the standard 0-3 scale. The Measures section also calls PGSI>=3 'pathological gamblers', but no separate cumulative estimate is printed beyond 'exceeds 60%' in the Discussion (121+153 = 274/438 = 62.6% is not stated by the authors). The Table 3 offline percentages use 249 offline gamblers as the denominator, not 438.
Заметка ИИ: One sample: online esports/virtual sports bettors from a Polish opt-in panel. Eligibility depends on accepting a group defined as 'esports or virtual sports' bettors. Data years, funding and the PGSI time frame are not reported. There are no page markers, so locations are given by section.

### ST034-1 · Esports/virtual sports bettors from IMAS Internet panel, Poland, n=438
Отчёты: R3889 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | PGSI · PGSI 0 | **below** | **78 / 438** | 17.8 | Results, Prevalence of Gambling Disorder Among esports Bett… | «non-problem gamblers (0 points in PGSI) accounted for 17.8% (n = 78, 95%CI[14.4%, 21.6%])» |
| E2 | all | PGSI · PGSI 1-2 | **L1** | **86 / 438** | 19.6 | Results, Prevalence of Gambling Disorder Among esports Bett… | «19.6% (n = 86, 95%CI[16.1%, 23.5%]) showed a low risk of gambling addiction (1–2 points, low-risk gamblers)» |
| E3 | all | PGSI · PGSI 3-7 | **L2** | **121 / 438** | 27.6 | Results, Prevalence of Gambling Disorder Among esports Bett… | «27.6% (n = 121, 95%CI[23.6%, 32.0%]) showed a moderate level of addiction risk (3–7 points, moderate risk gamblers)» |
| E4 | all | PGSI · PGSI>=8 | **L3** | **153 / 438** | 34.9 | Results, Prevalence of Gambling Disorder Among esports Bett… | «34.9% (n = 153, 95%CI[30.6%, 39.5%]) esports gamblers exhibited gambling disorder symptoms (above 8 points in PGSI, problem gamblers)» |

- E1: cumulative: no; источник порога: standard; правило: PGSI row; score 0 is below L1; у авторов: «non-problem gamblers»; главная у авторов: no; период: NR; заметка: The PGSI time frame is not stated.
- E2: cumulative: no; источник порога: standard; правило: PGSI row; 1-2 band starts at L1; у авторов: «low-risk gamblers»; главная у авторов: no; период: NR
- E3: cumulative: no; источник порога: standard; правило: PGSI row; 3-7 band starts at L2; у авторов: «moderate risk gamblers»; главная у авторов: no; период: NR
- E4: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ starts at L3; у авторов: «problem gamblers (gambling disorder symptoms)»; главная у авторов: yes; период: NR; заметка: The Results say 'above 8 points' but the Measures section defines '8 and more'; the categories add up to 438, so this is taken as >=8.

**Ключевые поля выборки:**
- **n_bettors: 438** — Methods, Participants and Procedure — «The esports bettors sample consisted of 438 people aged 18 to 64 (M = 33.1, SD = 9.27).»
- **sample_type: gamblers_survey_subsample** — Methods, Participants and Procedure — «Esports bettors were selected from the broader sample of Internet gamblers.»
- **sampling: convenience** — Methods, Participants and Procedure — «IMAS invited 46,806 panel users to participate in the research. The invitation was accepted by 8511 (18.2%) of them.»
- **betting_period: past 12 months** — Methods, Participants and Procedure — «"Have you gambled for money on esports or virtual sports betting online over the past 12 months?"»

**Остальные поля:**
- parent_population: IMAS Internet panel users in Poland who gambled online in the past 12 months or spent money on free-to-play games (n=2074) — Methods, Participants and Procedure — «(1) they have gambled online during the last 12 months or (2) they have spent money on free-to-play games. Respondents meeting one or both of these criteria fo…»
- min_frequency: none — Methods, Participants and Procedure — «people who gave positive answers to the question: "Have you gambled for money on esports or virtual sports betting online over the past 12 months?" were select…»
- country: POL — Abstract — «This study presents the results of the first research in Poland (N = 438) on esports betting (ESB).»
- subnational: NA — Methods, Participants and Procedure — «The panel has operated in Poland since 2005»
- data_years: NR — Methods, Participants and Procedure — «The survey was conducted by an IMAS Internet panel among registered users.»
- design: cross-sectional — Discussion — «The main limitation of our research is its cross-sectional and not longitudinal design.»
- gambling_disclosed: NR — Methods, Participants and Procedure — «IMAS invited 46,806 panel users to participate in the research.»
- betting_mode: online only — Methods, Participants and Procedure — «"Have you gambled for money on esports or virtual sports betting online over the past 12 months?"»
- pct_online: all — Methods, Participants and Procedure — «esports or virtual sports betting online over the past 12 months»
- pct_inplay: NR — NR — «NR»
- pct_dfs: NR — Table 3 — «9. Sports betting (including fantasy sports) | 193 | 44.1»
- pct_esports: all — Methods, Participants and Procedure — «The esports bettors sample consisted of 438 people aged 18 to 64»
- sports_lottery: no — Methods, Participants and Procedure — «"Have you gambled for money on esports or virtual sports betting online over the past 12 months?"»
- mixed_race: no — Methods, Participants and Procedure — «esports or virtual sports betting online»
- legal_status: regulated legal market — Introduction — «In Poland, in 2011, online bookmakers were legalized as the only form of online gambling. Currently (2021), it is also possible to bet on esports bettings, lot…»
- n_invited: 46806 — Methods, Participants and Procedure — «IMAS invited 46,806 panel users to participate in the research.»
- n_responded: 8511 — Methods, Participants and Procedure — «The invitation was accepted by 8511 (18.2%) of them.»
- response_rate: 18.2 — Methods, Participants and Procedure — «The invitation was accepted by 8511 (18.2%) of them.»
- age_mean: 33.1 — Methods, Participants and Procedure — «438 people aged 18 to 64 (M = 33.1, SD = 9.27)»
- age_sd: 9.27 — Methods, Participants and Procedure — «438 people aged 18 to 64 (M = 33.1, SD = 9.27)»
- age_min: 18 — Methods, Participants and Procedure — «438 people aged 18 to 64»
- age_max: 64 — Methods, Participants and Procedure — «438 people aged 18 to 64»
- age_group: adults — Methods, Participants and Procedure — «438 people aged 18 to 64»
- pct_male: 63 — Methods, Participants and Procedure — «Women constituted 37% and men 63% of respondents.»
- mode: online — Methods, Participants and Procedure — «The survey was conducted by an IMAS Internet panel among registered users.»
- weights: NR — Statistical Analysis — «Frequencies and percentages were used to describe categorical variables.»
- instruments: PGSI (Polish translation) — Measures, Gambling Disorder — «measured using the Polish translation of the Problem Gambling Severity Index (PGSI; Ferris et al., 2001)»
- instrument_validated_in_language: NR — Measures, Gambling Disorder — «the Polish translation of the Problem Gambling Severity Index (PGSI; Ferris et al., 2001)»
- industry_funding: NR — NR — «NR»
- funding_coi: NR (no funding or conflict-of-interest statement in the text provided) — NR — «NR»
- pub_status: journal — Header — «Journal of gambling studies; DOI: 10.1007/s10899-021-10015-4»
- language: English — Full text — «Online Gambling Activity, Pay-to-Win Payments, Motivation to Gamble and Coping Strategies as Predictors of Gambling Disorder Among e-sports Bettors»
- notes: Sample defined by online betting on 'esports or virtual sports' in the past 12 months; virtual sports (simulated events) are bundled with esports and cannot be separated, so eligibility needs reviewer judgement. Age and sex describe the 438 esports bettors. Data collection years not reported (IMAS 2019 is cited only to describe the panel). The PGSI response scale is printed as 0,1,3,4 (likely a typo for 0-3). 44.1% (193/438) also bet online on traditional sports (including fantasy sports) and 134 reported offline sports betting. The authors also group PGSI>=3 as 'pathological gamblers' and sa…

**Риск смещения (JBI):**
1. рамка выборки: **no** — The frame is registered users of one commercial online panel, which covers only part of Polish esports bettors. — Methods, Participants and Procedure — «The survey was conducted by an IMAS Internet panel among registered users.»
2. способ отбора: **no** — Non-probability, volunteer online panel with paid participation. — Methods, Participants and Procedure — «based on voluntary paid cooperation, following ESOMAR's research standards»
3. размер выборки: **yes** — 438 sports bettors, which is at least 385. — Methods, Participants and Procedure — «The esports bettors sample consisted of 438 people»
4. описание выборки и условий: **unclear** — Age, sex, setting and country are reported; dates of data collection are not. — Methods, Participants and Procedure — «438 people aged 18 to 64 (M = 33.1, SD = 9.27). Women constituted 37% and men 63% of respondents.»
5. охват (пропуски): **yes** — All 438 bettors are classified into the PGSI categories (78+86+121+153=438). — Results, Prevalence of Gambling Disorder — «17.8% (n = 78 ... 19.6% (n = 86 ... 27.6% (n = 121 ... 34.9% (n = 153»
6. валидность определения случая: **unclear** — PGSI with the standard 8+ cut-off, but the Polish translation has no cited validation and the response scale is misprinted. — Measures, Gambling Disorder — «Polish translation of the Problem Gambling Severity Index (PGSI; Ferris et al., 2001)... 8 and more—problem player.»
7. единое надёжное измерение: **yes** — Same instrument and online mode for everyone; reliability is reported for this sample. — Measures, Gambling Disorder — «The reliability of PGSI in the present study was α = 0.93.»
8. статистика (числитель и знаменатель): **yes** — Counts, denominator and 95% CIs are reported. — Results, Prevalence of Gambling Disorder — «34.9% (n = 153, 95%CI[30.6%, 39.5%])»
9. отклик: **no** — 18.2% acceptance, with no comparison of responders and non-responders and no weighting. — Methods, Participants and Procedure — «The invitation was accepted by 8511 (18.2%) of them.»

Правки:
- 

Проверено: да

---

## ST035 · Wardle 2021 · Addictive behaviors

Основной отчёт R4056: [текст](../../fulltext/text/R4056.txt) — «The impact of the initial Covid-19 lockdown upon regular sports bettors in Britain: Findings from a cross-sectional online study.» — [DOI](https://doi.org/10.1016/j.addbeh.2021.106876)
Приложен R3634: [текст](../../fulltext/text/R3634.txt) · [PDF](../../fulltext/pdf/R3634.pdf) — «Is the economic model of gambling dependent on problem gambling? Evidence from an online survey of regular sports betto…»
Приложен R3635: [текст](../../fulltext/text/R3635.txt) — «The association between gambling marketing and unplanned gambling spend: Synthesised findings from two online cross-sec…»
Связь отчётов: Betting and Gaming COVID-19 Impact Study, YouGov cohort of regular sports bettors in Britain: wave 1 (6-19 July 2020, n = 3,866) is reported in R4056; R3634 uses two waves (T0, T2) and R3635 uses wave 2 (November 2020) of the same cohort. Waves of one panel: the first wave enters (codebook)
Расхождения в тексте: (1) R4056 has 3,866 participants: 4,016 − 89 speeders − 61 implausible answers. R3634 has 3,865 at T0 and mentions only the 89 speeders. (2) R3634 Table 1 at T0 gives PGSI 3+ = 507, but the R4056 sex tables add up to 508 (289+59+135+25). PGSI 0 (2,670) and PGSI 1-2 (688) match exactly. (3) R3634 calls the T0 data the pre-pandemic period. The wave-1 PGSI, however, refers to the 3-month lockdown (mid-March to mid-June 2020), as R4056 and R3634 both state. (4) R4056 gives weighted percentages with unweighted counts; R3634 does not use weights. (5) There are small errors in R4056 Table 3a: the age band percentages (35.5% is printed twice) and conflict 'About the same 2087 (14.9%)'. Neither affects the PGSI counts. (6) In R3634 the T0 mean spend for PGSI 3+ is £1050.10 in the text but £1010.50 in Table 1; this is not relevant to prevalence.
Заметка ИИ: The whole-sample PGSI estimates were derived by adding the male and female counts in R4056 Tables 2a/2b. R4056 gives weighted percentages only by sex. The PGSI time frame is 3 months (the initial lockdown) rather than the usual 12 months, so the review may want to treat this sample in a sensitivity analysis. Sampling was coded quota (non-probability YouGov panel); there is no explicit quota design.

### ST035-1 · YouGov cohort of regular sports bettors, Great Britain, wave 1 (6-19 July 2020), n=3,866
Отчёты: R4056 (main); R3634; R3635

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | PGSI · PGSI 0 | **below** | **2670 / 3866** | 69.1 | Table 2a; Table 2b | «Non-problem gambling (0) (n = 2096) [men]; Non-problem gambling (0) (n = 574) [women]» |
| E2 | all | PGSI · PGSI 1-2 | **L1** | **688 / 3866** | 17.8 | Table 2a; Table 2b | «Low risk gambling (1–2)(n = 564) [men]; Low risk gambling (1–2)(n = 124) [women]» |
| E3 | all | PGSI · PGSI 3-7 | **L2** | **348 / 3866** | 9.0 | Table 2a; Table 2b | «Moderate risk gambling (3–7) (n = 289) [men]; Moderate risk gambling (3–7) (n = 59) [women]» |
| E4 | all | PGSI · PGSI>=8 | **L3** | **160 / 3866** | 4.1 | Table 2a; Table 2b | «Problem gambling (8 + )(n = 135) [men]; Problem gambling (8 + )(n = 25) [women]» |
| E5 | all | PGSI · PGSI>=3 | **L2** | **507 / 3865** | 13.1 | R3634, p.8, Table 1 (T0) | «Moderate risk/ problem gambling (score 3 +) 507 13.1% ... All 3865 100%» |
| E6 | male | PGSI · PGSI 0 | **below** | **2096 / 3084** | 68.0 | Table 2a | «Non-problem gambling (0) (n = 2096)... All male regular sports bettors 64.7» |
| E7 | male | PGSI · PGSI 1-2 | **L1** | **564 / 3084** | 18.3 | Table 2a | «Low risk gambling (1–2)(n = 564)... 19.3» |
| E8 | male | PGSI · PGSI 3-7 | **L2** | **289 / 3084** | 9.4 | Table 2a; Results | «Moderate risk gambling (3–7) (n = 289)... A further 10.7% of men and 8.3% of women experienced moderate risk gambling» |
| E9 | male | PGSI · PGSI>=8 | **L3** | **135 / 3084** | 4.4 | Table 2a; Results | «Problem gambling (8 + )(n = 135)... 5.4% of male sports bettors (Table 2a)... experienced problem gambling (PGSI score ≥ 8)» |
| E10 | female | PGSI · PGSI 0 | **below** | **574 / 782** | 73.4 | Table 2b | «Non-problem gambling (0) (n = 574)... All female regular sports bettors 71.2 (67.6–74.6)» |
| E11 | female | PGSI · PGSI 1-2 | **L1** | **124 / 782** | 15.9 | Table 2b | «Low risk gambling (1–2)(n = 124)... 16.6 (14.0–19.7)» |
| E12 | female | PGSI · PGSI 3-7 | **L2** | **59 / 782** | 7.5 | Table 2b | «Moderate risk gambling (3–7) (n = 59)... 8.3 (6.4–10.7)» |
| E13 | female | PGSI · PGSI>=8 | **L3** | **25 / 782** | 3.2 | Table 2b; Results | «Problem gambling (8 + )(n = 25)... 3.9 (2.5–5.9)» |

- E1: cumulative: no; источник порога: standard; правило: PGSI row; score 0 is below L1; у авторов: «Non-problem gambling»; главная у авторов: no; период: past 3 months; **расчёт: Men 2096 + women 574 = 2670; n = 3084 + 782 = 3866**; заметка: R3634 Table 1 (T0) gives 2670/3865 = 69.1% unweighted. PGSI 0 also covers people who did not gamble during lockdown.
- E2: cumulative: no; источник порога: standard; правило: PGSI row; 1-2 band starts at L1; у авторов: «Low risk gambling»; главная у авторов: no; период: past 3 months; **расчёт: Men 564 + women 124 = 688**; заметка: R3634 Table 1 (T0): 688 (17.8%).
- E3: cumulative: no; источник порога: standard; правило: PGSI row; 3-7 band starts at L2; у авторов: «Moderate risk gambling»; главная у авторов: no; период: past 3 months; **расчёт: Men 289 + women 59 = 348**
- E4: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ = L3; у авторов: «Problem gambling»; главная у авторов: no; период: past 3 months; **расчёт: Men 135 + women 25 = 160**; заметка: The authors give the main prevalence by sex only; the whole-sample figure here is aggregated across sexes, not across score bands.
- E5: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 = L2; у авторов: «Moderate risk/problem gambling (score 3+)»; главная у авторов: no; период: past 3 months; заметка: This is a study-reported cumulative from R3634 for the same wave-1 data (unweighted). It differs by 1 from the R4056 sum (289+59+135+25 = 508; n 3866). Labelled T0 in R3634, but the PGSI refers to the lockdown period.
- E6: cumulative: no; источник порога: standard; правило: PGSI row; score 0 is below L1; у авторов: «Non-problem gambling»; главная у авторов: no; период: past 3 months; взвешенная доля: 64.7; заметка: Counts are unweighted; the percentage is weighted.
- E7: cumulative: no; источник порога: standard; правило: PGSI row; 1-2 band starts at L1; у авторов: «Low risk gambling»; главная у авторов: no; период: past 3 months; взвешенная доля: 19.3
- E8: cumulative: no; источник порога: standard; правило: PGSI row; 3-7 band starts at L2; у авторов: «Moderate risk gambling»; главная у авторов: no; период: past 3 months; взвешенная доля: 10.7
- E9: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ = L3; у авторов: «Problem gambling»; главная у авторов: yes; период: past 3 months; взвешенная доля: 5.4; заметка: Unweighted 135/3084 = 4.4%.
- E10: cumulative: no; источник порога: standard; правило: PGSI row; score 0 is below L1; у авторов: «Non-problem gambling»; главная у авторов: no; период: past 3 months; взвешенная доля: 71.2
- E11: cumulative: no; источник порога: standard; правило: PGSI row; 1-2 band starts at L1; у авторов: «Low risk gambling»; главная у авторов: no; период: past 3 months; взвешенная доля: 16.6
- E12: cumulative: no; источник порога: standard; правило: PGSI row; 3-7 band starts at L2; у авторов: «Moderate risk gambling»; главная у авторов: no; период: past 3 months; взвешенная доля: 8.3
- E13: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ = L3; у авторов: «Problem gambling»; главная у авторов: yes; период: past 3 months; взвешенная доля: 3.9; заметка: Unweighted 25/782 = 3.2%.

**⚠ Проверка скриптом (обратите внимание):**
- E5: n оценки не равно n_bettors выборки (3866): проверьте знаменатель

**Ключевые поля выборки:**
- **n_bettors: 3866** — Statistical analysis — «Hence, 3866 participants (3084 men, 782 women) were included in the main analyses.»
- **sample_type: bettor_recruited** — Methods, Design — «The survey was conducted by YouGov who recruited a cohort of sport bettors from their existing non-probabilistic panel of one million people.»
- **sampling: quota** — Methods, Design; Sample and eligibility — «YouGov's panel contains information on members, allowing us to target specific panellists... YouGov identified 19,237 eligible panellists who were sent e-mail invitations.»
- **betting_period: past 12 months** — R3634, p.4 (Design); R4056 Sample and eligibility — «they had gambled at least monthly on sports (including horse and dog races) in the year prior to the pandemic»

**Остальные поля:**
- parent_population: NA — Methods, Design — «recruited a cohort of sport bettors from their existing non-probabilistic panel of one million people»
- min_frequency: at least monthly (regular) per YouGov panel profile; plus bet on sports/horse racing in Dec 2019-Feb 2020 — Methods, Sample and eligibility — «to have previously reported betting on sports (including horse racing) at least monthly... only those who reported betting on sporting events (including horse …»
- country: GBR — Methods, Sample and eligibility — «To be eligible, panellists had to be aged 18 or over, living in Britain»
- subnational: NA — Methods, Sample and eligibility — «living in Britain»
- data_years: 2020 — Methods, Design — «A cohort of regular sports bettors from Britain completed an online survey between 6th and 19th July 2020 (n = 3,866)»
- design: cohort baseline — Methods, Design — «represent the first wave of longitudinal assessment of how the pandemic has impacted on 'regular' sports betters»
- gambling_disclosed: NR — Methods, Design — «YouGov identified 19,237 eligible panellists who were sent e-mail invitations.»
- betting_mode: both — Table 1a/1b — «Online sports betting 2327 78.7 ... Betting on sports in a bookmakers 806 26.7»
- pct_online: NR — Table 1a/1b — «Prior to lockdown online sports betting was the most commonly reported gambling activity (78.7% men, 61.4% women).»
- pct_inplay: NR — NA — «NR»
- pct_dfs: NR — NA — «NR»
- pct_esports: NR — Table 1a/1b — «Online betting on esports 71 2.8 (2.2–3.6) [men]; 16 2.4 (1.5–4.1) [women]»
- sports_lottery: unclear — Table 1a/1b — «Football pools 252 8.6 (7.6–9.8)»
- mixed_race: yes — Methods, Sample and eligibility — «have previously reported betting on sports (including horse racing) at least monthly»
- legal_status: regulated legal market — Introduction — «The British regulator, the Gambling Commission (GC), identified transitions to different forms of gambling, especially faster (online) forms of gambling, as an…»
- n_invited: 19237 — Methods, Sample and eligibility — «In total, YouGov identified 19,237 eligible panellists who were sent e-mail invitations.»
- n_responded: 4016 — Statistical analysis — «Data were obtained from 4016 participants.»
- response_rate: 20.9 — Methods, Sample and eligibility; Statistical analysis — «YouGov identified 19,237 eligible panellists who were sent e-mail invitations. Of those who accessed the initial information and consent page using the e-mail …»
- age_mean: NR — NA — «NR»
- age_sd: NR — NA — «NR»
- age_min: 18 — Methods, Sample and eligibility — «panellists had to be aged 18 or over»
- age_max: NR — NA — «NR»
- age_group: adults — Methods, Sample and eligibility — «panellists had to be aged 18 or over»
- pct_male: 79.8 — Statistical analysis — «3866 participants (3084 men, 782 women)»
- mode: online — Methods, Design — «completed an online survey between 6th and 19th July 2020»
- weights: yes — Statistical analysis — «All estimates were weighted to match the age, sex, regional and sports betting profile of the broader sample of regular sports bettors within the YouGov panel.…»
- instruments: PGSI (English, 9 items, 3-month reference period = initial lockdown mid-March to mid-June 2020) — Methods, Problem gambling — «Participants completed the 9-item Problem Gambling Severity Index (PGSI) (Ferris & Wynne, 2001)... we purposively used a three month reference period»
- instrument_validated_in_language: yes — Methods, Problem gambling — «Participants completed the 9-item Problem Gambling Severity Index (PGSI) (Ferris & Wynne, 2001) scored on a four-point scale (0 = Never to 3 = Almost always).»
- industry_funding: no — Funding — «This work is supported by a grant from UK Research and Innovation (Economic and Social Research Council), grant number ES/V004549/1.»
- funding_coi: ESRC/UKRI grant ES/V004549/1; HW was paid by Gambling Commission (regulator) as ABSG deputy chair, past GambleAware-funded work by HW and others; funders had no role — Funding; Conflicts of Interest — «HW was Deputy Chair of the Advisory Board for Safer Gambling... remunerated by the Gambling Commission... The funders have no role in the design of the study»
- pub_status: journal — Header — «Year: 2021; venue: Addictive behaviors; DOI: 10.1016/j.addbeh.2021.106876»
- language: English — Full text — «The impact of the initial Covid-19 lockdown upon regular sports bettors in Britain: Findings from a cross-sectional online study»
- notes: pct_male = 3084/3866 (whole sample = sports bettors). No age mean; male age bands 55+ 1387, 35-54 1296, <35 401. Response 20.9% = 4016/19237; 78% of those who opened the consent page completed. Includes horse racing (mixed_race). Inclusion: bet on sports/horses Dec 2019-Feb 2020 and at least monthly by panel profile (R3634: year before pandemic); coded past 12 months as nearest option. The PGSI 3-month frame = lockdown, when sport was suspended and ~30% stopped gambling, so PGSI 0 includes non-gamblers. Later waves: wave 2 Nov 2020 (3195 retained; 2980 gambled). R3634 T2: PGSI 0 2040, 1-2 520…

**Риск смещения (JBI):**
1. рамка выборки: **no** — The frame is YouGov panel members flagged as regular sports bettors, so it covers only part of the regular sports bettors in Britain. — Methods, Design — «recruited a cohort of sport bettors from their existing non-probabilistic panel of one million people»
2. способ отбора: **no** — Participants came from a non-probability online panel through targeted invitations. — Discussion — «Participants were recruited from a non-probability online panel, with consequent issues for generalisability.»
3. размер выборки: **yes** — n = 3,866, which is at least 385. — Statistical analysis — «3866 participants (3084 men, 782 women) were included in the main analyses»
4. описание выборки и условий: **yes** — The report gives sex, age (eligibility 18+ and age bands), setting (YouGov online panel), country and dates. — Design; Table 3a — «completed an online survey between 6th and 19th July 2020»
5. охват (пропуски): **yes** — Missing data are described as minimal, and the PGSI categories add up to the full n by sex. 150 people were excluded for quality reasons (3.7%). — Statistical analysis; Table 2a/2b — «Missing data within this final sample were minimal and are excluded unless explicitly stated.»
6. валидность определения случая: **yes** — The PGSI was used with its standard thresholds in the original English version. The reference period was changed to 3 months (lockdown). — Methods, Problem gambling — «a score of 8 or more is indicative of problem gambling... we purposively used a three month reference period»
7. единое надёжное измерение: **yes** — Everyone answered the same online PGSI with the same time frame, and reliability is reported. — Methods, Problem gambling — «In our sample, the composite score had strong internal consistency (Cronbach's α = 0.91).»
8. статистика (числитель и знаменатель): **yes** — Unweighted counts and weighted percentages are given by sex, with CIs for women. Complex survey weights were applied. — Table 2a/2b; Statistical analysis — «Problem gambling (8 + )(n = 135)... All bi-variate analyses were performed using the complex survey module in SPSS v25.»
9. отклик: **yes** — Response was low (4,016 of 19,237 invited = 20.9%), but the data were weighted for non-response using panel profile information. — Discussion — «a strength of sampling from YouGov's panel of known sports bettors is that we could weight data for non-response by age, sex, geography and gambling behaviour»

Правки:
- # E5 n=3865 from linked report R3634 (T0 baseline)

Проверено: да

---

## ST036 · Yüce 2021 · International Journal of Mental Health and Addiction

Основной отчёт R4080: [текст](../../fulltext/text/R4080.txt) · [PDF](../../fulltext/pdf/R4080.pdf) — «Effects of Sports Betting Motivations on Sports Betting Addiction in a Turkish Sample» — [DOI](https://doi.org/10.1007/s11469-021-00563-6)
Не выписано ИИ: Study 1 interviews (n=30 male bettors in betting shops): qualitative, no problem-gambling measure. Study 1 pilot / Study 2 PSBSI validation sample (n=251, 91.23% male, regular sports bettors in the past 12 months): PSBSI given, but only psychometrics reported, with no prevalence by category. Study 1 CFA sample (n=230): SBMS only, no problem-gambling measure.
Расхождения в тексте: 1) Abstract sample sizes disagree with the Methods. The abstract gives Study 1 n=281 and Study 2 n=230; the Methods give Study 1 n=30+251 and n=230, and say Study 2 used the n=251 sample. 2) Sex: text 89.2% male (p.10) and 89.3% (p.11) vs Table 5 89.3%; table used. 3) Text descriptives differ from Table 5. Education: text 55%/41.7%, table 55.5/41.4. Income: text "medium (22.2%) and high (35.5%)", table low 22.2, middle 42.1, high 35.6. Frequency 2-3 times per week: text 43.7%, table 43.4%. 4) Stated PSBSI scoring (0-3 per item, 0-27 total) conflicts with the observed range of 9-27 for all participants. Table 6 counts add up to 643.
Заметка ИИ: One eligible sample (Study 3, n=643). All estimates are coded adhoc/not_levelled because the levels table notes class the Turkish PSBSI as having non-standard scoring (total 9-27). Zero-count categories were derived from the reported 9-27 score range.

### ST036-1 · Turkey, sports fans who bet regularly (Study 3), Jan-May 2019, n=643
Отчёты: R4080 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | adhoc · PSBSI>=8 (stated 0-27 scoring; observed range 9-27) | **not_levelled** | **643 / 643** | 100.0 | Page 11, Results; Page 12, Table 6 | «The PSBSI score of all (100%) sports bettors participating in the survey is between 9-27 ... Accordingly, it can be stated that all participants are at risk of sports betting addiction» |
| E2 | all | adhoc · PSBSI 3-7 | **not_levelled** | **0 / 643** | 0.0 | Page 11; Page 12, Table 6 | «The PSBSI score of all (100%) sports bettors participating in the survey is between 9-27.» |
| E3 | all | adhoc · PSBSI 1-2 | **not_levelled** | **0 / 643** | 0.0 | Page 11; Page 12, Table 6 | «The PSBSI score of all (100%) sports bettors participating in the survey is between 9-27.» |
| E4 | all | adhoc · PSBSI 0 | **not_levelled** | **0 / 643** | 0.0 | Page 11; Page 12, Table 6 | «The PSBSI score of all (100%) sports bettors participating in the survey is between 9-27.» |

- E1: cumulative: yes; источник порога: standard; правило: adhoc row: levels table notes list Turkish PSBSI (items 1-3, total 9-27) as adhoc -> not levelled; у авторов: «problem sports bettors ("all participants are at risk of sports betting addicti…»; главная у авторов: yes; период: past 12 months; **расчёт: Sum of Table 6 counts for scores 9-27: 80+46+44+32+21+20+29+30+26+30+35+41+42+42+37+31+29+11+17 = 643 (all scores >=8)**; заметка: 100% is probably a scoring artefact: the minimum possible score appears to be 9.
- E2: cumulative: no; источник порога: standard; правило: adhoc row: Turkish PSBSI non-standard scoring -> not levelled; у авторов: «moderate-risk sports bettors»; главная у авторов: no; период: past 12 months; **расчёт: No scores below 9 in Table 6 (all 643 scored 9-27), so 0 cases**; заметка: Category defined in the paper, but no participant fell in it.
- E3: cumulative: no; источник порога: standard; правило: adhoc row: Turkish PSBSI non-standard scoring -> not levelled; у авторов: «low-risk sports bettors»; главная у авторов: no; период: past 12 months; **расчёт: No scores below 9 in Table 6, so 0 cases**; заметка: Category defined in the paper, but no participant fell in it.
- E4: cumulative: no; источник порога: standard; правило: adhoc row: Turkish PSBSI non-standard scoring -> not levelled; у авторов: «non-problem (Table 6 note: non-addictive) sports bettors»; главная у авторов: no; период: past 12 months; **расчёт: No scores below 9 in Table 6, so 0 cases**; заметка: Category defined in the paper, but no participant fell in it.

**Ключевые поля выборки:**
- **n_bettors: 643** — Page 12, Table 6 — «PSBSI scores of the participants ... 9.00 80 12.4 16.88; 5.57»
- **sample_type: bettor_recruited** — Page 10, Study 3 Participants and Procedure — «the participants were told that they would be included in the research if they were primarily interested in sports and bet on sports regularly»
- **sampling: convenience** — Page 10, Study 3 Participants and Procedure — «Judgement sampling was used in this study and the data were collected between January 2019 and May 2019 both online and face-to-face.»
- **betting_period: past 12 months** — Page 10 — «who live in Turkey and bet on sports regularly for last 12 months»

**Остальные поля:**
- parent_population: NA — Page 10 — «data were collected from sport fans (n=643 ...) who live in Turkey and bet on sports regularly»
- min_frequency: "regularly" (not defined); lowest frequency category in Table 5 = once in a couple of weeks — Page 10; Page 12, Table 5 — «bet on sports regularly for last 12 months ... Once in a couple of weeks 101 15.7»
- country: TUR — Page 10, Study 3 Participants and Procedure — «data were collected from sport fans (n=643 ...) who live in Turkey and bet on sports regularly for last 12 months»
- subnational: NA — Page 10 — «who live in Turkey and bet on sports regularly for last 12 months»
- data_years: 2019 — Page 10, Study 3 Participants and Procedure — «the data were collected between January 2019 and May 2019 both online and face-to-face»
- design: cross-sectional — Page 10, Study 3 — «Study 3 (Exploratory Study, Effects of Sports Betting Motivations on Sports Betting Addiction)»
- gambling_disclosed: yes — Page 10, Study 3 Participants and Procedure — «the participants were told that they would be included in the research if they were primarily interested in sports and bet on sports regularly. The participant…»
- betting_mode: both — Page 12, Table 5 — «Sports Betting Platform Betting Shops 295 45.9 Websites 348 54.1»
- pct_online: 54.1 — Page 12, Table 5 — «Websites 348 54.1»
- pct_inplay: NR — NR — «NR»
- pct_dfs: NR — NR — «NR»
- pct_esports: NR — NR — «NR»
- sports_lottery: unclear — NR — «NR»
- mixed_race: no — Page 10 — «bet on sports regularly for last 12 months»
- legal_status: mixed — Page 3 — «about 5 million people aged 18 and over are betting on sports legally in Turkey, and in addition to this, almost 5 million people are betting on sports illegal…»
- n_invited: NR — NR — «NR»
- n_responded: 643 — Page 10 — «data were collected from sport fans (n=643, 574 males and 69 females»
- response_rate: NR — NR — «NR»
- age_mean: 27.39 — Page 10 — «Mage = 27.39 years; SD = 7.89»
- age_sd: 7.89 — Page 10 — «Mage = 27.39 years; SD = 7.89»
- age_min: 18 — Page 10 — «range 18–51»
- age_max: 51 — Page 10 — «range 18–51»
- age_group: adults — Page 10; Table 5 — «range 18–51»
- pct_male: 89.3 — Page 12, Table 5 — «Gender Male 574 89.3 Female 69 10.7»
- mode: mixed — Page 10 — «the data were collected between January 2019 and May 2019 both online and face-to-face»
- weights: NR — Page 11, Data Analysis — «percentage-frequency and arithmetic averages for the scores received from the sports betting addiction index were examined»
- instruments: PSBSI (Problem Sports Betting Severity Index), PGSI (Ferris & Wynne 2001) items reworded for sports betting, Turkish version (Brislin back-translation) — Page 10, Instruments; Page 8-9, Study 2 — «The PSBSI is an adapted and validated Turkish version of the Problem Gambling Severity Index (PGSI; Ferris and Wynne 2001) where the words “gambling” and “bet”…»
- instrument_validated_in_language: yes — Page 9, Study 2 Results — «it was determined that PSBSI has similar psychometric features as PGSI and in this study, it can be used to determine the risks of individuals' sports betting …»
- industry_funding: NR — Page 18, Declarations — «Conflict of Interest The authors declare no competing interests.»
- funding_coi: No funding statement; authors declare no competing interests — Page 18, Declarations — «Conflict of Interest The authors declare no competing interests.»
- pub_status: journal — Page 1 — «International Journal of Mental Health and Addiction (2022) 20:3022–3043»
- language: English — Page 1 — «Effects of Sports Betting Motivations on Sports Betting Addiction in a Turkish Sample»
- notes: Age and sex describe the whole Study 3 sample (all are sports bettors). Text says 89.2% male; Table 5 says 89.3% (574/643); table value used. The Turkish PSBSI was validated in Study 2 of this same article (n=251, alpha=.901), not in a separate publication. Stated scoring is 0-3 per item (0-27 total), but all 643 scored 9-27 (minimum = 9 items x 1). This points to 1-3 item coding, and the levels table lists the Turkish PSBSI as adhoc (total 9-27). So all estimates are coded adhoc/not_levelled, and the 100% 'problem sports bettor' figure is probably an artefact of the scoring. The data likely …

**Риск смещения (JBI):**
1. рамка выборки: **no** — Sports fans recruited by judgement sampling, online and face-to-face. The frame does not cover Turkish sports bettors, and the authors say the results cannot be generalised. — Page 10; Page 17, Limitations — «these findings cannot be generalized to all sports bettors»
2. способ отбора: **no** — Judgement (non-probability) sampling of volunteers. — Page 10 — «Judgement sampling was used in this study»
3. размер выборки: **yes** — 643 sports bettors, which is at least 385. — Page 10 — «data were collected from sport fans (n=643»
4. описание выборки и условий: **yes** — Age, sex, country, dates and online/face-to-face setting are all reported. — Page 10; Table 5 — «between January 2019 and May 2019 both online and face-to-face ... Mage = 27.39 years ... 89.2% male»
5. охват (пропуски): **yes** — The PSBSI score distribution in Table 6 adds up to all 643 participants, so no PGSI data are missing. — Page 12, Table 6 — «9.00 80 12.4 ... 27.00 17 2.6»
6. валидность определения случая: **no** — The observed scores (9-27) do not match the stated 0-27 scoring, which suggests non-standard item coding. The levels table classes the Turkish PSBSI as adhoc, so the standard PGSI threshold is not validly applied. — Page 11, Results — «The PSBSI score of all (100%) sports bettors participating in the survey is between 9-27.»
7. единое надёжное измерение: **no** — Data were collected both online and face-to-face with no check for mode effects. Reliability was reported only for the Study 2 sample, not for this sample. — Page 10; Page 9 — «data were collected between January 2019 and May 2019 both online and face-to-face»
8. статистика (числитель и знаменатель): **yes** — Table 6 gives counts with denominator 643, so a CI can be calculated. Weights are not required for this design. — Page 12, Table 6 — «Problem Sports Betting Severity Index Scores* n %»
9. отклик: **no** — Volunteer sample with no denominator of people invited; response rate not reported. — Page 10 — «asked whether they volunteered to participate in the study»

Правки:
- 

Проверено: да

---

## ST037 · Anyanwu 2020 · Research Square

Основной отчёт R4132: [текст](../../fulltext/text/R4132.txt) · [PDF](../../fulltext/pdf/R4132.pdf) — «Prevalence and Correlates of Gambling Disorder Among Secondary School Students in Mbarara Municipality, Uganda.» — [DOI](https://doi.org/10.21203/rs.3.rs-25227/v1)
Расхождения в тексте: 1. Table 2 gives 109 (68.6%) with GD bet on sports, but 109/160 = 68.1%, so the printed percentage implies a denominator of about 159. 2. In Table 3, sports betting is 148 + 28 = 176, while Table 2 gives 177. 3. In Table 1, the subgroup counts do not add up to the column totals (e.g., age 481 + 332 = 813 of 905; ever-gambled by age 178 + 145 = 323 of 362; GD by age 59 + 78 = 137 of 160). The Guardian 'Parents' row in the ever-gambled column, 91 (91.0), is implausible. 4. In the text, '64.1% ... of the male students had ever gambled' actually refers to the column share (230/359), not the share of male students. 5. The cut-off of >=4 is cited to DSM-5 (ref 48), not to Fisher 2000.
Заметка ИИ: There is one eligible sample: pupils who had ever bet on sports, taken from a school survey with cluster random sampling. The estimate comes from Table 2, which gives activity participation for ever-gamblers and for those with gambling disorder. Gambling disorder was measured for gambling in general, using the DSM-IV-MR-J with a cut-off of 4 or more.

### ST037-1 · Secondary school pupils who ever bet on sports, Mbarara Municipality, Uganda, 2019 (n=177)
Отчёты: R4132 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | DSM-IV-MR-J · DSM-IV-MR-J>=4 (range 0-9) | **L3** | **109 / 177** | 61.6 | Page 11, Table 2; Page 10 text | «Sports betting 177 (49.0) 109 (68.6)» |
| E2 | all | DSM-IV-MR-J · DSM-IV-MR-J 0-3 (range 0-9) | **below** | **68 / 177** | 38.4 | Page 11, Table 2; Page 7, Measures | «Sports betting 177 (49.0) 109 (68.6); A score of 0–3 was classified as "no gambling disorder"» |

- E1: cumulative: yes; источник порога: standard; правило: DSM-IV-MR-J row; >=4 is L3; у авторов: «gambling disorder»; главная у авторов: no; период: NR; **расчёт: Table 2 cross-tabulation: 177 of 362 ever-gamblers bet on sports (Ever Gambled column, which includes those with GD); 109 of 160 with GD bet on sports -> cases…**; заметка: The authors' main estimate is GD in all 905 pupils (17.7%) and in all ever-gamblers (44.2%). The DSM-IV-MR-J covers gambling in general. 109/160 = 68.1%, but 68.6% is printed.
- E2: cumulative: no; источник порога: standard; правило: DSM-IV-MR-J row; 0-3 band starts at 0 (below L1); у авторов: «no gambling disorder»; главная у авторов: no; период: NR; **расчёт: 177 sports bettors - 109 with GD = 68**; заметка: This is the complement of the GD category. Score bands 1-3 are not reported separately.

**Ключевые поля выборки:**
- **n_bettors: 177** — Page 11, Table 2 — «Sports betting 177 (49.0) 109 (68.6)»
- **sample_type: school_pupils** — Page 6, Methods — «a total of 921 students from 12 schools were randomly selected using multi-stage cluster random sampling»
- **sampling: probability** — Page 6, Methods — «921 students from 12 schools were randomly selected using multi-stage cluster random sampling... at least 60 students were randomly selected with 10 students from each class using the class register»
- **betting_period: lifetime** — Page 11, Table 2 — «Gambling Activity / Ever Gambled n (%) ... Sports betting 177 (49.0)»

**Остальные поля:**
- parent_population: Secondary school students in Mbarara Municipality, Uganda (about 35 schools, 11,106 enrolled) — Page 6, Methods — «There were about 35 secondary schools with a total enrollment of 11,106 students in the municipality»
- min_frequency: none — Page 11, Table 2 — «Ever Gambled ... Sports betting 177 (49.0)»
- country: UGA — Page 6, Methods — «A cross-sectional study was conducted among secondary school students in Mbarara Municipality Uganda, in 2019.»
- subnational: Mbarara Municipality — Page 6, Methods — «secondary school students in Mbarara Municipality Uganda»
- data_years: 2019 — Page 6, Methods — «secondary school students in Mbarara Municipality Uganda, in 2019»
- design: cross-sectional — Page 6, Methods — «A cross-sectional study was conducted among secondary school students»
- gambling_disclosed: NR — Page 6, Methods — «They explained the objectives of the study to the students and assured them that all information was anonymous»
- betting_mode: NR — Page 11, Table 2 — «Internet/online 43 (11.9)»
- pct_online: NR — Page 11, Table 2 — «Internet/online 43 (11.9)»
- pct_inplay: NR — NA
- pct_dfs: NR — NA
- pct_esports: NR — NA
- sports_lottery: no — Page 11, Table 2 — «Sports betting 177 (49.0) ... Pool betting 81 (22.4) ... National lottery/play lotto 3 (0.8)»
- mixed_race: no — Page 11, Table 2 — «Sports betting 177 (49.0) ... Betting on animals 44 (12.2)»
- legal_status: regulated legal market — Page 3, Background — «The NGB was established to guide the conduct of gambling activities, provide for licensing and regulation of gaming and betting activities. According to the lo…»
- n_invited: NR — Page 6, Methods — «a total of 921 students from 12 schools were randomly selected»
- n_responded: 921 — Page 8, Results — «Out of the 921 questionnaires returned, 905 questionnaires were included in the analyses»
- response_rate: NR — Page 6, Ethical Considerations — «The decision of students who were not willing to participate was respected.»
- age_mean: 16.9 — Page 8, Results — «The participants had a mean age of 16.9 ± 2.2 years, and 59.2% were aged below 18 years.»
- age_sd: 2.2 — Page 8, Results — «mean age of 16.9 ± 2.2 years»
- age_min: NR — NA
- age_max: NR — NA
- age_group: mixed — Page 9, Table 1 — «Below 18 years 481 (59.2) / 18 years and above 332 (40.8)»
- pct_male: 53.8 — Page 8, Results; Table 1 — «53.8% of the students were male»
- mode: paper — Page 6, Methods — «Research assistants that had been trained, administered the paper and pencil questionnaire.»
- weights: NR — Page 6, Methods — «adjustments were made for the clustering effect of schools with an intra cluster correlation ... ICC of 0.014»
- instruments: DSM-IV-MR-J (language version not stated) — Page 7, Measures — «measured based on the Diagnostic and Statistical Manual of Mental Health Fourth Version Adapted for Juveniles Multiple Response (DSM-IV-MR-J) scores»
- instrument_validated_in_language: NR — Page 7, Measures — «The DSM-IV-MR-J instrument has been shown to be reliable and valid among young people with a Cronbach's alpha value of 0.75 (47).»
- industry_funding: no — Page 21, Funding — «This research was funded by the Queen Elizabeth Commonwealth Scholarship.»
- funding_coi: Queen Elizabeth Commonwealth Scholarship; authors declare no competing interests — Page 21, Declarations — «The authors declare that they have no competing interests. ... This research was funded by the Queen Elizabeth Commonwealth Scholarship.»
- pub_status: preprint — Page 1 — «Research Square ... Posted Date: May 14th, 2020»
- language: English — Page 1 — «Prevalence and Correlates of Gambling Disorder Among Secondary School Students in Mbarara Municipality, Uganda.»
- notes: Sports bettors = ever-gamblers (lifetime) who reported sports betting (Table 2); 148 of them last gambled on sports within the past year (Table 3). Gambling disorder (DSM-IV-MR-J >=4) is measured for gambling in general, not for sports betting specifically. Age (mean 16.9, SD 2.2) and % male (53.8%) describe the whole sample of 905 pupils, not the sports bettors. Language of the questionnaire is not stated; DSM-IV-MR-J validation cited is Fisher 2000 (English). The authors cite DSM-5 (ref 48) for the >=4 cut-off. Betting is illegal for persons under 25 under the 2016 Act, so all pupils' betti…

**Риск смещения (JBI):**
1. рамка выборки: **yes** — Frame was the list of schools from the Municipal Education Office and the class registers, which covers secondary pupils in the municipality. — Page 6, Methods — «A list of schools in Mbarara Municipality was obtained from Mbarara Municipal Education Office ... 10 students from each class using the class register»
2. способ отбора: **yes** — Parent survey used multi-stage cluster random sampling of schools and pupils. — Page 6, Methods — «921 students from 12 schools were randomly selected using multi-stage cluster random sampling»
3. размер выборки: **no** — 177 sports bettors, which is below 385. — Page 11, Table 2 — «Sports betting 177 (49.0)»
4. описание выборки и условий: **yes** — Age, sex, school setting, country and year were reported (for the whole sample). — Pages 6, 8 — «in Mbarara Municipality Uganda, in 2019 ... mean age of 16.9 ± 2.2 years ... 53.8% of the students were male»
5. охват (пропуски): **yes** — Only 16 of 921 questionnaires (1.7%) were excluded for missing gambling information. — Page 8, Results — «905 questionnaires were included in the analyses and 16 questionnaires were excluded as they were returned incomplete and had missing information on gambling»
6. валидность определения случая: **unclear** — DSM-IV-MR-J with its standard cut-off of >=4, but the language version is not stated and the cut-off is attributed to DSM-5. — Page 7, Measures — «A score of 0–3 was classified as "no gambling disorder" and a score of 4 and above classified as "gambling disorder" (48).»
7. единое надёжное измерение: **yes** — One self-administered paper questionnaire for all pupils; reliability is cited from the source (alpha 0.75). — Pages 6-7 — «administered the paper and pencil questionnaire ... reliable and valid among young people with a Cronbach's alpha value of 0.75 (47)»
8. статистика (числитель и знаменатель): **yes** — Numerator (109) and denominator (177) for sports bettors can be traced in Table 2 and a CI can be calculated, though the printed percentages are slightly inconsistent and clustering is not applied to the prevalence. — Page 11, Table 2 — «Sports betting 177 (49.0) 109 (68.6)»
9. отклик: **unclear** — Refusals and the number invited were not reported; 921 questionnaires were returned. — Page 8, Results — «Out of the 921 questionnaires returned, 905 questionnaires were included»

Правки:
- 

Проверено: да

---

## ST038 · Håkansson 2020 · Frontiers in psychology

Основной отчёт R4314: [текст](../../fulltext/text/R4314.txt) — «Impact of COVID-19 on Online Gambling - A General Population Survey During the Pandemic.» — [DOI](https://doi.org/10.3389/fpsyg.2020.568543)
⚠ Возможное пересечение (держим раздельно; если видите общие данные — напишите в «Правки»): possible overlap with R4315 (ST039): Both Ipsos web panel samples of Swedish online gamblers (Hakansson); R4314 (May 2020, N = 997) says it repeats the recruitment of an earlier study, probably R4315 (N = 1,004): different years, panel members may overlap
Не выписано ИИ: The whole sample of 997 online gamblers is not extracted as a sports-betting sample; only its past-year sports bettors (n=619) are. No samples were recruited for gambling problems. The 7% with a history of Spelpaus self-exclusion are part of the panel sample, not a separately recruited group.
Расхождения в тексте: The text gives PGSI 3-7 / 8+ among past-30-day sports bettors as 18% / 13% (sum 31%) and among non-recent bettors as 16% / 5% (sum 21%). Table 3 gives moderate-risk or problem gambling as 30% vs 20%. The difference is likely rounding. Whole-sample counts for the 619 sports bettors are derived from rounded subgroup percentages, so they are approximate. The non-recent subgroup n (219) is derived as 619 - 400. Table 3's header says 'past-30-month', which is presumably a typo for past-30-day.
Заметка ИИ: One sample: past-year sports bettors (n=619) within an Ipsos web-panel survey of frequent Swedish online gamblers (N=997), May 2020. The authors did not report PGSI categories for all sports bettors, so the whole-sample estimates are derived. Industry funding is coded yes because the author's overall funding came from Svenska Spel. Possible overlap with R4315.

### ST038-1 · Sweden, Ipsos web panel of frequent online gamblers, past-year sports bettors, May 2020 (n=619)
Отчёты: R4314 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | PGSI · PGSI 3-7 | **L2** | **107 / 619** | 17.3 | Results (Characteristics of Past-30-Day Sports Bettors); Ta… | «Among respondents reporting any sports betting during the past-year (n = 619), those who reported past-30-day sports betting (n = 400)... moderate-risk and problem gamblers being 18 and 13% vs. 16 and 5%» |
| E2 | all | PGSI · PGSI>=8 | **L3** | **63 / 619** | 10.2 | Results (Characteristics of Past-30-Day Sports Bettors); Ta… | «with the proportions of moderate-risk and problem gamblers being 18 and 13% vs. 16 and 5%» |
| E3 | past-30-day sports bettors | PGSI · PGSI 3-7 | **L2** | **72 / 400** | 18.0 | Results (Characteristics of Past-30-Day Sports Bettors) | «those who reported past-30-day sports betting (n = 400)... moderate-risk and problem gamblers being 18 and 13%» |
| E4 | past-30-day sports bettors | PGSI · PGSI>=8 | **L3** | **52 / 400** | 13.0 | Results (Characteristics of Past-30-Day Sports Bettors) | «those who reported past-30-day sports betting (n = 400)... moderate-risk and problem gamblers being 18 and 13%» |
| E5 | past-30-day sports bettors | PGSI · PGSI>=3 | **L2** | **120 / 400** | 30.0 | Table 3 | «Total: Any sports betting / 30 / 20 / <0.01» |
| E6 | past-year but not past-30-day sports bettors | PGSI · PGSI 3-7 | **L2** | **35 / 219** | 16.0 | Results (Characteristics of Past-30-Day Sports Bettors) | «moderate-risk and problem gamblers being 18 and 13% vs. 16 and 5%» |
| E7 | past-year but not past-30-day sports bettors | PGSI · PGSI>=8 | **L3** | **11 / 219** | 5.0 | Results (Characteristics of Past-30-Day Sports Bettors) | «moderate-risk and problem gamblers being 18 and 13% vs. 16 and 5%» |
| E8 | past-year but not past-30-day sports bettors | PGSI · PGSI>=3 | **L2** | **44 / 219** | 20.1 | Table 3 | «Total: Any sports betting / 30 / 20 / <0.01» |
| E9 | in-play (live) bettors, past-30-day | PGSI · PGSI>=3 | **L2** | **100 / 277** | 36.1 | Tables 2 and 3 | «Sports live betting / 474 (48) / 277 / 58; Sports live betting / 36 / 22 / 0.001» |
| E10 | in-play (live) bettors, past-year but not past-30-day | PGSI · PGSI>=3 | **L2** | **43 / 197** | 21.8 | Tables 2 and 3 | «Sports live betting / 474 (48) / 277 / 58; Sports live betting / 36 / 22 / 0.001» |
| E11 | non-live sports bettors, past-30-day | PGSI · PGSI>=3 | **L2** | **78 / 279** | 28.0 | Tables 2 and 3 | «Sports non-live betting / 495 (50) / 279 / 56; Sports non-live betting / 28 / 22 / 0.12» |
| E12 | non-live sports bettors, past-year but not past-30-day | PGSI · PGSI>=3 | **L2** | **48 / 216** | 22.2 | Tables 2 and 3 | «Sports non-live betting / 495 (50) / 279 / 56; Sports non-live betting / 28 / 22 / 0.12» |

- E1: cumulative: no; источник порога: standard; правило: PGSI row; 3-7 band starts at L2; у авторов: «moderate-risk gamblers»; главная у авторов: no; период: past 12 months; **расчёт: 18% x 400 = 72 (past-30-day) + 16% x 219 = 35.0 -> 35 (non-recent; 219 = 619 - 400) = 107**; заметка: Whole-sample figure not reported by authors; derived from rounded subgroup percentages, approximate
- E2: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ = L3; у авторов: «problem gamblers»; главная у авторов: no; период: past 12 months; **расчёт: 13% x 400 = 52 + 5% x 219 = 10.95 -> 11 = 63**; заметка: Whole-sample figure not reported by authors; derived from rounded subgroup percentages, approximate
- E3: cumulative: no; источник порога: standard; правило: PGSI row; 3-7 band starts at L2; у авторов: «moderate-risk gamblers»; главная у авторов: no; период: past 12 months; **расчёт: 18% x 400 = 72**
- E4: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ = L3; у авторов: «problem gamblers»; главная у авторов: no; период: past 12 months; **расчёт: 13% x 400 = 52**
- E5: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 = L2; у авторов: «moderate-risk or problem gambling»; главная у авторов: yes; период: past 12 months; **расчёт: 30% x 400 = 120**; заметка: Text gives 18% + 13% = 31%; Table 3 gives 30% (rounding)
- E6: cumulative: no; источник порога: standard; правило: PGSI row; 3-7 band starts at L2; у авторов: «moderate-risk gamblers»; главная у авторов: no; период: past 12 months; **расчёт: n = 619 - 400 = 219; 16% x 219 = 35.0 -> 35**
- E7: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ = L3; у авторов: «problem gamblers»; главная у авторов: no; период: past 12 months; **расчёт: 5% x 219 = 10.95 -> 11**
- E8: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 = L2; у авторов: «moderate-risk or problem gambling»; главная у авторов: no; период: past 12 months; **расчёт: 20% x 219 = 43.8 -> 44**; заметка: Text gives 16% + 5% = 21%; Table 3 gives 20% (rounding)
- E9: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 = L2; у авторов: «moderate-risk or problem gambling»; главная у авторов: no; период: past 12 months; **расчёт: 36% x 277 = 99.7 -> 100**
- E10: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 = L2; у авторов: «moderate-risk or problem gambling»; главная у авторов: no; период: past 12 months; **расчёт: n = 474 - 277 = 197; 22% x 197 = 43.3 -> 43**
- E11: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 = L2; у авторов: «moderate-risk or problem gambling»; главная у авторов: no; период: past 12 months; **расчёт: 28% x 279 = 78.1 -> 78**
- E12: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 = L2; у авторов: «moderate-risk or problem gambling»; главная у авторов: no; период: past 12 months; **расчёт: n = 495 - 279 = 216; 22% x 216 = 47.5 -> 48**; заметка: Rounding ambiguous (47.5)

**Ключевые поля выборки:**
- **n_bettors: 619** — Table 2; Results — «Among respondents reporting any sports betting during the past-year (n = 619)»
- **sample_type: gamblers_survey_subsample** — Participants; Table 2 — «The sample addressed were web panel members of a Swedish market survey company, Ipsos... Total: Any sports betting | 619 (62)»
- **sampling: convenience** — Participants — «web panel members of a Swedish market survey company, Ipsos, i.e., individuals already enrolled with that company's web panel»
- **betting_period: past 12 months** — Table 2; Results — «Among respondents reporting any sports betting during the past-year (n = 619)»

**Остальные поля:**
- parent_population: Members of the Ipsos Swedish web panel who gambled on sports betting or online casino 10+ times in the past 12 months (frequent online gamblers) — Participants — «Only individuals responding "10 times or more" were further considered in the study.»
- min_frequency: none for sports betting itself; parent survey entry required sports betting or online casino 10+ times in past 12 months — Participants — «Only individuals responding "10 times or more" were further considered in the study.»
- country: SWE — Setting — «The present study took place in Sweden»
- subnational: NA — Setting — «The present study took place in Sweden»
- data_years: 2020 — Study Design — «The survey was carried out from May 5 to 12»
- design: cross-sectional — Discussion (limitations) — «another limitation is the cross-sectional study design»
- gambling_disclosed: yes — Participants — «they were included with the question "if you think about the past 12 months, how often have you gambled on sports betting or online casino games?"»
- betting_mode: NR — Measures — «sports live betting, sports non-live betting»
- pct_online: NR — Measures — «sports live betting, sports non-live betting»
- pct_inplay: 76.6 — Table 2 — «Sports live betting | 474 (48) ... Total: Any sports betting | 619 (62)»
- pct_dfs: NR — Measures — «gambling types assessed were online casino, land-based casino, online horse betting...»
- pct_esports: NR — Measures — «gambling types assessed were online casino, land-based casino, online horse betting...»
- sports_lottery: unclear — Measures — «sports live betting, sports non-live betting»
- mixed_race: no — Table 2 — «Total: Any sports betting | 619 (62) ... Online horse betting | 646 (65)»
- legal_status: regulated legal market — Setting — «gambling, since January 1st, 2019, is regulated in a license-based system... betting on sports and horse racing... are subject to competition between a number …»
- n_invited: NR — Participants — «The study had the intention to include 1,000 individuals.»
- n_responded: 1007 — Participants — «When closing the study, 1,007 individuals had answered the survey.»
- response_rate: NR — Participants — «When closing the study, 1,007 individuals had answered the survey.»
- age_mean: NR — Table 1 — «Age groups (years)»
- age_sd: NR — Table 1 — «Age groups (years)»
- age_min: 18 — Table 1 — «18–24 | 11 (1)»
- age_max: NR — Table 1 — «70 and above | 163 (16)»
- age_group: adults — Table 1 — «18–24 | 11 (1)»
- pct_male: 74.6 — Table 1 — «Male gender | 744 (75)»
- mode: online — Introduction; Participants — «designed prior to the COVID-19 crisis as a web survey»
- weights: NR — Statistical Methods — «Sample characteristics and gambling patterns were reported as descriptive data.»
- instruments: PGSI (language version not stated; presumably Swedish) — Measures — «Problem gambling severity was measured using the Problem Gambling Severity Index (PGSI), a nine-item scale (Wynne and Ferris, 2001)»
- instrument_validated_in_language: NR — Measures — «Problem Gambling Severity Index (PGSI), a nine-item scale (Wynne and Ferris, 2001)»
- industry_funding: yes — Conflict of Interest; Funding — «the study could be carried out thanks to the researcher's overall funding from the Swedish state-owed gambling operator Svenska Spel»
- funding_coi: No specific funding; author's overall funding from Svenska Spel (state-owned operator) and its research council, alcohol monopoly, Enforcement Authority, Sports Federation, regional hospital; funders had no stated influence — Conflict of Interest; Funding — «None of these organization have been involved in or had any influence on any part of the present work.»
- pub_status: journal — Header — «Year: 2020; venue: Frontiers in psychology»
- language: English — Full text — «Impact of COVID-19 on Online Gambling – A General Population Survey During the Pandemic»
- notes: Age and sex fields are for the whole sample (N=997); age given only in bands. Male % among sports bettors: 84% past-30-day (n=400), 80% non-recent (n=219), about 83% overall (derived). pct_inplay = 474/619 (derived). Parent survey entry: sports betting or online casino 10+ times in the past year. Online vs land-based sports betting not specified. PGSI not reported for all 619 sports bettors, only by recency subgroup. 10 of 1,007 excluded for missing PGSI items; 3 with missing items kept as 8+. Data collected during the COVID-19 sports lockdown. Possible overlap with R4315 (ST039): both are Ip…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame is one market research company's web panel, covering only part of Swedish sports bettors — Discussion (limitations) — «the study can only claim to be representative of web panel-recruited online gamblers»
2. способ отбора: **no** — Non-probability opt-in online panel — Participants — «individuals already enrolled with that company's web panel, and typically receiving market surveys and political opinion polls»
3. размер выборки: **yes** — 619 past-year sports bettors (>=385) — Results — «Among respondents reporting any sports betting during the past-year (n = 619)»
4. описание выборки и условий: **yes** — Age (bands), sex, setting, country and dates reported (for whole sample) — Study Design; Table 1 — «The survey was carried out from May 5 to 12... Male gender | 744 (75)»
5. охват (пропуски): **yes** — 10 of 1,007 respondents (<1%) excluded for missing PGSI items — Participants — «The remaining 10 individuals were excluded from further analyses»
6. валидность определения случая: **unclear** — PGSI with standard thresholds, but language version and its validation not stated — Measures — «Problem Gambling Severity Index (PGSI), a nine-item scale (Wynne and Ferris, 2001)... problem gambling (8 points and above)»
7. единое надёжное измерение: **unclear** — Same instrument, time frame and web mode for all; reliability not reported — Measures — «with questions asked with a time frame of the past 12 months»
8. статистика (числитель и знаменатель): **unclear** — PGSI prevalence for all 619 sports bettors not reported; only rounded percentages by recency subgroup; no CIs — Results (Characteristics of Past-30-Day Sports Bettors) — «with the proportions of moderate-risk and problem gamblers being 18 and 13% vs. 16 and 5%»
9. отклик: **no** — Online panel survey with no denominator of invited panel members; no response rate — Participants — «The study had the intention to include 1,000 individuals. When closing the study, 1,007 individuals had answered the survey.»

Правки:
- 

Проверено: да

---

## ST039 · Håkansson 2020 · Frontiers in psychiatry

Основной отчёт R4315: [текст](../../fulltext/text/R4315.txt) — «Over-Indebtedness and Problem Gambling in a General Population Sample of Online Gamblers.» — [DOI](https://doi.org/10.3389/fpsyt.2020.00007)
⚠ Возможное пересечение (держим раздельно; если видите общие данные — напишите в «Правки»): possible overlap with R4314 (ST038): Both Ipsos web panel samples of Swedish online gamblers (Hakansson); R4314 (May 2020, N = 997) says it repeats the recruitment of an earlier study, probably R4315 (N = 1,004): different years, panel members may overlap
Расхождения в тексте: The Table 3 counts for live-betting groups (14+351=365; 77+100=177) match the text's group sizes (365, 177) and Table 2's live sports betting total (542). Text percentages (44%, 4%) match Table 3 counts (77/177=43.5%; 14/365=3.8%). The male-gender row of Table 6 looks transposed: future over-indebtedness '20 (185)' vs no future over-indebtedness '41 (33)'. This is not used here. The over-indebtedness items are internally inconsistent: 10% lifetime vs 11% past year, which the authors acknowledge.
Заметка ИИ: The sports-bettor sample is the past-30-day live (in-play) bettors within an Ipsos panel survey of Swedish online gamblers. All estimates come from Table 3 counts or from the text's subgroup percentages. The whole-sample PGSI>=3 is approximate because it is summed from rounded subgroup percentages.

### ST039-1 · Sweden, Ipsos web panel of online gamblers, past-30-day live sports bettors (n=542 of 1,004)
Отчёты: R4315 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | PGSI · PGSI>=8 | **L3** | **91 / 542** | 16.8 | Table 3; Table 2 | «Live betting, no online casino / 11 (14) / 40 (351) ... Both / 58 (77) / 11 (100)» |
| E2 | all | PGSI · PGSI 0-7 | **below** | **451 / 542** | 83.2 | Table 3 | «Live betting, no online casino / 11 (14) / 40 (351) ... Both / 58 (77) / 11 (100)» |
| E3 | all | PGSI · PGSI>=3 | **L2** | **192 / 542** | 35.4 | Results, Problem Gambling | «The summed measure of moderate-risk gambling and problem gambling was met by 65% of subjects reporting both online casino and live betting ... by 21% of subjects reporting only live betting» |
| E4 | live betting + online casino (past 30 days) | PGSI · PGSI>=8 | **L3** | **77 / 177** | 43.5 | Table 3; Results | «The percentage of respondents with problem gambling was 44% in subjects reporting both past 30-day online casino gambling and live betting» |
| E5 | live betting + online casino (past 30 days) | PGSI · PGSI>=3 | **L2** | **115 / 177** | 65.0 | Results, Problem Gambling | «The summed measure of moderate-risk gambling and problem gambling was met by 65% of subjects reporting both online casino and live betting» |
| E6 | live betting, no online casino (past 30 days) | PGSI · PGSI>=8 | **L3** | **14 / 365** | 3.8 | Table 3; Results | «In subjects reporting only live betting and no casino gambling, as well as in subjects reported neither of these gambling activities, 4% were problem gamblers.» |
| E7 | live betting, no online casino (past 30 days) | PGSI · PGSI>=3 | **L2** | **77 / 365** | 21.1 | Results, Problem Gambling | «the same measure was met by 21% of subjects reporting only live betting and no past 30-day online casino gambling» |

- E1: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ = L3; у авторов: «problem gambling»; главная у авторов: yes; период: past 12 months; **расчёт: Reverse table (Table 3): problem 14 (live, no casino) + 77 (both) = 91; no problem 351 + 100 = 451; n = 91 + 451 = 542 (= Table 2 live sports betting 542)**; заметка: The authors' main estimate is PGSI 8+ (13% of all 1,004 online gamblers). This live-sports-bettor figure is derived from their table. PGSI time frame is not stated; the Discussion refers to 'past-year problem gambling'.
- E2: cumulative: no; источник порога: standard; правило: PGSI row; lower bound 0 = below (combined band 0-7); у авторов: «no problem gambling»; главная у авторов: no; период: past 12 months; **расчёт: Table 3 no problem gambling: 351 (live, no casino) + 100 (both) = 451**; заметка: Combined band that includes no-risk, low-risk and moderate-risk respondents
- E3: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 = L2; у авторов: «moderate-risk or problem gambling»; главная у авторов: no; период: past 12 months; **расчёт: 65% x 177 = 115.05 -> 115 (both) + 21% x 365 = 76.65 -> 77 (live only) = 192**; заметка: Approximate: summed from rounded subgroup percentages. The study does not report this figure for all live bettors.
- E4: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ = L3; у авторов: «problem gambling»; главная у авторов: no; период: past 12 months; **расчёт: n = 77 problem + 100 no problem = 177 (Table 3); text gives n = 177**
- E5: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 = L2; у авторов: «moderate-risk gambling and problem gambling»; главная у авторов: no; период: past 12 months; **расчёт: 65% x 177 = 115.05 -> 115**
- E6: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ = L3; у авторов: «problem gamblers»; главная у авторов: no; период: past 12 months; **расчёт: n = 14 problem + 351 no problem = 365 (Table 3); text gives n = 365**
- E7: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 = L2; у авторов: «moderate-risk gambling and problem gambling»; главная у авторов: no; период: past 12 months; **расчёт: 21% x 365 = 76.65 -> 77**

**Ключевые поля выборки:**
- **n_bettors: 542** — Table 2; Table 3 — «Live sports betting | 542 | 54»
- **sample_type: gamblers_survey_subsample** — Methods, Participants; Table 2 — «recruited from the web panel of the market survey company Ipsos ... Live sports betting | 542 | 54»
- **sampling: quota** — Methods, Participants — «stratified for age ... The participants were recruited from the web panel of the market survey company Ipsos»
- **betting_period: past 30 days or month** — Measures, Gambling Involvement; Table 2 — «clients were post hoc divided into categories depending on their recent (30-day) gambling on online casino ... and live sports betting (“sports and odds—live betting”)»

**Остальные поля:**
- parent_population: Adult Ipsos web panel members in Sweden who gambled on online casino or online betting sites at least 10 times in the past 12 months — Methods, Participants — «roughly 1,000 adult individuals from the general population, stratified for age, who had gambled for money on either an online casino site or an online betting…»
- min_frequency: none within past 30 days for live betting; parent survey entry required online casino/betting at least 10 times in past 12 months — Methods, Participants — «Only individuals endorsing the latter option were further included in the study»
- country: SWE — Background — «In Sweden, the setting addressed in the present study»
- subnational: NA — Methods, Design — «recruited from a pre-existing web panel of a national market research company»
- data_years: NR — Methods, Design — «approved by the regional ethics board in Lund, Sweden (file number 2018/495)»
- design: cross-sectional — Methods, Design — «The present study is a cross-sectional survey study conducted in a sample derived from the adult general population»
- gambling_disclosed: yes — Methods, Participants; Limitations — «“If you think about the past 12 months, how often have you gambled on betting services online or online casinos?” ... people who engage in a web survey panel a…»
- betting_mode: NR — Measures, Gambling Involvement; Table 3 — «The gambling activities listed, for land-based and online gambling modalities ... sports and odds (live betting)»
- pct_online: NR — Measures, Gambling Involvement — «sports and odds (live betting), sports and odds (non-live betting)»
- pct_inplay: all — Table 2 — «Live sports betting | 542 | 54»
- pct_dfs: NR — NR
- pct_esports: NR — Table 2 — «Gambling for money within video games | 79 | 8»
- sports_lottery: no — Measures, Gambling Involvement — «sports and odds (live betting)»
- mixed_race: no — Measures, Gambling Involvement — «online horse race betting, land-based horse race betting, sports and odds (live betting)»
- legal_status: NR — Background — «governmental sources in Sweden have reported that foreign-based online gambling operators were gaining larger and larger shares of the gambling market»
- n_invited: NR — Methods, Participants — «Finally, a total number of 1,009 individuals answered the survey.»
- n_responded: 1009 — Methods, Participants — «Finally, a total number of 1,009 individuals answered the survey.»
- response_rate: NR — Methods, Participants — «a total number of 1,009 individuals answered the survey»
- age_mean: NR — Table 1 — «18–24 years | 41 | 4»
- age_sd: NR — Table 1
- age_min: 18 — Table 1 — «18–24 years | 41 | 4»
- age_max: NR — Table 1 — «70 years and older | 77 | 8»
- age_group: adults — Methods, Participants — «roughly 1,000 adult individuals from the general population»
- pct_male: 78 — Table 1; Methods, Participants — «leaving a final sample of 1,004 included subjects, 78% of whom were men»
- mode: online — Abstract — «were examined in an online survey»
- weights: NR — Statistical Analyses — «In addition to descriptive data, analyses examined variables associated with three outcome measures»
- instruments: PGSI (language version not reported; survey conducted in Sweden) — Measures, Problem Gambling — «Problem gambling was measured using the Problem Gambling Severity Index, PGSI (26).»
- instrument_validated_in_language: NR — Measures, Problem Gambling — «constitutes a well- established measure for epidemiological studies of problem gambling in the general population (4, 34)»
- industry_funding: yes — Funding — «the first author holds a position at Lund University which is sponsored by the Swedish government-owned gambling operator Svenska spel AB ... Svenska spel AB h…»
- funding_coi: Study grant from research council of the Swedish Enforcement Authority; first author's position sponsored by state-owned operator Svenska spel; both authors receive Svenska spel research funding; COI declared none — Funding; Conflict of Interest — «financed by a study-specific grant from the research council of the Swedish Enforcement Authority ... receive study-specific and non-specific research funding …»
- pub_status: journal — Header — «Frontiers in psychiatry; DOI: 10.3389/fpsyt.2020.00007»
- language: English — Full text — «Over-Indebtedness and Problem Gambling in a General Population Sample of Online Gamblers»
- notes: Sample = past-30-day live sports bettors (542 = 177 live+online casino + 365 live without casino). Non-live sports bettors (n=605) have no PGSI breakdown, so the total of all sports bettors cannot be determined. Age and sex describe the whole sample (N=1,004). Data years not reported (ethics 2018/495). Authors call live betting 'online sports betting' in places, but the item wording does not say online, so betting_mode = NR. Missing PGSI: 20 of 1,009 had a missing item; 15 zero-imputed, 5 excluded. Possible overlap with R4314 (ST038): Both Ipsos web panel samples of Swedish online gamblers (H…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame is one market-research web panel (Ipsos), which does not cover all sports bettors in Sweden — Methods, Participants — «The participants were recruited from the web panel of the market survey company Ipsos»
2. способ отбора: **no** — Non-probability online panel stratified by age — Methods, Participants — «stratified for age ... recruited from the web panel of the market survey company Ipsos»
3. размер выборки: **yes** — 542 live sports bettors (>=385) — Table 2 — «Live sports betting | 542 | 54»
4. описание выборки и условий: **unclear** — Age, sex, setting and country reported (whole sample); dates of data collection not reported — Table 1; Methods — «leaving a final sample of 1,004 included subjects, 78% of whom were men»
5. охват (пропуски): **yes** — Missing PGSI in 20 of 1,009 (2%); handled by imputation (15) and exclusion (5) — Methods, Participants — «answers were missing on any of the items for a total of 20 individuals ... these five individuals were excluded»
6. валидность определения случая: **unclear** — PGSI with standard 8+ threshold, but the language version and its validation are not reported — Measures, Problem Gambling — «with a sum of eight or more describing problem gambling, 3–7 indicating moderate-risk gambling, 1–2 indicating low-risk gambling»
7. единое надёжное измерение: **unclear** — Same instrument, mode and threshold for all respondents; reliability not reported — Measures, Problem Gambling — «Problem gambling was measured using the Problem Gambling Severity Index, PGSI (26).»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator for live bettors can be traced from Table 3 counts (matches Table 2); CI calculable; unweighted panel — Table 3 — «Live betting, no online casino | 11 (14) | 40 (351) ... Both | 58 (77) | 11 (100)»
9. отклик: **no** — Online panel with no denominator of invited members; response rate not reported — Methods, Participants — «Finally, a total number of 1,009 individuals answered the survey.»

Правки:
- 

Проверено: да

---

## ST040 · Lelonek-Kuleta 2020 · International journal of environmental research and public health

Основной отчёт R4368: [текст](../../fulltext/text/R4368.txt) — «The Prevalence of E-Gambling and of Problem E-Gambling in Poland.» — [DOI](https://doi.org/10.3390/ijerph17020404)
Расхождения в тексте: Text: 22 of 83 online gamblers at risk, reported as "26.8%". 22/83 = 26.5%. Table 4 NPeG percentages for sports betting (11 = 18.3%) and esports (10 = 16.7%) imply a denominator of 60, not 61. The gender column for NPeG also sums to 60 (45+15), so some NPeG items appear to have one missing answer. In Table 4, sports betting counts (11+8=19) and esports counts (10+1=11) match the Table 2 totals of 19 and 11. Table 1 lists children "Yes 268 (63.4%)" and "No 732 (36.6%)". These numbers do not add up, and 268 looks like a typo for 1268.
Заметка ИИ: This draft was built from the reverse-table rule using Table 4 (problem vs non-problem online gamblers by game type). Very small n (19 sports bettors). The brief BBGS screen was reworded for online gambling.

### ST040-1 · Online sports bettors (incl. fantasy sports) within Polish national CAPI survey of adults, Dec 2018 (n=19)
Отчёты: R4368 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | BBGS · BBGS>=1 (range 0-3) | **L3-screen** | **8 / 19** | 42.1 | Table 4 | «Online sports betting (including "fantasy sports") / 11 / 18.3 / 8 / 36.4 / 2.940 / 0.086» |
| E2 | all | BBGS · BBGS 0 (range 0-3) | **below** | **11 / 19** | 57.9 | Table 4 | «Online sports betting (including "fantasy sports") / 11 / 18.3 / 8 / 36.4» |
| E3 | esports | BBGS · BBGS>=1 (range 0-3) | **L3-screen** | **1 / 11** | 9.1 | Table 4 | «Online betting on e-sports or online virtual sports / 10 / 16.7 / 1 / 4.5 / 2.036 / 0.154» |
| E4 | esports | BBGS · BBGS 0 (range 0-3) | **below** | **10 / 11** | 90.9 | Table 4 | «Online betting on e-sports or online virtual sports / 10 / 16.7 / 1 / 4.5» |

- E1: cumulative: yes; источник порога: standard; правило: BBGS row; any positive item = L3-screen; у авторов: «problem online gamblers (PeG) / at risk of becoming problem gamblers»; главная у авторов: no; период: past 12 months; **расчёт: Reverse table: sports bettors among NPeG 11 + among PeG 8 = 19 (matches Table 2 n=19); cases = 8**; заметка: Authors' primary estimate is for all 83 online gamblers (22/83, reported as 26.8%); the sports-betting estimate is derived. BBGS reworded to online gambling.
- E2: cumulative: no; источник порога: standard; правило: BBGS row; score 0 = below screen threshold; у авторов: «non-problem online gamblers (NPeG)»; главная у авторов: no; период: past 12 months; **расчёт: 11 NPeG + 8 PeG = 19 sports bettors; cases = 11**
- E3: cumulative: yes; источник порога: standard; правило: BBGS row; any positive item = L3-screen; у авторов: «problem online gamblers (PeG)»; главная у авторов: no; период: past 12 months; **расчёт: Reverse table: NPeG 10 + PeG 1 = 11 (matches Table 2 n=11); cases = 1**; заметка: Category combines esports and virtual sports betting; overlap with the 19 online sports bettors not reported.
- E4: cumulative: no; источник порога: standard; правило: BBGS row; score 0 = below screen threshold; у авторов: «non-problem online gamblers (NPeG)»; главная у авторов: no; период: past 12 months; **расчёт: 10 NPeG + 1 PeG = 11; cases = 10**; заметка: Esports or virtual sports combined.

**Ключевые поля выборки:**
- **n_bettors: 19** — Table 2; Table 4 — «Online sports betting (including "fantasy sports") | 19 | 1.0»
- **sample_type: rep_survey_subsample** — 2.1. Participants — «The sample was representative and randomly selected on the basis of PESEL (Personal Identification Number).»
- **sampling: probability** — 2.1. Participants — «the municipalities with probabilities proportional to the number of residents older than 18 years of age were randomly selected... the interviewers selected the respondents using the Kish grid»
- **betting_period: past 12 months** — 2.2.1. E-Gambling — «the respondent was asked to select the online games on which they have bet money at least once within the last 12 months»

**Остальные поля:**
- parent_population: Adult (18+) inhabitants of Poland — Abstract — «The study was conducted using a representative sample of the adult inhabitants of Poland (n = 2000).»
- min_frequency: none — 2.2.1. E-Gambling — «have bet money at least once within the last 12 months»
- country: POL — 2.1. Participants — «This study was conducted on a nationwide sample of 2000 adult Poles.»
- subnational: NA — 2.1. Participants — «nationwide sample of 2000 adult Poles»
- data_years: 2018 — 4. Discussion — «sheds light on the results of this study, which was conducted in December 2018»
- design: prevalence survey — Abstract — «This study estimated the levels of involvement in e-gambling and problem e-gambling in Poland»
- gambling_disclosed: NR — 2.2 Measures — «The questionnaire consisted of questions regarding use of online gambling games»
- betting_mode: online only — 2.2.1. E-Gambling — «online sports betting (including "fantasy sports")»
- pct_online: all — Table 2 — «Online sports betting (including "fantasy sports") | 19 | 1.0»
- pct_inplay: NR — NA
- pct_dfs: NR — 2.2.1. E-Gambling — «online sports betting (including "fantasy sports")»
- pct_esports: NR — Table 2 — «Online betting on e-sports or online virtual sports | 11 | 0.6»
- sports_lottery: no — 2.2.1. E-Gambling — «Totalizator Sportowy number games via the Internet ... online sports betting (including "fantasy sports")»
- mixed_race: no — 2.2.1. E-Gambling — «online sports betting (including "fantasy sports")»
- legal_status: regulated legal market — 1. Introduction — «Legal online betting games are currently offered by nine private operators. Until 2017, when Poland tightened its restrictions on the betting market... 90% of …»
- n_invited: NR — NA
- n_responded: 2000 — 2.1. Participants — «nationwide sample of 2000 adult Poles»
- response_rate: NR — NA
- age_mean: 45.61 — 2.2.3. Sociodemographic Variables — «Their average age was 45.61 years (SD = 18.456, minimum = 18, maximum = 94).»
- age_sd: 18.456 — 2.2.3. Sociodemographic Variables — «SD = 18.456»
- age_min: 18 — 2.2.3. Sociodemographic Variables — «minimum = 18»
- age_max: 94 — 2.2.3. Sociodemographic Variables — «maximum = 94»
- age_group: adults — 2.1. Participants — «nationwide sample of 2000 adult Poles»
- pct_male: 48.2 — Table 1 — «Gender | Male | 964 | 48.2»
- mode: face-to-face — 2.1. Participants — «conducted computer-assisted personal interviews with them»
- weights: NR — 2.3. Data Analysis — «Categorical data are presented as frequencies and percentages»
- instruments: BBGS (Polish adaptation by Niewiadomska et al., reworded to refer to online gambling) — 2.2.2. Problem E-Gambling — «The Brief Biosocial Gambling Screen (BBGS), adapted to Polish by Niewiadomska et al., was adjusted to the assessment of problem e-gambling»
- instrument_validated_in_language: yes — 2.2.2. Problem E-Gambling — «The psychometric properties of the Polish adaptation of BBGS were tested on a representative sample of high school students of the Lublin province... Sensitivi…»
- industry_funding: no — Funding — «This research was funded by the Ministry of Health—the Republic of Poland Fund for Solving Gambling Problems, grant number 362/HE/2018.»
- funding_coi: Ministry of Health, Fund for Solving Gambling Problems (grant 362/HE/2018); authors declare no conflict of interest — Funding; Conflicts of Interest — «The authors declare no conflict of interest. The funders had no role in the design of the study»
- pub_status: journal — Header — «International journal of environmental research and public health; DOI: 10.3390/ijerph17020404»
- language: English — Full text — «The Prevalence of E-Gambling and of Problem E-Gambling in Poland»
- notes: Sample = respondents reporting past-12-month online sports betting (incl. fantasy sports) among 83 past-year online gamblers in a national survey of 2000 adults. The separate category 'online betting on e-sports or online virtual sports' (n=11) is extracted as a subgroup. Its overlap with the 19 sports bettors is not reported, so the union cannot be computed. Age and sex fields describe the whole sample of 2000; they are not reported for sports bettors. Offline gambling was not measured, so land-based sports bettors are not captured. Interviewers could substitute a person of the same age and …

**Риск смещения (JBI):**
1. рамка выборки: **yes** — Parent survey frame was the national PESEL population register of adults. — 2.1. Participants — «drawing households proportionally to the number of household members according to the PESEL census records»
2. способ отбора: **yes** — Multistage stratified probability sampling with Kish grid; substitution of unavailable respondents is a minor concern. — 2.1. Participants — «the municipalities with probabilities proportional to the number of residents older than 18 years of age were randomly selected»
3. размер выборки: **no** — Only 19 online sports bettors. — Table 2 — «Online sports betting (including "fantasy sports") | 19 | 1.0»
4. описание выборки и условий: **no** — Setting, country and dates reported, but age and sex of the sports bettors not reported (whole-sample only). — Table 1; Table 4 — «Descriptive statistics for the sociodemographic variables for the test group (n = 2000)»
5. охват (пропуски): **yes** — All 83 online gamblers classified by BBGS (61+22); sports bettors in Table 4 sum to 19, matching Table 2. — Table 4 — «non-problem online gamblers (NPeG, n = 61) and problem online gamblers (PeG, n = 22)»
6. валидность определения случая: **no** — BBGS brief screen used to classify problem gamblers, reworded for online gambling (modified version not validated). — 2.2.2; Limitations — «the adjustment of BBGS to online gambling by rewording the questions... is a very unusual technique, and it is uncertain how that step affected the results obt…»
7. единое надёжное измерение: **unclear** — Same instrument and CAPI mode for all, but reliability not reported for the sample. — 2.1; 2.2.2 — «conducted computer-assisted personal interviews with them»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator of sports bettors traceable from Table 4 (8 of 19); CI calculable; weighting not reported. — Table 4 — «Online sports betting (including "fantasy sports") | 11 | 18.3 | 8 | 36.4»
9. отклик: **unclear** — Response rate not reported. — 2.1. Participants — «Within the framework of each selected municipality, 6 interviews with randomly selected respondents were carried out.»

Правки:
- 

Проверено: да

