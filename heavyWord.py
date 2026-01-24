# Считываем 4 слова
words = []
for _ in range(4):
    word = input()
    words.append(word)

# Переменные для хранения максимального веса и самого тяжёлого слова
max_weight = 0
heaviest_word = ""

# Перебираем все слова
for word in words:
    # Считаем вес текущего слова
    current_weight = 0
    for char in word:
        current_weight += ord(char)
    
    # Если текущий вес больше максимального, обновляем
    if current_weight > max_weight:
        max_weight = current_weight
        heaviest_word = word

# Выводим самое тяжёлое слово
print(heaviest_word)