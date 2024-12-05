import time

import requests
from bs4 import BeautifulSoup

import src.config as cfg


def get_flights():
    response = requests.get(cfg.URL)
    soup = BeautifulSoup(response.text, 'lxml')
    flights = {}
    for section in soup.find_all("tbody"):
        section_type = section.get("id").lower()
        flights[section_type] = []

        for index, line in enumerate(section.find_all("tr")):
            *_, time, status = [d.text for d in line.find_all("div")]
            flights[section_type].append((time))

    return flights


def check_total_flights(flights):
    time_list = []
    for i in flights.values():
        for b in i:
            time_list.append(time.strftime(b))

    filtered_flight = [
        flight for flight in time_list if cfg.start_time <= flight <= cfg.end_time
        ]
    print(len(filtered_flight))
    if len(filtered_flight) >= cfg.compare_flights:
        return True
    else:
        return False
