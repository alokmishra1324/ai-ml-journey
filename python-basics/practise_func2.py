##Celsius to Fahrenheit
def convert_temp(temp ,unit):
    if(unit == 'C'):
        return temp * 9/5 +32
    else:
        return "Invalid unit"
    
print(convert_temp(100 , 'C'))

## Area of rectangle

def area(l , b):
    return l*b;

rect_area = area(45, 67)
print(rect_area)


##Distance covered by vehicle
def distance_covered(s , t):
    """Distance covered by vehicle"""
    return s*t

dist = distance_covered(60 , 4)
print(dist)


##sum of list elements
lst = [4,5,7,8,1,18,9,5]

def sum_list(list):
    sum = 0
    for i in list:
        sum += i
    return sum

print(sum_list(lst))

## Largest element in list
def greater_ele(list):
    maxi = 0
    for i in list:
        maxi = max(maxi , i)
    return maxi

print(greater_ele(lst))


##Remove the duplicates in list
def remove_dup(input_list):
    return list(set(input_list))


print(remove_dup(lst))

##Reverse the list
def reverse_list(list):
    return list[::-1]

reve_list = reverse_list(lst)
print(reve_list)


##Even number functions
def even_num(list):
    evenlst = []
    for x in list:
        if x%2==0:
            evenlst.append(x)
    return evenlst

evenlist = even_num(lst)
print(evenlist)


## Check list is subset of another list
num1 = [1,2,3,4,5,6,13]
num2 = [1,2,3,4,5,6,7,8,9,10,11,12]

list1 = set(num1)
list2 = set(num2)

print(list1.issubset(list2))


##maximum consecutive difference between 
def maxi_con(list2):
    maxcon = 0
    for i in range(len(list2)-1):
        diff = abs(list2[i] - list2[i+1])
        maxcon = max(maxcon, diff)
    return maxcon

print(maxi_con(num1))



listone  = [3, 6, 8, 43,77, 90]
listtwo = [7, 22, 23, 56, 66]
def merge_lists(list1, list2):
    n = len(list1)
    m = len(list2)
    
    i = n - 1
    j = m - 1
    k = n + m - 1
    
    # Pre-allocate list3 with correct size
    list3 = [0] * (n + m)
    
    while i >= 0 and j >= 0:
        if list1[i] > list2[j]:
            list3[k] = list1[i]
            i -= 1
        else:
            list3[k] = list2[j]
            j -= 1
        k -= 1
    
    # Remaining elements of list2
    while j >= 0:
        list3[k] = list2[j]
        j -= 1
        k -= 1
    
    # Remaining elements of list1
    while i >= 0:
        list3[k] = list1[i]
        i -= 1
        k -= 1
    
    return list3

merged_sorted_list = merge_lists(listone , listtwo)
print(merged_sorted_list)


##Rotate list
lst2 = [4,5,6,1,3,8]
def rotate_list(list1 , k):
    k = k%(len(list1))
    return list1[-2:] + list1[:-2]

print(rotate_list(lst2 , 2))


def rotate_list2(list1 , k):
    k = k%(len(list1))

    def reverse(start , end):
        while(start <end):
            list1[start] , list1[end] = list1[end] , list1[start]
            start += 1
            end  -= 1
    
    reverse(0 , len(list1)-1)
    reverse(0 , k-1)
    reverse(k , len(list1)-1)


print(rotate_list(lst2 , 2))

##merge 2 list into dictionary
numbers1 = [1,2,3]
numbers2 = [4,5,6]

merge_list = dict(zip(numbers1 , numbers2))
print(merge_list)


## merge multiple dictionary
dict1 = {"a":1 , "b":2}
dict2 = {"c":3 , "d":4}
dict3 = {"e":6 , "f" :7}
merges_dict = {**dict1 , **dict2 , **dict3}
print(merges_dict)

##word frequency in sentence

greet = "Hello everyone, welcome to python tutorial hello"

def word_count(msg):
    frequency = {}
    words = msg.split()
    for word in words:
        word = word.lower().strip('.,!?;:"\'')
        frequency[word] = frequency.get(word ,0)+1
    return frequency

print(word_count(greet)) 


##merge dictionaries with common keys

d1 = {"a" :1, "b":2}
d2 = {"a" :3 , "b" :4}
d3 = {"a" :5 , "b" :6}

d1.update(d2)
d1.update(d3)

print(d1)

##pallindromic tuple

tup= ("a man a plan a canal panama")
def check_pallindromic_tuple(tup1):
    tup1 = tup1.lower().replace(" ", "")
    return tup1 == tup1[::-1]

print(check_pallindromic_tuple(tup))