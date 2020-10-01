from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# init driver
driver = webdriver.Chrome(executable_path=r"C:\Users\vibha\Projects\JobEasy\AutoProject\python-selenium-automation\chromedriver\chromedriver.exe")
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/gp/help/customer/display.html')
search=driver.find_element(By.ID,'helpsearch')
search.clear()
search.send_keys('Cancel Order',Keys.ENTER)

#Verify
assert 'Cancel Items or Orders' in driver.find_element(By.XPATH,"//div[@class='help-content']").text

driver.quit()

