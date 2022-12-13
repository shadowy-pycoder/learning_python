#!/usr/bin/env python3
# yandex_downloader.py - a simple parsing tool to convert collections of
# translations into JSON format

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyinputplus as pyip
from bs4 import BeautifulSoup
from time import sleep
import json
import pprint

# prompt user for login/password/secret word
# pass and secret don't show up on the terminal
email_login = pyip.inputEmail('Insert your email login(yandex.ru): ')
email_pass = pyip.inputPassword('Insert password: ')
email_word = pyip.inputPassword('Insert secret word: ')

browser = webdriver.Firefox()
browser.get('https://passport.yandex.ru/auth?mode=add-user&retpath=https%3A%2F%2Ftranslate.yandex.ru%2Fcollections')

# inserting login
login = WebDriverWait(browser, 10000).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="passp-field-login"]')))
login = browser.find_element(By.XPATH, '//*[@id="passp-field-login"]')
login.send_keys(email_login)
login.submit()
sleep(2)

# inserting password
password = WebDriverWait(browser, 10000).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="passp-field-passwd"]')))
password = browser.find_element(By.XPATH, '//*[@id="passp-field-passwd"]')
password.send_keys(email_pass)
password.submit()
sleep(2)

# inserting secret word
# comment this block if needed (sometimes yandex doesn't ask for it)
secret_word = WebDriverWait(browser, 10000).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="passp-field-question"]')))
secret_word = browser.find_element(By.XPATH, '//*[@id="passp-field-question"]')
secret_word.send_keys(email_word)
secret_word.submit()
sleep(5)

k = 1
for i in range(4, 17):  # these values depend on the XPATH to collections

    # locate a collection tab
    collection = WebDriverWait(browser, 10000).until(
        EC.visibility_of_element_located((By.XPATH,
                                          f"/html/body/div[2]/div[1]/div/div[1]/div/div[1]/ul[1]/li[{i}]/div[1]/div")))
    collection = browser.find_element(
        By.XPATH, f"/html/body/div[2]/div[1]/div/div[1]/div/div[1]/ul[1]/li[{i}]/div[1]/div")
    collection.click()

    # locate word list
    web_page = browser.find_element(By.XPATH, "//*[@id='recordsListContent']")
    web_page = web_page.get_attribute('innerHTML')
    soup = BeautifulSoup(web_page, 'html.parser')
    words = soup.select(".record-line_speaker")
    word_list = []  # this list will contain words from a collection
    for i in range(len(words)):
        word_list.append(words[i].get('data-text'))
    word_dict = dict()
    for i in range(0, len(word_list), 2):  # create dictionary from a list of words
        # key - original word, value - translation
        word_dict[word_list[i]] = word_list[i+1]

    # create a json file from dictionary
    json_obj = json.dumps(word_dict)
    with open(f'word_dict{k}.json', 'w', encoding='UTF-8') as f:
        f.write(json_obj)

    k += 1  # increment for a json filename

    # locate a button to get back on a previous page
    return_button = WebDriverWait(browser, 10000).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div/div[3]/div[1]/div[1]/div[1]/span[1]")))
    sleep(2)
    return_button = browser.find_element(
        By.XPATH, "/html/body/div[2]/div[1]/div/div[3]/div[1]/div[1]/div[1]/span[1]")
    return_button.click()

browser.close()
