n = int(input())
current = 1

for i in range(1, n + 1):
    row = []
    for j in range(i):
        row.append(str(current))
        current += 1
    print(" ".join(row))