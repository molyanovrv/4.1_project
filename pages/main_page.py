from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators

class MainPage(BasePage):
    def go_to_login_page(self):
        #login_link = self.browser.find_element(By.CSS_SELECTOR, "#registration_link")
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)
    
    def should_be_login_link(self):
        #self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")
        #assert self.is_element_present(By.CSS_SELECTOR, "#registration_link"), "Login link is not presented"
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

'''
    def add_to_cart(self):
        addToCart = self.browser.find_element(*MainPageLocators.ADD_TO_CART_LINK)
        addToCart.click()
        self.solve_quiz_and_get_code()
        prod_name = self.browser.find_element(By.CSS_SELECTOR, ".product_main>h1")
        prod_price = self.browser.find_element(By.CSS_SELECTOR, ".product_main>.price_color")
        print(prod_name.text+"  "+prod_price.text)
        confirm_massage = self.browser.find_element(By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success strong")
        cart_price = self.browser.find_element(By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info strong")
        print(confirm_massage.text+"  "+cart_price.text)
        assert prod_name.text == confirm_massage.text, "\n\nНе совпадает"
'''
