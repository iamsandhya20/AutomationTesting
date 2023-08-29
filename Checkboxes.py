import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))

op2 = driver.find_element(By.ID, "checkBoxOption2")
op2.click()
time.sleep(2)
op3 = driver.find_element(By.ID, "checkBoxOption3")
assert op2.is_selected()

ab = driver.find_element(By.ID, "mousehover")
action = ActionChains(driver)
action.move_to_element(ab.perform())