import pandas as pd

data = {
    "Time": [1,None,3,None,5],
    "Value": [10, None, 40, None, 70]
}

df = pd.DataFrame(data)
print('Before interpolation')
print(df)

df ['Time'] = df ['Time']. interpolate(method="linear")
df ['Value'] = df ['Value']. interpolate(method="linear")
print('After interpolation')
print(df)

"""
1- timer series data
2- numeric data with trends
3- avoid dropping rows|
"""

