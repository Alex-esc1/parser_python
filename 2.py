from bs4 import BeautifulSoup
import requests


def save():
    with open('1.txt', 'a', encoding="utf-8") as file:
        file.write(f'{comp["title"]} -> Price: {comp["price"]} -> img: {comp["img"]}\n')


def parse(line):
    URL = line.strip()
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(URL, headers = HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    # поиск в определнном блоке на странице items = soup.findAll('div', class_ = 'offer-wrapper' )
    items = soup.findAll('body') # поиск по всей странице
    comps = []
    
    for item in items:
        img = item.find('img', class_ = 'fleft')

        imgSrc = ''
        try:
            imgSrc = img.get('src')
        except:
            pass

        NameS = ''
        try:
            NameS = item.find('h3', class_ = 'lheight22 margintop5').get_text(strip = True)
        except:
            pass

        priceS = ''
        try:
            priceS = item.find('p', class_ = 'price').get_text(strip = True)
        except:
            pass

        descriptionS = ''
        try:
            descriptionS = item.find('p', class_ = 'price').get_text(strip = True)
        except:
            pass

        comps.append({
            'title': NameS,
            'price': priceS,
            'img': imgSrc,
            'description': descriptionS
        })

        global comp
        for comp in comps:
            print(f'{comp["title"]} -> Price: {comp["price"]} -> img: {comp["img"]}')
            save()


with open("2.txt", "r", encoding="utf-8") as file1:
    for line in file1:
        parse (line)
