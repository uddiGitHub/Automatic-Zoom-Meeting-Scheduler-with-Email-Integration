from selenium import webdriver
import pandas

# import the credentials
from credentials import emailId, password, gmail_url

# import 
from login_manager import login
from mail_Reader import read
from mail_Analyzer import analyze

# define the Xpath of the required elements of the web page
emailXpath = "//input[@id='identifierId']"
passName = "Passwd"
enterXpath = "//span[normalize-space()='Next']"

# create a instance of gmail login
gmail_login = login(emailId,password,gmail_url,emailXpath,passName,enterXpath)
driver = gmail_login.loginMethod()

# now read the unread mails
readInstatnce = read(driver)

unread_mails_df = readInstatnce.read_text()
# unread_mails_df.to_csv("mails.csv", index=False)
if unread_mails_df is None:
    print("No unread mails")
else:
    #analyze the mails
    analyzeInstance = analyze(unread_mails_df)
    qualified_mails = analyzeInstance.qualify_the_mail()
    linkReqMails = analyzeInstance.extract_date_and_time(qualified_mails)
    print(linkReqMails)
    linkReqMails.to_csv("linkReqMails.csv", index=False)

# close the driver
driver.close()

