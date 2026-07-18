import numpy as np

arr1 = np.array([1,2,3,4,5,6,7,8,9])

print(arr1[[0,5,7]])

arr2 = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

print(arr2[[0,2]])

print(arr2[[0,1],1])

arr3 = np.array([2,3,4,5,6,7,8])

print(arr3>4)

arr4 = np.array([
    [2,4,60,3],
    [11,13,23,49]
])

print(arr4[arr4%2==0])

arr5 = np.array([3,6,7,8,9])

arr5[arr5>3] = 99
print(arr5)

arr6 = np.array([5,10,15,20,25,30])
arr6 = np.where(arr6>10, 1, 0)

print(arr6)

# mini challenge
marks = np.array([45, 72, 88, 91, 63, 55, 99, 38])

print(marks[marks>=60])
print(marks[marks<50])

print(marks[marks%2==0])




t4 = np.where(marks<40,40,marks)

t5 = np.where(marks>=50,'PASS','FAIL')
print(t5)

