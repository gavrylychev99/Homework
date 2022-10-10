# my_dictionary = {'key': 'value'}
# user = {'firstname': 'Valeriy',
#         'lastname': 'Havrylychev',
#         'items': ['шапка', 'гусли']}
# print(user['items'][0])

my_dict1 = {"name": "John",
            "lastname": "Havrylychev",
            "age": [17, 15, 13, 11],
            "email": 'gavrylychev99@gmail.com'}

print(my_dict1['age'][2])
print(list(my_dict1.values()))
print(list(my_dict1.keys()))
print(my_dict1.get('login'))
