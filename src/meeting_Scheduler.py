from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import datetime
from mail_analyzer import bardAnalyzer
import pyautogui as pg
import pyperclip
import pandas as pd


class schedule:
    def __init__(self, driver):
        self.driver = driver

    def schedule_zoom_meeting(self, linkReqMails):
        wait = WebDriverWait(self.driver, 300)
        # list
        invitation_link = []

        # extract the required details from the mail from bard analyzer
        bardInstance = bardAnalyzer(linkReqMails)
        meeting_details = bardInstance.extract_meeting_details(linkReqMails)
        # print(meeting_details)

        for index in range(len(meeting_details)):
            # strat the process of scheduling the meeting
            scheduler_path = "//ul[@aria-label='meetings']//a[@id='btnScheduleMeeting']"
            scheduler = wait.until(
                EC.visibility_of_element_located((By.XPATH, scheduler_path))
            )
            scheduler.click()

            # define the topic of the meeting
            topic_path = "//input[@id='topic']"
            topic = wait.until(
                EC.visibility_of_element_located((By.XPATH, topic_path))
            )
            topic.send_keys(meeting_details['Topic'].iloc[index])

            # set the date of the meeting
            date = meeting_details['Date'].iloc[index]
            date = datetime.datetime.strptime(str(date), '%Y-%m-%d')

            # extract day month and year
            ex_day = date.day
            ex_month = date.strftime('%B')
            ex_year = date.year
            ex_weekday = date.strftime("%A")
            web_date_format = ex_month + " " + str(ex_day) + " " + str(ex_year) + " " + ex_weekday
            print(web_date_format)
            # set the calendar
            calender = self.driver.find_element(
                By.XPATH, "//input[@id='mt_time']")
            self.driver.execute_script("arguments[0].scrollIntoView();", topic)
            calender.click()
            # select the month
            month_sel = wait.until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, "div[role='application' i] span:nth-child(1)"))
            )
            cmonth = month_sel.text
            year_sel = wait.until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, "div[role='application' i] span:nth-child(2)"))
            )
            cyear = year_sel.text
            # iterate till the year and month are equal
            while True:
                if cmonth == str(ex_month) and cyear == str(ex_year):
                    break
                else:
                    next = wait.until(
                        EC.visibility_of_element_located((By.XPATH, "//button[contains(@class, 'zm-date-picker__next-month-btn') and contains(@aria-label, 'Next Month')]"))
                    )
                    action = ActionChains(self.driver)
                    action.move_to_element(next).click().perform()
                    cmonth = wait.until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, "div[role='application' i] span:nth-child(1)"))
                    ).text
                    cyear = wait.until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, "div[role='application' i] span:nth-child(2)"))
                    ).text
            # select the date
            table = self.driver.find_element(By.CLASS_NAME, "zm-date-table")
            rows = table.find_elements(By.CLASS_NAME, "zm-date-table__row")
            for row in rows:
                cells = row.find_elements(By.TAG_NAME, "td")
                for cell in cells:
                    date_element = cell.find_element(By.TAG_NAME, "a")
                    date_text = date_element.text
                    aria_label = date_element.get_attribute("aria-label")
                    if date_text == str(ex_day) and web_date_format in aria_label:
                        date_element.click()
                        break

            # define the start time of the meeting
            start_time_path = "//div[@class='zm-select mgl-sm start-time zm-select--small']//div[@class='zm-select-input']"
            start_time = self.driver.find_element(By.XPATH, start_time_path)
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
            self.driver.find_element(By.XPATH, period_dropdown_path).click()
            if period == 'AM':
                # self.driver.find_element(
                #     By.XPATH, "(//dd[@id='select-item-start_time2-0'])[1]").click()
                pg.press('enter')
            else:
                # select PM
                # self.driver.find_element(
                #     By.XPATH, "(//dd[@id='select-item-start_time2-1'])[1]").click()
                pg.press('down')
                pg.press('enter')

            # set the time zone
            timezone_india = "(GMT+5:30) India"
            timezone_path = '//input[@placeholder="select" and @aria-label="select time zone,(GMT-7:00) Pacific Time (US and Canada)" and @class="zm-select-input__inner"]'
            timezone = self.driver.find_element(By.XPATH, timezone_path)
            timezone.click()
            timezone.send_keys(timezone_india)
            pg.press('enter')

            # set the attendees
            attendees_path = "//input[@placeholder='Enter user names or email addresses']"
            attendees = self.driver.find_element(By.XPATH, attendees_path)
            attendees_name = meeting_details['Attendees'].iloc[index]
            attendees.click()
            attendees.send_keys(attendees_name)
            pg.sleep(5)
            pg.press('enter')

            # save the meeting
            save_path = "//div[@class='zm-sticky-fixed schedule-bar-sticky']//button[1]"
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, save_path))
            ).click()

            # copy the meeting link as invitation
            wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//button[contains(@class, 'zm-button--plain') and contains(@class, 'zm-button--small') and contains(@class, 'zm-button') and span[contains(@class, 'zm-button__slot') and contains(., 'Copy Invitation')]]"))
            ).click()

            # copy to clipboard
            wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//button[contains(@class, 'zm-button--primary') and contains(@class, 'zm-button--small') and contains(@class, 'zm-button') and span[contains(@class, 'zm-button__slot') and contains(., 'Copy Meeting Invitation')]]"))
            ).click()
            invitation = pyperclip.paste()
            invitation_link.append(invitation)
            self.driver.find_element(By.XPATH, "//div[@aria-labelledby='customTitle']//span[@class='zm-button__slot'][normalize-space()='Cancel']").click()

        # add the invitation link to the dataframe
        meeting_details['Invitation Link'] = pd.Series(invitation_link).tolist()

        return meeting_details
