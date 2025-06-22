#plt.subplot(nrows, ncols, index)

import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,15,25]

plt.subplot(2,2,1) #1 row, 2column, 1st subplot
plt.plot(x,y)
plt.title('Line chart')

plt.subplot(2, 2, 2) #1row, 2column, 2nd suplot
plt.bar(x,y)
plt.title('Bar Chart')

# plt.tight_layout()
plt.show()