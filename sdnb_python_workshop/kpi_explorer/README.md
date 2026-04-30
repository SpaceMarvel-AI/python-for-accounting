# 📊 SDNB KPI Explorer v2 — auto-EDA + KPI dashboard in a single HTML file

A **zero-install** browser tool: drop in any CSV / TSV / JSON / Excel file, get an automatic exploratory analysis, an interactive filter and pivot system, and a KPI dashboard.

> Built for SDNB Vaishnav College students who want a fully interactive feel for a dataset *before* writing Python.

## ✨ What's new in v2

| Area | v1 → v2 |
|------|---------|
| **Inputs** | CSV only → **CSV / TSV / JSON / Excel (.xlsx, .xls)** via SheetJS |
| **Filters** | none → **click any bar to filter** the entire dashboard, with chip removal |
| **Chart types** | fixed → **per-chart switcher** (bar / horizontal / doughnut, histogram / boxplot) |
| **Stats depth** | basic → **min / Q1 / median / Q3 / max + IQR + outliers per column** |
| **Correlation** | none → **interactive Pearson correlation heatmap** |
| **Pivot builder** | none → **interactive group-by + 6 aggregations** in the sidebar |
| **Insights** | shallow → **MoM growth, outliers, top correlation, dominant categorical, date span** |
| **Theme** | dark only → **dark + light toggle**, persisted in localStorage |
| **Tables** | static → **sortable** column profile, click any header |
| **Export** | none → **PNG download per chart**, **PDF/print export** of the whole dashboard |
| **Layout** | top-to-bottom → **sidebar + main**, mobile-responsive, sticky header & filter bar |
| **Errors** | crashed silently → friendly toast with reason |
| **Sample data** | 3 samples → **4 samples**, available both in upload screen and sidebar |

## ▶️ How to use

1. Open [`kpi_dashboard.html`](kpi_dashboard.html) in any modern browser.
2. **Drop a file** onto the upload box, or click and pick. Or click any sample button.
3. Use the dashboard:
   - **Click any bar/category** → filter the entire dashboard to that value (chips appear at the top, click ✕ to remove).
   - **Switch a chart type** with the dropdown in its top-right corner (categorical: bar / horizontal / doughnut · numeric: histogram / boxplot).
   - **Build a custom pivot** in the left sidebar: choose group, aggregation, value column, chart type → it appears at the bottom of the chart grid.
   - **Sort the column profile** by clicking any header (col / type / mean / outliers / etc.).
   - **Download a chart** as PNG with the 📥 button on each card.
   - **Export the whole dashboard** as a PDF with the 🖨 button (uses browser print → "Save as PDF").
   - **Toggle theme** with ☀️/🌙 — the choice persists across sessions.

## 🔒 Privacy

Your data never leaves your computer. PapaParse, SheetJS and Chart.js all run entirely in the browser — there is no server, no upload, no telemetry.

## 🧠 How does it decide what to show?

Heuristics applied to every column:

| Type | Trigger | What gets shown |
|------|---------|-----------------|
| **Numeric**  | ≥85% of values parse as a number (`₹$€,%` stripped) | Histogram (toggle to boxplot) + headline KPIs + correlation matrix participation |
| **Date** | ≥80% of values match `YYYY-MM-DD` / `DD-MM-YYYY` style and parse as Date | Time-series line chart of top numeric column |
| **Categorical** | otherwise, with reasonable cardinality (≤30 unique, ≤50% of rows) | Top-values bar chart + (if ≤6 categories) doughnut |
| **ID-like** | high uniqueness *and* name like `id / no / number / code / sku` | Excluded from auto-charting |

Money-like (`revenue`, `amount`, `price`, …), quantity-like (`qty`, `units`, `stock`, …), and rate-like (`rate`, `percent`, `margin`, …) names are detected and prioritised in headline KPI selection.

**Outliers** are flagged using the standard IQR rule: `< Q1 − 1.5 × IQR` or `> Q3 + 1.5 × IQR`.

## 📁 What's inside

- [`kpi_dashboard.html`](kpi_dashboard.html) — the entire app: HTML + inline CSS + inline JS (~1,400 lines).
- Libraries via CDN:
  - [PapaParse 5.4.1](https://www.papaparse.com/) — CSV / TSV parsing
  - [SheetJS 0.18.5](https://sheetjs.com/) — Excel parsing
  - [Chart.js 4.4.4](https://www.chartjs.org/) — visualisations
  - [chartjs-chart-boxplot 4.4.4](https://github.com/sgratzl/chartjs-chart-boxplot) — boxplots

## 🛠️ Customising it

The file is intentionally a single `.html` so it's easy to fork. Add a new chart type, a new heuristic, a new sample dataset, or a new aggregation — each lives in a clearly-marked section (search for `═════` in the source).

## 💡 Try it with the workshop datasets

Auto-EDA produces useful dashboards on every CSV in the workshop:

| File | Try it for |
|------|------------|
| `data/sales_data.csv` | Time-series, category mix, region totals |
| `data/customer_ages.csv` | Age histogram + city distribution + segment pie |
| `data/exam_marks.csv` | Subject-wise distributions, correlation between subjects |
| `case_studies/data/branch_sales_12m.csv` | Multi-branch monthly trends, click branch to filter |
| `case_studies/data/telecom_customers.csv` | Plan / AutoPay distributions, churn slices via filter |
| `case_studies/data/budget_vs_actual.csv` | Department vs Line Item heatmap, variance pivot |
| `case_studies/data/ar_invoices.csv` | Customer outstanding bars, age via filtering |
