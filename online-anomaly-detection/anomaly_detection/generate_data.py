import datetime

from .tools import split_date, original_express
from .detect_algorithm import z_score
import random

# According to the weight calculate a series date
def get_history_data(weight=None):
    result_list = []
    x_list = []
    color = []
    normal_list = []
    # the simulation period is from 2020/1/1 to 2020/12/31
    start_date = datetime.date(2020, 1, 1)
    end_date = datetime.date(2020, 12, 31)
    delta = datetime.timedelta(days=1)
    # Convert string which from the user update to float
    if weight is not None:
        for index in range(7):
            weight[index] = float(weight[index])
    print(weight)
    count = 0
    # each data point present a day
    while start_date <= end_date:
        year, season, month, weekday, day = split_date(start_date)
        # the predict value
        y_est = original_express(year, season, month, weekday, day, count, weight)
        count += 1
        # the real value which may be anomaly data or predict value add a random noise
        if random.random() < 0.02 and count >= 30:
            y_tar = random.random() * 500
        else:
            y_tar = original_express(year, season, month, weekday, day, count,
                                     weight=weight) + random.random() * 1 - 0.5
        result_list.append(y_tar)
        x_list.append(start_date.strftime('%Y/%m/%d'))

        color.append(z_score(normal_list, y_est - y_tar))
        start_date += delta
    # return the y,x,and color of each point
    return result_list, x_list, color
