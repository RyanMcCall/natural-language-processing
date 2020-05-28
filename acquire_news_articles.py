from requests import get
from bs4 import BeautifulSoup
from os import path
import pandas as pd

def get_news_articles(keep_old=True):
    
    if path.isfile('news_articles.csv') and keep_old:
        return pd.read_csv('news_articles.csv')
    
    else:
        pages = ['/business', '/sports', '/technology','/entertainment']

        articles = []

        for page in pages:
            url = 'https://inshorts.com/en/read' + page
            response = get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            headlines = soup.find_all('span', itemprop='headline')
            contents = soup.find_all('div', itemprop='articleBody')

            for n in range(len(headlines)):
                article = {'title': headlines[n].text,
                          'content': contents[n].text,
                          'catagory': page[1:]}
                articles.append(article)
        
        df = pd.DataFrame(articles)
        
        df.to_csv('news_articles.csv')

        return df