#!/usr/bin/env python3
# Write a program that takes an email address and string of text on the
# command line and then, using selenium, logs in to your email account
# and sends an email of the string to the provided address. (You might
# want to set up a separate email account for this program.)


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import pyinputplus as pyip


if len(sys.argv) < 3:
    print('Usage: app.py <email> <message>')
    sys.exit(1)

email = sys.argv[1]
message = ' '.join(sys.argv[2:])

email_login = pyip.inputEmail('Insert your email login(mail.ru): ')
email_pass = pyip.inputPassword('Insert password: ')

browser = webdriver.Firefox()
browser.get('https://account.mail.ru/login')

login = WebDriverWait(browser, 10000).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.base-0-2-63 > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)')))
login = browser.find_element(
    By.CSS_SELECTOR, '.base-0-2-63 > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)')
login.send_keys(email_login)
login.submit()

password = browser.find_element(
    By.CSS_SELECTOR, 'span.inner-0-2-89:nth-child(1)')
password = WebDriverWait(browser, 10000).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.withIcon-0-2-78')))
password = browser.find_element(By.CSS_SELECTOR, '.withIcon-0-2-78')
password.click()
password.send_keys(email_pass)

signin_button = browser.find_element(
    By.CSS_SELECTOR, 'span.inner-0-2-89:nth-child(1)')
signin_button.click()

send_button = WebDriverWait(browser, 10000).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.compose-button__txt')))
send_button = browser.find_element(
    By.CSS_SELECTOR, '.compose-button__txt')
send_button.click()

address_field = WebDriverWait(browser, 10000).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.container--ItIg4 > div:nth-child(1) > input:nth-child(1)')))
address_field = browser.find_element(
    By.CSS_SELECTOR, '.container--ItIg4 > div:nth-child(1) > input:nth-child(1)')
address_field.click()
address_field.send_keys(email)

message_field = WebDriverWait(browser, 10000).until(
    EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/div[3]/div[5]/div/div/div[2]/div[1]')))
message_field = browser.find_element(
    By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/div[3]/div[5]/div/div/div[2]/div[1]')
message_field.send_keys(message)

send_email = browser.find_element(
    By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[3]/div[1]/div[1]/div/button/span')
send_email.click()
