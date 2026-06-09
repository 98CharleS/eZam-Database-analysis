# eZamDB: Analysis & Visualization

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Pandas](https://img.shields.io/badge/library-pandas-green.svg)
![Plotly](https://img.shields.io/badge/library-plotly-purple.svg)
![Tableau](https://img.shields.io/badge/tool-Tableau-orange.svg)
![Status](https://img.shields.io/badge/status-in%20progress-yellow.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 📌 Project Overview

This repository is the **third and final stage** of the **eZamówienia data pipeline**. It takes the clean, aggregated tender data produced by [`eZam-Database-formating`](https://github.com/98CharleS/eZam-Database-formating) and turns it into insights — statistical analysis, interactive charts, and Tableau dashboards.

The dataset covers **517,840 tender notices** published on Poland's public procurement platform between **2021 and 2025** (data import was configured from 2020, but the earliest available notice dates from 2 January 2021 — see the report for details). The analysis explores how tenders are distributed across CPV categories, Polish voivodeships, and time, and how tender volume correlates with regional GDP and population.

> **Part of a larger project:**
> [`eZam-Database-extraction`](https://github.com/98CharleS/eZam-Database-extraction) → [`eZam-Database-formating`](https://github.com/98CharleS/eZam-Database-formating) → **`eZam-Database-analysis`** *(Work in Progress)*

📄 **Read the full research report: [Polish](report.md) · [English](report_en.md)**

---

## 🛠️ Technical Stack

- **Language:** Python
- **Data Processing:** `pandas`, `numpy`
- **Statistics & time series:** `statsmodels` (STL decomposition, trend/seasonality strength)
- **Visualization:** `plotly` (interactive HTML), `matplotlib` (static PNG charts), **Tableau** (`.twb` dashboards)
- **Input format:** CSV (`;`-delimited, from the formatting stage)

---

## 📁 Repository Structure

```
eZam-Database-analysis/
│
├── data/                                  # Aggregated CSVs from the formatting stage
│   ├── tenders_by_cpv.csv                 # Tender count per primary CPV code
│   ├── tenders_by_cpv_division.csv        # Tender count per CPV division (45 divisions)
│   ├── tenders_by_day.csv                 # Daily tender counts (for seasonality)
│   ├── tenders_by_gdp.csv                 # Tenders enriched with regional GDP
│   ├── tenders_by_gdp_per_capita.csv      # Tenders enriched with GDP per capita
│   ├── tenders_by_population.csv          # Tenders enriched with population
│   ├── tenders_by_population_warsaw_split.csv  # Population enrichment, Warsaw split out
│   ├── tenders_by_province.csv            # Tender count per voivodeship
│   ├── tenders_by_province_and_division.csv    # Province × CPV division
│   ├── tenders_by_month_and_division.csv  # Month × CPV division (for per-division seasonality)
│   ├── top10_cpv_per_year.csv             # Top 10 CPV codes per year (2021–2025)
│   ├── top5_cpv_by_province.csv           # Top 5 CPV codes per province (all years)
│   ├── top5_cpv_per_province_total.csv    # Top 5 CPV codes per province, ranked
│   └── top5_cpv_by_provinces_in_years/    # Top 5 CPV per province, split by year
│       └── top5_cpv_by_province_2021.csv … 2025.csv
│
├── output/
│   ├── tenders_correlation.html           # Interactive correlation charts (from analyst.py)
│   ├── seasonality.*                       # Whole-dataset seasonality (PNG/HTML + monthly index CSV)
│   └── seasonality_by_division.*           # Per-division seasonality (PNG/HTML + CSV)
│
├── analyst.py                             # Correlation analysis → Plotly HTML
├── seasonality.py                         # Whole-dataset seasonality (STL, indices) → PNG/HTML/CSV
├── seasonality_by_division.py             # Per-division seasonality (STL Fs, indices) → PNG/HTML/CSV
├── index.html                             # Redirect to the generated chart
├── Dashboards*.twb                        # Tableau dashboards (CPV, divisions, seasonality)
├── report.md                              # Full analytical report (Polish)
├── report_en.md                           # Full analytical report (English)
├── requirements.txt                       # Python dependencies
└── README.md
```

---

## 📊 What's Inside

### `analyst.py` — Correlation Analysis
Generates a 5-panel interactive Plotly figure ([`output/tenders_correlation.html`](output/tenders_correlation.html)) exploring how tender volume relates to regional economic factors. Each panel fits a linear trend line and reports the Pearson coefficient (`r`) and coefficient of determination (`R²`):

| Panel | Relationship |
|---|---|
| 1 | Tenders vs **GDP** (`r = 0.974`) |
| 2 | Tenders vs **Population** (`r = 0.953`) |
| 3 | Tenders vs Population, **Warsaw split out** (`r = 0.874`) |
| 4 | GDP vs Population (`r = 0.951`) |
| 5 | Tenders vs **GDP per capita** (`r = 0.880`) |

**Key finding:** absolute regional GDP is the strongest single predictor of tender activity — economically stronger regions generate disproportionately more tenders, with Warsaw standing out as a clear outlier.

### `seasonality.py` & `seasonality_by_division.py` — Seasonality Analysis
Two scripts characterising the temporal structure of tender publication using **STL decomposition** and the trend/seasonality strength measures (`Ft`, `Fs`) of Wang, Smith & Hyndman:
- **`seasonality.py`** — whole-dataset seasonality: monthly and weekly seasonal indices, trend vs. seasonality strength. **Key finding:** volume is saturated and its variation is almost purely **seasonal** (`Fs=0.691`), peaking in November and troughing in January, concentrated on working days.
- **`seasonality_by_division.py`** — per-division seasonality across the 45 CPV divisions (limited to the 34 with ≥ 2,000 tenders). **Key finding:** cyclically contracted services (insurance, fuel, postal, food) peak in autumn, while one-off equipment/machinery supplies are effectively aseasonal.

Both write a static PNG (matplotlib) plus an interactive HTML (plotly) and a CSV of coefficients to `output/`.

### Tableau Dashboards (`*.twb`)
The `.twb` files contain the dashboards behind the visuals embedded in [`report.md`](report.md):
- CPV code distribution (5,047 codes, strongly right-skewed) and CPV division distribution (45 divisions)
- Top 5 CPV codes per voivodeship, broken down by year (2021–2025)
- Seasonality of tender publication over time

### `report.md` / `report_en.md` — Research Report (Polish / English)
The full written analysis: abstract, data description, CPV / division distribution, regional top-5 breakdowns, time trend and seasonality (both overall and per CPV division), and correlation against GDP and population, ending with a summary and conclusions. [`report_en.md`](report_en.md) is the English translation of [`report.md`](report.md).

---

## 🚀 Usage

### Prerequisites
```bash
pip install -r requirements.txt
```

### Run the correlation analysis
```bash
python analyst.py
```
This writes `output/tenders_correlation.html` and opens the interactive figure in your browser. Opening `index.html` redirects to the same output.

### Run the seasonality analyses
```bash
python seasonality.py              # whole-dataset seasonality  → output/seasonality.*
python seasonality_by_division.py  # per-division seasonality   → output/seasonality_by_division.*
```
Each script writes a static PNG, an interactive HTML, and a CSV of computed coefficients to `output/`.

### Tableau dashboards
Open any `Dashboards*.twb` file in [Tableau Desktop](https://www.tableau.com/products/desktop) (or Tableau Public). The workbooks read their extracts from the CSVs in `data/`.

---

## 🗺️ Data Source

Tender data originates from **[eZamówienia](https://ezamowienia.gov.pl)** — the official Polish public procurement platform — extracted and cleaned in the earlier pipeline stages. Regional reference data (GDP, population) is sourced from **GUS** (Główny Urząd Statystyczny / Central Statistical Office of Poland).

---

## 🔗 Related Repositories

| Repository | Description |
|---|---|
| [eZam-Database-extraction](https://github.com/98CharleS/eZam-Database-extraction) | Stage 1 — API extraction to CSV |
| [eZam-Database-formating](https://github.com/98CharleS/eZam-Database-formating) | Stage 2 — CSV → SQLite, cleaning & aggregations |
| *(this repo)* | Stage 3 — Analysis, Plotly charts & Tableau dashboards |

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
