import requests
from bs4 import BeautifulSoup
import csv

res = requests.get('https://ge.globo.com/futebol/times/corinthians/noticia/2023/04/20/corinthians-fara-reuniao-nessa-quinta-feira-para-avaliar-se-demite-fernando-lazaro.ghtml')
soup = BeautifulSoup(res.text, 'html.parser')

if res.status_code != 200:
    raise RuntimeError(f'Error: {res.status_code}')

scraped_title = soup.find('div', attrs={'class':'title'})
scraped_text = soup.findAll('p', attrs={'class':'content-text__container'})


full_text = scraped_title.text + ' '.join([tag.text for tag in scraped_text])

file = open('scrapped_data.csv', 'w')
writer = csv.writer(file)

writer.writerow(['Scraped Text'])

writer.writerow([full_text.encode('utf-8')])

file.close()

