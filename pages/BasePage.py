from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
 
class BasePage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def __waitForElement_to_be_visible(self,locator):
       return self.wait.until(EC.visibility_of_element_located(locator))


    def _clickOn(self,locator):
        self.wait.until(EC.visibility_of_element_located(locator)).click()

    def _write_text_on(self,locator,text):
        element = self.__waitForElement_to_be_visible(locator)
        element.send_keys(text)

    def _get_attribute(self, locator,attribute):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.get_dom_attribute(attribute)