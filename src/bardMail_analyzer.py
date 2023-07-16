import os
import re
import spacy
import pandas as pd
from credentials import bard_api_key
from bardapi import Bard
from dateutil import parser
from datetime import datetime, timedelta

# load the spacy model
nlp = spacy.load("en_core_web_sm")

# set the API key
os.environ["_BARD_API_KEY"] = bard_api_key

class bardAnalyzer:
    def __init__(self, unread_mail_df):
        self.unread_mail_df = unread_mail_df

    # use chatGPT API to analyze the mail
    def analyze_the_mail(self):
        # list
        qualifiedResponse_list = []
        for index in range(len(self.unread_mail_df)):
            # get the body of the mail
            body = self.unread_mail_df['Body'].iloc[index]

            # set the prompt
            prompt = 'Response should be one token only, no other explanation: just "Yes" or "No": Is this mail a meeting request?\n' + body + "\nDon't add any other information in the response.(Yes/No)\n)"

            # call the API
            bard = Bard()
            qualifyResponse = bard.get_answer(prompt)['content']
            qualifyResponse_token = nlp(qualifyResponse)[0].text

            # append the response to the list
            qualifiedResponse_list.append(qualifyResponse_token)

        # add the response to the dataframe
        qualified_mails = self.unread_mail_df.copy()
        qualified_mails['Response'] = pd.Series(qualifiedResponse_list).tolist()

        # filter the mails based on the response
        qualified_mails = qualified_mails[qualified_mails['Response'] == 'Yes']

        return qualified_mails
    
    def extract_date_and_time(self,qualified_mails):
        # empty list to store the date time and Duration
        date_list = []
        time_list = []
        duration_list = []

        for index in range(len(qualified_mails)):
            # get the body of the mail
            body = qualified_mails['Body'].iloc[index]

            # find the date from the body
            date = parser.parse(body, fuzzy=True).date()
            # date = parser.parse(body, fuzzy_with_tokens=True, dayfirst=True).date()


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

            # convert the date and time to datetime format
            # date_and_time = datetime.strptime(str(date) + " " + time, '%Y-%m-%d %I:%M %p')


            # append the date time and duration to the list
            # date_and_time_list.append(date_and_time)
            date_list.append(date)
            time_list.append(time)
            duration_list.append(duration)

        # add the date and time and duration to the dataframe
        linkReqMails = qualified_mails.drop('Body',axis=1)
        linkReqMails['Date'] = pd.Series(date_list).tolist()
        linkReqMails['Time'] = pd.Series(time_list).tolist()
        linkReqMails['Duration'] = pd.Series(duration_list).tolist()

        return linkReqMails