import pytest

from configuration import HOME_PAGE_LINK
from configuration import REGISTRATION_PHONE_NUMBER_ALREADY_EXIST, REGISTRATION_PHONE_NUMBER_INVALID, \
    REGISTRATION_PHONE_NUMBER_INVALID_MESSAGE, REGISTRATION_EMAIL_ALREADY_EXIST_MESSAGE, \
    REGISTRATION_EMAIL_ALREADY_EXIST, REGISTRATION_SHORT_PASSWORD, REGISTRATION_SHORT_PASSWORD_MESSAGE, \
    LOG_IN_INVALID_EMAIL, LOG_IN_INVALID_PASSWORD
from pages.home_page import HomePage


@pytest.fixture(scope="function")
def page(browser):
    page = HomePage(browser, HOME_PAGE_LINK)
    page.open()
    page.close_news_list()
    page.open_authorization_modal_window()
    yield page


class TestRegistration:
    def test_user_can_open_terms_of_use(self, page):
        page.go_to_registration_form()
        page.go_to_terms_of_use_link_in_authorization_window()
        page.check_if_user_is_redirected_to_terms_of_use_page()

    def test_user_can_not_register_with_already_registered_phone_number(self, page):
        page.go_to_registration_form()
        page.fill_the_registration_fields(reg_phone_number=REGISTRATION_PHONE_NUMBER_ALREADY_EXIST)
        registration_button = page.registration_button_is_present()
        registration_button.click()
        page.check_if_entered_registration_data_is_invalid()

    def test_user_can_not_register_with_invalid_phone_number(self, page):
        page.go_to_registration_form()
        page.fill_the_registration_fields(reg_phone_number=REGISTRATION_PHONE_NUMBER_INVALID)
        registration_button = page.registration_button_is_present()
        registration_button.click()
        page.check_if_entered_registration_data_is_invalid(expected_message=REGISTRATION_PHONE_NUMBER_INVALID_MESSAGE)

    def test_user_can_not_register_with_already_registered_email(self, page):
        page.go_to_registration_form()
        page.fill_the_registration_fields(reg_email=REGISTRATION_EMAIL_ALREADY_EXIST)
        registration_button = page.registration_button_is_present()
        registration_button.click()
        page.check_if_entered_registration_data_is_invalid(
            expected_message=REGISTRATION_EMAIL_ALREADY_EXIST_MESSAGE + REGISTRATION_EMAIL_ALREADY_EXIST)

    def test_user_can_not_register_with_short_password(self, page):
        page.go_to_registration_form()
        page.fill_the_registration_fields(reg_password=REGISTRATION_SHORT_PASSWORD)
        registration_button = page.registration_button_is_present()
        registration_button.click()
        page.check_if_entered_registration_data_is_invalid(
            expected_message=REGISTRATION_SHORT_PASSWORD_MESSAGE)


class TestLogIn:
    def test_user_can_log_in(self, page):
        page.fill_the_log_in_fields()
        log_in_button = page.log_in_button_is_present()
        log_in_button.click()
        page.check_if_user_has_logged_in()

    def test_user_can_not_log_in_with_invalid_data(self, page):
        page.fill_the_log_in_fields(log_in_email=LOG_IN_INVALID_EMAIL, log_in_password=LOG_IN_INVALID_PASSWORD)
        log_in_button = page.log_in_button_is_present()
        log_in_button.click()
        page.check_if_entered_log_in_data_is_invalid()

    def test_user_can_not_log_in_with_invalid_password(self, page):
        page.fill_the_log_in_fields(log_in_password=LOG_IN_INVALID_PASSWORD)
        log_in_button = page.log_in_button_is_present()
        log_in_button.click()
        page.check_if_entered_log_in_data_is_invalid()

    def test_user_can_not_log_in_with_invalid_email(self, page):
        page.fill_the_log_in_fields(log_in_email=LOG_IN_INVALID_EMAIL)
        log_in_button = page.log_in_button_is_present()
        log_in_button.click()
        page.check_if_entered_log_in_data_is_invalid()

