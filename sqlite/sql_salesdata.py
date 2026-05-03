## Working with Sales Data

# Connect to an SQLite database
import sqlite3
connection  = sqlite3.connect('sales_data.db')
cursor = connection.cursor()

## Create a table for sales data

cursor.execute('''
CREATE TABLE IF NOT EXISTS sales(
               id INTEGER PRIMARY KEY,
               date TEXT NOT NULL,
               product TEXT NOT NULL,
               sales INTEGER,
               region TEXT
               )

''')

# Insert data into the sales table

sales_data = [
        ('2026-01-01' , 'Product1' , 100 ,  'North'),
        ('2026-01-02' , 'Product2' , 200 ,  'South'),
        ('2026-01-03' , 'Product1' , 150 ,  'East'),
        ('2026-01-04' , 'Product3' , 250 ,  'West'),
        ('2026-01-05' , 'Product2' , 300 ,  'North'),

]

cursor.executemany('''
Insert into sales(date , product , sales , region)
                   values(?,?,?,?)
''' , sales_data)

connection.commit()

cursor.execute('Select * from sales')
rows = cursor.fetchall()

for row in rows:
    print(row)


    ## close the connection

    connection.close()