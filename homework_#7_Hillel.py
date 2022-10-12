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
sum1 = 0
for person in my_dict:
    sum1 = sum1 + person.get('age')
print(sum1 // len(my_dict))

# Homework #2
dict1 = {1: 1, 2: 5, 3: 10, 4: 15, 5: 20}
dict2 = {6: 11, 7: 15, 3: 21, 9: 28, 5: 31}

# а) Список из ключей, которые есть в обоих словарях
all_dict = []
for key in dict1:
    if key in dict2.keys():
        all_dict.append(key)
print('keys: ', all_dict)

# б) Список из ключей, которые есть в первом, но нет во втором словаре.
# 1й способ
all_dict = list(key for key in dict1 if key not in dict2.keys())
print('keys:', all_dict)

# 2й способ
all_dict2 = []
for key in dict1:
    if key not in dict2.keys():
        all_dict2.append(key)
print('keys:', all_dict2)

# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
# 1й способ
new_dict = dict(new for new in dict1.items() if new[0] not in dict2)
print(new_dict)

# 2й способ
for new in dict1.items():
    if new[0] not in dict2:
        new_dict = dict(new_dict)
print(new_dict)

# г) Объединить эти два словаря в новый словарь по правилу:

my_dict3 = {}
for new in dict1.items():
    if new[0] in dict2:
        my_dict3[new[0]] = [new[1], dict2[new[0]]]
    else:
        my_dict3[new[0]] = new[1]
print(my_dict3)
