class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class UserRepository:
    def save(self, user):
        print(f"Saving {user.name} to database...")


class EmailService:
    def send_email(self, user, message):
        print(f"Sending email to {user.email}: {message}")


class ReportGenerator:
    def generate_user_report(self, user):
        print(f"Generating report for {user.name}")


class UserManager:
    def __init__(self, user):
        self.user = user
        self.repository = UserRepository()
        self.email_service = EmailService()
        self.report_generator = ReportGenerator()

    def change_user_name(self, new_name):
        self.user.name = new_name
        self.repository.save(self.user)
        self.email_service.send_email(self.user, f"Name changed to {new_name}")