from selenium.webdriver.common.by import By
import time

class read:
    def __init__(self,driver):
        self.driver = driver
        
    def read_text(self):
        # define the paths of the web elements
        primary_mailbox_path = "//div[@id=':1s']"
        mailsClassName = "bog"

        primary_mailbox = self.driver.find_element(By.XPATH, primary_mailbox_path)
        primary_mailbox.click()

        # find all the emails
        mails = self.driver.find_elements(By.CLASS_NAME,mailsClassName)

        # create a empty list list to store all the mails
        mail_df = []

        for email in mails:
        #    print(email.text)
        #    subject = email.text
               
           #open the unread mail    
           email.click()

           senderElement = self.driver.find_element(By.XPATH,"//span[@class='gD']")
           sender = senderElement.text

           bodyElement = self.driver.find_element(By.XPATH,"//div[@class='gs']")
           body = bodyElement.text

           mail_df.append({
            #    'Subject':subject,
                           'Sender': sender,
                           'Body': body})
           
           time.sleep(3)
           self.driver.back()
    
        return mail_df