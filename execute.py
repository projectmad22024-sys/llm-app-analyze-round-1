# Fixed execute.py
import json
import pandas as pd

def main():
    # Read the data
    df = pd.read_excel("data.xlsx")

    # Compute revenue
    df["revenue"] = df["units"] * df["price"]

    # row_count
    row_count = len(df)

    # regions: count of distinct regions
    regions_count = df["region"].nunique()

    # top_n_products_by_revenue (n=3)
    n = 3
    top_products = (
        df.groupby("product")["revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
        .reset_index()
    )
    top_products_list = [
        {"product": row["product"], "revenue": float(row["revenue"])}
        for _, row in top_products.iterrows()
    ]

    # rolling_7d_revenue_by_region: for each region, last value of 7-day moving average of daily revenue
    df["date"] = pd.to_datetime(df["date"])
    # Ensure 'revenew' typo is fixed in processing; using correct column 'revenue'
    daily_rev = (
        df.groupby(["region", "date"])["revenue"]
        .sum()
        .reset_index()
    )
    # Compute 7-day rolling mean for each region
    rolling_avg = (
        daily_rev
        .groupby("region")
        .apply(lambda x: x.set_index("date")
               .sort_index()
               .rolling(window=7)
               .mean()
               .reset_index())
    ).reset_index(drop=True)
    # For each region, get last rolling average date
    result = {}
    for region, group in rolling_avg.groupby("region"):
        last_date = group["date"].iloc[-1]
        last_value = group["revenue"].iloc[-1]
        result[region] = {
            "last_date": last_date.strftime("%Y-%m-%d"),
            "7_day_avg_revenue": float(last_value)
        }

    # Compile output data
    output = {
        "row_count": row_count,
        "regions_count": regions_count,
        "top_products": top_products_list,
        "rolling_7d_revenue_by_region": result
    }

    # Write to JSON
    with open("result.json", "w") as f:
        json.dump(output, f, indent=2)

if __name__ == "__main__":
    main()
