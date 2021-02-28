FORMAT = '{:02d}'
message_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

idx = 0
size = len(message_list)
while idx < size:
    temp = message_list[idx]
    symbol = ''
    for idy in range(len(temp)):
        if temp[idy:].isdigit():
            symbol = temp[:idy]
            temp = temp[idy:]
            message_list[idx] = symbol + FORMAT.format(int(temp))
            # Вставка ковычек перед числом
            message_list.insert(idx, '".')
            # Сдвиг на 2 элемента
            idx += 2
            # Вставка ковычек после числа
            message_list.insert(idx, '."')
            break
    idx += 1
    size = len(message_list)

print(' '.join(message_list).replace('". ', '"').replace(' ."', '"'))
