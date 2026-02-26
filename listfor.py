numbers = [2, 1, 1, 3, 4]

total = 0
for num in numbers:
    if num % 2 == 1:
        total = total + num

print(total)