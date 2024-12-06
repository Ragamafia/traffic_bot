from datetime import datetime, timedelta


URL = 'https://iktport.ru/ru/passengers/shortdates-ru.html?DayKey=+0'

compare_flights = 20


def get_time():
    start = datetime.utcnow() + timedelta(hours=6)
    end = datetime.utcnow() + timedelta(hours=10)
    hours_ago = start.strftime("%H:%M")
    hours_later = end.strftime("%H:%M")

    return hours_ago, hours_later

start_time, end_time = get_time()
