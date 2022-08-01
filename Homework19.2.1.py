from selenium import webdriver

#imports for selenium WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome(executable_path='../drivers/chromedriver')
driver.get("https://techskillacademy.net/brainbucket/index.php")

driver.maximize_window()

wd_wait = WebDriverWait(driver, 10) # creating a new object that can be reused in the script

logo = wd_wait.until(
    EC.visibility_of_element_located((By.XPATH, "//img[@title='Brainbucket']")))

#activating My Account dropdown
account_btn = driver.find_element_by_xpath("//a[@title='My Account']")
account_btn.click()

#Selecting Resgister from dropdown
wd_wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@class='dropdown-menu dropdown-menu-right']")))

register_option = driver.find_element_by_xpath("//*[@class='dropdown-menu dropdown-menu-right']/li[1]")
register_option.click()

#Register Account
#Personal Details
firstname_field = driver.find_element_by_xpath("//fieldset/div[2]")
firstname_field_class = firstname_field.get_attribute("class")
assert "required" in firstname_field_class

firstname_input = driver.find_element_by_id("input-firstname")
firstname_input.clear()
firstname_input.send_keys("Svetlana")

time.sleep(2)

#Assignemnt 19.2.1

#Exercise 1.1 - Select your state from the Region/State dropdown
#select country
country_dropdown = driver.find_element_by_id("input-country")
country_dropdown_select = Select(country_dropdown)
country_dropdown_select.select_by_visible_text('United States') # that will select United States

#Exercise 1.2 - Check “I have read and agree to the Privacy Policy”
agree_btn = driver.find_element_by_xpath("//input[@name='agree' and @value='1']")
if not agree_btn.is_selected():
    agree_btn.click()

time.sleep(2)

#Exercise 1.3 - Select “No” in the subscription
select_no_btn = driver.find_element_by_xpath("//input[@name='newsletter' and @value='0']")
if not select_no_btn.is_selected():
    select_no_btn.click()

time.sleep(5)
driver.quit()