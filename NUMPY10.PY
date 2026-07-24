import numpy as np

arr = np.array([[10,20,30,50],[60,70,80,90]])

print(arr[[0],[2]])

arr1 = np.array([15,9,23,43])
print(np.where(arr1>10))

arr2= np.array([[1,2,56,43],[43,56,42,13]])
print(np.where(arr2>4,0,arr))

arrr = np.arange(1,26)
arrr = arrr.reshape(5,5)
print(arrr)
print(arrr)

print(arrr[[0,3]])

print(arrr[[0,2,4],[4,2,0]])

print(np.where(arrr>18,999,arrr))

print(np.where(arrr/3))

print(arrr[(arrr>=10) & (arrr<=20)])