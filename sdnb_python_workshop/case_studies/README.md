# 📁 Case Studies — SDNB Business Analytics & Accounting Capstone

Six end-to-end case studies that combine the skills from Days 1–4 of the workshop into realistic business and accounting problems. The first three are **business-analytics** focused; cases 4–6 are **accounting-specific** workflows. Each notebook follows the same structure:

1. **Background & scenario** (markdown)
2. **Specific business questions** to answer
3. **Step-by-step analysis** with code + charts
4. **Findings** after each section
5. **A board-ready dashboard or scorecard**
6. **Concrete recommendations** to management
7. **Practice extensions** for self-study

---

## Case 1 — [Saravana Stores: Retail Chain Performance](Case1_Saravana_Stores_Retail_Performance.ipynb)

**Industry:** Multi-branch retail (Tamil Nadu, 5 stores)
**Skills exercised:** Pandas `groupby`, pivot tables, time-series, comparative dashboards
**The puzzle:** One branch (Salem) is hiding a Q4 contraction inside the chain's overall growth. Find it, explain it, and propose a turnaround.

**Data:** `data/branch_sales_12m.csv` — 300 rows (5 branches × 12 months × 5 categories)

---

## Case 2 — [Bharath Mobile: Customer Churn](Case2_Bharath_Mobile_Customer_Churn.ipynb)

**Industry:** Telecom
**Skills exercised:** Filtering, comparative aggregations, building a custom risk score, exporting a CSV action list
**The puzzle:** 22% of customers have churned. Profile who churns, build a 0–5 risk score, and produce the **Top 100 active at-risk customers** for the retention call team.

**Data:** `data/telecom_customers.csv` — 500 customer profiles with usage, billing and a `Churned` flag

---

## Case 3 — [Lakshmi Textiles: Financial Health](Case3_Lakshmi_Textiles_Financial_Health.ipynb)

**Industry:** Textile manufacturing (mid-cap)
**Skills exercised:** Multi-file joins, ratio analysis, trend interpretation, formal investment recommendation
**The puzzle:** Compute every standard profitability / liquidity / leverage / efficiency ratio across 3 years and arrive at a clear **Buy / Hold / Avoid** call.

**Data:**
- `data/pnl.csv` — 3-year Profit & Loss
- `data/balance.csv` — 3-year Balance Sheet

---

## 🧾 Accounting-focused case studies

## Case 4 — [Saraswathi Garments: AR Aging & Provision](Case4_Saraswathi_AR_Aging_and_Provision.ipynb)

**Workflow:** Accounts Receivable management
**Skills exercised:** Date arithmetic, conditional bucketing, customer-level aggregation, journal entry preparation
**The puzzle:** Build the standard 4-bucket aging schedule from raw invoices, compute provision per the company's IndAS-aligned matrix (1% / 5% / 15% / 30% / 50%), surface the top 5 customers to chase, and pass the provision journal entry.

**Data:** `data/ar_invoices.csv` — 67 outstanding invoices across 12 customers

---

## Case 5 — [Bharath Cotton: Inventory Valuation Comparison](Case5_Bharath_Cotton_Inventory_Valuation.ipynb)

**Workflow:** Inventory accounting (Ind AS 2 / AS 2)
**Skills exercised:** Implementing FIFO via a `deque`, LIFO via a stack, perpetual weighted-average; comparing COGS, gross profit, tax and ending inventory under each
**The puzzle:** Q1 purchase prices climbed from ₹320 → ₹410. Apply all three methods to the same purchase + sales transactions, compute downstream P&L impact, then recommend the right method (FIFO vs Weighted Average — LIFO is not Ind-AS-permitted but shown for comparison).

**Data:** `data/inventory_transactions.csv` — 10 mixed purchase + sale transactions

---

## Case 6 — [Murugan Industries: Budget vs Actual Variance](Case6_Murugan_Industries_Budget_Variance.ipynb)

**Workflow:** Management accounting / variance analysis
**Skills exercised:** Pivot tables, heatmaps with diverging colour scales, materiality thresholds, auto-generated MD&A bullets
**The puzzle:** 6 departments × 8 line items = 43 budget lines. Compute every variance, classify favourable / adverse, surface materially adverse items (>10%), build a Department × LineItem heatmap, and produce the board-ready MD&A.

**Data:** `data/budget_vs_actual.csv` — 43 budget vs actual lines

---

## ▶️ How to run

These notebooks are designed to run on **Google Colab** or local **Jupyter**:

- Open Colab → File → Upload notebook → choose any `Case*.ipynb`
- Also upload the matching CSV file(s) from `data/` into a folder also named `data/`
- Press **Runtime → Run all**

Each notebook auto-detects whether it's running locally (`data/`) or with the data folder one level up (`case_studies/data/`).

## 🛠️ Regenerating the datasets

All datasets are reproducible:

```bash
python _build/gen_case_data.py            # rewrites Cases 1-3 datasets
python _build/gen_accounting_case_data.py # rewrites Cases 4-6 datasets
python _build/build_case1.py              # rebuilds the Case 1 notebook
python _build/build_case2.py
python _build/build_case3.py
python _build/build_case4.py
python _build/build_case5.py
python _build/build_case6.py
```

## 🎯 How to use these as student assignments

For each case study, you can ask students to:

1. **Replicate** every cell themselves and explain what each line does
2. **Modify** thresholds in the risk score / ratio benchmarks and re-run
3. **Extend** by completing the "Practice extensions" section at the bottom
4. **Present** the recommendations to a peer, defending each finding from the data
