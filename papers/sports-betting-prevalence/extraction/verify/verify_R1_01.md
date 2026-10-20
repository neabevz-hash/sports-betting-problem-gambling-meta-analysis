# Проверка выписывания — файл 1 из 6

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

## ST001 · Auer 2026 · International Journal of Mental Health and Addiction

Основной отчёт R0081: [текст](../../fulltext/text/R0081.txt) · [PDF](../../fulltext/pdf/R0081.pdf) — «Using Machine-Learning Algorithms to Predict Self-Reported Problem Gambling Among a Sample of Online Gamblers» — [DOI](https://doi.org/10.1007/s11469-025-01602-2)
Расхождения в тексте: 1) Fig. 3 data labels do not match the text. In the extracted figure the 'yes' values are listed 12%, 18%, 20%, 18% in the order Lottery, Sports, Casino, Bingo, which would make casino 20% and bingo 18%. The text says casino 18%/8% and bingo 20%/12% (p.11 and p.20). For sports, both the figure position and the text give 18% (yes) and 13% (no); the text value is used. 2) The sample sizes in the data-cleaning paragraph contain typos: '2,310 to 2,069' and '2,139 to 378' against 2,130 elsewhere. The counts of 0 scores also conflict: 643 at 30 s, while 476 is reported after the 60 s rule. 3) Gender: 690 + 693 + 227 = 1,610, not 1,611. 4) Table 3 sex percentages do not sum to 100%. 5) Page 15 says 17.4% of the analysis dataset were problem gamblers; 168/963 = 17.4%, consistent.
Заметка ИИ: One eligible sample: the 121 online sports bettors within one operator's PGSI respondents. The number of cases is derived from a rounded percentage (18%). Country unclear (North America). Age and sex are given only for the whole sample.

### ST001-1 · Online customers of one North American multi-product gambling website who bet on sports in the 30 days before the PGSI, 2023-2025 (n=121)
Отчёты: R0081 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | PGSI · PGSI>=8 (range 0-27) | **L3** | **22 / 121** | 18.2 | Page 11-12, Results and Fig. 3; Page 20, Discussion | «121 had at least one wager on sports (7.5%)... The respective rates for bingo games and sports betting were 20%/12% and 18%/13%, respectively.» |
| E2 | sports-only bettors (bet exclusively on sports) | PGSI · PGSI>=8 (range 0-27) | **L3** | **2 / 16** | 12.5 | Page 13, Results | «Out of the 1,611 participants, 16 exclusively played sports games (1%). Out of these two reported problem gambling (12.5%).» |

- E1: cumulative: yes; источник порога: standard; правило: PGSI row; >=8 = L3; у авторов: «problem gambling»; главная у авторов: yes; период: NR; **расчёт: 18% x 121 = 21.8 -> 22**; заметка: The percentage among sports bettors is given only rounded (18%). The authors' headline estimate is 13% for all 1,611 players; this is the only estimate for the whole sports-bettor sample. z = 1.73, p = 0.08 versus non-sports bettors.
- E2: cumulative: yes; источник порога: standard; правило: PGSI row; >=8 = L3; у авторов: «reported problem gambling»; главная у авторов: no; период: NR; заметка: A subgroup of the 121 sports bettors who placed no wagers on lottery, casino or bingo.

**Ключевые поля выборки:**
- **n_bettors: 121** — Page 11, Results — «121 had at least one wager on sports (7.5%)»
- **sample_type: gamblers_survey_subsample** — Page 11, Results — «Out of the 1,611 players, ... 121 had at least one wager on sports (7.5%)»
- **sampling: operator_customers** — Page 7, Method — «a secondary dataset from a North American online gambling website»
- **betting_period: past 30 days or month** — Page 7, Method; Page 11, Results — «as well as age and gender, in the 30 days prior to answering the PGSI.»

**Остальные поля:**
- parent_population: Customers of one North American online gambling website (lottery, casino, bingo, sports betting) who answered the PGSI and wagered at least once in the prior 30 days, after removal of PGSI completions under one minute — Page 7, Method; Page 10, Data Cleaning — «Only players who wagered at least once during the 30 days prior to answering the PGSI or on the day of answering the PGSI were available to the authors.»
- min_frequency: none (at least one sports wager in the 30 days before the PGSI) — Page 11, Results — «121 had at least one wager on sports (7.5%)»
- country: NR — Page 7, Method — «The authors had access to a secondary dataset from a North American online gambling website which offers lottery games, casino games, and bingo games, as well …»
- subnational: NR — Page 7, Method — «a North American online gambling website»
- data_years: 2023-2025 — Page 7, Method — «Each of the participants answered the PGSI between April 2023 and February 2025»
- design: cross-sectional — Page 6, The Present Study — «utilizing a new secondary dataset from a sample of real-world online gamblers»
- gambling_disclosed: NR — Page 7, Method — «the time interval, measured in seconds, between a player's initial click on the PGSI site and the final submission»
- betting_mode: online only — Page 7, Method — «a North American online gambling website»
- pct_online: all — Page 7, Method — «a North American online gambling website»
- pct_inplay: NR — NA
- pct_dfs: NR — NA
- pct_esports: NR — NA
- sports_lottery: unclear — Page 7, Method — «offers lottery games, casino games, and bingo games, as well as sports betting»
- mixed_race: no — Page 11, Results — «121 had at least one wager on sports (7.5%)»
- legal_status: NR — NA
- n_invited: NR — NA
- n_responded: 2130 — Page 10, Data Cleaning — «A total of 2,130 players answered the PGSI between April 2023 and February 2025 and placed at least one bet in the 30 days prior to answering the PGSI.»
- response_rate: NR — NA
- age_mean: 55 — Page 11, Results — «The average age among the 1,611 players was 55 years (SD = 16).»
- age_sd: 16 — Page 11, Results — «The average age among the 1,611 players was 55 years (SD = 16).»
- age_min: NR — NA
- age_max: NR — NA
- age_group: NR — Page 17 — «six age groups (younger than 25 years, 25–34 years, 35–44 years, 45–54 years, 55–64 years, and older than 64 years)»
- pct_male: 43 — Page 11, Results — «The sample (N = 1611) comprised 690 females (42.8%), 693 males (43%), and 227 'other' (14%).»
- mode: online — Page 7, Method — «between a player's initial click on the PGSI site and the final submission after completing all nine PGSI questions»
- weights: no — Page 11, Results — «Out of the 1,611 players, 209 had a PGSI score of 8 or more (13%)»
- instruments: PGSI (9 items, Ferris & Wynne 2001; English items listed in Appendix 1) — Page 7, Method; Page 24, Appendix 1 — «Players were given four response options for each of the nine PGSI items: 'Never' (0), 'Sometimes' (1), 'Most of the time' (2), and 'Almost always' (3), result…»
- instrument_validated_in_language: yes — Page 24, Appendix 1 — «Items in the Problem Gambling Severity Index (Ferris & Wynne, 2001)»
- industry_funding: NR — Page 26, Funding — «Funding Not applicable.»
- funding_coi: No funding for this study; the operator supplied the data. Both authors received research funding from Norsk Tipping and do consultancy for gaming companies. MDG has received GambleAware funding. The first author works at Neccton GmbH. — Page 26, Declarations; Page 1 affiliations — «Both authors have received research funding from Norsk Tipping (the gambling operator owned by the Norwegian government)... Both authors undertake consultancy …»
- pub_status: journal — Page 1 — «International Journal of Mental Health and Addiction (2026) 24:4436–4464»
- language: English — Page 1 — «Using Machine-Learning Algorithms to Predict Self-Reported Problem Gambling Among a Sample of Online Gamblers»
- notes: Secondary player-tracking data from one operator. Sports bettors are the 121 of the 1,611 cleaned players (2,130 before removing PGSI completions under 60 s) with at least one sports wager in the 30 days before the PGSI. Age (mean 55, SD 16) and sex (43% male, 14% 'other') describe the whole cleaned sample of 1,611, not the sports bettors. The country is given only as 'North American' (USA or Canada not specified). The PGSI time frame is not stated. How players were invited to answer the PGSI is not described. The ML analyses use 963 non-lottery-only players. Only PGSI>=8 is reported; no othe…

**Риск смещения (JBI):**
1. рамка выборки: **no** — The frame is the customers of one online operator who completed the PGSI; it does not cover sports bettors in general. — Page 23, Limitations — «the dataset was limited to a single online gambling operator which may not fully generalize to other platforms»
2. способ отбора: **no** — Players who chose to answer the PGSI on the operator site (self-selected); no probability sampling. — Page 10, Data Cleaning — «A total of 2,130 players answered the PGSI between April 2023 and February 2025»
3. размер выборки: **no** — Only 121 sports bettors (<385). — Page 11 — «121 had at least one wager on sports (7.5%)»
4. описание выборки и условий: **unclear** — Age, sex, setting and dates are reported (for the whole sample); the country is given only as 'North American'. — Page 7; Page 11 — «a North American online gambling website»
5. охват (пропуски): **no** — 519 of 2,130 respondents (24%) were excluded for completing the PGSI in under one minute; how this affected sports bettors is not reported. — Page 10, Data Cleaning — «players who answered the nine PGSI questions in less than one minute were removed from the analysis... The cleaned dataset comprised 1,611 players.»
6. валидность определения случая: **yes** — PGSI with the standard >=8 threshold; English items, validated by Ferris & Wynne. — Page 7; Appendix 1 — «A score of 8 or greater indicates problem gambling.»
7. единое надёжное измерение: **unclear** — Same online PGSI for everyone, but no reliability is reported for this sample. — Page 7, Method — «Players were given four response options for each of the nine PGSI items»
8. статистика (числитель и знаменатель): **unclear** — The denominator (121) is given, but the numerator is only a rounded percentage in a figure and the text; no CI. — Page 12, Fig. 3; Page 20 — «The respective rates for bingo games and sports betting were 20%/12% and 18%/13%, respectively.»
9. отклик: **no** — No denominator of invited players; no response rate and no non-response handling. — Page 10 — «A total of 2,130 players answered the PGSI»

Правки:
- 

Проверено: да

---

## ST002 · Biaou 2026 · Santé Publique

Основной отчёт R0129: [текст](../../fulltext/text/R0129.txt) · [PDF](../../fulltext/pdf/R0129.pdf) — «Troubles liés à l’usage des jeux de hasard et d’argent chez les adolescents et jeunes adultes en Afrique subsaharienne : analyse exploratoire de la prévalence …» — [DOI](https://doi.org/10.3917/spub.263.0279)
Не выписано ИИ: Students who gambled but did not bet on sports (154 of 455), and all gamblers (455) and all students (1,360), are excluded because they are not sports-bettor samples. Estimates for those groups (19.6% among gamblers, 6.5% among all students, severity bands 12.1/6.8/0.7%) are not extracted.
Расхождения в тексте: Share of sports bettors: text (p.6) says 66.2%, Table III says 301 (66.1%); the table is used. Share of men among gamblers: text says 81.4%, Table I says 369 (81.1%); the table is used. Internet access: text says 87.6% have frequent access, Table II says 404 (88.8%). Exposure to advertising: text says 62.5%, Table II says 391 (85.9%). Gambling-app influencer: text says 33.3%, Table II says 34.3%. Table IV is titled 'Bénin, 2024' while the rest says 2025. The English abstract says 'online gambling' duration, but the French text says duration of gambling in general.
Заметка ИИ: One eligible sample: the sports bettors among randomly sampled university students. The only sports-bettor estimate is DSM-5 >=4: 72/301. Questions for the reviewer: is legal status coded NR correctly, given the text only mentions a regulatory framework? And does the questionnaire's language and validation affect JBI item 6?

### ST002-1 · University students who bet on sports, Cotonou/Dassa-Zoumè/Parakou, Benin, 2024-2025 (n=301)
Отчёты: R0129 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | DSM-5-screen · DSM-5 criteria>=4 (score >3 on 9 criteria, range 0-9) | **L3** | **72 / 301** | 23.9 | Page 13, Tableau IV (Jouer aux paris sportifs) | «Jouer aux paris sportifs 0,001 Oui 72 (23,92) 229 (76,08) 2,5 (1,43 – 4,47)» |

- E1: cumulative: yes; источник порога: standard; правило: DSM-5-screen row; >=4 is L3; у авторов: «troubles liés à l'usage des JHA [gambling-related disorders]»; главная у авторов: no; период: NR; заметка: 23.92% among sports bettors. n = 72 + 229 = 301, matching Table III. The authors' primary estimate is for all gamblers (89/455 = 19.6%). The severity breakdown is not given by activity.

**Ключевые поля выборки:**
- **n_bettors: 301** — Page 9, Tableau III; Page 13, Tableau IV — «Jouer aux paris sportifs Oui 301 66,1»
- **sample_type: students** — Page 4, Population et échantillonnage — «La population d'étude était constituée des étudiants inscrits pour l'année universitaire 2024–2025 dans les établissements d'enseignement supérieur publics ou privés des villes concernées»
- **sampling: probability** — Page 4, Population et échantillonnage — «deux écoles/facultés des universités privées et deux des universités publiques [...] choisies par ville par sondage aléatoire simple [...] 15 % des classes ont été choisies de façon aléatoire [...] Tous les étudiants présents [...] ont été inclus»
- **betting_period: past 12 months** — Page 6, Résultats — «455 (33,5 %) avaient joué à un JHA au cours des douze derniers mois précédents l'enquête [had gambled in the 12 months before the survey]»

**Остальные поля:**
- parent_population: Students enrolled in 2024-2025 at public and private higher-education institutions in Cotonou, Dassa-Zoumè and Parakou, Benin, present in class on survey day — Page 4, Population et échantillonnage — «étudiants inscrits pour l'année universitaire 2024–2025 [...] présents dans les salles de cours ou les amphithéâtres lors de la collecte des données»
- min_frequency: none — Page 9, Tableau III — «Fréquence de jeux 1 à 4 fois par mois 305 67,0 1 à 3 fois par semaine 124 27,3 Tous les jours 26 5,7»
- country: BEN — Page 4, Cadre d'étude — «trois villes universitaires du Bénin, à savoir : Cotonou (urbaine, sud du Bénin), Dassa-Zoumè (semi-urbaine, centre du Bénin) et Parakou (urbaine, nord du Béni…»
- subnational: Cotonou, Dassa-Zoumè and Parakou (three university towns) — Page 4, Cadre d'étude — «établissements d'enseignement supérieurs privés et publics de trois villes universitaires du Bénin, à savoir : Cotonou [...], Dassa-Zoumè [...] et Parakou»
- data_years: 2024-2025 — Page 4, Type d'étude — «collectées sur une période de trois mois (du 05 novembre 2024 au 07 février 2025)»
- design: cross-sectional — Page 4, Type d'étude — «Il s'est agi d'une étude transversale à visée analytique [It was a cross-sectional analytical study]»
- gambling_disclosed: NR — Page 6, Déroulement de la collecte — «Leur rôle consistait à expliquer le contexte, les objectifs et la méthodologie de l'étude [Their role was to explain the context, aims and methods of the study]»
- betting_mode: both — Page 9, Tableau III — «Moyen d'accès aux JHA Accès en ligne 399 87,7 Accès physique 37 8,1 En ligne et physique 19 4,2»
- pct_online: NR — Page 9, Tableau III — «Accès en ligne 399 87,7 [...] En ligne et physique 19 4,2»
- pct_inplay: NR — NA
- pct_dfs: NR — NA
- pct_esports: NR — NA
- sports_lottery: unclear — Page 9, Tableau III — «Jouer aux paris sportifs Oui 301 66,1 [...] Jouer à la loterie Oui 26 5,7»
- mixed_race: no — Page 9, Tableau III — «Jouer au PMU Oui 3 0,7 [...] Jouer aux paris sportifs Oui 301 66,1»
- legal_status: NR — Page 4, Introduction — «malgré l'existence d'un cadre réglementaire instauré par les autorités afin de mieux encadrer ces activités sur le territoire béninois [despite a regulatory fr…»
- n_invited: NR — NA
- n_responded: 1360 — Page 6, Résultats — «Au final, 1 360 étudiants ont répondu à ce sondage»
- response_rate: NR — Page 4, Population et échantillonnage — «un taux de non-réponse estimé à 10,0 %, soit 1 337 étudiants [planned non-response for sample size only]»
- age_mean: NR — Page 7, Tableau I — «Tranche d'âge 15 – 20 287 63,1 21 et plus 168 36,9»
- age_sd: NR — NA
- age_min: 15 — Page 7, Tableau I — «Tranche d'âge 15 – 20 287 63,1»
- age_max: NR — Page 7, Tableau I — «21 et plus 168 36,9»
- age_group: mixed — Page 7, Tableau I — «Tranche d'âge 15 – 20 287 63,1 21 et plus 168 36,9»
- pct_male: 81.1 — Page 7, Tableau I — «Sexe Masculin 369 81,1 Féminin 86 18,9»
- mode: online — Page 6, Déroulement de la collecte — «collectées de manière anonyme via un questionnaire digitalisé sur le serveur KoBoToolbox , dont le lien a été partagé avec les étudiants le jour de l'enquête»
- weights: NR — Page 6, Traitement et analyse des données — «les fréquences ont été calculées pour les variables catégorielles»
- instruments: DSM-5 nine criteria for gambling disorder, self-report (scored 0/1, total 0-9), questionnaire language not stated (article in French) — Page 5, Instruments de mesure — «la présence de troubles liés à l'usage des JHA a été évaluée en utilisant les neuf critères diagnostics du DSM-V [6]»
- instrument_validated_in_language: NR — Page 5, Instruments de mesure — «Cet outil a démontré une validité et une fiabilité adéquates et a été recommandé pour les études de prévalence examinant le jeu chez les adolescents et les jeu…»
- industry_funding: NR — Page 17, Liens d'intérêts — «Les auteurs déclarent n'avoir connaissance d'aucun conflit d'intérêts en lien avec le contenu de l'article.»
- funding_coi: Funding not reported; authors declare no conflicts of interest — Page 17, Liens d'intérêts — «Les auteurs déclarent n'avoir connaissance d'aucun conflit d'intérêts»
- pub_status: journal — Page 1 — «Dans Santé Publique 2026/3 vol. 38 , pages 279 à 295»
- language: French — Page 2-17 — «Troubles liés à l'usage des jeux de hasard et d'argent chez les adolescents et jeunes adultes en Afrique subsaharienne»
- notes: Sports bettors = gamblers (past-12-month JHA) answering yes to 'Jouer aux paris sportifs' (301 of 455 gamblers); the sports-betting item's own reference period is not stated separately. Age bands, pct_male (81.1%), betting mode and frequency describe all 455 past-year gamblers, not sports bettors only. No mean age is reported; age_min 15 is the lower bound of the youngest age band. Severity (mild/moderate/severe) is reported only for all gamblers. The authors' main prevalence is for all gamblers (89/455 = 19.6%). Legal status: the text mentions a regulatory framework (national operators and o…

**Риск смещения (JBI):**
1. рамка выборки: **no** — The frame (DGES list of institutions) covers only three towns, while the study describes university students in Benin. It also covers only students present in class on the survey day. — Page 4; Page 16 — «L'étude a été menée uniquement dans trois communes et pourrait ne pas refléter pleinement la réalité des autres régions du pays.»
2. способ отбора: **yes** — Multi-stage random sampling of institutions and classes, then all students present in the selected classes. — Page 4, Population et échantillonnage — «choisies par ville par sondage aléatoire simple [...] 15 % des classes ont été choisies de façon aléatoire et sans remise»
3. размер выборки: **no** — 301 sports bettors, which is below 385. — Page 9, Tableau III — «Jouer aux paris sportifs Oui 301 66,1»
4. описание выборки и условий: **yes** — Age bands, sex, setting, country and dates are reported, though for all gamblers rather than sports bettors only. — Page 4; Page 7, Tableau I — «du 05 novembre 2024 au 07 février 2025 [...] Masculin 369 81,1»
5. охват (пропуски): **yes** — All 301 sports bettors are classified as having or not having the disorder (72 + 229 = 301). — Page 13, Tableau IV — «Jouer aux paris sportifs [...] Oui 72 (23,92) 229 (76,08)»
6. валидность определения случая: **unclear** — Self-reported DSM-5 criteria with the standard threshold of 4 or more. The item wording, language version and validation are not cited, and the time frame is not stated. — Page 5, Instruments de mesure — «Le trouble était considéré comme présent si le score total était strictement supérieur à 3»
7. единое надёжное измерение: **unclear** — Same instrument and online mode for everyone. Reliability is asserted but not reported for this sample or cited. — Page 5, Instruments de mesure — «Cet outil a démontré une validité et une fiabilité adéquates»
8. статистика (числитель и знаменатель): **yes** — Numerator (72) and denominator (301) of sports bettors are clear, so a CI can be calculated. No weights were used; the cluster design was not accounted for. — Page 13, Tableau IV — «Oui 72 (23,92) 229 (76,08)»
9. отклик: **unclear** — The number of students invited or present is not reported, so the response rate cannot be determined. — Page 6, Résultats — «Au final, 1 360 étudiants ont répondu à ce sondage»

Правки:
- 

Проверено: да

---

## ST003 · Coloma-Carmona 2026 · Adicciones

Основной отчёт R0534: [текст](../../fulltext/text/R0534.txt) · [PDF](../../fulltext/pdf/R0534.pdf) — «Traditional gambling, betting in video games, and financial trading: Associations with gambling severity and associated harm in young adults.» — [DOI](https://doi.org/10.20882/adicciones.2512)
Расхождения в тексте: Table 2 and the text agree: there are 185 sports bettors (18.2%), and the whole-sample PGSI categories (671/148/85/114) add up to 1,018. Only 450 of 1,018 answered the main-access-mode question (223+189+38=450), yet the text gives those percentages without noting the reduced denominator. The Discussion gives an aOR of 2.83 for commodity trading, while the Results give 2.86. That does not affect the extraction.
Заметка ИИ: The PGSI distribution among sports bettors is shown only in Figure 1, which is an image with no numbers in the text. The reviewer must read the 'Apuestas deportivas' bars from the figure (or the supplementary OSF material, https://osf.io/gh9ab) to fill in the cases for n=185.

### ST003-1 · Spain, online panel of young adult gamblers (18-34), RCT baseline Dec 2024-Jan 2025: sports bettors in past 60 days, n=185
Отчёты: R0534 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | PGSI · PGSI 0 | **below** | **NR / 185** |  | Page 8, Figura 1 | «Figura 1 Distribución de la gravedad del juego (PGSI) entre los participantes de cada tipo de actividad de juego» |
| E2 | all | PGSI · PGSI 1-2 | **L1** | **NR / 185** |  | Page 8, Figura 1 | «Figura 1 Distribución de la gravedad del juego (PGSI) entre los participantes de cada tipo de actividad de juego» |
| E3 | all | PGSI · PGSI 3-7 | **L2** | **NR / 185** |  | Page 8, Figura 1 | «Figura 1 Distribución de la gravedad del juego (PGSI) entre los participantes de cada tipo de actividad de juego» |
| E4 | all | PGSI · PGSI>=8 | **L3** | **NR / 185** |  | Page 8, Figura 1 | «Figura 1 Distribución de la gravedad del juego (PGSI) entre los participantes de cada tipo de actividad de juego» |
| E5 | esports | PGSI · PGSI>=8 | **L3** | **31 / 53** | 58.5 | Page 7, Results text; Page 6, Tabla 2 | «También se registraron porcentajes elevados de juego problemático en los que participaban en actividades gamblificadas relacionadas con videojuegos, como ... las apuestas en eSports (58,5%); Apuestas en eSports 5,2 (53)» |

- E1: cumulative: no; источник порога: standard; правило: PGSI row; score 0 is below L1; у авторов: «juego no problemático [non-problem gambling]»; главная у авторов: no; период: past 12 months; заметка: The value is shown only in Figure 1 (graphic, not in the text). The reviewer should read the percentage for 'Apuestas deportivas' from the figure and apply it to n=185.
- E2: cumulative: no; источник порога: standard; правило: PGSI row; 1-2 band starts at L1; у авторов: «bajo riesgo [low risk]»; главная у авторов: no; период: past 12 months; заметка: Shown only in Figure 1 (graphic). Read from the figure.
- E3: cumulative: no; источник порога: standard; правило: PGSI row; 3-7 band starts at L2; у авторов: «riesgo moderado [moderate risk]»; главная у авторов: no; период: past 12 months; заметка: Shown only in Figure 1 (graphic). Read from the figure.
- E4: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ = L3; у авторов: «juego problemático [problem gambling]»; главная у авторов: no; период: past 12 months; заметка: Shown only in Figure 1 (graphic); the text does not give the sports-betting percentage. The authors' primary estimate is for the whole sample (11.2%, 114/1,018), not for sports bettors.
- E5: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ = L3; у авторов: «juego problemático [problem gambling]»; главная у авторов: no; период: past 12 months; **расчёт: 58.5% x 53 = 31.0 -> 31**; заметка: Esports bettors in the past 60 days. Their overlap with the 185 sports bettors is unknown, so this group may not be a strict subgroup of them. The other PGSI categories for esports appear only in Figure 1.

**Ключевые поля выборки:**
- **n_bettors: 185** — Page 6, Tabla 2 — «Apuestas deportivas 18,2 (185)»
- **sample_type: gamblers_survey_subsample** — Page 3-4, Diseño y procedimiento; Page 6, Tabla 2 — «La muestra fue reclutada mediante un panel online gestionado por una empresa externa [recruited through an online panel run by an external company]; Apuestas deportivas 18,2 (185)»
- **sampling: convenience** — Page 3-4, Diseño y procedimiento — «La invitación se envió exclusivamente a personas inscritas en el panel que cumplían el rango de edad establecido (18-34 años) [Invitation sent only to panel members in the age range]»
- **betting_period: NR** — Page 5, Variables predictoras — «Se evaluó la participación (sí/no) en los últimos 60 días en ocho productos de juego ... (2) apuestas deportivas [participation in the past 60 days ... sports betting]»

**Остальные поля:**
- parent_population: Young adults aged 18-34 living in Spain, members of a commercial online panel, who gambled (traditional gambling) in the past 60 days (those only betting in video games or trading excluded) — Page 3-4, Participantes — «se excluyeron del análisis a aquellos participantes cuya implicación se limitaba exclusivamente a las apuestas en videojuegos o el trading de activos financier…»
- min_frequency: none (any sports betting in the past 60 days) — Page 5, Variables predictoras — «Se evaluó la participación (sí/no) en los últimos 60 días»
- country: ESP — Page 3, Diseño y procedimiento — «tener entre 18 y 34 años, residir en España»
- subnational: NA — Page 3 — «residir en España [living in Spain]»
- data_years: 2024-2025 — Page 3, Diseño y procedimiento — «La recogida de datos se llevó a cabo entre diciembre de 2024 y enero de 2025. [Data were collected between December 2024 and January 2025.]»
- design: experiment baseline — Page 3, Diseño y procedimiento; Page 4 — «La muestra analizada en este estudio procede de un ensayo controlado aleatorizado registrado (ClinicalTrials.gov ID: NCT06681103) [The sample comes from a regi…»
- gambling_disclosed: NR — Page 3-4, Diseño y procedimiento — «Quienes aceptaron participar completaron una breve evaluación de elegibilidad para verificar el cumplimiento de los criterios de inclusión.»
- betting_mode: both — Page 5, Variables predictoras — «No se diferenciaron los canales de acceso (online, presencial o mixto) para cada actividad [Access channels were not differentiated for each activity]»
- pct_online: NR — Page 6-7, Tabla 2 (cont.), note a — «Dado que no se registró el modo de acceso (online o presencial) para cada actividad específica»
- pct_inplay: NR — NA — «NR»
- pct_dfs: NR — NA — «NR»
- pct_esports: NR — Page 6, Tabla 2 — «Apuestas en eSports 5,2 (53)»
- sports_lottery: no — Page 6, Tabla 2 — «Loterías, primitiva, quinielas, bonoloto, cupones ONCE, eurojackpot 87,9 (895); Apuestas deportivas 18,2 (185)»
- mixed_race: no — Page 6, Tabla 2 — «Apuestas deportivas 18,2 (185); Apuestas en carreras de caballos 4,4 (45)»
- legal_status: NR — NA — «NR»
- n_invited: NR — Page 4, Participantes — «De las 1.889 personas que accedieron a la encuesta»
- n_responded: 1889 — Page 4, Participantes — «De las 1.889 personas que accedieron a la encuesta, 1.112 cumplían los criterios de inclusión.»
- response_rate: NR — NA — «NR»
- age_mean: 28.6 — Page 4, Tabla 1 — «Edad, M (DT, Rango) 28,6 (4,4; 18-34)»
- age_sd: 4.4 — Page 4, Tabla 1 — «Edad, M (DT, Rango) 28,6 (4,4; 18-34)»
- age_min: 18 — Page 4, Tabla 1 — «Edad, M (DT, Rango) 28,6 (4,4; 18-34)»
- age_max: 34 — Page 4, Tabla 1 — «Edad, M (DT, Rango) 28,6 (4,4; 18-34)»
- age_group: adults — Page 3 — «tener entre 18 y 34 años»
- pct_male: 44.2 — Page 4, Tabla 1 — «Hombre 44,2 (450)»
- mode: online — Page 3, Diseño y procedimiento — «Cada participante pudo acceder una sola vez a la encuesta a través de un enlace personalizado.»
- weights: NR — Page 5, Análisis de datos — «Se calcularon estadísticos descriptivos (medias, desviaciones típicas, frecuencias y porcentajes)»
- instruments: PGSI, Spanish version (López-González et al., 2018), past 12 months; SGHS (Short Gambling Harm Screen; harm measure, not a problem-gambling screen) — Page 4, Variables criterio — «Se evaluó mediante el Problem Gambling Severity Index, en su versión española (PGSI; Ferris y Wynne, 2001; López-González et al., 2018), estableciendo como mar…»
- instrument_validated_in_language: yes — Page 4; References p.16 — «La versión española del PGSI ha mostrado una excelente consistencia interna (αordinal=0,97); Lopez-Gonzalez ... (2018). Spanish validation of the Problem Gambl…»
- industry_funding: no — Page 13, Reconocimientos — «La presente investigación fue financiada por la Dirección General de Ordenación del Juego (Ministerio de Derechos Sociales, Consumo y Agenda 2030) (Ref. SUBV23…»
- funding_coi: Funded by the Spanish gambling regulator (DGOJ, Ministry of Social Rights, Consumer Affairs and Agenda 2030), Ref. SUBV23/00004; authors declare no conflicts of interest — Page 13, Reconocimientos; Conflicto de intereses — «Todos los autores declaran que no existe conflicto de interés»
- pub_status: journal — Page 1 — «ADICCIONES, 2026 · VOL. 38 N. 1»
- language: Spanish — Whole text — «Juego tradicional, apuestas en videojuegos y trading financiero: Asociaciones con la gravedad del juego y el daño asociado en adultos jóvenes»
- notes: Sports bettors defined by participation in the past 60 days (this period is not in the code list, so betting_period = NR). This is the baseline of an RCT (NCT06681103; protocol Coloma-Carmona et al. 2026, JMIR Res Protoc). Age, sex and PGSI reliability describe the whole analysed sample (N=1,018), not the sports bettors. Only 450 of 1,018 answered the main-access-mode question, and mode was not recorded per activity. The PGSI distribution among sports bettors appears only in Figure 1 (a graphic), not in the text. Esports bettors (n=53) were asked about separately; their overlap with the 185 s…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame is one commercial online research panel, which covers only part of young adult sports bettors in Spain. — Page 3-4; Page 12, limitations — «El uso de un panel online como estrategia de reclutamiento limita la generalización de los resultados»
2. способ отбора: **no** — Non-probability, opt-in online panel. — Page 3-4, Diseño y procedimiento — «La muestra fue reclutada mediante un panel online gestionado por una empresa externa especializada»
3. размер выборки: **no** — 185 sports bettors, below 385. — Page 6, Tabla 2 — «Apuestas deportivas 18,2 (185)»
4. описание выборки и условий: **yes** — Age, sex, setting, country and dates are reported (age and sex for the whole analysed sample only). — Page 3-4, Tabla 1 — «La recogida de datos se llevó a cabo entre diciembre de 2024 y enero de 2025; Edad, M (DT, Rango) 28,6 (4,4; 18-34)»
5. охват (пропуски): **yes** — PGSI categories add up to the full analysed sample (671+148+85+114=1,018), so no missing PGSI data. — Page 7, Tabla 2 (cont.) — «No problemático (PGSI=0) 65,9 (671); Riesgo bajo (PGSI 1-2) 14,5 (148); Riesgo medio (PGSI 3-7) 8,3 (85); Problemático (PGSI ≥8) 11,2 (114)»
6. валидность определения случая: **yes** — PGSI Spanish version with a published validation, standard 8+ threshold. — Page 4, Variables criterio — «se aplicó la categorización habitual de la escala en cuatro niveles de riesgo ... juego problemático (PGSI≥8)»
7. единое надёжное измерение: **yes** — Same online PGSI and time frame for everyone; reliability reported for this sample. — Page 4 — «En la presente muestra, la consistencia interna del PGSI fue de ω=0,94.»
8. статистика (числитель и знаменатель): **no** — The PGSI distribution for sports bettors is shown only graphically (Figure 1). No counts or CI for sports bettors are given in the text. — Page 7-8, Figura 1 — «Figura 1 Distribución de la gravedad del juego (PGSI) entre los participantes de cada tipo de actividad de juego»
9. отклик: **no** — Online panel with no denominator of invited people and no non-response handling. — Page 4, Participantes — «De las 1.889 personas que accedieron a la encuesta, 1.112 cumplían los criterios de inclusión.»

Правки:
- 

Проверено: да

---

## ST004 · Hawker 2026 · Journal of gambling studies

Основной отчёт R0712: [текст](../../fulltext/text/R0712.txt) · [PDF](../../fulltext/pdf/R0712.pdf) — «A Cross-Sectional Examination of the Relationships Between Sports and Race Betting Motives, Expenditure, Problem Severity, and Harm in Young Australian Adults.» — [DOI](https://doi.org/10.1007/s10899-026-10533-z)
Не выписано ИИ: Regular race betting sample (n=127; race-specific PGSI, n=120 analysed): race betting only (horse, harness, greyhound), so not sports betting; 124 of them overlap with the sports sample. The whole sample of 188 was not extracted as a unit: it includes 3 race-only bettors and has no PGSI for all bettors combined.
Расхождения в тексте: The text gives 11.4% non-problem and 88.7% at some risk. Table 2 gives 21/185 (11.35%), and 164/185 is 88.65%: rounding differences only. Text and table agree for 32.4%, 38.4% and 17.8%. The Table 2 categories (21+33+71+60) add up to 185. Table 2 shows SD 23.23 for race-betting financial motives, which looks like a typo; it does not affect sports estimates. On page 13 the text gives race coping B = 0.18, but Table 5 gives 1.3 (race sample only).
Заметка ИИ: One eligible sample extracted. The PGSI was reworded for sports betting with 0-3 item scoring unchanged, so it is coded PGSI. Legal status of sports betting is not described in the text.

### ST004-1 · Regular sports bettors aged 18-30, Australian community online survey (EMA baseline), 2023-2024, n=185
Отчёты: R0712 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | PGSI · PGSI 0 | **below** | **21 / 185** | 11.4 | Page 9, Table 2 | «Non-problem betting, n (%) 21 (11.35)» |
| E2 | all | PGSI · PGSI 1-2 | **L1** | **33 / 185** | 17.8 | Page 9, Table 2 | «Low-risk betting, n (%) 33 (17.84)» |
| E3 | all | PGSI · PGSI 3-7 | **L2** | **71 / 185** | 38.4 | Page 9, Table 2 | «Moderate-risk betting, n (%) 71 (38.38)» |
| E4 | all | PGSI · PGSI>=8 | **L3** | **60 / 185** | 32.4 | Page 9, Table 2; Page 8, Results | «Problem betting, n (%) 60 (32.43)» |
| E5 | all | PGSI · PGSI>=1 | **L1** | **164 / 185** | 88.6 | Page 8, Results | «In the regular sports betting sample, 88.7% endorsed some level of risk on the adapted PGSI (32.4% problem betting, 38.4% moderate-risk, 17.8% low-risk)» |

- E1: cumulative: no; источник порога: standard; правило: PGSI row; score 0 = below L1; у авторов: «non-problem betting»; главная у авторов: no; период: past 12 months; заметка: Sports-specific adapted PGSI
- E2: cumulative: no; источник порога: standard; правило: PGSI row; 1-2 band starts at L1; у авторов: «low-risk betting»; главная у авторов: no; период: past 12 months
- E3: cumulative: no; источник порога: standard; правило: PGSI row; 3-7 band starts at L2; у авторов: «moderate-risk betting»; главная у авторов: no; период: past 12 months
- E4: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ = L3; у авторов: «problem betting»; главная у авторов: yes; период: past 12 months; заметка: Prevalence was descriptive only; the study's main aim was motives-outcome associations.
- E5: cumulative: yes; источник порога: standard; правило: PGSI row; >=1 = L1; у авторов: «endorsed some level of risk»; главная у авторов: no; период: past 12 months; **расчёт: 88.7% x 185 = 164.1 -> 164 (equals 33+71+60 from Table 2)**; заметка: Cumulative figure reported by authors in text; 164/185 = 88.65%.

**Ключевые поля выборки:**
- **n_bettors: 185** — Page 9, Table 2 — «Regular sports betting (n = 185)»
- **sample_type: bettor_recruited** — Page 4, Participants — «endorsed regular online betting on sports events or racing events (operationalised as betting at least twice in the past month and at least twice in a typical month over the past 12 months)»
- **sampling: convenience** — Page 7, Procedure — «using convenience and snowball sampling via social media (e.g., Facebook, Instagram), online advertising platforms (e.g., Google Ads, Gumtree), and online forums related to sports and race betting and gambling help-seeking»
- **betting_period: past 30 days or month** — Page 4, Participants — «betting at least twice in the past month and at least twice in a typical month over the past 12 months»

**Остальные поля:**
- parent_population: NA — Page 4, Participants — «Within the total sample, 185 participants met criteria for regular sports betting»
- min_frequency: at least twice in the past month and at least twice in a typical month over the past 12 months — Page 4, Measures — «regular engagement (i.e., betting at least twice in the past month and in a typical month over the past 12 months) in the relevant activity»
- country: AUS — Page 4, Participants — «(2) resided in Australia»
- subnational: NA — Page 4, Participants — «188 young adults recruited from the Australian community»
- data_years: 2023-2024 — Page 7, Procedure — «Participants were recruited between December 2023 and February 2024»
- design: EMA baseline — Page 3, Study Design and Terminology — «This study employed a cross-sectional design, analysing baseline survey data collected as part of a broader Ecological Momentary Assessment (EMA) project»
- gambling_disclosed: yes — Page 7, Procedure; Page 4, Participants — «online forums related to sports and race betting and gambling help-seeking. Recruitment materials directed participants to an online Qualtrics survey»
- betting_mode: both — Page 9, Table 2 — «Smartphone application 79.76 (24.44) ... Self-service terminal at a venue 4.11 (10.57) In person at a venue 3.32 (8.35)»
- pct_online: NR — Page 4, Participants; Page 9, Table 2 — «endorsed regular online betting on sports events or racing events ... via a mobile phone, tablet, or computer»
- pct_inplay: NR — NA — «NR»
- pct_dfs: NR — NA — «NR»
- pct_esports: NR — NA — «NR»
- sports_lottery: no — Page 5, Measures — «sports betting referred broadly to wagering on "sporting events" (e.g., football, cricket, soccer, basketball, and tennis)»
- mixed_race: no — Page 4-5, Measures — «Participants who engaged in both activities completed separate measures for sports betting and race betting»
- legal_status: NR — NA — «NR»
- n_invited: NR — Page 7, Procedure — «Of the 425 individuals who initiated the survey»
- n_responded: 188 — Page 7, Procedure — «The final analytic sample comprised 188 participants, including 185 young adults who reported regular sports betting»
- response_rate: NR — Page 7, Procedure — «Of the 425 individuals who initiated the survey, 303 completed the sports betting section»
- age_mean: 24.07 — Page 4, Participants; Table 1 — «185 participants met criteria for regular sports betting (85.4% male; Mage = 24.07, SD = 3.77)»
- age_sd: 3.77 — Page 4, Participants — «Mage = 24.07, SD = 3.77»
- age_min: 18 — Page 4, Participants — «mean age of 24.11 years (SD = 3.76, range: 18–30)»
- age_max: 30 — Page 4, Participants — «mean age of 24.11 years (SD = 3.76, range: 18–30)»
- age_group: adults — Page 4, Participants — «were young adults aged 18–30 years»
- pct_male: 85.41 — Page 5, Table 1 — «Male 158 (85.41)»
- mode: online — Page 7, Procedure — «Recruitment materials directed participants to an online Qualtrics survey, which took approximately 30 min to complete.»
- weights: no — Page 7, Statistical Analysis — «Descriptive statistics include means and standard deviations for continuous variables and counts and percentages for categorical variables»
- instruments: PGSI adapted for sports betting (English); also PGSI adapted for race betting (English, race sample only) — Page 6, Betting Problem Severity — «Betting problem severity was assessed using the PGSI (Ferris & Wynne, 2001), adapted to assess symptoms specific to sports and race betting.»
- instrument_validated_in_language: yes — Page 6, Betting Problem Severity — «Graupensperger and Calhoun (2024) demonstrated the validity of a sports betting adaptation of the PGSI with closely comparable item wording in a sample of youn…»
- industry_funding: no — Page 17, Funding; Conflict of Interest — «This project was funded by the Victorian Responsible Gambling Foundation, now part of the Department of Justice and Community Safety. ... None of the authors h…»
- funding_coi: Victorian Responsible Gambling Foundation (now part of Victorian Department of Justice and Community Safety); funder had no role; authors declare no COI; authors have had funding including via hypothecated taxes from gambling revenue — Page 17, Funding; Declarations — «all authors have received research and/or consultancy funding from multiple sources, including via hypothecated taxes from gambling revenue»
- pub_status: journal — Page 1, header — «ORIGINAL PAPER Journal of Gambling Studies https://doi.org/10.1007/s10899-026-10533-z»
- language: English — Full text — «A Cross-Sectional Examination of the Relationships Between Sports and Race Betting Motives, Expenditure, Problem Severity, and Harm in Young Australian Adults»
- notes: Age mean/SD and pct_male are for the 185 sports bettors; age range 18-30 is for the whole sample of 188. 124 of the 185 also bet regularly on racing; PGSI was sports-specific (separate race-specific PGSI). Recruitment channels included gambling help-seeking forums, but participants were not recruited for gambling problems, so the sample is eligible. Eligibility required regular online betting on sports OR racing, so whether all 185 bet on sports online is not certain (pct_online NR); smartphone app plus computer made up about 91% of sports betting volume on average. 425 started the survey; 11…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame was social media, online ads and betting/help-seeking forums, which covers only part of young Australian adults who bet regularly. — Page 7, Procedure — «via social media (e.g., Facebook, Instagram), online advertising platforms (e.g., Google Ads, Gumtree), and online forums related to sports and race betting an…»
2. способ отбора: **no** — Convenience and snowball sampling. — Page 7, Procedure — «Participants were recruited ... using convenience and snowball sampling»
3. размер выборки: **no** — 185 sports bettors, below 385. — Page 9, Table 2 — «Regular sports betting (n = 185)»
4. описание выборки и условий: **yes** — Age, sex, setting, country and recruitment dates are reported. — Page 4-5, Participants, Table 1; Page 7, Procedure — «185 participants met criteria for regular sports betting (85.4% male; Mage = 24.07, SD = 3.77)»
5. охват (пропуски): **yes** — No missing data for sports betting variables. — Page 7, Statistical Analysis — «There were no missing data for sports betting variables»
6. валидность определения случая: **yes** — Sports-adapted PGSI with unchanged 0-3 scoring and standard cut-offs; the adaptation has a cited validation. — Page 6, Betting Problem Severity — «Standard cut-offs were used to classify betting problem severity as non-problem (score of 0), low-risk (scores of 1–2), moderate-risk (scores of 3–7), and prob…»
7. единое надёжное измерение: **yes** — Same online instrument, time frame and threshold for everyone; alpha reported. — Page 6, Betting Problem Severity — «Internal consistency was high for both sports and race betting in this study (α = 0.91 and 0.94, respectively).»
8. статистика (числитель и знаменатель): **yes** — Counts and denominator (185) given in Table 2; CI can be calculated; no design that needs weights. — Page 9, Table 2 — «Problem betting, n (%) 60 (32.43)»
9. отклик: **no** — Open online recruitment with no denominator of invited people; no handling of non-response. — Page 7, Procedure — «Of the 425 individuals who initiated the survey, 303 completed the sports betting section»

Правки:
- 

Проверено: да

---

## ST005 · Heirene 2026 · Harm reduction journal

Основной отчёт R0714: [текст](../../fulltext/text/R0714.txt) — «Development of lower-risk guidelines for online sports and race betting in Australia using objective behavioural data.» — [DOI](https://doi.org/10.1186/s12954-026-01402-4)
Расхождения в тексте: Participant flow: 24,829 invited, 3,867 accessed, 1,959 completed up to the PGSI, 1,647 completed all PGSI items (the analysed sample), 1,470 answered every question, and 1,580 completed the GHM. Table 1 counts PGSI harm as 448 + 406 = 854 and no harm as 24 + 702 = 726, which add to 1,580. These are the GHM completers, which is why the table shows 854 rather than the 893 PGSI-harmed reported among all 1,647. Table 3 note: 592 people did not report income, leaving 1,055 (1,647 - 592 = 1,055, which matches). For the 18-25 subgroup, 87 GHM-harmed is printed as 41%. That does not fit a denominator of 239 (it would be 36.4%), so the GHM denominator for this group is unreported. The Discussion says GHM harm affected 'just under 30% of the unweighted sample' (472/1,580 = 29.9%) and PGSI harm 'slightly more than half' (893/1,647 = 54.2%). Both agree with the counts.
Заметка ИИ: One sample: online wagering customers of one operator (Entain) in Australia. The sample mixes sports and race betting, and no sports-only estimate is reported. The study does not report standard PGSI categories (0, 1-2, 3-7, 8+). Problem gambling is reported only as a modified 7-item PGSI harm index (items scored 0/1, harmed at 2 or more) and as GHM harm. Both are coded not_levelled, so for prevalence purposes this study fits only the ad hoc / evidence-map strand.

### ST005-1 · Customers of two Entain online wagering sites (sports and race betting), Australia, 2024, n=1,647
Отчёты: R0714 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | adhoc · PGSI 7-item harm index (items dichotomised 0/1, range 0-7) >=2 | **not_levelled** | **893 / 1647** | 54.2 | Results, Rates of harm | «Among the 1,647 people who completed the PGSI items, 893 met the criteria for experiencing harm (equivalent to 50% of the weighted sample).» |
| E2 | all | other · Gambling Harm Measure: any 'yes' at strain/pressure level (level 2) in any domain, or yes to the legal item | **not_levelled** | **472 / 1580** | 29.9 | Results, Rates of harm; Table 1 | «Among the 1,580 who completed all items of the GHM, 472 (25% of the weighted sample) met the criteria for experiencing harm.» |
| E3 | 18-25 | adhoc · PGSI 7-item harm index (items dichotomised 0/1, range 0-7) >=2 | **not_levelled** | **159 / 239** | 66.5 | Results, Exploratory analyses | «Harm rates were higher in this younger group of 239 participants, with 159 (67% [unweighted]) reporting PGSI harm and 87 (41%) reporting GHM harm.» |
| E4 | 18-25 | other · Gambling Harm Measure: any 'yes' at strain/pressure level in any domain, or yes to the legal item | **not_levelled** | **87 / NR** |  | Results, Exploratory analyses | «with 159 (67% [unweighted]) reporting PGSI harm and 87 (41%) reporting GHM harm.» |

- E1: cumulative: yes; источник порога: study's own; правило: adhoc row: 7 of 9 PGSI items with dichotomous scoring = PGSI-like scale with other scoring -> adhoc, not levelled; у авторов: «harmed (PGSI harm)»; главная у авторов: yes; период: past 12 months; взвешенная доля: 50; заметка: Mixed sports and race bettors. Threshold taken from prior lower-risk guideline studies [1, 20]. Weighted for oversampling of operator-flagged at-risk customers. Table 1 shows 854 PGSI-harmed among the 1,580 GHM completers.
- E2: cumulative: yes; источник порога: study's own; правило: GHM not in levels table (harm measure, not a problem-gambling screen) -> not levelled; у авторов: «harmed (GHM harm)»; главная у авторов: no; период: past 12 months; взвешенная доля: 25; заметка: Denominator = GHM completers (1,580), not all 1,647. Table 1: 448 + 24 = 472.
- E3: cumulative: yes; источник порога: study's own; правило: adhoc row: PGSI-like scale with non-standard scoring -> not levelled; у авторов: «PGSI harm»; главная у авторов: no; период: past 12 months; заметка: Exploratory, not preregistered; participants aged 25 or younger (described as 18-25). Unweighted percentage.
- E4: cumulative: yes; источник порога: study's own; правило: GHM not in levels table -> not levelled; у авторов: «GHM harm»; главная у авторов: no; период: past 12 months; заметка: Denominator unclear: 87/239 = 36.4%, but 41% printed; likely the number of young GHM completers (~212), not reported.

**⚠ Проверка скриптом (обратите внимание):**
- E2: n оценки не равно n_bettors выборки (1647): проверьте знаменатель
- E2: ни случаев, ни n нет в вашей строке «Где цифры» (этап полных текстов) — сверьте

**Ключевые поля выборки:**
- **n_bettors: 1647** — Results, Rates of harm — «Among the 1,647 people who completed the PGSI items, 893 met the criteria for experiencing harm»
- **sample_type: bettor_recruited** — Methods, Participants & recruitment — «Customers from two licensed online wagering platforms in Australia... were invited to participate in a survey about their gambling behaviour.»
- **sampling: operator_customers** — Methods, Participants & recruitment — «the operator flagged all eligible customers who had been classified as "at-risk"... Second, a random sample of "not-at-risk" customers was drawn at a 20:80 ratio»
- **betting_period: current** — Methods, Participants & recruitment — «To be eligible, customers needed to have placed at least one bet within the preceding six months, held an account for a minimum of 30 days»

**Остальные поля:**
- parent_population: NA — NA — «NA»
- min_frequency: none (at least one bet in the preceding six months) — Methods, Participants & recruitment — «customers needed to have placed at least one bet within the preceding six months»
- country: AUS — Methods, Participants & recruitment — «Customers from two licensed online wagering platforms in Australia, operated by the same international parent company»
- subnational: NA — Methods, Participants & recruitment — «two licensed online wagering platforms in Australia»
- data_years: 2023-2024 — Procedures; Strengths and limitations — «In January 2024, we received a dataset containing unique customer identification numbers... our study uses some of the most recently available data (2023–2024)»
- design: cross-sectional — Methods — «invited to take part in a survey including the Problem Gambling Severity Index (PGSI) and the Gambling Harm Measure (GHM). Survey responses were matched to cus…»
- gambling_disclosed: yes — Methods, Participants & recruitment — «were invited to participate in a survey about their gambling behaviour»
- betting_mode: online only — Methods, Participants & recruitment — «two licensed online wagering platforms in Australia»
- pct_online: all — Methods, Participants & recruitment — «Customers from two licensed online wagering platforms in Australia»
- pct_inplay: NR — NA — «NR»
- pct_dfs: NR — NA — «NR»
- pct_esports: NR — NA — «NR»
- sports_lottery: no — Behavioural indicators — «horseracing, greyhound racing, harness racing, basketball, and soccer being the five most common activities by total bets placed»
- mixed_race: yes — Behavioural indicators; Background — «lower-risk guidelines that are [1] specific to online sports and race betting in Australia... horseracing, greyhound racing, harness racing, basketball, and so…»
- legal_status: regulated legal market — Background; Participants & recruitment — «online sports and race betting in Australia (the only legal form of online gambling other than lottery in Australia)... two licensed online wagering platforms»
- n_invited: 24829 — Methods, Participants & recruitment — «Of the 24,829 individuals invited, 3,867 accessed the survey, 1,959 completed up to the PGSI, and 1,470 provided responses to all questions.»
- n_responded: 1647 — Results — «The 1,647 people who completed all PGSI items formed our initial sample for analyses.»
- response_rate: 6.6 — Methods, Participants & recruitment (computed) — «Of the 24,829 individuals invited, 3,867 accessed the survey, 1,959 completed up to the PGSI»
- age_mean: 44.1 — Results — «the mean age was 44.1 years (SD = 15.5)»
- age_sd: 15.5 — Results — «the mean age was 44.1 years (SD = 15.5)»
- age_min: 18 — H5 section (exploratory aim) — «we sought to identify lower-risk limits specific to young people aged 18 to 25 by isolating this group in our sample»
- age_max: NR — NA — «NR»
- age_group: adults — H5 section (exploratory aim) — «young people aged 18 to 25 by isolating this group in our sample»
- pct_male: 84.6 — Results; Footnote 4 — «Of this sample, 84.6% were male (1.6% were recorded as having an "unknown" gender by the operator)»
- mode: online — Procedures — «Unique invitation links were generated through Qualtrics, where the survey was hosted»
- weights: yes — Data analysis, Stage I — «Weighted percentages accounted for our oversampling of "at-risk" customers flagged by the operator's risk detection system by applying sample weights (adjusted…»
- instruments: PGSI (English; past 12 months; used as a 7-item dichotomised harm index); Gambling Harm Measure (GHM, 16 items, English) — Outcome variables — «we focused on the seven items relating to gambling harms within the PGSI... we used the Gambling Harm Measure [38], a 16-item scale»
- instrument_validated_in_language: NR — Outcome variables — «A score of 2 or more across these seven items was used to classify a participant as harmed, again consistent with prior research using this same index [1, 20].»
- industry_funding: yes — Funding — «This customer data analysed for this project was provided by the online wagering operator Entain, who also facilitated the collection of survey data... funded …»
- funding_coi: Data and survey facilitation by operator Entain; partly funded by ICRG (funded by Bally's Corporation); authors report multiple industry-funded projects (Entain, Sportsbet, Responsible Wagering Australia, etc.); funders stated to have no input. — Funding; Competing interests — «Entain, ICRG, and Bally's Corporation did not have any input into the research question(s), design, data analysis, or interpretation of findings of this study.»
- pub_status: journal — Header — «Harm reduction journal; DOI: 10.1186/s12954-026-01402-4»
- language: English — Full text — «Development of lower-risk guidelines for online sports and race betting in Australia using objective behavioural data»
- notes: Sample is online sports AND race bettors (wagering customers), not sports bettors alone; horse/greyhound/harness racing are among the most common activities; no sports-only estimate. All 4,829 operator-flagged at-risk customers plus a random 20,000 not-at-risk customers were invited (oversampling; weighted estimates). 3,867 accessed, 1,959 completed up to the PGSI, 1,647 completed all PGSI items, 1,470 completed all questions. n_responded is set to the 1,647 PGSI completers; response rate 1,647/24,829 = 6.6% (15.6% accessed). Age and sex are of the analysed sample (n=1,647), weighted (footnot…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame is the customers of two sites of one operator, only part of Australian online sports/race bettors that the guidelines target. — Methods, Participants & recruitment — «Customers from two licensed online wagering platforms in Australia, operated by the same international parent company»
2. способ отбора: **yes** — Census of at-risk flagged customers plus random sample of not-at-risk customers from the operator's eligible customer list (stratified probability invitation; weighted). — Methods, Participants & recruitment — «the operator flagged all eligible customers who had been classified as "at-risk"... Second, a random sample of "not-at-risk" customers was drawn»
3. размер выборки: **yes** — 1,647 bettors analysed (>=385). — Results — «The 1,647 people who completed all PGSI items formed our initial sample for analyses.»
4. описание выборки и условий: **yes** — Age, sex, setting (two online operators), country and dates reported. — Results; Procedures — «84.6% were male... the mean age was 44.1 years (SD = 15.5)... In January 2024, we received a dataset»
5. охват (пропуски): **no** — Of 1,959 who reached the PGSI, 312 (15.9%) did not complete all items and were excluded without handling; GHM available for 1,580. — Participants & recruitment; Results — «1,959 completed up to the PGSI... The 1,647 people who completed all PGSI items formed our initial sample»
6. валидность определения случая: **no** — Primary outcome is a study-modified 7-item PGSI harm index with dichotomised items and a >=2 cut-off, not the standard PGSI scoring/threshold. — Outcome variables — «participants were assigned a score of 0 (representing a response of "Never") or 1... A score of 2 or more across these seven items was used to classify a parti…»
7. единое надёжное измерение: **unclear** — Same online survey, time frame and threshold for all, but no reliability of the harm index reported in this sample. — Outcome variables — «Items in our survey focused on experiences over the past 12 months.»
8. статистика (числитель и знаменатель): **yes** — Unweighted counts and denominators given, weighted percentages for oversampling; CI calculable. — Results, Rates of harm — «Among the 1,647 people who completed the PGSI items, 893 met the criteria for experiencing harm (equivalent to 50% of the weighted sample).»
9. отклик: **yes** — Response very low (~6.6%) but responders compared with non-responders using account data and weights adjusted for response rates. — Participants & recruitment; Data analysis Stage I — «Compared to non-responders, survey responders bet more frequently over the past six months (Cohen's d = 0.58), had placed a bet more recently (d = − 0.51), wer…»

Правки:
- # E2 n=1580 completers of GHM, as published in Table 1

Проверено: да

---

## ST006 · McGrane 2026 · Addictive behaviors reports

Основной отчёт R0907: [текст](../../fulltext/text/R0907.txt) — «The effect of television advertising on gambling behaviour: a quasi-experimental study during the 2022 Qatar FIFA World Cup.» — [DOI](https://doi.org/10.1016/j.abrep.2026.100666)
Расхождения в тексте: Table 2 PGSI counts (95+128+103+39) sum to 365, which matches the final analysed sample. The 396 baseline completers include 31 people without complete daily data, and their PGSI is not reported. One conflict: the inclusion criterion 'no history of personal gambling problems' and the Limitations text on excluding 'possible gambling disorder' do not fit with 39 participants (11%) scoring PGSI 8+. The paper does not say whether the PGSI time frame is past 12 months.
Заметка ИИ: Main report R0907 is a quasi-experiment on TV gambling advertising. The PGSI baseline distribution is a descriptive characteristic of the sample, not a prevalence aim, so no estimate is marked as primary for the authors. Language validation of the PGSI is not cited; the instrument is the original English version.

### ST006-1 · Prolific panel male football bettors aged 18-45, England, Nov-Dec 2022 (World Cup quasi-experiment), n=365
Отчёты: R0907 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | PGSI · PGSI 0 | **below** | **95 / 365** | 26.0 | Table 2 | «Gambling Risk Level ... No risk / 95 / 26 %» |
| E2 | all | PGSI · PGSI 1-2 | **L1** | **128 / 365** | 35.1 | Table 2 | «Lower Risk / 128 / 35 %» |
| E3 | all | PGSI · PGSI 3-7 | **L2** | **103 / 365** | 28.2 | Table 2 | «Medium Risk / 103 / 28 %» |
| E4 | all | PGSI · PGSI>=8 | **L3** | **39 / 365** | 10.7 | Table 2 and note | «Higher Risk / 39 / 11 % ... 8+ "higher-risk" (or 'problem' gambler)» |

- E1: cumulative: no; источник порога: standard; правило: PGSI row; 0 is below L1; у авторов: «no risk»; главная у авторов: no; период: NR; заметка: Denominator = 365 analysed (sum 95+128+103+39). Prevalence is not the study's aim.
- E2: cumulative: no; источник порога: standard; правило: PGSI row; 1-2 band starts at L1; у авторов: «low-risk»; главная у авторов: no; период: NR
- E3: cumulative: no; источник порога: standard; правило: PGSI row; 3-7 band starts at L2; у авторов: «medium-risk»; главная у авторов: no; период: NR
- E4: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ is L3; у авторов: «higher-risk (or 'problem' gambler)»; главная у авторов: no; период: NR; заметка: Sample excluded people with a history of personal gambling problems, and the 400 most frequent bettors were selected on purpose, so this is not a population prevalence.

**Ключевые поля выборки:**
- **n_bettors: 365** — Results, Recruitment; Table 2 — «A total of 92 % of participants provided complete data, resulting in a final sample of 365»
- **sample_type: bettor_recruited** — Methods, Participants; Recruitment — «Gambling: regular football gamblers (at least once in the last 12 months)... Participants were recruited via Prolific»
- **sampling: convenience** — Methods, Sampling; Recruitment — «This study uses purposive sampling... the 400 individuals with the highest football gambling frequency were purposively selected»
- **betting_period: past 12 months** — Methods, Participants — «regular football gamblers (at least once in the last 12 months)»

**Остальные поля:**
- parent_population: NA — NA
- min_frequency: at least once in past 12 months on football; then the 400 with the highest football gambling frequency selected — Methods, Participants; Recruitment — «the 400 individuals with the highest football gambling frequency were purposively selected»
- country: GBR — Methods, Participants — «Location: England»
- subnational: England — Methods, Participants — «Location: England»
- data_years: 2022 — Methods, Recruitment; Surveys — «On 14th November 2022, an invitation was sent to 1,000 potential participants... On 17th November 2022, participants completed a baseline survey»
- design: experiment baseline — Methods, Surveys — «On 17th November 2022, participants completed a baseline survey on demographics and gambling behaviour. From 21st November to 3rd December, they completed dail…»
- gambling_disclosed: NR — Methods, Surveys — «Participants remained anonymised and were blinded to the study's true purpose throughout.»
- betting_mode: NR — Methods, Participants — «Gambling: regular football gamblers (at least once in the last 12 months)»
- pct_online: NR — Table 2 — «Online betting on another sport/event | 359 | 98 %»
- pct_inplay: NR — NA
- pct_dfs: NR — NA
- pct_esports: NR — NA
- sports_lottery: unclear — Table 2 — «Football Pools | 51 | 14 %»
- mixed_race: no — Methods, Participants — «regular football gamblers»
- legal_status: regulated legal market — Methods, The quasi-experimental setup — «Advertisements for sports betting products are permitted around live sports broadcasts in the UK only within the pre- and post-match section»
- n_invited: 1000 — Methods, Recruitment — «On 14th November 2022, an invitation was sent to 1,000 potential participants.»
- n_responded: 396 — Results, Recruitment — «In total, 396 participants provided consent and completed the baseline survey before the study commenced.»
- response_rate: NR — Results, Recruitment — «The 400 participants with the highest football gambling frequency were invited to the study. In total, 396 participants provided consent and completed the base…»
- age_mean: 33 — Table 1 — «Age | | 33 (7) | [18, 45]»
- age_sd: 7 — Table 1 — «Age | | 33 (7) | [18, 45]»
- age_min: 18 — Table 1 — «Age | | 33 (7) | [18, 45]»
- age_max: 45 — Table 1 — «Age | | 33 (7) | [18, 45]»
- age_group: adults — Methods, Participants — «Age: 18 to 45»
- pct_male: 100 — Methods, Participants — «Sex: males»
- mode: online — Methods, Recruitment — «Participants were recruited via Prolific and completed surveys in Qualtrics.»
- weights: NR — NA
- instruments: PGSI (English) — Table 2 note — «Gambling risk level measured using the Problem Gambling Severity Index (PGSI): 0 "no risk" 1–2 "low-risk" 3–7 "medium-risk" 8+ "higher-risk" (or 'problem' gamb…»
- instrument_validated_in_language: NR — Table 2 note — «Problem Gambling Severity Index (PGSI)»
- industry_funding: no — Funding — «This work was funded by a Wellcome Trust grant [224852/Z/21/Z].»
- funding_coi: Wellcome Trust; one author (MF) received grants from MRC and the Academic Forum for the Study of Gambling — Funding; Declaration of competing interest — «MF has received grants from the Medical Research Council and the Academic Forum for the Study of Gambling within the past 36 months.»
- pub_status: journal — Header — «Addictive behaviors reports; DOI: 10.1016/j.abrep.2026.100666»
- language: English — Full text — «The effect of television advertising on gambling behaviour: a quasi-experimental study during the 2022 Qatar FIFA World Cup»
- notes: Quasi-experiment, not a prevalence study; the baseline PGSI distribution is extracted. 1,000 Prolific members were invited to screening (number who answered not reported). The 400 with the highest football betting frequency were selected, so higher-risk bettors are over-represented. 396 completed baseline; the 365 with complete data across all surveys form the analysed sample, and Table 2 PGSI counts sum to 365. The eligibility criterion 'no history of personal gambling problems' (Limitations: people with 'possible gambling disorder' excluded) conflicts with 39 (11%) scoring PGSI 8+, so preva…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame is Prolific online panel members, covering only part of male football bettors in England. — Methods, Recruitment — «Participants were recruited via Prolific and completed surveys in Qualtrics.»
2. способ отбора: **no** — Purposive selection of the 400 most frequent bettors from a non-probability panel. — Methods, Sampling; Recruitment — «the 400 individuals with the highest football gambling frequency were purposively selected»
3. размер выборки: **no** — 365 sports bettors, below 385. — Results, Recruitment — «resulting in a final sample of 365»
4. описание выборки и условий: **yes** — Age, sex, setting (Prolific online), country/region and dates reported. — Methods, Participants; Surveys; Table 1 — «Sex: males Age: 18 to 45 ... Location: England»
5. охват (пропуски): **yes** — 365 of 396 baseline completers analysed (31 excluded, 7.8%, under 10%). — Results, Recruitment — «A total of 92 % of participants provided complete data, resulting in a final sample of 365»
6. валидность определения случая: **yes** — PGSI with standard thresholds, original English version. — Table 2 note — «PGSI: 0 "no risk" 1–2 "low-risk" 3–7 "medium-risk" 8+ "higher-risk" (or 'problem' gambler)»
7. единое надёжное измерение: **unclear** — Same instrument and online mode for all; reliability not reported. — Methods, Surveys — «participants completed a baseline survey on demographics and gambling behaviour»
8. статистика (числитель и знаменатель): **yes** — Counts and denominator (365) given; CI calculable; no weights needed for this design. — Table 2 — «No risk | 95 | 26 % ... Higher Risk | 39 | 11 %»
9. отклик: **unclear** — Number answering the 1,000 screening invitations not reported; 396 of 400 selected completed baseline. — Methods, Recruitment; Results, Recruitment — «an invitation was sent to 1,000 potential participants... 396 participants provided consent and completed the baseline survey»

Правки:
- 

Проверено: да

---

## ST007 · Rockloff 2026 · Addiction (Abingdon, England)

Основной отчёт R1094: [текст](../../fulltext/text/R1094.txt) — «Direct gambling marketing, direct harm: A randomised experiment.» — [DOI](https://doi.org/10.1111/add.70369)
Не выписано ИИ: Not extracted: the full baseline EMA survey of Hing et al. [ref 14] (n=1015 completed of 1189 started). This report gives no PGSI prevalence for it, and it is a separate report. No treatment, helpline or self-exclusion samples are present.
Расхождения в тексте: 1. Table 1, treatment arm, PGSI 'No problem' is printed as 25 (26.8%), but 25/96 = 26.0%, and the treatment-arm PGSI percentages add to 100.7%. The counts were used. 2. Summed counts 58+51+64+54 = 227 match the n analysed, and 118/227 = 52.0% matches the abstract. 3. The age t-test is reported as t(208), although n = 227. 4. The Limitations say 'attrition was very low', yet 173 of the 400 enrolled were excluded after randomisation (151 for no opt-out proof, 22 for no EMA).
Заметка ИИ: This is one sample: sports and race bettors combined, so mixed_race = yes. PGSI categories are pooled across the two randomised arms at baseline. The randomised arms were not extracted as subgroups. The report gives no breakdowns by sex, age or betting mode.

### ST007-1 · Australian regular sports and race bettors, Qualtrics online panels, direct-marketing opt-out experiment, 2023 (n=227)
Отчёты: R1094 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | PGSI · PGSI 0 | **below** | **58 / 227** | 25.6 | Table 1 | «PGSI, n (%) / No problem / 33 (25.2) / 25 (26.8)» |
| E2 | all | PGSI · PGSI 1-2 | **L1** | **51 / 227** | 22.5 | Table 1 | «Low risk / 27 (20.6) / 24 (25.0)» |
| E3 | all | PGSI · PGSI 3-7 | **L2** | **64 / 227** | 28.2 | Table 1 | «Moderate risk / 39 (29.8) / 25 (26.0)» |
| E4 | all | PGSI · PGSI>=8 | **L3** | **54 / 227** | 23.8 | Table 1 | «Problem / 32 (24.4) / 22 (22.9)» |
| E5 | all | PGSI · PGSI>=3 | **L2** | **118 / 227** | 52.0 | Abstract; Table 1 | «52.0% of whom scored in the moderate‐risk or problem range on the Problem Gambling Severity Index (PGSI)» |
| E6 | all | PGSI · PGSI 0-2 | **below** | **109 / 227** | 48.0 | Table 1 | «No problem or low risk / 60 (45.8) / 49 (51.0)» |

- E1: cumulative: no; источник порога: standard; правило: PGSI row; score 0 is below L1; у авторов: «No problem»; главная у авторов: no; период: NR; **расчёт: 33 control + 25 treatment = 58; n = 131 + 96 = 227**; заметка: Treatment-arm percentage printed as 26.8 although 25/96 = 26.0%. Sports or race bettors combined.
- E2: cumulative: no; источник порога: standard; правило: PGSI row; 1-2 band starts at L1; у авторов: «Low risk»; главная у авторов: no; период: NR; **расчёт: 27 + 24 = 51; n = 131 + 96 = 227**; заметка: Sports or race bettors combined.
- E3: cumulative: no; источник порога: standard; правило: PGSI row; 3-7 band starts at L2; у авторов: «Moderate risk»; главная у авторов: no; период: NR; **расчёт: 39 + 25 = 64; n = 131 + 96 = 227**; заметка: Sports or race bettors combined.
- E4: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ starts at L3; у авторов: «Problem»; главная у авторов: no; период: NR; **расчёт: 32 + 22 = 54; n = 131 + 96 = 227**; заметка: Sports or race bettors combined.
- E5: cumulative: yes; источник порога: standard; правило: PGSI row; >=3 starts at L2; у авторов: «moderate-risk or problem range»; главная у авторов: yes; период: NR; **расчёт: 71 + 47 = 118; 118/227 = 52.0%, matching the abstract**; заметка: Cumulative category reported by the study. Sports or race bettors combined.
- E6: cumulative: no; источник порога: standard; правило: PGSI row; band 0-2 lower bound 0 is below L1; у авторов: «No problem or low risk»; главная у авторов: no; период: NR; **расчёт: 60 + 49 = 109; n = 131 + 96 = 227**; заметка: Combined closed band reported by the study; it duplicates PGSI 0 + PGSI 1-2.

**⚠ Проверка скриптом (обратите внимание):**
- all: категории (E1+E2+E3+E6+E4) дают 336, а n = 227

**Ключевые поля выборки:**
- **n_bettors: 227** — Table 1; Methods, Participants — «Ultimately, 140 male and 87 female participants complied with the instructions and completed one or more EMA survey(s).»
- **sample_type: bettor_recruited** — Methods, Participants — «recruited via Qualtrics, a panel aggregator using independent market research panels. Participants were eligible if they: ... (iv) reported typically betting on sports or races at least once fortnightly in the past 12 months»
- **sampling: convenience** — Methods, Participants — «recruited via Qualtrics, a panel aggregator using independent market research panels»
- **betting_period: past 12 months** — Methods, Participants — «(iii) had an active online wagering account used within the previous 12 months; (iv) reported typically betting on sports or races at least once fortnightly in the past 12 months»

**Остальные поля:**
- parent_population: NA — Methods, Participants — «The current experiment drew on a subset of participants who had previously completed a baseline survey»
- min_frequency: at least once fortnightly (sports or races) — Methods, Participants — «reported typically betting on sports or races at least once fortnightly in the past 12 months»
- country: AUS — Abstract, Setting — «SettingNationwide, Australia (July–August 2023).»
- subnational: NA — Methods, Participants — «Australian residents from all states and territories were recruited via Qualtrics»
- data_years: 2023 — Methods, Procedure — «All survey results were collected between Tuesday 18 July and Tuesday 29 August 2023.»
- design: experiment baseline — Abstract, Design — «Stratified randomised field experiment with a between‐participants design, embedded in a 14‐day ecological momentary assessment (EMA).»
- gambling_disclosed: yes — Discussion, Limitations — «People who took part in the study were necessarily aware that we were asking about their betting»
- betting_mode: NR — Methods, Participants — «had an active online wagering account used within the previous 12 months»
- pct_online: all — Methods, Participants — «had an active online wagering account used within the previous 12 months»
- pct_inplay: NR — NR — «NR»
- pct_dfs: NR — NR — «NR»
- pct_esports: NR — NR — «NR»
- sports_lottery: no — Methods, Participants — «reported typically betting on sports or races»
- mixed_race: yes — Abstract, Participants — «were regular Australian sports and race bettors recruited from online panels»
- legal_status: NR — NR — «NR»
- n_invited: 615 — Methods, Participants — «A total of 615 participants were invited to take part in the experiment, and 405 (65.9%) opted to do so»
- n_responded: 405 — Methods, Participants — «A total of 615 participants were invited to take part in the experiment, and 405 (65.9%) opted to do so»
- response_rate: 65.9 — Methods, Participants — «615 participants were invited to take part in the experiment, and 405 (65.9%) opted to do so»
- age_mean: 45 — Abstract, Participants — «Participants (n = 227; 61.7% men; mean age = 45)»
- age_sd: NR — Table 1 — «Age, years, mean (SD) | | 45.2 (15.4) | 45.6 (15.0)»
- age_min: 18 — Methods, Participants — «(i) were aged 18 years or older»
- age_max: NR — NR — «NR»
- age_group: adults — Methods, Participants — «(i) were aged 18 years or older»
- pct_male: 61.7 — Abstract; Table 1 — «Participants (n = 227; 61.7% men; mean age = 45)»
- mode: online — Methods, Procedure — «The survey links were delivered via email at 4 PM»
- weights: no — Methods, Analytic approach — «Baseline characteristics for the treatment and control groups were compared descriptively (means and proportions)»
- instruments: PGSI (English); adapted 10-item Short Gambling Harm Screen (SGHS, 48-hour version; harm measure, not a problem-gambling screen) — Methods, Procedure; Short-term betting harms — «The baseline survey that preceded the EMAs included questions on gambling behaviour, demographics and PGSI»
- instrument_validated_in_language: yes — Table 1; Levels table — «PGSI, n (%) | No problem ... | Low risk ... | Moderate risk ... | Problem»
- industry_funding: NR — Methods; Declaration of interests — «De‐identified data will be made available upon reasonable request, subject to approval by Gambling Research Australia»
- funding_coi: No funding statement in the text supplied; data access is subject to Gambling Research Australia approval (government body). All authors declare no conflicts of interest; they report government and public-agency gambling research funding. — Methods; Declaration of interests — «He declares no conflicts of interest in relation to this article.»
- pub_status: journal — Header — «venue: Addiction (Abingdon, England); DOI: 10.1111/add.70369»
- language: English — Full text — «Direct gambling marketing, direct harm: A randomised experiment»
- notes: Sample is sports OR race bettors combined (mixed_race = yes); no separate sports-only estimate. It overlaps with the baseline EMA survey of Hing et al. [ref 14] (n=1015 completed of 1189 started; 58.8% men), and the 227 are a subset of that sample. Selection: 615 invited to the experiment, 405 agreed, 400 enrolled, 151 excluded (allocated to treatment but gave no opt-out proof), 22 completed no EMA, leaving 227 analysed (control 131, treatment 96). Only people willing to opt out of direct marketing were eligible. Age mean 45 is for the whole analysed sample (abstract); arm SDs are 15.4 and 15…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame is members of market-research online panels, which cover only part of Australian regular sports/race bettors. — Methods, Participants — «recruited via Qualtrics, a panel aggregator using independent market research panels»
2. способ отбора: **no** — Opt-in online panel, further restricted to people willing to opt out of marketing and to those who complied. — Methods, Participants — «(vii) indicated a willingness to opt out of direct marketing from their wagering operator(s) for the duration of the study»
3. размер выборки: **no** — n = 227, below 385. — Abstract — «Participants (n = 227; 61.7% men; mean age = 45)»
4. описание выборки и условий: **yes** — Age, sex, setting, country and dates are reported. — Abstract; Table 1; Procedure — «Nationwide, Australia (July–August 2023). Participants (n = 227; 61.7% men; mean age = 45)»
5. охват (пропуски): **no** — 173 of the 400 enrolled (43%) were excluded after randomisation (151 for no opt-out proof, 22 for no EMA); this was not handled for prevalence. — Methods, Design — «excluded from the study because they did not provide the required proof of having opted out ... (n = 151) or did not take part in any of the EMA surveys (n = 2…»
6. валидность определения случая: **yes** — PGSI (English) with standard categories no problem/low/moderate/problem. — Table 1 — «PGSI, n (%) | No problem | ... | Low risk | ... | Moderate risk | ... | Problem»
7. единое надёжное измерение: **unclear** — Same online baseline PGSI for all, but no PGSI reliability is reported and the time frame is not stated. — Methods, Procedure — «The baseline survey that preceded the EMAs included questions on gambling behaviour, demographics and PGSI»
8. статистика (числитель и знаменатель): **yes** — Counts by category and arm sum to 227, so CI can be calculated. Unweighted, which suits a non-probability sample. — Table 1 — «Moderate risk or problem | 71 (54.2) | 47 (49.0)»
9. отклик: **no** — Baseline panel has no denominator of invited people. 65.9% agreed to the experiment, but only 227 of the 400 enrolled were analysed, without non-response handling. — Methods, Participants — «A total of 615 participants were invited to take part in the experiment, and 405 (65.9%) opted to do so»

Правки:
- E6 удалить # PGSI 0-2 (109) duplicates E1 (58) + E2 (51)

Проверено: да

---

## ST008 · Szaszi 2026 · PsyArXiv

Основной отчёт R1200: [текст](../../fulltext/text/R1200.txt) · [PDF](../../fulltext/pdf/R1200.pdf) — «The impact of cash out availability on online betting behavior» — [DOI](https://doi.org/10.31234/osf.io/rkb7a_v1)
Расхождения в тексте: The PGSI categories in Table 1 add up to 595 (78+155+230+132). Methods give 474 participants who placed bets (80%), but the Discussion gives 'N= 471'. This concerns the betting task only, not the prevalence estimates. Methods say 'half' were assigned to each condition, but the arms are 348 and 247. Exclusion counts overlap, so they do not add up to the 531 excluded.
Заметка ИИ: This is an experimental Registered Report, not a prevalence study. The PGSI distribution comes from baseline characteristics (Table 1) after exclusions that were not related to gambling problems. Industry funding is coded yes because the operator Vegas.hu paid participant compensation and recruited the participants.

### ST008-1 · Vegas.hu online sports bettors, Hungary, 2026, cash-out experiment (n=595)
Отчёты: R1200 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | PGSI · PGSI 0 | **below** | **78 / 595** | 13.1 | Table 1, page 17 | «Problem Gambling Severity Category Non-problem 78 (13%)» |
| E2 | all | PGSI · PGSI 1-2 | **L1** | **155 / 595** | 26.1 | Table 1, page 17 | «Low risk 155 (26%)» |
| E3 | all | PGSI · PGSI 3-7 | **L2** | **230 / 595** | 38.7 | Table 1, page 17 | «Moderate risk 230 (39%)» |
| E4 | all | PGSI · PGSI>=8 | **L3** | **132 / 595** | 22.2 | Table 1, page 17 | «Problem Gambler 132 (22%)» |

- E1: cumulative: no; источник порога: standard; правило: PGSI row; score 0 is below L1; у авторов: «Non-problem»; главная у авторов: no; период: past 12 months; заметка: Score bands are not stated explicitly; the text says categories follow the PGSI scoring guide. This is an experiment, so no estimate is presented as the main prevalence estimate.
- E2: cumulative: no; источник порога: standard; правило: PGSI row; 1-2 band starts at L1; у авторов: «Low risk»; главная у авторов: no; период: past 12 months
- E3: cumulative: no; источник порога: standard; правило: PGSI row; 3-7 band starts at L2; у авторов: «Moderate risk»; главная у авторов: no; период: past 12 months
- E4: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ = L3; у авторов: «Problem Gambler»; главная у авторов: no; период: past 12 months; заметка: Mean PGSI 4.74 (SD 4.56).

**Ключевые поля выборки:**
- **n_bettors: 595** — Page 17; Table 1 — «the final analytic sample consisted of 595 participants»
- **sample_type: bettor_recruited** — Page 16, Sampling — «participants were recruited via the mailing list of the Hungarian online gambling service provider, Vegas.hu. Individuals who met the criteria of being at least 18 years old, residing in Hungary, and having prior experience in sports betting were eligible»
- **sampling: operator_customers** — Page 16, Sampling — «Vegas.hu sent out recruitment emails in chunks to the participants»
- **betting_period: lifetime** — Page 16, Sampling — «having prior experience in sports betting were eligible to participate»

**Остальные поля:**
- parent_population: NA — Page 16, Sampling — «recruited via the mailing list of the Hungarian online gambling service provider, Vegas.hu»
- min_frequency: none — Page 16, Sampling — «having prior experience in sports betting were eligible to participate»
- country: HUN — Page 16, Sampling — «Individuals who met the criteria of being at least 18 years old, residing in Hungary, and having prior experience in sports betting were eligible to participat…»
- subnational: NA — Page 16, Sampling — «residing in Hungary»
- data_years: 2026 — Page 16, Sampling — «data collection took place from 19 January 2026 to 28 January 2026»
- design: experiment baseline — Page 6, Design and procedure — «The study was designed as an online experiment to delineate the effect of the perceived availability of the cash-out option on online gambling behavior.»
- gambling_disclosed: yes — Page 2, Abstract — «Hungarian residents with an online gambling history (N=595) were informed that they would have the chance to gamble with real money on sports events.»
- betting_mode: online only — Page 32, Discussion — «While recruiting active online sports bettors was a strength for ecological relevance»
- pct_online: all — Page 2, Abstract; Page 32 — «Hungarian residents with an online gambling history (N=595)»
- pct_inplay: NR — Table 1, page 18 — «Had Prior Cash-Out Experience 575 (97%)»
- pct_dfs: NR — NA
- pct_esports: NR — NA
- sports_lottery: unclear — NA
- mixed_race: no — Page 16, Sampling — «having prior experience in sports betting»
- legal_status: NR — Page 34, Competing interest statement — «Supervisory Authority for Regulatory Affairs (SARA), which is the regulatory body of gambling in Hungary»
- n_invited: NR — Page 16, Sampling — «Vegas.hu sent out recruitment emails in chunks to the participants»
- n_responded: 1126 — Page 16, Sampling — «A total of 1,126 participants were recruited for the study.»
- response_rate: NR — Page 16, Sampling — «A total of 1,126 participants were recruited for the study.»
- age_mean: 37.86 — Table 1, page 18 — «Age 37.86 (11.15)»
- age_sd: 11.15 — Table 1, page 18 — «Age 37.86 (11.15)»
- age_min: 18 — Page 16, Sampling — «at least 18 years old»
- age_max: NR — NA
- age_group: adults — Page 16, Sampling — «at least 18 years old»
- pct_male: 92 — Table 1, page 18 — «Man 546 (92%) ... Woman 47 (7.9%) ... No Answer 2 (0.3%)»
- mode: online — Page 6, Design and procedure — «Participants completed the study online.»
- weights: no — Table 1; Methods — «The sample comprises the final analytic sample (N = 595) after applying all exclusion criteria»
- instruments: PGSI, Hungarian version (PGSI-HU; Gyollai et al., 2013) — Page 12, Self-report measures — «The nine-item Problem Gambling Severity Index (Ferris & Wynne, 2001; Hungarian version: Gyollai et al., 2013) was used to assess problem gambling.»
- instrument_validated_in_language: yes — Page 12; References p. 37 — «Gyollai, Á., ... (2013). A Szerencsejáték Súlyossága Kérdőív magyar változatának (PGSI-HU) bemutatása. Psychiatria Hungarica [Presentation of the Hungarian ver…»
- industry_funding: yes — Page 34, Competing interest statement — «The compensation of the participants is covered by Vegas.hu. Vegas.hu had no role in study design, analysis, decision to on the conclusions, and the preparatio…»
- funding_coi: Funded by SARA (Hungarian gambling regulator); participant compensation paid by operator Vegas.hu (also recruiter); authors report consultancy/funding from gambling operators (MDG, ZD; ELTE helpline funded by Szerencsejáték Ltd.), stated unrelated to this study. — Pages 34-35, Competing interest statement; Acknowledgements — «We would like to thank the Supervisory Authority for Regulatory Affairs for the financial support.»
- pub_status: preprint — Header (venue: PsyArXiv) — «Year: 2026; venue: PsyArXiv; DOI: 10.31234/osf.io/rkb7a_v1»
- language: English — Full text — «The impact of cash-out availability on online betting behavior»
- notes: Registered Report experiment among customers of one Hungarian online operator (Vegas.hu). Age, sex and PGSI describe the final analytic sample (n=595) after heavy exclusions from 1,126 recruited: attention check, CAPTCHA performance (n=221), failure to understand cash-out (n=155), incomplete responses (n=35), invariant responding and speeders. These exclusions could bias prevalence. Missing PGSI values were imputed (kNN, k=3); the number imputed is not reported. The text does not give the legal status of sports betting in Hungary. pct_male 92% = 546/595 (Table 1). Discussion reports 471 betto…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame is the mailing list of one online operator; does not cover Hungarian sports bettors generally. — Page 16, Sampling — «participants were recruited via the mailing list of the Hungarian online gambling service provider, Vegas.hu»
2. способ отбора: **no** — Volunteer opt-in response to recruitment emails, followed by extensive exclusions. — Page 16, Sampling — «Vegas.hu sent out recruitment emails in chunks to the participants»
3. размер выборки: **yes** — 595 sports bettors >= 385. — Page 17 — «the final analytic sample consisted of 595 participants»
4. описание выборки и условий: **yes** — Age, sex, setting, country and dates reported. — Page 16; Table 1 — «data collection took place from 19 January 2026 to 28 January 2026»
5. охват (пропуски): **yes** — Missing PGSI values handled by kNN imputation (proportion missing not reported). — Page 20, Treatment of missing values — «Imputation was performed only for age, impulsiveness, PGSI, poverty index, and numeracy.»
6. валидность определения случая: **yes** — PGSI with standard categories, in a published Hungarian validation. — Page 12 — «Participants were categorized into four categories (i.e., no-risk, low-risk, moderate-risk, and problem gambler) according to the scoring guide of the PGSI»
7. единое надёжное измерение: **yes** — Same online PGSI-HU for all; reliability reported in sample. — Page 19, Results of reliability — «The PGSI‑HU demonstrated excellent reliability (α = .90, ω = .90).»
8. статистика (числитель и знаменатель): **yes** — Counts and denominator given in Table 1; CI calculable; no weighting needed for a customer sample. — Table 1, page 17 — «Problem Gambler 132 (22%)»
9. отклик: **no** — Number of invited customers not reported; no comparison of responders and non-responders. — Page 16, Sampling — «A total of 1,126 participants were recruited for the study.»

Правки:
- 

Проверено: да

---

## ST009 · Torrance 2026 · Journal of gambling studies

Основной отчёт R1215: [текст](../../fulltext/text/R1215.txt) · [PDF](../../fulltext/pdf/R1215.pdf) — «(Mis)Comprehension and (Mistaken) Attractiveness of Financial Gambling Inducements among UK Bettors.» — [DOI](https://doi.org/10.1007/s10899-026-10491-6)
Расхождения в тексте: Table 1 gives the total mean age as 42.2 (SD 12.1), but the two arm means are 42 and 41.8. A pooled mean cannot be higher than both arm means, so one of these values is wrong. PGSI counts sum to 585 (275+141+108+61) and the percentages sum to 100. Sex counts sum to 585. Control-condition comprehension counts are consistent (269+16+6=291). The text calls the median estimate of £500 'exactly two-thirds below' the correct value (p.8) and 'one-third below' (p.12); £500 is one-third below £750.
Заметка ИИ: This study has no sports-bettor-specific problem-gambling estimate. The sample is past-year UK gamblers recruited on Prolific: 70.8% bet on sports online and 17.6% in person, and the overlap is not reported. The PGSI distribution is given only for all 585 participants. Those whole-sample estimates are included with clear labels so the reviewer can decide eligibility. They should probably not enter the sports-bettor meta-analysis unless sports-bettor data (e.g., OSF data) are obtained.

### ST009-1 · Prolific UK past-year gamblers (not lottery-only), online experiment, GBR, 2025 (n=585; sports bettors not separated)
Отчёты: R1215 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all participants (past-year gamblers, NOT sports bettors only) | PGSI · PGSI 0 | **below** | **275 / 585** | 47.0 | Page 6, Gambling Severity | «275 participants (47.0%) were classified as no-risk» |
| E2 | all participants (past-year gamblers, NOT sports bettors only) | PGSI · PGSI 1-2 | **L1** | **141 / 585** | 24.1 | Page 6, Gambling Severity | «141 (24.1%) as low-risk» |
| E3 | all participants (past-year gamblers, NOT sports bettors only) | PGSI · PGSI 3-7 | **L2** | **108 / 585** | 18.5 | Page 6, Gambling Severity | «108 (18.5%) as moderate-risk» |
| E4 | all participants (past-year gamblers, NOT sports bettors only) | PGSI · PGSI>=8 | **L3** | **61 / 585** | 10.4 | Page 6, Gambling Severity and footnote 1 | «61 (10.4%) as high-risk bettors» |

- E1: cumulative: no; источник порога: standard; правило: PGSI row; 0 = below L1; у авторов: «no-risk»; главная у авторов: no; период: NR; заметка: Whole gambler sample, not restricted to sports bettors; cut-offs not stated, standard PGSI categories assumed from 'PGSI categories'.
- E2: cumulative: no; источник порога: standard; правило: PGSI row; 1-2 band starts at L1; у авторов: «low-risk»; главная у авторов: no; период: NR; заметка: Whole gambler sample, not restricted to sports bettors.
- E3: cumulative: no; источник порога: standard; правило: PGSI row; 3-7 band starts at L2; у авторов: «moderate-risk»; главная у авторов: no; период: NR; заметка: Whole gambler sample, not restricted to sports bettors.
- E4: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ = L3; у авторов: «high-risk (relabelled from 'problem gambler')»; главная у авторов: no; период: NR; заметка: Whole gambler sample, not restricted to sports bettors. Authors relabel 'problem gambler' as 'high-risk'.

**Ключевые поля выборки:**
- **n_bettors: NR** — Page 5, Table 1 — «Online: Sports betting ... 414 (70.8) ... In-person/venue: Sports betting ... 103 (17.6) ... a :Participants could choose more than one answer»
- **sample_type: gamblers_survey_subsample** — Page 4, Participants and Recruitment; Page 5, Table 1 — «had gambled on something other than exclusively lottery in the past 12-months»
- **sampling: convenience** — Page 4, Participants and Recruitment — «Participants were recruited via the online crowdsourcing platform Prolific and directed to a Qualtrics survey»
- **betting_period: past 12 months** — Page 5, Table 1 — «Past-year gambling engagement a Online: Sports betting 209 (71.8) 205 (69.7) 414 (70.8)»

**Остальные поля:**
- parent_population: UK residents 18+ on the Prolific crowdsourcing platform, fluent in English, who gambled on something other than exclusively lottery in the past 12 months — Page 4, Participants and Recruitment — «Eligible participants were UK residents aged 18 or older, fluent in English, and had gambled on something other than exclusively lottery in the past 12-months.»
- min_frequency: none — Page 4, Participants and Recruitment — «had gambled on something other than exclusively lottery in the past 12-months»
- country: GBR — Page 4, Participants and Recruitment — «Eligible participants were UK residents aged 18 or older»
- subnational: NA — Page 4, Participants and Recruitment — «Eligible participants were UK residents aged 18 or older»
- data_years: 2025 — Page 4, Participants and Recruitment — «directed to a Qualtrics survey in October 2025»
- design: experiment baseline — Page 4, Design; Page 7, Procedure — «This was a between-subjects, mixed-methods online randomised experiment with two Conditions»
- gambling_disclosed: NR — Page 4, Participants and Recruitment — «Participants were recruited via the online crowdsourcing platform Prolific»
- betting_mode: both — Page 5, Table 1 — «Online: Sports betting ... 414 (70.8) ... In-person/venue: Sports betting ... 103 (17.6)»
- pct_online: NR — Page 5, Table 1 — «Online: Sports betting 209 (71.8) 205 (69.7) 414 (70.8)»
- pct_inplay: NR — NA
- pct_dfs: NR — NA
- pct_esports: NR — NA
- sports_lottery: unclear — Page 5, Table 1 — «Sports betting ... Lottery ... Scratch cards»
- mixed_race: no — Page 5, Table 1 — «Sports betting»
- legal_status: regulated legal market — Page 3; Page 13 — «In the UK, the Gambling Commission, who oversee the regulation of gambling ... While licensed operators disclose wagering requirements»
- n_invited: NR — Page 4 — «we aimed to recruit 600 participants»
- n_responded: 600 — Page 4, Participants and Recruitment — «After 15 such responses were excluded (all under one minute), the final sample comprised 585 participants.»
- response_rate: NR — Page 4 — «Participants were recruited via the online crowdsourcing platform Prolific»
- age_mean: 42.2 — Page 5, Table 1 — «Age: mean (SD) 42 (12.2) 41.8 (11.8) 42.2 (12.1)»
- age_sd: 12.1 — Page 5, Table 1 — «Age: mean (SD) 42 (12.2) 41.8 (11.8) 42.2 (12.1)»
- age_min: 18 — Page 4, Participants and Recruitment — «Eligible participants were UK residents aged 18 or older»
- age_max: NR — NA
- age_group: adults — Page 4 — «UK residents aged 18 or older»
- pct_male: 59.5 — Page 5, Table 1 — «Sex Male 165 (56.7) 183 (62.2) 348 (59.5)»
- mode: online — Page 4 — «recruited via the online crowdsourcing platform Prolific and directed to a Qualtrics survey»
- weights: no — Page 7, Analysis — «All analyses were conducted in SPSS (version 30.0.0)»
- instruments: PGSI (English) — Page 6, Gambling Severity — «Gambling severity was assessed using the Problem Gambling Severity Index (PGSI)... (Ferris & Wynne, 2001)»
- instrument_validated_in_language: yes — Page 6, Gambling Severity — «The PGSI is a standardised tool for assessing at-risk gambling in community samples (Ferris & Wynne, 2001)»
- industry_funding: no — Page 14, Funding — «This study was funded by the Gambling Research, Education, and Treatment (GREAT) Centre, Swansea University.»
- funding_coi: Funded by GREAT Centre, Swansea University (infrastructure from Welsh Government via HCRW); authors declare no conflicts; SD directs a centre funded by regulatory settlements; authors received various non-industry gambling research grants (GREO, AFSG, ICRG). — Pages 14-15, Funding; Competing interests — «None of the authors have any conflicts of interest to declare.»
- pub_status: journal — Page 1 — «ORIGINAL PAPER ... Journal of Gambling Studies https://doi.org/10.1007/s10899-026-10491-6»
- language: English — Full text — «(Mis)Comprehension and (Mistaken) Attractiveness of Financial Gambling Inducements among UK Bettors»
- notes: IMPORTANT: The sample is past-year UK gamblers (anything other than lottery only), not sports bettors. 414/585 (70.8%) bet on sports online and 103/585 (17.6%) in person in the past year; overlap not reported, so the number of sports bettors is unknown (at least 414). PGSI categories are reported only for the whole sample of 585 gamblers, not for sports bettors; there is no sports-bettor-specific prevalence. The estimates below are for the whole gambler sample and are included for reviewer judgement only; probably not eligible as sports-bettor estimates. Age and sex are for the whole sample. …

**Риск смещения (JBI):**
1. рамка выборки: **no** — Prolific crowdsourcing panel covers only part of UK sports bettors. — Page 4; Page 13 — «data were collected via a crowdsourcing platform (Prolific) and are limited to a single jurisdiction»
2. способ отбора: **no** — Volunteer opt-in online non-probability panel. — Page 4 — «Participants were recruited via the online crowdsourcing platform Prolific»
3. размер выборки: **yes** — At least 414 online sports bettors (>=385), although the exact number of sports bettors is not reported. — Page 5, Table 1 — «Online: Sports betting 209 (71.8) 205 (69.7) 414 (70.8)»
4. описание выборки и условий: **yes** — Age, sex, setting (Prolific online), country (UK) and date (October 2025) reported, for the whole sample. — Page 4; Table 1 — «directed to a Qualtrics survey in October 2025»
5. охват (пропуски): **yes** — PGSI categories cover all 585 participants (275+141+108+61=585). — Page 6 — «275 participants (47.0%) were classified as no-risk, 141 (24.1%) as low-risk, 108 (18.5%) as moderate-risk and 61 (10.4%) as high-risk»
6. валидность определения случая: **yes** — Standard PGSI in English with standard categories. — Page 6 — «contains 9 items rated on a 4-point Likert-scale ranging from 0 (never) to 3 (almost always)»
7. единое надёжное измерение: **yes** — Same online PGSI for all; reliability reported (alpha 0.92). — Page 6 — «Internal consistency for the PGSI in the present study was excellent (Cronbach’s α = 0.92)»
8. статистика (числитель и знаменатель): **no** — PGSI is reported only for all gamblers; no numerator or denominator for sports bettors. — Page 6; Table 1 — «based on PGSI categories, 275 participants (47.0%) were classified as no-risk»
9. отклик: **no** — Online panel with no denominator of invited people; response rate not reported or handled. — Page 4 — «we aimed to recruit 600 participants ... the final sample comprised 585 participants»

Правки:
- 

Проверено: да

---

## ST010 · Kerimu I.  Joel 2025 · Zenodo

Основной отчёт R1744: [текст](../../fulltext/text/R1744.txt) · [PDF](../../fulltext/pdf/R1744.pdf) — «Sports Betting And Gambling Problems Among University Student-Athletes» — [DOI](https://doi.org/10.5281/zenodo.15663047)
Расхождения в тексте: Table 1 gives the Residence total as 113, but its rows (36 + 82) add up to 118. The PGSI categories add up to 118 (55+13+35+15) and their percentages (46.6/11.0/29.7/12.7) match n=118. The Discussion rounds the non-problem share to 46% instead of the 46.6% in the Results. The Abstract and Discussion repeat the 55.1% male figure from Table 1 (65/118).
Заметка ИИ: One sample was extracted. Its eligibility is questionable: the denominator is all student-athletes who responded, with no sports-betting participation screen. The reviewer should decide whether it counts as a sample of sports bettors.

### ST010-1 · Student-athletes, University of Nigeria Nsukka, Nigeria, n=118
Отчёты: R1744 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | PGSI · PGSI 0 | **below** | **55 / 118** | 46.6 | Page 5, Fig. 1 text | «a total of 55 (46.6%) were non-problem sports bettors» |
| E2 | all | PGSI · PGSI 1-2 | **L1** | **13 / 118** | 11.0 | Page 5, Fig. 1 text | «13 (11.0%) were low level sports bettors» |
| E3 | all | PGSI · PGSI 3-7 | **L2** | **35 / 118** | 29.7 | Page 5, Fig. 1 text | «35 (29.7%) were moderate sports bettors» |
| E4 | all | PGSI · PGSI>=8 | **L3** | **15 / 118** | 12.7 | Page 5, Fig. 1 text; Abstract | «15 (12.7%) were problem sports bettors» |

- E1: cumulative: no; источник порога: standard; правило: PGSI row; score 0 = below; у авторов: «non-problem sports bettors»; главная у авторов: no; период: NR; заметка: Denominator is all respondents; betting status not ascertained. The Discussion gives 46% instead of 46.6%.
- E2: cumulative: no; источник порога: standard; правило: PGSI row; 1-2 band starts at L1; у авторов: «low level sports bettors»; главная у авторов: no; период: NR
- E3: cumulative: no; источник порога: standard; правило: PGSI row; 3-7 band starts at L2; у авторов: «moderate sports bettors»; главная у авторов: no; период: NR
- E4: cumulative: yes; источник порога: standard; правило: PGSI row; 8+ = L3; у авторов: «problem sports bettors»; главная у авторов: yes; период: NR; заметка: This is the headline estimate in the Abstract. Denominator is all 118 respondents.

**Ключевые поля выборки:**
- **n_bettors: 118** — Page 5, Fig. 1 text — «of all the respondents, a total of 55 (46.6%) were non-problem sports bettors, while 13 (11.0%) were low level ... 35 (29.7%) were moderate ... 15 (12.7%) were problem sports bettors»
- **sample_type: athletes** — Page 3, 2.2 — «The population for the study comprised 216 student-athletes that represented the University of Nigeria at the Nigeria Universities Games 2022 in Lagos, Nigeria.»
- **sampling: census** — Page 3, 2.3 — «The researchers intended to use the total population (216); however, among the 216 students we approached to participate in the study, 118 (54.6%) accepted»
- **betting_period: NR** — Page 3, 2.4 — «NR»

**Остальные поля:**
- parent_population: 216 student-athletes who represented the University of Nigeria at the Nigeria Universities Games 2022 — Page 3, 2.2 — «The population for the study comprised 216 student-athletes that represented the University of Nigeria at the Nigeria Universities Games 2022»
- min_frequency: NR — Page 3, 2.2-2.4 — «NR»
- country: NGA — Page 3, 2.1 — «A cross-sectional study was carried out among student-athletes of the University of Nigeria, Nsukka, Nigeria.»
- subnational: Nsukka (University of Nigeria) — Page 3, 2.1 — «student-athletes of the University of Nigeria, Nsukka, Nigeria»
- data_years: NR — Page 3, 2.2; Page 6, Ethics — «216 student-athletes that represented the University of Nigeria at the Nigeria Universities Games 2022 ... approved on January 26, 2024»
- design: cross-sectional — Page 3, 2.1 — «A cross-sectional study was carried out among student-athletes»
- gambling_disclosed: yes — Page 3, 2.3 and 2.5 — «Following a briefing on the study's objectives ... the confidence to face the topic may have caused their declined from participating in the study.»
- betting_mode: NR — Methods — «NR»
- pct_online: NR — Results — «NR»
- pct_inplay: NR — Results — «NR»
- pct_dfs: NR — Results — «NR»
- pct_esports: NR — Results — «NR»
- sports_lottery: unclear — Methods — «NR»
- mixed_race: no — Page 3, 2.4 — «“gambling” and “bet” were changed with the words “sports betting” and “sports bet.”»
- legal_status: regulated legal market — Page 1, Introduction — «As of January 2025, the National Lottery Regulatory Commission (NLRC) has licensed 72 sports betting companies to operate across the country»
- n_invited: 216 — Page 3, 2.3 — «among the 216 students we approached to participate in the study, 118 (54.6%) accepted»
- n_responded: 118 — Page 3, 2.3 — «118 (54.6%) accepted to be involved»
- response_rate: 54.6 — Page 3, 2.3 — «118 (54.6%) accepted to be involved»
- age_mean: NR — Page 4, Table 1 — «NR»
- age_sd: NR — Page 4, Table 1 — «NR»
- age_min: 16 — Page 1, Abstract; Page 4, Table 1 — «aged between 16 and 40 years old»
- age_max: 40 — Page 1, Abstract; Page 4, Table 1 — «aged between 16 and 40 years old»
- age_group: mixed — Page 4, Table 1 — «16 - 19 years old 15 12.7»
- pct_male: 55.1 — Page 4, Table 1 — «Male 65 55.1 Female 53 44.9 Total 118 100.0»
- mode: paper — Page 3, 2.5 — «the research team personally distributed questionnaires to participants in Nsukka ... we collected 118 filled questionnaires»
- weights: no — Page 3, 2.6 — «Frequencies, percentages, means, and standard deviations were used to analyse the data.»
- instruments: PGSI (English, adapted: 'gambling'/'bet' reworded to 'sports betting'/'sports bet'; 0-3 item scoring, 0-27 total) — Page 3, 2.4 — «The researchers adapted the Problem Gambling Severity Index (PGSI) ... “gambling” and “bet” were changed with the words “sports betting” and “sports bet.” ... …»
- instrument_validated_in_language: yes — Page 3, 2.4 — «The scale validity and reliability have been ensured, with a Cronbach α of .91 [51].»
- industry_funding: no — Page 6, Conflict of interest — «The authors declare no conflicts of interest. Furthermore, no financial assistance was received.»
- funding_coi: No funding; no conflicts of interest declared — Page 6, Conflict of interest — «The authors declare no conflicts of interest. Furthermore, no financial assistance was received.»
- pub_status: journal — Page 1, header — «Journal of Sport Industry & Blockchain Technology– 2025, 2(1), 1-8»
- language: English — Full text — «Sports Betting And Gambling Problems Among University Student-Athletes»
- notes: The sample is all responding student-athletes, not screened sports bettors. The paper reports no sports-betting participation question or reference period: the PGSI was given to all 118 respondents and all are called 'sports bettors', so PGSI 0 (n=55) may include non-bettors. Eligibility needs reviewer confirmation. Age range and sex describe the whole sample (n=118). Data collection dates are not reported: the population is the 2022 Nigeria Universities Games team, and ethics approval is dated 26 January 2024, so data were probably collected in 2024 or later. The PGSI time frame is not state…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame is one university's 216 Games team members; it covers only part of the claimed target (university student-athletes in Nigeria), and the frame is not defined as sports bettors. — Page 3, 2.2; Page 5, Discussion — «the use of one University for the study may affect the generalization of the results»
2. способ отбора: **yes** — The whole frame was approached (attempted census); non-response is rated under item 9. — Page 3, 2.3 — «The researchers intended to use the total population (216)»
3. размер выборки: **no** — n=118, below 385. — Page 3, 2.3 — «118 (54.6%) accepted to be involved»
4. описание выборки и условий: **unclear** — Age, sex, setting and country are reported, but the dates of data collection are not. — Page 4, Table 1; Page 3, 2.5 — «The researchers met the student-athletes at the Sports council of the University of Nigeria, Nsukka.»
5. охват (пропуски): **yes** — All 118 respondents fall into a PGSI category (55+13+35+15=118). — Page 5, Fig. 1 text — «55 (46.6%) ... 13 (11.0%) ... 35 (29.7%) ... 15 (12.7%)»
6. валидность определения случая: **yes** — PGSI with the standard 8+ threshold. The English original is validated; the items were reworded for sports betting with the 0-3 scoring unchanged. — Page 3, 2.4 — «problem gamblers (score of 8 or higher)»
7. единое надёжное измерение: **yes** — Everyone got the same paper questionnaire and threshold; reliability is cited from the source (alpha .91). — Page 3, 2.4 — «The scale validity and reliability have been ensured, with a Cronbach α of .91 [51].»
8. статистика (числитель и знаменатель): **unclear** — Counts and n are given and a CI can be calculated, but the denominator is all responding student-athletes. Sports betting participation was never ascertained. — Page 5 — «of all the respondents, a total of 55 (46.6%) were non-problem sports bettors»
9. отклик: **no** — Response was 54.6%, with no comparison of non-responders and no weighting. — Page 3, 2.3 — «118 (54.6%) accepted to be involved»

Правки:
- 

Проверено: да

