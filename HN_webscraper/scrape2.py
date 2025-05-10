import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titleline')
subline = soup.select('.subline')

def create_custom_hn(links, subline):
    hn=[]
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subline[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
             hn.append({'title': title, 'link': href, 'votes': points})
            return hn


pprint.pprint(create_custom_hn(links,subline))