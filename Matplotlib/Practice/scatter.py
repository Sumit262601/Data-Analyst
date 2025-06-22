import pandas as pd
import matplotlib.pyplot as plt

# load the data
df = pd.read_csv("netflix_titles.csv")

df = df.dropna(subset=['type', 'release_year', 'rating', 'country', 'duration'])

release_counts = df ['release_year' ]. value_counts() .sort_index()
plt.figure(figsize=(10,6))
plt.scatter(release_counts. index, release_counts.values, color='red' )
plt.title('Release Year VS Number of Shows')
plt.xlabel('Release Year')
plt.ylabel('Number of Shows')
plt.grid() 
plt.tight_layout()
plt.savefig('release_year_Scatter.png')
plt.show()