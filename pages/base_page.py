import time

from configuration import REGISTRATION_NAME, REGISTRATION_EMAIL, REGISTRATION_PHONE_NUMBER, REGISTRATION_PASSWORD,\
    REGISTRATION_PHONE_NUMBER_ALREADY_EXIST_MESSAGE, LOG_IN_EMAIL, LOG_IN_PASSWORD, LOG_IN_GREETING,\
    LOG_IN_INVALID_MESSAGE
from .locators import BasePageLocators, AuthorizationModalWindowLocators
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
            print(f'Error with {what} element: {error}')
            return False
        return element

    def check_if_user_is_redirected(self, first_url):
        current_url = self.browser.current_url
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

    def shopping_cart_modal_window_is_visible(self):
        shopping_cart = self.element_is_visible(*BasePageLocators.SHOPPING_CART_MODAL_WINDOW)
        assert shopping_cart, "Shopping cart modal window is missing"

    @staticmethod
    def check_if_selected_product_is_present_in_cart(product_title_text, product_title_shopping_cart):
        assert product_title_shopping_cart in product_title_text, \
            'Another product has been present in shopping cart than the one selected'

    def news_window_title_is_visible(self):
        news_window_title = self.element_is_visible(*BasePageLocators.NEWS_WINDOW_TITLE)
        assert news_window_title, "News list is not visible"
        return news_window_title

    def news_window_is_present(self):
        news_window = self.is_element_present(*BasePageLocators.NEWS_WINDOW)
        assert news_window, "News list is missing"
        return news_window

    def close_news_list(self):
        if self.news_window_is_present():
            news_window_title = self.news_window_title_is_visible()
            ac = ActionChains(self.browser)
            ac.move_to_element(news_window_title).move_by_offset(100, 400).click().perform()

    def check_if_user_is_redirected_to_terms_of_use_page(self):
        current_url = self.browser.current_url
        assert "terms_of_use" in current_url, "Redirection to terms of use page is not carried out"

    # AUTHORIZATION MODAL WINDOW
    def authorization_button_is_present(self):
        authorization_btn = self.is_element_present(*BasePageLocators.AUTHORIZATION_BTN)
        assert authorization_btn, "Authorization button is missing"
        return authorization_btn

    def open_authorization_modal_window(self):
        authorization_btn = self.authorization_button_is_present()
        authorization_btn.click()

    def registration_link_is_present(self):
        registration_link = self.is_element_present(*AuthorizationModalWindowLocators.REGISTRATION_LINK)
        assert registration_link, "Registration link is missing"
        return registration_link

    def go_to_registration_form(self):
        registration_link = self.registration_link_is_present()
        registration_link.click()

    def terms_of_use_link_is_present(self):
        terms_of_use_link = self.is_element_present(*AuthorizationModalWindowLocators.TERMS_OF_USE_LINK)
        assert terms_of_use_link, "Terms of use link is missing"
        return terms_of_use_link

    def go_to_terms_of_use_link_in_authorization_window(self):
        terms_of_use_link = self.terms_of_use_link_is_present()
        terms_of_use_link.click()

    def fill_the_registration_fields(self, reg_name=REGISTRATION_NAME, reg_email=REGISTRATION_EMAIL,
                                     reg_phone_number=REGISTRATION_PHONE_NUMBER, reg_password=REGISTRATION_PASSWORD):
        name_field = self.is_element_present(*AuthorizationModalWindowLocators.REGISTRATION_NAME_FIELD)
        name_field.send_keys(reg_name)
        email_field = self.is_element_present(*AuthorizationModalWindowLocators.REGISTRATION_EMAIL_FIELD)
        email_field.send_keys(reg_email)
        phone_number_field = self.is_element_present(*AuthorizationModalWindowLocators.REGISTRATION_PHONE_NUMBER_FIELD)
        phone_number_field.send_keys(reg_phone_number)
        password_field = self.is_element_present(*AuthorizationModalWindowLocators.REGISTRATION_PASSWORD_FIELD)
        password_field.send_keys(reg_password)

    def registration_button_is_present(self):
        registration_btn = self.is_element_present(*AuthorizationModalWindowLocators.REGISTRATION_BTN)
        assert registration_btn, "Registration button is missing"
        return registration_btn

    def check_if_entered_registration_data_is_invalid(self, expected_message=REGISTRATION_PHONE_NUMBER_ALREADY_EXIST_MESSAGE):
        error_message = self.element_is_visible(*AuthorizationModalWindowLocators.REGISTRATION_ERROR_MESSAGE,
                                                wait_time=100).text
        assert expected_message in error_message, \
            "Your data is correct or you have another message"

    def fill_the_log_in_fields(self, log_in_email=LOG_IN_EMAIL, log_in_password=LOG_IN_PASSWORD):
        email_or_phone_field = self.is_element_present(*AuthorizationModalWindowLocators.LOG_IN_EMAIL_OR_PHONE_FIELD)
        email_or_phone_field.send_keys(log_in_email)
        password_field = self.is_element_present(*AuthorizationModalWindowLocators.LOG_IN_PASSWORD)
        password_field.send_keys(log_in_password)

    def log_in_button_is_present(self):
        log_in_btn = self.is_element_present(*AuthorizationModalWindowLocators.LOG_IN_BTN)
        assert log_in_btn, "Log in button is missing"
        return log_in_btn

    def check_if_user_has_logged_in(self, expected_message=LOG_IN_GREETING):
        actual_message = self.element_is_visible(*AuthorizationModalWindowLocators.LOG_IN_GREETING_TEXT,
                                                wait_time=100).text
        assert expected_message in actual_message, \
            "Your entered incorrect data in log in fields"

    def check_if_entered_log_in_data_is_invalid(self, expected_message=LOG_IN_INVALID_MESSAGE):
        actual_message = self.element_is_visible(*AuthorizationModalWindowLocators.LOG_IN_ERROR_MESSAGE,
                                                wait_time=60).text
        assert expected_message in actual_message, \
            "Your entered correct data in log in fields or you received another error"

