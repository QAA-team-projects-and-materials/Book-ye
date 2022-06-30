from .base_page import BasePage
from .locators import BookLoversClubPageLocators


class BookLoversClubPage(BasePage):
    def topic_list_is_present(self):
        topic_list = self.browser.find_element(*BookLoversClubPageLocators.TOPIC_LIST)
        assert topic_list , "\nTopic list (book lovers club) is missing"
        return topic_list
