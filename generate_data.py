import datetime

from change_data import y_real
from tools import split_date, original_express
import random

start_date = datetime.date(2010,1,1)
end_date = datetime.date(2020,12,31)

delta = datetime.timedelta(days=1)

total_sum = 0

result_list = []


while start_date <= end_date:
    year, season, month, weekday, day = split_date(start_date)

    y_est = original_express(year, season, month, weekday, day)

    y_tar = original_express(year, season, month, weekday, day) + random.random() * 10 - 5

    result_list.append(y_tar)

    print(f'year: {year} - season: {season} - month: {month} - weekday: {weekday} - day: {day} - diff: {result_list[-1]}')
    start_date += delta
