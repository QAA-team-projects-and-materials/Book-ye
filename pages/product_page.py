from .base_page import BasePage
from .locators import ProductPageLocators
from configuration import ACTIVE_FLAG


class ProductPage(BasePage):
    def product_title_is_present(self):
        product_title_text = self.is_element_present(*ProductPageLocators.PRODUCT_TITLE).text
        assert product_title_text, "Product title text is missing"
        return product_title_text

    @staticmethod
    def check_if_opened_page_is_selected_product(product_title, product_title_product_page):
        assert product_title in product_title_product_page, 'Another product has been opened than the one selected'

    def feedback_button_is_present(self):
        feedback_button = self.is_element_present(*ProductPageLocators.FEEDBACK_BTN)
        assert feedback_button, "Feedback button is missing"
        return feedback_button

    @staticmethod
    def check_if_feedback_button_is_active(feedback_button):
        feedback_btn_class = feedback_button.get_attribute("class")
        assert ACTIVE_FLAG in feedback_btn_class, 'Feedback button (product page) is not active'

