import datetime

from .tools import split_date, original_express, z_score
import random


def get_history_data(weight=None):
    result_list = []
    x_list = []
    color = []
    normal_list = []
    start_date = datetime.date(2020, 1, 1)
    end_date = datetime.date(2020, 12, 31)
    delta = datetime.timedelta(days=1)
    if weight is not None:
        for index in range(7):
            weight[index] = float(weight[index])
    print(weight)
    count = 0
    while start_date <= end_date:
        year, season, month, weekday, day = split_date(start_date)
        y_est = original_express(year, season, month, weekday, day, count, weight)
        count += 1
        if random.random() < 0.05:
            y_tar = random.random() * 500
        else:
            y_tar = original_express(year, season, month, weekday, day, count,
                                     weight=weight) + random.random() * 1 - 0.5
        result_list.append(y_tar)
        x_list.append(start_date.strftime('%Y/%m/%d'))

        color.append(z_score(normal_list, y_est - y_tar))
        start_date += delta

    return result_list, x_list, color
