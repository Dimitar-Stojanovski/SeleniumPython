from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.LoginPage import LoginPage 


driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
print(driver.title)

login_page = LoginPage(driver)
login_page.login_as("standard_user", "secret_sauce")
