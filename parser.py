import re

import requests
from bs4 import BeautifulSoup

import config as cfg


response = requests.get(cfg.URL)
soup = BeautifulSoup(response.text, 'lxml')


def count_flight(tag, start_time, end_time):

    flights = soup.find_all(id=tag)
    for i in flights:
        print(i.text)
        time = re.findall(cfg.pattern, i.text)
        time_list = [f"{h}:{m}" for h, m in time]
        print(time_list)
        print(len(time_list))
        filtered_times = [
            time for time in time_list if start_time <= time <= end_time
        ]
        print(filtered_times)
        return filtered_times


def waring(total):
    print(f'С {cfg.start_time} до {cfg.end_time} ожидается {total} рейсов.')
    if total >= cfg.compare_flights:
        print('Движение затруднено')
    else:
        print('Дорога свободна')


arrival = count_flight(cfg.tag_arrival, cfg.start_time, cfg.end_time)
departure = count_flight(cfg.tag_departure, cfg.start_time, cfg.end_time)
total = len(arrival + departure)


if __name__ == '__main__':
    waring(total)
