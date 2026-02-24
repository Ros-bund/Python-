# 1. Читаем количество чисел
n = int(input())

# 2. Создаем и наполняем список
numbers = []
for _ in range(n):
    num = int(input())
    numbers.append(num)

# 3. Удаляем элементы по нечетным индексам
# Мы идем от последнего индекса (len(numbers) - 1) до 0 с шагом -1
for i in range(len(numbers) - 1, -1, -1):
    if i % 2 != 0:  # Проверяем, является ли индекс нечетным
        del numbers[i]

# 4. Выводим результат
print(numbers)