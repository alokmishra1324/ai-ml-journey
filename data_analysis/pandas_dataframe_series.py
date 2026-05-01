import pandas as pd
##Series

data = [1,2,3,4,5]
series = pd.Series(data)
print("Series\n " , series)
print(type(series))

##Create a series from dictionary

data1= {'a' :1, 'b':2 ,'c':3}
series_dict = pd.Series(data1)
print(series_dict)

data3 = [10,20,30]
index = ['a' ,'b','c']
print(pd.Series(data3, index=index))


##Dataframe
## create a dataframe from dictionary
data4={
    'Name' :['Alok' , 'Rahul' , 'Rohit'],
    'Age' : [24,25,27],
    'City' :['Hyd' , 'Mum' , 'Bang']
}

df = pd.DataFrame(data4)
print(df)
print(type(df))


import numpy as np

print(np.array(data4))


## Create a dataframe from a list of Dictionaries

data5=[
    {'Name':'Alok' , 'Age' : 25 , 'City': 'Bang'},
    {'Name':'Amit' , 'Age' : 29 , 'City': 'Mum'},
    {'Name':'Aman' , 'Age' : 24 , 'City': 'Hyd'},
    {'Name':'Amulya','Age' : 23 , 'City': 'Bang'},
]

df1 = pd.Series(data5)
print(df1)


df3 = pd.read_csv('customers-100.csv')
print(df3.head(5))


##Accessing Data from Dataframe
print(df['Name'])

print(df.loc[0])


print(df.iloc[0])


##Accesing a specified element

print(df.at[1,'Age'])
print(df.at[1,'Name'])

## Accesing a specified element using iat

print(df.iat[2,2])

## Data manipulation with dataframe
##Adding a col
df['Salary'] = [50000, 60000 , 70000]
print(df)

df.drop('Salary' , axis=1 , inplace= True) ## by default axis is taking 0 so not able to find & delete Salary col and inplace=True for permanent delete the col

print(df)

##Add age to the column
df['Age'] = df['Age']+1
print(df)

print(df3.describe())