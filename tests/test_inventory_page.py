
import pytest
from pages.inventory_page import InventoryPage


@pytest.mark.usefixtures("setup_teardown")
class Test05:

    def test_all_items_button(self):
        inventory_page = InventoryPage()
        inventory_page.check_login_successful()
        inventory_page.open_side_menu()
        inventory_page.check_all_items()

@pytest.mark.usefixtures("setup_teardown")
class Test06:

    def test_about_button(self):
        inventory_page = InventoryPage()
        inventory_page.check_login_successful()
        inventory_page.open_side_menu()
        inventory_page.check_about_button()

@pytest.mark.usefixtures("setup_teardown")
class Test07:

    def test_logout_button(self):
        inventory_page = InventoryPage()
        inventory_page.check_login_successful()
        inventory_page.open_side_menu()
        inventory_page.check_logout_user

@pytest.mark.usefixtures("setup_teardown")
class Test08:

    def test_reset_app_state_button(self):
        inventory_page = InventoryPage()
        inventory_page.check_login_successful()
        inventory_page.add_item_to_cart("sauce-labs-backpack", "1")

@pytest.mark.usefixtures("setup_teardown")
class Test09:

    def test_sort_a_to_z(self):
        inventory_page = InventoryPage()
        inventory_page.check_login_successful()
        inventory_page.check_sort_z_to_a()
        inventory_page.check_sort_a_to_z()

@pytest.mark.usefixtures("setup_teardown")
class Test10:

    def test_sort_z_to_a(self):
        inventory_page = InventoryPage()
        inventory_page.check_login_successful()
        inventory_page.check_sort_z_to_a()

@pytest.mark.usefixtures("setup_teardown")
class Test11:

    def test_sort_low_to_high(self):
        inventory_page = InventoryPage()
        inventory_page.check_login_successful()
        inventory_page.check_sort_low_to_high()

@pytest.mark.usefixtures("setup_teardown")
class Test12:

    def test_sort_high_to_low(self):
        inventory_page = InventoryPage()
        inventory_page.check_login_successful()
        inventory_page.check_sort_high_to_low()

@pytest.mark.usefixtures("setup_teardown")
class Test13:

    def test_add_products_to_cart(self):
        inventory_page = InventoryPage()
        inventory_page.check_login_successful()
        inventory_page.check_add_two_items()
