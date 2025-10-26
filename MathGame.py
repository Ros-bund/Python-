import operator
import random
def errorHandle(problem_answer):
    switch = False
    validated_guess = 0.0
    while switch == False:
        try:
            validated_guess = float(input('Пожалуста напишите коректное чилсо : '))
            if type(validated_guess) is float:
                switch = True
                break
        except ValueError:
            pass
    return validated_guess
def random_problem():
    operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    }

    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    operation = random.choice(list(operators.keys()))
    answer = float(round(operators.get(operation)(num_1, num_2),3))
    print(f'Что это {num_1} {operation} {num_2}')
    return answer
def ask_question():
    answer = random_problem()
    try:
        guess = float(input('Введите ваше число : '))
    except ValueError:
        guess = errorHandle(answer)
    return guess == answer
def game():
    score = 0
    while True:
        if ask_question()  == True:
            score += 1
            print('Правильно !')
        else:
            print('Неправильно')
            break
    print(f'======== Конец игры ========\nВашы очки {score}\nЕще разок?')

game()