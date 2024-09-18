
import pytest
import conftest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup_teardown")
class Test01:

    def test_login_success(self):
        driver = conftest.driver
        login_page = LoginPage()
        login_page.make_login("standard_user", "secret_sauce")
        assert driver.current_url == "https://www.saucedemo.com/inventory.html"
