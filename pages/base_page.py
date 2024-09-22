import conftest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self):
        self.driver = conftest.driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def write(self, locator, text):
        return self.driver.find_element(*locator).send_keys(text)

    def click(self, locator):
        return self.driver.find_element(*locator).click()

    def is_element_visible(self, locator):
        self.wait_element(locator)
        assert self.find_element(locator).is_displayed(), f"The element '{locator}' was not found."

    def wait_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_url(self, url, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.url_to_be(url))
