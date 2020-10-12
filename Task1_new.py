# Scripts goes to https://www.tiketa.lt/EN/search and follows the steps:
# 1) Writes "trys" in Caption field 2) Selects Kaunas city 3) Chooses dates 2020-09-01 - 2021-12-31
# 4) Presses Search button 5) Presses Buy button on „TRYS PARŠIUKAI“ event 
# 6) Presses Buy 7) Selects Balkonas sector
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.tiketa.lt/en/search/")
driver.set_window_size(1050, 708)
driver.find_element(By.NAME, "sf_TextFilter").send_keys("trys")
driver.find_element(By.NAME, "sf_DateFrom").send_keys("2020-09-01")
driver.find_element(By.NAME, "sf_DateTo").send_keys("2021-12-31")
driver.find_element(By.ID, "dropdownMenu3").click() 
driver.find_element(By.LINK_TEXT, "Kaunas").click()
driver.find_element(By.CSS_SELECTOR, ".bn").click()

time.sleep(2)
driver.find_element(By.XPATH, "//p[contains(.,'MUZIKINĖ POPIETĖ VISAI ŠEIMAI „TRYS PARŠIUKAI“')]").click() 

time.sleep(2)
driver.find_element(By.XPATH, "//a[contains(text(),'Pirkti')]").click()
time.sleep(1)

# If dialog for login appears
try:
    element = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "btnNoLogin"))
    )
except:
    print("No dialog")
else: 
    driver.find_element(By.ID, "btnNoLogin").click()
  
# Google anti robot captcha
self.driver.execute_script("window.scrollTo(0,662)")
self.driver.switch_to.frame(0)
self.driver.find_element(By.CSS_SELECTOR, ".svg-holder [data-style=\'0\'] path:first-child").click()
time.sleep(5)
driver.quit()
