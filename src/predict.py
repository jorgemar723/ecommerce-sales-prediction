import pandas as pd
import joblib
import xgboost as xgb
import sys

# Load the trained model
model_path = "../models/xgboost_ecommerce_model.pkl"
model = joblib.load(model_path)

# Define the expected feature columns
feature_columns = [
    "Discount_Applied", "Revenue", "Clicks", "Impressions",
    "Conversion_Rate", "Category", "Region", "Ad_CTR", "Ad_CPC",
    "Ad_Spend", "Day", "Month", "Year", "Rolling_Mean_7",
    "Rolling_Mean_14", "Lag_1", "Lag_7",
    "Price_Discount_Interaction", "Marketing_Impact"
]

# Function to preprocess and predict sales
def predict_sales(df):
    """Preprocess input DataFrame and make predictions."""
    # Ensure categorical features are encoded correctly
    df["Category"] = df["Category"].astype("category").cat.codes
    df["Region"] = df["Region"].astype("category").cat.codes

    # Make predictions
    predictions = model.predict(df)
    
    return predictions

# If running from the command line
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python predict.py <input_csv_file>")
        sys.exit(1)

    # Read input CSV
    input_file = sys.argv[1]
    df_input = pd.read_csv(input_file)

    # Ensure it has the correct columns
    missing_cols = set(feature_columns) - set(df_input.columns)
    if missing_cols:
        print(f"Error: Missing columns in input CSV: {missing_cols}")
        sys.exit(1)

    # Make predictions
    df_input["Predicted_Units_Sold"] = predict_sales(df_input)

    # Save predictions to a new CSV
    output_file = "predictions.csv"
    df_input.to_csv(output_file, index=False)

    print(f"Predictions saved to {output_file}")
