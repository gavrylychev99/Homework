# Homework #1
children_school = int(input('Введите количество школьников:'))

apple = int(input('Теперь введите количество яблок:'))
print('Отлично')

amount_children_school = (apple // children_school)
print(f'У каждого школьника останется', amount_children_school)

basket = (apple % children_school)
print(f'Останется в корзинке, {basket}')

# Homework #2
Classroom1 = int(input('Введите количество учеников первого класса:'))
Classroom2 = int(input('Введите количество учеников второго класса:'))
Classroom3 = int(input('Введите количество учеников третьего класса:'))
Desks = int(Classroom1+Classroom2+Classroom3)/2
if int(Classroom1+Classroom2+Classroom3) % 2 == True:
    print(f'Всего нужно закупить:{Desks + 0.5}')
else:
    print(f'Всего нужно закупить:{Desks}')

# Homework #3
num1 = int(input('введите число:'))
num2 = num1 % 10 * 100
num3 = num1 // 10
num3 = num3 % 10 * 10
num4 = num1 // 10 // 10
print(num2+num3+num4)
