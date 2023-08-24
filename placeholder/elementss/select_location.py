
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys 
from findelement import find_e
from findelement import send
fe=find_e()
sd=send()

class loc:
    from_field=Select(fe.findelement("xpath",'//select[@name="fromPort"]'))
    to_field = Select(fe.findelement("xpath", '//select[@name="toPort"]'))
    submit = fe.findelement("xpath", "/html/body/div[3]/form/div/input")
def location():
    lc= loc()
    lc.from_field.select_by_value("Paris")
    lc.to_field.select_by_value("London")
    lc.submit(sd.sendkeys(Keys.ENTER))
    