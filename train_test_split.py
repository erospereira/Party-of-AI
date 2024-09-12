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

    # Inspect the DataFrame columns to ensure the correct column name
    print("Columns in DataFrame:", data.columns)

    # Check for the specific column
    target_column = 'Economics.Median_Total_Income_Individuals'
    if target_column in data.columns:
        X = data.drop(columns=[target_column])  # Features
        y = data[target_column]  # Target

        # Split the data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        print("Data split successfully.")
    else:
        print(f"Column '{target_column}' not found in DataFrame.")
