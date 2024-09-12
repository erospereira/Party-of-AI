import pymongo
import pandas as pd

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["CALGARY"]
collection = db["Statistics"]

# Retrieve all documents
raw_data = list(collection.find({}))
data = pd.json_normalize(raw_data)

print(f"Number of records retrieved: {len(data)}")
print(data.head())  # Preview the first few records
