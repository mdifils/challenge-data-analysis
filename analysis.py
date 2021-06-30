import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# customize color
colors = ['#ffc078','#ffe066','#cdeb75','#8ce99a','#63e6be','#66d9e8','#74c0fc',
          '#91a7ff','#b197fc','#e599f7','#faa2c1','#ffaba8','#dee2e6']
sns.set_palette(sns.color_palette(colors))

# Importing dataset from .csv file to pandas dataframe
df = pd.read_csv('cleaned_dataset.csv')

# Number of rows and columns
print(df.shape)
print(df.head(10))

# scatter plots between the target: `price` and the other variables
fig, axes = plt.subplots(2, 3, figsize=(15, 5))
fig.suptitle('Scatter plot between target and others variables')
fig.tight_layout(pad=3.0)
# area
sns.scatterplot(ax=axes[0,0], y='area', x='price', data=df)
axes[0,0].set_title('scatterplot between price and area')

# number_bedrooms
sns.scatterplot(ax=axes[0,1], y='number_bedrooms', x='price', data=df)
axes[0,1].set_title('scatterplot between price and number_bedrooms')

# number_bedrooms
sns.scatterplot(ax=axes[0,2], y='number_facades', x='price', data=df)
axes[0,2].set_title('scatterplot between price and number_facades')

# zip_code
sns.scatterplot(ax=axes[1,0], y='zip_code', x='price', data=df)
axes[1,0].set_title('scatterplot between price and zip_code')

# land_surface
sns.scatterplot(ax=axes[1,1], y='land_surface', x='price', data=df)
axes[1,1].set_title('scatterplot between price and land_surface')

# garden_surface
sns.scatterplot(ax=axes[1,2], y='garden_surface', x='price', data=df)
axes[1,2].set_title('scatterplot between price and garden_surface')

# plt.savefig('scatterplot.png')
plt.show()