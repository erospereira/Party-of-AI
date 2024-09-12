import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from pymongo import MongoClient

# Sample DataFrame (replace with your actual data loading step)
data = pd.DataFrame({
    'feature1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'feature2': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    'Median_Total_Income_Individuals': [30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000, 70000, 75000]
})

# Define features and target variable
X = data[['feature1', 'feature2']]  # Features
y = data['Median_Total_Income_Individuals']  # Target

# Perform train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a simple model (Decision Tree)
model = DecisionTreeRegressor()
model.fit(X_train, y_train)

# Assuming new data to predict
new_data = X_test.iloc[:5]  # Example of new data

# Make predictions
predictions = model.predict(new_data)

# Connect to MongoDB (adjust the connection string as needed)
client = MongoClient("mongodb://localhost:27017/")
db = client["CALGARY"]  # Replace with your actual database name
collection = db["Statistics"]  # Replace with your actual collection name

# Update MongoDB with predictions
for i, pred in enumerate(predictions):
    # Convert numpy.int64 to Python int
    _id = int(new_data.index[i])  # Ensure _id is a Python int
    pred = int(pred)  # Convert prediction to Python int if necessary
    collection.update_one({"_id": _id}, {"$set": {"Predicted_Income": pred}})

print("Predictions updated in MongoDB successfully!")
