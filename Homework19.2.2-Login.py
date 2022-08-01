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

my_account_btn = driver.find_element_by_xpath("//span[@class='caret']")

my_account_btn.click()

time.sleep(2)


#2 - Select the ‘Login’ option and verify that you are able to land on the login page.

select_login_btn = driver.find_element_by_xpath("//a[contains(text(), 'Login')]")
if not select_login_btn.is_selected():
    select_login_btn.click()
