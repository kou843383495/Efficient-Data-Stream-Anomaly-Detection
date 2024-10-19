from datetime import date
import random

i_val_1 = random.random()
i_val_2 = random.random()

w1 = random.random()
w2 = random.random()
w3 = random.random()
w4 = random.random()
w5 = random.random()
w6 = random.random()
w7 = random.random()


def split_date(current_date:date):
    day = current_date.day
    weekday = current_date.weekday() + 1
    month = current_date.month
    season = (current_date.month - 1) // 3 + 1
    year = current_date.year
    return year, season, month, weekday, day


def original_express(year, season, month, weekday, day):
    return year * w1 + season * w2 + month * w3 + weekday * w4 + day * w5 + i_val_1 * w6 + i_val_2 * w7