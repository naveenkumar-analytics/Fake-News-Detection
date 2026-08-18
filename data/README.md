# 📂 Data Folder

This folder contains the dataset used for the Fake News Detection project.

## Dataset Information

| File | Description | Records |
|------|-------------|---------|
| `Fake.csv` | Fake news articles | ~23,500 |
| `True.csv` | Real news articles | ~21,398 |

## Dataset Columns

- **title**: Headline of the news article
- **text**: Full content of the article
- **subject**: Category of the news
- **date**: Publication date

## Source

The dataset is from [Kaggle Fake News Dataset](https://www.kaggle.com/datasets)

## Usage

   python
import pandas as pd

# Load fake news
fake = pd.read_csv("data/Fake.csv")

# Load real news
true = pd.read_csv("data/True.csv")  
