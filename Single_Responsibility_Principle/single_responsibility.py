"""
Давайте в качестве примера возьмем приложение телефонного справочника.
Мы будем делать телефонный справочник, в котором будет класс TelephoneDirectory.
Он будет «нести ответственность» за ведение записей справочника,
то есть телефонных номеров и названий организаций, которым принадлежат номера.
Ожидается, что класс будет выполнять следующие операции:
добавлять новую запись (Name и Telephone Number), удалять существующую запись,
изменять номер телефона, присвоенный сущности Name, и предоставлять поиск,
который будет возвращать номер, присвоенный сущности Name.
"""

class TelephoneDirectory:
    def __init__(self):
        self.telephone_directory = {}

    def add_entry(self, name, number):
        self.telephone_directory[name] = number

    def delete_entry(self, name):
        self.telephone_directory.pop(name)

    def update_entry(self, name, new_number):
        self.telephone_directory[name] = new_number

    def lookup_number(self, name):
        return self.telephone_directory[name]

    def __str__(self):
        for name, number in self.telephone_directory.items():
            print(f"{name} - {number}")


myTelephoneDirectory = TelephoneDirectory()
myTelephoneDirectory.add_entry("Ravi", 123456)
myTelephoneDirectory.add_entry("Vikas", 678452)
print(myTelephoneDirectory)

myTelephoneDirectory.delete_entry("Ravi")
myTelephoneDirectory.add_entry("Ravi", 123456)
myTelephoneDirectory.update_entry("Vikas", 776589)
print(myTelephoneDirectory.lookup_number("Vikas"))
print(myTelephoneDirectory)

# Сейчас наш класс TelephoneDirectory выглядит хорошо, в нем точно реализованы ожидаемые функции