import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple


n_groups = 5

means_men = (20, 35, 30, 35, 27)
std_men = (2, 3, 4, 1, 2)

fig, ax = plt.subplots()

index = ['A','B','C','D','E']
print(index)

bar_width = 0.35

rects1 = ax.bar(index, means_men, bar_width,
                  color='b'
                 )


ax.set_xlabel('Group')
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.legend()

fig.tight_layout()
plt.show()