# tuples

t1 = (10,20,30,"ahmad")
print(t1[3])


print(len(t1))

print(t1[1:4])  #slcicing

print(20 in t1)

# tuple unpacking

t = (10,20,20)
a,b,c = t
print(a)
print(b)
print(c)

#task 1
task1 = (19,20,490,49)
print(task1[0])  #first elemt
print(task1[-1]) #last element

#task 2

print(490 in task1)

#task 3

task3 = (5, 10, 15)

d,e,f = task3

print(d)
print(e)
print(f)


#task4

for n in task1:
    if n>25:
        print(n)