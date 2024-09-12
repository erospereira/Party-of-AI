import pymongo
import pandas as pd

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["CALGARY"]  # Replace with your actual database name
collection = db["Statistics"]  # Replace with your collection name

# Load data from MongoDB
raw_data = list(collection.find())

if len(raw_data) == 0:
    print("No data found in the collection.")
else:
    # Flatten nested structure
    data = pd.json_normalize(raw_data)

    # Print column names to understand the structure
    print("Columns in DataFrame:", data.columns.tolist())
