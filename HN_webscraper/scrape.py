import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')


#grab elements using css selectors
# learn css selectors to grab certain elements from a webpage
links = soup.select('.titleline')
votes = soup.select('.score')

#we can keep chaining this.

print(votes[5].get('id'))