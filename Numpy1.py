import numpy as np

arr1 = np.array([
    [1,3,4],
    [6,9,7]
])

print(arr1.shape)

# create 3D array

arr2 = np.array([
    [
        [1,2,3],
        [4,5,6]
    ],
    [
    [7,8,9],
    [10,11,12]]
])

print(arr2.shape)

print(arr1.ndim)
print(arr2.ndim)

#1D ARRAY

arr3 = np.array([2,4,6.8,8])
print(arr3.shape)


print(arr3.dtype)


# PRACTICE QUESTIONS

#q1
ar1 = np.array([1,2,3,4])
print(ar1)

#q2
ar2 = np.array([
    
        [1,2],
        [3,4],
        [5,6]
    
])

print(ar2)

#q3

ar3 = np.array([
    [10,20,30],
    [40,50,60]
    
])

print(ar3)
print(ar3.shape)
print(ar3.ndim)
print(ar3.size)

#q4
ar4 = np.array([1,2,3,4])
ar4_1 = ar4.astype(float)

print(ar4_1.dtype)


#q5
ar5 = np.array([3.14, 5.6, 8.9])
print(ar5.dtype)


# MINI CHALLENGE

arr5 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(arr5)
print(arr5.shape)
print(arr5.size)
print(arr5.ndim)
print(arr5.dtype)

