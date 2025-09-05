class MySQLDatabase:
    def connect(self):
        return "MySQL connection established"

    def query(self, sql):
        return f"Executing MySQL query: {sql}"


class Application:
    def __init__(self):
        self.database = MySQLDatabase()  # Прямая зависимость от конкретного класса

    def get_data(self):
        self.database.connect()
        return self.database.query("SELECT * FROM users")

# Проблема: сложно изменить базу данных на другую