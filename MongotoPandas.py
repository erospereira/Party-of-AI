import pymongo
import pandas as pd
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["CALGARY"]  # Replace with your actual database name

# Query the collection and load data into DataFrame
collection = db["Statistics"]  # Replace with your collection name
data = pd.DataFrame(list(collection.find()))

# Display the DataFrame
print(data.head())
