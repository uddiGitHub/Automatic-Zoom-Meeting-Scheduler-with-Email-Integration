from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class compose:
    def __init__(self,driver):
        self.driver = driver
    
    def compose_mail(self,invitation_df):
        wait = WebDriverWait(self.driver, 300)
        # iterate over invitation_df
        for index in range(len(invitation_df)):
            #click on compose button
            composeButton = wait.until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Compose')]"))
            )
            composeButton.click()

            # enter the mail id
            toMail = wait.until(
                EC.visibility_of_element_located((By.XPATH, '//input[@class="agP aFw" and @peoplekit-id="BbVjBd"]'))
                )
            toMail.click()
            email_ID = invitation_df['Attendees'].iloc[index]
            toMail.send_keys(email_ID + Keys.ENTER)

            # enter the subject
            toSubject = self.driver.find_element(By.XPATH, '//input[@name="subjectbox"]')
            subject = "Invitation to the meeting on the topic: " + invitation_df['Topic'].iloc[index]
            toSubject.click()
            toSubject.send_keys(subject + Keys.ENTER)

            # enter the body
            toBody = self.driver.find_element(By.XPATH, '//*[@aria-label="Message Body" and @contenteditable="true"]')
            toBody.click()
            toBody.send_keys(invitation_df['Invitation Link'].iloc[index])

            # send the mail
            self.driver.find_element(By.XPATH, "//div[@class='dC']").click()
        
        time.sleep(5)
        self.driver.close()