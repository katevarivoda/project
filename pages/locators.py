from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_BUTTON = (By.XPATH, "//button[contains(text(),'Add to basket')]")
    BOOK_NAME_ADDED_TO_CART = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    BOOK_NAME = (By.TAG_NAME, "h1")
    VIEW_BASKET = (By.XPATH, "//a[contains(text(),'View basket')]")
    BOOK_PRICE = (By.XPATH, "//p[@class='price_color']")
    PRICE_ADDED_TO_CART = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
