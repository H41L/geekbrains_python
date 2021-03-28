class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_weight(self, weight_for_one_square_meter, thickness):
        return self._length * self._width * weight_for_one_square_meter * thickness


if __name__ == '__main__':
    road = Road(20, 5000)
    weight_ton = road.calc_weight(25, 5) / 1000
    print('Масса асфальта, для покрытия всей дороги:', weight_ton, 'т.')
