## Fake-News-Detection
Fake News Detection using NLP &amp; Machine Learning


# 🎯 Fake News Detection using NLP & Machine Learning

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.0+-orange.svg)](https://scikit-learn.org/)
[![NLTK](https://img.shields.io/badge/NLTK-3.6+-green.svg)](https://www.nltk.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **An end-to-end Machine Learning solution to detect fake news with 95.5% accuracy using Natural Language Processing**

---

## 📌 Project Overview

In today's digital age, misinformation spreads faster than ever. This project aims to combat fake news by building a robust machine learning model that can accurately classify news articles as **Fake (0)** or **Real (1)**.

### 🎯 Key Highlights
- ✅ **95.5% Accuracy** on test data
- ✅ **0.99 ROC-AUC Score** - Excellent discrimination power
- ✅ **No Overfitting** - Validated with 5-fold cross-validation
- ✅ **Real-time Prediction** via Streamlit Web App
- ✅ **End-to-End Pipeline** from data preprocessing to deployment

---

## 📊 Dataset Information

| Feature | Details |
|---------|---------|
| **Source** | Kaggle Fake News Dataset |
| **Total Records** | 44,898 articles |
| **Fake News** | 23,500 articles |
| **Real News** | 21,398 articles |
| **Columns** | Title, Text, Subject, Date |

---

## 🧠 Methodology

### Architecture


### 1. Data Preprocessing
- Tokenization & Stopword Removal
- Stemming using Porter Stemmer
- Text Cleaning (removed special characters)

### 2. Feature Extraction
- **TF-IDF Vectorizer**: Converted text to numerical features
- **Max Features**: Top 5,000 important words

### 3. Model Performance

| Model | Accuracy | Precision | Recall | F1-Score |
|-------|----------|-----------|--------|----------|
| **Logistic Regression** | **95.5%** | 0.95 | 0.95 | 0.95 |
| Random Forest | 94.8% | 0.94 | 0.94 | 0.94 |

### 4. Overfitting Check ✅
- **Train Accuracy**: 95.8%
- **Test Accuracy**: 95.5%
- **Difference**: 0.3% ✅ **No Overfitting**
- **Cross-Validation**: 5-Fold CV (Mean: 94.8%)


## 🏗️ Tech Stack
Python 3.8+
├── Pandas (Data Manipulation)
├── NumPy (Numerical Computing)
├── Scikit-learn (Machine Learning)
├── NLTK (Natural Language Processing)
└── Streamlit (Web Application)



## 🚀 Installation & Setup

### Step 1: Clone Repository

git clone https://github.com/naveenkumar-analytics/Fake-News-Detection.git
cd Fake-News-Detection

Step 2: Install Dependencies
pip install -r requirements.txt

Step 3: Download NLTK Data
import nltk
nltk.download('stopwords')

Step 4: Run Jupyter Notebook
jupyter notebook notebooks/fake_news_detection.ipynb

Step 5: Run Streamlit App
cd app
python -m streamlit run app.py



