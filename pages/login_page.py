from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://www.saucedemo.com/")
sleep(3)
browser.find_element(By.ID, "user-name").send_keys("standard_user")
browser.find_element(By.ID, "password").send_keys("secret_sauce")
browser.find_element(By.ID, "login-button").click()

sleep(3)
assert browser.current_url == "https://www.saucedemo.com/inventory.html"

