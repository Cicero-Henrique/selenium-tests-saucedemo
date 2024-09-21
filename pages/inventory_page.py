from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage
from pages.login_page import LoginPage

class InventoryPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        text_title = "Swag Labs"
        text_all_items = "All Items"
        # elements
        self.title = (By.XPATH, f"//div[@class='app_logo' and (text() = '{text_title}')]")
        self.side_menu = (By.CLASS_NAME, "bm-burger-button")
        self.all_items = (By.XPATH, f"//a[@href='#' and (text() = '{text_all_items}')]")

    def check_login_successful(self):
        login_page = LoginPage()
        login_page.make_login("standard_user", "secret_sauce")
        assert self.driver.current_url == "https://www.saucedemo.com/inventory.html"
        self.is_element_visible(self.title)

    def open_side_menu(self):
        self.click(self.side_menu)

    def click_on_all_items(self):
        self.click(self.all_items)
