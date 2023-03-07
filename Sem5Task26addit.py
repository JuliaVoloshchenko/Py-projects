'''
Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
и возводит число А в целую степень B с помощью рекурсии.
'''
a = int(input('Введите число А: '))
b = int(input('Введите число В: '))
def rec_pow(a, b):
    if b <= 1:
        return a
    return a * rec_pow(a, b - 1)
res = rec_pow(a, b)
print(res)