import time
print('=====EasyMathPanel====')
print()
print('1-- Сложение')
print('2-- Вычитание')
print()

Command_Panel = int(input('Введите число, от 1 до 2: '))
if Command_Panel == 1:
    Number = float(input('Введите число: '))
    Result_Command_Panel_1 = Number + Number
    print(Result_Command_Panel_1)
elif Command_Panel == 2:
    Number = float(input('Введите число: '))
    Result_Command_Panel_2 = Number - Number
    print(Result_Command_Panel_2)
print()
print('End')
