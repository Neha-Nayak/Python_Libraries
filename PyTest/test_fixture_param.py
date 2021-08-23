from selenium import webdriver
import pytest

@pytest.fixture(params=['chrome', 'Edge'], scope="class")
def init__driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome("chromedriver.exe")
    if request.param == "Edge":
        web_driver = webdriver.Edge(executable_path="msedgedriver.exe")
    request.cls.driver = web_driver
    yield
    web_driver.close()

@pytest.mark.usefixtures('init__driver')
class BaseTest:
    pass

class Test_google(BaseTest):
    def test_google_title(self):
        self.driver.get("http://google.com")
        assert self.driver.title == "Google"
