a = int(input())
b = int(input())

for num in range(a, b + 1):
    if num < 2:
        continue
    
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(num)