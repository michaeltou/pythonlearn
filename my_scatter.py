import numpy as np
import matplotlib.pyplot as plt

# 数据个数
n = 1000
# 均值为0, 方差为1的随机数
x = np.random.normal(20, 4, n)
y = np.random.normal(0, 1, n)

# 计算颜色值
color = np.arctan2(y, x)
# 绘制散点图
plt.scatter(x, y, s = 75,  alpha = 0.5)
# 设置坐标轴范围


# 不显示坐标轴的值
#plt.xticks(())
#plt.yticks(())

plt.show()