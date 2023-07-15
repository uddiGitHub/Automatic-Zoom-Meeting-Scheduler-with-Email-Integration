from selenium import webdriver
import pandas

# import the credentials
from credentials import emailId, gmail_password, zoom_password

# import 
from login_manager import login
from mail_Reader import read
from mail_Analyzer import analyze

# define the Xpath of the required elements of the web page
emailXpath = "//input[@id='identifierId']"
passName = "Passwd"
enterXpath = "//span[normalize-space()='Next']"

# gmail page url
gmail_url = 'https://mail.google.com/'

# login to gmail
gmail_login = login(emailId,gmail_password,gmail_url,emailXpath,passName,enterXpath)
mailDriver = gmail_login.loginMethod()

# now read the unread mails
readInstatnce = read(mailDriver)

unread_mails_df = readInstatnce.read_text()
# unread_mails_df.to_csv("mails.csv", index=False)
if unread_mails_df is None:
    print("No unread mails")

    # close the driver
    mailDriver.close()
else:
    #analyze the mails
    analyzeInstance = analyze(unread_mails_df)
    qualified_mails = analyzeInstance.qualify_the_mail()
    linkReqMails = analyzeInstance.extract_date_and_time(qualified_mails)
    # print(linkReqMails)
    linkReqMails.to_csv("linkReqMails.csv", index=False)

    # close the driver
    mailDriver.close()

    # zoom page url
    zoom_url = 'https://zoom.us/signin#/login'

    # define the xpath
    usernameXpath = "//input[@id='email']"
    passwordName = "password"
    singinXpath = "//span[normalize-space()='Sign In']"

    # login to zoom
    zoom_login = login(emailId,zoom_password,zoom_url,usernameXpath,passwordName,singinXpath)
    zoomDriver = zoom_login.loginMethod()

    print("Login to zoom successful")
    # close the zoom driver
    zoomDriver.close()



