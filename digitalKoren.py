n = int(input())
while n > 9:
    total = 0
    temp = n
    while temp > 0:
        total += temp % 10 
        temp //= 10
    n = total
print(n)