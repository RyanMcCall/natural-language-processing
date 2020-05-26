from requests import get
from bs4 import BeautifulSoup

def get_news_articles():
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

    return articles