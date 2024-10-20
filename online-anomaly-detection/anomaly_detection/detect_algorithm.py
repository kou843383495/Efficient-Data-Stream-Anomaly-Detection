import statistics as stat

diff_list = []
new_diff_list = []

# this function will calculate the z-score of current predict error with previous predict error list. If the z-score smaller than three,
# it means current date is not an anomaly date and color will be blue, otherwise the color will be red.
def z_score(x):
    # when diff_list less than 10 always return no anomaly, because not have enough to decide.
    if len(diff_list) < 10:
        diff_list.append(x)
        return 'blue'
    mean = stat.mean(diff_list)
    std = stat.stdev(diff_list)
    print(abs(x - mean) , std, len(diff_list))
    # when z-score greater than 3, the point should be an anomaly data. The diff_list will keep the recent 100 predict error.
    # when previous 50 point z-score greater than 3, we exchange diff list and consider it has a concept drift
    if abs(x - mean) > (3 * std):
        new_diff_list.append(x)
        if len(new_diff_list) > 50:
            diff_list.clear()
            diff_list.extend(new_diff_list)
            new_diff_list.clear()
        return 'red'
    else:
        diff_list.append(x)
        if len(diff_list) > 100:
            diff_list.pop(0)
            if len(new_diff_list) != 0:
                new_diff_list.pop()
        return 'blue'

