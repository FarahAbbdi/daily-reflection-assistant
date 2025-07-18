from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

def get_range_for_date():
    """
    Get the time range for today (midnight to 9 PM) in the Australia/Melbourne timezone.

    Returns:
        tuple: A tuple containing two ISO 8601 timestamp strings:
            - start_of_day (str): Midnight of the current day.
            - nine_pm (str): 9:00 PM of the current day.
    """
    tz = ZoneInfo("Australia/Melbourne")
    now = datetime.now(tz)

    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    nine_pm = now.replace(hour=21, minute=0, second=0, microsecond=0)

    return start_of_day.isoformat(), nine_pm.isoformat()

def get_event_time(hour: int, minute: int = 0, duration_minutes: int = 30):
    """
    Generate start and end time for an event in Australia/Melbourne timezone.

    Args:
        hour (int): The hour of the event start time (24-hour format).
        minute (int, optional): The minute of the event start time. Defaults to 0.
        duration_minutes (int, optional): Duration of the event in minutes. Defaults to 30.

    Returns:
        tuple: A tuple containing two ISO 8601 timestamp strings:
            - start_time (str): Event start time.
            - end_time (str): Event end time.
    """
    tz = ZoneInfo("Australia/Melbourne")
    start_time = datetime.now(tz).replace(hour=hour, minute=minute, second=0, microsecond=0)
    end_time = start_time + timedelta(minutes=duration_minutes)

    return start_time.isoformat(), end_time.isoformat()