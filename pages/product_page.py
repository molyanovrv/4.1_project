from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_cart(self):
        addToCart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_LINK)
        addToCart.click()
        #self.solve_quiz_and_get_code()
        #self.prod_name_confirmed()
        #self.prod_price_confirmed()
        
    def prod_name_confirmed(self):
        prod_name = self.browser.find_element(By.CSS_SELECTOR, ".product_main>h1").text
        #confirm_message = self.browser.find_element(By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success strong")
        confirm_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        print("prod_name_confirmed done")
        assert prod_name == confirm_message, "В подтверждении нет названия продукта"
        
    def prod_price_confirmed(self):
        prod_price = self.browser.find_element(By.CSS_SELECTOR, ".product_main>.price_color")
        cart_price = self.browser.find_element(By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info strong")
        print("prod_price_confirmed done")
        assert prod_price.text == cart_price.text, "В корзине цена отличается"

    # элемента нет (упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый)
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

