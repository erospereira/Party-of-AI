import tensorflow as tf
from sklearn import datasets
from pymongo import MongoClient

print("TensorFlow version:", tf.__version__)
iris = datasets.load_iris()
print("Iris dataset loaded with shape:", iris.data.shape)

# Test MongoDB connection
client = MongoClient("your_mongodb_connection_string")
print("MongoDB version:", client.server_info()['version'])
