import numpy as np

# Copying and Viewing Arrays
# A copy is a "deep" copy while a view is a "shallow" copy

print("Array Copy")
arr = np.array([1,2,3,4])
copied_arr = arr.copy()
copied_arr[0] = 42
print(arr)
print(copied_arr)
print(f"id of orignial arr {id(arr)} v. id of copied arr: {id(copied_arr)}")

print("Array View")
arr1 = np.array([1,2,3,4])
viewed_arr = arr1.view()
viewed_arr[0] = 42
print(arr1)
print(viewed_arr)
print(f"id of orignial arr {id(arr1)} v. id of viewed arr base: {id(viewed_arr.base)}")

# Setting dimensions at array init
print("np.array([1,2,3,4],[5,6,7,8])")
arr = np.array([[1,2,3,4],[5,6,7,8]])
print(arr)
print(arr.ndim)
print(arr.shape)

print("np.array([1,2,3,4], ndmin=4)")
arr = np.array([1,2,3,4], ndmin=4)
print(arr)
print(arr.ndim)
print(arr.shape)

# ReShaping
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
print(arr)
print(arr.ndim)
print(arr.shape)
print("ReShaping..")
arr2 = arr.reshape(1,2,1,4,2)
print(arr2)
print(arr2.ndim)
print(arr2.shape)
