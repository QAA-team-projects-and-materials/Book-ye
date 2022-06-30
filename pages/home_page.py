from .base_page import BasePage
from .locators import HomePageLocators
from configuration import ACTIVE_FLAG


class HomePage(BasePage):

    def product_card_is_present(self):
        product_card = self.is_element_present(*HomePageLocators.PRODUCT_CARD)
        assert product_card, "\nProduct card is missing"
        return product_card

    def product_title_is_present(self):
        product_title = self.is_element_present(*HomePageLocators.PRODUCT_TITLE)
        assert product_title, "\nProduct title is missing"
        return product_title

    def get_product_title_text(self):
        self.product_title_is_present()
        product_title_text = self.browser.find_element(*HomePageLocators.PRODUCT_TITLE).text
        assert product_title_text, "\nProduct title text is missing"
        return product_title_text

    def go_to_product_page(self):
        product_title = self.product_title_is_present()
        product_title.click()

    # SLIDER BLOCK
    def slider_block_is_present(self):
        assert self.is_element_present(*HomePageLocators.SLIDER_BLOCK), "\nSlider block is missing"

    def right_arrow_is_present_sb(self):
        right_arrow = self.is_element_present(*HomePageLocators.RIGHT_ARROW_SB)
        assert right_arrow, "\nRight arrow (slider block) is missing"
        return right_arrow

    def left_arrow_is_present_sb(self):
        left_arrow = self.is_element_present(*HomePageLocators.LEFT_ARROW_SB)
        assert left_arrow, "\nLeft arrow (slider block) is missing"
        return left_arrow

    def find_next_pagination_point(self, NEXT_INDEX):
        pagination_point = self.browser.find_elements(*HomePageLocators.PAGINATION_POINTS)[NEXT_INDEX]
        return pagination_point

    def detailed_info_btn_is_present(self):
        detailed_info_btn = self.is_element_present(*HomePageLocators.DETAILED_INFO_BTN)
        assert detailed_info_btn, "\nDetailed info button (slider block) is missing"
        return detailed_info_btn

    def detailed_info_btn_is_visible(self):
        detailed_info_btn = self.element_is_visible(*HomePageLocators.DETAILED_INFO_BTN)
        return detailed_info_btn

    def go_to_promotions_page(self):
        detailed_info_btn = self.detailed_info_btn_is_visible()
        self.detailed_info_btn_is_present()
        detailed_info_btn.click()

    def check_if_news_has_changed(self, index):
        # Check if active next point in pagination block
        self.is_element_present(*HomePageLocators.PAGINATION_BLOCK)
        pagination_point = self.browser.find_elements(*HomePageLocators.PAGINATION_POINTS)[index]
        pagination_point_class = pagination_point.get_attribute("class")
        assert ACTIVE_FLAG in pagination_point_class, "\nPoint in pagination (slider block) is not active"

    def first_pagination_point_is_present(self):
        first_pagination_point = self.browser.find_elements(*HomePageLocators.PAGINATION_POINTS)[0]
        assert self.is_element_present(*HomePageLocators.PAGINATION_POINTS), \
            "\nFirst point in pagination (slider block) is missing"
        return first_pagination_point

    def go_to_first_pagination_point(self):
        first_pagination_point = self.first_pagination_point_is_present()
        first_pagination_point.click()
        first_pagination_point_class = first_pagination_point.get_attribute("class")
        # Check if active first point in pagination block
        assert ACTIVE_FLAG in first_pagination_point_class, "\nFirst point in pagination (slider block) is not active"
        return first_pagination_point

    # PRE ORDER BLOCK
    def pre_order_block_is_present(self):
        assert self.is_element_present(*HomePageLocators.PRE_ORDER_BLOCK), "\nPre-order block is missing"

    def right_arrow_in_pre_order_block_is_present(self):
        assert self.is_element_present(*HomePageLocators.RIGHT_ARROW_PO), \
            "\nRight arrow (pre-order block) is missing"

    def left_arrow_in_pre_order_block_is_present(self):
        assert self.is_element_present(*HomePageLocators.LEFT_ARROW_PO), \
            "\nLeft arrow (pre-order block) is missing"

    def see_all_link_in_pre_order_block_is_present(self):
        see_all_link = self.is_element_present(*HomePageLocators.SEE_ALL_LINK_PO)
        assert see_all_link, "\nLink 'Дивитись усі' (pre-order block) is missing"
        return see_all_link

    def product_feedback_link_in_pre_order_block_is_present(self):
        feedback_link = self.is_element_present(*HomePageLocators.FEEDBACK_LINK_PO)
        assert feedback_link, "\nFeedback link (pre-order block) is missing"
        return feedback_link

    def pre_order_btn_is_present(self):
        pre_order_btn = self.is_element_present(*HomePageLocators.PRE_ORDER_BTN_PO)
        assert pre_order_btn, "\nPre-order button (pre-order block) is missing"
        return pre_order_btn

    # PERSONAL FOR YOU BLOCK
    def personal_for_you_block_is_present(self):
        assert self.is_element_present(*HomePageLocators.PERSONAL_FOR_YOU_BLOCK), "\nPersonal for you block is missing"

    def right_arrow_in_personal_for_you_block_is_present(self):
        assert self.is_element_present(*HomePageLocators.RIGHT_ARROW_PFY), \
            "\nRight arrow (personal for you block) is missing"

    def left_arrow_in_personal_for_you_block_is_present(self):
        assert self.is_element_present(*HomePageLocators.LEFT_ARROW_PFY), \
            "\nLeft arrow (personal for you block) is missing"

    def get_product_title_text_in_personal_for_you_block(self):
        product_title_text = self.browser.find_element(*HomePageLocators.PRODUCT_TITLE_PFY).text
        assert product_title_text, "\nProduct title text (personal for you block) is missing"
        return product_title_text

    def order_btn_in_personal_for_you_block_is_present(self):
        order_btn = self.is_element_present(*HomePageLocators.ORDER_BTN_PFY)
        assert order_btn, "\nOrder button (personal for you block) is missing"
        return order_btn

    # NOVELTY BLOCK
    def novelty_block_is_present(self):
        assert self.is_element_present(*HomePageLocators.NOVELTY_BLOCK), "\nNovelty block is missing"

    def right_arrow_in_novelty_block_is_present(self):
        assert self.is_element_present(*HomePageLocators.RIGHT_ARROW_N), \
            "\nRight arrow (novelty block) is missing"

    def left_arrow_in_novelty_block_is_present(self):
        assert self.is_element_present(*HomePageLocators.LEFT_ARROW_N), \
            "\nLeft arrow (novelty block) is missing"

    def see_all_link_in_novelty_block_is_present(self):
        see_all_link = self.is_element_present(*HomePageLocators.SEE_ALL_LINK_N)
        assert see_all_link, "\nLink 'Дивитись усі' (novelty block) is missing"
        return see_all_link

    def product_feedback_link_in_novelty_block_is_present(self):
        feedback_link = self.is_element_present(*HomePageLocators.FEEDBACK_LINK_N)
        assert feedback_link, "\nFeedback link (novelty block) is missing"
        return feedback_link

    def get_product_title_text_in_novelty_block(self):
        product_title_text = self.browser.find_element(*HomePageLocators.PRODUCT_TITLE_N).text
        assert product_title_text, "\nProduct title text (novelty block) is missing"
        return product_title_text

    def order_btn_in_novelty_block_is_present(self):
        order_btn = self.is_element_present(*HomePageLocators.ORDER_BTN_N)
        assert order_btn, "\nOrder button (novelty block) is missing"
        return order_btn

    # TOP BLOCK
    def top_block_is_present(self):
        assert self.is_element_present(*HomePageLocators.TOP_BLOCK), "\nTop block is missing"

    def right_arrow_in_top_block_is_present(self):
        assert self.is_element_present(*HomePageLocators.RIGHT_ARROW_T), \
            "\nRight arrow (top block) is missing"

    def left_arrow_in_top_block_is_present(self):
        assert self.is_element_present(*HomePageLocators.LEFT_ARROW_T), \
            "\nLeft arrow (top block) is missing"

    def see_all_link_in_top_block_is_present(self):
        see_all_link = self.is_element_present(*HomePageLocators.SEE_ALL_LINK_T)
        assert see_all_link, "\nLink 'Дивитись усі' (top block) is missing"
        return see_all_link

    def product_feedback_link_in_top_block_is_present(self):
        feedback_link = self.is_element_present(*HomePageLocators.FEEDBACK_LINK_T)
        assert feedback_link, "\nFeedback link (top block) is missing"
        return feedback_link

    def get_product_title_text_in_top_block(self):
        product_title_text = self.browser.find_element(*HomePageLocators.PRODUCT_TITLE_T).text
        assert product_title_text, "\nProduct title text (top block) is missing"
        return product_title_text

    def order_btn_in_top_block_is_present(self):
        order_btn = self.is_element_present(*HomePageLocators.ORDER_BTN_T)
        assert order_btn, "\nOrder button (top block) is missing"
        return order_btn

    # STORE RECOMMENDED BLOCK
    def store_recommended_block_is_present(self):
        assert self.is_element_present(*HomePageLocators.STORE_RECOMMENDED_BLOCK), "\nStore recommended block is missing"

    def right_arrow_in_store_recommended_block_is_present(self):
        assert self.is_element_present(*HomePageLocators.RIGHT_ARROW_SR), \
            "\nRight arrow (store recommended block) is missing"

    def left_arrow_in_store_recommended_block_is_present(self):
        assert self.is_element_present(*HomePageLocators.LEFT_ARROW_SR), \
            "\nLeft arrow (store recommended block) is missing"

    def see_all_link_in_store_recommended_block_is_present(self):
        see_all_link = self.is_element_present(*HomePageLocators.SEE_ALL_LINK_SR)
        assert see_all_link, "\nLink 'Дивитись усі' (store recommended block) is missing"
        return see_all_link

    def product_feedback_link_in_store_recommended_block_is_present(self):
        feedback_link = self.is_element_present(*HomePageLocators.FEEDBACK_LINK_SR)
        assert feedback_link, "\nFeedback link (store recommended block) is missing"
        return feedback_link

    def get_product_title_text_in_store_recommended_block(self):
        product_title_text = self.browser.find_element(*HomePageLocators.PRODUCT_TITLE_SR).text
        assert product_title_text, "\nProduct title text (store recommended block) is missing"
        return product_title_text

    def order_btn_in_store_recommended_block_is_present(self):
        order_btn = self.is_element_present(*HomePageLocators.ORDER_BTN_SR)
        assert order_btn, "\nOrder button (store recommended block) is missing"
        return order_btn

    # BLOG BLOCK
    def blog_block_is_present(self):
        assert self.is_element_present(*HomePageLocators.BLOG_BLOCK), "\nBlog block is missing"

    def blog_link_is_present(self):
        blog_link = self.is_element_present(*HomePageLocators.BLOG_LINK)
        assert blog_link, "\nBlog link (blog block) is missing"
        return blog_link

    def go_to_blog_page(self):
        blog_link = self.blog_link_is_present()
        blog_link.click()
        return blog_link

    def go_to_blog_section(self):
        blog_section_title = self.is_element_present(*HomePageLocators.BLOG_SECTION_TITLE)
        blog_section_title_text = blog_section_title.text
        blog_section_title.click()
        return blog_section_title_text

    def go_to_blog_topic_via_picture(self):
        blog_topic_image = self.is_element_present(*HomePageLocators.BLOG_TOPIC_IMAGE)
        blog_topic_image_title = blog_topic_image.get_attribute("title")
        blog_topic_image.click()
        return blog_topic_image_title

    def go_to_blog_topic_via_title(self):
        blog_topic_title = self.is_element_present(*HomePageLocators.BLOG_TOPIC_TITLE)
        blog_topic_title_text = blog_topic_title.text
        blog_topic_title.click()
        return blog_topic_title_text

    # INFO ABOUT STORE BLOCK
    def store_advantages_block_is_present(self):
        assert self.is_element_present(*HomePageLocators.STORE_ADVANTAGES_BLOCK), "\nStore advantages block is missing"

    def info_about_store_block_is_present(self):
        info_about_store = self.is_element_present(*HomePageLocators.INFO_ABOUT_STORE_BLOCK)
        assert info_about_store, "\nInfo about store block is missing"
        return info_about_store

    def full_info_about_store_btn_is_present(self):
        open_full_info_about_store_btn = self.is_element_present(*HomePageLocators.FULL_INFO_ABOUT_STORE_BTN)
        assert open_full_info_about_store_btn, "\nOpen full info about store 'v' is missing"
        return open_full_info_about_store_btn

    def check_if_full_info_about_store_has_opened(self):
        info_about_store = self.info_about_store_block_is_present()
        info_about_store_class = info_about_store.get_attribute("class")
        assert ACTIVE_FLAG in info_about_store_class, '\nFull info about store (info about store block) is not open'

    # BOOK LOVERS CLUB BLOCK
    def book_lovers_club_block_is_present(self):
        book_lovers_club = self.is_element_present(*HomePageLocators.BOOK_LOVERS_CLUB_BLOCK)
        assert book_lovers_club, "\nBook lovers club block is missing"
        return book_lovers_club

    def go_to_book_lovers_page(self):
        book_lovers_club = self.book_lovers_club_block_is_present()
        book_lovers_club.click()

    # MOST POPULAR QUERIES
    def most_popular_queries_block_is_present(self):
        assert self.is_element_present(*HomePageLocators.MOST_POPULAR_QUERIES_BLOCK), \
            '\nMost popular queries block is missing'

    def popular_query_is_present(self):
        popular_query = self.is_element_present(*HomePageLocators.POPULAR_QUERY)
        assert popular_query, '\nPopular query is missing'
        return popular_query

    def go_to_one_of_popular_queries(self):
        popular_query = self.popular_query_is_present()
        popular_query.click()


