s = input()

for char in s:
    if char.isdigit():
        print('Цифра')
        break
else:
    print('Цифр нет')