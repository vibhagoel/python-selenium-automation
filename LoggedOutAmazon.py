from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# init driver
driver = webdriver.Chrome(executable_path=r"C:\Users\vibha\Projects\JobEasy\AutoProject\python-selenium-automation\chromedriver\chromedriver.exe")
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com')
# click on orders
orders=driver.find_element(By.ID,'nav-orders')
sleep(5)
orders.click()

#Verify
assert 'Sign-In' in driver.find_element(By.XPATH,"//div[@class='a-box-inner a-padding-extra-large']").text

driver.quit()




