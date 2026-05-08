import yfinance as yf
import pandas as pd
from config import STOCKS

START_DATE = "2020-01-01"
END_DATE = "2025-01-01"

all_data = []

for stock in STOCKS:

    print(f"Downloading {stock}...")

    df = yf.download(
        stock,
        start=START_DATE,
        end=END_DATE,
        auto_adjust=False
    )

    # Flatten columns
    df.columns = df.columns.get_level_values(0)

    # Reset index
    df.reset_index(inplace=True)

    # Add ticker column
    df["Ticker"] = stock

    all_data.append(df)

# Combine all stocks
final_df = pd.concat(all_data, ignore_index=True)

print(final_df.head())
print(final_df.shape)

# Save CSV
final_df.to_csv("../data/raw/nifty50_raw.csv", index=False)

print("Raw data saved successfully")