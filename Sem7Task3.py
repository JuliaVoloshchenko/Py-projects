'''
Задание 3. Реализовать базовый класс Worker (работник), в котором определить
публичные атрибуты name, surname, position (должность),и защищенный атрибут
income (доход). Последний атрибут должен ссылаться на словарь, содержащий
элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать публичные методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры
класса Position, передать данные, проверить значения атрибутов,
вызвать методы экземпляров).
Попытайтесь добить вывода информации о сотруднике также через перегрузку str
str(self) - вызывается функциями str, print и format. Возвращает строковое
представление объекта.
'''
class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

    def __str__(self):
        return 'Информация о сотрудниках'

obj = Position('Сергей', 'Иванов', 'менеджер', 80, 30)
print(obj)
obj_1 = Position('Андрей', 'Кузнецов', 'продавец', 50, 20)
print(obj.name, obj.surname, obj.position, obj._income)
print(obj.get_full_name(), obj.get_total_income())
print(obj_1.name, obj_1.surname, obj_1.position, obj_1._income)
print(obj_1.get_full_name(), obj_1.get_total_income())