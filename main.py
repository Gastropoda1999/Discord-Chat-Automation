import profile
from re import I
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import *
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from time import sleep, time
from colorama import Fore , init
import time
import random
import os
from colorama import init , Fore
import requests

profilepath = r'C:\Users\Gastropoda\AppData\Roaming\Mozilla\Firefox\Profiles\o9urgzrk.test bot'
profile = webdriver.FirefoxProfile(profilepath)
option = webdriver.FirefoxOptions()
# option.headless = True
driver = webdriver.Firefox(firefox_profile=profile , options=option )

def clearpromp():
    clear = lambda: os.system('cls')
    clear()

clearpromp()

def start():
    url = input('Discord Chat url : ')

    driver.get(url) #load page

    try: #login
        username = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/div[1]/div/div[2]/input'))).send_keys('Gastropoda1999@gmail.com')
        password = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/div[2]/div/input'))).send_keys('M23037oo')
        login_confirm = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]/div'))).click()
    except:
        pass

    discord_name = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[1]/nav/div[1]/header/h1'))).text
    print('Discord name : ',discord_name)

    discord_chat = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[3]/div/main/form/div/div/div/div[1]/div/div[3]/div[1]'))).text
    print('Discord chat : ',discord_chat)

    time.sleep(5)


def sentence():
    file = open("word.txt", encoding="utf8").read().splitlines()
    word = random.choice(file)
    msg_input = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[3]/div[2]/main/form/div[1]/div/div/div[1]/div/div[3]/div[2]/div')
    msg_input.send_keys(word)
    msg_input.send_keys(Keys.ENTER)
    time.sleep(1)
start()
sentence()
