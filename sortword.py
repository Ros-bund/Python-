# Считываем три слова
word1 = input()
word2 = input()
word3 = input()

# Помещаем слова в список
words = [word1, word2, word3]

# Сортируем список
sorted_words = sorted(words)

# Выводим отсортированные слова через пробел
print(sorted_words[0], sorted_words[1], sorted_words[2])