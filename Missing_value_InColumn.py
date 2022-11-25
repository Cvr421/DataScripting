
# We can use pandas “isnull()” function to find out all the fields which have missing values
# Use isnull() function to identify the missing values in the data frame
# Use sum() functions to get sum of all missing values per column.
# use sort_values(ascending=False) function to get columns with the missing values in descending order.
# Divide by len(df) to get % of missing values in each column.

from IPython.display import display
import pandas as pd
dataframe=pd.read_csv('titanic.csv')
dataframe.head()
print("The Data set has {} rows and {} columns".format(dataframe.shape[0],dataframe.shape[1]))#Here we are getting the no of row and columns
print("Print a count of missing Value for each columns")
print(dataframe.isnull().sum())#This will give the number of All missing value in the column


