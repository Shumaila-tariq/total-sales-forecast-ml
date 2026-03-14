# Sales Prediction API 🛒📈

A machine learning project that predicts **Total Sales** from historical 
sales data using a regression model, exposed through a simple Flask REST API.

## Features
- Predicts Total Sales based on Day, Month, Weekday, Total Users & Total Orders
- Trained regression model saved with Pickle
- REST API built with Flask to serve real-time predictions
- Validated on unseen future data using sample CSV input

## Project Structure
| File | Description |
|---|---|
| `app.py` | Flask API for serving predictions |
| `training_notebook.ipynb` | Model training & preprocessing notebook |
| `trained_model.pkl` | Saved trained ML model |
| `sample_input.csv` | Sample input data for testing |
| `accuracy_report.txt` | Model performance summary (MAE) |

## ⚙️ Installation
pip install flask pandas scikit-learn

##  Usage
Run the Flask API:
python app.py

Send a POST request to /predict:
POST http://127.0.0.1:5000/predict
Content-Type: application/json

##  Model Details
- Algorithm: Regression
- Target Variable: Total Sales
- Features: Day, Month, Weekday, Total Users, Total Orders
- Evaluation Metric: Mean Absolute Error (MAE)
