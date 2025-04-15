from flask import Flask, request, jsonify, render_template
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
from thefuzz import process
import pandas as pd
from database import data

# Initialize Flask app
app = Flask(__name__)

# Convert to DataFrame
df = pd.DataFrame(data)

# Vectorize symptoms
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["symptoms"])

# KNN model using cosine similarity
knn_model = NearestNeighbors(n_neighbors=3, metric='cosine')
knn_model.fit(X)

# Fuzzy match helper
def fuzzy_match_symptom(input_symptom, choices, threshold=60):
    match, score = process.extractOne(input_symptom, choices)
    return match if score >= threshold else None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict_medicine():
    data = request.get_json()
    symptoms_input = data.get("symptoms", "")

    # Fuzzy match
    matched_symptom = fuzzy_match_symptom(symptoms_input, df["symptoms"].tolist())

    if matched_symptom is None:
        return jsonify({
            "medicine": [],
            "message": "No close match found. Please rephrase your symptoms."
        })

    # Transform matched symptom and get top 3
    input_vector = vectorizer.transform([matched_symptom])
    distances, indices = knn_model.kneighbors(input_vector)

    # Get top 3 suggested medicines
    top_medicines = [df.iloc[i]["medicine"] for i in indices[0]]

    return jsonify({
        "input_symptom": symptoms_input,
        "matched_symptom": matched_symptom,
        "suggested_medicines": top_medicines
    })

if __name__ == "__main__":
    app.run(debug=True)
