def val_checker(check_valid):
    def _val_checker(func):
        def wrapper(*args):
            if not check_valid(args[0]):
                raise ValueError(f'wrong val {args[0]}')
            result = func(*args)
            return result

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


if __name__ == "__main__":
    print(calc_cube(2))
