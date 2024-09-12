import pandas as pd
from sklearn.model_selection import train_test_split
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["CALGARY"]
collection = db["Statistics"]

# Load data from MongoDB
raw_data = list(collection.find())

# Check if any data was retrieved
if len(raw_data) == 0:
    print("No data found in the collection.")
else:
    print(f"Number of records retrieved: {len(raw_data)}")

    # Load data into DataFrame
    data = pd.json_normalize(raw_data)  # Flatten the nested structure

    # Inspect the first few rows to understand the structure
    print(data.head())
    print("Columns in DataFrame:", data.columns)
