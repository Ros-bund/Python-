import time
from math import *
print('=====MathPanel=====')
print()

print('1--возведение числа')
time.sleep(0.3)
print('2--округление числа до ближайшего наибольшего целого')
time.sleep(0.3)
print('3--округление числа до ближайшего наименьшего целого')
time.sleep(0.3)
print('4--факториал числа')
time.sleep(0.3)
print('5--квадратный корень')
time.sleep(0.3)
print()

X = int(input('Pls input number 1-5: '))
print()
Num = float(input('Pls input Your number: '))
print()

if X < 1 or X > 5:
    print('Error, input 1-5')
elif X == 1:
    Power1 = int(input('Pls input power pow: '))
    P1 = pow(Num, Power1)
    time.sleep(1)
    print('99%...')
    time.sleep(1)
    print(P1)
elif X == 2:
    C1 = ceil(Num)
    time.sleep(1)
    print('67%...')
    time.sleep(1)
    print(C1)
elif X == 3:
    F1 = floor(Num)
    time.sleep(1)
    print('69%...')
    time.sleep(1)
    print(F1)
elif X == 4:
    Fact1 = factorial(Num)
    time.sleep(1)
    print('42%...')
    time.sleep(1)
    print(Fact1)
elif X == 5:
    if Num >= 9:
        S1 = sqrt(Num)
        time.sleep(1)
        print('1%...')
        time.sleep(2)
        print('67%...')
        time.sleep(3)
        print('99%...')
        time.sleep(4)
        print(S1)
    else:
        print("It's number don't have sqrt")
    
print()
print('=====End====')
print('goodbye!')
print('Pls rate it mathpanel')
Z = int(input('1-5: '))
if Z == 1:
    print('*')
elif Z == 2:
    print('**')
elif Z == 3:
    print('***')
elif Z == 4:
    print('****')
elif Z == 5:
    print('*****')


Want_Play_Next_Panel = input('Want you next play "EasyMathPanel?"(Y/N): ')
if Want_Play_Next_Panel == 'Y':
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

if Want_Play_Next_Panel == 'N':
    print('Ok, goodbye')


if Want_Play_Next_Panel != 'Y' and Want_Play_Next_Panel != 'N':
    print('Pls enter Y or N')