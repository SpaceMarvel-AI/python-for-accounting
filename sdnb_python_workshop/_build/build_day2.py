"""Build Day2_Functions_and_Business_Logic.ipynb."""

from nb_helpers import Notebook, COLAB_SETUP

nb = Notebook()

# ── COVER ────────────────────────────────────────────────────────────────
nb.md("""
# 📘 Day 2 — Functions and Business Logic
**SDNB Vaishnav College for Women, Chromepet**

**Date:** Tuesday, 28 April 2026 | **Duration:** 9:30 AM – 1:00 PM (3 hours)

---

### 🎯 By the end of today you will have built:
- ✅ A **Net Salary Calculator** that produces a real payslip
- ✅ A **GST Invoice Generator** like the one used in shops every day
- ✅ A **Fixed Deposit Maturity Calculator** with compounding options
- ✅ A **Sales Commission Calculator** with leaderboard
""")

nb.code(COLAB_SETUP)

# ── Quick Recap ─────────────────────────────────────────────────────────
nb.md("""
## 🔁 Quick Recap of Day 1 *(5 min)*

Three quick warm-ups before we start. Try to answer in your head, then run the cell.

1. What does `price * 0.18` calculate when the price is in rupees?
2. What kind of value does `students_count = 45` create — `int`, `float`, or `str`?
3. What's the difference between `5 / 2` and `5 // 2` in Python?
""")
nb.code('''# Recap answers in code
price = 1000
print("1. GST on ₹1,000 @ 18% =", price * 0.18)        # → 180.0

students_count = 45
print("2. Type of students_count =", type(students_count).__name__)  # → int

print("3. 5 / 2  =", 5 / 2)     # → 2.5  (float divide)
print("   5 // 2 =", 5 // 2)    # → 2    (integer/floor divide)
''')

# ── SECTION 1 — What is a Function? ─────────────────────────────────────
nb.md("""
## 🪧 Section 1 — What is a Function? *(20 min)*

> **The stamp analogy:**
> A function is like a **stamp in a CA office**. Instead of writing "Received and Verified by Accounts Department, Chennai" 200 times by hand on 200 invoices, you make ONE rubber stamp and just press it. In Python, instead of writing the same calculation 200 times, you **define ONE function and just call it.**

### Anatomy of a function

```
┌─────────────────────────────────────────────────────┐
│  def   calculate_gst   (price, gst_rate):          │
│   │          │              │                      │
│  keyword  function_name   parameters                │
│                                                     │
│      gst_amount = price * gst_rate    ← body        │
│      return gst_amount                ← output      │
└─────────────────────────────────────────────────────┘
```

**Vocabulary:**
- `def` — keyword that *defines* a new function
- **parameters** — the variables in the parentheses (placeholders)
- **arguments** — the actual values passed when *calling* the function
- `return` — the single value the function gives back to whoever called it
- If you forget `return`, the function gives back `None` — like handing back a blank receipt.
""")

nb.code('''# Three small examples before the big exercises

def greet_customer(name):
    """Print a welcome message — does NOT return anything."""
    print(f"🙏 Welcome, {name}! Thank you for choosing us.")


def calculate_discount(price, discount_pct):
    """Return price after discount."""
    return price - (price * discount_pct / 100)


def is_eligible_for_credit(monthly_income, loan_amount):
    """Eligible if monthly income is at least 30% of the loan amount."""
    return monthly_income >= loan_amount * 0.30


# Calling each one
greet_customer("Priya")
print("Discounted price :", calculate_discount(2499, 20))
print("Eligible?         :", is_eligible_for_credit(50000, 100000))

# What happens when we forget return?
def broken_discount(price, pct):
    discounted = price - price * pct / 100   # forgot to return!

result = broken_discount(2499, 20)
print("\\nBroken function returned :", result, "  ← None = blank receipt")
''')

# ── SECTION 2 — Net Salary Calculator ───────────────────────────────────
nb.md("""
## 💰 Section 2 — Net Salary Calculator *(35 min)*

**Scenario:** *You are the HR Executive at SDNB Exports Pvt Ltd. Build a payroll system that calculates the net salary for any employee.*

**Income Tax slabs (FY 2025-26, simplified New Tax Regime):**
| Annual income (₹) | Tax rate |
|--------------------|----------|
| Up to 3,00,000 | 0% |
| 3,00,001 – 7,00,000 | 5% |
| 7,00,001 – 10,00,000 | 10% |
| 10,00,001 – 12,00,000 | 15% |
| Above 12,00,000 | 20% (simplified) |

**Other deductions:**
- **PF** (Provident Fund) = 12% of Basic Salary
- **Professional Tax** (Tamil Nadu) = ₹200 / month flat
""")

nb.code('''def calculate_pf(basic_salary):
    """Provident Fund = 12% of basic."""
    return round(basic_salary * 0.12, 2)


def calculate_professional_tax():
    """Tamil Nadu professional tax — flat ₹200 per month."""
    return 200


def calculate_income_tax(annual_ctc):
    """Apply simplified slab system, return MONTHLY income tax."""
    if annual_ctc <= 3_00_000:
        annual_tax = 0
    elif annual_ctc <= 7_00_000:
        annual_tax = (annual_ctc - 3_00_000) * 0.05
    elif annual_ctc <= 10_00_000:
        annual_tax = (4_00_000 * 0.05) + (annual_ctc - 7_00_000) * 0.10
    elif annual_ctc <= 12_00_000:
        annual_tax = (4_00_000 * 0.05) + (3_00_000 * 0.10) + (annual_ctc - 10_00_000) * 0.15
    else:
        annual_tax = (4_00_000 * 0.05) + (3_00_000 * 0.10) + (2_00_000 * 0.15) + (annual_ctc - 12_00_000) * 0.20
    return round(annual_tax / 12, 2)


def generate_payslip(employee_name, employee_id, basic_salary, hra, special_allowance):
    gross = basic_salary + hra + special_allowance
    annual_ctc = gross * 12

    pf  = calculate_pf(basic_salary)
    pt  = calculate_professional_tax()
    tax = calculate_income_tax(annual_ctc)

    deductions = pf + pt + tax
    net_pay    = gross - deductions

    print("╔══════════════════════════════════════════════╗")
    print("║          SDNB EXPORTS PVT LTD               ║")
    print("║              PAY SLIP — APR 2026            ║")
    print("╠══════════════════════════════════════════════╣")
    print(f"║ Employee: {employee_name:<22s}  ID: {employee_id:<6s} ║")
    print("╠═══════════════════════╦══════════════════════╣")
    print("║ EARNINGS              ║ DEDUCTIONS           ║")
    print("╠═══════════════════════╬══════════════════════╣")
    print(f"║ Basic Salary {basic_salary:>8,.0f}  ║ PF        {pf:>8,.0f}  ║")
    print(f"║ HRA          {hra:>8,.0f}  ║ Prof Tax  {pt:>8d}  ║")
    print(f"║ Special Allow{special_allowance:>8,.0f}  ║ Income Tax{tax:>8,.0f}  ║")
    print("╠═══════════════════════╬══════════════════════╣")
    print(f"║ Gross : ₹{gross:>10,.0f}  ║ Total Ded:₹{deductions:>8,.0f}  ║")
    print("╠══════════════════════════════════════════════╣")
    print(f"║ NET TAKE-HOME PAY: ₹{net_pay:>20,.2f}  ║")
    print("╚══════════════════════════════════════════════╝")

    return {
        "name": employee_name, "id": employee_id,
        "gross": gross, "pf": pf, "pt": pt, "tax": tax,
        "deductions": deductions, "net_pay": net_pay,
    }


# Run for 3 different employees
generate_payslip("Kavitha R.",      "EMP-0042", 25000, 10000,  5000)
print()
generate_payslip("Suresh Kumar",    "EMP-0103", 60000, 24000, 12000)
print()
generate_payslip("Devika Nair",     "EMP-0001", 90000, 36000, 24000)
''')

nb.md("""
**Interactive version** — uncomment to run with your own values:
""")
nb.code('''# name  = input("Employee name: ")
# emp_id= input("Employee ID  : ")
# basic = float(input("Basic salary (₹): "))
# hra   = float(input("HRA (₹): "))
# spl   = float(input("Special allowance (₹): "))
# generate_payslip(name, emp_id, basic, hra, spl)
print("(Interactive cell skipped — uncomment lines to use input())")
''')

# ── SECTION 3 — GST Invoice Generator ───────────────────────────────────
nb.md("""
## 🧾 Section 3 — GST Invoice Generator *(40 min)*

**Scenario:** *Rajesh runs a textile wholesale shop in Chennai. He needs a Python function that generates a proper GST invoice for any sale.*

**GST rates by category:**
- Textiles & Clothing **below** ₹1,000 → **5%**
- Textiles & Clothing **₹1,000 and above** → **12%**
- Electronics → **18%**
- Groceries / Food → **0%**
- Luxury Goods → **28%**

GST is split equally into **CGST (Central)** and **SGST (State)** — so 18% becomes 9% + 9%.
""")

nb.code('''def get_gst_rate(category, price):
    """Return GST rate (decimal) based on category and price tier."""
    cat = category.lower()
    if "textile" in cat or "cloth" in cat:
        return 0.05 if price < 1000 else 0.12
    if "electronics" in cat:
        return 0.18
    if "grocer" in cat or "food" in cat:
        return 0.00
    if "luxury" in cat:
        return 0.28
    return 0.18    # default fallback


def calculate_invoice_line(product_name, qty, unit_price, category):
    """Build one invoice line as a dictionary with all GST splits."""
    taxable_value = qty * unit_price
    rate          = get_gst_rate(category, unit_price)
    cgst          = round(taxable_value * rate / 2, 2)
    sgst          = round(taxable_value * rate / 2, 2)
    line_total    = round(taxable_value + cgst + sgst, 2)

    return {
        "product"      : product_name,
        "qty"          : qty,
        "unit_price"   : unit_price,
        "taxable_value": round(taxable_value, 2),
        "gst_rate"     : rate,
        "cgst"         : cgst,
        "sgst"         : sgst,
        "line_total"   : line_total,
    }


# Quick test
sample = calculate_invoice_line("Silk Saree", 2, 2499, "Textiles")
for k, v in sample.items():
    print(f"  {k:<14s}: {v}")
''')

nb.md("""
### `number_to_words` helper (simplified, for amounts up to 99,999)
""")
nb.code('''ONES = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
        "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
        "Seventeen", "Eighteen", "Nineteen"]
TENS = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]


def _two_digit_words(n):
    if n < 20:
        return ONES[n]
    return (TENS[n // 10] + (" " + ONES[n % 10] if n % 10 else "")).strip()


def number_to_words(amount):
    """Convert an integer rupee amount up to 99,999 to words."""
    n = int(amount)
    if n == 0:
        return "Zero"
    parts = []
    if n >= 1000:
        parts.append(_two_digit_words(n // 1000) + " Thousand")
        n %= 1000
    if n >= 100:
        parts.append(ONES[n // 100] + " Hundred")
        n %= 100
    if n > 0:
        parts.append(_two_digit_words(n))
    return " ".join(parts).strip()


# Quick demo
for amt in [49, 999, 12345, 87650]:
    print(f"₹{amt:>6,}  →  Rupees {number_to_words(amt)} Only")
''')

nb.md("""
### The full invoice generator
""")
nb.code('''def generate_gst_invoice(seller_info, buyer_info, items_list, invoice_no, invoice_date):
    line_items = [calculate_invoice_line(**it) for it in items_list]

    subtotal   = sum(li["taxable_value"] for li in line_items)
    total_gst  = sum(li["cgst"] + li["sgst"] for li in line_items)
    grand_total= subtotal + total_gst

    print("╔════════════════════════════════════════════════════════════╗")
    print("║                       TAX INVOICE                          ║")
    print("║                  (As per GST Act, 2017)                    ║")
    print("╠════════════════════════════════════════════════════════════╣")
    print(f"║ SELLER : {seller_info['name']:<48s}║")
    print(f"║ GST No : {seller_info['gst']:<48s}║")
    print(f"║ Address: {seller_info['city']:<48s}║")
    print("╠────────────────────────────────────────────────────────────╣")
    print(f"║ BUYER  : {buyer_info['name']:<48s}║")
    print(f"║ GST No : {buyer_info['gst']:<48s}║")
    print(f"║ Address: {buyer_info['city']:<48s}║")
    print("╠════════════════════════════════════════════════════════════╣")
    print(f"║ Invoice No: {invoice_no:<14s}    Date: {invoice_date:<22s}║")
    print("╠══════════════════════╦═════╦════════╦═══════╦══════╦═════════╣")
    print("║ Item                 ║ Qty ║   Rate ║  CGST ║ SGST ║   Total ║")
    print("╠══════════════════════╬═════╬════════╬═══════╬══════╬═════════╣")
    for li in line_items:
        print(f"║ {li['product']:<20s} ║ {li['qty']:>3d} ║ {li['unit_price']:>6,.0f} "
              f"║ {li['cgst']:>5,.0f} ║ {li['sgst']:>4,.0f} ║ {li['line_total']:>7,.0f} ║")
    print("╠══════════════════════╩═════╩════════╩═══════╩══════╩═════════╣")
    print(f"║ Subtotal     : ₹{subtotal:>10,.2f}                              ║")
    print(f"║ Total GST    : ₹{total_gst:>10,.2f}                              ║")
    print(f"║ INVOICE TOTAL: ₹{grand_total:>10,.2f}                              ║")
    print(f"║ Amount in Words: Rupees {number_to_words(grand_total)} Only" + " " * max(0, 33 - len(number_to_words(grand_total))) + "║")
    print("╚════════════════════════════════════════════════════════════╝")
    return grand_total


seller = {"name": "Rajesh Textiles",         "gst": "33AABCR1234F1ZX", "city": "Chennai, TN"}
buyer  = {"name": "SDNB College Stores",     "gst": "33AABCS5678G1ZY", "city": "Chromepet, Chennai"}

# Invoice 1 — textiles
items = [
    {"product_name": "Silk Saree",   "qty": 2, "unit_price": 2499, "category": "Textiles"},
    {"product_name": "Cotton Kurti", "qty": 5, "unit_price":  799, "category": "Textiles"},
    {"product_name": "Bedsheet",     "qty": 3, "unit_price": 1199, "category": "Textiles"},
]
generate_gst_invoice(seller, buyer, items, "INV-2026-0042", "28-Apr-2026")
''')

nb.code('''# Invoice 2 — electronics
items2 = [
    {"product_name": "Bluetooth Spk","qty": 4, "unit_price": 1999, "category": "Electronics"},
    {"product_name": "Mobile Charger","qty": 10,"unit_price":  349, "category": "Electronics"},
]
generate_gst_invoice(seller, buyer, items2, "INV-2026-0043", "28-Apr-2026")

print()

# Invoice 3 — mixed
items3 = [
    {"product_name": "Filter Coffee", "qty": 6, "unit_price": 299, "category": "Groceries"},
    {"product_name": "LED Bulb 9W",   "qty":12, "unit_price": 149, "category": "Electronics"},
    {"product_name": "Gold Bracelet", "qty": 1, "unit_price":24999,"category": "Luxury"},
]
generate_gst_invoice(seller, buyer, items3, "INV-2026-0044", "28-Apr-2026")
''')

# ── SECTION 4 — FD Calculator ───────────────────────────────────────────
nb.md("""
## 🏦 Section 4 — Fixed Deposit Maturity Calculator *(25 min)*

**Scenario:** *SBI has appointed you as a financial advisor chatbot. Build a function that generates a complete FD maturity schedule.*

**Compounding formula:**
$$A = P \\times \\left(1 + \\frac{r}{n}\\right)^{n \\times t}$$

where `n` = compounding frequency:
- Monthly = 12, Quarterly = 4, Half-yearly = 2, Annually = 1
""")

nb.code('''COMPOUND_N = {"monthly": 12, "quarterly": 4, "half-yearly": 2, "annually": 1}


def calculate_fd_maturity(principal, annual_rate, years, compounding="quarterly"):
    """Return dict with maturity_amount, interest_earned, effective_annual_rate."""
    n = COMPOUND_N[compounding]
    r = annual_rate / 100
    maturity = principal * (1 + r / n) ** (n * years)
    interest = maturity - principal
    effective_rate = ((maturity / principal) ** (1 / years) - 1) * 100
    return {
        "compounding"           : compounding,
        "maturity_amount"       : round(maturity, 2),
        "interest_earned"       : round(interest, 2),
        "effective_annual_rate" : round(effective_rate, 2),
    }


def compare_fd_options(principal, annual_rate, years):
    print(f"════════════════════════════════════════════════════════")
    print(f"   FD COMPARISON — ₹{principal:,.0f} @ {annual_rate}% for {years} Years")
    print(f"════════════════════════════════════════════════════════")
    print(f"{'Compounding':<14s}{'Maturity Amt':>16s}{'Interest':>14s}{'Eff Rate':>10s}")
    print("-" * 56)
    results = []
    for opt in ["annually", "half-yearly", "quarterly", "monthly"]:
        r = calculate_fd_maturity(principal, annual_rate, years, opt)
        results.append(r)
    best = max(results, key=lambda x: x["maturity_amount"])
    for r in results:
        flag = "  ← BEST" if r is best else ""
        print(f"{r['compounding'].title():<14s}"
              f"₹{r['maturity_amount']:>14,.0f}"
              f"₹{r['interest_earned']:>12,.0f}"
              f"{r['effective_annual_rate']:>9.2f}%{flag}")
    print("════════════════════════════════════════════════════════")


def fd_schedule(principal, annual_rate, years, compounding="quarterly"):
    n = COMPOUND_N[compounding]
    r = annual_rate / 100
    print(f"\\nYear-by-year schedule ({compounding}, {annual_rate}% p.a.):")
    print(f"{'Year':>5s}{'Balance':>16s}{'Yearly Gain':>16s}")
    prev = principal
    for y in range(1, years + 1):
        bal  = principal * (1 + r / n) ** (n * y)
        gain = bal - prev
        print(f"{y:>5d}  ₹{bal:>13,.2f}  ₹{gain:>13,.2f}")
        prev = bal


compare_fd_options(100000, 7.5, 3)
fd_schedule(100000, 7.5, 3, "quarterly")
''')

# ── SECTION 5 — Sales Commission ────────────────────────────────────────
nb.md("""
## 🏆 Section 5 — Sales Commission Calculator *(20 min)*

**Scenario:** *You are the Sales Manager at TN Motors. Build a fair commission system that rewards top performers more.*

| Quarterly sales | Commission rate |
|-----------------|-----------------|
| Below ₹50,000 | 2% |
| ₹50,000 – ₹1,00,000 | 5% |
| ₹1,00,001 – ₹2,00,000 | 8% |
| Above ₹2,00,000 | 12% |

**Bonus:** quarterly sales > ₹5,00,000 → flat ₹10,000 bonus.
""")

nb.code('''def calculate_commission(sales_amount):
    """Return (commission_amount, rate_pct) for the slab applying to this amount."""
    if sales_amount < 50_000:
        rate = 0.02
    elif sales_amount <= 1_00_000:
        rate = 0.05
    elif sales_amount <= 2_00_000:
        rate = 0.08
    else:
        rate = 0.12
    return round(sales_amount * rate, 2), rate * 100


def quarterly_commission_report(sales_person_name, monthly_sales_list):
    print("─" * 56)
    print(f"  Sales Executive: {sales_person_name}")
    print("─" * 56)
    print(f"  {'Month':<10s}{'Sales (₹)':>14s}{'Rate':>8s}{'Commission':>16s}")
    total_sales      = 0
    total_commission = 0
    months = ["Jan", "Feb", "Mar"]
    for m, s in zip(months, monthly_sales_list):
        c, r = calculate_commission(s)
        total_sales      += s
        total_commission += c
        print(f"  {m:<10s}{s:>14,.0f}{r:>7.0f}%{c:>16,.2f}")
    bonus = 10000 if total_sales > 5_00_000 else 0
    print("─" * 56)
    print(f"  {'TOTAL':<10s}{total_sales:>14,.0f}{'':>8s}{total_commission:>16,.2f}")
    print(f"  Bonus (sales > ₹5,00,000)            : ₹{bonus:>10,.2f}")
    print(f"  GRAND COMMISSION (incl. bonus)       : ₹{total_commission + bonus:>10,.2f}")
    print("─" * 56)
    return {"name": sales_person_name, "sales": total_sales,
            "commission": total_commission + bonus}


sales_team = [
    ("Karthik R.", [180000, 220000, 195000]),
    ("Priya S.",   [ 75000, 110000,  95000]),
    ("Mohan K.",   [ 45000,  35000,  60000]),
    ("Devika N.",  [250000, 280000, 305000]),
    ("Suresh M.",  [125000, 145000, 130000]),
]

results = [quarterly_commission_report(name, ms) for name, ms in sales_team]

# Leaderboard
print("\\n╔══════════════════════════════════════════════════════════╗")
print("║                  Q1 2026 — LEADERBOARD                  ║")
print("╠══════════════════════════════════════════════════════════╣")
print(f"║  {'Rank':<6s}{'Sales Person':<18s}{'Sales (₹)':>15s}{'Earnings':>13s}  ║")
print("╠──────────────────────────────────────────────────────────╣")
for rank, r in enumerate(sorted(results, key=lambda x: -x["commission"]), 1):
    print(f"║  #{rank:<5d}{r['name']:<18s}{r['sales']:>15,.0f}{r['commission']:>13,.2f}  ║")
print("╚══════════════════════════════════════════════════════════╝")
''')

# ── Recap ───────────────────────────────────────────────────────────────
nb.md("""
## 📚 Key Concepts Learned Today

| Concept | Demonstrated in |
|---------|-----------------|
| `def` and `return` | Every exercise |
| Functions calling other functions | `generate_payslip` calls `calculate_pf` etc. |
| Returning dictionaries | `calculate_invoice_line`, `calculate_fd_maturity` |
| Default parameter values | `compounding="quarterly"` |
| Looping over function results | Sales team leaderboard |
| Combining `if/elif/else` with functions | Tax slabs, GST slabs, commission slabs |

---

➡️ **Next: Day 3** — Data Visualisation. We'll turn the numbers we've been printing into **bar charts, pie charts, histograms, and scatter plots** that look like real business dashboards.
""")

path = nb.save("Day2_Functions_and_Business_Logic.ipynb")
print("✅ Built", path)
