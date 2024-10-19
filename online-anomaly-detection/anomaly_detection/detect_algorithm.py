import statistics as stat

# this function will calculate the z-score of current predict error with previous predict error list. If the z-score smaller than three,
# it means current date is not an anomaly date and color will be blue, otherwise the color will be red.
def z_score(diff_list,x):
    # when diff_list less than 10 always return no anomaly, because not have enough to decide.
    if len(diff_list) < 10:
        diff_list.append(x)
        return 'blue'
    mean = stat.mean(diff_list)
    std = stat.stdev(diff_list)
    # when z-score greater than 3, the point should be a anomaly data. The diff_list will keep the recent 100 predict error.
    if abs(x - mean) > (3 * std):
        diff_list.append(x)
        if len(diff_list) > 100:
            diff_list.pop(0)
        return 'red'
    else:
        diff_list.append(x)
        if len(diff_list) > 100:
            diff_list.pop(0)
        return 'blue'
