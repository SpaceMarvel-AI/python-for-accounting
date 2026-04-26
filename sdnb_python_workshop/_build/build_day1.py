"""Build Day1_Python_Basics_and_Finance.ipynb."""

from nb_helpers import Notebook, COLAB_SETUP

nb = Notebook()

# ── COVER ────────────────────────────────────────────────────────────────
nb.md("""
# 📘 Day 1 — Python Basics & Finance Calculators
**Shrimathi Devkunvar Nanalal Bhatt Vaishnav College for Women, Chromepet**

**Programme:** Business Analytics Using Python — Hands-On Sessions
**Date:** Monday, 27 April 2026 | **Duration:** 9:30 AM – 1:00 PM (3 hours)

---

### 🎯 What will you be able to do by the end of today?
- ✅ Build a working **Simple Interest & Compound Interest calculator**
- ✅ Create a **USD → INR currency converter** with customs duty
- ✅ Record and summarise **10 sales entries** at end of day
- ✅ Calculate **monthly savings** automatically and grade them

> **No prior programming experience required.** If you've used Excel and Tally, you already think the way Python wants you to think.
""")

nb.code(COLAB_SETUP)

# ── SECTION 1 — Welcome & Setup ─────────────────────────────────────────
nb.md("""
## 🪔 Section 1 — Welcome & Setup *(15 min)*

### Why Python for Commerce?

Think of Python as a **very smart calculator + Tally + Excel combined** — but you give it instructions in plain English-like language.

| Task | In Excel | In Tally | In Python |
|------|----------|----------|-----------|
| Calculate GST on a sale | `=A1 * 18%` | Journal Entry → GST Output | `gst = price * 0.18` |
| Total of a column | `=SUM(B2:B100)` | Trial Balance | `sum(sales_list)` |
| Filter sales > ₹10,000 | AutoFilter | Group filter | `[s for s in sales if s > 10000]` |
| Average of marks | `=AVERAGE(...)` | — | `sum(marks) / len(marks)` |

**The good news:** the *thinking* is the same. The *typing* is different.
""")

nb.code('''# Print our workshop title as a banner — this is just plain printing for now
print("=" * 60)
print("    SDNB BUSINESS ANALYTICS USING PYTHON — DAY 1")
print("    Python Basics & Finance Calculators")
print("    Date: 27-Apr-2026  |  Duration: 3 hours")
print("=" * 60)
''')

# ── SECTION 2 — Variables & Data Types ──────────────────────────────────
nb.md("""
## 🗄️ Section 2 — Variables & Data Types *(30 min)*

> **Analogy:** Variables are like **labelled drawers in your office cabinet**.
> Just like you label a drawer "Petty Cash" and put ₹500 inside, in Python you write:
> `petty_cash = 500`

There are **5 basic types** of "stuff" you'll put in those drawers:

| Type | What it holds | Real-world example |
|------|---------------|--------------------|
| `int`   | Whole number      | Number of invoices = 45 |
| `float` | Decimal (money)   | Product price = 2499.99 |
| `str`   | Text              | Company = "SDNB Textiles" |
| `bool`  | True / False      | Is GST registered = True |
| `None`  | Empty / blank     | Email not provided yet |
""")

# 2A — int
nb.md("""
### A) Integer (`int`) — whole numbers

Use these for things you **count**: invoices, employees, units sold.
""")
nb.code('''# Whole numbers — no decimal point
number_of_invoices = 45      # 45 invoices issued today
employees_count    = 12      # 12 staff in the office

# type() tells us what kind of value is stored
print("Type of number_of_invoices:", type(number_of_invoices))

# Arithmetic — same as a calculator
total = number_of_invoices + 5    # add  5 more invoices
diff  = number_of_invoices - 10   # cancel 10 invoices
prod  = employees_count * 8       # 8 working hours per employee
quot  = number_of_invoices // 7   # full weeks of invoices (integer divide)
rem   = number_of_invoices %  7   # leftover invoices not in full week

# f-string = formatted string, lets us drop variables right inside the text
print(f"Total invoices after adding 5    : {total}")
print(f"Invoices after 10 cancelled      : {diff}")
print(f"Total working hours              : {prod}")
print(f"Full 7-day weeks of invoicing    : {quot}")
print(f"Leftover invoices                : {rem}")
''')

nb.md("""
**🧠 What just happened?**
We stored whole numbers in two drawers, asked Python what type they were, and did the same arithmetic you'd do on a calculator. The `//` operator gives the *quotient* (full weeks); `%` gives the *remainder* (leftover invoices).
""")

# 2B — float
nb.md("""
### B) Float (`float`) — decimal numbers (money amounts)

Use these for **money, percentages, weights** — anything that can have a decimal.
""")
nb.code('''# Decimals — for amounts in rupees and paise
product_price = 2499.99       # premium saree
gst_rate      = 0.18          # 18% GST as a decimal

gst_amount = product_price * gst_rate
total      = product_price + gst_amount

# round(value, 2) — round to 2 decimal places, like a paise rounding in ledger
print("─────────────────────────────────")
print(f"Product   : Premium Saree")
print(f"Price     : ₹{product_price:,.2f}")
print(f"GST (18%) : ₹{round(gst_amount, 2):,.2f}")
print(f"Total     : ₹{round(total, 2):,.2f}")
print("─────────────────────────────────")
''')

nb.md("""
**⚠️ Why does the computer sometimes show `0.30000000000000004`?**

Computers store decimals in binary, not in decimal. So tiny rounding errors creep in — exactly like how 1/3 written as a decimal is 0.33333… and never ends. Watch:
""")
nb.code('''# A famous floating-point surprise
print(0.1 + 0.2)                    # → 0.30000000000000004
print(round(0.1 + 0.2, 2))          # → 0.3   (this is what you want for money)

# Rule for accounting work: ALWAYS round money to 2 decimal places before printing.
''')

nb.md("""
**🧠 What just happened?**
The first line shows the raw machine answer — ugly and wrong-looking. The second line uses `round(..., 2)` to clean it up. **In all financial code, round amounts before showing them**, just like you would round paise in a ledger.
""")

# 2C — string
nb.md("""
### C) String (`str`) — text

Use these for **names, descriptions, invoice numbers, addresses**.
""")
nb.code('''# Strings live inside quotes (single or double — both are fine)
company_name   = "SDNB Textiles Pvt Ltd"
invoice_number = "INV-2026-001"
seller_city    = "Chennai"

# Useful operations on text
print(f"Length of company name : {len(company_name)} characters")
print(f"Upper case             : {company_name.upper()}")
print(f"Lower case             : {company_name.lower()}")
print(f"Whitespace stripped    : '{'   Chennai   '.strip()}'")

# Concatenation — joining text with +
header = "Invoice from " + company_name + " | " + seller_city
print(header)

# f-string version (cleaner)
header2 = f"Invoice {invoice_number} | {company_name} | {seller_city}"
print(header2)
''')

nb.md("""
**✏️ Try It Yourself:** Build an invoice header line that says:
`SDNB TEXTILES PVT LTD | INV-2026-042 | Chennai - 600044`
using **f-strings** and the `.upper()` method.
""")

# 2D — bool
nb.md("""
### D) Boolean (`bool`) — True / False decisions

> **Analogy:** Like a **YES/NO checkbox** on a form.

Booleans are how Python answers "yes-or-no" questions. They power every `if/else` decision.
""")
nb.code('''is_gst_registered   = True
is_payment_received = False

print(f"Is the seller GST registered? {is_gst_registered}")
print(f"Has the customer paid?        {is_payment_received}")

# Booleans are usually the result of a comparison
revenue = 75000
target  = 50000
target_achieved = revenue > target
print(f"Revenue ₹{revenue:,} > Target ₹{target:,}?  →  {target_achieved}")
''')

# 2E — None
nb.md("""
### E) `None` — empty / missing

> **Analogy:** Like a **blank cell in Excel** or an unfilled field in a ledger.

`None` is Python's way of saying "we don't have a value yet". Different from `0` or `""` — it specifically means *nothing has been recorded*.
""")
nb.code('''customer_email = None         # customer didn't share email at counter

if customer_email is None:
    print("⚠️  Email missing — please collect at next visit.")
else:
    print(f"Email on file: {customer_email}")
''')

# ── SECTION 3 — Input & Operators ────────────────────────────────────────
nb.md("""
## ⌨️ Section 3 — User Input & Operators *(20 min)*

> **Analogy:** `input()` is like asking a question on a paper form — the user fills in the blank and Python uses their answer.

The catch: `input()` always returns **text** (a string), even if the user typed numbers. We must convert it to a number using `float()` or `int()` before doing arithmetic.

The cell below has the input lines as **comments** so the notebook runs top-to-bottom without pausing for keyboard input. Uncomment them when you want the interactive version.
""")
nb.code('''# ── INTERACTIVE VERSION (uncomment to run) ──
# principal = float(input("Enter principal amount (₹): "))
# rate      = float(input("Enter annual interest rate (%): "))
# years     = int(input("Enter number of years: "))

# ── Hardcoded version so the notebook keeps running smoothly ──
principal = 100000.0
rate      = 8.0
years     = 5

print(f"Principal entered : ₹{principal:,.2f}")
print(f"Rate entered      : {rate}% per annum")
print(f"Years entered     : {years} year(s)")
''')

nb.md("""
**⚠️ Common error:** if you forget the `float()` and write `principal = input(...)` then try to do arithmetic, Python complains:
`TypeError: can't multiply sequence by non-int of type 'float'`
That's like trying to add **apples and oranges** in your accounts — type mismatch.

### Arithmetic operators with business meaning

| Op | Meaning | Business example |
|----|---------|------------------|
| `+` | add        | Adding invoice amounts |
| `-` | subtract   | Profit = Revenue − Cost |
| `*` | multiply   | Total = Qty × Price |
| `/` | divide     | Cost per unit = Total ÷ Units |
| `//`| floor div  | How many full cartons fit? |
| `%` | remainder  | Leftover units after packing |
| `**`| power      | Used in Compound Interest |
""")

nb.code('''units_sold  = 47
carton_size = 12
total_amount = 9450
cost_price   = 7200

revenue          = total_amount
profit           = revenue - cost_price
cost_per_unit    = total_amount / units_sold
full_cartons     = units_sold // carton_size
leftover_units   = units_sold %  carton_size
power_example    = (1 + 0.08) ** 5     # CI growth factor over 5 years @ 8%

print(f"Profit               : ₹{profit:,.2f}")
print(f"Cost per unit        : ₹{cost_per_unit:,.2f}")
print(f"Full cartons packed  : {full_cartons}")
print(f"Leftover units       : {leftover_units}")
print(f"CI growth factor (5y): {power_example:.4f}")
''')

nb.md("""
### Comparison & logical operators

`==`, `!=`, `>`, `<`, `>=`, `<=` answer **yes/no questions** about numbers.
`and`, `or`, `not` combine multiple yes/no answers.
""")
nb.code('''revenue       = 75000
target        = 50000
stock         = 8
reorder_level = 10

print(f"Revenue ≥ target?   {revenue >= target}")
print(f"Stock < reorder?    {stock < reorder_level}")

# Loan eligibility = salary > 25,000 AND credit score >= 700
salary       = 32000
credit_score = 720
eligible = (salary > 25000) and (credit_score >= 700)
print(f"Loan eligible?      {eligible}")
''')

# ── SECTION 4 — if/elif/else + Loops ────────────────────────────────────
nb.md("""
## 🔀 Section 4 — Decisions & Loops *(30 min)*

> **Analogy:** `if / else` is like the **decision column in a ledger**:
> IF the balance is positive → write it in the *Debit* column,
> ELSE write it in the *Credit* column.

### A) GST Slab Calculator using `if / elif / else`

| Bill amount | GST rate |
|-------------|----------|
| Below ₹1,000 | 5% |
| ₹1,000 – ₹5,000 | 12% |
| ₹5,000 – ₹10,000 | 18% |
| Above ₹10,000 | 28% |
""")
nb.code('''bill_amount = 6750.00     # try changing this and re-running

if bill_amount < 1000:
    gst_rate = 0.05
    slab     = "5% — small purchase"
elif bill_amount < 5000:
    gst_rate = 0.12
    slab     = "12% — regular purchase"
elif bill_amount < 10000:
    gst_rate = 0.18
    slab     = "18% — bulk purchase"
else:
    gst_rate = 0.28
    slab     = "28% — luxury purchase"

gst   = bill_amount * gst_rate
total = bill_amount + gst

print("════════════════════════════════════════")
print("           GST CALCULATION              ")
print("════════════════════════════════════════")
print(f"Bill Amount    : ₹{bill_amount:>10,.2f}")
print(f"Slab           : {slab}")
print(f"GST @ {int(gst_rate*100)}%      : ₹{gst:>10,.2f}")
print(f"Total Payable  : ₹{total:>10,.2f}")
print("════════════════════════════════════════")
''')

# B — for loop
nb.md("""
### B) `for` loop

> **Analogy:** "Like going through each row in a ledger book one by one."
""")
nb.code('''# Example 1 — list of product prices
product_prices = [499, 1299, 2499, 799, 3999]
print("Product Price List:")
for serial, price in enumerate(product_prices, start=1):
    print(f"  {serial}. ₹{price:,}")

print()

# Example 2 — month numbers
months = ["Apr", "May", "Jun", "Jul", "Aug", "Sep"]
for i, m in enumerate(months, start=1):
    print(f"Month {i:2d}: {m}")

print()

# Example 3 — simulate 10 transaction entries
print("Simulating 10 transaction entries:")
for txn in range(1, 11):
    amount = 1000 * txn        # mock amount
    print(f"  Txn #{txn:02d}  →  ₹{amount:,}")
''')

# C — while loop
nb.md("""
### C) `while` loop

> **Analogy:** "Keep checking outstanding invoices **WHILE** there are unpaid ones."
""")
nb.code('''# Keep adding items to a shopping bill while total stays below ₹10,000
items   = [(1499, "Saree"), (799, "Kurti"), (3499, "Watch"),
           (149, "Pen"), (2999, "Bedsheet"), (4999, "Lehenga")]

bill    = 0
counter = 0

while bill < 10000 and counter < len(items):
    price, name = items[counter]
    if bill + price > 10000:
        print(f"  Skip {name} (₹{price}) — would exceed ₹10,000")
        break
    bill += price
    counter += 1
    print(f"  Added {name:10s}  ₹{price:>5,}   (running total ₹{bill:,})")

print(f"\\nFinal bill: ₹{bill:,}")
''')

# D — nested loop
nb.md("""
### D) Nested loop — pricing grid

A pricing matrix where rows = quantity tiers, columns = discount levels.
""")
nb.code('''base_price = 1000
quantities = [10, 50, 100]            # 3 quantity tiers
discounts  = [0.00, 0.05, 0.10, 0.15] # 4 discount levels

print(f"{'Qty':>5} | " + " ".join(f"{int(d*100):>3d}%" for d in discounts))
print("-" * 35)
for q in quantities:
    row = f"{q:>5} | "
    for d in discounts:
        unit  = base_price * (1 - d)
        total = unit * q
        row  += f"{int(total/1000):>3d}k "
    print(row)
''')

# ── SECTION 5 — Lists & Dictionaries ─────────────────────────────────────
nb.md("""
## 📋 Section 5 — Lists & Dictionaries *(25 min)*

### A) Lists

> **Analogy:** A list is like a **column in your Excel sheet** — an ordered collection you can add to, remove from, sort, or loop through.
""")
nb.code('''product_prices = [499, 1299, 2499, 799, 3999, 149, 599, 999, 1799, 2999]

print("First product price :", product_prices[0])    # indexing from 0
print("Last  product price :", product_prices[-1])   # negative index = from end
print("Middle 3 prices     :", product_prices[2:5])  # slicing [start:stop]

# In-place modifications
product_prices.append(4999)            # add a new product
product_prices.remove(149)             # remove the LED bulb pack
product_prices.sort()                  # sort ascending
print("After edits         :", product_prices)

# Built-in summaries
total_value = sum(product_prices)
average     = total_value / len(product_prices)
print()
print("════════ PRICE ANALYSIS ════════")
print(f"Number of products : {len(product_prices)}")
print(f"Cheapest           : ₹{min(product_prices):,}")
print(f"Most expensive     : ₹{max(product_prices):,}")
print(f"Average price      : ₹{average:,.2f}")
print(f"Total catalogue    : ₹{total_value:,}")
print("════════════════════════════════")
''')

# B — Dictionaries
nb.md("""
### B) Dictionaries

> **Analogy:** A dictionary is like a **customer record card** — each field has a label (key) and a value.
""")
nb.code('''customer = {
    "name"        : "Priya Sharma",
    "account_no"  : "SB-2026-001",
    "balance"     : 45000.00,
    "city"        : "Chennai",
    "is_premium"  : True,
}

# Access by key
print("Customer name :", customer["name"])
print("City          :", customer["city"])

# Update a value
customer["balance"] = 47500.00

# Add a new key
customer["email"] = "priya.sharma@example.com"

# Loop through items
print("\\n──── ACCOUNT STATEMENT ────")
for field, value in customer.items():
    label = field.replace("_", " ").title()
    print(f"{label:14s}: {value}")
print("───────────────────────────")
''')

nb.md("""
### List of dictionaries — a mini database
""")
nb.code('''sales_records = [
    {"date": "27-Apr-2026", "product": "Silk Saree",   "amount": 2499},
    {"date": "27-Apr-2026", "product": "Kurti Set",    "amount": 1299},
    {"date": "27-Apr-2026", "product": "Bluetooth Spk","amount": 1999},
    {"date": "27-Apr-2026", "product": "Bedsheet",     "amount": 1199},
    {"date": "27-Apr-2026", "product": "Filter Coffee","amount":  299},
]

total = 0
print(f"{'Date':<12s} {'Product':<16s} {'Amount':>10s}")
print("-" * 42)
for record in sales_records:
    total += record["amount"]
    print(f"{record['date']:<12s} {record['product']:<16s} ₹{record['amount']:>8,}")
print("-" * 42)
print(f"{'TOTAL':<28s} ₹{total:>8,}")
''')

# ── SECTION 6 — Unit I exercises ─────────────────────────────────────────
nb.md("""
## 💼 Section 6 — Unit I: Financial Calculators *(60 min — main exercises)*

These four exercises bring everything together. Each one has:
1. A real-world scenario
2. The formula
3. A worked example with hardcoded values
4. An interactive version (commented — uncomment to use `input()`)
5. A formatted business-document output
""")

# EX 1 — Simple & Compound Interest
nb.md("""
### Exercise 1 — Simple Interest & Compound Interest Calculator

**Scenario:** *You are a Junior Accountant at Lakshmi Finance Ltd. A client wants to invest ₹1,00,000. Show them how much they will earn with Simple Interest vs Compound Interest over 5 years at 8% p.a.*

**Formulas:**

```
Simple Interest    = (Principal × Rate × Time) / 100
Compound Interest  = Principal × (1 + Rate/100)^Time  −  Principal
Total Amount (SI)  = Principal + Simple Interest
Total Amount (CI)  = Principal × (1 + Rate/100)^Time
```
""")
nb.code('''def investment_report(principal, rate, time):
    """Print SI vs CI comparison for given principal/rate/time."""
    si              = (principal * rate * time) / 100
    maturity_si     = principal + si
    maturity_ci     = principal * (1 + rate / 100) ** time
    ci              = maturity_ci - principal
    extra_with_ci   = maturity_ci - maturity_si

    print("════════════════════════════════════════════════")
    print("        INVESTMENT COMPARISON REPORT            ")
    print("        Lakshmi Finance Ltd | FD Advisory Desk  ")
    print("════════════════════════════════════════════════")
    print(f"Principal Amount   : ₹{principal:>14,.2f}")
    print(f"Interest Rate      : {rate:>14.2f}% per annum")
    print(f"Investment Period  : {time:>14d} Years")
    print("------------------------------------------------")
    print(f"{'':<20s}{'SI':>14s}{'CI':>14s}")
    print(f"Interest Earned    {si:>14,.2f}{ci:>14,.2f}")
    print(f"Maturity Amount    {maturity_si:>14,.2f}{maturity_ci:>14,.2f}")
    print(f"Extra with CI      {'':>14s}₹{extra_with_ci:>13,.2f}  (Choose CI!)")
    print("════════════════════════════════════════════════")

    # Year-by-year CI growth schedule
    print("\\nYear-by-year CI growth schedule:")
    print(f"{'Year':>6s}  {'Balance':>14s}  {'Yearly Gain':>14s}")
    prev = principal
    for y in range(1, time + 1):
        bal  = principal * (1 + rate / 100) ** y
        gain = bal - prev
        print(f"{y:>6d}  ₹{bal:>13,.2f}  ₹{gain:>13,.2f}")
        prev = bal


# Worked example — Mrs. Lakshmi
investment_report(principal=100000, rate=8, time=5)

# Interactive version (uncomment to use)
# p = float(input("Principal (₹): "))
# r = float(input("Rate (% p.a.): "))
# t = int  (input("Years: "))
# investment_report(p, r, t)
''')

# EX 2 — Currency converter
nb.md("""
### Exercise 2 — USD → INR Currency Converter

**Scenario:** *Your college is importing lab equipment worth $2,500 from the USA. The current exchange rate is ₹83.50 per dollar. Calculate the INR cost, add 5% customs duty, and show the total landed cost.*
""")
nb.code('''def import_voucher(usd_amount, fx_rate, duty_pct):
    base_inr   = usd_amount * fx_rate
    duty       = base_inr * duty_pct / 100
    landed     = base_inr + duty

    print("════════════════════════════════════════════════")
    print("        IMPORT PURCHASE VOUCHER                 ")
    print("        SDNB College — Procurement Department   ")
    print("════════════════════════════════════════════════")
    print(f"Invoice Amount (USD) : ${usd_amount:>14,.2f}")
    print(f"Exchange Rate        : ₹{fx_rate:>14,.2f} per USD")
    print(f"Base Cost (INR)      : ₹{base_inr:>14,.2f}")
    print(f"Customs Duty ({duty_pct:.0f}%)    : ₹{duty:>14,.2f}")
    print("------------------------------------------------")
    print(f"TOTAL LANDED COST    : ₹{landed:>14,.2f}")
    print("════════════════════════════════════════════════")
    return landed


# Hardcoded example
import_voucher(usd_amount=2500, fx_rate=83.50, duty_pct=5)

# Interactive version (uncomment)
# u = float(input("Amount in USD: $"))
# f = float(input("FX rate (₹ per $): "))
# d = float(input("Customs duty %: "))
# import_voucher(u, f, d)

# Mini conversion table
print("\\nQuick Reference (FX = ₹83.50):")
print(f"{'USD':>10s}  →  {'INR':>14s}")
print("-" * 30)
for usd in [100, 500, 1000, 2500, 5000]:
    print(f"${usd:>9,}  →  ₹{usd*83.50:>12,.2f}")
''')

# EX 3 — Sales tracker 10 entries
nb.md("""
### Exercise 3 — End-of-Day Sales Tracker (10 entries)

**Scenario:** *You are the Sales Executive at Chennai Textiles. Enter today's 10 sales transactions and generate an end-of-day sales summary.*
""")
nb.code('''# We use a hardcoded list so the notebook runs end-to-end.
# To make it interactive, replace this with the while-loop version below.

todays_sales = [3450, 1200, 5400, 2780, 950, 4250, 800,
                3100, 2860, 1810]

# ── INTERACTIVE while-loop version (uncomment to use) ──
# todays_sales = []
# count = 1
# while count <= 10:
#     amt = float(input(f"Enter amount of sale #{count}: ₹"))
#     todays_sales.append(amt)
#     count += 1

total   = sum(todays_sales)
average = total / len(todays_sales)
above_avg = sum(1 for s in todays_sales if s > average)

print("════════════════════════════════════════════════")
print("        END-OF-DAY SALES SUMMARY                ")
print("        Chennai Textiles | Date: 27-Apr-2026    ")
print("════════════════════════════════════════════════")
for i, s in enumerate(todays_sales, start=1):
    print(f"  Sale {i:>2d}  :  ₹{s:>10,.2f}")
print("------------------------------------------------")
print(f"  Total Sales    : ₹{total:>10,.2f}")
print(f"  Average Sale   : ₹{average:>10,.2f}")
print(f"  Highest Sale   : ₹{max(todays_sales):>10,.2f}")
print(f"  Lowest Sale    : ₹{min(todays_sales):>10,.2f}")
print(f"  # above average: {above_avg} of {len(todays_sales)}")
print("════════════════════════════════════════════════")
''')

# EX 4 — Monthly savings
nb.md("""
### Exercise 4 — Monthly Savings Calculator

**Scenario:** *Meena, a Junior Accountant, wants to track if she is saving enough for her annual vacation fund. Help her build a savings tracker.*

Savings rate grading:
- **>30%** = Excellent 🌟
- **20–30%** = Good ✅
- **10–20%** = Okay ⚠️
- **<10%** = Needs Work ❌
""")
nb.code('''def savings_statement(income, fixed_expenses, variable_expenses):
    total_expense = fixed_expenses + variable_expenses
    savings       = income - total_expense
    rate_pct      = (savings / income) * 100 if income else 0
    annual        = savings * 12

    if rate_pct > 30:
        grade = "Excellent 🌟"
    elif rate_pct >= 20:
        grade = "Good ✅"
    elif rate_pct >= 10:
        grade = "Okay ⚠️"
    else:
        grade = "Needs Work ❌"

    print("════════════════════════════════════════════════")
    print("        PERSONAL FINANCE STATEMENT              ")
    print("        Account Holder: Meena                   ")
    print("════════════════════════════════════════════════")
    print(f"Monthly Income          : ₹{income:>12,.2f}")
    print(f"Fixed Expenses          : ₹{fixed_expenses:>12,.2f}")
    print(f"Variable Expenses       : ₹{variable_expenses:>12,.2f}")
    print("------------------------------------------------")
    print(f"Total Expenses          : ₹{total_expense:>12,.2f}")
    print(f"Monthly Savings         : ₹{savings:>12,.2f}")
    print(f"Savings Rate            :  {rate_pct:>11.2f}%")
    print(f"Grade                   :  {grade}")
    print(f"Projected Annual Savings: ₹{annual:>12,.2f}")
    print("════════════════════════════════════════════════")


# Hardcoded example for Meena
savings_statement(
    income            = 38000,
    fixed_expenses    = 12000 + 5000,    # rent + EMI
    variable_expenses = 6000  + 2500 + 2000,  # food + transport + misc
)

# Interactive (uncomment)
# inc = float(input("Monthly income: ₹"))
# fix = float(input("Fixed expenses (rent + EMI): ₹"))
# var = float(input("Variable expenses (food + transport + misc): ₹"))
# savings_statement(inc, fix, var)
''')

# ── KEY CONCEPTS RECAP ───────────────────────────────────────────────────
nb.md("""
## 📚 Key Concepts Learned Today

| Concept | What it is | Where we used it |
|---------|------------|-------------------|
| Variables & types | Labelled drawers — int, float, str, bool, None | Every exercise |
| `input()` & casting | Asking the user for data | All 4 calculators |
| `if / elif / else` | Decision branching | GST slabs, savings grade |
| `for` loops | Walking a list one row at a time | CI schedule, sales summary |
| `while` loops | Looping while a condition holds | Shopping bill builder |
| Lists | Ordered collection (a "column") | Sales totals, prices |
| Dictionaries | Labelled record (a "card") | Customer record |
| Functions (preview) | Reusable block of code | All Unit I exercises |

## 🏠 Practice Exercises

1. **EMI Calculator** — Use the formula `EMI = P × r × (1+r)^n / ((1+r)^n − 1)` where `r = annual_rate / 12 / 100` and `n = years × 12`. Print the EMI, total interest paid, and total repayment for a ₹5,00,000 home loan @ 9% for 10 years.
2. **Multi-currency converter** — Extend Exercise 2 to support USD, EUR, GBP, and SGD with their own rates stored in a dictionary `rates = {"USD": 83.50, "EUR": 90.20, ...}`.
3. **Tip calculator** — Read a restaurant bill and number of diners, compute 18% GST + 10% service tip + per-person split; print a clean cheque-style breakdown.

---

➡️ **Next: Day 2** — Functions and Business Logic. We'll build a Net Salary Calculator, GST Invoice Generator, FD Maturity Schedule, and Sales Commission Engine — all using **functions** so we can reuse logic just like a stamp.
""")

path = nb.save("Day1_Python_Basics_and_Finance.ipynb")
print("✅ Built", path)
