import re


def email_parse(email_address):
    result = re.fullmatch(r'^(\w+)@(\w+\.\w+)$', email_address)
    if result is None:
        raise ValueError("Невалидный email!")
    return {
        'username': result.groups()[0],
        'domain': result.groups()[1]
    }


if __name__ == '__main__':
    email = "someone@geekbrains.ru"
    print(email_parse(email))
