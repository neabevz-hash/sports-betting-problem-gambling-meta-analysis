# PRISMA 2020 flow diagram (identification of new studies via databases, registers and other sources).
#
# Reads fulltext/prisma_counts.json (search -> screening -> full texts), forms/samples.csv (studies and samples in the
# review) and analysis/results/selection_log.csv (samples in the pooled analyses); writes analysis/figures/prisma.png
# and prisma.pdf. Template: papers/misophonia-prevalence/analysis/prisma.R.
# Run from the repository root: Rscript papers/sports-betting-prevalence/analysis/prisma.R

suppressPackageStartupMessages({
  library(ggplot2)
  library(jsonlite)
})

paper <- "papers/sports-betting-prevalence"
pc <- fromJSON(file.path(paper, "fulltext", "prisma_counts.json"))
fig_dir <- file.path(paper, "analysis", "figures")
fmt <- function(x) prettyNum(x, big.mark = ",")

src_names <- c(pubmed = "PubMed", europepmc = "Europe PMC", openalex = "OpenAlex",
               openalex_non_en = "OpenAlex, non-English queries", s2 = "Semantic Scholar", crossref = "Crossref",
               citations = "Citation search of Tran et al. (2024)", datacite = "DataCite", openaire = "OpenAIRE")
by_src <- pc$records_per_source
src_txt <- paste(sprintf("%s (n = %s)", src_names[names(by_src)], fmt(unlist(by_src))), collapse = "\n")
excl <- unlist(pc$reports_excluded_full_text)
excl_names <- c(E4_no_pg_instrument = "No problem-gambling instrument",
                E2_no_sports_bettor_estimate = "No estimate for sports bettors",
                E5_design = "Design (review, commentary, policy,\nqualitative)",
                no_extractable_counts = "No count or proportion with n",
                E1_selected_sample = "Recruited for gambling problems",
                E6_duplicate = "Duplicate report of a sample",
                E7_operator_data_only = "Operator account data only",
                E3_distribution_cutoff = "Cut-off from the sample's distribution",
                other = "Other")
excl <- excl[order(-excl)]
excl_txt <- paste(sprintf("%s (n = %s)", excl_names[names(excl)], fmt(excl)), collapse = "\n")

s <- read.csv(file.path(paper, "forms", "samples.csv"), colClasses = "character")
sel <- read.csv(file.path(paper, "analysis", "results", "selection_log.csv"), colClasses = "character")
pooled <- unique(sel$sample_id[!startsWith(sel$analysis, "post hoc")])
studies_txt <- sprintf(paste0("Studies included in review (n = %d)\nReports of included studies (n = %d)\n",
                              "Independent samples of sports bettors (n = %d)\n",
                              "Samples in the meta-analyses (n = %d)"),
                       length(unique(s$study_id)), pc$reports_included, nrow(s) - 3, length(pooled))

boxes <- data.frame(
  x = c(1, 3, 1, 3, 1, 3, 1, 3, 1),
  y = c(9, 9, 7, 7, 5, 5, 3, 3, 1),
  w = 1.9,
  h = c(1.9, 1.1, 0.7, 0.7, 0.7, 0.9, 0.7, 1.7, 1.0),
  label = c(
    paste0("Records identified (n = ", fmt(pc$records_identified), "):\n", src_txt),
    paste0("Records removed before screening:\nDuplicate records (n = ", fmt(pc$duplicates_removed),
           ")\nRemoved by automation tools (n = ", fmt(pc$removed_by_automation), "):\nnon-study records and commercial deposits"),
    paste0("Records screened\n(n = ", fmt(pc$records_screened_title_abstract), ")"),
    paste0("Records excluded\n(n = ", fmt(pc$records_excluded_title_abstract), ")"),
    paste0("Reports sought for retrieval\n(n = ", fmt(pc$reports_sought_for_retrieval), ")"),
    paste0("Reports not retrieved (n = ", fmt(pc$reports_not_retrieved), "):\nno open-access full text (n = ",
           fmt(pc$reports_not_retrieved_detail$no_open_access_copy_or_blocked), ")\nretrieved file was another work (n = ",
           fmt(pc$reports_not_retrieved_detail$retrieved_file_did_not_contain_the_report), ")"),
    paste0("Reports assessed for eligibility\n(n = ", fmt(pc$reports_assessed_for_eligibility), ")"),
    paste0("Reports excluded (n = ", fmt(sum(excl)), "):\n", excl_txt),
    studies_txt),
  stringsAsFactors = FALSE)
arrows <- data.frame(
  x = c(1, 1.95, 1, 1.95, 1, 1.95, 1, 1.95), y = c(9 - 0.95, 9, 7 - 0.35, 7, 5 - 0.35, 5, 3 - 0.35, 3),
  xend = c(1, 2.05, 1, 2.05, 1, 2.05, 1, 2.05), yend = c(7 + 0.35, 9, 5 + 0.35, 7, 3 + 0.35, 5, 1 + 0.5, 3))

p <- ggplot() +
  geom_rect(data = boxes, aes(xmin = x - w / 2, xmax = x + w / 2, ymin = y - h / 2, ymax = y + h / 2),
            fill = "white", colour = "black", linewidth = 0.3) +
  geom_text(data = boxes, aes(x = x, y = y, label = label), size = 2.3, lineheight = 0.95) +
  geom_segment(data = arrows, aes(x = x, y = y, xend = xend, yend = yend),
               arrow = arrow(length = unit(0.12, "cm"), type = "closed"), linewidth = 0.3) +
  annotate("text", x = -0.25, y = c(9, 6, 1), label = c("Identification", "Screening", "Included"),
           angle = 90, size = 2.8, fontface = "bold") +
  annotate("text", x = 2, y = 10.35, label = "Databases, search engines and citation search", size = 2.8,
           fontface = "bold") +
  coord_cartesian(xlim = c(-0.4, 4), ylim = c(0.3, 10.5)) +
  theme_void()
ggsave(file.path(fig_dir, "prisma.png"), p, width = 6.5, height = 7.5, dpi = 300, bg = "white")
ggsave(file.path(fig_dir, "prisma.pdf"), p, width = 6.5, height = 7.5)
cat("PRISMA diagram written to", fig_dir, "\n")
