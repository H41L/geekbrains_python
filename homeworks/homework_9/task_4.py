class Car:
    def __init__(self, speed, color, name, is_police=False):
        self._speed = speed
        self._color = color
        self._name = name
        self._is_police = is_police

    def __str__(self):
        return f'Автомобиль: {self._name}, скорость: {self._speed}, цвет: {self._color}, полицейский: {self._is_police}'

    def go(self):
        print('Автомобиль', self._name, 'поехал')

    def stop(self):
        print('Автомобиль', self._name, 'остановился')

    def turn(self, direction):
        print('Автомобиль', self._name, 'повернул', direction)

    def show_speed(self):
        print('Текущая скорость автомобиля', self._name, self._speed)


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self._speed > 60:
            print('Скорость превышена на', self._speed - 60)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self._speed > 40:
            print('Скорость превышена на', self._speed - 40)


class PoliceCar(Car):
    pass


if __name__ == '__main__':
    town_car = TownCar(70, 'black', 'toyota')
    print(town_car)
    town_car.go()
    town_car.stop()
    town_car.turn('налево')
    town_car.show_speed()
    sport_car = SportCar(140, 'yellow', 'ferrari')
    print(sport_car)
    sport_car.go()
    sport_car.stop()
    sport_car.turn('направо')
    sport_car.show_speed()
    work_car = WorkCar(45, 'white', 'GAZ')
    print(work_car)
    work_car.go()
    work_car.stop()
    work_car.turn('направо')
    work_car.show_speed()
    police_car = PoliceCar(55, 'white', 'VAZ', True)
    print(police_car)
    police_car.go()
    police_car.stop()
    police_car.turn('направо')
    police_car.show_speed()
