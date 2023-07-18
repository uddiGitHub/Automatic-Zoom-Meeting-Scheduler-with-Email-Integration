from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
from bardMail_analyzer import bardAnalyzer
import pyautogui as pg
import pyperclip
import pandas as pd

class schedule:
    def __init__(self,driver):
        self.driver = driver

    def schedule_zoom_meeting(self,linkReqMails):
        #list 
        invitation_link = []

        # extract the required details from the mail from bard analyzer
        bardInstance = bardAnalyzer(linkReqMails)
        meeting_details = bardInstance.extract_meeting_details(linkReqMails)

        for index in range(len(meeting_details)):
            # strat the process of scheduling the meeting
            scheduler_path = "//ul[@aria-label='meetings']//a[@id='btnScheduleMeeting']"
            scheduler = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, scheduler_path))
            )
            scheduler.click()

            # define the topic of the meeting
            topic_path = "//input[@id='topic']"
            topic = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, topic_path))
            )
            topic.send_keys(meeting_details['Topic'].iloc[index])

            # set the date of the meeting
            date = meeting_details['Date'].iloc[index]
            date = datetime.datetime.strptime(str(date), '%Y-%m-%d')
            # extract day month and year
            day = date.day
            month = date.strftime('%B')
            year = date.year

            # //div[@class='zm-picker-panel__content']//tbody//td[@class!='normal disabled']


            #click on the clender icon
            self.driver.find_element(By.XPATH,"//input[@id='mt_time']").click()
            # while self.driver.find_element(By.XPATH,"//span[normalize-space()='July']").text != month:
            #     self.driver.find_element(By.XPATH,"(//i[@class='zm-icon-right'])[6]").click()
            # while self.driver.find_element(By.XPATH,"//span[normalize-space()='2023']").text != str(year):
            #     self.driver.find_element(By.XPATH,"(//i[@class='zm-icon-right-1'])[1]").click()
            # select the date
            date_class = "available"
            date_calender = self.driver.find_elements(By.XPATH, date_class)
            for elements in date_calender:
                a_tags = elements.find_elements(By.TAG_NAME,'a')
                for a_tag in a_tags:
                    if a_tag.text == str(day):
                        a_tag.click()
                        break


            # define the start time of the meeting
            start_time_path = "//div[@class='zm-select mgl-sm start-time zm-select--small']//div[@class='zm-select-input']"
            start_time = self.driver.find_element(By.XPATH,start_time_path)
            # get the time from the dataframe
            time_string = meeting_details['Time'].iloc[index]
            time_parts = time_string.split()
            if len(time_parts) == 2:
                time = time_parts[0]
                period = time_parts[1]
            # send the time to the start time
            start_time.click()
            pg.typewrite(time)
            pg.press('enter')
            # set the period of the meeting
            period_dropdown_path = "(//span[@id='start_time2'])[1]"
            self.driver.find_element(By.XPATH,period_dropdown_path).click()
            if period == 'AM':
                self.driver.find_element(By.XPATH,"(//dd[@id='select-item-start_time2-0'])[1]").click()
            else:
                # select PM
                self.driver.find_element(By.XPATH,"(//dd[@id='select-item-start_time2-1'])[1]").click()

            # set the time zone
            timezone_india = "(GMT+5:30) India"
            timezone_path = "//input[@aria-label='select time zone,(GMT-7:00) Pacific Time (US and Canada)']"
            timezone = self.driver.find_element(By.XPATH,timezone_path)
            timezone.click()
            timezone.send_keys(timezone_india)
            pg.press('enter')

            # set the attendees
            attendees_path = "//input[@placeholder='Enter user names or email addresses']"
            attendees = self.driver.find_element(By.XPATH,attendees_path)
            attendees.click()
            attendees.send_keys(meeting_details['Attendees'].iloc[index])
            pg.press('enter')

            # save the meeting
            save_path = "//div[@class='zm-sticky']//div[1]//button[1]//span[1]"
            save = self.driver.find_element(By.XPATH,save_path)
            save.click()
            time.sleep(2)

            # copy the meeting link as invitation
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Copy Invitation']//button[@id='copy_invitation']"))
            ).click()

            # copy to clipboard
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//span[@class='zm-button__slot'][normalize-space()='Copy Meeting Invitation']"))
            ).click()
            invitation = pyperclip.paste()
            invitation_link.append(invitation)
        
        # add the invitation link to the dataframe
        meeting_details['Invitation Link'] = pd.Series(invitation_link).tolist()

        return meeting_details


            