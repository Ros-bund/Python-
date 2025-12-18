def English():
    Test_Eng = 'This a test'
    Test_Ru = 'Это тест'
    return Test_Eng, Test_Ru
def Test():
    ru, eng = English()
    print(eng)
    print(ru)

Test()