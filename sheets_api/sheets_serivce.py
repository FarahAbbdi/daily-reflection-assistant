from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from datetime import datetime
from zoneinfo import ZoneInfo

# Returns an authenticated Google Sheets API service
def get_sheets_service(creds):
    return build("sheets", "v4", credentials=creds)

# Returns latest reflection text from google sheets
def get_latest_reflection(service, spreadsheet_id, range_name, today):
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

        # Loop through rows (skips header)
        for row in reversed(values[1:]): 
            timestamp_str = row[0] # timestamp column
            reflection_text = row[1] # reflection text column

            mel_tz = ZoneInfo("Australia/Melbourne")
            timestamp = datetime.strptime(timestamp_str, "%m/%d/%Y %H:%M:%S").replace(tzinfo=mel_tz)
            today = datetime.now(mel_tz).date()

            if timestamp.date() == today:
                    return reflection_text
        
        return None # No reflection found for today

    except HttpError as error:
        print(f"An error occurred: {error}")
        return None