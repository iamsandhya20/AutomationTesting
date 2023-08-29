from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()

print("current URL - " + driver.current_url)
print("title - " + driver.title)
print("browser name -"+driver.name)

txtbox = driver.find_element(By.ID, "APjFqb")
txtbox.send_keys("red dress")
gmail = driver.find_element(By.XPATH, "//a[@aria-label='Gmail (opens a new tab)']")
gmail.click()
driver.back()
driver.forward()