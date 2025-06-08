import pandas as pd

# Reading CSV file
# df = pd.read_csv('sales_data_sample.csv', encoding='latin1') # Uncomment this line to read a CSV file

df = pd.read_excel("SampleSuperstore.xlsx")
print(df)