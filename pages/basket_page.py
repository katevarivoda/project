from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):


    def check_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Empty basket message is absent"

    def check_no_items_in_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_ITEMS_SECTION), "There is an item section in the basket"
