"""Build Day4_Morning_Data_Analysis.ipynb."""

from nb_helpers import Notebook, COLAB_SETUP

nb = Notebook()

nb.md("""
# 📘 Day 4 (Morning) — Data Analysis with Pandas
**SDNB Vaishnav College for Women, Chromepet**

**Date:** Thursday, 30 April 2026 | **Duration:** 9:30 AM – 1:00 PM

---

### 🎯 By the end of this morning you will:
- ✅ Read CSV files into Pandas and explore them
- ✅ Analyse `sales_data.csv` end-to-end (revenue, top performers, charts)
- ✅ Build a **7-day weekly sales report** in both plain Python and Pandas
- ✅ Reconcile a `bank_transactions.csv` automatically
- ✅ Manage `inventory.csv` — read, add new product, save back
""")

nb.code(COLAB_SETUP)

# Recap
nb.md("""
## 🔁 Quick Recap — Day 3

We learned to **draw** with Matplotlib. Today we learn to **analyse** with Pandas. The two tools work hand in hand: Pandas reshapes the data, Matplotlib displays it.
""")

# ── SECTION 1 — Pandas Intro ────────────────────────────────────────────
nb.md("""
## 🐼 Section 1 — Introduction to Pandas *(25 min)*

> **Analogy:** Pandas is **Excel inside Python**. A *DataFrame* is exactly like an Excel sheet — rows, columns, filters, formulas. Except it can handle 10 MILLION rows without crashing, and you can automate everything.

| What you do in Excel | What you do in Pandas |
|----------------------|------------------------|
| Open a `.csv` file | `pd.read_csv("file.csv")` |
| See first 5 rows | `df.head()` |
| See column names | `df.columns` |
| Filter rows (AutoFilter) | `df[df["Sales"] > 5000]` |
| Sum a column | `df["Sales"].sum()` |
| Group by category | `df.groupby("Category").sum()` |
| Sort by column | `df.sort_values("Amount")` |
| Add new column (formula) | `df["Tax"] = df["Price"] * 0.18` |
""")

nb.code('''import pandas as pd

# 1) Build a tiny DataFrame from scratch (5 rows × 4 cols)
mini = pd.DataFrame({
    "Date"   : ["27-Apr", "27-Apr", "28-Apr", "28-Apr", "29-Apr"],
    "Product": ["Saree", "Kurti", "Watch", "Bedsheet", "Saree"],
    "Units"  : [3, 5, 2, 4, 6],
    "Price"  : [2499, 1299, 3499, 1199, 2499],
})
print(mini)
''')

nb.code('''# 2) The basic inspection toolkit
print("\\nhead(3):"); print(mini.head(3))
print("\\ntail(2):"); print(mini.tail(2))
print("\\nshape  :", mini.shape, "(rows, cols)")
print("\\ndtypes :"); print(mini.dtypes)
print("\\ncolumns:", list(mini.columns))
print("\\ndescribe (numeric only):"); print(mini.describe())
''')

nb.code('''# 3) Selecting, filtering, calculating
print("Single column:"); print(mini["Product"], "\\n")

# Filter rows where Units > 3
print("Rows with Units > 3:")
print(mini[mini["Units"] > 3], "\\n")

# Add a calculated column
mini["Revenue"] = mini["Units"] * mini["Price"]
print("With Revenue column:")
print(mini)
''')

nb.code('''# 4) iloc vs loc
print("First row by position (iloc[0]):")
print(mini.iloc[0], "\\n")

print("Cell at row 2, column 'Product' (loc):")
print(mini.loc[2, "Product"])
''')

nb.code('''# 5) Missing values
import numpy as np
sample = pd.DataFrame({"Item": ["A", "B", "C"], "Stock": [10, np.nan, 0]})
print("With missing values:"); print(sample)
print("\\nisnull():"); print(sample.isnull())
print("\\nfillna(0):"); print(sample.fillna(0))
print("\\ndropna():"); print(sample.dropna())
''')

nb.md("""**🧠 What just happened?** `fillna()` is like *filling blank cells in your attendance register* — it replaces missing values. `dropna()` removes any row that has missing data.""")

# ── EXERCISE 1 — Sales CSV ──────────────────────────────────────────────
nb.md("""
## 📊 Exercise 1 — Sales CSV Analysis *(30 min)*

Load `sales_data.csv` and do a full analysis.
""")

nb.code('''try:
    sales = pd.read_csv(DATA_PATH + "sales_data.csv")
    print(f"✅ Loaded {len(sales)} sales records")
except FileNotFoundError:
    print("⚠️ File not found at", DATA_PATH)
    raise

# Step 1 — Data overview
print("\\nShape   :", sales.shape)
print("Columns :", list(sales.columns))
print("\\nFirst 5 rows:"); print(sales.head())
print("\\nMissing values per column:"); print(sales.isnull().sum())
print("\\ndescribe():"); print(sales.describe())
''')

nb.code('''# Clean: coerce Units to numeric and drop missing units
sales["Units"] = pd.to_numeric(sales["Units"], errors="coerce")
sales_clean = sales.dropna(subset=["Units"]).copy()
sales_clean["Units"] = sales_clean["Units"].astype(int)

# Step 2 — Revenue analysis
sales_clean["Revenue"] = sales_clean["Units"] * sales_clean["Price"]
total_revenue = sales_clean["Revenue"].sum()
print(f"Total revenue across {len(sales_clean)} rows: ₹{total_revenue:,.2f}")

# Revenue by Category
rev_by_cat = sales_clean.groupby("Category")["Revenue"].sum().sort_values(ascending=False)
print("\\nRevenue by Category:")
print(rev_by_cat.apply(lambda v: f"₹{v:,.0f}"))

# Revenue by Region (handle missing)
rev_by_region = sales_clean.assign(Region=sales_clean["Region"].fillna("Unknown")) \\
    .groupby("Region")["Revenue"].sum().sort_values(ascending=False)
print("\\nRevenue by Region:")
print(rev_by_region.apply(lambda v: f"₹{v:,.0f}"))
''')

nb.code('''# Revenue by Month
sales_clean["Date"] = pd.to_datetime(sales_clean["Date"], errors="coerce")
sales_clean["Month"] = sales_clean["Date"].dt.month_name().str[:3]
rev_by_month = sales_clean.groupby("Month", sort=False)["Revenue"].sum()

# Sort months chronologically
month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
rev_by_month = rev_by_month.reindex([m for m in month_order if m in rev_by_month.index])
print("\\nRevenue by Month:")
print(rev_by_month.apply(lambda v: f"₹{v:,.0f}"))
''')

nb.code('''# Step 3 — Top performers
top_products = sales_clean.groupby("Product")["Revenue"].sum().sort_values(ascending=False).head(5)
top_regions  = sales_clean.assign(Region=sales_clean["Region"].fillna("Unknown")) \\
                          .groupby("Region")["Revenue"].sum().sort_values(ascending=False).head(3)
best_month   = rev_by_month.idxmax()
worst_month  = rev_by_month.idxmin()

print("Top 5 products by revenue:")
print(top_products.apply(lambda v: f"₹{v:,.0f}"))
print("\\nTop 3 regions:")
print(top_regions.apply(lambda v: f"₹{v:,.0f}"))
print(f"\\nBest performing month  : {best_month}  (₹{rev_by_month.max():,.0f})")
print(f"Worst performing month : {worst_month} (₹{rev_by_month.min():,.0f})")
''')

nb.code('''# Step 4 — Visualise findings
import matplotlib.pyplot as plt
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

rev_by_cat.plot(kind="bar", ax=axes[0], color="#7B2CBF",
                title="Revenue by Category")
axes[0].set_ylabel("Revenue (₹)")
for i, v in enumerate(rev_by_cat.values):
    axes[0].text(i, v, f"₹{int(v):,}", ha="center", va="bottom", fontsize=8)

rev_by_region.plot(kind="bar", ax=axes[1], color="#FFB703",
                   title="Revenue by Region")
axes[1].set_ylabel("Revenue (₹)")

rev_by_month.plot(kind="line", marker="o", ax=axes[2], color="#00BBF9",
                  title="Monthly Revenue Trend", linewidth=2)
axes[2].set_ylabel("Revenue (₹)")

plt.tight_layout()
plt.show()
''')

nb.md("""
### 📋 Sales Analysis Report — Summary
""")
nb.code('''print("════════════════════════════════════════════════")
print("           SALES ANALYSIS REPORT — Q1 2026     ")
print("════════════════════════════════════════════════")
print(f"  Total Revenue      : ₹{total_revenue:,.2f}")
print(f"  Records analysed   : {len(sales_clean)} (after cleaning)")
print(f"  Best month         : {best_month}")
print(f"  Worst month        : {worst_month}")
print(f"  Top category       : {rev_by_cat.idxmax()} (₹{rev_by_cat.max():,.0f})")
print(f"  Top region         : {rev_by_region.idxmax()} (₹{rev_by_region.max():,.0f})")
print(f"  #1 product         : {top_products.index[0]} (₹{top_products.iloc[0]:,.0f})")
print("════════════════════════════════════════════════")
''')

# ── EXERCISE 2 — 7-day weekly sales ─────────────────────────────────────
nb.md("""
## 📅 Exercise 2 — 7-Day Sales Summary *(20 min)*

**Scenario:** *Week-end review at a Chennai retail store. The manager wants a quick weekly performance summary.*

We'll do this **two ways** — once with plain Python (yesterday's tools), once with Pandas — to feel the difference.
""")

nb.code('''# ── INTERACTIVE VERSION (uncomment to use input()) ──
# weekly_sales = []
# i = 1
# while i <= 7:
#     amt = float(input(f"Enter Day {i} sales: ₹"))
#     weekly_sales.append(amt)
#     i += 1

# Hardcoded so the notebook runs end-to-end
weekly_sales = [28400, 31200, 19800, 42500, 38900, 51200, 15300]
day_names    = ["Monday", "Tuesday", "Wednesday", "Thursday",
                "Friday", "Saturday", "Sunday"]

# ── Plain Python ──
total_p   = sum(weekly_sales)
avg_p     = total_p / len(weekly_sales)
max_p     = max(weekly_sales)
min_p     = min(weekly_sales)
best_idx  = weekly_sales.index(max_p)
worst_idx = weekly_sales.index(min_p)
print(f"Plain Python  →  total ₹{total_p:,} | avg ₹{avg_p:,.0f} | best {day_names[best_idx]} | worst {day_names[worst_idx]}")

# ── Pandas ──
s = pd.Series(weekly_sales, index=day_names, name="Sales")
print(f"Pandas        →  total ₹{s.sum():,} | avg ₹{s.mean():,.0f} | "
      f"best {s.idxmax()} | worst {s.idxmin()}")
''')

nb.code('''# Pretty weekly summary report with ASCII bar chart
above_avg = sum(1 for x in weekly_sales if x > avg_p)
max_val   = max(weekly_sales)

print("════════════════════════════════════════")
print("     WEEKLY SALES REPORT                ")
print("     Chennai Retail Store | Week 17, 2026")
print("════════════════════════════════════════")

for day, sale in zip(day_names, weekly_sales):
    bar_len = int(round((sale / max_val) * 10))
    bar     = "▓" * bar_len + "░" * (10 - bar_len)
    flag    = " ← BEST DAY" if sale == max_val else (" ← WORST" if sale == min_p else "")
    print(f"  {day:<10s}: ₹{sale:>7,}  [{bar}]{flag}")

print("─────────────────────────────────────────")
print(f"  Total       : ₹{total_p:,}")
print(f"  Average     : ₹{avg_p:,.0f}")
print(f"  Best Day    : {day_names[best_idx]} (₹{max_p:,})")
print(f"  Worst Day   : {day_names[worst_idx]} (₹{min_p:,})")
print(f"  Above avg   : {above_avg} of 7 days")
print("════════════════════════════════════════")
''')

# ── EXERCISE 3 — Bank Statement ─────────────────────────────────────────
nb.md("""
## 🏦 Exercise 3 — Bank Transaction CSV Parser *(25 min)*

**Scenario:** *The accounts assistant at SDNB College needs to reconcile the bank statement. Build an automated analyser.*
""")

nb.code('''bank = pd.read_csv(DATA_PATH + "bank_transactions.csv")
print(f"✅ Loaded {len(bank)} transactions")

# Replace blanks with 0 for arithmetic
bank["Debit"]  = pd.to_numeric(bank["Debit"],   errors="coerce").fillna(0)
bank["Credit"] = pd.to_numeric(bank["Credit"],  errors="coerce").fillna(0)
bank["Balance"]= pd.to_numeric(bank["Balance"], errors="coerce")
bank["Date"]   = pd.to_datetime(bank["Date"], errors="coerce")
bank.head()
''')

nb.code('''credit_count = (bank["Credit"] > 0).sum()
debit_count  = (bank["Debit"]  > 0).sum()
total_credits= bank["Credit"].sum()
total_debits = bank["Debit"].sum()

largest_credit = bank.loc[bank["Credit"].idxmax()]
largest_debit  = bank.loc[bank["Debit"].idxmax()]

avg_credit = bank.loc[bank["Credit"] > 0, "Credit"].mean()
avg_debit  = bank.loc[bank["Debit"]  > 0, "Debit"].mean()

big_txns = bank[(bank["Credit"] > 50000) | (bank["Debit"] > 50000)]

print("════════════════════════════════════════════════════════")
print("             BANK RECONCILIATION STATEMENT             ")
print("             SDNB COLLEGE — Period: Jan 2026          ")
print("════════════════════════════════════════════════════════")
print(f"  Total transactions   : {len(bank)}")
print(f"  Credit entries       : {credit_count}")
print(f"  Debit entries        : {debit_count}")
print("--------------------------------------------------------")
print(f"  Total credits        : ₹{total_credits:>14,.2f}")
print(f"  Total debits         : ₹{total_debits:>14,.2f}")
print(f"  Net flow             : ₹{total_credits - total_debits:>14,.2f}")
print("--------------------------------------------------------")
print(f"  Largest credit       : ₹{largest_credit['Credit']:,.2f} ({largest_credit['Description']})")
print(f"  Largest debit        : ₹{largest_debit['Debit']:,.2f} ({largest_debit['Description']})")
print(f"  Avg credit           : ₹{avg_credit:,.2f}")
print(f"  Avg debit            : ₹{avg_debit:,.2f}")
print("--------------------------------------------------------")
print(f"  Transactions > ₹50k  : {len(big_txns)}")
print("════════════════════════════════════════════════════════")
''')

nb.code('''# Monthly summary
bank["Month"] = bank["Date"].dt.month_name().str[:3]
monthly = bank.groupby("Month")[["Credit", "Debit"]].sum()
monthly = monthly.reindex([m for m in ["Jan","Feb","Mar","Apr","May","Jun"] if m in monthly.index])

print("\\nMonthly inflows vs outflows:")
print(monthly.applymap(lambda v: f"₹{v:>12,.0f}"))

# Bar chart
import matplotlib.pyplot as plt
ax = monthly.plot(kind="bar", figsize=(10, 5),
                  color=["#2EC4B6", "#E71D36"], edgecolor="black")
ax.set_title("Bank — Credits vs Debits by Month")
ax.set_ylabel("Amount (₹)")
plt.tight_layout()
plt.show()
''')

# ── EXERCISE 4 — Inventory ──────────────────────────────────────────────
nb.md("""
## 📦 Exercise 4 — Inventory File Management *(20 min)*

Load `inventory.csv`, find low-stock items, append a new product, save back.
""")

nb.code('''inv = pd.read_csv(DATA_PATH + "inventory.csv")
print(f"✅ Loaded {len(inv)} inventory items")
inv.head()
''')

nb.code('''# Part A — value & alerts
inv["StockValue"] = inv["Stock"] * inv["UnitPrice"]
total_value = inv["StockValue"].sum()
print(f"Total inventory value: ₹{total_value:,.2f}")

low_stock = inv[(inv["Stock"] > 0) & (inv["Stock"] < 10)]
out_stock = inv[inv["Stock"] == 0]
healthy   = inv[inv["Stock"] >= 10]
print(f"\\n  ✅ Healthy stock (≥10) : {len(healthy)} items")
print(f"  ⚠️  Low stock (1-9)    : {len(low_stock)} items")
print(f"  ❌ Out of stock        : {len(out_stock)} items")

print("\\nReorder alert list (sorted by stock):")
print(low_stock.sort_values("Stock")[["ProductID", "Name", "Stock"]].to_string(index=False))

print("\\nTop 5 most valuable line items:")
print(inv.sort_values("StockValue", ascending=False)
         .head(5)[["ProductID", "Name", "Stock", "UnitPrice", "StockValue"]]
         .to_string(index=False))
''')

nb.code('''# Part B — append a new product, save updated CSV
import os

new_product = pd.DataFrame([{
    "ProductID" : "P031",
    "Name"      : "Cotton Towel Pack",
    "Category"  : "Textiles",
    "Stock"     : 50,
    "UnitPrice" : 299.00,
}])
inv_updated = pd.concat([inv.drop(columns=["StockValue"], errors="ignore"),
                         new_product], ignore_index=True)

out_path = DATA_PATH + "inventory_updated.csv"
inv_updated.to_csv(out_path, index=False)
print(f"✅ Wrote updated CSV to {out_path}  (now {len(inv_updated)} rows)")

# Reload & verify
reloaded = pd.read_csv(out_path)
print("\\nLast 3 rows of reloaded file:")
print(reloaded.tail(3).to_string(index=False))
''')

nb.code('''# Stock Status Report
def stock_status(stock):
    if stock == 0:    return "❌ OUT"
    if stock < 10:    return "⚠️ LOW"
    return "✅ OK"

inv["Status"] = inv["Stock"].apply(stock_status)
print("════════════════════════════════════════════════")
print("            STOCK STATUS REPORT                ")
print("════════════════════════════════════════════════")
print(f"  Total SKUs             : {len(inv)}")
print(f"  Total units in stock   : {int(inv['Stock'].sum()):,}")
print(f"  Total inventory value  : ₹{inv['StockValue'].sum():,.2f}")
print("------------------------------------------------")
print(f"  ✅ OK    : {(inv['Status']=='✅ OK').sum():>3} items")
print(f"  ⚠️ LOW   : {(inv['Status']=='⚠️ LOW').sum():>3} items")
print(f"  ❌ OUT   : {(inv['Status']=='❌ OUT').sum():>3} items")
print("════════════════════════════════════════════════")
''')

nb.md("""
## 📚 Recap

- **`pd.read_csv()` / `to_csv()`** — open & save spreadsheets
- **`.head()`, `.shape`, `.dtypes`, `.describe()`** — quick inspection
- **Filtering** — `df[df["col"] > value]`
- **Calculated columns** — `df["new"] = df["a"] * df["b"]`
- **`groupby` + `sum/mean`** — pivot-style aggregation
- **`fillna`, `dropna`** — handle missing data
- **`pd.to_datetime`** — convert text dates to real dates
- **`pd.concat`** — append new rows

---

➡️ **Next: Day 4 Afternoon — KPI Dashboard.** We'll calculate every important business KPI (margin, turnover, ROI, ATV, CAC) and ship a dark-themed 3×3 dashboard.
""")

path = nb.save("Day4_Morning_Data_Analysis.ipynb")
print("✅ Built", path)
