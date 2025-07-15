from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from utils.utils import get_event_time

def get_calendar_service(creds):
    """Build and return the Google Calendar API service."""
    return build("calendar", "v3", credentials=creds)

def get_today_events(service, time_min, time_max):
    """Fetch events between time_min and time_max from the primary calendar."""
    try:    
        print("Getting all events today")
        events_result = (
            service.events()
            .list(
                calendarId="primary",
                timeMin=time_min,
                timeMax=time_max,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )
        return events_result.get("items", [])
    except HttpError as error:
        print(f"An error occurred: {error}")

def create_reflection_event(service):
    """Create a reflection event in Google Calendar at 9 PM Melbourne time."""

    start_time, end_time = get_event_time(21, 0, 30)  # 9 PM, 30 mins

    event = {
        "summary": "Daily Reflection",
        "description": "Click the link to add your thoughts for today.",
        "colorId": "6",  # Blue
        "start": {
            "dateTime": start_time,
            "timeZone": "Australia/Melbourne",
        },
        "end": {
            "dateTime": end_time,
            "timeZone": "Australia/Melbourne",
        },
    }

    # Insert the event into the primary calendar
    created_event = service.events().insert(calendarId="primary", body=event).execute()
    print(f"Reflection event created: {created_event.get('htmlLink')}")