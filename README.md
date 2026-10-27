# Movie Industry Correlation Analysis – Python

An exploratory data analysis of a movie dataset (`movies.csv`) that looks at which factors are most strongly linked to a film's gross earnings.

## Objective

Find out which features (budget, votes, production company and others) correlate most with box office gross.

## Tools & Libraries

- **Python**
- **pandas** for loading, cleaning and transforming data
- **NumPy** for numeric operations
- **Matplotlib** and **Seaborn** for visualisation

## Workflow

1. **Data loading and inspection**: read the CSV and preview the first rows.
2. **Missing data check**: work out the share of null values in each column.
3. **Data types**: convert `budget` and `gross` to nullable integers (`Int64`).
4. **Feature fix**: create `yearcorrect` by pulling the 4-digit year out of the `released` column, because the original `year` column doesn't always match the release date.
5. **Sorting and review**: sort by gross earnings and display the full dataset.
6. **Duplicate check**: review unique production companies.
7. **Budget vs gross**: draw a scatter plot and a Seaborn regression plot.
8. **Correlation analysis**:
   - compare the Pearson, Kendall and Spearman methods
   - show a heatmap of the numeric features
   - encode text columns as category codes so every feature can be included
   - unstack and sort the correlation pairs to find the strong ones (> 0.5)

## Key Findings

- **Budget** and **votes** have the highest correlation with gross earnings.
- **Company** has a low correlation with gross earnings.

## How to Run

```bash
pip install pandas numpy matplotlib seaborn
python movie_correlation.py
```

Put `movies.csv` in the same folder as the script. It also runs in Jupyter Notebook, where plots show inline.

## Dataset

Movie industry data with columns such as name, rating, genre, year, released, score, votes, director, writer, star, country, budget, gross, company and runtime.
