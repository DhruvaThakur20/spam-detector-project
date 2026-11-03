from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)  # allows frontend (different port) to call this API

# Load trained model + vectorizer
with open("spam_model.pkl", "rb") as f:
    model = pickle.load(f)
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    message = data.get("message", "")

    if not message.strip():
        return jsonify({"error": "Empty message"}), 400

    vec = vectorizer.transform([message])
    pred = model.predict(vec)[0]
    prob = model.predict_proba(vec)[0][pred] * 100

    result = {
        "label": "Spam" if pred == 1 else "Not Spam",
        "confidence": round(float(prob), 2)
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
