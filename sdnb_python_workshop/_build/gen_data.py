"""Generate all 7 CSV data files for the SDNB Python Workshop.

Realistic Indian business data, slightly imperfect (a few NaNs / outliers)
so students learn to handle real data.
"""

import csv
import random
from datetime import date, timedelta
from pathlib import Path

random.seed(20260427)  # workshop start date as seed -> reproducible builds

DATA = Path(__file__).resolve().parent.parent / "data"
DATA.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------------------------
# Shared pools
# ---------------------------------------------------------------------------
INDIAN_FIRST_NAMES = [
    "Priya", "Kavitha", "Lakshmi", "Meena", "Divya", "Anitha", "Devika",
    "Sangeetha", "Bhavya", "Aishwarya", "Rajesh", "Suresh", "Karthik",
    "Vignesh", "Arun", "Bharath", "Mohan", "Naveen", "Senthil", "Mani",
    "Pooja", "Revathi", "Saranya", "Hemalatha", "Janani", "Ramesh",
    "Gopal", "Hari", "Krishna", "Vasanth"
]
INDIAN_LAST_NAMES = [
    "Sharma", "Iyer", "Subramanian", "Krishnan", "Raj", "Murugan",
    "Pillai", "Nair", "Reddy", "Gupta", "Patel", "Shah", "Rao",
    "Menon", "Bose", "Chandran", "Balaji", "Natarajan"
]
CITIES = ["Chennai", "Bengaluru", "Mumbai", "Delhi", "Hyderabad",
          "Coimbatore", "Madurai", "Tiruchirappalli", "Salem"]


def full_name():
    return f"{random.choice(INDIAN_FIRST_NAMES)} {random.choice(INDIAN_LAST_NAMES)}"


# ---------------------------------------------------------------------------
# 1. sales_data.csv  (90 rows: Date, Product, Category, Units, Price, Region)
# ---------------------------------------------------------------------------
def gen_sales_data():
    products = [
        ("Silk Saree",          "Textiles",    2499.00),
        ("Cotton Saree",        "Textiles",     899.00),
        ("Bridal Lehenga",      "Textiles",    8999.00),
        ("Kurti Set",           "Textiles",    1299.00),
        ("Bluetooth Speaker",   "Electronics", 1999.00),
        ("Mobile Charger",      "Electronics",  349.00),
        ("LED Bulb 9W",         "Electronics",  149.00),
        ("Smart Watch",         "Electronics", 3499.00),
        ("Basmati Rice 5kg",    "Groceries",    549.00),
        ("Filter Coffee 500g",  "Groceries",    299.00),
        ("Toor Dal 1kg",        "Groceries",    149.00),
        ("Cooking Oil 1L",      "Groceries",    189.00),
        ("Notebook A4 200pg",   "Stationery",    89.00),
        ("Ball Pen Pack",       "Stationery",    49.00),
        ("Calculator",          "Stationery",   449.00),
        ("Bedsheet Double",     "Textiles",    1199.00),
    ]
    regions = ["Chennai", "Coimbatore", "Madurai", "Tiruchirappalli", "Salem"]

    rows = []
    start = date(2026, 1, 1)
    for i in range(90):
        d = start + timedelta(days=random.randint(0, 89))
        prod, cat, base_price = random.choice(products)
        units = random.randint(1, 25)
        # small price drift +/- 5%
        price = round(base_price * random.uniform(0.95, 1.05), 2)
        region = random.choice(regions)
        rows.append([d.isoformat(), prod, cat, units, price, region])

    # imperfections: 2 missing units, 1 missing region, 1 outlier
    rows[7][3] = ""           # missing units
    rows[42][3] = ""           # missing units
    rows[55][5] = ""           # missing region
    rows[80][3] = 250          # outlier huge order

    with (DATA / "sales_data.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["Date", "Product", "Category", "Units", "Price", "Region"])
        w.writerows(rows)


# ---------------------------------------------------------------------------
# 2. bank_transactions.csv (60 rows)
# ---------------------------------------------------------------------------
def gen_bank_transactions():
    descriptions_credit = [
        "Fee Collection - Semester", "Donation Received", "Bank Interest",
        "Govt Grant Disbursed", "Hostel Fee", "Library Fee Refund",
        "Workshop Income", "Alumni Contribution"
    ]
    descriptions_debit = [
        "Salary Payment", "Electricity Bill - TANGEDCO", "Internet Bill - ACT",
        "Stationery Purchase", "Lab Equipment", "Cleaning Services",
        "Security Services", "Annual Day Expenses", "Books Purchase",
        "Software License", "Travel Reimbursement"
    ]

    rows = []
    bal = 1_500_000.00
    start = date(2026, 1, 1)

    for i in range(60):
        d = start + timedelta(days=i * 2)
        is_credit = random.random() < 0.4
        if is_credit:
            desc = random.choice(descriptions_credit)
            amt = round(random.uniform(15000, 350000), 2)
            bal += amt
            rows.append([d.isoformat(), desc, "", round(amt, 2), round(bal, 2)])
        else:
            desc = random.choice(descriptions_debit)
            amt = round(random.uniform(2500, 95000), 2)
            bal -= amt
            rows.append([d.isoformat(), desc, round(amt, 2), "", round(bal, 2)])

    # one missing balance to simulate imperfection
    rows[33][4] = ""

    with (DATA / "bank_transactions.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["Date", "Description", "Debit", "Credit", "Balance"])
        w.writerows(rows)


# ---------------------------------------------------------------------------
# 3. inventory.csv (30 rows)
# ---------------------------------------------------------------------------
def gen_inventory():
    items = [
        ("P001", "Silk Saree - Red",       "Textiles",    18,  2499.00),
        ("P002", "Silk Saree - Green",     "Textiles",     5,  2499.00),
        ("P003", "Cotton Saree Pack",      "Textiles",    42,   899.00),
        ("P004", "Bridal Lehenga",         "Textiles",     3,  8999.00),
        ("P005", "Kurti - Medium",         "Textiles",    25,  1299.00),
        ("P006", "Kurti - Large",          "Textiles",    19,  1299.00),
        ("P007", "Bedsheet Double",        "Textiles",    14,  1199.00),
        ("P008", "Bluetooth Speaker",      "Electronics", 11,  1999.00),
        ("P009", "Mobile Charger Type-C",  "Electronics", 60,   349.00),
        ("P010", "LED Bulb 9W",            "Electronics", 120,  149.00),
        ("P011", "Smart Watch",            "Electronics",  6,  3499.00),
        ("P012", "Wired Earphones",        "Electronics", 38,   249.00),
        ("P013", "Power Bank 10000mAh",    "Electronics",  9,  1499.00),
        ("P014", "Basmati Rice 5kg",       "Groceries",   55,   549.00),
        ("P015", "Filter Coffee 500g",     "Groceries",   33,   299.00),
        ("P016", "Toor Dal 1kg",           "Groceries",   72,   149.00),
        ("P017", "Cooking Oil 1L",         "Groceries",   48,   189.00),
        ("P018", "Sugar 1kg",              "Groceries",   28,    49.00),
        ("P019", "Tea Powder 250g",        "Groceries",   21,   149.00),
        ("P020", "Notebook A4 200pg",      "Stationery",  90,    89.00),
        ("P021", "Ball Pen Pack of 10",    "Stationery", 130,    49.00),
        ("P022", "Calculator Casio",       "Stationery",  17,   449.00),
        ("P023", "Stapler",                "Stationery",  22,   199.00),
        ("P024", "A4 Paper Ream",          "Stationery",  44,   299.00),
        ("P025", "File Folder",            "Stationery",   8,    79.00),
        ("P026", "Marker Pens Set",        "Stationery",   2,   149.00),  # low stock
        ("P027", "Whiteboard 4x3",         "Stationery",   0,  2499.00),  # out of stock
        ("P028", "Highlighter Pack",       "Stationery",   4,    99.00),  # low stock
        ("P029", "Glue Stick",             "Stationery",  65,    35.00),
        ("P030", "Sticky Notes",           "Stationery",  39,    79.00),
    ]
    with (DATA / "inventory.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["ProductID", "Name", "Category", "Stock", "UnitPrice"])
        for r in items:
            w.writerow(r)


# ---------------------------------------------------------------------------
# 4. customer_ages.csv (100 rows)
# ---------------------------------------------------------------------------
def gen_customer_ages():
    rows = []
    for i in range(1, 101):
        cid = f"C{i:04d}"
        name = full_name()
        # bulk in 25-45 range with longer tails
        if random.random() < 0.65:
            age = random.randint(25, 45)
        elif random.random() < 0.5:
            age = random.randint(18, 25)
        else:
            age = random.randint(45, 70)
        city = random.choice(CITIES)
        seg = "Premium" if random.random() < 0.3 else "Regular"
        rows.append([cid, name, age, city, seg])

    # 2 missing ages to make it realistic
    rows[14][2] = ""
    rows[71][2] = ""

    with (DATA / "customer_ages.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["CustomerID", "Name", "Age", "City", "Segment"])
        w.writerows(rows)


# ---------------------------------------------------------------------------
# 5. ad_spend.csv (24 rows)
# ---------------------------------------------------------------------------
def gen_ad_spend():
    months = []
    for y in (2024, 2025):
        for m in range(1, 13):
            months.append(f"{y}-{m:02d}")
    channels = ["Digital", "Print", "Outdoor", "Social"]
    rows = []
    for i, m in enumerate(months):
        ch = channels[i % 4]
        spend = round(random.uniform(40000, 220000), 2)
        # sales = 8 * spend + noise + Q4 seasonal bump
        month_num = int(m.split("-")[1])
        bump = 1.25 if month_num in (10, 11, 12) else 1.0
        revenue = round((spend * 8 * bump) + random.uniform(-50000, 80000), 2)
        rows.append([m, spend, revenue, ch])

    with (DATA / "ad_spend.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["Month", "AdSpend", "SalesRevenue", "Channel"])
        w.writerows(rows)


# ---------------------------------------------------------------------------
# 6. exam_marks.csv (40 rows)
# ---------------------------------------------------------------------------
def gen_exam_marks():
    rows = []
    for i in range(1, 41):
        roll = f"R{2026000 + i}"
        name = full_name()
        # base ability per student
        ability = random.gauss(65, 15)
        marks = []
        for subj_offset in (0, 5, -3, 2, 4):
            m = ability + subj_offset + random.gauss(0, 8)
            m = max(15, min(99, round(m)))
            marks.append(m)
        rows.append([roll, name, *marks])

    # add one fail edge case
    rows[7][2:] = [22, 30, 18, 35, 28]
    # and one star
    rows[2][2:] = [98, 95, 99, 97, 96]

    with (DATA / "exam_marks.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["RollNo", "Name", "Maths", "Accounts", "Economics",
                    "Commerce", "English"])
        w.writerows(rows)


# ---------------------------------------------------------------------------
# 7. monthly_expenses.csv (12 rows)
# ---------------------------------------------------------------------------
def gen_monthly_expenses():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    rows = []
    for i, m in enumerate(months):
        rent      = 85000
        salary    = 320000 + i * 1500 + random.randint(-2000, 4000)
        utilities = 12000 + random.randint(-1500, 3500)
        marketing = 45000 + random.randint(-15000, 35000)
        misc      = 15000 + random.randint(-3000, 12000)
        rows.append([m, rent, salary, utilities, marketing, misc])

    with (DATA / "monthly_expenses.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["Month", "Rent", "Salary", "Utilities", "Marketing", "Misc"])
        w.writerows(rows)


def main():
    gen_sales_data()
    gen_bank_transactions()
    gen_inventory()
    gen_customer_ages()
    gen_ad_spend()
    gen_exam_marks()
    gen_monthly_expenses()
    print("✅ Generated 7 CSV files in", DATA)
    for p in sorted(DATA.glob("*.csv")):
        with p.open(encoding="utf-8") as f:
            n = sum(1 for _ in f) - 1
        print(f"  - {p.name:30s}  {n:4d} rows")


if __name__ == "__main__":
    main()
