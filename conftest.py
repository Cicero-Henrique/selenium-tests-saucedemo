import pytest
from selenium import webdriver


def setup_teardown():
    global driver
    driver = webdriver.Chrome()
    driver.implicit_wait(5)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    # run test
    yield

    # teardown

    driver.quit()
