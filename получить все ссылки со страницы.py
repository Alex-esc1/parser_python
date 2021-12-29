from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

 
options = Options()
options.headless = True
driver = webdriver.Firefox(executable_path=r"C:/test/geckodriver.exe")
driver.maximize_window()
driver.get("https://minus50.by/")
 



elems = driver.find_elements_by_xpath("//a[@href]")
for elem in elems:
    print (elem.get_attribute("href"))

print(driver.title) #получить заголовок страницы