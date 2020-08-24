from selenium.webdriver.common.by import By

from Hogwarts.PageObject.Page.base_page import BasePage
from Hogwarts.PageObject.Page.main import MainPage
from Hogwarts.PageObject.Page.register import Register


class Login(BasePage):
    def go_to_register(self):
        self.find(By.CSS_SELECTOR, ".login_registerBar_link").click()
        return Register

    def go_to_main(self):
        return MainPage