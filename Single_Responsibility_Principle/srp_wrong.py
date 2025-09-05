# нарушение SRP

class UserManager:
    def __init__(self, user):
        self.user = user

    def change_user_name(self, new_name):
        # Изменение имени пользователя
        self.user.name = new_name

    def save_user_to_database(self):
        # Сохранение в базу данных
        print(f"Saving {self.user.name} to database...")

    def send_email_notification(self, message):
        # Отправка email
        print(f"Sending email to {self.user.email}: {message}")

    def generate_user_report(self):
        # Генерация отчета
        print(f"Generating report for {self.user.name}")

# Проблема: класс делает слишком много разных вещей