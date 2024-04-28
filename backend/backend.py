import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI

app = FastAPI()

url = "https://indianexpress.com/"

def scrape_news(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Identify news article elements using appropriate selectors (e.g., class names, IDs, tags)
    news_articles = soup.find_all('div', class_='other-article')  # Replace with actual selectors

    news_data = []
    for article in news_articles:
        # Extract news data (headline, summary, URL) using proper selectors
        # headline = article.find('h3').text.strip()  # Replace with actual selectors
        summary = article.find('h3').text.strip()  # Replace with actual selectors
        image_url= article.find('img').get('src')
        # article_url = article.find('a')['href']

        news_data.append({
            # 'headline': headline,
            'summary': summary,
            'image_url': image_url,
            # 'url': article_url
        })

    return news_data

news = scrape_news(url)
print(news)

@app.get("/news/top")
async def get_news():
    # scraped_news = scrape_news("https://www.example.com/news")  # Replace with target URL
    return news
