'''
Задание 7. Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
'''
n = int(input('Введите число N (до 20): '))
lst_obj = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
res = 0
def get_sum(lst_obj):
    if len(lst_obj) == 1:
        return lst_obj[0]
    return lst_obj[0] + get_sum(lst_obj[1:n])
print(get_sum(lst_obj))
m = n * (n + 1) // 2
print(m)