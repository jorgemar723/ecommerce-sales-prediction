import pandas as pd
import xgboost as xgb
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load processed dataset
data_path = "../data/processed_ecommerce_data.csv"
df = pd.read_csv(data_path)

# Define feature columns
FEATURES = [
    "Revenue", "Discount_Applied", "Clicks", "Impressions",
    "Conversion_Rate", "Ad_Spend", "Rolling_Mean_7"
]

X = df[FEATURES]
y = df["Units_Sold"]

# Split into train/test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = xgb.XGBRegressor(objective="reg:squarederror", n_estimators=100)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"📊 Model Performance:\nMSE: {mse:.4f}\nR²: {r2:.4f}")

# Save model
model_path = "../models/xgboost_ecommerce_model.pkl"
with open(model_path, "wb") as file:
    pickle.dump(model, file)

print(f"✅ Model saved to {model_path}")
