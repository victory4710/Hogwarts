from selenium.webdriver.common.by import By

from Hogwarts.PageObject.Page.base_page import BasePage
from Hogwarts.PageObject.Page.login import Login
from Hogwarts.PageObject.Page.register import Register


class First(BasePage):
    _url = "https://work.weixin.qq.com/"

    def go_to_register(self):
        self.find(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        return Register(self.driver)

    def go_to_login(self):
        self.find(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        return Login(self.driver)
