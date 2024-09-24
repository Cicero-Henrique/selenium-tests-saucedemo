from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage
from pages.inventory_page import InventoryPage


class ProductPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        # elements
        self.inventory_name = (By.XPATH, "//a[@id='item_4_title_link']/div")
        self.inventory_desc = (By.XPATH, "//div[@class='inventory_list']/div[1]//div[@class='inventory_item_desc']")
        self.inventory_price = (By.XPATH, "//div[@class='inventory_list']/div[1]//div[@class='inventory_item_price']")
        self.product_name = (By.XPATH, "//div[@data-test='inventory-item-name']")
        self.product_desc = (By.XPATH, "//div[@data-test='inventory-item-desc']")
        self.product_price = (By.XPATH, "//div[@data-test='inventory-item-price']")

    def make_product_assertions(self, inventory, product):
        inventory_page = InventoryPage()
        inventory_page.check_login_successful()
        info_inventory = self.find_element(inventory).text
        self.click(self.inventory_name)
        self.wait_url("https://www.saucedemo.com/inventory-item.html?id=4")
        info_product = self.find_element(product).text
        assert info_inventory == info_product, f"Expected product name to be {info_inventory}, but got {info_product}"

    def check_name_on_product_page(self):
        self.make_product_assertions(self.inventory_name, self.product_name)

    def check_desc_on_product_page(self):
        self.make_product_assertions(self.inventory_desc, self.product_desc)

    def check_price_on_product_page(self):
        self.make_product_assertions(self.inventory_price, self.product_price)
