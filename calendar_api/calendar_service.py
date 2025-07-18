from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from utils.utils import get_event_time


def get_calendar_service(creds):
    """
    Initialize and return a Google Calendar API service instance.

    Args:
        creds (google.oauth2.credentials.Credentials): Authorized user credentials.

    Returns:
        Resource: A Google Calendar API service object.
    """
    return build("calendar", "v3", credentials=creds)


def get_today_events(service, time_min, time_max):
    """
    Fetch all events from the primary calendar within the specified time range.

    Args:
        service (Resource): Google Calendar API service instance.
        time_min (str): Start time in ISO 8601 format (e.g., '2025-07-18T00:00:00+10:00').
        time_max (str): End time in ISO 8601 format (e.g., '2025-07-18T21:00:00+10:00').

    Returns:
        list: A list of event objects. Empty list if no events are found.
    """
    try:    
        print("Fetching today's events from Google Calendar...")
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


def create_reflection_event(service, form_url):
    """
    Create or update a 'Daily Reflection' event at 9 PM Melbourne time in Google Calendar.
    If the event already exists for today, it will be updated.

    Args:
        service (Resource): Google Calendar API service instance.
        form_url (str): URL to the reflection form to include in the event description.

    Returns:
        dict: The created or updated event object.
    """
    # Define reflection event time range (9:00 PM to 9:30 PM)
    start_time, end_time = get_event_time(21, 0, 30)  # 9 PM, 30 mins

    event_body = {
        "summary": "Daily Reflection",
        "description": f"Submit your reflection here: {form_url}",
        "colorId": "6",
        "start": {
            "dateTime": start_time,
            "timeZone": "Australia/Melbourne",
        },
        "end": {
            "dateTime": end_time,
            "timeZone": "Australia/Melbourne",
        },
    }

    try:
        # Check if today's reflection event already exists
        events = (
            service.events()
            .list(
                calendarId="primary",
                timeMin=start_time,
                timeMax=end_time,
                q="Daily Reflection",
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
            .get("items", [])
        )

        if events:
            event_id = events[0]["id"]
            return service.events().update(calendarId="primary", eventId=event_id, body=event_body).execute()
        else: 
            return service.events().insert(calendarId="primary", body=event_body).execute()
        
    except HttpError as error:
        print(f"An error occurred while creating/updating the event: {error}")
        return None