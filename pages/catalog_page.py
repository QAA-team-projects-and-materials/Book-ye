from .base_page import BasePage
from .locators import CatalogPageLocators


class CatalogPage(BasePage):
    def side_bar_is_present(self):
        side_bar = self.browser.find_elements(*CatalogPageLocators.FILTER_SIDE_BAR)
        assert side_bar , "\nSide bar (catalog page) is missing"
        return side_bar
