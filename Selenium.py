from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options

def save():
    with open('2.txt', 'a', encoding="utf-8") as file:
        file.write(f'{comp["title"]}@Price: {comp["price"]}@img: {comp["img"]}@description: {comp["description"]}\n')

def parse(line):
    URL = line.strip()
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options, executable_path=r"C:/test/geckodriver.exe")
    driver.maximize_window()
    WebDriverWait(driver,10)
    driver.get(URL) 
    comps = []
    try:
        name = driver.find_elements_by_css_selector('p.b-product__price')
        for names in name:
            name = (names.text)
    except:
        pass

    try:
        price = driver.find_elements_by_css_selector('p.b-product__price')
        for prices in price:
            price = (prices.text)
    except:
        pass

    description = driver.find_elements_by_css_selector('p.b-product__price')
    for descriptions in description:
        description = (descriptions.text)
    imgsrc = driver.find_elements_by_css_selector('p.b-product__price')
    for imgsrcs in imgsrc:
        imgsrc = (imgsrcs.text)

    comps.append({
            'title': name,
            'price': price,
            'img': imgsrc,
            'description': description
        })

    global comp
    for comp in comps:
            print(f'{comp["title"]} -> description: {comp["description"]} -> Price: {comp["price"]} -> img: {comp["img"]}')
            save()
    driver.quit()

with open("1.txt", "r", encoding="utf-8") as file1:
    for line in file1:
        parse (line)





