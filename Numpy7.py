# practice problem 1
import numpy as np
arr = np.array([5,10,15,20,25,30])

print(arr[2])
print(arr[-1])
print(arr[2:5])
print(arr[0:-1: 2])

# PRACTICE PROBLEM 2 
arr2 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(arr2[1,1])
print(arr2[-1])
print(arr2[:,0])
print(arr2[1: ,1:])

# practice peoblem 3
marks = np.array([35,48,46,78,90])
print(marks[marks>60])
print(marks[marks<50])
print(marks[(marks>50) & (marks <=80)])

# HOMEWORK

data = np.array([
    [12,34,56],
    [67,78,75],
    [10,89,94]
])

print(data[0])
print(data[:,1])
print(data[-1])
print(data[1,1])
print(data[:2])
print(data[:,1:])
print(data[data>50])
print(data[(data>= 30) &(data<=80)])

