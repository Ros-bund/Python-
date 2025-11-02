slovo = input()
count = 0
while slovo != 'стоп' and slovo != 'хватит' and slovo != 'достаточно':
    print(slovo)
    slovo = input()
    count += 1
print(count)