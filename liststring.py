# Считываем количество строк
n = int(input())

# Создаем пустой список для хранения строк
lines = []

# В цикле считываем n строк и добавляем их в список
for _ in range(n):
    string = input()
    lines.append(string)

# Выводим итоговый список
print(lines)