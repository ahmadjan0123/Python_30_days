#sets

set1 = {1,2,3,3,4}
print(set1)

set1.add(7)
set1.remove(2) # error if not present
set1.discard(10) #no error- silently executed
print(set1) 


a  = {1,2,3}
b= {4,5,6}
print(a | b)  #union 


print(a & b) #intersection

print(a-b) # difference - present i a not in b

'''
Task 1:

Create a set of numbers and:

Add 2 new numbers
Remove 1 number
'''

task1 = {1,2,3}
task1.add(4)
task1.add(5)

task1.remove(1)
print(task1)

#task2
task2 =  set([1,2,2,3,4,4,5])

for q in task2:
    print(q)


#task 3
a1 = {10, 20, 30}
b1 = {20, 30, 40}

print(a1 & b1)

#task 4
s = {5, 10, 15}
 
if 7 in s:
    print("Yes")
else:
    print("NO")

#task 5

classA = {"Ali", "Sara", "Ahmed"}
classB = {"Sara", "Zain", "Ali"}

print(classA & classB)  #students in both the classess
print(classA | classB)  # students in both the classess
print(classA-classB) # students only in class a


nums = set([10, 20, 20, 30, 40, 40, 50])

print(nums)

for q in nums:
    if q>25:
        print(q)

nums2 = {20,30,60}

print(nums & nums2)