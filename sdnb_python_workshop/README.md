# SDNB Python Workshop — Business Analytics Using Python

**College:** Shrimathi Devkunvar Nanalal Bhatt Vaishnav College for Women, Chromepet, Chennai
**Programme:** Business Analytics Using Python — Hands-On Sessions
**Duration:** 15 hours across 4 days | **Dates:** 27–30 April 2026

---

## 🎯 What you'll build this week

By Thursday afternoon you'll have:

1. A working **Simple Interest / Compound Interest calculator**
2. A **USD → INR currency converter** with customs duty
3. A **GST-compliant invoice generator**
4. A **Net Salary / Payslip generator** with Indian tax slabs
5. A **Fixed Deposit maturity calculator** with compounding options
6. A **Sales commission engine** with leaderboard
7. **Bar / pie / histogram / scatter** charts in Matplotlib
8. **Sales / bank / inventory** Pandas analysis
9. A **3×3 KPI dashboard** (dark theme) for any retailer
10. A **capstone Q1 business analytics report** for SDNB Retail Pvt Ltd

---

## 📁 Folder structure

```
sdnb_python_workshop/
├── data/
│   ├── sales_data.csv          (90 rows  | Date, Product, Category, Units, Price, Region)
│   ├── bank_transactions.csv   (60 rows  | Date, Description, Debit, Credit, Balance)
│   ├── inventory.csv           (30 rows  | ProductID, Name, Category, Stock, UnitPrice)
│   ├── customer_ages.csv       (100 rows | CustomerID, Name, Age, City, Segment)
│   ├── ad_spend.csv            (24 rows  | Month, AdSpend, SalesRevenue, Channel)
│   ├── exam_marks.csv          (40 rows  | RollNo, Name, 5 subjects)
│   └── monthly_expenses.csv    (12 rows  | Month, Rent, Salary, Utilities, Marketing, Misc)
├── notebooks/
│   ├── Day1_Python_Basics_and_Finance.ipynb
│   ├── Day2_Functions_and_Business_Logic.ipynb
│   ├── Day3_Data_Visualisation.ipynb
│   ├── Day4_Morning_Data_Analysis.ipynb
│   ├── Day4_Afternoon_KPI_Dashboard.ipynb
│   └── Capstone_Business_Analytics_Report.ipynb
├── charts/                     (auto-created by Day 3)
├── capstone/                   (auto-created by Day 4 PM & capstone)
├── requirements.txt
└── README.md
```

> **All data files are in the `data/` folder. Do not move them** — every notebook expects them at that relative path.

---

## ▶️ How to run

### Option A — Google Colab (recommended for the workshop)

1. Zip the whole `sdnb_python_workshop/` folder (right-click → "Send to → Compressed").
2. Open [colab.research.google.com](https://colab.research.google.com) and sign in with your Google account.
3. Click **File → Upload notebook**, then upload one of the notebooks from `notebooks/`.
4. In the file pane (folder icon on the left), click **Upload** and add the matching CSV files from `data/` to a folder also called `data/`. (Colab stores them under `/content/`.)
5. Click **Runtime → Run all**.

### Option B — Local Jupyter

```bash
pip install -r requirements.txt
cd notebooks
jupyter notebook        # or:  jupyter lab
```

Open each notebook and run all cells. The first cell auto-detects whether it's running locally (`../data/`) or on Colab (`data/`).

---

## 📅 Recommended order

> **Run the notebooks in this order: Day1 → Day2 → Day3 → Day4_Morning → Day4_Afternoon → Capstone.** Each one assumes the concepts of the previous one.

| # | Notebook | Day | Hours | Key skills | Commerce context |
|---|---|---|---|---|---|
| 1 | `Day1_Python_Basics_and_Finance` | Mon Apr 27 | 3 | Variables, loops, lists, I/O | SI/CI, Currency, Sales, Savings |
| 2 | `Day2_Functions_and_Business_Logic` | Tue Apr 28 | 3 | Functions | Payslip, GST Invoice, FD, Commission |
| 3 | `Day3_Data_Visualisation` | Wed Apr 29 | 3 | Matplotlib | Expenses, Market Share, Customer Age, Ad ROI |
| 4 | `Day4_Morning_Data_Analysis` | Thu Apr 30 AM | 3 | Pandas + CSV | Sales, Bank Stmt, Inventory |
| 5 | `Day4_Afternoon_KPI_Dashboard` | Thu Apr 30 PM | 2 | Pandas + Matplotlib | Marksheet, KPI Dashboard |
| 6 | `Capstone_Business_Analytics_Report` | Thu Apr 30 final | 0.5 submit | Full pipeline | End-to-end Q1 business report |

---

## ✏️ Design principles followed in every notebook

1. **Real-world business analogy first**, then the Python code (think: drawer = variable, stamp = function).
2. **Comments on every line** — what the line does, in plain English.
3. After each code cell, a "🧠 What just happened?" Markdown beat.
4. Major sections end with a "✏️ Try It Yourself" exercise.
5. Output formatted like a real business document (payslip, invoice, statement).
6. **All amounts in Indian Rupees (₹)** with `:,.2f` formatting.
7. Variables named like business fields (`gross_salary`, not `x`).

---

## 🛠️ Regenerating everything from scratch

Every artefact in this workshop is reproducible. Inside `_build/`:

```bash
python _build/gen_data.py               # rebuilds the 7 CSV files
python _build/build_day1.py             # rebuilds Day 1 notebook
python _build/build_day2.py             # ... etc
python _build/build_day3.py
python _build/build_day4_morning.py
python _build/build_day4_afternoon.py
python _build/build_capstone.py
```

To re-execute notebooks (clears and regenerates output):
```bash
jupyter nbconvert --to notebook --execute --inplace notebooks/Day1_Python_Basics_and_Finance.ipynb
```

---

*Built for the M.Com Business Analytics module at SDNB Vaishnav College for Women, Chromepet, Chennai.*
