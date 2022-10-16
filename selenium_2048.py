#!/usr/bin/env python3
# 2048 is a simple game where you combine tiles by sliding them up, down,
# left, or right with the arrow keys. You can actually get a fairly high score
# by repeatedly sliding in an up, right, down, and left pattern over and over
# again. Write a program that will open the game at https://gabrielecirulli​
# .github.io/2048/ and keep sending up, right, down, and left keystrokes to
# automatically play the game.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


browser = webdriver.Firefox()
browser.get('https://play2048.co/')
new_game_button = browser.find_element(By.LINK_TEXT, 'New Game')
new_game_button.click()
game_area = browser.find_element(By.TAG_NAME, 'html')
game_over = False
while not game_over:
    time.sleep(0.1)
    game_area.send_keys(Keys.UP)
    time.sleep(0.1)
    game_area.send_keys(Keys.RIGHT)
    time.sleep(0.1)
    game_area.send_keys(Keys.DOWN)
    time.sleep(0.1)
    game_area.send_keys(Keys.LEFT)
    try:
        game_over = browser.find_element(By.LINK_TEXT, 'Try again')
    except:
        pass
