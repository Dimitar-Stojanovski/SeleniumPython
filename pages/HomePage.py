from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

ADD_TO_CART_BUTTON = (By.XPATH, "//*[text()='Add to cart']")
SHOPPING_CART = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
PRODUCTS_IN_CART = (By.CSS_SELECTOR, "[data-test*='remove']")

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def add_products_to_cart(self, index):
       elements = self._wait_for_elements(ADD_TO_CART_BUTTON)
       elements[index].click()

    def _open_shoping_cart(self):
        self._clickOn(SHOPPING_CART)

    def _get_products_from_cart(self):
        return self._wait_for_elements(PRODUCTS_IN_CART)
