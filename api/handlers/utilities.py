from datetime import datetime, timezone, timedelta


def datetime_set_timezone(utc_hours: int) -> datetime:
    # Time zone in Thailand UTC+7
    tz = timezone(timedelta(hours=utc_hours))

    return datetime.now(tz=tz)