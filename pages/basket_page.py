from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):

    # def is_not_basket_element_present(self, how, what, timeout=4):
    #     try:
    #         WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
    #         result = False
    #     except TimeoutException:
    #         result = True

    def check_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Empty basket message is absent"

    def check_no_items_in_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_ITEMS_SECTION), "There is an item section in the basket"
