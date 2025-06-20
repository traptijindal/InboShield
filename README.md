# 📧 Spam Detection Web App

This project is a **Spam Classification Model** that analyzes SMS text messages and predicts whether a message is **Spam** or **Ham** (not spam). The model gives a clear prediction along with confidence scores and a satisfaction meter for better interpretability.

---

## 🚀 Features

- Predicts whether a message is spam or ham
- Displays prediction confidence as percentages
- Satisfaction meter showing the model’s confidence visually
- User-friendly visual feedback (✔️✅ vs ❌❌)
- Interactive interface built using Streamlit

---

## 📊 Example Outputs

Here are some sample results from the app:

### Example 1 - Spam Message
> **Message**: "Congratulations! You've won a $1000 Walmart gift card..."
- **Prediction**: Confidently Spam ❌❌
- **Spam Confidence**: 87.35%
- **Ham Confidence**: 12.65%
- **Satisfaction Meter**: ● ● ● ◌ ◌

### Example 2 - Ham Message
> **Message**: "Hey, are we still meeting for lunch today?"
- **Prediction**: Confidently Ham ✅✅✅
- **Spam Confidence**: 0.08%
- **Ham Confidence**: 99.92%
- **Satisfaction Meter**: ● ● ● ● ●

---

## 🧠 Model Info

- Built using:
  - `Multinomial Naive Bayes`
  - `Random Forest Classifier`
  - `Support Vector Classifier (SVC)` for comparison
- Preprocessing includes:
  - Text cleaning
  - Tokenization
  - Vectorization using `CountVectorizer` or `TfidfVectorizer`
- Dataset used: [SMS Spam Collection Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)

---

## 🛠 Technologies Used

- Python
- Pandas, NumPy
- Streamlit (for web interface)
- Matplotlib / Seaborn (for plotting, optional)

---

## 🧪 How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/spam-classifier.git
   cd spam-classifier

2. Install the required packages:
   pip install -r requirements.txt

3.Run the Streamlit app:
   streamlit run app.py

## Screenshots


![image](https://github.com/user-attachments/assets/17575967-d205-4dd7-97a1-6532800f0fe3)

### Output
![image](https://github.com/user-attachments/assets/55683ac8-e356-4611-9e3e-df8cd2e28bf6)

