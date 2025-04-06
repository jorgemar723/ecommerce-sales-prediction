import pandas as pd
import matplotlib.pyplot as plt
import pickle
import xgboost as xgb
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Load processed dataset
df = pd.read_csv("../data/processed_ecommerce_data.csv")

# Define features
features = [
    "Revenue", "Discount_Applied", "Clicks", "Impressions",
    "Conversion_Rate", "Ad_Spend", "Rolling_Mean_7"
]
X = df[features]
y = df["Units_Sold"]

# Load model
with open("../models/xgboost_ecommerce_model.pkl", "rb") as file:
    model = pickle.load(file)

# Make predictions
y_pred = model.predict(X)

# Save metrics
mse = mean_squared_error(y, y_pred)
mae = mean_absolute_error(y, y_pred)
r2 = r2_score(y, y_pred)

print(f"📊 MSE: {mse:.2f}, MAE: {mae:.2f}, R²: {r2:.4f}")

# Feature importance plot
plt.figure(figsize=(8, 6))
xgb.plot_importance(model, importance_type="weight", show_values=False)
plt.title("Feature Importance - XGBoost")
plt.tight_layout()
plt.savefig("../plots/feature_importance.png")

# Actual vs predicted plot
plt.figure(figsize=(8, 6))
plt.scatter(y, y_pred, alpha=0.5, edgecolors='k')
plt.xlabel("Actual Units Sold")
plt.ylabel("Predicted Units Sold")
plt.title("Actual vs Predicted Units Sold")
plt.grid(True)
plt.tight_layout()
plt.savefig("../plots/actual_vs_predicted.png")

# Save sample predictions
sample = df.copy()
sample["Predicted_Units_Sold"] = y_pred
sample[features + ["Units_Sold", "Predicted_Units_Sold"]].sample(5).to_csv("../plots/sample_predictions.csv", index=False)
