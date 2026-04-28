"""Build 100_Python_Examples.ipynb — Colab-friendly demo notebook."""

from nb_helpers import Notebook

nb = Notebook()

# ── Cover ────────────────────────────────────────────────────────────────
nb.md("""
# 🐍 100 Python Examples — Basic to Intermediate
**SDNB Vaishnav College for Women, Chromepet**
*Business Analytics Using Python — Reference Notebook*

---

This notebook contains **100 short Python examples** (1–10 lines each), themed around accounting and commerce. Each example is in its own cell — run them in order, or jump to any section.

| Section | Examples | Topic |
|---------|----------|-------|
| 1 | 1–15 | Print, variables, numbers, basic math |
| 2 | 16–25 | Strings |
| 3 | 26–35 | Input & type conversion |
| 4 | 36–45 | Conditionals (`if/elif/else`, boolean logic) |
| 5 | 46–55 | Lists |
| 6 | 56–65 | Loops (`for`, `while`) |
| 7 | 66–75 | Comprehensions, sorting, filtering |
| 8 | 76–85 | Dictionaries, tuples, sets |
| 9 | 86–95 | Functions |
| 10 | 96–100 | Exceptions, files, modules |

### ▶️ How to run on Google Colab
1. Open Colab → **File → Upload notebook** → pick this `.ipynb`.
2. Press **Runtime → Run all**, or run any cell by clicking it and pressing **Shift + Enter**.

> Examples 26–35 use `input()`. Each shows the live interactive line as a comment, plus a hardcoded version below it that runs without prompting.
""")

# ──────────────────────────────────────────────────────────────────────
# Helper: add a section header and a list of (title, code) examples.
# ──────────────────────────────────────────────────────────────────────

def section(heading, blurb=""):
    md = f"## {heading}"
    if blurb:
        md += "\n\n" + blurb
    nb.md(md)


def ex(num, title, code):
    """Add one numbered example as a single code cell."""
    nb.code(f"# {num}. {title}\n{code}")


# ──────────────────────────────────────────────────────────────────────
# 1-15  PRINT, VARIABLES, NUMBERS, BASIC MATH
# ──────────────────────────────────────────────────────────────────────
section("1️⃣ Print, Variables, Numbers, Basic Math (Examples 1–15)")

ex(1,  "Hello world",
   'print("Hello, SDNB!")')
ex(2,  "Print multiple values separated by commas",
   'print("Invoice", 2026, "amount", 4500)')
ex(3,  "Custom separator and ending",
   'print("A", "B", "C", sep=" | ", end=".\\n")')
ex(4,  "Assign a variable",
   'petty_cash = 500\nprint(petty_cash)')
ex(5,  "Multiple assignment in one line",
   'basic, hra, special = 25000, 10000, 5000\nprint(basic, hra, special)')
ex(6,  "Integer arithmetic",
   'print(45 + 12 - 7 * 3)')
ex(7,  "Float (decimal) arithmetic",
   'print(2499.99 * 0.18)')
ex(8,  "Floor division and modulo",
   'print(47 // 12, 47 % 12)        # full cartons + leftover units')
ex(9,  "Power operator",
   'print(1.08 ** 5)                # CI growth factor at 8% over 5 years')
ex(10, "Rounding for money",
   'print(round(0.1 + 0.2, 2))      # → 0.3 (cleaned up)')
ex(11, "Check the type of a value",
   'print(type(2499.99))            # → <class \'float\'>')
ex(12, "Convert int → float and back",
   'print(float(45), int(99.7))')
ex(13, "f-string with a number",
   'amount = 8499\nprint(f"Amount: ₹{amount}")')
ex(14, "f-string with thousand separator and 2 decimals",
   'gross = 1234567.5\nprint(f"₹{gross:,.2f}")         # → ₹1,234,567.50')
ex(15, "Constants and naming convention",
   'GST_RATE = 0.18                 # ALL_CAPS = constant\nprint(GST_RATE)')


# ──────────────────────────────────────────────────────────────────────
# 16-25  STRINGS
# ──────────────────────────────────────────────────────────────────────
section("2️⃣ Strings (Examples 16–25)")

ex(16, "Concatenate strings with +",
   'print("INV-" + "2026-" + "001")')
ex(17, "Repeat a string",
   'print("=" * 40)')
ex(18, "Length of a string",
   'print(len("SDNB Vaishnav College"))')
ex(19, "Upper / lower case",
   'print("sdnb".upper(), "CHENNAI".lower())')
ex(20, "Strip whitespace",
   'print("   Chennai   ".strip())')
ex(21, "Split a string into a list",
   'print("Saree,Kurti,Bedsheet".split(","))')
ex(22, "Replace text",
   'print("Invoice 2026".replace("2026", "2027"))')
ex(23, "Slice a string",
   'print("INV-2026-001"[4:8])      # → 2026')
ex(24, "startswith / endswith / in",
   'print("INV-2026".startswith("INV"), "saree" in "Silk saree pack")')
ex(25, "Multi-line string with triple quotes",
   '''note = """Dear Customer,
Your invoice is attached.
Regards, SDNB"""
print(note)''')


# ──────────────────────────────────────────────────────────────────────
# 26-35  INPUT & TYPE CONVERSION
# ──────────────────────────────────────────────────────────────────────
section("3️⃣ Input & Type Conversion (Examples 26–35)",
        "Each example shows the live `input()` form as a comment, then a "
        "hardcoded version below it that actually runs.")

ex(26, "Read a name as text",
   '''# name = input("Your name: ")
name = "Priya"   # demo value
print("Welcome,", name)''')
ex(27, "Read a number as int",
   '''# qty = int(input("Quantity: "))
qty = 12         # demo value
print("Total units:", qty)''')
ex(28, "Read a price as float",
   '''# price = float(input("Price ₹: "))
price = 2499.99  # demo value
print(f"Recorded ₹{price:,.2f}")''')
ex(29, "Mini GST calculator from user input",
   '''# bill = float(input("Bill amount: "))
bill = 6750
print(f"GST 18% = ₹{bill * 0.18:,.2f}")''')
ex(30, "USD to INR converter",
   '''# usd = float(input("USD: "))
usd = 2500
print(f"INR = ₹{usd * 83.50:,.2f}")''')
ex(31, "Read two numbers and add",
   '''# a = float(input("a: ")); b = float(input("b: "))
a, b = 1500.0, 2300.0
print("Sum:", a + b)''')
ex(32, "Read 3 marks and compute average",
   '''# m1, m2, m3 = [int(input(f"Mark {i+1}: ")) for i in range(3)]
m1, m2, m3 = 78, 85, 91
print("Average:", (m1 + m2 + m3) / 3)''')
ex(33, "Simple Interest from user input",
   '''# p = float(input("Principal: "))
# r = float(input("Rate %: "))
# t = int(input("Years: "))
p, r, t = 100000, 8, 5
print("Simple Interest =", p * r * t / 100)''')
ex(34, "Boolean from yes/no input",
   '''# answer = input("GST registered? (y/n) ").lower()
answer = "y"
print("Registered:", answer == "y")''')
ex(35, "Wrap input + arithmetic in one line",
   '''# print("Total:", float(input("Price: ")) * int(input("Qty: ")))
price, qty = 1299, 4
print("Total:", price * qty)''')


# ──────────────────────────────────────────────────────────────────────
# 36-45  CONDITIONALS
# ──────────────────────────────────────────────────────────────────────
section("4️⃣ Conditionals (Examples 36–45)")

ex(36, "Compare two numbers",
   'revenue, target = 75000, 50000\nprint("Target met:", revenue >= target)')
ex(37, "Logical AND / OR / NOT",
   'salary, score = 32000, 720\nprint("Loan eligible:", salary > 25000 and score >= 700)')
ex(38, "if / else",
   'age = 30\nprint("Adult" if age >= 18 else "Minor")')
ex(39, "if / elif / else for grades",
   '''pct = 72
if pct >= 90:   grade = "O"
elif pct >= 75: grade = "A+"
elif pct >= 60: grade = "A"
else:           grade = "B"
print("Grade:", grade)''')
ex(40, "Ternary (one-line if/else)",
   'stock = 8\nstatus = "LOW" if stock < 10 else "OK"\nprint(status)')
ex(41, "Truthy / falsy values",
   'print(bool(0), bool(""), bool([]), bool("x"))')
ex(42, "is None check",
   'email = None\nprint("Missing email" if email is None else email)')
ex(43, "Min / max of two",
   'print(min(120, 90), max(120, 90))')
ex(44, "Absolute value",
   'diff = 5000 - 7500\nprint("Loss:", abs(diff))')
ex(45, "Chained comparison",
   'mark = 67\nprint("Pass" if 40 <= mark < 80 else "Other")')


# ──────────────────────────────────────────────────────────────────────
# 46-55  LISTS
# ──────────────────────────────────────────────────────────────────────
section("5️⃣ Lists (Examples 46–55)")

ex(46, "Create a list",
   'prices = [499, 1299, 2499, 799, 3999]\nprint(prices)')
ex(47, "Index access (positive and negative)",
   'prices = [499, 1299, 2499, 799, 3999]\nprint(prices[0], prices[-1])')
ex(48, "Slice a list",
   'prices = [499, 1299, 2499, 799, 3999]\nprint(prices[1:4])')
ex(49, "Append a new value",
   'prices = [499, 1299, 2499]\nprices.append(599)\nprint(prices)')
ex(50, "Remove a value",
   'prices = [499, 1299, 2499, 799]\nprices.remove(799)\nprint(prices)')
ex(51, "Sort ascending and descending",
   '''prices = [499, 1299, 2499, 799, 3999]
prices.sort()
print(prices)
prices.sort(reverse=True)
print(prices)''')
ex(52, "Reverse in place",
   'nums = [1, 2, 3]\nnums.reverse()\nprint(nums)')
ex(53, "Built-in summaries",
   'prices = [499, 1299, 2499, 799, 3999]\nprint(sum(prices), min(prices), max(prices), len(prices))')
ex(54, "Average of a list",
   'prices = [499, 1299, 2499, 799, 3999]\nprint(sum(prices) / len(prices))')
ex(55, "Membership test",
   'prices = [499, 1299, 2499]\nprint(2499 in prices)')


# ──────────────────────────────────────────────────────────────────────
# 56-65  LOOPS
# ──────────────────────────────────────────────────────────────────────
section("6️⃣ Loops (Examples 56–65)")

ex(56, "for over a list",
   '''for p in [499, 1299, 2499]:
    print(f"₹{p}")''')
ex(57, "for with enumerate",
   '''for i, m in enumerate(["Apr", "May", "Jun"], 1):
    print(i, m)''')
ex(58, "for over range",
   '''for n in range(1, 6):
    print("Day", n)''')
ex(59, "for with a step",
   '''for n in range(0, 21, 5):
    print(n)''')
ex(60, "while loop",
   '''balance = 10000
while balance > 0:
    balance -= 2500
    print("Remaining:", balance)''')
ex(61, "Break out of a loop",
   '''for n in range(1, 100):
    if n > 5:
        break
    print(n)''')
ex(62, "continue (skip iteration)",
   '''for n in range(1, 6):
    if n == 3:
        continue
    print(n)''')
ex(63, "Nested loops — multiplication grid",
   '''for q in [10, 50, 100]:
    for d in [0, 5, 10]:
        print(q, d, q * (1 - d / 100))''')
ex(64, "Sum with a for loop",
   '''total = 0
for s in [3450, 1200, 5400, 2780, 950]:
    total += s
print("Total:", total)''')
ex(65, "Count items meeting a condition",
   '''sales = [3450, 1200, 5400, 2780, 950]
above = sum(1 for s in sales if s > 2000)
print("Sales above ₹2,000:", above)''')


# ──────────────────────────────────────────────────────────────────────
# 66-75  COMPREHENSIONS / SORT / FILTER
# ──────────────────────────────────────────────────────────────────────
section("7️⃣ Comprehensions, Sorting, Filtering (Examples 66–75)")

ex(66, "List comprehension — squares",
   'print([n * n for n in range(1, 6)])')
ex(67, "Add GST to every price",
   'prices = [499, 1299, 2499]\nprint([round(p * 1.18, 2) for p in prices])')
ex(68, "Conditional comprehension",
   'print([p for p in [499, 1299, 2499, 99] if p > 500])')
ex(69, "Build a list of strings",
   'prices = [499, 1299, 2499]\nprint([f"₹{p:,}" for p in prices])')
ex(70, "Sum via comprehension",
   'prices = [499, 1299, 2499]\nprint(sum(p for p in prices))')
ex(71, "sorted() with a key (case-insensitive)",
   'names = ["priya", "ARUN", "kavitha"]\nprint(sorted(names, key=str.lower))')
ex(72, "sorted() of dicts by a field",
   '''sales = [{"prod": "Saree", "amt": 2499}, {"prod": "Kurti", "amt": 1299}]
print(sorted(sales, key=lambda r: r["amt"], reverse=True))''')
ex(73, "filter() with a lambda",
   'prices = [499, 1299, 2499]\nprint(list(filter(lambda p: p > 1000, prices)))')
ex(74, "map() with a lambda",
   'prices = [499, 1299, 2499]\nprint(list(map(lambda p: round(p * 1.18, 2), prices)))')
ex(75, "Combine two lists with zip()",
   '''months = ["Jan", "Feb", "Mar"]
revenue = [120000, 150000, 175000]
print(list(zip(months, revenue)))''')


# ──────────────────────────────────────────────────────────────────────
# 76-85  DICTS, TUPLES, SETS
# ──────────────────────────────────────────────────────────────────────
section("8️⃣ Dictionaries, Tuples, Sets (Examples 76–85)")

ex(76, "Create a dictionary (customer record)",
   'customer = {"name": "Priya", "balance": 45000, "city": "Chennai"}\nprint(customer)')
ex(77, "Access by key",
   'customer = {"name": "Priya", "balance": 45000}\nprint(customer["name"])')
ex(78, "Update / add a key",
   '''customer = {"name": "Priya", "balance": 45000}
customer["balance"] = 47500
customer["email"] = "priya@example.com"
print(customer)''')
ex(79, "Safe get with default",
   'customer = {"name": "Priya"}\nprint(customer.get("phone", "N/A"))')
ex(80, "Loop over keys, values, items",
   '''customer = {"name": "Priya", "balance": 45000, "city": "Chennai"}
for key, val in customer.items():
    print(key, "=", val)''')
ex(81, "Dict comprehension — square map",
   'print({n: n * n for n in range(1, 6)})')
ex(82, "Count word frequency with a dict",
   '''words = "saree kurti saree bedsheet kurti saree".split()
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
print(freq)''')
ex(83, "Tuple — fixed pair (immutable)",
   'point = ("Chennai", 600044)\nprint(point[0], point[1])')
ex(84, "Tuple unpacking",
   'city, pin = ("Chennai", 600044)\nprint(city, pin)')
ex(85, "Sets and union/intersection",
   '''a = {"saree", "kurti", "watch"}
b = {"watch", "bedsheet"}
print(a | b, a & b)              # union, intersection''')


# ──────────────────────────────────────────────────────────────────────
# 86-95  FUNCTIONS
# ──────────────────────────────────────────────────────────────────────
section("9️⃣ Functions (Examples 86–95)")

ex(86, "Define and call a function",
   '''def greet(name):
    print(f"Welcome, {name}!")
greet("Priya")''')
ex(87, "Return a value",
   '''def add_gst(price, rate=0.18):
    return round(price * (1 + rate), 2)
print(add_gst(2499))''')
ex(88, "Function with default parameter",
   '''def discount(price, pct=10):
    return price - price * pct / 100
print(discount(2499), discount(2499, 25))''')
ex(89, "Multiple return values",
   '''def stats(nums):
    return min(nums), max(nums), sum(nums) / len(nums)
print(stats([3450, 1200, 5400]))''')
ex(90, "*args (any number of arguments)",
   '''def total(*amounts):
    return sum(amounts)
print(total(100, 200, 300, 400))''')
ex(91, "**kwargs (keyword arguments)",
   '''def invoice(**fields):
    for k, v in fields.items():
        print(k, ":", v)
invoice(no="INV-001", amount=4500, gst=810)''')
ex(92, "Lambda (anonymous function)",
   'square = lambda x: x * x\nprint(square(7))')
ex(93, "Recursion — factorial",
   '''def fact(n):
    return 1 if n <= 1 else n * fact(n - 1)
print(fact(5))''')
ex(94, "Nested functions / closures",
   '''def make_taxer(rate):
    def add_tax(p):
        return p * (1 + rate)
    return add_tax
gst = make_taxer(0.18)
print(round(gst(2499), 2))''')
ex(95, "Docstring on a function",
   '''def margin(rev, cost):
    """Return profit margin in %."""
    return (rev - cost) / rev * 100
print(round(margin(28_50_000, 17_10_000), 2))''')


# ──────────────────────────────────────────────────────────────────────
# 96-100  EXCEPTIONS, FILES, MODULES
# ──────────────────────────────────────────────────────────────────────
section("🔟 Exceptions, Files, Modules (Examples 96–100)")

ex(96, "try / except for safe input parsing",
   '''try:
    n = int("ABC")               # this fails on purpose
except ValueError:
    print("Not a valid number")''')
ex(97, "try / except / finally",
   '''try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Cleanup done")''')
ex(98, "Write a small text file",
   '''with open("hello.txt", "w") as f:
    f.write("SDNB Workshop notes\\nLine 2\\n")
print("✅ wrote hello.txt")''')
ex(99, "Read it back, line by line",
   '''with open("hello.txt") as f:
    for line in f:
        print(line.strip())''')
ex(100, "Use built-in modules",
   '''import math, datetime, random
print(math.sqrt(16), datetime.date.today(), random.randint(1, 100))''')


# ── End ─────────────────────────────────────────────────────────────────
nb.md("""
## 🎓 You did it!

If you've worked through all 100, you now know:

- ✅ How to print, store and format data
- ✅ How to manipulate text and numbers
- ✅ How to take input and make decisions
- ✅ How to work with lists, dicts, tuples, sets
- ✅ How to write loops and comprehensions
- ✅ How to build and call functions (including `*args`, lambdas, recursion, closures)
- ✅ How to handle errors, read & write files, and use built-in modules

You're ready to move on to the **main workshop notebooks** in the same folder:
**Day1 → Day2 → Day3 → Day4 → Capstone.**
""")

path = nb.save("100_Python_Examples.ipynb")
print("✅ Built", path)
