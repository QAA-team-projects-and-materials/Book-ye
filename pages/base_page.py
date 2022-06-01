import time

from .locators import BasePageLocators
import math
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage(object):
    def __init__(self, browser: webdriver, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            element = self.browser.find_element(how, what)
        except Exception as error:
            print(f'Error: {error}')
            return False
        return element

    @staticmethod
    def wait(wait_time=5):
        return time.sleep(wait_time)

    def check_if_user_is_redirected(self, first_url):
        self.wait()
        current_url = self.browser.current_url
        print(first_url != current_url)
        assert first_url != current_url, "Redirection to page is not carried out"

    def element_is_clickable(self, how, what, wait_time=10):
        element = WebDriverWait(self.browser, wait_time).until(EC.element_to_be_clickable((how, what)))
        return element

    def element_is_visible(self, how, what, wait_time=10):
        element = WebDriverWait(self.browser, wait_time).until(EC.visibility_of_element_located((how, what)))
        return element

    def verify_header(self):
        header = self.browser.find_element(*BasePageLocators.HEADER)
        assert header, "Header is missing"

    def shopping_cart_modal_window_is_present(self):
        shopping_cart = self.is_element_present(*BasePageLocators.SHOPPING_CART_MODAL_WINDOW)
        assert shopping_cart, "Shopping cart modal window is missing"

    @staticmethod
    def check_if_selected_product_is_present_in_cart(product_title_text, product_title_shopping_cart):
        assert product_title_shopping_cart in product_title_text, \
            'Another product has been present in shopping cart than the one selected'

    def news_list_is_present(self):
        news_list = self.is_element_present(*BasePageLocators.NEWS_LIST)
        assert news_list, "News list is missing"
        return news_list

    def news_list_title_is_present(self):
        news_list_title = self.is_element_present(*BasePageLocators.NEWS_LIST_TITLE)
        assert news_list_title, "News list close button is missing"
        return news_list_title

    def close_news_list(self):
        self.wait(3)
        if self.news_list_is_present():
            news_list_title = self.news_list_title_is_present()
            ac = ActionChains(self.browser)
            ac.move_to_element(news_list_title).move_by_offset(100, 400).click().perform()
