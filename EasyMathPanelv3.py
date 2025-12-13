import time
print('=====EasyMathPanel====')
print()
print('1-- Сложение')
print('2-- Вычитание')
print('3-- Умножение')

Command_Panel = int(input('Введите число, от 1 до 3: '))
Number_1 = float(input('Введите число: '))
Vibor = (input('Хотите ли вы добавить второе число?(Y, N): '))
if Vibor == 'N':
    if Command_Panel == 1:
        Result_Command_Panel_1 = Number_1 + Number_1
        print(Result_Command_Panel_1)
    elif Command_Panel == 2:
        Result_Command_Panel_2 = Number_1 - Number_1
        print(Result_Command_Panel_2)
    elif Command_Panel == 3:
        Result_Command_Panel_3 = Number_1 * Number_1
        print(Result_Command_Panel_3)


if Vibor == 'Y':
    Number_2 = float(input('Введите второе число: '))
    if Command_Panel == 1:
        Result_Command_Panel_1 = Number_1 + Number_2
        print(Result_Command_Panel_1)
    elif Command_Panel == 2:
        Result_Command_Panel_2 = Number_1 - Number_2
        print(Result_Command_Panel_2)
    elif Command_Panel == 3:
        Result_Command_Panel_3 = Number_1 * Number_2
        print(Result_Command_Panel_3)


if Vibor != 'Y' and Vibor != 'N':
    print('Y or N')
print()
print('End')
