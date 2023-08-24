def execute1():
    import elementss.select_location as select_location
    import elementss.select_flight as select_flight
    import elementss.coustomerid as coustomerid
    import elementss.verify as verify

    from selenium import webdriver
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.common.keys import Keys 
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("https://blazedemo.com/")
    print("\n\ndriver opened\n\n")
    driver.implicitly_wait(30)
    select_location.location("Paris","London")
    select_flight.select_flights()
    coustomerid.coustomer_id()