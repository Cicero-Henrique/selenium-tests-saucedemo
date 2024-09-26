import pytest
from selenium import webdriver

@pytest.fixture
def setup_teardown():
    global driver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(5)

    # run test
    yield

    # teardown

    driver.quit()
