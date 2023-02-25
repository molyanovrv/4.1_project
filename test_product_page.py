from pages.main_page  import MainPage
from pages.product_page import ProductPage
#from pages.login_page import LoginPage
import time
#link = "http://selenium1py.pythonanywhere.com/"
#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.add_to_cart()               # кладем в корзину
    #page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    ##login_page = page.go_to_login_page()  #иниц-ия LoginPage через Return из главной страницы
    #login_page = LoginPage(browser, browser.current_url)  #иниц-ия LoginPage как отдельного класса прямым вызовом, но с неявной передачей URL
    #time.sleep(2)
    #login_page.should_be_login_page()  # вызываем метод, вызывающий другие проверки
    