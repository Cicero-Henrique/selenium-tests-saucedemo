from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        error_message = "Username and password do not match any user in this service"
        # elements
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_div = (By.XPATH, "//*[@data-test='error']")
        self.error_message = (By.XPATH, f"//h3[contains(., {error_message}")

    def make_login(self, username, password):
        self.write(self.username_field, username)
        self.write(self.password_field, password)
        self.click(self.login_button)

    def check_error_message(self):
        self.find_element(self.error_div)
        self.find_element(self.error_message)
