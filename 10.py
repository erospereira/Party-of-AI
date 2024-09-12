import transformers
import vaderSentiment
import sklearn
import pandas as pd
import numpy as np

print("All libraries imported successfully!")

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from transformers import pipeline
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score

# Load your dataset
data = pd.read_csv('calgary_news_data.csv')  # Replace with your dataset path
texts = data['text'].values
labels = data['label'].values  # If you have labeled data

# Preprocess your data
vectorizer = CountVectorizer(stop_words='english')
X = vectorizer.fit_transform(texts)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

# VADER Sentiment Analysis
vader_analyzer = SentimentIntensityAnalyzer()
data['vader_sentiment'] = data['text'].apply(lambda x: vader_analyzer.polarity_scores(x)['compound'])

# Naive Bayes Sentiment Analysis
nb_model = MultinomialNB()
nb_model.fit(X_train, y_train)
y_pred_nb = nb_model.predict(X_test)
print(f"Naive Bayes Accuracy: {accuracy_score(y_test, y_pred_nb)}")

# BERT Sentiment Analysis
bert_analyzer = pipeline("sentiment-analysis")
data['bert_sentiment'] = data['text'].apply(lambda x: bert_analyzer(x)[0]['label'])

# Combine the sentiment scores
data['combined_sentiment'] = data[['vader_sentiment', 'bert_sentiment']].mean(axis=1)

# Example analysis: Average sentiment for Calgary housing
housing_data = data[data['text'].str.contains('housing', case=False)]
average_sentiment = housing_data['combined_sentiment'].mean()
print(f"Average sentiment for Calgary housing: {average_sentiment}")

# Visualize the results
import matplotlib.pyplot as plt

data['combined_sentiment'].hist()
plt.title('Distribution of Combined Sentiment Scores')
plt.show()
