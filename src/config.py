from datetime import datetime, timedelta


URL = 'https://iktport.ru/ru/passengers/shortdates-ru.html?DayKey=+0'

compare_flights = 20


def get_time():
    start = datetime.now() - timedelta(hours=2)
    end = datetime.now() + timedelta(hours=3)
    two_hours_ago = start.strftime("%H:%M")
    three_hours_later = end.strftime("%H:%M")

    return two_hours_ago, three_hours_later

start_time, end_time = get_time()