# Hotel Revenue Growth Strategy

Business Analytics case focused on identifying commercial opportunities to increase hotel revenue by 20% using historical booking data.

## Overview

This project analyzes nearly 40,000 hotel reservations (2015–2017) to identify the main revenue drivers, quantify revenue leakage and propose prioritized business initiatives.

Instead of focusing only on descriptive analytics, this case aims to answer:

> How can a hotel increase annual revenue by 20% using data-driven business decisions?

---

## Business Goal

Current Revenue

R$ 4.97M

Target Revenue (+20%)

R$ 5.96M

Gap to Close

≈ R$ 994K

---

## Main Business Questions

- Where is revenue being lost?
- Which customer segments are more valuable?
- Which booking channels generate higher profitability?
- Which room categories should be prioritized?
- How can cancellations be reduced?
- Which initiatives provide the highest business impact?

---

## Dataset

- ~39,800 hotel reservations
- Period: 2015–2017
- Multiple customer, booking and commercial attributes
- SQL analysis performed using DuckDB

---

## Tech Stack

- Python
- DuckDB
- SQL
- Pandas
- Matplotlib
- Google Colab

---

## Project Structure

```
data/
notebooks/
sql/
images/
docs/
src/
```

---

## Analysis Performed

### Revenue Overview

- Total Revenue
- Lost Revenue
- Cancellation Rate
- ADR
- Average Stay

### Cancellation Analysis

- Lead Time
- Payment Type
- Booking Channel
- Customer Type

### Commercial Analysis

- Market Segments
- Room Categories
- Customer Loyalty
- Seasonality
- Upsell Opportunities

### Customer Analysis

- Repeat Customers
- Weekend vs Weekday Guests
- Special Requests

---

## Key Findings

### 1. Cancellations

27.8% of all reservations were cancelled.

≈ R$3.25M in potential revenue was lost.

---

### 2. Lead Time

Bookings made over 90 days in advance account for the majority of lost revenue.

---

### 3. Direct Channel

Direct bookings show:

- lower cancellation
- competitive ADR
- higher net margin

---

### 4. Repeat Customers

Repeat guests cancel 4.5x less than first-time guests.

---

### 5. Room Mix

Premium rooms represent a very small share of bookings despite much higher ADR.

---

## Business Recommendations

- Deposit policy for long lead-time bookings
- Pre-arrival room upgrades
- CRM retention campaigns
- Direct booking strategy
- Low-season packages
- Loyalty program
- Corporate agreements

Estimated impact:

≈ R$870K recovered revenue

---

## Repository Contents

- Complete notebook
- SQL queries
- Business report
- Visualizations
- Documentation

---

## Author

Dante Costa

Senior Data Analyst | Business Analytics | SQL | Data Strategy
