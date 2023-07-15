import pandas as pd
import re
from dateutil import parser
from datetime import datetime, timedelta

class analyze:
    def __init__(self, unread_mail_df):
        self.unread_mail_df = unread_mail_df

    def qualify_the_mail(self):
        # define the keywords
        keywords = ['Zoom','Meeting','Link','Meeting ID','Password','Meeting Password','Meeting Link','Zoom Link','Zoom Meeting']

        # create a empty dataframe to store the qualified mails
        qualified_mails = self.unread_mail_df[self.unread_mail_df['Body'].str.contains('|'.join(keywords))]

        return qualified_mails
    
    def extract_date_and_time(self,qualified_mails):
        # empty list to store the date time and Duration
        date_and_time_list = []
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
            date_and_time = datetime.strptime(str(date) + " " + time, '%Y-%m-%d %I:%M %p')

            # append the date time and duration to the list
            date_and_time_list.append(date_and_time)
            duration_list.append(duration)

        # add the date and time and duration to the dataframe
        linkReqMails = qualified_mails.drop('Body',axis=1)
        linkReqMails['Date and Time'] = pd.Series(date_and_time_list).tolist()
        linkReqMails['Duration'] = pd.Series(duration_list).tolist()

        return linkReqMails

