import pymongo
import pandas as pd
from sklearn.model_selection import train_test_split

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

    # Print the column names to understand the structure
    print("Columns in DataFrame:", data.columns)

    # Look for the specific field
    target_column = 'Economics.Median_Total_Income_Individuals'

    if target_column in data.columns:
        X = data.drop(columns=[target_column])  # Features
        y = data[target_column]  # Target

        # Split the data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        print("Data split successfully.")
    else:
        print(f"Column '{target_column}' not found in DataFrame.")
        print("Available columns are:", data.columns)
