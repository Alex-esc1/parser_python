from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options, executable_path=r"C:/test/geckodriver.exe")
driver.maximize_window()

def save():
    with open('2.csv', 'a', encoding="utf-8") as file:
        file.write(f'{elem.get_attribute("href")}\n')

with open("1.txt", "r", encoding="utf-8") as file:
    for line in file:
        URL = line.strip()
        driver.get(URL)
        elems = driver.find_elements_by_xpath("//a[@href]")
        for elem in elems:
            print (elem.get_attribute("href"))
            save()