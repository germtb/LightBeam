import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_subplot(111)
x, y = np.random.rand(2, 30)
line = ax.plot(x, y)

plt.show()