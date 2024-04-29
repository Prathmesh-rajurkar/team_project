import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI

app = FastAPI()

# url = "https://indianexpress.com/"

def scarpe_news(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    news_articles = soup.find_all('div', class_='other-article') 
    news_data = []
    for article in news_articles:
        summary = article.find('h3').text.strip()
        image_url = article.find('img').get('src')
        # image_alt = article.find('img').get('alt')
        # article_url = article.find('a')['href']
        news_data.append({
            # 'headline': headline,
            'summary': summary,
            'image_url': image_url,
            # 'image_alt': image_alt,
            # 'url': article_url
        })
    return news_data

def scarper(url,div_name=None):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    news_articles = soup.find_all('div', class_=div_name) 
    news_data = []
    for article in news_articles:
        headline = article.find(class_="title").text.strip()
        image_url = article.find('img').get('src')
        summary = article.find('p').text.strip()
        news_data.append({
            'headline': headline,
            'summary': summary,
            'image_url': image_url,
        })
    return news_data
    
news_top = scarpe_news("https://indianexpress.com/")
news_business = scarper("https://indianexpress.com/section/business/")
news_sports = scarper("https://indianexpress.com/section/sports/",div_name="nation")
news_entertainment = scarper("https://indianexpress.com/section/entertainment/",div_name="stories")
news_politics = scarper("https://indianexpress.com/section/political-pulse/")


@app.get("/news/top")
async def get_news():
    return news_top


@app.get("/news/business")
async def get_news():
    return news_business


@app.get("/news/sports")
async def get_news():
    return news_sports

@app.get("/news/business")
async def get_news():
    return news_business

@app.get("/news/entertainment")
async def get_news():
    return news_entertainment

@app.get("/news/politics")
async def get_news():
    return news_politics

