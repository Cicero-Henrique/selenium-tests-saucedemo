from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage
from pages.login_page import LoginPage
from selenium.webdriver.support.select import Select


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
        self.add_to_cart_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.shopping_cart_button = (By.ID, "shopping_cart_container")
        self.shopping_cart_list = (By.CLASS_NAME, "cart_list")
        self.sort_select = (By.CLASS_NAME, "product_sort_container")
        self.az_option = (By.CSS_SELECTOR, 'option[value=az]')
        self.za_option = (By.CSS_SELECTOR, 'option[value=za]')
        self.list_items = (By.CLASS_NAME, "inventory_item_name")

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

    def check_cart_counter(self, expected_counter):
        self.side_menu_button = (By.CLASS_NAME, "shopping_cart_badge")
        counter = self.find_element(self.side_menu_button).text
        assert counter == expected_counter, f"Expected counter to be {expected_counter}, but got {counter}"

    def add_item_to_cart(self, counter):
        self.click(self.add_to_cart_button)
        self.check_cart_counter(counter)
        # Open shopping cart
        self.click(self.shopping_cart_button)
        self.wait_url("https://www.saucedemo.com/cart.html")
        list_size = len(self.find_elements(self.shopping_cart_list))
        assert str(list_size) == counter, f"Expected size to be {list_size}, but got {counter}"

    def check_first_item(self, item_name):
        first_item = self.find_elements(self.list_items)[0]
        assert first_item.text == item_name, f"Exepected item to be '{item_name}', but got '{first_item.text}'"

    def check_sort_z_to_a(self):
        select_element = self.find_element(self.sort_select)
        select = Select(select_element)
        select.select_by_visible_text('Name (Z to A)')
        assert self.find_element(self.za_option).is_selected()
        self.check_first_item("Test.allTheThings() T-Shirt (Red)")

    def check_sort_a_to_z(self):
        select_element = self.find_element(self.sort_select)
        select = Select(select_element)
        select.select_by_visible_text('Name (A to Z)')
        assert self.find_element(self.az_option).is_selected()
        self.check_first_item("Sauce Labs Backpack")
