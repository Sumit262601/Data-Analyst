import matplotlib.pyplot as plt
import numpy as np

x = ('Mon', 'Tue', 'Wed', 'Thu', 'Fir', 'Sat', 'Sun')
y = (0, 2, 3, 5, 11, 8, 10)

plt.plot(x, y, color='orange', linestyle='--', linewidth=2, label='Total no of Sales', marker='^')

plt.title("Bakery Sales in this weeks") ## FOR TITLE

plt.xlabel("Days of the week") ## FOR xLABEL

plt.ylabel("Sales Per Day") ## FOR yLABEL

plt.legend(loc='upper left', fontsize=12) ## FOR SHOW LABELS IN YOUR LOCTIONS

plt.grid(color= 'gray', linestyle='solid', linewidth=1) ## FOR BETTER visulization

# plt.xlim(1,5) ## FOR LIMITAION IN x axis

# plt.ylim(1,8) ## FOR  LIMITAION IN y axis

plt.xticks([1,2,3,4,5,6,7], ['Mo', 'Tu', 'We', 'Th', 'Fi', 'St', 'Sn'])

plt.show() ## FOR SHOW() IS A METHOD


"""
ValueError: 'top left' is not a valid value for loc; supported values are 'best', 'upper right', 'upper left', 'lower left', 'lower right', 'right', 'center left', 'center right', 'lower center', 'upper center', 'center'
"""