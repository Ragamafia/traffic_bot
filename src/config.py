from datetime import datetime, timedelta, timezone

URL = 'https://iktport.ru/ru/passengers/shortdates-ru.html?DayKey=+0'

compare_flights = 33

offset_ago = timedelta(hours=6)
offset_later = timedelta(hours=10)

def get_time():
    start_time = datetime.now(timezone(offset_ago)).strftime("%H:%M")
    end_time = datetime.now(timezone(offset_later)).strftime("%H:%M")

    return start_time, end_time

start_time, end_time = get_time()
