Data Analysis
Description
This project is part of BeCode AI training. It's a group project to perform a data analysis from a real estate dataset. The dataset has been previously acquired by scrapping ImmoWeb website. The purpose of this project is to gather some information in order to predict the prices on Belgium'sales.

To achieve this goal, this project is structured into three main parts:

Data cleaning.
Data analysis.
Data interpretation
Usage
To be able to follow along this project and reproduce the same results. Make sure to meet the following requirements.

Python is the main language used.
Libraries to install: Numpy, Pandas, Matplotlib and Seaborn.
Make sure to have the dataset file uncleaned_dataset.csv in your working directory.
Run the file cleaning.py to have a clean dataset cleaned_dataset.csv.
Run the file analysis.py to visualize data and see some interpretation.
Data cleaning
import numpy as np
import pandas as pd

# Importing dataset from .csv file to pandas dataframe
df = pd.read_csv('uncleaned_dataset.csv')
This is how the data looks like:

Uncleaned Data

First of all, we delete the Unnamed: 0 column and rename columns. This will help to easily manipulate data.

# deleting the "Unnamed: 0" column from the dataframe
df.drop('Unnamed: 0', axis=1, inplace=True)
# renaming columns
df.rename(columns={'Area [m²]': 'area', 'Price [€]': 'price', 'state of the building': 'building_status',
                   'number of facades': 'number_facades', 'number of bedrooms': 'number_bedrooms',
                   'fully equipped kitchen': 'kitchen_equipped', 'open fire': 'open_fire', 'locality [zip code]': 'zip_code',
                   'surface of the land [m²]': 'land_surface', 'terrace surface [m²]': 'terrace_surface',
                   'swimming pool': 'swimming_pool', 'type of property': 'property_type',
                   'subtype of property': 'property_subtype', 'garden surface [m²]': 'garden_surface'}
, inplace=True)
Uncleaned Data

# Checking the columns type
print(df.dtypes)
Data type

Since price should be a float, let's change its type from object to float. Be aware that null values have been encoded as string 'no'. So float('no') will raise an error because no is not a number. For this reason, we need to replace first 'no' by 'NaN' or np.nan

df.replace({'no':np.nan}, inplace=True)
df["price"] = pd.to_numeric(df["price"])
# percentage of missing values in each column
df.isna().sum()*100/len(df)
Missing Values

Since price is the target variable, so rows without price are not relevant. We'll delete rows without area as well.

df.dropna(subset=['area','price'], inplace=True)
df.shape = (8333, 17)

The locality has been encoded as a zip code in the dataset. So we need to link those zip code with their corresponding municipalities or provinces. That's why we are going to add a new column province to the dataset.

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
print(df.province.value_counts())
Provinces

Data Analysis
Create the subsets of data
Create new Series/columns to plot the data
Check the target variables, input, output variables
Data Interpretation
Bonus
In your opinion, which model of machine learning could solve the task of predicting the sales?]

[...]" Multivariate Regression: supervised machine learning algorithm involving multiple data variables for analysis. A Multivariate regression is an extension of multiple regression with one dependent variable and multiple independent variables. Based on the number of independent variables, we try to predict the output.

Multivariate regression tries to find out a formula that can explain how factors in variables respond simultaneously to changes in others." (source: https://www.mygreatlearning.com/blog/introduction-to-multivariate-regression/ consulted on 29/06/21)

In our case, we have only one target variable, which is the price. Thus the goal of this project is to see (to be able to predict in the future, using ML) how the other variables (location, n° of rooms, swimming pool, etc...) impact the price of a property.

