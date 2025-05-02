from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

USERNAME_INPUT = (By.ID, "user-name")
PASSWORD_INPUT = (By.ID,"password")
LOGIN_BUTTON= (By.ID, "login-button")

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def login_as(self, username,password):
        self._write_text_on(USERNAME_INPUT,username)

        self._write_text_on(PASSWORD_INPUT,password)

        self._clickOn(LOGIN_BUTTON)
    