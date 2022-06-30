from .base_page import BasePage
from .locators import WishlistPageLocators


class WishlistPage(BasePage):
    def product_title_text_is_present(self):
        product_title = self.browser.find_element(*WishlistPageLocators.PRODUCT_TITLE).text
        assert product_title, "\nProduct title in wishlist page is missing"
        return product_title

    @staticmethod
    def check_if_wishlist_consist_of_selected_product(product_title, product_title_product_page):
        assert product_title in product_title_product_page, "\nAnother product has been opened than the one selected"
