import numpy as np

ar1 = np.arange(1,10)
print(ar1)


# reshape the array

arr1 = ar1.reshape(3,3)
print(arr1)

# create zeros

arr2 = np.zeros(7)
print(arr2)


# create ones

arr3 = np.ones((3,3))
print(arr3)


# full function

arr4 = np.full((2,3),8)
print(arr4)

# identity matrix

arr5 = np.eye(4)
print(arr5)

# linspace 

arr6 = np.linspace(1,10,5)
print(arr6)

# random number

# float
arr6 = np.random.rand(3,3)
print(arr6)

# integar

arr7 = np.random.randint(1,10,size = (3,3))
print(arr7)

# Practice questions

# question - 1

p1 = np.arange(5,11)
print(p1)

# question - 2

p2 = np.arange(1,7)

p2 = p2.reshape(2,3)

print(p2)


# question - 3
p3 = np.zeros((4,4))

print(p3)

# question - 4
p4 = np.ones((2,5))
print(p4)

# question - 5
p5 = np.full((3,3),99)
print(p5)

# question - 6
p6 = np.eye(5,5)
print(p6)

# question - 7
p7 = np.linspace(0,30,6)
print(p7)

# question - 8
p8 = np.random.randint(10,50,size=(4,4))
print(p8)


