# Table of Contents
- [Abstract](#abstract)
- [Input Data](#input-data)
- [Overview and Analysis of the Obtained Data](#overview-and-analysis-of-the-obtained-data)
- [Analysis of Tender Distribution](#analysis-of-tender-distribution)
  - [Introduction](#introduction)
  - [Distribution of CPV Codes](#distribution-of-cpv-codes)
  - [Distribution of Tender Divisions](#distribution-of-tender-divisions)
  - [Differences Between Voivodeships](#differences-between-voivodeships)
    - [Most Common Codes by Voivodeship](#most-common-codes-by-voivodeship)
    - [Deviation Between Voivodeships](#deviation-between-voivodeships)
    - [2021](#2021)
    - [2022](#2022)
    - [2023](#2023)
    - [2024](#2024)
    - [2025](#2025)
    - [Legend](#legend)
    - [Summary](#summary)
- [Seasonality Analysis of Tender Distribution](#seasonality-analysis-of-tender-distribution)
  - [Trend and Seasonality Measures](#trend-and-seasonality-measures)
    - [Seasonality](#seasonality)
    - [Trend](#trend)
  - [Change in the Number of Tenders Over the Analyzed Period](#change-in-the-number-of-tenders-over-the-analyzed-period)
  - [Seasonality Analysis of CPV Divisions](#seasonality-analysis-of-cpv-divisions)
- [Analysis of Tender Distribution Against Other Factors](#analysis-of-tender-distribution-against-other-factors)
  - [Introduction](#introduction-1)
  - [Data Analysis](#data-analysis)
    - [Number of Tenders vs. Voivodeship GDP](#number-of-tenders-vs-voivodeship-gdp)
    - [Number of Tenders vs. Voivodeship Population](#number-of-tenders-vs-voivodeship-population)
    - [Number of Tenders vs. Voivodeship Population, Excluding Warsaw from the Masovian Voivodeship](#number-of-tenders-vs-voivodeship-population-excluding-warsaw-from-the-masovian-voivodeship)
    - [Population vs. GDP](#population-vs-gdp)
    - [Number of Tenders vs. GDP per Capita](#number-of-tenders-vs-gdp-per-capita)
- [Summary](#summary-1)
- [Conclusions](#conclusions)

# Abstract
This study presents an analysis of **517,840** below-EU-threshold public procurement notices published on the **eZamówienia (BZP)** platform between **2021 and 2025**. The aim of the study is a quantitative characterisation of the Polish public procurement market across three dimensions — **thematic** (distribution by CPV codes and divisions), **spatial** (variation across voivodeships), and **temporal** (trend and seasonality) — as well as an examination of the relationship between procurement activity and regional economic factors (GDP and population). The analysis is based on the main CPV code of each notice, aggregated into **45 divisions** consistent with Commission Regulation (EC) No 213/2008. The methods employed include descriptive statistics, the Total Variation Distance (TVD) for comparing the thematic structure of voivodeships, STL decomposition together with trend- and seasonality-strength measures (`Fs`, `Ft`) and seasonal indices, as well as linear regression and the Pearson correlation coefficient for the economic relationships.

The results show that the distribution of tenders is strongly **right-skewed** and dominated by construction works (code **45000000-7** — 11.38% of tenders; division **45** — 32.25%). The thematic structure of procurement is highly **homogeneous** nationwide (inter-voivodeship deviations in the range of 4.0–9.2%). After the platform's roll-out period in 2021, the overall number of tenders **stabilised** (the trend model explains only about 6% of the variance over the stable 2022–2025 period), and its fluctuations are almost exclusively **seasonal** (`Fs=0.691`) — peaking in November, troughing in January, with a marked concentration of publications on working days; the seasonality of individual divisions, in turn, reflects service-contracting cycles. The number of tenders is **strongly correlated with voivodeship GDP** (`r=0.974`), with the city of Warsaw constituting a clear outlier exhibiting above-average procurement activity per capita. At the same time, the market displays high **reactivity to external systemic impulses** — central programmes, EU funding, and the geopolitical context.

# Input Data
The analysis was conducted on data downloaded from the [eZamówienia BZP](https://ezamowienia.gov.pl/mo-client-board/bzp) portal via its API ([eZam-Database-extraction](https://github.com/98CharleS/eZam-Database-extraction)), which were subsequently formatted and processed ([eZam-Database-formating](https://github.com/98CharleS/eZam-Database-formating)) in order to achieve standardisation, readability, and compatibility with other software.
Data import was configured to begin on **1 January 2020**; however, the earliest available notice dates from **2 January 2021**. This is because the eZamówienia portal in its current form has been operating only since **1 January 2021**, following the entry into force of the amended **Public Procurement Law**, and does not contain earlier proceedings. The actual temporal scope of the dataset therefore covers tenders from the period **2 January 2021 – 31 December 2025**, and the dataset itself comprises **517,840** records.

# Overview and Analysis of the Obtained Data
Among the available attributes, `TenderType` and `procedureResult` contained NULL values throughout. These are attributes that remain unused in the database. In addition, all tenders within the analysed scope shared the same value `True` in the `isTenderAmountBelowEU` column. This attribute indicates whether the tender value was below the **[EU threshold](https://www.gov.pl/web/uzp/aktualne-progi-unijne-oraz-ich-rownowartosci-w-zlotych-na-lata-2026-2027)**. The uniform `True` values mean that all tenders in the analysed dataset were below the **EU threshold**. To improve readability and data integrity, the aforementioned columns were dropped.

# Analysis of Tender Distribution
## Introduction
The downloaded data contained numerous CPV codes in the `cpvCode` column. This results from the structural characteristics of tender notices, in which there is one main CPV code, possibly followed by many additional CPV codes whose relevance to the overall subject of the tender may vary.
Because it is impossible to assess the significance of an additional CPV code for the tender as a whole, and because a varying number of additional codes would distort the frequency statistics relative to the number of tenders, only the main CPV code available in the attributes of each entry was analysed. This approach ensures standardisation, consistency, and readability of the results.

## Distribution of CPV Codes

<img width="2117" height="1314" alt="image" src="https://github.com/user-attachments/assets/4655b18d-7fd7-4c8f-9918-7c6096da2900" />

The analysed database contains **5,047** CPV codes. A very large disproportion is evident between the numbers of tenders falling under individual CPV codes. **51.79%** of all CPV codes appeared **fewer than 10 times** in the database, as many as **87.18%** appeared **fewer than 100 times**, and as many as **98.18%** of the set appeared **fewer than 1,000 times**.
All CPV codes accounting for 1% or more of the set are presented in the table below:

| CPV Code | Name | Tender Count | Share % |
|---------|-------|-------------------|----------|
| **45000000-7** | Construction works | 58,906 | **11.38%** |
| 45200000-8 | Road works | 9,423 | 1.82% |
| 45231000-6 | Road construction works | 9,148 | 1.77% |
| 71200000-3 | Engineering design services | 8,356 | 1.61% |
| 79700000-3 | Security services | 6,220 | 1.20% |
| 45300000-9 | Repair and renovation works | 5,944 | 1.15% |
| 45243000-0 | Road surface works | 5,160 | 1.00% |

The most common CPV code — "**45000000-7 Construction works**" — appeared as the main CPV code in **58,906** tenders, accounting for **11.38%** of all tenders in the set. The next most common code, **45200000-8 Road works**, appeared in **9,423** tenders, a figure more than **6 times smaller**. The differences between the numbers of tenders for individual CPV codes diminish as the number of tenders decreases.
Such a data distribution indicates that the set is characterised by a strongly right-skewed distribution with a long tail.

## Distribution of Tender Divisions

**CPV codes** provide a precise representation of a tender's subject matter, but owing to their specificity they are very numerous and divide all tenders into narrow ranges that are difficult to present visually and to generalise. For simplification, the **CPV codes were aggregated into 45 divisions** covering a broader scope. The divisions were adopted in accordance with the applicable classification set out in [Commission Regulation (EC) No 213/2008 of 28 November 2007](https://eur-lex.europa.eu/legal-content/PL/TXT/?uri=CELEX:32008R0213).

<img width="2114" height="1306" alt="image" src="https://github.com/user-attachments/assets/ea3247d3-7a2c-4988-bc0a-b1541c2fec86" />

The 10 largest divisions are presented in the table below:

| Division | Name | Tender Count | Share % |
|-----|-------|-------------------|----------|
| **45** | Construction works | 167,010 | **32.25%** |
| 33 | Medical and pharmaceutical equipment | 39,843 | 7.69% |
| 71 | Architectural and engineering services | 31,379 | 6.06% |
| 90 | Environmental and sanitation services | 23,543 | 4.55% |
| 15 | Food products and beverages | 22,319 | 4.31% |
| 9 | Petroleum products, fuel and energy | 20,268 | 3.91% |
| 34 | Transport equipment and vehicles | 19,757 | 3.82% |
| 30 | Computer and office equipment | 19,462 | 3.76% |
| 79 | Business and consulting services | 15,855 | 3.06% |
| 39 | Furniture and furnishings | 14,948 | 2.89% |

The largest number of tenders concerned the **Construction works** division, which accounted for **32.25%** of all tenders and constituted the clear leader of the ranking. This confirms the observations from the previous analysis, in which **CPV codes** related to construction works also dominated in terms of frequency. A significant disproportion appeared between first and second place — the next division, **Medical and pharmaceutical equipment**, accounted for **7.69%** of tenders, meaning it was **4.19 times less numerous than the leader**. This difference, although considerable, is markedly smaller than the analogous disproportion observed at the level of individual **CPV codes**, where the leader exceeded its successor more than sixfold.
Subsequent positions in the ranking were occupied by the divisions: **Architectural and engineering services (6.06%), Environmental and sanitation services (4.55%)**, and **Food products and beverages (4.31%)**. The differences between successive divisions in this part of the ranking are already much smaller and gradually diminish as the number of tenders decreases. The divisions in positions 6 to 10 — **Petroleum products, fuel and energy; Transport equipment and vehicles; Computer and office equipment; Business and consulting services; and Furniture and furnishings** — accounted for between **3.91% and 2.89%** of tenders respectively, forming a relatively compact group with similar shares.
The phenomenon of lower stratification results from the natural effect of aggregation — grouping CPV codes into divisions smooths out the extreme differences visible at a more detailed level of classification. The distribution of these data also exhibits a strongly right-skewed character with a long tail, meaning that the vast majority of tenders are concentrated in a few divisions, while the remaining categories — including **Petroleum industry services**, with only 18 tenders — constitute a marginal share of the set.

The further analysis will employ a breakdown by both **divisions and CPV codes**, depending on the level of detail appropriate to the particular issue being analysed.

## Differences Between Voivodeships

### Most Common Codes by Voivodeship

<img width="1106" height="724" alt="image" src="https://github.com/user-attachments/assets/0305f33c-e0e2-46fe-ac50-f6f182213e22" />
<img width="809" height="424" alt="image" src="https://github.com/user-attachments/assets/239a2ee7-1d66-4157-a0f3-75dfe94cad87" />

In all voivodeships, the most numerous **CPV code** was **Construction works**, which accounted for between 51.5% and as much as 69.9% of all tenders within the group of the 5 most numerous codes and gathered a total of 58,906 tenders.
The next most numerous is the **CPV code Road construction**, which appeared in positions 2 to 5 in 11 of the 16 voivodeships, gathering a total of 7,427 tenders. Immediately behind it was the code **Road works**, which likewise appeared in 11 voivodeships in positions 2 to 5 and gathered 7,403 tenders. A similar, though slightly smaller, result is observed for the **CPV code Design services**. It gathered 7,034 tenders and likewise appeared in 11 voivodeships in positions 2 to 5.

### Deviation Between Voivodeships
To quantitatively compare the thematic structure of procurement across voivodeships, for each of them the share of each of the **45 divisions** in its total number of tenders was calculated and then compared with the **national** structure. As a measure of divergence, the **Total Variation Distance** (TVD = ½·Σ|share_voiv − share_nat|) was adopted, which takes values from 0% to 100% and expresses the proportion of a given voivodeship's tenders that would have to be reassigned to other divisions for its structure to be identical to the national one. The higher the value, the more the voivodeship's procurement profile deviates from the average.

| Voivodeship | Deviation (TVD) | Tender Count |
|-------------|:----------------:|------------------:|
| **Lubusz** | **9.2%** | 12,681 |
| **Kuyavian-Pomeranian** | **9.1%** | 26,891 |
| Greater Poland | 8.0% | 41,803 |
| Masovian | 7.9% | 91,898 |
| Pomeranian | 7.8% | 29,471 |
| Subcarpathian | 7.4% | 29,010 |
| Podlaskie | 7.2% | 18,300 |
| Opole | 6.5% | 13,748 |
| Warmian-Masurian | 6.4% | 19,835 |
| Świętokrzyskie | 6.4% | 18,060 |
| West Pomeranian | 6.1% | 22,245 |
| Łódź | 6.0% | 30,341 |
| Lesser Poland | 5.9% | 47,809 |
| Lublin | 5.4% | 32,420 |
| Lower Silesian | 5.0% | 36,298 |
| **Silesian** | **4.0%** | 47,023 |

The deviations are **small** — they fall within the range of **4.0% to 9.2%** (mean **6.8%**, median **6.5%**), which means that the thematic structure of procurement is highly **homogeneous** nationwide. This results directly from the previously described dominance of division **45 (Construction works)**, whose share across all voivodeships remains similar — from **29.1%** (Pomeranian) to **37.5%** (Lubusz), against a national average of **32.3%**. No voivodeship therefore has a fundamentally different profile, and the differences concern only the proportions of the divisions in the further positions.

The largest deviations were recorded by **Lubusz** (9.2%) and **Kuyavian-Pomeranian** (9.1%). In the case of **Lubusz**, this results from an above-average share of construction works (37.5% versus 32.3% nationally, +5.3 pp) and of transport equipment, with a simultaneous under-representation of food products (2.5% versus 4.3%) and medical equipment. **Kuyavian-Pomeranian**, in turn, stands out for an unusually high share of financial and insurance services (div. 66: 4.1% versus 1.4%, +2.7 pp), medical and pharmaceutical equipment (div. 33: 10.3% versus 7.7%), and health services — pointing to a stronger-than-average presence of contracting authorities from the healthcare sector and financial institutions.

**Masovian** (7.9%) warrants separate comment, as its deviation is distinctly **metropolitan** in nature: an above-average share of business and consulting services (div. 79: 5.2% versus 3.1%, +2.2 pp), IT services (div. 72), and software packages (div. 48), alongside the lowest share of construction works in this group (30.1%). This profile reflects the concentration of central institutions and the service sector in the Warsaw agglomeration.

At the opposite pole is **Silesian** (4.0%) — a voivodeship with a structure closest to the national average, with only a slightly elevated share of food products (6.2% versus 4.3%). **Lower Silesian** (5.0%) and **Lublin** (5.4%) likewise represent a typical profile. It is worth noting that the deviation is not related to the size of the voivodeship — the large **Masovian** (91,898 tenders) deviates from the average more strongly than the much smaller **Świętokrzyskie** (18,060), which is determined not by scale but by the local economic and institutional specificity of the contracting authorities.

### 2021

<img width="1219" height="726" alt="image" src="https://github.com/user-attachments/assets/59ba843c-bdc2-478a-b9ba-7d75d787e63e" />

The year 2021 constituted the first full edition of the procurement system operating under the regime of the amended Public Procurement Law, in force since 1 January 2021. The procurement structure was dominated by CPV code **45000000-7** (**construction works**), with tender volumes varying spatially — from 1,168 proceedings in the **Masovian** voivodeship to 248 in **Podlaskie**. Further positions in the regional rankings were consolidated by the categories of road infrastructure (CPV **45233120-6**, **45233140-2**), engineering services (**71320000-7**), and the protection of persons and property (**79710000-4**). Distinct regional specificity manifested itself, among other things, in the dominance of training services in the **Lublin** voivodeship (CPV **80500000-9**, 103 proceedings) — which corresponds to the intensive co-financing of projects from the European Social Fund in that period — and in the presence of snow-clearing services in **Lesser Poland** (**90620000-9**, 134 proceedings), reflecting the region's geographical conditions.

### 2022

<img width="1214" height="724" alt="image" src="https://github.com/user-attachments/assets/f17f2ac6-1545-48f1-bde9-48d74f102082" />

The year 2022 brought a marked increase in the volume of tender proceedings across all analysed voivodeships. In **Masovian**, the number of construction tenders rose from 1,168 to 1,971; in **Lower Silesian** — from 684 to 1,053; and in **Silesian** — from 972 to 1,454. This increase can be interpreted as a cumulative effect of: the unblocking of investments suspended during the COVID-19 pandemic, the absorption of funds from the National Recovery Plan, and the time-shifted launch of the EU 2021–2027 financial perspective. A characteristic novelty of 2022 was the mass appearance of CPV code **30213100-6** (**portable computers**) in many voivodeships simultaneously — **Lower Silesian** (118), **Kuyavian-Pomeranian** (101), **Lubusz** (54), **Warmian-Masurian** (77), **West Pomeranian** (80), and **Greater Poland** (161). This phenomenon was almost certainly linked to a centrally coordinated programme for equipping schools with computer hardware. An increase in activity was also recorded in procurement for computer equipment (**30200000-1**) — among others in **Subcarpathian** (126) and **Podlaskie** (66).

### 2023

<img width="1213" height="725" alt="image" src="https://github.com/user-attachments/assets/e44a4f0d-3b9e-4684-b2c4-ebb24a2cd457" />

In 2023 there was a partial correction in volume following the peak of the previous year. In the **Masovian** voivodeship, the number of construction tenders fell slightly from 1,971 to 1,861, and in **Silesian** — from 1,454 to 1,148. At the same time, however, in the **Lublin** voivodeship a dynamic increase was observed in road categories (CPV **45233120-6**: up from 149 to 214; CPV **45233000-9**: up from 143 to 187), which may indicate a shift in investment priorities towards transport infrastructure on the country's eastern flank. The CPV code **33100000-1** (**medical devices**), appearing in the procurement structure in **Lower Silesian** (111) and **Kuyavian-Pomeranian** (69), points to the continued re-equipping of healthcare facilities, initiated in response to the pandemic. The category of security services (**79710000-4**) consolidated its position in the rankings of most voivodeships.

### 2024

<img width="1216" height="728" alt="image" src="https://github.com/user-attachments/assets/ce24d1ec-72be-494c-8f42-62f3fba05d9d" />

In 2024, tender volumes remained at levels comparable to the previous year, with a marked revival recorded in **Masovian** (a return to 1,979 construction proceedings) and **Łódź** (an increase from 809 to 951). An important signal of a qualitative change in the structure of demand was the dynamic growth in procurement for insurance services (CPV **66510000-8**) in the **Kuyavian-Pomeranian** voivodeship — from 146 to 212 — which may reflect a growing awareness of risk management in the public sector. In **Lesser Poland**, pharmaceutical products (CPV **33600000-6**, 187 proceedings) appeared in the top of the ranking for the first time, which fits into the systematic increase in the procurement activity of regional hospitals. Also worth noting is the marked presence of renovation works (CPV **45453000-7**) in the procurement structures of **Masovian** (292) and **Greater Poland** (159) — which may suggest that the hitherto emphasis on new investment is beginning to be complemented by the systematic maintenance of existing infrastructure.

### 2025

<img width="1211" height="724" alt="image" src="https://github.com/user-attachments/assets/7e84bcfe-b486-45f1-8f79-9d1b274c362d" />

The data for 2025 reveal two distinct qualitative tendencies. First, CPV code **31122000-7** (**generator sets**) appeared suddenly and in high volumes in the voivodeships: **Lublin** (109), **Podlaskie** (79), **Warmian-Masurian** (70), and **Łódź** (129). The geographical concentration of this demand — strong in the east and north-east of the country — points to a connection with the geopolitical context (direct proximity to Ukraine and Belarus) and with the implementation of programmes to strengthen infrastructural resilience. Second, the position of CPV **80000000-4** (**educational and training services**) recorded a significant increase in the voivodeships: **Lubusz** (138), **Silesian** (183), **Łódź** (146), and **Lublin** (110). This may indicate intensive absorption of funds from the European Social Fund Plus under the current financial perspective. Also noteworthy is the increase in the number of tenders for passenger cars (CPV **34110000-1**) in several voivodeships (**Kuyavian-Pomeranian**, **Lubusz**, **West Pomeranian**), which may reflect deferred decisions to renew public vehicle fleets after years of investment cuts.

### Legend

<img width="1036" height="675" alt="image" src="https://github.com/user-attachments/assets/f2af6d88-c725-4257-bf38-5a7f67df0322" />

### Summary

Throughout the entire analysed period, CPV code **45000000-7** held, without exception, first place in all voivodeships and in all years, and the share of this CPV position in the rankings was so predominant that it justifies treating it not as one of the procurement categories but as a constitutive feature of the Polish public procurement market. The absolute values were at the same time strongly correlated with the demographic and economic size of the regions: **Masovian** and **Silesian** consistently recorded volumes several times higher than those of voivodeships with smaller economic potential (**Lubusz**, **Opole**, **Świętokrzyskie**).

The systematic growth in the volume of tenders for engineering design services (CPV **71320000-7**) in the years 2021–2025 may be interpreted as a leading indicator of future construction investment — the design phase precedes implementation by one to several years. This observation suggests that the public procurement market in Poland does not yet show signs of saturation in the infrastructure segment.

The persistent differences in the composition of CPV positions between voivodeships reflect not only geographical conditions (snow clearing in **Lesser Poland** and **Subcarpathia**, road infrastructure in eastern Poland) but also the institutional structure of the contracting authorities — the concentration of clinical hospitals (pharmaceutical products and medical devices in **Lesser Poland** and **Silesian**), the presence of large educational institutions (training services in **Lublin** and **Łódź**), or the activity of metropolitan local governments (security and renovations in **Masovian**).

The data analysis indicates that the Polish public procurement structure is sensitive to external systemic impulses: purchases of ICT equipment for schools in 2022, the increased demand for generator sets in the geopolitical context in 2025, or the intensification of training services in connection with ESF+ absorption. This phenomenon attests to the high reactivity of the procurement market to decisions taken at the central or EU level, which may be regarded both as an adaptive feature of the system and as a sign of the limited strategic autonomy of regional contracting authorities.

# Seasonality Analysis of Tender Distribution
<img width="1261" height="721" alt="image" src="https://github.com/user-attachments/assets/b6bceb05-1fa1-423e-a48e-e63c494535c0" />

The seasonality decomposition and the monthly and weekly indices are presented in the chart below, generated by the [`seasonality.py`](seasonality.py) script. The trend and STL decomposition were computed over the full 2021–2025 range, while the seasonal indices were computed over the years 2022–2025 — the year 2021 constituted the set's ramp-up period (January 2021 ≈ 15 tenders/day versus 175–218 in subsequent years), which would understate the seasonal profile.

<img width="1400" alt="Seasonality analysis of tenders" src="output/seasonality.png" />

## Trend and Seasonality Measures
The characteristics of the time series were described using an STL decomposition of monthly tender volumes and measures of trend and seasonality strength (Wang, Smith, Hyndman), taking values in the range from 0 to 1.

### Seasonality
The seasonality-strength coefficient `Fs=0.691` indicates strong, regular seasonality — more than **69%** of the series' variance, after removing the trend, is explained by a recurring annual pattern. This is confirmed by the amplitude of the seasonal index: the peak month (**November**, index **128.1**) generates nearly twice as many tenders (`1.99×`) as the month of lowest activity (**January**, index **64.2**), with a coefficient of variation of the monthly index of `CV=15.1%`.
In addition to the annual cycle, the data also exhibit strong **weekly seasonality** — publications are concentrated on working days (peak on **Thursday**, index **158.6**), while at weekends activity is negligible (index `≈1.7`).

### Trend
The trend-strength coefficient `Ft=0.637` (computed over the full 2021–2025 range) indicates a clear, though weaker than seasonality, trend component. It is, however, largely the effect of the one-off **ramp-up of the set in 2021**, rather than a sustained increase in the number of tenders. After restricting the analysis to the stable **2022–2025** period, the fit of the linear trend is very weak — the Pearson coefficient `r=0.241` and the coefficient of determination `R²=0.058` mean that the linear model explains only about **6%** of the variance in monthly volumes. The slope of the trend line is `+28` tenders per month (`+337` annually), which, against an average level of about **9,000** tenders per month, is a marginal value. This means that after the platform's roll-out period in 2021 ended, the number of tenders stabilised, and the observed fluctuations are almost exclusively seasonal in nature.

## Change in the Number of Tenders Over the Analyzed Period
The number of published tenders rose markedly in the first two years of the set's operation and then stabilised at a similar level.
In **2021**, **73,597** tenders were published; however, this was the platform's ramp-up period — January 2021 averaged a mere **26.5** tenders per day, versus about 175–218 in subsequent years.
In **2022**, the number of tenders rose to **113,592**, a jump of **+54.3%** relative to the previous year, reflecting the full implementation of mandatory procurement electronisation.
In subsequent years, the volume remained within a narrow range: **104,408** in 2023 (**−8.1%**), **108,229** in 2024 (**+3.7%**), and **118,007** in 2025 (**+9.0%**), which was the year with the highest number of tenders in the entire set.

Fitting a linear trend to the monthly volumes over the full **2021–2025** range yields a Pearson coefficient `r=0.544` and a coefficient of determination `R²=0.296`, with a slope of `+69` tenders per month (`+829` annually).
This result, however, is largely the effect of the one-off ramp-up of the set in 2021, rather than a sustained increase in the number of tenders.
After restricting the analysis to the stable **2022–2025** period, the fit of the linear trend almost disappears — the Pearson coefficient `r=0.241` and the coefficient of determination `R²=0.058` mean that the linear model explains only about **6%** of the variance in monthly volumes.
The slope of the trend line in this period is `+28` tenders per month (`+337` annually), which, against an average level of about **9,255** tenders per month, is a marginal value.
This means that after the platform's roll-out period in 2021 ended, the overall number of tenders stabilised, and the observed fluctuations are almost exclusively seasonal in nature (see [Seasonality Analysis of Tender Distribution](#seasonality-analysis-of-tender-distribution)).

## Seasonality Analysis of CPV Divisions
To assess seasonality in the thematic cross-section, a separate monthly time series was constructed for each of the **45 divisions** (data [`tenders_by_month_and_division`](data/tenders_by_month_and_division.csv)), and the same measures as for the entire set were computed for it: the **STL seasonality strength** (`Fs`, 2021–2025 range) and the **seasonal index** together with the peak/trough amplitude (the years 2022–2025). The analysis was limited to the **34 divisions with a volume ≥ 2,000** tenders, because for rare divisions the coefficients are too noisy to interpret. The results are generated by the [`seasonality_by_division.py`](seasonality_by_division.py) script.

<img width="1500" alt="Seasonality of tenders by CPV division" src="output/seasonality_by_division.png" />

The divisions **differ markedly** in their degree of regularity — the seasonality strength ranges from `Fs=0.98` to almost zero. The most strongly seasonal are **recurring services contracted cyclically**, the least — **one-off supplies of equipment and machinery**.

**Divisions with the strongest seasonality:**

| Division | Fs | Amplitude (peak/trough) | Peak → Trough |
|-------|:--:|:--:|:--:|
| **60 Road transport services** | **0.98** | 7.8× | Jul → Apr |
| 90 Environmental and sanitation services | 0.96 | 4.8× | Nov → Aug |
| 85 Health and social services | 0.96 | 4.7× | Dec → Aug |
| 64 Postal and telecommunications services | 0.95 | **11.6×** | Nov → Aug |
| 15 Food products and beverages | 0.94 | 5.3× | Nov → Apr |
| 66 Financial and insurance services | 0.94 | 3.6× | Nov → Jan |
| 9 Petroleum products, fuel and energy | 0.91 | 4.7× | Nov → Apr |

The dominant pattern is an **autumn peak (November)** with a trough during the holiday period or at the start of the year. This corresponds to the mechanism of **contracting continuous services in advance for the following calendar year** — insurance (div. 66), fuel and energy supplies (div. 9), postal services (div. 64), sanitation (div. 90), or catering (div. 15) are awarded in autumn so as to take effect from January. This coincides with the November peak observed for the entire set. The exception is **road transport** (div. 60), whose peak falls in **July** — which corresponds to contracting student transport before the start of the school year in September.

**Divisions with the weakest seasonality:**

| Division | Fs | Amplitude (peak/trough) | Peak → Trough |
|-------|:--:|:--:|:--:|
| 43 Mining machinery | 0.04 | 6.8× | Oct → Jan |
| 31 Electrical equipment | 0.07 | 8.4× | Oct → Jan |
| 35 Safety and security equipment | 0.35 | 6.4× | Oct → Jan |
| 42 Industrial machinery | 0.39 | 4.1× | Oct → Jan |
| 80 Education services | 0.46 | 2.1× | Mar → Dec |
| 18 Clothing and footwear | 0.55 | 1.9× | Oct → Jan |

The lowest `Fs` values are reached by **supplies of equipment and machinery** (electrical equipment `Fs=0.07`, mining machinery `Fs=0.04`, industrial machinery `Fs=0.39`), that is, procurements of a **one-off and project-based** nature, whose timing results from individual investment needs rather than from the budget calendar. It is worth noting that these divisions exhibit at the same time a **high amplitude** (electrical equipment 8.4×) but a **low seasonality strength** — this means that their fluctuations are of the nature of **irregular spikes** rather than a recurring annual pattern. This illustrates why amplitude alone is misleading, whereas the `Fs` measure (which separates regular seasonality from noise) better captures actual cyclicality.

A distinct rhythm is exhibited by **education services** (div. 80, `Fs=0.46`) — their peak falls in **March** and their trough in **December**, reflecting an **academic** rather than a budgetary cycle. The division dominant across the entire set, **45 (Construction works)**, in turn sits in the middle of the scale (`Fs=0.77`), with a peak in **July** and a trough in **December**, consistent with the natural season for construction work.

# Analysis of Tender Distribution Against Other Factors
## Introduction
No data are available on the share of the **city of Warsaw** in the country's overall GDP. The only available data present the share of the **Warsaw Capital Region** under the **NUTS 2** classification. Converting the data obtained from the eZamówienia platform to the **NUTS 2** system could lead to the misallocation of local government units, owing to the original data structure containing `organizationProvince`, which represents the contracting authority's voivodeship, and `organizationCity`, which represents the contracting authority's locality. Owing to the scale resulting from the number of localities comprising the **Warsaw Capital Region**, and at the same time the low precision of the original data representing the tender's location in relation to the administrative system, converting the data to the **NUTS 2** format and enriching it with data on the population of the municipalities comprising the **Warsaw Capital Region** carries too high a risk of erroneous data aggregation during the conversion process.
In view of the above, it was only in the analysis of the correlation between population and the number of tenders that it was possible to exclude the city of Warsaw as a separate unit.

## Data Analysis
### Number of Tenders vs. Voivodeship GDP
The number of tenders in a voivodeship is highly correlated with that voivodeship's GDP indicator.
The Pearson coefficient `r=0.974` indicates a very strong positive correlation.
The coefficient of determination `R²=0.949` indicates that the linear model describes the variation in the number of tenders based on GDP very well.
The chart shows that the **Masovian** voivodeship clearly stands out from the other elements of the set on both the axis representing the number of tenders and that representing GDP, yet it lies almost perfectly on the trend line.

### Number of Tenders vs. Voivodeship Population
The number of tenders in the voivodeships is also highly correlated with the number of inhabitants of a given voivodeship, though not as strongly as with GDP.
The Pearson coefficient `r=0.953` indicates a very strong positive correlation.
The coefficient of determination `R²=0.908` indicates that the linear model describes the variation in the number of tenders based on population well.
The chart shows that in this case too, the **Masovian** voivodeship clearly stands out from the other elements of the set on both the axis representing the number of tenders and that representing the number of inhabitants, but this time it is considerably distant from the trend line, in the direction of a greater number of tenders per capita than the other elements of the set.

### Number of Tenders vs. Voivodeship Population, Excluding Warsaw from the Masovian Voivodeship
After separating the **city of Warsaw** from the rest of the **Masovian voivodeship**, the overall correlation declined.
The Pearson coefficient `r=0.874` indicates a strong positive correlation, although markedly weaker than with the full data of the **Masovian voivodeship**.
The coefficient of determination `R²=0.764` indicates that the linear model explains about 76% of the variance in the number of tenders based on population — a decline of more than 14 percentage points relative to the analysis without splitting the **Masovian voivodeship**.
Despite the fact that the correlation declined relative to the **Number of Tenders vs. Voivodeship Population** chart, the chart shows that the **Masovian voivodeship**, after excluding the **city of Warsaw**, moved closer to the trend line, with the other voivodeships clustering around it. The exception remains the **city of Warsaw**, which stands out against the set with a high number of tenders per capita.

### Population vs. GDP
In order to examine the relationship between the two analysed factors, a chart was created presenting voivodeship GDP against population.
The Pearson coefficient `r=0.951` indicates a very strong positive correlation between GDP and the number of inhabitants of the voivodeships.
The coefficient of determination `R²=0.904` indicates that more than 90% of the variance in GDP can be explained by the number of inhabitants alone, confirming that the two variables are strongly interdependent and do not constitute independent predictors of the number of tenders.
The number of inhabitants increases in the same direction as voivodeship GDP. Also worth noting on this chart is the distinct position of the **Masovian voivodeship**, whose GDP is markedly higher relative to its number of inhabitants than in the case of other voivodeships.

### Number of Tenders vs. GDP per Capita
The Pearson coefficient `r=0.880` indicates a strong positive correlation, though lower than in the case of absolute GDP.
The coefficient of determination `R²=0.775` indicates that the linear model explains about 78% of the variance in the number of tenders — a poorer result than for total GDP, suggesting that per-capita affluence alone is a weaker predictor of procurement activity than the economic scale of the region.
Despite the relatively high values of the **Pearson and determination coefficients**, the chart shows considerably greater dispersion of the set's elements than in the previous charts.

# Summary
1. Data description

   The analysis covered **517,840** tenders originating from the eZamówienia (BZP) portal and spanning the period **2021–2025**. As part of data preparation, attributes devoid of informational value were dropped (`TenderType` and `procedureResult` — exclusively NULL values — as well as `isTenderAmountBelowEU`, with the constant value `True`), and the analysis of CPV codes was based solely on the main code of each notice. For the purposes of generalisation, the CPV codes were aggregated into **45 divisions** consistent with Commission Regulation (EC) No 213/2008.

2. Popularity description

   The distribution of tenders — both at the level of individual **CPV codes** (5,047 codes) and of **divisions** — is strongly **right-skewed with a long tail**. The undisputed leader is code **45000000-7 (Construction works)**, accounting for **11.38%** of all tenders at the CPV level and **32.25%** at the division level, exceeding the next position in the ranking more than sixfold. The dominance of construction works is universal — this code held first place in **all voivodeships and in all years** — while the further positions in the regional rankings reflect the geographical and institutional specificity of individual voivodeships.

3. Description of changes over time

   The overall number of tenders rose abruptly during the platform's implementation period (from **73,597** in 2021 to **113,592** in 2022) and then stabilised within the range of **104–118 thousand** annually. After excluding the set's 2021 ramp-up, the linear trend practically disappears (`R²=0.058`), meaning that the tender volume has reached saturation. The series' variability is almost exclusively **seasonal** in nature — seasonality strength `Fs=0.691`, with a peak in **November** and a trough in **January** (nearly a twofold difference), and a marked concentration of publications on working days. At the level of the thematic structure, by contrast, a high reactivity of the market to external systemic impulses is visible (purchases of ICT equipment for schools in 2022, generator sets in 2025, or training services financed from ESF+).

4. External factors

   GDP is the best factor on the basis of which the number of tenders can be predicted. The high correlation between the number of tenders and GDP means that regions with a stronger regional economy generate more tenders. This is a logical relationship, but it shows that procurement activity in Poland remains strongly concentrated in the most economically developed regions. This may attest to persistent regional disparities despite numerous programmes, such as the **Operational Programme Eastern Poland 2014–2020 (PO PW)**, **European Funds for Eastern Poland 2021–2027 (FEPW)**, and the **Regional Operational Programmes (ROP)** financed from EU funds, which were intended to equalise developmental disparities between voivodeships.
   The thesis of persistent concentration of procurement activity is confirmed by the charts of the number of tenders against population, which show a linear increase in the number of tenders with population. The exception remains the **city of Warsaw**, which generates considerably more tenders per capita than the trend would suggest. This is clearly visible in the inflated result of the **Masovian voivodeship** in the second chart, and in the third chart with the **city of Warsaw** separated out, whose model fit (`R²=0.764`) is more than 18 percentage points lower than that of the chart with the entire **Masovian voivodeship** (`R²=0.949`).
   The anomaly associated with the inflated result of the **Masovian voivodeship** is also visible in the fourth chart, and strikingly so in the fifth, where the other voivodeships represent a similar level of number of tenders and GDP per capita, clustering in the lower-left corner, while the **Masovian voivodeship** is isolated in the opposite one. The weaker model fit in the fifth chart shows that per-capita affluence alone is not a good predictor of the number of tenders — what matters above all is the absolute economic scale of the region.
   In order to better examine the validity of the correlation between the number of tenders and GDP, the **city of Warsaw** or the **Warsaw Capital Region** would need to be excluded from the **Masovian voivodeship**, which, for the reasons explained in the introduction, was not done.

# Conclusions
1. **Application of the research and work**

   The results of the analysis have direct practical application for both sides of the procurement market. For **contractors**, the most important operational conclusion is the ability to **plan the bidding calendar and production capacity** based on the identified seasonal patterns — knowing that cyclically contracted services are awarded in **November**, and student transport (div. 60) in **July**, makes it possible to prepare teams and resources for the anticipated peaks in advance. A second direction is **development towards segments that grow year over year**: the systematic growth in procurement for engineering design services (CPV **71320000-7**) heralds future construction investment, while categories reacting to systemic impulses (generator sets, ICT equipment for schools, training services financed from ESF+) indicate areas of growing demand in which it is worth building competencies. For **contracting authorities**, by contrast, a practical guideline is **publishing proceedings outside the November peak** — in a period of lower accumulation of notices, competition for contractors' attention is less dispersed, which increases the chance of a greater number of bids and more favourable terms.

2. **Predictability of the procurement market**

   The predictability of the procurement market is twofold. The **regular component** — the overall number of tenders — is well predictable: after the platform's implementation ended, the volume stabilised (`R²=0.058` for the trend over the stable 2022–2025 period), and its fluctuations are almost exclusively **seasonal** (`Fs=0.691`), with a recurring annual and weekly rhythm. This makes it possible to forecast monthly and weekly activity levels using a simple seasonal model. The **structural component** — that is, *which* categories will suddenly gain in importance — cannot, however, be predicted from the time series itself, because it depends on external decisions: central programmes, the geopolitical context, or the schedule of EU funding tranches. The demonstrated high reactivity of the market means, however, that such changes **can be detected and explained early**, by treating unusual spikes in the thematic structure as a signal of the launch of a specific systemic impulse. The market is therefore predictable in its rhythm, but not in the content of demand shocks.

3. **Limitations of the analysis and directions for further research**

   The conclusions presented should be read in light of the **limitations of the analysis**. First, the set comprises exclusively proceedings **below the EU threshold** (`isTenderAmountBelowEU=True`), so the largest contracts remain outside the analysis. Second, the **number** of tenders was studied, not their **value** — the results describe procurement activity but not the scale of expenditure. Third, the analysis was based **solely on the main CPV code** of each notice, and the `procedureResult` attribute contained NULL values, which made it impossible to assess the outcomes and competitiveness of the proceedings. The problem of separating the **city of Warsaw / Warsaw Capital Region** from the Masovian voivodeship in the NUTS 2 system also remained unresolved. A natural direction for further research is therefore to link the set with **contract values**, the **number of bids submitted** (as a measure of the intensity of competition), and **data on the winners**, which would make it possible to move from analysing activity alone to analysing the efficiency and competitiveness of the public procurement market.
