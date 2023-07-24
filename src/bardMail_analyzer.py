import os
import re
import pandas as pd
from credentials import bard_api_key
from bardapi import Bard
from dateutil import parser
from datetime import timedelta

# set the API key
os.environ["_BARD_API_KEY"] = bard_api_key

class bardAnalyzer:
    def __init__(self, unread_mail_df):
        self.unread_mail_df = unread_mail_df

    def analyze_the_mail(self):
        # define the keywords
        keywords = ['zoom','meeting','link','meeting id','password','meeting password','meeting link','zoom link','zoom meeting']

        # create a empty dataframe to store the qualified mails
        qualified_mails = self.unread_mail_df[self.unread_mail_df['Body'].str.contains('|'.join(keywords))]

        return qualified_mails
    '''
    # use Bard API to analyze the mail
    def analyze_the_mail(self):
        # list
        qualifiedResponse_list = []

        for index in range(len(self.unread_mail_df)):
            # get the body of the mail
            body = self.unread_mail_df['Body'].iloc[index]

            # set the prompt
            prompt = "I am trying to analyze a mail for meeting request.\nHere I am giving you a body of a mail to analyze and tell me if it is a zoom meeting request?\nMail body:" + body + "\nI am taking response in just 1 or 0.0 means No and 1 means Yes\nThe 1 or 0 should be inside curly barces. Example {1} or {0}"
            # call the API
            bard = Bard()
            qualifyResponse = bard.get_answer(prompt)['content']
            print(qualifyResponse)
            qualifyResponse_token = re.search(r'{(.*?)}', qualifyResponse).group(1)
            # check if the response is Yes or No
            for word in qualifyResponse_token.split():
                if word == '1' or word == '0':
                    qualifyResponse_token = word
                    break
            # append the response to the list
            qualifiedResponse_list.append(qualifyResponse_token)

        # add the response to the dataframe
        qualified_mails = self.unread_mail_df.copy()
        qualified_mails['Response'] = pd.Series(qualifiedResponse_list).tolist()

        # filter the mails based on the response
        qualified_mails = qualified_mails[qualified_mails['Response'] == '1']
        return qualified_mails
    '''
    def extract_date_and_time(self,qualified_mails):
        # empty list to store the date time and Duration
        date_list = []
        time_list = []
        duration_hour_list = []
        duration_minute_list = []

        for index in range(len(qualified_mails)):
            # get the body of the mail
            body = qualified_mails['Body'].iloc[index]

            # find the date from the body
            date = parser.parse(body, fuzzy=True).date()

            # find the time and Duration of the meeting from the body
            matchTime = re.search(r'Time: (\d{1,2}:\d{2} [AP]M)', body)
            matchDuration = re.search(r'Duration: ([\d.]+) (\w+)', body)
            if matchTime and matchDuration:
                time = matchTime.group(1)

                duration_val = float(matchDuration.group(1))
                duration_unit = matchDuration.group(2)
                if duration_unit == 'hour' or duration_unit == 'hours':
                    duration = timedelta(hours=duration_val)
                elif duration_unit == 'minute' or duration_unit == 'minutes':
                    duration = timedelta(minutes=duration_val)
                else:
                    duration = timedelta()
            else:
                time = None
                duration = None

            # convert the duration to appropriate format
            hours = duration.seconds // 3600
            minutes = (duration.seconds // 60) % 60

            # append the date time and duration to the list
            date_list.append(date)
            time_list.append(time)
            duration_hour_list.append(hours)
            duration_minute_list.append(minutes)

        # add the date and time and duration to the dataframe
        linkReqMails = qualified_mails.copy()
        linkReqMails['Date'] = pd.Series(date_list).tolist()
        linkReqMails['Time'] = pd.Series(time_list).tolist()
        linkReqMails['Duration_Hours'] = pd.Series(duration_hour_list).tolist()
        linkReqMails['Duration_Minutes'] = pd.Series(duration_minute_list).tolist()

        return linkReqMails

    # def extract_date_and_time(self,qualified_mails):
    #     # empty list to store the date time and Duration
    #     date_list = []
    #     time_list = []

    #     # call the bard API
    #     bard = Bard()

    #     for index in range(len(qualified_mails)):
    #         # get the body of the mail
    #         body = qualified_mails['Body'].iloc[index]

    #         # find the date from the body using bard API
    #         data_prompt = 'From the mail body that is mentioned below, please extract the date of the meeting. Format of the date response should be in {%Y-%m-%d}\n' + body + '\nGive the response inside curly braces. Example {2021-09-30}\nIf no date is mentioned in the body of the mail. then give a random date in the format {%Y-%m-%d}\n'
    #         date_respone = bard.get_answer(data_prompt)['content']
    #         # print(date_respone)
    #         date = re.search(r"{(.*?)}", date_respone).group(1)
    #         # print(date)
    #         date_list.append(date)

    #         # find the time of the meeting from the body using bard API
    #         time_prompt = 'From the mail body that is mentioned below, please extract the time of the meeting. Format of the time response should be in {"%I:%M %p"}\n' + body + '\nGive the response inside curly braces. Example {10:30 PM}\nIf no time is mentioned in the body of the mail. then give a random time in the format {"%I:%M %p"}\n'
    #         time_respone = bard.get_answer(time_prompt)['content']
    #         time = re.search(r'Time: (\d{1,2}:\d{2} [AP]M)', time_respone).group(1)
    #         # print(time)
    #         time_list.append(time)

    #     # add the date and time and duration to the dataframe
    #     linkReqMails = qualified_mails.copy()
    #     linkReqMails['Date'] = pd.Series(date_list).tolist()
    #     linkReqMails['Time'] = pd.Series(time_list).tolist()    
    #     return linkReqMails

    def extract_meeting_details(self,mail):
        # call the API
        bard = Bard()

        # empty list  
        topic_list = []
        attendees_list = []

        for index in range(len(mail)):
            # topic of the meeting 
            subject = mail['Subject'].iloc[index]
            body = mail['Body'].iloc[index]
            topic_prompt = 'Response should be one sentence only, no other explanation: just the topic for the meeting.\n' + subject + body + "\nDon't add any other information in the response.\nGive the responese inside curly braces)"
            topic = bard.get_answer(topic_prompt)['content']
            topic = re.search(r'{(.*?)}', topic).group(1)

            # get the attendees mail id
            attendees = mail['Sender ID'].iloc[index]
            attendees_email_address = re.search(r'[\w\.-]+@[\w\.-]+', attendees).group(0)

            # append the topic to the list
            topic_list.append(topic)
            attendees_list.append(attendees_email_address)



        # add the topic to the dataframe
        mail['Topic'] = pd.Series(topic_list).tolist()
        mail['Attendees'] = pd.Series(attendees_list).tolist()

        return mail

