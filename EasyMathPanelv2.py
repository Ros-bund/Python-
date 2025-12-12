import time
print('=====EasyMathPanel====')
print()
print('1-- Сложение')
print('2-- Вычитание')
print('3-- Умножение')

Command_Panel = int(input('Введите число, от 1 до 3: '))
Number = float(input('Введите число: '))
if Command_Panel == 1:
    Result_Command_Panel_1 = Number + Number
    print(Result_Command_Panel_1)
elif Command_Panel == 2:
    Result_Command_Panel_2 = Number - Number
    print(Result_Command_Panel_2)
elif Command_Panel == 3:
    Result_Command_Panel_3 = Number * Number
    print(Result_Command_Panel_3)
print()
print('End')
