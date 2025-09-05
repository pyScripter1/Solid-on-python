"""
Принцип единственной ответственности требует от нас не добавлять дополнительные обязанности к классу,
чтобы нам не приходилось менять класс, когда нам нужно изменить функционал сохранения справочника в базу данных или в файл.
Мы можем передать экземпляр класса TelephoneDirectory экземплярам этих классов и записать любые дополнительные функции в них.

Так мы гарантируем, что у класса TelephoneDirectory есть лишь одна причина для изменения –
это изменения в его основной «ответственности».
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

# создаем новые классы со своими методами
class persist_to_database:
  #functionality of the class
  def __init__(self, object_to_persist):
    pass

class save_to_file:
  #functionality of the class
  def __init__(self, object_to_save):
    pass


myTelephoneDirectory = TelephoneDirectory()
myTelephoneDirectory.add_entry("Ravi", 123456)
myTelephoneDirectory.add_entry("Vikas", 678452)
print(myTelephoneDirectory)

myTelephoneDirectory.delete_entry("Ravi")
myTelephoneDirectory.add_entry("Ravi", 123456)
myTelephoneDirectory.update_entry("Vikas", 776589)
print(myTelephoneDirectory.lookup_number("Vikas"))
print(myTelephoneDirectory)