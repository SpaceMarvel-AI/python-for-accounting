"""Build Case Study 2 — Bharath Mobile Customer Churn Analysis."""

import nbformat as nbf
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "case_studies"

nb = nbf.v4.new_notebook()
nb["metadata"] = {"kernelspec": {"display_name": "Python 3",
                                 "language": "python", "name": "python3"},
                  "language_info": {"name": "python", "version": "3.11"}}
cells = []

def md(s):   cells.append(nbf.v4.new_markdown_cell(s.strip("\n")))
def code(s): cells.append(nbf.v4.new_code_cell(s.strip("\n")))


# ── COVER ────────────────────────────────────────────────────────────────
md("""
# 📞 Case Study 2 — Bharath Mobile: Reducing Customer Churn

**SDNB Vaishnav College for Women — Business Analytics Capstone**

---

## 🏢 Background

You have joined **Bharath Mobile**, a fast-growing Indian telecom operator, as their first **Customer Analytics Intern**.

The Head of Retention, Ms. Latha Krishnan, has a pressing problem:

> *"We're losing customers faster than we can acquire them. I have a suspicion who's at risk, but I need data to back it up. Build me a profile of who churns — and tell me which 100 customers we should call this month before we lose them."*

You have a snapshot of **500 active customers** with their tenure, plan, billing, usage, and a `Churned` flag (Yes / No) showing whether they cancelled service.

## 🎯 Your tasks

1. Compute the overall churn rate
2. Compare churners vs non-churners across every variable
3. Identify the top **3 churn drivers**
4. Build a simple **risk score** from the drivers
5. Produce the **at-risk customer list** for the call team
6. Recommend two **retention interventions**
""")

code('''import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

DATA = "data/" if os.path.isdir("data") else "case_studies/data/"
df = pd.read_csv(DATA + "telecom_customers.csv")
print(f"✅ Loaded {len(df)} customers × {df.shape[1]} columns")
df.head()
''')

code('''# Data check
print(df.dtypes)
print("\\nMissing values:", df.isnull().sum().sum())
print("\\nPlan mix:")
print(df["Plan"].value_counts())
''')


# ── Q1 — Overall churn rate ─────────────────────────────────────────────
md("""
## 🔹 Question 1 — What is the overall churn rate?

The "headline number" Latha needs in the first slide of every meeting.
""")

code('''churn_rate = (df["Churned"] == "Yes").mean() * 100
n_churn   = (df["Churned"] == "Yes").sum()
n_total   = len(df)

print(f"Total customers : {n_total}")
print(f"Churned         : {n_churn}")
print(f"Retained        : {n_total - n_churn}")
print(f"Churn rate      : {churn_rate:.1f}%")
''')

code('''# Visualise the headline
fig, ax = plt.subplots(figsize=(6, 6))
counts = df["Churned"].value_counts()
ax.pie(counts, labels=counts.index, autopct="%1.1f%%",
       colors=["#2EC4B6", "#E71D36"], startangle=90,
       wedgeprops=dict(edgecolor="white", linewidth=2))
ax.set_title("Bharath Mobile — Customer Status Snapshot",
             fontsize=13, fontweight="bold")
plt.show()
''')

md("""
**📝 Finding:** Roughly **22%** of the customer base has churned. For a benchmark, healthy Indian telecom monthly churn sits around 1.5–2%; the snapshot here reflects accumulated churn — still meaningful and worth attacking.
""")


# ── Q2 — Compare churners vs non-churners ──────────────────────────────
md("""
## 🔹 Question 2 — How are churners *different* from loyal customers?

For every numeric variable, compare the average for churners vs retained customers.
""")

code('''numeric_cols = ["Tenure_months", "MonthlyCharge", "TotalSpend",
                "DataUsage_GB", "ServiceCalls"]
profile = df.groupby("Churned")[numeric_cols].mean().round(2).T
profile["Difference"]    = (profile["Yes"] - profile["No"]).round(2)
profile["Diff_%"]        = (profile["Difference"] / profile["No"] * 100).round(1)
print(profile)
''')

code('''# Visualise the gap on each variable
fig, axes = plt.subplots(1, 5, figsize=(18, 4))
for i, col in enumerate(numeric_cols):
    means = df.groupby("Churned")[col].mean()
    colors = ["#2EC4B6", "#E71D36"]
    axes[i].bar(means.index, means.values, color=colors, edgecolor="black")
    axes[i].set_title(col, fontsize=10)
    for j, v in enumerate(means.values):
        axes[i].text(j, v, f"{v:.1f}", ha="center", va="bottom",
                     fontsize=9, fontweight="bold")
fig.suptitle("Average value: Retained vs Churned customers",
             fontsize=13, fontweight="bold", y=1.02)
plt.tight_layout()
plt.show()
''')

md("""
**📝 Finding:** The most striking gaps:
- **Tenure** is much lower among churners — they leave before they're locked in
- **Service calls** are higher — every extra support call is a warning sign
- **Data usage** is lower — light users get less value, easier to leave

`MonthlyCharge` and `TotalSpend` are not strong differentiators on their own.
""")


# ── Q3 — Categorical drivers (Plan, AutoPay) ───────────────────────────
md("""
## 🔹 Question 3 — Which plan & payment behaviour predicts churn?
""")

code('''def churn_rate_by(group):
    return (df.groupby(group)["Churned"].apply(lambda s: (s == "Yes").mean() * 100)
              .round(1)
              .sort_values(ascending=False))

plan_churn    = churn_rate_by("Plan")
autopay_churn = churn_rate_by("AutoPay")

print("Churn rate by Plan:")
print(plan_churn.astype(str) + " %")
print("\\nChurn rate by AutoPay:")
print(autopay_churn.astype(str) + " %")
''')

code('''fig, axes = plt.subplots(1, 2, figsize=(13, 4.5))
axes[0].bar(plan_churn.index, plan_churn.values,
            color=["#E71D36" if v > 25 else "#FFB703" if v > 20 else "#2EC4B6"
                   for v in plan_churn.values],
            edgecolor="black")
axes[0].axhline(22, color="grey", linestyle="--",
                label="Overall 22%")
axes[0].set_title("Churn rate by Plan")
axes[0].set_ylabel("Churn rate (%)")
axes[0].legend()
for i, v in enumerate(plan_churn.values):
    axes[0].text(i, v, f" {v}%", ha="center", va="bottom", fontsize=9)

axes[1].bar(autopay_churn.index, autopay_churn.values,
            color=["#E71D36", "#2EC4B6"], edgecolor="black")
axes[1].set_title("Churn rate by AutoPay enrolment")
axes[1].set_ylabel("Churn rate (%)")
for i, v in enumerate(autopay_churn.values):
    axes[1].text(i, v, f" {v}%", ha="center", va="bottom", fontsize=9)

plt.tight_layout()
plt.show()
''')

md("""
**📝 Finding:** **Customers without AutoPay churn far more often** than those with AutoPay enabled. **Basic-plan** users also churn the most — they have the least to lose by switching.
""")


# ── Q4 — Risk score & flag ─────────────────────────────────────────────
md("""
## 🔹 Question 4 — Build a simple risk score

Combine the strongest signals into a single 0–5 score where each ✅ = +1 risk point:

| Risk factor | Threshold |
|-------------|-----------|
| Short tenure | < 6 months |
| Many service calls | ≥ 3 |
| Low data usage | < 5 GB |
| No AutoPay | `No` |
| Basic plan | `Basic` |
""")

code('''def risk_score(row):
    score = 0
    if row["Tenure_months"] < 6:    score += 1
    if row["ServiceCalls"] >= 3:    score += 1
    if row["DataUsage_GB"] < 5:     score += 1
    if row["AutoPay"] == "No":      score += 1
    if row["Plan"] == "Basic":      score += 1
    return score

df["RiskScore"] = df.apply(risk_score, axis=1)

risk_summary = (df.groupby("RiskScore")
                  .agg(customers=("CustomerID","count"),
                       churn_rate=("Churned",
                                   lambda s: round((s == "Yes").mean() * 100, 1)))
                  .reset_index())
print(risk_summary)
''')

code('''fig, ax = plt.subplots(figsize=(9, 5))
colors = ["#2EC4B6", "#FEE440", "#FFB703", "#FB5607", "#E71D36", "#9B0000"]
bars = ax.bar(risk_summary["RiskScore"], risk_summary["churn_rate"],
              color=[colors[s] for s in risk_summary["RiskScore"]],
              edgecolor="black")
ax.set_title("Churn rate climbs steeply with the Risk Score",
             fontsize=13, fontweight="bold")
ax.set_xlabel("Risk score (0 = safe, 5 = highest risk)")
ax.set_ylabel("Churn rate (%)")
for b, n, r in zip(bars, risk_summary["customers"],
                   risk_summary["churn_rate"]):
    ax.text(b.get_x() + b.get_width() / 2, r + 0.6,
            f"{r}%\\n(n={n})", ha="center", fontsize=9)
plt.tight_layout()
plt.show()
''')

md("""
**📝 Finding:** Customers scoring ≥3 churn at multiples of the average rate. Score thresholds become a clear tier system: **0–1 = safe, 2 = monitor, 3+ = call this week.**
""")


# ── Q5 — At-risk customer list ─────────────────────────────────────────
md("""
## 🔹 Question 5 — Top 100 at-risk active customers (the call list)

Of customers still active, prioritise by risk score and then by lifetime spend (we don't want to lose the high-value ones first).
""")

code('''active = df[df["Churned"] == "No"].copy()
call_list = (active.sort_values(["RiskScore", "TotalSpend"],
                                 ascending=[False, False])
                   .head(100)
                   .reset_index(drop=True))

print(f"Total active customers      : {len(active)}")
print(f"Active customers with risk≥3: {(active['RiskScore'] >= 3).sum()}")
print(f"\\nFirst 10 of the call list:")
print(call_list.head(10)[["CustomerID","Tenure_months","Plan","TotalSpend",
                          "ServiceCalls","AutoPay","RiskScore"]])

# Save it for the call team
call_list.to_csv("case2_call_list.csv", index=False)
print("\\n✅ Full 100-customer list saved as case2_call_list.csv")
''')


# ── Recommendations ────────────────────────────────────────────────────
md("""
## 📋 Recommendations to Ms. Latha Krishnan

### 1️⃣ This week — call the 100 highest-risk customers
**Finding:** Active customers with RiskScore ≥3 churn at significantly higher rates than the base.
**Action:** Hand the saved `case2_call_list.csv` to the retention team. Offer each customer:
- A free month of data top-up (low cost, high perceived value), and
- A nudge to enrol in AutoPay with a 5% bill discount.

**Expected impact:** Even a 25% save rate on these 100 customers preserves ~25 customers at an average lifetime spend that pays for the entire campaign many times over.

### 2️⃣ Strategic — make AutoPay the default
**Finding:** Non-AutoPay customers churn at roughly 1.5–2× the AutoPay rate.
**Action:** Make AutoPay opt-out instead of opt-in for new customers, and run a one-time amnesty window for existing customers (5% bill discount for the first 3 months after enrolling).
**Expected impact:** Could shave 3–5 points off churn rate within two billing cycles.

### Bonus — fix the support experience
The data shows churners average noticeably more service calls than retained customers. Investigate the **top 5 reason codes** for support calls — fixing those will reduce churn upstream of the retention call.

---

## ✏️ Practice extensions

- Add a **probabilistic** churn model with `sklearn.linear_model.LogisticRegression`
- Test the score on a **hold-out sample** by splitting the dataset 80/20
- Compute **lifetime value** for each segment (`MonthlyCharge × expected remaining tenure`)
- Cluster customers with `sklearn.cluster.KMeans` and compare against the risk tiers
""")


nb["cells"] = cells
out_path = OUT / "Case2_Bharath_Mobile_Customer_Churn.ipynb"
with out_path.open("w", encoding="utf-8") as f:
    nbf.write(nb, f)
print("✅ Built", out_path)
