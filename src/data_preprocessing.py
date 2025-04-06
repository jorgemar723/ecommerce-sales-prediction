import pandas as pd

# Load dataset
data_path = "../data/ecommerce_data.csv"  # Make sure this filename matches your actual CSV
df = pd.read_csv(data_path)

# ✅ Add Rolling_Mean_7 based on Units_Sold
df["Rolling_Mean_7"] = df["Units_Sold"].rolling(window=7, min_periods=1).mean()

# ✅ Select only the necessary 7 features + target
selected_features = [
    "Revenue", "Discount_Applied", "Clicks", "Impressions",
    "Conversion_Rate", "Ad_Spend", "Rolling_Mean_7"
]

df = df[selected_features + ["Units_Sold"]]  # Include target variable

# ✅ Save the processed dataset
df.to_csv("../data/processed_ecommerce_data.csv", index=False)

print("✅ Data preprocessing complete. Saved as processed_ecommerce_data.csv")
