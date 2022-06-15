from .base_page import BasePage
from .locators import ContactsLocators


class ContactsPage(BasePage):
    def phone_numbers_is_present(self):
        phone_numbers = self.browser.find_element(*ContactsLocators.CONTACTS_PHONE_NUMBER).text
        assert phone_numbers, "\nPhone numbers in contacts page is missing"
        return phone_numbers