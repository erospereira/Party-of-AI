import pandas as pd
from sklearn.model_selection import train_test_split
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["CALGARY"]
collection = db["Statistics"]

# Load data into DataFrame
data = pd.DataFrame(list(collection.find()))

# For demonstration, let's assume we're focusing on predicting 'Median_Total_Income_Individuals'
X = data.drop(columns=['Median_Total_Income_Individuals'])  # Features
y = data['Median_Total_Income_Individuals']  # Target

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
