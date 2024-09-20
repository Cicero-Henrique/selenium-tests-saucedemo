import pytest
from selenium import webdriver

@pytest.fixture
def setup_teardown():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(5)

    # run test
    yield

    # teardown

    driver.quit()
