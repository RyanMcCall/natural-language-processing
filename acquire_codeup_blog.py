from requests import get
from bs4 import BeautifulSoup

def get_soup(link):
    headers = {'User-Agent': 'Codeup Data Science'}
    response = get(link, headers=headers)
    
    return BeautifulSoup(response.content, 'html.parser')

def get_article_info(soup):
    article_text = soup.find('div', class_='jupiterx-post-content clearfix').text
    article_title = soup.find('h1', class_='jupiterx-post-title').text

    return {'title': article_title,
            'content': article_text}

def get_blog_articles():
    links = ['https://codeup.com/codeups-data-science-career-accelerator-is-here/',
    'https://codeup.com/data-science-myths/',
    'https://codeup.com/data-science-vs-data-analytics-whats-the-difference/',
    'https://codeup.com/10-tips-to-crush-it-at-the-sa-tech-job-fair/',
    'https://codeup.com/competitor-bootcamps-are-closing-is-the-model-in-danger/']

    articles = []

    for link in links:
        soup = get_soup(link)

        article_dict = get_article_info(soup)
        
        articles.append(article_dict)

    return articles

def get_all_blog_articles():
    url = 'https://codeup.com/resources/#blog'
    headers = {'User-Agent': 'Codeup Data Science'}
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    links = []

    for a in soup.find_all('a', class_='jet-listing-dynamic-link__link', href=True):
        links.append(a['href'])
        
    articles = []

    for link in links:
        headers = {'User-Agent': 'Codeup Data Science'}
        response = get(link, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        article_text = soup.find('div', class_='jupiterx-post-content clearfix').text
        article_title = soup.find('h1', class_='jupiterx-post-title').text

        article_dict = {'title': article_title,
                        'content': article_text}

        articles.append(article_dict)

    return articles