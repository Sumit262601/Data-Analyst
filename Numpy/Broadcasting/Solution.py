import numpy as np

prices = np.array([100, 200, 300, 400, 500])
discount = 10 # 10% discount

final_prices = prices - (prices * discount / 100)

print(final_prices)
