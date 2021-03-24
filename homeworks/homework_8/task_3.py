def print_type(desc, arg):
    print(desc, ': ', type(arg))


def type_logger(func):
    def wrapper(*args, **kwargs):
        for item in args:
            print_type(item, item)
        for item in kwargs.items():
            print_type(item[0], item[1])
        result = func(*args, **kwargs)
        print('Тип возвращаемого значения функции: ', type(result))
        return result

    return wrapper


@type_logger
def calc_cube(x, y, test=23.2, test2=12):
    return x ** 3


if __name__ == "__main__":
    calc_cube(5, 3.45, test=2.5, test2=2)
