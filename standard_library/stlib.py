import array

arr = array.array('i' , [1,2,3,4,])
print(arr)

##random
import random

print(random.randint(1,11))
print(random.choice(['apple' , 'banana' ,'cherry']))

## File and directory access

import os
print(os.getcwd())  ##current directory

os.mkdir('test_dir') ##create folder


##High level operations on files and collections of files

import shutil
shutil.copyfile('source.txt' , 'destination.txt')


##Data Serialization

import json
data ={'name':'Alok' , 'age':25}

json_str = json.dumps(data)
print(json_str)
print(type(json_str))

parsed_data = json.loads(json_str)
print(parsed_data)
print(type(parsed_data))

## csv

import csv

with open('example.csv' , mode = 'w' , newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name' ,'age'])
    writer.writerow(['Alok' , 25])

with open('example.csv' , mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


from datetime import datetime , timedelta

now = datetime.now()
print(now)

yesterday = now-timedelta(days=1)
print(yesterday)

import time
print(time.time())
time.sleep(3)
print(time.time())


##Regular expression

import re 
pattern = r'\d+'
text = "There are 123 apples "
match = re.search(pattern , text)
print(match.group())