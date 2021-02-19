from pages.base_page import BasePage
from pages.locators import MainPageLocators, ProductPageLocators

class ProductPage(BasePage):
    def pick_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        link.click()
        return