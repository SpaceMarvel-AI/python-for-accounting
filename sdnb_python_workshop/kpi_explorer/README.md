# 📊 SDNB KPI Explorer — auto-EDA + KPI dashboard in a single HTML file

A **zero-install** browser tool: drop in any CSV, get an automatic exploratory analysis and KPI dashboard.

> Built for SDNB Vaishnav College students who want a quick visual feel for a dataset *before* writing Python.

## ▶️ How to use

1. Open [`kpi_dashboard.html`](kpi_dashboard.html) in any modern browser (Chrome / Edge / Firefox / Safari).
2. **Drop a CSV file** onto the upload box, or click and choose. *(Or click one of the built-in samples to see it in action.)*
3. The page renders instantly:
   - Dataset snapshot (rows, columns, completeness)
   - Auto-detected headline KPIs (sum / mean / max for the most "important" numeric columns)
   - Column profile table (type, missing, unique, min/max/mean)
   - Plain-English insights (data quality, top values, date range)
   - 8–12 charts auto-built from the column types
   - First 10 rows preview

## 🔒 Privacy

**Your data never leaves your computer.** PapaParse and Chart.js run entirely in the browser. There is no server, no upload, no telemetry.

## 🧠 How does it decide what to show?

It applies these heuristics to every column:

| Type detected | Trigger | What gets shown |
|---------------|---------|-----------------|
| **Numeric**       | ≥85% of values parse as a number (`₹`, `$`, `,`, ` ` are stripped) | Histogram + headline KPIs |
| **Date**          | ≥80% of values match a `YYYY-MM-DD` / `DD-MM-YYYY` style and parse as Date | Time-series line chart |
| **Categorical**   | otherwise, with reasonable cardinality (`≤30` unique, `≤50%` of rows) | Top-values bar chart + (if ≤6 categories) doughnut |
| **ID-like**       | Very high uniqueness *and* the column name matches `id / no / number / code` | Excluded from charts |

It also recognises **money-like** column names (`revenue`, `amount`, `price`, `salary`, `cost`…), **quantity-like** names (`qty`, `units`, `stock`…) and **ratio-like** names (`rate`, `percent`, `margin`…) — and prioritises them when picking headline KPIs.

## 📁 What's inside

- [`kpi_dashboard.html`](kpi_dashboard.html) — the entire app: HTML + inline CSS + inline JS (~700 lines).
- Libraries loaded from CDN:
  - [PapaParse 5.4.1](https://www.papaparse.com/) — CSV parsing
  - [Chart.js 4.4.4](https://www.chartjs.org/) — visualisations

## 🛠️ Customising it

The file is intentionally a single `.html` so it's easy to fork:

- Change the colour palette: edit the `:root { --... }` block at the top.
- Add a new chart type: drop a `drawXxx()` function next to `drawHistogram` / `drawBar` / `drawLine` and call it from `renderCharts()`.
- Add a new heuristic: extend `nameLooksLikeMoney()` / `nameLooksLikeQty()` to recognise more column names.
- Add a built-in sample dataset: append an entry to the `SAMPLES = { ... }` object near the bottom.

## 💡 Try it with the workshop datasets

The auto-EDA produces useful dashboards on every CSV in the workshop:

| File | Try it for |
|------|------------|
| `data/sales_data.csv`        | Time-series, category mix, region totals |
| `data/customer_ages.csv`     | Age histogram + city distribution + segment pie |
| `data/exam_marks.csv`        | Subject-wise distributions |
| `case_studies/data/branch_sales_12m.csv` | Multi-branch monthly trends |
| `case_studies/data/telecom_customers.csv` | Plan/AutoPay distributions, churn slices |
| `case_studies/data/budget_vs_actual.csv` | Department vs LineItem heatmap-style bar |
