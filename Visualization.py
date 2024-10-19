from generate_data import result_list

import matplotlib.pyplot as plt


fig, ax = plt.subplots()
ax.plot(range(1,len(result_list) + 1),result_list)

fig.savefig('test.png')