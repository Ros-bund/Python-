n = int(input())

# Допустимые буквы класса
valid_letters = "АБВГДЕЖЗИЙКЛМНОП"

# Проверяем n названий классов
for _ in range(n):
    class_name = input()
    
    # Проверяем длину (должно быть ровно 2 символа)
    if len(class_name) != 2:
        print("NO")
    else:
        # Проверяем первый символ (цифра 0-9)
        if not ('0' <= class_name[0] <= '9'):
            print("NO")
        # Проверяем второй символ (буква А-П)
        elif class_name[1] not in valid_letters:
            print("NO")
        else:
            print("YES")