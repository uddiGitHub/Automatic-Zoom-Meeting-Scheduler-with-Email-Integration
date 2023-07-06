# import the credentials
from credentials import emailId, password, gmail_url

# import PyAutoGui and Selenium for automating the process
import pyautogui as gui
from selenium import webdriver
import time


def login(emailId, password, url):
    # create a new instance
    driver = webdriver.Chrome()

    # navigate to gmail login page
    driver.get(url)

    # type the email and password using pyautogui
    gui.typewrite(emailId)
    gui.press('enter')

    gui.sleep(5)  # sleep for 3sec to complete the above process

    gui.typewrite(password)
    gui.press('enter')

    time.sleep(10)

    # Wait for the login process to complete
    driver.implicitly_wait(10)


def automate():
    # login to the gmail account
    login(emailId, password, gmail_url)


automate()