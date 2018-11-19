
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns


a = np.random.normal(60,1,size=1000)
b=np.random.normal(30,1,size=1000)
print(a)
print(b)

sns.kdeplot(a,b,shade=True,cbar=True)
plt.show()