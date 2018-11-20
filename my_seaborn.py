import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

sns.set(style="ticks")
tips = sns.load_dataset("tips")
g = sns.jointplot(x="total_bill", y="tip",kind="kde" ,data=tips)


plt.show()