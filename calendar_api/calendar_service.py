from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from utils.utils import get_event_time

# Returns an authenticated Google Calendar API service
def get_calendar_service(creds):
    return build("calendar", "v3", credentials=creds)

# Returns events from primary calendar between given start and end times
def get_today_events(service, time_min, time_max):
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


# Create or update a daily reflection event at 9 PM Melbourne time with form URL
def create_reflection_event(service, form_url):
    # Refection time range: 9 PM to 9:30 PM
    start_time, end_time = get_event_time(21, 0, 30)  # 9 PM, 30 mins

    # Event body
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

    #  Search if today's reflection event already exists
    events = service.events().list(
        calendarId="primary",
        timeMin=start_time,
        timeMax=end_time,
        q="Daily Reflection",
        singleEvents=True,
        orderBy="startTime"
    ).execute().get("items", [])

    if events:
        event_id = events[0]["id"]
        updated_event = service.events().update(calendarId="primary", eventId=event_id, body=event_body).execute()
    else: 
        created_event = service.events().insert(calendarId="primary", body=event_body).execute()