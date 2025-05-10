import requests
from bs4 import BeautifulSoup
import pandas as pd

title = []
link = []
date = []

for x in range(1, 662):
    print(f'=====> Scraping from page {x}')
    url = f'https://www.atlasobscura.com/articles?page={x}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text, 'lxml')

    articles = soup.find_all('div', class_='col-md-4 col-sm-6 col-xs-12')
    for s in articles:
        story = s.find('div', class_='content-card-text').find('h3').find('span').text
        title.append(story)
        href = 'https://www.atlasobscura.com' + str(s.find('div').find('a')['href'])
        link.append(href)
        m_d_y = s.find('div', class_='detail-sm article-card-detail article-card-date').text.strip()
        if m_d_y is str:
            date.append(m_d_y)
        else:
            date.append('January 1, 2000')
    print(story, href, m_d_y)


    atlasobscura = pd.DataFrame({
        'Title': title,
        'Link': link,
        'Date': date
    })
    atlasobscura.to_excel('Atlasobscura.com.xlsx', index=False)