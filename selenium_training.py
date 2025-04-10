from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Edge(options=options)
driver.get("https://dashboard.flysepehran.com/login")
driver.maximize_window()
driver.find_element(By.ID, "user").send_keys('hooshmand')
driver.find_element(By.ID, "password").send_keys('951623')
driver.find_element(By.CLASS_NAME, "captcha_value").send_keys('25')
sleep(1)
driver.find_element(By.CLASS_NAME, "login-btn").click()
