# Prevalence of problem gambling among people who bet on sports: meta-analysis (protocol v1.0, sections 13, 15-17).
#
# Reads forms/samples.csv (verified extraction, extraction/finalize.py) and analysis/data/level_estimates.csv
# (cumulative levels built from the verified categories, analysis/build_levels.py), and writes the results to
# analysis/results/ and the figures to analysis/figures/. Every pooled analysis uses one estimate per sample, chosen by
# the rules of section 13; the choices are written to results/selection_log.csv.
# Template: papers/misophonia-prevalence/analysis/analysis.R.
#
# Run from the repository root:
#   Rscript papers/sports-betting-prevalence/analysis/analysis.R [paper_dir]
# Default: papers/sports-betting-prevalence.

suppressPackageStartupMessages({
  library(metafor)
  library(lme4)
  library(clubSandwich)
  library(dplyr)
  library(readr)
  library(ggplot2)
})

args <- commandArgs(trailingOnly = TRUE)
paper <- if (length(args) >= 1) args[1] else "papers/sports-betting-prevalence"
res_dir <- file.path(paper, "analysis", "results")
fig_dir <- file.path(paper, "analysis", "figures")
dir.create(res_dir, showWarnings = FALSE, recursive = TRUE)
dir.create(fig_dir, showWarnings = FALSE, recursive = TRUE)
MIN_K <- 3        # section 15b: a pooled estimate needs at least three independent samples
MIN_K_MOD <- 10   # exploratory moderators are tested only when k >= 10 samples
TRAN <- c(prev = 0.089, lo = 0.052, hi = 0.135)   # Tran et al. 2024, adults who bet on sports, representative surveys

# Samples whose estimates are not for sports bettors: the denominator includes people who did not bet on sports
# (the PGSI is reported only for all gamblers or all respondents). They stay in the evidence tables, are left out of
# the pooled analyses, and are added back in a sensitivity analysis (deviations.md, D8).
NOT_BETTORS <- c("S009", "S015", "S034")   # confirmed by R1, 2026-10-20

# ---------------------------------------------------------------------------------------------------------------
# Data
# ---------------------------------------------------------------------------------------------------------------

num <- function(x) suppressWarnings(as.numeric(gsub(",", "", trimws(as.character(x)))))
pct_all <- function(x) ifelse(trimws(x) == "all", 100, num(x))

samples <- read_csv(file.path(paper, "forms", "samples.csv"), col_types = cols(.default = "c"), na = character())
lev <- read_csv(file.path(paper, "analysis", "data", "level_estimates.csv"), col_types = cols(.default = "c"),
                na = character())

samples <- samples |>
  mutate(
    stype = case_when(
      sample_type == "rep_survey_subsample" ~ "bettors in representative surveys",
      sample_type == "gamblers_survey_subsample" ~ "bettors in other gambler surveys",
      sample_type == "bettor_recruited" ~ "bettors recruited as such",
      sample_type %in% c("students", "school_pupils", "athletes", "other") ~ "students, pupils and other",
      TRUE ~ "other"),
    prob = sampling %in% c("probability", "census"),
    agegrp = case_when(age_group == "adolescents" ~ "adolescents", age_group == "adults" ~ "adults",
                       TRUE ~ "mixed or NR"),
    regiongrp = case_when(region %in% c("Europe", "Oceania", "sub-Saharan Africa", "North America") ~ region,
                          region == "" | is.na(region) ~ NA_character_, TRUE ~ "other"),
    age_mean_n = num(age_mean), pct_male_n = num(pct_male), year_data = num(substr(data_years, 1, 4)),
    journal = pub_status == "journal",
    online_only = case_when(betting_mode == "online only" ~ "online only", betting_mode == "land-based only" ~
                              "land-based only", betting_mode == "both" ~ "both", TRUE ~ NA_character_),
    inplay_n = pct_all(pct_inplay), esports = ifelse(pct_all(pct_esports) >= 50, "esports", "other sports"),
    dfs = ifelse(!is.na(pct_all(pct_dfs)) & pct_all(pct_dfs) >= 50, "DFS", "other"),
    regular = ifelse(trimws(tolower(min_frequency)) %in% c("none", "nr", ""), "any bettor", "minimum frequency"),
    period = ifelse(betting_period %in% c("past 12 months", "past 30 days or month", "lifetime"), betting_period, NA),
    legal = ifelse(legal_status %in% c("regulated legal market", "state monopoly", "not legal or unregulated", "mixed"),
                   legal_status, NA),
    disclosed = ifelse(gambling_disclosed %in% c("yes", "no"), gambling_disclosed, NA),
    funded = ifelse(industry_funding %in% c("yes", "no"), industry_funding, NA),
    survey_mode = ifelse(mode %in% c("online", "telephone", "face-to-face", "paper", "mixed"), mode, NA),
    mixed_or_lottery = mixed_race == "yes" | sports_lottery == "unclear")

lev <- lev |>
  mutate(cases_n = num(cases), n_n = num(n),
         level3 = ifelse(level %in% c("L3", "L3-screen"), "L3", level)) |>   # L3-screen counts as L3 (sensitivity 3)
  left_join(samples |> select(sample_id, study_id, first_author, year, country, region, regiongrp, stype, prob,
                              agegrp, age_mean_n, pct_male_n, year_data, journal, pub_status, online_only, inplay_n,
                              esports, dfs, regular, period, legal, disclosed, funded, survey_mode, mixed_or_lottery,
                              starts_with("jbi_")),
            by = "sample_id")

whole_all <- lev |> filter(whole == "yes", n_n > 0, cases_n >= 0, cases_n <= n_n)
whole <- whole_all |> filter(!sample_id %in% NOT_BETTORS)

# ---------------------------------------------------------------------------------------------------------------
# One estimate per sample (section 13)
# ---------------------------------------------------------------------------------------------------------------

# Within a level: the authors' primary instrument; otherwise the PGSI; otherwise the standard threshold of the levels
# table; if several remain, the median logit prevalence (with an even number, the lower of the two middle values).
choose_one <- function(d) {
  if (nrow(d) == 1) return(list(row = d, rule = "only estimate"))
  why <- c()
  step <- function(keep, label) {
    if (any(keep) && !all(keep)) { d <<- d[keep, , drop = FALSE]; why <<- c(why, label) }
  }
  step(d$instrument %in% d$instrument[d$primary_for_authors == "yes"], "authors' primary instrument")
  if (nrow(d) > 1) step(d$instrument == "PGSI", "PGSI")
  if (nrow(d) > 1) step(d$standard == "yes", "standard threshold")
  if (nrow(d) > 1) step(d$level != "L3-screen", "full screen before brief screen")
  if (nrow(d) == 1) return(list(row = d, rule = paste(why, collapse = "; ")))
  lg <- qlogis(pmin(pmax(d$cases_n / d$n_n, 1e-6), 1 - 1e-6))
  o <- order(lg)
  list(row = d[o[ceiling(length(o) / 2)], , drop = FALSE], rule = paste(c(why, "median logit"), collapse = "; "))
}

# levels: the levels allowed, highest first (primary: L4, else L3).
select_level <- function(data, levels, analysis) {
  out <- list(); log <- list()
  for (s in unique(data$sample_id)) {
    d <- data |> filter(sample_id == s, level3 %in% levels)
    if (nrow(d) == 0) next
    lv <- levels[levels %in% d$level3][1]
    d <- d |> filter(level3 == lv)
    ch <- choose_one(d)
    out[[s]] <- ch$row
    log[[s]] <- tibble(analysis = analysis, sample_id = s, estimate_ids = ch$row$estimate_ids, level = ch$row$level,
                       instrument = ch$row$instrument, threshold = ch$row$threshold, source = ch$row$source,
                       cases = ch$row$cases_n, n = ch$row$n_n, candidates = nrow(d), rule = ch$rule)
  }
  list(data = bind_rows(out), log = bind_rows(log))
}

# ---------------------------------------------------------------------------------------------------------------
# Pooling
# ---------------------------------------------------------------------------------------------------------------

empty_row <- function(label, d, note) {
  tot <- function(col) if (nrow(d) == 0 || !col %in% names(d)) 0 else sum(d[[col]])
  tibble(analysis = label, k = nrow(d), n_total = tot("n_n"), cases_total = tot("cases_n"), prev = NA_real_,
         ci.lb = NA_real_, ci.ub = NA_real_, pi.lb = NA_real_, pi.ub = NA_real_, tau2 = NA_real_, I2 = NA_real_,
         method = NA_character_, note = note)
}

pool_glmm <- function(d, label) {
  if (nrow(d) < MIN_K) return(empty_row(label, d, sprintf("k < %d: not pooled", MIN_K)))
  m <- tryCatch(rma.glmm(measure = "PLO", xi = d$cases_n, ni = d$n_n, method = "ML"), error = function(e) e)
  if (inherits(m, "error")) return(empty_row(label, d, paste("GLMM failed:", conditionMessage(m))))
  p <- predict(m, transf = transf.ilogit)
  tibble(analysis = label, k = m$k, n_total = sum(d$n_n), cases_total = sum(d$cases_n), prev = p$pred,
         ci.lb = p$ci.lb, ci.ub = p$ci.ub, pi.lb = p$pi.lb, pi.ub = p$pi.ub, tau2 = m$tau2, I2 = m$I2,
         method = "GLMM (binomial-normal, ML)", note = "")
}

pool_iv <- function(d, label) {
  if (nrow(d) < MIN_K) return(empty_row(label, d, sprintf("k < %d: not pooled", MIN_K)))
  es <- escalc(measure = "PLO", xi = d$cases_n, ni = d$n_n)
  m <- rma(yi, vi, data = es, method = "REML", test = "knha")
  p <- predict(m, transf = transf.ilogit)
  tibble(analysis = label, k = m$k, n_total = sum(d$n_n), cases_total = sum(d$cases_n), prev = p$pred,
         ci.lb = p$ci.lb, ci.ub = p$ci.ub, pi.lb = p$pi.lb, pi.ub = p$pi.ub, tau2 = m$tau2, I2 = m$I2,
         method = "inverse variance, logit, REML + Hartung-Knapp", note = "")
}

subgroup_test <- function(d, var) {
  g <- d[[var]]
  keep <- !is.na(g)
  d <- d[keep, ]; g <- factor(g[keep])
  if (nlevels(g) < 2 || nrow(d) < MIN_K) return(tibble(moderator = var, QM = NA, df = NA, p = NA))
  m <- tryCatch(rma.glmm(measure = "PLO", xi = d$cases_n, ni = d$n_n, mods = ~ g, method = "ML"),
                error = function(e) NULL)
  if (is.null(m)) return(tibble(moderator = var, QM = NA, df = NA, p = NA))
  tibble(moderator = var, QM = m$QM, df = m$p - 1, p = m$QMp)
}

results <- list()
logs <- list()

# Primary outcome: L4 if the sample has one, else L3 (problem gambling), all non-selected samples.
sel_primary <- select_level(whole, c("L4", "L3"), "primary L3/L4")
prim <- sel_primary$data
logs$primary <- sel_primary$log
results$primary <- pool_glmm(prim, "Primary: problem gambling (L3/L4)")

# Level-specific estimates (section 13: the estimate at that level).
level_data <- list()
for (lv in c("L1", "L2", "L3", "L4")) {
  s <- select_level(whole, lv, paste("level", lv))
  level_data[[lv]] <- s$data
  logs[[paste0("level_", lv)]] <- s$log
  results[[paste0("level_", lv)]] <- pool_glmm(s$data, paste("Level", lv))
}

# Subgroups of the primary outcome.
SUBS <- c(stype = "sample type", agegrp = "age group", regiongrp = "region")
for (v in names(SUBS)) {
  for (g in sort(unique(na.omit(prim[[v]])))) {
    results[[paste(v, g)]] <- pool_glmm(prim |> filter(.data[[v]] == g), paste0("Primary by ", SUBS[[v]], ": ", g))
  }
}
sub_tests <- bind_rows(lapply(names(SUBS), function(v) subgroup_test(prim, v)))
# Levels L1 and L2 by sample type (secondary outcome: prevalence by sample type at each level).
for (lv in c("L1", "L2")) {
  for (g in sort(unique(level_data[[lv]]$stype))) {
    results[[paste(lv, g)]] <- pool_glmm(level_data[[lv]] |> filter(stype == g), paste0("Level ", lv, " by sample type: ", g))
  }
}

# Post hoc (D9): the moderate-risk band alone (PGSI 3-7), pooled from the closed bands, so that the size of the
# moderate-risk group is not read off as the difference between two pooled levels with different samples.
bands <- read_csv(file.path(paper, "forms", "estimates.csv"), col_types = cols(.default = "c"), na = character()) |>
  filter(instrument == "PGSI", trimws(threshold) == "PGSI 3-7", !sample_id %in% NOT_BETTORS) |>
  left_join(samples |> select(sample_id, n_bettors), by = "sample_id") |>
  mutate(cases_n = num(cases), n_n = num(n)) |>
  filter(!is.na(cases_n), !is.na(n_n), tolower(trimws(subgroup)) == "all" | n_n == num(n_bettors)) |>
  group_by(sample_id) |> slice(1) |> ungroup()
results$band_3_7 <- pool_glmm(bands, "Post hoc: moderate-risk band only (PGSI 3-7)")

# Benchmark (descriptive): bettors in representative surveys beside Tran et al. (2024).
bench <- results[["stype bettors in representative surveys"]] |>
  mutate(tran_prev = TRAN[["prev"]], tran_ci.lb = TRAN[["lo"]], tran_ci.ub = TRAN[["hi"]],
         note = "descriptive comparison, no formal test (protocol 15b)")

# ---------------------------------------------------------------------------------------------------------------
# Sensitivity analyses on the primary outcome (section 15c)
# ---------------------------------------------------------------------------------------------------------------

sens <- list()
sens$s1 <- pool_glmm(prim |> filter(jbi_2 == "yes"), "S1 probability or census sampling (JBI 2 = yes)")
sens$s2 <- pool_glmm(prim |> filter(jbi_6 == "yes"), "S2 validated instrument and cut-off (JBI 6 = yes)")
sens$s3 <- pool_glmm(prim |> filter(level != "L3-screen"), "S3 without brief screens (L3-screen)")
# S4: PGSI revised thresholds (Currie et al. 2013: 1-4 / 5-7 / 8+) leave L3 (PGSI >= 8) unchanged; the revised
# moderate-risk level (PGSI >= 5) is pooled where the categories allow.
rev5 <- whole |> filter(instrument == "PGSI", threshold == "PGSI>=5")
sens$s4 <- pool_glmm(rev5, "S4 PGSI revised moderate-risk threshold (>= 5); L3 unchanged by the revision")
sens$s5 <- pool_glmm(prim |> filter(jbi_9 %in% c("yes", "NA")), "S5 response rate >= 60% or handled (JBI 9)")
sens$s6 <- pool_glmm(prim |> filter(!mixed_or_lottery), "S6 without sports-and-race or unclear sports-lottery samples")
# The drafts used sports_lottery = unclear also for "not stated" (D8), so S6 as coded drops samples that only listed
# lotteries as a separate activity; S6b drops only the samples defined as sports-and-race or by a sports lottery.
sens$s6b <- pool_glmm(prim |> filter(!sample_id %in% samples$sample_id[samples$mixed_race == "yes" | samples$sports_lottery == "yes"]),
                      "S6b (post hoc) without sports-and-race samples and samples defined by a sports lottery")
sens$s7 <- pool_glmm(prim |> filter(journal), "S7 journal articles only")
sens$s8 <- pool_glmm(prim |> filter(n_n >= 100), "S8 n >= 100")
sens$s9 <- pool_iv(prim, "S9 inverse-variance pooling of logits (REML, Hartung-Knapp)")
sel_all <- select_level(whole_all, c("L4", "L3"), "post hoc: with samples whose denominator includes non-bettors")
logs$with_nonbettors <- sel_all$log
sens$s11 <- pool_glmm(sel_all$data, "S11 (post hoc) with samples whose denominator includes non-bettors (D8)")
sens$s12 <- pool_glmm(prim |> filter(sample_id != "S010"), "S12 (post hoc) without student-athletes not screened for betting (S010)")
sel_l3 <- select_level(whole, "L3", "L3 instead of L4")
sens$s13 <- pool_glmm(sel_l3$data, "S13 L3 for every sample (the L4 interview estimate replaced by the sample's L3)")

# S10: leave-one-out (GLMM) and influence diagnostics (inverse-variance model).
loo <- NULL; infl <- NULL
if (nrow(prim) > MIN_K) {
  loo <- bind_rows(lapply(seq_len(nrow(prim)), function(i) {
    r <- pool_glmm(prim[-i, ], paste("without", prim$sample_id[i]))
    r$sample_id <- prim$sample_id[i]
    r
  }))
  es <- escalc(measure = "PLO", xi = prim$cases_n, ni = prim$n_n)
  m <- rma(yi, vi, data = es, method = "REML", test = "knha")
  inf <- influence(m)
  infl <- tibble(sample_id = prim$sample_id, rstudent = inf$inf$rstudent, cook = inf$inf$cook.d,
                 influential = inf$is.infl)
}

# ---------------------------------------------------------------------------------------------------------------
# Three-level moderator analysis on all whole-sample cumulative estimates (section 15b)
# ---------------------------------------------------------------------------------------------------------------

zs <- function(x) as.numeric(scale(x))   # continuous moderators centred and scaled, so that glmer converges
ml <- whole |> mutate(est_id = row_number(), level = factor(level3, levels = c("L1", "L2", "L3", "L4")),
                      stype = factor(stype, levels = c("bettors in representative surveys", "bettors in other gambler surveys",
                                                       "bettors recruited as such", "students, pupils and other")),
                      age_z = zs(age_mean_n), male_z = zs(pct_male_n), year_z = zs(year_data), inplay_z = zs(inplay_n))
re_terms <- function(g) paste0("(1 | ", names(getME(g, "flist")), ")")
fit_glmer <- function(formula_fixed, data, re = c("(1 | study_id)", "(1 | sample_id)", "(1 | est_id)"),
                      drop = TRUE) {
  repeat {
    f <- as.formula(paste("cbind(cases_n, n_n - cases_n) ~", formula_fixed, "+", paste(re, collapse = " + ")))
    g <- tryCatch(glmer(f, data = data, family = binomial,
                        control = glmerControl(optimizer = "bobyqa", optCtrl = list(maxfun = 2e5))),
                  error = function(e) NULL)
    if (is.null(g)) return(NULL)
    if (!drop || !isSingular(g) || length(re) == 1) return(g)
    vc <- as.data.frame(VarCorr(g))
    zero <- vc$grp[which.min(vc$vcov)]
    re <- re[!grepl(paste0("\\| ", zero, "\\)"), re)]   # drop the variance component estimated at zero
  }
}
multilevel <- list()
if (length(unique(ml$sample_id)) >= MIN_K_MOD) {
  multilevel$prespecified <- fit_glmer("level + stype + prob", ml)
  es_ml <- escalc(measure = "PLO", xi = ml$cases_n, ni = ml$n_n, data = ml)
  mv <- tryCatch(rma.mv(yi, vi, mods = ~ level + stype + prob, random = ~ 1 | study_id / sample_id / est_id,
                        data = es_ml, method = "REML"), error = function(e) NULL)
  multilevel$rma_mv <- mv
  multilevel$robust <- if (!is.null(mv)) coef_test(mv, vcov = "CR2", cluster = es_ml$study_id) else NULL
  explore <- c("online_only", "inplay_z", "dfs", "esports", "regular", "period", "regiongrp", "legal", "year_z",
               "age_z", "male_z", "survey_mode", "disclosed", "jbi_2", "jbi_6", "jbi_9", "journal", "funded")
  coefs <- list()
  lrt <- function(v, d, base) {
    k <- length(unique(d$sample_id))
    if (k < MIN_K_MOD || length(unique(d[[v]])) < 2) {
      return(tibble(moderator = v, k_samples = k, chisq = NA, df = NA, p = NA,
                    note = "k < 10 or no variation: not tested"))
    }
    g1 <- fit_glmer(paste(base, "+", v), d)
    g0 <- if (is.null(g1)) NULL else fit_glmer(base, d, re = re_terms(g1), drop = FALSE)   # same random part
    if (is.null(g1) || is.null(g0)) return(tibble(moderator = v, k_samples = k, chisq = NA, df = NA, p = NA,
                                                   note = "model failed"))
    a <- anova(g0, g1)
    cf <- summary(g1)$coefficients
    cf <- cf[startsWith(rownames(cf), v), , drop = FALSE]
    ref <- if (is.numeric(d[[v]])) "per SD" else levels(factor(d[[v]]))[1]
    coefs[[v]] <<- tibble(moderator = v, term = rownames(cf), reference = ref, OR = exp(cf[, 1]),
                          ci.lb = exp(cf[, 1] - 1.96 * cf[, 2]), ci.ub = exp(cf[, 1] + 1.96 * cf[, 2]),
                          p = cf[, 4], n_estimates = nrow(d),
                          n_samples_term = vapply(rownames(cf), function(t) {
                            lv <- substring(t, nchar(v) + 1)
                            if (is.numeric(d[[v]])) k else length(unique(d$sample_id[as.character(d[[v]]) == lv]))
                          }, integer(1)))
    tibble(moderator = v, k_samples = k, chisq = a$Chisq[2], df = a$Df[2], p = a$`Pr(>Chisq)`[2],
           note = if (base == "level") "likelihood-ratio test, adjusted for level" else
             "likelihood-ratio test, L3 estimates only")
  }
  ok <- function(x) !is.na(x) & as.character(x) != "" & as.character(x) != "NR"
  multilevel$exploratory <- bind_rows(
    lapply(explore, function(v) lrt(v, ml |> filter(ok(.data[[v]])), "level")),
    lrt("instrument", ml |> filter(level == "L3") |> mutate(instrument = ifelse(instrument == "PGSI", "PGSI", "other")), "1"))
  multilevel$exploratory_coefs <- bind_rows(coefs)
  vtot <- function(m) if (is.null(m)) NA_real_ else sum(as.data.frame(VarCorr(m))$vcov)
  g_null <- fit_glmer("1", ml)
  multilevel$variance_explained <- tibble(
    model = c("level", "level + sample type", "level + sample type + probability sampling"),
    total_variance = c(vtot(fit_glmer("level", ml)), vtot(fit_glmer("level + stype", ml)), vtot(multilevel$prespecified)),
    null_variance = vtot(g_null)) |>
    mutate(pseudo_R2 = 1 - total_variance / null_variance)
}

# ---------------------------------------------------------------------------------------------------------------
# Sex difference (log odds ratio, male vs female, at the sample's primary level and instrument)
# ---------------------------------------------------------------------------------------------------------------

sexdat <- lev |> filter(!sample_id %in% NOT_BETTORS, tolower(trimws(subgroup)) %in% c("male", "female"),
                        n_n > 0, cases_n >= 0, cases_n <= n_n)
sex_rows <- list()
for (s in unique(sexdat$sample_id)) {
  d <- sexdat |> filter(sample_id == s) |> mutate(sx = tolower(trimws(subgroup)))
  pairs <- d |> group_by(level3, instrument, threshold) |> filter(all(c("female", "male") %in% sx)) |> ungroup()
  if (nrow(pairs) == 0) next
  p <- prim |> filter(sample_id == s)
  if (nrow(p) == 1 && any(pairs$level3 == p$level3 & pairs$instrument == p$instrument)) {
    pairs <- pairs |> filter(level3 == p$level3, instrument == p$instrument)
  } else {
    top <- c("L4", "L3", "L2", "L1")[c("L4", "L3", "L2", "L1") %in% pairs$level3][1]
    pairs <- pairs |> filter(level3 == top)
  }
  m <- pairs |> filter(sx == "male") |> slice(1)
  f <- pairs |> filter(sx == "female", threshold == m$threshold) |> slice(1)
  sex_rows[[s]] <- tibble(sample_id = s, instrument = m$instrument, level = m$level3, threshold = m$threshold,
                          m_cases = m$cases_n, m_n = m$n_n, f_cases = f$cases_n, f_n = f$n_n)
}
sex <- bind_rows(sex_rows)
sex_result <- NULL
if (nrow(sex) >= MIN_K) {
  es <- escalc(measure = "OR", ai = sex$m_cases, n1i = sex$m_n, ci = sex$f_cases, n2i = sex$f_n)
  sm <- rma(yi, vi, data = es, method = "REML", test = "knha")
  sp <- predict(sm, transf = exp)
  sex_result <- tibble(k = sm$k, OR = sp$pred, ci.lb = sp$ci.lb, ci.ub = sp$ci.ub, pi.lb = sp$pi.lb,
                       pi.ub = sp$pi.ub, tau2 = sm$tau2, I2 = sm$I2, comparison = "male vs female")
}

# ---------------------------------------------------------------------------------------------------------------
# Within-study contrasts (post hoc, descriptive; D9): groups of bettors compared inside one study with the same
# instrument and recruitment, where the exploratory moderators could not be tested (k < 10).
# ---------------------------------------------------------------------------------------------------------------

CONTRASTS <- tribble(
  ~contrast, ~study, ~sample_a, ~sub_a, ~sample_b, ~sub_b, ~level,
  "esports vs traditional sports bettors", "Greer et al. 2021 (two quota samples, Australia)", "S035", "all", "S036", "all", "L3",
  "esports vs traditional sports bettors", "Wardle et al. 2020 (emerging adults, Great Britain)", "S046", "esports", "S046", "other sports", "L3",
  "weekly vs less frequent sports bettors", "Castrén et al. 2013 (population survey, Finland)", "S058", "bet on sports at least once a week",
  "S058", "bet on sports less than once a week", "L3",
  "online vs land-based sports bettors (groups overlap)", "Tomei et al. 2025 (conscripts, Switzerland)", "S013", "online", "S013",
  "land-based", "L2")
within <- bind_rows(lapply(seq_len(nrow(CONTRASTS)), function(i) {
  ct <- CONTRASTS[i, ]
  get <- function(s, sb) lev |> filter(sample_id == s, subgroup == sb, level3 == ct$level, standard == "yes") |> slice(1)
  a <- get(ct$sample_a, ct$sub_a); b <- get(ct$sample_b, ct$sub_b)
  if (nrow(a) == 0 || nrow(b) == 0) return(NULL)
  e <- escalc(measure = "OR", ai = a$cases_n, n1i = a$n_n, ci = b$cases_n, n2i = b$n_n)
  tibble(contrast = ct$contrast, study = ct$study, level = ct$level, threshold = a$threshold,
         cases_a = a$cases_n, n_a = a$n_n, prev_a = a$cases_n / a$n_n, cases_b = b$cases_n, n_b = b$n_n,
         prev_b = b$cases_n / b$n_n, OR = exp(e$yi), ci.lb = exp(e$yi - 1.96 * sqrt(e$vi)),
         ci.ub = exp(e$yi + 1.96 * sqrt(e$vi)))
}))

# ---------------------------------------------------------------------------------------------------------------
# Meta-biases (section 16) and GRADE inputs (section 17)
# ---------------------------------------------------------------------------------------------------------------

bias <- NULL
if (nrow(prim) >= MIN_K) {
  es <- escalc(measure = "PLO", xi = prim$cases_n, ni = prim$n_n, data = prim)
  es$inv_sqrt_n <- 1 / sqrt(es$n_n)
  reg <- rma(yi, vi, mods = ~ inv_sqrt_n, data = es, method = "REML", test = "knha")
  pubm <- tryCatch(rma.glmm(measure = "PLO", xi = prim$cases_n, ni = prim$n_n, mods = ~ prim$journal, method = "ML"),
                   error = function(e) NULL)
  bias <- tibble(test = c("logit prevalence on 1/sqrt(n) (REML, Hartung-Knapp)", "journal vs other (GLMM)"),
                 estimate = c(coef(reg)[2], if (is.null(pubm)) NA else coef(pubm)[2]),
                 p = c(reg$pval[2], if (is.null(pubm)) NA else pubm$pval[2]))
  ggplot(es, aes(x = yi, y = sqrt(vi))) + geom_point() + scale_y_reverse() +
    labs(x = "Logit prevalence", y = "Standard error", title = "Primary outcome: logit prevalence vs standard error") +
    theme_minimal()
  ggsave(file.path(fig_dir, "bias_logit_vs_se.png"), width = 6, height = 4.5, dpi = 300, bg = "white")
}

grade_one <- function(d, label, r, yi, vi, measure) {
  m <- rma(yi, vi, method = "REML")
  w <- weights(m) / 100
  j <- samples[match(d$sample_id, samples$sample_id), ]
  no <- function(x) !is.na(x) & x == "no"
  reg <- if (measure == "prevalence" && nrow(d) >= 10) {
    tryCatch(rma(yi, vi, mods = ~ I(1 / sqrt(d$n_n)), method = "REML", test = "knha"), error = function(e) NULL)
  } else NULL
  ctry <- j$country[!grepl("^MULTI", toupper(j$country)) & !grepl("^NR", j$country) & j$country != ""]
  tibble(outcome = label, measure = measure, k = nrow(d),
         participants = if (measure == "prevalence") sum(d$n_n) else sum(d$m_n + d$f_n),
         estimate = if (measure == "prevalence") r$prev else r$OR, ci.lb = r$ci.lb, ci.ub = r$ci.ub,
         pi.lb = r$pi.lb, pi.ub = r$pi.ub,
         weight_jbi2_no = sum(w[no(j$jbi_2)]), weight_jbi6_no = sum(w[no(j$jbi_6)]), weight_jbi9_no = sum(w[no(j$jbi_9)]),
         weight_any_no = sum(w[no(j$jbi_2) | no(j$jbi_6) | no(j$jbi_9)]),
         countries = length(unique(ctry)), regions = length(unique(na.omit(j$region[j$region != ""]))),
         small_study_p = if (is.null(reg)) NA_real_ else reg$pval[2])
}
grade_rows <- list()
plo <- function(d) escalc(measure = "PLO", xi = d$cases_n, ni = d$n_n)
if (nrow(prim) >= MIN_K) {
  e <- plo(prim)
  grade_rows$primary <- grade_one(prim, "Problem gambling (L3/L4), all samples", results$primary, e$yi, e$vi, "prevalence")
  rs <- prim |> filter(stype == "bettors in representative surveys")
  if (nrow(rs) >= MIN_K) {
    e <- plo(rs)
    grade_rows$rep <- grade_one(rs, "Problem gambling (L3/L4), bettors in representative surveys",
                                results[["stype bettors in representative surveys"]], e$yi, e$vi, "prevalence")
  }
}
for (lv in c("L2", "L1")) {
  if (!is.null(level_data[[lv]]) && nrow(level_data[[lv]]) >= MIN_K) {
    e <- plo(level_data[[lv]])
    grade_rows[[lv]] <- grade_one(level_data[[lv]], paste0(if (lv == "L2") "Moderate risk or higher" else "Any risk",
                                                           " (", lv, "), all samples"),
                                  results[[paste0("level_", lv)]], e$yi, e$vi, "prevalence")
  }
}
if (!is.null(sex_result)) {
  e <- escalc(measure = "OR", ai = sex$m_cases, n1i = sex$m_n, ci = sex$f_cases, n2i = sex$f_n)
  grade_rows$sex <- grade_one(sex, "Male-to-female odds ratio at the primary level", sex_result, e$yi, e$vi, "odds ratio")
}
grade <- if (length(grade_rows)) bind_rows(grade_rows) else NULL

# ---------------------------------------------------------------------------------------------------------------
# Descriptives, figures and tables
# ---------------------------------------------------------------------------------------------------------------

inc <- samples |> filter(!sample_id %in% NOT_BETTORS)
desc <- bind_rows(
  inc |> count(variable = "sample type", value = stype),
  inc |> count(variable = "region", value = region),
  inc |> count(variable = "age group", value = agegrp),
  inc |> count(variable = "sampling", value = sampling),
  inc |> count(variable = "betting mode", value = betting_mode),
  inc |> count(variable = "publication status", value = pub_status),
  inc |> count(variable = "country", value = country))
write_csv(desc, file.path(res_dir, "descriptives.csv"))

if (nrow(prim) > 0) {
  cp <- function(x, n) cbind(ifelse(x == 0, 0, qbeta(0.025, x, n - x + 1)), ifelse(x == n, 1, qbeta(0.975, x + 1, n - x)))
  ci <- cp(prim$cases_n, prim$n_n)
  st_order <- c("bettors in representative surveys", "bettors in other gambler surveys", "bettors recruited as such",
                "students, pupils and other")
  fd <- prim |>
    mutate(p = cases_n / n_n, lo = ci[, 1], hi = ci[, 2],
           author = ifelse(first_author == toupper(first_author), tools::toTitleCase(tolower(first_author)), first_author),
           ay = paste(author, year)) |>
    group_by(ay) |> mutate(ay = if (n() > 1) paste0(ay, letters[seq_len(n())]) else ay) |> ungroup() |>
    mutate(lab = paste0(ay, " (", instrument, ", ", level, ", n = ", n_n, ")"), pooled = FALSE)
  pooled_rows <- bind_rows(lapply(split(fd, fd$stype), function(d) {
    r <- pool_glmm(d, "")
    tibble(stype = d$stype[1], p = r$prev, lo = r$ci.lb, hi = r$ci.ub, lab = sprintf("Pooled, k = %d", r$k), pooled = TRUE)
  })) |> filter(!is.na(p))
  fd <- bind_rows(fd, pooled_rows) |>
    mutate(stype = factor(stype, levels = st_order, labels = paste0(toupper(substr(st_order, 1, 1)), substring(st_order, 2))),
           id = paste(stype, lab)) |>
    arrange(stype, desc(pooled), desc(p))
  fd$id <- factor(fd$id, levels = unique(fd$id))
  ggplot(fd, aes(x = p, y = id)) +
    geom_errorbar(aes(xmin = lo, xmax = hi), width = 0.25, orientation = "y", linewidth = 0.3) +
    geom_point(aes(shape = pooled, size = pooled)) +
    scale_shape_manual(values = c(`FALSE` = 16, `TRUE` = 18), guide = "none") +
    scale_size_manual(values = c(`FALSE` = 1.2, `TRUE` = 3), guide = "none") +
    scale_y_discrete(labels = setNames(fd$lab, fd$id)) +
    facet_grid(stype ~ ., scales = "free_y", space = "free_y", labeller = label_wrap_gen(width = 16)) +
    geom_vline(xintercept = results$primary$prev, linetype = "dashed", linewidth = 0.3) +
    scale_x_continuous(labels = scales::percent, breaks = seq(0, 1, 0.1)) +
    labs(x = "Prevalence of problem gambling (95% CI)", y = NULL) +
    theme_minimal(base_size = 7.5) +
    theme(strip.text.y = element_text(angle = 0, hjust = 0), panel.grid.minor = element_blank(),
          panel.spacing = unit(0.6, "lines"))
  h <- max(4, 0.15 * nrow(fd) + 1.2)
  ggsave(file.path(fig_dir, "forest_primary.png"), width = 7, height = h, dpi = 300, bg = "white")
  ggsave(file.path(fig_dir, "forest_primary.pdf"), width = 7, height = h)
}
emap <- lev |> filter(whole == "yes", !sample_id %in% NOT_BETTORS) |> distinct(sample_id, instrument, level) |>
  count(instrument, level)
if (nrow(emap) > 0) {
  ggplot(emap, aes(x = level, y = instrument, fill = n)) + geom_tile() + geom_text(aes(label = n), size = 3) +
    scale_fill_gradient(low = "grey90", high = "grey40") +
    labs(x = "Case-definition level", y = NULL, title = "Evidence map: samples with a whole-sample estimate") +
    theme_minimal()
  ggsave(file.path(fig_dir, "evidence_map.png"), width = 6, height = 4.5, dpi = 300, bg = "white")
}

# Estimates that enter no pooled analysis: no counts, not levelled, distribution-based, or not sports bettors.
ests <- read_csv(file.path(paper, "forms", "estimates.csv"), col_types = cols(.default = "c"), na = character())
used <- unique(unlist(strsplit(c(prim$estimate_ids, unlist(lapply(level_data, function(d) d$estimate_ids))), "\\+")))
listed <- ests |>
  mutate(reason = case_when(
    sample_id %in% NOT_BETTORS ~ "denominator includes non-bettors (D8)",
    is.na(num(cases)) | is.na(num(n)) ~ "counts not reported (only percentages)",
    level %in% c("not_levelled", "E3", "NR") ~ paste("level", level),
    TRUE ~ NA_character_)) |>
  filter(!is.na(reason)) |>
  select(estimate_id, sample_id, subgroup, instrument, threshold, level, cases, n, reason, notes)

# ---------------------------------------------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------------------------------------------

write_csv(bind_rows(results), file.path(res_dir, "pooled.csv"))
write_csv(bench, file.path(res_dir, "benchmark_tran.csv"))
write_csv(bind_rows(sens), file.path(res_dir, "sensitivity.csv"))
write_csv(bind_rows(logs), file.path(res_dir, "selection_log.csv"))
write_csv(sub_tests, file.path(res_dir, "subgroup_tests.csv"))
write_csv(listed, file.path(res_dir, "listed_not_pooled.csv"))
write_csv(within, file.path(res_dir, "within_study_contrasts.csv"))
if (!is.null(loo)) write_csv(loo, file.path(res_dir, "leave_one_out.csv"))
if (!is.null(infl)) write_csv(infl, file.path(res_dir, "influence.csv"))
if (nrow(sex) > 0) write_csv(sex, file.path(res_dir, "sex_data.csv"))
if (!is.null(sex_result)) write_csv(sex_result, file.path(res_dir, "sex_or.csv"))
if (!is.null(bias)) write_csv(bias, file.path(res_dir, "meta_bias.csv"))
if (!is.null(grade)) write_csv(grade, file.path(res_dir, "grade_inputs.csv"))
if (!is.null(multilevel$prespecified)) {
  cf <- summary(multilevel$prespecified)$coefficients
  write_csv(tibble(term = rownames(cf), log_or = cf[, 1], se = cf[, 2], OR = exp(cf[, 1]),
                   ci.lb = exp(cf[, 1] - 1.96 * cf[, 2]), ci.ub = exp(cf[, 1] + 1.96 * cf[, 2]), p = cf[, 4]),
            file.path(res_dir, "multilevel_prespecified.csv"))
}
if (!is.null(multilevel$robust)) write_csv(as_tibble(multilevel$robust), file.path(res_dir, "multilevel_robust.csv"))
if (!is.null(multilevel$variance_explained)) write_csv(multilevel$variance_explained, file.path(res_dir, "variance_explained.csv"))
if (!is.null(multilevel$exploratory)) write_csv(multilevel$exploratory, file.path(res_dir, "moderators_exploratory.csv"))
if (!is.null(multilevel$exploratory_coefs)) write_csv(multilevel$exploratory_coefs, file.path(res_dir, "moderators_exploratory_coefs.csv"))
sink(file.path(res_dir, "multilevel.txt"))
for (nm in names(multilevel)) {
  cat("\n=====", nm, "=====\n")
  print(if (inherits(multilevel[[nm]], "merMod")) summary(multilevel[[nm]]) else multilevel[[nm]])
}
sink()
writeLines(capture.output(sessionInfo()), file.path(paper, "analysis", "sessionInfo.txt"))

fmt <- function(x) ifelse(is.na(x), "NA", sprintf("%.1f%%", 100 * x))
for (nm in c("primary", "level_L1", "level_L2", "level_L3", "stype bettors in representative surveys")) {
  r <- results[[nm]]
  cat(sprintf("%-45s k = %2d  %s (95%% CI %s-%s; PI %s-%s)\n", r$analysis, r$k, fmt(r$prev), fmt(r$ci.lb), fmt(r$ci.ub),
              fmt(r$pi.lb), fmt(r$pi.ub)))
}
cat("Results in", res_dir, "\n")
