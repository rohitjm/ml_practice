import numpy as np

# Creating and Accessing Elements in a numpy array
# Slicing

arr = np.array([1,2,3,4])
print(type(arr))
print(arr.dtype)

arr2 = np.array([5,6,7,8],dtype='int8')
print(type(arr2))
print(arr2.dtype)

print(type([1,2,3,4]))

# Creating a 2dimensional array with numpy w/ operations
arr3 = np.array([[1,2,3,4],[5,6,7,8]])
print(arr3)
print(arr3.size)
print(arr3.ndim)
print(arr3.shape)

arr4 = np.array([[[1,2,3,4],[5,6,7,8],[5,6,7,8]],[[9,10,11,12],[13,14,15,16],[55,66,32,23]]])
print(arr4)
print(arr4.size)
print(arr4.ndim)
# print(arr4.shape)

# Slicing and Accessing elements
# print("1st element of 1st row in 1st row:",arr4[0,0,0])
# print("3rd element of 2nd row in 1st row:",arr4[0,1,2])
# print(arr4[1,0,:2])
# print(arr4[0,1,-3:])
print(arr4[1:,1:,1:]) # start:stop:step

# Slicing of 2-d and n-d arrays
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]]) # 2*5
print(arr[0:2,2:5])
# expected output: ([3,4,5],[8,9,10])

print(arr[1,1:4])
# expected output: ([7,8,9])

print(arr[0:2,2])
# expected output: ([3,8])
