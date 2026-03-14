from flask import Flask, request, jsonify
import pandas as pd
import pickle
import os

app = Flask(__name__)

# Always find the trained_model.pkl in the same folder as this file
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "trained_model.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)

@app.route("/predict", methods=["POST"])
def predict():
    data = pd.DataFrame(request.json)
    predictions = model.predict(data)
    return jsonify(predictions.tolist())

if __name__ == "__main__":
    app.run(debug=True)
