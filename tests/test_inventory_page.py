
import pytest
import conftest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.usefixtures("setup_teardown")
class Test05:

    def test_all_items_button(self):
        driver = conftest.driver
        inventory_page = InventoryPage()
        inventory_page.check_login_successful()
        inventory_page.open_side_menu()
        inventory_page.click_on_all_items()
        assert driver.current_url == "https://www.saucedemo.com/inventory.html"
