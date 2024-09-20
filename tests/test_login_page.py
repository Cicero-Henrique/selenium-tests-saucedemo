
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
        login_page = LoginPage()
        login_page.make_login("wrong_user", "wrong_password")
        login_page.check_error_message(login_page.error_message_username_password)

@pytest.mark.usefixtures("setup_teardown")
class Test03:

    def test_empty_username(self):
        login_page = LoginPage()
        login_page.make_login("", "wrong_password")
        login_page.check_error_message(login_page.error_message_username)
