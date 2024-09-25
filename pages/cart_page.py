from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage
from pages.inventory_page import InventoryPage


class CartPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        # elements
        self.remove_item = (By.ID, "remove-sauce-labs-backpack")

    def check_remove_item(self):
        inventory_page = InventoryPage()
        inventory_page.check_login_successful()
        inventory_page.add_item_to_cart("sauce-labs-backpack", "1")
        self.driver.get("https://www.saucedemo.com/inventory.html")
        inventory_page.add_item_to_cart("sauce-labs-bike-light", "2")
        self.driver.get("https://www.saucedemo.com/cart.html")
        self.click(self.remove_item)
        inventory_page.check_cart_counter("1")
