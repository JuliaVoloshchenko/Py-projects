'''
Задание 5. Пользователь вводит строку из нескольких слов,
разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если слово длинное,
выводить только первые 10 букв в слове.
'''
my_str = input('Введите насколько слов через пробел: ').split()
for i in my_str:
    print(i[:10])
