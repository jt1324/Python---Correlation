# Import libraries

from ast import increment_lineno
import pandas as pd
import seaborn as sns
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from matplotlib.pyplot import figure

# Notebook-only. In a script this name does not exist, so skip it.
try:
    get_ipython().run_line_magic("matplotlib", "inline")
except NameError:
    pass
matplotlib.rcParams['figure.figsize'] = (12,8)  # Adjust the configuration of the plots to be created



# Read in the data

df = pd.read_csv(r'movies.csv')


# Look to the data

print(df.head().T)


# Checking for missing data

for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    print(f'{col} - {pct_missing:.2f}%')


# Data types - columns

print(df.dtypes)


# Changing data types

df['budget'] = df['budget'].astype('Int64')
df['gross'] = df['gross'].astype('Int64')

print(df.dtypes)
print(df.head().T)


# Create new column - correct year

df['yearcorrect'] = df['released'].astype(str).str.extract(r'(\d{4})', expand=False)
print(df.head().T)


# Order data

df.sort_values(by=['gross'], inplace=True, ascending=False)
print(df.head().T)


# Display the entire data

pd.set_option('display.max_rows', None)
print(df)


# Checking for duplicates 

print(df['company'].drop_duplicates().sort_values(ascending=False))

#df.drop_duplicates()                                               # delete duplicates base on all the columns


# Budget hight correlation
# Scatter plot with budget vs gross

plt.scatter(x=df['budget'], y=df['gross'])
plt.title('Budget vs Gross')
plt.xlabel('Budget')
plt.ylabel('Gross')
# plt.show()

# Plot budget vc gross using seaborn
sns.regplot(x='budget', y='gross', data=df, scatter_kws={"color": "orange"}, line_kws={"color": "blue"})
plt.show()


# Checking correlations - pearson(default) | kendall | spearman

print(df.corr(numeric_only=True))                       # pearson
print(df.corr(method='kendall', numeric_only=True))     # kendall
print(df.corr(method='spearman', numeric_only=True))    # spearman

correlation_matrix = df.corr(numeric_only=True)
sns.heatmap(correlation_matrix, annot = True)
plt.title('Correlation Matrix for Numeric Features')
plt.xlabel('Movie Features')
plt.ylabel('Movie Features')
plt.show()


# Looking at company
# Create a numeric identifier fiel to add all columns to the chart

df_numerized = df.copy()

for col_name in df_numerized.columns:
    if df_numerized[col_name].dtype == 'object' or str(df_numerized[col_name].dtype) == 'str':
        df_numerized[col_name] = df_numerized[col_name].astype('category')
        df_numerized[col_name] = df_numerized[col_name].cat.codes

print(df_numerized)

correlation_matrix_total = df_numerized.corr(numeric_only=True)
sns.heatmap(correlation_matrix_total, annot = True, fmt='.2f')
plt.title('Correlation Matrix for Numeric Features')
plt.xlabel('Movie Features')
plt.ylabel('Movie Features')
plt.show()

correlation_mat = df_numerized.corr()
corr_pairs = correlation_mat.unstack()
sorted_corr_pairs = corr_pairs.sort_values()
print(sorted_corr_pairs)

high_corr = sorted_corr_pairs[(sorted_corr_pairs > 0.5) & (sorted_corr_pairs < 0.99)].sort_values(ascending=False)
print(high_corr)

# Budget and Votes have the highest correlations to gross earnings
# Company has low correlation to gross earnings