from selenium import webdriver
import pytest

driver = None
@pytest.fixture(scope="module")
def init_driver():
    global driver
    driver = webdriver.Chrome("chromedriver.exe")
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("http://google.com")

    yield           # will be executed after all the test cases
    driver.quit()
@pytest.mark.usefixtures('init_driver')
def test_google_title():
    assert driver.title == "Google"
@pytest.mark.usefixtures('init_driver')
def test_google_url():
    assert driver.current_url == "https://www.google.com/?gws_rd=ssl"
# to run this use : pytest test_google_fixture.py -v -s --html=test_google_fixture_report.html
