import requests
api_key = "20d2f4f31892431b9e51d9721da17518"
news_data = fetch_news_via_api(api_key)

def fetch_news_via_api(api_key, query="Calgary"):
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}"
    response = requests.get(url)
    
    print(f"Response Status Code: {response.status_code}")
    
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
        formatted_data.append([headline, date, source, url])

    return formatted_data

# Replace with your actual API key

