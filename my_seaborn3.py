import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

tips= sns.load_dataset("tips")
sns.boxplot(x="day",y="total_bill",data=tips)

sns.violinplot(x="day",y="total_bill",data=tips)


plt.show()