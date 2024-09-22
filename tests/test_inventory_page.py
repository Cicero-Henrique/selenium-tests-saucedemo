
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
        inventory_page.add_item_to_cart("1")
