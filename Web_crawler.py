import requests
from bs4 import BeautifulSoup



def crawler(max_pages):
    pages = 1
    while pages<=max_pages:
        url = 'https://thenewboston.com/forum/recent_activity.php?page=' + str(pages)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for link in soup.findAll('a', {'class':'title text-semibold'}):
            href = link.get('href')
            title = link.string
            print(href)
            print(title)
        pages += 1

crawler(1)