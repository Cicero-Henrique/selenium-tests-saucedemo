from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage
from pages.login_page import LoginPage


class InventoryPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        text_title = "Swag Labs"
        text_all_items = "All Items"
        text_about = "About"
        text_logout = "Logout"
        # elements
        self.title = (By.XPATH, f"//div[@class='app_logo' and (text() = '{text_title}')]")
        self.side_menu_button = (By.CLASS_NAME, "bm-burger-button")
        self.all_items_button = (By.XPATH, f"//a[(text() = '{text_all_items}')]")
        self.about_button = (By.XPATH, f"//a[(text() = '{text_about}')]")
        self.logout_button = (By.XPATH, f"//a[(text() = '{text_logout}')]")

    def check_login_successful(self):
        login_page = LoginPage()
        login_page.make_login("standard_user", "secret_sauce")
        assert self.driver.current_url == "https://www.saucedemo.com/inventory.html"
        self.is_element_visible(self.title)

    def open_side_menu(self):
        self.click(self.side_menu_button)

    def check_all_items(self):
        self.is_element_visible(self.all_items_button)
        href_value = self.find_element(self.all_items_button).get_attribute('href')
        expected_href = "https://www.saucedemo.com/inventory.html#"
        assert href_value == expected_href, f"Expected href to be {expected_href}, but got {href_value}"

    def check_about_button(self):
        self.is_element_visible(self.about_button)
        href_value = self.find_element(self.about_button).get_attribute('href')
        expected_href = "https://saucelabs.com/"
        assert href_value == expected_href, f"Expected href to be {expected_href}, but got {href_value}"

    def check_logout_user(self):
        self.click(self.logout_button)
        href_value = self.find_element(self.logout_button).get_attribute('href')
        expected_href = "https://www.saucedemo.com/"
        assert href_value == expected_href, f"Expected href to be {expected_href}, but got {href_value}"
