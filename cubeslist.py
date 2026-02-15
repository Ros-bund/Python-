# Считываем количество чисел
n = int(input())

# Создаем пустой список для кубов
cubes = []

# В цикле считываем каждое число и возводим его в куб
for _ in range(n):
    number = int(input())
    cubes.append(number ** 3)

# Выводим готовый список
print(cubes)