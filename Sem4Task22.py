'''
Задача 22: Даны два неупорядоченных набора целых чисел (может быть,
с повторениями). Выдать без повторений в порядке возрастания все те числа,
которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества.
m - кол-во элементов второго множества. Затем пользователь вводит сами
элементы множеств.
'''
from random import randint
from timeit import timeit
len_1 = int(input('Введите длину первого множества: '))
len_2 = int(input('Введите длину второго множества: '))
def range_list(n):
    numbers = []
    for i in range(n):
        numbers.append(randint(0, 10))
    return numbers
numbers_1 = range_list(len_1)
print(numbers_1)
numbers_2 = range_list(len_2)
print(numbers_2)
numbers_1_set = set(numbers_1)
print(numbers_1_set)
numbers_2_set = set(numbers_2)
print(numbers_2_set)
new_numbers = numbers_1_set.intersection(numbers_2_set)
print(new_numbers)
print(timeit('range_list(len_1)', globals=globals(), number=1000))
print(timeit('range_list(len_2)', globals=globals(), number=1000))