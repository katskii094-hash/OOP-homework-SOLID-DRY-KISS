# неправильно (если что я выбрал принцип S)
class Report:
    def __init__(self, data):
        self.data = data

    def generate(self):                
        return f"Отчёт: {self.data}"

    def save_to_file(self, path):      
        with open(path, "w", encoding="utf-8") as f:
            f.write(self.generate())

    def send_by_email(self, email):    
        print(f"Отправка отчёта на {email}")

# правильно 
class Report:
    def __init__(self, data):
        self.data = data

    def generate(self) -> str:
        return f"Отчёт: {self.data}"


class FileSaver:
    @staticmethod
    def save(text: str, path: str):
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)


class EmailSender:
    @staticmethod
    def send(text: str, email: str):
        print(f"Отправка на {email}: {text}")



report = Report([1, 2, 3])
text = report.generate()

FileSaver.save(text, "report.txt")
EmailSender.send(text, "user@example.com")