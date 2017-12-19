import requests
from bs4 import BeautifulSoup
import csv

url = "http://www.values.com/inspirational-quotes"
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html5lib')

quotes = []		#list of dictionaries representing quotes

table = soup.find('div', attrs = {'id':'portfolio'})

for row in table.findAll('div', attrs = {'class':'portfolio-image'}):
	quote = {}		#dictionary
	#quote['theme'] = row.h5.text
	quote['url'] = row.a['href']
	quote['img'] = row.img['src']
	quote['lines'] = row.img['alt']
	#quote['author'] = row.p.text
	quotes.append(quote)

filename = 'Quotes.csv'
with open(filename, 'wb') as f:
	#w = csv.DictWriter(f, ['theme', 'url', 'img', 'lines', 'author'])
	w = csv.DictWriter(f, ['url', 'img', 'lines'])
	w.writeheader()
	for quote in quotes:
		w.writerow(quote)