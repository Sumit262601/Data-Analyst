import matplotlib.pyplot as plt

#fig, ax = plt.subplots(nrows, ncols, figsize=(width, height))
fig, ax = plt.subplots(1,3, figsize = (10,4))

x = [1,2,3,4]
y = [10,20,15,25]

ax[0].plot(x,y, color='orange')
ax[0].grid()
ax[0].set_title('Line Plot')

ax[1].bar(x,y, color='skyblue')
ax[1].set_title('Bar Chart')

ax[2].barh(x,y, color='green') 
ax[2].set_title('Pie Chart')

fig.suptitle('Comparision of Line & bar chart')

plt.tight_layout()
plt.show()