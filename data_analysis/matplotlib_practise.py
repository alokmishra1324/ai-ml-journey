import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [1,4,9,16,25]

## create a line plot

plt.plot(x,y)
plt.xlabel('X axis')
plt.ylabel('Y Axis')
plt.title('Basic Line Plot')
# plt.show()



plt.plot(x,y, color='red' ,linestyle = '-' , marker='o' , linewidth = 2, markersize=6)
plt.grid(True)
# plt.show()


## Multiple plots
## Sample data

x1 = [1,2,3,4,5]
y1 = [1,4,9,16,25]
y2 = [1,2,3,4,5]

plt.figure(figsize=(9,5))
plt.subplot(2,2,1)
plt.plot(x1, y1, color='green')
plt.title("Plot 1")
# plt.show()

plt.subplot(2,2,2)
plt.plot(y1, x1, color='red')
plt.title("Plot 2")
# plt.show()

plt.subplot(2,2,3)
plt.plot(x1, y2, color='blue')
plt.title("Plot 3")

plt.subplot(2,2,4)
plt.plot(x1, y2, color='green')
plt.title("Plot 4")
# plt.show()

##Bar Plot

categories = ['A' , 'B' ,'C' ,'D' , 'E']
values = [5,7,3,8,6]

##create a bar plot

plt.bar(categories, values, color='purple')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Plot')
# plt.show()


# Sample data
data =  [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]

## create a histogram
plt.hist(data  , bins=5 , color= 'orange' , edgecolor = 'black')
# plt.show()

# create a scatter plot

# Sample data
x= [1,2,3,4,5]
y = [2,3,4,5,6]

plt.scatter(x,y, color="blue",marker='x')
# plt.show()


## pie chart

labels  = ['A' , 'B' , 'C'  , 'D']
sizes = [30, 20, 40, 10]
colors = ['gold' , 'yellowgreen' , 'lightcoral' , 'lightskyblue']
explode = (0, 0, 0.2 , 0) ## move out the third slice

plt.pie(sizes , labels = labels, colors = colors, explode = explode,  autopct = '%1.1f%%' , shadow = True)
# plt.show()

## Sales Data Visualization

import pandas as pd
sales_data = pd.read_csv('sales_data.csv')
print(sales_data.head(5))

## plot total sales by products

total_sales_by_pdt = sales_data.groupby('Product Category')['Total Revenue'].sum()
print(total_sales_by_pdt)

total_sales_by_pdt.plot(kind ='bar' , color = 'teal')
# plt.show()

##plot sales trend over time

sales_trend = sales_data.groupby('Date')['Total Revenue'].sum().reset_index()
plt.plot(sales_trend['Date'] , sales_trend['Total Revenue'])
plt.show()

