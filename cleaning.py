import numpy as np
import pandas as pd

# Importing dataset from .csv file to pandas dataframe
df = pd.read_csv('uncleaned_dataset.csv')
print(df.head())

# deleting the "Unnamed: 0" column from the dataframe
df.drop('Unnamed: 0', axis=1, inplace=True)
# renaming columns
df.rename(columns={'Area [m²]': 'area', 'Price [€]': 'price', 'state of the building': 'building_status',
                   'number of facades': 'number_facades', 'number of bedrooms': 'number_bedrooms',
                   'fully equipped kitchen': 'kitchen_equipped', 'open fire': 'open_fire', 'locality [zip code]': 'zip_code',
                   'surface of the land [m²]': 'land_surface', 'terrace surface [m²]': 'terrace_surface',
                   'swimming pool': 'swimming_pool', 'type of property': 'property_type',
                   'subtype of property': 'subtype_property', 'garden surface [m²]': 'garden_surface'}
, inplace=True)
print(df.head())
# Checking any duplicated rows
print(df.duplicated().any())

# Checking the columns type
print(df.dtypes)

# Changing price type from object (string) to float
# price has either string 'number' where number is an integer or string 'no'
# so float('no') will raise an error because no is not a number. 
# For this reason, we need to replace first 'no' by 'NaN' or 'np.nan'
df.replace({'no':np.nan}, inplace=True)
df["price"] = pd.to_numeric(df["price"])
print(df.dtypes)

# percentage of missing values in each column
df.isna().sum()*100/len(df)

# Since price is the target variable, so rows without price are not relevant. 
# We'll delete rows without area as well.
df.dropna(subset=['area','price'], inplace=True)
print(df.shape)

# adding a new column province
conditions = [ (1000 <= df['zip_code']) & (df['zip_code'] < 1300),
              (1300 <= df['zip_code']) & (df['zip_code'] < 1500),
              ((1500 <= df['zip_code']) & (df['zip_code'] < 2000))| 
              ((3000 <= df['zip_code']) & (df['zip_code'] < 3500)),
              (2000 <= df['zip_code']) & (df['zip_code'] < 3000),
              (3500 <= df['zip_code']) & (df['zip_code'] < 4000),
              (4000 <= df['zip_code']) & (df['zip_code'] < 5000),
              (5000 <= df['zip_code']) & (df['zip_code'] < 6000),
              (6600 <= df['zip_code']) & (df['zip_code'] < 7000),
              ((6000 <= df['zip_code']) & (df['zip_code'] < 6600))|
              ((7000 <= df['zip_code']) & (df['zip_code'] < 8000)),
              (8000 <= df['zip_code']) & (df['zip_code'] < 9000),
              (9000 <= df['zip_code']) & (df['zip_code'] < 10000)]
values = ['Brussel-Capital', 'Walloon Brabant','Flemish Brabant','Antwerp','Limburg','Liege','Namur','Luxembourg','Hainaut','West Flanders','East Flanders']
df['province'] = np.select(conditions, values)
print(df['province'].value_counts())

# Add new column zone (region)
conditions = [ (1000 <= df['zip_code']) & (df['zip_code'] < 1300),
              ((1300 <= df['zip_code']) & (df['zip_code'] < 1500))| 
              ((4000 <= df['zip_code']) & (df['zip_code'] < 8000)),
              ((1500 <= df['zip_code']) & (df['zip_code'] < 4000))| 
              ((8000 <= df['zip_code']) & (df['zip_code'] < 10000))]

values = ['Brussels_zone', 'Wallonia_zone','Flanders_zone']
df['Zone'] = np.select(conditions, values)
print(df['Zone'].value_counts())

# add new column 
conditions = [(df['Zone'] == 'Brussels_zone'),
              (df['Zone'] == 'Wallonia_zone'), 
              (df['Zone'] == 'Flanders_zone')]

values = [1,2,3]
df['zone_num'] = np.select(conditions, values)
print(df['zone_num'].value_counts())

# add new column
df['price_per_m2'] = df.price/df.area

# saving cleaned dataframe to .csv file
df.to_csv('cleaned_dataset.csv', encoding='utf-8', index=False)