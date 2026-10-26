# Import libraries

from ast import increment_lineno
import pandas as pd
import seaborn as sns

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

print(df.head())

