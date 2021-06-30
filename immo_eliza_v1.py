# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 15:50:24 2021

@author: graci
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

immo_eliza = pd.read_csv("immo_eliza_dataset.csv")#

##***************************************************************************************
####MinHien 
#***********Per province based on zip_code
df4 = immo_eliza
conditions = [ (1000 <= df4['zip_code']) & (df4['zip_code'] < 1300),
              (1300 <= df4['zip_code']) & (df4['zip_code'] < 1500),
              ((1500 <= df4['zip_code']) & (df4['zip_code'] < 1999))|((3000 <= df4['zip_code']) & (df4['zip_code'] < 3500)),
              (2000 <= df4['zip_code']) & (df4['zip_code'] < 3000),
              (3500 <= df4['zip_code']) & (df4['zip_code'] <= 3999),
              (4000 <= df4['zip_code']) & (df4['zip_code'] <= 4999),
              (5000 <= df4['zip_code']) & (df4['zip_code'] <= 5999),
              (6600 <= df4['zip_code']) & (df4['zip_code'] <= 6999),
              ((6000 <= df4['zip_code']) & (df4['zip_code'] <= 6599))|((7000 <= df4['zip_code']) & (df4['zip_code'] <= 7999)),
              (8000 <= df4['zip_code']) & (df4['zip_code'] <= 8999),
              (9000 <= df4['zip_code']) & (df4['zip_code'] <= 9999)]
values = ['Brussels-Capital', 'Walloon Brabant','Flemish Brabant','Antwerp','Limburg','Liège','Namur','Luxembourg','Hainaut','West Flanders', 'East Flanders']
df4['zone10'] = np.select(conditions, values)
df4.head()
##***************************************************************************************
#***********Per type of property, in order to use only houses, villas and appartments
df2 = immo_eliza
df2.subtype_property.value_counts()
conditions = [(df2['subtype_property'] == 'house'), #1
            (df2['subtype_property'] == 'villa'),#2
            (df2['subtype_property'] == 'apartment'),#3, it misses a 't' on 'appartment'
            (df2['subtype_property'] == 'mixed'),#4
            (df2['subtype_property'] == 'exceptional'), #5
            (df2['subtype_property'] == 'mansion'),#6
            (df2['subtype_property'] == 'country'),#7
            (df2['subtype_property'] == 'town'),#8
            (df2['subtype_property'] == 'bungalow'),#9
            (df2['subtype_property'] == 'building'),#10
            (df2['subtype_property'] == 'farmhouse'),#11
            (df2['subtype_property'] == 'manor'),#12
            (df2['subtype_property'] == 'castle'),#13
            (df2['subtype_property'] == 'other')|#14
            (df2['subtype_property'] == 'chalet')|#14
            (df2['subtype_property'] == 'land')] #14 -->#combined last 3 cats

values = [1,2,3,4,5,6,7,8,9,10,11,12,13,14] #The NaN will be zero
df2['subtype'] = np.select(conditions, values)
print(df2['subtype'].value_counts())
df2['subtype_property'].value_counts()

"""
Subtype  N° of properties
1     6006
2     1061
4      271
3      259
0      235
6      176
8       92
7       88
9       60
11      28
12      22
14      20
13      15
Name: subtype, dtype: int64
Keeping only n° 1, 2 and 3 (houses, villas and appartments):
6006 + 1061 +259 = 7326 properties
"""

##***************************************************************************************
intresting_prop = df2[(df2['subtype'] > 0) & (df2['subtype'] < 4)] 
#To use only houses, villas and appartments

per_province = intresting_prop.groupby('zone10')
intresting_prop['m2_per_province'] = intresting_prop['price']/intresting_prop['area'] #calculate price/area
value_m2 = intresting_prop.groupby('zone10')['m2_per_province'].agg([min,max,np.mean,np.median])


##***************************************************************************************
#***********Per region
                        
conditions = [ (1000 <= df4['zip_code']) & (df4['zip_code'] < 1300),
              ((1300 <= df4['zip_code']) & (df4['zip_code'] < 1500))| 
              ((4000 <= df4['zip_code']) & (df4['zip_code'] < 8000)),
              ((1500 <= df4['zip_code']) & (df4['zip_code'] < 4000))| 
              ((8000 <= df4['zip_code']) & (df4['zip_code'] < 10000))]

values = ['Brussels_zone', 'Wallonia_zone','Flanders_zone']
df4['Zone'] = np.select(conditions, values)
df4['Zone'].value_counts()
                        
                        
df = df4
df['price_per_room'] = df.price/df.number_bedrooms
df['price_per_m2'] = df['price']/df['area']
df.price_per_m2.value_counts()
Zone_price = df2.groupby('Zone')['price_per_m2'].agg([min,max,np.mean,np.median])
print(Zone_price)
##***************************************************************************************
                        
                        
#******************************************************************************************
#                                   ******PLOTS*****                        
#******************************************************************************************                        

colors = ['#ffc078','#ffe066','#cdeb75','#8ce99a','#63e6be','#66d9e8','#74c0fc','#91a7ff',
          '#b197fc','#e599f7','#faa2c1']#,'#ffaba8','#dee2e6']
#[orange,yellow,lime,green,teal,cyan,blue,indigo,violet,grape,pink,red,gray]
          
##***************************************************************************************
##***PIE CHART**************************************

fig, ax = plt.subplots(figsize=[10,6])          
color = ['#cdeb75','#63e6be','#e599f7', '#66d9e8']         
kept_prop =[6006, 1061, 259, 1007] 
labels = ['Houses', 'Villas', 'Appartments', 'Others']
plt.pie(kept_prop, labels = labels, colors = color, startangle=0,shadow=True, 
        autopct='%1.2f%%', explode=(0.1, 0.1, 0.1, 0.1), textprops={'fontsize': 14})

plt.title("Type of properties used", fontsize = 16)

#provinces['count'], labels = values, shadow=True, startangle=90, colors=colors,
#        explode=(0.1, 0.1, 0.1, 0.1, 0.1,0.15,0.1,0.15,0.15,0.1,0.1), autopct='%1.2f%%')

fig.savefig('pie_properties.png')

##For legend, explaining others, but it lookd too crowded
#plt.text(0.9, 0.5, "others:")
#plt.text(0.9, 0.4, 'town')
#plt.text(0.9, 0.3, 'building')





##********SCATTER ************************************
#sns.lmplot(x='immo_eliza.price', y='immo_eliza.area', data = immo_eliza)
x=immo_eliza.price#/10**3
y=immo_eliza.area
#plt.scatter(x, y, alpha = 0.3)#, simsize = 0.2)
###plt.title("Most ordered items", fontsize = 12)
#plt.ylabel("Area [m²]")
#plt.xlabel("Price [€]")
#plt.xlim(2500, max(x))
#plt.ylim(0, max(y))
#plt.grid()
#plt.show()
##***************************************************************************************
##***Histograms**************************************
## type of properties
#sns.countplot(x='subtype_property', data=df4)
#plt.xticks(rotation=-45)
#plt.title("Property types", fontsize = 14)
#plt.ylabel("Amount")
#plt.grid()
#**********************************************

##to plot the amount of properties [only intresting ones] per province:
fig, ax = plt.subplots(figsize=[18,14])
sns.countplot(x='zone10', data=intresting_prop)
plt.title("Properties per province (total=7326)", fontsize = 30)
plt.ylabel("Number of properties", fontsize = 24)
plt.xticks(rotation=-50, fontsize = 14)
plt.grid()
fig.savefig('properties_per_province.png')