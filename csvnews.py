import requests
import pandas as pd
from bs4 import BeautifulSoup

# Example of web scraping news data from a website
def scrape_calgary_news():
    base_url = "https://calgaryherald.com/category/news/local-news/"
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    articles = soup.find_all('div', class_='article-card__details')
    news_data = []

    for article in articles:
        headline = article.find('a', class_='article-card__headline-link').get_text(strip=True)
        date = article.find('time').get_text(strip=True)
        url = article.find('a', class_='article-card__headline-link')['href']
        news_data.append([headline, date, "Calgary Herald", url])

    return news_data

# Save the news data into a CSV file
def save_to_csv(news_data, filename="calgary_news_dataset.csv"):
    df = pd.DataFrame(news_data, columns=['headline', 'date', 'source', 'url'])
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

# Example usage
news_data = scrape_calgary_news()
save_to_csv(news_data)
