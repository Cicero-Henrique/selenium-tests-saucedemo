from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        text_error_username_password = "Username and password do not match any user in this service"
        text_error_username = "Username is required"
        text_error_password = "Password is required"
        # elements
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_div = (By.XPATH, "//*[@data-test='error']")
        self.error_message_username_password = (By.XPATH, f"//h3[contains(., '{text_error_username_password}')]")
        self.error_message_username = (By.XPATH, f"//h3[contains(., '{text_error_username}')]")
        self.error_message_password = (By.XPATH, f"//h3[contains(., '{text_error_password}')]")

    def make_login(self, username, password):
        self.write(self.username_field, username)
        self.write(self.password_field, password)
        self.click(self.login_button)

    def check_error_message(self, message):
        self.is_element_visible(self.error_div)
        self.is_element_visible(message)
