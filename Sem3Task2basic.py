'''
2. Реализовать структуру «Рейтинг», представляющую собой не
возрастающий набор натуральных чисел
(каждый элемент ряда меньше или равен предыдущему).
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
'''
my_list = [7, 5, 3, 3, 2]
print(my_list)
new_elem = int(input('Введите новый элемент рейтинга: '))
if new_elem <= my_list[4]:
    my_list. append(new_elem)
    print(my_list)
elif new_elem >= my_list[0]:
    my_list. insert(0, new_elem)
    print(my_list)
elif new_elem < 7 and new_elem > 2:
    my_list. append(new_elem)
    my_list. sort(reverse=True)
    print(my_list)