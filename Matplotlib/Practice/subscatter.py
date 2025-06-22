import matplotlib.pyplot as plt
import pandas as pd

# load the data
df = pd.read_csv("netflix_titles.csv")

df = df.dropna(subset=['type', 'release_year', 'rating', 'country', 'duration'])

content_by_year = df.groupby(['release_year', 'type']).size().unstack().fillna(0)

fig, ax =  plt.subplots(1,2, figsize=(12, 5))

#first subplot:movies
ax [0].plot(content_by_year. index, content_by_year ['Movie'], color='blue', label='Movies')
ax [0].set_title('Movies Released Per Year' )
ax [0].set_xlabel('Year')
ax [0].set_ylabel('Number of Movies')
plt.legend()

#second subplot:TV Shows
ax [0].plot(content_by_year.index, content_by_year['TV Show'], color='orange', label='TV Shows')
ax [0].set_title('TV Shows Released Per Year' )
ax [0].set_xlabel('Year')
ax [0].set_ylabel ('Number of TV Shows')

fig.suptitle('Comparison of Movies and TV Shows Released Over Years')

plt.tight_layout()
plt.legend()
plt.savefig('movies_tv_show_comparision.png')
plt.show()



