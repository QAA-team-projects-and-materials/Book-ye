from .base_page import BasePage
from .locators import BlogPageLocators


class BlogPage(BasePage):
    def blog_menu_is_present(self):
        blog_menu = self.browser.find_element(*BlogPageLocators.BLOG_MENU)
        assert blog_menu , "Blog menu (blog page) is missing"
        return blog_menu

    def check_if_user_is_redirected_to_blog_page(self):
        current_url = self.browser.current_url
        assert "blog" in current_url, "Redirection to blog page is not carried out"

    def check_if_user_is_redirected_to_blog_section(self, blog_section_title):
        section_title = self.is_element_present(*BlogPageLocators.TITLE_IN_SEARCH_TREE).text
        section_title_upper_case = section_title.upper()
        assert blog_section_title in section_title_upper_case, "Redirection to blog section page is not carried out"

    def check_if_user_is_redirected_to_blog_topic(self, blog_topic_title):
        topic_title_in_search_tree = self.is_element_present(*BlogPageLocators.TITLE_IN_SEARCH_TREE).text
        assert blog_topic_title in topic_title_in_search_tree, "Redirection to blog topic page is not carried out"
