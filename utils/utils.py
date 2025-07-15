import datetime
from zoneinfo import ZoneInfo

def get_range_for_date():
    """Return ISO timestamps for today midnight and 9 PM in Australia/Melbourne timezone."""
    tz = ZoneInfo("Australia/Melbourne")
    now = datetime.datetime.now(tz)

    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    nine_pm = now.replace(hour=21, minute=0, second=0, microsecond=0)

    # Return ISO 8601 strings with timezone info
    return start_of_day.isoformat(), nine_pm.isoformat()