# Date functionalities

import datetime
from datetime import timedelta, date, time


def temporada(x):

    case = x['fecha_i']
    time_case = case.date()
    year = case.year

    if date(year, 12, 15) <= time_case <= date(year, 12, 31):
        return 1
    if date(year, 1, 1) <= time_case <= date(year, 3, 3):
        return 1
    elif date(year, 7, 15) <= time_case <= date(year, 7, 31):
        return 1
    elif date(year, 11, 11) <= time_case <= date(year, 11, 30):
        return 1
    else:
        return 0


def atraso(x, mins):
    if x['dif_min'] > mins:
        return 1
    else:
        return 0


def periodo(x):

    time_case = x['fecha_i'].time()

    text = ''

    if time(5,00) <= time_case <= time(11,59):
        text = "mañana"

    elif time(12,00) <= time_case <= time(18,59):
        text = "tarde"

    else:
        text = "noche"

    return text


def delay_rate(df):
    rate = (df['atraso_15'].sum() / df['atraso_15'].count() ) * 100
    delay_rate_r = round(rate, 2)
    return delay_rate_r