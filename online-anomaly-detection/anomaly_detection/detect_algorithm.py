import statistics as stat

def z_score(diff_list,x):
    if len(diff_list) < 10:
        diff_list.append(x)
        return 'blue'
    mean = stat.mean(diff_list)
    std = stat.stdev(diff_list)
    if abs(x - mean) > 2 * std:
        diff_list.append(x)
        if len(diff_list) > 100:
            diff_list.pop(0)
        return 'red'
    else:
        diff_list.append(x)
        if len(diff_list) > 100:
            diff_list.pop(0)
        return 'blue'
