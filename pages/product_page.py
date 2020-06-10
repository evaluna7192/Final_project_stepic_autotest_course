from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "Basket button is not present"
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def should_add_correct_product_to_basket(self):
        self.should_be_correct_product_name()
        self.should_be_correct_product_price()

    def should_be_correct_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        basket_product_name = self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_NAME).text
        assert product_name == basket_product_name, "Added product has incorrect name"

    def should_be_correct_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_product_price = self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_PRICE).text
        assert product_price == basket_product_price, "Added product has incorrect price"

