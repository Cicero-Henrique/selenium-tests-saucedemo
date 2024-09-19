
import pytest
import conftest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup_teardown")
class Test01:

    def test_successful_login(self):
        driver = conftest.driver
        login_page = LoginPage()
        login_page.make_login("standard_user", "secret_sauce")
        assert driver.current_url == "https://www.saucedemo.com/inventory.html"

@pytest.mark.usefixtures("setup_teardown")
class Test02:

    def test_invalid_user(self):
        driver = conftest.driver
        login_page = LoginPage()
        login_page.make_login("wrong_user", "wrong_password")
        login_page.check_error_message()
