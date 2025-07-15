from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

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