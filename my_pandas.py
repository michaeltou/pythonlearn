import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df)
print("---------------------------")


print(df.iloc[1:2,0:2])