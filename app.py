from flask import Flask, render_template, request
import pickle
import numpy as np
import os
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)

model_path = os.path.join("model", "model.pkl")
vectorizer_path = os.path.join("model", "vectorizer.pkl")

# Load model and vectorizer
with open(model_path, "rb") as f:
    voting_clf = pickle.load(f)
with open(vectorizer_path, "rb") as f:
    vectorizer = pickle.load(f)

# Setup NLTK
ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = [i for i in text if i.isalnum()]
    y = [i for i in y if i not in stopwords.words('english') and i not in string.punctuation]
    y = [ps.stem(i) for i in y]
    return " ".join(y)

def get_label_and_meter(spam_confidence, ham_confidence):
    diff = abs(spam_confidence - ham_confidence)
    if spam_confidence > ham_confidence:
        if diff > 60:
            label = "Confidently Spam ❌❌"
        elif diff > 30:
            label = "Possibly Spam ⚠️"
        else:
            label = "Uncertain 🤔"
    else:
        if diff > 60:
            label = "Confidently Ham ✅✅"
        elif diff > 30:
            label = "Likely Ham 🙂"
        else:
            label = "Uncertain 🤔"
    return label

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        msg = request.form['message']
        transformed = transform_text(msg)
        vectorized = vectorizer.transform([transformed]).toarray()
        probs = voting_clf.predict_proba(vectorized)[0]
        spam_conf = probs[1] * 100
        ham_conf = probs[0] * 100
        label = get_label_and_meter(spam_conf, ham_conf)

        # 
        result = {
            "message": msg,
            "prediction": label,
            "spam_conf": round(spam_conf, 2),
            "ham_conf": round(ham_conf, 2)
        }


       

        return render_template("index.html", result=result)

    return render_template("index.html", result=None)

# if __name__ == '__main__':
#     app.run(debug=True)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # take PORT from environment or use 5000 locally
    app.run(host="0.0.0.0", port=port)
