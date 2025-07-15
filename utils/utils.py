from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

def get_range_for_date():
    """Return ISO timestamps for today midnight and 9 PM in Australia/Melbourne timezone."""
    tz = ZoneInfo("Australia/Melbourne")
    now = datetime.now(tz)

    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    nine_pm = now.replace(hour=21, minute=0, second=0, microsecond=0)

    # Return ISO 8601 strings with timezone info
    return start_of_day.isoformat(), nine_pm.isoformat()

def get_event_time(hour: int, minute: int = 0, duration_minutes: int = 30):
    tz = ZoneInfo("Australia/Melbourne")
    start_time = datetime.now(tz).replace(hour=hour, minute=minute, second=0, microsecond=0)
    end_time = start_time + timedelta(minutes=duration_minutes)

    return start_time.isoformat(), end_time.isoformat()