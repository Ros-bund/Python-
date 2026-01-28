# Считываем 4 слова
words = []
for _ in range(4):
    word = input()
    words.append(word)

# Находим самую "маленькую" и самую "большую" строки
smallest_word = min(words)
largest_word = max(words)

# Берём последние символы этих слов
last_char_smallest = smallest_word[-1] if smallest_word else ''
last_char_largest = largest_word[-1] if largest_word else ''

# Находим их коды
code_smallest = ord(last_char_smallest)
code_largest = ord(last_char_largest)

# Вычисляем волшебное число
magic_number = (code_smallest * code_largest) ** 2

print(magic_number)