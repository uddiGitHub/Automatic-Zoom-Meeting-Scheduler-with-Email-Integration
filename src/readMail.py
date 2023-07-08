from selenium.webdriver.common.by import By

class read:
    def __init__(self,driver):
        self.driver = driver
        
    def read_text(self):
        # define the paths of the web elements
        primary_mailbox_path = "//div[@id=':1v']//div[@class='aKw']"
        unread_mail_className = "zA zE"

        primary_mailbox = self.driver.find_element(By.XPATH, primary_mailbox_path)
        primary_mailbox.click()

        # find all the unread emails
        unread_mails = self.driver.find_elements(By.CLASS_NAME,unread_mail_className)

        # create a empty list list to store all the unread mails
        unread_mail_df = []

        for email in unread_mails:
           subject = email.text
               
           #open the unread mail
           email.click()

           senderElement = self.driver.find_element(By.XPATH,"//span[@class='gD']")
           sender = senderElement.text

           bodyElement = self.driver.find_element(By.CLASS_NAME,"a3s aiL ")
           body = bodyElement.text

           unread_mail_df.append({'Subject':subject,
                                  'Sender': sender,
                                  'Body': body})
           self.driver.back()
    
        print(unread_mails)
        return unread_mail_df