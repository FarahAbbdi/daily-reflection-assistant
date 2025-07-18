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
from utils.file_export import export_ai_report_to_markdown
from ai.ai_analyser import analyze_daily_reflection

# Load environment variables from .env file
load_dotenv()

SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
FORM_URL = os.getenv("FORM_URL")
VAULT_PATH = os.getenv("VAULT_PATH")
RANGE_NAME = "Form Responses 1!A:H"


def main():
    # 1. Authenticate and initialize API services
    creds = get_credentials()
    calendar_service = get_calendar_service(creds)
    sheets_service = get_sheets_service(creds)

    # 2. Get time range (midnight to 9 PM Melbourne time)
    time_min, time_max = get_range_for_date()
    today_str = time_min.split("T")[0]

    # 3. Fetch latest reflection from Google Sheets
    reflection_data = get_latest_reflection(sheets_service, SPREADSHEET_ID, RANGE_NAME, time_min)
        
    # 4. Fetch today's calendar events
    events = get_today_events(calendar_service, time_min, time_max)
    event_summaries = [event['summary'] for event in events] if events else []

    # 5. Create or update the Daily Reflection event in Google Calendar
    create_reflection_event(calendar_service, FORM_URL)

    # 6. Analyze reflection data with AI
    markdown_report = analyze_daily_reflection(reflection_data, event_summaries)

    # 7. Export AI-generated markdown report
    saved_path = export_ai_report_to_markdown(today_str, markdown_report, VAULT_PATH)
    print(f"AI analysis report saved to: {saved_path}")

if __name__ == "__main__":
    main()