from bs4 import BeautifulSoup
import requests


def save():
    with open('2.txt', 'a', encoding="utf-8") as file:
        file.write(f'{comp["title"]} -> description: {comp["description"]} -> Price: {comp["price"]} -> img: {comp["img"]}\n')

def get_text(item, name=None, attrs={}, recursive=True, text=None, **kwargs):
    text = ''
    try:
        text = item.find(name, attrs, recursive, text, **kwargs).get_text(strip = True)
    except:
        pass

    return text

def get_image_src(item, name=None, attrs={}, recursive=True, text=None, **kwargs):
    text = ''
    try:
        text = item.find(name, attrs, recursive, text, **kwargs).get('src')
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
    items = soup.findAll('a', class_ = 'catalog-navigation-list__dropdown-item')
    #items = soup.findAll('body') # поиск по всей странице
    comps = []
    
    for item in items:
        NameS = get_text(item, 'span', class_ = 'catalog-navigation-list__dropdown-title')
        priceS = get_image_src(item,'a', class_ = 'catalog-navigation-list__dropdown-item')
        descriptionS = get_url(item,'a', class_ = 'catalog-navigation-list__dropdown-item')
        #imgSrc = get_href(item,'a', class_ = 'catalog-navigation-list__dropdown-item')

        try:
            imgSrc = item.get('href')
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
            print(f'{comp["title"]} -> description: {comp["description"]} -> Price: {comp["price"]} -> img: {comp["img"]}')
            save()


with open("1.txt", "r", encoding="utf-8") as file1:
    for line in file1:
        parse (line)