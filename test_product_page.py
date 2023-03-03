from pages.main_page  import MainPage
from pages.product_page import ProductPage
from selenium.webdriver.common.by import By
#from pages.login_page import LoginPage
import time
import pytest
#link = "http://selenium1py.pythonanywhere.com/"
#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.mark.xfail(reason="fixing this bug right now")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                         # открываем страницу
    page.add_to_cart()                  # кладем в корзину
    #page.prod_name_confirmed()
    #page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)
    result = page.is_not_element_present(By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success strong")
    assert result, "элемент найден, а тест на отсутствие"

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                         # открываем страницу
    result = page.is_not_element_present(By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success strong")
    assert result, "элемент найден, а ожидаем отсутствие"

@pytest.mark.xfail(reason="fixing this bug right now")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                         # открываем страницу
    page.add_to_cart()                  # кладем в корзину
    result = page.is_disappeared(By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success strong")
    assert result, "элемент найден, а тест на отсутствие"
       
def te_st_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                         # открываем страницу
    page.add_to_cart()                  # кладем в корзину
    page.prod_name_confirmed()
    page.prod_price_confirmed()
    #page.go_to_login_page()            # выполняем метод страницы — переходим на страницу логина
    #login_page = page.go_to_login_page()  #иниц-ия LoginPage через Return из главной страницы
    #login_page = LoginPage(browser, browser.current_url)  #иниц-ия LoginPage как отдельного класса прямым вызовом, но с неявной передачей URL
    #time.sleep(2)
    #login_page.should_be_login_page()  # вызываем метод, вызывающий другие проверки
    