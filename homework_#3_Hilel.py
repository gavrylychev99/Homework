# Homework #1 (calculater '+, -, *, /, **' )
num1 = int(input('введите первое число: '))
action = input('введите действтие:''+, -, *, /, ** : ')
num2 = int(input('введите второе число: '))
if action == '+':
    print(num1 + num2)
elif action == '-':
    print(num1 - num2)
elif action == '*':
    print(num1 * num2)
elif action == '/':
    if num2 == 0:
        print('деление на 0!')
    else:
        print(int(num1 / num2))
elif action == '**':
    print(num1 ** num2)

# Homework #2
n = int(input('введите число: '))
a = 1
for i in range(a, n):
    if i ** 2 < n:
        i = i ** 2
        print(i, end=' ')

# Homework #3
a = int(input('введите число:'))
b = 0
for i in range(2, a // 2 + 1):
    if a % i == 0:
        b = b + 1
if b <= 0:
    print('Это простое число')
else:
    print('Не подходит')
