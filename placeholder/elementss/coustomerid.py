from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from findelement import find_e
from findelement import send
fe=find_e()
sd=send()

class users:
    p_name = fe.findelement("id", "inputName")
    p_adress = fe.findelement("id", "address")
    p_city = fe.findelement("id", "city")
    p_state = fe.findelement("id", "state")
    p_zipcode = fe.findelement("id", "zipCode")
    p_cardtype = Select(fe.findelement("name", "cardType"))
    p_cardnum = fe.findelement("id", "creditCardNumber")
    p_cMonth = fe.findelement("id", "creditCardMonth")
    p_cYear = fe.findelement("id", "creditCardYear")
    p_cName = fe.findelement("id", "nameOnCard")
    remember = fe.findelement("xpath", '//input[@name="rememberMe"]')
    
def coustomer_id():
    user1 = users()
    user1.p_name(sd.sendkeys("arvi"))
    user1.p_adress(sd.sendkeys("rftgvbd"))
    user1.p_city(sd.sendkeys("rftgvbd"))
    user1.p_state(sd.sendkeys("rftgvbd"))
    user1.p_zipcode(sd.sendkeys("rftgvbd"))
    user1.p_cardtype(sd.sendkeys("rftgvbd"))
    user1.p_cardnum(sd.sendkeys("rftgvbd"))
    user1.p_cMonth(sd.sendkeys("rftgvbd"))
    user1.p_cYear(sd.sendkeys("rftgvbd"))
    user1.p_cName(sd.sendkeys("rftgvbd"))
    user1.remember(sd.sendkeys(Keys.ENTER))
    
 
    