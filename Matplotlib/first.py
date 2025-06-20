import matplotlib.pyplot as plt
import numpy as np

x = (1, 2, 3, 4, 5)
y = (2, 3, 5, 7, 11)

plt.plot(x, y, marker='o', linestyle='-', color='b', label='Data Points')
plt.title('Sample Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.show()