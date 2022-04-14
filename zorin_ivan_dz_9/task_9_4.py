class Car:
    is_police = False

    def __init__(self, color, name):
        self.color = color
        self.name = name
        self.speed = 0

    def go(self, speed=30):
        self.speed = speed
        print(f"Автомобиль {self.name} тронулся, скорость {self.speed} км/ч.")

    def stop(self):
        self.speed = 0
        print(f"Автомобиль {self.name} остановился.")

    def turn(self, direction):
        if direction == "лево" or direction == "право":
            print(f"Автомобиль {self.name} повернул на {direction}.")
        else:
            print(f"Автомобиль запрограммирован поворачивать на лево или на право.")

    def show_speed(self):
        print(f"Скорость автомобиля {self.speed} км/ч.")


class TownCar(Car):

    def show_speed(self):
        if self.speed >= 61:
            print(f"Ваша скорость {self.speed}, превышает разрешоно допустимую скорость для TownCar в 60 км/ч.")
        else:
            print(f"Скорость автомобиля {self.speed} км/ч.")


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed >= 41:
            print(f"Ваша скорость {self.speed}, превышает разрешоно допустимую скорость для WorkCar в 40 км/ч.")
        else:
            print(f"Скорость автомобиля {self.speed} км/ч.")


class PoliceCar(Car):
    is_police = True


auto_1 = WorkCar("белый", "Газ")
auto_1.go(39)
auto_1.show_speed()
auto_2 = PoliceCar("серебристая", "Лада")
auto_2.go(50)
auto_3 = SportCar("черный", "Субару")
auto_3.go(78)
auto_3.turn("лево")
auto_4 = TownCar("красный", "Ауди")
auto_4.go(58)
auto_4.turn("право")
auto_4.stop()
auto_4.show_speed()
