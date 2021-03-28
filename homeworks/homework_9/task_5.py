class Stationery:
    def __init__(self, title):
        self._title = title

    def draw(self):
        print('Запуск отрисовки. Канцелярская принадлежность:', self._title)


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки. Ручка:', self._title)


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки. Карандаш:', self._title)


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки. Маркер:', self._title)


if __name__ == '__main__':
    stationery = Stationery('Pilot')
    stationery.draw()
    pen = Pen('Pilot')
    pen.draw()
    pencil = Pencil('Castell')
    pencil.draw()
    handle = Handle('Touch')
    handle.draw()
