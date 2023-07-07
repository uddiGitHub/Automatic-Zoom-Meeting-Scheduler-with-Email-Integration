from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time

class login:
    def __init__(self, emailId, password, url,emailXpath,passXpath):
        self.emailId = emailId
        self.password = password
        self.url = url
        self.emailXpath = emailXpath
        self.passXpath = passXpath
    
    def loginMethod(self):
        # create a new instance
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        # go to gmail web page
        driver.get(self.url)

        # input the credentials 
        email = driver.find_element(By.XPATH,self.emailXpath)
        email.send_keys(self.emailId)

        Password = driver.find_element(By.XPATH,self.passXpath)
        Password.send_keys(self.password)
        
        time.sleep(4)
        return driver
