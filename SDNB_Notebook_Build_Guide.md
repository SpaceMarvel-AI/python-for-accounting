# SDNB Python Workshop — Claude Code Notebook Build Guide

**College:** Shrimathi Devkunvar Nanalal Bhatt Vaishnav College for Women, Chromepet, Chennai  
**Programme:** Business Analytics Using Python — Hands-On Sessions  
**Audience:** Commerce & Management students (no prior Python experience)  
**Duration:** 15 Hours across 4 Days | April 27–30, 2026  
**Output:** 5 Jupyter Notebook files (.ipynb) + 1 Capstone Project notebook  

---

## How to Use This Guide

1. Open your terminal and start Claude Code: `claude`
2. Run each prompt block below **in order** — one prompt = one notebook
3. All notebooks go into a folder called `sdnb_python_workshop/`
4. Each notebook is self-contained and runs top-to-bottom on Google Colab

> **Design principle for every notebook:**  
> Audience = Commerce students who know Excel, Tally, and basic accounting.  
> Every concept must be introduced with a **real-world business analogy first**, then the Python code.  
> No jargon without explanation. Every output must look like something from a real office.

---

## Project Scaffold — Run This First

```
Create a folder called sdnb_python_workshop/ with the following structure:

sdnb_python_workshop/
├── data/
│   ├── sales_data.csv          ← 90 rows: Date, Product, Category, Units, Price, Region
│   ├── bank_transactions.csv   ← 60 rows: Date, Description, Debit, Credit, Balance
│   ├── inventory.csv           ← 30 rows: ProductID, Name, Category, Stock, UnitPrice
│   ├── customer_ages.csv       ← 100 rows: CustomerID, Name, Age, City, Segment
│   ├── ad_spend.csv            ← 24 rows: Month, AdSpend, SalesRevenue, Channel
│   ├── exam_marks.csv          ← 40 rows: RollNo, Name, Maths, Accounts, Economics, Commerce, English
│   └── monthly_expenses.csv    ← 12 rows: Month, Rent, Salary, Utilities, Marketing, Misc
├── notebooks/
│   ├── Day1_Python_Basics_and_Finance.ipynb
│   ├── Day2_Functions_and_Business_Logic.ipynb
│   ├── Day3_Data_Visualisation.ipynb
│   ├── Day4_Morning_Data_Analysis.ipynb
│   ├── Day4_Afternoon_KPI_Dashboard.ipynb
│   └── Capstone_Business_Analytics_Report.ipynb
└── README.md

Generate all CSV files with realistic Indian business data:
- Use Indian names, cities (Chennai, Bengaluru, Mumbai, Delhi, Hyderabad)
- Products: sarees, electronics, groceries, stationery, textiles
- Amounts in INR (rupees)
- Dates in 2025-2026 range
- Make data slightly imperfect (a few missing values, outliers) so students
  learn to handle real data

Also create README.md explaining the folder structure and how to open notebooks in Google Colab.
```

---

## Notebook 1 — Day 1 (Monday, April 27 | 9:30 AM – 1:00 PM | 3 Hours)

### File: `Day1_Python_Basics_and_Finance.ipynb`

```
Create a Jupyter notebook called Day1_Python_Basics_and_Finance.ipynb for commerce students
learning Python for the first time. Follow every instruction below exactly.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
NOTEBOOK DESIGN RULES (apply to every cell):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Every new concept starts with a Markdown cell containing:
   - A real-world business analogy (relate to accounting, tally, or commerce)
   - What we will learn in plain English
   - A "Think of it like..." sentence
2. Code cells must have # comments on every line explaining what it does
3. After every code cell, add a Markdown "🧠 What just happened?" cell
4. End each major section with a "✏️ Try It Yourself" exercise cell
5. Use print() statements that produce clean, formatted output like a real business report
6. All variable names must be meaningful business words (not x, y, a, b)
7. All amounts in Indian Rupees (₹)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 1 — Welcome & Setup (15 min)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Markdown cell: Welcome banner with college name, programme name, day 1 title.
Include a "What will you be able to do by the end of today?" bullet list:
- Build a working Simple Interest & Compound Interest calculator
- Create a USD to INR currency converter
- Record and summarise 10 sales entries
- Calculate monthly savings automatically

Markdown cell: "Why Python for Commerce?"
Explain with this analogy: "Think of Python as a very smart calculator + Tally + Excel
combined — but you give it instructions in plain English-like language."
Include a comparison table (Markdown table) showing:
| Task | In Excel | In Tally | In Python |
Like: Calculate GST → =A1*18% → Journal Entry → product_price * 0.18

Code cell: Print the workshop title as a formatted banner using print() with = signs

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 2 — Python Basics Part 1: Variables & Data Types (30 min)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Markdown: "Variables are like labeled drawers in your office cabinet.
Just like you label a drawer 'Petty Cash' and put ₹500 inside,
in Python you write: petty_cash = 500"

Cover ALL of these with commerce examples:

A) Integer (int) — whole numbers
   Example: number_of_invoices = 45, employees_count = 12
   Show: type(), arithmetic (+, -, *, //, %), print with f-string

B) Float (float) — decimal numbers (money amounts)
   Example: product_price = 2499.99, gst_rate = 0.18
   Show: rounding with round(), formatting with f"₹{amount:.2f}"
   IMPORTANT: Explain why computers sometimes show 0.30000000000000004
   and use round() to fix it — relate to rounding in ledgers

C) String (str) — text
   Example: company_name = "SDNB Textiles Pvt Ltd", invoice_number = "INV-2026-001"
   Show: len(), upper(), lower(), strip(), f-strings, concatenation
   Exercise: Build a professional invoice header string using f-strings

D) Boolean (bool) — True/False decisions
   Example: is_gst_registered = True, is_payment_received = False
   Show: how these connect to if/else decisions
   Analogy: "Like a YES/NO checkbox in a form"

E) None — empty/missing
   Example: customer_email = None (customer didn't provide email)
   Relate to: blank cells in Excel, missing entries in ledger

After each type: print a formatted output. Example output for float:
   ─────────────────────────────────
   Product   : Premium Saree
   Price     : ₹2,499.99
   GST (18%) : ₹449.00
   Total     : ₹2,948.99
   ─────────────────────────────────

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 3 — Python Basics Part 2: User Input & Basic Operators (20 min)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Markdown: "input() is like asking a question on a paper form —
the user fills in the blank and Python uses their answer."

A) input() with float() and int() conversion
   Example: Ask for principal amount, rate, years — all as business fields
   Show the EXACT error that happens if you forget float() and explain why
   (type mismatch = like adding apples and oranges in accounts)

B) All arithmetic operators with business meaning:
   + → Adding invoice amounts
   - → Calculating profit (Revenue - Cost)
   * → Calculating total (Qty × Price)
   / → Per unit cost (Total ÷ Units)
   // → Floor division → How many full cartons fit?
   % → Remainder → Leftover units after packing
   ** → Power → Used in Compound Interest formula

C) Comparison operators:
   ==, !=, >, <, >=, <=
   Example: Check if revenue > target, if stock < reorder_level
   Show output: "Target Achieved: True"

D) Logical operators: and, or, not
   Business example: Eligible for loan IF salary > 25000 AND credit_score >= 700

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 4 — Python Basics Part 3: if/elif/else + Loops (30 min)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Markdown: "if/else is like the decision column in a ledger:
IF the balance is positive → THEN write it in the Debit column,
ELSE write it in the Credit column."

A) if / elif / else
   Full worked example: GST slab calculator
   - Below ₹1,000 → 5% GST
   - ₹1,000 to ₹5,000 → 12% GST
   - ₹5,000 to ₹10,000 → 18% GST
   - Above ₹10,000 → 28% GST
   Print a clean bill showing the category and tax applied

B) for loop
   Analogy: "Like going through each row in a ledger book one by one"
   Example 1: Loop through a list of 5 product prices, print each with serial number
   Example 2: Loop through months ["Apr", "May", "Jun"...] and print month number
   Example 3: Use range(1, 11) to simulate 10 transaction entries

C) while loop
   Analogy: "Like saying 'Keep checking outstanding invoices WHILE there are unpaid ones'"
   Example: Keep adding items to a shopping bill WHILE total is below ₹10,000
   Show how to exit with break when condition is met

D) Nested loop example:
   Print a multiplication table for a product pricing grid
   (3 quantity tiers × 4 discount levels = price matrix)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 5 — Python Basics Part 4: Lists & Dictionaries (25 min)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
A) Lists
   Analogy: "A list is like a column in your Excel sheet —
   an ordered collection of items you can add to, remove from, or loop through."
   
   Demonstrate with: product_prices = [499, 1299, 2499, 799, 3999, 149, 599, 999, 1799, 2999]
   Show ALL of: indexing [0], negative index [-1], slicing [2:5],
   append(), remove(), sort(), reverse(), len(), sum(), min(), max()
   
   Business exercise: Calculate average selling price, find most expensive & cheapest product
   Format output as a price analysis report

B) Dictionaries
   Analogy: "A dictionary is like a customer record card —
   each field has a label (key) and a value. Just like: Name: Priya, Balance: ₹45,000"
   
   Demonstrate with a full customer account dictionary:
   customer = {"name": "Priya Sharma", "account_no": "SB-2026-001",
                "balance": 45000.00, "city": "Chennai", "is_premium": True}
   
   Show: accessing keys, updating values, adding new keys, .keys(), .values(), .items()
   Loop through and print as a formatted account statement
   
   Advanced: List of dictionaries (like a mini database)
   sales_records = [{"date": ..., "product": ..., "amount": ...}, ...]
   Loop and calculate total

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 6 — Unit I: Financial Calculators (60 min) ← THE MAIN EXERCISES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
All 4 exercises must have:
- A clear real-world scenario (like "Mrs. Lakshmi deposits ₹50,000 at SBI...")
- Formula written as a Markdown math block before the code
- Input using input() so it's interactive
- Output formatted as a proper financial document
- A worked example already shown with hardcoded values so student can follow along

EXERCISE 1: Simple Interest & Compound Interest Calculator
Scenario: "You are a Junior Accountant at Lakshmi Finance Ltd.
A client wants to invest ₹1,00,000. Show them how much they will earn
with Simple Interest vs Compound Interest over 5 years at 8% p.a."

Formula block:
Simple Interest    = (Principal × Rate × Time) / 100
Compound Interest  = Principal × (1 + Rate/100)^Time
Total Amount (SI)  = Principal + Simple Interest
Total Amount (CI)  = Principal × (1 + Rate/100)^Time

Code must:
1. First show hardcoded example with Mrs. Lakshmi (Principal=100000, Rate=8, Time=5)
2. Then interactive version using input()
3. Print a comparison table:
   ════════════════════════════════════════════
        INVESTMENT COMPARISON REPORT
        Lakshmi Finance Ltd | FD Advisory Desk
   ════════════════════════════════════════════
   Principal Amount  : ₹1,00,000.00
   Interest Rate     : 8.00% per annum
   Investment Period : 5 Years
   ────────────────────────────────────────────
                    SI           CI
   Interest Earned  ₹40,000.00   ₹46,933.00
   Maturity Amount  ₹1,40,000.00 ₹1,46,933.00
   Extra with CI    ₹6,933.00    (Choose CI!)
   ════════════════════════════════════════════
4. Add a year-by-year CI growth table using a for loop showing balance each year

EXERCISE 2: Currency Converter (USD to INR)
Scenario: "Your college is importing lab equipment worth $2,500 from the USA.
The current exchange rate is ₹83.50 per dollar. Calculate the INR cost,
add 5% customs duty, and show the total landed cost."

Code must:
1. Hardcoded example first (amount=2500, rate=83.50, duty=5%)
2. Interactive version with input()
3. Show conversion output as a purchase voucher format:
   ════════════════════════════════════════════
        IMPORT PURCHASE VOUCHER
        SDNB College — Procurement Department
   ════════════════════════════════════════════
   Invoice Amount (USD) : $2,500.00
   Exchange Rate        : ₹83.50 per USD
   Base Cost (INR)      : ₹2,08,750.00
   Customs Duty (5%)    : ₹10,437.50
   ────────────────────────────────────────────
   TOTAL LANDED COST    : ₹2,19,187.50
   ════════════════════════════════════════════
4. Add a mini conversion table showing $100, $500, $1000, $2500, $5000 at current rate

EXERCISE 3: Sales Tracker — 10 entries
Scenario: "You are the Sales Executive at Chennai Textiles.
Enter today's 10 sales transactions and generate an end-of-day sales summary."

Code must:
1. Use a while loop with a counter (not just input 10 times manually)
2. Store sales in a list
3. After all 10 entries, print:
   ════════════════════════════════════════════
        END-OF-DAY SALES SUMMARY
        Chennai Textiles | Date: 27-Apr-2026
   ════════════════════════════════════════════
   Sale 1  :  ₹  3,450.00
   Sale 2  :  ₹  1,200.00
   ... (all 10)
   ────────────────────────────────────────────
   Total Sales   : ₹ 28,560.00
   Average Sale  : ₹  2,856.00
   Highest Sale  : ₹  5,400.00
   Lowest Sale   : ₹    800.00
   ════════════════════════════════════════════
4. Bonus: Count how many sales were above average

EXERCISE 4: Monthly Savings Calculator
Scenario: "Meena, a Junior Accountant, wants to track if she is saving enough
for her annual vacation fund. Help her build a savings tracker."

Code must:
1. Input: monthly income, fixed expenses (rent, EMI), variable expenses (food, transport, misc)
2. Calculate: Gross Savings, Savings Rate %, classify as Excellent/Good/Needs Improvement
3. Savings rate grading: >30% = Excellent 🌟, 20-30% = Good ✅, 10-20% = Okay ⚠️, <10% = Needs Work ❌
4. Project annual savings
5. Print formatted Personal Finance Statement

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
END OF NOTEBOOK 1
Add a "📚 Key Concepts Learned Today" recap Markdown cell
Add a "🏠 Practice Exercises" section with 3 additional problems to try at home
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Notebook 2 — Day 2 (Tuesday, April 28 | 9:30 AM – 1:00 PM | 3 Hours)

### File: `Day2_Functions_and_Business_Logic.ipynb`

```
Create Day2_Functions_and_Business_Logic.ipynb for commerce students.
Continue the same design rules from Day 1. Add a "Quick Recap of Day 1" 
section at the top (5 min warm-up with 3 quick review questions).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 1 — What is a Function? (20 min)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Analogy (MUST use this exact analogy):
"A function is like a stamp in a CA office.
Instead of writing 'Received and Verified by Accounts Department, Chennai' 
every time on 200 invoices, you make ONE rubber stamp and just press it.
In Python, instead of writing the same calculation 200 times,
you define ONE function and just call it."

Show the anatomy of a function with a labeled diagram in Markdown:
┌─────────────────────────────────────────────┐
│  def  calculate_gst  (price, gst_rate):     │
│  │     │               │                    │
│  │     function_name   parameters           │
│  keyword                                    │
│                                             │
│      gst_amount = price * gst_rate          │
│      return gst_amount      ← output        │
└─────────────────────────────────────────────┘

Show 3 simple examples before the exercises:
1. def greet_customer(name) → prints welcome message
2. def calculate_discount(price, discount_pct) → returns discounted price
3. def is_eligible_for_credit(monthly_income, loan_amount) → returns True/False

Explain: parameters vs arguments, return vs print, why return is important
Show what happens when you forget return (returns None — like a blank receipt)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 2 — Unit II Exercise 1: Net Salary Calculator (35 min)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Scenario: "You are the HR Executive at SDNB Exports Pvt Ltd.
Build a payroll system function that calculates net salary for any employee."

Indian tax slabs (FY 2025-26, New Tax Regime):
- Up to ₹3,00,000     → 0% tax
- ₹3,00,001 – ₹7,00,000 → 5% tax
- ₹7,00,001 – ₹10,00,000 → 10% tax
- ₹10,00,001 – ₹12,00,000 → 15% tax
- Above ₹12,00,000    → 20% tax (simplified)

Deductions to include:
- PF (Provident Fund) = 12% of Basic Salary
- Professional Tax = ₹200/month (fixed for Tamil Nadu)
- Income Tax = calculated on annual CTC, divided by 12

Build these functions (each as a separate def):
1. def calculate_pf(basic_salary) → returns PF amount
2. def calculate_professional_tax() → returns ₹200
3. def calculate_income_tax(annual_ctc) → returns monthly tax using slabs with if/elif
4. def generate_payslip(employee_name, employee_id, basic_salary, hra, special_allowance):
   - Calls all 3 above functions internally
   - Returns a dictionary with all components
   - Prints a formatted payslip

Output must look like a real payslip:
   ╔══════════════════════════════════════════════╗
   ║          SDNB EXPORTS PVT LTD               ║
   ║              PAY SLIP — APR 2026            ║
   ╠══════════════════════════════════════════════╣
   ║ Employee: Kavitha R.   | ID: EMP-0042       ║
   ╠═══════════════════════╦══════════════════════╣
   ║ EARNINGS              ║ DEDUCTIONS           ║
   ╠═══════════════════════╬══════════════════════╣
   ║ Basic Salary  25,000  ║ PF           3,000   ║
   ║ HRA           10,000  ║ Prof Tax       200   ║
   ║ Special Allow  5,000  ║ Income Tax   1,250   ║
   ╠═══════════════════════╬══════════════════════╣
   ║ Gross: ₹40,000        ║ Total Ded: ₹4,450    ║
   ╠══════════════════════════════════════════════╣
   ║ NET TAKE-HOME PAY: ₹35,550                  ║
   ╚══════════════════════════════════════════════╝

Test with 3 different employees (different salary levels) to show the function works for all.
Add interactive input version.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 3 — Unit II Exercise 2: GST Invoice Generator (40 min)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Scenario: "Rajesh runs a textile wholesale shop in Chennai.
He needs a Python function that generates a proper GST invoice for any sale."

GST rates by category (hardcode these in the function):
- Textiles & Clothing below ₹1,000 → 5%
- Textiles & Clothing ₹1,000 and above → 12%
- Electronics → 18%
- Groceries / Food → 0%
- Luxury Goods → 28%

Build:
1. def get_gst_rate(category, price) → returns the correct GST rate
2. def calculate_invoice_line(product_name, qty, unit_price, category):
   → returns dict: {product, qty, unit_price, taxable_value, gst_rate, cgst, sgst, line_total}
   (Split GST equally into CGST and SGST — 9% + 9% = 18% etc.)
3. def generate_gst_invoice(seller_info, buyer_info, items_list):
   → accepts a list of item dictionaries
   → prints a complete GST-compliant invoice

Output MUST look exactly like a real GST invoice:
   ╔════════════════════════════════════════════════════════╗
   ║                    TAX INVOICE                        ║
   ║            (As per GST Act, 2017)                     ║
   ╠══════════════════════╦═════════════════════════════════╣
   ║ SELLER               ║ BUYER                          ║
   ║ Rajesh Textiles      ║ SDNB College Stores            ║
   ║ GST: 33AABCR1234F1ZX ║ GST: 33AABCS5678G1ZY          ║
   ║ Chennai, Tamil Nadu  ║ Chromepet, Chennai             ║
   ╠══════════════════════╩═════════════════════════════════╣
   ║ Invoice No: INV-2026-0042  Date: 28-Apr-2026          ║
   ╠════════╦══════╦══════╦══════╦══════╦══════╦═══════════╣
   ║ Item   ║ Qty  ║ Rate ║ CGST ║ SGST ║ GST% ║ Total     ║
   ... (line items)
   ╠════════════════════════════════════════════════════════╣
   ║ Subtotal: ₹XX,XXX  |  Total GST: ₹X,XXX              ║
   ║ INVOICE TOTAL: ₹XX,XXX                               ║
   ║ Amount in Words: Rupees ... Only                      ║
   ╚════════════════════════════════════════════════════════╝

Include a number_to_words function (simplified for amounts up to 99,999)
Test with 3 sample invoices covering different product categories.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 4 — Unit II Exercise 3: Fixed Deposit Interest Calculator (25 min)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Scenario: "SBI has appointed you as a financial advisor chatbot.
Build a function that generates a complete FD maturity schedule."

FD interest compounding options: Monthly, Quarterly, Half-Yearly, Annually
Formula: A = P × (1 + r/n)^(n×t)  where n = compounding frequency

Build:
1. def calculate_fd_maturity(principal, annual_rate, years, compounding="quarterly"):
   → returns dict with: maturity_amount, interest_earned, effective_annual_rate
   → compounding can be: "monthly"(12), "quarterly"(4), "half-yearly"(2), "annually"(1)

2. def compare_fd_options(principal, annual_rate, years):
   → calls calculate_fd_maturity 4 times with different compounding
   → prints a comparison table showing which gives the best return

3. def fd_schedule(principal, annual_rate, years, compounding="quarterly"):
   → prints year-by-year balance (compound interest schedule table)

Output format for comparison:
   ════════════════════════════════════════════════════
      FD COMPARISON — ₹1,00,000 @ 7.5% for 3 Years
   ════════════════════════════════════════════════════
   Compounding    Maturity Amt    Interest    Eff Rate
   ────────────────────────────────────────────────────
   Annually     ₹1,24,230       ₹24,230      7.50%
   Half-Yearly  ₹1,24,861       ₹24,861      7.64%
   Quarterly    ₹1,25,188       ₹25,188      7.71%  ← BEST
   Monthly      ₹1,25,393       ₹25,393      7.76%
   ════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 5 — Unit II Exercise 4: Sales Commission Calculator (20 min)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Scenario: "You are the Sales Manager at TN Motors.
Build a fair commission system that rewards top performers more."

Commission slabs:
- Below ₹50,000 sales     → 2% commission
- ₹50,000 – ₹1,00,000    → 5% commission on the full amount
- ₹1,00,001 – ₹2,00,000  → 8% commission on the full amount
- Above ₹2,00,000         → 12% commission on the full amount
- Bonus: If quarterly target > ₹5,00,000 → additional ₹10,000 bonus

Build:
1. def calculate_commission(sales_amount) → returns commission amount and rate
2. def quarterly_commission_report(sales_person_name, monthly_sales_list):
   → takes a list of 3 monthly sales amounts
   → calculates each month's commission + quarterly total + bonus if applicable
   → prints a quarterly commission statement

Test with a list of 5 sales executives and their quarterly sales.
Print a leaderboard at the end sorted by total earnings.
```

---

## Notebook 3 — Day 3 (Wednesday, April 29 | 9:30 AM – 1:00 PM | 3 Hours)

### File: `Day3_Data_Visualisation.ipynb`

```
Create Day3_Data_Visualisation.ipynb for commerce students.
Same design rules. Add Day 2 recap at top.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 1 — Introduction to Data Visualisation (15 min)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Analogy: "A chart is like a financial dashboard — instead of reading 
100 rows of figures, one bar chart tells you instantly which month 
performed best. Finance directors look at charts before they look at 
raw data. You are learning to build those charts."

Show the imports block and explain each library:
import matplotlib.pyplot as plt  # The main charting library (like Excel charts)
import numpy as np               # For number arrays (like a smart list)
# Later we'll use seaborn too — it makes prettier charts automatically

Show setup code for consistent chart style:
plt.style.use('seaborn-v0_8-whitegrid')  # Professional clean look
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['figure.dpi'] = 100

Explain the anatomy of a Matplotlib chart with a labeled Markdown diagram:
Figure → Canvas (the whole image)
  └── Axes → The actual plot area
        ├── Title
        ├── X-axis label & ticks
        ├── Y-axis label & ticks
        └── Data (bars / slices / dots / line)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CHART 1 — Bar Chart: Monthly Expenses by Category (40 min)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Scenario: "SDNB College's Administration Office wants to visualise 
where the budget is going each month."

Data (hardcode this realistic data):
categories = ["Rent", "Salaries", "Utilities", "Marketing", "Stationery", "Events", "IT & Tech"]
jan_expenses = [85000, 320000, 12000, 45000, 8000, 25000, 15000]
apr_expenses = [85000, 335000, 14000, 62000, 6000, 80000, 22000]

Build FOUR versions of the bar chart, each adding one new concept:
Version 1 — Basic bar chart (just data plotted)
Version 2 — Add title, axis labels, value labels on top of each bar
Version 3 — Grouped bar chart (Jan vs Apr side by side), add legend
Version 4 — Styled version with custom colors (purple palette for SDNB),
            horizontal line for budget threshold, annotation for highest expense

After each version: Markdown "🔍 What did we add?" explaining the new elements
Final version must be publication-quality with:
- Chart title: "SDNB College — Monthly Expense Analysis (Jan vs Apr 2026)"
- X-axis: Categories, Y-axis: Amount (₹)
- Legend top-right
- Value labels on each bar (formatted as ₹X,XX,XXX)
- Color: purple for Jan, gold for Apr
- Save chart: plt.savefig("charts/expense_comparison.png", bbox_inches='tight', dpi=150)

Also: Load from monthly_expenses.csv from the data folder and reproduce the same chart

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CHART 2 — Pie Chart: Market Share for 5 Brands (30 min)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Scenario: "A Chennai textile distributor wants to understand which 
brands are dominating their sales."

Data:
brands = ["Bombay Dyeing", "Raymond", "Arvind", "Vardhman", "OCM"]
market_share = [28, 22, 20, 18, 12]  # percentages

Build THREE versions:
Version 1 — Basic pie chart
Version 2 — Explode the top brand (pull it out slightly), add % labels
Version 3 — Donut chart variant (set wedgeprops=dict(width=0.5)),
            add total sales figure in the center hole

Final version must have:
- Custom colors using a defined color palette (matching brand colors where possible)
- Percentage AND absolute value labels
- Legend outside the chart
- Title: "Chennai Textiles Distribution — Brand Market Share Q1 2026"

Add commentary cell: "📊 Business Insight: Brand X dominates with X% share.
The bottom 2 brands together hold less than X% — management should review their strategy."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CHART 3 — Histogram: Customer Age Distribution (30 min)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Scenario: "The Marketing Manager of a Chennai retail chain 
wants to understand the age profile of their customers to target campaigns better."

Load: customer_ages.csv from data folder (CustomerID, Name, Age, City, Segment)
Also create a fallback hardcoded list of 100 ages if file not found.

Build THREE versions:
Version 1 — Basic histogram with 10 bins
Version 2 — Styled histogram with bin edges highlighted, mean line (red dashed),
            median line (green dashed), legend showing mean and median values
Version 3 — Side-by-side histogram by customer segment 
            (Premium vs Regular customers — use the Segment column)

Add statistics Markdown cell showing:
- Mean age, Median age, Mode age range, Youngest, Oldest
- "Most customers are between X–Y years old (X% of total)"
- Marketing recommendation based on the age profile

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CHART 4 — Scatter Plot: Advertising Cost vs Sales (35 min)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Scenario: "The CFO of a mid-sized FMCG company wants to know: 
Is our advertising spend actually generating sales? 
Show me the relationship visually."

Load: ad_spend.csv (Month, AdSpend, SalesRevenue, Channel)
Fallback: Generate 24 months of realistic data with a positive correlation
(sales = 8 × ad_spend + random noise + seasonal bump in Oct-Dec)

Build FOUR versions:
Version 1 — Basic scatter plot (dots only)
Version 2 — Add trend line using numpy polyfit, color dots by channel
Version 3 — Add annotations for the best and worst performing months,
            add R² correlation coefficient in the chart corner
Version 4 — Complete business version with:
  - Quadrant lines dividing into High Spend/High Sales, Low Spend/High Sales etc.
  - Each quadrant labeled
  - Dot size = absolute sales volume
  - Color = Channel (Digital/Print/Outdoor/Social)

Business insights Markdown cell:
- Correlation coefficient interpretation
- ROI calculation: "For every ₹1 spent on ads, we generate ₹X in sales"
- Which channel gives the best ROI?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BONUS SECTION — Dashboard Preview (15 min)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Combine all 4 charts into a single 2×2 dashboard figure:
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
Title: "SDNB Business Analytics Dashboard — Q1 2026"
Save as: charts/business_dashboard.png

This gives students a preview of Day 4's KPI dashboard work.
```

---

## Notebook 4 — Day 4 Morning (Thursday, April 30 | 9:30 AM – 1:00 PM)

### File: `Day4_Morning_Data_Analysis.ipynb`

```
Create Day4_Morning_Data_Analysis.ipynb

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 1 — Introduction to Pandas (25 min)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Analogy: "Pandas is Excel inside Python. 
A DataFrame is exactly like an Excel sheet — rows, columns, filters, 
formulas. Except it can handle 10 MILLION rows without crashing, 
and you can automate everything."

Side-by-side comparison table (Markdown):
| What you do in Excel        | What you do in Pandas          |
|-----------------------------|--------------------------------|
| Open a .csv file            | pd.read_csv("file.csv")        |
| See first 5 rows            | df.head()                      |
| See column names            | df.columns                     |
| Filter rows (AutoFilter)    | df[df["Sales"] > 5000]         |
| Sum a column                | df["Sales"].sum()              |
| Group by category           | df.groupby("Category").sum()   |
| Sort by column              | df.sort_values("Amount")       |
| Add new column (formula)    | df["Tax"] = df["Price"] * 0.18 |

Build a mini Pandas tutorial notebook section:
1. Create a small DataFrame from scratch (5 rows, 4 columns — sales data)
2. Show: head(), tail(), info(), describe(), shape, dtypes, columns
3. Show: selecting columns, filtering rows, adding calculated columns
4. Explain iloc vs loc with relatable examples
5. Show handling missing values: isnull(), fillna(), dropna()
   Analogy: "fillna is like filling blank cells in your attendance register"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EXERCISE 1 — Sales CSV Analysis (30 min)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Load: sales_data.csv (Date, Product, Category, Units, Price, Region)

Perform ALL of these analyses with clean formatted outputs:

Step 1: Data Overview
- Shape, columns, data types
- First 5 rows, Last 5 rows
- Check for missing values (show count per column)
- Basic statistics (describe())

Step 2: Revenue Analysis
- Add new column: Revenue = Units × Price
- Total revenue across all rows
- Revenue by Category (groupby + sum)
- Revenue by Region (groupby + sum)
- Revenue by Month (parse date, extract month, groupby)

Step 3: Top Performers
- Top 5 best-selling products (by revenue)
- Top 3 regions by sales
- Best performing month
- Worst performing month

Step 4: Visualise findings
- Bar chart: Revenue by Category
- Bar chart: Revenue by Region
- Line chart: Monthly revenue trend

Print a final "Sales Analysis Report" Markdown summary with all key numbers

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EXERCISE 2 — 7-Day Sales Summary with Max/Min/Total (20 min)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Scenario: "Week-end review meeting at a Chennai retail store.
The manager wants a quick weekly performance summary."

Code: Use input() to collect 7 daily sales amounts interactively
Then analyse with BOTH plain Python (without Pandas) AND with Pandas
to show students the difference in effort:

Plain Python version:
  sales = []  → use while loop → input → append
  max(), min(), sum(), len(), sum/len for average

Pandas version:
  pd.Series(sales) → .max(), .min(), .sum(), .mean(), .idxmax()

Print a weekly summary report:
   ════════════════════════════════════════
      WEEKLY SALES REPORT
      Chennai Retail Store | Week 17, 2026
   ════════════════════════════════════════
   Monday    : ₹ 28,400  [▓▓▓▓▓▓▓░░░]
   Tuesday   : ₹ 31,200  [▓▓▓▓▓▓▓▓░░]
   Wednesday : ₹ 19,800  [▓▓▓▓░░░░░░]
   Thursday  : ₹ 42,500  [▓▓▓▓▓▓▓▓▓▓] ← BEST DAY
   Friday    : ₹ 38,900  [▓▓▓▓▓▓▓▓▓░]
   Saturday  : ₹ 51,200  [▓▓▓▓▓▓▓▓▓▓] ← BEST DAY
   Sunday    : ₹ 15,300  [▓▓▓░░░░░░░]
   ────────────────────────────────────────
   Total     : ₹2,27,300
   Average   : ₹ 32,471
   Best Day  : Saturday (₹51,200)
   Worst Day : Sunday   (₹15,300)
   Above Avg : 4 days out of 7
   ════════════════════════════════════════
Include a simple ASCII bar chart using string multiplication for visual effect

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EXERCISE 3 — Bank Transaction CSV Parser (25 min)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Load: bank_transactions.csv (Date, Description, Debit, Credit, Balance)

Scenario: "The accounts assistant at SDNB College needs to reconcile 
the bank statement. Build an automated analyser."

Analyses:
1. Count Credit entries vs Debit entries (use fillna(0) for missing amounts)
2. Total credits received, Total debits made
3. Largest single credit transaction (who paid the most?)
4. Largest single debit (what was the biggest expense?)
5. Average transaction size (credit), Average transaction size (debit)
6. Filter: Show all transactions above ₹50,000
7. Monthly summary: Credits vs Debits by month
8. Check: Does the final balance in the CSV match running calculation?

Print a Bank Reconciliation Statement format output.
Add a simple bar chart comparing monthly inflows vs outflows.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EXERCISE 4 — Inventory File Management (20 min)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Load: inventory.csv (ProductID, Name, Category, Stock, UnitPrice)

Part A — Read & Display:
- Load CSV, display neatly
- Show total inventory value (Stock × UnitPrice summed)
- Identify low-stock items (Stock < 10) — "Reorder Alert"
- Show top 5 most valuable items in inventory

Part B — Append New Product:
new_product = {"ProductID": "P031", "Name": "...", "Category": "...", 
               "Stock": 50, "UnitPrice": 299.00}
→ Use pd.concat() to add new row
→ Save back to CSV: df.to_csv("inventory_updated.csv", index=False)
→ Reload and verify the new product appears

Print a Stock Status Report showing:
- Items in stock (green ✅), Low stock (yellow ⚠️), Out of stock (red ❌)
- Total SKUs, Total units, Total inventory value
```

---

## Notebook 5 — Day 4 Afternoon (Thursday, April 30 | 2:00 PM – 4:00 PM)

### File: `Day4_Afternoon_KPI_Dashboard.ipynb`

```
Create Day4_Afternoon_KPI_Dashboard.ipynb

This is the most impressive notebook — students should feel proud 
showing this to anyone. Design it like a real business intelligence report.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 1 — Exam Marks Analyser (30 min)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Load: exam_marks.csv (RollNo, Name, Maths, Accounts, Economics, Commerce, English)

Build a complete result processing system:
1. Calculate total marks (out of 500) and percentage for each student
2. Assign grade: 
   90%+ = O (Outstanding), 75-89% = A+ (Excellent), 
   60-74% = A (Very Good), 50-59% = B+ (Good),
   40-49% = B (Pass), Below 40% = F (Fail)
3. Calculate class rank (1 = highest marks)
4. Class statistics: Highest %, Lowest %, Class Average %, Pass %
5. Subject-wise analysis: Which subject had highest average? Lowest pass rate?

Output must look like a real marksheet AND a class progress report:
Print top 10 rankers leaderboard.
Print students who failed any subject (remedial list).
Create a subject-wise performance bar chart.
Create a grade distribution pie chart.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 2 — KPI Business Dashboard (60 min) ← CENTREPIECE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Scenario: "You have been hired as a Business Analyst intern at 
Chennai Fashions Pvt Ltd. The CEO wants a monthly KPI report on her desk 
by Monday morning. Build it in Python."

Define these KPIs with formulas (show each as a Markdown formula block first):

PROFITABILITY KPIs:
- Gross Profit Margin = (Revenue - COGS) / Revenue × 100
- Net Profit Margin   = Net Profit / Revenue × 100
- EBITDA Margin       = EBITDA / Revenue × 100

OPERATIONAL KPIs:
- Inventory Turnover  = COGS / Average Inventory
- Days Sales Outstanding (DSO) = (Accounts Receivable / Revenue) × 365
- Operating Expense Ratio = Operating Expenses / Revenue × 100

GROWTH KPIs:
- Revenue Growth (MoM%) = (This Month - Last Month) / Last Month × 100
- Customer Acquisition Cost (CAC) = Marketing Spend / New Customers

RETAIL KPIs:
- Average Transaction Value (ATV) = Total Revenue / Number of Transactions
- Conversion Rate = (Buyers / Visitors) × 100
- Return on Investment (ROI) = (Gain - Cost) / Cost × 100

Build this in 3 parts:

PART A: KPI Calculator Functions
Define a function for EACH KPI above. Each function:
- Has a clear docstring explaining what it measures and why it matters
- Takes relevant parameters
- Returns the calculated value AND a rating (🟢 Good / 🟡 Average / 🔴 Needs Attention)
  based on industry benchmarks for Indian retail

PART B: Load Real Data & Calculate All KPIs
Use sales_data.csv + a business_summary dict you define at the top:
business_data = {
    "revenue": 28_50_000,
    "cogs": 17_10_000,
    "operating_expenses": 5_42_000,
    "net_profit": 3_89_000,
    "marketing_spend": 1_25_000,
    "new_customers": 312,
    "total_transactions": 1840,
    "store_visitors": 4200,
    "accounts_receivable": 3_45_000,
    "avg_inventory": 8_20_000,
    "last_month_revenue": 25_60_000
}

Calculate every KPI. Store results in a dictionary.

PART C: Dashboard Visualisation
Create a professional 3×3 matplotlib dashboard (fig, axes = plt.subplots(3, 3)):
- Panel 1: KPI scorecard (text-based, show all KPIs with RAG status)
- Panel 2: Revenue vs COGS bar chart
- Panel 3: Profit margins gauge/bar
- Panel 4: Monthly revenue trend line chart
- Panel 5: Expense breakdown pie chart
- Panel 6: Customer metrics bar chart
- Panel 7: Top products by revenue
- Panel 8: Regional sales heatmap (bar chart by region)
- Panel 9: KPI summary table

Style the entire dashboard in a dark professional theme:
plt.style.use('dark_background')
Use: red for negative metrics, green for positive, gold for targets

Title: "CHENNAI FASHIONS PVT LTD — BUSINESS INTELLIGENCE DASHBOARD | APR 2026"
Save: plt.savefig("capstone/kpi_dashboard.png", dpi=200, bbox_inches='tight')

Add a "📋 Executive Summary" Markdown cell at the end with:
- 3 key highlights (auto-generated from the KPI values)
- 2 areas of concern (auto-detected from 🔴 KPIs)
- 1 recommendation
```

---

## Notebook 6 — Capstone Project (Thursday, April 30 | 4:00 PM – 4:30 PM submission)

### File: `Capstone_Business_Analytics_Report.ipynb`

```
Create Capstone_Business_Analytics_Report.ipynb

This is the final submission notebook. It must be the most impressive file 
in the folder. Think of it as a Data Analyst's final report to a CEO.
Every section should show clear business thinking, not just code.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAPSTONE SCENARIO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"SDNB Retail Analytics — End of Quarter Business Review"

You are a Business Analytics Intern at SDNB Retail Pvt Ltd, a 
mid-sized textile and consumer goods retail chain with 5 branches 
across Tamil Nadu (Chennai, Coimbatore, Madurai, Tiruchirappalli, Salem).

The CEO, Ms. Devika Nair, has asked for a complete end-of-quarter analysis 
report before the Board Meeting. She is not technical — she wants clear 
charts, plain-English insights, and specific recommendations.

Your task: Analyse 3 months of sales, expenses, and customer data,
and produce a professional Business Analytics Report.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
NOTEBOOK STRUCTURE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CELL 1 — Cover Page (Markdown)
Beautiful styled cover with:
# 📊 SDNB RETAIL PVT LTD
## Business Analytics Report — Q1 2026 (January–March)
**Prepared by:** [Student Name] | **Date:** April 30, 2026
**Submitted to:** Ms. Devika Nair, CEO
Include a styled HTML table showing:
| Report Section | Page | Status |
with all sections listed and ✅ marks

CELL 2 — Table of Contents (Markdown with jump links)
1. Executive Summary
2. Revenue Analysis
3. Regional Performance
4. Product Category Analysis
5. Customer Analytics
6. Expense & Profitability Analysis
7. Trend Analysis & Forecasting
8. Recommendations
9. Appendix: Data Quality Report

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 1 — Data Loading & Quality Check
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Load ALL CSV files from the data/ folder.
For each dataset, print a Data Quality Report:
- Row count, Column count
- Missing values (count + %)
- Duplicate rows
- Data type issues
- Date range coverage
- "✅ Data is clean" or "⚠️ Issues found: ..."

After cleaning, print: "All datasets loaded. Total records: X,XXX rows ready for analysis."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 2 — Executive Summary (auto-generated)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
THIS MUST BE COMPLETELY AUTO-GENERATED FROM THE DATA.
No hardcoded strings in the summary — every number must come from a variable.

Build a function: def generate_executive_summary(sales_df, expenses_df):
It must print a board-room ready summary:
   ╔══════════════════════════════════════════════════════════════╗
   ║           EXECUTIVE SUMMARY — Q1 2026                      ║
   ║           SDNB RETAIL PVT LTD                              ║
   ╠══════════════════════════════════════════════════════════════╣
   ║ Total Revenue    : ₹XX,XX,XXX  (↑ X% vs last quarter)     ║
   ║ Gross Profit     : ₹XX,XX,XXX  (Margin: XX.X%)            ║
   ║ Net Profit       : ₹XX,XX,XXX  (Margin: XX.X%)            ║
   ║ Top Branch       : [City]       (₹XX,XX,XXX)              ║
   ║ Top Category     : [Category]   (XX% of revenue)          ║
   ║ Total Customers  : X,XXX        (XX new this quarter)     ║
   ╠══════════════════════════════════════════════════════════════╣
   ║ 🟢 HIGHLIGHTS: [auto-detected best performing areas]      ║
   ║ 🔴 CONCERNS:   [auto-detected underperforming areas]      ║
   ╚══════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 3 — Revenue Deep Dive
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Using sales_data.csv, perform and visualise ALL of:
1. Monthly revenue trend (line chart) — Jan, Feb, Mar
   Add month-over-month growth % annotations on the chart
2. Revenue by day of week (bar chart) — which days are busiest?
3. Revenue by product category (horizontal bar chart, sorted descending)
4. Top 10 products by revenue (horizontal bar chart)
5. Revenue contribution: each category as % of total (pie)

For each chart:
- Professional title
- Data labels on bars/slices
- Source annotation: "Source: SDNB Sales System | Q1 2026"
- Key insight text below: "💡 Insight: ..."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 4 — Regional Performance Analysis
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Analyse performance across 5 Tamil Nadu branches.

Create:
1. Revenue by branch (bar chart with target line at average)
2. Branch performance scorecard table:
   | Branch      | Revenue     | % of Total | vs Average | Rank | Status  |
   | Chennai     | ₹X,XX,XXX   | 35%        | +15%       | 1    | 🏆 Star  |
   | Coimbatore  | ₹X,XX,XXX   | 22%        | +2%        | 2    | ✅ Good  |
   | Madurai     | ₹X,XX,XXX   | 18%        | -5%        | 3    | ⚠️ Watch |
   | ...
3. Growth rate by branch (which branch is growing fastest?)

Insight cell: Which branch needs management attention? Why?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 5 — Customer Analytics
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Using customer_ages.csv:
1. Customer age distribution histogram (styled)
2. Customer segmentation: Premium vs Regular (count and revenue contribution)
3. City-wise customer distribution
4. Average transaction value by segment
5. Customer lifetime value estimate (simple: avg_purchase × avg_frequency × 12)

Insight: "Our target demographic is XX-XX year olds representing XX% of revenue.
Consider launching a loyalty programme for the XX-XX age group."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 6 — Expense & Profitability Analysis
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Using monthly_expenses.csv:
1. Expense breakdown pie chart (which categories cost the most?)
2. Monthly expense trend (are costs rising?)
3. Revenue vs Expenses waterfall chart (simple stacked bar)
4. Profit margin by month (line chart)
5. Cost per rupee of revenue (operating leverage metric)

Flag any expense category that grew faster than revenue (cost creep warning).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 7 — Trend Analysis & Simple Forecasting
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Using numpy for simple linear regression trend line:
1. Plot Q1 monthly revenue with trend line extended to Q2 (Apr, May, Jun)
2. Calculate: If current trend continues, what will Q2 revenue likely be?
3. Show optimistic (+10%) and pessimistic (-5%) scenarios as shaded bands

Keep explanation very simple:
"We draw a straight line through our past data points and extend it forward.
This is not a guarantee — it is a directional estimate based on current momentum."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 8 — Final Dashboard (THE MASTERPIECE)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Create ONE publication-quality dashboard — 4×3 grid (12 panels):

Row 1: KPI scorecards (4 panels, text-based):
  [Total Revenue] [Gross Profit %] [Net Profit %] [Revenue Growth]

Row 2: Core charts:
  [Monthly Revenue Trend] [Revenue by Category] [Branch Performance]

Row 3: Deep-dive charts:
  [Customer Segments] [Expense Breakdown] [Top 10 Products] [Ad Spend ROI]

Styling requirements:
- Dark professional background (#1a1a2e)
- Gold (#C8860A) for highlights
- Green for positive values, red for negative
- Company logo placeholder (text in top-left)
- Report date and page number in bottom-right
- Consistent font size hierarchy
- Every panel has a title + one-line insight

Save: plt.savefig("capstone/SDNB_Q1_2026_Analytics_Report.png", 
                  dpi=300, bbox_inches='tight', facecolor='#1a1a2e')

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 9 — Recommendations (Markdown)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
This section is a Markdown cell — students fill it in themselves.
But provide a structured template they MUST follow:

## 📋 Recommendations to Management

### Immediate Actions (This Week)
1. **[Finding from data]:** [Recommendation] → Expected Impact: ₹XX,XXX

### Short-Term (Next Month)
1. **[Finding]:** [Recommendation] → Expected Impact: X% improvement

### Strategic (Next Quarter)
1. **[Finding]:** [Recommendation] → Target: ₹X,XX,XXX additional revenue

### Risk Mitigation
1. **[Risk identified]:** [Mitigation plan]

---
*This report was generated using Python (Pandas + Matplotlib).
Prepared by: [Name], SDNB Vaishnav College for Women, Chromepet, Chennai*

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 10 — Appendix: Code Summary
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Final Markdown cell listing:
- All Python concepts used in this capstone
- All libraries imported
- Files read and written
- Charts generated
"If you understood and built this project, you have the skills of a 
Junior Business Analyst. Well done!"
```

---

## Final Polish — Run This Last

```
Do a final pass on all 6 notebooks in sdnb_python_workshop/notebooks/:

1. COLAB COMPATIBILITY: Add this as the very first code cell in every notebook:
   # ── Install & Setup (run this first on Google Colab) ──
   import sys, os
   try:
       import pandas as pd
       import matplotlib.pyplot as plt
       import numpy as np
       print("✅ All libraries ready!")
   except ImportError as e:
       print(f"Installing missing library: {e}")
       os.system(f"pip install pandas matplotlib numpy seaborn -q")
   
   # Set working directory to find data files
   # If on Colab, data files are in /content/sdnb_python_workshop/data/
   # If local, adjust this path:
   DATA_PATH = "data/"  # Change to full path if needed

2. CELL METADATA: Make sure every notebook has:
   - First cell: Markdown with the day title, date, time, and objectives
   - Last cell: Markdown with recap + "What's next?" link to next notebook

3. CHECKPOINT CELLS: After every major exercise, add a code cell:
   print("✅ Exercise X complete! Great work.")
   
4. ERROR HANDLING: Wrap all file reads in try/except with helpful messages:
   try:
       df = pd.read_csv(DATA_PATH + "sales_data.csv")
       print(f"✅ Loaded {len(df)} sales records")
   except FileNotFoundError:
       print("⚠️ File not found. Make sure you're in the right folder.")
       print("  Expected location: sdnb_python_workshop/data/sales_data.csv")
       print("  Creating sample data instead...")
       # fallback: create sample DataFrame inline

5. PROGRESSIVE DIFFICULTY: Check that within each notebook,
   exercises increase in complexity — early exercises have more
   hand-holding comments, later exercises have less.

6. Create a requirements.txt file:
   pandas>=2.0.0
   matplotlib>=3.7.0
   numpy>=1.24.0
   seaborn>=0.12.0
   openpyxl>=3.1.0

7. Update README.md with:
   - How to open in Google Colab (step-by-step with screenshots description)
   - Quick start: "Run notebooks in this order: Day1 → Day2 → Day3 → Day4_Morning → Day4_Afternoon → Capstone"
   - Note: "All data files are in the data/ folder. Do not move them."
```

---

## Summary Table

| Notebook | Day | Duration | Key Skills | Commerce Context |
|---|---|---|---|---|
| Day1_Python_Basics_and_Finance | Mon Apr 27 | 3 hrs | Variables, loops, lists, I/O | SI/CI, Currency, Sales, Savings |
| Day2_Functions_and_Business_Logic | Tue Apr 28 | 3 hrs | Functions, error handling | Payslip, GST Invoice, FD, Commission |
| Day3_Data_Visualisation | Wed Apr 29 | 3 hrs | Matplotlib, Seaborn | Expenses, Market Share, Customer Age, Ad ROI |
| Day4_Morning_Data_Analysis | Thu Apr 30 AM | 3 hrs | Pandas, CSV I/O | Sales CSV, Bank Stmt, Inventory |
| Day4_Afternoon_KPI_Dashboard | Thu Apr 30 PM | 2 hrs | Pandas + Matplotlib combined | Marksheet, KPI Dashboard |
| Capstone_Business_Analytics_Report | Thu Apr 30 final | 30 min submit | Full pipeline | End-to-end Q1 business report |

---

*All prompts above are designed for **Claude Code** (`claude` CLI). Run them in the `sdnb_python_workshop/` directory. Each prompt generates one complete, runnable `.ipynb` file.*
