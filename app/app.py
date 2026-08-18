import streamlit as st
import pickle
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
tfidf = pickle.load(open("vectorizer.pkl", "rb"))

ps = PorterStemmer()
stop_words = set(stopwords.words("english"))

def preprocess(text):
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    text = text.lower()
    words = text.split()

    words = [ps.stem(word) for word in words if word not in stop_words]

    return " ".join(words)

st.title("📰 Fake News Detection")
st.write("Enter a news article below.")

news = st.text_area("News Text")

if st.button("Predict"):

    processed = preprocess(news)

    vector = tfidf.transform([processed])

    prediction = model.predict(vector)

    if prediction[0] == 0:
        st.error("🚨 Fake News")
    else:
        st.success("✅ Real News")