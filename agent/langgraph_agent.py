from datetime import timedelta
from agent.nlp_utils import extract_datetime, is_booking_request, is_availability_request
from backend.calendar_utils import get_events, create_event
from dateutil import parser as date_parser

def langgraph_agent(user_input):
    target_dt = extract_datetime(user_input)

    if not target_dt:
        return "Please provide a valid date and time for me to help."

    # Check availability
    if is_availability_request(user_input):
        events = get_events(target_dt, target_dt + timedelta(hours=1))
        for e in events:
            ev_start = date_parser.parse(e['start'].get('dateTime'))
            ev_end = date_parser.parse(e['end'].get('dateTime'))
            if ev_start <= target_dt < ev_end:
                return f"You already have a meeting from {ev_start.strftime('%I:%M %p')} to {ev_end.strftime('%I:%M %p')}."
        return f"You are free around {target_dt.strftime('%I:%M %p')}!"

    # Book meeting
    elif is_booking_request(user_input):
        events = get_events(target_dt, target_dt + timedelta(hours=1))
        for e in events:
            ev_start = date_parser.parse(e['start'].get('dateTime'))
            ev_end = date_parser.parse(e['end'].get('dateTime'))
            if ev_start <= target_dt < ev_end:
                return f"You're busy from {ev_start.strftime('%I:%M %p')} to {ev_end.strftime('%I:%M %p')}. Please try another slot."

        create_event(target_dt, target_dt + timedelta(hours=1))
        return f"✅ Meeting scheduled on {target_dt.strftime('%A, %B %d at %I:%M %p')}."

    # Fallback
    else:
        return "I can help you check availability or book a slot. Just tell me what time you're looking for!"
