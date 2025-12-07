import time
from math import *
print('=====MathPanel=====')
print()

print('1--возведение числа')
print('2--округление числа до ближайшего наибольшего целого')
print('3--округление числа до ближайшего наименьшего целого')
print('4--факториал числа')
print()

X = int(input('Pls input number 1-4: '))
print()
Num = float(input('Pls input Your number: '))
print()

if X < 1 and X > 4:
    print('Error, input 1-4')
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
print()
print('=====End====')
print('goodbye!')