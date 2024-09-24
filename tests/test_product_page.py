import pytest
from pages.product_page import ProductPage


@pytest.mark.usefixtures("setup_teardown")
class Test14:

    def test_product_name(self):
        product_page = ProductPage()
        product_page.check_name_on_product_page()