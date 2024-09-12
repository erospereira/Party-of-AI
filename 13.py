import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from transformers import pipeline

# Load the CSV file into a DataFrame
df = pd.read_csv('calgary_news_dataset.csv')

# Display the first few rows to understand the data
print(df.head())

# Preprocess the 'content' column (remove missing values, convert to lowercase, etc.)
df['content'] = df['content'].fillna('').str.lower()

# Initialize VADER Sentiment Analyzer
vader_analyzer = SentimentIntensityAnalyzer()

# Apply sentiment analysis to each article's content
df['vader_sentiment'] = df['content'].apply(lambda x: vader_analyzer.polarity_scores(x)['compound'])

# Display the first few rows with the sentiment scores
print(df[['title', 'vader_sentiment']].head())

# Initialize the BERT sentiment analysis pipeline
bert_analyzer = pipeline("sentiment-analysis")

# Apply BERT sentiment analysis to each article's content
df['bert_sentiment'] = df['content'].apply(lambda x: bert_analyzer(x)[0]['label'])

# Display the first few rows with both VADER and BERT sentiment scores
print(df[['title', 'vader_sentiment', 'bert_sentiment']].head())
