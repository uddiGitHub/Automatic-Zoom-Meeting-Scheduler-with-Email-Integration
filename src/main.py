from selenium import webdriver

# import the credentials
from credentials import emailId, gmail_password, zoom_password

# import 
from login_manager import login
from mail_Reader import read
from mail_analyzer import bardAnalyzer
from meeting_Scheduler import schedule
from response import compose

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
    # close the driver
    mailDriver.close()

    # analyze the mails with Bard API
    print("Analyzing the mails:...........")
    bardInstance = bardAnalyzer(unread_mails_df)
    qualified_mails = bardInstance.analyze_the_mail()
    if qualified_mails.empty:
        print("No qualified mails")
    else:
        print("Getting the dates and time:...........")
        linkReqMails = bardInstance.extract_date_and_time(qualified_mails)
        print("Mails analyzed successfully")
        print(linkReqMails)

        print("Scheduling the meeting:...........")
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

        # schedule the meeting
        scheduleInstance = schedule(zoomDriver)
        invitation_df = scheduleInstance.schedule_zoom_meeting(linkReqMails)
        print("Meeting scheduled successfully")
        print(invitation_df)

        # close the zoom driver
        zoomDriver.close()

        # login to gmail
        response_gmail_login = login(emailId,gmail_password,gmail_url,emailXpath,passName,enterXpath)
        response_mailDriver = response_gmail_login.loginMethod()

        # compose the mail
        print("Composing the mail:...........")
        composeInstance = compose(response_mailDriver)
        composeInstance.compose_mail(invitation_df)
        print("Mail sent successfully")



