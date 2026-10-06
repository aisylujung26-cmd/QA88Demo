import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from conftest import driver


def hide_footer(driver):
    driver.execute_script("document.querySelector('footer').style.display='none'")

def scroll_down(driver, steps: int = 10, pixels: int = 500, pause: float = 0.5) -> None:
    for _ in range(steps):
        ActionChains(driver).scroll_by_amount(0, pixels).perform()
        time.sleep(pause)


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

        driver.find_element(By.CSS_SELECTOR, "[href='/elements']").click()

        #driver.find_element(By.ID, "item-0").click()
        #driver.find_element(By.CSS_SELECTOR, "#item-0").click()
        #"li#item-0"
        # driver.find_element(By.CSS_SELECTOR, "li#item-0").click()
        #"li#[id=item-0]"
        driver.find_element(By.CSS_SELECTOR, "a[class='router-link']").click()
        time.sleep(2)

        driver.back()

        driver.find_element(By.CSS_SELECTOR, "[class='router-link']").click()
        time.sleep(2)

        driver.back()

        driver.find_element(By.CLASS_NAME, "router-link").click()

        time.sleep(2)

        driver.back()

        driver.find_element(By.CLASS_NAME, "router-link").click()
        #driver.find_element(By.CLASS_NAME, "btn btn-light").click()nicht richtig
        #driver.find_element(By.CLASS_NAME, "btn").click()ist richtig
        time.sleep(2)

        driver.back()
        # "router-link"
        # ".router-link"
        # "a.router-link"
        # "a[class='router-link']"
        # "[class='router-link']"
        # "router-link"  By.CLASS_NAME
        # ".router-link" By.CSS_SELECTOR через сокращенную форму '.'
        # "a.router-link" By.CSS_SELECTOR tagname и через сокращенную форму '.'
        # "a[class='router-link']" By.CSS_SELECTOR  по  tagname и по аттрибуту
        # "[class='router-link']" By.CSS_SELECTOR  по аттрибуту


        driver.find_element(By.CSS_SELECTOR, ".router-link").click()
        #suchen css class kurz '.'
        time.sleep(2)

        driver.find_element(By.CSS_SELECTOR, "input#userName.mr-sm-2.form-control").send_keys("Ais")
        time.sleep(2)

        #div.element-list li:nth-child(5)a suche nach 5 kind per diese element
        driver.back()

        driver.find_element(By.CSS_SELECTOR, "div.element-list li:nth-child(5) a").click()

        time.sleep(2)
        hide_footer(driver)
        scroll_down(driver)

        driver.find_element(By.CSS_SELECTOR, "div.element-list li:last-child a").click()
        time.sleep(2)

    def test_selectors_css_parts(self, driver):
        time.sleep(2)
        #div.category-cards>a:nth-child(2)
        driver.find_element(By.CSS_SELECTOR, "div[class*='ory-card']>a:nth-child(2)").click()
        time.sleep(2)
        driver.back()

        driver.find_element(By.CSS_SELECTOR, "div[class^='category']>a:nth-child(2)").click()
        time.sleep(2)
        driver.back()

        driver.find_element(By.CSS_SELECTOR, "div[class$='cards']>a:nth-child(2)").click()
        time.sleep(2)

        # //a[@class='router-link'] By.Xpath
        # a[class='router-link']    By.CSS

        driver.find_element(By.XPATH, "//a[@href='/automation-practice-form']").click()

    def test_selectors_xpath(self, driver):
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[@href='/elements']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[@href='/text-box']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@placeholder='Full Name']").send_keys("Pups")
        time.sleep(2)
        driver.find_element(By.XPATH, "//form/div[2]/div[2]/input").send_keys("aisic@gmail.com")
        driver.find_element(By.XPATH, "//*[text()='Current Address']/../..//textarea").send_keys("19230 HGW")
        driver.find_element(By.XPATH, "//*[@id='permanentAddress-wrapper']/div[2]/textarea").send_keys("Giuz")
        #driver.find_element(By.XPATH, "//form/div[4]/div[2]/textarea").send_keys("12983 GSIU")
        driver.find_element(By.XPATH, "//button[text()='Submit']").click()

        div_output = driver.find_element(By.XPATH, "//div[@id='output']")

        assert "Pups" in div_output.text

    def test_selectors_xpath_parts(self, driver):
        time.sleep(2)
        #contains parts
        driver.find_element(By.XPATH, "//div[contains(@class, 'ory-cards')]/a[@href='/elements']").click()
        time.sleep(2)

        #//a[@href='/radio-button'] XPATH
        #//*[start-with@href='/radio-b']

        driver.find_element(By.XPATH, "//*[starts-with(@href,'/radio-b')]").click()
        time.sleep(2)
        #id="yesRadio" class ="form-check-input"
        #//input[@id='yesRadio' and @class ='form-check-input']

        driver.find_element(By.XPATH, "//input[@id='yesRadio' and @class ='form-check-input']").click()
        time.sleep(2)

        driver.find_element(By.XPATH,"//input[@id='impressiveRadio' or @class ='from-check-input']").click()
        time.sleep(2)

        # "//input[contains(@id,'yesRad') and starts-with(@class ='form-che')]").click()

        driver.find_element(By.XPATH,"//input[contains(@id,'yesRad') and starts-with(@class,'form-che')]").click()
        time.sleep(2)


        #driver.find_element(By.LINK_TEXT, "/text-box").click()

        driver.find_element(By.CSS_SELECTOR, "div[class='element-list accordion-collapse collapse show'] li:nth-child(2)>a").click()
        time.sleep(2)

        driver.find_element(By.XPATH,"//div[@class='element-list accordion-collapse collapse show']//li[3]/a").click()
        time.sleep(2)

        #//label[text()='No']/../../div[1]/input
        driver.find_element(By.XPATH,"//label[text()='No']/../../div[1]/input").click()
        time.sleep(2)

    def test_selectors_links(self, driver):
        driver.find_element(By.XPATH, "//div[contains(@class, 'ory-cards')]/a[@href='/elements']").click()
        time.sleep(2)

        driver.find_element(By.LINK_TEXT, "Links").click()
        time.sleep(2)

        driver.find_element(By.LINK_TEXT,"No Content").click()
        time.sleep(2)























