# Automatic-Zoom-Meeting-Scheduler-with-Email-Integration
This is an advanced Robotic Process Automation (RPA) bot designed to seamlessly automate the entire Zoom meeting scheduling process. The bot efficiently handles meeting requests received via Gmail and leverages the Zoom platform to schedule the meetings. Additionally, it effortlessly manages the distribution of meeting links to all intended attendees, streamlining the entire process for optimal efficiency and productivity.

### Results
Upon executing the [main.py](https://github.com/uddiGitHub/Automatic-Zoom-Meeting-Scheduler-with-Email-Integration/blob/main/src/main.py)  script with the appropriate credentials, the Robotic Process Automation (RPA) bot demonstrates remarkable proficiency in scheduling Zoom meetings and promptly dispatching the meeting links to attendees via email. Presented below is a representative output exemplifying the entire process.
> **Authenticating Gmail and Retrieving Emails**


https://github.com/uddiGitHub/Automatic-Zoom-Meeting-Scheduler-with-Email-Integration/assets/102317373/33425de0-2fe4-40c9-a1ca-9cc6cf6a70b1


> **Logging into Zoom Platform and Scheduling Meeting**


https://github.com/uddiGitHub/Automatic-Zoom-Meeting-Scheduler-with-Email-Integration/assets/102317373/bbfa0e82-ad67-4c41-8d1f-51b91c840d2e


> **Accessing Gmail Again and Sending the Meeting Link**


https://github.com/uddiGitHub/Automatic-Zoom-Meeting-Scheduler-with-Email-Integration/assets/102317373/b5d343a4-9790-495e-b48e-12a9f18bf90f



### Prerequisites
1. **Python 3.10.6 or greater:** To install Python, refer to the official Python website for the latest version. [Official website link](https://www.python.org/)
2. **Selenium:** Install the Selenium library using the following command:<br> `pip install selenium`
3. **Webdriver Manager:** Install the Webdriver Manager using the following command:<br> `pip install webdriver-manager`
4. **Pandas:** Install the Pandas library using the following command:<br> `pip install pandas`
5. **Bardapi:** Install the Bardapi library using the following command:<br> `pip install bardapi`
6. **PyAutoGUI:** Install the PyAutoGUI library using the following command:<br> `pip install pyautogui`
7. **Pyperclip:** Install the Pyperclip library using the following command:<br> `pip install pyperclip`

Alternatively, you can run the [prerequisite.py](https://github.com/uddiGitHub/Automatic-Zoom-Meeting-Scheduler-with-Email-Integration/blob/main/prerequisite.py) file available in this repository to automatically install all the required prerequisites.

### How to Use
1. Clone this repository to your local machine.
2. Install all the prerequisites as mentioned above.
3. Set up your personalized credentials in the [credentials.py](https://github.com/uddiGitHub/Automatic-Zoom-Meeting-Scheduler-with-Email-Integration/blob/main/src/credentials.py) file.<br>Obtain your unique `bard_api_key` to enable smooth integration with Bard. For guidance on acquiring the `bard_api_key`, please refer to the comprehensive [YouTube video](https://youtu.be/kT8Q7aIlgy0) provided by KNOWLEDGE DOCTOR.
4. Run the [main.py](https://github.com/uddiGitHub/Automatic-Zoom-Meeting-Scheduler-with-Email-Integration/blob/main/src/main.py) script in your Python environment.

### Limitations
While the ***Automatic Zoom Meeting Scheduler with Email Integration*** is a powerful tool, it does have some limitations that users should consider:

1. **Dependency on Email Format:**<br> The bot currently relies on a specific format for meeting requests in the email body. Any deviation from the expected format might lead to inaccurate scheduling or errors in processing.<br>
Example Format:<br>
> Subject of the mail<br>
> `Request for Zoom Meeting: Project Discussion.`

> Body of the mail
```
Dear IOCL,

I hope this email finds you well. I would like to request a Zoom meeting to discuss an important project that requires your input and guidance. The meeting will provide an opportunity to go over the project details, address any concerns, and ensure that we are aligned on the next steps.

I propose the following details for the Zoom meeting:

Date: July 30, 2023
Time: 10:00 AM (GMT)
Duration: 1 hour

Please let me know if the suggested date and time work for you, or if you have any alternative suggestions. I believe your expertise and insights will be invaluable to the success of this project, and I look forward to our discussion.

Thank you for considering my request. I appreciate your time and cooperation.

Best regards,
```
2. **Email Language Support:**<br> The project primarily supports meeting requests received in English. It will not work with emails in other languages.
3. **Internet Connection Requirement:**<br> The bot requires a stable internet connection to access Gmail and Zoom platforms. It may not function correctly in offline or low-bandwidth situations.
4. **Selenium Compatibility:**<br> The bot relies on the Selenium library for web automation, and any significant changes to the web elements or paths in the Zoom or Gmail interfaces might cause the bot to fail.
5. **Security Considerations:**<br> As the project deals with email credentials and API keys, it's crucial to handle these sensitive details securely and follow best practices for securing credentials.

### Future Scope/Development
The ***Automatic-Zoom-Meeting-Scheduler-with-Email-Integration*** project has considerable potential for future developments and enhancements. Some key areas for further improvement include:
1. **AI-based Email Classification:**<br> Implementing an AI model for email classification can significantly enhance the bot's accuracy in distinguishing Zoom meeting requests from other emails, making it more versatile and robust.
2. **Smart Meeting Time Extraction:**<br> Replacing the current regular expression (re) based approach with advanced natural language processing (NLP) techniques can improve the accuracy of extracting meeting details from emails.
3. **User-friendly Configurations:**<br> Offering a user-friendly configuration interface to customize meeting preferences, such as default meeting duration, time zones, and invitation message templates, can improve user experience and customization options.

### Credit
This project was developed as part of an internship program at IOCL Guwahati in the year 2023. We extend our gratitude to IOCL Guwahati for providing the opportunity and support during the development process. Contributions and enhancements from the open-source community are warmly welcomed and greatly appreciated.

