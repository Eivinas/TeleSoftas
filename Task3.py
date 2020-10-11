# Script selects text in described locations (Task 3)
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
  
# Use click_and_hold on link type elements
def select_text(locator, x_from, y_from, x_to, y_to):
    actions = ActionChains(driver)
    element = driver.find_element(By.CSS_SELECTOR, locator)
    actions.move_to_element(element)
    actions.move_by_offset(x_from, y_from)
    actions.click_and_hold(on_element=None)
    actions.move_by_offset(x_to, y_to)
    actions.perform()   
    time.sleep(2)
    actions = ActionChains(driver)
    actions.release(on_element=None)
    actions.perform() 

# Double click elements that are not link type
def double_click(locator):                               
    element = driver.find_element(By.CSS_SELECTOR, locator)
    actions = ActionChains(driver)
    actions.double_click(element).perform()
    time.sleep(2)

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/challenging_dom")
driver.set_window_size(1050, 708)

double_click("tr:nth-child(3) > td:nth-child(6)")
select_text("tr:nth-child(8) > td:nth-child(7)", -5, -10, 40, 10)   
select_text("tr:nth-child(3) > td:nth-child(7)", -30, -10, 22, 10) 
double_click("tr:nth-child(8) > td:nth-child(4)")
double_click("tr:nth-child(8) > td:nth-child(1)")

# Green button always go third
driver.find_element(By.XPATH, "//a[3]").click() 
time.sleep(2)
driver.quit()

  
