from selenium.webdriver.common.keys import Keys
from findelement import find_e
from findelement import send
fe=find_e()
sd=send()


class selectfli:
    flight_selection = fe.findelement("xpath",'//input[@value="Choose This Flight"]')
def select_flights():
    sf=selectfli()
    sf.flight_selection(sd.sendkeys(Keys.ENTER))