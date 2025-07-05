import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv(r"C:\Users\user\Desktop\projectPy\netflix_titles.csv",encoding='unicode_escape')


# Subset the DataFrame for type "Movie"
netflix_Movies = netflix_df[netflix_df['type'] == "Movie"]

# Filter to keep only movies released in the 1990s (1990 <= year < 2000)
movies_1990s = netflix_Movies[(netflix_Movies['release_year'] >= 1990) & (netflix_Movies['release_year'] < 2000)]

# Define appropriate bins using multiple strategies
num_data_points = len(movies_1990s)
bins_sturges = int(np.log2(num_data_points) + 1)  # Sturges' Rule
bins_sqrt = int(np.sqrt(num_data_points))         # Square Root Rule

# Visualize the duration column with an appropriate number of bins
# You can choose either 'bins_sturges' or 'bins_sqrt' or a manual bin number.
plt.hist(movies_1990s["duration"], bins=bins_sqrt)  # Using Square Root rule for more detail
plt.title('Distribution of Movie Durations in the 1990s')
plt.xlabel('Duration (Minutes)')
plt.ylabel('Number of Movies')
plt.show()

# Find the most frequent movie duration (mode of the duration)
duration = movies_1990s["duration"].mode()[0]  # Mode gives the most frequent value
print(f"The most frequent movie duration in the 1990s is {duration} minutes.")

# Filter to keep only Action movies from the 1990s
action_movies_1990s = movies_1990s[movies_1990s['genre'] == 'Action']

# Count the number of short action movies (duration < 90 minutes)
short_movie_count = len(action_movies_1990s[action_movies_1990s['duration'] < 90])

# Output the count of short action movies
print(f"Number of short action movies (duration < 90 minutes) in the 1990s: {short_movie_count}")