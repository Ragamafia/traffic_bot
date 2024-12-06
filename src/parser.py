import requests
from bs4 import BeautifulSoup

import config as cfg


def get_flights():  # получаем полный список рейсов с онлайн-табло аэропорта
    flights = {}

    response = requests.get(cfg.URL)
    soup = BeautifulSoup(response.text, 'lxml')

    for section in soup.find_all("tbody"):
        section_type = section.get("id").lower()
        flights[section_type] = []

        for index, line in enumerate(section.find_all("tr")):
            *_, time, status = [d.text for d in line.find_all("div")]
            flights[section_type].append(time)

    return flights


def select_flights(flights):    # отбор рейсов в заданном временном промежутке
    filtered_flights = {}

    for k, v in flights.items():
        filtered_flights[k] = [
            select for select in v if cfg.start_time <= select <= cfg.end_time
        ]

    return filtered_flights


filtered_flights = select_flights(get_flights())
