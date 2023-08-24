import pytest
import elementss.select_location as select_location
# import elementss.select_flight as select_flight
# import elementss.coustomerid as coustomerid


import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()  
    yield driver
    driver.quit()  

    
def test_1(driver):  # Pass the 'driver' fixture here
    select_location.location(driver)
    # select_flight.select_flights(driver)
    # coustomerid.coustomer_id(driver)  