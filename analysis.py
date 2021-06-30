import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Importing dataset from .csv file to pandas dataframe
df = pd.read_csv('cleaned_dataset.csv')
print(df.head())