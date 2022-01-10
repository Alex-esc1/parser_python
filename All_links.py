from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

options = Options()
options.headless = True
driver = webdriver.Chrome(options=options,executable_path=r"C:/test/chromedriver.exe")
driver.maximize_window()

with open("1.txt", "r", encoding="utf-8") as file:
    for line in file:
      URL = line.strip()
      driver.get(URL)
      elems = driver.find_elements_by_xpath("//a[@href]")
      for elem in elems:
        NameS = elem.get_attribute("href")
        Title = driver.title
        print (f'{Title};{NameS}')
        with open('2.txt', 'a', encoding="utf-8") as file:
          file.write(f'{Title};{NameS}\n')