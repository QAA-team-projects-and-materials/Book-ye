import pytest

from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.promotions_page import PromotionsPage
from pages.catalog_page import CatalogPage
from pages.blog_page import BlogPage
from pages.book_lovers_club_page import BookLoversClubPage
from configuration import HOME_PAGE_LINK, NEXT_INDEX, PREVIOUS_INDEX


@pytest.fixture(scope="function")
def page(browser):
    page = HomePage(browser, HOME_PAGE_LINK)
    page.open()
    page.close_news_list()
    yield page


class TestHomePage:
    def test_user_can_open_product_page(self, browser, page):
        product_title = page.go_to_product_page()
        product_page = ProductPage(browser, browser.current_url)
        product_title_product_page = product_page.product_title_is_present()
        product_page.check_if_user_is_redirected(page.url)
        product_page.check_if_opened_page_is_selected_product(product_title, product_title_product_page)


class TestSliderBlock:
    def test_find_slider_block(self, page):
        page.slider_block_is_present()

    def test_change_news_via_arrows_slider_block(self, page):
        page.go_to_first_pagination_point()
        right_arrow = page.right_arrow_is_present_sb()
        right_arrow.click()
        page.check_if_news_has_changed(NEXT_INDEX)

        page.go_to_first_pagination_point()
        left_arrow = page.left_arrow_is_present_sb()
        left_arrow.click()
        page.check_if_news_has_changed(PREVIOUS_INDEX)

    def test_change_news_via_slider_pagination_slider_block(self, page):
        page.go_to_first_pagination_point()
        next_pagination_point = page.find_next_pagination_point(NEXT_INDEX)
        next_pagination_point.click()
        page.check_if_news_has_changed(NEXT_INDEX)

    def test_open_detailed_info_about_news_slider_block(self, browser, page):
        page.go_to_first_pagination_point()
        page.go_to_promotions_page()
        promotions_page = PromotionsPage(browser, browser.current_url)
        promotions_page.check_if_user_is_redirected(page.url)


class TestPreOrderBlock:
    def test_find_pre_order_block(self, page):
        page.pre_order_block_is_present()

    def test_find_arrows_in_pre_order_block(self, page):
        page.right_arrow_in_pre_order_block_is_present()
        page.left_arrow_in_pre_order_block_is_present()

    def test_user_is_redirected_to_page_with_all_products_in_pre_order_block(self, browser, page):
        see_all_link = page.see_all_link_in_pre_order_block_is_present()
        see_all_link.click()
        catalog_page = CatalogPage(browser, browser.current_url)
        catalog_page.check_if_user_is_redirected(page.url)

    def test_user_can_open_feedback_about_product_pre_order_block(self, browser, page):
        feedback_link = page.product_feedback_link_in_pre_order_block_is_present()
        feedback_link.click()
        product_page = ProductPage(browser, browser.current_url)
        product_page.check_if_user_is_redirected(page.url)
        feedback_button = product_page.feedback_button_is_present()
        product_page.check_if_feedback_button_is_active(feedback_button)

    def test_user_can_pre_order_product(self, page):
        product_title_text = page.get_product_title_text()
        pre_order_btn = page.pre_order_btn_is_present()
        pre_order_btn.click()
        page.shopping_cart_modal_window_is_present()
        product_title_shopping_cart = page.product_title_shopping_cart_is_present()
        page.check_if_selected_product_is_present_in_cart(product_title_text, product_title_shopping_cart)


class TestPersonalForYou:
    def test_find_personal_for_you_block(self, page):
        page.personal_for_you_block_is_present()

    def test_find_arrows_in_personal_for_you_block(self, page):
        page.right_arrow_in_personal_for_you_block_is_present()
        page.left_arrow_in_personal_for_you_block_is_present()

    def test_user_can_order_product_personal_for_you_block(self, page):
        product_title_text = page.get_product_title_text_in_personal_for_you_block()
        order_btn = page.order_btn_in_personal_for_you_block_is_present()
        order_btn.click()
        page.shopping_cart_modal_window_is_present()
        product_title_shopping_cart = page.product_title_shopping_cart_is_present()
        page.check_if_selected_product_is_present_in_cart(product_title_text, product_title_shopping_cart)


class TestNovelty:
    def test_find_novelty_block(self, page):
        page.novelty_block_is_present()

    def test_find_arrows_in_novelty_block(self, page):
        page.right_arrow_in_novelty_block_is_present()
        page.left_arrow_in_novelty_block_is_present()

    def test_user_is_redirected_to_page_with_all_products_in_novelty_block(self, browser, page):
        see_all_link = page.see_all_link_in_novelty_block_is_present()
        see_all_link.click()
        catalog_page = CatalogPage(browser, browser.current_url)
        catalog_page.check_if_user_is_redirected(page.url)

    def test_user_can_open_feedback_about_product_novelty_block(self, browser, page):
        feedback_link = page.product_feedback_link_in_novelty_block_is_present()
        feedback_link.click()
        product_page = ProductPage(browser, browser.current_url)
        product_page.check_if_user_is_redirected(page.url)
        feedback_button = product_page.feedback_button_is_present()
        product_page.check_if_feedback_button_is_active(feedback_button)

    def test_user_can_order_product_novelty_block(self, page):
        product_title_text = page.get_product_title_text_in_novelty_block()
        order_btn = page.order_btn_in_novelty_block_is_present()
        order_btn.click()
        page.shopping_cart_modal_window_is_present()
        product_title_shopping_cart = page.product_title_shopping_cart_is_present()
        page.check_if_selected_product_is_present_in_cart(product_title_text, product_title_shopping_cart)


class TestTop:
    def test_find_top_block(self, page):
        page.top_block_is_present()

    def test_find_arrows_in_top_block(self, page):
        page.right_arrow_in_top_block_is_present()
        page.left_arrow_in_top_block_is_present()

    def test_user_is_redirected_to_page_with_all_products_in_top_block(self, browser, page):
        see_all_link = page.see_all_link_in_top_block_is_present()
        see_all_link.click()
        catalog_page = CatalogPage(browser, browser.current_url)
        catalog_page.check_if_user_is_redirected(page.url)

    def test_user_can_open_feedback_about_product_top_block(self, browser, page):
        feedback_link = page.product_feedback_link_in_top_block_is_present()
        feedback_link.click()
        product_page = ProductPage(browser, browser.current_url)
        product_page.check_if_user_is_redirected(page.url)
        feedback_button = product_page.feedback_button_is_present()
        product_page.check_if_feedback_button_is_active(feedback_button)

    def test_user_can_order_product_top_block(self, page):
        product_title_text = page.get_product_title_text_in_top_block()
        order_btn = page.order_btn_in_top_block_is_present()
        order_btn.click()
        page.shopping_cart_modal_window_is_present()
        product_title_shopping_cart = page.product_title_shopping_cart_is_present()
        page.check_if_selected_product_is_present_in_cart(product_title_text, product_title_shopping_cart)


class TestStoreRecommended:
    def test_find_store_recommended_block(self, page):
        page.store_recommended_block_is_present()

    def test_find_arrows_in_store_recommended_block(self, page):
        page.right_arrow_in_store_recommended_block_is_present()
        page.left_arrow_in_store_recommended_block_is_present()

    def test_user_is_redirected_to_page_with_all_products_in_store_recommended_block(self, browser, page):
        see_all_link = page.see_all_link_in_store_recommended_block_is_present()
        see_all_link.click()
        catalog_page = CatalogPage(browser, browser.current_url)
        catalog_page.check_if_user_is_redirected(page.url)

    def test_user_can_open_feedback_about_product_store_recommended_block(self, browser, page):
        feedback_link = page.product_feedback_link_in_store_recommended_block_is_present()
        feedback_link.click()
        product_page = ProductPage(browser, browser.current_url)
        product_page.check_if_user_is_redirected(page.url)
        feedback_button = product_page.feedback_button_is_present()
        product_page.check_if_feedback_button_is_active(feedback_button)

    def test_user_can_order_product_store_recommended_block(self, page):
        product_title_text = page.get_product_title_text_in_store_recommended_block()
        order_btn = page.order_btn_in_store_recommended_block_is_present()
        order_btn.click()
        page.shopping_cart_modal_window_is_present()
        product_title_shopping_cart = page.product_title_shopping_cart_is_present()
        page.check_if_selected_product_is_present_in_cart(product_title_text, product_title_shopping_cart)


class TestBlog:
    def test_find_blog_block(self, page):
        page.blog_block_is_present()

    def test_user_can_open_blog_page(self, browser, page):
        page.go_to_blog_page()
        blog_page = BlogPage(browser, browser.current_url)
        blog_page.check_if_user_is_redirected_to_blog_page()

    def test_user_can_open_blog_section(self, browser, page):
        blog_section_title = page.go_to_blog_section()
        blog_page = BlogPage(browser, browser.current_url)
        blog_page.check_if_user_is_redirected_to_blog_section(blog_section_title)

    def test_user_can_open_blog_topic_via_picture(self, browser, page):
        blog_topic_image_title = page.go_to_blog_topic_via_picture()
        blog_page = BlogPage(browser, browser.current_url)
        blog_page.check_if_user_is_redirected_to_blog_topic(blog_topic_image_title)

    def test_user_can_open_blog_topic_via_title(self, browser, page):
        blog_topic_title = page.go_to_blog_topic_via_title()
        blog_page = BlogPage(browser, browser.current_url)
        blog_page.check_if_user_is_redirected_to_blog_topic(blog_topic_title)


class TestInfoAboutStore:
    def test_find_store_advantages_block(self, page):
        page.store_advantages_block_is_present()

    def test_find_info_about_store_block(self, page):
        page.info_about_store_block_is_present()

    def test_user_can_open_full_info_about_store(self, page):
        open_full_info_about_store_btn = page.full_info_about_store_btn_is_present()
        open_full_info_about_store_btn.click()
        page.check_if_full_info_about_store_has_opened()


class TestBookLoversClub:
    def test_user_can_open_book_lovers_club_page(self,browser, page):
        page.go_to_book_lovers_page()
        book_lovers_club_page = BookLoversClubPage(browser, browser.current_url)
        book_lovers_club_page.check_if_user_is_redirected(page.url)


class TestMostPopularQueries:
    def test_find_most_popular_queries_block(self, page):
        page.most_popular_queries_block_is_present()

    def test_user_can_open_page_with_popular_query(self, page):
        page.go_to_one_of_popular_queries()
        page.check_if_user_is_redirected(page.url)

