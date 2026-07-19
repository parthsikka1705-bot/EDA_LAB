import pandas as pd
import numpy as np

# Read CSV
df = pd.read_csv("1000 Sales Records.csv")

print("First 5 Rows")
print(df.head())

# Split data
first_half = df.iloc[:500]
second_half = df.iloc[500:]

# Vertical concat
vertical_concat = pd.concat([first_half, second_half], ignore_index=True)

print("\nVertical Concatenation")
print(vertical_concat.head())

# Horizontal concat
horizontal_concat = pd.concat(
    [
        first_half.reset_index(drop=True),
        second_half.reset_index(drop=True)
    ],
    axis=1
)

print("\nHorizontal Concatenation")
print(horizontal_concat.head())

# Merge data
df1 = df[['Order ID', 'Country', 'Region']]
df2 = df[['Order ID', 'Item Type', 'Total Profit']]

inner_join = pd.merge(df1, df2, on="Order ID", how="inner")
left_join = pd.merge(df1, df2, on="Order ID", how="left")
right_join = pd.merge(df1, df2, on="Order ID", how="right")
outer_join = pd.merge(df1, df2, on="Order ID", how="outer")

print("\nInner Join")
print(inner_join.head())

print("\nLeft Join")
print(left_join.head())

print("\nRight Join")
print(right_join.head())

print("\nOuter Join")
print(outer_join.head())

# Add column
df["Profit Per Unit"] = df["Unit Price"] - df["Unit Cost"]

print("\nProfit Per Unit")
print(df[["Unit Price", "Unit Cost", "Profit Per Unit"]].head())

# Summary
print("\nDescriptive Statistics")
print(df.describe())

# Count values
print("\nRegion Counts")
print(df["Region"].value_counts())

print("\nItem Type Counts")
print(df["Item Type"].value_counts())

print("\nSales Channel Counts")
print(df["Sales Channel"].value_counts())

# Pivot table
pivot = df.pivot_table(
    values="Total Profit",
    index="Region",
    columns="Sales Channel",
    aggfunc="sum"
)

print("\nPivot Table")
print(pivot)

# Stack
stacked = pivot.stack()

print("\nStacked Data")
print(stacked)

# Unstack
unstacked = stacked.unstack()

print("\nUnstacked Data")
print(unstacked)

# Series concat
series1 = df["Country"].head(5)
series2 = df["Item Type"].head(5)

combined = pd.concat(
    [series1, series2],
    keys=["Country", "ItemType"]
)

print("\nHierarchical Series")
print(combined)

print("\nUnstacked Series")
print(combined.unstack())

# Save file
df.to_csv("1000_Sales_Records_Updated.csv", index=False)

print("\nDone! File saved.")