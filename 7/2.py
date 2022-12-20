class Road:
    def __init__(self, length, width):
        self._width = width
        self._length = length

    def calc(self):
        result = self._length * self._width * 25 * 5 / 1000
        print(f"{result} т")


obj = Road(20, 5000)
obj.calc()
