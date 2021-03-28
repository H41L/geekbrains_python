class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

    def __str__(self):
        return f'Имя: {self.name}, фамилия: {self.surname}, должность: {self.position}, доход: {self._income}'

    def get_wage(self):
        return self._income.get('wage')

    def get_bonus(self):
        return self._income.get('bonus')


class Position(Worker):
    def get_full_name(self):
        return f'{self.surname} {self.name}'

    def get_total_income(self):
        return self.get_wage() + self.get_bonus()


if __name__ == '__main__':
    pos = Position('Петр', 'Васильев', 'инженер-программист', {'wage': 100000, 'bonus': 50000})
    print(pos)
    print('Полное имя сотрудника:', pos.get_full_name())
    print('Доход с учетом премии:', pos.get_total_income())
