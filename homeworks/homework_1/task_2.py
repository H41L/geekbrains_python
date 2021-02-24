odd_cubes_list = []
sum_result = 0

# Заполнение списка кубами нечетных чисел от 1 до 1000
for idx in range(1, 1000 + 1):
    if idx % 2 != 0:
        odd_cubes_list.append(idx ** 3)

# Вычисление суммы чисел, сумма цифр которых делится нацело на 7
for idx in range(len(odd_cubes_list)):
    temp = odd_cubes_list[idx]
    num_sum = 0
    # Вычисление суммы цифр
    while temp != 0:
        num_sum += temp % 10
        temp //= 10
    # Проверка деления суммы цифр нацело на 7
    if num_sum % 7 == 0:
        # Вычисление суммы чисел
        sum_result += odd_cubes_list[idx]
print("Сумма чисел =", sum_result)

# Добавление к каждому элемента списка 17
for idx in range(len(odd_cubes_list)):
    odd_cubes_list[idx] += 17

# Вычисление суммы чисел, сумма цифр которых делится нацело на 7 для списка с новыми значениями
sum_result = 0
for idx in range(len(odd_cubes_list)):
    temp = odd_cubes_list[idx]
    num_sum = 0
    # Вычисление суммы цифр
    while temp != 0:
        num_sum += temp % 10
        temp //= 10
    # Проверка деления суммы цифр нацело на 7
    if num_sum % 7 == 0:
        # Вычисление суммы чисел
        sum_result += odd_cubes_list[idx]
print("Сумма чисел =", sum_result)
