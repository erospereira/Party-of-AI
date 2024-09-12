import pymongo
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Connect to MongoDB and load data
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["CALGARY"]  # Replace with your database name
collection = db["Statistics"]
raw_data = list(collection.find())
data = pd.json_normalize(raw_data)

# Select features and target
X = data[['Economics.Labour_Force_Status.Employed', 
          'Economics.Labour_Force_Status.Unemployed']]  # Example features
y = data['Economics.Income_Statistics_2020.Median_Total_Income_Individuals']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions and evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Linear Regression MSE: {mse}")
