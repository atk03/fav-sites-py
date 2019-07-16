import requests
from bs4 import BeautifulSoup

# url definition
url = "https://www.vice.com/it"
# Request
req = requests.get(url)
req.status_code

# We'll save in coverpage the cover page content
content = req.content

# Soup creation
soup1 = BeautifulSoup(content, 'html.parser')

# News identification
news = soup1.find_all('a', class_= 'grid__wrapper__card grd-col col-12-xs col-6-m col-3-hd dsp-block-xs p-t-3-xs col-3-xl')
len(news)

# Number of articles in the home page
number_of_articles = len(news)

# Empty lists for links
list_links = []

for n in range(number_of_articles):
    # Getting the link of the article
    link = 'https://www.vice.com' + news[n].get('href')
    list_links.append(link)

print(list_links)

