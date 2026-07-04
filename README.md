# Hotel Revenue Growth Strategy

> End-to-end Business Analytics case using SQL, DuckDB and Python to identify nearly **R$1M** in annual revenue opportunities through cancellation reduction, pricing optimization and customer retention.

[🇧🇷 Read in Portuguese](README.pt-BR.md)

---

## Overview

This repository presents a Business Analytics case study based on historical hotel reservation data (2015–2017).

The objective was to identify the main revenue drivers and propose commercially viable initiatives capable of increasing annual revenue by approximately **20%**.

Unlike a traditional exploratory analysis, this project focuses on translating data into business decisions by combining SQL analysis, hypothesis validation and financial impact estimation.

---

## Business Problem

Current Revenue

**R$ 4.97M**

Target Revenue (+20%)

**R$ 5.96M**

Revenue Gap

**≈ R$994K**

The project investigates three strategic questions:

- Where is revenue currently being lost?
- Which customer segments generate the highest value?
- Which initiatives should be prioritized according to impact and implementation effort?

---

## Dataset

Historical hotel reservation dataset.

| Metric | Value |
|---------|-------:|
| Reservations | 39,859 |
| Period | 2015–2017 |
| Cancellation Rate | 27.82% |
| Revenue | R$4.97M |

Main attributes include:

- Booking channel
- Lead time
- Customer type
- Country
- Room category
- ADR
- Stay duration
- Deposit type
- Special requests
- Reservation status

---

## Tech Stack

- Python
- SQL
- DuckDB
- Pandas
- Matplotlib
- Google Colab

---

## Repository Structure

```
hotel-revenue-growth-case/

README.md
README.pt-BR.md

config.py

01_data_exploration.py
02_revenue_diagnosis.py
03_customer_engagement_analysis.py
04_business_recommendations.py
```

---

## Project Workflow

```
Business Problem

↓

Exploratory Data Analysis

↓

Business Hypotheses

↓

SQL Validation

↓

Business Insights

↓

Strategic Recommendations

↓

Estimated Financial Impact
```

---

## Analysis Performed

### Revenue Diagnosis

- Revenue decomposition
- Lost revenue estimation
- ADR analysis
- Average stay

### Cancellation Analysis

- Lead time
- Booking channels
- Deposit policy
- Customer profile

### Customer Analysis

- Repeat customers
- Special requests
- Customer engagement

### Commercial Analysis

- Room categories
- Seasonality
- Direct vs OTA channels

---

## Key Findings

### Revenue Leakage

- 27.82% cancellation rate
- R$3.25M in lost revenue

### Long Lead Time

Reservations made over 90 days in advance represent the majority of lost revenue.

### Direct Channel

Lowest cancellation rate and highest estimated net profitability.

### Repeat Customers

Only 4.4% of customers are repeat guests, yet they cancel 4.5× less than first-time guests.

### Premium Rooms

Premium rooms generate substantially higher ADR while representing a very small share of reservations.

### Customer Engagement

Each additional special request correlates with higher ADR and longer stays.

---

## Business Recommendations

| Initiative | Estimated Impact |
|------------|----------------:|
| Deposit policy | R$200K |
| Pre-arrival upsell | R$180K |
| CRM retention campaigns | R$100K |
| Direct booking strategy | R$150K |
| Low season packages | R$100K |
| Loyalty program | R$80K |
| Corporate agreements | R$60K |

Estimated opportunity:

**≈ R$870K**

Equivalent to approximately **87%** of the target revenue increase.

---

## Future Improvements

Potential future developments include:

- Dynamic pricing simulation
- Cancellation prediction model
- Customer Lifetime Value
- Recommendation engine
- Interactive dashboard
- Revenue forecasting

---

## Author

**Dante Costa**

Senior Data Analyst

Business Analytics • SQL • Data Strategy • Business Architecture
