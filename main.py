import os
from dotenv import load_dotenv

from auth.auth import get_credentials
from calendar_api.calendar_service import (
    get_calendar_service,
    get_today_events,
    create_reflection_event,
)
from sheets_api.sheets_serivce import (
    get_sheets_service,
    get_latest_reflection,
)
from utils.utils import get_range_for_date
from utils.file_export import export_daily_review_to_markdown

# Load environment variables from .env file
load_dotenv()

SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
FORM_URL = os.getenv("FORM_URL")
VAULT_PATH = os.getenv("VAULT_PATH")
RANGE_NAME = "Form Responses 1!A:B"  # Column A: Timestamp, Column B: Reflection


def main():
    # 1. Authenticate and initialize API services
    creds = get_credentials()
    calendar_service = get_calendar_service(creds)
    sheets_service = get_sheets_service(creds)

    # 2. Get time range (midnight to 9 PM Melbourne time)
    time_min, time_max = get_range_for_date()
    today_str = time_min.split("T")[0]

    # 3. Fetch latest reflection from Google Sheets
    reflection_text = get_latest_reflection(sheets_service, SPREADSHEET_ID, RANGE_NAME, time_min)
    # TODO: LEAVE FOR DEBUGGING REMOVE LATER
    print(f"Latest reflection: {reflection_text}" if reflection_text else "No reflection submitted yet.")
        
    # 4. Fetch today's calendar events
    # TODO: REMOVE PRINT STATEMENTS
    events = get_today_events(calendar_service, time_min, time_max)
    event_summaries = []
    if not events:
        print("No events found for today.")
    else:
        print("\nToday's Events:")
        for event in events:
            summary = f"{event['summary']}"
            print(summary) # FOR DEBUGGING
            event_summaries.append(summary)

    # 5. Create or update the Daily Reflection event in Google Calendar
    create_reflection_event(calendar_service, FORM_URL)

    # 6. Export daily review (events and reflection) as a markdown file to the specified path
    export_daily_review_to_markdown(today_str, event_summaries, reflection_text or "No reflection submitted.", VAULT_PATH)


if __name__ == "__main__":
    main()