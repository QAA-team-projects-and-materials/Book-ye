from .base_page import BasePage
from .locators import PromotionsPageLocators


class PromotionsPage(BasePage):
    def promotions_card_is_present(self):
        promotion_card = self.browser.find_elements(*PromotionsPageLocators.PROMOTIONS_CARDS)[0]
        assert promotion_card , "\nPromotions card in promotion page is missing"
