import numpy as np

arr1 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(arr1)

print(arr1[0,0])

print(arr1[-1,-1])

# accessing rows
print(arr1[0])
print(arr1[2])


# accessing columns

print(arr1[:,2])

# slicing the matrix

print(arr1[0:2])