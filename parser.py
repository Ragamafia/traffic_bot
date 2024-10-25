import json

import requests
from bs4 import BeautifulSoup

import config as cfg

STATUSES = {
    "прибыл": "arrived",
    "багаж": "baggage",
    "совершил посадку": "landed",
    "в пути": "in flight",
    "задержан": "delayed",
    "вылетел": "departed",
    "посадка окончена": "boarding closed",
    "посадка": "boarding",
    "регистрация закончена": "check-in closed",
    "регистрация": "check-in",
}

def get_flights():
    response = requests.get(cfg.URL)
    soup = BeautifulSoup(response.text, 'lxml')
    flights = {}
    for section in soup.find_all("tbody"):
        section_type = section.get("id").lower()
        flights[section_type] = []

        for index, line in enumerate(section.find_all("tr")):
            *_, time, status = [d.text for d in line.find_all("div")]
            status = STATUSES.get(status, "null")
            print(f"Found flight at {time} with status {status}")
            flights[section_type].append((time, status))

    return flights

def filter_flight(flights):
    for k, v in flights.items():
        filtered_flight = [
            time[0] for time in v if cfg.start_time <= time <= cfg.end_time # продумать фильтрацию рейсов по времени
            ]

        print(filtered_flight)


if __name__ == '__main__':
    flights = get_flights()
    print(json.dumps(flights, indent=4))
