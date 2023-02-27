from pages.main_page  import MainPage
from pages.product_page import ProductPage
#from pages.login_page import LoginPage
import time
import pytest
#link = "http://selenium1py.pythonanywhere.com/"
#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
                                  
def test_guest_can_add_product_to_basket(browser, link):
    #link = {link}
    print(link)
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.add_to_cart()               # кладем в корзину
    #page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    ##login_page = page.go_to_login_page()  #иниц-ия LoginPage через Return из главной страницы
    #login_page = LoginPage(browser, browser.current_url)  #иниц-ия LoginPage как отдельного класса прямым вызовом, но с неявной передачей URL
    #time.sleep(2)
    #login_page.should_be_login_page()  # вызываем метод, вызывающий другие проверки
    