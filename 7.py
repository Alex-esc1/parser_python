from bs4 import BeautifulSoup
import requests


def save():
    with open('2.txt', 'a', encoding="utf-8") as file:
        file.write(f'{comp["title"]} -> description: {comp["description"]} -> Price: {comp["price"]} -> img: {comp["img"]}\n')

def get_text(parent, name=None, index=0, attrs={}, recursive=True, text=None, **kwargs):
    items = parent.findAll(name, attrs, recursive, text, **kwargs)
    if index >= len(items):
        return ''
    item = items[index]
    try:
        return item.get_text(strip = True)
    except:
        return ''

#def get_image_src(parent, name=None, index=0, attrs={}, recursive=True, text=None, **kwargs):
    #items = parent.findAll(name, attrs, recursive, text, **kwargs).get('src')
   # if index >= len(items):
  #      return ''
 #   item = items[index]
#    try:
#        return item.get_image_src(strip = True)
#    except:
#        return ''

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

def get_title(item, name=None, attrs={}, recursive=True, text=None, **kwargs):
    text = ''
    try:
        text = item.find(name, attrs, recursive, text, **kwargs).get('title')
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
    items = soup.findAll('div', class_ = 'main-content')
    #items = soup.findAll('body') # ?????????? ???? ???????? ????????????????
    comps = []
    
    for item in items:
        NameS = get_title(item, 'img')
        priceS = get_text(item, 'span', class_ = 'current-price')
        descriptionS = get_text(item, 'div', class_ = 'ok-product-full-desc tab-pane active')
        imgSrc = get_image_src(item,'img')

        #try:
        #     imgSrc = item.get('href')
        #except:
        #     pass

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