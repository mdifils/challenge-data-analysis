import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Importing dataset from .csv file to pandas dataframe
df = pd.read_csv('cleaned_dataset.csv')

# Number of rows and columns
print(df.shape)

# scatter plots between the target: `price` and the other variables
fig, axes = plt.subplots(2, 3, figsize=(15, 5))
fig.suptitle('Scatter plot between target and others variables')
fig.tight_layout(pad=3.0)
# area
sns.scatterplot(ax=axes[0,0], x='area', y='price', data=df)
axes[0,0].set_title('scatterplot between price and area')

# number_bedrooms
sns.scatterplot(ax=axes[0,1], x='number_bedrooms', y='price', data=df)
axes[0,1].set_title('scatterplot between price and number_bedrooms')

# number_bedrooms
sns.scatterplot(ax=axes[0,2], x='number_facades', y='price', data=df)
axes[0,2].set_title('scatterplot between price and number_facades')

# zip_code
sns.scatterplot(ax=axes[1,0], x='zip_code', y='price', data=df)
axes[1,0].set_title('scatterplot between price and zip_code')

# land_surface
sns.scatterplot(ax=axes[1,1], x='land_surface', y='price', data=df)
axes[1,1].set_title('scatterplot between price and land_surface')

# garden_surface
sns.scatterplot(ax=axes[1,2], x='garden_surface', y='price', data=df)
axes[1,2].set_title('scatterplot between price and garden_surface')

plt.savefig('scatterplot.png')
plt.show()