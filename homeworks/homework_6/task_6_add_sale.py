from sys import argv

if __name__ == '__main__':
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.write(argv[1] + '\n')
