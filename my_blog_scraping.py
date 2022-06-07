import requests
from bs4 import BeautifulSoup

blog_url = 'https://broken-works-screeming.blogspot.com/'
html_text = requests.get(blog_url)
soup = BeautifulSoup(html_text)
post = soup.find_all('div', class_='widget FeaturedPost')
