from time import sleep

from selenium.webdriver.common.by import By

from Hogwarts.PageObject.Page.add_department import AddDepartment
from Hogwarts.PageObject.Page.add_member import AddMember
from Hogwarts.PageObject.Page.base_page import BasePage
from Hogwarts.PageObject.Page.import_address_book import ImportAddressBook


class Contact(BasePage):

    def go_to_add_department(self):
        self.find(By.CSS_SELECTOR, ".member_colLeft_top_addBtnWrap.js_create_dropdown").click()
        self.find(By.CSS_SELECTOR, ".js_create_party").click()
        return AddDepartment(self.driver)

    def go_to_add_member(self):
        sleep(2)
        self.find(By.CSS_SELECTOR, ".ww_operationBar .qui_btn.ww_btn.js_add_member").click()
        return AddMember(self.driver)

    def go_to_import_address_book(self):
        sleep(2)
        self.find(By.CSS_SELECTOR, ".ww_operationBar .ww_btn_PartDropdown_left").click()
        self.find(By.XPATH,
                  '//*[@id="js_contacts44"]/div/div[2]/div/div[2]/div[3]/div[1]/div[2]/div/ul/li[1]/a').click()
        return ImportAddressBook(self.driver)

    def get_department_list(self):
        sleep(2)
        return self.driver.find_element(By.XPATH, "//ul[@class='jstree-children']//li[last()]").text
