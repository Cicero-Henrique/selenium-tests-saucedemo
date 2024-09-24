from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage
from pages.inventory_page import InventoryPage


class ProductPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        # elements
        self.inventory_name = (By.XPATH, "//a[@id='item_4_title_link']/div")
        self.product_name = (By.XPATH, "//div[@data-test='inventory-item-name']")

    def check_name_on_product_page(self):
        inventory_page = InventoryPage()
        inventory_page.check_login_successful()
        name_inventory = self.find_element(self.inventory_name).text
        self.click(self.inventory_name)
        self.wait_url("https://www.saucedemo.com/inventory-item.html?id=4")
        name_product = self.find_element(self.product_name).text
        assert name_inventory == name_product, f"Expected product name to be {name_inventory}, but got {name_product}"