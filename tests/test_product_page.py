import pytest

from configuration import PRODUCT_PAGE_LINK
from pages.product_page import ProductPage
from pages.wishlist_page import WishlistPage
from pages.contacts_page import ContactsPage


@pytest.fixture(scope="function")
def page(browser):
    page = ProductPage(browser, PRODUCT_PAGE_LINK)
    page.open()
    page.close_news_list()
    yield page


class TestProduct:
    def test_the_user_can_buy_the_book(self, page):
        product_title_text = page.product_title_text_is_present()
        buy_button = page.buy_button_is_present()
        buy_button.click()
        page.shopping_cart_modal_window_is_visible()
        product_title_shopping_cart = page.product_title_shopping_cart_is_present()
        page.check_if_selected_product_is_present_in_cart(product_title_text, product_title_shopping_cart)

    def test_the_user_can_add_the_book_to_the_wishlist(self, browser, page):
        product_title_text_product_page = page.product_title_text_is_present()
        page.log_in()
        add_product_to_wishlist_link = page.add_product_to_wishlist_link_is_present()
        add_product_to_wishlist_link.click()
        page.go_to_wishlist_page()
        wishlist_page = WishlistPage(browser, browser.current_url)
        product_title_text_wishlist_page = wishlist_page.product_title_text_is_present()
        wishlist_page.check_if_wishlist_consist_of_selected_product(product_title_text_wishlist_page,
                                                                    product_title_text_product_page)

    def test_the_user_can_read_the_passage(self, page):
        read_the_passage_link = page.read_the_passage_link_is_present()
        read_the_passage_link.click()
        page.read_the_passage_modal_window_is_visible()

    def test_the_user_can_go_to_page_with_shop_addresses(self, browser, page):
        page.go_to_contacts_page()
        contacts_page = ContactsPage(browser, browser.current_url)
        contacts_page.check_if_user_is_redirected_to_contacts_page()

    def test_the_user_can_see_information_about_delivery(self, page):
        page.open_info_about_delivery()
        page.info_about_delivery_is_visible()

    def test_the_user_can_see_information_about_payment(self, page):
        page.open_info_about_payment()
        page.info_about_payment_is_visible()
