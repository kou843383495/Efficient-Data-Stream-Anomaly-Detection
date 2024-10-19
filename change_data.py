import datetime
from tools import split_date
import random

start_date = datetime.date(2021, 1, 1)
end_date = datetime.date(2024, 12, 31)

delta = datetime.timedelta(days=1)

total_sum = 0

result_list = []

while start_date <= end_date:
    year, season, month, weekday, day = split_date(start_date)

    i_val_1 = random.random()
    i_val_2 = random.random()

    w1 = random.random()
    w2 = random.random()
    w3 = random.random()
    w4 = random.random()
    w5 = random.random()
    w6 = random.random()
    w7 = random.random()

    y = year * w1 + season * w2 + month * w3 + weekday * w4 + day * w5 + i_val_1 * w6 + i_val_2 * w7 + random.random() * 10 - 5

    y_real = year * w1 + season * w2 + month * w3 + weekday * w4 + day * w5 + i_val_1 * w6 + i_val_2 * w7

    result_list.append((y - y_real) ** 2)

    print(
        f'year: {year} - season: {season} - month: {month} - weekday: {weekday} - day: {day} - label: {y} - y_real: {y_real}')
    start_date += delta
