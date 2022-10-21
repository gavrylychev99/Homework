# Homework #1
def set1(my_list: list):
    new_list = []
    for index in range(len(my_list)):
        if index % 2 != 0:
            new_list.append(my_list[index][::-1])
        else:
            new_list.append(my_list[index])
    return new_list


li = ['Valeriy', 'Vova', 'Sergey', 'Pasha', 'Kirill']
print(set1(li))


# Homework 2
def set2(my_list: list):
    new_list = []
    for element in my_list:
        if element[0] == 'A':
            new_list.append(element)
    return new_list


li2 = ['Alexandr', 'Vova', 'Sergey', 'Pasha', 'Kirill']
print(set2(li2))


# Homework 3
def set3(my_list: list):
    new_list = []
    for element in my_list:
        if element.find('a') != -1:
            new_list.append(element)
    return new_list


li3 = ['Valeriy', 'Vova', 'Sergey', 'Pasha', 'Kirill']
print(set3(li3))

# Homework 4
