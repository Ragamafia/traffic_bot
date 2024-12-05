from src.parser import get_flights, check_total_flights
import src.config as cfg


def create_message():
    if check_total_flights(get_flights()):
        traffic = f'С {cfg.start_time} до {cfg.end_time} прибывает и убывает более {cfg.compare_flights} авиарейсов.' \
                  f'\nВ районе Аэропорта возможно затруднение движения.'
    else:
        traffic = f'С {cfg.start_time} до {cfg.end_time} ожидается менее {cfg.compare_flights} авиарейсов.' \
                  f'\n.Дорога у Аэропорта свободна.'
    return traffic