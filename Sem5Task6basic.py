'''
Задание 6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
'''
from random import randint

n = randint(0, 100)


def random_num(n, i=0):
    a = int(input('Введите число: '))
    if a == n:
        print('Вы отгадали загаданное число!')
        return
    elif i == 10:
        print(f'Вы проиграли. Загаданное число: {n}')
        return
    elif a < n:
        print('загаданное число больше')
    else:
        print('загаданное число меньше')
    random_num(n, i=+1)
    return
random_num(n, i=0)