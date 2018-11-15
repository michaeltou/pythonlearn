import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats,integrate
import seaborn as sns


sns.set(color_codes=True)

mean, cov = [0,1], [(1,.5),(.5,1)]

data = np.random.multivariate_normal(mean,cov,200)

print(data)

print(type(data))

df = pd.DataFrame(data,columns=["x","y"])
print(df)

sns.jointplot(x="x",y="y",data=df)

plt.show()