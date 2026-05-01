import pandas as pd

df = pd.read_csv("customers-100.csv")
df1 = pd.read_csv("data.csv")

## fetch the first 5 rows

# print(df.head(5))
# print(df.tail(5))

print(df1.head(5))
print(df1.tail(5))

# print(df.describe())
# print(df.dtypes)

print(df1.describe())
print(df1.dtypes)

##Handling missing values

# print(df.isnull())
# print(df.isnull().any())
# print(df.isnull().sum())
print(df1.isnull().sum())

print(df1.fillna(0)) ## if there any empty value it will change to 0

## filling missing values with the mean of the column

# df['website_fillNA'] = df['Website'].fillna(df['Website'].mean())

df1 = df1.rename(columns={'Date' : 'Sales Date'})
print(df1.head())
# print(df.dtypes)

#change datatypes

df1['Value_new'] = df1['Value'].fillna(df1['Value'].mean()).astype(int)
print(df1.head())

df1['New Value'] = df1['Value'].apply(lambda x:x*2)
print(df1.head())


## Data Aggregating and grouping

grouped_mean = df1.groupby('Product')['Value'].mean()
print(grouped_mean)

grouped_sum = df1.groupby(['Product' , 'Region'])['Value'].sum()
print(grouped_sum)

#Aggregate multiple functions
grouped_agg = df1.groupby('Region')['Value'].agg(['mean' , 'sum' , 'count'])
print(grouped_agg)


## Merging and joining Dataframes

df2 = pd.DataFrame({'Key' : ['A' , 'B' ,'C'] , 'Value1' : [1,2,3]})
df3 = pd.DataFrame({'Key' : ['A' , 'B' , 'D'], 'Value2' : [4,5,6]})

print(df2)

##Merge DataFrame on the 'Key Columns'

merged_dfs_inner = pd.merge(df2 , df3, on="Key", how="inner")
print(merged_dfs_inner)

merged_dfs_outer = pd.merge(df2 , df3 , on="Key" , how ="outer")
print(merged_dfs_outer)

merged_dfs_left = pd.merge(df2 , df3 , on="Key" , how ="left")
print(merged_dfs_left)

merged_dfs_right = pd.merge(df2 , df3 , on="Key" , how ="right")
print(merged_dfs_right)