import pymongo
import pandas as pd

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["CALGARY"]  # Replace with your actual database name
collection = db["Statistics"]  # Replace with your collection name

# Load data from MongoDB
raw_data = list(collection.find())

# Check if any data was retrieved
if len(raw_data) == 0:
    print("No data found in the collection.")
else:
    # Flatten nested structure
    data = pd.json_normalize(raw_data)

    # Print column names to understand the structure
    print("Columns in DataFrame:", data.columns.tolist())

    # Define the target column based on the column structure
    target_column = 'Economics.Income_Statistics_2020.Median_Total_Income_Individuals'  # Adjust based on the actual column name

    # Check if the target column exists in the DataFrame
    if target_column in data.columns:
        X = data.drop(columns=[target_column])  # Features
        y = data[target_column]  # Target
        print("Column found, proceeding with train-test split.")
    else:
        print(f"Column '{target_column}' not found in DataFrame.")
        print("Available columns are:", data.columns.tolist())
