import pytest
from pages.product_page import ProductPage


@pytest.mark.usefixtures("setup_teardown")
class Test14:

    def test_product_name(self):
        product_page = ProductPage()
        product_page.check_name_on_product_page()


@pytest.mark.usefixtures("setup_teardown")
class Test15:

    def test_product_desc(self):
        product_page = ProductPage()
        product_page.check_desc_on_product_page()

@pytest.mark.usefixtures("setup_teardown")
class Test16:

    def test_product_price(self):
        product_page = ProductPage()
        product_page.check_price_on_product_page()
