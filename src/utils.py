import config as cfg


def generate_message(filtered_flights):
    total = len(filtered_flights["arrival"]) + len(filtered_flights["departure"])

    message = (
        f'Interval: {cfg.start_time} - {cfg.end_time}\n'
        f'Arrival: {len(filtered_flights["arrival"])}\n'
        f'Departure: {len(filtered_flights["departure"])}\n'
        f'Total flight: {total}\n'
    )
    if total >= cfg.compare_flights:
        message += f'Ожидается более {cfg.compare_flights} рейсов. Возможно затруднение движения'
    else:
        message += f'Ожидается менее {cfg.compare_flights} рейсов. Дорога у Аэропорта свободна'

    return message
