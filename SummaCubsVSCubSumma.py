a = int(input())
b = int(input())

SummaCubs = (a ** 3) + (b ** 3)
CubSumma = (a + b) ** 3

print(f'Для чисел {a} и {b}:')
print(f'  Сумма кубов: {a}**3 + {b}**3 = {SummaCubs}')
print(f'  Куб суммы: ({a} + {b})**3 = {CubSumma}')