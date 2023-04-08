from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators  import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

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

    def register_new_user(self, email, password):
        #Реализуйте его, описав соответствующие элементы страницы.
        self.browser.find_element(By.CSS_SELECTOR, "#id_registration-email").send_keys(email)
        self.browser.find_element(By.CSS_SELECTOR, "#id_registration-password1").send_keys(password)
        self.browser.find_element(By.CSS_SELECTOR, "#id_registration-password2").send_keys(password)
        self.browser.find_element(By.XPATH, "//button[@name='registration_submit']").click()
        
    def user_logined(self):
        result = self.is_element_present(*LoginPageLocators.USER_ICON)
        assert result, "элемент USER_ICON не найден, пользователь не залогинен"
    