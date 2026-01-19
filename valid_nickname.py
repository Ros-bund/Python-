nickname = input()

if nickname.startswith('@'):
    # Длина никнейма включая @ должна быть от 5 до 15
    if 5 <= len(nickname) <= 15:
        # Проверяем символы после @ (их должно быть от 4 до 14)
        is_valid = True
        for char in nickname[1:]:
            if not ('a' <= char <= 'z' or '0' <= char <= '9'):
                is_valid = False
                break
        
        if is_valid:
            print('Correct')
        else:
            print('Incorrect')
    else:
        print('Incorrect')
else:
    print('Incorrect')