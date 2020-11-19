import os
import time
from datetime import datetime
import pandas as pd
import pyautogui

from helpers import *


def join_meeting(id, password):
     # This function will open up zoom, and join the meeting using the given id and password
    os.popen('zoom')
    time.sleep(15)
    clickOnImage('images/join_button.png')


    time.sleep(2)
    clickOnImage('images/id_box.png')
    pyautogui.write(id)

    clickOnMultipleImage('images/checkbox.png')

    clickOnImage('images/join2_button.png')
    
    time.sleep(5)
    clickOnImage('images/password_field.png')
    pyautogui.write(password)
    pyautogui.press('enter')

def get_current_meeting(meetings):
    now = datetime.now().strftime('%H:%M')
    if now in str(meetings['time']):
        row = meetings.loc[meetings['time'] == now]
        meeting_id = str(row.iloc[0,0])
        meeting_password = str(row.iloc[0,1])
        return meeting_id, meeting_password

while True:
    meetings = pd.read_csv('meetings.csv')
    current_meeting = get_current_meeting(meetings)
    if current_meeting is not None:
        meeting_id, meeting_password = current_meeting
        join_meeting(meeting_id, meeting_password)
    clickOnImage('images/ok_button.png')