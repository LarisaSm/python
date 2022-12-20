import time


class TrafficLight:
    def __init__(self, color="red"):
        self.__color = color

    def running(self):
        self.__color = "red"
        print(self.__color)
        time.sleep(7)
        self.__color = "yellow"
        print(self.__color)
        time.sleep(2)
        self.__color = "green"
        print(self.__color)
        time.sleep(10)


obj = TrafficLight()
obj.running()
