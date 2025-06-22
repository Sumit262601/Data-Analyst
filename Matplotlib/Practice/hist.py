import pandas as pd
import matplotlib.pyplot as plt

# load the data
df = pd.read_csv("netflix_titles.csv")


df = df.dropna(subset=['type', 'release_year', 'rating', 'country', 'duration'])

movie_df = df[df['type'] == 'Movie'].copy()
movie_df['duration_int'] = movie_df['duration'].str.replace(' min', '').astype(int)

plt.figure(figsize=(8,6))
plt.hist(movie_df ['duration_int'], bins=30, color='purple', edgecolor='black' )
plt.title('Distributaion of Movie Duration')
plt.xlabel('Duration (minutes)')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('movie_duration_histogram.png')
plt.show()