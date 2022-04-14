class Worker:

    def __init__(self, name, surname, position, wage=None, bonus=None):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return f"{sum(self.income.values())}"


security_guard = Position("Иван", "Иванов", "Delta", 25000, 10000)
print(security_guard.get_full_name())
print(security_guard.position)
print(security_guard.get_total_income())
