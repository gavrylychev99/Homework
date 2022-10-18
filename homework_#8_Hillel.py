# Homework #1
def set1(a: str = 'Valeriy', b: str = 'Vova', c: str = 'Sergey', d: str = 'Pasha'):
    my_list = [a] + [b[::-1]] + [c] + [d[::-1]]
    return my_list


new_list = set1()
print(new_list)

# Homework #2





# my_list1 = []
# for element in my_list:
#     if element == my_list[1::2]:
#         my_list1 = my_list[::-1]
#     elif element == my_list[::2]:
#         my_list1 = element
# return my_list1
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
