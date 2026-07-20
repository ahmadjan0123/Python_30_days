import numpy as np

a1 = np.array([1,2,3,4])
a2 = np.array([5,6,7,8])

print('sum of the arries is:',a1+a2)
print('difference between the two arraies is:',a1-a2)
print('multiple of the arries is:',a1*a2)
print('division of the arries is:',a1/a2)
print('floor of the arries is:',a1//a2)
print('ai to the power 2:',a1**2)



# MULTIPLICATION GROUP

a3 = np.array([1,4,9,16,25])

sqaure_root = np.sqrt(a3)
print(sqaure_root)

sqaure = np.square(a3)
print(sqaure)

exp = np.exp(a3)
print(exp)

log = np.log(a3)
print(log)


# statistical functions

mark = np.array([2,4,6,8,10])
mean = np.mean(mark)
print(mean)


var = np.var(mark)
print(var)
std = np.std(mark)
print(std)

maxx = np.max(mark)
print(maxx)

minn = np.min(mark)
print(minn)


# Rounding Functions

x = np.array([2.34,5.68,7.87,9.85])
print(np.round(x,1))

print(np.floor(x))

# problems

data= np.array([12.47,16.78,23.47,57.78])

print('Mean',np.mean(data))
print('Median:',np.median(data))
print('Sum',np.sum(data))
print('Variance',np.var(data))
print('STD:',np.std(data))
print('Max',np,max(data))
print('min',np.min(data))
print('Sqaure Root',np.sqrt(data))
print('square',np.square(data))
print('LESS THAN 50: ',data>50)