from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def adding_to_cart(self):
        self.should_add_to_cart()
        # self.should_be_success_message()

    def should_add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_to_cart_button.click()


    def book_name_is_correct(self):
        book_name_success_message = (self.browser.find_element(*ProductPageLocators.BOOK_NAME_ADDED_TO_CART)).text
        book_name = (self.browser.find_element(*ProductPageLocators.BOOK_NAME)).text
        assert book_name_success_message == book_name, "Book title and message book title are different"

    def book_price_is_correct(self):
        book_price_success_message = (
            self.browser.find_element(*ProductPageLocators.PRICE_ADDED_TO_CART)).get_attribute("innerText")
        book_price = (self.browser.find_element(*ProductPageLocators.BOOK_PRICE)).text
        assert book_price_success_message == book_price, "Book price and basket price are different"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is still present"
