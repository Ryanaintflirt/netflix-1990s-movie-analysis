# netflix-1990s-movie-analysis

This project analyzes movie data from Netflix, focusing on films released in the 1990s. It explores the distribution of movie durations and investigates short action films during that decade.

🔍 Features

- Filters Netflix data to include only movies from the 1990s.
- Visualizes movie durations using histogram binning techniques:
  - Sturges' Rule
  - Square Root Rule
- Calculates the most frequent movie duration (mode).
- Identifies and counts short action movies (duration < 90 minutes).

📊 Visualization

- Histogram: Distribution of movie durations in the 1990s

📁 Files

- `netflix_analysis.py`: Main analysis script
- `netflix_titles.csv`: Dataset (optional to include; you may link to it on Kaggle)

🧠 Skills Demonstrated

- Data cleaning and filtering with `pandas`
- Statistical binning with `numpy`
- Data visualization with `matplotlib`
- Conditional filtering using string matching

💡 Sample Output
The most frequent movie duration in the 1990s is 90 minutes.
Number of short action movies (duration < 90 minutes) in the 1990s: 8


🎯 Ideal for data science beginners to demonstrate EDA (Exploratory Data Analysis).
