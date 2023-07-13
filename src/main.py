from selenium import webdriver
import pandas

# import the credentials
from credentials import emailId, password, gmail_url

# import 
from login import login
from readMail import read

# define the Xpath of the required elements of the web page
emailXpath = "//input[@id='identifierId']"
passName = "Passwd"
enterXpath = "//span[normalize-space()='Next']"

# create a instance of gmail login
gmail_login = login(emailId,password,gmail_url,emailXpath,passName,enterXpath)

# call the loginMethod from login class
driver = gmail_login.loginMethod()

# now read the unread mails
readInstatnce = read(driver)

unread_mails_df = readInstatnce.read_text()
unread_mails_df.to_csv("mails.csv", index=False)

print(unread_mails_df)

# close the driver
driver.close()

