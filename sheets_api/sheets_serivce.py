from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from datetime import datetime
from zoneinfo import ZoneInfo


def get_sheets_service(creds):
    """
    Initialize and return a Google Sheets API service instance.

    Args:
        creds (google.oauth2.credentials.Credentials): Authorized user credentials.

    Returns:
        Resource: A Google Sheets API service object.
    """
    return build("sheets", "v4", credentials=creds)


def get_latest_reflection(service, spreadsheet_id, range_name, today):
    """
    Retrieve the most recent reflection text for the current day from Google Sheets.

    Args:
        service (Resource): Google Sheets API service instance.
        spreadsheet_id (str): ID of the target spreadsheet.
        range_name (str): The range to read from the sheet (e.g., "Form Responses 1!A:B").
        today (str): Not used in current implementation (can be removed for clarity).

    Returns:
        str or None: The reflection text if found for today, otherwise None.
    """
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

        # Iterate over rows in reverse (latest first), skipping the header row
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
        print(f"An error occurred while fetching reflection: {error}")
        return None