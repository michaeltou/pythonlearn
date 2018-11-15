import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats,integrate
import seaborn as sns


sns.set(color_codes=True)
x= np.random.normal(size=100)

print(x)

print(type(x))

sns.distplot(x,bins=10)

plt.show()