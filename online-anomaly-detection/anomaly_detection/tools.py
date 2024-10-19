import random
from datetime import date
import statistics as stat

i_val_1 = random.random()
i_val_2 = random.random()

default_weight = [1.0 for x in range(7)]

default_weight[0] = 0


def split_date(current_date: date):
    day = current_date.day
    weekday = current_date.weekday() + 1
    month = current_date.month
    season = (current_date.month - 1) // 3 + 1
    year = current_date.year
    return year, season, month, weekday, day


def original_express(year, season, month, weekday, day, count, weight=None):
    if weight is None:
        weight = default_weight
    print(weight)
    return year * weight[0] + season * weight[1] + month * weight[2] + weekday * weight[3] + day * weight[4] + count * \
        weight[5]

def z_score(diff_list,x):
    if len(diff_list) < 10:
        diff_list.append(x)
        return 'blue'
    mean = stat.mean(diff_list)
    std = stat.stdev(diff_list)
    if abs(x - mean) > 3 * std:
        return 'red'
    else:
        diff_list.append(x)
        if len(diff_list) > 100:
            diff_list.pop(0)
        return 'blue'
