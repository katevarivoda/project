from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET = (By.XPATH, "//a[contains(text(),'View basket')]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL = (By.NAME, "registration-email")
    PASSWORD = (By.NAME, "registration-password1")
    CONFIRM_PASSWORD = (By.NAME, "registration-password2")
    REGISTER_BTN = (By.NAME, "registration_submit")


class ProductPageLocators:
    ADD_BUTTON = (By.XPATH, "//button[contains(text(),'Add to basket')]")
    BOOK_NAME_ADDED_TO_CART = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    BOOK_NAME = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
    BOOK_PRICE = (By.XPATH, "//div[@class='col-sm-6 product_main']/p[@class='price_color']")
    PRICE_ADDED_TO_CART = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) > .alertinner")


class BasketPageLocators:
    EMPTY_BASKET_MESSAGE = (By.XPATH, "//div[@id='content_inner']")
    BASKET_ITEMS_SECTION = (By.CSS_SELECTOR, ".basket-items")
