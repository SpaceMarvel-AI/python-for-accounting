# =====================================================================
#  100 Python Examples — Basic to Intermediate
#  SDNB Python Workshop | Each example is 1-10 lines.
#  Open in IDLE, copy any block into the shell, and try it out.
# =====================================================================
#
#  SECTIONS:
#    1-15   : Print, variables, numbers, basic math
#    16-25  : Strings
#    26-35  : Input & type conversion
#    36-45  : Conditionals (if/elif/else, boolean logic)
#    46-55  : Lists
#    56-65  : Loops (for, while)
#    66-75  : List comprehensions, sorting, filtering
#    76-85  : Dictionaries, tuples, sets
#    86-95  : Functions
#    96-100 : Exceptions, files, modules
# =====================================================================


# ─────────────────────────────────────────────────────────────────────
#  1-15  PRINT, VARIABLES, NUMBERS, BASIC MATH
# ─────────────────────────────────────────────────────────────────────

# 1. Hello world
print("Hello, SDNB!")

# 2. Print multiple values separated by commas
print("Invoice", 2026, "amount", 4500)

# 3. Custom separator and ending
print("A", "B", "C", sep=" | ", end=".\n")

# 4. Assign a variable
petty_cash = 500

# 5. Multiple assignment in one line
basic, hra, special = 25000, 10000, 5000

# 6. Integer arithmetic
print(45 + 12 - 7 * 3)

# 7. Float (decimal) arithmetic
print(2499.99 * 0.18)

# 8. Floor division and modulo
print(47 // 12, 47 % 12)        # full cartons + leftover units

# 9. Power operator
print(1.08 ** 5)                # CI growth factor at 8% over 5 years

# 10. Rounding for money
print(round(0.1 + 0.2, 2))      # → 0.3 (cleaned up)

# 11. Check the type of a value
print(type(2499.99))            # → <class 'float'>

# 12. Convert int → float and back
print(float(45), int(99.7))

# 13. f-string with a number
amount = 8499
print(f"Amount: ₹{amount}")

# 14. f-string with thousand separator and 2 decimals
gross = 1234567.5
print(f"₹{gross:,.2f}")         # → ₹1,234,567.50

# 15. Constants and naming convention
GST_RATE = 0.18                 # ALL_CAPS = constant


# ─────────────────────────────────────────────────────────────────────
#  16-25  STRINGS
# ─────────────────────────────────────────────────────────────────────

# 16. Concatenate strings with +
print("INV-" + "2026-" + "001")

# 17. Repeat a string
print("=" * 40)

# 18. Length of a string
print(len("SDNB Vaishnav College"))

# 19. Upper / lower case
print("sdnb".upper(), "CHENNAI".lower())

# 20. Strip whitespace
print("   Chennai   ".strip())

# 21. Split a string into a list
print("Saree,Kurti,Bedsheet".split(","))

# 22. Replace text
print("Invoice 2026".replace("2026", "2027"))

# 23. Slice a string
print("INV-2026-001"[4:8])      # → 2026

# 24. startswith / endswith / in
print("INV-2026".startswith("INV"), "saree" in "Silk saree pack")

# 25. Multi-line string with triple quotes
note = """Dear Customer,
Your invoice is attached.
Regards, SDNB"""
print(note)


# ─────────────────────────────────────────────────────────────────────
#  26-35  INPUT & TYPE CONVERSION
# ─────────────────────────────────────────────────────────────────────

# 26. Read a name as text
# name = input("Your name: ")
# print("Welcome,", name)

# 27. Read a number as int
# qty = int(input("Quantity: "))
# print("Total units:", qty)

# 28. Read a price as float
# price = float(input("Price ₹: "))
# print(f"Recorded ₹{price:,.2f}")

# 29. Mini GST calculator from user input
# bill = float(input("Bill amount: "))
# print(f"GST 18% = ₹{bill * 0.18:,.2f}")

# 30. USD to INR converter
# usd = float(input("USD: "))
# print(f"INR = ₹{usd * 83.50:,.2f}")

# 31. Read two numbers and add
# a = float(input("a: ")); b = float(input("b: "))
# print("Sum:", a + b)

# 32. Read 3 marks and compute average
# m1, m2, m3 = [int(input(f"Mark {i+1}: ")) for i in range(3)]
# print("Average:", (m1 + m2 + m3) / 3)

# 33. EMI principal × rate × time
# p = float(input("Principal: ")); r = float(input("Rate %: ")); t = int(input("Years: "))
# print("Simple Interest =", p * r * t / 100)

# 34. Boolean from yes/no input
# answer = input("GST registered? (y/n) ").lower()
# print("Registered:", answer == "y")

# 35. Wrap input + arithmetic in one line
# print("Total:", float(input("Price: ")) * int(input("Qty: ")))


# ─────────────────────────────────────────────────────────────────────
#  36-45  CONDITIONALS
# ─────────────────────────────────────────────────────────────────────

# 36. Compare two numbers
revenue, target = 75000, 50000
print("Target met:", revenue >= target)

# 37. Logical AND / OR / NOT
salary, score = 32000, 720
print("Loan eligible:", salary > 25000 and score >= 700)

# 38. if / else
age = 30
print("Adult" if age >= 18 else "Minor")

# 39. if / elif / else for grades
pct = 72
if pct >= 90:   grade = "O"
elif pct >= 75: grade = "A+"
elif pct >= 60: grade = "A"
else:           grade = "B"
print("Grade:", grade)

# 40. Ternary (one-line if/else)
stock = 8
status = "LOW" if stock < 10 else "OK"
print(status)

# 41. Truthy / falsy values
print(bool(0), bool(""), bool([]), bool("x"))

# 42. is None check
email = None
print("Missing email" if email is None else email)

# 43. Min / max of two
print(min(120, 90), max(120, 90))

# 44. Absolute value
diff = 5000 - 7500
print("Loss:", abs(diff))

# 45. Chained comparison
mark = 67
print("Pass" if 40 <= mark < 80 else "Other")


# ─────────────────────────────────────────────────────────────────────
#  46-55  LISTS
# ─────────────────────────────────────────────────────────────────────

# 46. Create a list
prices = [499, 1299, 2499, 799, 3999]

# 47. Index access (positive and negative)
print(prices[0], prices[-1])

# 48. Slice a list
print(prices[1:4])

# 49. Append a new value
prices.append(599)
print(prices)

# 50. Remove a value
prices.remove(799)
print(prices)

# 51. Sort ascending and descending
prices.sort()
print(prices)
prices.sort(reverse=True)
print(prices)

# 52. Reverse in place
nums = [1, 2, 3]
nums.reverse()
print(nums)

# 53. Built-in summaries
print(sum(prices), min(prices), max(prices), len(prices))

# 54. Average of a list
print(sum(prices) / len(prices))

# 55. Membership test
print(2499 in prices)


# ─────────────────────────────────────────────────────────────────────
#  56-65  LOOPS
# ─────────────────────────────────────────────────────────────────────

# 56. for over a list
for p in [499, 1299, 2499]:
    print(f"₹{p}")

# 57. for with enumerate
for i, m in enumerate(["Apr", "May", "Jun"], 1):
    print(i, m)

# 58. for over range
for n in range(1, 6):
    print("Day", n)

# 59. for with a step
for n in range(0, 21, 5):
    print(n)

# 60. while loop
balance = 10000
while balance > 0:
    balance -= 2500
    print("Remaining:", balance)

# 61. Break out of a loop
for n in range(1, 100):
    if n > 5:
        break
    print(n)

# 62. continue (skip iteration)
for n in range(1, 6):
    if n == 3:
        continue
    print(n)

# 63. Nested loops — multiplication grid
for q in [10, 50, 100]:
    for d in [0, 5, 10]:
        print(q, d, q * (1 - d / 100))

# 64. Sum with a for loop
total = 0
for s in [3450, 1200, 5400, 2780, 950]:
    total += s
print("Total:", total)

# 65. Count items meeting a condition
above = sum(1 for s in [3450, 1200, 5400, 2780, 950] if s > 2000)
print("Sales above ₹2,000:", above)


# ─────────────────────────────────────────────────────────────────────
#  66-75  COMPREHENSIONS, SORTING, FILTERING
# ─────────────────────────────────────────────────────────────────────

# 66. List comprehension — squares
print([n * n for n in range(1, 6)])

# 67. Add GST to every price
prices = [499, 1299, 2499]
print([round(p * 1.18, 2) for p in prices])

# 68. Conditional comprehension
print([p for p in [499, 1299, 2499, 99] if p > 500])

# 69. Build a list of strings
print([f"₹{p:,}" for p in prices])

# 70. Sum via comprehension
print(sum(p for p in prices))

# 71. sorted() with a key (case-insensitive)
names = ["priya", "ARUN", "kavitha"]
print(sorted(names, key=str.lower))

# 72. sorted() of dicts by a field
sales = [{"prod": "Saree", "amt": 2499}, {"prod": "Kurti", "amt": 1299}]
print(sorted(sales, key=lambda r: r["amt"], reverse=True))

# 73. filter() with a lambda
print(list(filter(lambda p: p > 1000, prices)))

# 74. map() with a lambda
print(list(map(lambda p: round(p * 1.18, 2), prices)))

# 75. Combine two lists with zip()
months = ["Jan", "Feb", "Mar"]
revenue = [120000, 150000, 175000]
print(list(zip(months, revenue)))


# ─────────────────────────────────────────────────────────────────────
#  76-85  DICTIONARIES, TUPLES, SETS
# ─────────────────────────────────────────────────────────────────────

# 76. Create a dictionary (customer record)
customer = {"name": "Priya", "balance": 45000, "city": "Chennai"}

# 77. Access by key
print(customer["name"])

# 78. Update / add a key
customer["balance"] = 47500
customer["email"] = "priya@example.com"
print(customer)

# 79. Safe get with default
print(customer.get("phone", "N/A"))

# 80. Loop over keys, values, items
for key, val in customer.items():
    print(key, "=", val)

# 81. Dict comprehension — square map
print({n: n * n for n in range(1, 6)})

# 82. Count word frequency with a dict
words = "saree kurti saree bedsheet kurti saree".split()
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
print(freq)

# 83. Tuple — fixed pair (immutable)
point = ("Chennai", 600044)
print(point[0], point[1])

# 84. Tuple unpacking
city, pin = ("Chennai", 600044)
print(city, pin)

# 85. Sets and union/intersection
a = {"saree", "kurti", "watch"}
b = {"watch", "bedsheet"}
print(a | b, a & b)              # union, intersection


# ─────────────────────────────────────────────────────────────────────
#  86-95  FUNCTIONS
# ─────────────────────────────────────────────────────────────────────

# 86. Define and call a function
def greet(name):
    print(f"Welcome, {name}!")
greet("Priya")

# 87. Return a value
def add_gst(price, rate=0.18):
    return round(price * (1 + rate), 2)
print(add_gst(2499))

# 88. Function with default parameter
def discount(price, pct=10):
    return price - price * pct / 100
print(discount(2499), discount(2499, 25))

# 89. Multiple return values
def stats(nums):
    return min(nums), max(nums), sum(nums) / len(nums)
print(stats([3450, 1200, 5400]))

# 90. *args (any number of arguments)
def total(*amounts):
    return sum(amounts)
print(total(100, 200, 300, 400))

# 91. **kwargs (keyword arguments)
def invoice(**fields):
    for k, v in fields.items(): print(k, ":", v)
invoice(no="INV-001", amount=4500, gst=810)

# 92. Lambda (anonymous function)
square = lambda x: x * x
print(square(7))

# 93. Recursion — factorial
def fact(n):
    return 1 if n <= 1 else n * fact(n - 1)
print(fact(5))

# 94. Nested functions / closures
def make_taxer(rate):
    def add_tax(p): return p * (1 + rate)
    return add_tax
gst = make_taxer(0.18)
print(round(gst(2499), 2))

# 95. Docstring on a function
def margin(rev, cost):
    """Return profit margin in %."""
    return (rev - cost) / rev * 100
print(round(margin(28_50_000, 17_10_000), 2))


# ─────────────────────────────────────────────────────────────────────
#  96-100  EXCEPTIONS, FILES, MODULES
# ─────────────────────────────────────────────────────────────────────

# 96. try / except for safe input parsing
try:
    n = int("ABC")               # this fails on purpose
except ValueError:
    print("Not a valid number")

# 97. try / except / finally
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Cleanup done")

# 98. Write a small text file
with open("hello.txt", "w") as f:
    f.write("SDNB Workshop notes\nLine 2\n")

# 99. Read it back, line by line
with open("hello.txt") as f:
    for line in f:
        print(line.strip())

# 100. Use built-in modules
import math, datetime, random
print(math.sqrt(16), datetime.date.today(), random.randint(1, 100))


print("\n[OK] 100 examples — practice complete!")
