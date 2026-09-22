import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestSelectorsCss:
    def test_selectors_css(self, driver):
        time.sleep(2)
        footer = driver.find_element(By.TAG_NAME, 'footer')
        print(footer.tag_name)

        tools = driver.find_element(By.CSS_SELECTOR, "img[src='/assets/Toolsqa-DZdwt2ul.jpg']")
        print(tools.get_attribute('src'))

        driver.find_element(By.CSS_SELECTOR, "a[href='/elements']").click()
        time.sleep(2)

        driver.back()





