'''
Задача 30:  Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
'''
first_elem = int(input('Введите первый элемент арифметической прогрессии: '))
step = int(input('Введите шаг арифметической прогрессии: '))
count_elem = int(input('Введите количество элементов: '))
for i in range(count_elem):
    print(first_elem + i * step)