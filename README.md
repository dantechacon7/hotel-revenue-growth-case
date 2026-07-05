# Hotel Revenue Growth Strategy

> End-to-end Business Analytics case using SQL, DuckDB and Python to identify **R$1M+** in annual revenue opportunities through cancellation reduction, pricing optimization and customer retention.

[🇧🇷 Read in Portuguese](README.pt-BR.md)

---

## Overview

This repository presents a Business Analytics case study based on historical hotel reservation data (2015–2017). The objective was to identify the main revenue drivers and propose commercially viable initiatives capable of increasing annual revenue by approximately **20%**.

---

## Business Problem

| | |
|---|---|
| Current Revenue | **R$11.60M** |
| Target Revenue (+20%) | **R$13.92M** |
| Revenue Gap | **≈ R$2.32M** |

- Where is revenue currently being lost?
- Which customer segments generate the highest value?
- Which initiatives should be prioritized according to impact and implementation effort?

---

## Dataset

| Metric | Value |
|--------|------:|
| Reservations | 39,859 |
| Period | 2015–2017 |
| Cancellation Rate | 27.82% |
| Realized Revenue | R$11.60M |
| Lost Revenue (cancellations) | R$5.84M |
| Average Daily Rate | R$91.29 |

Main attributes: booking channel, lead time, customer type, country, room category, ADR, stay duration, deposit type, special requests, reservation status.

---

## Tech Stack

Python · SQL · DuckDB · Pandas · Matplotlib · Google Colab

---

## Repository Structure

```
hotel-revenue-growth-case/
├── README.md
├── README.pt-BR.md
├── config.py
├── 01_data_exploration.py
├── 02_revenue_diagnosis.py
├── 03_customer_engagement_analysis.py
├── 04_business_recommendations.py
└── gold_analytics_fct_hotel_reservations.ipynb
```

---

## Key Findings

**Revenue Leakage:** 27.82% cancellation → R$5.84M lost. Reservations 90+ days in advance: 40% of volume, 64% of lost revenue.

**Direct Channel:** Lowest cancellation (13.48%), ADR R$111.67, no OTA commission. Highest net revenue per reservation.

**Non-refundable deposit anomaly:** 96% cancellation — concentrated in Portuguese groups. Euro/BRL asymmetry renders deposit irrelevant as retention barrier.

**Repeat Customers:** 4.4% of base, cancel 4.5× less. Weekend repeats reach ADR R$155–222 with ~6-night stays.

**Customer Engagement:** Each additional special request = +R$20–30 ADR, +0.3 nights, independent of seasonality. HB + 3 requests: R$168 ADR, 9% cancellation. FB + 3 requests: 0% cancellation.

---

## Business Recommendations

| # | Initiative | Est. Impact | Effort | Timeline |
|---|-----------|------------:|--------|----------|
| 1 | Deposit policy >30 days (excl. Groups) | ~R$380K | Low | Immediate |
| 2 | Pre-arrival upsell (room + meal + engagement) | ~R$180K | Low | Immediate |
| | **Immediate subtotal** | **~R$560K (24%)** | | |
| 3 | Demand management (retention + low season) | ~R$200K | Medium | 1–2 months |
| 4 | Direct channel migration | ~R$150K | Medium | 3–6 months |
| | **Short/mid-term subtotal** | **~R$910K (39%)** | | |
| 5 | Retention & loyalty (loyalty + corporate) | ~R$140K | Med/High | 3–12 months |
| | **Total** | **~R$1.05M (45%)** | | |

Reaching 100% of the target requires levers beyond the dataset: dynamic pricing, new markets, or capacity expansion.

---

## Methodology Note

**Revenue bug (fixed):** Original dataset uses comma as decimal separator in `receita_por_noite`. Earlier sessions underestimated revenue ~2.34×. Fix: `str.replace(',', '.')` before float cast. See `config.py`.

---

## Future Improvements

- Cancellation prediction model · Dynamic pricing simulation · Customer Lifetime Value · Interactive dashboard

---

## Author

**Dante Costa** — Senior Data Analyst
Business Analytics · SQL · Data Strategy · Business Architecture
