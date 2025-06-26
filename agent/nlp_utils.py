from dateutil import parser as date_parser
from pytz import timezone

IST = timezone("Asia/Kolkata")

def extract_datetime(user_input):
    try:
        dt = date_parser.parse(user_input, fuzzy=True)
        return IST.localize(dt)
    except:
        return None

def is_booking_request(text):
    keywords = [
        'book', 'schedule', 'set up', 'make an appointment', 'reserve',
        'fix a time', 'create meeting', 'add to calendar', 'arrange',
        'put on my calendar', 'organize meeting', 'block time', 'set a meeting'
    ]
    return any(k in text.lower() for k in keywords)


def is_availability_request(text):
    keywords = [
        'free', 'available', 'open slots', 'when can i', 'check my calendar',
        'do i have time', 'am i busy', 'is my calendar free', 'see my schedule',
        'do i have availability', 'am i free', 'check schedule'
    ]
    return any(k in text.lower() for k in keywords)

