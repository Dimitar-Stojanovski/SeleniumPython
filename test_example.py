from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.LoginPage import LoginPage 
import pytest

@pytest.fixture
def browser():
  driver = webdriver.Chrome()
  driver.maximize_window()
  yield driver
  driver.quit()
 

def test_login_scenario(browser):
 browser.get("https://www.saucedemo.com/")
 login_page = LoginPage(browser)
 login_page.login_as("standard_user", "secret_sauce")
 assert browser.title == "Swag Labs", f"Page title is not ${browser.title}"



