from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://blazedemo.com/")

class find_e:
    @staticmethod
    def findelement(type,path):
        global a
        a= driver.find_element((type,path))

class send:
    @staticmethod
    def sendkeys(data):
        a.send_keys(data)
