from selenium.webdriver.common.by import By

from Hogwarts.PageObject.Page.base_page import BasePage


class ImportAddressBook(BasePage):
    def import_address_book(self, path):
        self.find(By.CSS_SELECTOR, "#js_upload_file_input").send_keys(path)
        return path
