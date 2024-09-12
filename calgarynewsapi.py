import requests
import pandas as pd

def fetch_news_via_api(api_key, query="Calgary"):
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Failed to fetch data from the API")
        return []

    news_data = response.json().get('articles', [])
    formatted_data = []

    for article in news_data:
        headline = article['title']
        date = article['publishedAt']
        source = article['source']['name']
        url = article['url']
        
        # Append the data to the list
        formatted_data.append([headline, date, source, url])

    return formatted_data

def save_to_csv(news_data, filename="calgary_news_dataset_api.csv"):
    df = pd.DataFrame(news_data, columns=['headline', 'date', 'source', 'url'])
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

# Example usage
api_key = "your_newsapi_key_here"
news_data = fetch_news_via_api(api_key)
if news_data:
    save_to_csv(news_data)
