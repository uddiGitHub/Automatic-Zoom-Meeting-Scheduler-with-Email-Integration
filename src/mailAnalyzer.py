import pandas as pd
class analyze:
    def __init__(self, unread_mail_df):
        self.unread_mail_df = unread_mail_df

    def qualify_the_mail(self):
        # define the keywords
        keywords = ['Zoom','Meeting','Link','Meeting ID','Password','Meeting Password','Meeting Link','Zoom Link','Zoom Meeting']

        # create a empty dataframe to store the qualified mails
        qualified_mails = self.unread_mail_df[self.unread_mail_df['Body'].str.contains('|'.join(keywords))]

        return qualified_mails
    
    def extract_date_and_time(qualified_mails):
        return 0

