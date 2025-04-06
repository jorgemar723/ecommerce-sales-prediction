from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle

# Initialize Flask app
app = Flask(__name__, static_folder="static", template_folder="templates")

# Load trained model
model_path = "../models/xgboost_ecommerce_model.pkl"
with open(model_path, "rb") as model_file:
    model = pickle.load(model_file)

# Define the selected features
FEATURES = [
    "Revenue", "Discount_Applied", "Clicks", "Impressions",
    "Conversion_Rate", "Ad_Spend", "Rolling_Mean_7"
]

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.form  # Get form data from POST request

        # Ensure all required features are present
        if not all(feature in data for feature in FEATURES):
            return jsonify({"error": "Missing required input features"}), 400

        # Convert input data to numpy array
        input_data = np.array([float(data[feature]) for feature in FEATURES]).reshape(1, -1)

        # Make prediction
        predicted_units = model.predict(input_data)[0]

        # Return prediction as a rounded float
        return jsonify({"prediction": round(float(predicted_units), 2)})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Run Flask app
if __name__ == "__main__":
    app.run(debug=True)
