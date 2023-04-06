from pages.basket_page import BasketPage
from selenium.webdriver.common.by import By
import pytest
from pages.main_page  import MainPage
from pages.login_page import LoginPage
import time
link = "http://selenium1py.pythonanywhere.com/"
#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    time.sleep(7)
    page.go_to_basket_page()
    basketpage = BasketPage(browser, browser.current_url)
    assert basketpage.is_disappeared(By.CSS_SELECTOR, "a.btn.btn-lg.btn-primary.btn-block"), "Не отсутствует Перейти к оформлению"
    basketpage.havnt_book_in_basket()
    
@pytest.mark.skip(reason="no way of currently testing this")    
@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      # открываем страницу
        page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
        #login_page = page.go_to_login_page()  #иниц-ия LoginPage через Return из главной страницы
        login_page = LoginPage(browser, browser.current_url)  #иниц-ия LoginPage как отдельного класса прямым вызовом, но с неявной передачей URL
        #time.sleep(2)
        login_page.should_be_login_page()  # вызываем метод, вызывающий другие проверки
        
    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
   
   