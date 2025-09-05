from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def query(self, sql):
        pass


class MySQLDatabase(Database):
    def connect(self):
        return "MySQL connection established"

    def query(self, sql):
        return f"Executing MySQL query: {sql}"


class PostgreSQLDatabase(Database):
    def connect(self):
        return "PostgreSQL connection established"

    def query(self, sql):
        return f"Executing PostgreSQL query: {sql}"


class Application:
    def __init__(self, database: Database):  # Зависимость от абстракции
        self.database = database

    def get_data(self):
        self.database.connect()
        return self.database.query("SELECT * FROM users")


# Теперь можно легко менять реализацию базы данных
mysql_app = Application(MySQLDatabase())
postgres_app = Application(PostgreSQLDatabase())