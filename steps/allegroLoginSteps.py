from behave import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@given('I launch Chrome browser')
def open_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

@when('I open allegro page')
def open_page(context):
    context.driver.get('https://allegro.pl/')

@when('close pop up window')
def close_popup(context):
    WebDriverWait(context.driver, 40).until(EC.presence_of_element_located((By.XPATH, '//*[@id="dialog-title"]')))
    context.driver.find_element_by_xpath('/html/body/div[2]/div[8]/div/div[2]/div/button/img').click()

@when('click sign in button')
def click_signin(context):
    context.driver.find_element_by_xpath('/html/body/div[2]/div[5]/div/div/div[1]/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/p/a').click()

@when('I enter "{email}" as e-mail')
def enter_valid_email(context, email):
    WebDriverWait(context.driver, 40).until(EC.presence_of_element_located((By.ID, 'username')))
    context.driver.find_element_by_id('username').send_keys(email)


@when('enter "{password}" as password')
def enter_valid_password(context, password):
    context.driver.find_element_by_id('password').send_keys(password)

@when('click Zaloguj się')
def click_zaloguj(context):
    context.driver.find_element_by_xpath('//*[@id="login-button"]/span').click()

@then('I am logged in')
def logged_in(context):
    WebDriverWait(context.driver, 40).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/header/div[1]/nav/div[4]/button/span[1]')))
    text = context.driver.find_element_by_xpath('/html/body/div[2]/div[1]/header/div[1]/nav/div[4]/button/span[1]').get_attribute('innerText')
    assert text == 'testing789@onet.pl'
    context.driver.close()

@then('Login fails')
def login_failed(context):
    WebDriverWait(context.driver, 40).until(EC.presence_of_element_located((By.XPATH, '//*[@id="wrong-password-error-title"]/span')))
    error = context.driver.find_element_by_xpath('//*[@id="wrong-password-error-title"]/span').get_attribute('innerText')
    assert error == 'Login, e-mail lub hasło są nieprawidłowe'
    context.driver.close()


