from .base_page import BasePage
from .locators  import LoginPageLocators
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
    def havnt_book_in_basket(self):
        self.is_disappeared(*BasketPageLocators.PROCEED_TO_CHECKOUT), "Не отсутствует Перейти к оформлению"
        text = "Your basket is empty. Continue shopping"
        result = self.is_element_with_text_present(*BasketPageLocators.EMPTY_TEXT,text)
        return result
    
    def have_empty_message(self):
        assert result, "элемент не найден"
    
    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        #assert True
        #assert driver.current_url.find(LOGIN_URL_STRING), "login is not find in URL"
        assert "login" in self.browser.current_url, "login is not find in URL"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Login form is not presented"

    def should_not_see_success_message(self):
        assert page.is_not_element_present(*BasketPageLocators.SUCCESS_MESSAGE)