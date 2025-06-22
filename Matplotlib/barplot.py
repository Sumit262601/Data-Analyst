import matplotlib.pyplot as plt

Product = ['A', 'B', 'C', 'D']
Sales = [100, 1500, 400, 600]

# plt.barh(Product, Sales, color=value', label='title_Name')
plt.barh(Product, Sales, color='Orange', label='Sales 2025') # for horizontal barh / for vertical using only bar
plt.xlabel('Product Name')
plt.ylabel('Sales of this year')
plt.title('Product Sale comparision')
plt.legend()
plt.show()