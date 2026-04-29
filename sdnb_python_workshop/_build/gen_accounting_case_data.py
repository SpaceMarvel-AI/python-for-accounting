"""Generate datasets for 3 accounting case studies (Cases 4-6)."""

import csv
import random
from datetime import date, timedelta
from pathlib import Path

random.seed(20260429)

DATA = Path(__file__).resolve().parent.parent / "case_studies" / "data"
DATA.mkdir(parents=True, exist_ok=True)


# =====================================================================
# CASE 4 — Accounts Receivable Aging
#   columns: InvoiceNo, InvoiceDate, CustomerCode, CustomerName,
#            BillAmount, AmountReceived, Outstanding
# =====================================================================
def gen_case4():
    customer_pool = [
        ("C001", "Anand Trading Co"),
        ("C002", "Bhuvana Garments"),
        ("C003", "Chennai Imports Pvt Ltd"),
        ("C004", "Devi Stores"),
        ("C005", "Eswar Enterprises"),
        ("C006", "Fortune Distributors"),
        ("C007", "Geetha Silks"),
        ("C008", "Hariharan & Sons"),
        ("C009", "Indus Apparels"),
        ("C010", "Jaya Marketing"),
        ("C011", "Kannan Wholesale"),
        ("C012", "Lakshmi Retail"),
    ]
    # Customer "personality": payment behaviour
    profiles = {
        "good"   : (0.85, 1.00),     # paid 85-100%
        "slow"   : (0.40, 0.80),     # partial payments
        "delinq" : (0.00, 0.30),     # mostly unpaid
    }
    cust_profile = {
        "C001": "good", "C002": "good",   "C003": "slow",
        "C004": "good", "C005": "delinq", "C006": "slow",
        "C007": "good", "C008": "good",   "C009": "delinq",
        "C010": "slow", "C011": "good",   "C012": "delinq",
    }

    today = date(2026, 4, 30)
    rows = []
    inv_no = 5001

    for cust_code, cust_name in customer_pool:
        n = random.randint(2, 8)
        for _ in range(n):
            days_old = random.choices(
                [random.randint(0, 30),    # current
                 random.randint(31, 60),   # 31-60
                 random.randint(61, 90),   # 61-90
                 random.randint(91, 180),  # > 90
                 ],
                weights=[0.35, 0.30, 0.20, 0.15]
            )[0]
            inv_date = today - timedelta(days=days_old)
            amount = round(random.uniform(15000, 250000), 2)
            lo, hi = profiles[cust_profile[cust_code]]
            received = round(amount * random.uniform(lo, hi), 2)
            outstanding = round(amount - received, 2)
            rows.append([f"INV-{inv_no:05d}", inv_date.isoformat(),
                         cust_code, cust_name, amount, received, outstanding])
            inv_no += 1

    # Keep only invoices with outstanding > 0 (others are fully paid)
    rows = [r for r in rows if r[6] > 0]

    with (DATA / "ar_invoices.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["InvoiceNo", "InvoiceDate", "CustomerCode",
                    "CustomerName", "BillAmount", "AmountReceived",
                    "Outstanding"])
        w.writerows(rows)
    print(f"Case 4: {len(rows)} outstanding invoices -> ar_invoices.csv")


# =====================================================================
# CASE 5 — Inventory transactions for FIFO / LIFO / Weighted Average
#   columns: Date, Type, Quantity, UnitPrice
#   Type ∈ {Purchase, Sale}
# =====================================================================
def gen_case5():
    txns = [
        # (date, type, qty, unit price)  — applies to one SKU: "Cotton Saree"
        ("2026-01-05", "Purchase",  500, 320.00),
        ("2026-01-12", "Purchase",  300, 340.00),
        ("2026-01-20", "Sale",      400, None),
        ("2026-02-02", "Purchase",  400, 360.00),
        ("2026-02-15", "Sale",      350, None),
        ("2026-03-01", "Purchase",  600, 380.00),
        ("2026-03-10", "Purchase",  200, 400.00),
        ("2026-03-22", "Sale",      500, None),
        ("2026-04-05", "Purchase",  300, 410.00),
        ("2026-04-18", "Sale",      450, None),
    ]

    rows = []
    for d, kind, qty, up in txns:
        rows.append([d, kind, qty, "" if up is None else f"{up:.2f}"])

    with (DATA / "inventory_transactions.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["Date", "Type", "Quantity", "UnitPrice"])
        w.writerows(rows)
    print(f"Case 5: {len(rows)} inventory transactions -> inventory_transactions.csv")


# =====================================================================
# CASE 6 — Budget vs Actual P&L (departmental)
#   columns: Department, LineItem, Budget, Actual
# =====================================================================
def gen_case6():
    departments = ["Manufacturing", "Sales & Marketing", "Logistics",
                   "HR", "IT", "Finance"]

    line_items = [
        # (item, budget_per_dept dict, actual_variance_range)
        ("Salaries", {"Manufacturing": 4_50_000, "Sales & Marketing": 3_20_000,
                      "Logistics": 2_10_000, "HR": 1_80_000,
                      "IT": 2_50_000, "Finance": 1_60_000},
         (-0.05, 0.08)),
        ("Rent", {d: 80_000 for d in departments},
         (0.0, 0.0)),
        ("Utilities", {d: 25_000 for d in departments},
         (-0.10, 0.20)),
        ("Travel", {"Manufacturing": 35_000, "Sales & Marketing": 1_50_000,
                    "Logistics": 60_000, "HR": 25_000,
                    "IT": 40_000, "Finance": 30_000},
         (-0.20, 0.40)),
        ("Marketing", {"Sales & Marketing": 2_50_000,
                       "Manufacturing": 0, "Logistics": 0,
                       "HR": 0, "IT": 0, "Finance": 0},
         (-0.10, 0.30)),
        ("Software & Licenses", {"IT": 1_20_000,
                                 "Sales & Marketing": 25_000,
                                 "Finance": 30_000,
                                 "Manufacturing": 15_000,
                                 "Logistics": 10_000, "HR": 12_000},
         (-0.05, 0.50)),     # IT systems often overspend
        ("Training", {d: 35_000 for d in departments},
         (-0.30, 0.10)),
        ("Misc / Office", {d: 18_000 for d in departments},
         (-0.10, 0.25)),
    ]

    rows = []
    for item, dept_map, (lo, hi) in line_items:
        for d in departments:
            budget = dept_map.get(d, 0)
            if budget == 0:
                continue
            actual = budget * (1 + random.uniform(lo, hi))
            rows.append([d, item, round(budget, 2), round(actual, 2)])

    # Stress one specific department: Sales & Marketing massively over on Travel
    for r in rows:
        if r[0] == "Sales & Marketing" and r[1] == "Travel":
            r[3] = round(r[2] * 1.65, 2)         # 65% over budget — flag

    with (DATA / "budget_vs_actual.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["Department", "LineItem", "Budget", "Actual"])
        w.writerows(rows)
    print(f"Case 6: {len(rows)} budget lines -> budget_vs_actual.csv")


def main():
    gen_case4()
    gen_case5()
    gen_case6()
    print("\nAll accounting case datasets written to", DATA)


if __name__ == "__main__":
    main()
