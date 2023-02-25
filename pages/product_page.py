from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_cart(self):
        addToCart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_LINK)
        addToCart.click()
        self.solve_quiz_and_get_code()
        prod_name = self.browser.find_element(By.CSS_SELECTOR, ".product_main>h1")
        prod_price = self.browser.find_element(By.CSS_SELECTOR, ".product_main>.price_color")
        print(prod_name.text+"  "+prod_price.text)
        confirm_massage = self.browser.find_element(By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success strong")
        cart_price = self.browser.find_element(By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info strong")
        print(confirm_massage.text+"  "+cart_price.text)
        assert prod_name.text == confirm_massage.text, "\n\nНе совпадает"

