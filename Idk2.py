num = input()
LenNum = len(num)
if int(num) > 100:
    print('Pls input low tier number')
else:
    for i in range(1, LenNum):
        if i == (i % 2 == 0):
            continue
print(LenNum)
        
