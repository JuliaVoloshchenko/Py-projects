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
first_list = ['разработка', 'сокет', 'декоратор']
second_list = []


def encode_to_unicode_escape(my_list):
    for i in range(len(my_list)):
        s = my_list[i].encode('unicode_escape').decode()
        second_list.append(s)
    return second_list


def type_obsession(new_list):
    for i in range(len(new_list)):
        print(new_list[i])
        print(type(new_list[i]))
    return new_list


print(first_list)
second_list = encode_to_unicode_escape(first_list)
print(second_list)
type_obsession(first_list)
type_obsession(second_list)
