import requests

api_key = "20d2f4f31892431b9e51d9721da17518"
query = "Calgary"
url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}"

response = requests.get(url)

if response.status_code == 200:
    news_data = response.json()
    print(news_data)
else:
    print(f"Failed to fetch data: {response.status_code}")
