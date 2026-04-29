# 📁 Case Studies — SDNB Business Analytics Capstone

Three end-to-end case studies that combine the skills from Days 1–4 of the workshop into realistic business problems. Each notebook follows the same structure:

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

## ▶️ How to run

These notebooks are designed to run on **Google Colab** or local **Jupyter**:

- Open Colab → File → Upload notebook → choose any `Case*.ipynb`
- Also upload the matching CSV file(s) from `data/` into a folder also named `data/`
- Press **Runtime → Run all**

Each notebook auto-detects whether it's running locally (`data/`) or with the data folder one level up (`case_studies/data/`).

## 🛠️ Regenerating the datasets

All datasets are reproducible:

```bash
python _build/gen_case_data.py     # rewrites the 4 CSV files in case_studies/data/
python _build/build_case1.py       # rebuilds the Case 1 notebook
python _build/build_case2.py
python _build/build_case3.py
```

## 🎯 How to use these as student assignments

For each case study, you can ask students to:

1. **Replicate** every cell themselves and explain what each line does
2. **Modify** thresholds in the risk score / ratio benchmarks and re-run
3. **Extend** by completing the "Practice extensions" section at the bottom
4. **Present** the recommendations to a peer, defending each finding from the data
