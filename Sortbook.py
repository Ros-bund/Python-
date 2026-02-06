n = int(input())

prev_author = ""
prev_title = ""
is_sorted = True

for i in range(n):
    book = input()
    
    # Разделяем строку на части
    # Формат: "Фамилия И.О., «Название»"
    parts = book.split(', ')
    
    # Фамилия автора (первое слово до пробела в первой части)
    author = parts[0].split()[0]
    
    # Название книги (удаляем « и »)
    title = parts[1].strip('«»')
    
    if i > 0:  # Начиная со второй книги сравниваем с предыдущей
        # Сравниваем сначала фамилии, потом названия
        if prev_author > author or (prev_author == author and prev_title > title):
            is_sorted = False
            break
    
    # Сохраняем текущие значения для следующего сравнения
    prev_author = author
    prev_title = title

if is_sorted:
    print("YES")
else:
    print("NO")