# Homework #1
def set1(a: str = 'Valeriy', b: str = 'Vova', c: str = 'Sergey', d: str = 'Pasha'):
    my_list = [a] + [b[::-1]] + [c] + [d[::-1]]
    return my_list


new_list = set1()

# Homework 2
# Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list у которых первый символ - буква "a".

# def set2(a: str = 'Valeriy', b: str = 'Vova', c: str = 'Sergey', d: str = 'Pasha', s: str = 'Aleksey'):
#     my_list2 = [a, b, c, d]
#     for element in:
#         if element in my_list2:
#             my_list2 = element.find('a')
#     return my_list2
#
#
# new_list2 = set2()
# print(new_list2)
