import datetime

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
from obsidian.obsidian_sync import save_markdown_to_obsidian

# Constants
SPREADSHEET_ID = "1lCGerTSAFwgQa8WArFFcmQorlO6K2QINrhKEWQFF8Pc"
RANGE_NAME = "Form Responses 1!A:B"  # Column A: Timestamp, Column B: Reflection
FORM_URL = (
    "https://docs.google.com/forms/u/0/d/e/1FAIpQLSdx42543jkBPucHV2gE-fhOXXN4CgIl4NOB2hJKD4d2JJUnYw/formResponse"
)

def main():
    # 1. Authenticate and initialize services
    creds = get_credentials()
    calendar_service = get_calendar_service(creds)
    sheets_service = get_sheets_service(creds)

    # 2. Get time range (midnight to 9 PM Melbourne time)
    time_min, time_max = get_range_for_date()
    today_str = time_min.split("T")[0]

    # 3. Fetch latest reflection from Google Sheets
    reflection_text = get_latest_reflection(sheets_service, SPREADSHEET_ID, RANGE_NAME, time_min)
    if reflection_text:
        print(f"Latest reflection: {reflection_text}")
    else:
        print("No reflection submitted yet.")

    # 4. Fetch today's calendar events
    events = get_today_events(calendar_service, time_min, time_max)
    event_summaries = []
    if not events:
        print("No events found for today.")
    else:
        print("\nToday's Events:")
        for event in events:
            start = event["start"].get("dateTime", event["start"].get("date"))
            summary = f"- {start}: {event['summary']}"
            print(summary)
            event_summaries.append(summary)

    # 5. Create or update the Daily Reflection event in Google Calendar
    create_reflection_event(calendar_service, FORM_URL)

    # 6. Save data to Obsidian markdown file
    vault_path = input("Enter Vault_path: ")
    save_markdown_to_obsidian(today_str, event_summaries, reflection_text or "No reflection submitted.", vault_path)



if __name__ == "__main__":
    main()