#  savefilg('filename.extension', dpi=value, bbox_inches='tight)
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,15,25]

# create plot
# plt.plot(x,y, color='skyblue', marker='o')
# plt.title('Simple Line Plot')
# plt.xlabel('X Axis')
# plt.ylabel('Y Axis')


# Create bar
plt.bar(x, y, color='skyblue',)
plt.title('Simple Line Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.savefig('bar_plot.png', dpi=300, bbox_inches='tight')
plt.show()

