from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("D:/Coders_ club/Python_/Selenium/Driver/chromedriver.exe")

driver.set_page_load_timeout(10)
driver.get("http://google.com")
driver.find_element_by_name("q").send_keys("wikipedia")
driver.find_element_by_name("btnk").send_keys(Keys.ENTER)
time.sleep(4)
driver.quit()
