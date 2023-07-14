from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class login:
    def __init__(self, emailId, password, url,emailXpath,passName,enterXpath):
        self.emailId = emailId
        self.password = password
        self.url = url
        self.emailXpath = emailXpath
        self.passName = passName
        self.enterXpath = enterXpath
    
    def loginMethod(self):
        # create a new instance of chrome
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        # go to gmail web page 
        driver.get(self.url)

        # input the credentials and login
        email = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.emailXpath))
        )
        email.send_keys(self.emailId)
        driver.find_element(By.XPATH, self.enterXpath).click()

        time.sleep(2)

        password = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME  , self.passName))
        )
        password.send_keys(self.password)
        driver.find_element(By.XPATH, self.enterXpath).click()

        return driver
