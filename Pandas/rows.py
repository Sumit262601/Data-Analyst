#head() tail()
#head() to see the records in th top of the dataset or default value in head() is 5
#tail() to see the records in the bottom of the dataset or default value in tail() is 5

import pandas as pd

df = pd.read_json("sample_Data.json")

print("Display 10 rows of first")
print(df.head(10))

print("Display 10 rows of first")
print(df.tail(10))

