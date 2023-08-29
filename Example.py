import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.ID, "name").send_keys("sandhya")
time.sleep(2)
driver.find_element(By.ID, "alertbtn").click()

alert = Alert(driver)
print(alert.text)
alert.accept()
driver.find_element(By.ID, "confirmbtn").click()
time.sleep(2)