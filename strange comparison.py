str1 = input()
str2 = input()

# Фильтруем и приводим к нижнему регистру
filtered1 = ''.join(char.lower() for char in str1 if char.isalpha())
filtered2 = ''.join(char.lower() for char in str2 if char.isalpha())

if filtered1 == filtered2:
    print("YES")
else:
    print("NO")