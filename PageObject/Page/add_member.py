from selenium.webdriver.common.by import By

from Hogwarts.PageObject.Page.base_page import BasePage


class AddMember(BasePage):

    def add_member(self, name, account, phone_number):
        from Hogwarts.PageObject.Page.contact import Contact
        self.find(By.ID, "username").send_keys(name)
        self.find(By.ID, "memberAdd_acctid").send_keys(account)
        self.find(By.ID, "memberAdd_phone").send_keys(phone_number)
        self.find(By.CSS_SELECTOR, ".qui_btn.ww_btn.js_btn_save").click()
        return Contact(self.driver)
