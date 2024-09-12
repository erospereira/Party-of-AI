import pandas as pd
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["CALGARY"]  # Your actual database name
collection = db["Statistics"]  # Your actual collection name

# Query the MongoDB collection and load data into a DataFrame
# Replace 'Field1', 'Field2', etc., with actual field names from your MongoDB documents
query = {}
projection = {
    'Population_and_Dwellings.Total_Population': 2,
    'Population_Change_Percentage_2016_2021': 5.5,
}

cursor = collection.find(query, projection)

# Convert the cursor to a list of dictionaries and then to a DataFrame
data = pd.DataFrame(list(cursor))

# Remove the '_id' column if you don't need it
data = data.drop(columns=['_id'])

# Display the DataFrame
print(data.head())

# Now, you can use 'data' as your DataFrame with actual data from MongoDB
