from selenium import webdriver

#imports for Selenium WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome(executable_path='../drivers/chromedriver')
driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")

#maximizing the browser window
driver.maximize_window()

# wait up to 10 seconds until the logo will be visible
logo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//img[@title='Brainbucket']")))

new_registrant_btn = driver.find_element_by_xpath("//a[contains(text(), 'Continue')]")

new_registrant_btn.click()

time.sleep(5)

#Register Account
#Personal Details
#firstname_field = driver.find_element_by_xpath("//fieldset/div[2]")
#firstname_field_class = firstname_field.get_attribute("class")
#assert "required" in firstname_field_class

#firstname_input = driver.find_element_by_id("input-firstname")
#firstname_input.clear()
#firstname_input.send_keys("Svetlana")

driver.quit()