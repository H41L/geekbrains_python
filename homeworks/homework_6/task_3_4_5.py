from sys import argv

# 1 аргумент: имя файла с пользователями
# 2 аргумент: имя файла с хобби
# 3 аргумент: имя файла с результами
if __name__ == '__main__':
    with open(argv[1], 'r', encoding='utf-8') as f:
        with open(argv[2], 'r', encoding='utf-8') as f_2:
            users = (line.strip() for line in f)
            hobbies = (line.strip() for line in f_2)
            users_hobbies = (users_hobbies[::-1] for users_hobbies in zip(hobbies, users))
            with open(argv[3], 'w', encoding='utf-8') as f:
                for user in users_hobbies:
                    f.write(f'{user[0]}: {user[1]}\n')
                users_without_hobbies = (_users for _users in users)
                for user in users_without_hobbies:
                    f.write(f'{user}: {None}\n')
