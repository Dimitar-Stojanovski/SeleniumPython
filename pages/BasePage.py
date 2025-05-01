from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
 
class BasePage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def __waitForElement_to_be_visible(self,by,value):
       return self.wait.until(EC.visibility_of_element_located((by,value)))


    def _clickOn(self,by,value):
        self.__waitForElement_to_be_visible(by,value).click()

    def _write_text_on(self,by,value,text):
        element = self.__waitForElement_to_be_visible(by,value)
        element.send_keys(text)

    def _get_attribute(self, by,value,attribute):
        element = self.wait.until(EC.visibility_of_element_located((by,value)))
        return element.get_dom_attribute(attribute)