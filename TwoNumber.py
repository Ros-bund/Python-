n = int(input())

temp = n
count = 0
while temp > 0:
    count += 1
    temp //= 10

for i in range(count - 2):
    n //= 10
two_number = n % 10

print(two_number))