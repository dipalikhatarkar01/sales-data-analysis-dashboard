# Sales Data Analysis Dashboard

An end-to-end sales analysis project using **SQL, Excel and Power BI**: exploring revenue trends, top-performing products, regional performance and the effect of discounts, then presenting the findings in an interactive dashboard.

> **Note:** The dataset in `data/sales_data.csv` is **synthetic sample data** (2,000 orders, Jan 2024 – Dec 2025) created for learning and portfolio purposes. It is not real company data.

## Business Questions
1. What are the overall revenue and average order value?
2. How does revenue change month to month?
3. Which products and categories drive the most revenue?
4. Which regions perform best?
5. Do discounts lead to higher order values?

## Tools Used
- **SQL** – aggregation, grouping, subqueries (`sql/analysis_queries.sql`)
- **Excel** – data cleaning checks and pivot tables
- **Power BI** – interactive dashboard with KPIs, slicers and charts
- **Python (matplotlib)** – preview charts in `images/`

## Dataset
| Column | Description |
|---|---|
| order_id | Unique order number |
| order_date | Date of order |
| region | North / South / East / West |
| product, category | Product sold and its category |
| unit_price, quantity | Price per unit and units sold |
| discount_pct | Discount given (0, 5, 10, 15) |
| revenue | unit_price × quantity × (1 − discount) |

## Project Structure
```
data/sales_data.csv          sample dataset
sql/analysis_queries.sql     7 analysis queries
images/                      charts and dashboard screenshots
make_charts.py               generates preview charts
```

## Key Findings (on the sample data)
- Total revenue is about ₹4.3 crore across 2,000 orders (average order value ≈ ₹21,500).
- **Electronics contributes ~78%** of revenue; Laptops and Smartphones are the top two products.
- West and North are the highest-revenue regions.
- Higher discounts did **not** raise average quantity per order, so deep discounts may not be paying off.

## Preview
![Monthly revenue](images/monthly_revenue.png)
![Top products](images/top_products.png)

<!-- Add your Power BI dashboard screenshot below -->
<!-- ![Dashboard](images/dashboard.png) -->

## How to Run
1. Load `data/sales_data.csv` into a SQL database (a table named `sales`) and run the queries in `sql/analysis_queries.sql`.
2. Open Power BI Desktop → Get Data → Text/CSV → load `sales_data.csv`.
3. Build the dashboard (KPI cards, monthly line chart, top products bar chart, region map or bar, slicers for category and year).

## Author
Dipali Khatarkar · [LinkedIn](https://linkedin.com/in/dipali-khatarkar) · [GitHub](https://github.com/dipalikhatarkar01)
