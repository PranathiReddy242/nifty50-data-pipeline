import pandas as pd

df = pd.read_csv("../data/raw/nifty50_raw.csv")

# Remove duplicates
df.drop_duplicates(inplace=True)

# Remove nulls
df.dropna(inplace=True)

# Convert date column
df["Date"] = pd.to_datetime(df["Date"])

# Sort values
df.sort_values(by=["Ticker", "Date"], inplace=True)

# Reset index
df.reset_index(drop=True, inplace=True)

# Save cleaned CSV
df.to_csv("../data/processed/nifty50_clean.csv", index=False)

# Save parquet
df.to_parquet("../data/processed/nifty50_clean.parquet")

print("Cleaned parquet saved successfully")
print(df.head())
print(df.info())
print(df.describe())