from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def adding_to_cart(self):
        self.should_add_to_cart()
        # self.should_be_success_message()

    def should_add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_to_cart_button.click()

    def go_to_basket(self):
        view_basket_button = self.browser.find_element(*ProductPageLocators.VIEW_BASKET)
        view_basket_button.click()

    def book_name_is_correct(self):
        book_name_success_message = (self.browser.find_element(*ProductPageLocators.BOOK_NAME_ADDED_TO_CART)).text
        book_name = (self.browser.find_element(*ProductPageLocators.BOOK_NAME)).text
        assert book_name_success_message == book_name

    def book_price_is_correct(self):
        book_price_success_message = (self.browser.find_element(*ProductPageLocators.PRICE_ADDED_TO_CART)).text
        book_price = (self.browser.find_element(*ProductPageLocators.BOOK_PRICE)).text
        assert book_price_success_message == book_price
