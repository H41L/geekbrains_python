message = 'Привет, {}!'
employees_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
                  'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for employee in employees_list:
    employee_name = employee.rsplit(' ', 1)[1]
    print(message.format(employee_name.title()))
