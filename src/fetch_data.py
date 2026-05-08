import yfinance as yf
import pandas as pd
from config import STOCKS

START_DATE = "2020-01-01"
END_DATE = "2025-01-01"

all_data = []

for stock in STOCKS:
    print(f"Downloading {stock}...")

    df = yf.download(stock, start=START_DATE, end=END_DATE)

    df.reset_index(inplace=True)

    df["Ticker"] = stock

    all_data.append(df)

final_df = pd.concat(all_data)

final_df.to_csv("../data/raw/nifty50_raw.csv", index=False)

print("Raw data saved successfully")