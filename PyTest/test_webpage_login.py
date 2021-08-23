from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriveManager

import time

def test_google():
    driver = webdriver.Chrome("chromedriver.exe")
    driver.implicitly_wait(10)
    driver.get("http://google.com")
    assert driver.title == "Google"
    driver.quit()

def test_youtube():
    driver = webdriver.Chrome("chromedriver.exe")
    driver.implicitly_wait(10)
    driver.get("http://youtube.com")
    assert driver.title == "YouTube"
    driver.quit()

def test_github():
    driver = webdriver.Chrome("chromedriver.exe")
    driver.implicitly_wait(10)
    driver.get("http://github.com")
    assert driver.title == "GitHub: Where the world builds software · GitHub"
    driver.quit()

