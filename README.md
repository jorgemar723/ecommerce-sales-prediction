# E-Commerce Sales Prediction

This project predicts units sold for e-commerce products using historical, synthetically generated data. It combines machine learning (XGBoost), clean data preprocessing, and a user-friendly Flask web interface. It’s ideal for exploring sales forecasting, UI design, and regression-based modeling.

---

## Project Structure

```
E-Commerce Sales/
├── data/                       # Raw and processed datasets
│   └── processed_ecommerce_data.csv
│
├── models/                     # Trained ML model
│   └── xgboost_ecommerce_model.pkl
│
├── plots/                      # Visualizations for the report
│   ├── actual_vs_predicted.png
│   └── feature_importance.png
│
├── src/                        # Core scripts
│   ├── data_preprocessing.py
│   ├── train_model.py
│   ├── generate_plots.py
│   └── predict.py
│
├── webapp/                     # Flask frontend
│   ├── app.py
│   ├── static/
│   │   ├── style.css
│   │   └── scripts.js
│   └── templates/
│       └── index.html
│
├── ProjectReport.tex           # Final LaTeX report (compiled separately)
└── README.md
```
---

## Features

- Predicts units sold from 7 key features
- Web interface with TXST-themed light/dark mode toggle
- Prediction history log with live UI updates
- Preprocessed and trained with XGBoost
- Clean modular structure for reproducibility

---

## Model & Dataset

- **Model:** XGBoost Regressor
- **Target:** `Units_Sold`
- **Features Used (7 out of original 19):**
  - Revenue
  - Discount_Applied
  - Clicks
  - Impressions
  - Conversion_Rate
  - Ad_Spend
  - Rolling_Mean_7
- **Dataset Source:**  
  [Comprehensive Synthetic E-commerce Dataset](https://www.kaggle.com/datasets/imranalishahh/comprehensive-synthetic-e-commerce-dataset)

---

## Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/jorgemar723/ecommerce-sales-prediction.git
cd ecommerce-sales-prediction


2. Create and activate a conda environment

conda create -n CS4347 python=3.10
conda activate CS4347


3. Install dependencies

pip install -r requirements.txt

Usage

1. Preprocess Data

cd src
python data_preprocessing.py

2. Train the Model

python train_model.py

3. Generate Plots

python generate_plots.py

4. Predict from CLI

python predict.py 5000 10 300 50 0.05 2000 30

Arguments:

Revenue Discount_Applied Clicks Impressions Conversion_Rate Ad_Spend Rolling_Mean_7

5. Launch Web App

cd ../webapp
python app.py

Then open http://127.0.0.1:5000 in your browser.
```

## Assumptions & Notes
Dataset is synthetic and pre-cleaned

The model only supports 7 input features

Features were reduced from 19 → 7 to streamline UI and improve interpretability

All processing and training are done locally using CSV files

## License
Licensed under the MIT License.

## Author
Jorge Martinez-Lopez

Project for CS 4347 - Intro to Machine Learning

Texas State University, Spring 2025
