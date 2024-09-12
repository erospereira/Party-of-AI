import requests
import pandas as pd

# Replace with your actual API key
api_key = "20d2f4f31892431b9e51d9721da17518"
query = "Calgary"
url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}"

response = requests.get(url)

if response.status_code == 200:
    news_data = response.json()
    
    # Extract the articles from the JSON response
    articles = news_data['articles']
    
    # Create a DataFrame from the articles
    df = pd.DataFrame(articles)
    
    # Save the DataFrame to a CSV file
    df.to_csv('calgary_news_dataset.csv', index=False)
    
    print("Data saved to calgary_news_dataset.csv")
else:
    print(f"Failed to fetch data: {response.status_code}")
