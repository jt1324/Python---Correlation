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


