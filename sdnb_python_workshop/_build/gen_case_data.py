"""Generate datasets for the 3 SDNB case studies."""

import csv
import random
from datetime import date, timedelta
from pathlib import Path

random.seed(20260428)

DATA = Path(__file__).resolve().parent.parent / "case_studies" / "data"
DATA.mkdir(parents=True, exist_ok=True)


# =====================================================================
# CASE 1 — Saravana Stores 12-month branch sales
#   columns: Month, Branch, Category, Revenue, Customers
# =====================================================================
def gen_case1():
    branches = ["Chennai", "Coimbatore", "Madurai", "Tiruchirappalli", "Salem"]
    branch_factor = {"Chennai": 1.4, "Coimbatore": 1.0, "Madurai": 0.9,
                     "Tiruchirappalli": 0.8, "Salem": 0.7}
    categories = ["Textiles", "Electronics", "Groceries", "Stationery", "Home"]
    cat_share = {"Textiles": 0.32, "Electronics": 0.24, "Groceries": 0.22,
                 "Stationery": 0.10, "Home": 0.12}

    months = [f"2025-{m:02d}" for m in range(1, 13)]
    rows = []
    for m_idx, m in enumerate(months):
        # Seasonal pattern: peak in Oct-Dec (festival), trough Apr-Jun
        month_num = m_idx + 1
        seasonal = {1: 1.05, 2: 0.95, 3: 1.0, 4: 0.85, 5: 0.80, 6: 0.85,
                    7: 0.95, 8: 1.0, 9: 1.05, 10: 1.30, 11: 1.40, 12: 1.25}[month_num]

        for b in branches:
            base_revenue = 800_000 * branch_factor[b] * seasonal
            for c in categories:
                rev = base_revenue * cat_share[c] * random.uniform(0.85, 1.15)
                customers = int(rev / random.uniform(800, 1500))
                rows.append([m, b, c, round(rev, 2), customers])

    # Make Salem branch struggle in Q4 (cost creep / poor management)
    for r in rows:
        if r[1] == "Salem" and r[0] in ("2025-10", "2025-11", "2025-12"):
            r[3] = round(r[3] * 0.65, 2)   # 35% lower than expected

    with (DATA / "branch_sales_12m.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["Month", "Branch", "Category", "Revenue", "Customers"])
        w.writerows(rows)
    print(f"Case 1: {len(rows)} rows -> branch_sales_12m.csv")


# =====================================================================
# CASE 2 — Bharath Mobile telecom customer churn
#   columns: CustomerID, Tenure_months, Plan, MonthlyCharge, TotalSpend,
#            DataUsage_GB, ServiceCalls, AutoPay, Churned
# =====================================================================
def gen_case2():
    plans = ["Basic", "Standard", "Premium", "Family"]
    plan_charge = {"Basic": 199, "Standard": 399, "Premium": 699, "Family": 999}

    rows = []
    for i in range(1, 501):
        cid = f"BMC{i:05d}"
        tenure = max(1, int(random.gauss(28, 18)))     # months
        plan   = random.choices(plans, weights=[0.30, 0.35, 0.20, 0.15])[0]
        charge = plan_charge[plan] * random.uniform(0.95, 1.10)
        total  = round(charge * tenure * random.uniform(0.95, 1.05), 2)
        data_gb = round(random.uniform(2, 80), 1)
        calls = max(0, int(random.gauss(2, 2.5)))
        autopay = random.random() < 0.55

        # Churn drivers: low tenure, high service calls, low data usage,
        # no autopay, basic plan more likely
        churn_score = 0
        if tenure < 6:           churn_score += 0.30
        if calls >= 4:           churn_score += 0.25
        if data_gb < 5:          churn_score += 0.15
        if not autopay:          churn_score += 0.15
        if plan == "Basic":      churn_score += 0.10
        churn_score += random.uniform(-0.05, 0.10)
        churned = random.random() < churn_score

        rows.append([cid, tenure, plan, round(charge, 2), total,
                     data_gb, calls, "Yes" if autopay else "No",
                     "Yes" if churned else "No"])

    with (DATA / "telecom_customers.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["CustomerID", "Tenure_months", "Plan", "MonthlyCharge",
                    "TotalSpend", "DataUsage_GB", "ServiceCalls",
                    "AutoPay", "Churned"])
        w.writerows(rows)
    n_churn = sum(1 for r in rows if r[-1] == "Yes")
    print(f"Case 2: 500 customers ({n_churn} churned, {n_churn/5:.1f}%) -> telecom_customers.csv")


# =====================================================================
# CASE 3 — Lakshmi Textiles 3-year P&L + Balance Sheet
#   File 1: pnl.csv      (Year, Revenue, COGS, OpEx, InterestExpense, Tax)
#   File 2: balance.csv  (Year, CurrentAssets, FixedAssets, Inventory,
#                         Receivables, CurrentLiab, LongTermDebt, Equity)
# =====================================================================
def gen_case3():
    years = [2023, 2024, 2025]
    pnl_rows = []
    bal_rows = []
    rev = 12_50_00_000      # ₹12.5 Cr starting

    for y in years:
        # Modest growth, but margins thinning
        rev = rev * random.uniform(1.06, 1.12)
        cogs = rev * random.uniform(0.62, 0.66)
        opex = rev * random.uniform(0.18, 0.22)
        interest = 35_00_000 + random.uniform(-2_00_000, 5_00_000)
        ebt = rev - cogs - opex - interest
        tax = max(0, ebt) * 0.25
        pnl_rows.append([y, round(rev, 0), round(cogs, 0), round(opex, 0),
                         round(interest, 0), round(tax, 0)])

        # Balance sheet
        ca = rev * 0.28
        fa = rev * 0.42
        inv = rev * 0.18                # rising inventory (concerning)
        ar  = rev * 0.15
        cl  = rev * 0.20
        ltd = 4_00_00_000 - (y - 2023) * 30_00_000   # paying down debt
        equity = ca + fa - cl - ltd
        bal_rows.append([y, round(ca, 0), round(fa, 0), round(inv, 0),
                         round(ar, 0), round(cl, 0), round(ltd, 0),
                         round(equity, 0)])

    with (DATA / "pnl.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["Year", "Revenue", "COGS", "OpEx",
                    "InterestExpense", "Tax"])
        w.writerows(pnl_rows)

    with (DATA / "balance.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["Year", "CurrentAssets", "FixedAssets", "Inventory",
                    "Receivables", "CurrentLiab", "LongTermDebt", "Equity"])
        w.writerows(bal_rows)
    print("Case 3: 3y P&L + balance sheet -> pnl.csv, balance.csv")


def main():
    gen_case1()
    gen_case2()
    gen_case3()
    print("\nAll case study datasets written to", DATA)


if __name__ == "__main__":
    main()
