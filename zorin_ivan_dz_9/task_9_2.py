class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate(self, wigth=25, thickness=5):
        return f'Масса асфальта: {(self._length * self._width * wigth * thickness) / 1000} т'


road_1 = Road(5000, 20)
print(road_1.calculate())
