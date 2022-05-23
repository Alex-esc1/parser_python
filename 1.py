from bs4 import BeautifulSoup
import requests
def save():
    with open('1.txt', 'a') as file:
        file.write(f'{comp["title"]} -> Price: {comp["price"]} -> img: {comp["img"]}\n')
def parse():
     URL = 'https://www.olx.kz/elektronika/kompyutery-i-komplektuyuschie/'
     HEADERS = {
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
     }
     response = requests.get(URL, headers = HEADERS)
     soup = BeautifulSoup(response.content, 'html.parser')
     items = soup.findAll('div', class_ = 'offer-wrapper' )
     comps = []
     
     for item in items:
        comps.append({
            'title': item.find('h3', class_ = 'lheight22 margintop5').get_text(strip = True),
            'price': item.find('p', class_ = 'price').get_text(strip = True),
            'img': item.find('img', class_ = 'fleft').get('src')
        })
        global comp
        for comp in comps:
            print(f'{comp["title"]} -> Price: {comp["price"]} -> img: {comp["img"]}')
            save()


234325435


parse ()

