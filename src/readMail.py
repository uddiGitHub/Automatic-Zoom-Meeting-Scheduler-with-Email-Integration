from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class read:
    def __init__(self,driver):
        self.driver = driver
        
    def read_text(self):
        # define the paths of the web elements
        primary_mailbox_path = "//div[@id=':1s']"
        unread_mailsClassName = "zA.zE"

        primary_mailbox = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, primary_mailbox_path))
        )
        primary_mailbox.click()

        # find all the emails
        unread_mails = self.driver.find_elements(By.CLASS_NAME,unread_mailsClassName)

        # create a empty list list to store all the mails
        unread_mail_df = []

        if unread_mails != []:
            for email in unread_mails:
                #open the unread mails    
                email.click()

                subject = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, "hP"))
                )
                subject = subject.text

                senderElement = self.driver.find_element(By.CLASS_NAME, "gD")
                sender = senderElement.text
                
                bodyElement = self.driver.find_element(By.CLASS_NAME, "ii.gt")
                body = bodyElement.text

                unread_mail_df.append({'Subject':subject,'Sender': sender,'Body': body})

                self.driver.back()

            return unread_mail_df 
        else:
            empty = "No unread mails"
            return empty

        