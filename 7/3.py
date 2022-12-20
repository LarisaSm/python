class Worker:
    def __init__(self, name, surname, position, wage, bonus) -> None:
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus) -> None:
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f"Полное имя: {self.name} {self.surname}")

    def get_total_income(self):
        result = self._income["wage"] + self._income["bonus"]
        print(f"Доход с учетом премии: {result}")


obj = Position("Имя", "Фамилия", "Позиция", 10000, 3000)

obj.get_full_name()
obj.get_total_income()
