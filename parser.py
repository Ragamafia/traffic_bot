import re

import requests
from bs4 import BeautifulSoup

import config as cf


response = requests.get(cf.URL)
soup = BeautifulSoup(response.text, 'lxml')


def count_flight(tag, start_time, end_time):
    flights = soup.find_all(id=tag)
    for i in flights:
        time = re.findall(cf.pattern, i.text)
        time_list = [f"{h}:{m}" for h, m in time]
        filtered_times = [
            time for time in time_list if start_time <= time <= end_time
        ]
        return filtered_times


def waring(num_arrival, num_departure, start_time, end_time, fligths):
    if len(num_arrival + num_departure) >= 10:
        print(f'С {start_time} до {end_time} ожидается {fligths} рейсов. Движение затруднено')
    else:
        print(f'С {start_time} до {end_time} ожидается {fligths} рейсов. Дорога свободна')


arrival = count_flight(cf.tag_arrival, cf.start_time, cf.end_time)
departure = count_flight(cf.tag_departure, cf.start_time, cf.end_time)


if __name__ == '__main__':
    waring(arrival, departure, cf.start_time, cf.end_time, cf.flights)
