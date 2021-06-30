# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 12:30:00 2021

@author: graci
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

properties = pd.read_csv("file.txt", sep= '\s+')#
provinces = pd.read_csv("regions.txt", sep= '\s+')
m2_prov = pd.read_csv("m2_per_province.txt", sep= '\s+')

m2_prov = m2_prov.sort_values(['mean1']) #To have organized per ascending average price


values = ['Brussel-Capital', 'Walloon Brabant','Flemish Brabant','Antwerp',
         'Limburg','Liège','Namur','Luxembourg','Hainaut','West Flanders', 'East Flanders']
colors = ['#ffc078','#ffe066','#cdeb75','#8ce99a','#63e6be','#66d9e8','#74c0fc','#91a7ff',
          '#b197fc','#e599f7','#faa2c1']#,'#ffaba8','#dee2e6']
#[orange,yellow,lime,green,teal,cyan,blue,indigo,violet,grape,pink,red,gray]

#colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6', 
#          '#c2c2f0','#ffb3e6', '#ffc078','#ffe066','#cdeb75']#,'#ffb3e6']


          
plt.title("Number of properties per province", fontsize = 14)
plt.pie(provinces['count'], labels = values, shadow=True, startangle=90, colors=colors,
        explode=(0.1, 0.1, 0.1, 0.1, 0.1,0.15,0.1,0.15,0.15,0.1,0.1), autopct='%1.2f%%')#, colors="plasma")
#sns.countplot(x='subtype_property', data=properties)#, palette=pkmn_type_colors)

##***************************************************************************************
###Bar plot for m2 

fig, ax = plt.subplots(figsize=[18,14])
ax = sns.barplot(x="zone10", y="mean1", data=m2_prov)
plt.title("Average prices per m² for every province", fontsize = 30)
plt.ylabel("Average price per m² [€]", fontsize = 24)
plt.xticks(rotation=-50, fontsize = 14)
plt.grid()
fig.savefig('m2_per_province.png')