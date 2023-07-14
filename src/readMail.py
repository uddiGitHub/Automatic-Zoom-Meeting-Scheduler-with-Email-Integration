from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

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

        # create a empty dataframe to store the unread mails
        unread_mail_df = pd.DataFrame(columns=['Subject','Sender','Sender ID','Body'])

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
                
                senderId = self.driver.find_element(By.CLASS_NAME, "go")
                senderId = senderId.text

                bodyElement = self.driver.find_element(By.CLASS_NAME, "ii.gt")
                body = bodyElement.text

                mail_data = {'Subject':subject,'Sender': sender,'Sender ID': senderId,'Body': body}
                unread_mail_df = pd.concat([unread_mail_df,pd.DataFrame(mail_data,index=[0])],ignore_index=True)

                self.driver.back()

            return unread_mail_df 
        else:
            return None

        