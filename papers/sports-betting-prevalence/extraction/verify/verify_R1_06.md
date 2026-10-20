# Проверка выписывания — файл 6 из 6

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

## ST051 · Huic 2017 · Frontiers in psychology

Основной отчёт R5435: [текст](../../fulltext/text/R5435.txt) — «Problem Gambling among Adolescent Girls in Croatia-The Role of Different Psychosocial Predictors.» — [DOI](https://doi.org/10.3389/fpsyg.2017.00792)
Не выписано ИИ: No treatment/help-seeking samples. Girls who bet on sports occasionally or regularly (189 + 38 = 227, Table 2) not extracted as a separate sample: problem gambling is given only for regular sports bettors (Table 3). Whole-sample (1,372) and lifetime-gambler (862) CAGI estimates are not specific to sports bettors.
Расхождения в тексте: Table 3 sports-betting counts (15+16+7=38) match the regular sports bettors in Table 2 (38). The column percentages in Table 3 suggest these category denominators: yellow 16/16.8% ≈ 95 and red 7/25.9% ≈ 27, which fits the text (11.2% and 3.2% of 862 ≈ 97 and 28). Green 15/2.1% ≈ 714, but 862−95−27 = 740 (15/740 = 2.0%). This is a small discrepancy, probably rounding or missing data. The Measures section says frequency is rated 'on a 5 point scale, from 0 = never to 5 = every day', which gives 6 points, so the description is internally inconsistent. The paper does not print the CAGI score cut-offs.
Заметка ИИ: The single extracted sample is regular (weekly or more) sports bettors among Croatian high-school girls, n=38. It comes from a reverse table, and the authors do not present it as a prevalence estimate for sports bettors. Funding includes Croatian Lottery Ltd, so industry_funding is coded yes.

### ST051-1 · Croatian high-school girls who bet on sports regularly (weekly+), 7 cities, n=38 (of 1,372 girls)
Отчёты: R5435 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | CAGI · CAGI GPSS 0-1 (green light) | **below** | **15 / 38** | 39.5 | Table 3 | «Sports Betting / 15 / 2.1 / 16 / 16.8 / 7 / 25.9» |
| E2 | all | CAGI · CAGI GPSS 2-5 (yellow light) | **L2** | **16 / 38** | 42.1 | Table 3 | «Sports Betting / 15 / 2.1 / 16 / 16.8 / 7 / 25.9» |
| E3 | all | CAGI · CAGI GPSS>=6 (red light) | **L3** | **7 / 38** | 18.4 | Table 3 | «Sports Betting / 15 / 2.1 / 16 / 16.8 / 7 / 25.9» |

- E1: cumulative: no; источник порога: standard; правило: CAGI row; green light below L2 (L1 not defined); у авторов: «CAGI green light / no problem (social gamblers)»; главная у авторов: no; период: NR; **расчёт: Reverse table: regular sports bettors 15 (green) + 16 (yellow) + 7 (red) = 38; cases = 15**; заметка: Only regular (weekly+) sports bettors; authors' main estimates are for all girls/lifetime gamblers, not sports bettors.
- E2: cumulative: no; источник порога: standard; правило: CAGI row; yellow light (>=2) starts at L2; у авторов: «CAGI yellow light / low to moderate severity (at-risk gamblers)»; главная у авторов: no; период: NR; **расчёт: Reverse table: 15 + 16 + 7 = 38 regular sports bettors; cases = 16**; заметка: Score bands for yellow/red not printed in the paper; standard CAGI cut-offs assumed from instrument description.
- E3: cumulative: yes; источник порога: standard; правило: CAGI row; red light (>=6) = L3; у авторов: «CAGI red light / high severity (problem gamblers)»; главная у авторов: no; период: NR; **расчёт: Reverse table: 15 + 16 + 7 = 38 regular sports bettors; cases = 7**; заметка: 7/38 = 18.4%.

**Ключевые поля выборки:**
- **n_bettors: 38** — Table 2; Table 3 — «Sports Betting | 1,145 | 83.5 | 189 | 13.8 | 38 | 2.8»
- **sample_type: school_pupils** — Participants — «In regional centers (Zagreb, Rijeka, Osijek, Split), high-schools were randomly selected from the list of available schools in the city. In smaller towns, a convenient sample of schools was used.»
- **sampling: convenience** — Participants — «In regional centers (Zagreb, Rijeka, Osijek, Split), high-schools were randomly selected from the list of available schools in the city. In smaller towns, a convenient sample of schools was used.»
- **betting_period: NR** — Measures; Results, Descriptives — «The respondents were asked to evaluate the frequency of their gambling (on a 5 point scale, from 0 = never to 5 = every day or almost every day).»

**Остальные поля:**
- parent_population: Female high-school students (aged 14-20) in 7 Croatian cities — Participants — «A total of N = 1,372 high-school girls from 7 Croatian cities participated in the study.»
- min_frequency: regularly = once a week or more often — Results, Descriptives; Table 3 — «played regularly (once a week or more often)... Only games played regularly (once a week or more often) are included.»
- country: HRV — Participants — «A total of N = 1,372 high-school girls from 7 Croatian cities participated in the study.»
- subnational: 7 cities: Zagreb, Split, Rijeka, Osijek, Koprivnica, Slavonski Brod, Vinkovci — Participants; Table 1 — «City/Town | Zagreb | Split | Rijeka | Osijek | Koprivnica | Slavonski brod | Vinkovci»
- data_years: NR — Procedure — «The data was collected in school classrooms, during regularly scheduled classes.»
- design: cross-sectional — Discussion (limitations) — «Firstly, our design was cross-sectional and we rely on self-reports»
- gambling_disclosed: NR — Procedure — «after the participants were fully informed about the study»
- betting_mode: NR — Measures — «We focused on six games: (1) sports betting, (2) lotto, (3) scratch cards, (4) slot machines, (5) electronic roulette, and (6) betting on virtual races.»
- pct_online: NR — NA — «NR»
- pct_inplay: NR — NA — «NR»
- pct_dfs: NR — NA — «NR»
- pct_esports: NR — NA — «NR»
- sports_lottery: unclear — Measures — «We focused on six games: (1) sports betting, (2) lotto, (3) scratch cards»
- mixed_race: no — Measures — «(1) sports betting ... (6) betting on virtual races»
- legal_status: regulated legal market — Introduction; Discussion — «Croatia, with its liberal gambling market, and high accessibility and availability of gambling venues... In spite of gambling being illegal for minors (adolesc…»
- n_invited: NR — NA — «NR»
- n_responded: 1372 — Participants; Table 2 — «Table 2: Frequency of Gambling (N = 1,372).»
- response_rate: NR — NA — «NR»
- age_mean: 16.45 — Participants — «Age ranged from 14 to 20 years (M = 16.45, SD = 1.154).»
- age_sd: 1.154 — Participants — «Age ranged from 14 to 20 years (M = 16.45, SD = 1.154).»
- age_min: 14 — Participants — «Age ranged from 14 to 20 years»
- age_max: 20 — Participants — «Age ranged from 14 to 20 years»
- age_group: mixed — Participants — «Age ranged from 14 to 20 years (M = 16.45, SD = 1.154).»
- pct_male: 0 — Participants — «A total of N = 1,372 high-school girls»
- mode: paper — Procedure — «The researcher distributed the paper-pencil surveys and students completed them independently and anonymously.»
- weights: NR — Statistical analyses — «We calculated descriptive statistical parameters in order to analyze frequency of gambling and problem gambling.»
- instruments: Canadian Adolescent Gambling Inventory (CAGI), General Problem Severity Subscale (9 items); language version not stated (presumably Croatian) — Measures — «In this study we used only the nine items which provide a composite measure, a General Problem Severity Subscale (GPSS) (α = 0.79).»
- instrument_validated_in_language: NR — Measures — «Several studies confirm good classification accuracy of the GPSS measure–Se = 0.97 and Sp = 0.93 (Tremblay et al., 2010); Se = 0.93, Sp = 0.99 and hit rate = 0…»
- industry_funding: yes — Funding — «financially and organizationally supported by the Ministry of Science, Education and Sports of the Republic of Croatia, Education and Teacher Training Agency, …»
- funding_coi: Project 'Youth gambling in Croatia' funded by Ministry of Science, Education and Sports, Education and Teacher Training Agency, and Croatian Lottery Ltd (gambling operator); authors declare no COI — Funding; Conflict of interest statement — «supported by the Ministry of Science, Education and Sports of the Republic of Croatia, Education and Teacher Training Agency, and Croatian Lottery, Ltd.»
- pub_status: journal — Header — «Frontiers in psychology; DOI: 10.3389/fpsyg.2017.00792»
- language: English — Full text — «Problem Gambling among Adolescent Girls in Croatia—The Role of Different Psychosocial Predictors»
- notes: Sample = girls who bet on sports regularly (weekly or more); derived from reverse Table 3 (regular sports betting by CAGI category among 862 lifetime gamblers). The green/yellow/red groups cover all 862 lifetime gamblers without overlap; the sum 15+16+7=38 matches Table 2 regular sports bettors (38). Occasional+regular sports bettors (189+38=227) have no problem-gambling estimate. Age and sex describe the whole sample of 1,372 girls (all female). Reference period for betting frequency not stated. Gambling is illegal for minors in Croatia; most of the sample is under 18. Boys reported separate…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame is school lists in 4 cities plus convenience schools in 3 towns; does not cover all Croatian pupils. — Participants — «In smaller towns, a convenient sample of schools was used.»
2. способ отбора: **no** — Partly random school selection, partly convenience sample of schools. — Participants — «high-schools were randomly selected from the list of available schools in the city. In smaller towns, a convenient sample of schools was used.»
3. размер выборки: **no** — Only 38 regular sports bettors (<385). — Table 2 — «Sports Betting | 1,145 | 83.5 | 189 | 13.8 | 38 | 2.8»
4. описание выборки и условий: **unclear** — Age, sex, setting and country reported; dates of data collection missing. — Participants; Procedure — «Age ranged from 14 to 20 years (M = 16.45, SD = 1.154).»
5. охват (пропуски): **unclear** — Missing CAGI data not reported. — Table 3 — «Table 3: Frequency of regular gambling according to CAGI categories (N = 862).»
6. валидность определения случая: **unclear** — CAGI GPSS with standard categories, but language version and its validation not stated. — Measures — «participants are classified into 3 categories: (1) no problem (“green light”), (2) low to moderate severity (“yellow light”), and (3) high severity (“red light…»
7. единое надёжное измерение: **yes** — Same paper questionnaire for all; reliability reported in sample. — Measures; Procedure — «a General Problem Severity Subscale (GPSS) (α = 0.79)»
8. статистика (числитель и знаменатель): **yes** — Counts per CAGI category for regular sports bettors given; numerator/denominator derivable, CI calculable. — Table 3 — «Sports Betting | 15 | 2.1 | 16 | 16.8 | 7 | 25.9»
9. отклик: **unclear** — Response/participation rate of schools and pupils not reported. — Procedure — «Students could decline participation at any point during instrument administration.»

Правки:
- 

Проверено: да

---

## ST052 · Hanss 2014 · Journal of Gambling Studies

Основной отчёт R6342: [текст](../../fulltext/text/R6342.txt) — «Prevalence and Correlates of Problem Gambling in a Representative Sample of Norwegian 17-Year-Olds» — [DOI](https://doi.org/10.1007/s10899-014-9455-4)
Не выписано ИИ: Whole-sample prevalence (2,049 17-year-olds; 536 past-month gamblers): not specific to sports bettors, so not extracted as a sample (it is the parent survey). 'Gambling on the internet (e.g., betting, poker, casino games)' (Table 2): a mixed category, not specific to sports betting, so not extracted. Later follow-ups at ages 18 and 19 are mentioned but not reported here. No treatment or help-seeking groups.
Расхождения в тексте: The text gives 2,049 classified participants, with 416 non-problem, 84 low-risk, 31 moderate-risk and 5 problem gamblers. Table 1 (by gender) totals 2,045 and shows 415 non-problem and 1,510 non-gamblers, because 4 people did not answer the gender item. The text gives 1,513 non-gamblers. Table 2 uses N=120 risk-problem gamblers (84+31+5) and N=416 non-problem gamblers, which matches the text (536 gamblers). The percentages in Table 2 match the counts: 18/120 = 15%, 7/416 = 1.7%, 16/120 = 13.3%, 21/416 = 5%. The response rate is computed as 2,059/2,923; the 2,059 includes 4 respondents excluded for being under 17.
Заметка ИИ: One sample was extracted: past-month sports bettors in a national registry sample of 17-year-olds in Norway. Players of odds games and tipping are reported only as separate rows of a reverse table (Table 2) and overlap to an unknown degree, so the total number of sports bettors cannot be derived (n_bettors = NR). The estimates are given by betting type. The only problem-gambling split available by betting type is the authors' merged 'risk-problem' group (PGSI>=1, L1) against non-problem (PGSI 0). No L2 or L3 estimate is available for sports bettors.

### ST052-1 · Norway, national registry sample of 17-year-olds, 2013: past-month sports bettors (odds games n=25; tipping n=37)
Отчёты: R6342 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | odds games | PGSI · PGSI>=1 (0-27) | **L1** | **18 / 25** | 72.0 | Table 2 | «Odds games / 18 / 15 / 7 / 1.7» |
| E2 | odds games | PGSI · PGSI 0 (0-27) | **below** | **7 / 25** | 28.0 | Table 2 | «Odds games / 18 / 15 / 7 / 1.7» |
| E3 | tipping (sports pools) | PGSI · PGSI>=1 (0-27) | **L1** | **16 / 37** | 43.2 | Table 2 | «Tipping / 16 / 13.3 / 21 / 5» |
| E4 | tipping (sports pools) | PGSI · PGSI 0 (0-27) | **below** | **21 / 37** | 56.8 | Table 2 | «Tipping / 16 / 13.3 / 21 / 5» |

- E1: cumulative: yes; источник порога: standard; правило: PGSI row; >=1 lower bound is L1 (low risk + moderate risk + problem merged by authors); у авторов: «risk-problem gambling»; главная у авторов: no; период: NR; **расчёт: Reverse table: 18 risk-problem + 7 non-problem odds-game players = 25 past-month odds-game players; cases = 18**; заметка: Risk-problem group (N=120) and non-problem group (N=416) together cover all 536 past-month gamblers without overlap. The paper does not say that odds games are sports bets, though it pairs them with sports betting in the text.
- E2: cumulative: no; источник порога: standard; правило: PGSI row; score 0 = below; у авторов: «non-problem gambling»; главная у авторов: no; период: NR; **расчёт: 18 risk-problem + 7 non-problem = 25 odds-game players; cases = 7**
- E3: cumulative: yes; источник порога: standard; правило: PGSI row; >=1 lower bound is L1 (low risk + moderate risk + problem merged by authors); у авторов: «risk-problem gambling»; главная у авторов: no; период: NR; **расчёт: Reverse table: 16 risk-problem + 21 non-problem tipping players = 37 past-month tipping players; cases = 16**; заметка: The authors gloss tipping as 'sports betting (tipping)'. It overlaps with odds-game players to an unknown degree.
- E4: cumulative: no; источник порога: standard; правило: PGSI row; score 0 = below; у авторов: «non-problem gambling»; главная у авторов: no; период: NR; **расчёт: 16 risk-problem + 21 non-problem = 37 tipping players; cases = 21**

**Ключевые поля выборки:**
- **n_bettors: NR** — Table 2 — «Odds games | 18 | 15 | 7 | 1.7 ... Tipping | 16 | 13.3 | 21 | 5»
- **sample_type: rep_survey_subsample** — Method, Participants and Procedure; Table 2 — «A sample of 3,000 17-year-olds (n = 1,500 female) was randomly drawn from the Norwegian National Registry»
- **sampling: probability** — Method, Participants and Procedure — «was randomly drawn from the Norwegian National Registry»
- **betting_period: past 30 days or month** — Measures, Gambling Behavior During Previous Month — «asked to indicate (yes vs. no) whether they had played each of the games during the past month»

**Остальные поля:**
- parent_population: 17-year-olds living in Norway (Norwegian National Registry) — Method, Participants and Procedure — «A sample of 3,000 17-year-olds (n = 1,500 female) was randomly drawn from the Norwegian National Registry»
- min_frequency: none — Measures, Gambling Behavior During Previous Month — «asked to indicate (yes vs. no) whether they had played each of the games during the past month»
- country: NOR — Method, Participants and Procedure — «A sample of 3,000 17-year-olds (n = 1,500 female) was randomly drawn from the Norwegian National Registry»
- subnational: NA — Method, Participants and Procedure — «randomly drawn from the Norwegian National Registry»
- data_years: 2013 (responses received before 1 April 2013; start date NR) — Footnote 1 — «The sample includes responses to the survey that we received before April 1st 2013.»
- design: cohort baseline — Measures, Gambling Problems — «Because the participants of this study will be followed up at ages 18 and 19 it was important that the instrument to measure gambling problems could be used fo…»
- gambling_disclosed: yes — Method, Participants and Procedure — «The letter described the purpose of the study (i.e., determining to what degree 17-year-old Norwegians are involved in gambling activities)»
- betting_mode: NR — Table 2 — «Odds games | 18 | 15 | 7 | 1.7»
- pct_online: NR — Table 2 — «Gambling on the internet (e.g., betting, poker, casino games) | 32 | 26.7 | 33 | 7.9»
- pct_inplay: NR — NA
- pct_dfs: NR — NA
- pct_esports: NR — NA
- sports_lottery: yes — Results, Gambling Behavior of Problem and Non-problem Gambl… — «playing odds games and sports betting (tipping) were more prominent among risk-problem gamblers than among non-problem gamblers.»
- mixed_race: no — Table 2 — «Odds games ... Tipping»
- legal_status: regulated legal market — Discussion — «in Norway gambling is highly regulated, and thus adolescents have restricted access to gambling options. The age limit for gambling is 18 years in Norway»
- n_invited: 3000 — Method, Participants and Procedure — «Of the 3,000 individuals contacted 2,059 completed the questionnaire.»
- n_responded: 2059 — Method, Participants and Procedure — «Of the 3,000 individuals contacted 2,059 completed the questionnaire.»
- response_rate: 70.4 — Method, Participants and Procedure — «The response rate was 70.4 % (i.e., 2,059 of 2,923) after excluding 54 people with invalid addresses»
- age_mean: NR — Method — «A sample of 3,000 17-year-olds»
- age_sd: NR — Method
- age_min: 17 — Method, Participants and Procedure — «four participants had to be excluded because they were younger than age 17»
- age_max: 17 — Method, Participants and Procedure — «A sample of 3,000 17-year-olds»
- age_group: adolescents — Title; Method — «Representative Sample of Norwegian 17-Year-Olds»
- pct_male: 47.1 — Method, Participants and Procedure — «Just over half of the remaining 2,055 participants were female (52.9 %, n = 1,088).»
- mode: mixed — Method, Participants and Procedure — «Those who decided to participate could choose between completing the paper version of the questionnaire or, alternatively, an online version of the questionnai…»
- weights: NR — Data Analysis — «Prevalence rates were computed by determining the share of participants belonging to each of five gambling categories»
- instruments: PGSI (from the CPGI; language version not stated, presumably Norwegian) — Measures, Gambling Problems — «The Problem Gambling Severity Index (PGSI) included in the Canadian Problem Gambling Index (CPGI) (Ferris and Wynne 2001) was used to assess gambling status.»
- instrument_validated_in_language: NR — Measures, Gambling Problems — «Although the PGSI was originally developed for use in the general adult population, recent studies have used the instrument in samples including adolescents»
- industry_funding: no — Acknowledgments — «This research was supported by a grant from The Research Council of Norway (grant no. 213757).»
- funding_coi: Research Council of Norway grant 213757; COI not reported — Acknowledgments — «This research was supported by a grant from The Research Council of Norway (grant no. 213757).»
- pub_status: journal — Header — «Journal of Gambling Studies; DOI: 10.1007/s10899-014-9455-4»
- language: English — Full text — «Prevalence and Correlates of Problem Gambling in a Representative Sample of Norwegian 17-Year-Olds»
- notes: Sports bettors = past-month players of 'odds games' and/or 'tipping' (the authors' 'sports betting (tipping)'). The data come only from a reverse table (Table 2: by risk-problem vs non-problem gamblers). The two betting types overlap to an unknown degree, so the total number of sports bettors cannot be derived (between 37 and 62); estimates are given per betting type. The paper does not say whether odds games are sports bets. pct_male (47.1 = 100 - 52.9% female) and age (17) describe the whole sample of 2,055, not the bettors. Underage gambling is illegal in Norway (age limit 18). The cohort …

**Риск смещения (JBI):**
1. рамка выборки: **yes** — Parent survey frame was the national population registry covering all 17-year-olds in Norway. — Method, Participants and Procedure — «randomly drawn from the Norwegian National Registry»
2. способ отбора: **yes** — Random sample from the registry. — Method, Participants and Procedure — «A sample of 3,000 17-year-olds (n = 1,500 female) was randomly drawn from the Norwegian National Registry»
3. размер выборки: **no** — Only 25 odds-game and 37 tipping past-month bettors. — Table 2 — «Odds games | 18 | 15 | 7 | 1.7 ... Tipping | 16 | 13.3 | 21 | 5»
4. описание выборки и условий: **unclear** — Age, country and setting reported, sex only for the whole sample; data collection dates only partly reported (before 1 April 2013). — Method; Footnote 1 — «The sample includes responses to the survey that we received before April 1st 2013.»
5. охват (пропуски): **yes** — Only 6 of 2,055 respondents could not be classified; missing data for bettors not reported separately but small overall. — Results, Prevalence Rates — «2,049 could be assigned to one of five gambling categories ... The remaining six participants could not be classified because of missing data.»
6. валидность определения случая: **unclear** — PGSI with standard bands, but the available sports-betting estimate is PGSI>=1 (risk-problem combined); language version and its validation are not stated; adult instrument used in adolescents. — Measures, Gambling Problems; Results — «we merged the three subgroups into one risk-problem gambling category for the remaining analyses»
7. единое надёжное измерение: **no** — Same PGSI for all and alpha reported (.85), but paper and online modes were mixed and not compared. — Method; Measures — «could choose between completing the paper version of the questionnaire or, alternatively, an online version ... Cronbach's alpha across the nine PGSI items was…»
8. статистика (числитель и знаменатель): **yes** — Counts by PGSI group for odds games and tipping can be traced to a numerator and denominator per betting type; no CI given but it can be calculated; no union of sports bettors. — Table 2 — «Risk-problem gambling (N = 120) | Non-problem gambling (N = 416)»
9. отклик: **yes** — Parent survey response rate 70.4%. — Method, Participants and Procedure — «The response rate was 70.4 % (i.e., 2,059 of 2,923)»

Правки:
- 

Проверено: да

---

## ST053 · Castrén 2013 · BMC Public Health

Основной отчёт R6580: [текст](../../fulltext/text/R6580.txt) — «An analysis of problem gambling among the Finnish working-age population: a population survey» — [DOI](https://doi.org/10.1186/1471-2458-13-519)
Расхождения в тексте: Table 3, sports betting row: in the moderate column, 24 of 33 is printed as 72.2% but works out to 72.7% (counts used as printed). Text: sports betting by 14.1% of males and 1.5% of females. Applied to the 1243 male and 1583 female respondents, that gives about 175 + 24 = 199, not the Table 3 total of 190. The denominators may differ, for example because of missing PGSI data. Text gives a gender comparison of PGSI ('low level males = 88.9%, females = 97%'; chi2(2, 2738) = 73.47) that does not match Table 2 (low 20.3% vs 9.5%; chi2(3, 2738) = 154.24). Text says 28% bet on sports at least weekly, which matches Table 3 (54/190 = 28.4%). The reported 57% response rate matches 2826/5000 = 56.5%.
Заметка ИИ: Problem-gambling categories for sports bettors come from the Table 3 sports-betting row. In that table PGSI 0 and 1-2 are merged, so separate L1 counts cannot be given. The reference period for sports betting and the PGSI time frame are not reported. The Finnish PGSI is not validated, as the authors acknowledge.

### ST053-1 · Finland AVTK 2010 health behaviour postal survey, sports bettors (n=190)
Отчёты: R6580 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | PGSI · PGSI 0-2 | **below** | **139 / 190** | 73.2 | Table 3, row 5 (Sports Betting) | «5. Sports Betting# ... Total / 139 (100) / 33 (100) / 18 (100) / 190 (100)» |
| E2 | all | PGSI · PGSI 3-7 | **L2** | **33 / 190** | 17.4 | Table 3, row 5 (Sports Betting) | «5. Sports Betting# ... Total / 139 (100) / 33 (100) / 18 (100) / 190 (100)» |
| E3 | all | PGSI · PGSI>=8 | **L3** | **18 / 190** | 9.5 | Table 3, row 5 (Sports Betting) | «5. Sports Betting# ... Total / 139 (100) / 33 (100) / 18 (100) / 190 (100)» |
| E4 | bet on sports less than once a week | PGSI · PGSI 0-2 | **below** | **103 / 136** | 75.7 | Table 3, row 5 (Sports Betting) | «5. Sports Betting# / < once a week / 103 (74.1) / 24 (72.2) / 9 (50) / 136 (71.6)» |
| E5 | bet on sports less than once a week | PGSI · PGSI 3-7 | **L2** | **24 / 136** | 17.6 | Table 3, row 5 (Sports Betting) | «5. Sports Betting# / < once a week / 103 (74.1) / 24 (72.2) / 9 (50) / 136 (71.6)» |
| E6 | bet on sports less than once a week | PGSI · PGSI>=8 | **L3** | **9 / 136** | 6.6 | Table 3, row 5 (Sports Betting) | «5. Sports Betting# / < once a week / 103 (74.1) / 24 (72.2) / 9 (50) / 136 (71.6)» |
| E7 | bet on sports at least once a week | PGSI · PGSI 0-2 | **below** | **36 / 54** | 66.7 | Table 3, row 5 (Sports Betting) | «≥ once a week / 36 (25.9) / 9 (27.3) / 9 (50) / 54 (28.4)» |
| E8 | bet on sports at least once a week | PGSI · PGSI 3-7 | **L2** | **9 / 54** | 16.7 | Table 3, row 5 (Sports Betting) | «≥ once a week / 36 (25.9) / 9 (27.3) / 9 (50) / 54 (28.4)» |
| E9 | bet on sports at least once a week | PGSI · PGSI>=8 | **L3** | **9 / 54** | 16.7 | Table 3, row 5 (Sports Betting) | «≥ once a week / 36 (25.9) / 9 (27.3) / 9 (50) / 54 (28.4)» |

- E1: cumulative: no; источник порога: standard; правило: PGSI row; combined 0-2 band has lower bound 0 = below; у авторов: «Low or no problem»; главная у авторов: no; период: NR; заметка: Table 3 combines PGSI 0 (non-problem) and 1-2 (low level); footnote: 'No problem gambling included in low level of gambling problems.'
- E2: cumulative: no; источник порога: standard; правило: PGSI row; 3-7 band starts at L2; у авторов: «Moderate (moderate level of gambling problems)»; главная у авторов: no; период: NR
- E3: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ = L3; у авторов: «Problem gambling»; главная у авторов: yes; период: NR; заметка: The authors' headline estimate is for the whole population (PGSI 8+ = 1.1%). This is the matching PGSI 8+ category for sports bettors.
- E4: cumulative: no; источник порога: standard; правило: PGSI row; combined 0-2 band has lower bound 0 = below; у авторов: «Low or no problem»; главная у авторов: no; период: NR; заметка: Subgroup by sports betting frequency
- E5: cumulative: no; источник порога: standard; правило: PGSI row; 3-7 band starts at L2; у авторов: «Moderate»; главная у авторов: no; период: NR; заметка: Printed column % 72.2 does not match 24/33 = 72.7%
- E6: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ = L3; у авторов: «Problem gambling»; главная у авторов: no; период: NR
- E7: cumulative: no; источник порога: standard; правило: PGSI row; combined 0-2 band has lower bound 0 = below; у авторов: «Low or no problem»; главная у авторов: no; период: NR; заметка: Subgroup by sports betting frequency
- E8: cumulative: no; источник порога: standard; правило: PGSI row; 3-7 band starts at L2; у авторов: «Moderate»; главная у авторов: no; период: NR
- E9: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ = L3; у авторов: «Problem gambling»; главная у авторов: no; период: NR

**Ключевые поля выборки:**
- **n_bettors: 190** — Table 3, row 5 — «5. Sports Betting# ... Total | 139 (100) | 33 (100) | 18 (100) | 190 (100)»
- **sample_type: rep_survey_subsample** — Table 3 note — «Only subjects who reported at least some amount of gambling were included in the table.»
- **sampling: probability** — Methods, Recruitment — «was sent to a random sample of Finnish adults (N=5000) aged between 15 and 64. The sample was derived from the Finnish Population Register.»
- **betting_period: NR** — Methods, Measures — «Frequency of gambling was measured using a 5-point Likert scale: not at all, less than once a week, 1–2 days per week, 3–5 days per week, 6–7 days per week.»

**Остальные поля:**
- parent_population: Finnish residents aged 15-64 (Finnish Population Register) — Methods, Recruitment — «a random sample of Finnish adults (N=5000) aged between 15 and 64. The sample was derived from the Finnish Population Register.»
- min_frequency: none — Table 3 note — «Only subjects who reported at least some amount of gambling were included in the table.»
- country: FIN — Methods, Recruitment — «sent to a random sample of Finnish adults (N=5000) aged between 15 and 64. The sample was derived from the Finnish Population Register.»
- subnational: NA — Methods, Recruitment — «The sample was derived from the Finnish Population Register.»
- data_years: 2010 — Methods, Recruitment — «During April to June 2010, a total of 2826 individuals (1243 males and 1583 females) replied to the survey.»
- design: cross-sectional — Methods, Recruitment — «An annual postal survey, entitled Health Behaviour and Health among the Finnish Adult Population (AVTK), was sent to a random sample of Finnish adults»
- gambling_disclosed: no — Methods, Recruitment — «The primary purpose of the AVTK survey was to obtain information about current health-related behaviours of working-age Finns... Two sections of gambling-relat…»
- betting_mode: NR — Methods, Measures — «e) sports betting»
- pct_online: NR — NR — «NR»
- pct_inplay: NR — NR — «NR»
- pct_dfs: NR — NR — «NR»
- pct_esports: NR — NR — «NR»
- sports_lottery: unclear — Methods, Measures — «Gambling types were: a) Lotto and Viking lotto, b) daily Keno lotteries, c) slot machines, d) scratch cards, e) sports betting, f) horse race betting»
- mixed_race: no — Table 3 — «5. Sports Betting ... 6. Horse race Betting»
- legal_status: NR — Background — «Internet games (national and international) attracted 1% of the Finns.»
- n_invited: 5000 — Methods, Recruitment — «a random sample of Finnish adults (N=5000)»
- n_responded: 2826 — Methods, Recruitment — «a total of 2826 individuals (1243 males and 1583 females) replied to the survey.»
- response_rate: 57 — Methods, Participants — «The response rate was 57%.»
- age_mean: 42.9 — Methods, Participants — «The mean age of the respondents was 42.9 years (SD = 14.4).»
- age_sd: 14.4 — Methods, Participants — «The mean age of the respondents was 42.9 years (SD = 14.4).»
- age_min: 15 — Methods, Recruitment — «a random sample of Finnish adults (N=5000) aged between 15 and 64.»
- age_max: 64 — Methods, Recruitment — «a random sample of Finnish adults (N=5000) aged between 15 and 64.»
- age_group: mixed — Methods, Recruitment — «aged between 15 and 64»
- pct_male: 44.0 — Methods, Recruitment — «a total of 2826 individuals (1243 males and 1583 females) replied to the survey.»
- mode: paper — Methods, Recruitment — «An annual postal survey... Participants sent their replies by pre-paid mail.»
- weights: NR — Limitations — «future studies would benefit from face-to-face interviews or correction weights (1.00) as suggested by Williams et al.»
- instruments: PGSI (Finnish translation) — Methods, Measures — «Finnish translation of the Problem Gambling Severity Index (PGSI), [20] where the sum of 9 items was computed, maximum points being 27»
- instrument_validated_in_language: no — Limitations — «This study used PGSI which has not been validated in a Finnish cultural context. So far, there are no validated gambling scales available in Finland.»
- industry_funding: NR — Competing interests — «The authors declare that they have no competing interests.»
- funding_coi: Funding source not reported; authors declare no competing interests. — Competing interests — «The authors declare that they have no competing interests.»
- pub_status: journal — Header — «BMC Public Health; DOI: 10.1186/1471-2458-13-519»
- language: English — Full text — «An analysis of problem gambling among the Finnish working-age population: a population survey»
- notes: Sports bettors = respondents reporting any sports betting (Table 3, 'at least some amount of gambling'); the reference period for gambling and the PGSI time frame are not stated. Age (mean, SD, range) and pct_male describe the whole responding sample (pct_male = 1243/2826 = 44.0%, derived; text says 56% female), not the sports bettors. Text: sports betting 14.1% of males, 1.5% of females. Table 3 merges PGSI 0 and 1-2 ('Low or no problem'). AVTK 2008 gambling data were published in Finnish [17]; 2011 data not yet analysed.

**Риск смещения (JBI):**
1. рамка выборки: **yes** — Parent survey frame was the Finnish Population Register, which covers the target population. — Methods, Recruitment — «The sample was derived from the Finnish Population Register.»
2. способ отбора: **yes** — Random (probability) sample drawn from the register. — Methods, Recruitment — «was sent to a random sample of Finnish adults (N=5000) aged between 15 and 64.»
3. размер выборки: **no** — Only 190 sports bettors (<385). — Table 3 — «Total | 139 (100) | 33 (100) | 18 (100) | 190 (100)»
4. описание выборки и условий: **no** — Setting, country and dates are reported, but age and sex are given only for the whole sample, not for the sports bettors. — Methods, Participants — «There were more females (56%) than males in this sample. The mean age of the respondents was 42.9 years (SD = 14.4).»
5. охват (пропуски): **unclear** — PGSI totals were available for 2738 of 2826 respondents; missing PGSI data among sports bettors is not reported. — Table 2 — «Total | 2165 (79.1) | 393 (14.4) | 150 (5.5) | 30 (1.1) | 2738 (100)»
6. валидность определения случая: **no** — PGSI with standard thresholds, but the Finnish version has no published validation (as stated by the authors). — Limitations — «This study used PGSI which has not been validated in a Finnish cultural context.»
7. единое надёжное измерение: **yes** — Same postal PGSI and scoring for all; Cronbach's alpha reported. — Methods, Measures — «using a 4-point Likert scale with 0 = never, to 3 = almost always. Cronbach's alpha was 0.79.»
8. статистика (числитель и знаменатель): **yes** — Counts and the denominator of sports bettors are given in Table 3, so a CI can be calculated; simple random sample without design weights. — Table 3 — «5. Sports Betting# ... Total | 139 (100) | 33 (100) | 18 (100) | 190 (100)»
9. отклик: **no** — Response rate 57% (<60%), with no non-response weighting and no comparison with non-responders. — Methods, Participants; Limitations — «The response rate was 57%.»

Правки:
- 

Проверено: да

