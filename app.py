from flask import Flask, request, jsonify, render_template
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from database import data
import pandas as pd

app = Flask(__name__)

df = pd.DataFrame(data)

# Train ML Model
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["symptoms"])
y = df["medicine"]
model = LogisticRegression()
model.fit(X, y)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict_medicine():
    data = request.get_json()
    symptoms = data.get("symptoms", "")
    input_vector = vectorizer.transform([symptoms])
    predicted_medicine = model.predict(input_vector)[0]
    return jsonify({"medicine": predicted_medicine})

if __name__ == "__main__":
    app.run(debug=True)
