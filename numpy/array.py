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