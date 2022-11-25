from IPython.display import display
from statistics import mean 
import pandas as pd
dataframe=pd.read_csv('titanic.csv')
dataframe.head()
# print(df.isnull().sum())#This will give the number of All missing value in the column
print("The Data set has {} rows and {} columns".format(dataframe.shape[0],dataframe.shape[1]))#Here we are getting the no of row and columns
survived = dataframe[dataframe['Survived'] == 1]
print('{0} Person who Survived'.format(survived.shape[0]))
print('Oldest person who Survived:',survived['Age'].max(),'Year')
print('Youngest person who Survived:',survived['Age'].min(),'Year')
print('Average Age of the person who survived:',survived['Age'].mean().round(2),'Year')