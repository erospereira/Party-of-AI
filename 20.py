from pymongo import MongoClient
import pandas as pd

# Replace with your MongoDB connection string
client = MongoClient("mongodb://localhost:27017/CALGARY.Statistics")

# Connect to the database
db = client.PAI_Database

# Retrieve the collection and load it into a DataFrame
demographics_collection = db.demographics
demographics_data = list(demographics_collection.find())

# Check if the collection is not empty
if demographics_data:
    # Load data into a Pandas DataFrame
    demographics_df = pd.DataFrame(demographics_data)

    # Perform operations on the DataFrame
    demographics_df['population_growth_rate'] = demographics_df['Population'.pct_change().fillna(0)
    print(demographics_df.head())
else:
    print("The demographics collection is empty. Please check the data.")

