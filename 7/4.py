class Car:
    def __init__(self, speed, color, name, is_police) -> None:
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула на {direction}")

    def show_speed(self):
        print(f"Текущая скорость: {self.speed}")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police) -> None:
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Текущая скорость: {self.speed}")
        if self.speed > 60:
            print("Превышение скорости!!!")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police) -> None:
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police) -> None:
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Текущая скорость: {self.speed}")
        if self.speed > 40:
            print("Превышение скорости!!!")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police) -> None:
        super().__init__(speed, color, name, is_police)


town = TownCar(66, "green", "town", False)
sport = SportCar(30, "red", "sport", False)
work = WorkCar(50, "yellow", "work", False)
police = PoliceCar(100, "blue", "police", True)

town.speed = 70
print(town.speed)
sport.color = "reddddd"
print(sport.color)
work.name = "workCar"
print(work.name)
police.color = "blue-blue"
print(police.color)


town.show_speed()
sport.show_speed()
work.show_speed()
police.show_speed()
