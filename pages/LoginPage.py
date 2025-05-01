from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

__USERNAME_INPUT = (By.ID, "user-name")
__PASSWORD_INPUT = (By.ID,"password")
__LOGIN_BUTTON= (By.ID, "login-button")

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def login_as(self, username,password):
        self._write_text_on(By.ID,"user-name",username)

        self._write_text_on(By.ID,"password",password)

        self._clickOn(By.ID, "login-button")
    