import matplotlib.pyplot as plt
# plt.pie(values, labels=label_list, color=color_list, autopct='%1.1f%%)

regions = ['North', 'South', 'East', 'West']
revenue = [3000, 2000, 1000, 500]

plt.pie(revenue, labels=regions, autopct='%1.1f%%', colors=['lightgreen', 'blue', 'orange', 'coral'] )
plt.title('Revenue Contribution by Regions')
plt.show()