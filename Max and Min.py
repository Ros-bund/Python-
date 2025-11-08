num = int(input())
Max = 0
Min = 9
while num != 0:
    lust = num % 10
    if lust > Max:
        Max = lust
    
    
    if lust < Min:
        Min = lust
    num //= 10
print(f'Максимальная цифра равна {Max}')
print(f'Минимальная цифра равна {Min}')