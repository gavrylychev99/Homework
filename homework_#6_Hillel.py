# from random import randint

# # # Homework 1
# num = int(input('Введите число: '))
# num = str(num)
# result = 0
# for i in num:
#     if i == '0':
#         result += 1
# print(result)

# # Homework 2
# num = int(input('Введите число: '))
# num = str(num)
# result = 0
# for i in num[::-1]:
#     if i == '0':
#         result += 1
#     else:
#         break
# print(result)

# # # # Homework 3
# my_list1 = [randint(1, 10) for i in range(10)]
# my_list2 = [randint(11, 20) for a in range(10)]
# my_result = my_list1[1::2] + my_list2[::2]
# print(my_result)

# # # Homework 4
# my_list = [randint(1, 20) for i in range(5)]
# new_list = my_list.copy()
# new_list.pop(0)
# new_list = new_list + my_list[0:1]
# print(my_list)
# print(new_list)

# # # Homework 5
# my_list = [randint(1, 20) for i in range(5)]
# print(my_list)
# my_list1 = my_list.pop(0)
# my_list.append(my_list1)
# print(my_list)

# # # Homework 6
# string = '31 больше 11 но меньше 54'
# new_str = string.split()
# num = 0
# for i in new_str:
#     if i.isdigit():
#         num += int(i)
# print(num)

# # # Homework 7
# my_str = 'My long string'
# l_limit = 'o'
# r_limit = 'g'
# search1 = my_str.find(l_limit) + 1
# search2 = my_str.rfind(r_limit)
# sub_str = my_str[5:13]
# print(sub_str)

# # Homework 8
# my_str1 = 'abdcdee'
# result = []
# for element in range(0, len(my_str1), 2):
#     result.append(my_str1[element:element + 2])
#     if len(result[-1]) < 2:
#         result[-1] += '_'
# print(result)

# Homework 9


# Homework 10
# my_list = [1, 2, 3, "11", "22", 33]
# new_li = []
# for element in my_list:
#     if type(element) == str:
#         new_li.append(element)
# print(new_li)

# Homework 11
# my_str = 'fsdfsdtwefsdfsdf'
# a = []
# for i in my_str:
#     if my_str.count(i) == 1:
#         a.append(i)
# print(a)
