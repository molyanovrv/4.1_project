from .base_page import BasePage
from .locators  import LoginPageLocators
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
    def havnt_book_in_basket(self):
        #result = self.is_element_present(By.CSS_SELECTOR, ".content>#content_inner>p")
        #result = self.browser.find_element(By.CSS_SELECTOR, ".content>#content_inner>p").text
        text = "Your basket is empty. Continue shopping"
        result = self.is_element_with_text_present(By.CSS_SELECTOR, ".content>#content_inner>p",text)
        #print(result + "\nhavnt_book_in_basket") 
        assert result , f'Элемент не найден:{text}'
    
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
