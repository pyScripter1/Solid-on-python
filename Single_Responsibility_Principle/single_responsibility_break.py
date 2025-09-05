"""
А теперь скажем, что в проекте есть еще два требования – Сохранить содержимое справочника в базе данных
 и перенести содержимое справочника в файл.

Теперь добавим еще два метода в класс TelephoneDirectory, как показано ниже:
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

    def save_to_file(self, file_name, location):
        # code to save the contents of telephonedirectory dictionary to the file
        pass

    def persist_to_database(self, database_details):
        # code to persist the contents of telephonedirectory dictionary to database
        pass

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

"""
Так вот, именно сейчас мы нарушили принцип единственной ответственности.
Добавив функции сохранения в базу данных и сохранения в файл, мы дали классу дополнительные обязанности,
которые не входят в его основную зону ответственности. Теперь в классе есть дополнительные функции,
которые могут привести к его изменению. В будущем, если появятся какие-то требования, связанные с сохранением данных,
это может привести к изменениям в классе TelephoneDirectory. Получается,
что класс TelephoneDirectory подвержен изменениям по причинам, которые не являются его основной ответственностью.
"""