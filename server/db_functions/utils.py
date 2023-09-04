from datetime import datetime

def get_str_date(date: datetime):
    now = datetime.now()
    if now.year != date.year:
        return date.strftime("%H:%M:%S %d.%m.%Y")
    if now.date() == date.date():
        return "today"
    return date.strftime("%H:%M:%S %d.%m")