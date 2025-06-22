import pandas as pd
import matplotlib.pyplot as plt

# load the data
df = pd.read_csv("netflix_titles.csv")

df = df.dropna(subset=['type', 'release_year', 'rating', 'country', 'duration'])

country_count = df['country'].value_counts().head(10)
plt.figure(figsize=(8,6))
plt.barh(country_count.index, country_count.values, color='teal')
plt.title('Top 10 Countries by Number of Showsl')
plt.xlabel('Number of Shows')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig('Top_10_country.png')
plt.show()


