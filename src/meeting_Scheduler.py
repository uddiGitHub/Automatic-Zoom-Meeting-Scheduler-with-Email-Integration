from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class schedule:
    def __init__(self,driver):
        self.driver = driver

    def schedule_zoom_meeting(self,linkReqMails):
        scheduler_path = "//ul[@aria-label='meetings']//a[@id='btnScheduleMeeting']"
        scheduler = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, scheduler_path))
        )
        scheduler.click()
        time.sleep(2)

        # define the topic of the meeting