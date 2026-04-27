# =====================================================================
#  SDNB Python Workshop — IDLE Starter Example
#  A single-file program you can run in Python IDLE.
#  Demonstrates: variables, input(), if/elif/else, for loop, function.
# =====================================================================
#  How to run:
#   1. Open IDLE  ->  File -> Open  ->  pick this file
#   2. Press F5 (or Run -> Run Module)
#   3. Answer the questions in the IDLE shell window
# =====================================================================


def calculate_gst(amount):
    """Return GST rate (%) and GST amount based on Indian slabs."""
    if amount < 1000:
        rate = 5
    elif amount < 5000:
        rate = 12
    elif amount < 10000:
        rate = 18
    else:
        rate = 28
    gst = amount * rate / 100
    return rate, gst


def simple_interest(principal, rate, years):
    return (principal * rate * years) / 100


def compound_interest(principal, rate, years):
    return principal * (1 + rate / 100) ** years - principal


# ---------------------------------------------------------------------
# Banner
# ---------------------------------------------------------------------
print("=" * 50)
print("  SDNB BUSINESS ANALYTICS — IDLE STARTER")
print("  Mini Accounting Toolkit")
print("=" * 50)


# ---------------------------------------------------------------------
# Part 1 — GST Calculator
# ---------------------------------------------------------------------
print("\n[1] GST Calculator")
print("-" * 50)
bill = float(input("Enter bill amount (Rs.): "))
rate, gst = calculate_gst(bill)
total = bill + gst

print(f"  Bill amount  : Rs.{bill:>10,.2f}")
print(f"  GST rate     : {rate}%")
print(f"  GST amount   : Rs.{gst:>10,.2f}")
print(f"  Grand total  : Rs.{total:>10,.2f}")


# ---------------------------------------------------------------------
# Part 2 — Simple Interest vs Compound Interest
# ---------------------------------------------------------------------
print("\n[2] Investment Comparison")
print("-" * 50)
principal = float(input("Principal amount (Rs.): "))
annual    = float(input("Annual rate (%)       : "))
years     = int(input("Years                 : "))

si = simple_interest(principal, annual, years)
ci = compound_interest(principal, annual, years)

print(f"  Simple Interest   : Rs.{si:>10,.2f}")
print(f"  Compound Interest : Rs.{ci:>10,.2f}")
print(f"  Extra with CI     : Rs.{ci - si:>10,.2f}")


# ---------------------------------------------------------------------
# Part 3 — Sales Summary (5 entries via for loop)
# ---------------------------------------------------------------------
print("\n[3] Daily Sales Summary (5 entries)")
print("-" * 50)
sales = []
for i in range(1, 6):
    amt = float(input(f"  Sale #{i} amount (Rs.): "))
    sales.append(amt)

total_sales = sum(sales)
average     = total_sales / len(sales)
highest     = max(sales)
lowest      = min(sales)

print()
print("  ===== END OF DAY SUMMARY =====")
for i, s in enumerate(sales, start=1):
    print(f"   Sale {i} : Rs.{s:>10,.2f}")
print("  -------------------------------")
print(f"   Total   : Rs.{total_sales:>10,.2f}")
print(f"   Average : Rs.{average:>10,.2f}")
print(f"   Highest : Rs.{highest:>10,.2f}")
print(f"   Lowest  : Rs.{lowest:>10,.2f}")
print("  ===============================")

print("\n[OK] Done. Press Enter to exit.")
input()
