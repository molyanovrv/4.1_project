from pages.main_page import MainPage
link = "http://selenium1py.pythonanywhere.com/"
#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    
def go_to_login_page(browser):
    #login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    #login_link = browser.find_element(By.CSS_SELECTOR, "#registration_link")
    login_link = browser.find_element(*MainPageLocators.LOGIN_LINK)
    login_link.click()    
    
def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()