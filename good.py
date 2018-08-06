import os
import time
import random
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

#session = requests.session()
i=1


driver = webdriver.Chrome("c:/Users/haruki/Desktop/chromedriver.exe")

driver.get("https://tinder.com/app/login")

######
PHONE_NUMBER = "08011453035"
login_info = {
    "phone_number":PHONE_NUMBER,
}
######

key = input('type "y":')
people = 100

if key == "y":
    while i < people:
        i=i+1
        driver.find_element_by_tag_name("body").send_keys(Keys.RIGHT)
        time.sleep(0.3)
        print(i)
    else:
        print("swipe", people, "people")
        driver.close()