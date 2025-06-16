import pandas as pd

df = pd.read_json("sample_Data.json").head(40)
print(df.info())

