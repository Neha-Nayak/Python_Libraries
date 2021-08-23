from selenium import webdriver
import pytest
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(scope="class")
def init_chrome_driver(request):
    ch_driver = webdriver.Chrome("chromedriver.exe")
    request.cls.driver = ch_driver
    yield
    ch_driver.close()
@pytest.fixture(scope="class")
def init_Edge_driver(request):
    Edge_driver = webdriver.Edge(executable_path="msedgedriver.exe")
    request.cls.driver = Edge_driver
    yield
    Edge_driver.close()

@pytest.mark.usefixtures('init_chrome_driver')
class Base_Chrome_Test:
    pass
class Test_Google_chrome(Base_Chrome_Test):
    def test_google_title_chrome(self):
        self.driver.get("http://google.com")
        assert self.driver.title == "Google"

@pytest.mark.usefixtures('init_Edge_driver')
class Base_Edge_Test:
    pass
class Test_google_Edge(Base_Edge_Test):
    def test_google_title_Edge(self):
        self.driver.get("http://google.com")
        assert self.driver.title == "Google"