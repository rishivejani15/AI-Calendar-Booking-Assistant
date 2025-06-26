from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime
import pytz
import os

SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = 'credentials/service-account.json'

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)

calendar_service = build('calendar', 'v3', credentials=credentials)
CALENDAR_ID = 'rishi15vejani2006@gmail.com'  # or your actual calendar ID

def get_events(start_dt, end_dt):
    start = start_dt.astimezone(pytz.utc).isoformat()
    end = end_dt.astimezone(pytz.utc).isoformat()

    events_result = calendar_service.events().list(
        calendarId=CALENDAR_ID,
        timeMin=start,
        timeMax=end,
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    return events_result.get('items', [])

def create_event(start_dt, end_dt):
    event = {
        'summary': 'Booked Meeting',
        'start': {
            'dateTime': start_dt.astimezone(pytz.utc).isoformat(),
            'timeZone': 'Asia/Kolkata',
        },
        'end': {
            'dateTime': end_dt.astimezone(pytz.utc).isoformat(),
            'timeZone': 'Asia/Kolkata',
        }
    }

    created_event = calendar_service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
    return created_event
