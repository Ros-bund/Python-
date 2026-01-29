# Инициализируем переменные для минимальной и максимальной строк
first_string = input()

# Если сразу ввели "КОНЕЦ"
if first_string == "КОНЕЦ":
    # Последовательность пустая - нет строк для сравнения
    min_string = ""
    max_string = ""
else:
    # Первая строка становится и минимумом и максимумом
    min_string = first_string
    max_string = first_string
    
    # Читаем остальные строки
    while True:
        current_string = input()
        if current_string == "КОНЕЦ":
            break
        
        # Обновляем минимум
        if current_string < min_string:
            min_string = current_string
            
        # Обновляем максимум
        if current_string > max_string:
            max_string = current_string

# Выводим результат
print(f"Минимальная строка ⬇️: {min_string}")
print(f"Максимальная строка ⬆️: {max_string}")