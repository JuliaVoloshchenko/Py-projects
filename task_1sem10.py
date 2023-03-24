"""
Задание 1.

Каждое из слов «разработка», «сокет», «декоратор» представить
в буквенном формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать
в набор кодовых точек Unicode (НО НЕ В БАЙТЫ!!!)
и также проверить тип и содержимое переменных.

*Попытайтесь получить кодовые точки без онлайн-конвертера!
без хардкода!

Подсказки:
--- 'разработка' - буквенный формат
--- '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430' - набор кодовых точек
--- используйте списки и циклы, не дублируйте функции
"""
First_list = ['разработка', 'сокет', 'декоратор']
Second_list = []


def encode_to_unicode_escape(my_list):
    for i in range(len(my_list)):
        s = my_list[i].encode('unicode_escape').decode()
        Second_list.append(s)
    return Second_list


def type_obsession(New_list):
    for i in range(len(New_list)):
        print(New_list[i])
        print(type(New_list[i]))
    return New_list


print(First_list)
Second_list = encode_to_unicode_escape(First_list)
print(Second_list)
type_obsession(First_list)
type_obsession(Second_list)
