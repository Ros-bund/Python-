text = input()

text_lower = text.lower()

adenin = text_lower.count('а')
guanin = text_lower.count('г')
citozin = text_lower.count('ц')
timin = text_lower.count('т')

print('Аденин:', adenin)
print('Гуанин:', guanin)
print('Цитозин:', citozin)
print('Тимин:', timin)