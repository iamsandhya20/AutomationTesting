import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

dropdown = Select(driver.find_element(By.ID, "dropdown-class-example"))
dropdown.select_by_index(2)
time.sleep(2)

#dropdown.select_by_visible_text("option2")