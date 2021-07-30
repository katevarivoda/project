from selenium.webdriver.common.by import By

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.login_page import LoginPageLocators


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес

    page.open()  # открываем страницу
    page.go_to_login_page()
    page = LoginPage(browser, url = "http://selenium1py.pythonanywhere.com/ru/accounts/login/")
    page.should_be_login_page()
