# Homework #1
from random import randint

my_list = [randint(1, 200) for i in range(10)]
for element in my_list:
    if element > 100:
        print(element, end=' ')
print()

# Homework #2
my_list = [randint(1, 200) for i in range(20)]
my_results = []
for i in my_list:
    if i > 100:
        my_results.append(i)
print(my_list)
print(my_results)

# # Homework #3
my_list = [randint(1, 10) for i in range(5)]
if len(my_list) >= 2:
    my_list.append(my_list[-1] + my_list[-2])
else:
    my_list.append(0)
print(my_list)
