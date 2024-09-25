from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage
from pages.inventory_page import InventoryPage


class CartPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        # elements
        self.remove_item = (By.ID, "remove-sauce-labs-backpack")
        self.checkout_button = (By.ID, "checkout")
        self.continue_button = (By.ID, "continue")
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")

    def check_remove_item(self):
        inventory_page = InventoryPage()
        inventory_page.check_login_successful()
        inventory_page.add_item_to_cart("sauce-labs-backpack", "1")
        self.driver.get("https://www.saucedemo.com/inventory.html")
        inventory_page.add_item_to_cart("sauce-labs-bike-light", "2")
        self.driver.get("https://www.saucedemo.com/cart.html")
        self.click(self.remove_item)
        inventory_page.check_cart_counter("1")

    def complete_form(self):
        self.write(self.first_name_input, "Elon")
        self.write(self.last_name_input, "Musk")
        self.write(self.postal_code_input, "1234")
        self.click(self.continue_button)

    def check_make_checkout(self):
        inventory_page = InventoryPage()
        inventory_page.check_login_successful()
        inventory_page.add_item_to_cart("sauce-labs-backpack", "1")
        self.driver.get("https://www.saucedemo.com/cart.html")
        self.click(self.checkout_button)
        self.wait_url("https://www.saucedemo.com/checkout-step-one.html")
        self.complete_form()
        current_url = self.driver.current_url
        expected_url = "https://www.saucedemo.com/checkout-step-two.html"
        assert current_url == expected_url, f"Expected url to be {expected_url}, but got {current_url}"
