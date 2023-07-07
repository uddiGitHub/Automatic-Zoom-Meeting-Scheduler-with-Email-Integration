from selenium import webdriver

# import the credentials
from credentials import emailId, password, gmail_url

# import the login class to log into the gmail
from login import login

# define the Xpath of the required elements of the web page
emailXpath = "//input[@id='identifierId']"
passXpath = "//input[@name='password']"

# create a instance of gmail login
gmail_login = login(emailId,password,gmail_url,emailXpath,passXpath)

# call the loginMethod from login class
driver = gmail_login.loginMethod()

# close the driver
driver.close()

