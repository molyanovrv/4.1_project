from pages.locators import LoginPageLocators
from pages.locators import ProductPageLocators
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
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

@pytest.mark.skip(reason="no way of currently testing this")
@pytest.mark.xfail(reason="fixing this bug right now")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                         # открываем страницу
    page.add_to_cart()                  # кладем в корзину
    #page.prod_name_confirmed()
    #page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)
    result = page.is_not_element_present(By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success strong")
    assert result, "элемент найден, а тест на отсутствие"

@pytest.mark.skip(reason="no way of currently testing this")
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                         # открываем страницу
    result = page.is_not_element_present(By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success strong")
    assert result, "элемент найден, а ожидаем отсутствие"

@pytest.mark.skip(reason="no way of currently testing this")
@pytest.mark.xfail(reason="fixing this bug right now")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                         # открываем страницу
    page.add_to_cart()                  # кладем в корзину
    result = page.is_disappeared(By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success strong")
    assert result, "элемент найден, а тест на отсутствие"
       
#@pytest.mark.skip(reason="no way of currently testing this")
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                         # открываем страницу
    page.add_to_cart()                  # кладем в корзину
    page.prod_name_confirmed()
    page.prod_price_confirmed()
    
@pytest.mark.skip(reason="no way of currently testing this")
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    
@pytest.mark.skip(reason="no way of currently testing this")
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    
@pytest.mark.skip(reason="no way of currently testing this")
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = ProductPage(browser, link)
    page.open()
    time.sleep(7)
    page.go_to_basket_page()
    basketpage = BasketPage(browser, browser.current_url)
    assert basketpage.is_disappeared(By.CSS_SELECTOR, "a.btn.btn-lg.btn-primary.btn-block"), "Не отсутствует Перейти к оформлению"
    assert basketpage.havnt_book_in_basket()
    
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        #открыть страницу регистрации;
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        #зарегистрировать нового пользователя;
        email = str(time.time()) + "@fakemail.org"
        password = "I6vvc$_hcxe98,,"
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(email, password)
        #проверить, что пользователь залогинен
        result = page.is_element_present(*LoginPageLocators.USER_ICON)
        assert result, "элемент USER_ICON не найден, пользователь не залогинен"
        
    @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.need_review
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                         # открываем страницу
        result = page.is_not_element_present(By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success strong")
        assert result, "элемент найден, а ожидаем отсутствие"

    @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        time.sleep(4)
        print("---===  я вошел  ===---")
        page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                         # открываем страницу
        page.add_to_cart()                  # кладем в корзину
        #addToCart = browser.find_element(*ProductPageLocators.ADD_TO_CART_LINK)
        #addToCart.click()
        #self.solve_quiz_and_get_code()
        time.sleep(4)
        #page.prod_name_confirmed()
        #page.prod_price_confirmed()
