import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

theta = np.arange(0, 2*np.pi, 0.1)
r = 1.5

xs = r*np.cos(theta)
ys = r*np.sin(theta)

poly = Polygon(list(zip(xs, ys)), animated=True)

fig, ax = plt.subplots()
ax.add_patch(poly)

#ax.add_line(p.line)
ax.set_title('Click and drag a point to move it')
ax.set_xlim((-2,2))
ax.set_ylim((-2,2))
plt.show()