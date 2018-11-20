import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats,integrate
import seaborn as sns



tips = sns.load_dataset("tips")
g = sns.jointplot(x="total_bill", y="tip", data=tips)
g2 = sns.jointplot(x="total_bill", y="tip", data=tips, kind="scatter")
