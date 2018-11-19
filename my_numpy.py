import numpy as np
import pandas as pd
from scipy.stats import *
import matplotlib.pyplot as plt
import seaborn as sns

a = np.array([[2,1, 2, 3, 2, 3, 4,3,4], [3, 3, 4, 3, 4, 6, 3, 7, 4]])

sns.kdeplot(a[0], a[1])

plt.show()
