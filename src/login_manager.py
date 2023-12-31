from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
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
        driver.maximize_window()
        # go to gmail web page 
        driver.get(self.url)

        wait = WebDriverWait(driver, 300)

        # input the credentials and login
        email = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.emailXpath))
        )
        email.send_keys(self.emailId)

        try:
            # try to find the password field
            driver.find_element(By.XPATH, self.passName)
            # if the password field is found, control goes out of the try and except block
        except NoSuchElementException:
            # if the password field is not found, click on the next button
            driver.find_element(By.XPATH, self.enterXpath).click()

        password = wait.until(
            EC.visibility_of_element_located((By.NAME  , self.passName))
        )
        password.send_keys(self.password)
        time.sleep(2)
        driver.find_element(By.XPATH, self.enterXpath).click()

        return driver
