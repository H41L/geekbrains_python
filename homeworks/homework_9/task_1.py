import time


class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        while True:
            if self.__color == 'red':
                print('Горит красный')
                time.sleep(7)
                self.__color = 'yellow'
            if self.__color == 'yellow':
                print('Горит желтый')
                time.sleep(2)
                self.__color = 'green'
            if self.__color == 'green':
                print('Горит зеленый')
                time.sleep(14)
                self.__color = 'red'


if __name__ == '__main__':
    traffic = TrafficLight('green')
    traffic.running()
