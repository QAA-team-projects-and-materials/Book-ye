from selenium.webdriver.common.action_chains import ActionChains

from .base_page import BasePage
from .locators import ProductPageLocators
from configuration import ACTIVE_FLAG


class ProductPage(BasePage):
    def product_title_text_is_present(self):
        product_title_text = self.is_element_present(*ProductPageLocators.PRODUCT_TITLE).text
        assert product_title_text, "\nProduct title text is missing"
        return product_title_text

    @staticmethod
    def check_if_opened_page_is_selected_product(product_title, product_title_product_page):
        assert product_title in product_title_product_page, '\nAnother product has been opened than the one selected'

    def feedback_button_is_present(self):
        feedback_button = self.is_element_present(*ProductPageLocators.FEEDBACK_BTN)
        assert feedback_button, "\nFeedback button is missing"
        return feedback_button

    @staticmethod
    def check_if_feedback_button_is_active(feedback_button):
        feedback_btn_class = feedback_button.get_attribute("class")
        assert ACTIVE_FLAG in feedback_btn_class, '\nFeedback button (product page) is not active'

    def buy_button_is_present(self):
        buy_button = self.is_element_present(*ProductPageLocators.BUY_BTN)
        assert buy_button, "\nBuy button is missing"
        return buy_button

    def add_product_to_wishlist_link_is_present(self):
        add_product_to_wishlist_link = self.is_element_present(*ProductPageLocators.ADD_PRODUCT_TO_WISHLIST_LINK)
        assert add_product_to_wishlist_link, "\nAdd product to wishlist link is missing"
        return add_product_to_wishlist_link

    def read_the_passage_link_is_present(self):
        read_the_passage_link = self.is_element_present(*ProductPageLocators.READ_THE_PASSAGE_LINK)
        assert read_the_passage_link, "\nRead the passage link is missing"
        return read_the_passage_link

    def read_the_passage_modal_window_is_visible(self):
        read_the_passage_modal_window = self.element_is_visible(*ProductPageLocators.READ_THE_PASSAGE_MODAL_WINDOW)
        assert read_the_passage_modal_window, "\nRead the passage modal window is missing"
        return read_the_passage_modal_window

    def shop_addresses_link_is_present(self):
        shop_addresses_link = self.is_element_present(*ProductPageLocators.SHOP_ADDRESSES_LINK)
        assert shop_addresses_link, "\nRead the passage link is missing"
        return shop_addresses_link

    def go_to_contacts_page(self):
        shop_addresses_link = self.shop_addresses_link_is_present()
        shop_addresses_link.click()

    def delivery_text_is_present(self):
        delivery_text = self.is_element_present(*ProductPageLocators.DELIVERY_TEXT)
        assert delivery_text, "\nDelivery text is missing"
        return delivery_text

    def open_info_about_delivery(self):
        delivery_text = self.delivery_text_is_present()
        ac = ActionChains(self.browser)
        ac.move_to_element(delivery_text).perform()

    def info_about_delivery_is_visible(self):
        info_about_delivery = self.element_is_visible(*ProductPageLocators.INFO_ABOUT_DELIVERY)
        assert info_about_delivery, "\nInfo about delivery is missing"

    def payment_text_is_present(self):
        payment_text = self.is_element_present(*ProductPageLocators.PAYMENT_TEXT)
        assert payment_text, "\nPayment text is missing"
        return payment_text

    def open_info_about_payment(self):
        payment_text = self.payment_text_is_present()
        ac = ActionChains(self.browser)
        ac.move_to_element(payment_text).perform()

    def info_about_payment_is_visible(self):
        info_about_payment = self.element_is_visible(*ProductPageLocators.INFO_ABOUT_PAYMENT)
        assert info_about_payment, "\nInfo about payment is missing"
