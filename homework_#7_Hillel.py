# Homework #1
my_dict = [{"name": "John", "age": 15},
           {"name": "Alexandr", "age": 25},
           {"name": "Jack", "age": 45},
           {"name": "Vladimir", "age": 15},
           {"name": "Vladislav", "age": 72},
           {"name": "Edward", "age": 16}]

# а) Программа для получения имени самого молодого человека из списка.
min_age = float('inf')
for person in my_dict:
    if person['age'] < min_age:
        min_age = person['age']
names_min_age = [p['name'] for p in my_dict if p['age'] == min_age]
print(names_min_age)

# б) Программа для получения самого длинного имени из списка.
max_longer = float('-inf')
for persons in my_dict:
    if len(persons['name']) > max_longer:
        max_longer = len(persons['name'])
names_max_longer = [p['name'] for p in my_dict if len(p['name']) == max_longer]
print(names_max_longer)

# в) Посчитать среднее количество лет всех людей из начального списка
sum = 0
for person in my_dict:
    sum = sum + person.get('age')
print(sum // len(my_dict))

# Homework #2
# 2)Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях -
# поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
#
# {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}