import pytest
from pages.cart_page import CartPage


@pytest.mark.usefixtures("setup_teardown")
class Test19:

    def test_product_name(self):
        cart_page = CartPage()
        cart_page.check_remove_item()
