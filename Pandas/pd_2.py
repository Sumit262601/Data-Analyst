import pandas as pd

# Reading CSV file
# df = pd.read_csv('sales_data_sample.csv', encoding='latin1').head(40) # Uncomment this line to read a CSV file

# df = pd.read_excel("SampleSuperstore.xlsx").head(60)

df = pd.read_json("sample_Data.json").head(40)

print(df)

