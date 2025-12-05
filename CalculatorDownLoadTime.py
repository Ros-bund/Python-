import time
print('========Калькулятор времени скачки========')
print()
Speed_Download = float(input('Пожалуста введите вашу скорость в мегаБИТАХ: '))
print()
Weight_Game = float(input('Пожалуста введите вес файла в гигаБАЙТАХ: '))
print()
MB = Speed_Download / 8
print(f'Принял команду!')
time.sleep(1)
Weight_MB = Weight_Game * 1024
print(f'Так, ага произвожу расчеты')
time.sleep(2)
Time_Second = Weight_MB / MB
print(f'Время в секундах: {Time_Second:.2f}')
Time_Min = Time_Second / 60
print(f'Время в минутах: {Time_Min:.2f}')
Time_Hour = Time_Min / 60
print(f'Время в часах: {Time_Hour:.2f}')
print()
print('===============Конец===============')
print('Внимание, это примерное время \nтак как во время скачки может произойти многое')