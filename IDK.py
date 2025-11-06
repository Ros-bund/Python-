num = int(input())
Max = 0
Min = 9
while num != 0:
    lust = num % 10
    if lust > Max:
        Max = Max
    
    
    if lust > Min:
        Min = Min
    num //= 10
print(Max)
print(Min)