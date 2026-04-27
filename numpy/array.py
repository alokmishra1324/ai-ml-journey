import numpy as np

##Create a 1-D array containing the values 1,2,3,4,5:
arr = np.array([1,2,3,4,5,6,7])

print(arr)

print(type(arr))

##Use a tuple to create a NumPy array

arr1 = np.array((1,2,3,4,5))
print(arr1)
print(type(arr1))

## 0 d array or scalers

arr2 = np.array(45)
print(arr2)

##2 d array where 1d array as its elements
arr3 = np.array([[1,2,3] ,[4,5,6]])
print(arr3)

## Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6:

arr4 = np.array([[[1,2,3] ,[4,5,6]] , [[1,2,3] ,[4,5,6]]])
print(arr4)

print(arr.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)
print(arr4.ndim)

arr5 = np.array([1,2,3,4,5] , ndmin=5)
print(arr5)
print(arr5.ndim)

print(arr[2])
print(arr1[1]) ## accessing element in 1nd dimension
print(arr3[0,2]) ## accessing element in 2nd dimension
print(arr4[0,0,1]) ## accessing element in 3rd dimension
print(arr3[1,-1]) ## last element in 2nd dim
print(arr4[0,1,-1]) ## last element in 3rd dim


print(arr[1:4])
print(arr[:4])
print(arr[4:])
print(arr[-3:-1])
print(arr[1:5:2])
print(arr[::2])

print(arr3[1, 1:4]) ## From both elements, return index 2
print(arr3[0:2 , 1]) ##From both elements, return index 2
print(arr3[0:2 , 1:4]) ##from both elements, slice index 1 to index 4 (not included), this will return a 2-D array

print(arr.dtype)

# arr5 = np.array(['apple' , 'orange' , 'mango'] , dtype = 'S')
# print(arr5.dtype)

arr6 = np.array([1,2,3,4] , dtype = 'i4')
print(arr6.dtype)

arr7  = np.array([1.1 , 2.1 , 3.1])
newarr = arr7.astype('i') ## or int 
print(newarr)
print(newarr.dtype)

arr8 = np.array([1, 0, 3])
newarr1 = arr8.astype(bool)
print(newarr1)
print(newarr1.dtype)

##copy function
arr8 = np.array([1,2,3,4,5])
x = arr8.copy()

arr8[0] = 40
print(arr8)
print(x)

##view function
arr9 = np.array([1,2,3,4,5])
y = arr9.view()

arr9[0] = 40
print(arr9)
print(y)

arr10 = np.array([6,7,4,9,10])
z = arr10.view()
z[0] = 98

print(z)
print(arr10)

arr11 = np.array([9,8,7,6,5])
m = arr11.copy()
n = arr11.view()

print(m.base) ## copy owns the data 
print(n.base) ## view do not owns data

##shape
print(arr3.shape)
print(arr4.shape)
print(arr5.shape)

##reshaping

##Convert the following 1-D array with 12 elements into a 2-D array
arr12 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

k = arr12.reshape(4,3)
print(k)
print(k.shape)
print(k.base)

## Convert the following 1-D array with 12 elements into a 3-D array.
l = arr12.reshape(2,3,2)
print(l)

##unknown dimension

arr13 = np.array([1,2,3,4,5,6,7,8])
c = arr13.reshape(2,2,-1)
print(c)

## Flattening the array to 1 d array
a = arr5.reshape(-1)
print(a)

## Numpy array interating

for x in arr:
    print(x)


## In a 2-D array it will go through all the rows
for x in arr3:
    print(x)

for x in arr3:
    for y in x:
        print(y)


##In a 3-D array it will go through all the 2-D arrays.
for x in arr4:
    print(x)

for x in arr4:
    for y in x:
        for z in y:
            print(z)

## Iterating Arrays Using nditer()

for x in np.nditer(arr4):
    print(x)

# Iterating Array With Different Data Types

# We can use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating.

# NumPy does not change the data type of the element in-place (where the element is in array) so it needs some other 
# space to perform this action, that extra space is called buffer, and in order to enable it in nditer() we pass flags=['buffered'].

for x in np.nditer(arr , flags=['buffered'] , op_dtypes=['S']):
    print(x)

## Iterate through every scalar element of the 2D array skipping 1 element:

for x in np.nditer(arr3[:, ::2]):
    print(x)

# Enumerated Iteration Using ndenumerate()
# Enumeration means mentioning sequence number of somethings one by one.

# Sometimes we require corresponding index of the element while iterating, the ndenumerate() method can be used for those usecases.

for idx, x in np.ndenumerate(arr4):
    print(idx , x)


arr14 = np.array([1,2,3])
arr15 = np.array([4,5,6])

arr_res = np.concatenate((arr14 , arr15))
print(arr_res)

## Join two 2-D arrays along rows (axis=1):

arr16 = np.array([[1,2] , [3,4]])
arr17 = np.array([[5,6] , [7,8]])

## We pass a sequence of arrays that we want to join to the concatenate() function, along with the axis. If axis is not explicitly passed, it is taken as 0.

arr_res1 = np.concatenate((arr16 , arr17) , axis=1)
print(arr_res1)

## We pass a sequence of arrays that we want to join to the stack() method along with the axis. If axis is not explicitly passed it is taken as 0.

arr_st = np.stack((arr16 , arr17) , axis=1)
print(arr_st)

arr_st1 = np.stack((arr14 , arr15) , axis=1)
print(arr_st1)

## NumPy provides a helper function: hstack() to stack along rows.

arr_hst = np.hstack((arr14 , arr15))
print(arr_hst)

##NumPy provides a helper function: vstack()  to stack along columns.
arr_vst = np.vstack((arr14 , arr15))

print(arr_vst)

arr_vst1 = np.vstack((arr16 , arr17))

print(arr_vst1)

## NumPy provides a helper function: dstack() to stack along height, which is the same as depth

arr_dst = np.dstack((arr14 , arr15))
print(arr_dst)

arr_dst1 = np.dstack((arr16 , arr17))
print(arr_dst1)

## We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.

newsplitarr = np.array_split(arr , 3)
print(newsplitarr)

print(newsplitarr[0])
print(newsplitarr[1])
print(newsplitarr[2])


arr18 = np.array([[1,2] ,[3,4] ,[5,6] ,[7,8] ,[9,10] ,[11,12]])

newsplitarr2d = np.array_split(arr18 , 3)

print(newsplitarr2d)
print(newsplitarr2d[0])
print(newsplitarr2d[1])
print(newsplitarr2d[2])

arr19 = np.array([[1,2,3] ,[4,5,6] ,[7,8,9] ,[10,11,12] ,[13,14,15] ,[16,17,18]])

newarr = np.array_split(arr19 , 3, axis=1)
print(newarr)

newarr1 = np.hsplit(arr19 , 3)
print(newarr1)


# Searching Arrays
# You can search an array for a certain value, and return the indexes that get a match.

# To search an array, use the where() method.
x1 = np.where(arr==4)
print(x1)

x2 = np.where(arr%2==1)
print(x2)

## Search Sorted
# There is a method called searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.
arr20 = np.array([6, 7, 8, 9])

x3 = np.searchsorted(arr20 , 7 , side='right')

print(x3)


arr21 = np.array([1, 3, 5, 7])

x4 = np.searchsorted(arr, [2, 4, 6])

print(x4)

arr22 = np.array([3,2,0,1])
print(np.sort(arr22))

arr23 = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr23))


arr24 = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr24))

# Filtering Arrays
# Getting some elements out of an existing array and creating a new array out of them is called filtering.

# In NumPy, you filter an array using a boolean index list.

# If the value at an index is True that element is contained in the filtered array, if the value at that index is False that element is excluded from the filtered array.

arr25 = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr4 = arr25[x]

print(newarr4)

filter_arr = []

# for element in arr25:
#     if element >42:
#         filter_arr.append(True)
#     else:
#         filter_arr.append(False)
filter_arr = arr25 >42
newarr5 = arr25[filter_arr]

print(filter_arr)
print(newarr5)


filter_arr1 = []

# for element in arr:
#     if element %2 == 0:
#         filter_arr1.append(True)
#     else:
#         filter_arr1.append(False)

filter_arr1 = arr%2==0

newarr6 = arr[filter_arr1]

print(filter_arr1)
print(newarr6)