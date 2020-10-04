from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ORDER_INPUT=(By.ID, 'nav-orders')
RESULTS=(By.XPATH, "//div[@class='a-box-inner a-padding-extra-large']")

@given ('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')


@when ('Click on Orders')
def click_orders(context):
    orders = context.driver.find_element(*ORDER_INPUT)
    sleep(5)
    orders.click()

@then ('{result_text} page is displayed')
def signIn_text(context,result_text):
    assert result_text in context.driver.find_element(*RESULTS).text


