"""Quick preview charts for the README (the main dashboard is built in Power BI)."""
import pandas as pd, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

df = pd.read_csv("data/sales_data.csv", parse_dates=["order_date"])

monthly = df.groupby(df.order_date.dt.to_period("M"))["revenue"].sum() / 1e6
ax = monthly.plot(figsize=(9, 4), marker="o", color="#1f4e79")
ax.set_title("Monthly Revenue (₹ million)"); ax.set_xlabel(""); ax.grid(alpha=.3)
plt.tight_layout(); plt.savefig("images/monthly_revenue.png", dpi=150); plt.close()

top = df.groupby("product")["revenue"].sum().sort_values().tail(5) / 1e6
ax = top.plot(kind="barh", figsize=(9, 4), color="#1f4e79")
ax.set_title("Top 5 Products by Revenue (₹ million)"); ax.set_ylabel("")
plt.tight_layout(); plt.savefig("images/top_products.png", dpi=150); plt.close()
print("charts saved")
