import pytest
from selenium import webdriver
import time

BASE_URL = "https://demoqa.com/"

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.set_page_load_timeout(10)
    driver.implicitly_wait(10)

    driver.get(BASE_URL)

    yield driver

    time.sleep(5)
    driver.quit()
    #driver.close()

    def test_selectors_xpath(self, driver):
        time.sleep(2)
        # поиск по части аттрибута By.CSS_SELECTOR




