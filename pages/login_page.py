from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        # elements
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def make_login(self, username, password):
        self.write(self.username_field, username)
        self.write(self.password_field, password)
        self.click(self.login_button)
