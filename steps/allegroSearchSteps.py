from behave import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@when('I enter "{product_name}" in search field')
def enter_product_name(context, product_name):
    context.driver.find_element_by_xpath('/html/body/div[2]/div[2]/header/div/div/div/div/form/input').send_keys(product_name)


@when('click SZUKAJ button')
def click_find(context):
    context.driver.find_element_by_xpath('/html/body/div[2]/div[2]/header/div/div/div/div/form/button').click()


@then('list of products appears')
def show_products(context):
    WebDriverWait(context.driver, 40).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[4]/div/div/div/div/div/div[2]/div[1]/div[3]/div[1]/div/div')))
    first_product = context.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div/div/div/div/div/div[2]/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/div/section[1]/section/article[1]/div/div[2]/div[1]/h2')
    product_text = first_product.get_attribute('InnerText')
    assert product_text == 'Głośnik przenośny' or 'GŁOŚNIK PRZENOŚNY'
    context.driver.close()
