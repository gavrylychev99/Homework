height = int(input('введите число: '))

# Homework 1
for h in range(0, height):
    for w in range(0, h + 1):
        print('*', end=' ')
    print()
for h in range(height, 0, - 1):
    for w in range(0, h - 1):
        print('*', end=' ')
    print()

# Homework 2
for h in range(height, 0, - 1):
    for i in range(h, height):
        print(' ', end=' ')
    for w in range(0, h):
        print('*', end=' ')
    for n in range(0, h - 1):
        print('*', end=' ')
    print()

print()
# Homework 3
for h in range(0, height):
    for k in range(0, height):
        print(' ', end=' ')
    for i in range(h, height - 1):
        print(' ', end=' ')
    for w in range(0, h + 1):
        print('*', end=' ')
    print()
for h in range(0, height - 1):
    for k in range(0, height):
        print(' ', end=' ')
    for i in range(0, h + 1):
        print(' ', end=' ')
    for s in range(h, height - 1):
        print('*', end=' ')
    print()

print()
# Homework 4
for h in range(0, height):
    for i in range(h, height - 1):
        print(' ', end=' ')
    for w in range(0, h + 1):
        print('*', end=' ')
    for n in range(0, h):
        print('*', end=' ')
    print()

print()
# Homework A
for h in range(0, height):
    for i in range(h, height - 1):
        print(' ', end=' ')
    for w in range(0, h):
        if h == 0 or w == 0 or h == height - 1 or w == h:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    for n in range(0, h + 1):
        if h == height - 1 or n == h or h == n or n == h:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

print()
# Homework B
for h in range(0, height):
    for i in range(h, height - 1):
        print(' ', end=' ')
    for w in range(0, h + 1):
        print('*', end=' ')
    for n in range(0, h):
        print('*', end=' ')
    print()

print()
# Homework C
for h in range(0, height):
    for i in range(h, height - 1):
        print(' ', end=' ')
    for w in range(0, h + 1):
        print('*', end=' ')
    for n in range(0, h):
        print('*', end=' ')
    print()
for h in range(0, height):
    for i in range(0, h + 1):
        print(' ', end=' ')
    for w in range(height, h + 1, -1):
        if h == w or w == height or h == w - 1 or w == h:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    for n in range(h + 1, height - 1):
        if h == height or n == height - 2 or h == n or n == h:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

# Homework D
for h in range(0, height):
    for i in range(h, height - 1):
        print(' ', end=' ')
    for w in range(0, h + 1):
        print('*', end=' ')
    for n in range(0, h):
        print('*', end=' ')
    print()
for h in range(0, height):
    for i in range(0, h + 1):
        print(' ', end=' ')
    for w in range(height - 1, h, -1):
        if h == w or w == height - 1 or h == w - 1 or w == h + 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    for n in range(height - 3, h - 1, -1):
        if h == n:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
