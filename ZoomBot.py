from selenium import webdriver
import chromedriver_autoinstaller  # This module will automatically download chromedriver.exe
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import random

options = Options()
options.headless = True  # To make browser visible set it to False
path = chromedriver_autoinstaller.install()  # Returns path of the chromedriver.exe
driver = webdriver.Chrome(executable_path=path, options=options)

meeting_id = input("Enter the meeting id")  # meeting id of the meeting to join

driver.get("https://zoom.us/signin")
email_box = driver.find_element_by_id("email")
email_box.send_keys(input("Enter your Email-id"))  # Email-id for login
password_box = driver.find_element_by_id("password")
password_box.send_keys(input("Enter your Password"))  # Password for login
sign_in_btn = driver.find_element_by_xpath(
    """/html/body/div[1]/div[3]/div[2]/div[2]/div/div[2]/div/form/div[3]/div/div[1]/a""")
sign_in_btn.click()

sleep(0.5)  # Delay to avoid conflict while redirecting to different page

driver.get("https://zoom.us/j/" + meeting_id + "?status=success")

join_online = driver.find_element_by_xpath("""/html/body/div[2]/div/div/div[4]/a""")
driver.get(join_online.get_attribute("href"))

try:
    join_btn = driver.find_element_by_id("joinBtn")
    join_btn.click()
except NoSuchElementException:
    pass

# The below code is to spam the zoom chat if one wants

sleep(5)  # Delay so that the session loads
chat_btn = driver.find_element_by_xpath(
    """/html/body/div[2]/div[2]/div/div[2]/div/div[1]/div/footer/div[2]/button[3]""")
chat_btn.click()
try:
    chat_box = driver.find_element_by_xpath(
        """/html/body/div[9]/div/div/div/div[2]/div/div/div[2]/div/div[2]/textarea""")
except NoSuchElementException:
    chat_box = driver.find_element_by_xpath(
        """/html/body/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/textarea""")
chat_box.click()

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

while True:
    input_string = ''.join(random.choices(numbers, k=5))
    chat_box.send_keys(input_string)
    chat_box.send_keys(Keys.ENTER)
    sleep(1)  # Reduce timing in seconds to accelerate spamming
    chat_box.send_keys(Keys.ENTER)
