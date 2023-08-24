from selenium import webdriver 
driver=webdriver.Chrome()

def verify_url():

    current = driver.current_url
    expected= "https://blazedemo.com"

    if current== expected:
        print("done")
    else:
        assert current != expected, "Purchase fail"
        import datetime
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        screenshot_file = f"failure_{timestamp}.png"
        driver.save_screenshot(screenshot_file)
