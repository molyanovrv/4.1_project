from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    #ADD_TO_CART_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")
    #LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_URL_STRING = "login"

class ProductPageLocators():
    ADD_TO_CART_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE  = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success strong")
