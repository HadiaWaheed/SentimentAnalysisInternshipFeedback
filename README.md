# 🎯 Sentiment Analysis on Internship Feedback

## 📌 Project Overview

This project focuses on analyzing internship feedback using **Sentiment Analysis**. The goal is to classify feedback into three categories:

* ✅ **Positive**
* ⚠️ **Neutral**
* ❌ **Negative**

The system is designed to help organizations quickly evaluate feedback from interns and improve their training programs.

---

## 🚀 Features

* Upload or enter internship feedback text.
* Predict sentiment using a trained **Machine Learning model**.
* Visualize sentiment distribution with interactive charts.
* User-friendly web interface built with **Flask + HTML/CSS**.
* Handles multiple feedback entries and provides summary insights.

---

## 🛠️ Tech Stack

* **Python** – Main programming language
* **Flask** – Web framework
* **scikit-learn** – Machine Learning (Naive Bayes / Random Forest)
* **Pandas & NumPy** – Data preprocessing
* **Matplotlib / Chart.js** – Visualization
* **HTML, CSS, Bootstrap** – Frontend design

---

## 📂 Project Structure

```
SentimentAnalysisInternshipFeedback/
│── app.py                # Flask backend application
│── models/               # Saved ML models & vectorizer
│── static/               # CSS, JS, Images
│   └── style.css
│── templates/            # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── result.html
│   └── insights.html
│── dataset.csv           # Feedback dataset
│── requirements.txt      # Project dependencies
│── README.md             # Project documentation
```

---

## ⚙️ How It Works

1. User enters feedback text on the website.
2. Text is preprocessed (tokenization, stopword removal, vectorization).
3. ML model predicts the sentiment class.
4. Results + insights (distribution charts) are displayed on the dashboard.
5.  After every prediction, results are saved in:

  * **CSV file:** `data/feedback_results.csv`
  * **Excel file:** `data/feedback_results.xlsx`

* Both files are **automatically updated** whenever new feedback is submitted.

* Columns inside both CSV and Excel:

  * `Intern Name`
  * `Email`
  * `Feedback`
  * `Review`
  * `Predicted Sentiment`
  * `Date & Time`

**Example (Excel/CSV data):**

| Intern Name | Email                                         | Feedback                      | Review         | Predicted Sentiment | Date & Time         |
| ----------- | --------------------------------------------- | ----------------------------- | -------------- | ------------------- | ------------------- |
| Hadia       | [hadia@example.com](mailto:hadia@example.com) | The internship was amazing!   | Great learning | Positive            | 2025-09-06 12:45:23 |
| Anonymous   |                                               | It was okay, nothing special. |                | Neutral             | 2025-09-06 12:46:11 |
| Hacker        | [ali@example.com](mailto:ali@example.com)     | Not helpful at all.           |                | Negative            | 2025-09-06 12:47:02 |

---

## 📊 Example Output

* Input: `"The internship was very helpful and I learned a lot."`
  → Output: ✅ Positive

* Input: `"It was okay, nothing special."`
  → Output: ⚠️ Neutral

* Input: `"The sessions were boring and not useful."`
  → Output: ❌ Negative

---

## 🖥️ Installation & Usage

### 1️⃣ Clone Repository

```bash
git clone https://github.com/HadiaWaheed/SentimentAnalysisInternshipFeedback.git
cd SentimentAnalysisInternshipFeedback
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Flask App

```bash
python app.py
```

### 5️⃣ Open in Browser

Go to 👉 `http://127.0.0.1:5000/`

---

## 📌 Future Improvements

* Add deep learning (LSTM / BERT) for better accuracy.
* Deploy on **Heroku / Render / AWS** for public use.
* Add **multilingual support** for feedback analysis.

---

## 👩‍💻 Author

**Hadia Waheed**

* 🚀 Machine Learning Enthusiast
* 💡 Cybersecurity & AI Explorer
* 🌐 [LinkedIn Profile](https://www.linkedin.com/in/hadia-waheed-1647892aa?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app)


