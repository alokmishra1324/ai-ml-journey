##Basic plotting with seaborn
import seaborn as sns

tips = sns.load_dataset('tips')
# print(tips)

## craete a scatterplot

import matplotlib.pyplot as plt

sns.scatterplot(x='total_bill' , y = 'tip' , data= tips)
plt.title("Scatter Plot of Total Bill vs Tip")

# plt.show()

sns.lineplot(x='size' , y='total_bill', data = tips)
plt.title("Line plot of Total by size")
plt.show()

# Categorial  Plots

## Bar plot
sns.barplot(x='day' , y='total_bill' , data= tips)
plt.title("Bar Plot of Total Bill By Day")
plt.show()


# Box Plot

sns.boxplot(x="day" , y="total_bill" , data= tips)
plt.show()

#Violin Plot

sns.violinplot(x="day" , y="total_bill" , data= tips)
plt.show()

## Histogram

sns.histplot(tips['total_bill'] , bins=10, kde = True)
plt.show()


##KDE Plot
sns.kdeplot(tips['total_bill'] , shade=True)
plt.show()

## Pair Plot

sns.pairplot(tips)
plt.show()

## Heat map
corr = tips[['total_bill' , 'tip' , 'size']].corr()
print(corr)
sns.heatmap(corr, annot =True , cmap='coolwarm')
plt.show()

import pandas as pd

sales_df = pd.read_csv('sales_data.csv')
print(sales_df.head())

## Plot total sales by product
plt.figure(figsize = (10 , 6))
sns.barplot(x='Product Category'  , y = 'Total Revenue' , data = sales_df , estimator = sum)
plt.title("Total Sales by Product")
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.show()
