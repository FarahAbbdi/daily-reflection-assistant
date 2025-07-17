from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from datetime import datetime
from zoneinfo import ZoneInfo

def get_sheets_service(creds):
    """Build and return the Google Calendar API service."""
    return build("sheets", "v4", credentials=creds)

def get_latest_reflection(service, spreadsheet_id, range_name):
    """Fetch latest reflection text from google sheets"""
    try:
        result = (
            service.spreadsheets()
            .values()
            .get(spreadsheetId=spreadsheet_id, range=range_name)
            .execute()
        )

        values = result.get("values", [])
        if not values or len(values) < 2:
            return None
        
        # Current date in Melbourne timezone
        mel_tz = ZoneInfo("Australia/Melbourne")
        today = datetime.now(mel_tz).date()

        # Loop through rows (skip header)
        for row in reversed(values[1:]):  # Start from last entry
            timestamp_str = row[0] 
            reflection_text = row[1]

            mel_tz = ZoneInfo("Australia/Melbourne")
            timestamp = datetime.strptime(timestamp_str, "%m/%d/%Y %H:%M:%S").replace(tzinfo=mel_tz)
            today = datetime.now(mel_tz).date()

            if timestamp.date() == today:
                    return reflection_text
        
        return None

    except HttpError as error:
        print(f"An error occurred: {error}")
        return None