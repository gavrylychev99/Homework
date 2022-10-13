# Функции в отдельном модуле, проверка работоспосмобности в main
# 1. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.

# Homework #1
# my_list = ['Alisa', 'Andrey', 'Vova','Nikita','Alexandr']

def set1(a: str = 'Alisa', b: str = 'Andrey', c: str = 'Vova', d: str = 'Nikita', e: str = 'Alexandr'):
    my_list =



# def create_point(x: float = 1, y: float = 10, z: float = 9):
#     point = {'x': x,
#              'y': y}
#     return point
#
#
# p = create_point(3, 4)
# print(p)
#
#
# def where_is_point(point: dict):
#     if point['x'] < 0 and point['y'] > 0:
#         return 1
#     else:
#         return 2
#
#
# print(where_is_point(p))
