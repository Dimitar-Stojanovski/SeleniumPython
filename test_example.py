from selenium import webdriver
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage 
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


def test_add_to_Cart_Scenario(browser):
 browser.get("https://www.saucedemo.com/")
 login_page = LoginPage(browser)
 login_page.login_as("standard_user", "secret_sauce")
 home_page = HomePage(browser)
 home_page.add_products_to_cart(0)
 home_page.add_products_to_cart(1)
 home_page._open_shoping_cart()
 products = home_page._get_products_from_cart()
 assert len(products) == 2
 
 


