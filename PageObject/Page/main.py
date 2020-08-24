from selenium.webdriver.common.by import By

from Hogwarts.PageObject.Page.add_member import AddMember
from Hogwarts.PageObject.Page.base_page import BasePage
from Hogwarts.PageObject.Page.contact import Contact
from Hogwarts.PageObject.Page.import_address_book import ImportAddressBook


class MainPage(BasePage):
    _url = "https://work.weixin.qq.com/wework_admin/frame"

    def go_to_contact(self):
        self.find(By.CSS_SELECTOR, "#menu_contacts").click()
        return Contact(self.driver)

    def go_to_add_member(self):
        self.find(By.CSS_SELECTOR, "[node-type=addmember]").click()
        return AddMember(self.driver)

    def go_to_import_address_book(self):
        self.find(By.CSS_SELECTOR, "[node-type=memberJoin]").click()
        return ImportAddressBook(self.driver)
