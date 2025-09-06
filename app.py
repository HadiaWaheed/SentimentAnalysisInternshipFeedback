from flask import Flask, render_template, request, redirect, url_for, flash
import os, re, csv, datetime as dt, json
import joblib
import numpy as np
from sklearn.exceptions import NotFittedError

app = Flask(__name__)
app.secret_key = "internship-feedback-analysis-secret-key"

# --- Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(BASE_DIR, "models")
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

# --- Model paths
PACKAGE_PATH = os.path.join(MODELS_DIR, "sentiment_model_package.pkl")

# --- Load trained model package
try:
    model_package = joblib.load(PACKAGE_PATH)
    model = model_package['model']
    vectorizer = model_package['vectorizer']
    label_encoder = model_package['encoder']
    print("✅ Model package loaded successfully!")
except FileNotFoundError:
    try:
        MODEL_PATH = os.path.join(MODELS_DIR, "sentiment_model.pkl")
        VECT_PATH = os.path.join(MODELS_DIR, "tfidf_vectorizer.pkl")
        LABEL_PATH = os.path.join(MODELS_DIR, "label_encoder.pkl")
        
        model = joblib.load(MODEL_PATH)
        vectorizer = joblib.load(VECT_PATH)
        label_encoder = joblib.load(LABEL_PATH)
        print("✅ Individual model components loaded successfully!")
    except FileNotFoundError:
        print("❌ Model files not found. Please train and save the model first.")
        model = None
        vectorizer = None
        label_encoder = None

# --- Text cleaning
def clean_text(text: str):
    text = str(text).lower()
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# --- Storage CSV
CSV_PATH = os.path.join(DATA_DIR, "feedback_log.csv")
if not os.path.exists(CSV_PATH):
    with open(CSV_PATH, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "timestamp", "intern_name", "intern_email", "feedback", "review",
            "predicted_sentiment", "confidence"
        ])

# --- Routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if model is None or vectorizer is None or label_encoder is None:
        flash("Models not loaded. Please train and save the models first.")
        return redirect(url_for("home"))
    
    feedback = request.form.get("feedback", "").strip()
    review = request.form.get("review", "").strip()
    intern_name = request.form.get("name", "").strip()
    intern_email = request.form.get("email", "").strip()

    if not feedback:
        flash("Please enter your feedback before submitting.")
        return redirect(url_for("home"))

    cleaned = clean_text(feedback)
    try:
        X = vectorizer.transform([cleaned])
    except NotFittedError:
        flash("Vectorizer is not fitted. Please retrain and save your models.")
        return redirect(url_for("home"))
    
    # Prediction
    p = model.predict_proba(X)[0]
    pred_idx = int(np.argmax(p))
    confidence = float(p[pred_idx])
    label = label_encoder.inverse_transform([pred_idx])[0]

    # Save to CSV
    with open(CSV_PATH, "a", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            dt.datetime.now().isoformat(timespec="seconds"),
            intern_name, intern_email, feedback, review, label, f"{confidence:.4f}"
        ])

    # Tips
    tips = []
    if label.lower() == "negative":
        tips = [
            "Provide clearer guidance and structured tasks.",
            "Balance intern workload and set realistic expectations.",
            "Increase frequency of mentor check-ins and feedback.",
        ]
    elif label.lower() == "neutral":
        tips = [
            "Add more challenging, real-world tasks.",
            "Offer deeper training sessions and resources.",
        ]

    return render_template(
        "result.html",
        label=label,
        confidence=f"{confidence*100:.1f}%",
        feedback=feedback,
        review=review,
        tips=tips,
    )

@app.route("/insights")
def insights():
    rows = []
    if os.path.exists(CSV_PATH):
        with open(CSV_PATH, newline='', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)

    counts = {"Positive": 0, "Neutral": 0, "Negative": 0}
    for r in rows:
        s = r.get("predicted_sentiment", "")
        if s in counts:
            counts[s] += 1

    total = sum(counts.values()) or 1
    pct = {k: round(v*100/total, 1) for k, v in counts.items()}

    recent_feedback = rows[-5:] if len(rows) > 5 else rows
    recent_feedback.reverse()

    return render_template(
        "insights.html",
        counts=counts,
        pct=pct,
        recent_feedback=recent_feedback,
        counts_json=json.dumps(counts)   # 👈 send JSON for Chart.js
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
