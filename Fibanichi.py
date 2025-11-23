n = int(input())

if n == 1:
    print(1)
elif n >= 2:
    a, b = 1, 1
    print(a, b, end=' ')
    
    for i in range(2, n):
        a, b = b, a + b
        print(b, end=' ')