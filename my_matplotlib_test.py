# sphinx_gallery_thumbnail_number = 3
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 100)

print(x)

plt.plot(x, x,label="linear")
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')

plt.xlabel('x label')
plt.ylabel('y label')
plt.legend()
plt.show()