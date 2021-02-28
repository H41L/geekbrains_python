price_parsed = '{:d} руб {:02d} коп'
prices_list = [57.8, 46.51, 97, 2, 0.43, 99.99, 111.2, 23, 35.3, 83.98, 11.23, 152.3]
result = []

print('Задание A:')
for price in prices_list:
    temp = str(float(price)).split('.')
    result.append((price_parsed.format(int(temp[0]), int(temp[1]))))
print(', '.join(result))

print('Задание B:')
result = []
id_before_sort = id(prices_list)
prices_list.sort()
id_after_sort = id(prices_list)
for price in prices_list:
    temp = str(float(price)).split('.')
    result.append((price_parsed.format(int(temp[0]), int(temp[1]))))
print(', '.join(result))
print('Идентификатор объекта после сортировки не изменился:', id_before_sort == id_after_sort)

print('Задание C:')
result = []
prices_list_new = sorted(prices_list, reverse=True)
for price in prices_list_new:
    temp = str(float(price)).split('.')
    result.append((price_parsed.format(int(temp[0]), int(temp[1]))))
print(', '.join(result))
print('Идентификаторы объектов разные:', id(prices_list_new) != id_after_sort)

print('Задание D:')
result = []
max_prices = sorted(prices_list_new[:5])
for price in max_prices:
    temp = str(float(price)).split('.')
    result.append((price_parsed.format(int(temp[0]), int(temp[1]))))
print(', '.join(result))

