import config as cfg


def generate_message(filtered_flights):
    total = len(filtered_flights["arrival"]) + len(filtered_flights["departure"])

    if total >= cfg.compare_flights:
        compare_word, message = "более", "Возможно затруднение движения"
    else:
        compare_word, message = "менее", "Дорога у Аэропорта свободна"

    return (
        '<code>'
        f'Time: {cfg.start_time} - {cfg.end_time}\n'
        f'Arrival: {len(filtered_flights["arrival"])}\n'
        f'Departure: {len(filtered_flights["departure"])}\n'
        f'Total flights: {total}\n'
        f'Ожидается {compare_word} {cfg.compare_flights} рейсов. {message}'
        '</code>'
    )
