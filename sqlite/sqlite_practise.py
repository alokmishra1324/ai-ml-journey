import sqlite3

## Connect to an SQLite

connection = sqlite3.connect('example.db')
print(connection)

cursor = connection.cursor()

## Create a table

cursor.execute('''
Create Table If Not Exists employees(
               id Integer Primary Key,
               name Text Not Null,
               age Integer,
               department text
               )
        ''')

## Commit the changes

connection.commit()

cursor.execute('''
Select * from employees
        ''')

## Insert the data in sqlite table
cursor.execute('''
Insert Into employees(name , age , department)
               values('Alok' , 25, 'AI/ML')
''')

cursor.execute('''
Insert Into employees(name , age , department)
               values('Amit' , 32, 'Testing')
''')

cursor.execute('''
Insert Into employees(name , age , department)
               values('Rahul' , 24, 'Finance')
''')

connection.commit()

## Query the data from the table

cursor.execute('Select * from employees')
rows = cursor.fetchall()

# Print the query data
for row in rows:
    print(row)


## Update the data in the table
cursor.execute('''
UPDATE employees
Set age = 26
where name = "Alok"

''')

cursor.execute('Select * from employees')
rows = cursor.fetchall()

connection.commit()

for row in rows:
    print(row)


## Delete the data from the table

cursor.execute('''
Delete from employees 
              where name = 'Amit'
''')


cursor.execute('Select * from employees')
rows = cursor.fetchall()

connection.commit()

for row in rows:
    print(row)


