#Problem Solving with Functions + Lists (Interview Style)

def find_max(nums):
    max = nums[0]

    for i in nums:
        if i> max:
            max = i

    return max

print(find_max([3,6,8,9,13]))


def reverse_series(lst): # 1,2,3,4,

    reverse_list = []

    for i in lst:
        reverse_list = [i] + reverse_list

    return reverse_list

print(reverse_series([1,2,3,4]))


print("\nTASK 1")

def find_min(lst):
    smallest = lst[0]

    for i in lst:
        if i < smallest:
            smallest = i
    return smallest


print(find_min([1,3,5,6]))


print("\nTASK 2")

def task2(lst):
    even_list = []

    for i in lst:
        if i%2 == 0:
            even_list.append(i)

    return even_list

print(task2([2,3,4,6]))


def task3(lst):

    even_total = 0
    odd_total = 0

    for i in lst:
        if i%2== 0:
            even_total += i
        else:
            odd_total += i
    return     even_total,odd_total   
    #print(f"The sum of even numbers is: {even_total}")
    #print(f"The sum of odd numbers is: {odd_total}")



even , odd = task3([5, 10, 15, 20, 25])
print(f"EVEN: {even}")
print(f"ODD: {odd}")