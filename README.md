# challenge-data-analysis
Repository: challenge-data-analysis
Type of Challenge: Consolidation
Duration: 3 days
Deadline: 30/06/2021 16:30
Team members : Anne Jungers, Graciela Lopez Rossion, Michel Ombessa, Minh Hien Vo

#Step 1. Data Cleaning

#Check No duplicates
#Check No blank spaces (ex: " I love python " => "I love python")
# No errors -> needs to be accepted by data visualization methods
# No empty rows

# Data manipulating
# Rename the columns to retrieve easily

# Check the target, potential varible for correlation testing

# Check if each columns/variables exists NaN, zero, or incorrect data types values (ex: 'no' in price)

# Changes the datatypes
# Reports
# - How many missing values for each, zero -> calculate percentage of missing values
# - The outliers for each valriables
# - 


# Step 2. Data analysis
[Requirement: 
Which variable is the target ?
How many rows and columns ?
What is the correlation between the variables and the target ? (Why might that be?)
What is the correlation between the variables and the other variables ? (Why?)
Which variables have the greatest influence on the target ?
Which variables have the least influence on the target ?
How many qualitative and quantitative variables are there ? How would you transform these values into numerical values ?
Percentage of missing values per column ?]

# Create the subsets of data 

# Create new Series/columns to plot the data

# Check the target variables, input, output variables

# 


# Step 3 : Data Interpretation

[After analyzing your data, it's finally time to interpret your results. You have to communicate your analysis using simple words and a table or graph, then use the results to decide on your best course of action.

Example of questions you should be able to answer to:

*NB: This is a non-exhaustive list. Try to make a maximum of interpretations of the dataset. Bonus points from yours truly for creative and outside the box questions that you answer.*

You must be able to answer :

Are there any outliers? If yes, which ones and why?
Which variables would you delete and why ?
In your opinion, which 5 variables are the most important and why?
What are the most expensive municipalities in Belgium? (Average price, median price, price per square meter)
What are the most expensive municipalities in Wallonia? (Average price, median price, price per square meter)
What are the most expensive municipalities in Flanders? (Average price, median price, price per square meter)
What are the less expensive municipalities in Belgium? (Average price, median price, price per square meter)
What are the less expensive municipalities in Wallonia? (Average price, median price, price per square meter)
What are the less expensive municipalities in Flanders? (Average price, median price, price per square meter)


# Bonus
In your opinion, which model of machine learning could solve the task of predicting the sales?]

[...]" *Multivariate Regression*: supervised machine learning algorithm involving multiple data variables for analysis. A Multivariate regression is an extension of multiple regression with one dependent variable and multiple independent variables. Based on the number of independent variables, we try to predict the output.

Multivariate regression tries to find out a formula that can explain how factors in variables respond simultaneously to changes in others." (source: https://www.mygreatlearning.com/blog/introduction-to-multivariate-regression/ consulted on 29/06/21)

In our  case, we have only one target variable, which is the price. Thus the goal of this project is to see (to be able to predict in the future, using ML) how the other variables (location, n° of rooms, swimming pool, etc...) impact the price of a property.


