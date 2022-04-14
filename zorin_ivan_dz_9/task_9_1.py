from time import sleep


class TrafficLight:

    def __init__(self):
        self.__color = None

    def running(self):
        while True:
            self.__color = "Красный"
            print("\033[41m( )\033[0m", f"{self.__color}")
            sleep(7)
            self.__color = "Желтый"
            print("\033[43m( )\033[0m", f"{self.__color}")
            sleep(2)
            self.__color = "Зеленый"
            print("\033[42m( )\033[0m", f"{self.__color}")
            sleep(7)
            self.__color = "Желтый"
            print("\033[43m( )\033[0m", f"{self.__color}")
            sleep(2)


trafficlight = TrafficLight()
trafficlight.running()
