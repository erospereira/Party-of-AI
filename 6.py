import pymongo
import pandas as pd

# Step 1: Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")  # Replace with your actual MongoDB URI if different

# Step 2: Access the specific database
db = client["CALGARY"]  # Replace with your database name

# Step 3: Specify the collection
collection = db["Statistics"]  # Replace with your collection name

# Step 4: Retrieve data from the collection
raw_data = list(collection.find({}))  # Query all documents in the collection

# Step 5: Normalize and load data into a DataFrame
data = pd.json_normalize(raw_data)

# Display the DataFrame
print(f"Number of records retrieved: {len(data)}")
print(data.head())  # Preview the first few records


additional_documents = [
    {
        "Population_and_Dwellings": {
            "Total_Population": 1300000,
            "Private_Dwellings": 530000,
            "Occupied_Dwellings": 500000,
            "Population_Change_Percentage_2016_2021": 5.0
        },
        "Economics": {
            "Median_Total_Income_Individuals": 45000,
            "Labour_Force_Status": {
                "Employed": 680000,
                "Unemployed": 40000,
            }
        }
        # Add other fields as necessary...
    },
    # Add more documents here...
]

collection.insert_many(additional_documents)
