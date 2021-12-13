from bs4 import BeautifulSoup
import requests


def save():
    with open('2.csv', 'a', encoding="utf-8") as file:
        file.write(f'{comp["title"]};link: {comp["links"]};Price: {comp["price"]};img: {comp["img"]};description: {comp["description"]}\n')

def get_text(parent, name=None, index=0, attrs={}, recursive=True, text=None, **kwargs):
    items = parent.findAll(name, attrs, recursive, text, **kwargs)
    if index >= len(items):
        return ''
    item = items[index]
    try:
        return item.get_text(strip = True)
    except:
        return ''

def get_image_src(item, name=None, attrs={}, recursive=True, text=None, **kwargs):
    text = ''
    try:
        text = item.find(name, attrs, recursive, text, **kwargs).get('src')
    except:
        pass

    return text

def get_image(item, name=None, attrs={}, recursive=True, text=None, **kwargs):
    text = ''
    try:
        text = item.find(name, attrs, recursive, text, **kwargs).get('data-srcset')
    except:
        pass

    return text

def get_href(item, name=None, attrs={}, recursive=True, text=None, **kwargs):
    text = ''
    try:
        text = item.find(name, attrs, recursive, text, **kwargs).get('href')
    except:
        pass

    return text

def get_url(item, name=None, attrs={}, recursive=True, text=None, **kwargs):
    text = ''
    try:
        text = item.find(name, attrs, recursive, text, **kwargs).get('url')
    except:
        pass

    return text

def parse(line):
    URL = line.strip()
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(URL, headers = HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    #items = soup.findAll('section', class_ = 'l-content')
    items = soup.findAll('body') # поиск по всей странице
    comps = []
    
    for item in items:
        NameS = get_text(item, 'h1')
        priceS = get_text(item, 'div', class_ = 'prices')
        descriptionS = soup.findAll(True, {"class": ["description"]})
        imgSrc = get_image_src(item,'img', class_ = 'product-image')
        link = URL

        #try:
        #     imgSrc = item.get('href')
        #except:
        #     pass

        comps.append({
            'title': NameS,
            'price': priceS,
            'img': imgSrc,
            'links': link,
            'description': descriptionS
        })

        global comp
        for comp in comps:
            print(f'{comp["title"]} -> description: {comp["description"]} -> Price: {comp["price"]} -> img: {comp["img"]} -> link: {comp["links"]}')
            save()


with open("1.txt", "r", encoding="utf-8") as file1:
    for line in file1:
        parse (line)