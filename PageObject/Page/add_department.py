from selenium.webdriver.common.by import By

from Hogwarts.PageObject.Page.base_page import BasePage


class AddDepartment(BasePage):
    def add_department(self, department_name):
        from Hogwarts.PageObject.Page.contact import Contact
        self.find(By.CSS_SELECTOR, "[name='name']").send_keys(department_name)
        self.find(By.CSS_SELECTOR, ".qui_btn.ww_btn.ww_btn_Dropdown.js_toggle_party_list").click()
        self.find(By.CSS_SELECTOR,
                  ".qui_dropdownMenu.ww_dropdownMenu.member_colLeft.js_party_list_container .jstree-anchor").click()
        self.find(By.CSS_SELECTOR, "[d_ck='submit']").click()
        return Contact(self.driver)

