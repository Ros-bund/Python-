letter = input()

# Получаем код текущей буквы
current_code = ord(letter)

# Проверяем, не является ли буква последней в алфавите (Я)
if letter == 'Я':
    print("Дальше букв нет")
else:
    # Получаем код следующей буквы
    next_code = current_code + 1
    # Преобразуем код обратно в букву
    next_letter = chr(next_code)
    print(next_letter)