
import pytest
import conftest
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

@pytest.mark.usefixtures("setup_teardown")
class Test05:

    def test_about_button(self):
        inventory_page = InventoryPage()
        inventory_page.check_login_successful()
        inventory_page.open_side_menu()
        inventory_page.check_about_button()
        href_value = inventory_page.find_element(inventory_page.about_button).get_attribute('href')
        expected_href = "https://saucelabs.com/"
        assert href_value == expected_href, f"Expected href to be {expected_href}, but got {href_value}"
