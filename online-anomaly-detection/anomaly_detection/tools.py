import random
from datetime import date

# setting the default weight of express
default_weight = [1.0 for x in range(7)]
default_weight[0] = 0

# get the day, weekday, month, season, year of a date object
def split_date(current_date: date):
    day = current_date.day
    weekday = current_date.weekday() + 1
    month = current_date.month
    season = (current_date.month - 1) // 3 + 1
    year = current_date.year
    return year, season, month, weekday, day

# fellow the express y = year * w1 + season * w2 + month * w3 + weekday * w4 + day * w5 + t * w6 calculate the data
def original_express(year, season, month, weekday, day, count, weight=None):
    if weight is None:
        weight = default_weight
    print(weight)
    return year * weight[0] + season * weight[1] + month * weight[2] + weekday * weight[3] + day * weight[4] + count * \
        weight[5]
