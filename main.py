import datetime

from auth.auth import get_credentials
from calendar_api.calendar_service import get_calendar_service, get_today_events, create_reflection_event
from utils.utils import get_range_for_date

def main():
    # Authenticate and get Google API credentials
    creds = get_credentials()

    # Initialize Google Calendar API service
    service = get_calendar_service(creds)

    # Get start and end time (midnight to 9 PM Melbourne time)
    time_min, time_max = get_range_for_date()

    # Fetch today's events within the specifed range
    events = get_today_events(service, time_min, time_max)

    if not events:
        print("No upcoming events found.")
        return

    # Prints all events for today with start time and summary
    for event in events:
        start = event["start"].get("dateTime", event["start"].get("date"))
        print(start, event["summary"])

    # Creates Daily Reflection event in calendar
    create_reflection_event(service)

if __name__ == "__main__":
    main()